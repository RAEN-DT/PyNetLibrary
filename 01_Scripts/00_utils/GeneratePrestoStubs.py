# SPDX-License-Identifier: MIT
# Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform

"""
Generate the Presto API stubs from Presto's COM type library.

Presto has no .NET assemblies: its API is the COM automation server "Presto.App.18" described by
"Presto Type Library" (Bin\\presto.tlb). GenerateStubs.py reflects .NET types inside a host, so it
cannot see this API; this script reads the type library instead.

Runs standalone with local CPython + comtypes -- no Presto running, no MCP bridge:

    uv run --with comtypes python 01_Scripts/00_utils/GeneratePrestoStubs.py [path\\to\\Bin]

Without an argument it uses the newest "C:\\Program Files\\Presto*\\<version>\\Bin" it finds.

Writes into 02_PyNet Stubs/Presto/ (deletes only that folder, like GenerateStubs.py per host):
    __init__.py   PrestoApplication -- the interface scripts get as __presto__
    PrmCom.py     ComPrmDllFunction -- interface of parametric-concept DLLs (PrestoPrmCom.tlb)

Then re-run IndexStubs.py so CLASSES.tsv picks the classes up.

Stub conventions (they differ from the .NET stubs on purpose):
- Every member is written as a method, properties included, because that is how the __presto__
  proxy exposes them: obra.Project(), obra.VersionStr().
- Parameter names are the type library's own (Spanish in older members: tabla, clave, valor...).
- Optional parameters (type library [optional] / [defaultvalue]) get "= ..." or their default.
- VARIANT parameters and returns are typed "object": Presto decides the real type at run time.
"""

import shutil
import sys
from pathlib import Path

import comtypes.typeinfo as ti

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "02_PyNet Stubs" / "Presto"

# IUnknown / IDispatch plumbing: present in the type library, never called by scripts.
PLUMBING = {"QueryInterface", "AddRef", "Release", "GetTypeInfoCount", "GetTypeInfo",
            "GetIDsOfNames", "Invoke"}

# VARTYPE -> Python annotation
VT = {
    2: "int", 3: "int", 16: "int", 17: "int", 18: "int", 19: "int", 20: "int", 21: "int",
    22: "int", 23: "int", 25: "None",
    4: "float", 5: "float", 6: "float", 14: "float",
    7: "object",        # VT_DATE
    8: "str",           # VT_BSTR
    9: "object",        # VT_DISPATCH
    10: "int",          # VT_ERROR / HRESULT
    11: "bool",
    12: "object",       # VT_VARIANT
    13: "object",       # VT_UNKNOWN
    24: "None",         # VT_VOID
    30: "str", 31: "str",
}
VT_PTR, VT_SAFEARRAY, VT_CARRAY, VT_USERDEFINED = 26, 27, 28, 29
PARAMFLAG_FOUT, PARAMFLAG_FRETVAL, PARAMFLAG_FOPT, PARAMFLAG_FHASDEFAULT = 2, 8, 16, 32
INVOKE_FUNC, INVOKE_PROPGET, INVOKE_PROPPUT, INVOKE_PROPPUTREF = 1, 2, 4, 8
KEYWORDS = {"from", "in", "is", "not", "and", "or", "class", "def", "return", "type", "print",
            "lambda", "global", "with", "as", "if", "else", "for", "while", "pass", "import"}


def annotation(tdesc):
    vt = tdesc.vt
    if vt == VT_PTR:
        return annotation(tdesc._.lptdesc[0])
    if vt in (VT_SAFEARRAY, VT_CARRAY):
        return "list"
    if vt == VT_USERDEFINED:
        return "object"
    return VT.get(vt, "object")


def py_name(name):
    return name + "_" if name in KEYWORDS else name


def default_literal(pdesc):
    try:
        value = pdesc._.pparamdescex[0].varDefaultValue.value
    except Exception:
        return "..."
    return repr(value)


def collect(tinfo):
    """name -> {"doc", "params", "ret", "kinds"}; propget/propput pairs merge into one entry."""
    attr = tinfo.GetTypeAttr()
    members = {}
    for f in range(attr.cFuncs):
        fd = tinfo.GetFuncDesc(f)
        names = tinfo.GetNames(fd.memid, fd.cParams + 1)
        name = names[0]
        if name in PLUMBING:
            continue
        doc = tinfo.GetDocumentation(fd.memid)[1]
        params, ret = [], annotation(fd.elemdescFunc.tdesc)
        for p in range(fd.cParams):
            ed = fd.lprgelemdescParam[p]
            flags = ed._.paramdesc.wParamFlags
            ann = annotation(ed.tdesc)
            if flags & PARAMFLAG_FRETVAL:
                ret = ann
                continue
            pname = names[p + 1] if p + 1 < len(names) else f"arg{p}"
            default = None
            if flags & PARAMFLAG_FHASDEFAULT:
                default = default_literal(ed._.paramdesc)
            elif flags & PARAMFLAG_FOPT:
                default = "..."
            params.append((py_name(pname), ann, default, bool(flags & PARAMFLAG_FOUT)))
        entry = members.setdefault(name, {"doc": doc, "params": params, "ret": ret, "kinds": set()})
        entry["kinds"].add(fd.invkind)
        if fd.invkind in (INVOKE_FUNC, INVOKE_PROPGET):
            entry["params"], entry["ret"] = params, ret
            entry["doc"] = entry["doc"] or doc
    return members


