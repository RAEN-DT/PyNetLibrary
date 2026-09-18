# Skill: ClashDetection

Full Clash Detection workflow for the PyNET platform on Autodesk Navisworks.

> **Read first:** [docs/navisworks.md](../../docs/navisworks.md) — boilerplate, `CastUtils`, the
> `pynet_clash` helpers (`get_clash_tests`, `iter_results`) and the heavy-model rules.
> **Loaded on demand by step:** [clash-approval-criteria.md](../../docs/clash-approval-criteria.md) (step 10) ·
> [clash-review.md](../../docs/clash-review.md) (steps 11–12: images, status, comments, grouping) ·
> [clash-dashboard.md](../../docs/clash-dashboard.md) (step 13).
>
> **Related skill:** [ClashCoordination.md](ClashCoordination.md) — takes the Reviewed results from this
> workflow and creates the floor openings in Revit.

## Context

- Classification parameter: `PYNET_Classification` — a **type parameter** that appears at multiple hierarchy levels
- Tolerances, centers and distances are in **document units** (feet only if the model is in feet) → convert with
  `UnitConversion.ScaleFactor` (`mm_to_doc` below), never a fixed `0.3048`
- Clash tests must reference **dynamic SearchSets**, never static snapshots via `CopyFrom(FindAll(...))`
- Iterate tests/results only through `get_clash_tests(clashDoc)` / `iter_results(test)` — never
  `testsData.Tests` or `testsData.Value.TestsRoot.Children` directly (API changed between versions)

### PYNET_Classification — where it appears

In a Navisworks NWC the Revit type parameter appears in **three** places:

| Where | Internal category | Display name | hasGeometry |
|---|---|---|:---:|
| TYPE container node (class=Tipo) | `lcldrevit_tab_type` | `"Tipo"` | False |
| Instance node (class=element) | `LcRevitData_Type` | `"Tipo de Revit"` | False |
| Instance node (shared param export) | `LcRevitData_TypeCustom` | `"Tipo Personalizar"` | False |

**Discovery and coverage** (step 2) scan the TYPE container nodes (`ClassDisplayName == "Tipo"`) — one
node per type, cheap. **SearchSets** (step 4) use whichever category the Search API actually resolves
to geometry — measured, not assumed (see step 4).

### Imports

```python
clr.AddReference("Autodesk.Navisworks.Api")
from Autodesk.Navisworks.Api import (Application, Search, SearchCondition, SearchLocations,
                                     SelectionSet, UnitConversion, Units, VariantData)
clr.AddReference("Autodesk.Navisworks.Clash")
from Autodesk.Navisworks.Api.Clash import DocumentClash, ClashTest, ClashTestType
from System.Collections.Generic import List

def mm_to_doc(mm):
    """Millimetres -> document units (what ClashTest.Tolerance expects)."""
    scale = UnitConversion.ScaleFactor(doc.Models.First.Units, Units.Meters)   # metres per doc unit
    return mm * 0.001 / scale

TEST_NAME_FORMAT = "{a} vs {b}"   # the PROJECT's naming convention (step 5) - this is only the default

clashDoc = CastUtils.CastTo[DocumentClash](doc.Clash)   # CastUtils: see docs/navisworks.md
testsData = clashDoc.TestsData
```

## Workflow

### 1. Verify active session
Use `list_active_instances` to get the active PID.

### 2. Discover and validate the classification parameter

**Every federated model is different. Never assume a fixed parameter name or property category — always discover first.**

#### Step 2a — Discovery: find the classification parameter

Ask the user: *"Which parameter is used to classify elements in this project?"*

If the user doesn't know or wants you to detect it automatically, run a discovery scan.

> ⚠ **Performance — mandatory, this caused a real production incident (session hang, forced Navisworks
> restart, twice in the same afternoon).** Never scan `model.RootItem.Descendants` unfiltered — every
> property read is a pythonnet↔.NET interop call, and Navisworks re-exposes the TYPE node's value on
> every instance under it. **Always filter to container nodes first** (`ClassDisplayName == "Tipo"`).
> Measured: unfiltered scan over one 9,710-descendant model hung past 120 s; filtered to 131 `"Tipo"`
> nodes it finished in **~1 s**. The number of interop calls is the bottleneck, not model size.

