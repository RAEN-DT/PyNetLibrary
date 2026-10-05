# Skill: TeklaApiPatterns

Reference guide for Tekla Open API patterns on the PyNET platform. Read this skill whenever writing
any script that queries, iterates, measures or modifies objects in a Tekla Structures model. Read
[docs/tekla.md](../../docs/tekla.md) first for the boilerplate (`__teklamodel__`), `CommitChanges`,
catalogs and how PyNET runs out of process.

> Verified in Tekla Structures 2026 (CPython 3 + pythonnet) unless marked ⏳ (written from the API,
> not yet run in a session). Validated examples: `01_Scripts/05_Tekla/`.

---

## Rule #1 — Ask the selector for the types you need, never "everything"

`GetAllObjects()` returns far more than geometry. On a model with 264 parts it returned 1,106
objects: the parts, but also 264 `Assembly`, 528 `ControlPoint` (part end points), 37 `GridPlane`,
and the project organizer (`Site`, `Building`, `HierarchicDefinition`, `HierarchicObject`) plus
`LoadGroup`. Ask for the types directly:

```python
import clr
clr.AddReference("Tekla.Structures.Model")
from System import Array, Type
from Tekla.Structures.Model import Beam, ContourPlate, PolyBeam

# CORRECT — only the part types you need
types = Array[Type]([clr.GetClrType(Beam), clr.GetClrType(ContourPlate), clr.GetClrType(PolyBeam)])
parts = model.GetModelObjectSelector().GetAllObjectsWithType(types)

# WRONG — walks organizer, assemblies, control points... and needs filtering afterwards
everything = model.GetModelObjectSelector().GetAllObjects()
```

When you genuinely need "all geometry" (e.g. a delete-all), use `GetAllObjects()` **and filter with
`isinstance`** against a whitelist — never delete or report whatever comes back:

```python
from Tekla.Structures.Model import BaseComponent, Part, BoltGroup, BaseWeld, Reinforcement, Grid

GEOMETRY = (BaseComponent, Part, BoltGroup, BaseWeld, Reinforcement, Grid)
e = model.GetModelObjectSelector().GetAllObjects()
while e.MoveNext():
    obj = e.Current
    if isinstance(obj, GEOMETRY):
        ...
```

- `ModelObject.ModelObjectEnum` has **no `PART`** — only concrete kinds (`BEAM`, `CONTOURPLATE`, …).
  Use the `Type[]` overload with the concrete classes or `isinstance(obj, Part)`.
- `Beam` covers beams **and** columns (`beam.Type` tells them apart; insert columns with
  `Beam(Beam.BeamTypeEnum.COLUMN)`).

---

## Rule #2 — Every call is a round trip: keep them few

PyNET talks to Tekla across processes, so per-object calls dominate run time on big models.

- **Don't load object data you won't read.** For identity-only work (delete, collect ids) set
  `enumerator.SelectInstances = False` before iterating: objects come back with their
  `Identifier` and correct Python type, without their data. `Delete()` works on them (verified:
  the delete-all button).
- **One `CommitChanges()` at the end**, never per object.
- **Read only the report properties you need**, once per object; don't call `GetReportProperty`
  inside nested loops.
- Print progress every ~10 % on long loops.

```python
e = model.GetModelObjectSelector().GetAllObjects()
e.SelectInstances = False        # identifiers + types only
while e.MoveNext():
    ...
```

---

## Rule #3 — Identity: store the GUID, not the ID

`obj.Identifier.ID` (int) is local to the model; `obj.Identifier.GUID` is the stable id that
survives sharing, IFC and Trimble Connect. Store and report `str(obj.Identifier.GUID)`.

To get an object back:

```python
from Tekla.Structures import Identifier

fresh = Beam()
fresh.Identifier = Identifier(guid)        # ⏳ or model.SelectModelObject(Identifier(guid))
if fresh.Select():                         # False = deleted / not found
    ...
```

After `Modify()` the Python object already holds the new state; after **another** script or the
user changed it, call `Select()` again to refresh.

---

## Reading data: report properties and UDAs

Tekla's property data comes in two kinds:

| Kind | What | Read | Write |
|---|---|---|---|
| **Report properties** | computed by Tekla: `LENGTH`, `WEIGHT`, `VOLUME`, `AREA`, `PROFILE`, `MATERIAL`, `ASSEMBLY_POS`, `PART_POS`, `PHASE`… | `GetReportProperty(name, default)` | never (computed) |
| **UDAs** (user-defined attributes) | values stored on the object, defined in `objects.inp` | `GetUserProperty(name, default)` | `SetUserProperty(name, value)` |

Both C# methods use a `ref` argument; pythonnet passes the default in and ⏳ returns a
`(found, value)` tuple. **The type of the default picks the overload** — `""` for strings, `0.0`
for doubles, `0` for integers. Asking `LENGTH` with `""` or `PROFILE` with `0.0` gives
`found = False`.

```python
found, length_mm = part.GetReportProperty("LENGTH", 0.0)
found, profile = part.GetReportProperty("PROFILE", "")
found, comment = part.GetUserProperty("comment", "")
```

