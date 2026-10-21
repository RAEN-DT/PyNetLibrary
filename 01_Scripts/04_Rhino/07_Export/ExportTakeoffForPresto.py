# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import json
import math
import re
import uuid
from datetime import datetime
from pathlib import Path

import clr

clr.AddReference("RhinoCommon")

from System import Environment
from Rhino import RhinoApp, RhinoDoc, RhinoMath, UnitSystem
from Rhino.DocObjects import InstanceObject, ObjectEnumeratorSettings, ObjectType
from Rhino.Geometry import (AreaMassProperties, BoundingBox, Brep, Curve, Extrusion, Mesh, Point, PointCloud, Point3d,
                            SubD, Surface, Transform, Vector3d, VolumeMassProperties)

# The host injects the active document as __rhinodoc__
try:
    doc = __rhinodoc__
except NameError:
    doc = RhinoDoc.ActiveDoc

# ---------------------------------------------------------------------------
# Quantity takeoff for RIB Presto with ISO 19650 traceability: ONE
# MEASUREMENT LINE PER MODEL OBJECT, each carrying an IFC GlobalId, so every
# budget quantity can be traced back to the Rhino object (and to the IFC
# exported from it). Read-only on the model.
#
# Output: one JSON on the Desktop, "<model> - Presto takeoff.json", in the
# format of 01_Scripts/06_Presto/02_Write/CreateBudgetFromJson.py (chapters >
# partidas with unit and quantity) plus, per partida, its "lines" for
# 01_Scripts/06_Presto/02_Write/WriteMeasurementLinesFromJson.py, and a
# "source" block (file, date, unit system, skipped objects, warnings).
# Same format as 01_Scripts/05_Tekla/06_Export/ExportTakeoffForPresto.py.
# Workflow:
#   1. this script (Rhino)  2. CreateBudgetFromJson.py (Presto, the tree)
#   3. WriteMeasurementLinesFromJson.py (Presto, the lines)
#   4. 01_Read/ReadMeasurementLines.py (Presto, the traceability check)
#
# - Units: always the unit of the Rhino document (doc.ModelUnitSystem, set
#   in Rhino: Options > Units): metres -> metres, mm -> mm..., scaled to
#   metres for Presto with RhinoMath.UnitScale. If the geometry does not fit
#   that unit (whole model outside PLAUSIBLE_EXTENT_M or median object
#   outside PLAUSIBLE_MEDIAN_M - e.g. drawn in metres in a mm file) the
#   script STOPS before writing anything: fix the unit in Rhino (_Units,
#   without scaling the geometry) and run it again. ABORT_ON_UNIT_MISMATCH =
#   False only warns.
# - Unit per object (UNIT_BY_KIND): closed Brep / Extrusion / Mesh / SubD ->
#   m3 (VolumeMassProperties), open ones -> m2 (AreaMassProperties), curves
#   -> m (GetLength), points and block instances -> u. COUNT_CLASSES (e.g.
#   doors, windows) are always counted in u. Blocks: BLOCK_MODE "count" (one
#   line per instance) or "explode" (virtual: one line per definition object,
#   transformed by the instance, nested blocks included; nothing is changed).
# - Line = N x Longitud x Anchura x Altura (m). m3: the box aligned to the
#   object's horizontal edges (Longitud >= Anchura in plan, Altura = Z); when
#   its volume differs from the real one (> DIM_TOLERANCE: openings, slopes,
#   curved shapes) the line is Longitud = volume and the object is listed in
#   "dimension_mismatches". m2: the two largest box sides when they match the
#   area, else Longitud = area. m: Longitud = length. u: N = 1.
# - Line quantities are rounded to DECIMALS, like Presto does with
#   Obra.DecCantMed = DECIMALS, so "quantity" (sum of the rounded lines) is
#   what Presto will show; "quantity_model" is the unrounded model total.
# - GuidElem: the IFC GlobalId stored in user text (IFC_GUID_KEYS - IFC
#   imports, VisualARQ, Rhino.Inside) or, without one, the IFC 22-char
#   compression of the Rhino object Id (said in Nota). Exploded block pieces
#   get a stable id derived from the instance Id + the piece Id. A user-text
#   GlobalId repeated on several objects (copied objects keep their user
#   text) is kept on the first one only; the others fall back to their Id.
# - CategoríaBIM: user text (IFC_CLASS_KEYS), else the first LAYER_CLASS_MAP
#   pattern matching the layer path (leaf layer first), else
#   IfcBuildingElementProxy. TipoBIM: user text TYPE_KEYS, else the object
#   name without trailing numbering, else the block name. FamiliaBIM: layer
#   full path. Área: user text BUILDING_KEYS, else BUILDING, else the model.
# - Planta / Cota: user text LEVEL_KEYS / ELEVATION_KEYS, else a layer path
#   segment matching LEVEL_LAYER_RE, else the highest level <= the object's
#   reference Z (base; top for slabs/roofs) + 1 mm, from LEVELS (m) or
#   auto-detected from wall/column bases and slab tops (rounded to 1 cm,
#   levels closer than LEVEL_MERGE_M merged into the lower one).
#
# Verified elsewhere in the library (Rhino 8): GetObjectList with
# ObjectEnumeratorSettings, Layers.FindIndex / FullPath / IsVisible /
# IsLocked, GetUserStrings / AllKeys, Extrusion.ToBrep, Brep.IsSolid,
# Mesh.IsClosed, Area/VolumeMassProperties.Compute, GetBoundingBox(True),
# Transform.Rotation / Multiply. The IFC compression is the Tekla script's
# (checked against a Tekla IFC4 export).
# Run on Rhino 8 (2026-10-20, Burj_khalifa.3dm): 238 closed solids -> 4
# partidas / 2 chapters in m3, 165 storeys auto-detected, GuidElem from the
# Rhino ids. That file says Millimeters but is drawn in metres: read in mm
# every quantity came out ~0 (0.834 m model), which the unit check now stops.
# ⏳ Not exercised by that model: Brep.TryConvertBrep (SubD / Surface),
# InstanceDefinition.GetObjects + InstanceXform for "explode",
# Attributes.Space, Curve.GetLength, IFC GUID / class from user text.
# A GlobalId compressed from the Rhino Id does NOT necessarily match the one
# a Rhino IFC exporter writes: export with the same GUIDs, or store the
# exporter's GlobalId in user text first. Nothing is saved or changed.
# ---------------------------------------------------------------------------
JSON_PATH = None               # None -> Desktop / "<model> - Presto takeoff.json"
SELECTION_ONLY = False         # True -> only the selected objects
ROOT_SUMMARY = ""              # "" -> "<model> - takeoff"
PLAUSIBLE_EXTENT_M = (2.0, 10000.0)     # whole model (largest bounding box side), metres
PLAUSIBLE_MEDIAN_M = (0.05, 200.0)      # median object size (largest bounding box side), metres
ABORT_ON_UNIT_MISMATCH = True  # True -> stop when the geometry does not fit the document unit; False -> warn

