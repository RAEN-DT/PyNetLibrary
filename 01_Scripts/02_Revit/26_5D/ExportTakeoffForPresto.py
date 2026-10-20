# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import json
import re
from datetime import datetime
from pathlib import Path

import clr

clr.AddReference("RevitAPI")

from System import Environment
from Autodesk.Revit.DB import (BuiltInCategory, BuiltInParameter, ElementId, ExportUtils,
                               FilteredElementCollector, Level, ParameterTypeId, UnitTypeId, UnitUtils)

# __revit__ is injected by the plugin - always use this to get the document
uidoc = __revit__.ActiveUIDocument  # type: ignore
doc = uidoc.Document

# ---------------------------------------------------------------------------
# Quantity takeoff for RIB Presto with ISO 19650 traceability: ONE
# MEASUREMENT LINE PER ELEMENT, each carrying the element's IFC GlobalId, so
# every budget quantity can be traced back to the model element (and to the
# IFC exported from it). Read-only on the model: no transaction.
#
# Output: one JSON on the Desktop, "<model> - Presto takeoff.json", in the
# format of 01_Scripts/06_Presto/02_Write/CreateBudgetFromJson.py (chapters >
# partidas with unit and quantity) plus, per partida, its "lines" for
# 01_Scripts/06_Presto/02_Write/WriteMeasurementLinesFromJson.py, and a
# "source" block (model, date, GUID sources, skipped elements, dimension
# mismatches, warnings). Same format as the Tekla exporter
# 01_Scripts/05_Tekla/06_Export/ExportTakeoffForPresto.py. Workflow:
#   1. this script (Revit)  2. CreateBudgetFromJson.py (Presto, the tree)
#   3. WriteMeasurementLinesFromJson.py (Presto, the lines)
#   4. 01_Read/ReadMeasurementLines.py (Presto, the traceability check)
#
# - Elements of the CATEGORIES below (instances only: no types, no
#   view-specific elements, no nested shared components, no stacked-wall
#   members, no secondary design options / demolished unless configured).
# - Partidas = elements grouped by GROUP_BY (default category + family +
#   type); chapters = CHAPTER_BY (default the category). A group whose
#   elements get different units (structural material per instance) is split.
# - Unit per category from UNITS: m3 (HOST_VOLUME_COMPUTED), m2
#   (HOST_AREA_COMPUTED), m (CURVE_ELEM_LENGTH / STRUCTURAL_FRAME_CUT_LENGTH /
#   INSTANCE_LENGTH_PARAM) or u (N = 1). A pair (a, b) = a when the
#   structural material (or the family name) matches CONCRETE_RE, b
#   otherwise. kg is NOT offered: Revit has no weight parameter.
# - Line dims (m): m3 = Longitud x Anchura x Altura (wall length x width x
#   height, beam/column length x b x h, footing L x W x T) or superficie x
#   espesor (floors, roofs, ceilings: Longitud = area m2, Altura = thickness);
#   m2 walls = Longitud x Anchura (length x height); m = Longitud; u = N.
#   Checked against the model quantity (DIM_TOLERANCE); when they differ
#   (openings, joins, edited profiles) the line becomes (volume / thickness) x
#   thickness, or the model quantity in Longitud, with a Nota, and the element
#   is listed in source.dimension_mismatches.
# - Line quantities are rounded to DECIMALS, like Presto does with
#   Obra.DecCantMed = DECIMALS, so "quantity" (sum of the rounded lines) is
#   what Presto will show; "quantity_model" is the unrounded model total.
# - GuidElem = IFC GlobalId: the IfcGUID parameter (IFC_GUID, written by an
#   IFC export with "Store the IFC GUID") when set, valid and not repeated;
#   otherwise ExportUtils.GetExportId(doc, id) compressed to 22 chars - what
#   Revit's IFC exporter does for an element without IfcGUID (if the call
#   fails: episode GUID of the UniqueId XOR the element id, the same value;
#   a difference between both is reported in warnings). Repeated
#   IfcGUID values (elements copied after an export) fall back to the
#   computed GUID. The Nota of every line says which source was used.
# - CategoríaBIM: "Export to IFC As" (IFC_EXPORT_ELEMENT_AS, instance then
#   type) or the shared parameter IfcExportAs, else the category's default
#   class from CATEGORIES (flagged in Nota). Planta / Cota: the element's
#   level (LevelId or the category's level parameter) and its elevation (m).
#   Área: BUILDING or Project Information > Building Name (else project Name).
#
# Verified elsewhere in the library (✅): collectors per BuiltInCategory and
# GetParameter(ParameterTypeId.CurveElemLength / HostAreaComputed) +
# UnitUtils (26_5D/QuantityTakeoff.py); LevelId + level parameters, Level
# Elevation, DesignOption.IsPrimary, PHASE_DEMOLISHED, ElementType.FamilyName,
# ProjectInformation, PathName, UniqueId, str(ElementId(bic)) category match,
# CubicMeters (22_Exportations/RevitToPNT.py); Selection.GetElementIds
# (01_Selection User/AddSelection.py); get_BoundingBox(None) (03_Edit and
# Create Objects/ElementTransformUtilsRotate.py); the IFC GUID compression
# (Tekla exporter, matched 570 parts of an IFC4 export).
# Run on Revit 2025 (2026-10-20, AmigaNekane.rvt): 121 elements read, 84
# exported in 33 partidas / 7 chapters (36 secondary design option + 1
# nested skipped), GuidElem from the IfcGUID parameter for all 84, walls /
# floors in m2 with BIMLong / BIMSup / BIMVol, 20 dims != model quantity
# (openings) written with the model quantity. Valid JSON for Presto.
# ⏳ Still not exercised by that model: ExportUtils.GetExportId == the GlobalId of Revit's IFC export (check one
# element against an exported IFC); the ParameterTypeId members not used
# elsewhere (HostVolumeComputed, IfcGuid, IfcExportElementAs/TypeAs,
# WallAttrWidthParam, WallUserHeightParam, Floor/Roof thickness,
# CeilingThickness, StructuralFoundation*, StructuralFrameCutLength,
# InstanceLengthParam, StructuralMaterialParam); section / footing
# parameter names (SECTION_PARAMS, FOOTING_PARAMS - family dependent);
# railing length; stacked walls. Check the summary and source.warnings.
# Nothing is saved in the model.
# ---------------------------------------------------------------------------
JSON_PATH = None               # None -> Desktop / "<model> - Presto takeoff.json"
SELECTION_ONLY = False         # True -> only the elements selected in Revit
ROOT_SUMMARY = ""              # "" -> "<model> - takeoff"

