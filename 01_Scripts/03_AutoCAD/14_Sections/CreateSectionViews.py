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
from Autodesk.AutoCAD.Geometry import Point3d
from Autodesk.Civil.ApplicationServices import CivilApplication
from Autodesk.Civil.DatabaseServices import (
    SectionViewGroupCreationRangeOptions,
    SectionViewGroupCreationPlacementOptions,
    SectionDisplayOptionCollection,
)

doc = AcadApp.DocumentManager.MdiActiveDocument
db = doc.Database
civil_doc = CivilApplication.ActiveDocument

# ---------------------------------------------------------------------------
# Cross-sections, step 2: draw the section views for an existing sample line
# group (step 1: CreateSampleLinesAtInterval.py).
#
# The three options objects `SectionViewGroups.Add` needs are NOT discoverable
# from the stubs - two of them have no parameterless constructor. Resolved by
# reflection against the live API:
#     SectionViewGroupCreationRangeOptions(ObjectId sampleLineGroupId)
#     SectionDisplayOptionCollection(ObjectId sampleLineGroupOid)
#     SectionViewGroupCreationPlacementOptions()      <- parameterless
#
# Same two calling rules as step 1 - breaking either ABORTS Civil 3D with no
# catchable exception (docs/autocad-civil.md, "Hard crashes"):
#   1. everything inside `with doc.LockDocument():`
#   2. the SampleLineGroup open ForWrite (its live wrapper collections write)
# ---------------------------------------------------------------------------
ALIGNMENT_NAME = "PyNET_Carretera_Lamuela"
GROUP_NAME = "PyNET_Perfiles_Lamuela"
START_STATION = 0.0
END_STATION = 500.0
INSERT_POINT = Point3d(640000.0, 4602000.0, 0.0)   # clear of the model geometry
VIEW_STYLE = "Road Section"
BAND_SET_STYLE = "_No Bands"


def find_style_id(t, collection, name):
    """Style collections iterate yielding ObjectId, not style objects."""
    for oid in collection:
        if t.GetObject(oid, OpenMode.ForRead).Name == name:
            return oid
    return None


with doc.LockDocument():
    t = db.TransactionManager.StartTransaction()
    try:
        alignment = None
        for aid in civil_doc.GetAlignmentIds():
            a = t.GetObject(aid, OpenMode.ForRead)
            if a.Name == ALIGNMENT_NAME:
                alignment = a
                break
        if alignment is None:
            raise ValueError("Alignment '{}' not found".format(ALIGNMENT_NAME))

        slg_id = None
        for gid in alignment.GetSampleLineGroupIds():
            if t.GetObject(gid, OpenMode.ForRead).Name == GROUP_NAME:
                slg_id = gid
                break
        if slg_id is None:
            raise ValueError("Sample line group '{}' not found - run CreateSampleLinesAtInterval.py first".format(GROUP_NAME))

        slg = t.GetObject(slg_id, OpenMode.ForWrite)

        range_opts = SectionViewGroupCreationRangeOptions(slg_id)
        placement = SectionViewGroupCreationPlacementOptions()
        placement.UseDraftPlacement()   # grid in model space; no layout template needed

        # Each source defaults to Draw=False - nothing would be plotted otherwise.
        display = SectionDisplayOptionCollection(slg_id)
        drawn = []
        for opt in display:
            opt.Draw = True
            drawn.append(opt.SourceName)
        print("Fuentes a dibujar: {}".format(drawn))

        style_id = find_style_id(t, civil_doc.Styles.SectionViewStyles, VIEW_STYLE)
        band_id = find_style_id(t, civil_doc.Styles.SectionViewBandSetStyles, BAND_SET_STYLE)
        if style_id is None or band_id is None:
            raise ValueError("Section view style '{}' or band set '{}' not found".format(
                VIEW_STYLE, BAND_SET_STYLE))

        svg = slg.SectionViewGroups.Add(INSERT_POINT, START_STATION, END_STATION,
                                         range_opts, placement, display, style_id, band_id)
        view_count = svg.GetSectionViewIds().Count
        print("Grupo de vistas '{}' | vistas creadas: {} (PK {} - {})".format(
            svg.Name, view_count, START_STATION, END_STATION))

        t.Commit()
        ia_Result = {
            "type": "SectionViewGroup",
            "name": svg.Name,
            "views": view_count,
            "startStation": START_STATION,
            "endStation": END_STATION,
            "sourcesDrawn": drawn,
        }
    except Exception:
        t.Abort()
        raise
