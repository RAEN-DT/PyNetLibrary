# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

import clr
from pathlib import Path
from collections import defaultdict
from System import AppDomain
from System.Reflection import BindingFlags  # type:ignore

PYTHON_KEYWORDS = {
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
    'while', 'with', 'yield',
}

def safe_name(name):
    if not name:
        return "value_"
    return name + "_" if name in PYTHON_KEYWORDS else name

# ── Host detection ─────────────────────────────────────────────────────────────
HOST = None
try:
    _revit = __revit__  # type:ignore
    HOST = "Revit"
    VERSION = _revit.Application.VersionNumber
except NameError:
    pass

if HOST is None:
    # Rhino injects the active document as __rhinodoc__; check it before the Autodesk hosts.
    try:
        _rhinodoc = __rhinodoc__  # type:ignore
        HOST = "Rhino"
        try:
            clr.AddReference("RhinoCommon")
            from Rhino import RhinoApp as _RhinoApp
            VERSION = _RhinoApp.ExeVersion
        except Exception:
            VERSION = "unknown"
    except NameError:
        pass

if HOST is None:
    # PyNET for Tekla injects the connected model as __teklamodel__.
    try:
        _teklamodel = __teklamodel__  # type:ignore
        HOST = "Tekla"
        try:
            clr.AddReference("Tekla.Structures")
            from Tekla.Structures import TeklaStructuresInfo as _TeklaInfo
            VERSION = _TeklaInfo.GetCurrentProgramVersion()
        except Exception:
            VERSION = "unknown"
    except NameError:
        pass

if HOST is None:
    # Try Civil 3D before Navisworks
    try:
        clr.AddReference("AeccDbMgd")
        from Autodesk.Civil.ApplicationServices import CivilApplication as _CivilApp
        _civil_doc = _CivilApp.ActiveDocument
        HOST = "Civil"
        try:
            clr.AddReference("AcMgd")
            from Autodesk.AutoCAD.ApplicationServices import Application as _AcadApp
            VERSION = _AcadApp.Version.Major
        except Exception:
            VERSION = "unknown"
    except Exception:
        HOST = "Navisworks"
        try:
            clr.AddReference("Autodesk.Navisworks.Api")
            from Autodesk.Navisworks.Api import Application as _NavApp
            VERSION = str(_NavApp.Version.RuntimeMajor)
        except Exception:
            VERSION = "unknown"

print(f"Host: {HOST} {VERSION}")

# ── Assembly lists per host ────────────────────────────────────────────────────
ASSEMBLY_SETS = {
    "Navisworks": [
        "Autodesk.Navisworks.Api",
        "Autodesk.Navisworks.ComApi",
        "Autodesk.Navisworks.Interop.ComApi",
        "Autodesk.Navisworks.Clash",
    ],
    "Revit": [
        "RevitAPI",
        "RevitAPIUI",
    ],
    "Civil": [
        "AcMgd",
        "AcCoreMgd",
        "AcDbMgd",
        "AecBaseMgd",
        "AeccDbMgd",
        "AecPropDataMgd",
    ],
    "Rhino": [
        "RhinoCommon",
        "Rhino.UI",
        "Eto",
    ],
    # Open API assemblies as PyNET for Tekla resolves them: from the running Tekla's
    # bin\Net48Runtime (Tekla 2026+), then bin. Model also holds Model.UI/Operations, Drawing
    # holds Drawing.UI; Geometry3d lives in Tekla.Structures.
    "Tekla": [
        "Tekla.Structures",
        "Tekla.Structures.Model",
        "Tekla.Structures.Drawing",
        "Tekla.Structures.Datatype",
        "Tekla.Structures.Catalogs",
        "Tekla.Structures.Dialog",
        "Tekla.Structures.Plugins",
    ],
}

ASSEMBLIES = ASSEMBLY_SETS.get(HOST, ASSEMBLY_SETS["Navisworks"])

