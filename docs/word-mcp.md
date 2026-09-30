<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: Reading and writing Word files via MCP

Read this guide **before reading or writing any `.docx` file**. Always run through MCP (`send_command`)
— **never** Bash/PowerShell, never a local Python outside the host. Everything here uses
**python-docx** only.

Related: [excel-mcp.md](excel-mcp.md) · [pdf-mcp.md](pdf-mcp.md) · [security.md](security.md) · [bridge-troubleshooting.md](bridge-troubleshooting.md)

---

## Status and prerequisites

> **`docx` is whitelisted from bridge ≥ 1.5.6.** On an older bridge a script with `import docx` is
> rejected and there is no Word support — tell the user it needs a bridge update, do not retry the
> rejected script. Check the running bridge's version if unsure.

- **Package:** install `python-docx`, import `docx`. **Never `pip install docx`** — that is a different,
  abandoned Python 2 package that the validator would let through under the same import name.
- **Pin:** `python-docx>=1.2,<2` (MIT licence; depends on `lxml` and `typing_extensions`). The API
  changed between 0.8 and 1.x — the snippets below assume 1.x.
- **Where:** into the **host's** interpreter (`sys.prefix` of the running host), not the bridge's uv
  environment. Procedure in Step 0.
- **Not supported:** legacy binary `.doc`, computed fields (TOC, page numbers). Ask the user to save
  as `.docx`.

---

## Step 0 — check the library, install it if missing (MANDATORY)

Run this **before the first Word script of the session** on each host (read-only, no confirmation):

```python
import sys

try:
    import docx
    status = {"installed": True, "version": docx.__version__}
except ImportError:
    status = {"installed": False, "version": None}

ia_Result = [{"type": "env", "package": "python-docx", **status, "prefix": sys.prefix,
              "site": [p for p in sys.path if "site-packages" in p]}]
```

- **Validator rejects the script** → `docx` is not whitelisted in this bridge (see Status). Installing
  will not help; tell the user Word support needs a bridge update.
- **`installed: False`, or `version` below `1.2`** → tell the user you are installing `python-docx` for
  Word support, then from PowerShell (the one OS fallback, `AGENTS.md` §9):

  ```powershell
  & "<prefix>\python.exe" -m pip install "python-docx>=1.2,<2"
  ```

  No `python.exe` under `<prefix>` (embedded layout) → `py -3.10 -m pip install --target "<site>" "python-docx>=1.2,<2"`
  with a `site` path from the check. Details and locked-file errors: [bridge-troubleshooting.md](bridge-troubleshooting.md).
- **Re-run the check.** Continue only when it reports `installed: True` and version ≥ 1.2. If the import
  still fails after a successful install, restart the host.

---

## Which option

| Task | Option |
|---|---|
| Read text, headings, tables | 1 |
| Document has tracked changes or merged cells | 2 (on top of 1) |
| Fill a template | 3 |
| Create a document | 4 |

**Read cheaply.** For a long document, first return an index (headings + block positions + table
count), then read only the section you need. Do not dump a 200-page document into `ia_Result`.

---

## Option 1 — read

`iter_inner_content()` yields paragraphs and tables **in document order** (`doc.paragraphs` and
`doc.tables` lose the interleaving).

```python
from pathlib import Path
from docx import Document
from docx.table import Table

doc = Document(str(Path(r"C:\path\to\file.docx")))

blocks = []
for i, block in enumerate(doc.iter_inner_content()):
    if isinstance(block, Table):
        rows = [[cell.text for cell in row.cells] for row in block.rows]
        blocks.append({"type": "table", "index": i, "rows": rows})
    elif block.text.strip():
        blocks.append({"type": "paragraph", "index": i,
                       "style": block.style.name, "text": block.text})

ia_Result = blocks
```

- **Style names are English** even on a Spanish-authored file (`"Heading 1"` for *Título 1*) — safe to
  filter on. **Index only:** keep blocks whose `style` starts with `"Heading"` plus a table count.
- **Headers/footers:** `section.header` / `section.footer` (default). A separate first-page header
  exists only when `section.different_first_page_header_footer` is true (`section.first_page_header`),
  and even-page headers only when `doc.settings.odd_and_even_pages_header_footer` is true
  (`section.even_page_header`).
- **Matrix tables:** load `rows[1:]` into a pandas `DataFrame` with `rows[0]` as columns, same rule as
  [excel-mcp.md](excel-mcp.md).

## Option 2 — tracked changes and merged cells

**Tracked changes.** `paragraph.text` drops text inside pending insertions *and* deletions —
`"Closing door."` with `"door"` → `"window"` reads as `"Closing ."` (verified). Read those paragraphs
through their XML element instead (`p._p`, still python-docx): `w:t` holds live and inserted text,
`w:delText` holds deleted text.

```python
def has_changes(p):
    return bool(p._p.xpath(".//w:ins | .//w:del"))

def accepted_text(p):   # as if all changes were accepted -> "Closing window."
    return "".join(t.text or "" for t in p._p.xpath(".//w:t"))

def original_text(p):   # as if all changes were rejected -> "Closing door."
    return "".join(t.text or "" for t in p._p.xpath(".//w:t[not(ancestor::w:ins)] | .//w:delText"))
```

