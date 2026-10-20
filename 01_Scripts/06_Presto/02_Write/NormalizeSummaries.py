# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import re

import clr

clr.AddReference("System.Windows.Forms")

from System.Windows.Forms import MessageBox, MessageBoxButtons, MessageBoxIcon, DialogResult

# The host injects the Presto COM application (Presto.App.18) as __presto__
try:
    app = __presto__
except NameError:
    raise Exception("__presto__ not found: run this script from PyNET for Presto (Complementos > PyNET).")

# ---------------------------------------------------------------------------
# Bulk field update: rewrite the summary (Conceptos.Resumen) of every
# partida in sentence case - first letter upper case, the rest lower case -
# keeping words with digits ("140mm", "HA-25") and the acronyms in
# KEEP_WORDS as they are. Python version of the example in RIB's VBS tutorial.
#
# DRY_RUN = True (default) only lists the changes in the output and in
# ia_Result. Set it to False to write them, after a confirmation dialog, as
# a single Presto undo step.
#
# Two passes on purpose: first read all the summaries, then write each one
# with FindEqual + SetField + UpdateRecord (the verified write pattern), so
# the writes never move the cursor of the loop that is reading.
#
# Verified on Presto 26.01 (2026-10-20): the read loop (SetElement on the
# Conceptos table with mask '"*"' and filter "Conceptos.Nat==5" read the 10
# partidas) and the DRY_RUN = False path (36 summaries rewritten, a second
# dry run found 0 left). Proper names without digits are lowered too
# ("Revit" -> "revit"): add them to KEEP_WORDS. Changes are NOT saved: save
# the obra in Presto.
# ---------------------------------------------------------------------------
DRY_RUN = True
NATURE_FILTER = "Conceptos.Nat==5"            # partidas; any Presto expression on Conceptos
KEEP_WORDS = {"UNE", "PVC", "EPS", "XPS", "CTE", "BIM", "HVAC", "LED", "PE", "PP"}
MAX_PRINTED = 50


def sentence_case(text):
    words = text.lower().split(" ")
    original = text.split(" ")
    out = []
    for word, orig in zip(words, original):
        if re.search(r"\d", orig) or orig.strip(".,;:()").upper() in KEEP_WORDS:
            out.append(orig)
        else:
            out.append(word)
    result = " ".join(out)
    return result[:1].upper() + result[1:]


if not app.Project():
    raise Exception("No obra is open in Presto: open one and run the script again.")

changes = []
scanned = 0
app.SetElement(1, "Conceptos", "Conceptos.Código", '"*"', NATURE_FILTER)
while app.GetElement(1) == 0:
    scanned += 1
    code = app.GetFieldStr("Conceptos.Código")
    old = app.GetFieldStr("Conceptos.Resumen") or ""
    new = sentence_case(old)
    if new != old:
        changes.append({"type": "PrestoRename", "code": code, "old": old, "new": new})

print(f"{scanned} concepts read ({NATURE_FILTER}), {len(changes)} summaries to change{' (dry run)' if DRY_RUN else ''}:")
for c in changes[:MAX_PRINTED]:
    print(f"  {c['code']}: {c['old']}  ->  {c['new']}")
if len(changes) > MAX_PRINTED:
    print(f"  ... {len(changes) - MAX_PRINTED} more in ia_Result")

if changes and not DRY_RUN:
    answer = MessageBox.Show(
        f"Rewrite {len(changes)} summaries in\n\n{app.Project()}?\n\n"
        "Changes are not saved: close without saving to undo, or use Presto's undo.",
        "PyNET - Normalize summaries",
        MessageBoxButtons.YesNo,
        MessageBoxIcon.Question,
    )
    if answer != DialogResult.Yes:
        print("Cancelled: nothing was written.")
    else:
        app.BeginRedo()
        try:
            for c in changes:
                if app.FindEqual("Conceptos", "Conceptos.Código", c["code"]) == 0:
                    app.SetField("Conceptos.Resumen", c["new"])
                    app.UpdateRecord("Conceptos")
        finally:
            app.EndRedo()
        app.UpdateScreen()
        print(f"Rewrote {len(changes)} summaries. Save the obra in Presto.")

ia_Result = changes
