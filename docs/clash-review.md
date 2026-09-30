<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: clash review — images, status, comments, grouping (Navisworks)

Read [navisworks.md](navisworks.md) first (boilerplate, `CastUtils`, the `pynet_clash` helpers
`get_clash_tests` / `iter_results`). Used by the `ClashDetection` skill, steps 11–12.

```python
from Autodesk.Navisworks.Api import (Assignee, Comment, CommentCollection, CommentStatus,
                                     ImageGenerationStyle)
from Autodesk.Navisworks.Api.Clash import ClashResultStatus, ClashResultGroup, IClashResult
```

`Assignee`, `Comment*` and `ImageGenerationStyle` live in `Autodesk.Navisworks.Api`, **not** in the
Clash namespace.

---

## Generating and analyzing clash images

Each clash result has a built-in viewpoint. `TestsImageForResult` renders it directly — no screen
capture needed. Standard output folder:
`%AppData%\Pynet\Navisworks\{YYYYMMDD}_{federated_name}\`.

```python
from datetime import datetime

date_str = datetime.now().strftime("%Y%m%d")
doc_name = Path(doc.FileName).stem if doc.FileName else "Unknown"
save_dir = Path.home() / "AppData" / "Roaming" / "Pynet" / "Navisworks" / f"{date_str}_{doc_name}"
save_dir.mkdir(parents=True, exist_ok=True)

clash_index = 1
for test in get_clash_tests(clashDoc):
    for r in iter_results(test):
        if r.Status == ClashResultStatus.Reviewed:
            # Scene / ScenePlusOverlay / SceneUsingRayTrace — ScenePlusOverlay adds the clash highlight
            bmp = testsData.TestsImageForResult(r, ImageGenerationStyle.ScenePlusOverlay, 800, 600)
            bmp.Save(str(save_dir / f"clash_{clash_index:02d}_{test.DisplayName.replace(' ', '_')}.png"))
        clash_index += 1
```

Read each image with the Read tool and analyze visually. Overlay colors: **green** = one of the
clashing elements (Selection A or B), **red** = the penetration zone / conflicting geometry.

> `TestsViewpointForResult(result)` returns the `Viewpoint` without rendering — use
> `TestsImageForResult` for an image.

---

## Changing clash result status

```python
assignee = Assignee()
assignee.DisplayName = "PyNET"  # or any reviewer name
testsData.TestsEditResultStatus(result, ClashResultStatus.Reviewed, assignee)
```

Values: `New`, `Active`, `Reviewed`, `Approved`, `Resolved`. Constructing `Assignee()` directly works;
passing `None` for the `who` argument raises `ArgumentNullException`.

Always iterate with `get_clash_tests` + `iter_results` so the index mapping stays stable across
scripts (results inside groups included).

**Other metadata methods** (all take the `result`, not the test):

```python
testsData.TestsEditResultApprovedBy(result, assignee, ...)   # set approver
testsData.TestsEditResultAssignedTo(result, assignee, ...)   # assign to reviewer
# Comments — takes CommentCollection, NOT a plain string
comments = CommentCollection()
comments.Add(Comment(f"[Auto-review {run_date}] {reason}", CommentStatus.New))
testsData.TestsEditResultComments(result, comments)
# Description — takes IClashResult + plain string
testsData.TestsEditResultDescription(CastUtils.CastTo[IClashResult](result), "text")
```

---

## Grouping clash results

When multiple results involve the **same element** (e.g. one facade panel clashing with 3 columns),
group them in a `ClashResultGroup` so the Navisworks UI shows them as one logical issue.
**Criterion:** within a test, any element (Item1 or Item2) appearing in 2+ results → group those
results under that element's name. Run grouping **after** applying all statuses and comments —
moving results into groups changes the iteration structure.

> ⚠ **Performance — do not re-scan `test.Children` before every move.** Re-finding the index with a
> fresh scan before each `TestsMove` is **O(n²)** — millions of live .NET reads on a 2,200-result
> test. Track the index **locally in Python** (a list mirroring the flat children's order, updated in
> place after each move): O(n) total. Measured on a real 2,200-result / 540-group case: **17 s**.
> Test on a small test (a few results), then a medium one (~30), before the largest.

```python
from collections import defaultdict

def group_by_shared_element(testsData, test):
    children = list(test.Children)
    flat = [(hash(r), r) for r in children if not r.IsGroup]
    if len(flat) < 2:
        return

    # Local index mirroring the live flat-children order. New groups are appended at the end by
    # TestsAddCopy, so they never shift these indices.
    order = [rh for rh, r in flat]
    pos = {rh: i for i, rh in enumerate(order)}

    elem_map = defaultdict(list)
    for rh, r in flat:
        try:
            elem_map[hash(r.Item1)].append((rh, r.Item1.DisplayName))
            elem_map[hash(r.Item2)].append((rh, r.Item2.DisplayName))
        except:
            pass

    processed = set()
    for elem_hash, entries in elem_map.items():
        entries = [e for e in entries if e[0] not in processed]
        if len(entries) < 2:
            continue

        group_name = f"{entries[0][1]} – {len(entries)} clashes"
        group = ClashResultGroup()
        group.DisplayName = group_name
        testsData.TestsAddCopy(test, group)  # adds a copy — must re-find the live reference

        live_group = next((c for c in test.Children if c.IsGroup and c.DisplayName == group_name), None)
        if live_group is None:
            continue

        for move_idx, (rh, _name) in enumerate(entries):
            current_idx = pos.get(rh)   # O(1) local lookup, no .NET scan
            if current_idx is None:
                continue
            testsData.TestsMove(test, current_idx, live_group, move_idx)
            processed.add(rh)
            del order[current_idx]      # keep the local index in sync
            for h in order[current_idx:]:
                pos[h] -= 1
            del pos[rh]
```

- `TestsAddCopy(parent, item)` adds a copy; the returned object is not the live reference — find the
  live group in `test.Children` by `DisplayName`.
- `TestsMove(oldParent, oldIndex, newParent, newIndex)` moves by index.
- Use `hash()` (maps to `GetHashCode()`, stable), not `id()`, to track .NET objects — pythonnet
  creates a new wrapper on every access.
