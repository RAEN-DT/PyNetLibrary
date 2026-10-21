# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import json
import re
from pathlib import Path

import clr

clr.AddReference("System.Windows.Forms")

from System import Environment
from System.Windows.Forms import MessageBox, MessageBoxButtons, MessageBoxIcon, DialogResult

# The host injects the Presto COM application (Presto.App.18) as __presto__
try:
    app = __presto__
except NameError:
    raise Exception("__presto__ not found: run this script from PyNET for Presto (Complementos > PyNET).")

# ---------------------------------------------------------------------------
# Write the MEASUREMENT LINES (table Mediciones) of a BIM takeoff into the
# open obra: one line per model element with its IFC GlobalId (GuidElem),
# IFC class (CategoríaBIM), type, family, storey (Planta / Cota), building
# (Área), source file (Archivo), model length / volume (BIMLong / BIMVol) -
# the ISO 19650 link between every budget quantity and the model.
#
# Input: the JSON of 01_Scripts/05_Tekla/06_Export/ExportTakeoffForPresto.py
# (CreateBudgetFromJson.py format + "lines" per partida). The budget tree must
# exist first (CreateBudgetFromJson.py). Partidas without "lines" are ignored.
# A line is {"N", "Longitud", "Anchura", "Altura" (numbers or null),
# "Comentario", "GuidElem", "CategoríaBIM", "TipoBIM", "FamiliaBIM", "Planta",
# "Cota", "Área", "Archivo", "BIMLong", "BIMVol", "Nota"}; keys starting with
# "_" are not written. Presto computes Mediciones.Cantidad itself.
#
# Per partida: finds the relation(s) parent -> partida (the partida may have
# been moved, e.g. by ClassifyCypeChapters.py, so the JSON chapter is not
# used); more than one parent is refused unless ALLOW_MULTIPLE_PARENTS
# (then the lines are written under every parent). Partidas that already
# have lines are refused unless REPLACE_EXISTING (then their lines are
# deleted first). Sets the rounding to DECIMALS BEFORE inserting
# (Obra.DecCantMed and Conceptos.RedParc; the default 2 rounds lines to cm
# and 0.01 m3). Then sets Relaciones.CanPres = sum of the lines (Presto does
# not recompute it for lines written through the API) and reads everything
# back: line count, unique GuidElem, sum vs the JSON quantity (tolerance:
# half a unit of the last decimal per line), CanPres == sum.
#
# Verified on Presto 26.01 (2026-10-20), from one-off scripts on 570 lines
# of a Tekla model: InitRecord/SetField/InsertRecord on Mediciones with the
# fields above + Origen 3, the delete loop, Obra.DecCantMed / RedParc, the
# CanPres sync, the SetElement walk of the lines. Whole script run on
# Presto 26.01 (2026-10-20) on a blank obra after CreateBudgetFromJson.py:
# 570 lines / 12 partidas in ~60 s, every check passed, ReadMeasurementLines
# agrees. Mediciones.Cantidad is NOT ready right after InsertRecord, so the
# CanPres sync runs after Recalculate(1) as a SECOND undo step (2 Ctrl+Z).
# Changes are NOT saved: save the obra in Presto.
# ---------------------------------------------------------------------------
JSON_PATH = None               # None -> newest "* - Presto takeoff.json" on the Desktop
EXPECTED_PROJECT = ""          # e.g. "Model2Tekla.Presto" - "" accepts the open obra after confirmation
CODES = []                     # [] -> every partida with lines in the JSON; or a subset
REPLACE_EXISTING = False       # True -> delete the partida's existing lines first
ALLOW_MULTIPLE_PARENTS = False # True -> write the lines under every parent of the partida
DECIMALS = 3                   # Obra.DecCantMed and Conceptos.RedParc
CLEAN_SUMMARIES = False        # True -> drop a trailing "(...)" from the partida summary (e.g. "(24 ud)")
ORIGIN_PLUGIN = 3              # Mediciones.Origen: 3 = plugin

