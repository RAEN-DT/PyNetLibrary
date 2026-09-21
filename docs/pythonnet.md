<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Reference: Python.NET (pythonnet) behaviours that matter in PyNET

Applies to every host. Each item was hit in a real script.

| Situation | What happens | Do this |
|---|---|---|
| Output Window shows prints only at the end | stdout is block-buffered | `sys.stdout.reconfigure(line_buffering=True)` at the top of long scripts — prints appear live |
| Method with `out` / `ref` parameters | returned as a **tuple** | `e, n, _ = alignment.PointLocation(st, off, 0.01, 0.0, 0.0, 0.0)` |
| `List[T]([...])` | "No method matches … ctor" | `lst = List[T](); lst.Add(x)` |
| A .NET property Python cannot reach (e.g. `FamilySymbol.Name`) | `AttributeError` | `Element.Name.__get__(symbol)` |
| Type test | pythonnet returns the concrete class | `el.__class__ == Wall` / `isinstance(g, Solid)` |
| Tracking .NET objects in sets/dicts | a new Python wrapper per access | `hash(obj)` (→ `GetHashCode()`), never `id(obj)` |
| Implementing a .NET interface | works | `class F(ISelectionFilter): ...`, `class C(ICentralLockedCallback): ...` |
| Subclassing a .NET class (`Form`) | `NullReferenceException` on first property | `super().__init__()` first line |
| Integer into a .NET `int` field | Python `int` bridges as **Int64** | `System.Int32(0)` (AEC `PropertyDefinition.DefaultData`) |
| Enum member from a string | `getattr` is blocked by the bridge | `Enum.Parse(BuiltInCategory, "OST_Walls")` or a map built from `Enum.GetValues(T)` |
| Feature-detect a member | — | `try/except AttributeError` (`hasattr` is allowed, `getattr` is not) |
| `str()` of a Navisworks `VariantData` | debug text `"DisplayString:…"` | typed accessors — see [navisworks-properties.md](navisworks-properties.md) |
| Stubs show one overload / no constructor | the generator keeps one signature | reflection: `clr.GetClrType(T).GetMethods()` / `.GetConstructors()` |
| Loading a PyNET assembly | `clr.AddReference` finds an **already-loaded** assembly first | no path needed for `Raen.Core.Pynet.*`; never hardcode the bundle year — see AGENTS.md §6 |
| Enumerating thousands of .NET items from Python | ~ms per crossing | filter early; heavy geometry work belongs in the C# helpers of the plugin |

The runtime is **persistent** across executions in the same host session: a failed import can leave a
broken module in `sys.modules` for the rest of the session (see revit.md).
