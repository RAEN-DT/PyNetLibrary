<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: the PyNET VS Code viewer's MCP tools (`viewer_*`)

Reference for the `mcp__pynet-bridge__viewer_*` tools that drive the embedded viewer (ThatOpen /
web-ifc) from the AI side. See [docs/pnt-export.md](pnt-export.md) for how the `.pnt`
itself is built; this file is about **operating an already-loaded package** — selecting, isolating,
highlighting clashes, reading properties.

Source of truth for the tool signatures: `pynet_mcp/server.py` in the **`PyNetBridge`** repo
(installed via `uv tool` — see [bridge-troubleshooting.md](bridge-troubleshooting.md); never edit
the copy under `AppData\Roaming\uv\tools\...\site-packages`).
Source of truth for viewer behaviour: `viewer/src/main.ts` in the **PyNetVSCode** repo.

> If the `viewer_*` tools are **missing from the session** or a call returns
> `MCP error -32000: Connection closed`, the viewer is probably fine — the bridge failed to launch.
> Work [docs/bridge-troubleshooting.md](bridge-troubleshooting.md) before assuming the viewer is
> unavailable.

---

## Tool reference

| Tool | What it does | Notes |
|---|---|---|
| `viewer_status` | Reports whether a viewer is open (port, package, dataDir). | Call first — everything else needs a running viewer. |
| `viewer_load_package(pnt_path)` | Loads a `.pnt` into the open viewer. | Returns a summary read from `clashes.json`. |
| `viewer_get_state` | Reads the viewer's last reported state: `{"models": [...], "selected": <pnt_id or null>}`. | `selected` is whatever currently has the "select" highlight — a click in the 3D view, the tree panel, or the last `viewer_select` call. `null` if nothing is selected. |
| `viewer_list_clashes` | Reads the loaded package's `clashes.json` (the data source, not live IFC). | **Can be huge** — a federated model can return thousands of clash rows (~1 MB). Prefer filtering client-side (see "Filtering clashes" below) over dumping the whole list into a response. |
| `viewer_get_properties(pnt_ids?, model?, search?, limit?, offset?)` | Reads element properties from `properties.json`. | Pass `pnt_ids` for full properties (psets included). With no `pnt_ids`, returns a **paginated** lightweight index (`pnt_id`, `name`, `model`) — narrow with `model` (exact discipline name) and/or `search` (substring of the name), page with `limit`/`offset` (default 200, capped at 500). |
| `viewer_select(pnt_ids, pnt_ids_b?)` | Highlights one or two groups of elements by pnt_id, **neutral colours** (yellow `select` / blue `select-b`), nothing hidden. | Distinct channel from clash highlighting — does not isolate, does not use clash red/green. |
| `viewer_highlight_clash(pnt_id_a?, pnt_id_b?)` | Highlights a clash (A red, B green) and **isolates** the pair (hides everything else). | Separate style/channel from `viewer_select` (fixed 2026-07-14 — they used to collide). Either side accepts a **list** (fixed 2026-07-14) — e.g. one element (A) against every counterpart it clashes with (B), all shown at once. |
| `viewer_isolate(pnt_ids)` | Hides everything except the given pnt_ids. | |
| `viewer_isolate_models(models)` | Hides every loaded model except the named ones (whole disciplines). | Bridge **≥ 1.5.4**. Use for "just show me HVAC" — far cheaper than resolving every element id and calling `viewer_isolate`. Names must match `viewer_get_state`. |
| `viewer_fit` | Fits the camera to all loaded models. | Use after `viewer_clear` — clearing a highlight does **not** refit the camera, it stays zoomed on the last isolated selection. |
| `viewer_clear` | Clears highlights and un-isolates (shows everything again). | Does not move the camera — follow with `viewer_fit` if you isolated/zoomed before. |

## Typical flows

**Show one clash pair:**
```
viewer_list_clashes                      # find a pnt_id_a / pnt_id_b pair
viewer_highlight_clash(pnt_id_a, pnt_id_b)
```

**Show all clashes of one element against its (possibly varied) counterparts, isolated:**
Not a single tool call — filter `clashes.json` for rows where `pnt_id_a` or `pnt_id_b` equals the
element's id, collect the *other side* of each row, then:
```
viewer_highlight_clash(pnt_id_a=<the element>, pnt_id_b=[<all counterparts>])
```
`pnt_id_b` (and `pnt_id_a`) accept a list, not just one id — the element renders red, every
counterpart green, rest of the model isolated away. (Demonstrated 2026-07-14 with a beam
clashing against two separate walls — both showed correctly alongside the beam, isolated.)

**"What does the user have selected right now, and what does it clash with?"**
```
viewer_get_state                         # -> selected: <pnt_id>
# filter clashes.json for rows where pnt_id_a/pnt_id_b == <pnt_id>, collect the other side
viewer_highlight_clash(pnt_id_a=<pnt_id>, pnt_id_b=[<counterparts>])
```

**Show elements with neutral colours, no isolation, but still findable in a huge federated
model:** plain `viewer_select` alone tends to get visually lost — nothing else is hidden, so
the highlighted elements can be occluded by whatever's in front of the camera. Chain it with
`viewer_isolate` (same ids, union of both groups) instead:
```
viewer_select(pnt_ids=[...], pnt_ids_b=[...])   # sets the yellow/blue colours
viewer_isolate(pnt_ids=[...all ids from both groups...])  # hides everything else
```
Order matters — `viewer_select` always un-isolates first (it's designed to never isolate on its
own), so isolate must come *after* select, not before. A manual click in the viewer also repaints
the yellow group (they share the same "select" style), so re-issue `viewer_select` afterward if
that happens, then `viewer_isolate` again.

**Reset the view:**
```
viewer_clear
viewer_fit
```

## Filtering clashes without blowing the token budget

`viewer_list_clashes` reads straight from `clashes.json` inside the package's data dir
(`~/.pynet_viewer/<package>/clashes.json`) — nothing stops you from reading/filtering that file
directly (PowerShell `ConvertFrom-Json` / `Where-Object`, or a short Python/Node script) instead
of going through the MCP tool when you need a subset; it has no `model=`/`search` filter of its
own the way `viewer_get_properties` now does. The raw `clashes[]` rows carry `Test`, `Status`,
`Element A`/`Element B` (display names) and `pnt_id_a`/`pnt_id_b`. Example discipline-code prefixes
from a validated project's test names: `EST` structural, `ARQ` architectural, `HVA` HVAC, `ELE`
electrical, `PLU` plumbing; `PIL` columns, `ARM` framing/joists, `LOS` slabs (`Suelo` in
`Element A/B`), `MUR` walls (`Muro básico`), `CON` ducts (`Conducto redondo`), `TUB` pipes.

---

## Behaviour notes

- `viewer_highlight_clash` and `viewer_select` use separate channels (red/green + isolate vs neutral
  yellow/blue, no isolate). Both sides of either accept a list.
- `viewer_get_properties()` without `pnt_ids` is paginated (`limit`/`offset`, max 500) — a federated
  model has ~13k elements; never request it unfiltered in one call.
- Load failures inside the webview surface in VS Code (error message + output channel) — if a model
  "never appears", check there before retrying.
- Tools missing or a new tool not showing up after an update → [bridge-troubleshooting.md](bridge-troubleshooting.md)
  (dual install, reinstall, reload).
