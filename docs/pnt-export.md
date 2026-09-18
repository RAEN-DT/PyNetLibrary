<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: exporting a `.pnt` for the PyNET VS Code viewer

How to generate a `.pnt` package that the PyNET viewer (ThatOpen / web-ifc fragments, embedded in
the VS Code extension) loads and renders. Written while building the fire-risk digital-twin `.pnt`
(see the `PowerlineFireRisk` / `WindSiting` skills and `04_QGIS`).

Canonical reference producer: `01_Scripts/01_Navisworks/07_IFCExport/NavisworksPNT_IFC_Fast.py`
(the Navisworks → IFC → `.pnt` exporter). Copy its conventions — they are known to render.

---

## What a `.pnt` is

A plain **ZIP** archive containing:

```
<name>.pnt
├── clashes.json          # manifest the dashboard/viewer reads first
├── manifest.json         # optional (version/format metadata; not required to render)
├── properties.json       # optional (pnt_id → element properties, for the Properties panel)
└── models/
    └── <model>.ifc        # one or more IFC4 files (the geometry)
```

The `classification` array reports coverage per model. `ClassificationAnalyzer`
(`NavisworksPNT_IFC_Fast.py`) reuses the **SearchSets that already exist** in the document — whatever
strategy the project uses (PYNET_Classification, native Category, discipline…) — runs them and measures
how much geometry they cover; `basis` lists the SearchSets used (`"no SearchSets found"` otherwise).

