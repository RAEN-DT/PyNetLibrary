<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: TimeLiner (4D scheduling) — Navisworks

Read [navisworks.md](navisworks.md) first. This guide covers driving TimeLiner from a PyNET
script: creating tasks, linking them to geometry, and feeding them from a Primavera **P6 XER**
file — all in-process, with **no web-services connector and no CSV import**.

> **Why this exists.** Navisworks' native TimeLiner only ingests Primavera through the *web-services*
> data sources (see the "Orígenes de datos → Añadir" menu: the three P6 entries are all "servicios
> web"). There is **no native "import XER file"**. The API path below lets us read the exported XER
> ourselves and write the schedule straight into TimeLiner, bypassing that limitation.

---

## 1. Accessing the TimeLiner document part

`doc.Timeliner` returns an **`IDocumentTimeliner`** — the *managed* interface is effectively empty
(only `Equals/GetType/ToString`; no `Tasks`, no `Simulation`). The real API lives on the concrete
`DocumentTimeliner`, reached by **casting**, exactly like `doc.Clash` → `DocumentClash`:

```python
from Autodesk.Navisworks.Api.Timeliner import DocumentTimeliner, TimelinerTask
from Raen.Core.Pynet.Resources import CastUtils   # bundle boilerplate: see navisworks.md "CastUtils"

tl = CastUtils.CastTo[DocumentTimeliner](doc.Timeliner)   # real TimeLiner API
tl.Tasks.Count                                            # e.g. 0 on a fresh document
```

> `doc.GetTimeliner()` appears in Autodesk C# samples, but it is an **extension method** and
> pythonnet does **not** bind it to the instance (`'Document' object has no attribute 'GetTimeliner'`).
> Use the cast above.

Add/insert methods on `DocumentTimeliner`: `TaskAddCopy`, `TaskInsertCopy`,
`SimulationTaskTypeAddCopy`, `SimulationTaskTypeInsertCopy`.

---

## 2. Assembly & imports — do NOT `AddReference`

The TimeLiner types are in namespace **`Autodesk.Navisworks.Api.Timeliner`**, backed by the
assembly **`Autodesk.Navisworks.Timeliner`**.

That assembly is **not** on the validator's CLR whitelist ([security.md](security.md) lists only
`Autodesk.Navisworks.Api`, `.ComApi`, `.Interop.ComApi`, `.Clash`). But Navisworks **Manage always
preloads it**, so simply **import the types directly** — the whitelisted `Autodesk` import root lets
the `from Autodesk.Navisworks.Api.Timeliner import …` through. Adding the reference is both
unnecessary and rejected:

```python
clr.AddReference("Autodesk.Navisworks.Timeliner")   # ❌ validator: "Non-whitelisted assembly"
```

(A `clr.AddReference(var)` with a loop variable slips past the static check, but that is a hack —
rely on the preload instead.) **To make TimeLiner first-class**, add
`Autodesk.Navisworks.Timeliner` to the assembly whitelist in `PyNetBridge/pynet_mcp/server.py`
(keep [security.md](security.md) in sync).

---

## 3. Creating and adding tasks

```python
from System import DateTime

task = TimelinerTask()
task.DisplayName      = "Chiller procurement (16-wk lead)"
task.PlannedStartDate = DateTime(2026, 1, 12, 8, 0, 0)     # System.DateTime, not python datetime
task.PlannedEndDate   = DateTime(2026, 5, 5, 16, 0, 0)
tl.TaskAddCopy(task)                                        # appends a COPY of the task
```

`TimelinerTask` properties used here: `DisplayName`, `PlannedStartDate`, `PlannedEndDate`,
`SimulationTaskTypeName`, `Selection` (see §5).

### Gotcha — the task type must already exist

Setting `task.SimulationTaskTypeName = "Construct"` on a **blank document raises** on add:

```
Argument references a SimulationTaskType that does not exist
```

A new/empty document carries **no** simulation task types — the familiar
`Construct` / `Demolish` / `Temporary` are **not** present until something creates them. Options:

- **Omit** `SimulationTaskTypeName` — tasks are added untyped (fine for a schedule import; the type
  only drives simulation appearance).
