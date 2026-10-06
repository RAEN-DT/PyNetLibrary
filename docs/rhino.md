<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: Rhino scripts

Read this guide **before writing any Rhino script**. For object queries/measurements, also read [RhinoApiPatterns](../.claude/commands/RhinoApiPatterns.md). For forms/dialogs read [winforms.md](winforms.md).
Validated examples live in `01_Scripts/04_Rhino/` (layers, blocks, objects and user text, layouts,
geometry stats) — read the closest one first.

Related: [autocad-civil.md](autocad-civil.md) · [pythonnet.md](pythonnet.md) · [stubs.md](stubs.md)

> **Host detection:** Rhino appears as **"Rhino"** in `list_active_instances` (bridge >= 1.5.6).
> Rhino 7, 8 and 9 are supported; the API is RhinoCommon.

---

## Standard boilerplate

The plugin injects a `__rhinodoc__` global (a `Rhino.RhinoDoc`, what RhinoPython exposes as
`scriptcontext.doc`). **Do not rely on `rhinoscriptsyntax` / `scriptcontext` — PyNET is not Rhino's
script editor;** call RhinoCommon directly. You cannot probe for `__rhinodoc__` with `globals()` /
`getattr` (blocked by the validator): use the plain `try/except NameError` below.

Import **only the types the script uses**, by name — never `from Rhino.Geometry import *` (same
rule and reasons as [navisworks.md](navisworks.md#-never-use-from-namespace-import-)). Check an
uncertain name against the stubs index (`CLASSES.tsv`, `namespace` column `Rhino.*`; stubs in
`02_PyNet Stubs/Rhino/` and `02_PyNet Stubs/Eto/`) before importing it: `Point3d`, `Plane`,
`Vector3d` also exist in the Autodesk namespaces. `System.Drawing.Color` imports without an extra
`AddReference`.

```python
import clr
from pathlib import Path

clr.AddReference("RhinoCommon")
from Rhino import RhinoDoc
from Rhino.DocObjects import Layer, ObjectType   # what you use
from Rhino.Geometry import Point3d, Transform   # what you use

# __rhinodoc__ is injected by the plugin — always use this to get the document
try:
    doc = __rhinodoc__
except NameError:
    doc = RhinoDoc.ActiveDoc
```

| | Revit | Rhino |
|---|---|---|
| Document | `__revit__.ActiveUIDocument.Document` | `__rhinodoc__` |
| Main assembly | `RevitAPI` | `RhinoCommon` |
| UI access | `__revit__.ActiveUIDocument` | `doc.Views` (`ActiveView`, `Redraw()`) |
| Writes need transaction | **Yes** | No — **undo record** instead |
| Property data | Parameters | Attribute User Text (strings) |

### Document essentials

| Need | Call |
|---|---|
| Units / tolerances | `doc.ModelUnitSystem` (e.g. `Millimeters`), `doc.ModelAbsoluteTolerance`, `doc.ModelAngleToleranceRadians` |
| Layers | `doc.Layers` — `FindByFullPath("A::B", -1)` → index or `-1`, `FindIndex(i)`, `CurrentLayerIndex` |
| Objects | `doc.Objects` — `FindByLayer`, `FindByObjectType`, `FindByUserString`, `GetObjectList(ObjectEnumeratorSettings)` |
| Blocks | `doc.InstanceDefinitions` — `Find(name, True)`, `Add(...)`; instances via `doc.Objects.AddInstanceObject(idef.Index, xform, attrs)` |
| Layouts | `doc.Views.GetPageViews()` (`RhinoPageView`); model views: `GetStandardRhinoViews()` |
| Default attributes | `doc.CreateDefaultAttributes()` (current layer), then set `LayerIndex` etc. |

Layer paths use `::` as separator (`Layer.FullPath`). Colors are `System.Drawing.Color`.

---

> **PyNET install / form icon:** never hardcode the Rhino version or the install path — resolve them
> from the running `Raen.Core.Pynet.Engine`. Rhino has no `.bundle`: the engine lives in
> `<install>/Rhino <N>/` and the icon at the install root, so `PYNET_BIN.parent / "Pynet.ico"`
> (not `PYNET_BIN.parent.parent`). See [winforms.md](winforms.md) "Form icon".

## Undo records (required for any write)

Rhino has no transactions or document lock, and PyNET scripts run outside a Rhino command, so they
get **no automatic undo record**. Wrap every change in one so Ctrl+Z reverts the whole script step,
and redraw at the end:

```python
sn = doc.BeginUndoRecord("PyNET: <what the script does>")
try:
    # ... write operations ...
finally:
    doc.EndUndoRecord(sn)
doc.Views.Redraw()
```

- **Layers** from the table are live: set properties, then `layer.CommitChanges()`. The current layer
  and layers that still hold objects cannot be deleted (`Layers.Delete` returns `False`).
- **Object attributes:** `attrs = obj.Attributes.Duplicate()`, change it, then
  `doc.Objects.ModifyAttributes(obj, attrs, True)` — this is what records undo and notifies the
  document; do not edit `obj.Attributes` in place.
- **Transforms**: compose with `Transform.Multiply(a, b)` (applies `b` first), e.g. translation ×
  rotation (`Transform.Rotation(rad, Vector3d.ZAxis, Point3d.Origin)`) × `Transform.Scale(Point3d.Origin, s)`.

## Special folder paths

Never hardcode `Path.home() / "Desktop"` — it fails when OneDrive redirects the Desktop. Use .NET:

```python
from System import Environment
desktop = Environment.GetFolderPath(Environment.SpecialFolder.Desktop)
out_path = Path(desktop) / "output.csv"
```

## Iterating objects and tables

`for obj in doc.Objects` and `FindByObjectType` skip some hidden/locked objects. For a full
inventory use `ObjectEnumeratorSettings`:

```python
from Rhino.DocObjects import ObjectEnumeratorSettings, ObjectType

settings = ObjectEnumeratorSettings()
settings.HiddenObjects = True
settings.LockedObjects = True
settings.ObjectTypeFilter = ObjectType.AnyObject
for obj in doc.Objects.GetObjectList(settings):
    ...
```

Tables (`doc.Layers`, `doc.InstanceDefinitions`) keep deleted entries in their slot — `Count` does
not drop:

```python
for layer in doc.Layers:
    if layer is None or layer.IsDeleted:
        continue  # skip deleted slots
    ...
```

## User text — Rhino's property sets

Rhino's equivalent of AutoCAD property sets / Revit shared parameters is **Attribute User Text**:
free string key/value pairs on each object's attributes (no schema, every value is a string).

- Read: `obj.Attributes.GetUserStrings()` → `NameValueCollection` (`nvc.AllKeys`, `nvc[key]`), or
  `GetUserString(key)` (returns `None` when missing). `UserStringCount` is a cheap pre-check.
- Write: `SetUserString(key, value)` on a duplicated attributes object (see above); remove with
  `DeleteUserString(key)`.
- Search: `doc.Objects.FindByUserString(key, value, caseSensitive, searchGeometry, searchAttributes,
  ObjectType.AnyObject)` — value accepts wildcards (`"OBRA_*"`). May return `None` or an empty array
  when nothing matches — normalise with `or []`.
- `SetUserString(key, "")` **deletes** the key — there is no empty value (see RhinoApiPatterns).
- Layers and block definitions carry their own user strings (`Layer.GetUserStrings()`); document-level
  text is `doc.Strings`.

## Geometry measurement

`AreaMassProperties.Compute(geom)` / `VolumeMassProperties.Compute(geom)` accept `Brep` and `Mesh`.
Convert `Extrusion` first (`extrusion.ToBrep(True)`), compute volume only for closed geometry
(`brep.IsSolid`, `mesh.IsClosed`). This is slow on large models (~22 s for 254 Breps) — print progress
every ~10 %. Bounding box: `geom.GetBoundingBox(True)`.

## Gotchas (verified in Rhino 8, CPython 3 + pythonnet)

| Situation | What happens | Do this |
|---|---|---|
| Passing a Python list where RhinoCommon expects `IEnumerable<T>` | no conversion, "No method matches" | build `System.Collections.Generic.List[T]` and `.Add()` items |
| Random numbers | `random` is not whitelisted | `System.Random` |
| Layer / display-mode / view names | **localized** (Spanish Rhino: `Predeterminado`, `Perspectiva`) | never hardcode `Default` / `Perspective`; use `CurrentLayerIndex`, `ActiveView`, or indices |
| Stubs show one overload | the generator keeps a single signature | e.g. `Layers.FindByFullPath(path, -1)` is the int (not-found value) overload; check with `clr.GetClrType(T).GetMethods()` |
| Zoom to objects | — | `view.ActiveViewport.ZoomBoundingBox(bbox)` on `doc.Views.ActiveView`, then `doc.Views.Redraw()` |

---

## The Python.NET runtime is persistent

The Python runtime inside Rhino is **persistent and shared** across all executions (`send_command` and
buttons). A failed import can leave a broken module in `sys.modules` that affects every later script in
the session.

**Diagnosing a button that fails:**

1. **Does the same script work via `send_command`?** If yes, the script is correct — the session state
   is the problem; ask the user to restart Rhino.
2. **Import error on a type name?** Check the name and namespace in the stubs index — it may differ
   between Rhino 7, 8 and 9, or exist under an Autodesk namespace too (see the boilerplate note above).