# ── Output: repo stubs folder (committed to GitHub) ───────────────────────────
# Cleans only the Autodesk\<Host> subtree so Navisworks and Revit stubs coexist.
STUBS_ROOT = Path.home() / "source" / "repos" / "GithubRNM" / "PyNetLibrary" / "02_PyNet Stubs"
if not STUBS_ROOT.parent.exists():
    # Clones under repos\Github instead of repos\GithubRNM.
    STUBS_ROOT = Path.home() / "source" / "repos" / "Github" / "PyNetLibrary" / "02_PyNet Stubs"
STUBS_ROOT.mkdir(parents=True, exist_ok=True)

# Host root inside Autodesk\ (e.g. Autodesk\Revit or Autodesk\Navisworks)
HOST_NS_ROOT = {
    "Revit":     "Revit",
    "Navisworks": "Navisworks",
    "Civil":     "Civil3D",
}
HOST_AUTODESK_DIR = STUBS_ROOT / "Autodesk" / HOST_NS_ROOT.get(HOST, HOST)
# Folders this host actually writes (namespace roots), relative to STUBS_ROOT. Civil 3D spans three
# of them - cleaning only "Autodesk/Civil3D" (which is never written) left the real Civil stubs stale
# on every regeneration. Rhino's namespaces (Rhino.*, Eto.*) and Tekla's (Tekla.*) live at the
# root, not under Autodesk.
HOST_DIRS = {
    "Revit": ["Autodesk/Revit"],
    "Navisworks": ["Autodesk/Navisworks"],
    "Civil": ["Autodesk/AutoCAD", "Autodesk/Civil", "Autodesk/Aec"],
    "Rhino": ["Rhino", "Eto"],
    "Tekla": ["Tekla"],
}

print(f"Stubs root:  {STUBS_ROOT}")

# ── Clean only the host subtree ────────────────────────────────────────────────
def remove_tree(p: Path):
    if p.is_dir():
        for child in p.iterdir():
            remove_tree(child)
        p.rmdir()
    elif p.exists():
        p.unlink()

for _sub in HOST_DIRS.get(HOST, ["Autodesk/" + HOST_NS_ROOT.get(HOST, HOST)]):
    _dir = STUBS_ROOT / _sub
    if _dir.exists():
        print(f"Cleaning:    {_dir}")
        remove_tree(_dir)

# ── Type map ───────────────────────────────────────────────────────────────────
TYPE_MAP = {
    "String": "str",   "Boolean": "bool",
    "Int32": "int",    "Int64": "int",   "UInt32": "int",  "UInt64": "int",
    "Int16": "int",    "UInt16": "int",  "Byte": "int",    "SByte": "int",
    "Double": "float", "Single": "float",
    "Char": "str",     "Void": "None",   "Object": "object",
}

def map_type(t):
    try:
        if t.IsArray:
            return "list"
        if t.IsByRef or t.IsPointer:
            return map_type(t.GetElementType())
        name = t.Name.split("`")[0]
        return TYPE_MAP.get(name, name)
    except Exception:
        return "object"

# ── Code generators ────────────────────────────────────────────────────────────
def gen_methods(types, flags):
    grouped = defaultdict(list)
    for t in types:
        for m in t.GetMethods(flags):
            if m.IsSpecialName or m.DeclaringType != t:
                continue
            grouped[m.Name].append(m)

    lines = []
    for name, overloads in sorted(grouped.items()):
        try:
            safe_method = safe_name(name)
            best = max(overloads, key=lambda m: len(m.GetParameters()))
            params = [f"{safe_name(p.Name)}: {map_type(p.ParameterType)}" for p in best.GetParameters()]
            ret = map_type(best.ReturnType)
            if best.IsStatic:
                lines.append(f"    @staticmethod")
                lines.append(f"    def {safe_method}({', '.join(params)}) -> {ret}: ...")
            else:
                lines.append(f"    def {safe_method}(self, {', '.join(params)}) -> {ret}: ...")
        except Exception:
            continue
    return lines

