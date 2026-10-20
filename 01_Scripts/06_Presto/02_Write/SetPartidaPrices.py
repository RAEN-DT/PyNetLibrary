# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import csv
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
# Set the unit price of partidas from a CSV file (code;price) or from the
# PRICES dict below - e.g. to price the budget created by
# CreateBudgetFromJson.py.
#
# CSV: one "code;price" per line, a header line is skipped, decimal comma or
# point both accepted ("125,40" or "125.40").
#
# Skipped and reported: codes not in the obra, the root and chapters (their
# price is the sum of their children) and concepts that have a
# decomposition (Presto computes their price from it, a typed price would be
# overwritten by the recalculation).
#
# Verified on Presto 26.01 (2026-10-20, whole script): 36 partida prices from
# a CSV with decimal commas (CYPE Generador de Precios references) written to
# Conceptos.Pres, read back after Recalculate with 0 mismatches. Use
# PRICE_FIELD = "Conceptos.Obj" for the target-cost price (⏳).
# The script reads every price back after Recalculate and reports mismatches.
#
# The record pattern (FindEqual + SetField + UpdateRecord inside
# BeginRedo/EndRedo) is verified. Changes are NOT saved: save the obra in
# Presto, or close without saving to discard them.
# ---------------------------------------------------------------------------
CSV_PATH = Path(Environment.GetFolderPath(Environment.SpecialFolder.Desktop)) / "PrestoPrices.csv"
DELIMITER = ";"
PRICES = {}                    # e.g. {"01.001": 32.5} - when not empty, used instead of the CSV
PRICE_FIELD = "Conceptos.Pres"
EXPECTED_PROJECT = ""          # e.g. "MyProject.Presto"
FILTER = "Conceptos.Nat!=219 && Conceptos.Nat!=170"
LOOKUP_SLOT = 9

NAT_ROOT = 0
NAT_CHAPTER = 4


def parse_number(text):
    text = str(text).strip().replace(" ", "")
    if "," in text and "." in text:          # 1.234,56 -> 1234.56
        text = text.replace(".", "")
    return float(text.replace(",", "."))


def read_csv(path):
    if not path.exists():
        raise Exception(f"Input file not found: {path} (one 'code{DELIMITER}price' per line).")
    prices = {}
    with open(path, encoding="utf-8-sig", newline="") as fh:
        for row in csv.reader(fh, delimiter=DELIMITER):
            if len(row) < 2 or not row[0].strip():
                continue
            try:
                prices[row[0].strip()] = parse_number(row[1])
            except ValueError:
                continue                     # header or text line
    return prices


def has_children(code):
    app.SetElement(LOOKUP_SLOT, "Relaciones", "Relaciones.CodSup", '"' + code + '"', FILTER)
    return app.GetElement(LOOKUP_SLOT) == 0


prices = dict(PRICES) if PRICES else read_csv(CSV_PATH)
if not prices:
    raise Exception("No prices to set.")

project = str(app.Project() or "")
if not project:
    raise Exception("No obra is open in Presto: open one and run the script again.")
if EXPECTED_PROJECT and not project.lower().endswith(EXPECTED_PROJECT.lower()):
    raise Exception(f"The open obra is {project}, not {EXPECTED_PROJECT}: nothing was written.")

plan, skipped = [], []
for code, price in prices.items():
    if app.FindEqual("Conceptos", "Conceptos.Código", code) != 0:
        skipped.append({"type": "PrestoSkip", "code": code, "reason": "not in the obra"})
        continue
    nat = int(app.GetFieldNum("Conceptos.Nat") or 0)
    if nat in (NAT_ROOT, NAT_CHAPTER):
        skipped.append({"type": "PrestoSkip", "code": code, "reason": "root/chapter: price is the sum of its children"})
    elif has_children(code):
        skipped.append({"type": "PrestoSkip", "code": code, "reason": "has a decomposition: price is computed"})
    else:
        plan.append((code, price))

for s in skipped:
    print(f"  skipped {s['code']}: {s['reason']}")
if not plan:
    raise Exception("None of the codes can take a price: nothing was written.")

answer = MessageBox.Show(
    f"Set {PRICE_FIELD} of {len(plan)} concepts in\n\n{project}?\n\n"
    f"{len(skipped)} codes skipped (see the output).\n\n"
    "Changes are not saved: close without saving to undo, or use Presto's undo.",
    "PyNET - Set partida prices",
    MessageBoxButtons.YesNo,
    MessageBoxIcon.Question,
)
if answer != DialogResult.Yes:
    print("Cancelled: nothing was written.")
else:
    app.BeginRedo()
    try:
        for code, price in plan:
            app.FindEqual("Conceptos", "Conceptos.Código", code)   # make it the current record
            app.SetField(PRICE_FIELD, price)
            app.UpdateRecord("Conceptos")
    finally:
        app.EndRedo()
    app.Recalculate(1)
    app.UpdateScreen()

    # Read back: a mismatch means the field is not writable this way (or Presto recomputed it)
    mismatches = []
    for code, price in plan:
        app.FindEqual("Conceptos", "Conceptos.Código", code)
        stored = app.GetFieldNum(PRICE_FIELD)
        if stored is None or abs(float(stored) - price) > 0.005:
            mismatches.append({"type": "PrestoMismatch", "code": code, "wanted": price, "stored": stored})

    print(f"Set {len(plan)} prices, {len(mismatches)} mismatches. Save the obra in Presto.")
    for m in mismatches[:20]:
        print(f"  {m['code']}: wanted {m['wanted']}, Presto has {m['stored']}")
    if app.FindEqual("Conceptos", "Conceptos.Nat", NAT_ROOT) == 0:
        print(f"Budget now: {app.EvalNum('Conceptos.Pres')}")
    ia_Result = {"set": len(plan), "skipped": skipped, "mismatches": mismatches}