LINE_SLOT, LOOKUP_SLOT = 8, 9
TEXT_FIELDS = ["Comentario", "GuidElem", "CategoríaBIM", "TipoBIM", "FamiliaBIM", "Planta", "Área", "Archivo", "Nota"]
NUM_FIELDS = ["N", "Longitud", "Anchura", "Altura", "Cota", "BIMLong", "BIMSup", "BIMVol"]   # BIMSup ⏳ (field exists in Presto 26.01's dictionary, never written yet)


def q(text):
    return '"' + text + '"'


def line_filter(sup, code):
    return "Mediciones.CodSup==" + q(sup) + " && Mediciones.CodInf==" + q(code)


def parents_of(code):
    out = []
    app.SetElement(LOOKUP_SLOT, "Relaciones", "Relaciones.CodSup", '"*"', "Relaciones.CodInf==" + q(code))
    while app.GetElement(LOOKUP_SLOT) == 0:
        out.append(app.GetFieldStr("Relaciones.CodSup"))
    return out


def read_lines(sup, code):
    rows = []
    app.SetElement(LINE_SLOT, "Mediciones", "Mediciones.Relación", '"*"', line_filter(sup, code))
    while app.GetElement(LINE_SLOT) == 0:
        pres = app.GetFieldNum("Mediciones.Pres")
        rows.append({"guid": (app.GetFieldStr("Mediciones.GuidElem") or "").strip(),
                     "qty": float(app.GetFieldNum("Mediciones.Cantidad") or 0.0),
                     "counts": pres is None or float(pres) == 1.0})
    return rows


def strip_count(summary):
    """Summary without a trailing "(...)" such as "(24 ud)"."""
    return re.sub(r"\s*\([^()]*\)\s*$", "", summary).strip()


def find_relation(sup, code):
    app.SetElement(LOOKUP_SLOT, "Relaciones", "Relaciones.CodSup", q(sup), "Relaciones.CodInf==" + q(code))
    return app.GetElement(LOOKUP_SLOT) == 0


def set_canpres(sup, code, value):
    if not find_relation(sup, code):
        raise Exception(f"Relation {sup} -> {code} not found")
    app.SetField("Relaciones.CanPres", value)
    app.UpdateRecord("Relaciones")


# --- input ----------------------------------------------------------------------
if JSON_PATH:
    path = Path(JSON_PATH)
else:
    desktop = Path(Environment.GetFolderPath(Environment.SpecialFolder.Desktop))
    found = sorted((p for p in desktop.iterdir() if p.name.endswith(" - Presto takeoff.json")),
                   key=lambda p: p.stat().st_mtime)
    if not found:
        raise Exception(f"No '* - Presto takeoff.json' on {desktop}: set JSON_PATH.")
    path = found[-1]
if not path.exists():
    raise Exception(f"Input file not found: {path}")
with open(path, encoding="utf-8") as fh:
    data = json.load(fh)

partidas = []
for ch in data.get("chapters", []):
    for p in ch.get("partidas", []):
        if p.get("lines") and (not CODES or str(p.get("code")) in CODES):
            partidas.append(p)
if not partidas:
    raise Exception(f"{path.name} has no partidas with 'lines'" + (f" among {CODES}." if CODES else "."))

problems = []
for p in partidas:
    guids = [str(l.get("GuidElem") or "").strip() for l in p["lines"]]
    if not all(guids):
        problems.append(f"{p['code']}: {guids.count('')} lines without GuidElem in the JSON")
    if len(set(g for g in guids if g)) != len([g for g in guids if g]):
        problems.append(f"{p['code']}: repeated GuidElem in the JSON")

# --- target obra --------------------------------------------------------------------
project = str(app.Project() or "")
if not project:
    raise Exception("No obra is open in Presto: open one and run the script again.")
if EXPECTED_PROJECT and not project.lower().endswith(EXPECTED_PROJECT.lower()):
    raise Exception(f"The open obra is {project}, not {EXPECTED_PROJECT}: nothing was written.")
