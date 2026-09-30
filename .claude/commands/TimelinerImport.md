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

> **Save the `.nwf`/`.nwd` early and often once you start writing.** Nothing in this workflow
> (tasks, SelectionSets, clash tests, folder reorg) is on disk until you call `doc.SaveFile(path)` —
> it all lives in the live Navisworks process. If the host closes or crashes mid-session (see "Known
> incidents" below), everything since the last save is gone. Save right after the model loads, then
> again after each milestone (import done, 4D linked, tests run, folders organized) — not just once
> at the end.

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

**Gotcha — check whether simulation task types exist before setting `SimulationTaskTypeName`.** A
genuinely blank/new document carries no simulation task types (`Construct`/`Demolish`/`Temporary`
don't exist until something creates them); setting the name on an unregistered type raises `Argument
references a SimulationTaskType that does not exist`. **But** a document that already has a model
appended usually already has the default types registered (confirmed live: `tl.SimulationTaskTypes`
returned `Construcción`/`Demoler`/`Temporal`, localized, after `AppendFiles`) — check
`[t.DisplayName for t in tl.SimulationTaskTypes]` first. **If you only need dated rows** (no visible
construction in the Simulate tab), leaving tasks untyped is fine. **If the user wants an actual 4D
simulation, the type is not optional** — see "linking tasks to geometry" below: without a
`SimulationTaskTypeName`, Simulate shows the model static regardless of correct `Selection` links,
because TimeLiner has no rule telling it whether to reveal/hide/ghost the geometry over time.

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

## Optional — linking tasks to geometry (the actual "4D")

**A schedule import without this is not 4D** — it's a set of dated TimeLiner rows with nothing to
animate. If the user asks for 4D (not just "load the schedule"), this step is mandatory, not optional.
Ask first if it's unclear which elements belong to which task; do not silently guess a mapping for a
real project (a POC/sample model is a reasonable case to propose one, see below).

### Why a plain `SelectionCondition` search usually fails here

If the classification you're grouping by (e.g. a PyNET code, a house/zone) comes from a **Type-level**
Revit parameter, Navisworks only exports it onto the **TYPE container node** in the NWC — not onto
instances or their geometry. Confirmed live: `PropertyCategories` scan on an instance node under a
classified TYPE node returns an empty list for that property, and a `SearchCondition` built from it
matches only the 1 TYPE node (no geometry). `dir()`-probe the instance and its children first
(`try/except`, per AGENTS.md §6) before assuming Search will work — don't find this out from an empty
clash/selection result.

**Workaround — build the `ModelItemCollection` directly** (the coverage-scan pattern from
[ClashDetection.md](ClashDetection.md) step 2b), not a dynamic `Search`:

```python
from collections import defaultdict
from Autodesk.Navisworks.Api import Application, SelectionSet, ModelItemCollection

doc = Application.ActiveDocument
model = doc.Models[0]

# Pass 1: classify TYPE nodes by the parameter
classified = {}
for item in model.RootItem.Descendants:
    if item.ClassDisplayName != "Tipo":
        continue
    code = None
    for cat in item.PropertyCategories:
        if cat.DisplayName != "Tipo Personalizar":   # shared-param export category — verify per project
            continue
        for prop in cat.Properties:
            if prop.DisplayName == "PYNET_Classification":
                try:
                    code = prop.Value.ToDisplayString() or None
                except Exception:
                    pass
    if code:
        classified[hash(item)] = (code, item)

# Pass 2: geometry descendants per code, dedup by hash
code_items = defaultdict(list)
covered = set()
for h, (code, type_item) in classified.items():
    for desc in type_item.Descendants:
        if desc.HasGeometry and hash(desc) not in covered:
            covered.add(hash(desc))
            code_items[code].append(desc)
```

If the grouping also needs a spatial split (e.g. one task per building/zone, not just per discipline
code), cluster by bounding-box center rather than assume a fixed coordinate — **compute it from the
live data, don't hardcode thresholds copied from another host.** Read each candidate's
`item.BoundingBox()` (`.Min`/`.Max` have `.X/.Y/.Z`), sort the centers, and split on the largest gaps
(e.g. 2 gaps → 3 clusters) — this is robust to whatever offset/rotation the export's coordinate system
applied and needs no manual tuning:

```python
ys = sorted(center_y_of(item) for item in items)
gaps = sorted(((ys[i+1] - ys[i], i) for i in range(len(ys) - 1)), reverse=True)
cut1, cut2 = sorted(ys[gaps[0][1]] for _ in [0]) + sorted(ys[gaps[1][1]] for _ in [0])  # two cut points
```

### Building the SelectionSet and attaching it to an existing task

A live `TimelinerTask`'s `Selection` **cannot be set directly** (`IsReadOnly`) — edit through a copy,
same pattern as editing a live `ClashTest`'s tolerance. Critically, `TaskReplaceWithCopy` takes the
**index**, not the task object:

```python
from Autodesk.Navisworks.Api import SelectionSet, ModelItemCollection, SelectionSourceCollection

coll = ModelItemCollection()
for it in code_items["PIL"]:
    coll.Add(it)
ss = SelectionSet(coll)
ss.DisplayName = "H1-EST"
doc.SelectionSets.AddCopy(ss)                       # add to root first

def find_selset(root, name):
    for it in root.Children:
        if it.DisplayName == name:
            return it
        if it.IsGroup:
            f = find_selset(it, name)
            if f:
                return f
    return None

sel_set_item = find_selset(doc.SelectionSets.RootItem, "H1-EST")
source = doc.SelectionSets.CreateSelectionSource(sel_set_item)
sources = SelectionSourceCollection()
sources.Add(source)

CONSTRUCT_TYPE = "Construcción"   # confirm the exact localized name first: [t.DisplayName for t in tl.SimulationTaskTypes]

for i, t in enumerate(tl.Tasks):                    # find the live task's index — TaskReplaceWithCopy needs it
    if t.DisplayName == "Casita 1 - Estructura (PIL+LOS)":
        task_copy = t.CreateCopy()
        task_copy.Selection.CopyFrom(sources)
        task_copy.SimulationTaskTypeName = CONSTRUCT_TYPE   # set BOTH in the same copy — see "Known incidents"
        tl.TaskReplaceWithCopy(i, task_copy)         # (Int32 index, TimelinerTask) — NOT (task, task)
        break
```

**Verify the link before reporting success** — `t.Selection.GetSelectedItems(doc)` needs `doc` as an
argument (bare `GetSelectedItems()` raises "No method matches given arguments"):

```python
for t in tl.Tasks:
    n = sum(1 for _ in t.Selection.GetSelectedItems(doc))
    print("{}: {} linked items".format(t.DisplayName, n))
```

A task with 0 linked items after this means the mapping (code/house) found no matching geometry —
investigate before telling the user it's done.

---

## Optional — organizing SelectionSets into folders

Once you've created several SelectionSets (classification codes, per-task 4D links, …), group them
into folders instead of leaving them flat at root — do this whenever the flat list would mix unrelated
sets (e.g. classification codes next to per-task 4D links).

**Create a folder** with `FolderItem` and add it via the manager (`doc.SelectionSets`, not the plain
`SelectionSet` API):

```python
from Autodesk.Navisworks.Api import FolderItem

def find_direct(parent, name):
    for i, it in enumerate(parent.Children):
        if it.DisplayName == name:
            return i, it
    return None, None

mgr = doc.SelectionSets
root = mgr.RootItem

folder = FolderItem()
folder.DisplayName = "Clasificacion PYNET"
mgr.AddCopy(root, folder)
_, folder = find_direct(root, "Clasificacion PYNET")   # re-fetch: AddCopy copies, the local `folder` is stale
```

**Move existing sets into it — `Move`, not delete-and-recreate.** Recreating a set changes its GUID,
which silently breaks every `ClashTest`/`TimelinerTask` `Selection` that already references it.
`Move(oldParent, oldIndex, newParent, newIndex)` preserves identity, so anything already pointing at
that set keeps working:

```python
idx, item = find_direct(root, "PIL")
mgr.Move(root, idx, folder, folder.Children.Count)   # append at the end of the folder
```

Folders can nest (a folder's `Children` can itself hold another `FolderItem`) — build the parent
folder first, `AddCopy` it under root, re-fetch it via `find_direct`, then `AddCopy` each child folder
under *that* before moving sets into the leaf folders. Verify nothing broke afterward: re-run a cheap
check on any `ClashTest`/`TimelinerTask` that referenced a moved set (result count / linked-item count
unchanged confirms the `Move` didn't disturb the reference).

---

## Known incidents

- **2026-09-29 — Navisworks crashed mid-session, killing all unsaved 4D/clash work.** Sequence: a
  batch `doc.SelectionSets.Move(...)` reorg (15 moves, reorganizing classification + per-task 4D sets
  into folders) immediately followed by a second, separate loop of 9 `TaskReplaceWithCopy` calls (to
  set `SimulationTaskTypeName` on tasks whose `Selection` had *already* been set in an earlier loop —
  so each task had been through two full copy-edit-replace cycles). Mid-way through the second loop,
  the MCP call returned `Connection closed unexpectedly by PID <pid>` and the host process was gone
  from `list_active_instances` — not a bridge crash (`check_plugin_status` also failed to find the
  PID), the Navisworks process itself died. **Nothing had been saved at any point**, so the open
  document (SelectionSets, clash tests, TimeLiner tasks and their links) was lost entirely; only files
  already on disk (the source `.rvt`, the exported `.nwc`, the `.xer`) survived.
  Root cause is not confirmed with certainty — Navisworks was never queried for a crash dump — but the
  circumstantial pattern (stable through 21 total document mutations across three separate write
  scripts, then died partway through a fourth, immediately after a batch reorg, with no save in
  between any of them) points at accumulated undo-history/memory pressure from many scripted mutations
  with no flush. **Fix applied:** rebuilt the same 4D linking as a **single** `CreateCopy()` →
  set `Selection` **and** `SimulationTaskTypeName` together → **one** `TaskReplaceWithCopy` per task
  (9 total edits instead of 18), and called `doc.SaveFile(...)` immediately after loading the model
  and after every subsequent milestone (4D linked, tests re-run, folders reorganized) — see the
  "save early and often" note under Context. The combined-edit rebuild and the folder reorg both
  completed without incident on retry.
  **Takeaway:** don't chain multiple separate edit-copy-replace passes over the same tasks when the
  edits could be combined into one; save after every milestone, not just at the end, so a crash costs
  minutes of rework instead of the whole session.

---

## Common issues

| Symptom | Cause | Fix |
|---|---|---|
| `'Document' object has no attribute 'GetTimeliner'` | Used the C#-sample extension method | Cast instead: `CastUtils.CastTo[DocumentTimeliner](doc.Timeliner)` |
| `Non-whitelisted assembly` on `clr.AddReference("Autodesk.Navisworks.Timeliner")` | That assembly isn't on the CLR whitelist | Don't add it — Navisworks Manage preloads it; just `from Autodesk.Navisworks.Api.Timeliner import ...` directly |
| `Argument references a SimulationTaskType that does not exist` | Set `SimulationTaskTypeName` on a document with no registered task types | Omit the property (see step 6 gotcha) |
| Garbled dates / wrong row split | Wrong newline assumed | Detect CRLF vs LF from the raw bytes before splitting (`nl = "\r\n" if b"\r\n" in raw else "\n"`) — GitHub-hosted sample XERs are often LF-only while real P6 exports are CRLF |
| Mojibake in task names (accents, `°`) | Decoded as UTF-8 instead of the XER's native encoding | XER is **CP1252** — always `raw.decode("cp1252")`, never `.decode()` default/UTF-8 |
| `No method matches given arguments for DocumentTimeliner.TaskReplaceWithCopy: (TimelinerTask, TimelinerTask)` | Passed the live task object as the first argument | It takes `(Int32 index, TimelinerTask copy)` — find the task's index in `tl.Tasks` first |
| `No method matches given arguments for TimelinerSelection.GetSelectedItems: ()` | Called without the document | `GetSelectedItems(doc)` — the document is required |
| SearchCondition on a classification parameter matches only 1 item (the TYPE node), 0 geometry | The parameter is a **Type**-level Revit parameter — NWC only carries it on the TYPE container, not on instances/geometry | Build the `ModelItemCollection` directly from geometry descendants under classified TYPE nodes (see "linking tasks to geometry" above) instead of a `SearchCondition` |
| A moved/recreated `SelectionSet` breaks an existing `ClashTest`/`TimelinerTask` reference | Deleted and recreated the set instead of moving it — a new object gets a new GUID | Use `doc.SelectionSets.Move(oldParent, oldIndex, newParent, newIndex)` to reorganize into folders; never delete+recreate a set something already references |

---

<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->
