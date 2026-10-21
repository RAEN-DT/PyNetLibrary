# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import json
import uuid
from datetime import datetime
from pathlib import Path

import clr

clr.AddReference("AcMgd")
clr.AddReference("AcCoreMgd")
clr.AddReference("AcDbMgd")

from System import Environment
from Autodesk.AutoCAD.ApplicationServices import Application as AcadApp
from Autodesk.AutoCAD.DatabaseServices import OpenMode, BlockTableRecord, Curve, Hatch, BlockReference

# Civil 3D is optional: in plain AutoCAD only the layer source runs.
try:
    clr.AddReference("AecBaseMgd")
    clr.AddReference("AeccDbMgd")
    from Autodesk.Civil.ApplicationServices import CivilApplication
    from Autodesk.Civil.DatabaseServices import TinVolumeSurface
    civil_doc = CivilApplication.ActiveDocument
except Exception:
    civil_doc = None

doc = AcadApp.DocumentManager.MdiActiveDocument
db = doc.Database

# ---------------------------------------------------------------------------
# Quantity takeoff for RIB Presto from a Civil 3D (or AutoCAD) drawing with
# ISO 19650 traceability: ONE MEASUREMENT LINE PER MEASURED OBJECT (or per
# corridor station interval), each with a stable unique GuidElem. Read-only
# on the drawing.
#
# Output: one JSON on the Desktop, "<drawing> - Presto takeoff.json", in the
# format of 01_Scripts/06_Presto/02_Write/CreateBudgetFromJson.py (chapters >
# partidas with unit and quantity) plus, per partida, its "lines" for
# 01_Scripts/06_Presto/02_Write/WriteMeasurementLinesFromJson.py, and a
# "source" block (drawing, date, units, id scheme, warnings). Same JSON as
# 01_Scripts/05_Tekla/06_Export/ExportTakeoffForPresto.py. Workflow:
#   1. this script (Civil 3D)  2. CreateBudgetFromJson.py (Presto, the tree)
#   3. WriteMeasurementLinesFromJson.py (Presto, the lines)
#   4. 01_Read/ReadMeasurementLines.py (Presto, the traceability check)
#
# Sources (one chapter each, switchable below):
# - CORRIDORS: per corridor shape code (Pave, Base, SubBase...) in m3 by the
#   AVERAGE END AREA method: shape areas (AppliedAssembly.GetShapesByCode)
#   at every assembly insertion station of each baseline region, volume =
#   (A0 + A1) / 2 x (station1 - station0). Lines per station interval
#   (Longitud = interval, Anchura = mean area m2) or per region. No curve
#   correction (stations are measured on the baseline). Corridor material
#   lists (QTO / Compute Materials) are NOT used: they need sample lines and
#   a write operation, and no API path is verified in this library.
# - VOLUME SURFACES (TinVolumeSurface): cut and fill (m3) as two partidas,
#   one line per volume surface (GetVolumeProperties, adjusted or not).
# - PIPE NETWORKS: pipes by part size + material in m (PIPE_LENGTH), and
#   structures by part family + size in u.
# - LAYERS (fallback, plain AutoCAD entities in Model space): LAYER_MAP
#   layer -> partida; "m" = curve length, "m2" = area of closed curves /
#   hatches, "u" = count (block references and any other entity).
# - ALIGNMENTS (off by default): length per alignment in m.
#
# Identity: Civil 3D / AutoCAD objects have NO IFC GlobalId (only after an
# IFC export, and that id is not readable back here). GuidElem is built as
#   IFC-compressed (22 chars) uuid5(NAMESPACE, drawing_key|handle[|aux])
# drawing_key = Database.FingerprintGuid (kept across saves / Save As),
# falling back to the drawing path; handle = the object's DWG Handle (stable
# for the life of the drawing); aux = GuidAux-like suffix that tells apart
# several lines of one object (corridor region / code / station range,
# cut / fill). Re-running on the same drawing gives the same ids.
#
# Units: Civil 3D drawing units (Drawing Settings > Units and Zone), else
# INSUNITS; converted to metres (DRAWING_UNIT overrides). Written in "source".
# Line quantities are rounded to DECIMALS, like Presto does with
# Obra.DecCantMed = DECIMALS, so "quantity" (sum of the rounded lines) is
# what Presto will show; "quantity_model" is the unrounded model total.
#
# Verified elsewhere in this library (✅): the AutoCAD/Civil boilerplate,
# CorridorCollection / Baselines / BaselineRegions (13_Corridors/
# ListCorridors.py), Baseline.GetAppliedAssemblyAtStation (docs/
# civil-sections.md), GetSurfaceIds + type() (12_Surfaces/SurfaceStats.py),
# GetPipeNetworkIds / GetPipeIds / GetStructureIds / Length3DToInsideEdge /
# InnerDiameterOrWidth (15_Pipe_Networks/ListPipeNetworks.py), Alignment.
# Length (10_Alignments/ListAlignments.py), Model space walk (03_Entities/
# ListModelSpaceEntities.py), Handle.ToString() (03_Entities/
# ReadPropertySets.py), entity.Layer, doc.LockDocument().
# ⏳ The script as a whole has NOT been run (written 2026-10-20 without a
# Civil 3D session). ⏳ from the stubs only: Corridor.GetShapeCodes,
# BaselineRegion.SortedStations / RegionGUID, AppliedAssembly.
# GetShapesByCode + CalculatedShape.Area, TinVolumeSurface.
# GetVolumeProperties, the other Pipe lengths, PartSizeName / Material /
# PartFamilyName, Structure.RimElevation, Curve.GetDistanceAtParameter,
# Curve/Hatch.Area, Database.FingerprintGuid / Insunits, Civil
# Settings.DrawingSettings.UnitZoneSettings.DrawingUnits.
# Corridor objects are opened ForWrite (CORRIDOR_FOR_WRITE) because their
# shape collections are live wrappers - a ForRead object hit by a writing
# "Get" call aborts the host (docs/autocad-civil.md, hard crash #2). The
# transaction is never committed, so nothing is changed.
# ---------------------------------------------------------------------------
JSON_PATH = None               # None -> Desktop / "<drawing> - Presto takeoff.json"
ROOT_SUMMARY = ""              # "" -> "<drawing> - takeoff"
AREA = ""                      # Área for every line; "" -> PROJECTNAME or the drawing name
DECIMALS = 3                   # Presto Obra.DecCantMed / Conceptos.RedParc
DRAWING_UNIT = None            # None -> Civil 3D drawing units / INSUNITS; or "Meters", "Feet", "Millimeters"...
COTA_DEFAULT = 0.0             # Cota when the object has no meaningful elevation

