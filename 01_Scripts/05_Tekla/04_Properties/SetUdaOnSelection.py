# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import clr

clr.AddReference("Tekla.Structures.Model")
clr.AddReference("System.Windows.Forms")

from Tekla.Structures.Model import Model, Part
from Tekla.Structures.Model.UI import ModelObjectSelector as UISelector   # the user's selection
from System import Int32
from System.Windows.Forms import MessageBox, MessageBoxButtons, MessageBoxIcon, DialogResult

# The host injects the connected model as __teklamodel__
try:
    model = __teklamodel__
except NameError:
    model = Model()

# ---------------------------------------------------------------------------
# Write user-defined attributes (UDAs) to the parts the user has selected.
#
# UDAS maps attribute name -> value. The Python type of the value picks the
# overload, as for report properties: str for text, float for doubles, int
# for integers (wrapped in System.Int32 by typed(): a plain Python int picks
# the Double overload - verified for GetReportProperty). Parts that already hold the value are skipped (read first with
# GetUserProperty and a default of the same type). Asks for confirmation,
# checks the bool of every SetUserProperty, CommitChanges() once at the end.
#
# The UDA must be defined in the environment's objects.inp to appear in the
# part's dialog; an undefined name can still be stored, but nobody sees it.
# Report properties (LENGTH, WEIGHT, ...) are computed and cannot be written.
#
# Verified (TeklaApiPatterns): UI selection, one CommitChanges().
# Run on Tekla 2026 (2026-10-16, model with beams, columns, plates, bolts,
# welds): the whole script - GetUserProperty returns (found,
# value) in pythonnet, SetUserProperty -> bool with string and Int32 values.
# ⏳ The float (Double) overload of SetUserProperty is not exercised.
#
# Changes are committed but NOT saved: save the model (Ctrl+S) to keep them.
# ---------------------------------------------------------------------------
UDAS = {
    "comment": "Checked by PyNET",
    # "USER_FIELD_1": "Phase A",
}


def typed(value):
    """.NET-typed value: a Python int would pick the Double overload, so wrap it in Int32."""
    return Int32(value) if isinstance(value, int) and not isinstance(value, bool) else value


def current(obj, name, value):
    """Current UDA value (same type as `value`), or None when not set."""
    found, existing = obj.GetUserProperty(name, typed(type(value)()))
    return existing if found else None


if not model.GetConnectionStatus():
    raise Exception("Not connected to Tekla Structures.")

parts = []
selected = UISelector().GetSelectedObjects()
while selected.MoveNext():
    obj = selected.Current
    if isinstance(obj, Part):
        parts.append(obj)

if not parts:
    raise Exception("Select one or more parts in Tekla and run again.")

summary = "\n".join(f"  {k} = {v!r}" for k, v in UDAS.items())
answer = MessageBox.Show(
    f"Write these attributes to {len(parts)} selected parts?\n\n{summary}",
    "PyNET - Set UDAs on selection",
    MessageBoxButtons.YesNo,
    MessageBoxIcon.Question,
)

updated = unchanged = 0
failed = []
if answer != DialogResult.Yes:
    print("Cancelled: nothing was written.")
else:
    step = max(1, len(parts) // 10)
    for i, part in enumerate(parts, 1):
        if len(parts) > 50 and i % step == 0:
            print(f"  {i}/{len(parts)}")
        changed = False
        for name, value in UDAS.items():
            if current(part, name, value) == value:
                continue
            if part.SetUserProperty(name, typed(value)):
                changed = True
            else:
                failed.append({"guid": str(part.Identifier.GUID), "uda": name})
        if changed:
            updated += 1
        else:
            unchanged += 1

    model.CommitChanges("PyNET: set UDAs on selection")   # once, at the end
    print(f"Parts updated: {updated} | already up to date: {unchanged}")
    if failed:
        print(f"Tekla rejected {len(failed)} writes: {failed[:10]}")
    print("Save the model (Ctrl+S) to keep the changes.")

ia_Result = {
    "type": "TeklaSetUda",
    "udas": UDAS,
    "selectedParts": len(parts),
    "updated": updated,
    "alreadyUpToDate": unchanged,
    "failed": failed,
}