# Grouping keys: "category", "family", "type", "ifc_class", "predefined", "level", "material", "area"
GROUP_BY = ("category", "family", "type")
CHAPTER_BY = "category"        # one of the keys above, or None for a single chapter
SINGLE_CHAPTER_SUMMARY = "Edificio"

INCLUDE_SECONDARY_OPTIONS = False   # True -> also elements of secondary design options
INCLUDE_DEMOLISHED = False          # True -> also elements with a demolition phase
SKIP_NESTED = True                  # True -> skip shared nested components (counted in their parent)

# (key, BuiltInCategory, default IFC class, partida label, chapter summary) - chapter order
CATEGORIES = [
    ("walls", BuiltInCategory.OST_Walls, "IfcWall", "Muro", "Muros"),
    ("structural_foundations", BuiltInCategory.OST_StructuralFoundation, "IfcFooting", "Cimentación", "Cimentaciones"),
    ("structural_columns", BuiltInCategory.OST_StructuralColumns, "IfcColumn", "Pilar", "Pilares"),
    ("structural_framing", BuiltInCategory.OST_StructuralFraming, "IfcBeam", "Viga", "Vigas"),
    ("floors", BuiltInCategory.OST_Floors, "IfcSlab", "Suelo", "Suelos y forjados"),
    ("roofs", BuiltInCategory.OST_Roofs, "IfcRoof", "Cubierta", "Cubiertas"),
    ("ceilings", BuiltInCategory.OST_Ceilings, "IfcCovering", "Techo", "Techos"),
    ("columns", BuiltInCategory.OST_Columns, "IfcColumn", "Pilar arquitectónico", "Pilares arquitectónicos"),
    ("stairs", BuiltInCategory.OST_Stairs, "IfcStair", "Escalera", "Escaleras"),
    ("railings", BuiltInCategory.OST_StairsRailing, "IfcRailing", "Barandilla", "Barandillas"),
    ("doors", BuiltInCategory.OST_Doors, "IfcDoor", "Puerta", "Puertas"),
    ("windows", BuiltInCategory.OST_Windows, "IfcWindow", "Ventana", "Ventanas"),
    ("furniture", BuiltInCategory.OST_Furniture, "IfcFurniture", "Mueble", "Mobiliario"),
    ("plumbing_fixtures", BuiltInCategory.OST_PlumbingFixtures, "IfcSanitaryTerminal", "Aparato sanitario", "Aparatos sanitarios"),
    ("lighting_fixtures", BuiltInCategory.OST_LightingFixtures, "IfcLightFixture", "Luminaria", "Luminarias"),
    ("generic_models", BuiltInCategory.OST_GenericModel, "IfcBuildingElementProxy", "Modelo genérico", "Modelos genéricos"),
]
UNITS = {                      # unit per category key; a pair = (concrete, other); missing -> "u"
    "walls": "m2", "floors": "m2", "roofs": "m2", "ceilings": "m2",
    "structural_foundations": "m3", "structural_columns": ("m3", "u"), "structural_framing": ("m3", "m"),
    "railings": "m",
}
CONCRETE_RE = r"^C\d|^HA|^HM|concrete|hormig"          # structural material / family -> first unit of a pair
SECTION_PARAMS = (("b", "h"), ("Width", "Depth"), ("Anchura", "Canto"), ("Ancho", "Canto"))   # type, then instance
FOOTING_PARAMS = (("Length", "Width", "Foundation Thickness"), ("Longitud", "Anchura", "Grosor de cimentación"))
DECIMALS = 3                   # Presto Obra.DecCantMed / Conceptos.RedParc
DIM_TOLERANCE = 0.002          # 0.2 % dims product vs model quantity

