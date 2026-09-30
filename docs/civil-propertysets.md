<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: Property Sets (Civil 3D / AutoCAD)

Read [autocad-civil.md](autocad-civil.md) first — boilerplate, write pattern and the three API misuses that abort the host apply here too.

---

## Property Sets (Civil 3D / AutoCAD) — the Revit shared-parameter equivalent

| Revit | Civil 3D / AutoCAD |
|---|---|
| Shared parameter (definition) | `PropertyDefinition` |
| Parameter group | `PropertySetDefinition` |
| Category (`OST_Walls`…) | **no equivalent** — closest is the .NET object type, or the layer |
| Type vs Instance | **no equivalent** — every value lives on the instance |
| Parameter group in the UI | **no equivalent** — a PSet shows as one flat tab |

Definitions live **in the DWG**, in the `AEC_PROPERTY_SET_DEFS` dictionary of the
`NamedObjectsDictionary` — not in an external shared file like Revit's `.txt`. To share them between
drawings, copy them by script or start from a DWT that already has them.

**Attachment.** There is no native "bind to layer". Two mechanisms:

1. **By object type** — `PropertySetDefinition.AppliesToFilter`, the closest thing to a Revit category.
2. **Manually per entity** — `PropertyDataServices.AddPropertySet(entity, psetDefId)`. Setting
   `AppliesToAll = True` removes the type restriction, so the script's own criterion (e.g. the entity's
   `Layer`) decides what gets tagged. Attachment is per-PSet, never per-property.

Layer-driven attachment is therefore a **scan we implement**: walk ModelSpace, read `entity.Layer`,
attach the PSets that the matrix marks for that layer. It is not automatic — new geometry needs a re-run.

Reference script: `01_Scripts/03_AutoCAD/00_Workflow/CreateParameters.py` (Excel matrix → PSets →
layers → attachment, re-runnable). Two gotchas it encodes:

- **`PropertyDefinition.DefaultData` for `DataType.Integer` needs an explicit `System.Int32`.** A plain
  Python `int` bridges as `Int64` and the setter rejects it with
  `Value does not fall within the expected range. (Parameter 'defaultData')`. `Text`, `Real` and
  `TrueFalse` take `""`, `0.0` and `False` directly. (Live-verified enum members:
  `Integer, Real, Text, TrueFalse, AutoIncrement, AlphaIncrement, List, Graphic` — note it is
  `TrueFalse`, not `TrueFalseType`.)
- **`PropertyDataServices.GetPropertySet()` throws `eKeyNotFound` — it does not return a null
  `ObjectId` — whenever that PSet is not attached.** Checking `entity.ExtensionDictionary.IsNull` first
  is not enough: attaching the first of several PSets creates the dictionary, and the check for the
  second one then throws (verified live). Skip when there is no `ExtensionDictionary`, and otherwise wrap
  the call in `try/except` treating `ErrorStatus.KeyNotFound` as "not attached".