read_only = None
try:
    read_only = app.ReadOnly()     # ⏳ expected: non-zero when the obra was opened read-only
except Exception:
    pass
if read_only:
    raise Exception(f"{project} is open read-only: nothing was written.")

# --- plan: relations and existing lines -----------------------------------------------
plan, replaced, renamed = [], 0, []
for p in partidas:
    code = str(p["code"])
    if app.FindEqual("Conceptos", "Conceptos.Código", code) != 0:
        problems.append(f"{code}: not in the obra (create the budget first: CreateBudgetFromJson.py)")
        continue
    unit = app.GetFieldStr("Conceptos.Ud") or ""
    presto_summary = app.GetFieldStr("Conceptos.Resumen") or ""
    if strip_count(presto_summary).lower() != strip_count(str(p.get("summary") or "")).lower():
        renamed.append(f"  {code}: Presto '{presto_summary[:50]}' / JSON '{str(p.get('summary') or '')[:50]}'")
    if p.get("unit") and unit and unit.strip().lower() != str(p["unit"]).strip().lower():
        problems.append(f"{code}: unit in Presto '{unit}' but '{p['unit']}' in the JSON")
    sups = parents_of(code)
    if not sups:
        problems.append(f"{code}: has no parent in the budget tree")
        continue
    if len(sups) > 1 and not ALLOW_MULTIPLE_PARENTS:
        problems.append(f"{code}: hangs from {len(sups)} parents {sups} (set ALLOW_MULTIPLE_PARENTS = True)")
        continue
    for sup in sups:
        existing = len(read_lines(sup, code))
        if existing and not REPLACE_EXISTING:
            problems.append(f"{sup}/{code}: already has {existing} lines (set REPLACE_EXISTING = True)")
        replaced += existing
        plan.append((sup, code, p, existing))

if problems:
    raise Exception("Nothing was written:\n  " + "\n  ".join(problems))

n_lines = sum(len(p["lines"]) for _, _, p, _ in plan)
listing = "\n".join(f"  {sup}/{code}: {len(p['lines'])} lines, {p.get('quantity', 0):,.3f} {p.get('unit', '')}"
                    + (f" (replaces {ex})" if ex else "") for sup, code, p, ex in plan[:25])
if len(plan) > 25:
    listing += f"\n  ... and {len(plan) - 25} more"
answer = MessageBox.Show(
    f"Write {n_lines} measurement lines in {len(plan)} partidas of\n\n{project}\n\nfrom {path.name}?\n\n{listing}\n\n"
    + (f"{replaced} existing lines will be DELETED.\n" if replaced else "")
    + ("Summary differs (same code, another partida?):\n" + "\n".join(renamed[:10]) + "\n" if renamed else "")
    + f"Rounding of the obra and of these partidas set to {DECIMALS} decimals.\n"
    + "Changes are not saved: close without saving to undo, or use Presto's undo.",
    "PyNET - Write measurement lines",
    MessageBoxButtons.YesNo,
    MessageBoxIcon.Question,
)
if answer != DialogResult.Yes:
    print("Cancelled: nothing was written.")