def gen_class(types):
    """One Python class per .NET name. Generic arities share a Python name (Dialog and Dialog`1 are
    both `Dialog`, as pythonnet exposes them), so they are merged into a single class: emitting them
    separately made the later definition silently shadow the earlier one."""
    try:
        types = [t for t in types if t.IsPublic]
        if not types:
            return None
        # Non-generic first: its base class and member order win.
        types = sorted(types, key=lambda x: (x.IsGenericTypeDefinition, x.Name))
        t = types[0]
        name = t.Name.split("`")[0]
        bases = []
        if t.BaseType and t.BaseType.FullName not in (
                "System.Object", "System.ValueType",
                "System.Enum", "System.MulticastDelegate"):
            base = map_type(t.BaseType)
            if base != name:  # Dialog`1 derives from Dialog: never a self-reference
                bases.append(base)
        base_str = f"({', '.join(bases)})" if bases else ""

        flags = (BindingFlags.Public | BindingFlags.Instance |
                 BindingFlags.Static | BindingFlags.DeclaredOnly)

        body = [
            f'class {name}{base_str}:',
            f'    """.NET: {" | ".join(x.FullName for x in types)}"""',
            f'    def __init__(self, *args) -> None: ...',
        ]
        seen_props = set()
        for x in types:
            for p in x.GetProperties():
                try:
                    if p.Name in seen_props:
                        continue
                    seen_props.add(p.Name)
                    body.append(f"    {p.Name}: {map_type(p.PropertyType)}")
                except Exception:
                    continue
        body.extend(gen_methods(types, flags))
        if len(body) == 3:
            body.append("    ...")
        return "\n".join(body)
    except Exception:
        return None

# ── Namespace → relative file path ────────────────────────────────────────────
def ns_to_relpath(ns: str, all_ns: set) -> Path:
    parts = ns.split(".")
    has_children = any(n.startswith(ns + ".") for n in all_ns if n != ns)
    if has_children:
        return Path(*parts) / "__init__.py"
    return Path(*parts[:-1]) / f"{parts[-1]}.py"

def ensure_inits(file_path: Path, root: Path):
    current = file_path.parent
    while current != root and current != current.parent:
        init = current / "__init__.py"
        if not init.exists():
            init.write_text("# auto-generated\n", encoding="utf-8")
        current = current.parent

# ── Load assemblies ────────────────────────────────────────────────────────────
for asm_name in ASSEMBLIES:
    try:
        clr.AddReference(asm_name)
        print(f"  Loaded: {asm_name}")
    except Exception as e:
        print(f"  SKIP:   {asm_name} — {e}")

loaded = {a.GetName().Name.lower(): a for a in AppDomain.CurrentDomain.GetAssemblies()}

# ── Collect types by namespace ─────────────────────────────────────────────────
ns_types: dict = defaultdict(list)
for asm_name in ASSEMBLIES:
    asm = loaded.get(asm_name.lower())
    if asm is None:
        continue
    try:
        for t in asm.GetTypes():
            try:
                if t.IsPublic and t.Namespace:
                    ns_types[t.Namespace].append(t)
            except Exception:
                continue
    except Exception as e:
        print(f"  ERROR reading {asm_name}: {e}")

all_ns = set(ns_types.keys())
print(f"\nNamespaces: {len(all_ns)}")

# ── Write stub files ───────────────────────────────────────────────────────────
written = errors = 0
for ns, types in sorted(ns_types.items()):
    try:
        rel = ns_to_relpath(ns, all_ns)
        out = STUBS_ROOT / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        ensure_inits(out, STUBS_ROOT)

        lines = [f"# Auto-generated — {HOST} {VERSION} — {ns}", ""]
        by_name = defaultdict(list)
        for t in types:
            by_name[t.Name.split("`")[0]].append(t)
        for _name, group in sorted(by_name.items()):
            code = gen_class(group)
            if code:
                lines.append(code)
                lines.append("")

        out.write_text("\n".join(lines), encoding="utf-8")
        written += 1
    except Exception as e:
        print(f"  ERROR {ns}: {e}")
        errors += 1

print(f"\nDone: {written} files written, {errors} errors.")
print(f"Location: {STUBS_ROOT}")
