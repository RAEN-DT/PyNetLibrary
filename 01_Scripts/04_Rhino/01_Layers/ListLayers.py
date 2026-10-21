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

current_index = doc.Layers.CurrentLayerIndex

layers = []
for layer in doc.Layers:
    if layer.IsDeleted:
        continue
    objs = doc.Objects.FindByLayer(layer)  # None when the layer is empty
    layers.append(
        {
            "type": "Layer",
            "name": layer.Name,
            "full_path": layer.FullPath,
            "color": "#{:02X}{:02X}{:02X}".format(layer.Color.R, layer.Color.G, layer.Color.B),
            "visible": layer.IsVisible,
            "locked": layer.IsLocked,
            "current": layer.Index == current_index,
            "objects": len(objs) if objs else 0,
        }
    )

print(f"Found {len(layers)} layers")
ia_Result = layers