else:
    deleted, synced_in_step = 0, True
    app.BeginRedo()
    try:
        # Rounding BEFORE inserting: values already inserted keep their rounding.
        app.FindFirst("Obra", "Obra.Código")       # the obra's single record (return value not checked, as verified)
        app.SetField("Obra.DecCantMed", DECIMALS)
        app.UpdateRecord("Obra")
        for code in sorted(set(c for _, c, _, _ in plan)):
            if app.FindEqual("Conceptos", "Conceptos.Código", code) == 0:
                app.SetField("Conceptos.RedParc", DECIMALS)
                if CLEAN_SUMMARIES:
                    s = app.GetFieldStr("Conceptos.Resumen") or ""
                    clean = strip_count(s)
                    if clean and clean != s:
                        app.SetField("Conceptos.Resumen", clean)
                app.UpdateRecord("Conceptos")
        for sup, code, p, existing in plan:
            # Delete: restart the set after every DeleteRecord (deleting moves it).
            guard = existing + 10
            while guard > 0:
                app.SetElement(LINE_SLOT, "Mediciones", "Mediciones.Relación", '"*"', line_filter(sup, code))
                if app.GetElement(LINE_SLOT) != 0:
                    break
                app.DeleteRecord("Mediciones", 0)
                deleted += 1
                guard -= 1
            for line in p["lines"]:
                app.InitRecord("Mediciones")
                app.SetField("Mediciones.CodSup", sup)
                app.SetField("Mediciones.CodInf", code)
                for f in NUM_FIELDS:
                    if line.get(f) is not None:
                        app.SetField("Mediciones." + f, float(line[f]))
                for f in TEXT_FIELDS:
                    if line.get(f):
                        app.SetField("Mediciones." + f, str(line[f]))
                app.SetField("Mediciones.Origen", ORIGIN_PLUGIN)
                app.InsertRecord("Mediciones")
        # Relaciones.CanPres is not recomputed from lines written by API: set it to their sum.
        for sup, code, p, _ in plan:
            rows = read_lines(sup, code)
            total = sum(r["qty"] for r in rows if r["counts"])
            if total == 0 and float(p.get("quantity") or 0) > 0:
                synced_in_step = False       # Cantidad not computed yet: sync after Recalculate
                break
            set_canpres(sup, code, round(total, DECIMALS + 3))
    finally:
        app.EndRedo()     # always: a BeginRedo without EndRedo leaves Presto's undo blocked
    app.Recalculate(1)

    if not synced_in_step:
        app.BeginRedo()
        try:
            for sup, code, _, _ in plan:
                total = sum(r["qty"] for r in read_lines(sup, code) if r["counts"])
                set_canpres(sup, code, round(total, DECIMALS + 3))
        finally:
            app.EndRedo()
        app.Recalculate(1)
    app.UpdateScreen()

    # --- verify --------------------------------------------------------------------
    report, failures = [], []
    for sup, code, p, _ in plan:
        rows = read_lines(sup, code)
        total = sum(r["qty"] for r in rows if r["counts"])
        guids = [r["guid"] for r in rows]
        want_guids = set(str(l.get("GuidElem")).strip() for l in p["lines"])
        find_relation(sup, code)
        canpres = float(app.GetFieldNum("Relaciones.CanPres") or 0.0)
        expected = float(p.get("quantity") or 0.0)
        tol = len(p["lines"]) * 0.5 * 10 ** -DECIMALS + 1e-6
        ok = {"count": len(rows) == len(p["lines"]),
              "unique_guids": len(set(guids)) == len(guids) and set(guids) == want_guids,
              "sum_vs_json": abs(total - expected) <= tol,
              "canpres_vs_sum": abs(canpres - total) <= 10 ** -DECIMALS}
        if not all(ok.values()):
            failures.append(code)
        report.append({"type": "PrestoMeasurementLines", "parent": sup, "code": code, "lines": len(rows),
                       "expected_lines": len(p["lines"]), "sum_lines": round(total, 4), "json_quantity": expected,
                       "canpres": canpres, "checks": ok})
        print(f"  {sup}/{code}: {len(rows)} lines, sum {total:,.3f} (JSON {expected:,.3f}), CanPres {canpres:,.3f}"
              + ("" if all(ok.values()) else "  <-- CHECK " + ", ".join(k for k, v in ok.items() if not v)))

    print(f"Wrote {n_lines} lines in {len(plan)} partidas of {project} ({deleted} old lines deleted). "
          + ("One undo step. " if synced_in_step else "Two undo steps (lines, then CanPres). ")
          + ("All checks passed. " if not failures else f"CHECK {failures}. ") + "Save the obra in Presto.")
    ia_Result = {"type": "PrestoMeasurementLinesWrite", "project": project, "json": str(path),
                 "lines": n_lines, "deleted": deleted, "undo_steps": 1 if synced_in_step else 2,
                 "failures": failures, "partidas": report}
