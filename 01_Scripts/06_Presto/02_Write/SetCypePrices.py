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
# Price the partidas of the active obra with reference prices of the CYPE
# "Generador de Precios" (obra nueva, costes directos, Spain), by the group
# that holds each partida (run ClassifyCypeChapters.py first).
#
# Each group has a reference unit (partida) of generadordeprecios.info with
# its default options; VARIANTS picks another one from words in the partida
# summary. The prices were read from the site on 2026-10-20 - they are a
# first estimate, not the price of the exact element: edit PRICES to update
# them or to use your own partidas.
#
# Asks whether to overwrite prices already typed (Yes) or only fill the
# partidas without price (No). Partidas in groups with no price (chapter Z)
# and partidas whose unit differs from the reference one are reported and
# left untouched - except concrete measured in m3 against a CYPE price per m2
# (slabs, stairs), converted with the m3/m2 of the CYPE breakdown
# (CONCRETE_M3_PER_M2). The script reads every price back after
# Recalculate and reports mismatches.
#
# Verified on Presto 26.01. One undo step (Ctrl+Z in Presto). Changes are NOT
# saved: save the obra in Presto.
# ---------------------------------------------------------------------------
PRICE_FIELD = "Conceptos.Pres"
FILTER = "Conceptos.Nat!=219 && Conceptos.Nat!=170"
LOOKUP_SLOT = 9
NAT_CHAPTER = 4

# group: (CYPE partida, unit, price EUR, reference description)
PRICES = {
    "EAS": ("EAS010", "kg", 2.40, "Acero S275JR en pilares de perfiles laminados en caliente, imprimación antioxidante, uniones soldadas"),
    "EAP": ("EAP020", "kg", 2.40, "Acero S275JR en perfiles laminados en caliente, imprimación antioxidante, uniones soldadas"),
    "EAV": ("EAV010", "kg", 2.37, "Acero S275JR en vigas de perfiles laminados en caliente, imprimación antioxidante, uniones soldadas"),
    "EHE": ("EHE010", "m2", 129.35, "Losa de escalera de hormigón armado de 15 cm, con peldañeado de hormigón, HA-25"),
    "EHS": ("EHS010", "m3", 675.22, "Pilar rectangular o cuadrado de hormigón armado HA-25, 30x30 cm, encofrado metálico"),
    "EHV": ("EHV010", "m3", 584.05, "Viga descolgada de hormigón armado HA-25, 40x60 cm"),
    "EHL": ("EHL010", "m2", 109.15, "Losa maciza de hormigón armado, canto 24 cm, HA-25"),
    "EHM": ("EHM010", "m3", 338.44, "Muro de hormigón armado 2C, hasta 3 m de altura, espesor 30 cm, HA-25"),
    "EHN": ("EHN010", "m3", 355.05, "Pantalla/núcleo de hormigón armado 2C, hasta 3 m de altura, espesor medio 30 cm, HA-25"),
    "FFF": ("FFF010", "m2", 32.49, "Fachada de una hoja de ladrillo cerámico hueco triple 11 cm, para revestir"),
    "FFQ": ("FFQ020", "m2", 40.40, "Hoja de partición de bloque hueco de hormigón, para revestir"),
    "FBY": ("FBY010", "m2", 32.72, "Tabique sencillo de placas de yeso laminado, 78 mm"),
    "LCL": ("LCL060", "u", 456.98, "Ventana de aluminio gama básica, 800x500 mm, lacado blanco"),
    "LEL": ("LEL010", "u", 477.45, "Puerta de entrada a vivienda de aluminio, block de seguridad 90x210 cm"),
    "LPM": ("LPM010", "u", 252.54, "Puerta interior abatible ciega de madera, 203x82,5x3,5 cm"),
    "III": ("III101", "u", 170.75, "Luminaria circular tipo Downlight LED, empotrada"),
    "RSG": ("RSG110", "m2", 36.20, "Pavimento interior de gres esmaltado, capa fina"),
    "SAL": ("SAL005", "u", 240.29, "Lavabo sobre encimera, de porcelana sanitaria"),
    "SAI": ("SAI005", "u", 320.14, "Inodoro con tanque bajo, de porcelana sanitaria"),
    "SAD": ("SAD015", "u", 175.76, "Plato de ducha de porcelana sanitaria, 70x70 cm"),
    "SMM": ("SMM020", "u", 1380.06, "Mampara frontal para ducha, puerta corredera y panel fijo"),
    "SMN": ("SMN010", "u", 1376.12, "Mueble base para lavabo, madera de cerezo, 600 mm"),
    "SCF": ("SCF010", "u", 325.52, "Fregadero de acero inoxidable de 1 cubeta con grifería"),
    "SCM": ("SCM020", "u", 1209.56, "Mobiliario completo de cocina (3,5 m bajos + 3,5 m altos), frente recubierto"),
    "SNA": ("SNA010", "u", 518.00, "Encimera de aglomerado de cuarzo, 350x60x2 cm"),
}

# group: m3 of concrete per m2 in the CYPE price breakdown. Lets a partida
# measured in m3 (BIM takeoffs: Tekla, Revit volumes) take an m2 reference
# price: price per m3 = price per m2 / m3 per m2.
CONCRETE_M3_PER_M2 = {
    "EHL": 0.252,   # EHL010 canto 24 cm
    "EHE": 0.242,   # EHE010 losa 15 cm + peldañeado
}

# group: [(words in the partida summary, CYPE partida, price, description)] - first match wins
VARIANTS = {
    "III": [("cuadrad|square", "III102", 141.65, "Luminaria cuadrada tipo Downlight LED, empotrada")],
    "LPM": [("corredera|sliding", "LPM021", 254.05, "Puerta interior corredera ciega de madera, 203x82,5x3,5 cm")],
}


