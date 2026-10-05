# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import clr

clr.AddReference("RhinoCommon")

from Rhino import RhinoDoc

# The host injects the active document as __rhinodoc__
try:
    doc = __rhinodoc__
except NameError:
    doc = RhinoDoc.ActiveDoc

# ---------------------------------------------------------------------------
# Write Attribute User Text (key/value pairs) to every object on a LAYER.
#
# Rhino has no "bind user text to a layer": this is a scan - walk the objects,
# match the layer full path, write the keys. Objects drawn later need a re-run
# (safe: keys that already hold the same value are skipped). Sublayers are not
# included - list each one explicitly.
#
# Change a Duplicate() of obj.Attributes and push it back with
# doc.Objects.ModifyAttributes() - that records undo and notifies the document.
# ---------------------------------------------------------------------------
LAYER_USER_TEXT = {
    "Structure::Columns": {"Site": "OBRA_001", "Code": "PYN-TEST"},
    "Structure::Beams": {"Site": "OBRA_001", "Code": "PYN-TEST"},
}

# Resolve layer full paths -> indices
layer_values = {}
for path, values in LAYER_USER_TEXT.items():
    index = doc.Layers.FindByFullPath(path, -1)  # -1 = not found
    if index < 0:
        print(f"Layer not found: {path}")
    else:
        layer_values[index] = values

updated = skipped = 0
sn = doc.BeginUndoRecord("PyNET: attach user text by layer")
try:
    for obj in doc.Objects:
        values = layer_values.get(obj.Attributes.LayerIndex)
        if not values:
            continue
        attrs = obj.Attributes.Duplicate()
        changed = False
        for key, value in values.items():
            if attrs.GetUserString(key) != value:
                attrs.SetUserString(key, value)
                changed = True
        if changed:
            doc.Objects.ModifyAttributes(obj, attrs, True)
            updated += 1
        else:
            skipped += 1
finally:
    doc.EndUndoRecord(sn)

print(f"Objects updated: {updated} | already up to date: {skipped}")

ia_Result = {
    "type": "UserTextAttachment",
    "layers": list(LAYER_USER_TEXT.keys()),
    "updated": updated,
    "alreadyUpToDate": skipped,
}
