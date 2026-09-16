<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: AutoCAD & Civil 3D scripts

Read this guide **before writing any AutoCAD or Civil 3D script**. For forms/dialogs read [winforms.md](winforms.md).

> **Host detection:** Civil 3D appears as **"AutoCAD"** in `list_active_instances` (it runs on the AutoCAD platform). Civil 3D was added as a supported host on 2026-06-09.

Related: [navisworks.md](navisworks.md) · [revit.md](revit.md)

---

## Standard boilerplate — AutoCAD

```python
import clr
from pathlib import Path

clr.AddReference("AcMgd")
clr.AddReference("AcCoreMgd")
clr.AddReference("AcDbMgd")

from Autodesk.AutoCAD.ApplicationServices import Application as AcadApp
from Autodesk.AutoCAD.DatabaseServices import *
from Autodesk.AutoCAD.EditorInput import Editor

doc = AcadApp.DocumentManager.MdiActiveDocument
db = doc.Database
ed = doc.Editor
```

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
from Autodesk.AutoCAD.DatabaseServices import *
from Autodesk.AutoCAD.EditorInput import Editor
from Autodesk.Civil.ApplicationServices import CivilApplication
from Autodesk.Civil.DatabaseServices import *

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

## Editing external DWG files

Two validated patterns — choose based on whether the file should appear in the UI.

### Pattern A — Background (file never opens in UI)

```python
from Autodesk.AutoCAD.DatabaseServices import Database, FileOpenMode, DwgVersion

db = Database(False, True)
db.ReadDwgFile(str(file_path), FileOpenMode.OpenForReadAndAllShare, False, "")
try:
    t = db.TransactionManager.StartTransaction()
    try:
        # ... modifications ...
        t.Commit()
    except:
        t.Abort()
        raise
    # 4-arg SaveAs required — 2-arg fails on databases opened via ReadDwgFile
    db.SaveAs(str(file_path), False, DwgVersion.Current, None)
finally:
    db.Dispose()  # always — releases file handle, no stale .dwl files
```

- Use `OpenForReadAndAllShare` (not `OpenForReadAndWriteNoShare`) — an exclusive lock prevents `SaveAs` overwriting the same path.
- `db.Save()` and 2-arg `db.SaveAs(path, version)` both fail on `ReadDwgFile` databases inside the host. Always use 4-arg `SaveAs(path, bakAndRename, version, None)`.
- `db.Dispose()` in `finally` — omitting it on exception leaves a stale `.dwl` lock file.

### Pattern B — UI (file opens as a tab, stays open)

```python
from Autodesk.AutoCAD.ApplicationServices import Application as AcadApp, DocumentCollectionExtension

# DocumentCollectionExtension.Open is a static extension method — call as static
file_doc = DocumentCollectionExtension.Open(AcadApp.DocumentManager, str(file_path), True, "")
db = file_doc.Database

file_doc.UpgradeDocOpen()       # upgrade read-only -> read-write
lock = file_doc.LockDocument()  # required for write access in transactions
try:
    t = db.TransactionManager.StartTransaction()
    try:
        # ... modifications ...
        t.Commit()
    except:
        t.Abort()
        raise
finally:
    lock.Dispose()

# QSAVE saves through the document system — clears the asterisk in the UI tab
file_doc.SendStringToExecute("_.QSAVE ", True, False, False)
# Document stays open — do NOT close it; user sees it in the UI
```

- `DocumentCollectionExtension.Open` is a **static extension method**, not an instance method on `DocumentCollection`.
- Open with `forReadOnly=True` — opening with `False` then calling `UpgradeDocOpen()` throws `eWasOpenForWrite`.
- `LockDocument()` is still required after `UpgradeDocOpen()` — transactions throw `eLockViolation` without it.
- `lock.Dispose()` in `finally`, not `lock.Close()` — `LockDocument()` returns a `DocumentLock`.
- Save with `SendStringToExecute("_.QSAVE ")`, **not** `db.SaveAs()` — `SaveAs` leaves the modified asterisk on a document database.

