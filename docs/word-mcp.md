<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: Reading and writing Word files via MCP

Read this guide **before reading or writing any `.docx` file**. Always run through MCP (`send_command`)
— **never** Bash/PowerShell, never a local Python outside the host.

Related: [excel-mcp.md](excel-mcp.md) · [security.md](security.md) · [bridge-troubleshooting.md](bridge-troubleshooting.md)

---

## Status and prerequisites

> **`docx` is not yet in the validator whitelist.** Until the bridge ships it (update this line with
> the minimum bridge version and add it to [security.md](security.md) and `AGENTS.md` §7 in the same
> commit), a script with `import docx` is rejected. Use the **zipfile fallback** below for reading —
> do not retry the rejected script.

- **Package:** install `python-docx`, import `docx`. **Never `pip install docx`** — that is a different,
  abandoned Python 2 package that the validator would let through under the same import name.
- **Pin:** `python-docx>=1.2,<2` (MIT licence; depends on `lxml` and `typing_extensions`). The API
  changed between 0.8 and 1.x — the snippets below assume 1.x.
- **Where:** into the **host's** interpreter (`sys.prefix` of the running host), not the bridge's uv
  environment. Procedure in [bridge-troubleshooting.md](bridge-troubleshooting.md).
- **Not supported by either route:** legacy binary `.doc`, computed fields (TOC, page numbers). Ask the
  user to save as `.docx`.

---

## Which route

| Task | Use |
|---|---|
| Read text, headings, tables | python-docx (Option 1) |
| Fill a template, create a document | python-docx (Options 3–4) |
| Headers/footers in document order, tracked changes, bridge without `docx` | zipfile + xml (Option 2) |

**Read cheaply.** For a long document, first return an index (headings + block positions + table
count), then read only the section you need. Do not dump a 200-page document into `ia_Result`.

---

## Option 1 — read with python-docx

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

- **Index only:** keep blocks whose `style` starts with `"Heading"` plus a table count.
- **Tracked changes:** python-docx drops text inside pending insertions (`w:ins`) *and* deletions —
  `"Closing door."` changed to `"window"` reads as `"Closing ."` (verified). If `word/document.xml`
  contains `w:ins` or `w:del`, read with Option 2, which returns the changes-accepted view.
- **Merged cells:** `row.cells` always returns one entry per grid column (merged cells are repeated).
  Option 2 returns one entry per real cell, so a horizontally merged row is shorter than the header.
- **Matrix tables:** load `rows[1:]` into a pandas `DataFrame` with `rows[0]` as columns, same rule as
  [excel-mcp.md](excel-mcp.md).

## Option 2 — read with zipfile + xml (fallback)

A `.docx` is a ZIP; the body is `word/document.xml`. Deleted tracked text lives in `w:delText`, so
collecting `w:t` gives the "changes accepted" view.

```python
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

def text_of(el):
    return "".join(t.text or "" for t in el.iter(W + "t"))

with zipfile.ZipFile(Path(r"C:\path\to\file.docx")) as z:
    body = ET.fromstring(z.read("word/document.xml")).find(W + "body")

blocks = []
for i, el in enumerate(body):
    if el.tag == W + "p" and text_of(el).strip():
        style = el.find(f"{W}pPr/{W}pStyle")
        blocks.append({"type": "paragraph", "index": i, "text": text_of(el),
                       "style": style.get(W + "val") if style is not None else ""})
    elif el.tag == W + "tbl":
        rows = [[text_of(tc) for tc in tr.findall(W + "tc")] for tr in el.findall(W + "tr")]
        blocks.append({"type": "table", "index": i, "rows": rows})

ia_Result = blocks
```

- Merged cells: a cell spanning columns carries `w:tcPr/w:gridSpan` (`w:val` = columns spanned); use
  it to realign a short row with the header before building a `DataFrame`.
- `pStyle` holds the **style id**, which may be localized (`Ttulo1` instead of `Heading1`). It is
  absent — `style` comes back `""` — when the paragraph uses the default style (`Normal`).
- Headers/footers: `word/header*.xml`, `word/footer*.xml` — same parsing. Word usually writes three
  of each (default, first page, even pages) even when only one is used; skip the empty ones.

---

## Option 3 — fill a template

Word often splits a placeholder across runs (`{{PRO` + `JECT}}`), so replace over a group of
consecutive runs: write the result into the first run and empty the rest. This keeps the first run's
formatting and drops mixed formatting inside that group — acceptable for placeholders.

**Hyperlinks are a separate group.** `p.text` includes hyperlink text but `p.runs` does not, so
replacing `p.text` into `p.runs[0]` duplicates the link text and leaves its placeholder untouched
(verified on a Word-authored file). Walk `p.iter_inner_content()` and fill plain runs and each
hyperlink's runs independently. A placeholder must not cross a hyperlink boundary.

**Tracked changes:** python-docx cannot see runs inside pending insertions, so a placeholder typed with
Track Changes on is never replaced. If the template contains `w:ins`/`w:del`, ask the user to accept
or reject all changes in Word first.

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
- If the validator rejects `import docx`, the bridge is older than the whitelist change: read with
  Option 2 and tell the user writing needs a bridge update. Do not try to bypass the validator.
