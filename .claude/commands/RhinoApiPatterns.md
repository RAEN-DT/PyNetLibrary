# Skill: RhinoApiPatterns

Reference guide for RhinoCommon patterns on the PyNET platform. Read this skill whenever writing any
script that queries, iterates, or measures objects in a Rhino model. Read [docs/rhino.md](../../docs/rhino.md)
first for the boilerplate (`__rhinodoc__`), undo records and the general gotchas.

> Verified in Rhino 8 (CPython 3 + pythonnet). Validated examples: `01_Scripts/04_Rhino/`.

---

## Rule #1 — Query the tables, never rebuild them from objects

Rhino keeps layers, block definitions, materials, etc. in **document tables**. Query the table
directly; never iterate every object to discover which layers or blocks exist.

```python
# CORRECT — one pass over the definition table, the count comes from the API
for idef in doc.InstanceDefinitions:
    if idef is None or idef.IsDeleted:
        continue
    print(idef.Name, idef.UseCount())          # top-level references

# WRONG — walks every object in the model to rebuild the same information
counts = {}
for obj in doc.Objects:
    if obj.ObjectType == ObjectType.InstanceReference:
        name = obj.InstanceDefinition.Name    # DON'T DO THIS to count blocks
        counts[name] = counts.get(name, 0) + 1
```

