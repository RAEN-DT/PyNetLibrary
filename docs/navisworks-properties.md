<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: reading element properties robustly (Navisworks)

Read [navisworks.md](navisworks.md) first. This guide is about getting the **right value from the
right node** without depending on the UI language, the Navisworks version or the source format.

---

## 1. Match the internal name, not the display name

Every property tab has an internal `cat.Name` and a translated `cat.DisplayName`. The display name
changes with the UI language ("Elemento" / "Element", "Tipo de Revit" / "Revit Type"); the internal
name does not. **Match on `cat.Name` whenever you know it.**

| What | `cat.Name` (internal, stable) | Property | Display (ES) |
|---|---|---|---|
| Revit element id | `LcRevitId` | `Valor` / `Value` | ID de elemento |
| Revit type-level data | `LcRevitData_Type` | e.g. `PYNET_Classification` | Tipo de Revit |
| Shared-parameter export | `LcRevitData_TypeCustom` | — | Tipo Personalizar |
| TYPE container node | `lcldrevit_tab_type` | — | Tipo |
| Element data (size, diameter) | `LcRevitData_Element` | `Diámetro`, `Tamaño` | Componente |

When only the display name is known, keep a **bilingual list** and accept any of them:
`("Nombre", "Name")`, `("Categoría", "Category")`, `("Diámetro", "Diametro", "Diameter", "Tamaño")`.

> Hard lesson: category and property names also differ between Revit **versions** in the same
> language. A hardcoded list of Spanish category names silently dropped about half of the MEP and
> structural geometry of a federated model. Discover the names live (a cheap scan of the TYPE nodes)
> before trusting a list.

## 2. Walk up to the node that carries the data

A clash `Item1`/`Item2` or a selected item is usually a **geometry node**; the data lives on an
ancestor (instance node, TYPE node, file node). Walk up instead of reading the item alone:

```python
def find_prop(item, cat_name, prop_name, max_up=10):
    node = item
    for _ in range(max_up):
        if node is None:
            return None
        for cat in node.PropertyCategories:
            if cat.Name == cat_name:
                for prop in cat.Properties:
                    if prop.DisplayName == prop_name:
                        return prop.Value
        node = node.Parent
    return None
```

`[item] + list(item.Ancestors)` is the same walk in one list. Nodes worth knowing:

- **File node** — `ClassDisplayName == "Archivo"` (the NWC); `model.RootItem` for each loaded model.
- **Source `.rvt`** — tab `Elemento`, property `Archivo de origen` on any node under the model.
- **Model root** — `Elemento` / `Proyecto` / `Identidad` tabs hold project name, building name,
  source paths and the model transform (`Transformar` → `Ángulo de rotación` = true north, a
  `DoubleAngle` in radians).

Use `hash(item)` (maps to `GetHashCode()`), never `id(item)`: pythonnet creates a new wrapper on each
`.Parent` access. Do **not** identify items by `InstanceGuid` alone — many nodes carry `Guid.Empty`.

## 3. Unwrap `VariantData` by type

`str(prop.Value)` returns a debug string (`"DisplayString:Muro básico"`, `"Boolean:False"`), and
`ToDisplayString()` **throws** for anything that is not a display string. Dispatch on the type:

```python
import math

def variant_value(val):
    if val.IsDisplayString or val.IsIdentifierString:
        return val.ToDisplayString()
    if val.IsBoolean:
        return val.ToBoolean()
    if val.IsInt32:
        return val.ToInt32()
    if val.IsDoubleLength:
        return val.ToDoubleLength()            # document units
    if val.IsDoubleAngle:
        return math.degrees(val.ToDoubleAngle())
    if val.IsDoubleArea:
        return val.ToDoubleArea()
    if val.IsDoubleVolume:
        return val.ToDoubleVolume()
    if val.IsDouble or val.IsAnyDouble:
        return val.ToAnyDouble()
    if val.IsNamedConstant:
        return str(val.ToNamedConstant())
    if val.IsDateTime:
        return str(val.ToDateTime())
    return val.ToDisplayString()
```

Lengths, areas and volumes come in **document units** — convert with
`UnitConversion.ScaleFactor(doc.Models.First.Units, Units.Meters)` (see navisworks.md).

## 4. Source-format differences

The same element exposes different tabs depending on how it reached Navisworks:

| Source | Category | Type | Length |
|---|---|---|---|
| Revit NWC | `Tipo de Revit` / `Elemento` | `LcRevitData_Type` | `LcRevitData_Element` |
| IFC | `Other` → `Category` | `Other` → `Family and Type` | `Dimensions` / `BaseQuantities` → `Length` |

Check which tabs the model actually has (one cheap query on a few items) before writing the reader.

## 5. Cost

Every property read is a pythonnet ↔ .NET call. Filter nodes first (`ClassDisplayName == "Tipo"`,
`HasGeometry`) and read properties only on the survivors — see "Heavy models" in navisworks.md.

Reference scripts: `05_QueryElements/ExportClashesToJSON.py` (walk-up + internal names),
`05_QueryElements/WallLinearMeters.py` (IFC-sourced names, typed values),
`03_ClashDetection/ExtractClashElementInfo.py` (bilingual fallbacks).
