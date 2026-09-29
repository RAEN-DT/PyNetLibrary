"""
NavisworksToIFC — Exports one IFC4 file per linked NWC/NWD model in the active NWF.

Requirements:
    pip install ifcopenshell

Output:
    <NWF folder>/IFC_Export/<ModelName>.ifc  (one file per linked model)

Geometry:
    Real triangulated mesh from each element via TriangleMeshCollector (C# COM callback).
    Uses modern ModelItem API to traverse geometry, filtered to Triangles only.
    Navisworks API values are in feet; output is meters.

Colors:
    Read from ModelItem.FindFirstGeometry().ActiveColor (R/G/B floats 0-1).
    Applied via IfcSurfaceStyleRendering + IfcStyledItem on each IfcTriangulatedFaceSet.

Materials / Classification:
    The parent node of each geometry leaf carries the material name (e.g. "Acero, 45-345").
    Written as IfcMaterial and linked via IfcRelAssociatesMaterial.
    Materials are de-duplicated so each unique name produces a single IfcMaterial instance.

Property Sets:
    All Navisworks property categories are walked up the ancestor hierarchy.
    Each non-empty, non-internal category becomes one IfcPropertySet.
    Internal/metadata categories are excluded via blacklist.
"""

import clr
import sys
import json
import uuid
from pathlib import Path

clr.AddReference("Autodesk.Navisworks.Api")

from Autodesk.Navisworks.Api import Application

# PyNET bundle folder of the RUNNING Navisworks (right year, never hardcoded): the folder
# of the engine assembly executing this script. See docs/navisworks.md "CastUtils".
from System import AppDomain
_bundle = Path(next(a for a in AppDomain.CurrentDomain.GetAssemblies()
               if a.GetName().Name == "Raen.Core.Pynet.Engine").Location).parent
sys.path.append(str(_bundle))

clr.AddReference(next(a.GetName().Name for a in AppDomain.CurrentDomain.GetAssemblies()
                      if a.GetName().Name.startswith("Raen.Navisworks.Pynet.")))  # year-suffixed plugin

import ifcopenshell
import ifcopenshell.guid

# Property categories excluded from IFC export.
_SKIP_CATS = {
    "Elemento", "Element",
    "Geometría", "Geometry",
    "TimeLiner",
    "Material de Autodesk", "Autodesk Material",
    "Material",
    "Transformar", "Transform",
    "Identidad", "Identity",
    "Proyecto", "Project",
    "Ubicación", "Location",
    "Orientation", "DemolishedPhaseId", "CreatedPhaseId",
    "Id", "WorksetId", "Document",
}


# ─── Element extractor ────────────────────────────────────────────────────────

