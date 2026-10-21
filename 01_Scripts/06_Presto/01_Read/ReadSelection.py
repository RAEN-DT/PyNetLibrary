# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

# The host injects the Presto COM application (Presto.App.18) as __presto__
try:
    app = __presto__
except NameError:
    raise Exception("__presto__ not found: run this script from PyNET for Presto (Complementos > PyNET).")

# ---------------------------------------------------------------------------
# List the records the user selected in the active Presto window: code,
# nature, unit and summary of each selected concept.
#
# Read-only, changes nothing.
#
# Verified on Presto 26.01 (2026-10-20, 2 rows selected in the Presupuesto
# window): GetSelection(1, "Conceptos") moves to the FIRST selected record
# and returns 0, GetSelection(0, "Conceptos") to the next one, non-zero when
# there are no more (the Find*/GetElement convention). The loop also stops
# on a repeated code and after MAX_RECORDS.
# ---------------------------------------------------------------------------
TABLE = "Conceptos"
MAX_RECORDS = 5000

if not app.Project():
    raise Exception("No obra is open in Presto: open one and run the script again.")

selected = []
previous = None
rc = app.GetSelection(1, TABLE)
print(f"GetSelection(1, '{TABLE}') returned {rc!r}")
while rc == 0 and len(selected) < MAX_RECORDS:
    code = app.GetFieldStr("Conceptos.Código")
    if code == previous:
        break
    previous = code
    selected.append({
        "type": "PrestoConcept",
        "code": code,
        "nat": int(app.GetFieldNum("Conceptos.Nat") or 0),
        "unit": app.GetFieldStr("Conceptos.Ud") or None,
        "summary": app.GetFieldStr("Conceptos.Resumen") or None,
    })
    rc = app.GetSelection(0, TABLE)

if not selected:
    print("Nothing selected (or GetSelection works differently - see the note at the top).")
else:
    print(f"{len(selected)} selected:")
    for s in selected:
        print(f"  {s['code']}  [{s['nat']}]  {s['unit'] or ''}  {s['summary'] or ''}")

ia_Result = selected
