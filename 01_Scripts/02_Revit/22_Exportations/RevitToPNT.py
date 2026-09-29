"""
RevitToPNT — .pnt/IFC export from Revit for the PyNET viewer.

Same package contract as the Navisworks exporter (NavisworksToPNT.py): tessellated IFC4
per model, properties.json (pnt_id → name/model/psets, same pset names and value formatting),
clashes.json with the model list — but no clash data (Revit has no clash tests).

Revit-specific:
  - The user picks a 3D VIEW, not models (like Navisworks' NWC export): host elements visible in
    it (phase filter, design options, hidden elements/categories) and the links visible in it.
    Inside links, visibility is rule-based (not demolished, primary design option) — the
    FilteredElementCollector(doc, viewId, linkId) overload crashed Revit 2027, do not use it.
  - Geometry is written relative to a local origin (float32 precision in the viewer);
    properties["__meta__"]["originOffset"] holds the offset to the true coordinates.
  - Material transparency is exported (glass).
  - One IFC per document: the host, and each linked document. A document linked N times is
    tessellated once (in its own coordinates) and placed N times with each instance's transform;
    every placed copy keeps its own pnt_id and a PNT_Origin pset (Link, LinkFile).
  - Family geometry cache: instances sharing symbol geometry (GetSymbolGeometryId) are
    tessellated once and transformed per instance.
  - Real Revit levels become IfcBuildingStorey → the viewer tree groups Model · Level · Category ·
    Type · Instance.
  - Coordinates: COORDINATES = "shared" (like Navisworks' default Revit NWC export, so a Revit
    .pnt lines up with a Navisworks .pnt of the same model) or "internal".

Pro-only. Geometry (triangulation, family cache, rebar, vertex weld) runs in C#
(Raen.Revit.Pynet.Utils.RevitMeshExtractor, licence-gated); everything else — visibility, links,
properties, colours, IFC writing with ifcopenshell — stays in Python.
"""

import clr
import sys
import uuid
import json
import math
import zipfile
from pathlib import Path
from datetime import datetime
from collections import defaultdict

import numpy as np

try:
    sys.stdout.reconfigure(line_buffering=True)
except Exception:
    pass

clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import (FilteredElementCollector, RevitLinkInstance,  # type: ignore
                               CategoryType, BuiltInCategory, BuiltInParameter, ElementId,
                               StorageType, SpecTypeId, UnitUtils, UnitTypeId, Material, Level, View3D)

import ifcopenshell
import ifcopenshell.guid

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
from System import AppDomain, Environment, IntPtr  # type: ignore
from System.Runtime.InteropServices import Marshal  # type: ignore
from System.Windows.Forms import (Form, Label, ProgressBar, ProgressBarStyle,  # type: ignore
                                   Button, ListBox, GroupBox, SelectionMode, AnchorStyles, Screen, TextBox,
                                   FormBorderStyle, FormStartPosition, FormWindowState,
                                   DialogResult, Application as WinApp)
from System.Drawing import Size, Point, Icon, ContentAlignment  # type: ignore
from System.Threading import Thread, ThreadStart, ApartmentState, ManualResetEvent  # type: ignore
from System.Windows.Forms import Control, MethodInvoker  # type: ignore
from System.Collections.Generic import List  # type: ignore

PYNET_BIN = Path(next(a for a in AppDomain.CurrentDomain.GetAssemblies()
                      if a.GetName().Name == "Raen.Core.Pynet.Engine").Location).parent
FORM_ICON = PYNET_BIN.parent.parent / "Revit.ico"

# "shared": Revit shared coordinates (survey), like Navisworks' default NWC export.
# "internal": Revit internal origin.
COORDINATES = "shared"

# Face.Triangulate level of detail, 0..1 (Revit's own default is 0.5-ish; higher = more triangles).
TRIANGULATE_LOD = 0.5

# Non-physical or annotation-like model categories that must not reach the viewer. Model groups
# too: their members are exported as elements of their own.
_SKIP_BICS = [
    BuiltInCategory.OST_Rooms, BuiltInCategory.OST_MEPSpaces, BuiltInCategory.OST_Areas,
    BuiltInCategory.OST_Lines, BuiltInCategory.OST_RoomSeparationLines,
    BuiltInCategory.OST_MEPSpaceSeparationLines, BuiltInCategory.OST_AreaSchemeLines,
    BuiltInCategory.OST_Cameras, BuiltInCategory.OST_Mass, BuiltInCategory.OST_SketchLines,
    BuiltInCategory.OST_Levels, BuiltInCategory.OST_Grids, BuiltInCategory.OST_ProjectBasePoint,
    BuiltInCategory.OST_SharedBasePoint, BuiltInCategory.OST_IOSModelGroups, BuiltInCategory.OST_Viewers,
    BuiltInCategory.OST_LegendComponents,
]

FT_TO_M = UnitUtils.ConvertFromInternalUnits(1.0, UnitTypeId.Meters)
_DEFAULT_COLOR = (0.75, 0.75, 0.75, 0.0)   # r, g, b, transparency (0..1)

_ES = "Spanish" in str(__revit__.Application.Language)  # type: ignore  # noqa: F821
# Pset names follow what the Navisworks exporter writes for a Revit element (the viewer keys
# the tree's Category and Element ID on them) — Spanish or English by the host language.
PS_INSTANCE = "Componente" if _ES else "Component"
PS_TYPE     = "Tipo" if _ES else "Type"
PS_ELEMID   = "ID de elemento" if _ES else "Element ID"
PS_ITEM     = "Elemento" if _ES else "Item"
PS_PROJECT  = "Proyecto" if _ES else "Project"
K_NAME, K_TYPE, K_FAMILY, K_CATEGORY = ("Nombre", "Tipo", "Familia", "Categoría") if _ES else \
                                       ("Name", "Type", "Family", "Category")