CORRIDORS = True
CORRIDOR_SHAPE_CODES = []      # [] -> every code of Corridor.GetShapeCodes(); or e.g. ["Pave1", "Base", "SubBase"]
CORRIDOR_LINES = "interval"    # "interval" -> one line per station interval; "region" -> one per baseline region
CORRIDOR_SPLIT_BY_CORRIDOR = False   # True -> one partida per corridor and code
CORRIDOR_FOR_WRITE = True      # open corridors ForWrite (never committed) - see the header
VOLUME_SURFACES = True
USE_ADJUSTED_VOLUMES = True    # True -> AdjustedCut/FillVolume (cut / fill factors applied)
PIPE_NETWORKS = True
PIPE_LENGTH = "3d_inside"      # "3d_inside", "3d_center", "2d_inside", "2d_center"
LAYERS = True
LAYER_MAP = {                  # layer (case-insensitive) -> (partida summary, unit "m" | "m2" | "u", IFC class)
    # "C-BORDILLO": ("Bordillo prefabricado", "m", "IfcKerb"),
    # "C-ACERA": ("Pavimento de acera", "m2", "IfcCourse"),
    # "C-FAROLAS": ("Báculo de alumbrado", "u", "IfcBuildingElementProxy"),
}
ALIGNMENTS = False

