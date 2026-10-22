# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

from pathlib import Path

from System import Environment

# The host injects the Presto COM application (Presto.App.18) as __presto__
try:
    app = __presto__
except NameError:
    raise Exception("__presto__ not found: run this script from PyNET for Presto (Complementos > PyNET).")

# ---------------------------------------------------------------------------
# Export the open obra to FIEBDC-3 (.bc3), the Spanish standard exchange
# format for budgets, to OUTPUT_DIR as "<obra>.bc3".
#
# Read-only on the obra (it only writes the .bc3 file).
#
# Verified on Presto 26.01 (2026-10-20): ExportFIEBDC(full path) returns 0,
# shows no dialog and writes FIEBDC-3/2024 in ANSI (cp1252): ~V ~L ~K ~X,
# ~C concepts (chapters with "#", root "0##"), ~D decompositions with the
# quantities, ~E entities. With the default options it writes NO ~M
# measurement lines (an obra with 570 lines gave none) - the call has no
# options argument. The script still checks that the file exists and is
# newer than before the call, whatever the return value.
# The inverse is ImportFIEBDC(archivo) ⏳ - it writes into the open obra, so
# confirm with the user before using it.
# ---------------------------------------------------------------------------
OUTPUT_DIR = Path(Environment.GetFolderPath(Environment.SpecialFolder.Desktop))
OVERWRITE = False

project = str(app.Project() or "")
if not project:
    raise Exception("No obra is open in Presto: open one and run the script again.")

out = OUTPUT_DIR / f"{Path(project).stem}.bc3"
if out.exists() and not OVERWRITE:
    raise Exception(f"{out} already exists: set OVERWRITE = True or pick another OUTPUT_DIR.")
before = out.stat().st_mtime if out.exists() else None

rc = app.ExportFIEBDC(str(out))
print(f"ExportFIEBDC returned {rc!r}")

if not out.exists() or (before is not None and out.stat().st_mtime <= before):
    raise Exception(f"Presto did not write {out} (return value {rc!r}).")

size_kb = out.stat().st_size / 1024
print(f"Exported {project} to {out} ({size_kb:.1f} KB)")
ia_Result = {"type": "PrestoExport", "file": str(out), "format": "FIEBDC-3", "return": rc if rc is None or isinstance(rc, (int, float, str)) else str(rc), "size_kb": round(size_kb, 1)}
