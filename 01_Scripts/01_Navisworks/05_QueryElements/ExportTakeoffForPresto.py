# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import json
import re
from datetime import datetime
from pathlib import Path

import clr

_GLOB_CACHE = {}


def glob_match(name, pattern):
    """fnmatch sobre `re`: el modulo fnmatch no esta en el whitelist del bridge de PyNET.

    Misma semantica que fnmatch.fnmatch con las dos cadenas ya en minusculas, que es como
    llegan aqui: comodines `*`, `?` y clases `[seq]` / `[!seq]`, anclado al texto completo.
    """
    rx = _GLOB_CACHE.get(pattern)
    if rx is None:
        out, i, n = [], 0, len(pattern)
        while i < n:
            c = pattern[i]
            i += 1
            if c == "*":
                out.append(".*")
            elif c == "?":
                out.append(".")
            elif c == "[":
                j = i
                if j < n and pattern[j] in "!^":
                    j += 1
                if j < n and pattern[j] == "]":
                    j += 1
                while j < n and pattern[j] != "]":
                    j += 1
                if j >= n:
                    out.append(re.escape("["))
                else:
                    seq = pattern[i:j].replace("\\", "\\\\")
                    i = j + 1
                    if seq and seq[0] in "!^":
                        seq = "^" + seq[1:]
                    out.append("[" + seq + "]")
            else:
                out.append(re.escape(c))
        rx = re.compile("(?s:" + "".join(out) + ")\Z")
        _GLOB_CACHE[pattern] = rx
    return rx.match(name) is not None


clr.AddReference("Autodesk.Navisworks.Api")
from Autodesk.Navisworks.Api import Application, UnitConversion, Units

from System import Environment

doc = Application.ActiveDocument

# ---------------------------------------------------------------------------
# Quantity takeoff for RIB Presto with ISO 19650 traceability, from a
# FEDERATED Navisworks model (Revit, IFC, Tekla, Civil 3D... appended
# together): ONE MEASUREMENT LINE PER MODEL ELEMENT, each carrying the
# element's IFC GlobalId, so every budget quantity can be traced back to the
# source model. Read-only on the document.
#
# Output: one JSON on the Desktop, "<model> - Presto takeoff.json", in the
# format of 01_Scripts/06_Presto/02_Write/CreateBudgetFromJson.py (chapters >
# partidas with unit and quantity) plus, per partida, its "lines" for
# 01_Scripts/06_Presto/02_Write/WriteMeasurementLinesFromJson.py, and a
# "source" block (document, date, appended models, GUID / quantity sources
# used, skipped elements, warnings). Same JSON as the Tekla version
# (05_Tekla/06_Export/ExportTakeoffForPresto.py). Workflow:
#   1. this script (Navisworks)  2. CreateBudgetFromJson.py (Presto, the tree)
#   3. WriteMeasurementLinesFromJson.py (Presto, the lines)
#   4. 01_Read/ReadMeasurementLines.py (Presto, the traceability check)
#
# - Element = for each geometry node, the first node walking UP that carries
#   an element identity (Revit LcRevitId, an IFC GlobalId / IfcGUID / Tekla
#   GUID from GUID_SOURCES, or an IFC entity) - never a geometry fragment.
#   Stops at spatial IFC nodes (storey, building...) and at the file node;
#   then the geometry node itself is the element (flagged in Nota).
# - GuidElem: first hit of GUID_SOURCES (ordered (category, property) pairs,
#   matched on the internal cat.Name OR the display name, any UI language).
#   UUID-shaped values (Tekla GUID, Navisworks instance GUID) are compressed
#   to the 22-char IFC GlobalId. Last resort = Navisworks InstanceGuid, NOT an
#   IFC GlobalId of the source model: flagged in Nota. Duplicates get a suffix
#   (DUPLICATE_GUIDS) so every GuidElem is unique, and are listed.
# - CategoríaBIM: IFC entity (IFC_CLASS_SOURCES, or ClassDisplayName "Ifc*")
#   else source category (Revit Category...) through CLASS_MAP, else
#   IfcBuildingElementProxy.
# - Unit per element: UNIT_BY_CLASS first, then UNIT_PRIORITY, the first one
#   with a quantity in QTY_SOURCES (Revit Volume/Area/Length, IFC Qto_* /
#   BaseQuantities, Tekla Weight). Converted to m / m2 / m3 from the
#   VariantData type (DoubleLength/Area/Volume are document units) or from
#   the unit suffix of a display string. BBOX_FALLBACK uses the bounding box
#   (flagged). Elements without quantity are skipped and listed
#   (NO_QUANTITY = "count" writes them as 1 u instead).
# - Lines: N x Longitud x Anchura x Altura built from the element's dimension
#   properties when their product matches the quantity (DIM_TOLERANCE), else
#   the quantity goes in Longitud with a Nota. Rounded to DECIMALS like
#   Presto (Obra.DecCantMed = DECIMALS): "quantity" = sum of rounded lines,
#   "quantity_model" = unrounded model total.
# - Planta / Cota: IFC IfcBuildingStorey ancestor (name + Elevation), else a
#   Revit level property (Cota from LEVEL_ELEVATIONS), else the bounding box
#   min Z against LEVELS (m, document coordinates). Área: IfcBuilding
#   ancestor, else BUILDING, else the appended model name. Archivo: the
#   item's Source File property, else the model's source file / file name.
#
# Verified elsewhere in the library (✅): Application.ActiveDocument,
#   doc.Models / model.RootItem.Descendants / model.FileName
#   (01_ModelManagement/GetNwcSourceFile.py), CurrentSelection.SelectedItems
#   (05_QueryElements/PlanViewpointFromSelection.py), PropertyCategories by
#   cat.Name + walk up via Ancestors (05_QueryElements/ExportClashesToJSON.py,
#   03_ClashDetection/ExtractClashElementInfo.py), VariantData Is*/To* incl.
#   ToDoubleArea / ToDoubleVolume (07_IFCExport/NavisworksToPNT.py),
#   UnitConversion.ScaleFactor (04_DataAnalysis/ExportClashDashboard.py),
#   item.BoundingBox() (04_DataAnalysis/ScanHeavyGeometry.py), HasGeometry,
#   InstanceGuid, ClassDisplayName (05_QueryElements/IsolateFoundation.py).
# ⏳ The script as a whole has NOT been run on Navisworks yet: check its
# summary and the "source" warnings. Guessed (stubs only): the internal /
# display names of the IFC, Tekla and Qto categories, ClassDisplayName
# "Ifc*" on IFC items, the "Elevation" of storeys, DataProperty.Name,
# Model.SourceFileName, area / volume scaled by s^2 / s^3, plain doubles
# taken as SI (m, m2, m3, kg). Nothing is saved in the Navisworks document.
# ---------------------------------------------------------------------------
JSON_PATH = None               # None -> Desktop / "<model> - Presto takeoff.json"
SELECTION_ONLY = False         # True -> only the current selection (and its descendants)
MODEL_FILTER = []              # substrings of the appended file names (case-insensitive); [] -> all
ROOT_SUMMARY = ""              # "" -> "<model> - takeoff"