```python
from collections import defaultdict

# (cat_internal, cat_display, prop_display) → set of unique values found
param_index = defaultdict(set)

for model in doc.Models:
    for item in model.RootItem.Descendants:
        if item.ClassDisplayName != "Tipo":   # container nodes only — see perf note above
            continue
        for cat in item.PropertyCategories:
            for prop in cat.Properties:
                try:
                    val = prop.Value.ToDisplayString()
                    if val:
                        param_index[(cat.Name, cat.DisplayName, prop.DisplayName)].add(val)
                except:
                    pass

# Score candidates: prefer short distinct values (codes)
results = []
for (cat_int, cat_disp, prop_disp), values in param_index.items():
    avg_len = sum(len(v) for v in values) / len(values) if values else 0
    results.append({
        "category_internal": cat_int,
        "category_display": cat_disp,
        "property": prop_disp,
        "unique_values": sorted(values)[:20],
        "unique_value_count": len(values),
        "score": len(values) if avg_len <= 20 else 0,
    })
results.sort(key=lambda x: -x["score"])
ia_Result = results[:20]
```

After the scan, **propose the best candidate(s)** before asking the user to confirm:

- **Best candidate criteria:** short unique values (2–10 chars), 3–20 distinct values, present across all models, name suggests classification ("classification", "type", "code", "clase", "tipo").
- **Present a ranked shortlist** (top 3–5), say why each is good or poor, and state your recommendation.
- Then ask: *"Is this the parameter you want to use, or do you prefer another one from the list?"*

**Do not proceed to 2b until the user has confirmed the parameter name and its property category.** Store:
- `PARAM_DISPLAY_NAME` — display name of the property (e.g. `"PYNET_Classification"`)
- `PARAM_CAT_INTERNAL` — internal category name where it lives (e.g. `"lcldrevit_tab_type"`)
- `PARAM_CAT_DISPLAY` — display name of that category — candidate for the SearchSet condition

#### Step 2a-fallback — no classification parameter found (test/sample models)

Some models (generic Autodesk samples, test federations) carry no custom classification — the scan
returns only dimensional properties (width, area, weight…), never short codes. **Do not silently pick a
fallback basis — ask the user.** Options:

- **By native Revit Category** — container level `ClassDisplayName == "Categoría"` (one level above
  `"Tipo"`, even fewer nodes, ~1 s across 5 federated models):
  ```python
  for item in model.RootItem.Descendants:
      if item.ClassDisplayName == "Categoría":
          category_counts[item.DisplayName] += 1
  ```
  Each category name ("Muros", "Tuberías", …) becomes a code; the container node's `DisplayName` IS the
  code (no property lookup). For SearchSets combine `Archivo de origen` + `Categoría` so a category is
  scoped to its discipline model.
- **By discipline/source model** — one code per federated NWC. Coarser; hides intra-discipline conflicts.
- **Any other property the user names** — treat it like a confirmed parameter from step 2a.

Whichever basis is chosen, confirm exclusions explicitly (e.g. rebar — embedded in concrete, usually no
coordination value — ask, do not assume).

#### Step 2b — Validation: parameter populated and coverage

Validate each model at **TYPE node level** — the unit SearchSets target, so the unit where gaps matter.

- Filter `item.ClassDisplayName == "Tipo"` — never scan all descendants blindly.
- Use `hash(item)` (not `id(item)`) — pythonnet creates a new wrapper on each `.Parent` access.
- Count geometry **downward** from classified TYPE nodes (`.Descendants`); upward via `.Parent` is unreliable.
- A `covered_geo_hashes` set avoids double-counting geometry under several TYPE nodes.

```python
from collections import defaultdict

PARAM_DISPLAY_NAME = "..."   # from step 2a
PARAM_CAT_INTERNAL = "..."   # from step 2a

results = []
for model in doc.Models:
    model_name = model.FileName.split("\\")[-1]
    classified_types, unclassified_types = {}, []

    for item in model.RootItem.Descendants:           # pass 1: classify TYPE nodes
        if item.ClassDisplayName != "Tipo":
            continue
        code = None
        for cat in item.PropertyCategories:
            if cat.Name != PARAM_CAT_INTERNAL:
                continue
            for prop in cat.Properties:
                if prop.DisplayName == PARAM_DISPLAY_NAME:
                    try:
                        code = prop.Value.ToDisplayString() or None
                    except:
                        pass
        if code:
            classified_types[hash(item)] = code
        elif len(unclassified_types) < 15:
            unclassified_types.append(item.DisplayName or "(sin nombre)")

    code_counts, covered = defaultdict(int), set()    # pass 2: geometry under classified types
    for item in model.RootItem.Descendants:
        if item.ClassDisplayName != "Tipo" or hash(item) not in classified_types:
            continue
        code = classified_types[hash(item)]
        for desc in item.Descendants:
            if desc.HasGeometry and hash(desc) not in covered:
                covered.add(hash(desc))
                code_counts[code] += 1

    total_geo = sum(1 for it in model.RootItem.Descendants if it.HasGeometry)
    classified_geo = sum(code_counts.values())
    results.append({
        "model": model_name,
        "total_type_nodes": len(classified_types) + len(unclassified_types),
        "classified_types": len(classified_types),
        "unclassified_type_names": unclassified_types,
        "total_geometry_elements": total_geo,
        "classified_geo": classified_geo,
        "coverage_pct": round(classified_geo / total_geo * 100, 1) if total_geo else 0.0,
        "elements_per_code": dict(sorted(code_counts.items())),
    })
ia_Result = results
```

