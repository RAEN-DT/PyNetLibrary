# Skill: RevitApiPatterns

Reference guide for Revit API patterns on the PyNET platform. Read this skill whenever writing any script that queries, iterates, or measures elements in a Revit model.

> **Used by:** [QuantityTakeoff.md](QuantityTakeoff.md) · [QCModelAudit.md](QCModelAudit.md)

---

## Rule #1 — Query types directly, never through instances

**Always use `WhereElementIsElementType()` to get element types.** Never iterate instances and jump to their type via `GetTypeId()`.

```python
# CORRECT — direct type query, one step, no duplicates
wall_types = (FilteredElementCollector(doc)
    .OfCategory(BuiltInCategory.OST_Walls)
    .WhereElementIsElementType()
    .ToElements())

# WRONG — iterates 1,000+ instances to extract 30 types; wasteful and fragile
instances = FilteredElementCollector(doc).OfCategory(...).WhereElementIsNotElementType().ToElements()
for el in instances:
    type_el = doc.GetElement(el.GetTypeId())  # DON'T DO THIS to collect types
```

**Why it matters:** a model with 1,241 wall instances may have only 69 wall types. Using `WhereElementIsElementType()` queries 69 objects directly — not 1,241. Using `GetTypeId()` on instances also produces duplicates that must be de-duped, adding unnecessary complexity.

**When to use instances (`WhereElementIsNotElementType()`):** only when you need instance-level data — geometry, location, level, or instance parameters. For type names, family names, or type parameters: always query types directly.

---

## Rule #2 — ElementId in Revit 2024+

Since Revit 2024 use `ElementId.Value` (Int64). `ElementId.IntegerValue` (Int32) was deprecated in 2024 and is gone in current versions.

```python
# CORRECT — works in Revit 2024+
type_id = int(type_el.Id.Value)

# WRONG — raises AttributeError on current Revit versions
type_id = type_el.Id.IntegerValue
```

For compatibility across versions:
```python
def eid_val(eid):
    try:
        return int(eid.Value)         # Revit 2024+
    except AttributeError:
        return int(eid.IntegerValue)  # older versions
```

---

## Getting parameters — old `BuiltInParameter` vs new `ForgeTypeId`

Revit 2024+ is migrating fixed parameter enums to `ForgeTypeId`-based identifiers (the same system
already used for units — `UnitTypeId`, `SpecTypeId`). Both access paths still work; prefer the new
one in scripts written from now on.

```python
# OLD — get_Parameter(BuiltInParameter....), still works, used throughout older example scripts
p = el.get_Parameter(BuiltInParameter.WALL_TOP_OFFSET)

# NEW — GetParameter(ParameterTypeId....), the ForgeTypeId-based equivalent
p = el.GetParameter(ParameterTypeId.WallTopOffset)
```

| | Old | New |
|---|---|---|
| Method | `element.get_Parameter(...)` | `element.GetParameter(...)` |
| Argument | `BuiltInParameter` enum member | `ForgeTypeId` from `ParameterTypeId` |
| Import | `from Autodesk.Revit.DB import BuiltInParameter` | `from Autodesk.Revit.DB import ParameterTypeId` |
| Status | Legacy, still functional | Current direction of the API |

The two spellings are not always 1:1 — check `ParameterTypeId` has a matching member before assuming
one exists (`Grep` `ParameterTypeId\.` in the stubs, or search the BIP name in
`02_PyNet Stubs/Autodesk/Revit/DB/__init__.py` for its `ForgeTypeId` counterpart). Both return the
same `Parameter` object — `.AsDouble()`, `.AsString()`, `.Set(...)`, `.HasValue` work identically
either way, so the choice only affects how you *look up* the parameter, not how you read/write it.

**For new scripts, default to the `ParameterTypeId` form.** The `BuiltInParameter` examples elsewhere
in this document reflect the existing script library and remain valid — don't rewrite working scripts
just to switch styles — but write new code with `GetParameter(ParameterTypeId....)`.

---

## `HasValue` — freezes `True` once a parameter has ever been set

`Parameter.HasValue` does **not** mean "currently has a non-empty value" — it means "this parameter
slot has been assigned at least once." If a script (or a user) sets a value and later clears it
(`param.Set("")`, `param.Set(0)`, or equivalent), `HasValue` stays `True` forever after — it does not
revert to `False`. This applies to parameters you create and populate yourself in the same script.

```python
p = el.GetParameter(ParameterTypeId.SomeTextParam)
p.Set("draft")
p.HasValue        # True

p.Set("")          # "clearing" it
p.HasValue        # still True — NOT False
p.AsString()      # "" (empty), which is what you actually need to check
```