BUILDING = ""                  # Área for every element; "" -> Building Name, else project Name, else model name
NO_LEVEL = "Sin nivel"
PARTIDA_SUMMARY = "{label} {family}: {type} ({count} ud)"   # WriteMeasurementLinesFromJson CLEAN_SUMMARIES drops "(...)"

CH64 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_$"
IFC_GUID_RE = re.compile(r"^[0-3][0-9A-Za-z_$]{21}$")


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


def uid_guid(uid):
    """Export GUID from a UniqueId ("<episode GUID>-<element id hex>"): last 8 hex of the episode XOR the id."""
    if len(uid) != 45 or uid[36] != "-":
        return ""
    return uid[:28] + "%08x" % (int(uid[28:36], 16) ^ int(uid[37:45], 16))


def eid_val(eid):
    try:
        return int(eid.Value)         # Revit 2024+
    except AttributeError:
        return int(eid.IntegerValue)  # older versions


def param(el, ptid):
    if el is None:
        return None
    try:
        return el.GetParameter(ptid)
    except Exception:
        return None


def num(el, ptid, unit=UnitTypeId.Meters):
    p = param(el, ptid)
    if p is None or not p.HasValue:
        return 0.0
    try:
        return float(UnitUtils.ConvertFromInternalUnits(p.AsDouble(), unit))
    except Exception:
        return 0.0


def first_num(els, ptids, unit=UnitTypeId.Meters):
    for el in els:
        for ptid in ptids:
            v = num(el, ptid, unit)
            if v > 0:
                return v
    return 0.0


