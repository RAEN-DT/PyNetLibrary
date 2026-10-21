# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import clr
import math

clr.AddReference("RhinoCommon")

from Rhino import RhinoDoc
from Rhino.Geometry import Point3d, Vector3d, Transform

# The host injects the active document as __rhinodoc__
try:
    doc = __rhinodoc__
except NameError:
    doc = RhinoDoc.ActiveDoc

# --- Config ---
BLOCK_NAME = "Column"  # must exist in the document
POSITION = Point3d(100.0, 200.0, 0.0)  # model units
ROTATION_DEG = 90.0  # around the world Z axis
SCALE = 1.0
LAYER = "Structure::Columns"  # optional: full layer path; "" = current layer

idef = doc.InstanceDefinitions.Find(BLOCK_NAME, True)

if idef is None:
    print(f"Block '{BLOCK_NAME}' not found in document")
else:
    # Scale and rotate about the block base point, then move to POSITION
    xform = Transform.Multiply(
        Transform.Translation(Vector3d(POSITION)),
        Transform.Multiply(
            Transform.Rotation(math.radians(ROTATION_DEG), Vector3d.ZAxis, Point3d.Origin),
            Transform.Scale(Point3d.Origin, SCALE),
        ),
    )

    attrs = doc.CreateDefaultAttributes()
    if LAYER:
        layer_index = doc.Layers.FindByFullPath(LAYER, -1)
        if layer_index >= 0:
            attrs.LayerIndex = layer_index
        else:
            print(f"Layer '{LAYER}' not found, using the current layer")

    sn = doc.BeginUndoRecord("PyNET: insert block")
    try:
        obj_id = doc.Objects.AddInstanceObject(idef.Index, xform, attrs)
    finally:
        doc.EndUndoRecord(sn)
    doc.Views.Redraw()

    print(f"Inserted '{BLOCK_NAME}' at {POSITION} rotated {ROTATION_DEG}° — id: {obj_id}")
    ia_Result = {"type": "InstanceObject", "block": BLOCK_NAME, "id": str(obj_id)}
