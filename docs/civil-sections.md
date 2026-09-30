<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: Civil 3D sample lines, section views and road corridors

Read [autocad-civil.md](autocad-civil.md) first — boilerplate, write pattern and the three API misuses that abort the host apply here too.

---

## Sample lines & section views — API notes

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