# Grouping keys: "ifc_class", "layer", "top_layer", "type", "name", "kind", "planta" (the unit is always added)
GROUP_BY = ("ifc_class", "layer", "type")
CHAPTER_BY = "ifc_class"       # "ifc_class", "top_layer", "layer", or None for a single chapter
SINGLE_CHAPTER_SUMMARY = "Obra"

UNIT_BY_KIND = {"solid": "m3", "surface": "m2", "curve": "m", "point": "u", "block": "u"}   # each kind: its unit or "u"
COUNT_CLASSES = ("IfcDoor", "IfcWindow", "IfcFurnishingElement")   # always counted in u
BLOCK_MODE = "count"           # "count" -> 1 u per instance; "explode" -> measure the block's objects
DECIMALS = 3                   # Presto Obra.DecCantMed / Conceptos.RedParc
DIM_TOLERANCE = 0.002          # 0.2 % box dims product vs real volume / area

SKIP_HIDDEN_LAYERS = True      # objects on layers that are off
SKIP_LOCKED_LAYERS = False
SKIP_HIDDEN_OBJECTS = False    # objects hidden with Hide
INCLUDE_REFERENCE_OBJECTS = False   # worksession / linked-block objects

# User text keys (matched ignoring case, spaces, "_", "-" and ".")
IFC_GUID_KEYS = ("IfcGUID", "IFC GUID", "GlobalId", "IfcGlobalId", "IFC_GUID", "GUID IFC")
IFC_CLASS_KEYS = ("IfcClass", "IFC Class", "IfcEntity", "IFC Entity", "IfcExportAs")
TYPE_KEYS = ("Type", "TypeName", "Tipo", "IfcType")
LEVEL_KEYS = ("IfcBuildingStorey", "Level", "Planta", "Storey", "Nivel")
ELEVATION_KEYS = ("Elevation", "Cota", "LevelElevation")      # metres
BUILDING_KEYS = ("IfcBuilding", "Building", "Edificio")

LAYER_CLASS_MAP = [            # (regex on a layer name, IFC class) - first match wins, leaf layer first
    (r"muro\s*cortina|curtain", "IfcCurtainWall"),
    (r"muro|wall|tabique|partition", "IfcWall"),
    (r"losa|forjado|slab|floor|solera", "IfcSlab"),
    (r"pilar|column", "IfcColumn"),
    (r"viga|beam|j[aá]cena", "IfcBeam"),
    (r"cubierta|roof|tejado", "IfcRoof"),
    (r"zapata|cimentaci|footing|foundation|encepado", "IfcFooting"),
    (r"pilote|pile", "IfcPile"),
    (r"escalera|stair", "IfcStair"),
    (r"barandilla|railing", "IfcRailing"),
    (r"puerta|door", "IfcDoor"),
    (r"ventana|window", "IfcWindow"),
    (r"revestimiento|acabado|covering|falso\s*techo|ceiling", "IfcCovering"),
    (r"mobiliario|furniture", "IfcFurnishingElement"),
]
DEFAULT_CLASS = "IfcBuildingElementProxy"
SLAB_CLASSES = ("IfcSlab", "IfcRoof", "IfcCovering")   # their level is taken at the top, not the base
TYPE_STRIP_RE = r"[\s_\-#.]+\d+$"                    # "Muro 03" -> "Muro" when the name is the type

