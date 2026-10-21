# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import clr

clr.AddReference("Tekla.Structures.Model")

from System.Collections import ArrayList
from Tekla.Structures.Model import Model
from Tekla.Structures.Model.UI import ModelObjectSelector as UISelector   # the user's selection

# The host injects the connected model as __teklamodel__
try:
    model = __teklamodel__
except NameError:
    model = Model()

# ---------------------------------------------------------------------------
# Find objects by GUID and select them in Tekla, so the user sees them
# highlighted (e.g. GUIDs coming from an IFC/BCF issue, a clash report or an
# Excel export of ListParts / ExportPartsToExcel).
#
# GUIDs are the stable identity (TeklaApiPatterns Rule #3): Identifier.ID is
# local to the model. Lookup: model.GetIdentifierByGUID(str) -> Identifier,
# then model.SelectModelObject(identifier) -> the object (None / invalid when
# the GUID is not in the model). The UI selection takes an ArrayList - build
# it and .Add(), never pass a Python list. Selection only, no model change.
#
# Verified (TeklaApiPatterns): Identifier.GUID as identity, ArrayList.Add().
# Run on Tekla 2026 (2026-10-16, model with beams, columns, plates, bolts,
# welds): the whole script - GetIdentifierByGUID ->
# SelectModelObject (an unknown GUID is reported as missing), UI
# ModelObjectSelector().Select(ArrayList, False).
# ---------------------------------------------------------------------------
GUIDS = [
    # "ID4D3B8D1F-0000-0001-3133-353037303433",
    # "4d3b8d1f-0000-0001-3133-353037303433",
]


def find(guid):
    """The model object with this GUID, or None."""
    ident = model.GetIdentifierByGUID(guid.strip())
    if ident is None or not ident.IsValid():
        return None
    obj = model.SelectModelObject(ident)
    if obj is None or not obj.Identifier.IsValid():
        return None
    return obj


if not model.GetConnectionStatus():
    raise Exception("Not connected to Tekla Structures.")
if not GUIDS:
    raise Exception("Fill GUIDS at the top of the script with the GUIDs to select.")

found, missing = [], []
to_select = ArrayList()
for guid in GUIDS:
    obj = find(guid)
    if obj is None:
        missing.append(guid)
    else:
        to_select.Add(obj)
        found.append({"type": obj.GetType().Name, "guid": str(obj.Identifier.GUID)})

if to_select.Count:
    ok = UISelector().Select(to_select, False)   # False = no dimensions shown
    print(f"Selected {to_select.Count} of {len(GUIDS)} objects" + ("" if ok else " (Tekla rejected the selection)"))
else:
    print("None of the GUIDs is in this model.")
for guid in missing:
    print(f"  Not found: {guid}")

ia_Result = {"type": "TeklaSelectByGuid", "found": found, "missing": missing}