K_VALUE     = "Valor" if _ES else "Value"
K_CAT_ID    = "Id. de categoría" if _ES else "Category Id"
K_WORKSET   = "Subproyecto" if _ES else "Workset"
K_LAYER     = "Capa" if _ES else "Layer"
K_SOURCE    = "Archivo de origen" if _ES else "Source File"
YES, NO     = ("Sí", "No") if _ES else ("Yes", "No")
NO_LEVEL    = "<Sin nivel>" if _ES else "<No level>"


# ─── Orientation estimator (same as the Navisworks exporter) ──────────────────

class OrientationEstimator:
    def __init__(self, max_samples: int = 300_000):
        self.n = 0
        self.sx = self.sy = self.sxx = self.syy = self.sxy = 0.0
        self._max = max_samples

    def add(self, verts: np.ndarray) -> None:
        if self.n >= self._max or len(verts) == 0:
            return
        v = verts[: self._max - self.n]
        x, y = v[:, 0], v[:, 1]
        self.sx += float(x.sum()); self.sy += float(y.sum())
        self.sxx += float((x * x).sum()); self.syy += float((y * y).sum()); self.sxy += float((x * y).sum())
        self.n += len(v)

    def angle_deg(self) -> float:
        if self.n < 10:
            return 0.0
        mx = self.sx / self.n; my = self.sy / self.n
        cxx = self.sxx / self.n - mx * mx
        cyy = self.syy / self.n - my * my
        cxy = self.sxy / self.n - mx * my
        deg = math.degrees(0.5 * math.atan2(2 * cxy, cxx - cyy))
        return round(((deg + 45.0) % 90.0) - 45.0, 3)


# ─── Progress Window ──────────────────────────────────────────────────────────

class ProgressWindow:
    """Progress dialog with an indeterminate (marquee) bar, a phase + detail line and Cancel.

    It runs on its OWN STA thread with its own message loop. The export runs synchronously on
    the host's thread, so a dialog living there only repaints when the code yields (DoEvents) —
    the bar looked frozen for the whole of any long call (e.g. writing the IFC). On its own
    thread the marquee animates by itself.

    No Python ever runs on the dialog thread after it is built (except the Cancel click): texts
    are set straight from the export thread (a cross-thread WM_SETTEXT handled by .NET), so the
    dialog never waits for the GIL while the export is inside a long native call.
    Cancel is checked by the export between elements/models.

    NEVER call the Revit/Navisworks API from this class (event handlers included): it runs
    outside the host's API context. The export stays on the host thread; the dialog only
    shows text and raises the `cancelled` flag.
    """

    def __init__(self, title: str):
        self.cancelled = False
        self._title = title
        self._form = None
        self._ready = ManualResetEvent(False)
        Control.CheckForIllegalCrossThreadCalls = False
        self._thread = Thread(ThreadStart(self._ui))
        self._thread.SetApartmentState(ApartmentState.STA)
        self._thread.IsBackground = True
        self._thread.Start()
        self._ready.WaitOne(5000)

    def _ui(self):
        try:
            f = Form()
            f.Text            = "PNT exporter"
            f.ClientSize      = Size(560, 150)
            f.FormBorderStyle = FormBorderStyle.FixedDialog
            f.MaximizeBox     = False
            f.MinimizeBox     = False
            f.StartPosition   = FormStartPosition.CenterScreen
            f.TopMost         = True
            if FORM_ICON.exists():
                f.Icon = Icon(str(FORM_ICON))

            self._lbl_phase = Label()
            self._lbl_phase.Text, self._lbl_phase.Left, self._lbl_phase.Top = self._title, 16, 12
            self._lbl_phase.Width, self._lbl_phase.Height, self._lbl_phase.AutoEllipsis = 528, 26, True
            self._lbl_detail = Label()
            self._lbl_detail.Text, self._lbl_detail.Left, self._lbl_detail.Top = "", 16, 42
            self._lbl_detail.Width, self._lbl_detail.Height, self._lbl_detail.AutoEllipsis = 528, 26, True

            bar = ProgressBar()
            bar.Left, bar.Top, bar.Width, bar.Height = 16, 76, 528, 18
            bar.Style = ProgressBarStyle.Marquee
            bar.MarqueeAnimationSpeed = 30

            self._btn_cancel = Button()
            self._btn_cancel.Text, self._btn_cancel.Width, self._btn_cancel.Height = "Cancel", 90, 30
            self._btn_cancel.Left, self._btn_cancel.Top = 528 + 16 - 90, 106
            self._btn_cancel.Click += self._on_cancel

            for ctrl in (self._lbl_phase, self._lbl_detail, bar, self._btn_cancel):
                f.Controls.Add(ctrl)
            self._form = f
            f.Shown += lambda s, e: self._ready.Set()
            WinApp.Run(f)
        except Exception as ex:   # never let an exception escape a host thread — it kills the host
            print(f"  (progress window unavailable: {ex})")
        finally:
            self._ready.Set()

    def _on_cancel(self, sender, args):
        self.cancelled = True
        self._btn_cancel.Enabled = False
        self._btn_cancel.Text = "Cancelling..."

    def update(self, phase: str = None, detail: str = None, pct: float = None):
        """pct is accepted for call-site compatibility; the bar is indeterminate."""
        if self._form is None:
            return
        try:
            if phase is not None:
                self._lbl_phase.Text = phase
            if detail is not None:
                self._lbl_detail.Text = str(detail)
        except Exception:
            pass

    def close(self):
        if self._form is None:
            return
        try:
            self._form.BeginInvoke(MethodInvoker(self._form.Close))
            self._thread.Join(3000)
        except Exception:
            pass


