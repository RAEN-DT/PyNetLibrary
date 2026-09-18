<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: viewpoints, visibility and colour (Navisworks)

Read [navisworks.md](navisworks.md) first. Reference scripts:
`05_QueryElements/PlanViewpointFromSelection.py`, `05_QueryElements/IsolatePanels.py`,
`05_QueryElements/IsolateFoundation.py`.

---

## Isolate elements

There is no single "isolate" call: show everything, then hide the geometry you don't want.

```python
from Autodesk.Navisworks.Api import ModelItemCollection

all_items = doc.Models.RootItemDescendantsAndSelf
doc.Models.SetHidden(all_items, False)                 # reset

keep = set(hash(d) for it in targets for d in it.DescendantsAndSelf if d.HasGeometry)
hide = ModelItemCollection()
for it in all_items:
    if it.HasGeometry and hash(it) not in keep:
        hide.Add(it)
doc.Models.SetHidden(hide, True)
doc.CurrentSelection.CopyFrom(targets)
```

Hide **geometry** nodes, and protect the targets' geometry descendants — the target is often a
parent node without geometry. Don't use `InstanceGuid` as the identity (many nodes share
`Guid.Empty`).

Finding the targets: a `Search` with `SearchCondition.HasPropertyByDisplayName(tab, prop)` plus
`.DisplayStringContains(text)` (partial match) or `.EqualValue(VariantData.FromDisplayString(v))`.

## Colour overrides

```python
from Autodesk.Navisworks.Api import Color
doc.Models.OverridePermanentColor(items, Color(1.0, 0.0, 0.0))   # components 0..1, NOT 0..255
```

`OverridePermanentColor` survives orbiting, isolating and saved viewpoints.

## A plan viewpoint aligned with an element

```python
from Autodesk.Navisworks.Api import Vector3D, ViewpointProjection

vp = doc.CurrentViewpoint.CreateCopy()
vp.Projection = ViewpointProjection.Orthographic
vp.AlignUp(Vector3D(ux, uy, 0))          # element's local Y = screen up
vp.AlignDirection(Vector3D(0, 0, -1))    # look straight down
vp.ZoomBox(box)                          # BoundingBox3D of the selection
vp.SetExtentsAtFocalDistance(w, h)       # exact framing (box projected on the camera axes)
doc.CurrentViewpoint.CopyFrom(vp)        # apply to the active view FIRST

saved = doc.SavedViewpoints.CaptureRuntimeOverrides()   # also stores colour overrides
saved.DisplayName = name
doc.SavedViewpoints.AddCopy(None, saved)
live = next(s for s in doc.SavedViewpoints.RootItem.Children if str(s.DisplayName) == name)
doc.SavedViewpoints.ReplaceFromCurrentView(live)
```

**Save the viewpoint from the active view** (`CaptureRuntimeOverrides` + `ReplaceFromCurrentView`).
A `Viewpoint` built in code and saved directly restores **rotated**.

**The element's real rotation** is not a property. Read it from the geometry's local-to-world matrix
(COM API) — first geometry fragment under the item:

```python
from Autodesk.Navisworks.Api.ComApi import ComApiBridge
from Autodesk.Navisworks.Api.Interop import ComApi

for d in item.DescendantsAndSelf:
    if d.HasGeometry:
        for f in ComApiBridge.ToInwOaPath(d).Fragments():
            m = ComApi.InwLTransform3f3(ComApi.InwOaFragment3(f).GetLocalToWorldMatrix()).Matrix
            ax, ay = float(m[0]), float(m[1])      # local X axis in world coordinates
            break
        break
```

**Regenerate, don't pile up:** delete saved viewpoints by name prefix before creating new ones —
`doc.SavedViewpoints.Remove(root, old)` for each `old` in `list(root.Children)` whose name starts
with the prefix.
