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

**Test names are a project input, not a fixed format.** The ClashDetection skill is a base adapted
per project: the naming convention comes from the project (asked in the skill, step 5) and the
dashboard must parse *that* convention. Default when the project defines none: `CON vs MUR`.
`00_Workflows/UpdateModels.py` is a separate, rigid workflow with its own fixed convention
(`A_CON_vs_MUR`: tolerance letter + `_vs_`) — never align one to the other. The library's chart and
dashboard scripts accept both out of the box (`re.split(r"\s+vs\s+|_vs_", name)`, dropping a leading
`^[ABC]_`); a project with another convention adapts that split.

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
