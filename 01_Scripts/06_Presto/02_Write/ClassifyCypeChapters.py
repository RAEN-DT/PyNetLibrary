# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import clr

clr.AddReference("System.Windows.Forms")

from System.Windows.Forms import MessageBox, MessageBoxButtons, MessageBoxIcon, DialogResult

# The host injects the Presto COM application (Presto.App.18) as __presto__
try:
    app = __presto__
except NameError:
    raise Exception("__presto__ not found: run this script from PyNET for Presto (Complementos > PyNET).")

# ---------------------------------------------------------------------------
# Reorganise the partidas of the active obra into the chapter -> subchapter ->
# group structure of the CYPE "Generador de Precios" (obra nueva,
# generadordeprecios.info/obra_nueva), e.g. F > FF > FFQ.
#
# Made for budgets created from a BIM model (Revit category chapters such as
# "Muros", "Suelos", "Puertas"..., Tekla structure takeoffs such as "Acero
# A992 en vigas W410x60" or "Pilar de hormigón C30"): each partida is
# classified with the RULES below, from its summary and the summary of the
# chapter that holds it. Partidas with no CYPE equivalent (loose
# furniture...) go to chapter Z - the confirmation lists them.
#
# - Partidas keep their code, summary, unit and quantity: the relation to the
#   old chapter is replaced by a relation to the CYPE group.
# - Only the CYPE chapters/groups that receive partidas are created.
# - Old chapters left empty are deleted (Z too, once emptied).
# - Partidas already inside a CYPE group are left alone, except those in Z,
#   which are classified again: running it twice does nothing else.
#
# Verified on Presto 26.01. One undo step (Ctrl+Z in Presto). Changes are NOT
# saved: save the obra in Presto.
# ---------------------------------------------------------------------------
FILTER = "Conceptos.Nat!=219 && Conceptos.Nat!=170"
LOOKUP_SLOT = 9
NAT_CHAPTER = 4

# code: (summary, parent) - in Generador de Precios order
CYPE_TREE = [
    ("E", "Estructuras", None),
    ("EA", "Acero", "E"),
    ("EAS", "Pilares", "EA"),
    ("EAP", "Perfiles estructurales", "EA"),
    ("EAV", "Vigas", "EA"),
    ("EH", "Hormigón armado", "E"),
    ("EHE", "Escaleras", "EH"),
    ("EHS", "Pilares", "EH"),
    ("EHV", "Vigas", "EH"),
    ("EHL", "Losas macizas", "EH"),
    ("EHM", "Muros", "EH"),
    ("EHN", "Núcleos y pantallas", "EH"),
    ("F", "Fachadas y particiones", None),
    ("FF", "Fábrica no estructural", "F"),
    ("FFF", "Fachada de una hoja para revestir", "FF"),
    ("FFQ", "Hoja para revestir en partición", "FF"),
    ("FB", "Tabiquería de entramado autoportante", "F"),
    ("FBY", "De placas de yeso laminado", "FB"),
    ("L", "Carpintería, cerrajería, vidrios y protecciones solares", None),
    ("LC", "Carpintería", "L"),
    ("LCL", "De aluminio", "LC"),
    ("LE", "Puertas de entrada a vivienda", "L"),
    ("LEL", "De aluminio", "LE"),
    ("LP", "Puertas interiores", "L"),
    ("LPM", "De madera", "LP"),
    ("I", "Instalaciones", None),
    ("II", "Iluminación", "I"),
    ("III", "Interior", "II"),
    ("R", "Revestimientos y trasdosados", None),
    ("RS", "Pavimentos", "R"),
    ("RSG", "De piezas cerámicas", "RS"),
    ("S", "Señalización y equipamiento", None),
    ("SA", "Aparatos sanitarios", "S"),
    ("SAL", "Lavabos", "SA"),
    ("SAI", "Inodoros", "SA"),
    ("SAD", "Duchas", "SA"),
    ("SM", "Baños", "S"),
    ("SMM", "Mamparas", "SM"),
    ("SMN", "Muebles", "SM"),
    ("SC", "Cocinas/galerías", "S"),
    ("SCF", "Fregaderos y lavaderos", "SC"),
    ("SCM", "Muebles", "SC"),
    ("SN", "Encimeras", "S"),
    ("SNA", "De aglomerado de cuarzo", "SN"),
    ("Z", "Mobiliario y decoración (sin equivalente en Generador de Precios)", None),
]
CYPE = {code: (summary, parent) for code, summary, parent in CYPE_TREE}
FALLBACK_GROUP = "Z"

