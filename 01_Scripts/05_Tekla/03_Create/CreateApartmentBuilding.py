# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import clr

clr.AddReference("Tekla.Structures.Model")
clr.AddReference("System.Windows.Forms")

from System import Array, Type
from Tekla.Structures.Geometry3d import Point, AABB
from Tekla.Structures.Model import Model, Beam, ContourPlate, ContourPoint, PolyBeam, Position
from Tekla.Structures.Model.UI import Picker, ViewHandler
from System.Windows.Forms import MessageBox, MessageBoxButtons, MessageBoxIcon, DialogResult

# The host injects the connected model as __teklamodel__
try:
    model = __teklamodel__
except NameError:
    model = Model()

# ---------------------------------------------------------------------------
# Residential block: NF storeys, 2 dwellings per storey and a central core
# with a dog-leg stair and a lift shaft opening onto the landing. Concrete,
# footprint W x D (mm). Run it as many times as needed:
#   Yes -> pick the insertion point (bottom-left corner, ground level)
#   No  -> placed GAP mm beyond everything already modelled (+X, Y = 0)
#
# Plan (local mm): dwelling A X 0-10000 | core X 10000-14000 | dwelling B
# X 14000-24000. Core: lift Y 0-2300, landing Y 2300-7000, stair Y 7000-11800.
#
# Verified (Tekla 2026, 2026-10-20): rectangular concrete profile "H*W"
# (first = height); Beam Depth FRONT = above its line, BEHIND = below (also
# on inclined lines); ContourPlate Depth FRONT = above the contour, BEHIND
# below; 3D view clipping = View.WorkArea + ViewDepthUp/Down; IFC class
# override = UDAs proIfcEntityOvrd / proIfcEntityPreDef (checked in the IFC4
# export: IfcWall, IfcSlab, IfcStairFlight instead of IfcBeam / IfcPlate).
# ⏳ Not run yet: Picker.PickPoint (throws when the user presses Esc).
#
# Changes are committed but NOT saved: save the model (Ctrl+S) to keep them.
# ---------------------------------------------------------------------------
NF = 7                  # storeys
H = 3000.0              # floor to floor, mm
TS = 250.0              # slab thickness, mm
W, D = 24000.0, 12000.0 # footprint, mm
GAP = 10000.0           # clear distance to the existing model (auto placement)
MATERIAL = "C30"
FIT_VIEW = True         # fit the visible views' work area to the whole model

CLASS_SLAB, CLASS_COLUMN, CLASS_WALL, CLASS_LIFT, CLASS_STAIR = "8", "2", "3", "4", "6"

# Core / stair geometry (local mm)
SX1, SX2 = 10200.0, 13800.0     # stair box X
SY1, SY2 = 7000.0, 11800.0      # stair box Y
FA = (10300.0, 11500.0)         # flight A (goes up along +Y)
FB = (12500.0, 13700.0)         # flight B (goes up along -Y)
NR = 9                          # risers per flight
RISE = H / (2 * NR)
GOING = 300.0
YM = SY1 + NR * GOING           # half landing starts here

PART_TYPES = Array[Type]([clr.GetClrType(Beam), clr.GetClrType(ContourPlate), clr.GetClrType(PolyBeam)])


def model_extents():
    """(min, max) global corners of every part, or None for an empty model."""
    mn, mx = [1e18] * 3, [-1e18] * 3
    e = model.GetModelObjectSelector().GetAllObjectsWithType(PART_TYPES)
    found = False
    while e.MoveNext():
        s = e.Current.GetSolid()
        a, b = s.MinimumPoint, s.MaximumPoint
        for i, (p, q) in enumerate(((a.X, b.X), (a.Y, b.Y), (a.Z, b.Z))):
            mn[i], mx[i] = min(mn[i], p), max(mx[i], q)
        found = True
    return (mn, mx) if found else None


if not model.GetConnectionStatus():
    raise Exception("Not connected to Tekla Structures.")

