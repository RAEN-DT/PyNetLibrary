<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: building an HTML / Plotly dashboard or report

Read this **before writing any script that renders a chart-based report or dashboard** (AGENTS.md
§5). Covers the two patterns in use, the layout bug that recurs when Plotly is embedded in a flex
container, and where the reference implementations live.

Related: [clash-dashboard.md](clash-dashboard.md) (clash-specific structure, colors, test-naming) ·
[pnt-export.md](pnt-export.md) · [viewer-mcp.md](viewer-mcp.md)

---

## Two patterns — pick one, don't mix them

| | Static HTML report | Live Dash app |
|---|---|---|
| When | One-shot report/snapshot (clash lists, schedule crossovers, QC audits, takeoffs) | Something changes *while the script keeps running* (live memory/progress during a long batch) |
| How | Build a `str` in Python, `Path.write_text(...)`, `webbrowser.open(...)` | `dash.Dash`, `app.run(port=..., debug=False, use_reloader=False)`, `webbrowser.open("http://127.0.0.1:<port>")` |
| Reference | `01_Scripts/01_Navisworks/08_DataAnalysis/ClashDashboard.py`, `ClashScheduleReport.py` | `01_Scripts/01_Navisworks/00_Workflows/CoordinationDashboard.py` |
| Charts | Plotly (`graph_objects` + `plotly.offline.plot(output_type="div")`, JS embedded inline) or raw inline SVG for simple donuts/bars | Plotly via `dash.dcc.Graph`, refreshed by a `dcc.Interval` callback |

Never publish a Claude Artifact for either — see AGENTS.md §5.

---

## The flex-container resize bug (static HTML + Plotly)

**Symptom:** a chart renders squeezed into a corner of its box, with a blank gap next to it, as if
it kept an old, narrower width — e.g. a donut chart rendered small and shifted while its stacked bar
neighbor looks fine, or vice versa. Verified on `ClashScheduleReport.py` (2026-09-29): a
`Distribucion global de prioridad` donut inside a `display:flex` two-column layout rendered at a
fraction of its column width, with white space filling the rest of the box.

**Cause:** `plotly.offline.plot(..., output_type="div")` emits `Plotly.newPlot(id, data, layout,
{"responsive": true})` in an inline `<script>` that runs **synchronously as the browser parses that
point in the DOM** — before the surrounding flex container (`.charts { display:flex }`) has settled
its children's final widths. `responsive: true` only re-measures on the window's own `resize`
event, not when a flex ancestor's computed width changes on its own, so a chart that was measured
too early never self-corrects.

**Fix:** after all charts are in the DOM, force one resize pass once the page has fully loaded:

```html
<script>
window.addEventListener('load', function() {
  document.querySelectorAll('.plotly-graph-div').forEach(function(div) { Plotly.Plots.resize(div); });
});
</script>
```

Put this right before `</body>`, after every `{chart}_div` has been inserted. See
`ClashScheduleReport.py` for the full pattern (KPI row + two `.chart-box` columns + this snippet).

**Alternative — only for a live Dash app, not a static report:** `CoordinationDashboard.py` sidesteps
the bug entirely by giving each `dcc.Graph` a fixed CSS width and `config={"responsive": False}` +
`update_layout(autosize=False)`. That trades responsiveness (the chart never resizes to the browser
window) for never hitting the timing issue — acceptable for a local live dashboard the user opens
once, wrong for a static report meant to be viewed on different screens.

---

## Rules

- Embed `pyo.get_plotlyjs()` inline — the file must be self-contained, no internet dependency.
- Charts that sit inside a `display:flex` or `display:grid` container: add the resize-on-load
  snippet above. A single full-width chart with no flex siblings does not need it.
- Output path convention: `Path.home() / "AppData" / "Roaming" / "Pynet" / "Navisworks" /
  f"{ReportName}_{doc_name}_{YYYYMMDD_HHMMSS}.html"`.
- Open with `webbrowser.open(...)` from inside the host script at the end of the run.
- A script whose business logic is specific to one project (classification codes, site layout
  assumptions, hardcoded groupings) still belongs in the library if the *rendering pattern* is
  reusable — note which parts are project-specific in a module docstring, the way
  `ClashScheduleReport.py` does, instead of leaving future readers to guess.
