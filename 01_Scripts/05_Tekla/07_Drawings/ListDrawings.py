# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import clr

clr.AddReference("Tekla.Structures.Drawing")

from Tekla.Structures.Drawing import DrawingHandler

# ---------------------------------------------------------------------------
# List the drawings of the open Tekla model (Document manager content): type
# (GA, assembly, single-part, cast-unit, multi), mark, name, titles, status
# flags (issued, locked, frozen, ready for issue), up-to-date status and
# dates, with a count per type and status. Read-only.
#
# Drawings live in Tekla.Structures.Drawing (whitelisted): DrawingHandler()
# connects on its own - no __teklamodel__ needed. The drawing type is the
# .NET class name (GADrawing, AssemblyDrawing, SinglePartDrawing,
# CastUnitDrawing, MultiDrawing).
#
# Run on Tekla 2026 (2026-10-16) on a model WITHOUT drawings:
# DrawingHandler().GetConnectionStatus() and GetDrawings() (empty) work.
# ⏳ Not reached yet (no drawings): Drawing.Mark/Name/Title1/IsIssued/
# IsLocked/IsFrozen/IsReadyForIssue/UpToDateStatus/CreationDate/ModificationDate.
# ---------------------------------------------------------------------------
MAX_PRINTED = 30


def text(value):
    return str(value) if value not in (None, "") else None


handler = DrawingHandler()
if not handler.GetConnectionStatus():
    raise Exception("Not connected to Tekla Structures drawings.")

drawings = []
e = handler.GetDrawings()
while e.MoveNext():
    d = e.Current
    if d is None:
        continue
    drawings.append({
        "type": d.GetType().Name,
        "mark": text(d.Mark),
        "name": text(d.Name),
        "title1": text(d.Title1),
        "issued": bool(d.IsIssued),
        "locked": bool(d.IsLocked),
        "frozen": bool(d.IsFrozen),
        "readyForIssue": bool(d.IsReadyForIssue),
        "upToDate": text(d.UpToDateStatus),
        "created": text(d.CreationDate),
        "modified": text(d.ModificationDate),
    })

by_type, by_status = {}, {}
for d in drawings:
    by_type[d["type"]] = by_type.get(d["type"], 0) + 1
    by_status[d["upToDate"]] = by_status.get(d["upToDate"], 0) + 1

print(f"{len(drawings)} drawings")
for k, v in sorted(by_type.items()):
    print(f"  {k}: {v}")
print("Up-to-date status: " + ", ".join(f"{k} {v}" for k, v in sorted(by_status.items(), key=lambda kv: str(kv[0]))))
issued = sum(d["issued"] for d in drawings)
print(f"Issued: {issued} | locked: {sum(d['locked'] for d in drawings)} | frozen: {sum(d['frozen'] for d in drawings)}")
for d in drawings[:MAX_PRINTED]:
    print(f"  [{d['type']}] {d['mark'] or '-'}  {d['name'] or ''}  {d['upToDate'] or ''}")
if len(drawings) > MAX_PRINTED:
    print(f"  ... and {len(drawings) - MAX_PRINTED} more")

ia_Result = {
    "type": "TeklaDrawingList",
    "count": len(drawings),
    "byType": [{"type": k, "count": v} for k, v in sorted(by_type.items())],
    "drawings": drawings,
}