def named_num(els, name):
    for el in els:
        if el is None:
            continue
        p = el.LookupParameter(name)
        if p is not None and p.HasValue:
            try:
                v = float(UnitUtils.ConvertFromInternalUnits(p.AsDouble(), UnitTypeId.Meters))
            except Exception:
                v = 0.0
            if v > 0:
                return v
    return 0.0


def text(el, ptid):
    p = param(el, ptid)
    return (p.AsString() or "").strip() if p is not None and p.HasValue else ""


def level_of(el, levels):
    lid = None
    try:
        if el.LevelId is not None and el.LevelId != ElementId.InvalidElementId:
            lid = el.LevelId
    except Exception:
        pass
    if lid is None:
        for ptid in LEVEL_PARAMS:
            p = param(el, ptid)
            if p is not None and p.AsElementId() != ElementId.InvalidElementId:
                lid = p.AsElementId()
                break
    if lid is not None and str(lid) in levels:
        return levels[str(lid)]
    return (NO_LEVEL, None)


def ifc_class_of(el, t, default):
    """(class, predefined, from_param) from "Export to IFC As" / IfcExportAs, else the category default."""
    value = text(el, ParameterTypeId.IfcExportElementAs) or text(t, ParameterTypeId.IfcExportElementTypeAs)
    if not value:
        for e in (el, t):
            p = e.LookupParameter("IfcExportAs") if e is not None else None
            if p is not None and p.HasValue and (p.AsString() or "").strip():
                value = p.AsString().strip()
                break
    if not value:
        return default, "", False
    cls, _, predefined = value.partition(".")
    if cls.endswith("Type") and len(cls) > 7:
        cls = cls[:-4]
    return cls, predefined, True


def material_of(el, t):
    for e in (el, t):
        p = param(e, ParameterTypeId.StructuralMaterialParam)
        if p is not None and p.AsElementId() != ElementId.InvalidElementId:
            m = doc.GetElement(p.AsElementId())
            if m is not None:
                return m.Name or ""
    return ""


def r(v, n=DECIMALS):
    return None if v is None else round(v, n)


def product(L, A, H):
    v = 1.0
    for d in (L, A, H):
        if d is not None:
            v *= d
    return v


LEVEL_PARAMS = (ParameterTypeId.InstanceReferenceLevelParam, ParameterTypeId.FamilyLevelParam,
                ParameterTypeId.FamilyBaseLevelParam, ParameterTypeId.WallBaseConstraint,
                ParameterTypeId.StairsBaseLevelParam, ParameterTypeId.RoofBaseLevelParam,
                ParameterTypeId.StairsRailingBaseLevelParam, ParameterTypeId.LevelParam,
                ParameterTypeId.ScheduleLevelParam)
LENGTH_PARAMS = (ParameterTypeId.CurveElemLength, ParameterTypeId.StructuralFrameCutLength,
                 ParameterTypeId.InstanceLengthParam)
THICKNESS_PARAMS = (ParameterTypeId.FloorAttrThicknessParam, ParameterTypeId.FloorAttrDefaultThicknessParam,
                    ParameterTypeId.RoofAttrThicknessParam, ParameterTypeId.RoofAttrDefaultThicknessParam,
                    ParameterTypeId.CeilingThickness, ParameterTypeId.StructuralFoundationThickness)

# --- model ------------------------------------------------------------------------
model_file = doc.PathName or doc.Title
model_name = Path(doc.PathName).stem if doc.PathName else doc.Title.replace(".rvt", "")
info = doc.ProjectInformation
building = BUILDING or (info.BuildingName if info is not None else "") or (info.Name if info is not None else "") or model_name
try:
    revit_version = str(__revit__.Application.VersionNumber)  # type: ignore
except Exception:
    revit_version = ""
levels = {str(lv.Id): (lv.Name, round(UnitUtils.ConvertFromInternalUnits(lv.Elevation, UnitTypeId.Meters), 3))
          for lv in FilteredElementCollector(doc).OfClass(Level)}
cat_by_id = {str(ElementId(c[1])): c for c in CATEGORIES}

# --- elements -----------------------------------------------------------------------
if SELECTION_ONLY:
    candidates = [doc.GetElement(i) for i in uidoc.Selection.GetElementIds()]