### Reference scripts

- `01_Scripts/03_AutoCAD/04_WinForms/EditDwg_Background.py` — Pattern A, end-to-end with WinForms.
- `01_Scripts/03_AutoCAD/04_WinForms/EditDwg_WithUI.py` — Pattern B, end-to-end with WinForms.

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

### Related API notes found the same session

- `SectionSourceCollection` has **no `Add` method** — sources cannot be attached from the managed API.
  It exposes only `Count`/`Item`/enumerators; the per-source `IsSampled` flag is what selects which
  ones get sampled.
- `Alignment.Create` rejects `ObjectId.Null` for `styleId`/`labelSetId` (it accepts `Null` for
  `siteId`); resolve real ids by name first — see
  `01_Scripts/03_AutoCAD/10_Alignments/CreateAlignmentFromLines.py`.
- Style collections (`AlignmentStyleCollection`, label set collections) **iterate yielding `ObjectId`**,
  not style objects — open each through the transaction to read `.Name`.
- The three options objects `SectionViewGroups.Add()` needs **cannot be deduced from the stubs** — two
  have no parameterless constructor. Resolved by reflection against the live API
  (`clr.GetClrType(T).GetConstructors()`), which is the cheap move whenever a stub shows a type but no
  way to obtain one:

  | Type | Constructor |
  |---|---|
  | `SectionViewGroupCreationRangeOptions` | `(ObjectId sampleLineGroupId)` |
  | `SectionDisplayOptionCollection` | `(ObjectId sampleLineGroupOid)` |
  | `SectionViewGroupCreationPlacementOptions` | parameterless — then `UseDraftPlacement()` |

- Both `SectionSource.IsSampled` and `SectionDisplayOption.Draw` **default to `False`**. Miss either and
  the run "succeeds" with nothing sampled or nothing plotted — a silent empty result, not an error.
- Section views are small (the swath width, e.g. 30 m) and land wherever you put the insert point. On a
  multi-km site they are easy to miss on screen — zoom to them before telling the user they exist.
  **Do not use `ed.SetCurrentView()` for this**: through the bridge the view applies and is overwritten a
  moment later by the viewport's camera (zoom flashes, then reverts — worse in a 3D/isometric view).
  Queue commands instead, which run after the script ends:
  `doc.SendStringToExecute("_.UCS _W _.-VIEW _TOP _.ZOOM _W x1,y1 x2,y2 ", True, False, False)`.
- **Section view extents read in the same transaction as `SectionViewGroups.Add()` are wrong**: at that
  point every view is still stacked on the insert point. Civil 3D spreads them into the draft grid on
  commit. Read `GeometricExtents` (for zooming, reporting) in a **new transaction after the commit**.
- `ed.GetCurrentView().CenterPoint` is in **display coordinates relative to the view target**, not WCS —
  do not compare it against entity extents to "verify" a zoom.
- Erasing inside a transaction: `GetSampleLineGroupIds()` still lists an erased group until commit. Verify
  a delete in a fresh transaction. Erasing all section views leaves an **empty `SectionViewGroup`**
  behind — remove it with `SectionViewGroups.Remove(svg)`, or "skip if views exist" logic misfires.

---

## Road corridor for cut/fill cross-sections (desmonte y terraplén)

Sections that show only the ground are half the story: cut and fill appear only when a **designed road**
is compared against the terrain. The chain, verified end to end on 2026-09-14 (Civil 3D 2027, model
`MDT_LAMUELA`):

