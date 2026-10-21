# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import json
import re
from datetime import datetime
from pathlib import Path

import clr

clr.AddReference("Tekla.Structures.Model")
clr.AddReference("Tekla.Structures.Catalogs")

from System import Array, Environment, Type
from Tekla.Structures.Catalogs import LibraryProfileItem, MaterialItem
from Tekla.Structures.Model import Model, Beam, ContourPlate, PolyBeam
from Tekla.Structures.Model.Operations import Operation
from Tekla.Structures.Model.UI import ModelObjectSelector as UISelector

# The host injects the connected model as __teklamodel__
try:
    model = __teklamodel__
except NameError:
    model = Model()

# ---------------------------------------------------------------------------
# Quantity takeoff for RIB Presto with ISO 19650 traceability: ONE
# MEASUREMENT LINE PER PART, each carrying the part's IFC GlobalId, so every
# budget quantity can be traced back to the model element (and to the IFC
# exported from it). Read-only on the model.
#
# Output: one JSON on the Desktop, "<model> - Presto takeoff.json", in the
# format of 01_Scripts/06_Presto/02_Write/CreateBudgetFromJson.py (chapters >
# partidas with unit and quantity) plus, per partida, its "lines" for
# 01_Scripts/06_Presto/02_Write/WriteMeasurementLinesFromJson.py, and a
# "source" block (model, date, numbering, parts out of catalog, skipped
# parts, dimension mismatches). Workflow:
#   1. this script (Tekla)  2. CreateBudgetFromJson.py (Presto, the tree)
#   3. WriteMeasurementLinesFromJson.py (Presto, the lines)
#   4. 01_Read/ReadMeasurementLines.py (Presto, the traceability check)
#
# - Partidas = parts grouped by GROUP_BY (default IFC class + profile +
#   material); chapters = CHAPTER_BY (default the IFC class).
# - Unit: m3 (VOLUME) when the material matches CONCRETE_RE, kg (WEIGHT)
#   otherwise. Concrete line = N x Longitud x Anchura x Altura (m) checked
#   against VOLUME (0.2 %); when they differ (openings, irregular contour)
#   the line becomes net area (VOLUME / thickness) x thickness and the part
#   is reported. Steel line = Longitud (m) x Anchura (kg/m = WEIGHT / LENGTH).
# - Parts with NO SOLID (profile or material not in the environment catalog:
#   VOLUME = WEIGHT = LENGTH = 0): steel uses the axis length x
#   NOMINAL_KG_PER_M[profile]; without an entry the part is SKIPPED and
#   listed - add the profile to NOMINAL_KG_PER_M or fix the catalog.
#   Metric W shapes: the designation is the kg/m (W310X97 -> 97.0);
#   HSS152.4X12.7 (HSS6x6x1/2) = 52.44 kg/m (AISC 35.24 lb/ft).
# - Line quantities are rounded to DECIMALS, like Presto does with
#   Obra.DecCantMed = DECIMALS, so "quantity" (sum of the rounded lines) is
#   what Presto will show; "quantity_model" is the unrounded model total.
# - Planta / Cota: the highest level <= part reference Z + 1 mm. LEVELS (mm)
#   or, when empty, auto-detected per Area from column bases, horizontal beam
#   lines and slab tops (rounded to 10 mm, levels closer than LEVEL_MERGE_MM
#   merged into the lower one). Tekla's IFC export writes storeys "Unknown"
#   when the organizer has none, hence computed here.
#
# Verified (Tekla 2026, 2026-10-20) - the pieces, from one-off scripts:
#   IFC GlobalId = IFC base64 compression of str(Identifier.GUID) (matched all
#   570 parts of a Tekla IFC4 export; report property IFC_GUID is EMPTY before
#   an export). IFC class override = UDAs proIfcEntityOvrd /
#   proIfcEntityPreDef (UDA IFC_ENTITY is ignored by the export). Report
#   properties VOLUME mm3, WEIGHT kg, LENGTH mm (plate: longest side), WIDTH /
#   HEIGHT (plate: WIDTH = thickness); parts out of catalog have no solid.
#   LibraryProfileItem().Select / MaterialItem().Select, IsNumberingUpToDateAll.
# Whole script run on Tekla 2026 (2026-10-20, New Model 2): 570 parts,
# 0 skipped with NOMINAL_KG_PER_M for the 4 out-of-catalog steel profiles,
# then CreateBudgetFromJson + WriteMeasurementLinesFromJson in Presto: all
# line counts / GUIDs / sums checked, ReadMeasurementLines agrees.
# Default IFC classes without override are a GUESS (Tekla decides some by
# name/class) and are flagged in Nota.
# ---------------------------------------------------------------------------
OUTPUT_PATH = None             # None -> Desktop / "<model> - Presto takeoff.json"
SELECTION_ONLY = False         # True -> only the parts selected in Tekla
ROOT_SUMMARY = ""              # "" -> "<model> - takeoff"

