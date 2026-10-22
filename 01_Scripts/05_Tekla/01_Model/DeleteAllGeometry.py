# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import clr

clr.AddReference("Tekla.Structures.Model")
clr.AddReference("System.Windows.Forms")

from Tekla.Structures.Model import (
    Model, BaseComponent, Part, BoltGroup, BaseWeld, Reinforcement, Grid, ControlPoint,
)
from System.Windows.Forms import MessageBox, MessageBoxButtons, MessageBoxIcon, DialogResult

# The host injects the connected model as __teklamodel__
try:
    model = __teklamodel__
except NameError:
    model = Model()

# ---------------------------------------------------------------------------
# Delete ALL the geometry of the open Tekla model: components/connections,
# parts, bolts, welds, reinforcement, grids and loose control points.
#
# Only geometry: GetAllObjects() also returns the project organizer
# (Site, Building, HierarchicDefinition/HierarchicObject), load groups and
# assemblies - those are left alone (assemblies go away with their parts).
#
# Asks for confirmation first, with the count per type. Order matters:
# components first (they own their parts), then parts (they own bolts/welds and
# their control points), then the rest. Objects already removed with their
# owner are skipped. Set DELETE_GRIDS = False to keep the grids.
#
# Changes are committed but NOT saved: close without saving to get the model
# back if needed.
# ---------------------------------------------------------------------------
DELETE_GRIDS = True

# (type, delete order)
GEOMETRY = [
    (BaseComponent, 0),
    (Part, 1),
    (BoltGroup, 2),
    (BaseWeld, 2),
    (Reinforcement, 2),
    (Grid, 3),
    (ControlPoint, 4),
]


def delete_order(obj):
    for kind, order in GEOMETRY:
        if isinstance(obj, kind):
            if kind is Grid and not DELETE_GRIDS:
                return None
            return order
    return None


if not model.GetConnectionStatus():
    raise Exception("Not connected to Tekla Structures.")

objects = []
enumerator = model.GetModelObjectSelector().GetAllObjects()
enumerator.SelectInstances = False  # faster: identifiers only, Delete() does not need the data
while enumerator.MoveNext():
    obj = enumerator.Current
    if obj is not None and delete_order(obj) is not None:
        objects.append(obj)

if not objects:
    print("The model has no geometry to delete.")
else:
    counts = {}
    for obj in objects:
        name = obj.GetType().Name
        counts[name] = counts.get(name, 0) + 1
    summary = "\n".join(f"  {name}: {n}" for name, n in sorted(counts.items()))

    answer = MessageBox.Show(
        f"Delete ALL the geometry of model '{model.GetInfo().ModelName}'?\n\n{summary}\n\n"
        "Changes are not saved: close without saving to undo.",
        "PyNET - Delete all geometry",
        MessageBoxButtons.YesNo,
        MessageBoxIcon.Warning,
    )

    if answer != DialogResult.Yes:
        print("Cancelled: nothing was deleted.")
    else:
        deleted = skipped = 0
        for obj in sorted(objects, key=delete_order):
            # False when it was already removed together with its owner
            if obj.Delete():
                deleted += 1
            else:
                skipped += 1

        model.CommitChanges("PyNET: delete all geometry")
        print(f"Deleted {deleted} objects ({skipped} already removed with their owner).")