ACCENTS = str.maketrans("áéíóúüñàèìòùâêîôûäëïöçøå", "aeiouunaeiouaeiouaeiocoa")


def plain(text):
    return str(text or "").lower().translate(ACCENTS)


def q(text):
    return '"' + text + '"'


def unit(text):
    """Unit for comparison: m3 / m³ / M3 are the same unit, ud / u too."""
    u = plain(text).replace(" ", "").replace("³", "3").replace("²", "2").replace(".", "")
    return {"ud": "u", "un": "u", "uds": "u"}.get(u, u)


def reference(group, summary):
    s = plain(summary)
    for words, ref, price, desc in VARIANTS.get(group, []):
        if any(w in s for w in words.split("|")):
            return ref, price, desc
    ref, _, price, desc = PRICES[group]
    return ref, price, desc


def collect(sup, depth, out):
    """(code, summary, group, current price, unit) of every partida, group = the chapter that holds it."""
    rows = []
    app.SetElement(depth, "Relaciones", "Relaciones.CodSup", q(sup), FILTER)
    while app.GetElement(depth) == 0:
        rows.append((app.GetFieldStr("Relaciones.CodInf"),
                     int(app.GetFieldNum("Conceptos.Nat") or 0),
                     app.GetFieldStr("Conceptos.Resumen") or "",
                     app.GetFieldNum(PRICE_FIELD) or 0.0,
                     app.GetFieldStr("Conceptos.Ud") or ""))
    for code, nat, summary, price, ud in rows:
        if nat == NAT_CHAPTER:
            if depth < 8:
                collect(code, depth + 1, out)
        else:
            out.append((code, summary, sup, price, ud))


def has_decomposition(code):
    app.SetElement(LOOKUP_SLOT, "Relaciones", "Relaciones.CodSup", q(code), FILTER)
    return app.GetElement(LOOKUP_SLOT) == 0


project = app.Project()
if not project:
    raise Exception("No obra is open in Presto.")

app.FindEqual("Conceptos", "Conceptos.Nat", 0)
root = app.GetFieldStr("Conceptos.Código")
partidas = []
collect(root, 1, partidas)

priceable = [p for p in partidas if p[2] in PRICES]
unpriced_groups = [p for p in partidas if p[2] not in PRICES]
if not priceable:
    raise Exception("No partida is inside a group of the Generador de Precios: run 'Clasificar CYPE' first.")

with_price = sum(1 for p in priceable if p[3])
answer = MessageBox.Show(
    ("Obra: %s\n\n%d partidas en grupos del Generador de Precios (%d ya tienen precio).\n"
     "%d partidas sin precio de referencia (capítulo Z u otros) no se tocarán.\n\n"
     "Sí = poner precio a todas (sobrescribe)\nNo = solo a las que no tienen precio\nCancelar = salir") % (
        project, len(priceable), with_price, len(unpriced_groups)),
    "Precios CYPE", MessageBoxButtons.YesNoCancel, MessageBoxIcon.Question)

if answer != DialogResult.Cancel:
    overwrite = answer == DialogResult.Yes
    done, skipped = [], []
    app.BeginRedo()
    try:
        for code, summary, group, current, ud in priceable:
            per_m3 = unit(ud) == "m3" and unit(PRICES[group][1]) == "m2" and group in CONCRETE_M3_PER_M2
            if unit(ud) != unit(PRICES[group][1]) and not per_m3:
                skipped.append((code, "unidad %s distinta de la del precio de referencia %s (%s)" % (ud or "-", PRICES[group][1], PRICES[group][0])))
                continue
            if current and not overwrite:
                skipped.append((code, "ya tiene precio %.2f" % current))
                continue
            if has_decomposition(code):
                skipped.append((code, "tiene descomposición (Presto calcula su precio)"))
                continue
            ref, price, desc = reference(group, summary)
            if per_m3:
                factor = CONCRETE_M3_PER_M2[group]
                desc = "%s - %.2f EUR/m2 / %.3f m3/m2" % (desc, price, factor)
                price = round(price / factor, 2)
            if app.FindEqual("Conceptos", "Conceptos.Código", code) != 0:
                skipped.append((code, "no encontrado"))
                continue
            app.SetField(PRICE_FIELD, price)
            app.UpdateRecord("Conceptos")
            done.append((code, group, ref, price, desc, summary))
    finally:
        app.EndRedo()
    app.Recalculate(1)
    app.UpdateScreen()

    mismatches = []
    for code, group, ref, price, desc, summary in done:
        app.FindEqual("Conceptos", "Conceptos.Código", code)
        read = app.GetFieldNum(PRICE_FIELD) or 0.0
        if abs(read - price) > 0.005:
            mismatches.append("%s: escrito %.2f, leído %.2f" % (code, price, read))
        print("%-10s %-4s %-7s %10.2f  %s  <- %s" % (code, group, ref, price, desc[:50], summary[:40]))
    for code, why in skipped:
        print("OMITIDA   %-10s %s" % (code, why))
    for code, summary, group, _, _ in unpriced_groups:
        print("SIN PRECIO %-10s (%s) %s" % (code, group, summary[:60]))

    app.FindEqual("Conceptos", "Conceptos.Nat", 0)
    print("Partidas con precio: %d | omitidas: %d | sin referencia: %d" % (len(done), len(skipped), len(unpriced_groups)))
    print("Presupuesto de la obra: %.2f EUR (costes directos)" % (app.GetFieldNum("Conceptos.Pres") or 0.0))
    if mismatches:
        print("DISCREPANCIAS: " + "; ".join(mismatches))
    print("Precios de referencia de generadordeprecios.info (2026-10-20). Guarda la obra en Presto.")