**Always present the coverage report (TYPE nodes, not just geometry %) before proceeding:**

| Model | Type nodes | Classified | Unclassified types | Geo coverage |
|-------|:----------:|:----------:|:------------------:|:------------:|
| ModelA_ARQ.nwc | 5 | 3 | 2 | 66.7 % |

**Investigate unclassified TYPE nodes before flagging them:**
- **Reference/auxiliary elements** (level markers, axes, grids, construction planes) — legitimate, not an error.
- **Real buildable elements** (walls, columns, slabs, pipes, ducts) — a real gap: their geometry is invisible to clash tests. Report and ask the user.

```
Unclassified TYPE nodes:
  ✓ "Extremo inicial 8 mm" — level marker (reference element, expected)
  ✗ "Interior - bloques 140 mm" — wall type missing classification (real gap)
```

**Category consistency:** if the internal category holding the parameter differs between models,
SearchSet conditions must be built per model — flag it and ask before continuing.

### 3. Discover model classifications
Already obtained in 2b. Build `{code: (cat_internal, cat_display)}` per model for the SearchSets.

### 4. Create SearchSets (one per code)

**The category that works in the Search API is not necessarily where the parameter was found.** Test
every candidate and use the one returning the most elements — typically `"Tipo"` alone returns only the
TYPE container (1 item, no visible geometry), while `"Tipo de Revit"` returns the instance nodes that
parent the geometry. Measure it on each project:

```python
for cat_display in ["Tipo", "Tipo de Revit", "Tipo Personalizar"]:  # adapt to project
    search = Search()
    search.Locations = SearchLocations.DescendantsAndSelf
    search.Selection.SelectAll()
    cond = SearchCondition.HasPropertyByDisplayName(cat_display, PARAM_DISPLAY_NAME).EqualValue(
        VariantData.FromDisplayString(some_known_code))
    cond_list = List[SearchCondition]()
    cond_list.Add(cond)
    search.SearchConditions.AddGroup(cond_list)
    print(f"{cat_display}: {sum(1 for _ in search.FindAll(doc, False))} items")
```

> `AddGroup` semantics: conditions in the **same** `AddGroup(list)` call are ANDed; separate groups are
> ORed with each other. Plain `Add(condition)` at the top level ANDs with everything else.

Create and **always verify** each SearchSet before saving:

```python
CAT_DISPLAY = "..."   # confirmed by the test above
CODES = [...]         # discovered in step 2

results = []
for code in CODES:
    search = Search()
    search.Locations = SearchLocations.DescendantsAndSelf
    search.Selection.SelectAll()
    cond = SearchCondition.HasPropertyByDisplayName(CAT_DISPLAY, PARAM_DISPLAY_NAME).EqualValue(
        VariantData.FromDisplayString(code))
    cond_list = List[SearchCondition]()
    cond_list.Add(cond)
    search.SearchConditions.AddGroup(cond_list)

    count = sum(1 for _ in search.FindAll(doc, False))   # never create an empty SearchSet
    if count == 0:
        results.append({"code": code, "status": "EMPTY — not created", "items": 0})
        continue
    ss = SelectionSet(search)
    ss.DisplayName = code
    doc.SelectionSets.AddCopy(ss)
    results.append({"code": code, "status": "OK", "items": count})
ia_Result = results
```

Report the verification table (Code · Items · Status). If any set is EMPTY, investigate before
continuing — a missing set makes that discipline invisible in every clash test.

### 5. Propose the theoretical matrix — MANDATORY USER CONFIRMATION

**Always send the full matrix and wait for explicit confirmation before creating any clash test.**

**Table 1 — triangular matrix** (all codes on both axes, upper triangle only):
**A** = 10 mm (MEP vs any element) · **B** = 25 mm (PIL vs ARQ) · **C** = 50 mm (LOS vs ARQ) · **—** = same model, no test