# ─── View Selection Form ──────────────────────────────────────────────────────

class ViewSelectionForm(Form):
    """Pick the 3D view to export. The view decides everything, like Navisworks' NWC export:
    host elements visible in it (phase filter, design options, hidden elements/categories)
    and which links are exported (a link hidden in the view is left out)."""

    def __init__(self, views: list):
        Form.__init__(self)
        self.SelectedView = -1
        self._names = list(views)
        self._visible = []
        if FORM_ICON.exists():
            self.Icon = Icon(str(FORM_ICON))
        self.Text = "PNT exporter"
        self.WindowState = FormWindowState.Normal
        self.TopMost = True

        wa = Screen.PrimaryScreen.WorkingArea
        width, height = min(760, wa.Width - 40), min(680, wa.Height - 40)
        self.Width, self.Height = width, height
        self.MinimumSize = Size(min(400, width), min(300, height))
        self.FormBorderStyle = FormBorderStyle.Sizable
        self.MaximizeBox = True
        self.CenterToScreen()
        button_y = self.ClientSize.Height - 32 - 20

        label = Label()
        label.Text = "Select the 3D view to export to .pnt/IFC (host + visible links):"
        label.Location = Point(20, 10)
        label.Width, label.Height = self.ClientSize.Width - 40, 26
        label.Anchor = AnchorStyles.Left | AnchorStyles.Right | AnchorStyles.Top
        self.Controls.Add(label)

        # Filter: right-aligned, one third of the group's width.
        group_w = self.ClientSize.Width - 40
        filter_w = group_w // 3
        filter_x = 20 + group_w - filter_w
        self._filter = TextBox()
        self._filter.Location = Point(filter_x, 40)
        self._filter.Width = filter_w
        self._filter.Anchor = AnchorStyles.Right | AnchorStyles.Top
        self._filter.TextChanged += self._apply_filter
        self.Controls.Add(self._filter)
        filter_label = Label()
        filter_label.Text = "Filter:"
        filter_label.TextAlign = ContentAlignment.MiddleRight
        filter_label.Location = Point(filter_x - 70, 40)
        filter_label.Width, filter_label.Height = 65, 26
        filter_label.Anchor = AnchorStyles.Right | AnchorStyles.Top
        self.Controls.Add(filter_label)

        group_bottom = button_y - 15
        self._list = ListBox()
        self._list.Location = Point(50, 102)
        self._list.Width = self.ClientSize.Width - 80
        self._list.Height = max(100, group_bottom - 10 - 102)
        self._list.Anchor = AnchorStyles.Left | AnchorStyles.Right | AnchorStyles.Top | AnchorStyles.Bottom
        self._list.SelectionMode = SelectionMode.One
        self._list.HorizontalScrollbar = True
        self._list.DoubleClick += self._on_export
        self._apply_filter(None, None)   # no view preselected — the user picks one
        self.Controls.Add(self._list)

        for text, x, handler in (("Cancel", 240, self._on_cancel), ("Export", 120, self._on_export)):
            btn = Button()
            btn.Text, btn.Width, btn.Height = text, 110, 32
            btn.Location = Point(self.ClientSize.Width - x, button_y)
            btn.Anchor = AnchorStyles.Right | AnchorStyles.Bottom
            btn.Click += handler
            self.Controls.Add(btn)

        group = GroupBox()
        group.Text = "3D views"
        group.Size = Size(self.ClientSize.Width - 40, max(150, group_bottom - 72))
        group.Location = Point(20, 72)
        group.Anchor = AnchorStyles.Left | AnchorStyles.Right | AnchorStyles.Top | AnchorStyles.Bottom
        group.Parent = self

    def _apply_filter(self, sender, args):
        text = (self._filter.Text or "").strip().lower()
        chosen = self._visible[self._list.SelectedIndex] if self._list.SelectedIndex >= 0 else -1
        self._list.BeginUpdate()
        self._list.Items.Clear()
        self._visible = [i for i, n in enumerate(self._names) if text in n.lower()]
        for pos, i in enumerate(self._visible):
            self._list.Items.Add(self._names[i])
            if i == chosen:
                self._list.SelectedIndex = pos
        self._list.EndUpdate()

    def _on_export(self, sender, args):
        if self._list.SelectedIndex < 0:
            return
        self.SelectedView = self._visible[int(self._list.SelectedIndex)]
        self.DialogResult = DialogResult.OK
        self.Close()

    def _on_cancel(self, sender, args):
        self.SelectedView = -1
        self.DialogResult = DialogResult.Cancel
        self.Close()


# ─── Transforms (row-vector: p' = p @ A + o) ──────────────────────────────────

def _tf(t):
    """Revit Transform → (A 3x3, o 3)."""
    bx, by, bz, o = t.BasisX, t.BasisY, t.BasisZ, t.Origin
    return (np.array([[bx.X, bx.Y, bx.Z], [by.X, by.Y, by.Z], [bz.X, bz.Y, bz.Z]]),
            np.array([o.X, o.Y, o.Z]))


def _compose(inner, outer):
    """Apply `inner` first, then `outer`."""
    a1, o1 = inner
    a2, o2 = outer
    return a1 @ a2, o1 @ a2 + o2


