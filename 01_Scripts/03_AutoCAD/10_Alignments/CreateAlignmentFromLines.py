# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import clr

clr.AddReference("AcMgd")
clr.AddReference("AcCoreMgd")
clr.AddReference("AcDbMgd")
clr.AddReference("AecBaseMgd")
clr.AddReference("AeccDbMgd")

from Autodesk.AutoCAD.ApplicationServices import Application as AcadApp
from Autodesk.AutoCAD.DatabaseServices import OpenMode, BlockTableRecord, ObjectId
from Autodesk.Civil.ApplicationServices import CivilApplication
from Autodesk.Civil.DatabaseServices import Alignment, AlignmentType

doc = AcadApp.DocumentManager.MdiActiveDocument
db = doc.Database
civil_doc = CivilApplication.ActiveDocument

# ---------------------------------------------------------------------------
# Builds a Civil 3D Alignment on top of a chain of existing AutoCAD Line
# entities (e.g. a route/centerline drawn as plain geometry on a layer) -
# there is no direct "import objects as alignment" call in the managed API,
# so this walks the lines, orders them into a connected chain by matching
# endpoints, and adds each as a fixed-line alignment entity.
# ---------------------------------------------------------------------------
LAYER_NAME = "GIS_RI_LINEA"
ALIGNMENT_NAME = "PyNET_Carretera_Lamuela"
STYLE_NAME = "Proposed"
LABELSET_NAME = "Major and Minor only"


def collect_lines_on_layer(t, layer_name):
    """Reads every Line entity on the given layer from ModelSpace."""
    bt = t.GetObject(db.BlockTableId, OpenMode.ForRead)
    ms = t.GetObject(bt[BlockTableRecord.ModelSpace], OpenMode.ForRead)
    segs = []
    for oid in ms:
        e = t.GetObject(oid, OpenMode.ForRead)
        if type(e).__name__ == "Line" and e.Layer == layer_name:
            segs.append((e.StartPoint, e.EndPoint))
    return segs


def chain_segments(segs):
    """Orders disconnected (start, end) Point3d pairs into a single connected
    chain by matching endpoints (3-decimal tolerance). Assumes a simple open
    chain - no branching, no loops. Returns (ordered_segments, leftover_count);
    a non-zero leftover means the chain has a gap and stopped early."""
    def key(p):
        return (round(p.X, 3), round(p.Y, 3))

    remaining = list(segs)
    counts = {}
    for a, b in remaining:
        counts[key(a)] = counts.get(key(a), 0) + 1
        counts[key(b)] = counts.get(key(b), 0) + 1
    # a chain endpoint is a point that only one segment touches
    start_key = next(k for k, c in counts.items() if c == 1)

    ordered = []
    cur_key = start_key
    while remaining:
        for i, (a, b) in enumerate(remaining):
            if key(a) == cur_key:
                ordered.append((a, b))
                cur_key = key(b)
                remaining.pop(i)
                break
            if key(b) == cur_key:
                ordered.append((b, a))
                cur_key = key(a)
                remaining.pop(i)
                break
        else:
            break  # no segment continues the chain - stop, report the gap

    return ordered, len(remaining)


def find_style_id(t, style_collection, name):
    """AlignmentStyleCollection/LabelSetStyle collections yield ObjectId directly
    when iterated (not style objects) - each must be opened via the transaction
    to read .Name. Alignment.Create rejects ObjectId.Null for styleId/labelSetId,
    so a real id must be resolved by name first."""
    for oid in style_collection:
        if t.GetObject(oid, OpenMode.ForRead).Name == name:
            return oid
    return None


with doc.LockDocument():   # every write inside the document lock (autocad-civil.md, hard crash #1)
    t = db.TransactionManager.StartTransaction()
    try:
        segs = collect_lines_on_layer(t, LAYER_NAME)
        ordered, leftover = chain_segments(segs)
        print("Lines found on '{}': {} | chained: {} | leftover: {}".format(
            LAYER_NAME, len(segs), len(ordered), leftover))
        if leftover:
            print("  WARNING: the chain has a gap - check the leftover segments' layer/geometry.")

        lt = t.GetObject(db.LayerTableId, OpenMode.ForRead)
        layer0_id = lt["0"]

        style_id = find_style_id(t, civil_doc.Styles.AlignmentStyles, STYLE_NAME)
        labelset_id = find_style_id(t, civil_doc.Styles.LabelSetStyles.AlignmentLabelSetStyles, LABELSET_NAME)
        if style_id is None or labelset_id is None:
            raise ValueError("Alignment style '{}' or label set '{}' not found in this drawing".format(
                STYLE_NAME, LABELSET_NAME))

        align_id = Alignment.Create(civil_doc, ALIGNMENT_NAME, ObjectId.Null, layer0_id,
                                     style_id, labelset_id, AlignmentType.Centerline)
        alignment = t.GetObject(align_id, OpenMode.ForWrite)

        prev_id = -1
        for a, b in ordered:
            line = alignment.Entities.AddFixedLine(prev_id, a, b)
            prev_id = line.EntityId

        alignment.Update()
        print("Alignment created: {} | length: {} m | stations: {} - {}".format(
            alignment.Name, round(alignment.Length, 2), alignment.StartingStation, alignment.EndingStation))
        ia_Result = {
            "type": "Alignment",
            "name": alignment.Name,
            "length": round(alignment.Length, 2),
            "startStation": alignment.StartingStation,
            "endStation": alignment.EndingStation,
            "segmentsChained": len(ordered),
            "segmentsLeftover": leftover,
        }

        t.Commit()   # read everything above BEFORE committing
    except Exception:
        t.Abort()
        raise
