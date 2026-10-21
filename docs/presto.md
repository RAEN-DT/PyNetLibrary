<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: RIB Presto scripts

Read this guide **before writing any Presto script**. For reading or modifying the budget, also read
[PrestoApiPatterns](../.claude/commands/PrestoApiPatterns.md). For forms/dialogs read
[winforms.md](winforms.md). Examples live in `01_Scripts/06_Presto/` — read the closest one first.

Related: [tekla.md](tekla.md) (the other out-of-process host) · [pythonnet.md](pythonnet.md)

> **Host detection:** Presto appears as **"Presto"** in `list_active_instances` (bridge with Presto
> support, from 2026-10); the PID is the PyNET exe's. Verified on **Presto 26.01**. The API is
> Presto's COM automation server, ProgID **`Presto.App.18`** (valid for every Presto from 18 on).
> There is no .NET API: the stubs in `02_PyNet Stubs/Presto/` are generated from Presto's type
> library (`presto.tlb`) by `01_Scripts/00_utils/GeneratePrestoStubs.py`, with RIB's own Spanish
> description of every member (modes, return codes). Look them up like any other stub
> ([stubs.md](stubs.md)): `Grep` `CLASSES.tsv` for `PrestoApplication`, then `Read` the range.
> Scripts never import them — `__presto__` is late bound.

> **Verification marks:** ✅ = run on Presto 26.01 through PyNET; ⏳ = written from the type library,
> the RIB technical notes or the Presto manual, not run yet. Treat ⏳ calls as guesses and check
> their result.

---

## How PyNET runs in Presto — out of process, through COM

Presto has no in-process add-ins. Its extensions (*complementos*) are separate programs listed in
Presto's **Complementos** menu. PyNET for Presto is one such program, **`Raen.Presto.Pynet.exe`**
(one exe for every Presto version), started from **Complementos > PyNET**
(`C:\Users\Public\Presto\26.01\API Plugins\PyNET`). It attaches to the running Presto through COM.
Consequences for scripts:

- **The Complementos menu exists only with exactly one obra open.** With no obra open, or with two,
  the menu is not shown: the user opens one obra and then starts PyNET.
- **Presto Demo has no Complementos directory**, so no menu: start PyNET from its Start-menu shortcut.
- Presto reads the Complementos list **only when it starts**: after installing PyNET, restart Presto.
- **The exe closes when Presto closes.** `PyNet Instance (PID …) not found` right after the user
  closed Presto is expected — reopen Presto, open the obra, start PyNET from Complementos.
- With **two obras open**, PyNET re-attaches before every script and follows the **active** obra
  (the one in the front window). Always check `app.Project()` before writing — see Rule #5 of
  PrestoApiPatterns.
- **Every call is a cross-process COM round trip.** All calls run on the exe's STA UI thread, one
  script at a time; while Presto is busy (a dialog open, a recalculation) the message filter retries
  a call for up to 30 s, then it fails. Reading 10,000 concepts × 5 fields is 50,000 round trips —
  read only the fields you need.
- No `clr.AddReference` is needed for the Presto API itself. `System.Windows.Forms` (dialogs) and
  `System` work as in every host.

---

## Standard boilerplate

The host injects **`__presto__`**: a Python proxy over the Presto COM application (the object RIB's
samples call `Obra`). Use the plain `try/except NameError` below — no fallback exists outside PyNET,
and `globals()` / `getattr` are blocked by the validator.

```python
# The host injects the Presto COM application (Presto.App.18) as __presto__
try:
    app = __presto__
except NameError:
    raise Exception("__presto__ not found: run this script from PyNET for Presto (Complementos > PyNET).")

if not app.Project():
    raise Exception("No obra is open in Presto: open one and run the script again.")
```

How the proxy works (✅):

| Need | Write | Notes |
|---|---|---|
| Call a method | `app.FindEqual("Conceptos", "Conceptos.Nat", 0)` | late-bound IDispatch by name, like VB `Obra.FindEqual …` |
| Read a parameterless property | `app.VersionStr()`, `app.Project()` | **properties are called like methods**, with `()` |
| Force a property get / put | `app._get("Name", *index)` / `app._set("Name", value)` | when a member is both, or for indexed properties |
| Raw COM object | `app._com.Target` | `System.__ComObject`; rarely needed |
| Wrong member name | raises `MissingMemberException` (`DISP_E_UNKNOWNNAME`) | check the spelling against the type library |
| Presto rejects a call | raises `COMException` with the HRESULT | |

