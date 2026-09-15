# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import clr

clr.AddReference("AcMgd")
clr.AddReference("AcCoreMgd")
clr.AddReference("AcDbMgd")
clr.AddReference("AecBaseMgd")
clr.AddReference("AeccDbMgd")

from Autodesk.AutoCAD.ApplicationServices import Application as AcadApp
from Autodesk.AutoCAD.DatabaseServices import OpenMode
from Autodesk.AutoCAD.Geometry import Point2d, Point2dCollection
from Autodesk.Civil.ApplicationServices import CivilApplication
from Autodesk.Civil.DatabaseServices import SampleLineGroup, SampleLine

doc = AcadApp.DocumentManager.MdiActiveDocument
db = doc.Database
civil_doc = CivilApplication.ActiveDocument

# ---------------------------------------------------------------------------
# Cross-sections, step 1: sample lines at a fixed interval along an alignment.
#
# There is no "create sample lines at interval" call in the managed API (the
# UI wizard wraps it), so stations are walked manually and each sample line is
# built from two world points obtained with Alignment.PointLocation.
#
# TWO CALLING RULES - breaking either one ABORTS the Civil 3D process with no
# catchable Python exception (see docs/autocad-civil.md, "Hard crashes"):
#   1. Every write goes inside `with doc.LockDocument():`
#   2. SampleLineGroup.GetSectionSources() WRITES to the group despite the
#      `Get` prefix - the group must be open ForWrite before calling it.
# ---------------------------------------------------------------------------
ALIGNMENT_NAME = "PyNET_Carretera_Lamuela"
GROUP_NAME = "PyNET_Perfiles_Lamuela"
INTERVAL = 50.0          # metres between sample lines
LEFT_OFFSET = -15.0      # swath half-width, left of centreline
RIGHT_OFFSET = 15.0      # swath half-width, right of centreline


def find_alignment(t, name):
    for aid in civil_doc.GetAlignmentIds():
        a = t.GetObject(aid, OpenMode.ForRead)
        if a.Name == name:
            return a
    return None


def get_or_create_group(t, alignment, group_name):
    """Returns the sample line group's ObjectId, creating it if absent.
    SampleLineGroup.Create takes only (name, alignmentId) - sources are not
    passed in, they are auto-discovered and enabled separately below."""
    for gid in alignment.GetSampleLineGroupIds():
        if t.GetObject(gid, OpenMode.ForRead).Name == group_name:
            return gid
    return SampleLineGroup.Create(group_name, alignment.ObjectId)


def enable_all_sources(t, slg_id):
    """Turns on IsSampled for every available source (surfaces, corridors...).
    A freshly created group has them all OFF - sample lines would sample nothing.
    The group MUST be open ForWrite here: GetSectionSources() modifies it."""
    slg = t.GetObject(slg_id, OpenMode.ForWrite)
    enabled = []
    for src in slg.GetSectionSources():
        src.IsSampled = True
        enabled.append(src.SourceName)
    return enabled


def station_list(alignment, interval):
    stations = []
    st = alignment.StartingStation
    while st < alignment.EndingStation:
        stations.append(st)
        st += interval
    stations.append(alignment.EndingStation)
    return stations


def create_sample_lines(alignment, slg_id, stations):
    created, failed = 0, []
    for st in stations:
        try:
            e1, n1, _ = alignment.PointLocation(st, LEFT_OFFSET, 0.01, 0.0, 0.0, 0.0)
            e2, n2, _ = alignment.PointLocation(st, RIGHT_OFFSET, 0.01, 0.0, 0.0, 0.0)
            pts = Point2dCollection()
            pts.Add(Point2d(e1, n1))
            pts.Add(Point2d(e2, n2))
            SampleLine.Create("PK_{}+{:06.2f}".format(int(st // 1000), st % 1000), slg_id, pts)
            created += 1
            if created % 25 == 0:
                print("  ... {}/{} lineas creadas".format(created, len(stations)))
        except Exception as e:
            failed.append({"station": round(st, 2), "error": str(e).splitlines()[0]})
    return created, failed


with doc.LockDocument():
    t = db.TransactionManager.StartTransaction()
    try:
        alignment = find_alignment(t, ALIGNMENT_NAME)
        if alignment is None:
            raise ValueError("Alignment '{}' not found".format(ALIGNMENT_NAME))

        slg_id = get_or_create_group(t, alignment, GROUP_NAME)
        enabled = enable_all_sources(t, slg_id)
        print("Fuentes activadas: {}".format(enabled))

        stations = station_list(alignment, INTERVAL)
        created, failed = create_sample_lines(alignment, slg_id, stations)
        print("Lineas de muestreo creadas: {}/{} | fallidas: {}".format(
            created, len(stations), len(failed)))

        t.Commit()
        ia_Result = {
            "type": "SampleLineGroup",
            "alignment": ALIGNMENT_NAME,
            "group": GROUP_NAME,
            "sourcesEnabled": enabled,
            "interval": INTERVAL,
            "stationsPlanned": len(stations),
            "created": created,
            "failed": len(failed),
            "failures": failed[:5],
        }
    except Exception:
        t.Abort()
        raise
