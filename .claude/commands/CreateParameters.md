# Skill: CreateParameters

Start the conversation in english. If the user requests to change you can use the user language.

Creates Revit **shared parameters** from an Excel matrix and binds them as **project parameters**
(Type or Instance) to the categories the matrix marks, in a single transaction. Re-runnable: existing
definitions and bindings are reused/`ReInsert`-ed, not duplicated.

## Context

- **Host:** Revit only (uses `__revit__` global)
- **Write script** — creates shared parameter definitions and binds project parameters. Follows
  the standard confirmation policy (CLAUDE.md §8): confirm once before the first execution.
- **Input Excel:** always asked to the user, every run — never hardcoded, never reused silently
  from a previous session.

---

## Excel structure — what the matrix must provide

There is no rigid column checklist to run. When the user gives an Excel, open it and judge on the
spot whether it is actually a parameter-creation matrix — the shape below is the reference for what
"usable" looks like, not a validator to pass/fail mechanically.

**Sheet `Parametros`** — one row per shared parameter definition:

| Column (by position) | Meaning |
|---|---|
| `Uso` | Free-text note (not used by the automation) |
| `PSet` | DefinitionGroup name — parameters sharing a `PSet` are grouped together in the shared parameter file |
| `Nombre` | The parameter name (also the Excel `Matriz` column header that references it) |
| `Formato` | Data type key — see the Formato map below |
| `TipoOEjemplar` | `T` = Type parameter, `E` = Instance parameter |
| `GrupoRevit` | Revit parameter group (UI grouping) — see the GrupoRevit map below |

**Sheet `Matriz`** — one row per category, one column per parameter:

- First 3 columns: `Grupo` (discipline/free label), `Categoria` (display name), `BuiltInCategory`
  (exact enum name, e.g. `OST_Walls`)
- Remaining columns: one per parameter `Nombre` from the `Parametros` sheet. Mark `T` or `E` in a
  cell to bind that parameter to that category as Type or Instance respectively (must match what
  `Parametros.TipoOEjemplar` says for that parameter — the script does not cross-validate the two,
  so check it by eye if something looks off)

**Minimum for a usable Excel:** both sheets present, `Parametros.Nombre`/`Formato`/`TipoOEjemplar`/
`GrupoRevit` filled for every row that should be created, and at least one `T`/`E` marked per
parameter in `Matriz` (a parameter with no marked category is skipped with a warning, not an error).

---

## Formato map (Excel → Revit data type)

Implemented in `get_spec_map()`. Extend it in the script whenever the matrix introduces a new key —
this is expected to grow with the project, not a fixed list:

| Excel key | Revit `SpecTypeId` (2022+) | Old `ParameterType` fallback |
|---|---|---|
| `TEXT` | `String.Text` | `Text` |
| `MULTILINETEXT` | `String.MultilineText` | `MultilineText` |
| `URL` | `String.Url` | `URL` |
| `INTEGER` | `Int.Integer` | `Integer` |
| `NUMBER` | `Number` | `Number` |
| `YESNO` | `Boolean.YesNo` | `YesNo` |
| `LENGTH` | `Length` | `Length` |
| `AREA` | `Area` | `Area` |
| `VOLUME` | `Volume` | `Volume` |
| `ANGLE` | `Angle` | `Angle` |

If the Excel uses a `Formato` key not in this table, **add it to `get_spec_map()` before running** —
do not silently drop the parameter or guess a mapping.

## GrupoRevit map (Excel → Revit parameter group)

Implemented in `get_group_map()`, same extend-as-needed rule:

| Excel key | Revit `GroupTypeId` (2022+) | Old `BuiltInParameterGroup` fallback |
|---|---|---|
| `Datos de identidad` | `IdentityData` | `PG_IDENTITY_DATA` |
| `Fases` | `Phasing` | `PG_PHASING` |
| `Datos` | `Data` | `PG_DATA` |
| `Geometria` | `Geometry` | `PG_GEOMETRY` |
| `Materiales y acabados` | `MaterialsAndFinishes` | `PG_MATERIALS` |
| `Construccion` | `Construction` | `PG_CONSTRUCTION` |
| `Mecanico` | `Mechanical` | `PG_MECHANICAL` |
| `Electrico` | `Electrical` | `PG_ELECTRICAL` |
| `Estructural` | `Structural` | `PG_STRUCTURAL` |
| `Texto` | `Text` | `PG_TEXT` |
| `Visibilidad` | `Visibility` | `PG_VISIBILITY` |
| `General` | `General` | `PG_GENERAL` |

Same rule: an unmapped `GrupoRevit` key skips that parameter with a warning — add the key to the map
first if the matrix needs it.

---

## Workflow

### 1. Check active instance
```python
list_active_instances  # must be Revit
```

### 2. Ask the user for the Excel path
Always ask — never reuse a path from a previous run or `AI_History` without the user confirming it
for this run.

### 3. Open and judge the Excel
Read `Parametros` and `Matriz` (e.g. via the Excel-reading pattern in
[docs/excel-mcp.md](../../docs/excel-mcp.md)). Confirm it matches the shape above closely enough to
be usable. Check the `Formato` and `GrupoRevit` values actually used against the two maps above —
flag any key that isn't mapped yet and offer to add it to `get_spec_map()` / `get_group_map()`
before running.

### 4. Ask: reuse or new shared parameter file?

**Killer question — ask every run, do not assume:**