Strings with accents (`"Conceptos.Código"`) pass through unchanged (✅). COM objects returned by
Presto are wrapped again, so the same style keeps working. By-ref/out parameters are not supported
by the proxy.

| | Revit | Tekla | Presto |
|---|---|---|---|
| Document | `__revit__.ActiveUIDocument.Document` | `__teklamodel__` (`Model`) | **`__presto__`** (COM app, the open obra) |
| API | .NET (`RevitAPI`) | .NET Open API | **COM automation**, late bound (`Presto.App.18`) |
| Runs | in process | separate exe (remoting) | **separate exe (COM)**, from the Complementos menu |
| Data model | elements + parameters | model objects + UDAs | **tables of records** (`Conceptos`, `Relaciones`…) with a cursor |
| Writes | Transaction | `CommitChanges()` | `SetField` + `UpdateRecord`, grouped by **`BeginRedo()`/`EndRedo()`** |
| Success value | exceptions | `bool` | **`0` = OK** for Find*/GetElement (non-zero = not found / end) |
| Saved by the script | no | no | no — the user saves the obra in Presto |
| Stubs / IntelliSense | yes | yes | yes — `02_PyNet Stubs/Presto/` (from `presto.tlb`, reference only, never imported) |

---

## Data model in one page

A Presto obra is a set of **tables**. Fields are always written `Table.Field`, with the Spanish
names and accents exactly as Presto shows them in the column tooltips (`Conceptos.Código`, not
`Conceptos.Codigo`).