|  | **FAC** | **MUR** | **PAR** | **LOS** | **PIL** | **CON** | **TUB** |
|--|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
| **FAC** | — | — | — | C | B | A | A |
| **MUR** | | — | — | C | B | A | A |
| **PAR** | | | — | C | B | A | A |
| **LOS** | | | | — | — | A | A |
| **PIL** | | | | | — | A | A |
| **CON** | | | | | | — | — |
| **TUB** | | | | | | | — |

**Table 2 — test list:** Test · Selection A · Selection B · Tolerance.

**Test naming is a project input.** Ask how the project names its tests (e.g. `CON vs MUR`,
`A_CON_vs_MUR`, `ARQ-MUR_x_MEP-CON`…) and use it for every test. Default when the project has none:
`{A} vs {B}`. The dashboards and reports must then parse that same convention (clash-dashboard.md).

Rule: **never create intra-model tests** (elements of the same NWC do not clash against each other).
Proceed only after the user confirms the matrix (or requests changes).

### 6. Create ClashTests referencing SearchSets

```python
def find_set(root, name):
    for item in root.Children:
        if item.DisplayName == name:
            return item
        if item.IsGroup:
            found = find_set(item, name)
            if found:
                return found
    return None

source_a = doc.SelectionSets.CreateSelectionSource(find_set(doc.SelectionSets.RootItem, code_a))
source_b = doc.SelectionSets.CreateSelectionSource(find_set(doc.SelectionSets.RootItem, code_b))

test = ClashTest()                  # a new, detached test — its properties are writable
test.DisplayName = TEST_NAME_FORMAT.format(a=code_a, b=code_b)   # project convention, default "{a} vs {b}"
test.TestType = ClashTestType.Hard
test.Tolerance = mm_to_doc(10)
test.SelectionA.Selection.SelectionSources.Add(source_a)
test.SelectionB.Selection.SelectionSources.Add(source_b)
testsData.TestsAddCopy(None, test)  # None = root level
```

### 7. Apply tolerances

Standard criteria — adjust with the user: LOS vs ARQ (MUR/FAC/PAR) 50 mm · PIL vs ARQ 25 mm ·
MEP vs any element 10 mm.

A live test is read-only (`test.Tolerance = x` raises `NotSupportedException`). Edit through a copy:

```python
new_test = live_test.CreateCopy()
new_test.set_Tolerance(mm_to_doc(50))   # pattern verified in ClashToleranceComparison
testsData.TestsEditTestFromCopy(live_test, new_test)
```

### 8. Run the tests

```python
testsData.TestsRunAllTests()
```

### 9. Report results

`for test in get_clash_tests(clashDoc): sum(1 for _ in iter_results(test))` per test.

### 10. Preliminary analysis — propose Approve / Reviewed

Read [clash-approval-criteria.md](../../docs/clash-approval-criteria.md). Extract per result: name,
category, PYNET code, diameter, 3D center; apply the rules. Present:

| # | Test | Depth | Element A | Ø | Element B | Proposal | Reason |
|---|------|:---:|---|:---:|---|:---:|---|

Ask the user to confirm or adjust before applying anything.

### 11. Visual analysis of doubtful clashes

If there are **Reviewed** clashes (or cases the rules could not decide), ask:

> "I have **X** clashes flagged as Reviewed. Do you want me to generate and analyze an image for each one before applying the statuses?"

If yes: render them ([clash-review.md](../../docs/clash-review.md) → images), read each image, describe
the conflict, revise the proposal if the image shows something the data missed, and present the final
table for confirmation before writing any status.

### 12. Apply statuses and comments, then group

Only after the user confirms the final proposal, following [clash-review.md](../../docs/clash-review.md):

1. **Status** with `TestsEditResultStatus`.
2. **Comment** with `TestsEditResultComments` (`CommentCollection`, not a string):
   `f"[Auto-review {run_date}] {reason}"`.
3. **Group** related clashes — `group_by_shared_element` per test, **last** (it changes the iteration structure).

> ⚠ **Performance — write-heavy loop.** Two API calls per result; thousands of results is real work.
> Print progress every test (or every N results), time a small test first to set a realistic timeout,
> and if `send_command` times out **do not send anything else to that session** — it is very likely
> still running. Stop, tell the user, wait for confirmation, then verify by reading back a sample of
> `result.Status`. See docs/navisworks.md "Heavy models".

### 13. Generate the HTML dashboard

Build it per [clash-dashboard.md](../../docs/clash-dashboard.md) and open it with `webbrowser.open()`.

---

<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->
