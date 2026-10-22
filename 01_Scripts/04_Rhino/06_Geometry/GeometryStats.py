# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import clr

clr.AddReference("RhinoCommon")

from Rhino import RhinoDoc
from Rhino.DocObjects import ObjectType
from Rhino.Geometry import Extrusion, Mesh, AreaMassProperties, VolumeMassProperties

# The host injects the active document as __rhinodoc__
try:
    doc = __rhinodoc__
except NameError:
    doc = RhinoDoc.ActiveDoc

units = str(doc.ModelUnitSystem)
objects = list(doc.Objects.FindByObjectType(ObjectType.Brep | ObjectType.Extrusion | ObjectType.Mesh) or [])
step = max(1, len(objects) // 10)

stats = []
for i, obj in enumerate(objects, 1):
    geom = obj.Geometry
    if isinstance(geom, Extrusion):
        geom = geom.ToBrep(True)  # mass properties are computed on the Brep form

    # Volume only makes sense for closed geometry
    closed = geom.IsClosed if isinstance(geom, Mesh) else geom.IsSolid
    amp = AreaMassProperties.Compute(geom)
    vmp = VolumeMassProperties.Compute(geom) if closed else None
    bbox = geom.GetBoundingBox(True)

    stats.append(
        {
            "id": str(obj.Id),
            "type": str(obj.ObjectType),
            "layer": doc.Layers.FindIndex(obj.Attributes.LayerIndex).FullPath,
            "closed": closed,
            "area": round(amp.Area, 3) if amp else None,
            "volume": round(vmp.Volume, 3) if vmp else None,
            "bbox": {
                "min": [round(bbox.Min.X, 3), round(bbox.Min.Y, 3), round(bbox.Min.Z, 3)],
                "max": [round(bbox.Max.X, 3), round(bbox.Max.Y, 3), round(bbox.Max.Z, 3)],
            },
        }
    )
    if i % step == 0:
        print(f"  {i}/{len(objects)} objects measured")

totals = {}
for s in stats:
    t = totals.setdefault(s["type"], {"count": 0, "closed": 0, "area": 0.0, "volume": 0.0})
    t["count"] += 1
    t["closed"] += 1 if s["closed"] else 0
    t["area"] += s["area"] or 0.0
    t["volume"] += s["volume"] or 0.0

print(f"Measured {len(stats)} objects (units: {units})")
for name, t in totals.items():
    print(f"{name}: {t['count']} objects ({t['closed']} closed)")
    print(f"  Area: {t['area']:.3f}  Volume (closed only): {t['volume']:.3f}")

ia_Result = stats
