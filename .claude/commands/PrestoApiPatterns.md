# Skill: PrestoApiPatterns

Reference guide for RIB Presto COM API patterns on the PyNET platform. Read this skill whenever
writing any script that reads, walks, exports or modifies a Presto obra. Read
[docs/presto.md](../../docs/presto.md) first for the boilerplate (`__presto__`), the data model
(tables, `Nat` codes), how PyNET runs out of process and the Complementos menu rules.

> Verified on Presto 26.01 (CPython 3 + pythonnet, through PyNET's `__presto__` proxy) where marked
> ✅. ⏳ = written from the 26.01 type library, the RIB technical notes ("API: Desarrollo de
> complementos", VBS tutorial) or the Presto manual — not yet run in a session. Treat ⏳ calls as
> guesses: check their return value and read the result back. Examples: `01_Scripts/06_Presto/`.
>
> Exact signatures, optional parameters and RIB's own description of every member (modes, return
> codes) are in the stubs: `02_PyNet Stubs/Presto/__init__.py`, class `PrestoApplication` (generated
> from `presto.tlb`). Notes below quoted "tlb:" come from those descriptions — documented by RIB,
> but still ⏳ until run.

---

## Rule #1 — Presto is a record cursor, not an object model

There are no concept objects. Every call works on the **current record** of a table:

- `FindEqual(table, key, value)` (and the other Find*) **makes the found record current**.
- `GetFieldStr` / `GetFieldNum` / `GetField` / `EvalNum` read **the current record**.
- `SetField(field, value)` changes the current record in memory; **`UpdateRecord(table)`** commits it.
- New record: `InitRecord(table)` → `SetField` the key fields → `InsertRecord(table)` → **find it
  again** to make it current before setting more fields.

```python
# CORRECT (✅) - create the concept if missing, re-find it, then write its fields
if app.FindEqual("Conceptos", "Conceptos.Código", code) != 0:
    app.InitRecord("Conceptos")
    app.SetField("Conceptos.Código", code)
    app.InsertRecord("Conceptos")
    if app.FindEqual("Conceptos", "Conceptos.Código", code) != 0:
        raise Exception("Could not create " + code)
app.SetField("Conceptos.Nat", 5)
app.SetField("Conceptos.Resumen", "Brick wall 140 mm")
app.SetField("Conceptos.Ud", "m2")
app.UpdateRecord("Conceptos")

# WRONG - SetField after another Find* writes into whatever record that Find made current
app.FindEqual("Conceptos", "Conceptos.Código", "01")
app.FindEqual("Conceptos", "Conceptos.Nat", 0)        # cursor moved to the root
app.SetField("Conceptos.Resumen", "Walls")            # renames the ROOT
```

**Return codes: `0` = found / OK, non-zero = not found / end of the loop** (✅ for `FindEqual`,
`GetElement`). Always compare explicitly: `== 0`, `!= 0`.

Relations work the same way (✅):

```python
app.InitRecord("Relaciones")
app.SetField("Relaciones.CodSup", "01")
app.SetField("Relaciones.CodInf", "01.001")
app.InsertRecord("Relaciones")
# make it current (SetElement/GetElement on a free slot), then the quantity
app.SetElement(9, "Relaciones", "Relaciones.CodSup", '"01"', 'Relaciones.CodInf=="01.001"')
if app.GetElement(9) == 0:
    app.SetField("Relaciones.CanPres", 125.6)
    app.UpdateRecord("Relaciones")
```

---

## Rule #2 — Walk a table with `SetElement`/`GetElement`, one slot per nesting level

`SetElement(slot, table, key, mask, filter)` opens a set of records on a numbered **element slot**
(the "Elemento 1, 2…" sections of Presto reports); `GetElement(slot)` moves to the next one and
returns `0` while there are records (✅). The type library also has `ordenar_por, orden` (sort) as
6th/7th arguments ⏳.

- **mask**: applies to the key and **must include the double quotes**: `'"' + code + '"'` for an
  exact value, `'"*"'` for all, `'"01*"'` for codes starting with `01` (RIB VBS tutorial ⏳ for `*`).
- **filter**: any Presto expression on that table (`"Conceptos.Nat == 5 && Conceptos.Pres > 0"`),
  or `""`.
- A `Relaciones` element also exposes the **child concept's** fields: `GetFieldStr("Conceptos.Resumen")`
  inside a relation loop is the `CodInf` concept's summary (✅, RIB sample).
- **Nested loops need different slots** — slot 1 for the chapters, slot 2 for their children, …
  (✅, RIB "Recorrer 4 niveles" sample). Reusing the slot of an outer loop restarts it. Slots seen:
  1..9; keep 9 for one-off lookups.
- **Read every field of the current record before descending**: the inner loop moves the cursor.

```python
FILTER = "Conceptos.Nat!=219 && Conceptos.Nat!=170"     # skip _SPC_ and _CHG_ system concepts

def walk(sup, depth):
    app.SetElement(depth, "Relaciones", "Relaciones.CodSup", '"' + sup + '"', FILTER)
    while app.GetElement(depth) == 0:
        code = app.GetFieldStr("Relaciones.CodInf")
        nat = int(app.GetFieldNum("Conceptos.Nat") or 0)
        qty = app.GetFieldNum("Relaciones.CanPres")
        print("    " * depth + code, nat, app.GetFieldStr("Conceptos.Resumen"), qty)
        if nat == 4 and depth < 8:                       # chapters only
            walk(code, depth + 1)

app.FindEqual("Conceptos", "Conceptos.Nat", 0)           # the root
walk(app.GetFieldStr("Conceptos.Código"), 1)
```

RIB's sample starts the walk from the code `"###"`; walking from the root's own code (found with
`Nat == 0`, `"0"` in a new obra) is what PyNET's scripts use (✅).

---

## Rule #3 — Numbers with `GetFieldNum`, text with `GetFieldStr`

| Field kind | Read with | Notes |
|---|---|---|
| Text (`Código`, `Resumen`, `Ud`, `CodSup`, `CodInf`) | `GetFieldStr(field)` ✅ | `None` / `""` when empty |
| Numeric (`Nat`, `CanPres`, `Pres`…) | `GetFieldNum(field)` ✅ or `GetField(field)` ✅ | **`GetFieldStr` returns `None` for them** ✅ |
| An expression on the current record | `EvalNum(expr)` ✅ / `EvalStr(expr)` ⏳ | **`EvalNum` rounds to 2 decimals** ✅ |

`GetField*` take an optional `dimension` 2nd argument (type library) ⏳ — omit it.
`EvalNum("Conceptos.Pres")` on the root is the obra budget, `"Conceptos.Obj"` the target cost (✅).
`EvalNum("Conceptos[Nat==0].Pres")` (an expression that picks the root without moving the cursor)
was used in one test script ⏳.

---

## Rule #4 — Group every write in `BeginRedo()` / `EndRedo()`, then recalculate

```python
app.BeginRedo()
try:
    ...                       # all SetField / InsertRecord / UpdateRecord
finally:
    app.EndRedo()             # a BeginRedo without EndRedo leaves Presto's undo blocked (RIB)
app.Recalculate(1)            # amounts, chapter totals
app.UpdateScreen()            # refresh the windows
```

One `BeginRedo`/`EndRedo` pair per script = one undo step for the user (✅). `Recalculate(1)` +
`UpdateScreen()` after the writes (✅). `Calculate(mode)` ⏳, `SetUpdateScreen(0/1)` to freeze the
screen during long writes ⏳.

---

## Rule #5 — Check the target obra before writing, and say it is not saved

- `app.Project()` (✅) is the full path of the **active** obra. With two obras open PyNET follows the
  active one — the user may be looking at the other. Compare with an `EXPECTED_PROJECT` constant
  and/or confirm with a `MessageBox` YesNo that names the obra (see `CreateBudgetFromJson.py`).
- Refuse to overwrite existing content unless a flag says so: check the codes you will create with
  `FindEqual` first.
- `ReadOnly()` ⏳ (an int in the COM API) — check it before writing if you rely on it.
- **The script does not save the obra.** Tell the user to save it in Presto. ⏳ There is no `Save`
  method in the type library.

---

## Rule #6 — Measurement lines (`Mediciones`): walk by `Relación`, set decimals first, sync `CanPres`

One line per model element, with its IFC GlobalId in `GuidElem`, gives the ISO 19650 link between
the budget and the model. All ✅ on Presto 26.01 (570 lines written, read back, deleted, rewritten).
Field meanings and the full flow: [docs/presto.md → Measurement lines](../../docs/presto.md#measurement-lines-and-bim-traceability-iso-19650).

```python
flt = 'Mediciones.CodSup=="' + sup + '" && Mediciones.CodInf=="' + code + '"'

# walk the lines of one relation: key Mediciones.Relación (or Mediciones.Guid), mask "*"
app.SetElement(8, "Mediciones", "Mediciones.Relación", '"*"', flt)
while app.GetElement(8) == 0:
    guid = app.GetFieldStr("Mediciones.GuidElem")
    qty = app.GetFieldNum("Mediciones.Cantidad")      # computed by Presto: read, never write

# decimals BEFORE inserting (default 2: lines rounded to cm / 0.01 m3, and they stay rounded)
app.FindFirst("Obra", "Obra.Código")
app.SetField("Obra.DecCantMed", 3)
app.UpdateRecord("Obra")
app.FindEqual("Conceptos", "Conceptos.Código", code)
app.SetField("Conceptos.RedParc", 3)
app.UpdateRecord("Conceptos")

# insert a line (numbers: N, Longitud, Anchura, Altura, Cota, BIMLong, BIMVol, Origen;
# text: Comentario, GuidElem, CategoríaBIM, TipoBIM, FamiliaBIM, Planta, Área, Archivo, Nota)
app.InitRecord("Mediciones")
app.SetField("Mediciones.CodSup", sup)
app.SetField("Mediciones.CodInf", code)
app.SetField("Mediciones.N", 1.0)
app.SetField("Mediciones.Longitud", 14.4)            # an unset column is left out of the product
app.SetField("Mediciones.GuidElem", ifc_global_id)
app.SetField("Mediciones.Origen", 3)                 # 3 = plugin
app.InsertRecord("Mediciones")

# delete: restart the set after EVERY DeleteRecord
while True:
    app.SetElement(8, "Mediciones", "Mediciones.Relación", '"*"', flt)
    if app.GetElement(8) != 0:
        break
    app.DeleteRecord("Mediciones", 0)
```

- **`Relaciones.CanPres` is not recomputed** from lines written through the API (`Recalculate(1)`
  and `Calculate(3)` leave it): sum `Mediciones.Cantidad` (lines with `Pres == 1`) and write it to
  the relation (`SetElement(9, "Relaciones", …)` → `SetField("Relaciones.CanPres", total)` →
  `UpdateRecord`).
- **Find the partida's parent in the obra** (`SetElement(9, "Relaciones", "Relaciones.CodSup",
  '"*"', 'Relaciones.CodInf=="01.01"')`): it may have moved since the budget was created.
- Scripts: `02_Write/WriteMeasurementLinesFromJson.py`, `01_Read/ReadMeasurementLines.py` (✅ both run whole on 570 lines;
  the writer needs 2 undo steps: lines, then CanPres), fed by
  `05_Tekla/06_Export/ExportTakeoffForPresto.py`.

---

## Method reference (Presto 26.01 type library)

Parameter names are the type library's. Every member is called with `()` through the proxy.

### Session and obra

| Method | Use | |
|---|---|---|
| `VersionStr()` | `"Presto 26.01"` | ✅ |
| `Project()` | full path of the active obra (`""`/`None` if none ⏳) | ✅ |
| `VersionNum()`, `SubVersionNum()` | numeric version | ⏳ |
| `ReadOnly()`, `Status()`, `ProjectLanguage()`, `IULanguage()` | obra state / languages; tlb: language 0 es, 1 ca, 2 en, 3 fr, 4 gl, 5 pt, 6 de | ⏳ |
| `Open(bstrPath, nMode)`, `Close()`, `New(obra)`, `Delete(obra)` | open / close / create / delete obras; tlb: `nMode` 0 read/write, 1 read-only, 2 convert to `.Presto` | ⏳ — `New` raised `RPC_E_SERVERFAULT` once; avoid, let the user create the obra |
| `CheckProject()` | obra consistency check | ⏳ |
| `SetCurrentInvPeriod(sDate)` | current period | ⏳ |

### Navigation

| Method | Use | |
|---|---|---|
| `FindEqual(tabla, clave, valor)` | find a record by key value, make it current; `0` = found | ✅ |
| `FindFirst(tabla, clave)`, `FindNext`, `FindPrev`, `FindLast` | scan a table in key order | ✅ `FindFirst/FindNext("Conceptos", "Conceptos.Código")` return 0 and move (`ListConceptsByNature.py`, same count as `SetElement`); ✅ `FindFirst("Obra", "Obra.Código")` makes the obra record current; ✅ on `Mediciones` they return 1 and **don't move** — use `SetElement` |
| `FindGreat`, `FindGreatEqual`, `FindLessEqual(tabla, clave, valor)` | range positioning | ⏳ |
| `FindPos(tabla, clave, pos)`, `GetPos(tabla)` | position by index | ⏳ |
| `SetElement(elemento, tabla, clave, mascara, seleccion[, ordenar_por, orden])` | open a filtered loop on a slot | ✅ (5 args) |
| `GetElement(elemento[, anida])` | next record of the slot; `0` while there are records | ✅ |
| `GetSelection(first, tabla)` | records the user selected in the active window | ✅ `ReadSelection.py`: `(1, "Conceptos")` = first selected, `(0, …)` = next, 0 while found |

### Reading

| Method | Use | |
|---|---|---|
| `GetFieldStr(campo)` | text field of the current record | ✅ |
| `GetFieldNum(campo)`, `GetField(campo)` | numeric field | ✅ |
| `EvalNum(expresion)` | numeric expression, 2 decimals | ✅ |
| `EvalStr(expresion)` | text expression | ⏳ |
| `GetText(campo, tipo)` | long text (e.g. the concept's description) | ⏳ |
| `GetFieldBinary(campo)` | binary field | ⏳ |
| `ReadTableByKey(nOutputFormat, table, key, fieldsToRead, orderField, desc)` | whole table in ONE call — fastest read. **Fields separated by `;`** (commas/`|`/tabs → `None`, no error; table prefix optional). `nOutputFormat` 0 flat JSON `{"fields":[{name,type}],"retcode":rows,"val":[{"row":[{"data":v}]}]}` (numbers typed), 1 indented JSON, 2 text (header `Código;A24;Nat;C`, tab-separated rows). `orderField` any field (`""` = key order) | ✅ `ReadTableByKey.py` |
| `ReadTableByKeyValue(nOutputFormat, table, key, value, fieldsToRead, orderField, desc)` | same, only records whose key = value: works as a filter (`"Conceptos.Nat", 5` = partidas; `"Relaciones.CodSup", "EAV"` = children of EAV) | ✅ `ReadTableByKey.py` (`KEY_VALUE`) |
| `InfoCode(proyecto, codigo, unidad, resumen, precio)` | concept info from another obra | ⏳ |

### Writing

| Method | Use | |
|---|---|---|
| `InitRecord(tabla)` → `SetField` → `InsertRecord(tabla)` | new record | ✅ `Conceptos`, `Relaciones`, `Mediciones` (Rule #6) |
| `SetField(campo, valor[, dimension])` + `UpdateRecord(tabla)` | change the current record | ✅ `Nat`, `Resumen`, `Ud`, `CanPres`, `Conceptos.Pres` (`SetCypePrices.py`), `Conceptos.RedParc`, `Obra.DecCantMed` |
| `DeleteRecord(tabla, todo)` | delete the current record; tlb: `todo` 1 = also delete the related records | ✅ `todo` 0 on `Relaciones` and `Conceptos` (`ClassifyCypeChapters.py`) and `Mediciones` (Rule #6) — confirm with the user |
| `Duplicate(codigo, nuevo)` | copy a concept to a new code | ⏳ |
| `Rename(campo, valor)` | tlb: "renombra un registro" (renames the current record's key) | ⏳ |
| `SetText(campo, valor)` | long text | ⏳ |
| `SetFieldBinary(campo, valor)` | binary field | ⏳ |
| `Copy(origen, destino, dimension1, dimension2)` | copy field values | ⏳ |
| `SetVar(variable, valor)`, `InitVar()`, `CreateVariable(...)`, `Set*VarValue(...)` | obra / BIM variables | ⏳ |
| `InsertAttachmentFromPath(table, code, filePath, resetSourcePath)` | attach a file to a record | ⏳ |
| `AddSpace(...)`, `CreateSpace(...)`, `AddCert(...)` | spaces, certifications | ⏳ |
| `SetTakeoffInsertMode(n)` | measurement-line insert mode | ⏳ |

### Undo, calculation, screen, messages

| Method | Use | |
|---|---|---|
| `BeginRedo()` / `EndRedo()` | one undo step | ✅ |
| `Recalculate(activar)` | tlb: locks / unlocks automatic recalculation; `Recalculate(1)` after the writes re-enables it and recomputes | ✅ (`1`) |
| `UpdateScreen()` | refresh Presto's windows | ✅ |
| `Calculate(nCalculationMode)` | explicit calculation; tlb: 1 all, 2 prices, 3 measurements, 4 times, 5 documents, 6 real costs | ⏳ |
| `SetUpdateScreen(activar)`, `SetModal(activar)` | freeze screen / modal state | ⏳ |
| `LogBegin(head)`, `LogMsg(msg, nMode)`, `LogEnd()` | Presto log window (shown by `LogEnd`); tlb: `nMode` 0 info, 1 warning, 2 error | ⏳ |
| `MsgText(msg, nMode)`, `MsgClear()`, `MsgSetTabs`, `MsgWrapText` | message window text | ⏳ |
| `ShowWindow(id)`, `CloseWindow(id)`, `Command(opcion)` | UI; tlb: window 0 tree, 1 budget, 2 measurements, 3 temporary measurements, 4 spaces | ⏳ |

### Exchange

| Method | Use | |
|---|---|---|
| `ExportFIEBDC(archivo)` | export the obra to BC3 | ✅ `ExportFIEBDC.py`: full path, returns 0, no dialog, ANSI; ~C/~D/~E but **no ~M measurement lines** |
| `ImportFIEBDC(archivo)` | import a BC3 **into the open obra** | ⏳ — confirm first |
| `ExportRPT(informe, archivo, parametros, formato, …)`, `PrintRPT(…)` | run a Presto report to a file / printer | ⏳ |
| `ImportCad(proyecto, archivo, tipo)` | CAD measurement import | ⏳ |
| `SQLServerExport/Import/Delete(...)` | SQL Server exchange | ⏳ |

---

## Exporting to Excel

The openpyxl rules are host-agnostic — follow
[RevitApiPatterns → Exporting to Excel](RevitApiPatterns.md#exporting-to-excel-openpyxl): never
auto-fit via `ws.columns`, table names like `Tabla_1` (never `T1`), write empty cells as `None`.
Example: `01_Scripts/06_Presto/03_Export/ExportBudgetToExcel.py`.

---

## Common pitfalls

| Symptom | Cause | Fix |
|---|---|---|
| `GetFieldStr("Conceptos.Nat")` / `("Relaciones.CanPres")` is `None` | numeric field | `GetFieldNum` / `GetField` (Rule #3) |
| Amounts off by a few cents, prices with 2 decimals only | `EvalNum` rounds to 2 decimals | `GetFieldNum` for prices and quantities |
| `if app.FindEqual(...)` takes the wrong branch | `0` = found | compare `== 0` / `!= 0` |
| A field got written into the wrong concept | another Find*/GetElement moved the cursor before `SetField` | Find the record right before `SetField` + `UpdateRecord` (Rule #1) |
| `SetField` "did nothing" | no `UpdateRecord(table)` after it | commit every record |
| Inserted concept has no summary/nature | fields set before re-finding the new record | `InsertRecord` → `FindEqual` → `SetField` → `UpdateRecord` |
| Tree walk skips or repeats records | an inner loop reused the slot of an outer loop | one slot per depth (Rule #2) |
| Wrong values in a tree walk | fields read after descending | read the record before the recursive call |
| `_SPC_` / `_CHG_` rows in the output | system concepts (Nat 219 / 170) | filter `"Conceptos.Nat!=219 && Conceptos.Nat!=170"` |
| Mask matches nothing | mask without its own quotes | `'"' + code + '"'` |
| `MissingMemberException` (`DISP_E_UNKNOWNNAME`) | wrong member name (or a field name with a missing accent passed as a member) | check the method tables above; fields keep their accents: `Conceptos.Código` |
| `<function VersionStr>` printed instead of the value | property used without `()` | every member is a call: `app.VersionStr()` |
| `COMException RPC_E_SERVERFAULT` | stale COM object with 2 obras open (PyNET re-attaches before each script now); once on `New(path)` | one obra open; don't create obras from scripts |
| Script wrote into the other obra | 2 obras open, the active one was not the expected one | check `app.Project()` / confirm (Rule #5) |
| Presto's undo is stuck after a failed script | `BeginRedo` without `EndRedo` | `try/finally: app.EndRedo()` (Rule #4) |
| Totals not updated after a write | no recalculation | `Recalculate(1)` + `UpdateScreen()` |
| A call hangs ~30 s then fails | Presto busy (a dialog open) | close Presto's dialog; the message filter gives up after 30 s |
| No Complementos menu | 0 or 2+ obras open; Presto Demo has no Complementos directory | open exactly one obra; Demo: Start-menu shortcut |
| User lost the changes | the script does not save | tell the user to save the obra in Presto |
| `SetElement` on `Mediciones` returns 1 with key `CodSup` / `CodInf` / `Id` / `GuidElem` / `Planta` | not keys of the table | key `Mediciones.Relación` (or `Mediciones.Guid`), mask `'"*"'`, filter on `CodSup`/`CodInf` (Rule #6) |
| Every "line" read with `FindFirst`/`FindNext("Mediciones", …)` is the same / empty | they return 1 and don't move: you read the `InitRecord` buffer; `EvalStr`/`EvalNum` on `Mediciones[...]` are empty too | `SetElement`/`GetElement` (Rule #6) |
| Measurement lines rounded to cm / 0.01 m³ | `Obra.DecCantMed` / `Conceptos.RedParc` default 2 | set them to 3 before inserting; delete + reinsert existing lines |
| Partida quantity ≠ sum of its lines | `CanPres` not recomputed for API-written lines | sum `Mediciones.Cantidad`, write `Relaciones.CanPres` (Rule #6) |
| Lines written under the wrong / a missing relation | the partida was moved to another parent | find the parent(s) with `SetElement` on `Relaciones`, mask `'"*"'` |

---

<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->
