<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: AutoCAD & Civil 3D scripts

Read this guide **before writing any AutoCAD or Civil 3D script**, then the topic guide the task needs
(below). For forms/dialogs read [winforms.md](winforms.md).

> **Host detection:** Civil 3D appears as **"AutoCAD"** in `list_active_instances` (it runs on the AutoCAD platform). Civil 3D was added as a supported host on 2026-06-09.

Related: [navisworks.md](navisworks.md) · [revit.md](revit.md)

---

## Topic guides — read only the one the task needs

| If the task is… | Read |
|---|---|
| Opening / editing / saving **another DWG** (background or as a UI tab) | [autocad-external-dwg.md](autocad-external-dwg.md) |
| **Sample lines, section views, profiles, assemblies, corridors**, cut/fill | [civil-sections.md](civil-sections.md) |
| **Property Sets** (PSets — the Revit shared-parameter equivalent), attaching data to entities | [civil-propertysets.md](civil-propertysets.md) |

> This guide and the topic guides are a base, not final: external Civil 3D findings are expected to be
> merged in. When they arrive, merge into the matching topic guide — do not duplicate sections.

---

## Standard boilerplate — AutoCAD

```python
import clr
from pathlib import Path

clr.AddReference("AcMgd")
clr.AddReference("AcCoreMgd")
clr.AddReference("AcDbMgd")

from Autodesk.AutoCAD.ApplicationServices import Application as AcadApp
from Autodesk.AutoCAD.DatabaseServices import BlockTableRecord, OpenMode  # what you use

doc = AcadApp.DocumentManager.MdiActiveDocument
db = doc.Database
ed = doc.Editor
```

Import **only the types the script uses**, by name — never `from … import *` (same rule and reasons as
[navisworks.md](navisworks.md#-never-use-from-namespace-import-)). `Autodesk.AutoCAD.DatabaseServices`
and `Autodesk.Civil.DatabaseServices` share type names (e.g. `Entity`) — explicit imports also keep
the two apart. Resolve the namespace with the stubs index (`CLASSES.tsv`, match the `namespace` column).

> **PyNET bundle / form icon:** never hardcode the year or the bundle path — resolve them from the
> running `Raen.Core.Pynet.Engine` (`PYNET_BUNDLE / "C3D.ico"`). See [winforms.md](winforms.md) "Form icon".

## Standard boilerplate — AutoCAD + Civil 3D

Adds the Civil assemblies on top of AutoCAD.

```python
import clr
from pathlib import Path

clr.AddReference("AcMgd")
clr.AddReference("AcCoreMgd")
clr.AddReference("AcDbMgd")
clr.AddReference("AecBaseMgd")
clr.AddReference("AeccDbMgd")

from Autodesk.AutoCAD.ApplicationServices import Application as AcadApp
from Autodesk.AutoCAD.DatabaseServices import OpenMode                 # what you use
from Autodesk.Civil.ApplicationServices import CivilApplication
from Autodesk.Civil.DatabaseServices import Alignment, TinSurface     # what you use

doc = AcadApp.DocumentManager.MdiActiveDocument
db = doc.Database
ed = doc.Editor
civil_doc = CivilApplication.ActiveDocument
```

> Civil 3D covers alignments, profiles, corridors, surfaces, pipe networks. Treat it as a first-class host alongside Navisworks and Revit.

## Write operations — transaction pattern

```python
with doc.LockDocument():
    t = db.TransactionManager.StartTransaction()
    try:
        # ... modifications ...
        t.Commit()
    except:
        t.Abort()
        raise
```

---

## Hard crashes: three API misuses that abort the host (2026-09-14)

Writing Civil 3D cross-section scripts killed the Civil 3D process **four times** in one session
(`list_active_instances` goes empty mid-call, the bridge reports `Connection closed unexpectedly`).
None of the three causes was a Civil 3D bug — all were calling-convention mistakes on our side, and
**none surfaces as a catchable Python exception**: AutoCAD raises a native internal assertion and
aborts, so `try/except` around the call does nothing, and everything uncommitted in the drawing is
lost.

> **Diagnostic note.** The Windows Event Log (Application, Id 1000) shows `acad.exe` faulting in
> `coreclr.dll`, `0xC0000005`, at the same offset every time. That offset is only where the abort
> *surfaces* through the managed frame — it does **not** identify the cause, and reading it as a
> pythonnet/CoreCLR marshaling bug sent this investigation down a blind alley. The **AutoCAD error
> dialog** (`ERROR INTERNO: !dbobji.cpp@8703: eNotOpenForWrite`) is what actually identified it — ask
> the user for that dialog before theorising about the Event Log.

### 1. Writing without `doc.LockDocument()`

`SampleLine.Create(name, groupId, points)` aborted the process when called inside a bare
`db.TransactionManager.StartTransaction()`. **The identical script wrapped in `with doc.LockDocument():`
works** (verified both directions). This is just the write pattern documented above — but note that
unlocked writes are *undefined behaviour, not a reliable error*: in the same session two other
unlocked write scripts (`Alignment.Create`, `SampleLineGroup.Create`) completed fine, which is exactly
what makes the omission easy to miss.

Reminder on which document gets locked: `CivilApplication.ActiveDocument` (Civil objects: alignments,
surfaces, styles) has **no lock of its own** — it is a typed view over the same drawing. The lock and
the database belong to the AutoCAD document: `AcadApp.DocumentManager.MdiActiveDocument`.

### 2. Calling a writing method on an object opened `ForRead`

```python
g = t.GetObject(gid, OpenMode.ForRead)   # SampleLineGroup opened ForRead
sources = g.GetSectionSources()          # ABORTS: eNotOpenForWrite
```

`SampleLineGroup.GetSectionSources()` **modifies the group despite the `Get` prefix** (it appears to
initialise/refresh the source collection lazily), so it requires `OpenMode.ForWrite`. Called on a
`ForRead` object it trips `!dbobji.cpp@8703: eNotOpenForWrite` and takes the process down — with or
without a document lock (reproduced both ways).

**Generalise this:** on Civil 3D objects a `Get*` name is not proof the call is read-only. When a
`Get*`/property access aborts the host with `eNotOpenForWrite`, reopen that object `ForWrite` rather
than assuming the API is broken.

**The failure modes are asymmetric — this is the practical takeaway.** Opening `ForWrite` when you
only read costs almost nothing (an undo record, the drawing marked modified). Opening `ForRead` when
the call writes kills the process, with no catchable exception and no partial result. So when in
doubt on a Civil 3D object, open `ForWrite`.

Heuristic for telling them apart (observed, not exhaustively proven — verify before relying on it):

| The call returns | Verified examples | Open mode |
|---|---|---|
| Ids or plain values (a snapshot) | `GetAlignmentIds()`, `GetSampleLineGroupIds()`, `.Name`, `Alignment.PointLocation()` | `ForRead` is fine |
| A **live, mutable wrapper** over the object's internals | `SampleLineGroup.GetSectionSources()` → collection whose `IsSampled` you can set | requires `ForWrite` |

### 3. Using the transaction after `t.Commit()`

```python
t.Commit()
alignment = t.GetObject(align_id, OpenMode.ForRead)   # ABORTS: transaction already closed
```

Read every value the report needs — lengths, counts, names — **before** committing, and print
afterwards. This one bites specifically when refactoring a working script into functions: the summary
print drifts to the end of the block, past the commit, and the script that ran fine yesterday now
kills the session.

More Civil 3D API notes from the same session (section sources, style collections, section view
constructors, zooming, extents after commit) are in [civil-sections.md](civil-sections.md).
