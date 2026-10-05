<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: Tekla Structures scripts

Read this guide **before writing any Tekla script**. For model queries/measurements, also read
[TeklaApiPatterns](../.claude/commands/TeklaApiPatterns.md). For forms/dialogs read [winforms.md](winforms.md).
Validated examples live in `01_Scripts/05_Tekla/` — read the closest one first.

Related: [revit.md](revit.md) · [pythonnet.md](pythonnet.md) · [stubs.md](stubs.md)

> **Host detection:** Tekla appears as **"Tekla Structures <year>"** in `list_active_instances`
> (bridge with Tekla support, from 2026-10). Tekla 2023-2026 are supported; the API is the Tekla Open
> API (`Tekla.Structures.*`).

---

## How PyNET runs in Tekla — different from every other host

Tekla has no in-process add-ins. PyNET for Tekla is a **separate exe**
(`Raen.Tekla.Pynet.<year>.exe`) that connects to the running Tekla through the Open API remoting
channel. Consequences for scripts:

- The MCP pipe belongs to the PyNET exe, not to `TeklaStructures.exe`: the PID in
  `list_active_instances` is the exe's.
- **The exe closes when Tekla closes.** A `PyNet Instance (PID …) not found` right after the user
  closed Tekla is expected — ask them to reopen Tekla and click a PyNET macro (`PyNET_ShowButtons`).
- Every API call is a cross-process round trip. Loops of thousands of `Select()` /
  `GetReportProperty()` calls are noticeably slower than in Revit — see TeklaApiPatterns Rule #2.
- The Open API DLLs are always the running Tekla's own (`bin\Net48Runtime`, then `bin`), so
  `clr.AddReference("Tekla.Structures.Something")` loads the right version without a path.

---

## Standard boilerplate

The host injects `__teklamodel__` (a connected `Tekla.Structures.Model.Model`). Use the plain
`try/except NameError` below — you cannot probe for it with `globals()` / `getattr` (blocked by the
validator). Import **only the types the script uses**, by name — never `from Tekla.Structures.Model
import *`. Check uncertain names against the stubs index (`CLASSES.tsv`, `namespace` column
`Tekla.*`; stubs in `02_PyNet Stubs/Tekla/`): `Point`, `Model`, `Solid`, `Position` also exist in
other hosts' namespaces.

```python
import clr

clr.AddReference("Tekla.Structures.Model")
from Tekla.Structures.Model import Model, Beam, ContourPlate, Position   # what you use
from Tekla.Structures.Geometry3d import Point                            # Geometry3d needs no extra reference

# The host injects the connected model as __teklamodel__
try:
    model = __teklamodel__
except NameError:
    model = Model()

if not model.GetConnectionStatus():
    raise Exception("Not connected to Tekla Structures.")
```

| | Revit | Rhino | Tekla |
|---|---|---|---|
| Document | `__revit__.ActiveUIDocument.Document` | `__rhinodoc__` | `__teklamodel__` (`Model`) |
| Main assembly | `RevitAPI` | `RhinoCommon` | `Tekla.Structures.Model` |
| Writes | Transaction | Undo record | **`model.CommitChanges()`** |
| Units | feet (internal) | per file | **always mm** |
| Property data | Parameters | User Text | Report properties (read) + UDAs (read/write) |
| Object identity | `ElementId` | `Guid` | `Identifier` (`.ID` int, `.GUID`) |

### Assemblies

| Need | `clr.AddReference` | Namespaces |
|---|---|---|
| Model objects, selection, views | `Tekla.Structures.Model` | `Tekla.Structures.Model`, `.Model.UI`, `.Model.Operations` |
| Points, vectors, coordinate systems | (comes with Model) | `Tekla.Structures.Geometry3d` |
| Settings, version, advanced options | `Tekla.Structures` | `Tekla.Structures` |
| Drawings | `Tekla.Structures.Drawing` | `Tekla.Structures.Drawing`, `.Drawing.UI` |
| Profile / material / bolt catalogs | `Tekla.Structures.Catalogs` | `Tekla.Structures.Catalogs` |
| Distances, units for dialogs | `Tekla.Structures.Datatype` | `Tekla.Structures.Datatype` |

> The MCP bridge whitelists `Tekla.Structures`, `.Model`, `.Drawing`, `.Datatype`, `.Dialog`,
> `.Catalogs`, `.Plugins`. A bridge installed before `.Catalogs` was added rejects
> `clr.AddReference("Tekla.Structures.Catalogs")` with *Non-whitelisted assembly* — update the bridge.

### Model essentials

| Need | Call |
|---|---|
| Model name / folder | `model.GetInfo().ModelName` (`"X.db1"`), `.ModelPath` |
| Program version | `TeklaStructuresInfo.GetCurrentProgramVersion()` → `"2026"` |
| Advanced option | `TeklaStructuresSettings.GetAdvancedOption("XS_…", "")` — `ref` param: ⏳ expected to return `(ok, value)` in pythonnet |
| All objects | `model.GetModelObjectSelector().GetAllObjects()` — includes non-geometry, see TeklaApiPatterns Rule #1 |
| Objects of a type | `GetAllObjectsWithType(Array[Type]([clr.GetClrType(Beam)]))` |
| User's selection | `Tekla.Structures.Model.UI.ModelObjectSelector().GetSelectedObjects()` |
| Views | `Tekla.Structures.Model.UI.ViewHandler.GetVisibleViews()`, `ZoomToBoundingBox(view, AABB)`, `RedrawView(view)` |

---

## Writes: `Insert` / `Modify` / `Delete`, then `CommitChanges`