# Grouping keys: "ifc_class", "category", "family", "type", "material", "level", "area", "file"
GROUP_BY = ("ifc_class", "type", "material")
CHAPTER_BY = "ifc_class"       # one of the keys above, or None for a single chapter
SINGLE_CHAPTER_SUMMARY = "Modelo federado"

UNIT_PRIORITY = ("m3", "m2", "m", "kg")   # tried in order after UNIT_BY_CLASS; "u" only via the map / NO_QUANTITY
UNIT_BY_CLASS = {
    "IfcDoor": "u", "IfcWindow": "u", "IfcSanitaryTerminal": "u", "IfcLightFixture": "u",
    "IfcFurnishingElement": "u", "IfcFlowTerminal": "u",
    "IfcPipeSegment": "m", "IfcDuctSegment": "m", "IfcCableCarrierSegment": "m", "IfcRailing": "m",
    "IfcCovering": "m2", "IfcRoof": "m2", "IfcCurtainWall": "m2",
}
NO_QUANTITY = "skip"           # "skip" -> listed in source.items_without_quantity; "count" -> 1 u
BBOX_FALLBACK = False          # True -> no quantity property: m3 of the bounding box (NOT a real measurement)
DECIMALS = 3                   # Presto Obra.DecCantMed / Conceptos.RedParc
DIM_TOLERANCE = 0.002          # 0.2 % dims product vs quantity
DUPLICATE_GUIDS = "suffix"     # "suffix" -> "<guid>-2"... (unique GuidElem); "skip" -> drop the repeats
COMPRESS_UUIDS = True          # UUID-shaped GUIDs -> 22-char IFC GlobalId
MAX_UP = 8                     # nodes walked up from a geometry node looking for the element

LEVELS = []                    # m, e.g. [0.0, 3.5, 7.0] -> Planta from bounding box min Z when no storey/level
LEVEL_ELEVATIONS = {}          # {"Nivel 1": 0.0} -> Cota for Revit level names
LEVEL_TOLERANCE = 0.05         # m
STOREY_NAME = "Planta {index:02d} ({elevation:+.2f} m)"
BUILDING = ""                  # Área for every element; "" -> IfcBuilding name or appended model name

# Ordered (category, property) lookups. Category = internal cat.Name or display name (glob wildcards, any case).
# ("Item", "GUID") = Navisworks InstanceGuid, the last resort.
GUID_SOURCES = [
    ("IFC", "GlobalId"), ("IFC", "GUID"), ("Element", "GlobalId"), ("Element", "IfcGUID"),
    ("LcRevitData_Element", "IfcGUID"), ("Revit", "IfcGUID"), ("*", "IfcGUID"), ("*", "IFC GUID"),
    ("Tekla Common", "GUID"), ("Tekla Common", "IFC GUID"), ("*", "GlobalId"),
    ("Item", "GUID"),
]
IFC_CLASS_SOURCES = [
    ("IFC", "Entity"), ("IFC", "Type"), ("IFC", "IfcEntity"), ("Element", "IfcEntity"),
    ("*", "IfcExportAs"), ("*", "Export to IFC As"), ("*", "Exportar a IFC como"), ("*", "proIfcEntityOvrd"),
]
CATEGORY_SOURCES = [
    ("LcRevitData_Element", "Category"), ("LcRevitData_Element", "Categoría"), ("Element", "Category"),
    ("Tipo de Revit", "Categoría"), ("Revit Type", "Category"), ("LcRevitData_Type", "Category"),
    ("LcRevitData_Type", "Categoría"), ("Other", "Category"),
]
FAMILY_SOURCES = [
    ("LcRevitData_Element", "Family"), ("LcRevitData_Element", "Familia"), ("Element", "Family"),
    ("LcRevitData_Type", "Family Name"), ("LcRevitData_Type", "Nombre de familia"), ("Other", "Family"),
    ("Tekla Common", "Name"),
]
TYPE_SOURCES = [
    ("LcRevitData_Element", "Type"), ("LcRevitData_Element", "Tipo"), ("Element", "Type"),
    ("LcRevitData_Type", "Type Name"), ("LcRevitData_Type", "Nombre de tipo"), ("Other", "Family and Type"),
    ("IFC", "ObjectType"), ("Element", "ObjectType"), ("Tekla Common", "Profile"),
]
MATERIAL_SOURCES = [
    ("LcRevitData_Element", "Structural Material"), ("LcRevitData_Element", "Material estructural"),
    ("LcRevitData_Type", "Structural Material"), ("LcRevitData_Type", "Material estructural"),
    ("Tekla Common", "Material"), ("IFC", "Material"), ("Material", "Name"), ("Material", "Nombre"),
    ("Item", "Material"), ("LcOaNode", "Material"),
]
LEVEL_SOURCES = [
    ("LcRevitData_Element", "Level"), ("LcRevitData_Element", "Nivel"),
    ("LcRevitData_Element", "Base Constraint"), ("LcRevitData_Element", "Restricción de base"),
    ("LcRevitData_Element", "Reference Level"), ("LcRevitData_Element", "Nivel de referencia"),
    ("LcRevitData_Element", "Schedule Level"), ("LcRevitData_Element", "Nivel de planificación"),
    ("Element", "Level"), ("Element", "Base Constraint"),
]
STOREY_ELEVATION_SOURCES = [("IFC", "Elevation"), ("Element", "Elevation"), ("*", "Elevation"), ("*", "Elevación")]
SOURCE_FILE_SOURCES = [("LcOaNode", "Source File"), ("Item", "Source File"), ("LcOaNode", "Archivo de origen")]

