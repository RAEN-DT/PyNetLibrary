# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import clr

clr.AddReference("RhinoCommon")

from Rhino import RhinoDoc
from Rhino.DocObjects import ObjectType
from Rhino.Geometry import BoundingBox

# The host injects the active document as __rhinodoc__
try:
    doc = __rhinodoc__
except NameError:
    doc = RhinoDoc.ActiveDoc

USER_TEXT_KEY = "Site"
USER_TEXT_VALUE = "OBRA_001"  # wildcards allowed: "OBRA_*"

# Search attribute user text only (not geometry user text), case-insensitive
found = doc.Objects.FindByUserString(USER_TEXT_KEY, USER_TEXT_VALUE, False, False, True, ObjectType.AnyObject)
found = list(found) if found else []

print(f"Found {len(found)} object(s) with {USER_TEXT_KEY} = '{USER_TEXT_VALUE}'")
for obj in found:
    print(f"  {obj.ObjectType} — id {obj.Id}")

if found:
    # Select the found objects and zoom the active view to them
    doc.Objects.UnselectAll()
    bbox = BoundingBox.Empty
    for obj in found:
        obj.Select(True)
        bbox.Union(obj.Geometry.GetBoundingBox(True))

    view = doc.Views.ActiveView
    if view is not None and bbox.IsValid:
        view.ActiveViewport.ZoomBoundingBox(bbox)
    doc.Views.Redraw()

ia_Result = [{"type": str(o.ObjectType), "id": str(o.Id)} for o in found]