LEVELS = []                    # m, e.g. [0, 3.0, 6.0] or [("Planta baja", 0.0), ("Planta 1", 3.0)]; [] -> auto
LEVEL_MERGE_M = 0.3
LEVEL_LAYER_RE = r"(?i)^(planta|nivel|level|storey|piso|s[oó]tano|basement)\b"   # layer segment = storey
STOREY_NAME = "Planta {index:02d} ({elevation:+.2f} m)"
BUILDING = ""                  # Área for every object without user text; "" -> model name

CLASS_LABELS = {               # partida summary / chapter summary per IFC class
    "IfcWall": ("Muro", "Muros"), "IfcCurtainWall": ("Muro cortina", "Muros cortina"),
    "IfcSlab": ("Losa", "Losas y forjados"), "IfcColumn": ("Pilar", "Pilares"), "IfcBeam": ("Viga", "Vigas"),
    "IfcRoof": ("Cubierta", "Cubiertas"), "IfcFooting": ("Cimentación", "Cimentaciones"),
    "IfcPile": ("Pilote", "Pilotes"), "IfcStair": ("Escalera", "Escaleras"),
    "IfcRailing": ("Barandilla", "Barandillas"), "IfcDoor": ("Puerta", "Puertas"),
    "IfcWindow": ("Ventana", "Ventanas"), "IfcCovering": ("Revestimiento", "Revestimientos"),
    "IfcFurnishingElement": ("Mobiliario", "Mobiliario"), "IfcMember": ("Barra", "Barras"),
    "IfcPlate": ("Chapa", "Chapas"), "IfcBuildingElementProxy": ("Elemento", "Otros elementos"),
}
PARTIDA_SUMMARY = "{label} {type} - {layer_leaf} ({count} ud)"   # WriteMeasurementLinesFromJson CLEAN_SUMMARIES drops "(...)"

MAX_ORIENT_EDGES = 400         # edges / mesh faces sampled to find the plan orientation of the box
MAX_ORIENT_ANGLES = 6

CH64 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_$"
IFC22_RE = re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")
HEXGUID_RE = re.compile(r"^\{?[0-9a-fA-F]{8}-?[0-9a-fA-F]{4}-?[0-9a-fA-F]{4}-?[0-9a-fA-F]{4}-?[0-9a-fA-F]{12}\}?$")
SKIP_TYPES = {"ClipPlane", "Detail", "Annotation", "TextDot", "Light", "Hatch", "Grip", "Phantom",
              "Cage", "MorphControl", "InstanceDefinition"}
NATURAL_UNIT = {"solid": "m3", "surface": "m2", "curve": "m", "point": "u", "block": "u"}
MEASURABLE = (Brep, Extrusion, Mesh, SubD, Surface, Curve, Point, PointCloud)


def ifc_guid(guid):
    """IFC GlobalId (22 chars) from a GUID string: 2 chars from byte 0, then 5 x (3 bytes -> 4 chars)."""
    h = str(guid).replace("-", "").replace("{", "").replace("}", "")
    bs = [int(h[i:i + 2], 16) for i in range(0, 32, 2)]

    def b64(v, n):
        s = ""
        for _ in range(n):
            s = CH64[v % 64] + s
            v //= 64
        return s
    return b64(bs[0], 2) + "".join(b64((bs[i] << 16) + (bs[i + 1] << 8) + bs[i + 2], 4) for i in range(1, 16, 3))


def norm(key):
    return re.sub(r"[\s_\-.]", "", str(key)).lower()


def user_texts(attrs):
    out = {}
    if attrs.UserStringCount:
        strings = attrs.GetUserStrings()   # NameValueCollection
        for key in strings.AllKeys:
            value = strings[key]
            if key and value and str(value).strip():
                out[norm(key)] = str(value).strip()
    return out


def ut(texts, keys):
    for key in keys:
        value = texts.get(norm(key))
        if value:
            return value
    return ""


def to_float(text):
    try:
        return float(str(text).replace(",", "."))
    except ValueError:
        return None


def r(v, n=DECIMALS):
    return None if v is None else round(v, n)


def fits(product, target):
    return abs(product - target) <= DIM_TOLERANCE * max(target, 1e-9) + 0.5 * 10 ** -DECIMALS


# --- document -------------------------------------------------------------------
model_file = doc.Path or ""
model_name = Path(doc.Name).stem if doc.Name else (Path(model_file).stem if model_file else "Untitled")
try:
    rhino_version = str(RhinoApp.Version)
except Exception:
    rhino_version = ""

layers = {}
for layer in doc.Layers:
    if layer is None or layer.IsDeleted:
        continue
    path = layer.FullPath
    layers[layer.Index] = {"path": path, "top": path.split("::")[0], "leaf": path.split("::")[-1],
                           "visible": layer.IsVisible, "locked": layer.IsLocked}
NO_LAYER = {"path": "?", "top": "?", "leaf": "?", "visible": True, "locked": False}