**Never use `HasValue` alone to decide whether a parameter is meaningfully empty.** Check the actual
content instead — but see the note below before doing this for `Integer`/`Double` parameters:

```python
# WRONG — HasValue stays True even after the value was cleared
if p and p.HasValue:
    ...

# CORRECT for text — empty string is an unambiguous "no content"
if p and p.HasValue and (p.AsString() or "").strip():
# CORRECT for element references — InvalidElementId is unambiguous
if p and p.HasValue and p.AsElementId() != ElementId.InvalidElementId:
```

`HasValue` is still useful for its original purpose — telling apart a parameter that genuinely
doesn't exist / was never touched (`param is None`, or freshly created and untouched) from one the
script or model has assigned to at some point. It just isn't a stand-in for "is this currently blank."

### `Integer` / `Double` parameters: `0` is both "unset" and a valid value

Unlike text (`""`) or element references (`InvalidElementId`), a numeric parameter that was **never
set** also reads back as `0` via `AsInteger()` / `AsDouble()` — identical to a parameter someone
deliberately set to `0`. Combined with the `HasValue` freeze above, this means the "empty" signal on
a numeric parameter only exists for a single moment in its life:

> ✅ **Verified in-session** (brand-new shared parameter, bound to Walls, never assigned on any
> instance, tested inside a rolled-back transaction so nothing persisted): reading it fresh gave
> `HasValue = False`, `AsDouble() = 0.0`. The same parameter, immediately after any `Set(...)` call
> (including `Set(0.0)`), gave `HasValue = True`, `AsDouble() = 0.0` — indistinguishable from then on
> from a parameter someone deliberately zeroed out.

```python
p = el.GetParameter(ParameterTypeId.SomeCountParam)
p.AsDouble()   # 0.0 — could mean "never set" OR "explicitly set to 0"
```

**Practical rules:**
- `HasValue` **does** correctly tell apart "never set" (`False`) from "has a value" (`True`) — but
  only up to the *first* `Set(...)` call the parameter ever receives, from any source (a script, the
  user, a template). After that first write, `HasValue` is permanently `True` and the numeric value
  alone can no longer prove whether it's a real `0` or a leftover default.
- Don't use `p.AsDouble() != 0.0` (or `AsInteger() != 0`) as an "is this filled in" check — a
  legitimate zero value looks exactly like an empty one, and looks exactly like an untouched one too
  once `HasValue` has flipped to `True`.
- If a script needs to reliably tell "no data" apart from "zero" *after* the parameter may have been
  written to, don't rely on the numeric parameter alone — pair it with a boolean/text flag parameter
  that your own workflow controls.
- When reporting/aggregating numeric parameters (areas, counts, lengths), treat `0` at face value —
  don't try to filter out "unset" rows by value, since you cannot distinguish them from real zeros
  once the model has been touched.

---

## Getting family name and type name

```python
type_els = (FilteredElementCollector(doc)
    .OfCategory(BuiltInCategory.OST_Walls)
    .WhereElementIsElementType()
    .ToElements())

for t in type_els:
    type_name = t.Name or ""
    family_name = ""
    fp = t.get_Parameter(BuiltInParameter.ALL_MODEL_FAMILY_NAME)
    if fp:
        family_name = fp.AsString() or ""
    type_id = int(t.Id.Value)
```

---

## Counting instances per type

When you need both the type data and the instance count, query types first then build a count from instances:

```python
# Step 1: collect types
type_map = {}
for t in (FilteredElementCollector(doc)
        .OfCategory(bic)
        .WhereElementIsElementType()
        .ToElements()):
    type_map[int(t.Id.Value)] = {"name": t.Name, "count": 0}

# Step 2: count instances (only when count is needed)
for el in (FilteredElementCollector(doc)
        .OfCategory(bic)
        .WhereElementIsNotElementType()
        .ToElements()):
    tid = int(el.GetTypeId().Value)
    if tid in type_map:
        type_map[tid]["count"] += 1
```

---

## Area measurements by category

Areas come from built-in parameters. Internal units are **feet / square feet**.

> ⚠️ `WALL_ATTR_AREA_PARAM` does **NOT** exist in Revit 2024+. Walls are measured in ml via `CURVE_ELEM_LENGTH`, not m².

> **Always convert with `UnitUtils.ConvertFromInternalUnits`, never a hardcoded factor** (e.g. `* 0.3048`, `* 0.0929`).
> It's the API-sanctioned conversion — explicit about the target unit and safe against any future change to
> Revit's internal unit basis. Requires `from Autodesk.Revit.DB import UnitUtils, UnitTypeId`.