| # | Object | API |
|---|---|---|
| 1 | Terrain profile | `Profile.CreateFromSurface(name, civil_doc, alignmentName, surfaceName, layerName, styleName, labelSetName, offset, start, end)` |
| 2 | Design profile (rasante) | `Profile.CreateByLayout(name, civil_doc, alignmentName, layerName, styleName, labelSetName)` then `profile.PVIs.AddPVI(station, elevation)` |
| 3 | Assembly (sección tipo) | `civil_doc.AssemblyCollection.Add(name, AssemblyType.UndividedCrownedRoad, location, styleId, codeSetStyleId)` |
| 4 | Subassemblies | `civil_doc.SubassemblyCollection.ImportStockSubassembly(name, "Subassembly.<Class>", location)` |
| 5 | Corridor | `civil_doc.CorridorCollection.Add(name, baselineName, alignmentId, profileId, regionName, assemblyId)` |
| 6 | Targets + rebuild | `region.GetTargets()` → set `TargetIds` → `region.SetTargets(sameCollection)` → `corridor.Rebuild()` |
| 7 | Sections | the corridor then appears **automatically** in `SampleLineGroup.GetSectionSources()` |

Note that the profile factories take **names** (layer, style, label set) while the assembly and corridor
factories take **ids** — mixing them up is an easy `TypeError`.

### Design the rasante numerically, not by eye

A rasante made of straight grades between PVIs placed *on* the terrain gives either almost no difference
(dense PVIs — the chord hugs the ground) or very large ones (sparse PVIs). On `MDT_LAMUELA`, PVIs every
500 m gave ±0.5 m in PK 0–500 (nothing visible); only PVIs every 1500 m kept the grade under ~9 %, and
mixed cut/fill existed only in PK 4+500–7+500. Before building anything, sample terrain every 50 m,
evaluate candidate PVI spacings in Python (max grade, max cut, max fill, where each occurs) and pick the
view window from the numbers.

### Stock subassemblies

- Class names are `Subassembly.<ClassName>` (e.g. `Subassembly.LaneSuperelevationAOR`). The stock
  assembly (`C3DStockSubassemblies`) is **not loaded until the first import** — and the bridge validator
  rejects `clr.AddReference("C3DStockSubassemblies")`. You don't need it: `ImportStockSubassembly` loads
  it itself.
- Parameters are set by iterating `sa.ParamsDouble` / `ParamsLong` and matching `p.Key`, then assigning
  `p.Value` (open the subassembly `ForWrite` — the params collections are live wrappers). Real keys:

  | Class | Keys used | Defaults seen |
  |---|---|---|
  | `LaneSuperelevationAOR` | `Width`, `DefaultSlope` | 3.6, −0.02 |
  | `ShoulderExtendSubbase` | `ShoulderWidth`, `ShoulderDefaultSlope` (also `DaylightWidth`…) | 2.4, −0.06 |
  | `BasicSideSlopeCutDitch` | `CutGrade`, `FillGrade` — **rise/run**: 1:1 → `1.0`, 3:2 (H:V) → `0.6667` | 0.5, 0.25 |

- Hook points are found by **point code**, not index: lane outer edge `ETW`, shoulder outer edge `EPS`.
  `BasicSideSlopeCutDitch` has **no points** until the corridor resolves it against the target.

### Assembling — two overloads the stubs hide

The stub generator keeps **one signature per method name**, so overloads are invisible (see
[stubs.md](stubs.md)). Found by reflection (`clr.GetClrType(Assembly).GetMethods()`):

```python
asm.AddSubassembly(lane_id)                          # 1-arg: hooks to the assembly marker, returns AssemblyGroup
asm.AddSubassembly(shoulder_id, point_by_code(lane, "ETW"))    # 2-arg: hooks to a point
grp = asm.MirrorSubassembly(lane_id)                 # 1-arg: mirrored copy at the marker, returns AssemblyGroup
sh_l = asm.MirrorSubassembly(shoulder_id, point_by_code(lane_left, "ETW"))   # 2-arg: returns ObjectId
```

`asm.AddSubassembly(id, None)` is **not** the way to hook to the marker — it raises
`Value cannot be null (Parameter 'pointHookTo')` (a clean exception, not a crash). Mirroring copies the
names too (`Carril_D` on both sides) — rename if it matters.

### Corridor targets

- Default region frequency is **25 m** along tangents: it already inserts the assembly at every 50 m
  sample line station.
- Of all targets `GetTargets()` lists, only the `TargetDTM` ones (`TargetType` = `Surface`, one per side
  slope) are required; offset/elevation targets stay empty.
