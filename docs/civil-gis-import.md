<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: importing GIS results into Civil 3D

Read [autocad-civil.md](autocad-civil.md) first — every write goes inside `doc.LockDocument()`.
Reference buttons: `01_Scripts/03_AutoCAD/20_GIS/` (`CrearSuperficieMDT.py`, `MapaCalorEolico.py`,
`ImportarParcelasCatastro.py`, `ImportarRiesgoIncendio.py`, `InsertarAerogeneradores.py`).
The GIS analysis itself runs in standalone PyQGIS ([qgis.md](qgis.md)); these buttons only draw
its JSON / GeoJSON / XYZ output.

---

## Locating the exchange files

Machine-specific locations go in `%USERPROFILE%\.pynet\paths.json` (not versioned), never in code:

```python
_PATHS = Path.home() / ".pynet" / "paths.json"
CFG = json.loads(_PATHS.read_text(encoding="utf-8")) if _PATHS.exists() else {}
QGIS_DIR = Path(CFG.get("qgis_dir", r"C:\Repos\PyNetLibrary\01_Scripts\04_QGIS"))
```

## Repeatable imports

Every button **re-syncs**: it creates its layer if missing and erases what a previous run drew on it.

```python
lt = t.GetObject(db.LayerTableId, OpenMode.ForRead)
if not lt.Has(LAYER):
    lt.UpgradeOpen()
    ltr = LayerTableRecord(); ltr.Name = LAYER
    ltr.Color = Color.FromColorIndex(ColorMethod.ByAci, 3)
    lt.Add(ltr); t.AddNewlyCreatedDBObject(ltr, True)

for oid in ms:
    e = t.GetObject(oid, OpenMode.ForRead)
    if e.Layer == LAYER:
        e.UpgradeOpen(); e.Erase()
```

Keep one layer per result so a re-run never touches the user's own geometry.

## TIN surface from points

```python
surf_id = TinSurface.Create(db, "MDT_ZONA")
surf = t.GetObject(surf_id, OpenMode.ForWrite)
coll = Point3dCollection()
for x, y, z in points:
    coll.Add(Point3d(x, y, z))
    if coll.Count >= 20000:              # add in chunks — ~90k vertices in ~1 min
        surf.AddVertices(coll); coll = Point3dCollection()
if coll.Count:
    surf.AddVertices(coll)
```

Replace on re-run: find the old surface by name in `civil_doc.GetSurfaceIds()` and `Erase()` it first.
Contours as 2D polylines at their height: `Polyline` + `AddVertexAt(i, Point2d(x, y), 0, 0, 0)` +
`pl.Elevation = z`.

## Draping on the terrain

```python
def z_at(x, y, offset=2.0):
    try:
        return surface.FindElevationAtXY(x, y) + offset     # a few metres up avoids z-fighting
    except Exception:
        return None                                         # THROWS outside the TIN - skip the point
```

Always drape: geometry imported at z = 0 ends up floating under the terrain. When the drawing has
several surfaces, pick the TIN by name rather than `GetSurfaceIds()[0]`.

## Entities

| Need | Entity | Gotcha |
|---|---|---|
| Filled cell (heat map) | `Solid(p1, p2, p3, p4)` | vertex order **BL, BR, TL, TR** — BL, BR, TR, TL draws a bow-tie |
| Draped line / outline | `Polyline3d` | append the polyline to ModelSpace **first**, then each `PolylineVertex3d` + `AddNewlyCreatedDBObject(v, True)` |
| Parcel / polygon | closed `Polyline` | GeoJSON holes become separate polylines |
| Label | `MText` (`Contents`, `Location`, `TextHeight`) | line break is `\P` inside `Contents` |
| Circle | `Circle(center, Vector3d(0, 0, 1), r)` | — |

Colours: `ent.ColorIndex = aci` (ACI) or `ent.Color = Color.FromRgb(r, g, b)`.

## Blocks

```python
ref = BlockReference(Point3d(x, y, z), bt[block_name])
ref.ScaleFactors = Scale3d(scale)
ref.Rotation = math.radians((90 - wind_from_deg) % 360)   # meteorological (N=0, clockwise) -> AutoCAD
```

If the block is missing, build it: a new `BlockTableRecord` in the block table with `Solid3d`
primitives (`CreateFrustum`, `CreateBox`) moved with `TransformBy(Matrix3d.Displacement(...))` /
`Matrix3d.Rotation(angle, axis, origin)`. Put block entities on layer `0` with colour **ByBlock** so
the reference's layer controls them.

## Attaching data (Property Sets)

Create the definition if missing, attach, then write values — see
[civil-propertysets.md](civil-propertysets.md). Two import-specific points:

- Call `DictionaryPropertySetDefinitions(db)` before reading `AEC_PROPERTY_SET_DEFS` from the NOD —
  a drawing that never had Property Sets has no such dictionary.
- **Schema migration:** when a newer import adds a field, open the existing definition `ForWrite`
  and `Definitions.Add` the missing `PropertyDefinition` (see `InsertarAerogeneradores.py`).

End with `doc.SendStringToExecute("_.ZOOM _E ", True, False, False)` so the user sees the result.
