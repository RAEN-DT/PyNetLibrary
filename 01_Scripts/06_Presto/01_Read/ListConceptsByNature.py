# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

# The host injects the Presto COM application (Presto.App.18) as __presto__
try:
    app = __presto__
except NameError:
    raise Exception("__presto__ not found: run this script from PyNET for Presto (Complementos > PyNET).")

# ---------------------------------------------------------------------------
# Count every concept of the open obra by nature (Conceptos.Nat): root,
# chapters, partidas, labour, materials, machinery, entities, system concepts.
# Unlike WalkBudgetTree it scans the Conceptos TABLE, so it also finds
# concepts that are not used in the tree (e.g. loose prices from a database).
#
# Read-only, changes nothing.
#
# Verified on Presto 26.01 (2026-10-20, whole script). Two ways to scan the
# table, both give the same full count (34 concepts on a 10-partida obra):
#   "find"    - FindFirst/FindNext("Conceptos", "Conceptos.Código"): 0 while
#               a record was found, and it becomes the current record.
#   "element" - SetElement(1, "Conceptos", "Conceptos.Código", '"*"', "") +
#               GetElement(1): the form RIB's VBS tutorial uses on Conceptos.
# (On Mediciones FindFirst/FindNext do NOT move - see PrestoApiPatterns.)
# The loop still stops on a repeated code and after MAX_RECORDS.
# ---------------------------------------------------------------------------
METHOD = "find"            # "find" or "element"
MAX_RECORDS = 200000
SAMPLE_PER_NATURE = 5      # codes kept per nature in ia_Result

NATURES = {
    0: "Root", 4: "Chapter", 5: "Partida", 6: "Labour", 7: "Material", 8: "Machinery",
    9: "Other", 51: "BCF topic", 170: "_CHG_", 219: "_SPC_", 255: "System",   # 255 = code "###"
}


def nature_name(nat):
    if nat in NATURES:
        return NATURES[nat]
    return "Entity" if nat >= 100 else f"Nat {nat}"   # entities (agents, suppliers...) are 100+


def scan_find():
    rc = app.FindFirst("Conceptos", "Conceptos.Código")
    while rc == 0:
        yield
        rc = app.FindNext("Conceptos", "Conceptos.Código")


def scan_element():
    app.SetElement(1, "Conceptos", "Conceptos.Código", '"*"', "")
    while app.GetElement(1) == 0:
        yield


if not app.Project():
    raise Exception("No obra is open in Presto: open one and run the script again.")

counts = {}
samples = {}
seen = 0
previous = None
for _ in (scan_find() if METHOD == "find" else scan_element()):
    code = app.GetFieldStr("Conceptos.Código")
    if code == previous:
        print(f"Stopped: '{code}' returned twice (the scan does not advance).")
        break
    previous = code
    nat = int(app.GetFieldNum("Conceptos.Nat") or 0)   # numeric field: GetFieldNum, not GetFieldStr
    counts[nat] = counts.get(nat, 0) + 1
    samples.setdefault(nat, [])
    if len(samples[nat]) < SAMPLE_PER_NATURE:
        samples[nat].append(code)
    seen += 1
    if seen >= MAX_RECORDS:
        print(f"Stopped after MAX_RECORDS = {MAX_RECORDS}.")
        break
    if seen % 5000 == 0:
        print(f"  {seen} concepts...")

result = [
    {"type": "PrestoNature", "nat": nat, "name": nature_name(nat), "count": n, "sample": samples[nat]}
    for nat, n in sorted(counts.items())
]

print(f"{seen} concepts in {app.Project()} (method: {METHOD})")
for r in result:
    print(f"  {r['nat']:>4}  {r['name']:<10} {r['count']}")

ia_Result = result
