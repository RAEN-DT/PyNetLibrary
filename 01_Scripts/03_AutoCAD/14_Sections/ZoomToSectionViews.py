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
from Autodesk.Civil.ApplicationServices import CivilApplication

doc = AcadApp.DocumentManager.MdiActiveDocument
db = doc.Database
civil_doc = CivilApplication.ActiveDocument

# ---------------------------------------------------------------------------
# Cross-sections, step 3: zoom the screen onto the section views of a sample
# line group (step 2: CreateSectionViews.py).
#
# Section views land far from the model and are tiny next to a multi-km site,
# so they are easy to miss. Two rules for zooming to them:
#   1. Do NOT use ed.SetCurrentView(). Run through PyNET, the view is applied
#      and then overwritten a moment later by the viewport's own camera - the
#      zoom flashes and reverts (worse in a 3D/isometric view).
#      Queue AutoCAD commands instead: they run after the script ends.
#   2. Read GeometricExtents in a transaction AFTER the one that created the
#      views. Right after SectionViewGroups.Add every view is still stacked on
#      the insert point; Civil 3D spreads them into the grid on commit.
# ---------------------------------------------------------------------------
ALIGNMENT_NAME = "PyNET_Carretera_Lamuela"
GROUP_NAME = "PyNET_Perfiles_Lamuela"
MARGIN = 0.1             # 10 % of the extents on each side


def find_group(t, alignment_name, group_name):
    for aid in civil_doc.GetAlignmentIds():
        alignment = t.GetObject(aid, OpenMode.ForRead)
        if alignment.Name != alignment_name:
            continue
        for gid in alignment.GetSampleLineGroupIds():
            if t.GetObject(gid, OpenMode.ForRead).Name == group_name:
                return gid
    return None


# The group is opened ForWrite (its live wrapper collections write - see
# docs/autocad-civil.md, "Hard crashes"), and ForWrite needs the document lock
# even though nothing is committed (without it: eLockViolation, verified live).
with doc.LockDocument():
    t = db.TransactionManager.StartTransaction()
    try:
        slg_id = find_group(t, ALIGNMENT_NAME, GROUP_NAME)
        if slg_id is None:
            raise ValueError("Sample line group '{}' not found on '{}'".format(GROUP_NAME, ALIGNMENT_NAME))

        slg = t.GetObject(slg_id, OpenMode.ForWrite)
        minx = miny = 1e30
        maxx = maxy = -1e30
        views = 0
        for svg in slg.SectionViewGroups:
            ids = svg.GetSectionViewIds()
            for i in range(ids.Count):
                e = t.GetObject(ids[i], OpenMode.ForRead).GeometricExtents
                minx = min(minx, e.MinPoint.X); miny = min(miny, e.MinPoint.Y)
                maxx = max(maxx, e.MaxPoint.X); maxy = max(maxy, e.MaxPoint.Y)
                views += 1
    finally:
        t.Dispose()      # nothing to commit - only extents are read

if not views:
    raise ValueError("Group '{}' has no section views - run CreateSectionViews.py first".format(GROUP_NAME))

mx = (maxx - minx) * MARGIN
my = (maxy - miny) * MARGIN
x1, y1, x2, y2 = minx - mx, miny - my, maxx + mx, maxy + my

# -VIEW _TOP forces plan: section views are 2D drawings.
cmd = "_.UCS _W _.-VIEW _TOP _.ZOOM _W {:.3f},{:.3f} {:.3f},{:.3f} ".format(x1, y1, x2, y2)
doc.SendStringToExecute(cmd, True, False, False)
print("Zoom enviado sobre {} vistas de seccion".format(views))

ia_Result = {
    "type": "SectionViewZoom",
    "group": GROUP_NAME,
    "views": views,
    "window": [round(x1, 3), round(y1, 3), round(x2, 3), round(y2, 3)],
}