QTY_SOURCES = {
    "m3": [("LcRevitData_Element", "Volume"), ("LcRevitData_Element", "Volumen"), ("Element", "Volume"),
           ("Qto_*", "NetVolume"), ("*BaseQuantities", "NetVolume"), ("Qto_*", "GrossVolume"),
           ("*BaseQuantities", "GrossVolume"), ("Tekla Quantity", "Volume"), ("Tekla Common", "Volume"),
           ("Dimensions", "Volume")],
    "m2": [("LcRevitData_Element", "Area"), ("LcRevitData_Element", "Área"), ("Element", "Area"),
           ("Qto_*", "NetSideArea"), ("Qto_*", "NetArea"), ("*BaseQuantities", "NetSideArea"),
           ("*BaseQuantities", "NetArea"), ("Qto_*", "GrossArea"), ("*BaseQuantities", "GrossArea"),
           ("Dimensions", "Area")],
    "m": [("LcRevitData_Element", "Length"), ("LcRevitData_Element", "Longitud"), ("Element", "Length"),
          ("Qto_*", "Length"), ("*BaseQuantities", "Length"), ("Dimensions", "Length"), ("Tekla Common", "Length")],
    "kg": [("Tekla Common", "Weight"), ("Tekla Quantity", "Weight"), ("Qto_*", "NetWeight"),
           ("*BaseQuantities", "NetWeight"), ("Qto_*", "GrossWeight"), ("*", "Weight"), ("*", "Peso")],
}
DIM_SOURCES = {
    "length": QTY_SOURCES["m"],
    "width": [("LcRevitData_Element", "Width"), ("LcRevitData_Element", "Anchura"), ("LcRevitData_Type", "Width"),
              ("LcRevitData_Type", "Anchura"), ("Qto_*", "Width"), ("*BaseQuantities", "Width")],
    "height": [("LcRevitData_Element", "Unconnected Height"), ("LcRevitData_Element", "Altura desconectada"),
               ("LcRevitData_Element", "Height"), ("LcRevitData_Element", "Altura"),
               ("Qto_*", "Height"), ("*BaseQuantities", "Height")],
    "thickness": [("LcRevitData_Element", "Thickness"), ("LcRevitData_Element", "Grosor"),
                  ("LcRevitData_Type", "Default Thickness"), ("LcRevitData_Type", "Grosor por defecto"),
                  ("Qto_*", "Depth"), ("*BaseQuantities", "Depth"), ("Qto_*", "Width"), ("*BaseQuantities", "Width")],
}

CLASS_MAP = {                  # source category / class name (lower case) -> IFC class
    "walls": "IfcWall", "muros": "IfcWall", "floors": "IfcSlab", "suelos": "IfcSlab",
    "structural columns": "IfcColumn", "pilares estructurales": "IfcColumn", "columns": "IfcColumn", "pilares": "IfcColumn",
    "structural framing": "IfcBeam", "armazón estructural": "IfcBeam",
    "structural foundations": "IfcFooting", "cimentación estructural": "IfcFooting",
    "doors": "IfcDoor", "puertas": "IfcDoor", "windows": "IfcWindow", "ventanas": "IfcWindow",
    "roofs": "IfcRoof", "cubiertas": "IfcRoof", "ceilings": "IfcCovering", "techos": "IfcCovering",
    "stairs": "IfcStair", "escaleras": "IfcStair", "railings": "IfcRailing", "barandillas": "IfcRailing",
    "curtain panels": "IfcPlate", "paneles de muro cortina": "IfcPlate",
    "curtain wall mullions": "IfcMember", "montantes de muro cortina": "IfcMember",
    "pipes": "IfcPipeSegment", "tuberías": "IfcPipeSegment", "ducts": "IfcDuctSegment", "conductos": "IfcDuctSegment",
    "cable trays": "IfcCableCarrierSegment", "bandejas de cables": "IfcCableCarrierSegment",
    "plumbing fixtures": "IfcSanitaryTerminal", "aparatos sanitarios": "IfcSanitaryTerminal",
    "lighting fixtures": "IfcLightFixture", "luminarias": "IfcLightFixture",
    "furniture": "IfcFurnishingElement", "mobiliario": "IfcFurnishingElement",
    "generic models": "IfcBuildingElementProxy", "modelos genéricos": "IfcBuildingElementProxy",
}
EXCLUDE_CLASSES = {"IfcSpace", "IfcOpeningElement", "IfcVirtualElement", "IfcAnnotation", "IfcGrid", "IfcZone"}
EXCLUDE_CATEGORIES = {"rooms", "habitaciones", "spaces", "espacios", "areas", "áreas", "lines", "líneas",
                      "grids", "rejillas", "levels", "niveles", "<room separation>", "<separación de habitación>"}
SPATIAL_CLASSES = {"ifcproject", "ifcsite", "ifcbuilding", "ifcbuildingstorey", "ifcspatialzone"}