> "A PyNET shared parameter file already exists at `%AppData%\Pynet\Revit\PyNET_SharedParameters.txt`
> (if it does — check first). Reuse it (keep existing definitions, add/update on top) or start a new
> one (existing definitions in that file are discarded)?"

**Check existence via `send_command` (MCP), never via PowerShell/Bash.** This is a CLAUDE.md §9 rule
in general, but it bit us specifically here: a PowerShell `Test-Path` on this same path returned
`False` while the file did exist — checking from inside the Revit host process via `send_command`
(`Path.home() / "AppData" / "Roaming" / "Pynet" / "Revit" / "PyNET_SharedParameters.txt"`, `.exists()`)
gave the correct `True`. Whatever causes the mismatch (different user/env context), treat a
PowerShell/Bash check of this path as unreliable — always confirm through the bridge instead.

If the file doesn't exist yet (per the MCP check), skip the question — there's nothing to reuse.

Set `REUSE_SHARED_FILE = True/False` in the script accordingly.

### 5. Confirm before executing

This is a write script — confirm once before the first run (CLAUDE.md §8). Show the user:
- Excel path
- Parameters found / categories found (counts, not the raw script output)
- Shared parameter file path and reuse/new choice

**Always generate the parameter summary table as part of this confirmation — do not wait to be
asked for it.** One row per parameter (`PSet`, `Nombre`, `Formato`, `TipoOEjemplar`, `GrupoRevit`,
and how many categories it binds to — count them from the `Matriz` sheet columns already read in
step 3). This is the user's chance to catch a wrong Formato/Grupo or an unexpectedly small/large
category count before anything touches the live Revit project.

### 6. Execute via `send_command_by_path`

```python
send_command_by_path(
    pid=<pid>,
    script_name="CreateParameters",
    file_path=r"01_Scripts\02_Revit\00_Workflow\CreateParameters.py",
    timeout=90
)
```

Before sending, update in the file:
- `EXCEL_PATH` → the path from step 2
- `REUSE_SHARED_FILE` → the choice from step 4

### 7. Report results

Natural language (Production mode — no JSON, no script internals): parameters created, parameters
bound to categories, any skipped parameter and why (unmapped Formato/GrupoRevit, or no category
marked in the matrix).

### 8. If it fails and you fix it (unmapped Formato/GrupoRevit key, etc.)

Fix the map in the script and **re-execute immediately without asking again** — the user already
approved the intent (CLAUDE.md §8, "confirmed script fails and you fix it").

---

## Key implementation notes

### Idempotent by design
- `create_shared_param_file()`: resets the `.txt` only when `REUSE_SHARED_FILE` is `False` (or the
  file doesn't exist yet)
- `create_definitions()`: reuses an existing `DefinitionGroup`/`Definition` of the same name instead
  of failing — needed for the reuse path, harmless on a fresh file
- `bind_to_categories()`: `ReInsert` when the binding already exists, `Insert` otherwise — safe to
  re-run against the same project repeatedly

### Category set built from the matrix, not hardcoded
`build_category_set()` reads categories straight from the Excel `BuiltInCategory` column via
`Enum.GetValues(BuiltInCategory)` — no hardcoded category list to maintain in the script.

### No `getattr`/`setattr`
`build_category_lookup()` builds the `BuiltInCategory` name → enum lookup via `Enum.GetValues`, per
the bridge's blocked-calls list (CLAUDE.md §7) — do not reintroduce `getattr(BuiltInCategory, name)`.

---

## Production script

- **Location:** [01_Scripts/02_Revit/00_Workflow/CreateParameters.py](../../01_Scripts/02_Revit/00_Workflow/CreateParameters.py)
- **Single source of truth** — all improvements (new Formato/GrupoRevit keys) go on this file, no
  versioned copies.
- Only change before running: `EXCEL_PATH` and `REUSE_SHARED_FILE` at the top of the file.

---

## Common issues

| Symptom | Cause | Fix |
|---|---|---|
| Parameter skipped: "Grupo Revit desconocido" | `GrupoRevit` key not in `get_group_map()` | Add the key/mapping, re-run |
| `KeyError` on `spec_map[p["Formato"]]` | `Formato` key not in `get_spec_map()` | Add the key/mapping, re-run |
| Parameter skipped: "Sin categorias para" | No `T`/`E` marked for that parameter in `Matriz` | Ask the user to mark at least one category, or confirm it's intentionally unbound |
| `ArgumentException` creating a definition | Reused file already has a same-name definition with a **different type** | Not auto-resolved — ask the user whether to rename or start a new shared parameter file |
| Bindings not visible in the project | Ran outside a `Transaction` or it rolled back | Check the printed error before `t.RollBack()` — script re-raises on failure |
| `name 'BuiltInParameterGroup' is not defined` (or any error pointing at the `except` branch of `get_group_map()`/`get_spec_map()`) | Misleading — the real bug is an **`AttributeError` inside the `try` branch** on a wrong `GroupTypeId`/`SpecTypeId` member name (e.g. `GroupTypeId.MaterialsAndFinishes` doesn't exist; the real member is `GroupTypeId.Materials`), which falls through to the old-API `except` and fails there too, masking the actual cause. When this happens, don't just patch the `except`: check the `try` dict's member names against the stub (`CLASSES.tsv` → `GroupTypeId`/`SpecTypeId`) and fix the real key, then re-run |

---

<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->
