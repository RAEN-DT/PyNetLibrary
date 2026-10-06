# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import clr

clr.AddReference("RhinoCommon")

from Rhino import RhinoDoc
from Rhino.DocObjects import ObjectEnumeratorSettings

# The host injects the active document as __rhinodoc__
try:
    doc = __rhinodoc__
except NameError:
    doc = RhinoDoc.ActiveDoc

# Model objects: normal, locked and hidden; no block-definition geometry, no lights
settings = ObjectEnumeratorSettings()
settings.NormalObjects = True
settings.LockedObjects = True
settings.HiddenObjects = True
settings.IdefObjects = False
settings.IncludeLights = False

by_type = {}
by_layer = {}
for obj in doc.Objects.GetObjectList(settings):
    type_name = str(obj.ObjectType)
    layer_path = doc.Layers.FindIndex(obj.Attributes.LayerIndex).FullPath
    by_type[type_name] = by_type.get(type_name, 0) + 1
    key = (layer_path, type_name)
    by_layer[key] = by_layer.get(key, 0) + 1

result = sorted([{"type": k, "count": v} for k, v in by_type.items()], key=lambda x: -x["count"])
layers = sorted(
    [{"type": t, "layer": l, "count": v} for (l, t), v in by_layer.items()],
    key=lambda x: (x["layer"], x["type"]),
)

total = sum(r["count"] for r in result)
layer_count = len({r["layer"] for r in layers})
print(f"Found {total} objects across {len(result)} types and {layer_count} layers")
for r in result:
    print(f"  {r['type']}: {r['count']}")

ia_Result = {"by_type": result, "by_layer": layers}