| Table | One record is | Key fields | Useful fields |
|---|---|---|---|
| **`Conceptos`** | a concept: the root, a chapter, a partida, a basic price, an entity | `Código`, `Nat` | `Resumen` (summary) ✅, `Ud` (unit) ✅ read/write, `Pres` (budget price; on the root = obra budget) ✅ read (EvalNum, GetFieldNum) / write, `Obj` (target-cost price) ✅ read via EvalNum, `Fecha`, `Proveedor`, `Grupo` ⏳ |
| **`Relaciones`** | a parent → child link of the tree (the budget breakdown) | `CodSup`, `CodInf` | `CanPres` (budget quantity) ✅, `ImpPres` (amount = CanPres × Pres) ✅ read via GetFieldNum, `CanCert`/`ImpCert` (certified) ⏳, `CanObj`/`ImpObj` (target) ⏳, `Precio` (contract price) ⏳ |
| **`Mediciones`** | a measurement line of a partida (relation `CodSup` → `CodInf`) | walk with key **`Mediciones.Relación`** (or `Mediciones.Guid`) ✅ | `N`, `Longitud`, `Anchura`, `Altura` (columns A-D) ✅, `Cantidad` (computed by Presto, read only) ✅, `Pres` (1 = the line counts) ✅, `Comentario`, `GuidElem`, `CategoríaBIM`, `TipoBIM`, `FamiliaBIM`, `Planta`, `Cota`, `Área`, `Archivo`, `BIMLong`, `BIMVol`, `Nota`, `Origen` (3 = plugin) ✅ write — see [Measurement lines](#measurement-lines-and-bim-traceability-iso-19650) |
| `Obra` | the obra's own settings (one record) | `Código` | `DecCantMed` (decimals of line quantities) ✅ |
| `Precios` | price of a concept for one entity / contract | ⏳ | ⏳ |
| `Fases` | time-phased values (planning, certification periods) | ⏳ | ⏳ |

Prices live in `Conceptos`, quantities and amounts in `Relaciones` (the same concept can appear
under several parents with different quantities) — Presto manual. The root's `Pres` is the amount
of the whole budget.

### Natures (`Conceptos.Nat`)

| Nat | Concept | |
|---|---|---|
| 0 | Root (one per obra; code `"0"` in a new obra) | ✅ |
| 4 | Chapter (and sub-chapter) | ✅ |
| 5 | Partida (unit of work) | ✅ |
| 6 / 7 / 8 / 9 | Labour / material / machinery / other (basic prices) | ⏳ (manual) |
| 100+ | Entities (agents, suppliers…) | ✅ |
| 170 | `_CHG_` system concept | ✅ — filter it out of tree walks |
| 219 | `_SPC_` system concept | ✅ — filter it out of tree walks |
| 255 | system concept with code `###` (in every obra from the template) | ✅ seen, not in the tree |

In expressions and filters `Nat` is the number (`Conceptos.Nat == 5`); `%Conceptos.Nat == "Partida"`
compares the text form (manual). **Read numeric fields with `GetFieldNum`/`GetField` — `GetFieldStr`
returns `None` for them** (✅).

**Bulk reads in one COM call** (✅): `ReadTableByKey(0, "Conceptos", "Conceptos.Código",
"Conceptos.Código;Conceptos.Nat;Conceptos.Pres", "", False)` returns the whole table as JSON;
`ReadTableByKeyValue(0, table, key, value, fields, order, desc)` only the records whose key equals
`value` (e.g. `"Conceptos.Nat", 5` = every partida). **Fields are separated by `;`** — with commas
the call returns `None` without an error. See `01_Scripts/06_Presto/01_Read/ReadTableByKey.py`.

### Return codes

`FindEqual`, `GetElement` and the other navigation calls return **`0` when they found a record**
(and made it the current one), non-zero otherwise. Always compare with `== 0` / `!= 0` — never use
the value as a Python truth value (`if app.FindEqual(...):` means *not found*).

---

## Writes: the record cursor, `BeginRedo`/`EndRedo`, `Recalculate`

There are no objects to modify: you make a record **current** (Find*, SetElement/GetElement,
InitRecord), change its fields with `SetField`, and commit the record with `UpdateRecord(table)`
(existing) or `InsertRecord(table)` (new). The full pattern is in PrestoApiPatterns and in
`01_Scripts/06_Presto/02_Write/CreateBudgetFromJson.py` (✅).

```python
app.BeginRedo()                     # one undo step for the whole script
try:
    if app.FindEqual("Conceptos", "Conceptos.Código", "01") == 0:
        app.SetField("Conceptos.Resumen", "Structure")
        app.UpdateRecord("Conceptos")
finally:
    app.EndRedo()                   # ALWAYS: BeginRedo without EndRedo leaves Presto's undo blocked
app.Recalculate(1)                  # recompute amounts
app.UpdateScreen()                  # refresh Presto's windows
```

- **Check the obra first.** `app.Project()` is the full path of the active obra. Compare it with
  the expected one and/or ask with a `MessageBox` (YesNo) before writing — see
  `CreateBudgetFromJson.py`. With two obras open, the active one is the target.
- **Changes go into the open obra and are not saved by the script.** Tell the user to save the obra
  in Presto; closing without saving discards them. (⏳ The type library has no `Save` method;
  Presto writes unsaved changes to a `.PrestoRecover` file next to the obra in real time — manual.)
- Destructive scripts: dry run by default (`DRY_RUN = True`, list the changes in `ia_Result`),
  confirmation dialog, then write — `02_Write/NormalizeSummaries.py`.

---

## Measurement lines and BIM traceability (ISO 19650)

A partida's quantity can be the sum of **measurement lines** (table `Mediciones`), one per model
element. Writing the element's **IFC GlobalId** in `GuidElem` links every budget quantity to the
model and to the IFC exported from it — the traceability ISO 19650 asks for. Verified on
Presto 26.01 with 570 lines from a Tekla model (✅ unless marked):

| Field | Meaning (Presto's field dictionary `Data\LNG\Presto8.lng`) | Write |
|---|---|---|
| `CodSup`, `CodInf` | the relation (parent → partida) the line belongs to | text, required |
| `N`, `Longitud`, `Anchura`, `Altura` | columns A-D; `Cantidad` = their product, **an unset column is left out** | numbers |
| `Cantidad` | the line quantity — **computed by Presto**, read it, don't write it | — |
| `Pres` | `1` = the line counts in the partida | (default) |
| `GuidElem` / `GuidAux` | unique id of the element in the model / tells apart several lines of one element; `Guid` = `GuidElem` + `GuidAux` (padded) | text |
| `CategoríaBIM`, `TipoBIM`, `FamiliaBIM` | IFC class, type, family | text |
| `Planta`, `Cota` | `IfcBuildingStorey` name, storey elevation (m) | text, number |
| `Área` / `Zona` / `Elemento` | `IfcBuilding` (or site) / `IfcSpace` / IFC UniqueID | text (⏳ `Zona`, `Elemento`) |
| `Archivo`, `BIMLong`, `BIMSup`, `BIMVol`, `Nota`, `Comentario` | source file, model length / area / volume, user note, line text | text / numbers (⏳ `BIMSup`: written by WriteMeasurementLinesFromJson.py, not read back yet) |
| `Origen` | `3` = plugin | number |

```python
def q(t):
    return '"' + t + '"'

flt = "Mediciones.CodSup==" + q(sup) + " && Mediciones.CodInf==" + q(code)

# 1. decimals BEFORE inserting (default 2 rounds lines to cm / 0.01 m3; inserted lines keep it)
app.FindFirst("Obra", "Obra.Código")
app.SetField("Obra.DecCantMed", 3)
app.UpdateRecord("Obra")
app.FindEqual("Conceptos", "Conceptos.Código", code)
app.SetField("Conceptos.RedParc", 3)                  # per partida, dimension columns
app.UpdateRecord("Conceptos")

# 2. delete the partida's lines: restart the set after every delete
while True:
    app.SetElement(8, "Mediciones", "Mediciones.Relación", '"*"', flt)
    if app.GetElement(8) != 0:
        break
    app.DeleteRecord("Mediciones", 0)

# 3. insert one line per element
app.InitRecord("Mediciones")
app.SetField("Mediciones.CodSup", sup)
app.SetField("Mediciones.CodInf", code)
app.SetField("Mediciones.N", 1.0)
app.SetField("Mediciones.Longitud", 14.4)             # Anchura / Altura only if used
app.SetField("Mediciones.GuidElem", "2GjM2A44nD09l18W1Y9Grj")
app.SetField("Mediciones.CategoríaBIM", "IfcColumn")
app.SetField("Mediciones.Origen", 3)
app.InsertRecord("Mediciones")

# 4. read the lines back and sync the partida quantity (NOT recomputed for API lines)
total = 0.0
app.SetElement(8, "Mediciones", "Mediciones.Relación", '"*"', flt)
while app.GetElement(8) == 0:
    total += app.GetFieldNum("Mediciones.Cantidad") or 0.0
app.SetElement(9, "Relaciones", "Relaciones.CodSup", q(sup), "Relaciones.CodInf==" + q(code))
if app.GetElement(9) == 0:
    app.SetField("Relaciones.CanPres", total)
    app.UpdateRecord("Relaciones")
```

- **Find the parent of the partida in the obra**, not in your JSON: a partida may have been moved
  (e.g. by `ClassifyCypeChapters.py`). `SetElement(9, "Relaciones", "Relaciones.CodSup", '"*"',
  'Relaciones.CodInf=="01.01"')` lists every parent; normally one.
- Wrap 2-4 in `BeginRedo`/`EndRedo` and finish with `Recalculate(1)` + `UpdateScreen()`.

Scripts (⏳ as wholes, built from the ✅ pieces above), in workflow order:

| Script | Host | Does |
|---|---|---|
| `01_Scripts/05_Tekla/06_Export/ExportTakeoffForPresto.py` | Tekla | JSON takeoff, one line per part with its IFC GlobalId (run on Tekla 2026: 570 parts, totals checked) |
| `01_Scripts/02_Revit/26_5D/ExportTakeoffForPresto.py` | Revit | same JSON: one line per element, `IfcGUID` parameter or `ExportUtils.GetExportId` compressed; category → IFC class, level, m2/m3/m/u per category (✅ run on Revit 2025: 84 elements, 33 partidas, GUIDs from `IfcGUID`) |
| `01_Scripts/04_Rhino/07_Export/ExportTakeoffForPresto.py` | Rhino | same JSON: closed solids m3, surfaces m2, curves m, blocks u; IFC GUID from user text or the object Id; IFC class from user text / layer map; units scaled to metres (✅ run on Rhino 8: 238 solids; units = the Rhino document's, stops if the geometry does not fit them) |
| `01_Scripts/01_Navisworks/05_QueryElements/ExportTakeoffForPresto.py` | Navisworks | same JSON for **federated** models: per element the GUID / IFC class / quantities / storey of its source format (IFC, Revit, Tekla), configurable property lookup lists (⏳ not run) |
| `01_Scripts/03_AutoCAD/16_Quantities/ExportTakeoffForPresto.py` | Civil 3D | same JSON for infrastructure: corridor shape volumes by code (average end area, lines per station interval), volume surfaces cut/fill, pipes m / structures u, entities by layer; GuidElem = IFC-compressed uuid5 of drawing + handle (DWG objects have no IFC GlobalId) (⏳ not run) |
| `01_Scripts/06_Presto/02_Write/CreateBudgetFromJson.py` | Presto | ✅ chapters and partidas from the same JSON |
| `01_Scripts/06_Presto/02_Write/WriteMeasurementLinesFromJson.py` | Presto | ✅ the lines, decimals, CanPres sync, read-back checks (570 lines / 12 partidas on a blank obra, ~60 s) |
| `01_Scripts/06_Presto/01_Read/ReadMeasurementLines.py` | Presto | traceability check: lines vs CanPres, missing / duplicated `GuidElem`, per storey / IFC class, CSV/Excel (run on Presto 26.01: 570 lines, 10 partidas) |

---

## Output and dialogs

- `print` goes to the PyNET output window; `ia_Result` returns data to the AI, as in every host.
- `System.Windows.Forms.MessageBox` works for confirmations (✅). The dialog has no owner window, so
  it may open behind Presto (✅ seen 2026-10-20): `send_command` then times out while it waits, and
  the script still finishes after the user clicks.
- Presto's own message window: `LogBegin(title)`, `LogMsg(text, mode)` (mode 0 black, 1 blue, 2 red —
  RIB VBS tutorial), `LogEnd()` ⏳. RIB notes the messages appear all together at the end of the run.
- Files: `Environment.GetFolderPath(Environment.SpecialFolder.Desktop)` for the Desktop (OneDrive
  redirects it), `pathlib.Path`, never `os.path`.

---

## The Python.NET runtime is persistent

Same as the other hosts: the runtime lives as long as the PyNET exe (until Presto closes). A failed
import can leave a broken module in `sys.modules`; if a button fails but the same script works
through `send_command`, ask the user to restart Presto.

---

## Gotchas (verified on Presto 26.01)

| Situation | What happens | Do this |
|---|---|---|
| No Complementos menu | 0 or 2+ obras open, or Presto Demo | open exactly one obra; Demo: Start-menu shortcut |
| PyNET missing from Complementos after install | menu read only at Presto start | restart Presto |
| `app.VersionStr` without `()` | returns the bound member, not the value | call every member: `app.VersionStr()` |
| `MissingMemberException` / `DISP_E_UNKNOWNNAME` | wrong member name | check the type library list (PrestoApiPatterns) |
| `GetFieldStr("Conceptos.Nat")` is `None` | numeric field | `GetFieldNum` / `GetField` |
| `EvalNum` gives 2 decimals | it rounds | `GetFieldNum` for prices/quantities with more decimals |
| `if app.FindEqual(...):` "works backwards" | `0` = found | compare with `== 0` |
| `COMException RPC_E_SERVERFAULT` | stale COM object with 2 obras open (fixed: PyNET re-attaches before each script); also seen once on `New(path)` | close the extra obra; avoid `New` (⏳) |
| Script wrote into the wrong obra | 2 obras open, the other one was active | check `app.Project()` before writing |
| Changes lost | obra closed without saving | tell the user to save in Presto |
| `PyNet Instance not found` | Presto closed → PyNET exited | reopen Presto + obra, Complementos > PyNET |
| `SetElement(…, "Mediciones", "Mediciones.CodSup" / "CodInf" / "Id" / "GuidElem" / "Planta", …)` returns 1 | not a key of `Mediciones` | key **`Mediciones.Relación`** (or `Mediciones.Guid`), mask `'"*"'`, filter on `CodSup`/`CodInf` |
| `FindFirst/FindNext("Mediciones", …)` return 1, the "line" read is empty / always the same | they don't move on `Mediciones`: you read the `InitRecord` buffer | walk with `SetElement`/`GetElement`; `EvalStr`/`EvalNum` on `Mediciones[...]` return empty too |
| Lines rounded to cm / 0.01 m³ | `Obra.DecCantMed` and `Conceptos.RedParc` default 2 | set them to 3 **before** inserting; delete + reinsert lines already written |
| Partida quantity ≠ sum of its lines after writing lines | `Relaciones.CanPres` is not recomputed from API-written lines (neither `Recalculate(1)` nor `Calculate(3)`) | sum `Mediciones.Cantidad` and set `CanPres` + `UpdateRecord` |
| A `MessageBox` script "hangs", `send_command` times out | the box opened behind Presto and waits; the script finishes after the click | look for the PyNET dialog behind Presto / in the taskbar |
