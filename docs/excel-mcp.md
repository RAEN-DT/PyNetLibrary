<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: Reading Excel files via MCP

Read this guide **before reading any `.xlsx` file**. Always run through MCP (`send_command`) — **never** Bash/PowerShell.

Related: [revit.md](revit.md)

---

## Try openpyxl first; pandas as fallback — except for matrices

**If the sheet is a matrix** (rows of entities × columns of attributes/bindings — e.g. a parameter
matrix, a category/layer binding table) **use pandas (`DataFrame`) directly, not openpyxl.**
DataFrames give column-aligned access (`df["Nombre"]`, `df.columns`, boolean masks) that matches how
a matrix is actually consumed — openpyxl's `iter_rows(values_only=True)` forces manual positional
indexing (`row[2]`, `row[3:]`) that is more error-prone and harder to read for this shape. This is a
standing preference, not a one-off — do not default back to openpyxl for a matrix sheet.

For anything else (a single lookup, a small non-tabular read), openpyxl first / pandas fallback still
applies.

### Option 1 (preferred for non-matrix reads) — openpyxl

```python
import openpyxl

wb = openpyxl.load_workbook(r"C:\path\to\file.xlsx", data_only=True)

result = {}
for sheet_name in wb.sheetnames:
    ws = wb[sheet_name]
    rows = [[str(v) if v is not None else "" for v in row] for row in ws.iter_rows(values_only=True)]
    result[sheet_name] = {"rows": len(rows), "data": rows}

ia_Result = result
```

### Option 2 (fallback) — pandas

```python
import pandas as pd

xl = pd.ExcelFile(r"C:\path\to\file.xlsx")

result = {}
for sheet in xl.sheet_names:
    df = xl.parse(sheet)
    result[sheet] = {
        "columns": list(df.columns),
        "rows": len(df),
        "data": df.fillna("").to_dict(orient="records")
    }

ia_Result = result
```
