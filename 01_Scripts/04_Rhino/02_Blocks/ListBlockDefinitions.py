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

blocks = []
for idef in doc.InstanceDefinitions:
    # The table keeps deleted slots; skip them
    if idef is None or idef.IsDeleted:
        continue
    blocks.append(
        {
            "type": "InstanceDefinition",
            "name": idef.Name,
            "objects": idef.ObjectCount,
            "instances": len(idef.GetReferences(0)),  # 0 = top-level references only
            "linked": bool(idef.SourceArchive),
            "update_type": str(idef.UpdateType),
            "description": idef.Description or "",
        }
    )

print(f"Found {len(blocks)} block definitions")
ia_Result = sorted(blocks, key=lambda b: b["name"])