def render_class(lines, cls_name, dotted, doc, members):
    lines.append(f"class {cls_name}:")
    lines.append(f'    """COM: {dotted}' + (f" -- {doc}" if doc else "") + '"""')
    lines.append("    def __init__(self, *args) -> None: ...")
    for name in sorted(members, key=str.lower):
        m = members[name]
        args = []
        for pname, ann, default, is_out in m["params"]:
            args.append(f"{pname}: {ann}" + (f" = {default}" if default is not None else ""))
        signature = f"    def {name}(self, {', '.join(args)}) -> {m['ret']}:"
        notes = []
        if m["doc"]:
            notes.append(m["doc"])
        if INVOKE_PROPGET in m["kinds"]:
            notes.append("property (read" + ("/write" if m["kinds"] & {INVOKE_PROPPUT, INVOKE_PROPPUTREF} else "") + ")")
        if any(is_out for *_, is_out in m["params"]):
            notes.append("has [out] parameters")
        if notes:
            # Docstring inside the method, so Pylance shows it on hover
            text = "; ".join(notes).replace("\\", "\\\\").replace('"""', "'''")
            lines.append(signature)
            lines.append(f'        """{text}"""')
        else:
            lines.append(signature + " ...")
    lines.append("")


def generate(tlb_path, module_doc, wanted, version):
    tl = ti.LoadTypeLibEx(str(tlb_path))
    lib_name = tl.GetDocumentation(-1)[0]
    lines = [f"# Auto-generated — {version} — {lib_name} ({tlb_path.name})", ""]
    if module_doc:
        lines += ['"""', *module_doc.strip("\n").split("\n"), '"""', ""]
    count = 0
    for i in range(tl.GetTypeInfoCount()):
        tinfo = tl.GetTypeInfo(i)
        attr = tinfo.GetTypeAttr()
        iface_name, iface_doc = tl.GetDocumentation(i)[:2]
        if attr.cFuncs == 0 or iface_name not in wanted:
            continue
        render_class(lines, wanted[iface_name], f"{lib_name}.{iface_name}", iface_doc, collect(tinfo))
        count += 1
    return "\n".join(lines), count


INIT_DOC = """
RIB Presto API (COM, ProgID "Presto.App.18") -- reference stubs for PyNET for Presto.

Scripts never import this module: the host injects the application as __presto__, a late-bound
proxy, and calls each member by name. Every member below is called like a method, properties
included:

    app = __presto__
    app.Project()                                   # path of the active obra
    app.FindEqual("Conceptos", "Conceptos.Nat", 0)  # 0 = found

Proxy extras (not in the type library): app._get(name, *index) forces a property read,
app._set(name, value) a property write, app._com.Target is the raw System.__ComObject.

Return-code convention: Find*/GetElement/Open... return 0 on success. Read numeric fields with
GetFieldNum / GetField (GetFieldStr returns None for them). See docs/presto.md and
.claude/commands/PrestoApiPatterns.md for what has been verified.
"""

PRM_DOC = """
Interface a parametric-concept DLL implements for Presto (PrestoPrmCom.tlb). Presto calls it; it
is NOT reachable through __presto__. Reference only, for writing parametric concepts.
"""


def find_bin():
    candidates = []
    for pf in (Path(r"C:\Program Files"), Path(r"C:\Program Files (x86)")):
        for product in pf.glob("Presto*"):
            for ver in product.iterdir() if product.is_dir() else []:
                if (ver / "Bin" / "presto.tlb").is_file():
                    candidates.append(ver / "Bin")
    # Prefer the full product over the Demo, then the newest version
    candidates.sort(key=lambda p: ("Demo" not in p.parent.parent.name, p.parent.name))
    return candidates[-1] if candidates else None


def main():
    bin_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else find_bin()
    if bin_dir is None or not (bin_dir / "presto.tlb").is_file():
        print("presto.tlb not found. Pass the Presto Bin folder as the first argument.")
        return 1
    version = f"{bin_dir.parent.parent.name} {bin_dir.parent.name}"

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    text, n = generate(bin_dir / "presto.tlb", INIT_DOC, {"com_presto": "PrestoApplication"}, version)
    (OUT / "__init__.py").write_text(text, encoding="utf-8", newline="\n")
    print(f"__init__.py : {n} class(es)")

    prm = bin_dir / "PrestoPrmCom.tlb"
    if prm.is_file():
        text, n = generate(prm, PRM_DOC, {"IComPrmDllFunction": "ComPrmDllFunction"}, version)
        (OUT / "PrmCom.py").write_text(text, encoding="utf-8", newline="\n")
        print(f"PrmCom.py   : {n} class(es)")

    print(f"written -> {OUT}  ({version})")
    print("Now run: python 01_Scripts/00_utils/IndexStubs.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
