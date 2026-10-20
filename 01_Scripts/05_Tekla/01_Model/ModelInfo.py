# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import clr

clr.AddReference("Tekla.Structures")
clr.AddReference("Tekla.Structures.Model")

from Tekla.Structures import TeklaStructuresInfo
from Tekla.Structures.Model import (
    Model, Beam, ContourPlate, PolyBeam, Part, BaseComponent, BoltGroup, BaseWeld, Reinforcement, Grid,
)

# The host injects the connected model as __teklamodel__
try:
    model = __teklamodel__
except NameError:
    model = Model()

# ---------------------------------------------------------------------------
# Summary of the open Tekla model: name, folder, Tekla version, project info,
# phases and how many objects of each kind it holds. Read-only.
#
# Counting walks GetAllObjects() with SelectInstances = False (identifiers and
# Python types only, no object data) and keeps only geometry kinds via an
# isinstance whitelist - GetAllObjects() also returns assemblies, control
# points, grid planes and the project organizer (TeklaApiPatterns Rule #1).
#
# Verified (TeklaApiPatterns / tekla.md): GetInfo().ModelName/.ModelPath,
# TeklaStructuresInfo.GetCurrentProgramVersion(), GetAllObjects() +
# SelectInstances = False + isinstance whitelist.
# Run on Tekla 2026 (2026-10-16, model with beams, columns, plates, bolts,
# welds): the whole script, including GetProjectInfo() fields and
# GetPhases() iteration.
# ---------------------------------------------------------------------------
# (label, type) - first match wins, so concrete part kinds go before Part
KINDS = [
    ("Beam / column", Beam),
    ("Contour plate", ContourPlate),
    ("Poly beam", PolyBeam),
    ("Other part", Part),
    ("Component / connection", BaseComponent),
    ("Bolt group", BoltGroup),
    ("Weld", BaseWeld),
    ("Reinforcement", Reinforcement),
    ("Grid", Grid),
]

if not model.GetConnectionStatus():
    raise Exception("Not connected to Tekla Structures.")

info = model.GetInfo()
version = TeklaStructuresInfo.GetCurrentProgramVersion()

# project info and phases
project = {}
try:
    pi = model.GetProjectInfo()
    project = {"name": pi.Name or None, "number": pi.ProjectNumber or None,
               "designer": pi.Designer or None, "builder": pi.Builder or None}
except Exception as ex:
    print(f"Project info not available: {ex}")

phases = []
try:
    for ph in model.GetPhases():
        phases.append({"number": ph.PhaseNumber, "name": ph.PhaseName})
except Exception as ex:
    print(f"Phases not available: {ex}")

counts = {label: 0 for label, _ in KINDS}
enumerator = model.GetModelObjectSelector().GetAllObjects()
enumerator.SelectInstances = False  # identity + type only: fast
while enumerator.MoveNext():
    obj = enumerator.Current
    if obj is None:
        continue
    for label, kind in KINDS:
        if isinstance(obj, kind):
            counts[label] += 1
            break

total = sum(counts.values())
print(f"Model: {info.ModelName}  ({info.ModelPath})")
print(f"Tekla Structures {version}")
if project.get("name"):
    print(f"Project: {project['name']}  #{project.get('number') or '-'}")
print(f"Phases: {len(phases)}")
print(f"Geometry objects: {total}")
for label, n in counts.items():
    if n:
        print(f"  {label}: {n}")

ia_Result = {
    "type": "TeklaModelInfo",
    "modelName": info.ModelName,
    "modelPath": info.ModelPath,
    "teklaVersion": version,
    "project": project,
    "phases": phases,
    "counts": [{"type": label, "count": n} for label, n in counts.items()],
    "totalGeometry": total,
}