CLASS_LABELS = {               # partida summary / chapter summary per IFC class
    "IfcColumn": ("Pilar", "Pilares"), "IfcBeam": ("Viga", "Vigas"),
    "IfcMember": ("Barra", "Barras y montantes"), "IfcPlate": ("Chapa / panel", "Chapas y paneles"),
    "IfcSlab": ("Losa", "Losas y forjados"), "IfcWall": ("Muro", "Muros"),
    "IfcFooting": ("Cimentación", "Cimentaciones"), "IfcPile": ("Pilote", "Pilotes"),
    "IfcStair": ("Escalera", "Escaleras"), "IfcStairFlight": ("Tramo de escalera", "Escaleras"),
    "IfcRamp": ("Rampa", "Rampas"), "IfcRoof": ("Cubierta", "Cubiertas"), "IfcCovering": ("Revestimiento", "Revestimientos"),
    "IfcCurtainWall": ("Muro cortina", "Muros cortina"), "IfcRailing": ("Barandilla", "Barandillas"),
    "IfcDoor": ("Puerta", "Puertas"), "IfcWindow": ("Ventana", "Ventanas"),
    "IfcPipeSegment": ("Tubería", "Tuberías"), "IfcDuctSegment": ("Conducto", "Conductos"),
    "IfcCableCarrierSegment": ("Bandeja", "Bandejas"), "IfcSanitaryTerminal": ("Aparato sanitario", "Aparatos sanitarios"),
    "IfcLightFixture": ("Luminaria", "Luminarias"), "IfcFurnishingElement": ("Mobiliario", "Mobiliario"),
    "IfcBuildingElementProxy": ("Elemento", "Otros elementos"),
}
PARTIDA_SUMMARY = "{label} {type} {material} ({count} ud)"   # WriteMeasurementLinesFromJson CLEAN_SUMMARIES drops "(...)"

CH64 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_$"
IFC_ID_RE = re.compile(r"^[0-9A-Za-z_$]{22}$")
DISPLAY_RE = re.compile(r"^\s*(-?[\d.,]+)\s*([^\d\s].*)?$")
UNIT_FACTORS = {               # display-string suffix -> (factor to SI, kind)
    "mm": (0.001, "length"), "cm": (0.01, "length"), "m": (1.0, "length"), "km": (1000.0, "length"),
    "ft": (0.3048, "length"), "in": (0.0254, "length"),
    "mm²": (1e-6, "area"), "mm2": (1e-6, "area"), "cm²": (1e-4, "area"), "cm2": (1e-4, "area"),
    "m²": (1.0, "area"), "m2": (1.0, "area"), "sq m": (1.0, "area"), "ft²": (0.09290304, "area"),
    "ft2": (0.09290304, "area"), "sq ft": (0.09290304, "area"), "sf": (0.09290304, "area"),
    "mm³": (1e-9, "volume"), "mm3": (1e-9, "volume"), "cm³": (1e-6, "volume"), "cm3": (1e-6, "volume"),
    "m³": (1.0, "volume"), "m3": (1.0, "volume"), "cu m": (1.0, "volume"), "l": (0.001, "volume"),
    "ft³": (0.0283168466, "volume"), "ft3": (0.0283168466, "volume"), "cu ft": (0.0283168466, "volume"),
    "cf": (0.0283168466, "volume"), "kg": (1.0, "mass"), "t": (1000.0, "mass"), "lb": (0.45359237, "mass"),
}
UNIT_KIND = {"m3": "volume", "m2": "area", "m": "length", "kg": "mass"}


def r(v, n=DECIMALS):
    return None if v is None else round(v, n)


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


def normalize_guid(value):
    v = str(value or "").strip()
    if not v or v == "?":
        return None
    if IFC_ID_RE.match(v):
        return v
    h = v.replace("-", "").replace("{", "").replace("}", "")
    if len(h) == 32 and re.match(r"^[0-9a-fA-F]{32}$", h):
        if int(h, 16) == 0:
            return None
        return ifc_guid(h) if COMPRESS_UUIDS else v
    return v


def normalize_class(value):
    v = str(value or "").strip()
    if not v.lower().startswith("ifc"):
        return None
    for suffix in ("StandardCase", "ElementedCase", "STANDARDCASE", "ELEMENTEDCASE"):
        if v.endswith(suffix) and len(v) > len(suffix) + 3:
            v = v[:-len(suffix)]
    known = {k.lower(): k for k in list(CLASS_LABELS) + list(CLASS_MAP.values()) + list(EXCLUDE_CLASSES)}
    if v.lower() in known:
        return known[v.lower()]
    return "Ifc" + v[3:].capitalize() if v.isupper() else v


class PropertyReader:
    """Snapshots of a node's properties and ordered (category, property) lookups on them."""

    @staticmethod
    def Snapshot(node):
        rows = []
        try:
            for cat in node.PropertyCategories:
                cn = (cat.Name or "").lower()
                cd = (cat.DisplayName or "").lower()
                for prop in cat.Properties:
                    try:
                        pn = (prop.Name or "").lower()
                    except Exception:
                        pn = ""
                    rows.append((cn, cd, pn, (prop.DisplayName or "").lower(), prop.Value,
                                 cat.DisplayName or cat.Name or ""))
        except Exception:
            pass
        return rows

    @staticmethod
    def Matches(row, cat_pat, prop_name):
        cp, pp = cat_pat.lower(), prop_name.lower()
        if pp != row[2] and pp != row[3]:
            return False
        if row[0].startswith("lcoa"):          # Navisworks Item tab: "Elemento" in ES, never an element tab
            return glob_match(row[0], cp) or cp == "item"
        return glob_match(row[0], cp) or glob_match(row[1], cp)

    @staticmethod
    def Text(val):
        try:
            if val.IsDisplayString or val.IsIdentifierString:
                return val.ToDisplayString()
            if val.IsInt32:
                return str(val.ToInt32())
            if val.IsNamedConstant:
                return str(val.ToNamedConstant())
            if val.IsDouble or val.IsAnyDouble:
                return str(val.ToAnyDouble())
            return val.ToDisplayString()
        except Exception:
            return None

    @staticmethod
    def FindText(rows, pairs):
        """(value, "category > property") of the first non-empty hit, or (None, None)."""
        for cat_pat, prop_name in pairs:
            for row in rows:
                if PropertyReader.Matches(row, cat_pat, prop_name):
                    t = PropertyReader.Text(row[4])
                    if t is not None and str(t).strip() not in ("", "?"):
                        return str(t).strip(), f"{row[5]} > {prop_name}"
        return None, None

    @staticmethod
    def Number(val, s):
        """(value in SI, kind or None) from a VariantData; kind None = plain number (taken as SI)."""
        try:
            if val.IsDoubleVolume:
                return val.ToDoubleVolume() * s ** 3, "volume"
            if val.IsDoubleArea:
                return val.ToDoubleArea() * s ** 2, "area"
            if val.IsDoubleLength:
                return val.ToDoubleLength() * s, "length"
            if val.IsInt32:
                return float(val.ToInt32()), None
            if val.IsDouble or val.IsAnyDouble:
                return float(val.ToAnyDouble()), None
            if val.IsDisplayString or val.IsIdentifierString:
                return PropertyReader.ParseDisplay(val.ToDisplayString())
        except Exception:
            pass
        return None, None

    @staticmethod
    def ParseDisplay(text):
        m = DISPLAY_RE.match(str(text or ""))
        if not m:
            return None, None
        num = m.group(1)
        if "," in num and "." in num:
            num = num.replace(".", "").replace(",", ".") if num.rfind(",") > num.rfind(".") else num.replace(",", "")
        else:
            num = num.replace(",", ".")
        try:
            v = float(num)
        except ValueError:
            return None, None
        unit = (m.group(2) or "").strip().lower()
        if not unit:
            return v, None
        if unit not in UNIT_FACTORS:
            return None, None
        f, kind = UNIT_FACTORS[unit]
        return v * f, kind

    @staticmethod
    def FindNumber(rows, pairs, kind, s):
        """(value SI > 0, "category > property") of the first hit of the right kind, or (None, None)."""
        for cat_pat, prop_name in pairs:
            for row in rows:
                if PropertyReader.Matches(row, cat_pat, prop_name):
                    v, k = PropertyReader.Number(row[4], s)
                    if v is not None and v > 0 and (k is None or k == kind):
                        return v, f"{row[5]} > {prop_name}" + (" (plain number, SI assumed)" if k is None else "")
        return None, None


