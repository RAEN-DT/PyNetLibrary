<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: models, federations and batch runs (Navisworks)

Read [navisworks.md](navisworks.md) first. Reference scripts:
`01_ModelManagement/ModelManagement.py`, `00_Workflows/UpdateModels.py`,
`00_Workflows/CoordinationWorkflow.py`, `00_Workflows/BatchClashExport.py`.

---

## Open, append, save, publish

```python
from System.Collections.Generic import List
from Autodesk.Navisworks.Api import PublishProperties, NwdExportOptions
from System import DateTime

doc.OpenFile(path)                     # raises on failure
ok = doc.TryOpenFile(path)             # returns bool instead of raising
doc = Application.ActiveDocument       # take the active document again after opening

files = List[str]()
files.Add(path_a); files.Add(path_b)
doc.AppendFiles(files)                 # or TryAppendFiles(files)

doc.SaveFile(nwf_path)                 # .nwf (links) or .nwd

props = PublishProperties()
props.Author = "PyNET"; props.PublishDate = DateTime.Now; props.EmbedDatabaseProperties = True
doc.PublishFile(nwd_path, NwdExportOptions(), props)   # 3 arguments since Navisworks 2026
```

- **`PublishFile` needs `NwdExportOptions` since Navisworks 2026.** The old 2-argument call fails.
  `NwdExportOptions.FileVersion` pins the NWD version; leave it unset for the installed default.
- Skip files already loaded before appending: compare against `[m.FileName for m in doc.Models]`.

## Building a federation from scratch

**Navisworks cannot create a blank file.** Start from a *seed* `.nwf` and build on it:

1. `OpenFile(seed)`.
2. Remove anything the seed already carries: select every model root and delete it through COM —
   ```python
   loaded = ModelItemCollection()
   for m in doc.Models:
       loaded.Add(m.RootItem)
   doc.CurrentSelection.CopyFrom(loaded)
   ComApiBridge.State.DeleteSelectedFiles()
   ```
3. `AppendFiles(sources)` → create SearchSets → create clash tests → `SaveFile(target)`.

Make every step **idempotent** (skip SearchSets / tests whose name already exists) so the build can
be re-run after the source models change.

## The coordination Excel (UpdateModels / CoordinationWorkflow)

| Sheet | Columns |
|---|---|
| `FederateModels` | `Model` · `Path` (the built `.nwf`) · `Seed` |
| `ModelsMatrix` | `Model` · `Path` · `Extension` · one column per federation, `X` = include |
| `ClashMatrix` | `Description` · `PYNET_Classification` · one column per code, `A`/`B`/`C` = test + tolerance (10/25/50 mm) |

Test names built from it: `{letter}_{row}_vs_{col}` (see clash-dashboard.md for parsing).

**Portable paths.** Paths typed in the Excel carry the author's user folder. Rebase them on the
current user before opening:

```python
def resolve_path(raw):
    parts = list(Path(str(raw)).parts)
    for i in range(len(parts) - 1):
        if parts[i].lower() == "users":
            return Path.home().joinpath(*parts[i + 2:])
    return Path.home() / Path(str(raw))
```

**Project folders** used by the weekly workflow, next to each federation: `01_nwf/` (working
federations, plus a `<version>/` backup), `02_nwd/<version>/` (published NWD), `03_data/<version>/`
(clash CSV and model list).

## Batch over several files

```python
for path in models:
    document = Application.ActiveDocument
    if not document.TryOpenFile(str(path)):
        raise Exception(f"Could not open {path}")
    document = Application.ActiveDocument          # re-take it: the open replaced the content
    clash = CastUtils.CastTo[DocumentClash](document.Clash)
    ...
```

## Clash engine and review round-trip

- **Running the clash engine with no tests defined crashes Navisworks.** Check first:
  `if not get_clash_tests(clashDoc): return`.
- `TestsRunAllTests()` recomputes **every** test — on a big federation it is the slow step. Offer to
  export existing results without recomputing when the user only needs a report.
- **Carry review decisions across runs** with Navisworks' XML clash report: `clashtest@name` →
  `clashresult@guid`, `@status`, `comments/comment/body`. Match results by **GUID** and re-apply
  status + comments (`03_ClashDetection/ImportClashResults.py`).
- Rename a test with `testsData.TestsEditDisplayName(test, new_name)`.