In Option 1, use `accepted_text(block)` instead of `block.text` when `has_changes(block)`, and flag
the paragraph (`"tracked": True`) so the user knows the document has pending changes.

**Merged cells.** `row.cells` returns one entry per grid column, repeating a merged cell (verified: a
cell spanning two columns appears twice). To get each real cell once with its width:

```python
def real_cells(row):
    seen, cells = set(), []
    for cell in row.cells:
        if id(cell._tc) not in seen:
            seen.add(id(cell._tc))
            cells.append({"text": cell.text, "span": cell.grid_span})
    return cells
```

Use the grid form (`row.cells`) to build a `DataFrame` — it stays aligned with the header. Use
`real_cells` when the user needs to know which cells are merged.

`_p` and `_tc` are python-docx internals: stable within the pinned `<2` range, but re-verify both
helpers when raising the pin.

---

## Option 3 — fill a template

Word often splits a placeholder across runs (`{{PRO` + `JECT}}`), so replace over a group of
consecutive runs: write the result into the first run and empty the rest. This keeps the first run's
formatting and drops mixed formatting inside that group — acceptable for placeholders.

**Hyperlinks are a separate group.** `p.text` includes hyperlink text but `p.runs` does not, so
replacing `p.text` into `p.runs[0]` duplicates the link text and leaves its placeholder untouched
(verified on a Word-authored file). Walk `p.iter_inner_content()` and fill plain runs and each
hyperlink's runs independently. A placeholder must not cross a hyperlink boundary.

**Tracked changes:** runs inside pending insertions are not visible to `iter_inner_content()`, so a
placeholder typed with Track Changes on is never replaced. If any paragraph `has_changes` (Option 2),
ask the user to accept or reject all changes in Word first.

```python
from pathlib import Path
from docx import Document
from docx.text.hyperlink import Hyperlink

template = Path(r"C:\path\to\template.docx")
output = Path(r"C:\path\to\output.docx")
values = {"PROJECT": "Hospital Norte", "DATE": "2026-09-28"}

def fill_runs(runs):
    text = "".join(run.text for run in runs)
    new = text
    for key, val in values.items():
        new = new.replace("{{" + key + "}}", str(val))
    if new != text:
        runs[0].text = new
        for run in runs[1:]:
            run.text = ""

def fill(paragraphs):
    for p in paragraphs:
        group = []
        for item in p.iter_inner_content():
            if isinstance(item, Hyperlink):
                if group:
                    fill_runs(group)
                    group = []
                if item.runs:
                    fill_runs(item.runs)
            else:
                group.append(item)
        if group:
            fill_runs(group)

doc = Document(str(template))
fill(doc.paragraphs)
for table in doc.tables:
    for row in table.rows:
        for cell in row.cells:
            fill(cell.paragraphs)
for section in doc.sections:
    fill(section.header.paragraphs)
    fill(section.footer.paragraphs)
    if section.different_first_page_header_footer:
        fill(section.first_page_header.paragraphs)
        fill(section.first_page_footer.paragraphs)
    if doc.settings.odd_and_even_pages_header_footer:
        fill(section.even_page_header.paragraphs)
        fill(section.even_page_footer.paragraphs)

doc.save(str(output))
print(f"Saved {output}")
```

## Option 4 — create a document

```python
from pathlib import Path
from docx import Document
from docx.shared import Cm

records = [{"id": 1, "name": "Wall A", "height": 3.2}]
output = Path(r"C:\path\to\report.docx")

doc = Document()
doc.add_heading("Element report", level=1)
doc.add_paragraph(f"{len(records)} elements.")

columns = list(records[0])
table = doc.add_table(rows=1, cols=len(columns))
table.style = "Table Grid"
for cell, name in zip(table.rows[0].cells, columns):
    cell.text = name
for rec in records:
    for cell, name in zip(table.add_row().cells, columns):
        cell.text = str(rec[name])

# doc.add_picture(str(Path(r"C:\path\to\image.png")), width=Cm(15))
doc.save(str(output))
print(f"Saved {output}")
```

- Use the **English** built-in style names (`"Table Grid"`, `"Heading 1"`) even on a Word template
  authored in another language — python-docx resolves them. The localized UI name (`"Título 1"`)
  raises `KeyError` (verified on a Spanish-authored template). Custom styles use their own name.
- To inherit the user's styles, headers and page setup, start from their template:
  `Document(str(template_path))`, then append content.

---

## Rules

- **Never overwrite the source or template** — save to a new path. Ask the user once before
  overwriting any existing file.
- Save output next to the input or on the Desktop, and report the full path.
- Build tables from computed data; never type figures by hand (`AGENTS.md` §9).
- If the validator rejects `import docx`, the bridge is older than the whitelist change: tell the user
  Word support needs a bridge update. Do not try to bypass the validator.