**`found = False` means "not available for this object", not zero** — treat it as missing, not 0.

Report-property units (⏳ confirm on first use): `LENGTH` mm, `AREA` mm², `VOLUME` mm³,
`WEIGHT` kg. Convert explicitly (`/ 1000`, `/ 1e6`, `/ 1e9`) and say the unit in the output.

Writing UDAs (⏳): `part.SetUserProperty("comment", "OK")` returns `bool`; then
`model.CommitChanges()`. The UDA must exist in the environment's `objects.inp` to show in the
dialog — undefined names can still be stored but nobody sees them.

---

## Measurements

| Need | Call | Notes |
|---|---|---|
| Length of a member | `GetReportProperty("LENGTH", 0.0)` | mm, along the part (cut length) |
| Weight | `GetReportProperty("WEIGHT", 0.0)` | kg, from profile × length × density |
| Volume / area | `"VOLUME"` / `"AREA"` with `0.0` | mm³ / mm² |
| Bounding box | `part.GetSolid().MinimumPoint` / `.MaximumPoint` | ✅ verified; global coordinates, mm |
| Assembly totals | `part.GetAssembly()` then report properties on the assembly | ⏳ |

Group quantities by `Profile.ProfileString`, `Material.MaterialString`, `Name`, `Class` or
`PHASE` — these are plain properties on parts (after `Select()`), cheaper than report properties.

Checking how a profile sits on its line (the `Position.Depth` rule in tekla.md):

```python
s = beam.GetSolid()
print(beam.StartPoint.Z, round(s.MinimumPoint.Z, 1), round(s.MaximumPoint.Z, 1))
# BEHIND on a level line at Z=3600 should give max Z = 3600 (hanging below)
```

---

## The user's selection

```python
from Tekla.Structures.Model.UI import ModelObjectSelector as UISelector   # not the Model one

selected = UISelector().GetSelectedObjects()
while selected.MoveNext():
    obj = selected.Current
```

Two classes share the name `ModelObjectSelector`: `Tekla.Structures.Model.ModelObjectSelector`
(from `model.GetModelObjectSelector()`, the whole model) and
`Tekla.Structures.Model.UI.ModelObjectSelector` (the user's selection). Alias the UI one on import.
To select objects for the user: `UISelector().Select(ArrayList_of_objects)` (⏳).

---

## .NET collections

- `Type[]` for the selector: `Array[Type]([clr.GetClrType(Beam)])` (`from System import Array, Type`).
- APIs that take `ArrayList` (UI selection, contour points of some objects): build it and `.Add()`:

```python
from System.Collections import ArrayList
items = ArrayList()
for obj in objs:
    items.Add(obj)
```

- Generic `List[T]`: never pass a Python `list` to the constructor — build empty and `.Add()` (same
  rule as [RevitApiPatterns](RevitApiPatterns.md#building-a-net-listt--never-pass-a-python-list-to-the-constructor)).
- Enumerators: `while e.MoveNext(): obj = e.Current` is the form used in every verified script.

---

## Exporting to Excel

The openpyxl rules are host-agnostic — follow
[RevitApiPatterns → Exporting to Excel](RevitApiPatterns.md#exporting-to-excel-openpyxl): never
auto-fit via `ws.columns`, table names like `Tabla_1` (never `T1`), write empty cells as `None`.
Report object ids as `str(obj.Identifier.GUID)`.

---

## Common pitfalls

| Symptom | Cause | Fix |
|---|---|---|
| Inventory has 4× more objects than parts | `GetAllObjects()` includes assemblies, control points, grid planes, organizer | `GetAllObjectsWithType(Type[])` or `isinstance` whitelist (Rule #1) |
| `AttributeError: PART` on `ModelObjectEnum` | no such member | `Type[]` overload / `isinstance(obj, Part)` |
| Script is slow on a big model | thousands of round trips | `SelectInstances = False`, one `CommitChanges`, fewer report-property calls (Rule #2) |
| Changes not in the model | no `CommitChanges()` | call it once at the end |
| User lost the changes | `CommitChanges` doesn't save | tell the user to save (Ctrl+S) |
| `Insert()` returned `False`, no exception | Tekla rejected the object | always check the `bool`; check profile/material in the catalog |
| Profile `HEB300` "missing" in a US model | catalogs depend on the environment | enumerate the catalog, pick from candidates (tekla.md) |
| Report property always `found = False` | default of the wrong type picked the wrong overload | `0.0` for numbers, `""` for text, `0` for integers |
| Report value read as 0 and summed | `found = False` treated as zero | skip / flag missing values |
| Got the user's selection from the wrong class | `Model.ModelObjectSelector` vs `Model.UI.ModelObjectSelector` | import the UI one with an alias |
| Ids don't match after model sharing / IFC | stored `Identifier.ID` | store `Identifier.GUID` |
| `PyNet Instance not found` mid-session | the user closed Tekla, PyNET exited with it | reopen Tekla and click a PyNET macro |

---

<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->