# Grouping keys: "ifc_class", "predefined", "profile", "material", "name", "class", "area"
GROUP_BY = ("ifc_class", "name", "profile", "material")   # "name" keeps e.g. landings apart from slabs
CHAPTER_BY = "ifc_class"       # one of the keys above, or None for a single chapter
SINGLE_CHAPTER_SUMMARY = "Estructura"

CONCRETE_RE = r"^C\d|^HA|^HM|concrete|hormig"          # material -> m3, else kg
NOMINAL_KG_PER_M = {}          # e.g. {"W310X97": 97.0} for profiles out of catalog
DECIMALS = 3                   # Presto Obra.DecCantMed / Conceptos.RedParc
DIM_TOLERANCE = 0.002          # 0.2 % dims product vs VOLUME

LEVELS = []                    # mm, e.g. [0, 3000, 6000]; or {"Area name": [...]}; [] -> auto
LEVEL_MERGE_MM = 300.0
STOREY_NAME = "Planta {index:02d} ({elevation:+.2f} m)"
BUILDING = ""                  # Área for every part; "" -> model name
BUILDING_X_RANGES = []         # [(x_min_mm or None, x_max_mm or None, "Area name"), ...] first match wins

CLASS_LABELS = {               # partida summary / chapter summary per IFC class
    "IfcColumn": ("Pilar", "Pilares"), "IfcBeam": ("Viga", "Vigas"),
    "IfcMember": ("Barra", "Barras y arriostramientos"), "IfcPlate": ("Chapa", "Chapas"),
    "IfcSlab": ("Losa", "Losas"), "IfcWall": ("Muro", "Muros"),
    "IfcStairFlight": ("Tramo de escalera", "Escaleras"), "IfcFooting": ("Cimentación", "Cimentaciones"),
}
PARTIDA_SUMMARY = "{label} {profile} {material} ({count} ud)"   # WriteMeasurementLinesFromJson CLEAN_SUMMARIES drops "(...)"

CH64 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_$"
RECT_RE = re.compile(r"^\s*(\d+(?:\.\d+)?)\s*\*\s*(\d+(?:\.\d+)?)\s*$")   # concrete "H*W"


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


def report(part, name):
    found, value = part.GetReportProperty(name, 0.0)
    return float(value) if found else 0.0


def uda(part, name):
    found, value = part.GetUserProperty(name, "")
    return str(value).strip() if found and value else ""


def guess_class(part, kind, name):
    if kind == "Beam" and str(part.Type) == "COLUMN":
        return "IfcColumn"
    if re.search(r"BRACE|DIAG|ARRIOST", name, re.I):
        return "IfcMember"
    if kind == "ContourPlate":
        return "IfcSlab" if re.search(r"SLAB|LOSA|FORJADO", name, re.I) else "IfcPlate"
    return "IfcBeam"


def area_of(x):
    for x0, x1, area in BUILDING_X_RANGES:
        if (x0 is None or x >= x0) and (x1 is None or x < x1):
            return area
    return BUILDING or model_name


def r(v, n=DECIMALS):
    return None if v is None else round(v, n)


if not model.GetConnectionStatus():
    raise Exception("Not connected to Tekla Structures.")

info = model.GetInfo()
model_name = Path(info.ModelName).stem
model_file = str(Path(info.ModelPath) / info.ModelName)
numbering_ok = bool(Operation.IsNumberingUpToDateAll())

# --- parts --------------------------------------------------------------------
part_types = (Beam, ContourPlate, PolyBeam)
if SELECTION_ONLY:
    enumerator = UISelector().GetSelectedObjects()
else:
    enumerator = model.GetModelObjectSelector().GetAllObjectsWithType(
        Array[Type]([clr.GetClrType(t) for t in part_types]))