| Category | Unit | BuiltInParameter | UnitTypeId |
|---|---|---|---|
| Walls | ml | `CURVE_ELEM_LENGTH` | `UnitTypeId.Meters` |
| Floors | m² | `HOST_AREA_COMPUTED` | `UnitTypeId.SquareMeters` |
| Ceilings | m² | `HOST_AREA_COMPUTED` | `UnitTypeId.SquareMeters` |
| Roofs | m² | `HOST_AREA_COMPUTED` | `UnitTypeId.SquareMeters` |

```python
from Autodesk.Revit.DB import UnitUtils, UnitTypeId

# Wall length (ml)
p = el.get_Parameter(BuiltInParameter.CURVE_ELEM_LENGTH)
length_m = round(UnitUtils.ConvertFromInternalUnits(p.AsDouble(), UnitTypeId.Meters), 2) if p and p.HasValue else 0.0

# Floor / ceiling / roof area (m²)
p = el.get_Parameter(BuiltInParameter.HOST_AREA_COMPUTED)
area_m2 = round(UnitUtils.ConvertFromInternalUnits(p.AsDouble(), UnitTypeId.SquareMeters), 3) if p and p.HasValue else 0.0
```

To write a value back into internal units, use the inverse: `UnitUtils.ConvertToInternalUnits(value, unitTypeId)`.

**Note:** area parameters live on **instances**, not types. To get total area per type, iterate instances and accumulate.

---

## Count-based measurements

For doors, windows, luminaries, furniture, etc. — each instance counts as 1 unit. No parameter needed.

```python
# Count instances per type
instances = (FilteredElementCollector(doc)
    .OfCategory(BuiltInCategory.OST_Doors)
    .WhereElementIsNotElementType()
    .ToElements())

count_by_type = {}
for el in instances:
    tid = int(el.GetTypeId().Value)
    count_by_type[tid] = count_by_type.get(tid, 0) + 1
```

---

## Category → BuiltInCategory map (common)

```python
BIC_MAP = {
    "Muros":                  BuiltInCategory.OST_Walls,
    "Suelos":                 BuiltInCategory.OST_Floors,
    "Techos":                 BuiltInCategory.OST_Ceilings,
    "Cubiertas":              BuiltInCategory.OST_Roofs,
    "Puertas":                BuiltInCategory.OST_Doors,
    "Ventanas":               BuiltInCategory.OST_Windows,
    "Pilares estructurales":  BuiltInCategory.OST_StructuralColumns,
    "Armazón estructural":    BuiltInCategory.OST_StructuralFraming,
    "Luminarias":             BuiltInCategory.OST_LightingFixtures,
    "Aparatos sanitarios":    BuiltInCategory.OST_PlumbingFixtures,
    "Escaleras":              BuiltInCategory.OST_Stairs,
    "Barandillas":            BuiltInCategory.OST_Railings,
    "Mobiliario":             BuiltInCategory.OST_Furniture,
    "Equipos mecánicos":      BuiltInCategory.OST_MechanicalEquipment,
    "Conductos":              BuiltInCategory.OST_DuctCurves,
    "Tuberías":               BuiltInCategory.OST_PipeCurves,
}
```

---

## Reading / writing type parameters

```python
# Read a type parameter (string)
param = type_el.LookupParameter("MyParam")
val = param.AsString() if param and param.HasValue else ""

# Write a type parameter — requires transaction
t = Transaction(doc, "Set param")
t.Start()
try:
    param = type_el.LookupParameter("MyParam")
    if param and not param.IsReadOnly:
        param.Set("new_value")
    t.Commit()
except:
    t.RollBack()
    raise
```

---

## Exporting to Excel (openpyxl)

Hard-won rules — ignoring any of these turns a sub-second export into minutes, or produces a file Excel refuses to open ("Hemos encontrado un problema con el contenido…").

**1. NEVER auto-fit column widths with `ws.columns`.** It is the #1 performance trap: each access walks every cell of the sheet, so on a few thousand styled rows it takes *minutes* (measured: 210s on one audit). Just don't set widths — the user auto-fits with a double-click. If you really need widths, track the max length *while appending rows*, never via `ws.columns`.

```python
# WRONG — O(n²), can take minutes
for col in ws.columns:
    ws.column_dimensions[col[0].column_letter].width = min(max(len(str(c.value or '')) for c in col)+2, 60)

# RIGHT — don't set widths at all (user auto-fits), or track inline while appending
```

**2. Use a real Excel Table, and NEVER name it like a cell reference.** `displayName="T1"` corrupts the file silently — Excel reads `T1` as cell T1 and rejects the table. Use a name that can't be a cell reference (`Tabla_1`, `tbl_data`).