layer_class_re = [(re.compile(p, re.I), c) for p, c in LAYER_CLASS_MAP]
level_layer_re = re.compile(LEVEL_LAYER_RE) if LEVEL_LAYER_RE else None
type_strip_re = re.compile(TYPE_STRIP_RE) if TYPE_STRIP_RE else None
for kind_, unit_ in UNIT_BY_KIND.items():
    if unit_ not in (NATURAL_UNIT[kind_], "u"):
        raise Exception(f"UNIT_BY_KIND['{kind_}'] = '{unit_}': only '{NATURAL_UNIT[kind_]}' or 'u' can be measured.")
if BLOCK_MODE not in ("count", "explode"):
    raise Exception("BLOCK_MODE must be 'count' or 'explode'.")


def class_from_layer(path):
    for segment in reversed(path.split("::")):
        for rx, cls in layer_class_re:
            if rx.search(segment):
                return cls
    return ""


def level_from_layer(path):
    if not level_layer_re:
        return ""
    for segment in reversed(path.split("::")):
        if level_layer_re.search(segment.strip()):
            return segment.strip()
    return ""


# --- geometry -------------------------------------------------------------------
def plan_angles(geom):
    """Candidate plan rotations (rad, modulo 90 deg) from the horizontal edges of a Brep / Mesh."""
    weights = {}

    def add(dx, dy, dz):
        lh = (dx * dx + dy * dy) ** 0.5
        if lh <= 0 or abs(dz) > 0.01 * (lh + abs(dz)):
            return
        deg = round(math.degrees(math.atan2(dy, dx)) % 90.0, 2) % 90.0
        weights[deg] = weights.get(deg, 0.0) + lh

    if isinstance(geom, Brep):
        for i, edge in enumerate(geom.Edges):
            if i >= MAX_ORIENT_EDGES:
                break
            v = edge.PointAtEnd - edge.PointAtStart
            add(v.X, v.Y, v.Z)
    elif isinstance(geom, Mesh):
        for i in range(min(geom.Faces.Count, MAX_ORIENT_EDGES)):
            f = geom.Faces[i]
            a, b = geom.Vertices[f.A], geom.Vertices[f.B]
            add(b.X - a.X, b.Y - a.Y, b.Z - a.Z)
    best = sorted(weights, key=lambda d: -weights[d])[:MAX_ORIENT_ANGLES]
    return [0.0] + [math.radians(d) for d in best if d != 0.0]


def box_dims(geom):
    """(Longitud, Anchura, Altura) in m of the smallest box over the candidate plan rotations."""
    best = None
    for angle in plan_angles(geom):
        bb = geom.GetBoundingBox(Transform.Rotation(-angle, Vector3d.ZAxis, Point3d.Origin)) if angle \
            else geom.GetBoundingBox(True)
        dx, dy, dz = (bb.Max.X - bb.Min.X) * k, (bb.Max.Y - bb.Min.Y) * k, (bb.Max.Z - bb.Min.Z) * k
        score = (dx * dy * dz, dx * dy)
        if best is None or score < best[0]:
            best = (score, (max(dx, dy), min(dx, dy), dz))
    return best[1]


def measure(geom):
    """{kind, qty (m3/m2/m/u), dims, area, length, volume} or (None, reason)."""
    if isinstance(geom, Curve):
        length = geom.GetLength() * k
        if length <= 0:
            return None, "curve of zero length"
        return {"kind": "curve", "qty": length, "length": length, "dims": None}, ""
    if isinstance(geom, (Point, PointCloud)):
        return {"kind": "point", "qty": 1.0, "dims": None}, ""
    if isinstance(geom, Extrusion):
        work = geom.ToBrep(True)
    elif isinstance(geom, (Brep, Mesh)):
        work = geom
    else:
        work = Brep.TryConvertBrep(geom)            # SubD, Surface
        if work is None and isinstance(geom, SubD):
            work = Mesh.CreateFromSubD(geom, 3)
    if work is None:
        return None, "geometry could not be converted to a Brep or Mesh"
    closed = work.IsClosed if isinstance(work, Mesh) else work.IsSolid
    if closed:
        vmp = VolumeMassProperties.Compute(work)
        volume = abs(vmp.Volume) * k ** 3 if vmp else 0.0
        if volume <= 0:
            return None, "closed geometry without volume (VolumeMassProperties failed)"
        return {"kind": "solid", "qty": volume, "volume": volume, "dims": box_dims(work)}, ""
    amp = AreaMassProperties.Compute(work)
    area = abs(amp.Area) * k ** 2 if amp else 0.0
    if area <= 0:
        return None, "open geometry without area (AreaMassProperties failed)"
    return {"kind": "surface", "qty": area, "area": area, "dims": box_dims(work)}, ""


# --- objects ---------------------------------------------------------------------
settings = ObjectEnumeratorSettings()
settings.NormalObjects = True
settings.LockedObjects = True
settings.HiddenObjects = True
settings.IdefObjects = False
settings.IncludeLights = False
settings.IncludeGrips = False
settings.ReferenceObjects = INCLUDE_REFERENCE_OBJECTS
settings.ObjectTypeFilter = ObjectType.AnyObject
if SELECTION_ONLY:
    settings.SelectedObjectsFilter = True
