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
# Part inventory: every Beam (beams and columns), ContourPlate and PolyBeam
# with its type, GUID, name, class, profile, material, LENGTH (mm) and
# WEIGHT (kg). Read-only.
#
# The selector is asked for the part types only (GetAllObjectsWithType with a
# Type[] - never GetAllObjects(), TeklaApiPatterns Rule #1). Profile, material,
# name and class are plain properties (cheap); LENGTH and WEIGHT are report
# properties: the default's type picks the overload (0.0 = double) and a
# found = False result is reported as None (missing), never as 0.
#
# Verified (TeklaApiPatterns / tekla.md): GetAllObjectsWithType(Type[]),
# Profile.ProfileString / Material.MaterialString / Name / Class,
# Identifier.GUID.
# Run on Tekla 2026 (2026-10-16, model with beams, columns, plates, bolts,
# welds): the whole script - GetReportProperty returns
# (found, value) in pythonnet (missing -> None), LENGTH mm / WEIGHT kg,
# enumerator.GetSize(), str(beam.Type).
# ---------------------------------------------------------------------------
PART_TYPES = [Beam, ContourPlate, PolyBeam]
MAX_RESULT_ROWS = 5000   # cap for ia_Result; the printed summary covers all parts


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
print(f"Reading {total} parts...")

rows = []
by_type = {}
missing_length = missing_weight = 0
i = 0
while enumerator.MoveNext():
    part = enumerator.Current
    if part is None:
        continue
    i += 1
    if i % step == 0:
        print(f"  {i}/{total} ({100 * i // max(total, 1)}%)")

    kind = part.GetType().Name
    if isinstance(part, Beam):
        kind = "Column" if str(part.Type) == "COLUMN" else "Beam"
    by_type[kind] = by_type.get(kind, 0) + 1

    length = report(part, "LENGTH", 0.0)
    weight = report(part, "WEIGHT", 0.0)
    missing_length += length is None
    missing_weight += weight is None

    rows.append({
        "type": kind,
        "guid": str(part.Identifier.GUID),
        "name": part.Name,
        "class": part.Class,
        "profile": part.Profile.ProfileString,
        "material": part.Material.MaterialString,
        "length_mm": round(length, 1) if length is not None else None,
        "weight_kg": round(weight, 2) if weight is not None else None,
    })

print(f"Found {len(rows)} parts")
for kind, n in sorted(by_type.items()):
    print(f"  {kind}: {n}")
if missing_length or missing_weight:
    print(f"Missing report values: LENGTH {missing_length}, WEIGHT {missing_weight}")

ia_Result = {
    "type": "TeklaPartInventory",
    "count": len(rows),
    "byType": [{"type": k, "count": v} for k, v in sorted(by_type.items())],
    "units": {"length": "mm", "weight": "kg"},
    "parts": rows[:MAX_RESULT_ROWS],
    "truncated": len(rows) > MAX_RESULT_ROWS,
}