**Why it matters:** a model with 5,000 block instances may have 40 definitions. `UseCount()` /
`GetReferences(0)` answer per definition without touching unrelated geometry — and `for obj in
doc.Objects` silently skips hidden/locked objects anyway (see Rule #2).

| Need | Table call |
|---|---|
| Instances of a block | `idef.GetReferences(0)` → `InstanceObject[]` (`0` = top level, `1` = + nested, `2` = all) |
| How many instances | `idef.UseCount()` |
| Objects inside a block definition | `idef.GetObjects()` |
| Objects on a layer | `doc.Objects.FindByLayer(layer)` (`Layer` or full-path string) |

**When to iterate objects:** only when you need object-level data — geometry, attributes, user text —
and then with `GetObjectList` and a type filter, never a bare loop.

---

## Rule #2 — Full inventory: `GetObjectList` with explicit settings

`for obj in doc.Objects` and `FindByObjectType` skip some hidden and locked objects. For any
inventory, audit or takeoff, enumerate with `ObjectEnumeratorSettings`:

```python
from Rhino.DocObjects import ObjectEnumeratorSettings, ObjectType

settings = ObjectEnumeratorSettings()
settings.HiddenObjects = True
settings.LockedObjects = True
settings.ObjectTypeFilter = ObjectType.Brep | ObjectType.Extrusion | ObjectType.Mesh
for obj in doc.Objects.GetObjectList(settings):
    ...
```

Other useful filters on the same object: `LayerIndexFilter`, `NameFilter`, `ReferenceObjects`
(worksession/linked objects), `IncludeLights`.

---

## Rule #3 — Object identity is a `Guid`

Every object has a persistent `obj.Id` (`System.Guid`). Store and report `str(obj.Id)`; look objects
up again with `doc.Objects.FindId(guid)` (returns `None` when not found, including `Guid.Empty`).

- **Every `doc.Objects.Add*` returns a `Guid` — always check it is not `Guid.Empty`.** An invalid
  geometry (e.g. an empty boolean result) is rejected silently: no exception, just `Guid.Empty`.
- After `ModifyAttributes` / `Replace`, re-fetch with `FindId(guid)` — the old `RhinoObject`
  reference holds the previous state.
- Never key data by the runtime serial number (`obj.RuntimeSerialNumber`) across sessions.

```python
from System import Guid

gid = doc.Objects.AddBrep(brep)
if gid == Guid.Empty:
    print("AddBrep rejected the geometry")
```

---

## Units — scale with `RhinoMath.UnitScale`, never a hardcoded factor

Rhino stores coordinates in the **model unit system** (`doc.ModelUnitSystem`), which varies per file
(mm, m, cm, ft…). Unlike Revit there is no fixed internal unit. Never assume metres and never write
`* 0.001`:

```python
from Rhino import RhinoMath, UnitSystem

k = RhinoMath.UnitScale(doc.ModelUnitSystem, UnitSystem.Meters)   # mm file → 0.001

length_m = curve.GetLength() * k
area_m2  = amp.Area * k ** 2
vol_m3   = vmp.Volume * k ** 3
```

Inverse (write a metric value into the model): `RhinoMath.UnitScale(UnitSystem.Meters, doc.ModelUnitSystem)`.
Use `doc.ModelAbsoluteTolerance` for any tolerance argument — never a literal like `0.001`.

---

## Measurements by object type

| `obj.ObjectType` | Geometry | Measurement | Notes |
|---|---|---|---|
| `Curve` | `Curve` | `curve.GetLength()` | closed planar curves also give area via `AreaMassProperties.Compute(curve)` |
| `Surface` / `Brep` | `Brep` | `AreaMassProperties.Compute(brep).Area` | volume only if `brep.IsSolid` |
| `Extrusion` | `Extrusion` | convert first: `ext.ToBrep(True)` | lightweight extrusions are not Breps |
| `Mesh` | `Mesh` | `AreaMassProperties` / `VolumeMassProperties` | volume only if `mesh.IsClosed` |
| `InstanceReference` | `InstanceReferenceGeometry` | count per definition (Rule #1) | measure the definition's objects (`idef.GetObjects()`) × `UseCount()` |
| `Annotation`, `TextDot`, `Point` | — | count only | |

```python
from Rhino.Geometry import AreaMassProperties, VolumeMassProperties, Extrusion

geom = obj.Geometry
if isinstance(geom, Extrusion):
    geom = geom.ToBrep(True)

amp = AreaMassProperties.Compute(geom)
area_m2 = amp.Area * k ** 2 if amp else 0.0

vol_m3 = 0.0
if getattr(geom, "IsSolid", False) or getattr(geom, "IsClosed", False):
    vmp = VolumeMassProperties.Compute(geom)
    vol_m3 = vmp.Volume * k ** 3 if vmp else 0.0
```

`Compute` returns `None` for geometry it cannot evaluate — always guard. Mass properties are slow on
large models (~22 s for 254 Breps): print progress every ~10 %.

---

## Grouping by layer

Layers are hierarchical (`Parent::Child`). Group by `Layer.FullPath`, not `Layer.Name` — two layers
named `Walls` under different parents are different layers.

```python
layer_path = {}
for layer in doc.Layers:
    if layer is None or layer.IsDeleted:
        continue
    layer_path[layer.Index] = layer.FullPath

totals = {}
for obj in doc.Objects.GetObjectList(settings):
    path = layer_path.get(obj.Attributes.LayerIndex, "?")
    totals[path] = totals.get(path, 0) + 1
```

`FindByLayer(name)` returns `None` when the layer does not exist and an empty array when it exists but
is empty — normalise with `doc.Objects.FindByLayer(path) or []`.

---

## User text — empty vs missing

User text values are always strings, and **there is no "empty" state**:

> ✅ **Verified in-session:** `SetUserString("K", "")` **deletes** the key (`UserStringCount` drops,
> `GetUserString("K")` returns `None`). A missing key also returns `None`.

- Missing and blank are the same thing: test with `if not attrs.GetUserString(key):`.
- To store "explicitly zero / not applicable", write a real value (`"0"`, `"N/A"`), never `""`.
- Numbers come back as strings in the user's format — parse defensively
  (`float(v.replace(",", "."))` inside `try/except ValueError`).
- `doc.Objects.FindByUserString(...)` may return `None` or an empty array when nothing matches —
  normalise with `or []`.

```python
# Write — always on a duplicated attributes object, inside an undo record
attrs = obj.Attributes.Duplicate()
attrs.SetUserString("OBRA_Fase", "F2")
doc.Objects.ModifyAttributes(obj, attrs, True)
```

---

## Building a .NET `List[T]` — never pass a Python `list`

RhinoCommon methods that take `IEnumerable<T>` (booleans, joins, `InstanceDefinitions.Add`, …) do not
accept a Python `list`. Build an empty `List[T]()` and `.Add()` each item:

```python
from System.Collections.Generic import List
from Rhino.Geometry import Brep

cutters = List[Brep]()
for b in cutter_breps:
    cutters.Add(b)
result = Brep.CreateBooleanDifference(targets, cutters, doc.ModelAbsoluteTolerance)
```

Same for `List[Point3d]` → `Polyline`, `List[GeometryBase]` + `List[ObjectAttributes]` →
`InstanceDefinitions.Add(name, description, basePoint, geometry, attributes)`.

---

## Booleans

- Cutters must be closed and **outward-oriented** — after `CapPlanarHoles`, check
  `brep.SolidOrientation` and `brep.Flip()` if it is `Inward`.
- A cutter face **coplanar** with a target face gives an empty/invalid result: extend the cutter past
  the face (e.g. 0.3 m in model units).
- The result can be `None` or an empty array — check before `AddBrep`, then check the `Guid`.

---

## Exporting to Excel

The openpyxl rules are host-agnostic — follow
[RevitApiPatterns → Exporting to Excel](RevitApiPatterns.md#exporting-to-excel-openpyxl): never
auto-fit via `ws.columns`, table names like `Tabla_1` (never `T1`), write empty cells as `None`.
Report object ids as `str(obj.Id)`.

---

## Common pitfalls

| Symptom | Cause | Fix |
|---|---|---|
| Inventory misses objects | `for obj in doc.Objects` / `FindByObjectType` skip hidden/locked | `GetObjectList(ObjectEnumeratorSettings)` with `HiddenObjects`/`LockedObjects = True` |
| Slow block count | Iterating all objects to count instances | `idef.UseCount()` / `idef.GetReferences(0)` |
| Areas/lengths off by 1000 or 10⁶ | Assumed metres, or hardcoded `* 0.001` | `RhinoMath.UnitScale(doc.ModelUnitSystem, UnitSystem.Meters)` (² for area, ³ for volume) |
| Extrusions measured as 0 / `Compute` returns `None` | `Extrusion` is not a `Brep` | `ext.ToBrep(True)` first |
| Volume on open geometry | `VolumeMassProperties` on non-solid Brep/Mesh | check `IsSolid` / `IsClosed` |
| Object "added" but not in the model | `Add*` returned `Guid.Empty` (invalid geometry) | check the returned `Guid` |
| Attribute change lost / no undo | Edited `obj.Attributes` in place | `Duplicate()` → change → `ModifyAttributes(obj, attrs, True)` |
| User text key vanished after writing `""` | `SetUserString(key, "")` deletes the key | store an explicit value (`"0"`, `"N/A"`) |
| `TypeError: 'NoneType' object is not iterable` | `FindByLayer` / `FindByUserString` returned `None` | `... or []` |
| Two layers merged in a report | Grouped by `Layer.Name` | group by `Layer.FullPath` |
| `No method matches given arguments` | Python `list` passed for `IEnumerable<T>` | `List[T]()` + `.Add()` |
| Boolean gives empty result | Coplanar faces or inward cutter | extend cutter past the face; `Flip()` inward solids |

---

<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->
