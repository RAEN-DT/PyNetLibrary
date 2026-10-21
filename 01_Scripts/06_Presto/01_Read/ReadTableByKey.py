# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

# The host injects the Presto COM application (Presto.App.18) as __presto__
try:
    app = __presto__
except NameError:
    raise Exception("__presto__ not found: run this script from PyNET for Presto (Complementos > PyNET).")

# ---------------------------------------------------------------------------
# Read a whole table (or the records with one key value) in ONE COM call with
# ReadTableByKey / ReadTableByKeyValue, instead of one call per field and
# record. On big obras that is by far the fastest way to read data through
# the cross-process COM channel.
#
# Read-only, changes nothing. Rows in ia_Result as dicts {field: value}.
#
# Verified on Presto 26.01 (2026-10-20):
#   ReadTableByKey(fmt, table, key, fields, order_by, descending)
#   ReadTableByKeyValue(fmt, table, key, value, fields, order_by, descending)
# - fields are separated by SEMICOLONS ("Conceptos.Código;Conceptos.Nat").
#   Commas, "|", tabs or spaces return None with no error - so does a wrong
#   field name. The table prefix is optional ("Código;Nat" works too).
# - fmt 0 = flat JSON, 1 = indented JSON:
#     {"fields": [{"name": "Código", "type": "A24"}, ...], "retcode": <rows>,
#      "val": [{"row": [{"data": "01.01"}, {"data": 5}, ...]}, ...]}
#   numbers come typed (Nat 5, Pres 2.4); field types A<n> text, C byte, N number.
#   fmt 2 = text: header "Código;A24;Nat;C" then one tab-separated line per
#   record (avoid it if a text field may hold tabs or line breaks).
# - order_by: any field ("" = key order), descending True/False.
# - ReadTableByKeyValue filters on the key: e.g. key "Conceptos.Nat", value 5
#   = every partida; key "Relaciones.CodSup", value "EAV" = children of EAV.
# Reads the whole table: system concepts (###, _SPC_, _CHG_) and entities
# are included - filter them out in Python if needed.
# ---------------------------------------------------------------------------
import json

TABLE = "Conceptos"
KEY = "Conceptos.Código"
FIELDS = ["Conceptos.Código", "Conceptos.Nat", "Conceptos.Ud", "Conceptos.Resumen", "Conceptos.Pres"]
KEY_VALUE = None             # e.g. 5 with KEY = "Conceptos.Nat" -> only partidas; None = whole table
ORDER_BY = ""                # "" = key order
DESCENDING = False
MAX_PRINTED_LINES = 60


def read_table(table, key, fields, key_value=None, order_by="", descending=False):
    """Rows of a Presto table as a list of dicts, in one COM call."""
    field_list = ";".join(fields)
    if key_value is None:
        text = app.ReadTableByKey(0, table, key, field_list, order_by, descending)
    else:
        text = app.ReadTableByKeyValue(0, table, key, key_value, field_list, order_by, descending)
    if not text:
        raise Exception(f"ReadTableByKey returned nothing: check the table, key and field names ({field_list}).")
    data = json.loads(text)
    names = [f["name"] for f in data["fields"]]
    return [dict(zip(names, (cell["data"] for cell in rec["row"]))) for rec in data.get("val", [])]


if not app.Project():
    raise Exception("No obra is open in Presto: open one and run the script again.")

rows = read_table(TABLE, KEY, FIELDS, KEY_VALUE, ORDER_BY, DESCENDING)

print(f"{len(rows)} records from {TABLE} ({app.Project()})")
for row in rows[:MAX_PRINTED_LINES]:
    print("  " + " | ".join("" if v is None else str(v) for v in row.values()))
if len(rows) > MAX_PRINTED_LINES:
    print(f"  ... {len(rows) - MAX_PRINTED_LINES} more in ia_Result")

ia_Result = rows
