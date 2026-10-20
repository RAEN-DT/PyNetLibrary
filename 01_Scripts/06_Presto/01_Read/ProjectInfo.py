# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

# The host injects the Presto COM application (Presto.App.18) as __presto__
try:
    app = __presto__
except NameError:
    raise Exception("__presto__ not found: run this script from PyNET for Presto (Complementos > PyNET).")

# ---------------------------------------------------------------------------
# Summary of the obra open in Presto: Presto version, obra path, root concept
# (code and summary), budget and target-cost amounts, read-only status.
#
# Read-only, changes nothing.
#
# Verified on Presto 26.01 (2026-10-20, whole script): VersionStr, Project,
# FindEqual on the root (Conceptos.Nat == 0), GetFieldStr,
# EvalNum("Conceptos.Pres"/"Conceptos.Obj"), VersionNum (26),
# SubVersionNum (1), ReadOnly (0), ProjectLanguage (0).
#
# EvalNum rounds to 2 decimals: fine for amounts, not for unit prices or
# quantities with more decimals (use GetFieldNum for those).
# ---------------------------------------------------------------------------
NAT_ROOT = 0


def optional(call):
    """Runs an unverified API call; None when Presto rejects it or the member does not exist."""
    try:
        return call()
    except Exception as ex:  # MissingMemberException (wrong name) or COMException (Presto error)
        print(f"  (not available: {str(ex).splitlines()[0]})")
        return None


project = str(app.Project() or "")
if not project:
    raise Exception("No obra is open in Presto: open one and run the script again.")

info = {
    "type": "PrestoProject",
    "version": str(app.VersionStr()),
    "project": project,
    "version_num": optional(lambda: app.VersionNum()),        # ⏳
    "subversion_num": optional(lambda: app.SubVersionNum()),  # ⏳
    "read_only": optional(lambda: app.ReadOnly()),            # ⏳ int in the COM API (0 = writable, expected)
    "language": optional(lambda: app.ProjectLanguage()),     # ⏳
    "root_code": None,
    "root_summary": None,
    "budget": None,
    "target_cost": None,
}

# The root is the only concept with nature 0. Find* returns 0 when found and
# makes that record the current one for GetField*/EvalNum.
if app.FindEqual("Conceptos", "Conceptos.Nat", NAT_ROOT) == 0:
    info["root_code"] = app.GetFieldStr("Conceptos.Código")
    info["root_summary"] = app.GetFieldStr("Conceptos.Resumen")
    info["budget"] = app.EvalNum("Conceptos.Pres")       # budget amount (PEM) of the whole obra
    info["target_cost"] = app.EvalNum("Conceptos.Obj")   # target-cost amount
else:
    print("Warning: no root concept (Nat 0) found.")

print(f"{info['version']}")
print(f"Obra:        {info['project']}")
print(f"Root:        {info['root_code']} - {info['root_summary'] or ''}")
print(f"Budget:      {info['budget']}")
print(f"Target cost: {info['target_cost']}")
print(f"Read-only:   {info['read_only']}")

ia_Result = info