Tekla has no transactions and no undo record API. Each object call returns a **`bool`** — `False`
means Tekla rejected it, with **no exception**. Nothing is guaranteed visible/persisted until
`model.CommitChanges()`:

```python
beam = Beam()
beam.StartPoint = Point(0, 0, 3600)
beam.EndPoint = Point(6000, 0, 3600)
beam.Profile.ProfileString = "W410X60"
beam.Material.MaterialString = "A992"
beam.Name = "BEAM"
beam.Class = "3"                     # class = colour in the default representation
if not beam.Insert():
    print("Insert rejected")

model.CommitChanges("PyNET: what the script did")   # once, at the end
```

- **Always check the returned `bool`** of `Insert()`, `Modify()`, `Delete()`, `Select()`.
- **Call `CommitChanges()` once at the end**, not after every object (each call is a round trip).
- `CommitChanges` does **not save the model** — the user saves with Ctrl+S. Tell them; closing
  without saving discards the script's changes.
- Columns: `Beam(Beam.BeamTypeEnum.COLUMN)`; horizontal members: `Beam()`.
- Slabs / plates: `ContourPlate` + `AddContourPoint(ContourPoint(Point(...), None))`; profile string
  is the thickness for concrete (`"200"`), `"PL20"`-style for steel plates.

### Coordinates and positions

All coordinates are **millimetres** in the current work plane — the global plane unless the script
or user changed it (`model.GetWorkPlaneHandler()`). Never scale by 1000 "just in case".

How the profile sits on the reference line is `part.Position` (`Plane`, `Depth`, `Rotation`):

| Want | Set |
|---|---|
| Beam hanging under its level line | `beam.Position.Depth = Position.DepthEnum.BEHIND` |
| Slab sitting on its contour level | `slab.Position.Depth = Position.DepthEnum.FRONT` |
| Centred (default for columns) | `Position.DepthEnum.MIDDLE`, `Position.PlaneEnum.MIDDLE` |

> ⏳ Depth semantics as above are what the PyNET sample building uses; confirm with
> `part.GetSolid()` Z extents the first time you rely on them (TeklaApiPatterns has the check).

---

## Catalogs depend on the environment

Profile and material names come from the model's environment catalog, **not** from a fixed list:
a US-environment model has `W310X97` / `A992` / `C30`, a European one `HEB300` / `S355J2`.
Check the names against the catalog before inserting — don't rely on `Insert()` to reject an
unknown profile (⏳ what Tekla does with one is not verified yet):

```python
clr.AddReference("Tekla.Structures.Catalogs")
from Tekla.Structures.Catalogs import CatalogHandler, LibraryProfileItem, MaterialItem

profiles, materials = set(), set()
ch = CatalogHandler()
e = ch.GetLibraryProfileItems()
while e.MoveNext():
    profiles.add(e.Current.ProfileName)
e = ch.GetMaterialItems()
while e.MoveNext():
    materials.add(e.Current.MaterialName)

def pick(available, *candidates):
    """First candidate that exists in this model's catalog."""
    for c in candidates:
        if c in available:
            return c
    raise Exception(f"None of {candidates} in the catalog")

column_profile = pick(profiles, "HEB300", "W310X97")
```

> ✅ Verified (Tekla 2026, US catalog: 5,861 profiles, 249 materials). `LibraryProfileItem().Select(name)`
> returns `False` for names not in the catalog — fine as a single check, but enumerate once when
> checking many names.

---

## The Python.NET runtime is persistent

Same as the other hosts: the Python runtime inside PyNET for Tekla is persistent and shared across
`send_command` and buttons for as long as the exe lives (i.e. until Tekla closes). A failed import
can leave a broken module in `sys.modules`; if a button fails but the same script works through
`send_command`, ask the user to restart Tekla (that restarts PyNET too).

## Special folder paths

Never hardcode `Path.home() / "Desktop"` (OneDrive redirects it):
`Environment.GetFolderPath(Environment.SpecialFolder.Desktop)`.

---

## Gotchas (verified in Tekla 2026, CPython 3 + pythonnet)

| Situation | What happens | Do this |
|---|---|---|
| `GetAllObjects()` for "everything" | also returns `Site`, `Building`, `HierarchicDefinition`/`HierarchicObject` (organizer), `LoadGroup`, `Assembly`, `GridPlane`, `ControlPoint`s at part ends | filter by `isinstance` (TeklaApiPatterns Rule #1) |
| `ModelObjectEnum.PART` | does not exist (only concrete kinds: `BEAM`, `CONTOURPLATE`, …) | use the `Type[]` overload with `Part` subclasses, or `isinstance(obj, Part)` |
| Profile names from another region's catalog (`HEB300` in a US model) | not in the catalog | check the catalog first (see above) |
| Changes not visible / lost | no `CommitChanges()`, or model closed without saving | `CommitChanges()` at the end; tell the user to save |
| `PyNet Instance not found` | the user closed Tekla → PyNET exe exited | reopen Tekla, click a PyNET macro |
| `Non-whitelisted assembly: Tekla.Structures.Catalogs` | bridge older than the Catalogs whitelist entry | update the bridge |
| Passing a Python `list` where the API wants `Type[]` / `ArrayList` | no conversion | `Array[Type]([...])`; for `ArrayList` build it and `.Add()` |
| Confirmation before destructive scripts | — | `System.Windows.Forms.MessageBox.Show(..., MessageBoxButtons.YesNo, ...)` — see `01_Scripts/05_Tekla/01_Model/DeleteAllGeometry.py` |
