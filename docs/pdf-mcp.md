<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: Reading PDF files via MCP

Read this guide **before reading any `.pdf` file**. Always run through MCP (`send_command`) — **never**
Bash/PowerShell, never a local Python outside the host. **Read-only:** creating or editing PDFs is out
of scope.

Related: [word-mcp.md](word-mcp.md) · [excel-mcp.md](excel-mcp.md) · [security.md](security.md) · [bridge-troubleshooting.md](bridge-troubleshooting.md)

---

## Status and prerequisites

> **`pypdf` is not yet in the validator whitelist.** Until the bridge ships it (update this line with
> the minimum bridge version and add it to [security.md](security.md) and `AGENTS.md` §7 in the same
> commit), a script with `import pypdf` is rejected. There is **no standard-library fallback**: PDF
> content streams are compressed and font-encoded. Tell the user reading PDFs needs a bridge update —
> do not retry the rejected script.

- **Package:** `pip install pypdf`, import `pypdf`. **Never `PyPDF2`, `PyPDF3` or `PyPDF4`** — those are
  the deprecated predecessors (`PdfFileReader`, `getPage`, `extractText`). Agents trained on older code
  default to them; the validator would reject the import anyway.
- **Pin:** `pypdf>=6,<7` (BSD-3, pure Python, only depends on `typing_extensions` on Python < 3.11).
- **Where:** into the **host's** interpreter (`sys.prefix` of the running host), not the bridge's uv
  environment. Procedure in [bridge-troubleshooting.md](bridge-troubleshooting.md).
- **Not supported:** scanned PDFs (images, no text layer — would need OCR) and splitting table columns
  reliably. Tell the user instead of guessing.

---

## Step 0 — check the library, install it if missing (MANDATORY)

Run this **before the first PDF script of the session** on each host (read-only, no confirmation):

```python
import sys

try:
    import pypdf
    status = {"installed": True, "version": pypdf.__version__}
except ImportError:
    status = {"installed": False, "version": None}

ia_Result = [{"type": "env", "package": "pypdf", **status, "prefix": sys.prefix,
              "site": [p for p in sys.path if "site-packages" in p]}]
```

- **Validator rejects the script** → `pypdf` is not whitelisted in this bridge (see Status). Installing
  will not help; tell the user PDF reading needs a bridge update.
- **`installed: False`, or `version` below `6`** → tell the user you are installing `pypdf` for PDF
  support, then from PowerShell (the one OS fallback, `AGENTS.md` §9):

  ```powershell
  & "<prefix>\python.exe" -m pip install "pypdf>=6,<7"
  ```

  No `python.exe` under `<prefix>` (embedded layout) → `py -3.10 -m pip install --target "<site>" "pypdf>=6,<7"`
  with a `site` path from the check. Details and locked-file errors: [bridge-troubleshooting.md](bridge-troubleshooting.md).
- **Re-run the check.** Continue only when it reports `installed: True` and version ≥ 6. If the import
  still fails after a successful install, restart the host.

---

## Read cheaply: index first

Never dump a whole PDF into `ia_Result`. First return an index — page count, metadata, bookmarks,
whether it has form fields or a text layer — then read only the pages you need.

```python
from pathlib import Path
from pypdf import PdfReader

reader = PdfReader(str(Path(r"C:\path\to\file.pdf")))
if reader.is_encrypted:
    reader.decrypt("")  # empty user password; ask the user if this fails

def flatten(items, depth=0):
    out = []
    for item in items:
        if isinstance(item, list):
            out += flatten(item, depth + 1)
        else:
            out.append({"title": item.title, "depth": depth,
                        "page": reader.get_destination_page_number(item) + 1})
    return out

sample = [reader.pages[i].extract_text() or "" for i in range(min(3, len(reader.pages)))]

ia_Result = {
    "type": "pdf_index",
    "pages": len(reader.pages),
    "metadata": {k: str(v) for k, v in (reader.metadata or {}).items()},
    "outline": flatten(reader.outline),
    "has_form": bool(reader.get_fields()),
    "has_text": any(s.strip() for s in sample),
}
```

- `has_text: False` means there is **no text layer** — stop and tell the user. Two common causes:
  - a scanned document (would need OCR);
  - a **CAD/BIM export** rendered as images. Verified on a Revit 2025 sheet exported with *vector*
    processing selected: the page content was only image tiles (80 draws of 45 images, no text, no
    vector paths) — the exporter rasterized it anyway. `/creator: Autodesk Revit` in the metadata.
- If the metadata names Revit, AutoCAD or Navisworks as `/creator`, the model itself is a better data
  source than the PDF: offer to read the values from the open model instead of the PDF.
- `page` numbers in the outline are 1-based, like the ones the user sees in a PDF viewer.

## Read text by page range

```python
from pathlib import Path
from pypdf import PdfReader

reader = PdfReader(str(Path(r"C:\path\to\file.pdf")))
first, last = 1, 5  # 1-based, inclusive — as the user counts pages

ia_Result = []
for n in range(first, min(last, len(reader.pages)) + 1):
    text = reader.pages[n - 1].extract_text() or ""
    ia_Result.append({"type": "pdf_page", "page": n, "text": text, "empty": not text.strip()})
```

- **Tables:** `extract_text()` returns a table's cells as loose text, without rows or columns.
  `extract_text(extraction_mode="layout")` keeps the horizontal alignment, so columns can sometimes be
  split on runs of 2+ spaces (`re.split(r" {2,}", line)`). Treat it as a heuristic, check the result
  against the PDF, and tell the user when a table could not be parsed cleanly. Verified on a
  Word-exported PDF: regular rows split correctly; a row with merged cells comes back with fewer
  columns — keep it, do not silently drop it.
- **Reading order:** plain `extract_text()` follows the PDF's drawing order, not the page. On a
  Word-exported PDF the footer came out *before* the body. When order matters, use
  `extraction_mode="layout"`, which follows the page position (header on top, footer at the bottom).
- Layout mode pads the page with blank lines (dozens on a mostly empty page) — drop empty lines before
  returning the text.
- A PDF exported from Word with tracked changes visible contains both texts glued together
  (`"door"` deleted + `"window"` inserted → `"doorwindow"`). Mention it if the text looks garbled.

## Read form fields

```python
from pathlib import Path
from pypdf import PdfReader

reader = PdfReader(str(Path(r"C:\path\to\form.pdf")))
fields = reader.get_form_text_fields() or {}

ia_Result = [{"type": "pdf_field", "name": k, "value": v or ""} for k, v in fields.items()]
```

`get_form_text_fields()` returns text fields only; `get_fields()` also returns checkboxes and choices,
with the value under the `"/V"` key.

---

## Rules

- Index first, then read page ranges. Report page numbers 1-based.
- Never modify or overwrite the source PDF.
- Figures read from a PDF (quantities, dimensions) are text: convert and compute them in Python before
  reporting (`AGENTS.md` §9).
- If the validator rejects `import pypdf`, the bridge is older than the whitelist change: tell the user
  PDF reading needs a bridge update. Do not try to bypass the validator.