class ElementExtractor:
    """
    Thin wrapper around the C# IFCElementExtractor.
    Returns tuples of (name, verts, faces, color, mat_name, props) — one entry
    per sub-mesh so each color surface becomes a separate IFC element.
    """

    _SKIP_CATEGORIES = {
        "Habitaciones", "Rooms", "Room",
        "Espacios", "Spaces", "Space",
        "Líneas", "Lines", "Líneas de modelo", "Model Lines",
        "Líneas de detalle", "Detail Lines",
        "<Separación de espacios>", "<Space Separation>",
    }
    _FAST_CATS = {
        "Soportes", "Structural Columns", "Vegetación", "Planting",
        "Bordes de losa", "Slab Edges", "Columnas arquitectónicas", "Columns",
        "Mobiliario", "Furniture", "Aparatos sanitarios", "Plumbing Fixtures",
        "Equipamiento mecánico", "Mechanical Equipment", "Vigas", "Structural Framing",
        "Pilares", "Columns", "Barandillas", "Railings", "Escaleras", "Stairs",
        "Entorno", "Entourage", "Circulación vertical", "Vertical Circulation",
        "Rampas", "Ramps",
    }
    _INSTNODE_CATS = {
        "Ventanas", "Windows", "Muebles de obra", "Casework",
        "Luminarias", "Lighting Fixtures",
        "Equipo de servicios alimentarios", "Food Service Equipment",
        "Emplazamiento", "Site",
    }
    _DIRECT_CATS = {
        "Paneles de muro cortina", "Curtain Panels",
        "Montantes de muro cortina", "Curtain Wall Mullions",
        "Muros cortina", "Curtain Walls", "Puertas", "Doors",
        "Modelos genéricos", "Generic Models", "Aparcamiento", "Parking",
        "Equipos especializados", "Specialty Equipment",
        "Barandales superiores", "Top Rails", "Pasamanos", "Handrails",
        "Barridos de muro", "Wall Sweeps",
    }
    _PERLEAF_CATS = {"Muros", "Walls", "Techos", "Ceilings", "Suelos", "Floors", "Cubiertas", "Roofs"}

    def __init__(self):
        from Raen.Navisworks.Pynet.Utils import IFCElementExtractor  # type: ignore
        self._ext = IFCElementExtractor()
        for c in self._SKIP_CATEGORIES:
            self._ext.SkipCategories.Add(c)
        for c in self._FAST_CATS:
            self._ext.FastCats.Add(c)
        for c in self._INSTNODE_CATS:
            self._ext.InstNodeCats.Add(c)
        for c in self._DIRECT_CATS:
            self._ext.DirectCats.Add(c)
        for c in self._PERLEAF_CATS:
            self._ext.PerLeafCats.Add(c)
        for c in _SKIP_CATS:
            self._ext.SkipPropCats.Add(c)

    def extract(self, index: int) -> list:
        model = Application.ActiveDocument.Models[index]
        raw = self._ext.ExtractModel(model.RootItem)
        results = []
        for info in raw:
            props = json.loads(info.PropertiesJson) if info.PropertiesJson else {}
            for sm in info.SubMeshes:
                fv, ff = sm.FlatVertices, sm.FlatFaces
                nv, nf = len(fv) // 3, len(ff) // 3
                verts = [[fv[i*3], fv[i*3+1], fv[i*3+2]] for i in range(nv)]
                faces = [[ff[i*3], ff[i*3+1], ff[i*3+2]] for i in range(nf)]
                color = (sm.ColorR, sm.ColorG, sm.ColorB) if sm.HasColor else None
                results.append((info.Name, verts, faces, color, info.MaterialName, props))
        return results


# ─── IFC file builder ─────────────────────────────────────────────────────────

