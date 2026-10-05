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
# Rhino's equivalent of AutoCAD property sets is Attribute User Text: free
# key/value string pairs stored on each object's attributes (Properties panel
# > Attribute User Text). There is no schema - every value is a string.
# ---------------------------------------------------------------------------

result = []
for obj in doc.Objects:
    attrs = obj.Attributes
    if attrs.UserStringCount == 0:
        continue
    strings = attrs.GetUserStrings()  # System.Collections.Specialized.NameValueCollection
    user_text = {key: strings[key] for key in strings.AllKeys}
    result.append(
        {
            "id": str(obj.Id),
            "type": str(obj.ObjectType),
            "name": attrs.Name or "",
            "layer": doc.Layers.FindIndex(attrs.LayerIndex).FullPath,
            "user_text": user_text,
        }
    )

print(f"Found {len(result)} objects with user text")
ia_Result = result