CHAPTERS = {                   # source -> (code, summary)
    "corridor": ("01", "Firmes y pavimentos (corredores)"),
    "earthworks": ("02", "Movimiento de tierras"),
    "pipes": ("03", "Redes de tuberías"),
    "structures": ("04", "Pozos y arquetas"),
    "alignments": ("05", "Ejes"),
    "layers": ("06", "Elementos por capa"),
}
SHAPE_LABELS = {               # corridor shape code -> (partida label, IFC class)
    "Pave": ("Capa de rodadura", "IfcCourse"), "Pave1": ("Capa de rodadura", "IfcCourse"),
    "Pave2": ("Capa intermedia", "IfcCourse"), "Base": ("Capa de base", "IfcCourse"),
    "SubBase": ("Capa de subbase", "IfcCourse"), "Curb": ("Bordillo", "IfcKerb"),
    "Sidewalk": ("Acera", "IfcCourse"), "Median": ("Mediana", "IfcBuildingElementProxy"),
}
IFC_CLASSES = {                # CategoríaBIM per source (IFC 4.3)
    "cut": "IfcEarthworksCut", "fill": "IfcEarthworksFill", "pipe": "IfcPipeSegment",
    "structure": "IfcDistributionChamberElement", "alignment": "IfcAlignment",
    "default": "IfcBuildingElementProxy",
}
PARTIDA_SUMMARY = "{label} ({count} ud)"   # WriteMeasurementLinesFromJson CLEAN_SUMMARIES drops "(...)"

CH64 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_$"
NAMESPACE = uuid.uuid5(uuid.NAMESPACE_URL, "pynet:civil3d-takeoff")
UNIT_TO_M = {"Meters": 1.0, "Millimeters": 0.001, "Centimeters": 0.01, "Decimeters": 0.1,
             "Kilometers": 1000.0, "Feet": 0.3048, "Inches": 0.0254, "Yards": 0.9144,
             "USSurveyFeet": 1200.0 / 3937.0}


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


def elem_guid(handle, *aux):
    key = "|".join([drawing_key, str(handle)] + [str(a) for a in aux])
    return ifc_guid(uuid.uuid5(NAMESPACE, key)), key


def r(v, n=DECIMALS):
    return None if v is None else round(v, n)