class IFCWriter:
    """Builds and writes a single IFC4 file with tessellated geometry, colors,
    materials and property sets."""

    def __init__(self, project_name: str):
        self._ifc        = ifcopenshell.file(schema="IFC4")
        self._pending:   list = []
        self._materials: dict = {}
        self._build_skeleton(project_name)

    # ── Public ────────────────────────────────────────────────────────────────

    def add_element(self, name: str, verts: list, faces: list,
                    color=None, mat_name: str = "", props: dict = None):
        if not verts or not faces:
            return
        geo   = self._tessellation(verts, faces, color)
        place = self._world_placement()
        elem  = self._ifc.createIfcBuildingElementProxy(
            self._guid(), None, name, None, None, place, geo, None
        )
        if mat_name:
            self._associate_material(elem, mat_name)
        if props:
            self._add_property_sets(elem, props)
        self._pending.append(elem)

    def save(self, path: Path) -> Path:
        if self._pending:
            self._ifc.createIfcRelContainedInSpatialStructure(
                self._guid(), None, None, None, self._pending, self._storey
            )
        self._ifc.write(str(path))
        return path

    # ── Private ───────────────────────────────────────────────────────────────

    def _guid(self) -> str:
        return ifcopenshell.guid.compress(uuid.uuid4().hex)

    def _pt(self, xyz):
        return self._ifc.createIfcCartesianPoint(list(xyz))

    def _world_placement(self):
        ax = self._ifc.createIfcAxis2Placement3D(self._pt([0.0, 0.0, 0.0]), None, None)
        return self._ifc.createIfcLocalPlacement(None, ax)

    def _tessellation(self, verts: list, faces: list, color=None):
        coord_list = self._ifc.createIfcCartesianPointList3D([list(v) for v in verts])
        tri_set    = self._ifc.createIfcTriangulatedFaceSet(coord_list, None, None, faces, None)
        if color is not None:
            self._apply_color(tri_set, *color)
        shape = self._ifc.createIfcShapeRepresentation(
            self._body_ctx, "Body", "Tessellation", [tri_set]
        )
        return self._ifc.createIfcProductDefinitionShape(None, None, [shape])

    def _apply_color(self, tri_set, r: float, g: float, b: float):
        colour    = self._ifc.createIfcColourRgb(None, r, g, b)
        rendering = self._ifc.createIfcSurfaceStyleRendering(
            colour, 0.0, None, None, None, None, None, None, "FLAT"
        )
        style = self._ifc.createIfcSurfaceStyle(None, "BOTH", [rendering])
        self._ifc.createIfcStyledItem(tri_set, [style], None)

    def _associate_material(self, element, material_name: str):
        if material_name not in self._materials:
            self._materials[material_name] = self._ifc.createIfcMaterial(
                material_name, None, None
            )
        self._ifc.createIfcRelAssociatesMaterial(
            self._guid(), None, None, None, [element], self._materials[material_name]
        )

    def _add_property_sets(self, element, props: dict):
        for pset_name, properties in props.items():
            if not properties:
                continue
            ifc_props = [
                self._ifc.createIfcPropertySingleValue(
                    prop_name, None,
                    self._ifc.createIfcLabel(str(value)),
                    None
                )
                for prop_name, value in properties.items()
            ]
            pset = self._ifc.createIfcPropertySet(
                self._guid(), None, pset_name, None, ifc_props
            )
            self._ifc.createIfcRelDefinesByProperties(
                self._guid(), None, None, None, [element], pset
            )

    def _build_skeleton(self, name: str):
        units = self._ifc.createIfcUnitAssignment([
            self._ifc.createIfcSIUnit(None, "LENGTHUNIT",  None, "METRE"),
            self._ifc.createIfcSIUnit(None, "AREAUNIT",    None, "SQUARE_METRE"),
            self._ifc.createIfcSIUnit(None, "VOLUMEUNIT",  None, "CUBIC_METRE"),
        ])
        ax2p = self._ifc.createIfcAxis2Placement3D(
            self._pt([0.0, 0.0, 0.0]),
            self._ifc.createIfcDirection([0.0, 0.0, 1.0]),
            self._ifc.createIfcDirection([1.0, 0.0, 0.0]),
        )
        self._ctx = self._ifc.createIfcGeometricRepresentationContext(
            None, "Model", 3, 1.0e-5, ax2p, None
        )
        self._body_ctx = self._ifc.createIfcGeometricRepresentationSubContext(
            "Body", "Model", None, None, None, None, self._ctx, None, "MODEL_VIEW", None
        )
        self._project = self._ifc.createIfcProject(
            self._guid(), None, name, None, None, None, None, [self._ctx], units
        )
        p0 = self._world_placement()
        self._site = self._ifc.createIfcSite(
            self._guid(), None, "Site", None, None, p0, None, None,
            "ELEMENT", None, None, None, None, None
        )
        self._building = self._ifc.createIfcBuilding(
            self._guid(), None, "Building", None, None, p0, None, None,
            "ELEMENT", None, None, None
        )
        self._storey = self._ifc.createIfcBuildingStorey(
            self._guid(), None, "Level 0", None, None, p0, None, None,
            "ELEMENT", 0.0
        )
        self._agg(self._project,  [self._site])
        self._agg(self._site,     [self._building])
        self._agg(self._building, [self._storey])

    def _agg(self, parent, children):
        self._ifc.createIfcRelAggregates(self._guid(), None, None, None, parent, children)


# ─── Orchestrator ─────────────────────────────────────────────────────────────

class ExportManager:

    def __init__(self, doc, out_dir: Path):
        self._doc       = doc
        self._out_dir   = out_dir
        self._extractor = ElementExtractor()
        out_dir.mkdir(parents=True, exist_ok=True)

    def run(self) -> list:
        n = self._doc.Models.Count
        print(f"Found {n} linked model(s)")
        saved = []

        for i in range(n):
            model = self._doc.Models[i]
            stem  = Path(model.FileName).stem
            print(f"\n[{i+1}/{n}] {stem}")

            elements = self._extractor.extract(i)
            print(f"  Elements with geometry: {len(elements)}")

            if not elements:
                print("  No geometry — skipping")
                continue

            writer = IFCWriter(stem)
            for name, verts, faces, color, mat, props in elements:
                writer.add_element(name, verts, faces, color, mat, props)

            out = self._out_dir / f"{stem}.ifc"
            writer.save(out)
            print(f"  Saved → {out}")
            saved.append(out)

        print(f"\nExport complete: {len(saved)}/{n} IFC file(s) → {self._out_dir}")
        return saved


# ─── Entry point ──────────────────────────────────────────────────────────────

doc = Application.ActiveDocument

if doc.Models.Count == 0:
    print("No models loaded in the active document.")
else:
    try:
        out_dir = Path(doc.FileName).parent / "IFC_Export"
    except Exception:
        out_dir = Path(doc.Models[0].FileName).parent / "IFC_Export"

    ExportManager(doc, out_dir).run()