- Assign by building a new `ObjectIdCollection` into `tg.TargetIds`, and pass **the same collection
  object** you modified to `SetTargets` — calling `GetTargets()` again returns a fresh, unmodified copy.
- `Rebuild()` of a 9.95 km corridor with 400 insertions took ~2 s.

### Verifying cut/fill numerically

- Corridor `Section` objects expose **0 `SectionPoints`**, and `Section.LeftOffset`/`RightOffset` are the
  section extents (the right one sat at exactly the swath edge, +60 m, at every station) — **not** where
  the slopes end. Don't read them as daylight.
- Read the corridor itself: `baseline.GetAppliedAssemblyAtStation(st).GetPointsByCode("Daylight")`. Each
  `CalculatedPoint.StationOffsetElevationToBaseline` gives X = station, Y = offset, **Z relative to the
  profile elevation** (not absolute). Daylight Z < 0 → slope goes down → fill on that side; Z > 0 → cut.
- Size the sample-line swath to the daylight offsets: with 1:1 / 3:2 slopes and ~20 m heights the slopes
  reached 32 m from the axis, so ±15 m lines clipped them; ±60 m fit.

Reference: `01_Scripts/03_AutoCAD/00_Workflow/CreateCrossSections.py` builds the cross-sections on top of this
corridor (sample lines ±60 m, views PK 6+250–6+750).

---

## Property Sets (Civil 3D / AutoCAD) — the Revit shared-parameter equivalent

| Revit | Civil 3D / AutoCAD |
|---|---|
| Shared parameter (definition) | `PropertyDefinition` |
| Parameter group | `PropertySetDefinition` |
| Category (`OST_Walls`…) | **no equivalent** — closest is the .NET object type, or the layer |
| Type vs Instance | **no equivalent** — every value lives on the instance |
| Parameter group in the UI | **no equivalent** — a PSet shows as one flat tab |

Definitions live **in the DWG**, in the `AEC_PROPERTY_SET_DEFS` dictionary of the
`NamedObjectsDictionary` — not in an external shared file like Revit's `.txt`. To share them between
drawings, copy them by script or start from a DWT that already has them.

**Attachment.** There is no native "bind to layer". Two mechanisms:

1. **By object type** — `PropertySetDefinition.AppliesToFilter`, the closest thing to a Revit category.
2. **Manually per entity** — `PropertyDataServices.AddPropertySet(entity, psetDefId)`. Setting
   `AppliesToAll = True` removes the type restriction, so the script's own criterion (e.g. the entity's
   `Layer`) decides what gets tagged. Attachment is per-PSet, never per-property.

Layer-driven attachment is therefore a **scan we implement**: walk ModelSpace, read `entity.Layer`,
attach the PSets that the matrix marks for that layer. It is not automatic — new geometry needs a re-run.

Reference script: `01_Scripts/03_AutoCAD/00_Workflow/CreateParameters.py` (Excel matrix → PSets →
layers → attachment, re-runnable). Two gotchas it encodes:

- **`PropertyDefinition.DefaultData` for `DataType.Integer` needs an explicit `System.Int32`.** A plain
  Python `int` bridges as `Int64` and the setter rejects it with
  `Value does not fall within the expected range. (Parameter 'defaultData')`. `Text`, `Real` and
  `TrueFalse` take `""`, `0.0` and `False` directly. (Live-verified enum members:
  `Integer, Real, Text, TrueFalse, AutoIncrement, AlphaIncrement, List, Graphic` — note it is
  `TrueFalse`, not `TrueFalseType`.)
- **`PropertyDataServices.GetPropertySet()` throws `eKeyNotFound` — it does not return a null
  `ObjectId` — whenever that PSet is not attached.** Checking `entity.ExtensionDictionary.IsNull` first
  is not enough: attaching the first of several PSets creates the dictionary, and the check for the
  second one then throws (verified live). Skip when there is no `ExtensionDictionary`, and otherwise wrap
  the call in `try/except` treating `ErrorStatus.KeyNotFound` as "not attached".