else:
    candidates = []
    for c in CATEGORIES:
        candidates.extend(FilteredElementCollector(doc).OfCategory(c[1]).WhereElementIsNotElementType().ToElements())
total = len(candidates)
step = max(1, total // 10)
print(f"Reading {total} elements of {model_name}...")

elements, skipped, seen = [], [], 0
for el in candidates:
    seen += 1
    if seen % step == 0:
        print(f"  {seen}/{total}")
    if el is None or el.Category is None:
        continue
    cat = cat_by_id.get(str(el.Category.Id))
    if cat is None:
        continue
    key, _, default_class, label, _ = cat
    base = {"id": eid_val(el.Id), "category": key, "name": el.Name or ""}
    reason = ""
    if el.ViewSpecific:
        reason = "view-specific element"
    elif not INCLUDE_SECONDARY_OPTIONS and el.DesignOption is not None and not el.DesignOption.IsPrimary:
        reason = "secondary design option"
    elif not INCLUDE_DEMOLISHED and el.get_Parameter(BuiltInParameter.PHASE_DEMOLISHED) is not None \
            and el.get_Parameter(BuiltInParameter.PHASE_DEMOLISHED).AsElementId() != ElementId.InvalidElementId:
        reason = "demolished"
    else:
        try:
            if SKIP_NESTED and el.SuperComponent is not None:
                reason = "nested shared component (counted in its parent)"
        except AttributeError:
            pass
        try:
            if el.IsStackedWallMember:
                reason = "stacked wall member (the stacked wall is measured)"
        except AttributeError:
            pass
    if not reason and el.get_BoundingBox(None) is None:
        reason = "no geometry"
    if reason:
        skipped.append(dict(base, reason=reason))
        continue
    t = doc.GetElement(el.GetTypeId())
    family = ""
    try:
        family = t.FamilyName if t is not None else ""
    except Exception:
        pass
    ifc_class, predefined, ifc_from_param = ifc_class_of(el, t, default_class)
    lvl_name, cota = level_of(el, levels)
    mark_p = el.get_Parameter(BuiltInParameter.ALL_MODEL_MARK)
    e = dict(base, uid=el.UniqueId, label=label, family=family, type=(t.Name if t is not None else "") or "",
             mark=(mark_p.AsString() or "").strip() if mark_p is not None and mark_p.HasValue else "",
             ifc_class=ifc_class, predefined=predefined, ifc_guessed=not ifc_from_param,
             level=lvl_name, planta=lvl_name, cota=cota, area=building, material=material_of(el, t),
             volume=num(el, ParameterTypeId.HostVolumeComputed, UnitTypeId.CubicMeters),
             surface=num(el, ParameterTypeId.HostAreaComputed, UnitTypeId.SquareMeters),
             length=first_num([el], LENGTH_PARAMS),
             width=first_num([t, el], (ParameterTypeId.WallAttrWidthParam,)) if key == "walls" else 0.0,
             height=num(el, ParameterTypeId.WallUserHeightParam) if key == "walls" else 0.0,
             thick=first_num([el, t], THICKNESS_PARAMS))
    e["section"] = None
    for bn, hn in SECTION_PARAMS:
        b, h = named_num([t, el], bn), named_num([t, el], hn)
        if b > 0 and h > 0:
            e["section"] = (b, h)
            break
    e["footing"] = None
    fl, fw, ft = (first_num([el], (ParameterTypeId.StructuralFoundationLength,)),
                  first_num([el], (ParameterTypeId.StructuralFoundationWidth,)),
                  first_num([el], (ParameterTypeId.StructuralFoundationThickness,)))
    if not (fl > 0 and fw > 0 and ft > 0) and key == "structural_foundations":
        for ln, wn, tn in FOOTING_PARAMS:
            fl, fw, ft = named_num([t, el], ln), named_num([t, el], wn), named_num([t, el], tn)
            if fl > 0 and fw > 0 and ft > 0:
                break
    if fl > 0 and fw > 0 and ft > 0:
        e["footing"] = (fl, fw, ft)
    # IFC GlobalId: stored IfcGUID, else the export id
    stored = text(el, ParameterTypeId.IfcGuid)
    try:
        export_id = str(ExportUtils.GetExportId(doc, el.Id))
    except Exception:
        export_id = ""
    from_uid = uid_guid(el.UniqueId or "")
    e["guid_path"] = "GetExportId" if export_id else "UniqueId"
    e["guid_differs"] = bool(export_id and from_uid and export_id.lower() != from_uid.lower())
    e["computed_guid"] = ifc_guid(export_id or from_uid) if (export_id or from_uid) else ""
    e["stored_guid"] = stored if IFC_GUID_RE.match(stored) else ""
    if not e["stored_guid"] and not e["computed_guid"]:
        skipped.append(dict(base, reason="no IFC GUID (no IfcGUID, GetExportId and UniqueId failed)"))
        continue
    elements.append(e)

if not elements:
    raise Exception("No elements to export" + (" in the selection." if SELECTION_ONLY else "."))

# --- GuidElem: unique per element -------------------------------------------------------
warnings, guid_sources = [], {"IfcGUID": 0, "GetExportId": 0, "UniqueId": 0}
differs = sum(1 for e in elements if e["guid_differs"])
if differs:
    warnings.append(f"{differs} elements: GetExportId != GUID derived from UniqueId (GetExportId used)")
stored_count = {}
for e in elements:
    if e["stored_guid"]:
        stored_count[e["stored_guid"]] = stored_count.get(e["stored_guid"], 0) + 1
repeated = sum(1 for e in elements if e["stored_guid"] and stored_count[e["stored_guid"]] > 1)
if repeated:
    warnings.append(f"{repeated} elements share an IfcGUID value (copied after an IFC export): computed GUID used")
for e in elements:
    if e["stored_guid"] and stored_count[e["stored_guid"]] == 1:
        e["ifc_guid"], e["guid_note"] = e["stored_guid"], "GuidElem: parámetro IfcGUID"
        guid_sources["IfcGUID"] += 1
    else:
        e["ifc_guid"] = e["computed_guid"]
        e["guid_note"] = ("GuidElem: ExportUtils.GetExportId ⏳" if e["guid_path"] == "GetExportId"
                          else "GuidElem: calculado del UniqueId ⏳") + \
            (" (IfcGUID repetido)" if e["stored_guid"] else "")
        guid_sources[e["guid_path"]] += 1
all_guids = [e["ifc_guid"] for e in elements]
if len(set(all_guids)) != len(all_guids):
    dup = sorted(g for g in set(all_guids) if all_guids.count(g) > 1)
    raise Exception(f"Repeated GuidElem after the fallback (nothing written): {dup[:10]}")

# --- one measurement line per element ------------------------------------------------------
concrete_re = re.compile(CONCRETE_RE, re.I)
mismatches, groups = [], {}


def group_key(e, keys):
    return tuple(str(e[k] or "") for k in keys)


def matches(prod, q):
    return abs(prod - q) <= DIM_TOLERANCE * max(q, 1e-6) + 0.5 * 10 ** -DECIMALS


for e in elements:
    rule = UNITS.get(e["category"], "u")
    if isinstance(rule, tuple):
        rule = rule[0] if concrete_re.search(e["material"]) or concrete_re.search(e["family"]) else rule[1]
    unit = rule
    notes = [e["guid_note"]]
    if e["ifc_guessed"]:
        notes.append("clase IFC por categoría (sin IfcExportAs)")
    N, L, A, H = 1, None, None, None
    dims, thick, model_qty = None, e["width"] or e["thick"], 1.0
    if unit == "m3":
        model_qty = e["volume"]
        if e["category"] == "walls" and e["length"] > 0 and e["width"] > 0 and e["height"] > 0:
            dims, thick = (e["length"], e["width"], e["height"]), e["width"]
        elif e["footing"]:
            dims, thick = e["footing"], e["footing"][2]
        elif e["section"] and e["length"] > 0:
            dims, thick = (e["length"], e["section"][0], e["section"][1]), min(e["section"])
        elif e["surface"] > 0 and e["thick"] > 0:
            dims, thick = (e["surface"], None, e["thick"]), e["thick"]
            notes.append("Longitud = superficie m2 x Altura = espesor")
    elif unit == "m2":
        model_qty = e["surface"]
        if e["category"] == "walls" and e["length"] > 0 and e["height"] > 0:
            dims = (e["length"], e["height"], None)
    elif unit == "m":
        model_qty = e["length"]
        dims = (e["length"], None, None)
    if unit != "u" and model_qty <= 0:
        skipped.append({"id": e["id"], "category": e["category"], "name": e["name"],
                        "reason": f"no {unit} quantity in the model (HOST_VOLUME/AREA_COMPUTED or length = 0)"})
        continue
    if unit != "u":
        if dims is not None:
            L, A, H = r(dims[0]), r(dims[1]), r(dims[2])
        prod = product(L, A, H) if dims is not None else 0.0
        if dims is None or not matches(prod, model_qty):
            if dims is not None:
                mismatches.append({"id": e["id"], "guid": e["ifc_guid"], "category": e["category"],
                                   "type": e["type"], "dims": round(prod, 4), "model": round(model_qty, 4), "unit": unit})
                notes = [n for n in notes if not n.startswith("Longitud =")]
            if unit == "m3" and thick > 0:
                L, A, H = r(model_qty / thick), None, r(thick)
                notes.append("huecos, uniones o contorno irregular: Longitud = superficie neta m2 (volumen / espesor)")
            else:
                L, A, H = r(model_qty), None, None
                notes.append(("huecos o perfil editado: " if dims is not None else "")
                             + f"Longitud = cantidad del modelo {unit}")
    qty = round(N * product(L, A, H), DECIMALS) if unit != "u" else 1.0
    comment = " ".join(s for s in (e["mark"], e["type"]) if s) or e["label"]
    line = {
        "Comentario": f"{comment} - {e['planta']}",
        "N": N, "Longitud": L, "Anchura": A, "Altura": H,
        "GuidElem": e["ifc_guid"], "CategoríaBIM": e["ifc_class"],
        "TipoBIM": e["type"], "FamiliaBIM": e["family"],
        "Planta": e["planta"], "Cota": e["cota"], "Área": e["area"], "Archivo": model_file,
        "BIMLong": r(e["length"]) if e["length"] > 0 else None,
        "BIMSup": r(e["surface"], 4) if e["surface"] > 0 else None,
        "BIMVol": r(e["volume"], 4) if e["volume"] > 0 else None,
        "Nota": "; ".join(notes),
        "_quantity": qty, "_revit_id": e["id"], "_unique_id": e["uid"],
        "_model_quantity": model_qty if unit != "u" else 1.0,
    }
    key = group_key(e, GROUP_BY) + (unit,)
    g = groups.setdefault(key, {"unit": unit, "lines": [], "sample": e})
    g["lines"].append((e["cota"] if e["cota"] is not None else -1e9, e["mark"], e["id"], line))

# --- chapters and partidas ----------------------------------------------------------
cat_order = {c[0]: i for i, c in enumerate(CATEGORIES)}
cat_chapter = {c[0]: c[4] for c in CATEGORIES}
chapters = {}
for key, g in groups.items():
    ckey = str(g["sample"][CHAPTER_BY] or "") if CHAPTER_BY else ""
    chapters.setdefault(ckey, []).append((key, g))

if CHAPTER_BY == "category":
    chapter_keys = sorted(chapters, key=lambda k: cat_order.get(k, 999))
else:
    chapter_keys = sorted(chapters)

out_chapters, partida_rows = [], []
for ci, ckey in enumerate(chapter_keys, start=1):
    ccode = "%02d" % ci
    if not CHAPTER_BY:
        csummary = SINGLE_CHAPTER_SUMMARY
    elif CHAPTER_BY == "category":
        csummary = cat_chapter.get(ckey, ckey)
    else:
        csummary = ckey or NO_LEVEL
    partidas = []
    for pi, (key, g) in enumerate(sorted(chapters[ckey], key=lambda kg: kg[0]), start=1):
        s = g["sample"]
        lines = [l for _, _, _, l in sorted(g["lines"], key=lambda t: (t[0], t[1], t[2]))]
        summary = PARTIDA_SUMMARY.format(label=s["label"], family=s["family"], type=s["type"],
                                         ifc_class=s["ifc_class"], level=s["level"], material=s["material"],
                                         count=len(lines)).replace("  ", " ").strip()
        quantity = round(sum(l["_quantity"] for l in lines), DECIMALS)
        model_qty = sum(l["_model_quantity"] for l in lines)
        pcode = "%s.%02d" % (ccode, pi)
        partidas.append({"code": pcode, "summary": summary, "unit": g["unit"], "quantity": quantity,
                         "quantity_model": round(model_qty, 4), "group": dict(zip(GROUP_BY, key)), "lines": lines})
        partida_rows.append({"type": "PrestoPartida", "code": pcode, "summary": summary, "unit": g["unit"],
                             "elements": len(lines), "quantity": quantity, "quantity_model": round(model_qty, 4)})
    out_chapters.append({"code": ccode, "summary": csummary, "partidas": partidas})

if not partida_rows:
    raise Exception(f"No element has a quantity: {len(skipped)} skipped, first: {skipped[:1]}")

skipped_by_reason = {}
for s in skipped:
    skipped_by_reason[s["reason"]] = skipped_by_reason.get(s["reason"], 0) + 1

source = {
    "application": "Autodesk Revit", "version": revit_version, "model": model_file,
    "date": datetime.now().isoformat(timespec="seconds"), "selection_only": SELECTION_ONLY,
    "elements_read": len(elements), "elements_in_lines": sum(r_["elements"] for r_ in partida_rows),
    "group_by": list(GROUP_BY), "chapter_by": CHAPTER_BY, "decimals": DECIMALS,
    "units": {k: list(v) if isinstance(v, tuple) else v for k, v in UNITS.items()},
    "building": building, "levels_m": {name: z for name, z in levels.values()},
    "guid_sources": guid_sources, "warnings": warnings,
    "skipped_by_reason": skipped_by_reason, "skipped_elements": skipped, "dimension_mismatches": mismatches,
}
data = {"root_summary": ROOT_SUMMARY or f"{model_name} - takeoff", "source": source, "chapters": out_chapters}

out = Path(JSON_PATH) if JSON_PATH else \
    Path(Environment.GetFolderPath(Environment.SpecialFolder.Desktop)) / f"{model_name} - Presto takeoff.json"
with open(out, "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=1)

# --- summary ------------------------------------------------------------------------
print(f"{len(elements)} elements read, {source['elements_in_lines']} in {len(partida_rows)} partidas "
      f"({len(out_chapters)} chapters). GuidElem from IfcGUID: {guid_sources['IfcGUID']}, "
      f"GetExportId: {guid_sources['GetExportId']}, UniqueId: {guid_sources['UniqueId']}.")
for row in partida_rows:
    print(f"  {row['code']}  {row['quantity']:>12,.3f} {row['unit']:<3} {row['elements']:>4} el.  {row['summary']}")
for reason, n in sorted(skipped_by_reason.items()):
    print(f"  SKIPPED {n}: {reason}")
if mismatches:
    print(f"  {len(mismatches)} elements where the dims != model quantity: written with the model quantity (see Nota)")
for w in warnings:
    print(f"  WARNING: {w}")
print(f"Saved {out}")

ia_Result = {"type": "RevitPrestoTakeoff", "file": str(out), "elements": len(elements), "skipped": len(skipped),
             "skipped_by_reason": skipped_by_reason, "dimension_mismatches": len(mismatches),
             "guid_sources": guid_sources, "warnings": warnings, "partidas": partida_rows}