_IDENTITY = (np.eye(3), np.zeros(3))


# ─── Property formatting (same output as the Navisworks exporter) ─────────────

def _num(x: float, decimals: int) -> str:
    s = f"{x:.{decimals}f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


class PropertyReader:
    """Instance / type parameters → {pset: {name: display string}}. Lengths/areas/volumes in
    m / m² / m³, angles in °, Yes/No, element references by name. Empty parameters kept ("")."""

    def __init__(self):
        self._elem_names = {}

    def _ref_name(self, doc, eid) -> str:
        key = (doc.PathName or doc.Title, str(eid))
        if key not in self._elem_names:
            e = doc.GetElement(eid)
            self._elem_names[key] = (e.Name or "") if e is not None else ""
        return self._elem_names[key]

    def value(self, p, doc):
        try:
            st = p.StorageType
            if st == StorageType.String:
                return p.AsString() or ""
            if not p.HasValue:
                return ""
            if st == StorageType.ElementId:
                eid = p.AsElementId()
                if eid is None or eid == ElementId.InvalidElementId:
                    return ""
                # AsValueString is what Revit shows (e.g. "Familia" → family name, not the type
                # the id points to); the referenced element's name only as a fallback.
                return p.AsValueString() or self._ref_name(doc, eid) or str(eid)
            dt = p.Definition.GetDataType()
            if st == StorageType.Integer:
                if dt.Equals(SpecTypeId.Boolean.YesNo):
                    return YES if p.AsInteger() else NO
                return p.AsValueString() or str(p.AsInteger())
            if st == StorageType.Double:
                v = p.AsDouble()
                if dt.Equals(SpecTypeId.Length):
                    return _num(UnitUtils.ConvertFromInternalUnits(v, UnitTypeId.Meters), 3) + " m"
                if dt.Equals(SpecTypeId.Area):
                    return _num(UnitUtils.ConvertFromInternalUnits(v, UnitTypeId.SquareMeters), 3) + " m²"
                if dt.Equals(SpecTypeId.Volume):
                    return _num(UnitUtils.ConvertFromInternalUnits(v, UnitTypeId.CubicMeters), 3) + " m³"
                if dt.Equals(SpecTypeId.Angle):
                    return _num(UnitUtils.ConvertFromInternalUnits(v, UnitTypeId.Degrees), 2) + "°"
                return p.AsValueString() or _num(v, 6)
            return p.AsValueString() or ""
        except Exception:
            return None

    def params(self, el, doc) -> dict:
        out = {}
        for p in el.Parameters:
            try:
                name = p.Definition.Name
            except Exception:
                continue
            v = self.value(p, doc)
            if v is not None and name not in out:
                out[name] = v
        return dict(sorted(out.items()))


# ─── Geometry extraction ──────────────────────────────────────────────────────

def _csharp_extractor():
    """RevitMeshExtractor from the running PyNET Revit plugin (≥ 2.2). The exporter is a Pro
    feature: the licence is checked inside the C# constructor, and there is deliberately NO Python
    geometry fallback — it would bypass that check. A refusal propagates to the user as is."""
    name = next((a.GetName().Name for a in AppDomain.CurrentDomain.GetAssemblies()
                 if a.GetName().Name.lower().startswith("raen.revit.pynet.20")), None)
    if name is not None:
        clr.AddReference(name)
        try:
            from Raen.Revit.Pynet.Utils import RevitMeshExtractor  # type: ignore
            ext = RevitMeshExtractor()
            ext.TriangulateLod = TRIANGULATE_LOD
            return ext
        except ImportError:
            pass
    raise RuntimeError("The PNT exporter needs the PyNET Revit plugin 2.2 or later. "
                       "Update PyNET and try again.")


def _np_from_net(arr, dtype) -> np.ndarray:
    """.NET double[]/int[] → numpy in one memory copy (element-by-element iteration through
    pythonnet would cost as much as the triangulation done in C#)."""
    n = arr.Length
    out = np.empty(n, dtype=dtype)
    if n:
        Marshal.Copy(arr, 0, IntPtr(out.ctypes.data), n)
    return out


class GeometryReader:
    """Element geometry → {material key: (verts ndarray feet, faces ndarray 0-based)} in the
    element document's coordinates, computed by the C# RevitMeshExtractor: Face.Triangulate per
    face (null faces skipped), family symbol cache (SymbolGeometryId), rebar via
    GetFullGeometryForView, vertices welded per material. Validated identical to the former
    Python implementation (2,000 Snowdon elements: same vertices/triangles, max dev 1e-14 ft)."""

    def __init__(self):
        self._cs = _csharp_extractor()

    @property
    def cache_hits(self) -> int:
        return int(self._cs.CacheHits)

    def element_meshes(self, el, rebar_view=None) -> dict:
        return {str(part.MaterialId): (_np_from_net(part.Vertices, np.float64).reshape(-1, 3),
                                       _np_from_net(part.Faces, np.int32).reshape(-1, 3).astype(np.int64))
                for part in self._cs.Extract(el, rebar_view)}