objects = list(doc.Objects.GetObjectList(settings))


# --- units: the document's, checked against the size of the geometry -------------------
units_used = doc.ModelUnitSystem
k = RhinoMath.UnitScale(units_used, UnitSystem.Meters)
unit_note = ""
raw_sizes, model_box = [], BoundingBox.Empty
for obj in objects:
    try:
        bb = obj.Geometry.GetBoundingBox(True)
    except Exception:
        continue
    if not bb.IsValid:
        continue
    side = max(bb.Max.X - bb.Min.X, bb.Max.Y - bb.Min.Y, bb.Max.Z - bb.Min.Z)
    if side > 0:
        raw_sizes.append(side)
        model_box = BoundingBox.Union(model_box, bb)   # static: a struct copy is never mutated in place
if raw_sizes:
    raw_sizes.sort()
    median_m = raw_sizes[len(raw_sizes) // 2] * k
    extent_m = max(model_box.Max.X - model_box.Min.X, model_box.Max.Y - model_box.Min.Y,
                   model_box.Max.Z - model_box.Min.Z) * k
    if not (PLAUSIBLE_EXTENT_M[0] <= extent_m <= PLAUSIBLE_EXTENT_M[1]
            and PLAUSIBLE_MEDIAN_M[0] <= median_m <= PLAUSIBLE_MEDIAN_M[1]):
        unit_note = (f"in the document unit ({units_used}) the model measures {extent_m:g} m and the median object "
                     f"{median_m:g} m: the geometry looks drawn in another unit. Fix the unit in Rhino (_Units, "
                     f"without scaling) and run the script again")
        if ABORT_ON_UNIT_MISMATCH:
            raise Exception(unit_note + " - nothing was written (ABORT_ON_UNIT_MISMATCH = False to export anyway).")
        print("UNITS: " + unit_note)

step = max(1, len(objects) // 10)
print(f"Reading {len(objects)} objects of {model_name} (units {units_used}, x{k:g} -> m)...")

items, no_quantity, ignored, skipped_counts = [], [], {}, {}
attrs_bbox = {}                # block instance id -> bounding box (BLOCK_MODE "count")


def count(bucket, key):
    bucket[key] = bucket.get(key, 0) + 1


def add_item(geom, rhino_id, attrs, layer, texts, parent_texts, guid, guid_source, block_name, notes):
    ifc_class, class_source = ut(texts, IFC_CLASS_KEYS) or ut(parent_texts, IFC_CLASS_KEYS), "user_text"
    if ifc_class:
        ifc_class = ifc_class.split(".")[0]                # "IfcSlab.FLOOR" -> IfcSlab
    else:
        ifc_class, class_source = class_from_layer(layer["path"]), "layer"
        if not ifc_class:
            ifc_class, class_source = DEFAULT_CLASS, "default"
            notes.append(f"clase IFC por defecto ({DEFAULT_CLASS})")
        else:
            notes.append("clase IFC por nombre de capa")
    if block_name is not None and geom is None:
        m, reason = {"kind": "block", "qty": 1.0, "dims": None}, ""
    else:
        m, reason = measure(geom)
    if m is None:
        no_quantity.append({"id": rhino_id, "layer": layer["path"], "name": attrs.Name or "", "reason": reason})
        return
    unit = "u" if ifc_class in COUNT_CLASSES else UNIT_BY_KIND[m["kind"]]
    name = attrs.Name or ""
    type_ = ut(texts, TYPE_KEYS) or ut(parent_texts, TYPE_KEYS)
    if not type_ and name:
        type_ = type_strip_re.sub("", name).strip() if type_strip_re else name
    if not type_ and block_name:
        type_ = block_name
    bb = (geom.GetBoundingBox(True) if geom is not None else attrs_bbox[rhino_id])
    items.append({
        "id": rhino_id, "guid": guid, "guid_source": guid_source, "ifc_class": ifc_class, "class_source": class_source,
        "layer": layer["path"], "top_layer": layer["top"], "layer_leaf": layer["leaf"], "name": name, "type": type_,
        "kind": m["kind"], "unit": unit, "m": m, "notes": notes, "block": block_name or "",
        "zmin": bb.Min.Z * k, "zmax": bb.Max.Z * k, "ref_x": bb.Min.X * k, "ref_y": bb.Min.Y * k,
        "storey": ut(texts, LEVEL_KEYS) or ut(parent_texts, LEVEL_KEYS) or level_from_layer(layer["path"]),
        "elevation": to_float(ut(texts, ELEVATION_KEYS) or ut(parent_texts, ELEVATION_KEYS)),
        "building": ut(texts, BUILDING_KEYS) or ut(parent_texts, BUILDING_KEYS) or BUILDING or model_name,
    })


def guid_of(texts, rhino_id):
    value = ut(texts, IFC_GUID_KEYS)
    if value and IFC22_RE.match(value):
        return value, "user_text"
    if value and HEXGUID_RE.match(value):
        return ifc_guid(value), "user_text"
    return ifc_guid(rhino_id), "rhino_id"


def explode(inst, xform, path, inst_texts, inst_layer, depth):
    idef = inst.InstanceDefinition
    for piece in idef.GetObjects() or []:
        piece_path = path + [str(piece.Id)]
        if isinstance(piece, InstanceObject):
            if depth > 10:
                count(ignored, "nested blocks deeper than 10")
                continue
            explode(piece, Transform.Multiply(xform, piece.InstanceXform), piece_path, inst_texts, inst_layer, depth + 1)
            continue
        if str(piece.ObjectType) in SKIP_TYPES or not isinstance(piece.Geometry, MEASURABLE):
            count(ignored, str(piece.ObjectType))
            continue
        geom = piece.DuplicateGeometry()
        geom.Transform(xform)
        layer = layers.get(piece.Attributes.LayerIndex, inst_layer)
        if not class_from_layer(layer["path"]) and class_from_layer(inst_layer["path"]):
            layer = inst_layer                              # piece on a generic layer: use the instance's
        pid = str(uuid.uuid5(uuid.UUID(path[0]), "/".join(piece_path[1:])))
        add_item(geom, pid, piece.Attributes, layer, user_texts(piece.Attributes), inst_texts,
                 ifc_guid(pid), "block_piece", idef.Name,
                 [f"pieza del bloque {idef.Name} (GuidElem = Id instancia {path[0]} + Id pieza)"])


for i, obj in enumerate(objects, 1):
    if i % step == 0:
        print(f"  {i}/{len(objects)}")
    otype = str(obj.ObjectType)
    if otype in SKIP_TYPES:
        count(ignored, otype)
        continue
    attrs = obj.Attributes
    if str(attrs.Space) == "PageSpace":
        count(ignored, "layout (page space) object")
        continue
    if obj.IsReference and not INCLUDE_REFERENCE_OBJECTS:
        count(skipped_counts, "reference object")
        continue
    layer = layers.get(attrs.LayerIndex, NO_LAYER)
    if SKIP_HIDDEN_LAYERS and not layer["visible"]:
        count(skipped_counts, "hidden layer")
        continue
    if SKIP_LOCKED_LAYERS and layer["locked"]:
        count(skipped_counts, "locked layer")
        continue
    if SKIP_HIDDEN_OBJECTS and obj.IsHidden:
        count(skipped_counts, "hidden object")
        continue
    rid = str(obj.Id)
    texts = user_texts(attrs)
    if isinstance(obj, InstanceObject):
        if BLOCK_MODE == "explode":
            explode(obj, obj.InstanceXform, [rid], texts, layer, 1)
            continue
        attrs_bbox[rid] = obj.Geometry.GetBoundingBox(True)
        guid, source_ = guid_of(texts, rid)
        add_item(None, rid, attrs, layer, texts, {}, guid, source_, obj.InstanceDefinition.Name,
                 [] if source_ == "user_text" else ["GuidElem = Id Rhino comprimido (sin IfcGUID en texto de usuario)"])
        continue
    if not isinstance(obj.Geometry, MEASURABLE):
        count(ignored, otype)
        continue
    guid, source_ = guid_of(texts, rid)
    add_item(obj.Geometry, rid, attrs, layer, texts, {}, guid, source_, None,
             [] if source_ == "user_text" else ["GuidElem = Id Rhino comprimido (sin IfcGUID en texto de usuario)"])

if not items:
    raise Exception("No measurable objects to export" + (" in the selection." if SELECTION_ONLY else ".")
                    + f" Not measurable: {len(no_quantity)}, ignored: {ignored}, skipped: {skipped_counts}")

# --- unique GuidElem --------------------------------------------------------------
duplicate_guids, seen_guids = [], set()
for it in items:
    if it["guid"] in seen_guids and it["guid_source"] == "user_text":
        duplicate_guids.append({"id": it["id"], "layer": it["layer"], "ifc_guid": it["guid"]})
        it["guid"], it["guid_source"] = ifc_guid(it["id"]), "rhino_id"
        it["notes"].append("IfcGUID de texto de usuario repetido (objeto copiado): GuidElem = Id Rhino comprimido")
    seen_guids.add(it["guid"])
all_guids = [it["guid"] for it in items]
if len(set(all_guids)) != len(all_guids):
    raise Exception("Repeated GuidElem after the fallback - check the IFC GUID user text of the model.")

# --- levels -----------------------------------------------------------------------
for it in items:
    it["ref_z"] = it["zmax"] if it["ifc_class"] in SLAB_CLASSES and it["kind"] in ("solid", "surface") else it["zmin"]


def merge_levels(values):
    out = []
    for z in sorted(set(round(v * 100.0) / 100.0 for v in values)):
        if not out or z - out[-1] > LEVEL_MERGE_M:
            out.append(z)
    return out


if LEVELS:
    levels = sorted([(str(lv[0]), float(lv[1])) if isinstance(lv, (tuple, list)) else ("", float(lv))
                     for lv in LEVELS], key=lambda t: t[1])
    levels_source = "LEVELS"
else:
    cand = [it["ref_z"] for it in items if it["kind"] == "solid" and it["ifc_class"] in ("IfcWall", "IfcColumn", "IfcSlab")]
    levels_source = "auto (wall/column bases, slab tops)"
    if not cand:
        cand = [it["zmin"] for it in items]
        levels_source = "auto (object bases)"
    levels = [("", z) for z in merge_levels(cand)]

for it in items:
    idx = 0
    for j, (_, z) in enumerate(levels):
        if z <= it["ref_z"] + 0.001:
            idx = j
    lname, lz = levels[idx]
    level_name = lname or STOREY_NAME.format(index=idx, elevation=lz)
    if it["storey"]:
        it["planta"] = it["storey"]
        named = [z for n, z in levels if n and n.lower() == it["storey"].lower()]
        it["cota"] = round(it["elevation"] if it["elevation"] is not None else (named[0] if named else lz), 3)
    else:
        it["planta"] = level_name
        it["cota"] = round(it["elevation"] if it["elevation"] is not None else lz, 3)

# --- one measurement line per object --------------------------------------------------
mismatches, groups = [], {}
for it in items:
    m, unit, notes = it["m"], it["unit"], it["notes"]
    L = A = H = None
    comment_dims = ""
    bim_long = bim_sup = bim_vol = None
    if m["dims"]:
        bim_long = r(max(m["dims"]))
    if unit == "u":
        if m["kind"] not in ("point", "block"):
            notes.append(f"contado en ud ({m['qty']:.3f} {NATURAL_UNIT[m['kind']]} en el modelo)")
    elif unit == "m":
        L = r(m["length"])
        bim_long = r(m["length"])
        comment_dims = " - Longitud m"
    elif unit == "m3":
        bim_vol = r(m["volume"], 4)
        dl, da, dh = (r(v) for v in m["dims"])
        if fits(dl * da * dh, m["volume"]):
            L, A, H = dl, da, dh
            comment_dims = " - L x A x H m"
        else:
            mismatches.append({"id": it["id"], "layer": it["layer"], "name": it["name"],
                               "box_m3": round(dl * da * dh, 4), "volume_m3": round(m["volume"], 4)})
            L = r(m["volume"])
            notes.append("forma no prismática (huecos, pendientes, curvas): Longitud = volumen del modelo m3")
    elif unit == "m2":
        bim_sup = r(m["area"], 4)
        dl, da, dh = (r(v) for v in m["dims"])
        smallest = min((dl, "L"), (da, "A"), (dh, "H"))[1]
        pair = {"L": (None, da, dh), "A": (dl, None, dh), "H": (dl, da, None)}[smallest]
        product = (pair[0] or 1) * (pair[1] or 1) * (pair[2] or 1)
        if fits(product, m["area"]):
            L, A, H = pair
            if L is None:                                  # keep Longitud filled: Anchura x Altura -> Longitud x Altura
                L, A = A, None
            comment_dims = " - lados del rectángulo m"
        else:
            mismatches.append({"id": it["id"], "layer": it["layer"], "name": it["name"],
                               "box_m2": round(product, 4), "area_m2": round(m["area"], 4)})
            L = r(m["area"])
            notes.append("superficie no rectangular: Longitud = área del modelo m2")
    n = 1
    qty = round(n * (L if L is not None else 1) * (A if A is not None else 1) * (H if H is not None else 1), DECIMALS)
    model_qty = 1.0 if unit == "u" else m["qty"]
    label = CLASS_LABELS.get(it["ifc_class"], (it["ifc_class"], it["ifc_class"]))[0]
    line = {
        "Comentario": f"{it['name'] or it['type'] or label} - {it['planta']}{comment_dims}".strip(),
        "N": n, "Longitud": L, "Anchura": A, "Altura": H,
        "GuidElem": it["guid"], "CategoríaBIM": it["ifc_class"], "TipoBIM": it["type"], "FamiliaBIM": it["layer"],
        "Planta": it["planta"], "Cota": it["cota"], "Área": it["building"], "Archivo": model_file or model_name,
        "BIMLong": bim_long, "BIMSup": bim_sup, "BIMVol": bim_vol,
        "Nota": "; ".join(notes),
        "_quantity": qty, "_model_quantity": model_qty, "_rhino_id": it["id"], "_guid_source": it["guid_source"],
    }
    if CHAPTER_BY == "ifc_class":
        ckey = it["ifc_class"]
    elif CHAPTER_BY in ("top_layer", "layer"):
        ckey = it[CHAPTER_BY]
    else:
        ckey = ""
    key = (ckey,) + tuple(it[g] for g in GROUP_BY) + (unit,)
    g = groups.setdefault(key, {"unit": unit, "lines": [], "sample": it, "chapter": ckey})
    g["lines"].append((it["cota"], it["ref_x"], it["ref_y"], line))

# --- chapters and partidas ---------------------------------------------------------------
chapters = {}
for key, g in groups.items():
    chapters.setdefault(g["chapter"], []).append((key, g))

out_chapters, partida_rows = [], []
for ci, ckey in enumerate(sorted(chapters), start=1):
    ccode = "%02d" % ci
    if not CHAPTER_BY:
        csummary = SINGLE_CHAPTER_SUMMARY
    elif CHAPTER_BY == "ifc_class":
        csummary = CLASS_LABELS.get(ckey, (ckey, ckey))[1]
    else:
        csummary = str(ckey)
    partidas = []
    for pi, (key, g) in enumerate(sorted(chapters[ckey], key=lambda kg: kg[0]), start=1):
        s = g["sample"]
        lines = [t[3] for t in sorted(g["lines"], key=lambda t: (t[0], t[1], t[2]))]
        label = CLASS_LABELS.get(s["ifc_class"], (s["ifc_class"], s["ifc_class"]))[0]
        stype = "" if s["type"].lower() == label.lower() else s["type"]
        summary = PARTIDA_SUMMARY.format(label=label, type=stype, name=s["name"], layer=s["layer"],
                                         layer_leaf=s["layer_leaf"], top_layer=s["top_layer"],
                                         ifc_class=s["ifc_class"], unit=g["unit"], count=len(lines))
        summary = re.sub(r"\s+", " ", summary.replace(" -  - ", " - ")).replace(" - (", " (").strip()
        quantity = round(sum(l["_quantity"] for l in lines), DECIMALS)
        model_qty = sum(l["_model_quantity"] for l in lines)
        pcode = "%s.%02d" % (ccode, pi)
        group = dict(zip(GROUP_BY, key[1:-1]))
        group["unit"] = g["unit"]
        partidas.append({"code": pcode, "summary": summary, "unit": g["unit"], "quantity": quantity,
                         "quantity_model": round(model_qty, 4), "group": group, "lines": lines})
        partida_rows.append({"type": "PrestoPartida", "code": pcode, "summary": summary, "unit": g["unit"],
                             "objects": len(lines), "quantity": quantity, "quantity_model": round(model_qty, 4)})
    out_chapters.append({"code": ccode, "summary": csummary, "partidas": partidas})

# --- warnings -----------------------------------------------------------------------------
warnings = []
if unit_note:
    warnings.append(unit_note)
guid_sources = {}
class_sources = {}
for it in items:
    count(guid_sources, it["guid_source"])
    count(class_sources, it["class_source"])
if guid_sources.get("rhino_id") or guid_sources.get("block_piece"):
    warnings.append("GuidElem compressed from Rhino ids for objects without IFC GUID user text: it matches an "
                    "IFC export only if the exporter uses the same ids")
if duplicate_guids:
    warnings.append(f"{len(duplicate_guids)} objects repeated an IFC GUID from user text (copied objects)")

source = {
    "application": "Rhino", "rhino_version": rhino_version, "model": model_file or model_name,
    "date": datetime.now().isoformat(timespec="seconds"),
    "unit_system": str(doc.ModelUnitSystem), "unit_system_used": str(units_used), "scale_to_m": k,
    "selection_only": SELECTION_ONLY, "block_mode": BLOCK_MODE,
    "objects_read": len(objects), "objects_in_lines": sum(row["objects"] for row in partida_rows),
    "group_by": list(GROUP_BY), "chapter_by": CHAPTER_BY, "decimals": DECIMALS,
    "levels_m": [{"name": n or STOREY_NAME.format(index=j, elevation=z), "elevation": z} for j, (n, z) in enumerate(levels)],
    "levels_source": levels_source, "guid_sources": guid_sources, "class_sources": class_sources,
    "skipped": skipped_counts, "ignored_types": ignored, "objects_without_quantity": no_quantity,
    "dimension_mismatches": mismatches, "duplicate_ifc_guids": duplicate_guids, "warnings": warnings,
}
data = {"root_summary": ROOT_SUMMARY or f"{model_name} - takeoff", "source": source, "chapters": out_chapters}

out = Path(JSON_PATH) if JSON_PATH else \
    Path(Environment.GetFolderPath(Environment.SpecialFolder.Desktop)) / f"{model_name} - Presto takeoff.json"
with open(out, "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=1)

# --- summary ---------------------------------------------------------------------------------
print(f"{len(objects)} objects read, {source['objects_in_lines']} in {len(partida_rows)} partidas "
      f"({len(out_chapters)} chapters). Units {units_used} (x{k:g} -> m). GuidElem: {guid_sources}.")
for row in partida_rows:
    print(f"  {row['code']}  {row['quantity']:>12,.3f} {row['unit']:<3} {row['objects']:>4} obj  {row['summary']}")
if no_quantity:
    print(f"  WITHOUT QUANTITY {len(no_quantity)} objects - first: {no_quantity[0]}")
if skipped_counts:
    print(f"  Skipped: {skipped_counts}")
if ignored:
    print(f"  Ignored (not measurable): {ignored}")
if mismatches:
    print(f"  {len(mismatches)} objects whose box != real quantity: written as Longitud = model quantity")
print(f"  Levels ({levels_source}): {[round(z, 2) for _, z in levels]}")
for w in warnings:
    print(f"  WARNING: {w}")
print(f"Saved {out}")

ia_Result = {"type": "RhinoPrestoTakeoff", "file": str(out), "objects": len(items), "without_quantity": len(no_quantity),
             "dimension_mismatches": len(mismatches), "unit_system": str(units_used), "guid_sources": guid_sources,
             "duplicate_ifc_guids": len(duplicate_guids), "levels_m": source["levels_m"], "warnings": warnings,
             "partidas": partida_rows}
