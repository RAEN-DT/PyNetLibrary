# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import json
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
# Create a budget WITHOUT PRICES in the open obra from a JSON file: chapters
# (Nat 4) under the root and partidas (Nat 5) under each chapter, with their
# unit, summary and quantity (Relaciones.CanPres). Typical input: a quantity
# takeoff exported from Revit, Tekla or Rhino with PyNET.
#
# JSON format (codes are optional: "01", "02"... and "01.001"... by default):
#   {
#     "root_summary": "Office building - takeoff",          (optional)
#     "chapters": [
#       {"code": "01", "summary": "Walls", "partidas": [
#           {"code": "01.001", "summary": "Brick wall 140 mm", "unit": "m2", "quantity": 125.6}
#       ]}
#     ]
#   }
#
# Safety: the obra must match EXPECTED_PROJECT (if set) and the user confirms
# in a dialog. Codes that already exist are refused unless
# UPDATE_EXISTING = True (then their nature/summary/unit/quantity are
# overwritten). All the edits are one Presto undo step (BeginRedo/EndRedo).
#
# Verified on Presto 26.01 (same pattern as the Revit/Tekla/Rhino > Presto
# tests). The changes are made in the open obra but NOT saved: save it in
# Presto, or close without saving to discard them (⏳ Presto keeps a
# .PrestoRecover file of unsaved changes).
# ---------------------------------------------------------------------------
JSON_PATH = Path(Environment.GetFolderPath(Environment.SpecialFolder.Desktop)) / "PrestoBudget.json"
EXPECTED_PROJECT = ""          # e.g. "MyProject.Presto" - "" accepts the open obra after confirmation
UPDATE_EXISTING = False

NAT_ROOT = 0
NAT_CHAPTER = 4
NAT_PARTIDA = 5
LOOKUP_SLOT = 9                # element slot used for relation lookups (not used by any loop here)


def ensure_concept(code, nat, summary, unit):
    """Creates the concept when it does not exist, then writes its fields."""
    if app.FindEqual("Conceptos", "Conceptos.Código", code) != 0:
        app.InitRecord("Conceptos")
        app.SetField("Conceptos.Código", code)
        app.InsertRecord("Conceptos")
        if app.FindEqual("Conceptos", "Conceptos.Código", code) != 0:   # make it the current record
            raise Exception(f"Could not create concept {code}")
    app.SetField("Conceptos.Nat", nat)
    app.SetField("Conceptos.Resumen", summary)
    if unit:
        app.SetField("Conceptos.Ud", unit)
    app.UpdateRecord("Conceptos")


def find_relation(sup, inf):
    """Makes the sup -> inf relation the current record; False when it does not exist."""
    app.SetElement(LOOKUP_SLOT, "Relaciones", "Relaciones.CodSup", '"' + sup + '"',
                   'Relaciones.CodInf=="' + inf + '"')
    return app.GetElement(LOOKUP_SLOT) == 0


def link(sup, inf, quantity):
    if not find_relation(sup, inf):
        app.InitRecord("Relaciones")
        app.SetField("Relaciones.CodSup", sup)
        app.SetField("Relaciones.CodInf", inf)
        app.InsertRecord("Relaciones")
        if not find_relation(sup, inf):
            raise Exception(f"Could not create relation {sup} -> {inf}")
    app.SetField("Relaciones.CanPres", quantity)
    app.UpdateRecord("Relaciones")


# --- input ------------------------------------------------------------------
if not JSON_PATH.exists():
    raise Exception(f"Input file not found: {JSON_PATH} (format at the top of this script).")
with open(JSON_PATH, encoding="utf-8") as fh:
    data = json.load(fh)

chapters = []
for ci, ch in enumerate(data.get("chapters", []), start=1):
    ccode = str(ch.get("code") or "%02d" % ci)
    partidas = []
    for pi, p in enumerate(ch.get("partidas", []), start=1):
        partidas.append((str(p.get("code") or "%s.%03d" % (ccode, pi)), str(p.get("summary") or ""),
                         str(p.get("unit") or ""), float(p.get("quantity") or 0)))
    chapters.append((ccode, str(ch.get("summary") or ""), partidas))
if not chapters:
    raise Exception(f"{JSON_PATH.name} has no chapters.")

# --- target obra ------------------------------------------------------------
project = str(app.Project() or "")
if not project:
    raise Exception("No obra is open in Presto: open one and run the script again.")
if EXPECTED_PROJECT and not project.lower().endswith(EXPECTED_PROJECT.lower()):
    raise Exception(f"The open obra is {project}, not {EXPECTED_PROJECT}: nothing was written.")
read_only = None
try:
    read_only = app.ReadOnly()   # ⏳ expected: non-zero when the obra was opened read-only
except Exception:
    pass
if read_only:
    raise Exception(f"{project} is open read-only: nothing was written.")

if app.FindEqual("Conceptos", "Conceptos.Nat", NAT_ROOT) != 0:
    raise Exception("The obra has no root concept (Nat 0).")
root = app.GetFieldStr("Conceptos.Código")

all_codes = []
for ccode, _, partidas in chapters:
    all_codes.append(ccode)
    all_codes.extend(p[0] for p in partidas)
existing = [c for c in all_codes if app.FindEqual("Conceptos", "Conceptos.Código", c) == 0]
if existing and not UPDATE_EXISTING:
    raise Exception(f"{len(existing)} codes already exist in the obra (first: {existing[:5]}). "
                    "Set UPDATE_EXISTING = True to overwrite them.")

n_partidas = sum(len(ps) for _, _, ps in chapters)
answer = MessageBox.Show(
    f"Create {len(chapters)} chapters and {n_partidas} partidas (no prices) under root '{root}' of\n\n"
    f"{project}?\n\n"
    + (f"{len(existing)} existing codes will be overwritten.\n\n" if existing else "")
    + "Changes are not saved: close without saving to undo, or use Presto's undo.",
    "PyNET - Create budget from JSON",
    MessageBoxButtons.YesNo,
    MessageBoxIcon.Question,
)
if answer != DialogResult.Yes:
    print("Cancelled: nothing was written.")
else:
    app.BeginRedo()
    try:
        if data.get("root_summary"):
            app.FindEqual("Conceptos", "Conceptos.Código", root)
            app.SetField("Conceptos.Resumen", str(data["root_summary"]))
            app.UpdateRecord("Conceptos")
        for ccode, csummary, partidas in chapters:
            ensure_concept(ccode, NAT_CHAPTER, csummary, "")
            link(root, ccode, 1)
            for pcode, psummary, unit, qty in partidas:
                ensure_concept(pcode, NAT_PARTIDA, psummary, unit)
                link(ccode, pcode, qty)
            print(f"{ccode} {csummary}: {len(partidas)} partidas")
    finally:
        app.EndRedo()     # always: a BeginRedo without EndRedo leaves Presto's undo blocked

    app.Recalculate(1)
    app.UpdateScreen()
    print(f"Created {len(chapters)} chapters and {n_partidas} partidas in {project}. Save the obra in Presto.")
    ia_Result = {"type": "PrestoBudget", "project": project, "root": root,
                 "chapters": len(chapters), "partidas": n_partidas, "updated_codes": existing}
