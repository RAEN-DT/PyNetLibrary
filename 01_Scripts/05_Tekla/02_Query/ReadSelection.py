# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import clr

clr.AddReference("Tekla.Structures.Model")

from Tekla.Structures.Model import Model, Part, Beam, BoltGroup, BaseComponent
from Tekla.Structures.Model.UI import ModelObjectSelector as UISelector   # the user's selection

# The host injects the connected model as __teklamodel__
try:
    model = __teklamodel__
except NameError:
    model = Model()

# ---------------------------------------------------------------------------
# Read what the user has selected in Tekla: one entry per object with its
# type, GUID and the key properties of its kind - parts (name, class,
# profile, material, LENGTH, WEIGHT, assembly position), bolt groups
# (standard, size) and components (name, number). Read-only.
#
# Two classes are called ModelObjectSelector: the UI one returns the user's
# selection, the Model one (model.GetModelObjectSelector()) the whole model.
# Alias the UI one on import.
#
# Verified (TeklaApiPatterns): UI ModelObjectSelector().GetSelectedObjects(),
# part properties, Identifier.GUID.
# Run on Tekla 2026 (2026-10-16, model with beams, columns, plates, bolts,
# welds): part properties, GetReportProperty (found, value),
# ASSEMBLY_POS through part.GetAssembly().
# ⏳ Not reached yet (no bolt group / component selected): BoltGroup.
# BoltStandard/BoltSize, BaseComponent.Name/Number.
# ---------------------------------------------------------------------------
MAX_PRINTED = 50   # per-object lines printed; ia_Result holds all of them


def report(obj, name, default):
    """Report property value, or None when Tekla has none for this object."""
    if obj is None:
        return None
    found, value = obj.GetReportProperty(name, default)
    return value if found else None


if not model.GetConnectionStatus():
    raise Exception("Not connected to Tekla Structures.")

items = []
selected = UISelector().GetSelectedObjects()
while selected.MoveNext():
    obj = selected.Current
    if obj is None:
        continue
    entry = {"type": obj.GetType().Name, "guid": str(obj.Identifier.GUID)}

    if isinstance(obj, Part):
        if isinstance(obj, Beam):
            entry["type"] = "Column" if str(obj.Type) == "COLUMN" else "Beam"
        entry.update({
            "name": obj.Name,
            "class": obj.Class,
            "profile": obj.Profile.ProfileString,
            "material": obj.Material.MaterialString,
            "length_mm": report(obj, "LENGTH", 0.0),
            "weight_kg": report(obj, "WEIGHT", 0.0),
            "assemblyPos": report(obj.GetAssembly(), "ASSEMBLY_POS", ""),
        })
    elif isinstance(obj, BoltGroup):
        entry.update({"boltStandard": obj.BoltStandard, "boltSize_mm": obj.BoltSize})
    elif isinstance(obj, BaseComponent):
        entry.update({"name": obj.Name, "number": obj.Number})
    items.append(entry)

if not items:
    print("Nothing is selected in Tekla: select some objects and run again.")
else:
    counts = {}
    for e in items:
        counts[e["type"]] = counts.get(e["type"], 0) + 1
    print(f"Selected {len(items)} objects: " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    for e in items[:MAX_PRINTED]:
        details = ", ".join(f"{k}={v}" for k, v in e.items() if k not in ("type", "guid") and v not in (None, ""))
        print(f"  {e['type']} {e['guid']}  {details}")
    if len(items) > MAX_PRINTED:
        print(f"  ... and {len(items) - MAX_PRINTED} more")

ia_Result = items