answer = MessageBox.Show(
    f"Crear un edificio de {NF} plantas ({W / 1000:.0f} x {D / 1000:.0f} m, 2 viviendas por planta,\n"
    f"escalera y ascensor) en el modelo '{model.GetInfo().ModelName}'.\n\n"
    f"  Sí  -> designar el punto de inserción (esquina inferior izquierda)\n"
    f"  No  -> colocarlo a {GAP / 1000:.0f} m de lo ya modelado (+X)\n\n"
    "Los cambios no se guardan: cierra sin guardar para deshacer.",
    "PyNET - Edificio de viviendas",
    MessageBoxButtons.YesNoCancel,
    MessageBoxIcon.Question,
)

origin = None
if answer == DialogResult.Yes:
    try:
        origin = Picker().PickPoint("Designa la esquina inferior izquierda del edificio")
    except Exception:
        origin = None
        print("Point picking cancelled: nothing was created.")
elif answer == DialogResult.No:
    ext = model_extents()
    origin = Point(0.0, 0.0, 0.0) if ext is None else Point(ext[1][0] + GAP, 0.0, 0.0)
else:
    print("Cancelled: nothing was created.")

created, failed = [0], []

if origin is not None:
    X0, Y0, Z0 = origin.X, origin.Y, origin.Z

    def P(x, y, z):
        return Point(X0 + x, Y0 + y, Z0 + z)

    def insert(obj, what):
        if obj.Insert():
            created[0] += 1
        else:
            failed.append(what)

    def ifc_class(obj, entity, predefined):
        # IFC class for the export (ISO 19650 / IFC): walls and slabs are modelled as
        # beams and plates, so without the override Tekla exports IfcBeam / IfcPlate
        obj.SetUserProperty("proIfcEntityOvrd", entity)
        obj.SetUserProperty("proIfcEntityPreDef", predefined)

    def plate(rect, z, thick, depth, name, cls, ifc):
        x1, y1, x2, y2 = rect
        p = ContourPlate()
        for x, y in ((x1, y1), (x2, y1), (x2, y2), (x1, y2)):
            p.AddContourPoint(ContourPoint(P(x, y, z), None))
        p.Profile.ProfileString = str(int(round(thick)))
        p.Material.MaterialString = MATERIAL
        p.Position.Depth = depth
        p.Name, p.Class = name, cls
        ifc_class(p, *ifc)
        insert(p, name)

    def wall(a, b, z, h, name="MURO", cls=CLASS_WALL, t=200):
        w = Beam(P(a[0], a[1], z), P(b[0], b[1], z))
        w.Profile.ProfileString = f"{int(h)}*{t}"
        w.Material.MaterialString = MATERIAL
        w.Position.Plane = Position.PlaneEnum.MIDDLE
        w.Position.Depth = Position.DepthEnum.FRONT        # stands on its line
        w.Name, w.Class = name, cls
        ifc_class(w, "IfcWall", "SHEAR")
        insert(w, name)

    def column(x, y, z, h):
        c = Beam(Beam.BeamTypeEnum.COLUMN)
        c.StartPoint, c.EndPoint = P(x, y, z), P(x, y, z + h)
        c.Profile.ProfileString = "400*400"
        c.Material.MaterialString = MATERIAL
        c.Position.Plane = Position.PlaneEnum.MIDDLE
        c.Position.Depth = Position.DepthEnum.MIDDLE
        c.Name, c.Class = "PILAR", CLASS_COLUMN
        insert(c, "PILAR")

    def waist(flight, start, end):
        xc = (flight[0] + flight[1]) / 2
        s = Beam(P(xc, start[0], start[1]), P(xc, end[0], end[1]))
        s.Profile.ProfileString = f"150*{int(flight[1] - flight[0])}"
        s.Material.MaterialString = MATERIAL
        s.Position.Plane = Position.PlaneEnum.MIDDLE
        s.Position.Depth = Position.DepthEnum.BEHIND       # under the steps
        s.Name, s.Class = "LOSA ESCALERA", CLASS_STAIR
        ifc_class(s, "IfcStairFlight", "STRAIGHT")
        insert(s, "LOSA ESCALERA")

    BELOW, ABOVE = Position.DepthEnum.BEHIND, Position.DepthEnum.FRONT
    hw = H - TS     # clear height between slabs

    for i in range(NF + 1):
        L = i * H
        # Slab with its top at level L; intermediate floors leave the stair and lift openings
        slab = ("IfcSlab", "ROOF" if i == NF else "FLOOR")
        if i == 0 or i == NF:
            plate((0, 0, W, D), L, TS, BELOW, "LOSA", CLASS_SLAB, slab)
        else:
            for r in ((0, 0, SX1, D), (SX2, 0, W, D), (SX1, 2300, SX2, SY1), (12400, 0, SX2, 2300)):
                plate(r, L, TS, BELOW, "LOSA", CLASS_SLAB, slab)
        if i == NF:
            break

        for x in (0, 5000, 19000, 24000):
            for y in (0, 6000, 12000):
                column(x, y, L, hw)

        # Core walls, 1 m door to each dwelling
        for x in (10000, 14000):
            wall((x, 0), (x, 3500), L, hw)
            wall((x, 4500), (x, D), L, hw)
        # Lift shaft, door to the landing
        wall((12400, 0), (12400, 2300), L, hw, "ASCENSOR", CLASS_LIFT)
        wall((10000, 100), (12400, 100), L, hw, "ASCENSOR", CLASS_LIFT)
        wall((10000, 2300), (10800, 2300), L, hw, "ASCENSOR", CLASS_LIFT)
        wall((11800, 2300), (12400, 2300), L, hw, "ASCENSOR", CLASS_LIFT)
        # Core facades
        wall((12400, 100), (14000, 100), L, hw)
        wall((10000, 11900), (14000, 11900), L, hw)

        # Stair L -> L + H (none from the top storey)
        if i < NF - 1:
            flight, landing = ("IfcStairFlight", "STRAIGHT"), ("IfcSlab", "LANDING")
            for k in range(NR):
                plate((FA[0], SY1 + k * GOING, FA[1], SY1 + (k + 1) * GOING), L + k * RISE, RISE, ABOVE, "ESCALERA", CLASS_STAIR, flight)
            plate((SX1, YM, SX2, SY2), L + H / 2, 200, BELOW, "MESETA", CLASS_STAIR, landing)
            for k in range(NR):
                plate((FB[0], YM - (k + 1) * GOING, FB[1], YM - k * GOING), L + H / 2 + k * RISE, RISE, ABOVE, "ESCALERA", CLASS_STAIR, flight)
            waist(FA, (SY1, L), (YM, L + H / 2))
            waist(FB, (YM, L + H / 2), (SY1, L + H))

    model.CommitChanges("PyNET: create apartment building")   # once, at the end

    if FIT_VIEW:
        ext = model_extents()
        m = 2000.0
        views = ViewHandler.GetVisibleViews()
        while views.MoveNext():
            v = views.Current
            v.WorkArea = AABB(Point(ext[0][0] - m, ext[0][1] - m, ext[0][2] - m),
                              Point(ext[1][0] + m, ext[1][1] + m, ext[1][2] + m))
            v.ViewDepthUp = ext[1][2] + m
            v.ViewDepthDown = abs(ext[0][2]) + m
            v.Modify()
            ViewHandler.ZoomToBoundingBox(v, v.WorkArea)

    print(f"Created {created[0]} parts at ({X0:.0f}, {Y0:.0f}, {Z0:.0f}) mm.")
    if failed:
        print(f"Tekla rejected {len(failed)} parts: {sorted(set(failed))}")
    print("Save the model (Ctrl+S) to keep the changes.")

ia_Result = {
    "type": "TeklaCreateApartmentBuilding",
    "origin_mm": None if origin is None else [origin.X, origin.Y, origin.Z],
    "created": created[0],
    "failed": failed,
}