`properties.json` = `{pnt_id: {"pnt_id", "name", "model", "psets": {...}}}` plus one `"m_<stem>"`
entry per model root (Navisworks' own Elemento/Proyecto/Identidad tabs) and
`"__meta__": {"viewRotationDeg": …}` (true north). `manifest.json` = `{version, format: "pnt-ifc",
project, created, models, element_count, clash_count}`.

`clashes.json` is the entry point (the viewer's `server/pnt_server.py`, in the PyNetVSCode repo,
extracts the zip and reads it).
Minimum shape to render geometry — **clashes are optional, an empty list is fine**:

```json
{
  "project": "Gemelo riesgo incendio - La Muela",
  "models": [{ "fileName": "riesgo.ifc", "name": "Riesgo incendio" }],
  "clashes": [],
  "classification": []
}
```

The dashboard builds the viewer URL from `models[].fileName` (`?models=riesgo.ifc,...`); the viewer
fetches each from `/models/<fileName>`. The server's `/models/<fn>` route checks the extract root
first, then `models/` — so putting the IFC under `models/` works. `properties.json` is served from
`/data/properties.json` (the viewer fetches it; missing is non-fatal).

## How the viewer loads it

- Open via the MCP bridge tool `viewer_load_package(<path.pnt>)`, then `viewer_fit`. `viewer_status`
  reports the running viewer (port, package, dataDir).
- The viewer auto-loads the models listed in `clashes.json` (`config.autoLoad`, `config.modelUrls`).
- Models are **IFC** parsed by ThatOpen `IfcLoader` (web-ifc) into fragments — NOT glTF/GLB.

---

## Generating the IFC (the part that bites)

Build IFC4 with **ifcopenshell**. It is **not** in the QGIS Python — it IS on the **PyNET host**
(Civil 3D / Navisworks CPython 3.10, `ifcopenshell 0.8.5`). So generate via `send_command` on the
running host, or run a standalone script with a Python that has ifcopenshell. `zipfile` and
`numpy` are whitelisted (numpy since bridge 1.5.4); `getattr` is **not** (validator).

### Hard requirements (or nothing renders)

1. **Tessellated geometry only.** The viewer renders `IfcTriangulatedFaceSet` with representation
   type **`"Tessellation"`**. `IfcExtrudedAreaSolid` / `"SweptSolid"` does **NOT** render — this was
   the root cause of "no geometry". Build every shape as triangle meshes (`IfcCartesianPointList3D`
   + `IfcTriangulatedFaceSet`), exactly like `NavisworksPNT_IFC_Fast.py`.
2. **Colour via `IfcSurfaceStyleRendering`** on the tri-set: `IfcStyledItem(triSet, [IfcSurfaceStyle("BOTH",
   [IfcSurfaceStyleRendering(IfcColourRgb(...), 0.0, ..., "FLAT")])])`. RGB are floats 0..1.
3. **Double-side OPEN surfaces.** web-ifc back-face culls → an open mesh (terrain, a single plane,
   a heat-map cell) disappears when orbited from behind. Emit its triangles twice, once reversed:
   `faces + [(a, c, b) for (a, b, c) in faces]`. Closed solids (every Navisworks-exported element)
   don't need it — the Navisworks exporter does not double faces.
4. **Plain Python floats / ints.** `createIfcCartesianPointList3D` and `CoordIndex` accept nested
   lists of Python `float` / `int` (the Navisworks exporter passes lists). The `TypeError`
   *AGGREGATE OF AGGREGATE OF DOUBLE* comes from other item types (numpy scalars, .NET doubles, mixed
   ints) — `tuple(tuple(float(c) for c in v) for v in verts)` is the always-safe form.
   **`CoordIndex` is 1-based** (`[f[0] + 1, f[1] + 1, f[2] + 1]`).
5. **Subtract a local origin.** Keep coordinates near 0 (subtract the min X/Y/Z). Real UTM values
   (~6.3e5 / 4.6e6) overflow float32 precision on the GPU → vertex jitter. Real *scale* (a 7 km
   extent) is fine as long as the origin is local.

### Skeleton (low-level, version-stable)

```python
ifc = ifcopenshell.file(schema="IFC4")
units = ifc.createIfcUnitAssignment([ifc.createIfcSIUnit(None,"LENGTHUNIT",None,"METRE"),
                                     ifc.createIfcSIUnit(None,"AREAUNIT",None,"SQUARE_METRE"),
                                     ifc.createIfcSIUnit(None,"VOLUMEUNIT",None,"CUBIC_METRE")])
ax2p = ifc.createIfcAxis2Placement3D(pt([0,0,0]), dir([0,0,1]), dir([1,0,0]))
ctx  = ifc.createIfcGeometricRepresentationContext(None,"Model",3,1e-5,ax2p,None)
bctx = ifc.createIfcGeometricRepresentationSubContext("Body","Model",None,None,None,None,ctx,None,"MODEL_VIEW",None)
proj = ifc.createIfcProject(guid(),None,name,None,None,None,None,[ctx],units)
# site → building → storey via IfcLocalPlacement(None, IfcAxis2Placement3D(origin)) + IfcRelAggregates
# per element: triSet → IfcShapeRepresentation(bctx,"Body","Tessellation",[triSet])
#              → IfcProductDefinitionShape → IfcBuildingElementProxy(world_placement)
# finally: IfcRelContainedInSpatialStructure(..., proxies, storey); ifc.write(path)
```

Package with `zipfile`: `z.write(ifc_path, "models/riesgo.ifc")` + `z.writestr("clashes.json", ...)`.

### The fire-risk twin generator (current state)

Reads the QGIS outputs in `04_QGIS/output/<slug>/` (`prioridad_segmentos.json`,
`riesgo_incendio.json`, `desbroce_aerogeneradores.json`) and the live Civil 3D **TinSurface**:

- **Terrain**: sample `TinSurface.FindElevationAtXY` on a ~70 m grid → one tessellated mesh.
- **AT line / heatmap / turbines**: draped on the terrain (z from the surface), as coloured boxes
  (risk → green/yellow/orange/red; turbines → priority colour).
- Generated via `send_command` on the Civil 3D host (it needs ifcopenshell and the live TIN), so a
  saved version belongs under `03_AutoCAD`, **not** `04_QGIS`.

---

## Large (geographic) models

The viewer sets the camera `near`/`far` planes from the loaded models' bounding box, so a
multi-km model renders at **real scale (S = 1)** — no scaling tricks. Keep coordinates
origin-subtracted (requirement 5) to avoid float32 jitter.

---

## Quick checklist

- [ ] IFC built with `IfcTriangulatedFaceSet` + `"Tessellation"` (never SweptSolid)
- [ ] Colour via `IfcSurfaceStyleRendering`, RGB 0..1
- [ ] Open surfaces double-sided (reversed faces appended)
- [ ] Plain Python floats into `createIfcCartesianPointList3D`; `CoordIndex` 1-based
- [ ] Coordinates origin-subtracted (near 0)
- [ ] `clashes.json` with `models[].fileName`; IFC under `models/`
- [ ] Load with `viewer_load_package` → `viewer_fit`
