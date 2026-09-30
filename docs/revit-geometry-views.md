<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: geometry, rooms, masses, views and dimensions (Revit)

Read [revit.md](revit.md) and [RevitApiPatterns](../.claude/commands/RevitApiPatterns.md) first.
These patterns were validated in the generative-design engines and the example library.

---

## Rooms

- **Boundary:** `room.GetBoundarySegments(SpatialElementBoundaryOptions())` → loops of segments;
  each `seg.ElementId` is the wall/column that bounds the room.
- **Area:** `room.Area` is measured to the wall **faces** (usable area). A built area also needs half
  the wall thickness along every segment.
- **What stands inside:** scan every `CategoryType.Model` element and test the **bounding-box
  midpoint** with `room.IsPointInRoom(p)` — not `Location.Point` (the insertion point can sit
  off-centre), and not a hand-picked category list (it always misses something). Exclude the room's
  own boundary elements by id: a perimeter wall's centreline can test as inside.
- **Doors** hosted in the perimeter wall sit *outside* the room polygon (midpoint on the wall
  centreline) — accept them by distance to the boundary. Door ↔ room: `door.ToRoom[phase]` /
  `door.FromRoom[phase]`.
- **Floor under a room:** its bottom face (`FaceNormal == -Z`) → `face.GetEdgesAsCurveLoops()` →
  `Floor.Create(doc, loops, floor_type_id, room.LevelId)` (`doc.Create.NewFloor` was removed in 2022).

## Masses as generated geometry (DirectShape)

```python
loop = CurveLoop()
for i in range(4):
    loop.Append(Line.CreateBound(pts[i], pts[(i + 1) % 4]))
loops = List[CurveLoop](); loops.Add(loop)
solid = GeometryCreationUtilities.CreateExtrusionGeometry(loops, XYZ.BasisZ, height)
shape = List[GeometryObject](); shape.Add(solid)
ds = DirectShape.CreateElement(doc, ElementId(BuiltInCategory.OST_Mass))
ds.SetShape(shape)
```

`OST_Mass` is hidden by default in project views — `view.SetCategoryHidden(ElementId(BuiltInCategory.OST_Mass), False)`.

## Colour overrides with a solid fill

```python
solid_fill = next(fp.Id for fp in FilteredElementCollector(doc).OfClass(FillPatternElement)
                  if fp.GetFillPattern().IsSolidFill)
ogs = OverrideGraphicSettings()
ogs.SetProjectionLineColor(Color(r, g, b))
ogs.SetSurfaceForegroundPatternId(solid_fill)
ogs.SetSurfaceForegroundPatternColor(Color(r, g, b))
view.SetElementOverrides(element_id, ogs)
```

Copy overrides between views with `view_a.GetElementOverrides(id)` → `view_b.SetElementOverrides(id, ogs)`.

## Groups

- `doc.Create.NewGroup(List[ElementId])`. Group names must be unique.
- A group instance's bounding box is the **union of all its members** — an old variant group blocks
  every new candidate in a geometric test. Exclude previous groups' members explicitly.
- A group instance cannot be hidden (`CanBeHidden` is False) — hide its **members**.
- Deleting a group instance leaves its `GroupType` behind (the next group gets "(2)") — delete the
  type too.

## Views

- Duplicate: `view.Duplicate(ViewDuplicateOption.Duplicate)`; loop on the name until it is unique.
- Hide: `view.HideElements(List[ElementId])`, only ids where `el.CanBeHidden(view)` and not
  `el.IsHidden(view)`.
- **An open view cannot be deleted** — switch the active view first, outside the transaction.
- Detail lines report `CategoryType.Model` — exclude view-specific elements (`OwnerViewId` valid)
  from geometric scans.
- Activate a view from a script: `uidoc.RequestViewChange(view)`.

## Dimensions

```python
opt = Options()
opt.ComputeReferences = True          # REQUIRED - without it face.Reference is None
opt.DetailLevel = ViewDetailLevel.Fine
solid = next(g for g in el.get_Geometry(opt) if isinstance(g, Solid) and g.Volume > 0)
face = next(f for f in solid.Faces if isinstance(f, PlanarFace) and f.FaceNormal.IsAlmostEqualTo(XYZ(0, -1, 0)))
refs = ReferenceArray(); refs.Append(face.Reference); ...
doc.Create.NewDimension(view, Line.CreateBound(p1, p2), refs)
```

Walls can be dimensioned on their centreline with `Reference(wall)` (`09_Tags/DimensionWalls.py`).
Dimensions need a plan view (`ViewPlan`). For batch creation set
`FailureHandlingOptions.SetForcedModalHandling(False)` on the transaction so warnings don't stop it.

## Selection with a filter

```python
class WallFilter(ISelectionFilter):                   # .NET interface implemented in Python
    def AllowElement(self, e):
        return e.__class__ == Wall                    # pythonnet returns the concrete class
    def AllowReference(self, ref, pos):
        return True

try:
    refs = uidoc.Selection.PickObjects(ObjectType.Element, WallFilter(), "Select walls")
except OperationCanceledException:                    # Autodesk.Revit.Exceptions - user pressed ESC
    refs = []
```

Pre-select current elements in `PickObjects` with a list of
`Reference.ParseFromStableRepresentation(doc, el.UniqueId)`.
