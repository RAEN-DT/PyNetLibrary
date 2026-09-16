# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import clr

clr.AddReference("AcMgd")
clr.AddReference("AcCoreMgd")
clr.AddReference("AcDbMgd")
clr.AddReference("AecBaseMgd")
clr.AddReference("AecPropDataMgd")

from Autodesk.AutoCAD.ApplicationServices import Application as AcadApp
from Autodesk.AutoCAD.DatabaseServices import OpenMode, BlockTableRecord
from Autodesk.AutoCAD.Runtime import Exception as AcadException, ErrorStatus
from Autodesk.Aec.PropertyData.DatabaseServices import PropertyDataServices

doc = AcadApp.DocumentManager.MdiActiveDocument
db = doc.Database

# ---------------------------------------------------------------------------
# Attach existing PropertySetDefinitions to entities by LAYER.
# (create the definitions first: CreateAndUsePropertySet.py)
#
# Civil 3D / AutoCAD has no native "bind a property set to a layer" - the only
# built-in filter is by object type (AppliesToFilter). Layer-driven attachment
# is a scan we implement: walk ModelSpace, read entity.Layer, attach. It is not
# automatic - geometry drawn later needs a re-run (safe: already attached sets
# are skipped). Attachment is per property set, never per single property.
#
# GOTCHA - PropertyDataServices.GetPropertySet() does NOT return a null id when
# the set is missing: it throws eKeyNotFound. Checking ExtensionDictionary.IsNull
# first is not enough - attaching the first of two sets creates the dictionary,
# and the check for the second one then throws. See has_property_set() below.
# ---------------------------------------------------------------------------
NOD_PSET_KEY = "AEC_PROPERTY_SET_DEFS"

LAYER_PSETS = {
    "C-RED-SAN-POZO": ["PYNET_TEST_PSET"],
    "C-VIAL-EJE": ["PYNET_TEST_PSET"],
}


def get_pset_def_ids(t, names):
    nod = t.GetObject(db.NamedObjectsDictionaryId, OpenMode.ForRead)
    if not nod.Contains(NOD_PSET_KEY):
        raise ValueError("The drawing has no property set definitions")
    pset_dict = t.GetObject(nod.GetAt(NOD_PSET_KEY), OpenMode.ForRead)
    missing = [n for n in names if not pset_dict.Contains(n)]
    if missing:
        raise ValueError("Property set definitions not found: {}".format(missing))
    return {n: pset_dict.GetAt(n) for n in names}


def has_property_set(entity, pset_def_id):
    """True if the set is already attached - safe for entities without it."""
    if entity.ExtensionDictionary.IsNull:
        return False
    try:
        return not PropertyDataServices.GetPropertySet(entity, pset_def_id).IsNull
    except AcadException as ex:
        if ex.ErrorStatus == ErrorStatus.KeyNotFound:
            return False
        raise


with doc.LockDocument():
    t = db.TransactionManager.StartTransaction()
    try:
        all_names = sorted({n for names in LAYER_PSETS.values() for n in names})
        def_ids = get_pset_def_ids(t, all_names)

        bt = t.GetObject(db.BlockTableId, OpenMode.ForRead)
        ms = t.GetObject(bt[BlockTableRecord.ModelSpace], OpenMode.ForRead)

        attached = skipped = 0
        for oid in ms:
            entity = t.GetObject(oid, OpenMode.ForRead)
            for name in LAYER_PSETS.get(entity.Layer, []):
                if has_property_set(entity, def_ids[name]):
                    skipped += 1
                    continue
                if not entity.IsWriteEnabled:
                    entity.UpgradeOpen()
                PropertyDataServices.AddPropertySet(entity, def_ids[name])
                attached += 1

        t.Commit()
    except Exception:
        t.Abort()
        raise

print("Conjuntos asignados: {} | ya estaban: {}".format(attached, skipped))

ia_Result = {
    "type": "PropertySetAttachment",
    "layers": list(LAYER_PSETS.keys()),
    "attached": attached,
    "alreadyAttached": skipped,
}
