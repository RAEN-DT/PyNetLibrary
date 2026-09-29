# Skill: TimelinerImport

Imports a Primavera **P6 XER** schedule into Navisworks **TimeLiner** as tasks — bypassing the fact
that Navisworks' native TimeLiner only ingests Primavera through the *web-services* data sources
(there is no native "import XER file"). Validated end-to-end on a real session.

## Context

- **Host:** Navisworks only.
- **Read first:** [docs/navisworks-timeliner.md](../../docs/navisworks-timeliner.md) — the full
  TimeLiner API reference (casting `doc.Timeliner`, task-type gotcha, `Selection` linking). This
  skill is the workflow around it.
- **Write script** — adds tasks to the open document's TimeLiner. Follows the standard confirmation
  policy (AGENTS.md §8): confirm once before the first execution.
- **Input XER:** always ask the user for the path, every run — never reuse a path from a previous
  session or `AI_History` without confirming it for this run.

---

## Workflow

### 1. Check active instance
`list_active_instances` → must be Navisworks. If several sessions are open, identify by the open
document/model name, not PID alone (AGENTS.md §1).

### 2. Ask for the XER path (if not already given)
Confirm the file exists before doing anything else.

### 3. Inspect the open document (read-only)

```python
from Autodesk.Navisworks.Api import Application
from Autodesk.Navisworks.Api.Timeliner import DocumentTimeliner
from Raen.Core.Pynet.Resources import CastUtils

doc = Application.ActiveDocument
tl = CastUtils.CastTo[DocumentTimeliner](doc.Timeliner)

ia_Result = {
    "type": "DocInfo",
    "title": doc.Title,
    "current_file": str(doc.CurrentFileName),
    "existing_tasks": tl.Tasks.Count,
}
```

Report the document name and existing task count. If `existing_tasks > 0`, ask whether to append on
top or the user expected a clean TimeLiner — don't silently pile tasks onto a populated schedule.

### 4. Peek the XER (read-only) — size the import before writing

Parse it (CP1252, tab-delimited, `%T`/`%F`/`%R` blocks — see
[navisworks-timeliner.md §4](../../docs/navisworks-timeliner.md) for the full parser) and report,
**before touching the document**:

- `TASK` row count (this is how many TimeLiner tasks will be created)
- Tables present (`CALENDAR`, `PROJECT`, `PROJWBS`, `TASK`, `TASKPRED`, …) — confirms it's a real XER
- A sample of `TASK` field names, to catch a non-standard export early

```python
from pathlib import Path

raw  = Path(xer_path).read_bytes()
text = raw.decode("cp1252")
nl   = "\r\n" if b"\r\n" in raw else "\n"          # real P6 uses CRLF, GitHub samples LF

tables, cur = {}, None
for ln in text.split(nl):
    p = ln.split("\t")
    if   p[0] == "%T": cur = p[1]; tables[cur] = {"f": [], "r": []}
    elif p[0] == "%F": tables[cur]["f"] = p[1:]
    elif p[0] == "%R": tables[cur]["r"].append(p[1:])

ia_Result = {
    "type": "XerInfo",
    "task_count": len(tables.get("TASK", {"r": []})["r"]),
    "tables_present": list(tables.keys()),
    "task_fields_sample": tables.get("TASK", {"f": []})["f"][:15],
}
```

### 5. Confirm before executing

Write script — confirm once (AGENTS.md §8). State clearly: target document, task count about to be
added, and that this modifies the open document.

### 6. Import — create one `TimelinerTask` per `TASK` row

```python
from System import DateTime

f = tables["TASK"]["f"]
def col(r, name):
    i = f.index(name); return r[i] if i < len(r) else ""
def dt(s):
    s = s.strip()
    if not s: return None
    d, t = s.split(" "); y, mo, da = d.split("-"); hh, mi = t.split(":")
    return DateTime(int(y), int(mo), int(da), int(hh), int(mi), 0)

rows, total, added = tables["TASK"]["r"], len(tables["TASK"]["r"]), 0
for idx, r in enumerate(rows):
    task = TimelinerTask()
    task.DisplayName = col(r, "task_name") or col(r, "task_code")
    s = dt(col(r, "target_start_date")) or dt(col(r, "early_start_date"))
    e = dt(col(r, "target_end_date"))   or dt(col(r, "early_end_date"))
    if s: task.PlannedStartDate = s
    if e: task.PlannedEndDate   = e
    tl.TaskAddCopy(task)                            # no SimulationTaskTypeName -> untyped, adds clean
    added += 1
    if total >= 10 and (idx + 1) % max(1, total // 10) == 0:
        print("Progress: {}/{}".format(idx + 1, total))

ia_Result = {"type": "TimelinerLoadResult", "tasks_added": added, "total_in_timeliner": tl.Tasks.Count}
```

**Gotcha — do not set `SimulationTaskTypeName`.** A blank/new document carries no simulation task
types (`Construct`/`Demolish`/`Temporary` don't exist until something creates them); setting the name
on an unregistered type raises `Argument references a SimulationTaskType that does not exist`. Leave
tasks untyped — fine for a schedule import, the type only drives simulation appearance.

**Progress prints are mandatory** for any run ≥10 rows (AGENTS.md §5) so a timeout can be told apart
from a hang.

### 7. Report results

Natural language (Production mode): tasks added, total now in TimeLiner, and confirmation the user
can review them in the TimeLiner tab.

### 8. Script length / save-to-disk

The whole import is well under ~80 lines inline — keep it as `send_command` (development default,
AGENTS.md §6). Only save it to `01_Scripts/01_Navisworks/00_Workflow/TimelinerImport.py` and switch to
`send_command_by_path` if this becomes a recurring workflow for a project (repeated runs against the
same/similar schedules).

---

## Optional — linking tasks to geometry

Out of scope for a plain schedule import, but if the user also wants tasks to drive elements during
simulation, see [navisworks-timeliner.md §5](../../docs/navisworks-timeliner.md) (`Selection`,
built from a `SelectionSet` — documented, not yet validated live). Ask before extending the import to
build selection sets and attach them per task; requires `task_code`/WBS mapping to model elements
that the XER alone doesn't provide.

---

## Common issues

| Symptom | Cause | Fix |
|---|---|---|
| `'Document' object has no attribute 'GetTimeliner'` | Used the C#-sample extension method | Cast instead: `CastUtils.CastTo[DocumentTimeliner](doc.Timeliner)` |
| `Non-whitelisted assembly` on `clr.AddReference("Autodesk.Navisworks.Timeliner")` | That assembly isn't on the CLR whitelist | Don't add it — Navisworks Manage preloads it; just `from Autodesk.Navisworks.Api.Timeliner import ...` directly |
| `Argument references a SimulationTaskType that does not exist` | Set `SimulationTaskTypeName` on a document with no registered task types | Omit the property (see step 6 gotcha) |
| Garbled dates / wrong row split | Wrong newline assumed | Detect CRLF vs LF from the raw bytes before splitting (`nl = "\r\n" if b"\r\n" in raw else "\n"`) — GitHub-hosted sample XERs are often LF-only while real P6 exports are CRLF |
| Mojibake in task names (accents, `°`) | Decoded as UTF-8 instead of the XER's native encoding | XER is **CP1252** — always `raw.decode("cp1252")`, never `.decode()` default/UTF-8 |

---

<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->