# (context words or "" for any, words in the partida summary or "" for any, group)
# The context is the old chapter summary + the partida summary, so a material
# can come from either ("ESTRUCTURA METÁLICA" > "Vigas W410x60" or
# "Acero A992 en vigas"). First match wins. Words are compared lower case and
# without accents. Order matters: stairs and cores before slabs and walls.
STEEL = "acero|steel|metalic|s235|s275|s355|a992|a572"
CONCRETE = "hormigon|concrete|c25|c30|c35|c40|ha-|hormigón"
RULES = [
    # Structure
    (STEEL, "pilar|soporte|column", "EAS"),
    (STEEL, "viga|beam|correa|zuncho", "EAV"),
    (STEEL, "arriostr|brace|bracing|tirante|diagonal|perfil|hss", "EAP"),
    (CONCRETE, "escalera|stair|peldan|meseta", "EHE"),
    (CONCRETE, "nucleo|ascensor|elevator|lift|pantalla|shaft", "EHN"),
    (CONCRETE, "pilar|soporte|column", "EHS"),
    (CONCRETE, "viga|beam", "EHV"),
    (CONCRETE, "muro|wall", "EHM"),
    (CONCRETE, "losa|forjado|slab", "EHL"),
    # Finishes, carpentry, MEP and furniture
    ("", "mampara", "SMM"),
    ("", "ducha|shower", "SAD"),
    ("", "inodoro|toilet|wc ", "SAI"),
    ("", "lavabo|washbasin|wash_basin", "SAL"),
    ("", "fregadero|pia da cozinha|sink", "SCF"),
    ("", "encimera|countertop", "SNA"),
    ("mobiliario|casework|mueble", "cocina|kitchen", "SCM"),
    ("mobiliario|casework|mueble", "bano|bath", "SMN"),
    ("luminaria|iluminacion|lighting", "", "III"),
    ("puerta|door", "seguridad|sikkerhet|security|entrada|blindada|acorazada", "LEL"),
    ("puerta|door", "", "LPM"),
    ("ventana|window", "", "LCL"),
    ("suelo|floor|pavimento", "ceramic|gres|baldosa|tile", "RSG"),
    ("suelo|floor|losa|forjado", "", "EHL"),
    ("muro|wall|tabique", "particion|yeso|pladur|placa|drywall|gypsum", "FBY"),
    ("muro|wall|tabique", "interior", "FFQ"),
    ("muro|wall", "", "FFF"),
]


ACCENTS = str.maketrans("áéíóúüñàèìòùâêîôûäëïöçøå", "aeiouunaeiouaeiouaeiocoa")


def plain(text):
    return str(text or "").lower().translate(ACCENTS)


def matches(words, text):
    return words == "" or any(w in text for w in words.split("|"))


def classify(chapter_summary, summary):
    s = plain(summary)
    context = plain(chapter_summary) + " " + s
    for ctx_words, words, group in RULES:
        if matches(ctx_words, context) and matches(words, s):
            return group
    return FALLBACK_GROUP


def q(text):
    return '"' + text + '"'


def find_relation(sup, inf):
    app.SetElement(LOOKUP_SLOT, "Relaciones", "Relaciones.CodSup", q(sup), "Relaciones.CodInf==" + q(inf))
    return app.GetElement(LOOKUP_SLOT) == 0


def add_relation(sup, inf, qty):
    if not find_relation(sup, inf):
        app.InitRecord("Relaciones")
        app.SetField("Relaciones.CodSup", sup)
        app.SetField("Relaciones.CodInf", inf)
        app.InsertRecord("Relaciones")
        if not find_relation(sup, inf):
            raise Exception("Could not create the relation %s -> %s" % (sup, inf))
    app.SetField("Relaciones.CanPres", qty)
    app.UpdateRecord("Relaciones")


def children(sup, slot):
    """[(code, nat, summary, qty)] of a concept - read in full before any other lookup."""
    rows = []
    app.SetElement(slot, "Relaciones", "Relaciones.CodSup", q(sup), FILTER)
    while app.GetElement(slot) == 0:
        rows.append((app.GetFieldStr("Relaciones.CodInf"),
                     int(app.GetFieldNum("Conceptos.Nat") or 0),
                     app.GetFieldStr("Conceptos.Resumen") or "",
                     app.GetFieldNum("Relaciones.CanPres")))
    return rows


