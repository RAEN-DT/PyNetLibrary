# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import clr

clr.AddReference("Tekla.Structures.Model")
clr.AddReference("Tekla.Structures.Catalogs")
clr.AddReference("System.Windows.Forms")

from Tekla.Structures.Catalogs import CatalogHandler
from Tekla.Structures.Geometry3d import Point
from Tekla.Structures.Model import Model, Beam, Position
from System.Windows.Forms import MessageBox, MessageBoxButtons, MessageBoxIcon, DialogResult

# The host injects the connected model as __teklamodel__
try:
    model = __teklamodel__
except NameError:
    model = Model()

# ---------------------------------------------------------------------------
# Create a rectangular frame: one column at every grid intersection
# (GRID_X x GRID_Y, mm, global coordinates) from BASE_Z to TOP_Z and,
# optionally, top beams joining neighbouring columns in X and Y.
#
# Profiles and materials depend on the model's environment (a US model has
# W310X97 / A992, a European one HEB300 / S355J2): the catalog is enumerated
# once and the first candidate that exists is used - Insert() is never relied
# on to reject an unknown name. Asks for confirmation, checks the bool of
# every Insert(), and calls CommitChanges() once at the end.
#
# Placement (tekla.md "Coordinates and positions"): columns centred on their
# axis (Plane/Depth MIDDLE); beams hang below the top level line
# (Depth BEHIND), so their top flange is flush with TOP_Z.
#
# Verified (tekla.md): CatalogHandler profile/material enumeration, Beam()
# with StartPoint/EndPoint/Profile/Material/Name/Class, Insert() bool,
# CommitChanges() (run on Tekla 2026, 2026-10-16). ⏳ Still unconfirmed:
# Beam(Beam.BeamTypeEnum.COLUMN) constructor, the Depth semantics (confirm
# with GetSolid() Z extents).
#
# Changes are committed but NOT saved: save the model (Ctrl+S) to keep them,
# or close without saving to discard them.
# ---------------------------------------------------------------------------
GRID_X = [0.0, 6000.0, 12000.0]      # mm
GRID_Y = [0.0, 5000.0]               # mm
BASE_Z = 0.0                         # mm
TOP_Z = 3600.0                       # mm
CREATE_BEAMS = True

COLUMN_PROFILES = ["HEB300", "HEA300", "W310X97", "W12X65"]
BEAM_PROFILES = ["IPE400", "HEA400", "W410X60", "W16X40"]
MATERIALS = ["S355J2", "S355JR", "S275JR", "A992", "A572-50"]
COLUMN_CLASS = "2"                   # class = colour in the default representation
BEAM_CLASS = "3"


def pick(available, candidates, what):
    """First candidate that exists in this model's catalog."""
    for c in candidates:
        if c in available:
            return c
    raise Exception(f"None of the {what} {candidates} is in this model's catalog: edit the candidates.")


if not model.GetConnectionStatus():
    raise Exception("Not connected to Tekla Structures.")

# Catalog lookup - enumerate once, check many names
profiles, materials = set(), set()
catalog = CatalogHandler()
e = catalog.GetLibraryProfileItems()
while e.MoveNext():
    profiles.add(e.Current.ProfileName)
e = catalog.GetMaterialItems()
while e.MoveNext():
    materials.add(e.Current.MaterialName)

column_profile = pick(profiles, COLUMN_PROFILES, "column profiles")
beam_profile = pick(profiles, BEAM_PROFILES, "beam profiles") if CREATE_BEAMS else None
material = pick(materials, MATERIALS, "materials")

# What will be created
columns = [(x, y) for x in GRID_X for y in GRID_Y]
beams = []
if CREATE_BEAMS:
    for y in GRID_Y:
        beams += [((a, y), (b, y)) for a, b in zip(GRID_X, GRID_X[1:])]
    for x in GRID_X:
        beams += [((x, a), (x, b)) for a, b in zip(GRID_Y, GRID_Y[1:])]

answer = MessageBox.Show(
    f"Create in model '{model.GetInfo().ModelName}':\n\n"
    f"  {len(columns)} columns {column_profile} ({material}), Z {BASE_Z:.0f} to {TOP_Z:.0f} mm\n"
    + (f"  {len(beams)} beams {beam_profile} ({material}) at Z {TOP_Z:.0f} mm\n" if beams else "")
    + "\nChanges are not saved: close without saving to undo.",
    "PyNET - Create columns on grid",
    MessageBoxButtons.YesNo,
    MessageBoxIcon.Question,
)

created, failed = [], []
if answer != DialogResult.Yes:
    print("Cancelled: nothing was created.")
else:
    for x, y in columns:
        col = Beam(Beam.BeamTypeEnum.COLUMN)
        col.StartPoint = Point(x, y, BASE_Z)
        col.EndPoint = Point(x, y, TOP_Z)
        col.Profile.ProfileString = column_profile
        col.Material.MaterialString = material
        col.Name = "COLUMN"
        col.Class = COLUMN_CLASS
        col.Position.Plane = Position.PlaneEnum.MIDDLE
        col.Position.Depth = Position.DepthEnum.MIDDLE
        if col.Insert():
            created.append({"type": "Column", "guid": str(col.Identifier.GUID), "at_mm": [x, y]})
        else:
            failed.append({"type": "Column", "at_mm": [x, y]})

    for (x1, y1), (x2, y2) in beams:
        beam = Beam()
        beam.StartPoint = Point(x1, y1, TOP_Z)
        beam.EndPoint = Point(x2, y2, TOP_Z)
        beam.Profile.ProfileString = beam_profile
        beam.Material.MaterialString = material
        beam.Name = "BEAM"
        beam.Class = BEAM_CLASS
        beam.Position.Plane = Position.PlaneEnum.MIDDLE
        beam.Position.Depth = Position.DepthEnum.BEHIND     # hangs below the level line
        if beam.Insert():
            created.append({"type": "Beam", "guid": str(beam.Identifier.GUID),
                            "from_mm": [x1, y1], "to_mm": [x2, y2]})
        else:
            failed.append({"type": "Beam", "from_mm": [x1, y1], "to_mm": [x2, y2]})

    model.CommitChanges("PyNET: create columns on grid")   # once, at the end
    print(f"Created {len(created)} members ({column_profile} / {beam_profile or '-'}, {material}).")
    if failed:
        print(f"Tekla rejected {len(failed)} members: {failed}")
    print("Save the model (Ctrl+S) to keep the changes.")

ia_Result = {
    "type": "TeklaCreateColumnsOnGrid",
    "columnProfile": column_profile,
    "beamProfile": beam_profile,
    "material": material,
    "created": created,
    "failed": failed,
}
