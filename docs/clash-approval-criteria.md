<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Reference: clash approval criteria (Approve vs Reviewed)

Used by the `ClashDetection` skill (step 10) and by `ClashCoordination` to decide whether a clash can
be **Approved** (false positive / accepted condition) or must be **Reviewed** (real issue requiring
coordination). Codes are `PYNET_Classification` codes (`TUB` pipes, `CON` ducts, `LOS` slabs, `PIL`
columns, `FAC` facade, `PAR` partitions, `MUR` walls).

> These rules are definitive. Apply them mechanically — no judgment calls unless the geometry is ambiguous.

---

## RULE 1 — MEP vs structural elements (PIL / beams): always Reviewed, 100%

**Any clash between an MEP element (TUB or CON) and a structural element (column or beam) is ALWAYS Reviewed. No exceptions.**

- Diameter does not matter.
- Penetration depth does not matter.
- Proximity to other elements does not matter.

**Structural PYNET codes:** `PIL` (columns) and any beam codes present in the project.

**Why:** Structural elements carry loads. Any opening requires explicit sign-off from the structural engineer. There is no safe threshold.

## RULE 2 — Pipes through slabs (TUB vs LOS): Approve when conditions met

A pipe clashing with a slab or floor (`LOS`) can be **Approved** when ALL of the following are true:

1. **Pipe diameter < 175 mm** — a standard sleeve (pasatubos) can resolve it without structural coordination.
2. **No nearby MEP interference within ~1000 mm** — no other clash (CON or TUB) at the same location that would require a combined, larger structural opening.

If either condition fails → **Reviewed**.

**How to extract diameter:** read the pipe's `LcRevitData_Element` (display: `"Componente"`) property `"Diámetro"` (exact string with accent). Also available: `"Diámetro exterior"`, `"Diámetro interno"`.

**How to check spatial proximity:** compare `result.Center` (document units → mm with `UnitConversion.ScaleFactor`, see docs/navisworks.md) between the TUB clash and all other MEP clashes. Use 3D Euclidean distance with `math.sqrt`. Flag as Reviewed if any other MEP clash is within 1000 mm.

```python
import math
dist = math.sqrt((cx1 - cx2)**2 + (cy1 - cy2)**2 + (cz1 - cz2)**2)  # mm
```

> **Critical:** "no nearby interference" means no other clash physically close in 3D space — NOT just "no other clash in the same test". A TUB vs LOS 570 mm from a CON vs LOS means both go through the same slab zone → the opening must account for both → Reviewed.

## RULE 3 — Ducts through slabs (CON vs LOS): always Reviewed

Ducts require a larger opening that must be coordinated with the structural model. Always **Reviewed**, regardless of duct size or penetration depth.

## RULE 4 — Structural columns embedded in facade (PIL vs FAC): always Approved

Perimeter columns partially overlapping the facade skin are **always Approved** — intentional architectural/structural condition, not a coordination issue.

## RULE 5 — Columns wider than partition (PIL vs PAR): always Reviewed

When a column is wider than the partition it crosses, the architectural/structural conflict must be resolved explicitly. Always **Reviewed**.

---

## Summary table

| Clash | Condition | Decision |
|-------|-----------|:--------:|
| TUB/CON vs PIL or beam | any | **Reviewed** |
| TUB vs LOS | Ø < 175 mm AND no nearby MEP within 1000 mm | **Approve** |
| TUB vs LOS | Ø ≥ 175 mm OR nearby MEP within 1000 mm | **Reviewed** |
| CON vs LOS | any | **Reviewed** |
| PIL vs FAC | perimeter column overlapping facade | **Approve** |
| PIL vs PAR | column wider than partition | **Reviewed** |

> **Tie-break rule:** When in doubt — always **Reviewed**. The cost of missing a real issue is always higher than the cost of flagging a false positive.