def collect(sup, sup_summary, depth, out, chapters):
    """Partidas not yet in a CYPE group, plus those left in the fallback group Z
    (rules may have improved since): (code, summary, parent, parent summary, qty)."""
    for code, nat, summary, qty in children(sup, depth):
        if nat == NAT_CHAPTER:
            if code not in CYPE or code == FALLBACK_GROUP:
                chapters.append((sup, code))
            if depth < 8:
                # Z's own summary says nothing about its partidas: classify them on their summary only
                collect(code, "" if code == FALLBACK_GROUP else summary, depth + 1, out, chapters)
        elif sup not in CYPE or sup == FALLBACK_GROUP:
            out.append((code, summary, sup, sup_summary, qty))


def ensure_node(code, root, created):
    if code in created:
        return
    summary, parent = CYPE[code]
    parent_code = parent or root
    if parent:
        ensure_node(parent, root, created)
    if app.FindEqual("Conceptos", "Conceptos.Código", code) != 0:
        app.InitRecord("Conceptos")
        app.SetField("Conceptos.Código", code)
        app.InsertRecord("Conceptos")
        if app.FindEqual("Conceptos", "Conceptos.Código", code) != 0:
            raise Exception("Could not create the chapter " + code)
        app.SetField("Conceptos.Nat", NAT_CHAPTER)
        app.SetField("Conceptos.Resumen", summary)
        app.UpdateRecord("Conceptos")
    elif int(app.GetFieldNum("Conceptos.Nat") or 0) != NAT_CHAPTER:
        raise Exception("The code %s already exists and is not a chapter" % code)
    if not find_relation(parent_code, code):
        add_relation(parent_code, code, 1)
    created.add(code)


def delete_empty_chapters(chapters):
    """Deepest first: a chapter is deleted when nothing hangs from it any more."""
    deleted = []
    for sup, code in reversed(chapters):
        if children(code, LOOKUP_SLOT - 1):
            continue
        if find_relation(sup, code):
            app.DeleteRecord("Relaciones", 0)
        if app.FindEqual("Conceptos", "Conceptos.Código", code) == 0:
            app.DeleteRecord("Conceptos", 0)
        deleted.append(code)
    return deleted


project = app.Project()
if not project:
    raise Exception("No obra is open in Presto.")

app.FindEqual("Conceptos", "Conceptos.Nat", 0)
root = app.GetFieldStr("Conceptos.Código")

partidas, old_chapters = [], []
collect(root, "", 1, partidas, old_chapters)

plan = [(code, summary, sup, qty, classify(sup_summary, summary)) for code, summary, sup, sup_summary, qty in partidas]
plan = [p for p in plan if p[4] != p[2]]       # still unclassified partidas already in Z stay there

if not plan:
    MessageBox.Show("Todas las partidas ya están en grupos del Generador de Precios.\nNo hay nada que reorganizar.",
                    "Clasificar CYPE", MessageBoxButtons.OK, MessageBoxIcon.Information)
else:
    counts = {}
    for p in plan:
        counts[p[4]] = counts.get(p[4], 0) + 1
    summary_lines = ["%s  %s: %d" % (g, CYPE[g][0], counts[g]) for g, _, _ in CYPE_TREE if g in counts]
    warning = ""
    if FALLBACK_GROUP in counts:
        warning = ("\n\nATENCIÓN: %d partidas no encajan en ninguna regla y van al capítulo %s:\n%s" % (
            counts[FALLBACK_GROUP], FALLBACK_GROUP,
            "\n".join("  %s %s" % (p[0], p[1][:60]) for p in plan if p[4] == FALLBACK_GROUP)))
    text = ("Obra: %s\n\nSe moverán %d partidas a los grupos del Generador de Precios:\n\n%s%s\n\n"
            "Los capítulos antiguos que queden vacíos se eliminarán. ¿Continuar?") % (
        project, len(plan), "\n".join(summary_lines), warning)
    if MessageBox.Show(text, "Clasificar CYPE", MessageBoxButtons.YesNo, MessageBoxIcon.Question) == DialogResult.Yes:
        created = set()
        app.BeginRedo()
        try:
            # chapters in Generador de Precios order, so they show in that order under the root
            for g, _, _ in CYPE_TREE:
                if g in counts:
                    ensure_node(g, root, created)
            for code, summary, sup, qty, group in plan:
                add_relation(group, code, qty)
                if find_relation(sup, code):
                    app.DeleteRecord("Relaciones", 0)
            deleted = delete_empty_chapters(old_chapters)
        finally:
            app.EndRedo()
        app.Recalculate(1)
        app.UpdateScreen()

        for code, summary, sup, qty, group in plan:
            print("%-10s %-4s <- %-4s %s" % (code, group, sup, summary[:70]))
        print("Partidas movidas: %d | capítulos eliminados: %s" % (len(plan), ", ".join(deleted) or "-"))
        print("Revisa el capítulo Z (sin equivalente) y guarda la obra en Presto.")