class MaterialColors:
    def __init__(self):
        self._cache = {}

    def color(self, doc, mat_key: str, el):
        key = (doc.PathName or doc.Title, mat_key, None if mat_key != "-1" else str(el.Category.Id))
        if key in self._cache:
            return self._cache[key]
        rgb, name = None, ""
        try:
            mat = doc.GetElement(ElementId(int(mat_key))) if mat_key != "-1" else None
            if mat is None and el.Category is not None:
                mat = el.Category.Material
            if isinstance(mat, Material):
                name = mat.Name
                c = mat.Color
                if c.IsValid:   # Transparency 0..100 → 0..1 (glass is usually 100 in Revit)
                    rgb = (c.Red / 255.0, c.Green / 255.0, c.Blue / 255.0, min(0.9, mat.Transparency / 100.0))
        except Exception:
            pass
        self._cache[key] = (rgb or _DEFAULT_COLOR, name)
        return self._cache[key]


# ─── Element extraction per document ──────────────────────────────────────────

class DocumentExtractor:
    """Every exportable model element of one document, with meshes in that document's
    coordinates (feet) and its psets. Link placements reuse this result."""

    def __init__(self, geo: GeometryReader, props: PropertyReader, colors: MaterialColors):
        self._geo, self._props, self._colors = geo, props, colors
        self._skip_cats = {str(ElementId(b)) for b in _SKIP_BICS}

    def _exportable(self, el) -> bool:
        try:
            cat = el.Category
            if cat is None or cat.CategoryType != CategoryType.Model:
                return False
            return str(cat.Id) not in self._skip_cats and not isinstance(el, RevitLinkInstance)
        except Exception:
            return False

    @staticmethod
    def _rule_visible(el) -> bool:
        """Visibility without a view (linked documents): not demolished, and not in a secondary
        design option — what a typical 3D view shows."""
        try:
            p = el.get_Parameter(BuiltInParameter.PHASE_DEMOLISHED)
            if p is not None and p.AsElementId() != ElementId.InvalidElementId:
                return False
            opt = el.DesignOption
            if opt is not None and not opt.IsPrimary:
                return False
        except Exception:
            pass
        return True

    def extract(self, doc, progress, label: str, view=None) -> list:
        """view: a 3D view of THIS document — only what it shows is exported (phase filter,
        design options, hidden elements/categories). None → rule-based visibility (links)."""
        if view is not None:
            col = FilteredElementCollector(doc, view.Id).WhereElementIsNotElementType().WhereElementIsViewIndependent()
            els = [e for e in col if self._exportable(e)]
        else:
            col = FilteredElementCollector(doc).WhereElementIsNotElementType().WhereElementIsViewIndependent()
            els = [e for e in col if self._exportable(e) and self._rule_visible(e)]
        levels = {str(lv.Id): (lv.Name, lv.Elevation * FT_TO_M)
                  for lv in FilteredElementCollector(doc).OfClass(Level)}
        n = len(els)
        # 3D view of THIS document for rebar geometry: the export view for the host, the first
        # non-template 3D view of the linked document otherwise.
        rebar_view = view if view is not None else next(
            (v for v in FilteredElementCollector(doc).OfClass(View3D) if not v.IsTemplate), None)
        print(f"  {n} candidate elements")
        out, failed = [], []
        step = max(1, n // 10)
        for i, el in enumerate(els, 1):
            if progress.cancelled:
                break
            if i % step == 0 or i == n:
                pct = 100.0 * i / n
                print(f"  {label}: {i}/{n} ({pct:.0f}%)")
                progress.update(detail=f"{label}: {i}/{n} elements", pct=pct)
            try:
                meshes = self._geo.element_meshes(el, rebar_view)
            except Exception as ex:   # never drop an element silently — report it at the end
                failed.append((str(el.Id), el.Category.Name if el.Category else "", repr(ex)[:120]))
                continue
            if not meshes:
                continue
            sub, mat_name = [], ""
            for mat_key, (v, f) in meshes.items():
                rgb, mname = self._colors.color(doc, mat_key, el)
                mat_name = mat_name or mname
                sub.append((v, f, rgb))
            out.append({
                "el": el,
                "name": self._display_name(doc, el),
                "sub": sub,
                "mat": mat_name,
                "level": self._level(el, levels),
                "psets": self._element_psets(el, doc),
            })
        if failed:
            print(f"  WARNING: {len(failed)} element(s) skipped by geometry errors:")
            for eid, cat, err in failed[:20]:
                print(f"    {eid} ({cat}): {err}")
        return out

    @staticmethod
    def _display_name(doc, el) -> str:
        t = doc.GetElement(el.GetTypeId())
        return (t.Name if t is not None else "") or el.Name or "element"

    @staticmethod
    def _level(el, levels: dict):
        lid = None
        try:
            if el.LevelId is not None and el.LevelId != ElementId.InvalidElementId:
                lid = el.LevelId
        except Exception:
            pass
        if lid is None:
            for bip in (BuiltInParameter.INSTANCE_REFERENCE_LEVEL_PARAM,
                        BuiltInParameter.FAMILY_LEVEL_PARAM,
                        BuiltInParameter.SCHEDULE_LEVEL_PARAM):
                p = el.get_Parameter(bip)
                if p is not None and p.AsElementId() != ElementId.InvalidElementId:
                    lid = p.AsElementId()
                    break
        if lid is not None and str(lid) in levels:
            return levels[str(lid)]
        return (NO_LEVEL, None)

    @staticmethod
    def _workset(doc, el) -> str:
        try:
            if doc.IsWorkshared:
                ws = doc.GetWorksetTable().GetWorkset(el.WorksetId)
                return ws.Name if ws is not None else ""
        except Exception:
            pass
        return ""

    def _element_psets(self, el, doc) -> dict:
        t = doc.GetElement(el.GetTypeId())
        cat = el.Category.Name if el.Category is not None else ""
        family = ""
        try:
            family = t.FamilyName if t is not None else ""
        except Exception:
            pass
        cat_id = str(el.Category.Id) if el.Category is not None else ""
        workset = self._workset(doc, el)
        # Header fields first (same as the Navisworks "Componente"/"Tipo" psets); parameters never
        # overwrite them.
        inst = {K_NAME: t.Name if t is not None else el.Name, K_TYPE: t.Name if t is not None else "",
                K_FAMILY: family, K_CATEGORY: cat, K_CAT_ID: cat_id, "Id": str(el.Id)}
        if workset:
            inst[K_WORKSET] = workset
        for k, v in self._props.params(el, doc).items():
            inst.setdefault(k, v)
        psets = {PS_INSTANCE: inst}
        if t is not None:
            tp = {K_NAME: t.Name, K_CATEGORY: cat, K_CAT_ID: cat_id, "Id": str(t.Id)}
            if workset:
                tp[K_WORKSET] = self._workset(doc, t) or workset
            for k, v in self._props.params(t, doc).items():
                tp.setdefault(k, v)
            psets[PS_TYPE] = tp
        psets[PS_ELEMID] = {K_VALUE: str(el.Id)}
        return psets


# ─── IFC Writer ───────────────────────────────────────────────────────────────

class IFCWriter:
    """IFC4 with tessellated geometry, colours, materials, one IfcBuildingStorey per Revit level
    and a PNT_Identity pset carrying the pnt_id."""

    def __init__(self, project_name: str):
        self._ifc = ifcopenshell.file(schema="IFC4")
        self._pending = defaultdict(list)
        self._materials = {}
        self._storeys = {}
        self._build_skeleton(project_name)

    def add_element(self, name: str, sub_meshes: list, mat_name: str, pnt_id: str, level):
        tri_sets = []
        for verts, faces, color in sub_meshes:
            if len(verts) == 0 or len(faces) == 0:
                continue
            coords = self._ifc.createIfcCartesianPointList3D(tuple(tuple(map(float, v)) for v in verts))
            idx = tuple(tuple(int(i) for i in f) for f in faces)
            tri = self._ifc.createIfcTriangulatedFaceSet(coords, None, None, idx, None)
            if color is not None:
                self._apply_color(tri, *color)
            tri_sets.append(tri)
        if not tri_sets:
            return False
        shape = self._ifc.createIfcShapeRepresentation(self._body_ctx, "Body", "Tessellation", tri_sets)
        geo = self._ifc.createIfcProductDefinitionShape(None, None, [shape])
        elem = self._ifc.createIfcBuildingElementProxy(
            ifcopenshell.guid.compress(pnt_id), None, name, None, None, self._world_placement(), geo, None)
        self._add_pnt_identity(elem, pnt_id)
        if mat_name:
            self._associate_material(elem, mat_name)
        self._pending[self._storey(*level)].append(elem)
        return True

    def save(self, path: Path) -> Path:
        for storey, elems in self._pending.items():
            self._ifc.createIfcRelContainedInSpatialStructure(self._guid(), None, None, None, elems, storey)
        self._ifc.write(str(path))
        return path

    def _storey(self, name: str, elevation):
        if name not in self._storeys:
            st = self._ifc.createIfcBuildingStorey(
                self._guid(), None, name, None, None, self._world_placement(), None, None,
                "ELEMENT", float(elevation) if elevation is not None else None)
            self._ifc.createIfcRelAggregates(self._guid(), None, None, None, self._building, [st])
            self._storeys[name] = st
        return self._storeys[name]

    def _guid(self) -> str:
        return ifcopenshell.guid.compress(uuid.uuid4().hex)

    def _pt(self, xyz):
        return self._ifc.createIfcCartesianPoint(list(xyz))

    def _world_placement(self):
        return self._ifc.createIfcLocalPlacement(None, self._ifc.createIfcAxis2Placement3D(self._pt([0.0, 0.0, 0.0]), None, None))

    def _apply_color(self, tri, r, g, b, transparency=0.0):
        colour = self._ifc.createIfcColourRgb(None, r, g, b)
        rendering = self._ifc.createIfcSurfaceStyleRendering(colour, float(transparency), None, None, None, None, None, None, "FLAT")
        style = self._ifc.createIfcSurfaceStyle(None, "BOTH", [rendering])
        self._ifc.createIfcStyledItem(tri, [style], None)

    def _associate_material(self, element, name: str):
        if name not in self._materials:
            self._materials[name] = self._ifc.createIfcMaterial(name, None, None)
        self._ifc.createIfcRelAssociatesMaterial(self._guid(), None, None, None, [element], self._materials[name])

    def _add_pnt_identity(self, element, pnt_id: str):
        prop = self._ifc.createIfcPropertySingleValue("pnt_id", None, self._ifc.createIfcLabel(pnt_id), None)
        pset = self._ifc.createIfcPropertySet(self._guid(), None, "PNT_Identity", None, [prop])
        self._ifc.createIfcRelDefinesByProperties(self._guid(), None, None, None, [element], pset)

    def _build_skeleton(self, name: str):
        units = self._ifc.createIfcUnitAssignment([
            self._ifc.createIfcSIUnit(None, "LENGTHUNIT", None, "METRE"),
            self._ifc.createIfcSIUnit(None, "AREAUNIT", None, "SQUARE_METRE"),
            self._ifc.createIfcSIUnit(None, "VOLUMEUNIT", None, "CUBIC_METRE"),
        ])
        ax2p = self._ifc.createIfcAxis2Placement3D(
            self._pt([0.0, 0.0, 0.0]), self._ifc.createIfcDirection([0.0, 0.0, 1.0]),
            self._ifc.createIfcDirection([1.0, 0.0, 0.0]))
        ctx = self._ifc.createIfcGeometricRepresentationContext(None, "Model", 3, 1.0e-5, ax2p, None)
        self._body_ctx = self._ifc.createIfcGeometricRepresentationSubContext(
            "Body", "Model", None, None, None, None, ctx, None, "MODEL_VIEW", None)
        project = self._ifc.createIfcProject(self._guid(), None, name, None, None, None, None, [ctx], units)
        site = self._ifc.createIfcSite(self._guid(), None, "Site", None, None, self._world_placement(),
                                       None, None, "ELEMENT", None, None, None, None, None)
        self._building = self._ifc.createIfcBuilding(self._guid(), None, "Building", None, None,
                                                     self._world_placement(), None, None, "ELEMENT", None, None, None)
        self._ifc.createIfcRelAggregates(self._guid(), None, None, None, project, [site])
        self._ifc.createIfcRelAggregates(self._guid(), None, None, None, site, [self._building])


# ─── Export Manager ───────────────────────────────────────────────────────────

class ExportManager:

    def __init__(self, doc, sources: list, selected: list, view=None):
        self._doc = doc
        self._view = view
        self._sources = [sources[i] for i in selected]
        self._out_path = self._output_path(doc)
        self._tmp = self._out_path.parent / "_pnt_tmp"
        try:
            self._tmp.mkdir(parents=True, exist_ok=True)
        except OSError:  # read-only model folder (e.g. Revit's own Samples under Program Files)
            self._out_path = self._desktop() / self._out_path.name
            self._tmp = self._out_path.parent / "_pnt_tmp"
            self._tmp.mkdir(parents=True, exist_ok=True)
        to_shared = _IDENTITY
        if COORDINATES == "shared":
            # ProjectLocation total transform: shared → internal; its inverse takes internal → shared.
            to_shared = _tf(doc.ActiveProjectLocation.GetTotalTransform().Inverse)
        self._to_world = to_shared
        # Local origin: the viewer draws in float32 — at shared (UTM-like) coordinates of ~4e5 m
        # a vertex can only land every ~3 cm (jagged edges, z-fighting). Geometry is written
        # relative to the host's internal origin expressed in the chosen system, rounded to 1 m;
        # the offset goes to properties["__meta__"]["originOffset"] to recover true coordinates.
        self._offset_m = np.round(to_shared[1] * FT_TO_M)

    @staticmethod
    def _desktop() -> Path:
        return Path(Environment.GetFolderPath(Environment.SpecialFolder.Desktop))   # OneDrive-safe

    @classmethod
    def _output_path(cls, doc) -> Path:
        p = doc.PathName or ""
        if p and Path(p).parent.exists():
            base = Path(p)
        else:  # unsaved or cloud model
            base = cls._desktop() / (doc.Title or "project")
        return base.parent / f"{Path(base.name).stem}.pnt"

    def run(self) -> Path:
        t_total = datetime.now()
        progress = ProgressWindow(f"{self._out_path.stem} ({len(self._sources)} model(s))")
        try:
            return self._run(progress, t_total)
        finally:
            progress.close()

    def _run(self, progress, t_total) -> Path:
        n = len(self._sources)
        print(f"━━━ PNT/IFC Export (Revit) — {n} model(s), {COORDINATES} coordinates ━━━")
        geo, props, colors = GeometryReader(), PropertyReader(), MaterialColors()
        extractor = DocumentExtractor(geo, props, colors)
        orient = OrientationEstimator()
        ifc_files, model_infos, properties = [], [], {}
        stems = self._unique_stems()

        for pos, src in enumerate(self._sources, 1):
            if progress.cancelled:
                print(f"\nExport cancelled by user before model {pos}/{n}.")
                break
            sdoc, stem = src["doc"], stems[pos - 1]
            print(f"\n[{pos}/{n}] {stem}")
            progress.update(phase=f"{stem} — extracting geometry", detail="", pct=0)
            t0 = datetime.now()
            records = extractor.extract(sdoc, progress, stem,
                                        self._view if sdoc.Equals(self._doc) else None)
            print(f"  {len(records)} elements with geometry in {(datetime.now() - t0).total_seconds():.1f}s"
                  f" ({geo.cache_hits} family geometry reuses so far)")
            if not records:
                print("  No geometry — skipping")
                continue

            progress.update(phase=f"{stem} — writing IFC", detail="")
            t0 = datetime.now()
            writer = IFCWriter(stem)
            placements = src["placements"]   # [(link instance or None, transform to host internal)]
            written = 0
            for inst, inst_tf in placements:
                a, o = _compose(inst_tf, self._to_world)
                inst_uid = inst.UniqueId if inst is not None else ""
                for r in records:
                    sub = []
                    for v, f, rgb in r["sub"]:
                        w = (v @ a + o) * FT_TO_M - self._offset_m
                        orient.add(w)
                        sub.append((w, f + 1, rgb))   # 1-based for IFC
                    pnt_id = uuid.uuid5(uuid.NAMESPACE_URL, f"{sdoc.Title}|{inst_uid}|{r['el'].UniqueId}").hex
                    psets = dict(r["psets"])
                    psets[PS_ITEM] = {"GUID": r["el"].UniqueId, K_LAYER: r["level"][0], K_SOURCE: sdoc.Title}
                    if inst is not None:
                        psets["PNT_Origin"] = {"Link": inst.Name, "LinkFile": sdoc.PathName or sdoc.Title}
                    if writer.add_element(r["name"], sub, r["mat"], pnt_id, r["level"]):
                        written += 1
                        properties[pnt_id] = {"pnt_id": pnt_id, "name": r["name"], "model": stem, "psets": psets}
            ifc_path = writer.save(self._tmp / f"{stem}.ifc")
            print(f"  → {written} elements ({len(placements)} placement(s)), "
                  f"{ifc_path.stat().st_size / 1_048_576:.1f} MB IFC in {(datetime.now() - t0).total_seconds():.1f}s")

            ifc_files.append(ifc_path)
            model_infos.append({"name": stem, "fileName": f"{stem}.ifc", "fullPath": sdoc.PathName or sdoc.Title})
            properties[f"m_{stem}"] = {"pnt_id": f"m_{stem}", "name": stem, "model": stem,
                                       "psets": self._root_psets(sdoc)}

        view_rotation = orient.angle_deg()
        print(f"\n  View rotation (PCA estimate): {view_rotation}°  ({orient.n} sampled vertices)")
        properties["__meta__"] = {"viewRotationDeg": view_rotation, "coordinates": COORDINATES,
                                  "originOffset": [float(x) for x in self._offset_m],
                                  "view": self._view.Name if self._view is not None else None}

        clash_data = {
            "models": model_infos, "tests": [], "clashes": [], "classification": [],
            "summary": {"totalClashes": 0, "activeTests": 0, "totalModels": len(model_infos)},
        }
        manifest = {
            "version": "1.0", "format": "pnt-ifc", "source": "revit", "project": self._out_path.stem,
            "created": datetime.now().isoformat(), "models": [m["fileName"] for m in model_infos],
            "element_count": len(properties), "clash_count": 0,
        }

        print(f"\n━━━ Packaging → {self._out_path.name} ━━━")
        progress.update(phase="Packaging .pnt archive", detail="")
        with zipfile.ZipFile(self._out_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
            z.writestr("manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2))
            z.writestr("clashes.json", json.dumps(clash_data, ensure_ascii=False, indent=2))
            z.writestr("properties.json", json.dumps(properties, ensure_ascii=False, indent=2))
            for f in ifc_files:
                z.write(f, f"models/{f.name}")
        print(f"  → {self._out_path.stat().st_size / 1_048_576:.1f} MB")

        for f in ifc_files:
            try:
                f.unlink()
            except Exception:
                pass
        try:
            self._tmp.rmdir()
        except Exception:
            pass

        m, s = divmod(int((datetime.now() - t_total).total_seconds()), 60)
        print(f"\nDone → {self._out_path}  (total {m}m {s}s)")
        return self._out_path

    def _unique_stems(self) -> list:
        seen, stems = defaultdict(int), []
        for src in self._sources:
            base = src["stem"]
            seen[base] += 1
            stems.append(base if seen[base] == 1 else f"{base}_{seen[base]}")
        return stems

    @staticmethod
    def _root_psets(sdoc) -> dict:
        project = {}
        try:
            project = PropertyReader().params(sdoc.ProjectInformation, sdoc)
        except Exception:
            pass
        item = {K_NAME: sdoc.Title, K_SOURCE: sdoc.PathName or sdoc.Title}
        return {PS_ITEM: item, PS_PROJECT: {k: v for k, v in project.items() if v != ""}}


# ─── Sources: host + linked documents ─────────────────────────────────────────

def collect_sources(doc, view) -> list:
    """Host document + each loaded linked document visible in `view` (with all its visible
    placements). A link is left out when its instance or the RVT Links category is hidden."""
    sources = [{"label": f"{doc.Title} (host)", "stem": Path(doc.Title).stem, "doc": doc,
                "placements": [(None, _IDENTITY)]}]
    links_hidden = view.GetCategoryHidden(ElementId(BuiltInCategory.OST_RvtLinks))
    by_doc = {}
    for li in FilteredElementCollector(doc).OfClass(RevitLinkInstance):
        if links_hidden or li.IsHidden(view):
            print(f"  Link hidden in view '{view.Name}', skipped: {li.Name}")
            continue
        ldoc = li.GetLinkDocument()
        if ldoc is None:
            print(f"  Link not loaded, skipped: {li.Name}")
            continue
        key = ldoc.PathName or ldoc.Title
        if key not in by_doc:
            by_doc[key] = {"doc": ldoc, "stem": Path(ldoc.Title).stem, "placements": []}
        by_doc[key]["placements"].append((li, _tf(li.GetTotalTransform())))
    for src in by_doc.values():
        k = len(src["placements"])
        src["label"] = f"{src['doc'].Title} (link" + (f", {k} placements)" if k > 1 else ")")
        sources.append(src)
    return sources


# ─── Entry point ──────────────────────────────────────────────────────────────

doc = __revit__.ActiveUIDocument.Document  # type: ignore  # noqa: F821
views = sorted((v for v in FilteredElementCollector(doc).OfClass(View3D) if not v.IsTemplate), key=lambda v: v.Name)
if not views:
    print("No 3D view in the model — create one ({3D}) and run again.")
else:
    form = ViewSelectionForm([v.Name for v in views])
    if form.ShowDialog() == DialogResult.OK and form.SelectedView >= 0:
        view = views[form.SelectedView]
        sources = collect_sources(doc, view)
        print(f"View '{view.Name}': host + {len(sources) - 1} linked document(s)")
        ExportManager(doc, sources, list(range(len(sources))), view).run()
    else:
        print("Export cancelled.")