total = enumerator.GetSize()
step = max(1, total // 10)
print(f"Reading {total} objects of {model_name}...")

parts, seen = [], 0
while enumerator.MoveNext():
    part = enumerator.Current
    if part is None or not isinstance(part, part_types):
        continue
    seen += 1
    if seen % step == 0:
        print(f"  {seen}/{total}")
    kind = "ContourPlate" if isinstance(part, ContourPlate) else ("PolyBeam" if isinstance(part, PolyBeam) else "Beam")
    name = part.Name or ""
    p = {"guid": str(part.Identifier.GUID), "kind": kind, "name": name, "class": part.Class or "",
         "profile": part.Profile.ProfileString or "", "material": part.Material.MaterialString or "",
         "volume": report(part, "VOLUME"), "weight": report(part, "WEIGHT"), "length": report(part, "LENGTH"),
         "width": report(part, "WIDTH"), "height": report(part, "HEIGHT"),
         "column": kind == "Beam" and str(part.Type) == "COLUMN", "pts": None}
    p["ifc_guid"] = ifc_guid(p["guid"])
    override = uda(part, "proIfcEntityOvrd")
    p["ifc_class"] = override or guess_class(part, kind, name)
    p["ifc_guessed"] = not override
    p["predefined"] = uda(part, "proIfcEntityPreDef")
    solid = part.GetSolid()
    mn, mx = solid.MinimumPoint, solid.MaximumPoint
    p["bbox"] = ((mn.X, mn.Y, mn.Z), (mx.X, mx.Y, mx.Z))
    p["has_solid"] = p["volume"] > 0 and (mx.X - mn.X) + (mx.Y - mn.Y) + (mx.Z - mn.Z) > 0
    if kind == "Beam":
        p["pts"] = ((part.StartPoint.X, part.StartPoint.Y, part.StartPoint.Z),
                    (part.EndPoint.X, part.EndPoint.Y, part.EndPoint.Z))
    elif kind == "ContourPlate" and not p["has_solid"]:
        cps = part.Contour.ContourPoints
        p["pts"] = tuple((cp.X, cp.Y, cp.Z) for cp in cps)
    parts.append(p)

if not parts:
    raise Exception("No parts to export" + (" in the selection." if SELECTION_ONLY else "."))

# --- geometry helpers ---------------------------------------------------------
for p in parts:
    if p["pts"] and p["kind"] == "Beam":
        (x0, y0, z0), (x1, y1, z1) = p["pts"]
        p["axis"] = ((x1 - x0) ** 2 + (y1 - y0) ** 2 + (z1 - z0) ** 2) ** 0.5
    else:
        p["axis"] = 0.0
    (bx0, by0, bz0), (bx1, by1, bz1) = p["bbox"]
    if p["has_solid"]:
        ref_x = bx0
        horizontal = p["kind"] == "ContourPlate" and (bz1 - bz0) <= max(p["width"], 1.0) + 1.0
    else:
        xs = [q[0] for q in p["pts"] or [(0, 0, 0)]]
        zs = [q[2] for q in p["pts"] or [(0, 0, 0)]]
        ref_x, bz0, bz1 = min(xs), min(zs), max(zs)
        horizontal = p["kind"] == "ContourPlate" and bz1 - bz0 < 1.0
    p["horizontal_plate"] = horizontal
    if p["kind"] == "Beam":
        p["ref_z"] = min(p["pts"][0][2], p["pts"][1][2])      # column base / beam line (beams may hang below it)
    elif horizontal:
        p["ref_z"] = bz1                                       # slab top = its level
    else:
        p["ref_z"] = bz0
    p["area"] = area_of(ref_x)
    p["ref_x"] = ref_x

# --- levels -------------------------------------------------------------------
def merge_levels(values):
    out = []
    for z in sorted(set(round(v / 10.0) * 10.0 for v in values)):
        if not out or z - out[-1] > LEVEL_MERGE_MM:
            out.append(z)
    return out


levels_by_area = {}
for area in sorted(set(p["area"] for p in parts)):
    if isinstance(LEVELS, dict):
        levels_by_area[area] = sorted(float(z) for z in LEVELS.get(area, []))
    elif LEVELS:
        levels_by_area[area] = sorted(float(z) for z in LEVELS)
    else:
        cand = []
        for p in parts:
            if p["area"] != area:
                continue
            if p["column"]:
                cand.append(p["ref_z"])
            elif p["kind"] == "Beam" and abs(p["pts"][0][2] - p["pts"][1][2]) < 1.0 and p["ifc_class"] in ("IfcBeam", "IfcWall"):
                cand.append(p["ref_z"])
            elif p["horizontal_plate"] and p["ifc_class"] == "IfcSlab" and p["predefined"] not in ("LANDING",):
                cand.append(p["ref_z"])
        levels_by_area[area] = merge_levels(cand)

for p in parts:
    levels = levels_by_area.get(p["area"]) or [0.0]
    idx = 0
    for i, z in enumerate(levels):
        if z <= p["ref_z"] + 1.0:
            idx = i
    p["cota"] = round(levels[idx] / 1000.0, 3)
    p["planta"] = STOREY_NAME.format(index=idx, elevation=levels[idx] / 1000.0)

# --- catalog check for parts without solid --------------------------------------
no_solid = {}
for p in parts:
    if not p["has_solid"]:
        no_solid.setdefault((p["profile"], p["material"]), []).append(p)
out_of_catalog = []
for (profile, material), ps in sorted(no_solid.items()):
    out_of_catalog.append({"profile": profile, "material": material, "parts": len(ps),
                           "profile_in_catalog": bool(LibraryProfileItem().Select(profile)),
                           "material_in_catalog": bool(MaterialItem().Select(material))})

# --- one measurement line per part ----------------------------------------------
concrete_re = re.compile(CONCRETE_RE, re.I)
skipped, mismatches, groups = [], [], {}


def group_key(p, keys):
    return tuple(p[k] for k in keys)


for p in parts:
    concrete = bool(concrete_re.search(p["material"]))
    notes = []
    if p["ifc_guessed"]:
        notes.append("clase IFC supuesta (sin proIfcEntityOvrd)")
    L = A = H = None
    if concrete:
        unit = "m3"
        rect = RECT_RE.match(p["profile"]) if p["kind"] == "Beam" else None
        volume = p["volume"] / 1e9
        if p["has_solid"] and p["kind"] == "Beam" and rect:
            L, A, H = p["length"] / 1000.0, float(rect.group(2)) / 1000.0, float(rect.group(1)) / 1000.0
            thick = min(A, H)
        elif p["has_solid"] and p["kind"] == "ContourPlate":
            L, A, H = p["length"] / 1000.0, p["height"] / 1000.0, p["width"] / 1000.0
            thick = H
        elif p["has_solid"]:
            thick = 0.0
        elif rect and p["axis"] > 0:        # no solid but parametric H*W: axis x section
            L, A, H = p["axis"] / 1000.0, float(rect.group(2)) / 1000.0, float(rect.group(1)) / 1000.0
            volume, thick = L * A * H, min(A, H)
            notes.append("sin sólido en Tekla: volumen = eje x sección")
        else:
            skipped.append({"guid": p["guid"], "name": p["name"], "profile": p["profile"], "material": p["material"],
                            "reason": "no solid and no rectangular H*W profile"})
            continue
        if L is not None:
            L, A, H = r(L), r(A), r(H)
        product = (L or 0) * (A or 0) * (H or 0) if L is not None else 0.0
        if L is None or abs(product - volume) > DIM_TOLERANCE * max(volume, 1e-6) + 0.5 * 10 ** -DECIMALS:
            if L is not None:
                mismatches.append({"guid": p["guid"], "name": p["name"], "profile": p["profile"],
                                   "dims_m3": round(product, 4), "volume_m3": round(volume, 4)})
            if thick > 0:
                L, A, H = r(volume / thick), None, r(thick)
                notes.append("huecos o contorno irregular: Longitud = superficie neta m2 (VOLUME / espesor)")
            else:
                L, A, H = r(volume), None, None
                notes.append("Longitud = volumen del modelo m3")
        comment_dims = ""
        bim_vol = r(volume, 4)
    else:
        unit = "kg"
        if p["has_solid"] and p["length"] > 0 and p["weight"] > 0:
            L = r(p["length"] / 1000.0)
            A = r(p["weight"] / L) if L else None
            comment_dims = " - Longitud m x Anchura kg/m"
        elif p["axis"] > 0 and p["profile"] in NOMINAL_KG_PER_M:
            L, A = r(p["axis"] / 1000.0), float(NOMINAL_KG_PER_M[p["profile"]])
            comment_dims = " - Longitud m x Anchura kg/m nominal"
            notes.append("peso nominal %.2f kg/m (perfil sin sólido en Tekla, fuera del catálogo)" % A)
        else:
            skipped.append({"guid": p["guid"], "name": p["name"], "profile": p["profile"], "material": p["material"],
                            "reason": "no solid (profile/material out of catalog) and no NOMINAL_KG_PER_M entry"})
            continue
        bim_vol = r(p["volume"] / 1e9, 4) if p["volume"] > 0 else None
    qty = round((L or 0) * (A if A is not None else 1) * (H if H is not None else 1), DECIMALS)
    label = CLASS_LABELS.get(p["ifc_class"], (p["ifc_class"], p["ifc_class"]))[0]
    line = {
        "Comentario": f"{p['name'] or label} {p['profile']} {p['material']} - {p['planta']}{comment_dims}",
        "N": 1, "Longitud": L, "Anchura": A, "Altura": H,
        "GuidElem": p["ifc_guid"], "CategoríaBIM": p["ifc_class"],
        "TipoBIM": f"{p['profile']} {p['material']}".strip(), "FamiliaBIM": p["name"],
        "Planta": p["planta"], "Cota": p["cota"], "Área": p["area"], "Archivo": model_file,
        "BIMLong": r((p["axis"] or p["length"]) / 1000.0), "BIMVol": bim_vol,
        "Nota": "; ".join(notes),
        "_quantity": qty, "_tekla_guid": p["guid"],
        "_model_quantity": (p["volume"] / 1e9 if p["has_solid"] else qty) if unit == "m3" else (p["weight"] if p["has_solid"] else qty),
    }
    key = group_key(p, GROUP_BY)
    g = groups.setdefault(key, {"unit": unit, "lines": [], "sample": p})
    if g["unit"] != unit:
        raise Exception(f"Group {key} mixes m3 and kg parts: add 'material' to GROUP_BY.")
    g["lines"].append((p["cota"], p["ref_x"], line))

# --- chapters and partidas ----------------------------------------------------------
chapters = {}
for key, g in groups.items():
    s = g["sample"]
    ckey = s[CHAPTER_BY] if CHAPTER_BY else ""
    chapters.setdefault(ckey, []).append((key, g))

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
        lines = [l for _, _, l in sorted(g["lines"], key=lambda t: (t[0], t[1]))]
        label = CLASS_LABELS.get(s["ifc_class"], (s["ifc_class"], s["ifc_class"]))[0]
        summary = PARTIDA_SUMMARY.format(label=label, profile=s["profile"], material=s["material"], name=s["name"],
                                         ifc_class=s["ifc_class"], count=len(lines)).replace("  ", " ").strip()
        quantity = round(sum(l["_quantity"] for l in lines), DECIMALS)
        model_qty = sum(l["_model_quantity"] for l in lines)
        pcode = "%s.%02d" % (ccode, pi)
        partidas.append({"code": pcode, "summary": summary, "unit": g["unit"], "quantity": quantity,
                         "quantity_model": round(model_qty, 4), "group": dict(zip(GROUP_BY, key)), "lines": lines})
        partida_rows.append({"type": "PrestoPartida", "code": pcode, "summary": summary, "unit": g["unit"],
                             "parts": len(lines), "quantity": quantity, "quantity_model": round(model_qty, 4)})
    out_chapters.append({"code": ccode, "summary": csummary, "partidas": partidas})

source = {
    "application": "Tekla Structures", "model": model_file, "date": datetime.now().isoformat(timespec="seconds"),
    "selection_only": SELECTION_ONLY, "numbering_up_to_date": numbering_ok,
    "parts_read": len(parts), "parts_in_lines": sum(r_["parts"] for r_ in partida_rows),
    "group_by": list(GROUP_BY), "chapter_by": CHAPTER_BY, "decimals": DECIMALS,
    "levels_mm": levels_by_area, "parts_out_of_catalog": out_of_catalog,
    "skipped_parts": skipped, "dimension_mismatches": mismatches,
}
data = {"root_summary": ROOT_SUMMARY or f"{model_name} - takeoff", "source": source, "chapters": out_chapters}

out = Path(OUTPUT_PATH) if OUTPUT_PATH else \
    Path(Environment.GetFolderPath(Environment.SpecialFolder.Desktop)) / f"{model_name} - Presto takeoff.json"
with open(out, "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=1)

# --- summary ------------------------------------------------------------------------
print(f"{len(parts)} parts read, {source['parts_in_lines']} in {len(partida_rows)} partidas "
      f"({len(out_chapters)} chapters). Numbering up to date: {numbering_ok}.")
for row in partida_rows:
    print(f"  {row['code']}  {row['quantity']:>12,.3f} {row['unit']:<3} {row['parts']:>4} parts  {row['summary']}")
for c in out_of_catalog:
    print(f"  NO SOLID: {c['parts']} parts {c['profile']} / {c['material']} (profile in catalog: "
          f"{c['profile_in_catalog']}, material: {c['material_in_catalog']})")
if skipped:
    print(f"  SKIPPED {len(skipped)} parts - first: {skipped[0]}")
if mismatches:
    print(f"  {len(mismatches)} concrete parts where L x W x H != VOLUME: written as net area x thickness")
for area, lv in levels_by_area.items():
    print(f"  Levels {area}: {[round(z) for z in lv]}")
print(f"Saved {out}")

ia_Result = {"type": "TeklaPrestoTakeoff", "file": str(out), "parts": len(parts), "skipped": len(skipped),
             "dimension_mismatches": len(mismatches), "numbering_up_to_date": numbering_ok,
             "out_of_catalog": out_of_catalog, "levels_mm": levels_by_area, "partidas": partida_rows}
