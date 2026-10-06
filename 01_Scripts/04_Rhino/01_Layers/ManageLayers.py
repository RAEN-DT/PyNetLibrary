# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import clr

clr.AddReference("RhinoCommon")

from Rhino import RhinoDoc
from Rhino.DocObjects import Layer
from System.Drawing import Color

# The host injects the active document as __rhinodoc__
try:
    doc = __rhinodoc__
except NameError:
    doc = RhinoDoc.ActiveDoc

LAYER_NAME = "PYNET_EXAMPLE"

# Each block is one undo record, so Ctrl+Z reverts it (Rhino's equivalent
# of an AutoCAD transaction).

# --- CREATE + MODIFY ---
sn = doc.BeginUndoRecord("PyNET: create/modify layer")
try:
    index = doc.Layers.FindByFullPath(LAYER_NAME, -1)  # -1 = not found
    if index < 0:
        layer = Layer()
        layer.Name = LAYER_NAME
        layer.Color = Color.FromArgb(0, 128, 0)  # green
        index = doc.Layers.Add(layer)
        print(f"Created layer: {LAYER_NAME} (index {index})")
    else:
        print(f"Layer already exists: {LAYER_NAME}")

    # Layers from the table are live: change properties, then CommitChanges()
    layer = doc.Layers.FindIndex(index)
    layer.IsVisible = True   # turn on
    layer.IsLocked = False   # unlock
    layer.Color = Color.FromArgb(0, 0, 255)  # blue
    layer.CommitChanges()
    layer = doc.Layers.FindIndex(index)
    print(f"Modified layer: visible={layer.IsVisible}, locked={layer.IsLocked}, color=({layer.Color.R}, {layer.Color.G}, {layer.Color.B})")
finally:
    doc.EndUndoRecord(sn)

# --- DELETE (separate undo record) ---
# The current layer and layers holding objects cannot be deleted.
sn = doc.BeginUndoRecord("PyNET: delete layer")
try:
    index = doc.Layers.FindByFullPath(LAYER_NAME, -1)
    if index >= 0:
        if doc.Layers.Delete(index, True):
            print(f"Deleted layer: {LAYER_NAME}")
        else:
            print(f"Could not delete layer: {LAYER_NAME} (current or not empty)")
finally:
    doc.EndUndoRecord(sn)

doc.Views.Redraw()
print("Done")
