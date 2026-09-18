<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: Revit scripts

Read this guide **before writing any Revit script**. For element queries/measurements, also read [RevitApiPatterns](../.claude/commands/RevitApiPatterns.md). For forms/dialogs read [winforms.md](winforms.md).

Related: [navisworks.md](navisworks.md) · [autocad-civil.md](autocad-civil.md) · [excel-mcp.md](excel-mcp.md)

---

## Standard boilerplate

The plugin injects a `__revit__` global. **Do not use `Application` from the Navisworks namespace — it does not exist in Revit.**

Import **only the types the script uses**, by name — never `from Autodesk.Revit.DB import *` (same
rule and reasons as [navisworks.md](navisworks.md#-never-use-from-namespace-import-)). Check an
uncertain name against the stubs index (`CLASSES.tsv`) before importing it: several legacy types
(`ParameterType`, `BuiltInParameterGroup`) no longer exist in Revit 2025+ — their replacements are
`SpecTypeId` / `GroupTypeId`.

```python
import clr
from pathlib import Path

clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import BuiltInCategory, FilteredElementCollector, Transaction  # what you use

# __revit__ is injected by the plugin — always use this to get the document
doc = __revit__.ActiveUIDocument.Document
```

| | Navisworks | Revit |
|---|---|---|
| Document | `Application.ActiveDocument` | `__revit__.ActiveUIDocument.Document` |
| Main assembly | `Autodesk.Navisworks.Api` | `RevitAPI` |
| UI access | `Application` | `__revit__.ActiveUIDocument` |
| Writes need transaction | No | **Yes** |

---

## Transactions (required for any write)

```python
t = Transaction(doc, "Transaction name")
t.Start()
try:
    # ... write operations ...
    t.Commit()
except:
    t.RollBack()
    raise
```

## Special folder paths

Never hardcode `Path.home() / "Desktop"` — it fails when OneDrive redirects the Desktop. Use .NET:

```python
from System import Environment
desktop = Environment.GetFolderPath(Environment.SpecialFolder.Desktop)
out_path = Path(desktop) / "output.csv"
```

## Iterating BuiltInCategory

```python
from System import Enum
from Autodesk.Revit.DB import BuiltInCategory

for bic in Enum.GetValues(BuiltInCategory):
    if int(bic) >= 0:
        continue  # skip non-negative (invalid) values
    cat = doc.Settings.Categories.get_Item(bic)
    if cat is not None and str(cat.CategoryType) == "Model":
        ...
```

---

## The Python.NET runtime is persistent

The Python runtime inside Revit is **persistent and shared** across all executions (`send_command` and
buttons). A failed import can leave a broken module in `sys.modules` that affects every later script in
the session.

**Diagnosing a button that fails:**

1. **Does the same script work via `send_command`?** If yes, the script is correct — the session state
   is the problem; ask the user to restart Revit.
2. **Import error on a type name?** Check the name in the stubs index — it may have been removed or
   renamed in this Revit version (see the boilerplate note above).