def pk(station_m):
    st = round(station_m, 2)
    km = int(st // 1000)
    return "%d+%06.2f" % (km, st - km * 1000)


def new_line(comment, guid, cls, tipo, familia, planta, cota, L=None, A=None, H=None, N=1,
             bim_long=None, bim_sup=None, bim_vol=None, nota="", model_qty=0.0, key=""):
    qty = round(N * (L if L is not None else 1) * (A if A is not None else 1) * (H if H is not None else 1), DECIMALS)
    return {"Comentario": comment, "N": N, "Longitud": L, "Anchura": A, "Altura": H,
            "GuidElem": guid, "CategoríaBIM": cls, "TipoBIM": tipo, "FamiliaBIM": familia,
            "Planta": planta or "—", "Cota": cota, "Área": area_name, "Archivo": drawing_file,
            "BIMLong": bim_long, "BIMSup": bim_sup, "BIMVol": bim_vol, "Nota": nota,
            "_quantity": qty, "_model_quantity": model_qty, "_key": key}


def add(source, gkey, label, unit, line, sort):
    g = groups.setdefault((source, gkey), {"label": label, "unit": unit, "lines": []})
    g["lines"].append((sort, line))


# --- drawing, units -------------------------------------------------------------------
drawing_file = str(doc.Name)
drawing_name = Path(drawing_file).stem
warnings = []
fingerprint = str(db.FingerprintGuid or "").strip()
drawing_key = fingerprint or drawing_file
if not fingerprint:
    warnings.append("no FingerprintGuid: GuidElem built from the drawing path (changes if the file is moved)")
area_name = AREA or str(db.ProjectName or "").strip() or drawing_name

insunits = str(db.Insunits)
civil_units = None
if civil_doc is not None:
    try:
        uz = civil_doc.Settings.DrawingSettings.UnitZoneSettings
        civil_units = str(uz.DrawingUnits)
        if civil_units == "Feet" and "Survey" in str(uz.ImperialToMetricConversion):
            civil_units = "USSurveyFeet"
    except Exception as ex:
        warnings.append(f"Civil 3D drawing units not readable: {ex}")
unit_name = DRAWING_UNIT or civil_units or insunits
if unit_name not in UNIT_TO_M:
    warnings.append(f"drawing unit '{unit_name}' unknown (INSUNITS {insunits}): metres assumed - set DRAWING_UNIT")
    unit_name = "Meters"
k = UNIT_TO_M[unit_name]
if civil_units and insunits not in (civil_units, "Undefined") and not DRAWING_UNIT:
    warnings.append(f"Civil 3D units {civil_units} != INSUNITS {insunits}: Civil 3D units used for everything")

groups = {}
counts = {"corridor_intervals": 0, "volume_surfaces": 0, "pipes": 0, "structures": 0, "alignments": 0, "entities": 0}
skipped = []
print(f"Reading {drawing_name} (units {unit_name}, x{k} -> m)...")

# --- read everything inside one transaction (never committed) -------------------------
with doc.LockDocument():
    t = db.TransactionManager.StartTransaction()
    try:
        # --- corridors: average end area per shape code ---------------------------------
        if CORRIDORS and civil_doc is not None:
            for cid in civil_doc.CorridorCollection:
                c = None
                if CORRIDOR_FOR_WRITE:
                    try:
                        c = t.GetObject(cid, OpenMode.ForWrite, False, True)   # forceOpenOnLockedLayer
                    except Exception as ex:
                        warnings.append(f"corridor {cid} not openable ForWrite ({ex}): read ForRead")
                if c is None:
                    c = t.GetObject(cid, OpenMode.ForRead)
                c_handle = c.Handle.ToString()
                codes = list(CORRIDOR_SHAPE_CODES) or [str(x) for x in c.GetShapeCodes()]
                for b in c.Baselines:
                    try:
                        planta = t.GetObject(b.AlignmentId, OpenMode.ForRead).Name
                    except Exception:
                        planta = "—"
                    area_cache = {}

                    def shape_areas(st):
                        if st not in area_cache:
                            aa = b.GetAppliedAssemblyAtStation(st)
                            areas = {}
                            for code in codes:
                                a = 0.0
                                try:
                                    for sh in aa.GetShapesByCode(code):
                                        a += sh.Area
                                except Exception:
                                    pass
                                areas[code] = a * k * k
                            area_cache[st] = areas
                        return area_cache[st]

                    for reg in b.BaselineRegions:
                        reg_id = str(reg.RegionGUID)
                        stations = sorted(set(float(s) for s in reg.SortedStations()))
                        if len(stations) < 2:
                            skipped.append({"object": f"{c.Name}/{b.Name}/{reg.Name}", "reason": "fewer than 2 stations"})
                            continue
                        per_code = {code: [] for code in codes}
                        for s0, s1 in zip(stations[:-1], stations[1:]):
                            try:
                                a0, a1 = shape_areas(s0), shape_areas(s1)
                            except Exception as ex:
                                skipped.append({"object": f"{c.Name}/{b.Name}/{reg.Name} {s0:.2f}-{s1:.2f}",
                                                "reason": f"applied assembly not readable: {ex}"})
                                continue
                            for code in codes:
                                if a0[code] > 0 or a1[code] > 0:
                                    per_code[code].append((s0 * k, s1 * k, a0[code], a1[code]))
                        for code, ivs in per_code.items():
                            if not ivs:
                                continue
                            label, cls = SHAPE_LABELS.get(code, (code, IFC_CLASSES["default"]))
                            gkey = (c.Name, code) if CORRIDOR_SPLIT_BY_CORRIDOR else (code,)
                            glabel = f"{label} - {c.Name}" if CORRIDOR_SPLIT_BY_CORRIDOR else label
                            head = f"{c.Name} / {b.Name} / {reg.Name} - {code}"
                            if CORRIDOR_LINES == "region":
                                ivs = [(ivs[0][0], ivs[-1][1], None, None, sum((x1 - x0) * (p + q) / 2.0 for x0, x1, p, q in ivs))]
                            for iv in ivs:
                                x0, x1 = iv[0], iv[1]
                                length = x1 - x0
                                if CORRIDOR_LINES == "region":
                                    volume = iv[4]
                                    nota = "Anchura = área media equivalente m2 (volumen por áreas medias / longitud)"
                                else:
                                    volume = (iv[2] + iv[3]) / 2.0 * length
                                    nota = "Anchura = área media m2 (A0 %.3f, A1 %.3f)" % (iv[2], iv[3])
                                mean = volume / length if length > 0 else 0.0
                                guid, key = elem_guid(c_handle, reg_id, code, "%.3f-%.3f" % (x0, x1))
                                line = new_line(f"{head} - PK {pk(x0)} – {pk(x1)}", guid, cls, code, c.Name, planta,
                                                COTA_DEFAULT, L=r(length), A=r(mean), bim_long=r(length),
                                                bim_sup=r(mean), bim_vol=r(volume, 4), nota=nota,
                                                model_qty=volume, key=key)
                                add("corridor", gkey, glabel, "m3", line, (planta, x0))
                                counts["corridor_intervals"] += 1

        # --- volume surfaces: cut and fill ----------------------------------------------
        if VOLUME_SURFACES and civil_doc is not None:
            for sid in civil_doc.GetSurfaceIds():
                s = t.GetObject(sid, OpenMode.ForRead)
                if not isinstance(s, TinVolumeSurface):
                    continue
                vp = s.GetVolumeProperties()
                cut = (vp.AdjustedCutVolume if USE_ADJUSTED_VOLUMES else vp.UnadjustedCutVolume) * k ** 3
                fill = (vp.AdjustedFillVolume if USE_ADJUSTED_VOLUMES else vp.UnadjustedFillVolume) * k ** 3
                try:
                    base = t.GetObject(vp.BaseSurface, OpenMode.ForRead).Name
                    comp = t.GetObject(vp.ComparisonSurface, OpenMode.ForRead).Name
                except Exception:
                    base, comp = "?", "?"
                if s.IsOutOfDate:
                    warnings.append(f"volume surface {s.Name} is out of date: rebuild it before trusting its volumes")
                handle = s.Handle.ToString()
                factors = f"factores desmonte {vp.CutFactor:g} / terraplén {vp.FillFactor:g}" if USE_ADJUSTED_VOLUMES else "sin factores"
                for kind, label, vol in (("cut", "Desmonte", cut), ("fill", "Terraplén", fill)):
                    guid, key = elem_guid(handle, kind)
                    line = new_line(f"{s.Name} ({base} -> {comp}) - {label.lower()}", guid, IFC_CLASSES[kind],
                                    str(s.StyleName or ""), "TinVolumeSurface", "—", COTA_DEFAULT,
                                    L=r(vol), bim_vol=r(vol, 4),
                                    nota=f"Longitud = volumen m3 de la superficie de volumen ({factors})",
                                    model_qty=vol, key=key)
                    add("earthworks", (kind,), label, "m3", line, (s.Name,))
                counts["volume_surfaces"] += 1

        # --- pipe networks --------------------------------------------------------------
        if PIPE_NETWORKS and civil_doc is not None:
            for nid in civil_doc.GetPipeNetworkIds():
                n = t.GetObject(nid, OpenMode.ForRead)
                for pid in n.GetPipeIds():
                    p = t.GetObject(pid, OpenMode.ForRead)
                    if PIPE_LENGTH == "3d_center":
                        length = p.Length3DCenterToCenter
                    elif PIPE_LENGTH == "2d_inside":
                        length = p.Length2DToInsideEdge
                    elif PIPE_LENGTH == "2d_center":
                        length = p.Length2DCenterToCenter
                    else:
                        length = p.Length3DToInsideEdge
                    length *= k
                    size, material = str(p.PartSizeName or ""), str(p.Material or "")
                    guid, key = elem_guid(p.Handle.ToString())
                    line = new_line(f"{n.Name} / {p.Name} - {size}", guid, IFC_CLASSES["pipe"], size,
                                    str(p.PartFamilyName or ""), str(p.RefAlignmentName or ""),
                                    r(p.StartPoint.Z * k), L=r(length), bim_long=r(length),
                                    nota="Longitud = %s m; diámetro interior %.3f m" % (PIPE_LENGTH, p.InnerDiameterOrWidth * k),
                                    model_qty=length, key=key)
                    add("pipes", (size, material), f"Tubería {size} {material}".strip(), "m", line,
                        (n.Name, p.Name))
                    counts["pipes"] += 1
                for sid in n.GetStructureIds():
                    s = t.GetObject(sid, OpenMode.ForRead)
                    family, size = str(s.PartFamilyName or ""), str(s.PartSizeName or "")
                    guid, key = elem_guid(s.Handle.ToString())
                    line = new_line(f"{n.Name} / {s.Name} - {size}", guid, IFC_CLASSES["structure"], size, family,
                                    str(s.RefAlignmentName or ""), r(s.RimElevation * k), N=1,
                                    nota="Cota = rasante (rim) m; altura %.2f m" % (s.RimToSumpHeight * k),
                                    model_qty=1.0, key=key)
                    add("structures", (family, size), f"{family} {size}".strip(), "u", line, (n.Name, s.Name))
                    counts["structures"] += 1

        # --- alignments -----------------------------------------------------------------
        if ALIGNMENTS and civil_doc is not None:
            for aid in civil_doc.GetAlignmentIds():
                a = t.GetObject(aid, OpenMode.ForRead)
                length = a.Length * k
                guid, key = elem_guid(a.Handle.ToString())
                line = new_line(a.Name, guid, IFC_CLASSES["alignment"], str(a.StyleName or ""), "Alignment", a.Name,
                                COTA_DEFAULT, L=r(length), bim_long=r(length), model_qty=length, key=key)
                add("alignments", ("all",), "Eje", "m", line, (a.Name,))
                counts["alignments"] += 1

        # --- plain AutoCAD entities by layer (Model space) --------------------------------
        layer_map = {str(lk).upper(): v for lk, v in LAYER_MAP.items()}
        if LAYERS and layer_map:
            bt = t.GetObject(db.BlockTableId, OpenMode.ForRead)
            ms = t.GetObject(bt[BlockTableRecord.ModelSpace], OpenMode.ForRead)
            for oid in ms:
                e = t.GetObject(oid, OpenMode.ForRead)
                spec = layer_map.get(str(e.Layer).upper())
                if spec is None or str(e.GetType().Namespace) != "Autodesk.AutoCAD.DatabaseServices":
                    continue                         # Civil objects derive from Curve too: AutoCAD types only
                summary, unit, cls = spec
                tname = type(e).__name__
                handle = e.Handle.ToString()
                L = bim_long = bim_sup = None
                cota, nota, value = COTA_DEFAULT, "", 1.0
                try:
                    if unit == "m":
                        if not isinstance(e, Curve):
                            raise ValueError("not a curve")
                        value = (e.GetDistanceAtParameter(e.EndParam) - e.GetDistanceAtParameter(e.StartParam)) * k
                        L = bim_long = r(value)
                        cota = r(e.StartPoint.Z * k)
                    elif unit == "m2":
                        if isinstance(e, Hatch):
                            value = e.Area * k * k
                            cota = r(e.Elevation * k)
                        elif isinstance(e, Curve) and e.Closed:
                            value = e.Area * k * k
                            cota = r(e.StartPoint.Z * k)
                        else:
                            raise ValueError("not a hatch or closed curve")
                        L = bim_sup = r(value)
                        nota = "Longitud = área m2"
                    else:
                        if isinstance(e, BlockReference):
                            cota = r(e.Position.Z * k)
                except Exception as ex:
                    skipped.append({"object": f"{tname} {handle} on {e.Layer}", "reason": str(ex)})
                    continue
                familia = tname
                if isinstance(e, BlockReference):
                    try:
                        familia = t.GetObject(e.DynamicBlockTableRecord, OpenMode.ForRead).Name
                    except Exception:
                        familia = str(e.Name)
                guid, key = elem_guid(handle)
                line = new_line(f"{e.Layer} - {familia} {handle}", guid, cls or IFC_CLASSES["default"], tname, familia,
                                "—", cota, L=L, bim_long=bim_long, bim_sup=bim_sup, nota=nota,
                                model_qty=value, key=key)
                add("layers", (str(e.Layer).upper(),), summary, unit, line, (handle,))
                counts["entities"] += 1
    finally:
        t.Dispose()                                  # no Commit: anything opened ForWrite is rolled back

if civil_doc is None:
    warnings.append("Civil 3D not available: only the LAYER_MAP source ran")
if not groups:
    raise Exception("Nothing to export: no corridors / volume surfaces / pipe networks"
                    + (" and LAYER_MAP is empty." if not LAYER_MAP else " and no entity on the LAYER_MAP layers."))

# --- chapters and partidas ---------------------------------------------------------------
out_chapters, partida_rows, all_guids = [], [], []
for source in sorted(set(s for s, _ in groups), key=lambda s: CHAPTERS[s][0]):
    ccode, csummary = CHAPTERS[source]
    partidas = []
    for pi, gk in enumerate(sorted(gk for s, gk in groups if s == source), start=1):
        g = groups[(source, gk)]
        lines = [l for _, l in sorted(g["lines"], key=lambda t_: t_[0])]
        summary = PARTIDA_SUMMARY.format(label=g["label"], count=len(lines)).replace("  ", " ").strip()
        quantity = round(sum(l["_quantity"] for l in lines), DECIMALS)
        model_qty = sum(l["_model_quantity"] for l in lines)
        pcode = "%s.%02d" % (ccode, pi)
        partidas.append({"code": pcode, "summary": summary, "unit": g["unit"], "quantity": quantity,
                         "quantity_model": round(model_qty, 4), "group": [source] + list(gk), "lines": lines})
        partida_rows.append({"type": "PrestoPartida", "code": pcode, "summary": summary, "unit": g["unit"],
                             "lines": len(lines), "quantity": quantity, "quantity_model": round(model_qty, 4)})
        all_guids.extend(l["GuidElem"] for l in lines)
    out_chapters.append({"code": ccode, "summary": csummary, "partidas": partidas})

if len(set(all_guids)) != len(all_guids):
    raise Exception("Repeated GuidElem in the takeoff (same object measured twice?): nothing was written.")

source_block = {
    "application": "Autodesk Civil 3D" if civil_doc is not None else "Autodesk AutoCAD",
    "drawing": drawing_file, "date": datetime.now().isoformat(timespec="seconds"),
    "drawing_units": unit_name, "to_metres": k, "insunits": insunits, "civil_drawing_units": civil_units,
    "output_units": "m / m2 / m3 / u", "decimals": DECIMALS,
    "id_scheme": "GuidElem = IFC-compressed uuid5(NAMESPACE, drawing_key|handle[|aux]); drawing_key = "
                 + ("Database.FingerprintGuid " + fingerprint if fingerprint else "drawing path")
                 + "; aux = corridor region GUID|shape code|station range, or cut/fill",
    "ifc_globalid": "Civil 3D / AutoCAD objects have no IFC GlobalId unless the drawing is exported to IFC; "
                    "these ids are NOT the IFC export's GlobalIds",
    "sources": {"corridors": CORRIDORS, "corridor_lines": CORRIDOR_LINES, "corridor_method": "average end area",
                "volume_surfaces": VOLUME_SURFACES, "adjusted_volumes": USE_ADJUSTED_VOLUMES,
                "pipe_networks": PIPE_NETWORKS, "pipe_length": PIPE_LENGTH, "alignments": ALIGNMENTS,
                "layers": sorted(LAYER_MAP) if LAYERS else []},
    "counts": counts, "lines": len(all_guids), "skipped": skipped, "warnings": warnings,
}
data = {"root_summary": ROOT_SUMMARY or f"{drawing_name} - takeoff", "source": source_block, "chapters": out_chapters}

out = Path(JSON_PATH) if JSON_PATH else \
    Path(Environment.GetFolderPath(Environment.SpecialFolder.Desktop)) / f"{drawing_name} - Presto takeoff.json"
with open(out, "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=1)

# --- summary ---------------------------------------------------------------------------
print(f"{len(all_guids)} lines in {len(partida_rows)} partidas ({len(out_chapters)} chapters). Counts: {counts}")
for row in partida_rows:
    print(f"  {row['code']}  {row['quantity']:>12,.3f} {row['unit']:<3} {row['lines']:>5} lines  {row['summary']}")
if skipped:
    print(f"  SKIPPED {len(skipped)} - first: {skipped[0]}")
for w in warnings:
    print(f"  WARNING: {w}")
print(f"Saved {out}")

ia_Result = {"type": "Civil3DPrestoTakeoff", "file": str(out), "lines": len(all_guids), "counts": counts,
             "drawing_units": unit_name, "skipped": len(skipped), "warnings": warnings, "partidas": partida_rows}
