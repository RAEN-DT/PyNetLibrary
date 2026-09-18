<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Reference: clash HTML dashboard (Navisworks)

Used by the `ClashDetection` skill, step 13 — after statuses and groups are applied. Reference
implementation: `01_Scripts/01_Navisworks/08_DataAnalysis/ClashDashboard.py` (static HTML +
`webbrowser.open`). Not `04_DataAnalysis/ExportClashDashboard.py` — that one launches a Dash server
and a pywebview window, a different pattern.

**Navisworks status colors — always these, no exceptions:**

| Status | Color |
|--------|-------|
| New | `#ef4444` (red) |
| Active | `#f97316` (orange) |
| Reviewed | `#3b82f6` (blue) |
| Approved | `#22c55e` (green) |
| Resolved | `#eab308` (yellow) |

**Test names — two formats in use, parse both:** `CON vs MUR` (ClashDetection skill,
`CreateClashTest.py`) and `A_CON_vs_MUR` (`00_Workflows/UpdateModels.py`: tolerance letter A/B/C +
`_vs_`). Split with `re.split(r"\s+vs\s+|_vs_", name)` and drop a leading `^[ABC]_`. Do not rename
existing tests to unify them: `UpdateModels` skips tests whose name already exists, so a renamed
convention would duplicate every test on the next federation build.

**Must include:**
- KPI row: total clashes + one KPI per status present + number of federated models (KPI border-top
  color = status color)
- **Donut chart** — global status distribution
- **Stacked horizontal bar** — clashes per test, colored by status
- **Grouped bar** — clashes per discipline code, colored by status
- **Models table + bar** — model file names and geometry element count
- **Detail table** — every clash with test, group, status badge and reason (strip the
  `[Auto-review YYYY-MM-DD]` prefix for readability)

**Output path:** `Path.home() / "AppData" / "Roaming" / "Pynet" / "Navisworks" / f"ClashReport_{doc_name}_{YYYYMMDD_HHMMSS}.html"`

**Implementation notes:**
- `plotly.graph_objects` + `plotly.offline.plot(output_type="div")`; embed `pyo.get_plotlyjs()`
  inline so the file is self-contained (no internet dependency).
- Iterate with `get_clash_tests` + `iter_results` (grouped and flat results).
- Open with `webbrowser.open(str(html_path))` at the end of the script — never a Claude Artifact.