class ElementCollector:
    """Resolves geometry nodes to element nodes and reads identity, class, level, quantities."""

    def __init__(self, document, s):
        self.doc = document
        self.s = s
        self.identity = {}        # hash(node) -> bool
        self.snaps = {}           # hash(node) -> rows (element / storey nodes only)
        self.storey_elev = {}
        self.models = []
        self.root_model = {}      # hash(root) -> model info
        self.warnings = []
        self.excluded = 0
        self.fallback_nodes = 0
        self.skipped = []

    # --- scope ---------------------------------------------------------------
    def ModelsInScope(self):
        for i, m in enumerate(self.doc.Models):
            fname = str(m.FileName or "")
            try:
                src = str(m.SourceFileName or "")
            except Exception:
                src = ""
            info = {"index": i, "file": fname, "source_file": src, "units": str(m.Units),
                    "name": Path(fname).stem if fname else f"Model {i}", "elements": 0,
                    "included": not MODEL_FILTER or any(f.lower() in (fname + " " + src).lower() for f in MODEL_FILTER)}
            self.models.append(info)
            self.root_model[hash(m.RootItem)] = (info, m)
        if not any(mi["included"] for mi in self.models):
            raise Exception(f"No appended model matches MODEL_FILTER {MODEL_FILTER}.")

    def GeometryNodes(self):
        if SELECTION_ONLY:
            sel = list(self.doc.CurrentSelection.SelectedItems)
            if not sel:
                raise Exception("SELECTION_ONLY = True but nothing is selected.")
            for it in sel:
                if it.HasGeometry:
                    yield it
                for d in it.Descendants:
                    if d.HasGeometry:
                        yield d
        else:
            for mi in self.models:
                if not mi["included"]:
                    continue
                print(f"  model {mi['name']}...")
                for d in self.doc.Models[mi["index"]].RootItem.Descendants:
                    if d.HasGeometry:
                        yield d

    # --- element resolution ----------------------------------------------------
    def Rows(self, node):
        key = hash(node)
        if key not in self.snaps:
            self.snaps[key] = PropertyReader.Snapshot(node)
        return self.snaps[key]

    def HasIdentity(self, node):
        key = hash(node)
        if key in self.identity:
            return self.identity[key]
        rows = PropertyReader.Snapshot(node)
        found = any(row[0] == "lcrevitid" for row in rows) \
            or PropertyReader.FindText(rows, GUID_SOURCES[:-1])[0] is not None \
            or normalize_class(PropertyReader.FindText(rows, IFC_CLASS_SOURCES)[0]) is not None \
            or (node.ClassDisplayName or "").lower().startswith("ifc")
        self.identity[key] = found
        if found:
            self.snaps[key] = rows
        return found

    def ElementOf(self, geo):
        node = geo
        for _ in range(MAX_UP):
            if node is None or node.Parent is None:                    # file node: never an element
                break
            if (node.ClassDisplayName or "").lower() in SPATIAL_CLASSES:
                break
            if self.HasIdentity(node):
                return node, False
            node = node.Parent
        return geo, True

    def RootOf(self, node):
        while node.Parent is not None:
            node = node.Parent
        return self.root_model.get(hash(node), (None, None))

    # --- reading ---------------------------------------------------------------
    def Read(self):
        self.ModelsInScope()
        elements, seen, count = [], set(), 0
        print("Resolving elements...")
        for geo in self.GeometryNodes():
            count += 1
            if count % 5000 == 0:
                print(f"  {count} geometry nodes, {len(elements)} elements")
            node, fallback = self.ElementOf(geo)
            key = hash(node)
            if key in seen:
                continue
            seen.add(key)
            info, model = self.RootOf(node)
            if info is None or not info["included"]:
                continue
            e = self.ReadElement(node, fallback, info)
            if e is not None:
                info["elements"] += 1
                elements.append(e)
        print(f"  {count} geometry nodes -> {len(elements)} elements")
        return elements

    def ReadElement(self, node, fallback, info):
        rows = self.Rows(node)
        notes = []
        parent = node.Parent
        up_rows = rows
        if parent is not None and parent.Parent is not None \
                and (parent.ClassDisplayName or "").lower() not in SPATIAL_CLASSES:
            up_rows = rows + PropertyReader.Snapshot(parent)
        if fallback:
            self.fallback_nodes += 1
            notes.append("sin propiedades de identidad: elemento = nodo de geometría")

        # identity
        raw, gsrc = PropertyReader.FindText(rows, GUID_SOURCES[:-1])
        guid = normalize_guid(raw)
        if guid is None:
            guid = normalize_guid(str(node.InstanceGuid))
            gsrc = "Item > GUID (Navisworks InstanceGuid)"
            if guid is not None:
                notes.append("GUID de instancia de Navisworks (no es el IFC GlobalId del modelo de origen)")
        if guid is None:
            self.skipped.append({"name": node.DisplayName, "file": info["name"], "reason": "no GUID"})
            return None

        # class
        ifc_raw, csrc = PropertyReader.FindText(rows, IFC_CLASS_SOURCES)
        ifc_class = normalize_class(ifc_raw)
        category, _ = PropertyReader.FindText(up_rows, CATEGORY_SOURCES)
        if ifc_class is None:
            ifc_class = normalize_class(node.ClassDisplayName)
            csrc = "ClassDisplayName" if ifc_class else None
        if ifc_class is None and category and category.lower() in CLASS_MAP:
            ifc_class, csrc = CLASS_MAP[category.lower()], "CLASS_MAP(category)"
        if ifc_class is None and (node.ClassDisplayName or "").lower() in CLASS_MAP:
            ifc_class, csrc = CLASS_MAP[(node.ClassDisplayName or "").lower()], "CLASS_MAP(class)"
        if ifc_class is None:
            ifc_class, csrc = "IfcBuildingElementProxy", "default"
            notes.append(f"categoría '{category or node.ClassDisplayName}' sin clase IFC: IfcBuildingElementProxy")
        if ifc_class in EXCLUDE_CLASSES or (category or "").lower() in EXCLUDE_CATEGORIES:
            self.excluded += 1
            return None

        family, _ = PropertyReader.FindText(up_rows, FAMILY_SOURCES)
        type_, _ = PropertyReader.FindText(up_rows, TYPE_SOURCES)
        material, _ = PropertyReader.FindText(up_rows, MATERIAL_SOURCES)
        name = node.DisplayName or ""
        family = family or node.ClassDisplayName or ""
        type_ = type_ or name

        # bounding box (m)
        bbox = None
        try:
            bb = node.BoundingBox()
            bbox = ((bb.Min.X * self.s, bb.Min.Y * self.s, bb.Min.Z * self.s),
                    (bb.Max.X * self.s, bb.Max.Y * self.s, bb.Max.Z * self.s))
        except Exception:
            pass

        # storey / building / level
        storey = building = None
        for anc in node.Ancestors:
            cls = (anc.ClassDisplayName or "").lower()
            if cls == "ifcbuildingstorey" and storey is None:
                storey = anc
            elif cls == "ifcbuilding" and building is None:
                building = anc
        planta, cota = "", None
        if storey is not None:
            planta = storey.DisplayName or ""
            skey = hash(storey)
            if skey not in self.storey_elev:
                v, _ = PropertyReader.FindNumber(PropertyReader.Snapshot(storey), STOREY_ELEVATION_SOURCES, "length", self.s)
                self.storey_elev[skey] = v
            cota = self.storey_elev[skey]
        else:
            level, _ = PropertyReader.FindText(up_rows, LEVEL_SOURCES)
            if level:
                planta, cota = level, LEVEL_ELEVATIONS.get(level)
            elif LEVELS and bbox is not None:
                levels = sorted(float(z) for z in LEVELS)
                idx = 0
                for i, z in enumerate(levels):
                    if z <= bbox[0][2] + LEVEL_TOLERANCE:
                        idx = i
                planta = STOREY_NAME.format(index=idx, elevation=levels[idx])
                cota = levels[idx]
        area = (building.DisplayName if building is not None else "") or BUILDING or info["name"]
        archivo, _ = PropertyReader.FindText(rows, SOURCE_FILE_SOURCES)
        archivo = archivo or info["source_file"] or info["file"]

        # quantities
        q = {}
        for unit in UNIT_PRIORITY:
            q[unit] = PropertyReader.FindNumber(rows, QTY_SOURCES[unit], UNIT_KIND[unit], self.s)
        dims = {k: PropertyReader.FindNumber(up_rows, pairs, "length", self.s)[0] for k, pairs in DIM_SOURCES.items()}

        return {"node_name": name, "guid": guid, "guid_source": gsrc, "ifc_class": ifc_class,
                "class_source": csrc, "category": category or "", "family": family, "type": type_,
                "material": material or "", "level": planta, "planta": planta,
                "cota": None if cota is None else round(cota, 3), "area": area, "file": archivo,
                "model": info["name"], "bbox": bbox, "q": q, "dims": dims, "notes": notes}