- **Register the types first** with `tl.SimulationTaskTypeAddCopy(...)`, then set the name. *(Creating
  the task-type object is not yet validated in this repo — confirm the exact class before relying on
  it.)*

---

## 4. Feeding TimeLiner from a Primavera P6 XER  *(validated end-to-end)*

An **XER** is a **CP1252**, tab-delimited **text file** — a header line (`ERMHDR`) then repeating
`%T <table>` / `%F <fields>` / `%R <row>` blocks, ending in `%E`. It is not a database and needs no
Oracle, no server, no credentials. Parse it into pandas DataFrames (one per table) and map the
`TASK` table onto TimeLiner tasks.

```python
from pathlib import Path
from System import DateTime

raw  = Path.home().joinpath("Downloads", "sample-schedule.xer").read_bytes()
text = raw.decode("cp1252")
nl   = "\r\n" if b"\r\n" in raw else "\n"          # ⚠ detect: real P6 uses CRLF, GitHub samples LF

tables, cur = {}, None
for ln in text.split(nl):
    p = ln.split("\t")
    if   p[0] == "%T": cur = p[1]; tables[cur] = {"f": [], "r": []}
    elif p[0] == "%F": tables[cur]["f"] = p[1:]
    elif p[0] == "%R": tables[cur]["r"].append(p[1:])

f = tables["TASK"]["f"]
def col(r, name):
    i = f.index(name); return r[i] if i < len(r) else ""
def dt(s):
    s = s.strip()
    if not s: return None
    d, t = s.split(" "); y, mo, da = d.split("-"); hh, mi = t.split(":")
    return DateTime(int(y), int(mo), int(da), int(hh), int(mi), 0)

for r in tables["TASK"]["r"]:
    task = TimelinerTask()
    task.DisplayName      = col(r, "task_name") or col(r, "task_code")
    s = dt(col(r, "target_start_date")) or dt(col(r, "early_start_date"))
    e = dt(col(r, "target_end_date"))   or dt(col(r, "early_end_date"))
    if s: task.PlannedStartDate = s
    if e: task.PlannedEndDate   = e
    tl.TaskAddCopy(task)                            # no SimulationTaskTypeName -> untyped, adds clean
```

Useful `TASK` columns: `task_code`, `task_name`, `status_code`, `phys_complete_pct`,
`target_start_date`, `target_end_date`, `early_start_date`, `early_end_date`. Structure lives in
`PROJWBS` (WBS/phases), logic in `TASKPRED` (`pred_task_id` → `task_id`, `pred_type`, `lag_hr_cnt`).

> **Writing an XER back (round-trip)** is lossless only if you preserve the header envelope, exact
> field order, **CP1252** encoding and cross-table referential integrity (IDs) — it is **not**
> `DataFrame.to_csv()`. Rewriting byte-identical-except-edits has been validated on the sample.

---

## 5. Linking a task to model geometry (`Selection`)  *(documented, not yet validated here)*

To make a task drive elements during simulation, attach a selection built from a selection set
(pattern from the Autodesk API sample — verify live before relying):

```python
from Autodesk.Navisworks.Api import SelectionSourceCollection

sel_set    = ...                                   # a SelectionSet from doc.SelectionSets
source     = doc.SelectionSets.CreateSelectionSource(sel_set)
collection = SelectionSourceCollection(); collection.Add(source)
task.Selection.CopyFrom(collection)
tl.TaskAddCopy(task)
```

This is the entry point for the **model ↔ schedule linking** case (populate the link parameters in
Revit/Civil at origin, build selection sets, attach here).

---

## 6. Probing the API (forbidden calls)

When introspecting live, remember the MCP validator blocks `getattr`, `setattr`, `eval`, `exec`,
`compile`, `__import__`. Use `dir(obj)` plus **direct** attribute access wrapped in `try/except` to
discover members — not `getattr`/`hasattr`.

---

## 7. Confirmation

Adding/inserting tasks **modifies the open document** — treat as a write (ask once before the first
run, per [AGENTS.md](../AGENTS.md) §8). Reading an XER and building DataFrames is read-only.
