# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

# Fills in the enum members that GenerateStubs.py used to drop.
#
# An enum has neither properties nor declared methods, so the old generator left its body as "..."
# and its members were invisible from the stubs: SubassemblyLogicalNameType.Surface or
# SpiralType.Clothoid could only be found by reflection against a running host. GenerateStubs.py is
# now fixed, but regenerating the whole corpus is slow and overwrites everything -- this patches the
# existing stub files in place, surgically, from the live API.
#
# Run from the host via send_command_by_path. Re-run 00_utils/IndexStubs.py afterwards: the line
# ranges in _index/CLASSES.tsv shift when classes grow.

import clr
import json
from pathlib import Path

from System import AppDomain, Enum

# __file__ does not exist when the script arrives through the bridge (it is exec'd as a string),
# so the repo root comes from the machine paths file, like every other script here.
_PATHS = Path.home() / ".pynet" / "paths.json"
_QGIS = Path(json.loads(_PATHS.read_text(encoding="utf-8"))["qgis_dir"])
REPO = _QGIS.parents[1]            # <repo>/01_Scripts/04_QGIS -> <repo>
STUBS = REPO / "02_PyNet Stubs"
INDEX = STUBS / "_index" / "CLASSES.tsv"
if not INDEX.exists():
    raise Exception("No encuentro el indice de stubs: %s" % INDEX)


# The MCP validator does not whitelist the 'keyword' module, so the reserved words are listed
# here. Same purpose as safe_name() in GenerateStubs.py.
PALABRAS = {"False", "None", "True", "and", "as", "assert", "async", "await", "break", "class",
            "continue", "def", "del", "elif", "else", "except", "finally", "for", "from",
            "global", "if", "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass",
            "raise", "return", "try", "while", "with", "yield"}


def safe_name(name):
    return name + "_" if name in PALABRAS else name


# ---- 1. Every enum currently loaded, by full name ------------------------------------------
enums = {}
for asm in AppDomain.CurrentDomain.GetAssemblies():
    try:
        tipos = asm.GetTypes()
    except Exception:
        continue
    for t in tipos:
        try:
            if not t.IsEnum or not t.IsPublic:
                continue
            nombres = list(t.GetEnumNames())
            if not nombres:
                continue
            valores = []
            for n in nombres:
                try:
                    valores.append((n, int(Enum.Format(t, Enum.Parse(t, n), "d"))))
                except Exception:
                    valores.append((n, None))
            enums[t.FullName] = {"nombre": t.Name.split("`")[0],
                                 "namespace": t.Namespace or "",
                                 "valores": valores}
        except Exception:
            continue
print("Enums cargados en el host: %d" % len(enums))

# ---- 2. Locate each one in the stub index --------------------------------------------------
# CLASSES.tsv: name, namespace, file, line_start, line_end, base, n_members
por_fichero = {}
filas = 0
for linea in INDEX.read_text(encoding="utf-8").splitlines():
    if not linea.strip():
        continue
    campos = linea.split("\t")
    if len(campos) < 5:
        continue
    filas += 1
    nombre, namespace, fichero = campos[0], campos[1], campos[2]
    full = (namespace + "." + nombre) if namespace else nombre
    if full not in enums:
        continue
    try:
        ini, fin = int(campos[3]), int(campos[4])
    except ValueError:
        continue
    por_fichero.setdefault(fichero, []).append(
        {"full": full, "nombre": nombre, "ini": ini, "fin": fin, "info": enums[full]})
print("Filas en el indice: %d | enums localizados en los stubs: %d en %d ficheros"
      % (filas, sum(len(v) for v in por_fichero.values()), len(por_fichero)))

# ---- 3. Patch each file, bottom-up so the line numbers above stay valid ----------------------
completados, ya_estaban, no_cuadraban = 0, 0, 0
detalle = []
for fichero in sorted(por_fichero):
    ruta = STUBS / fichero
    if not ruta.exists():
        print("  falta el fichero %s" % fichero)
        continue
    lineas = ruta.read_text(encoding="utf-8").splitlines()
    for item in sorted(por_fichero[fichero], key=lambda x: x["ini"], reverse=True):
        ini, fin = item["ini"] - 1, item["fin"]        # tsv is 1-based, end inclusive
        bloque = lineas[ini:fin]
        if not bloque or not bloque[0].startswith("class " + item["nombre"]):
            no_cuadraban += 1
            continue
        cuerpo = "\n".join(bloque)
        if ": int" in cuerpo and "# =" in cuerpo:
            ya_estaban += 1
            continue
        nuevo = [
            "class %s:" % item["nombre"],
            '    """.NET enum: %s"""' % item["full"],
            "    def __init__(self, *args) -> None: ...",
        ]
        for n, v in item["info"]["valores"]:
            nuevo.append("    %s: int  # = %s" % (safe_name(n), v if v is not None else "?"))
        lineas[ini:fin] = nuevo
        completados += 1
        detalle.append({"enum": item["full"], "miembros": len(item["info"]["valores"]),
                        "fichero": fichero})
    ruta.write_text("\n".join(lineas) + "\n", encoding="utf-8")

print("\nCompletados: %d | ya tenian miembros: %d | bloque no coincidente: %d"
      % (completados, ya_estaban, no_cuadraban))

destacados = ["Autodesk.Civil.SpiralType",
              "Autodesk.Civil.DatabaseServices.SpiralParamType",
              "Autodesk.Civil.DatabaseServices.SubassemblyLogicalNameType",
              "Autodesk.Civil.DatabaseServices.AssemblyType",
              "Autodesk.Civil.DatabaseServices.CurveParamType"]
print("\nComprobacion de los que hicieron falta hoy:")
for d in destacados:
    if d in enums:
        vals = [n for n, _ in enums[d]["valores"]]
        print("  %-62s %d: %s" % (d, len(vals), ", ".join(vals[:8])))

print("\nAHORA: ejecuta 01_Scripts/00_utils/IndexStubs.py (CPython local) para rehacer el indice,")
print("porque las lineas de _index/CLASSES.tsv se han desplazado.")

ia_Result = [{"type": "completar_enums_stubs",
              "enums_en_host": len(enums),
              "completados": completados,
              "ya_tenian": ya_estaban,
              "no_coincidian": no_cuadraban,
              "ficheros": len(por_fichero),
              "detalle": detalle[:50]}]
