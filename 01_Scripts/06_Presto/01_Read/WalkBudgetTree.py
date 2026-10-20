# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

# The host injects the Presto COM application (Presto.App.18) as __presto__
try:
    app = __presto__
except NameError:
    raise Exception("__presto__ not found: run this script from PyNET for Presto (Complementos > PyNET).")

# ---------------------------------------------------------------------------
# Walk the budget tree of the open obra (root > chapters > sub-chapters >
# partidas) and print it indented: code, nature, unit, summary, quantity.
#
# Generalizes RIB's "Recorrer 4 niveles del árbol" sample to any depth.
# SetElement(slot, "Relaciones", key, mask, filter) opens the children of one
# concept on a numbered element slot and GetElement(slot) moves to the next
# one (0 while there are records). Each depth uses its OWN slot (depth 1 ->
# slot 1, depth 2 -> slot 2 ...): reusing a slot inside its own loop would
# restart the outer iteration. So the depth is limited by the slots (MAX_DEPTH).
#
# The filter skips the _SPC_ (Nat 219) and _CHG_ (Nat 170) system concepts,
# as RIB's sample does. By default it only descends into chapters (Nat 4);
# set DESCEND_INTO_DECOMPOSITION = True to also list what partidas and
# auxiliary prices are made of (labour, materials, machinery...).
#
# Read-only, changes nothing. Result rows in ia_Result.
#
# Verified on Presto 26.01 (2026-10-20, whole script): the SetElement/
# GetElement walk, GetFieldStr for codes, summaries and Conceptos.Ud,
# GetFieldNum for Nat, CanPres, Conceptos.Pres (unit price) and
# Relaciones.ImpPres (amount = CanPres x Pres).
# ---------------------------------------------------------------------------
MAX_DEPTH = 8                     # element slots 1..MAX_DEPTH (slot 9 is left free for lookups)
DESCEND_INTO_DECOMPOSITION = False
MAX_PRINTED_LINES = 400           # the tree goes to ia_Result whole; this only limits the prints
FILTER = "Conceptos.Nat!=219 && Conceptos.Nat!=170"

NAT_ROOT = 0
NAT_CHAPTER = 4


def num(field):
    """Numeric fields must be read with GetFieldNum: GetFieldStr returns None for them."""
    value = app.GetFieldNum(field)
    return float(value) if value is not None else None


def walk(sup, depth, rows):
    slot = depth
    app.SetElement(slot, "Relaciones", "Relaciones.CodSup", '"' + sup + '"', FILTER)
    while app.GetElement(slot) == 0:
        # Read everything of this record BEFORE descending: the recursion moves other records.
        code = app.GetFieldStr("Relaciones.CodInf")
        nat = int(num("Conceptos.Nat") or 0)
        rows.append({
            "type": "PrestoConcept",
            "depth": depth,
            "parent": sup,
            "code": code,
            "nat": nat,
            "unit": app.GetFieldStr("Conceptos.Ud") or None,          # ⏳
            "summary": app.GetFieldStr("Conceptos.Resumen") or None,
            "quantity": num("Relaciones.CanPres"),
            "price": num("Conceptos.Pres"),                           # ⏳ unit price
            "amount": num("Relaciones.ImpPres"),                      # ⏳ quantity x price
        })
        if depth < MAX_DEPTH and (nat == NAT_CHAPTER or DESCEND_INTO_DECOMPOSITION):
            walk(code, depth + 1, rows)


if not app.Project():
    raise Exception("No obra is open in Presto: open one and run the script again.")

if app.FindEqual("Conceptos", "Conceptos.Nat", NAT_ROOT) != 0:
    raise Exception("The obra has no root concept (Nat 0).")
root = app.GetFieldStr("Conceptos.Código")
root_summary = app.GetFieldStr("Conceptos.Resumen") or ""

rows = []
walk(root, 1, rows)

print(f"{root}  {root_summary}  ({len(rows)} concepts)")
for row in rows[:MAX_PRINTED_LINES]:
    qty = "" if row["quantity"] is None else f"{row['quantity']:g}"
    print(f"{'    ' * row['depth']}{row['code']}  [{row['nat']}]  {row['unit'] or ''}  "
          f"{row['summary'] or ''}  {qty}")
if len(rows) > MAX_PRINTED_LINES:
    print(f"... {len(rows) - MAX_PRINTED_LINES} more in ia_Result")

chapters = sum(1 for r in rows if r["nat"] == NAT_CHAPTER)
partidas = sum(1 for r in rows if r["nat"] == 5)
print(f"Chapters: {chapters} | Partidas: {partidas}")

ia_Result = {"root": root, "root_summary": root_summary, "rows": rows}