```python
from openpyxl.worksheet.table import Table, TableStyleInfo
ti = 0
for sec, rows in results.items():
    ws = wb.create_sheet(sec[:31])
    ws.append(['Check', 'Estado', 'Detalle', 'ElementId'])
    for r in rows:
        ws.append([r['Check'] or None, r['Estado'] or None, r['Detalle'] or None, r['ElementId'] or None])
    if rows:
        ti += 1
        tbl = Table(displayName=f'Tabla_{ti}', ref=f'A1:D{ws.max_row}')   # NOT f'T{ti}'
        tbl.tableStyleInfo = TableStyleInfo(name='TableStyleMedium2', showRowStripes=True)
        ws.add_table(tbl)
```

**3. Write empty values as `None`, never `''`.** An empty string becomes an invalid `<c t="inlineStr"></c>` cell (no `<is>`), which Excel flags as corrupt content. Coerce with `value or None` when appending.

**4. Debugging a "corrupt" xlsx:** an `.xlsx`/`.docx`/`.pptx` is just a **ZIP of XML**. Rename to `.zip` (or `unzip -l`) and inspect `xl/worksheets/sheet*.xml`, `xl/tables/table*.xml`, `[Content_Types].xml`. A sheet that is suddenly MBs in size = a runaway row count; check the table `ref` and the sheet `<dimension>`.

---

## Building a .NET `List[T]` — never pass a Python `list` to the constructor

In this platform's Python.NET runtime, `List[T](some_python_list)` **fails** — the constructor
overload that takes `IEnumerable<T>` does not accept a native Python `list`, even one containing
the right element type:

```python
# WRONG — raises: No method matches given arguments for List`1..ctor: (<class 'list'>)
categories = List[BuiltInCategory]([BuiltInCategory.OST_Walls, BuiltInCategory.OST_Doors])
ids = List[ElementId]([n.Id for n in collector])
```

**Always build it empty and populate with `.Add()`** — a fixed list or a loop over a comprehension:

```python
# CORRECT
categories = List[BuiltInCategory]()
categories.Add(BuiltInCategory.OST_Walls)
categories.Add(BuiltInCategory.OST_Doors)

ids = List[ElementId]()
for n in collector:
    ids.Add(n.Id)
```

Applies to any generic `List[T]` you build from a Python iterable — `ElementFilter`, `ElementId`,
`BuiltInCategory`, `System.Type`, etc. — not just Revit-specific types. Same constraint applies in
Navisworks scripts (see [navisworks.md](../../docs/navisworks.md)).

---

## Common pitfalls

| Symptom | Cause | Fix |
|---|---|---|
| 0 types found despite elements existing | Used `WhereElementIsNotElementType()` when querying types | Switch to `WhereElementIsElementType()` |
| `AttributeError: ElementId has no attribute IntegerValue` | Revit 2024+ | Use `eid.Value` |
| Area returns 0 | Parameter queried on type, not instance | Area BIPs live on instances |
| Hardcoded `* 0.3048` / `* 0.0929` conversion | Bypassing the API's own converter | Use `UnitUtils.ConvertFromInternalUnits(value, UnitTypeId.X)` |
| Type map empty after iteration | `GetTypeId()` returning null element | Always check `type_el is not None` |
| Excel export takes minutes | Auto-fitting widths via `ws.columns` | Don't set widths; user auto-fits |
| "Problema con el contenido" on open | Table `displayName` looks like a cell ref (`T1`) | Use `Tabla_1` / non-reference name |
| "Problema con el contenido" on open | Empty cells written as `''` (invalid `inlineStr`) | Write `value or None` |
| `No method matches given arguments for List\`1..ctor: (<class 'list'>)` | Passed a Python `list` to `List[T](...)` | Build empty `List[T]()` then `.Add()` each item |
| Using `get_Parameter(BuiltInParameter....)` in new code | Legacy access path, not wrong but outdated | Use `GetParameter(ParameterTypeId....)` for scripts written going forward |
| `HasValue` is `True` on a parameter you just cleared | `HasValue` freezes `True` once ever set — it doesn't revert on clear | Check the actual content (`AsString()`, `AsElementId()`) instead, not `HasValue` alone |
| Can't tell an "empty" numeric parameter from a real `0` | `Integer`/`Double` default to `0`; `HasValue` only proves "never set" *before* the first `Set(...)` — after that it's `True` forever | Don't filter numeric data by `!= 0`; use a separate flag parameter if "unset" must stay distinguishable post-write |

---

<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->
