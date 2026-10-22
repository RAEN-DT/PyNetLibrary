# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import clr

clr.AddReference("Tekla.Structures.Model")

from System import Array, Type
from Tekla.Structures.Model import Model, Beam, ContourPlate, PolyBeam

# The host injects the connected model as __teklamodel__
try:
    model = __teklamodel__
except NameError:
    model = Model()

# ---------------------------------------------------------------------------
# Quantity takeoff by profile + material: number of parts, total length (m)
# and total weight (kg and t) per group, sorted by weight. Read-only.
#
# Profile and material are plain part properties; LENGTH (mm) and WEIGHT (kg)
# are report properties read once per part with a 0.0 default (double
# overload). A found = False value is counted as missing for that group -
# never summed as 0 - so an incomplete total is visible.
#
# Set GROUP_BY_NAME = True to split groups by part Name too (e.g. BEAM vs
# COLUMN with the same profile).
#
# Verified (TeklaApiPatterns): GetAllObjectsWithType(Type[]), Profile /
# Material / Name properties.
# Run on Tekla 2026 (2026-10-16, model with beams, columns, plates, bolts,
# welds): the whole script - GetReportProperty (found, value),
# LENGTH mm / WEIGHT kg (also checked by 06_Export/ExportTakeoffForPresto.py
# against 570 parts), missing values flagged.
# ---------------------------------------------------------------------------
PART_TYPES = [Beam, ContourPlate, PolyBeam]
GROUP_BY_NAME = False


def report(obj, name, default):
    """Report property value, or None when Tekla has none for this object."""
    found, value = obj.GetReportProperty(name, default)
    return value if found else None


if not model.GetConnectionStatus():
    raise Exception("Not connected to Tekla Structures.")

types = Array[Type]([clr.GetClrType(t) for t in PART_TYPES])
enumerator = model.GetModelObjectSelector().GetAllObjectsWithType(types)
total = enumerator.GetSize()
step = max(1, total // 10)
print(f"Measuring {total} parts...")

groups = {}
i = 0
while enumerator.MoveNext():
    part = enumerator.Current
    if part is None:
        continue
    i += 1
    if i % step == 0:
        print(f"  {i}/{total} ({100 * i // max(total, 1)}%)")

    key = (part.Profile.ProfileString, part.Material.MaterialString, part.Name if GROUP_BY_NAME else "")
    g = groups.setdefault(key, {"count": 0, "length_mm": 0.0, "weight_kg": 0.0,
                                "missingLength": 0, "missingWeight": 0})
    g["count"] += 1
    length = report(part, "LENGTH", 0.0)
    weight = report(part, "WEIGHT", 0.0)
    if length is None:
        g["missingLength"] += 1
    else:
        g["length_mm"] += length
    if weight is None:
        g["missingWeight"] += 1
    else:
        g["weight_kg"] += weight

rows = []
for (profile, material, name), g in groups.items():
    row = {
        "type": "ProfileQuantity",
        "profile": profile,
        "material": material,
        "count": g["count"],
        "length_m": round(g["length_mm"] / 1000.0, 3),
        "weight_kg": round(g["weight_kg"], 1),
        "weight_t": round(g["weight_kg"] / 1000.0, 3),
        "missingLength": g["missingLength"],
        "missingWeight": g["missingWeight"],
    }
    if GROUP_BY_NAME:
        row["name"] = name
    rows.append(row)
rows.sort(key=lambda r: -r["weight_kg"])

total_kg = sum(r["weight_kg"] for r in rows)
total_m = sum(r["length_m"] for r in rows)
missing = sum(r["missingWeight"] for r in rows)
print(f"{len(rows)} groups, {i} parts: {total_m:,.1f} m, {total_kg / 1000.0:,.2f} t")
for r in rows[:20]:
    label = f"{r['profile']} {r['material']}" + (f" {r['name']}" if GROUP_BY_NAME else "")
    print(f"  {label}: {r['count']} pcs, {r['length_m']:,.2f} m, {r['weight_kg']:,.1f} kg")
if len(rows) > 20:
    print(f"  ... and {len(rows) - 20} more groups")
if missing:
    print(f"WARNING: {missing} parts without WEIGHT - totals are incomplete")

ia_Result = {
    "type": "TeklaQuantitiesByProfile",
    "units": {"length": "m", "weight": "kg / t"},
    "parts": i,
    "totalLength_m": round(total_m, 3),
    "totalWeight_kg": round(total_kg, 1),
    "groups": rows,
}
