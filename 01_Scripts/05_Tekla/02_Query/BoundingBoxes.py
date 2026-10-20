# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import clr

clr.AddReference("Tekla.Structures.Model")

from System import Array, Type
from Tekla.Structures.Geometry3d import AABB, Point
from Tekla.Structures.Model import Model, Part, Beam, ContourPlate, PolyBeam
from Tekla.Structures.Model.UI import ModelObjectSelector as UISelector, ViewHandler

# The host injects the connected model as __teklamodel__
try:
    model = __teklamodel__
except NameError:
    model = Model()

# ---------------------------------------------------------------------------
# Bounding box (global coordinates, mm) of every selected part plus the box
# that encloses them all; optionally zoom the visible model views to it.
# Read-only on the model (zooming only moves the views).
#
# part.GetSolid().MinimumPoint / .MaximumPoint give the part's axis-aligned
# box in global coordinates, mm. Works on the user's selection; with nothing
# selected, set USE_ALL_PARTS_IF_EMPTY to fall back to every part (slow on a
# big model: one GetSolid round trip per part).
#
# Verified (TeklaApiPatterns): UI selection, part.GetSolid().MinimumPoint /
# .MaximumPoint.
# Run on Tekla 2026 (2026-10-16, model with beams, columns, plates, bolts,
# welds): the whole script - AABB(min, max), union box,
# ViewHandler.GetVisibleViews(), ZoomToBoundingBox / RedrawView.
# ---------------------------------------------------------------------------
ZOOM_TO_RESULT = True
USE_ALL_PARTS_IF_EMPTY = False
MARGIN_MM = 500.0   # added on every side of the zoom box


def xyz(p):
    return [round(p.X, 1), round(p.Y, 1), round(p.Z, 1)]


if not model.GetConnectionStatus():
    raise Exception("Not connected to Tekla Structures.")

parts = []
selected = UISelector().GetSelectedObjects()
while selected.MoveNext():
    if isinstance(selected.Current, Part):
        parts.append(selected.Current)

if not parts and USE_ALL_PARTS_IF_EMPTY:
    # concrete part classes only - the selector is asked for types, not "Part" (Rule #1)
    types = Array[Type]([clr.GetClrType(t) for t in (Beam, ContourPlate, PolyBeam)])
    e = model.GetModelObjectSelector().GetAllObjectsWithType(types)
    while e.MoveNext():
        if isinstance(e.Current, Part):
            parts.append(e.Current)

if not parts:
    raise Exception("Select one or more parts in Tekla and run again.")

boxes = []
lo = [float("inf")] * 3
hi = [float("-inf")] * 3
step = max(1, len(parts) // 10)
for i, part in enumerate(parts, 1):
    if len(parts) > 50 and i % step == 0:
        print(f"  {i}/{len(parts)}")
    solid = part.GetSolid()
    mn, mx = solid.MinimumPoint, solid.MaximumPoint
    for k, (a, b) in enumerate(zip(xyz(mn), xyz(mx))):
        lo[k] = min(lo[k], a)
        hi[k] = max(hi[k], b)
    boxes.append({
        "type": part.GetType().Name,
        "guid": str(part.Identifier.GUID),
        "profile": part.Profile.ProfileString,
        "min_mm": xyz(mn),
        "max_mm": xyz(mx),
        "size_mm": [round(b - a, 1) for a, b in zip(xyz(mn), xyz(mx))],
    })

size = [round(b - a, 1) for a, b in zip(lo, hi)]
print(f"{len(boxes)} parts. Overall box (mm): min {lo}  max {hi}  size {size}")

zoomed = 0
if ZOOM_TO_RESULT:
    box = AABB(Point(lo[0] - MARGIN_MM, lo[1] - MARGIN_MM, lo[2] - MARGIN_MM),
               Point(hi[0] + MARGIN_MM, hi[1] + MARGIN_MM, hi[2] + MARGIN_MM))
    views = ViewHandler.GetVisibleViews()
    while views.MoveNext():
        if ViewHandler.ZoomToBoundingBox(views.Current, box):
            ViewHandler.RedrawView(views.Current)
            zoomed += 1
    print(f"Zoomed {zoomed} visible view(s)")

ia_Result = {
    "type": "TeklaBoundingBoxes",
    "units": "mm",
    "overall": {"min": lo, "max": hi, "size": size},
    "parts": boxes,
    "viewsZoomed": zoomed,
}