class LineBuilder:
    """One measurement line per element: unit, dimension columns, quantity."""

    @staticmethod
    def Fits(L, A, H, q):
        prod = (L if L is not None else 1) * (A if A is not None else 1) * (H if H is not None else 1)
        return abs(prod - q) <= DIM_TOLERANCE * max(q, 1e-6) + 0.5 * 10 ** -DECIMALS

    @staticmethod
    def Build(e, mismatches, bbox_used):
        order = []
        if UNIT_BY_CLASS.get(e["ifc_class"]):
            order.append(UNIT_BY_CLASS[e["ifc_class"]])
        order += [u for u in UNIT_PRIORITY if u not in order]
        unit = value = qsrc = None
        notes = list(e["notes"])
        for u in order:
            if u == "u":
                unit, value, qsrc = "u", 1.0, "count"
                break
            v, src = e["q"].get(u, (None, None))
            if v is not None:
                unit, value, qsrc = u, v, src
                break
        d = e["dims"]
        L = A = H = None
        comment_dims = ""
        if unit is None and BBOX_FALLBACK and e["bbox"] is not None:
            (x0, y0, z0), (x1, y1, z1) = e["bbox"]
            dx, dy, dz = x1 - x0, y1 - y0, z1 - z0
            if dx > 0 and dy > 0 and dz > 0:
                unit, qsrc = "m3", "bounding box"
                L, A, H = r(max(dx, dy)), r(min(dx, dy)), r(dz)
                value = L * A * H
                notes.append("caja envolvente (BBOX_FALLBACK): no es la medición real")
                bbox_used.append(e["guid"])
        if unit is None:
            if NO_QUANTITY != "count":
                return None
            unit, value, qsrc = "u", 1.0, "count (sin cantidad en el modelo)"
            notes.append("sin cantidad en el modelo: 1 ud")

        if qsrc == "bounding box":
            pass
        elif unit == "m3":
            dl, dw, dh, dt = d["length"], d["width"], d["height"], d["thickness"]
            area = e["q"].get("m2", (None, None))[0]
            if dl and dw and dh and LineBuilder.Fits(r(dl), r(dw), r(dh), value):
                L, A, H = r(dl), r(dw), r(dh)
            elif area and dt and LineBuilder.Fits(r(area), None, r(dt), value):
                L, H = r(area), r(dt)
                comment_dims = " - Longitud = superficie m2 x Altura = espesor"
            else:
                if dl and dw and dh:
                    mismatches.append({"guid": e["guid"], "name": e["node_name"], "dims_m3": round(dl * dw * dh, 4),
                                       "volume_m3": round(value, 4)})
                L = r(value)
                notes.append("Longitud = volumen del modelo m3")
        elif unit == "m2":
            dl, dh = d["length"], d["height"]
            if dl and dh and LineBuilder.Fits(r(dl), None, r(dh), value):
                L, H = r(dl), r(dh)
            else:
                L = r(value)
                notes.append("Longitud = superficie del modelo m2")
        elif unit == "m":
            L = r(value)
        elif unit == "kg":
            dl = d["length"]
            if dl:
                L = r(dl)
                A = r(value / L) if L else None
                comment_dims = " - Longitud m x Anchura kg/m"
            else:
                L = r(value)
                notes.append("Longitud = peso del modelo kg")
        qty = 1.0 if unit == "u" else round((L or 0) * (A if A is not None else 1) * (H if H is not None else 1), DECIMALS)
        vol = e["q"].get("m3", (None, None))[0]
        sup = e["q"].get("m2", (None, None))[0]
        lng = e["q"].get("m", (None, None))[0] or d["length"]
        line = {
            "Comentario": f"{e['node_name'] or e['type']} - {e['planta'] or e['model']}{comment_dims}".strip(),
            "N": 1, "Longitud": L, "Anchura": A, "Altura": H,
            "GuidElem": e["guid"], "CategoríaBIM": e["ifc_class"],
            "TipoBIM": f"{e['type']} {e['material']}".strip(), "FamiliaBIM": e["family"],
            "Planta": e["planta"], "Cota": e["cota"], "Área": e["area"], "Archivo": e["file"],
            "BIMLong": r(lng), "BIMSup": r(sup, 4), "BIMVol": r(vol, 4),
            "Nota": "; ".join(notes),
            "_quantity": qty, "_model_quantity": value,
        }
        return unit, qsrc, line


class TakeoffExporter:
    @staticmethod
    def Run(document):
        if document is None or document.Models.Count == 0:
            raise Exception("No model loaded in Navisworks.")
        s = UnitConversion.ScaleFactor(document.Models.First.Units, Units.Meters)   # metres per document unit
        model_name = Path(str(document.FileName)).stem if document.FileName else \
            Path(str(document.Models.First.FileName)).stem
        print(f"Reading {document.Models.Count} appended models of {model_name} (1 unit = {s} m)...")

        collector = ElementCollector(document, s)
        elements = collector.Read()
        if not elements:
            raise Exception("No elements to export" + (" in the selection." if SELECTION_ONLY else "."))

        # --- lines and groups -----------------------------------------------------
        groups, no_qty, mismatches, bbox_used, duplicates = {}, [], [], [], []
        guid_count, guid_sources, qty_sources, class_sources = {}, {}, {}, {}
        for e in elements:
            built = LineBuilder.Build(e, mismatches, bbox_used)
            if built is None:
                no_qty.append({"guid": e["guid"], "name": e["node_name"], "ifc_class": e["ifc_class"],
                               "category": e["category"], "file": e["model"]})
                continue
            unit, qsrc, line = built
            n = guid_count.get(e["guid"], 0) + 1
            guid_count[e["guid"]] = n
            if n > 1:
                duplicates.append({"guid": e["guid"], "name": e["node_name"], "file": e["model"], "copy": n})
                if DUPLICATE_GUIDS == "skip":
                    continue
                line["GuidElem"] = f"{e['guid']}-{n}"
                line["Nota"] = "; ".join(x for x in (line["Nota"], f"GUID repetido en el modelo (copia {n})") if x)
            guid_sources[e["guid_source"]] = guid_sources.get(e["guid_source"], 0) + 1
            qty_sources[f"{unit} {qsrc}"] = qty_sources.get(f"{unit} {qsrc}", 0) + 1
            class_sources[e["class_source"]] = class_sources.get(e["class_source"], 0) + 1
            key = tuple(e[k] for k in GROUP_BY) + (unit,)        # the unit always splits a group
            g = groups.setdefault(key, {"unit": unit, "lines": [], "sample": e})
            x0 = e["bbox"][0][0] if e["bbox"] else 0.0
            g["lines"].append((e["cota"] if e["cota"] is not None else -1e9, x0, line))

        # --- chapters and partidas --------------------------------------------------
        chapters = {}
        for key, g in groups.items():
            ckey = g["sample"][CHAPTER_BY] if CHAPTER_BY else ""
            chapters.setdefault(ckey, []).append((key, g))

        out_chapters, partida_rows = [], []
        for ci, ckey in enumerate(sorted(chapters), start=1):
            ccode = "%02d" % ci
            if not CHAPTER_BY:
                csummary = SINGLE_CHAPTER_SUMMARY
            elif CHAPTER_BY == "ifc_class":
                csummary = CLASS_LABELS.get(ckey, (ckey, ckey))[1]
            else:
                csummary = str(ckey) or "(sin valor)"
            partidas = []
            for pi, (key, g) in enumerate(sorted(chapters[ckey], key=lambda kg: tuple(str(x) for x in kg[0])), start=1):
                smp = g["sample"]
                lines = [l for _, _, l in sorted(g["lines"], key=lambda t: (t[0], t[1]))]
                label = CLASS_LABELS.get(smp["ifc_class"], (smp["ifc_class"], smp["ifc_class"]))[0]
                summary = PARTIDA_SUMMARY.format(label=label, type=smp["type"], material=smp["material"],
                                                 family=smp["family"], category=smp["category"],
                                                 ifc_class=smp["ifc_class"], count=len(lines))
                summary = re.sub(r"\s+", " ", summary).strip()
                quantity = round(sum(l["_quantity"] for l in lines), DECIMALS)
                model_qty = sum(l["_model_quantity"] for l in lines)
                pcode = "%s.%02d" % (ccode, pi)
                partidas.append({"code": pcode, "summary": summary, "unit": g["unit"], "quantity": quantity,
                                 "quantity_model": round(model_qty, 4),
                                 "group": dict(zip(list(GROUP_BY) + ["unit"], key)), "lines": lines})
                partida_rows.append({"type": "PrestoPartida", "code": pcode, "summary": summary, "unit": g["unit"],
                                     "elements": len(lines), "quantity": quantity, "quantity_model": round(model_qty, 4)})
            out_chapters.append({"code": ccode, "summary": csummary, "partidas": partidas})

        # --- source block -------------------------------------------------------------
        warnings = []
        inst = guid_sources.get("Item > GUID (Navisworks InstanceGuid)", 0)
        if inst:
            warnings.append(f"{inst} elements use the Navisworks InstanceGuid (no IFC GlobalId in the source model)")
        if collector.fallback_nodes:
            warnings.append(f"{collector.fallback_nodes} elements are geometry nodes (no element identity found up the tree)")
        if bbox_used:
            warnings.append(f"{len(bbox_used)} elements measured from their bounding box (BBOX_FALLBACK)")
        if no_qty:
            warnings.append(f"{len(no_qty)} elements without quantity were skipped (NO_QUANTITY = '{NO_QUANTITY}')")
        if duplicates:
            warnings.append(f"{len(duplicates)} repeated GUIDs ({DUPLICATE_GUIDS})")
        no_level = sum(1 for g in groups.values() for _, _, l in g["lines"] if not l["Planta"])
        if no_level:
            warnings.append(f"{no_level} lines without Planta (set LEVELS)")
        plain = sum(v for k, v in qty_sources.items() if "plain number" in k)
        if plain:
            warnings.append(f"{plain} quantities are plain numbers taken as SI (m, m2, m3, kg): check their units")

        n_lines = sum(row["elements"] for row in partida_rows)
        source = {
            "application": "Autodesk Navisworks", "file": str(document.FileName or ""), "model": model_name,
            "date": datetime.now().isoformat(timespec="seconds"), "selection_only": SELECTION_ONLY,
            "model_filter": list(MODEL_FILTER), "document_unit_to_m": s,
            "models": [{k: mi[k] for k in ("file", "source_file", "units", "elements", "included")}
                       for mi in collector.models],
            "elements_read": len(elements), "elements_in_lines": n_lines, "elements_excluded": collector.excluded,
            "group_by": list(GROUP_BY), "chapter_by": CHAPTER_BY, "decimals": DECIMALS,
            "unit_priority": list(UNIT_PRIORITY), "levels_m": list(LEVELS),
            "guid_sources": guid_sources, "class_sources": class_sources, "quantity_sources": qty_sources,
            "items_without_quantity": no_qty, "skipped_elements": collector.skipped,
            "duplicate_guids": duplicates, "dimension_mismatches": mismatches, "warnings": warnings,
        }
        for ch in out_chapters:
            for p in ch["partidas"]:
                for l in p["lines"]:
                    l.pop("_quantity", None)
                    l.pop("_model_quantity", None)
        data = {"root_summary": ROOT_SUMMARY or f"{model_name} - takeoff", "source": source, "chapters": out_chapters}

        out = Path(JSON_PATH) if JSON_PATH else \
            Path(Environment.GetFolderPath(Environment.SpecialFolder.Desktop)) / f"{model_name} - Presto takeoff.json"
        with open(str(out), "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False, indent=1)

        # --- summary ----------------------------------------------------------------------
        print(f"{len(elements)} elements read, {n_lines} in {len(partida_rows)} partidas "
              f"({len(out_chapters)} chapters), {collector.excluded} excluded.")
        for mi in collector.models:
            print(f"  model {mi['name']}: {mi['elements']} elements" + ("" if mi["included"] else " (filtered out)"))
        for row in partida_rows:
            print(f"  {row['code']}  {row['quantity']:>12,.3f} {row['unit']:<3} {row['elements']:>5} el.  {row['summary']}")
        for k, v in sorted(guid_sources.items(), key=lambda kv: -kv[1]):
            print(f"  GUID from {k}: {v}")
        for k, v in sorted(qty_sources.items(), key=lambda kv: -kv[1]):
            print(f"  quantity {k}: {v}")
        if no_qty:
            print(f"  WITHOUT QUANTITY {len(no_qty)} elements - first: {no_qty[0]}")
        if collector.skipped:
            print(f"  SKIPPED {len(collector.skipped)} elements - first: {collector.skipped[0]}")
        if mismatches:
            print(f"  {len(mismatches)} elements where L x W x H != volume: quantity written in Longitud")
        for w in warnings:
            print(f"  WARNING: {w}")
        print(f"Saved {out}")

        return {"type": "NavisworksPrestoTakeoff", "file": str(out), "elements": len(elements),
                "elements_in_lines": n_lines, "without_quantity": len(no_qty), "skipped": len(collector.skipped),
                "duplicate_guids": len(duplicates), "dimension_mismatches": len(mismatches),
                "guid_sources": guid_sources, "warnings": warnings, "partidas": partida_rows}


# Entry point
ia_Result = TakeoffExporter.Run(doc)
