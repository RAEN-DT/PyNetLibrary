"""
NavisworksToPNT — .pnt/IFC export with type-cache and room filter.

Optimizations over the original per-node exporter:
  - Type cache: instances of the same Revit type are tessellated ONCE in local
    space. All subsequent instances just read their transform matrix via
    TriangleMeshCollector.GetMatrix (no GenerateSimplePrimitives).
  - Room/Space filter: Habitaciones, Rooms, Espacios, Spaces skipped entirely.

Requirements:
    pip install ifcopenshell
"""

import clr
import sys
import uuid
import json
import re
import math
import zipfile
from pathlib import Path
from datetime import datetime
from collections import defaultdict

try:
    sys.stdout.reconfigure(line_buffering=True)
except Exception:
    pass

clr.AddReference("Autodesk.Navisworks.Api")
clr.AddReference("Autodesk.Navisworks.ComApi")
clr.AddReference("Autodesk.Navisworks.Interop.ComApi")
clr.AddReference("Autodesk.Navisworks.Clash")

from Autodesk.Navisworks.Api import Application, UnitConversion, Units
from Autodesk.Navisworks.Api.ComApi import ComApiBridge
from Autodesk.Navisworks.Api.Interop.ComApi import InwOaFragment3
from Autodesk.Navisworks.Api.Clash import DocumentClash

# PyNET bundle folder of the RUNNING Navisworks (right year, never hardcoded): the folder
# of the engine assembly executing this script. See docs/navisworks.md "CastUtils".
from System import AppDomain
_bundle = Path(next(a for a in AppDomain.CurrentDomain.GetAssemblies()
               if a.GetName().Name == "Raen.Core.Pynet.Engine").Location).parent
sys.path.append(str(_bundle))

clr.AddReference("Raen.Core.Pynet.Resources")
clr.AddReference(next(a.GetName().Name for a in AppDomain.CurrentDomain.GetAssemblies()
                      if a.GetName().Name.startswith("Raen.Navisworks.Pynet.")))  # year-suffixed plugin

from Raen.Core.Pynet.Resources import CastUtils  # type: ignore
from Raen.Navisworks.Pynet.Utils import TriangleMeshCollector  # type: ignore

import ifcopenshell
import ifcopenshell.guid

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
from System.Windows.Forms import (Form, Label, ProgressBar, ProgressBarStyle,  # type: ignore
                                   Button, ListBox, GroupBox, SelectionMode, AnchorStyles, Screen, TextBox,
                                   FormBorderStyle, FormStartPosition, FormWindowState,
                                   DialogResult, Application as WinApp)
from System.Drawing import Size, Point, Icon, ContentAlignment  # type: ignore
from System.Threading import Thread, ThreadStart, ApartmentState, ManualResetEvent  # type: ignore
from System.Windows.Forms import Control, MethodInvoker  # type: ignore
from System.Collections.Generic import List  # type: ignore

NavisworksinconPath = _bundle.parent.parent / "manage.ico"   # <bundle>/manage.ico


FEET_TO_METERS = 0.3048

# Set to False to skip clash extraction entirely — no tests_summary/clashes in the .pnt at all.
EXPORT_CLASHES = True

# Set to False to export whatever clash results already exist in the document as-is, without
# calling TestsRunAllTests() first — skips the (potentially slow) recomputation. Only meaningful
# when EXPORT_CLASHES is True. Existing tests with no prior run will simply report 0 clashes.
RUN_CLASH_TESTS = False


_SKIP_CATS = {
    "Elemento", "Element",
    "Geometría", "Geometry",
    "TimeLiner",
    "Material de Autodesk", "Autodesk Material",
    "Material",
    "Transformar", "Transform",
    "Identidad", "Identity",
    "Proyecto", "Project",
    "Ubicación", "Location",
    "Orientation", "DemolishedPhaseId", "CreatedPhaseId",
    "Id", "WorksetId", "Document",
}

# Properties are stored in properties.json only — IFC elements carry just the
# PNT_Identity pset (pnt_id) so consumers can cross-reference without bloating
# the IFC files with redundant pset data.
EXPORT_PSETS_IN_IFC = False


# ─── Orientation estimator ────────────────────────────────────────────────────
# Geometry is exported in Navisworks world coordinates, which already carry the model's
# true-north rotation — so the viewer shows the building tilted and its ViewCube "Front"
# lands oblique. We estimate that rotation once (PCA of the XY footprint over a bounded
# vertex sample) and store it in properties["__meta__"], so the viewer can align the
# ViewCube to the building's own axes.

class OrientationEstimator:
    def __init__(self, max_samples: int = 300_000):
        self.n = 0
        self.sx = self.sy = self.sxx = self.syy = self.sxy = 0.0
        self._max = max_samples

    def add(self, verts) -> None:
        if self.n >= self._max:
            return
        for v in verts:
            x = v[0]; y = v[1]
            self.sx += x; self.sy += y
            self.sxx += x * x; self.syy += y * y; self.sxy += x * y
            self.n += 1
            if self.n >= self._max:
                return

    def angle_deg(self) -> float:
        """Principal-axis angle of the footprint, normalised to the smallest rotation that
        aligns the building's orthogonal axes to world X/Y (in [-45, 45] degrees)."""
        if self.n < 10:
            return 0.0
        mx = self.sx / self.n; my = self.sy / self.n
        cxx = self.sxx / self.n - mx * mx
        cyy = self.syy / self.n - my * my
        cxy = self.sxy / self.n - mx * my
        theta = 0.5 * math.atan2(2 * cxy, cxx - cyy)  # radians, principal axis vs +X
        deg = math.degrees(theta)
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
            if NavisworksinconPath.exists():
                f.Icon = Icon(str(NavisworksinconPath))

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


# ─── Model Selection Form ─────────────────────────────────────────────────────

class ModelSelectionForm(Form):
    """
    Lets the user pick which federated model(s) to export, instead of always
    exporting the whole federation in one go. Screen-clamped sizing + AutoScroll
    follow the same pattern fixed in UpdateModels.py / CoordinationWorkflow.py.
    """

    def __init__(self, doc):
        Form.__init__(self)
        self._doc = doc
        self.SelectedIndices = []
        self._configure()
        self._build_list()
        self._build_buttons()
        self._build_group()

    def _configure(self):
        if NavisworksinconPath.exists():
            self.Icon = Icon(str(NavisworksinconPath))
        self.Text = "PNT exporter"
        self.WindowState = FormWindowState.Normal
        self.BringToFront()
        self.Topmost = True

        workingArea = Screen.PrimaryScreen.WorkingArea
        width = min(760, workingArea.Width - 40)
        height = min(680, workingArea.Height - 40)
        self.Width = width
        self.Height = height
        self.MinimumSize = Size(min(400, width), min(300, height))
        self.AutoScroll = True
        self.buttonRowY = self.ClientSize.Height - 32 - 20  # shared Y for the bottom button row
        self.FormBorderStyle = FormBorderStyle.Sizable
        self.MaximizeBox = True
        self.CenterToScreen()

    def _build_list(self):
        label = Label()
        label.Text = "Select one or more models to export to .pnt/IFC:"
        label.Location = Point(20, 10)
        label.Width = self.ClientSize.Width - 40
        label.Height = 20
        label.Anchor = AnchorStyles.Left | AnchorStyles.Right | AnchorStyles.Top
        self.Controls.Add(label)

        # Text filter over the model names; the selection is kept by model index, so filtering
        # never loses what was already picked.
        # Filter: right-aligned, one third of the group's width.
        groupW = self.ClientSize.Width - 40
        filterW = groupW // 3
        filterX = 20 + groupW - filterW
        self._filter = TextBox()
        self._filter.Location = Point(filterX, 40)
        self._filter.Width = filterW
        self._filter.Anchor = AnchorStyles.Right | AnchorStyles.Top
        self._filter.TextChanged += self._apply_filter
        self.Controls.Add(self._filter)
        filterLabel = Label()
        filterLabel.Text = "Filter:"
        filterLabel.TextAlign = ContentAlignment.MiddleRight
        filterLabel.Location = Point(filterX - 70, 40)
        filterLabel.Width, filterLabel.Height = 65, 26
        filterLabel.Anchor = AnchorStyles.Right | AnchorStyles.Top
        self.Controls.Add(filterLabel)

        listBoxY = 102
        groupBoxBottom = self.buttonRowY - 15
        self._listBox = ListBox()
        self._listBox.Location = Point(50, listBoxY)
        self._listBox.Width = self.ClientSize.Width - 80
        self._listBox.Height = max(100, groupBoxBottom - 10 - listBoxY)
        self._listBox.Anchor = AnchorStyles.Left | AnchorStyles.Right | AnchorStyles.Top | AnchorStyles.Bottom
        self._listBox.SelectionMode = SelectionMode.MultiExtended
        self._listBox.HorizontalScrollbar = True

        self._names = [Path(m.FileName).stem for m in self._doc.Models]
        self._visible = []
        self._picked = set()
        self._refreshing = False
        self._listBox.SelectedIndexChanged += self._on_selection
        self.Controls.Add(self._listBox)
        self._apply_filter(None, None)

    def _apply_filter(self, sender, args):
        text = (self._filter.Text or "").strip().lower()
        self._refreshing = True
        self._listBox.BeginUpdate()
        self._listBox.Items.Clear()
        self._visible = [i for i, n in enumerate(self._names) if text in n.lower()]
        for pos, i in enumerate(self._visible):
            self._listBox.Items.Add(self._names[i])
            if i in self._picked:
                self._listBox.SetSelected(pos, True)
        self._listBox.EndUpdate()
        self._refreshing = False

    def _on_selection(self, sender, args):
        if self._refreshing:
            return
        shown = set(self._visible)
        selected = {self._visible[int(k)] for k in self._listBox.SelectedIndices}
        self._picked = (self._picked - shown) | selected

    def _build_group(self):
        groupBoxY = 72
        groupBoxBottom = self.buttonRowY - 15
        groupBox = GroupBox()
        groupBox.Text = "Models to export"
        groupBox.Size = Size(self.ClientSize.Width - 40, max(150, groupBoxBottom - groupBoxY))
        groupBox.Location = Point(20, groupBoxY)
        groupBox.Anchor = AnchorStyles.Left | AnchorStyles.Right | AnchorStyles.Top | AnchorStyles.Bottom
        groupBox.Parent = self

    def _build_buttons(self):
        buttonHeight = 32
        y = self.buttonRowY

        btnCancel = Button()
        btnCancel.Text = "Cancel"
        btnCancel.Width = 110
        btnCancel.Height = buttonHeight
        btnCancel.Location = Point(self.ClientSize.Width - 240, y)
        btnCancel.Anchor = AnchorStyles.Right | AnchorStyles.Bottom
        btnCancel.Click += self._on_cancel
        self.Controls.Add(btnCancel)

        btnExport = Button()
        btnExport.Text = "Export"
        btnExport.Width = 110
        btnExport.Height = buttonHeight
        btnExport.Location = Point(self.ClientSize.Width - 120, y)
        btnExport.Anchor = AnchorStyles.Right | AnchorStyles.Bottom
        btnExport.Click += self._on_export
        self.Controls.Add(btnExport)

    def _on_export(self, sender, args):
        self.SelectedIndices = sorted(self._picked)
        if not self.SelectedIndices:
            return  # nothing picked — stay open rather than exporting nothing
        self.DialogResult = DialogResult.OK
        self.Close()

    def _on_cancel(self, sender, args):
        self.SelectedIndices = []
        self.DialogResult = DialogResult.Cancel
        self.Close()


# ─── Element Extractor ────────────────────────────────────────────────────────

class ElementExtractor:
    """
    Thin Python wrapper around the C# IFCElementExtractor.

    All tree traversal, category routing, type caching, color extraction and
    property serialization happen in C# — this wrapper only converts the flat
    arrays returned by C# into the (name, sub_meshes, mat, props, cx, cy, cz)
    tuple format expected by the rest of the script.

    cx/cy/cz are in native Navisworks feet (returned as-is from C#) so the
    bbox_index lookup still matches clash items.
    """

    _SKIP_CATEGORIES = {
        "Habitaciones", "Rooms", "Room",
        "Espacios", "Spaces", "Space",
        "Líneas", "Lines", "Líneas de modelo", "Model Lines",
        "Líneas de detalle", "Detail Lines",
        "<Separación de espacios>", "<Space Separation>",
    }

    _ALLOW_CATEGORIES = {
        "Muros", "Walls",
        "Suelos", "Floors",
        "Puertas", "Doors",
        "Ventanas", "Windows",
        "Aparatos sanitarios", "Plumbing Fixtures",
        "Mobiliario", "Furniture",
        "Vegetación", "Planting",
        "Muros cortina", "Curtain Walls",
        "Montantes de muro cortina", "Curtain Wall Mullions",
        "Paneles de muro cortina", "Curtain Panels",
        "Cubiertas", "Roofs",
        "Techos", "Ceilings",
        "Pilares", "Columns",
        "Vigas", "Structural Framing",
        "Pavimento", "Paving",
        "Muebles de obra", "Casework",
        "Luminarias", "Lighting Fixtures",
        "Equipos especializados", "Specialty Equipment",
        "Emplazamiento", "Site",
        "Modelos genéricos", "Generic Models",
        "Barandales superiores", "Top Rails",
        "Bordes de losa", "Slab Edges",
        "Equipo de servicios alimentarios", "Food Service Equipment",
        "Aparcamiento", "Parking",
        "Entorno", "Entourage",
        "Circulación vertical", "Vertical Circulation",
        "Rampas", "Ramps",
        "Pasamanos", "Handrails",
        "Barandillas", "Railings",
        "Soportes", "Structural Columns",
        "Escaleras", "Stairs",
        "Barridos de muro", "Wall Sweeps",
        "Conductos", "Ducts",
        "Tuberías", "Pipes",
        "Accesorios de conducto", "Duct Fittings",
        "Accesorios de tubería", "Pipe Fittings",
        "Sistemas de conductos", "Duct Systems",
        "Sistemas de tuberías", "Pipe Systems",
        "Equipamiento mecánico", "Mechanical Equipment",
        "Terminales de aire", "Air Terminals",
        "Equipos de fontanería", "Equipo de fontanería", "Plumbing Equipment",
        "Pilares estructurales", "Structural Columns",
        # ── Discovered via live category audit (Snowdon Towers federated model) ──
        # Spanish category names differ across Revit/Navisworks locales/versions; the
        # names above missed several real MEP/Structural categories entirely (~49% of
        # non-architecture geometry was silently dropped). Adding the variants found live.
        "Aparatos eléctricos", "Electrical Fixtures",
        "Tubos", "Conduits",
        "Uniones de tubo", "Conduit Fittings",
        "Equipos eléctricos", "Electrical Equipment",
        "Dispositivos de iluminación", "Lighting Devices",
        "Dispositivos de datos", "Data Devices",
        "Uniones de conducto",   # duct fittings (elbows/tees) — distinct category, see _INSTNODE_CATS
        "Uniones de tubería",    # pipe fittings (elbows/tees) — distinct category, see _INSTNODE_CATS
        "Accesorios de tuberías",  # pipe accessories (valves etc.) — plural variant of "Accesorios de tubería"
        "Equipos mecánicos",     # variant of "Equipamiento mecánico" (Mechanical Equipment)
        "Conductos flexibles", "Flex Ducts",
        # Re-added — sampled 3 separate "16K6" instances and found IDENTICAL bbox dims,
        # meaning same-Type instances share real local geometry in this model despite
        # CurveDrivenStructural. Testing type-cache (see _INSTNODE_CATS) instead of
        # excluding: one tessellation per Type (20 types) instead of per instance (959).
        "Armazón estructural",
        "Conexiones estructurales", "Structural Connections",
        "Cimentación estructural", "Structural Foundations",
        # "Armadura estructural" (rebar) stays OUT too — re-tested against a clean
        # baseline (Armazón excluded) and still hung/had to be killed. ~76M triangles
        # total (~60,600 avg/element) is not viable via Navisworks' per-triangle COM
        # callback tessellation. Both this and Armazón estructural are the intended
        # first candidates for the future Revit-native swept-solid exporter.
    }

    _FAST_CATS = {
        "Soportes", "Structural Columns",
        "Vegetación", "Planting",
        "Bordes de losa", "Slab Edges",
        "Columnas arquitectónicas", "Columns",
        "Mobiliario", "Furniture",
        "Aparatos sanitarios", "Plumbing Fixtures",
        "Equipamiento mecánico", "Mechanical Equipment",
        "Equipamiento específico", "Specialty Equipment",
        "Vigas", "Structural Framing",
        "Pilares", "Columns",
        "Barandillas", "Railings",
        "Escaleras", "Stairs",
        "Entorno", "Entourage",
        "Circulación vertical", "Vertical Circulation",
        "Rampas", "Ramps",
    }

    _INSTNODE_CATS = {
        "Ventanas", "Windows",
        "Muebles de obra", "Casework",
        "Luminarias", "Lighting Fixtures",
        "Equipo de servicios alimentarios", "Food Service Equipment",
        "Emplazamiento", "Site",
        # Aggressive cache (ratio > 15, user-approved risk) — verify against drift before trusting blindly.
        "Uniones de tubo",              # ratio 29.3 — OST_ConduitFitting, OneLevelBased loadable family
        "Dispositivos de iluminación",  # ratio 17.8
        # "Conexiones estructurales" is NOT here — measured empirically: 5m31s with
        # ApplyTypeCache attempted vs 5m30s forced PERLEAF (no cache) — identical, so
        # the cache silently fails for this WorkPlaneBased family (see _PERLEAF_CATS).
        # Loadable, typed families (per user + confirmed live via Revit API: OneLevelBased
        # placement, discrete catalog types) — same Type = same local geometry, cache is correct.
        "Uniones de conducto",     # OST_DuctFitting (elbows/tees) — ratio 24.3
        "Uniones de tubería",      # OST_PipeFitting (elbows/tees) — ratio 38.4
        "Accesorios de tuberías",  # OST_PipeAccessory (valves) — same OneLevelBased profile — ratio 10.5
        # RE-TEST: IFCElementExtractor's type-cache key now folds in bounding-box dims
        # (typeHash + dims), not just typeHash — 16K6/20K6/16K2 had real length variation
        # within the same Type (17/4/8 distinct dims) that would've cached wrong before
        # this fix. Requires the rebuilt/redeployed Raen.Navisworks.Pynet bundle.
        "Armazón estructural",
        # Real HVAC bottleneck found: "16x4 Connection 8 Diameter Duct" type has 404
        # instances at up to 56,808 tris/instance (526 fragments) — a diffuser+duct-stub
        # assembly, not a simple grille. Was stuck in _PERLEAF_CATS since the start despite
        # a good 14.5x reuse ratio. Safe now with the dims-aware cache key.
        "Terminales de aire",
    }

    _DIRECT_CATS = {
        "Paneles de muro cortina", "Curtain Panels",
        "Montantes de muro cortina", "Curtain Wall Mullions",
        "Muros cortina", "Curtain Walls",
        "Puertas", "Doors",
        "Modelos genéricos", "Generic Models",
        "Aparcamiento", "Parking",
        "Equipos especializados", "Specialty Equipment",
        "Barandales superiores", "Top Rails",
        "Pasamanos", "Handrails",
        "Barridos de muro", "Wall Sweeps",
        "Conductos flexibles",  # adaptive curve shape — never type-cacheable
    }

    _PERLEAF_CATS = {
        "Muros", "Walls",
        "Techos", "Ceilings",
        "Suelos", "Floors",
        "Cubiertas", "Roofs",
        "Conductos", "Ducts",
        "Tuberías", "Pipes",
        "Accesorios de conducto", "Duct Fittings",
        "Accesorios de tubería", "Pipe Fittings",
        "Sistemas de conductos", "Duct Systems",
        "Sistemas de tuberías", "Pipe Systems",
        "Tubos",  # electrical conduit runs — adaptive length, like Conductos/Tuberías
        # "Terminales de aire" moved to _INSTNODE_CATS — was the real HVAC bottleneck.
        # "Armazón estructural" moved to _INSTNODE_CATS — retesting with the dims-aware
        # cache key fix (typeHash + bbox dims) in IFCElementExtractor.cs.
        # OST_StructConnections ("SCN_Embed" etc.) — kept here PERLEAF for now (safe,
        # correctness-first). NOTE: an earlier "type-cache doesn't help" conclusion for
        # this category was WRONG — both compared runs also included Armazón estructural's
        # joists (~29M tris), which dominated and masked any real signal. Re-test INSTNODE
        # for this category later against a clean baseline if the speed matters.
        "Conexiones estructurales",
        # Rebar (round bars) — pathologically dense per-element (~60,600 tris/element avg,
        # up to 114,380 for one bar) but re-included per user call: looks good in the
        # viewer, and worth the time now that Armazón estructural's joists are isolated out.
        "Armadura estructural",
    }

    def __init__(self):
        from Raen.Navisworks.Pynet.Utils import IFCElementExtractor  # type: ignore
        self._ext = IFCElementExtractor()
        for c in self._SKIP_CATEGORIES:
            self._ext.SkipCategories.Add(c)
        for c in self._ALLOW_CATEGORIES:
            self._ext.AllowCategories.Add(c)
        for c in self._FAST_CATS:
            self._ext.FastCats.Add(c)
        for c in self._INSTNODE_CATS:
            self._ext.InstNodeCats.Add(c)
        for c in self._DIRECT_CATS:
            self._ext.DirectCats.Add(c)
        for c in self._PERLEAF_CATS:
            self._ext.PerLeafCats.Add(c)
        for c in _SKIP_CATS:
            self._ext.SkipPropCats.Add(c)

    def extract(self, model_index: int) -> list:
        model = Application.ActiveDocument.Models[model_index]
        raw = self._ext.ExtractModel(model.RootItem)
        # Repeated links (same .rvt placed N times) are tessellated once in C#; the stats are
        # optional so an older plugin build without them still works.
        try:
            self.replica_links     = int(self._ext.ReplicaLinks)
            self.replicated        = int(self._ext.ReplicatedElements)
            self.replica_fallbacks = int(self._ext.ReplicaFallbacks)
        except Exception:
            self.replica_links = self.replicated = self.replica_fallbacks = 0
        results = []
        for info in raw:
            props = json.loads(info.PropertiesJson) if info.PropertiesJson else {}
            sub_meshes = []
            for sm in info.SubMeshes:
                fv = sm.FlatVertices
                ff = sm.FlatFaces
                nv = len(fv) // 3
                nf = len(ff) // 3
                verts = [[fv[i*3], fv[i*3+1], fv[i*3+2]] for i in range(nv)]
                faces = [[ff[i*3], ff[i*3+1], ff[i*3+2]] for i in range(nf)]
                color = (sm.ColorR, sm.ColorG, sm.ColorB) if sm.HasColor else None
                sub_meshes.append((verts, faces, color))
            if sub_meshes:
                results.append((info.Name, sub_meshes, info.MaterialName,
                                 props, info.CenterX, info.CenterY, info.CenterZ))
        return results


# ─── IFC Writer ───────────────────────────────────────────────────────────────

class IFCWriter:
    """Builds and writes a single IFC4 file with tessellated geometry, colors,
    materials, property sets and a PNT_Identity pset carrying the pnt_id."""

    def __init__(self, project_name: str):
        self._ifc       = ifcopenshell.file(schema="IFC4")
        self._pending   = []
        self._materials = {}
        self._build_skeleton(project_name)

    def add_element(self, name: str, sub_meshes: list,
                    mat_name: str = "", pnt_id: str = None):
        """sub_meshes: list of (verts, faces, color) — one IfcTriangulatedFaceSet per entry."""
        if not sub_meshes:
            return
        ifc_guid  = ifcopenshell.guid.compress(pnt_id) if pnt_id else self._guid()
        tri_sets  = []
        for verts, faces, color in sub_meshes:
            if not verts or not faces:
                continue
            coord_list = self._ifc.createIfcCartesianPointList3D([list(v) for v in verts])
            tri_set    = self._ifc.createIfcTriangulatedFaceSet(coord_list, None, None, faces, None)
            if color is not None:
                self._apply_color(tri_set, *color)
            tri_sets.append(tri_set)
        if not tri_sets:
            return
        shape = self._ifc.createIfcShapeRepresentation(
            self._body_ctx, "Body", "Tessellation", tri_sets
        )
        geo   = self._ifc.createIfcProductDefinitionShape(None, None, [shape])
        place = self._world_placement()
        elem  = self._ifc.createIfcBuildingElementProxy(
            ifc_guid, None, name, None, None, place, geo, None
        )
        self._add_pnt_identity(elem, pnt_id or ifc_guid)
        if mat_name:
            self._associate_material(elem, mat_name)
        self._pending.append(elem)

    def save(self, path: Path) -> Path:
        if self._pending:
            self._ifc.createIfcRelContainedInSpatialStructure(
                self._guid(), None, None, None, self._pending, self._storey
            )
        self._ifc.write(str(path))
        return path

    def _guid(self) -> str:
        return ifcopenshell.guid.compress(uuid.uuid4().hex)

    def _pt(self, xyz):
        return self._ifc.createIfcCartesianPoint(list(xyz))

    def _world_placement(self):
        ax = self._ifc.createIfcAxis2Placement3D(self._pt([0.0, 0.0, 0.0]), None, None)
        return self._ifc.createIfcLocalPlacement(None, ax)

    def _tessellation(self, verts: list, faces: list, color=None):
        coord_list = self._ifc.createIfcCartesianPointList3D([list(v) for v in verts])
        tri_set    = self._ifc.createIfcTriangulatedFaceSet(coord_list, None, None, faces, None)
        if color is not None:
            self._apply_color(tri_set, *color)
        shape = self._ifc.createIfcShapeRepresentation(
            self._body_ctx, "Body", "Tessellation", [tri_set]
        )
        return self._ifc.createIfcProductDefinitionShape(None, None, [shape])

    def _apply_color(self, tri_set, r: float, g: float, b: float):
        colour    = self._ifc.createIfcColourRgb(None, r, g, b)
        rendering = self._ifc.createIfcSurfaceStyleRendering(
            colour, 0.0, None, None, None, None, None, None, "FLAT"
        )
        style = self._ifc.createIfcSurfaceStyle(None, "BOTH", [rendering])
        self._ifc.createIfcStyledItem(tri_set, [style], None)

    def _associate_material(self, element, material_name: str):
        if material_name not in self._materials:
            self._materials[material_name] = self._ifc.createIfcMaterial(
                material_name, None, None
            )
        self._ifc.createIfcRelAssociatesMaterial(
            self._guid(), None, None, None, [element], self._materials[material_name]
        )

    def _add_pnt_identity(self, element, pnt_id: str):
        ifc_props = [
            self._ifc.createIfcPropertySingleValue(
                "pnt_id", None,
                self._ifc.createIfcLabel(pnt_id),
                None
            )
        ]
        pset = self._ifc.createIfcPropertySet(
            self._guid(), None, "PNT_Identity", None, ifc_props
        )
        self._ifc.createIfcRelDefinesByProperties(
            self._guid(), None, None, None, [element], pset
        )

    def _build_skeleton(self, name: str):
        units = self._ifc.createIfcUnitAssignment([
            self._ifc.createIfcSIUnit(None, "LENGTHUNIT",  None, "METRE"),
            self._ifc.createIfcSIUnit(None, "AREAUNIT",    None, "SQUARE_METRE"),
            self._ifc.createIfcSIUnit(None, "VOLUMEUNIT",  None, "CUBIC_METRE"),
        ])
        ax2p = self._ifc.createIfcAxis2Placement3D(
            self._pt([0.0, 0.0, 0.0]),
            self._ifc.createIfcDirection([0.0, 0.0, 1.0]),
            self._ifc.createIfcDirection([1.0, 0.0, 0.0]),
        )
        self._ctx = self._ifc.createIfcGeometricRepresentationContext(
            None, "Model", 3, 1.0e-5, ax2p, None
        )
        self._body_ctx = self._ifc.createIfcGeometricRepresentationSubContext(
            "Body", "Model", None, None, None, None, self._ctx, None, "MODEL_VIEW", None
        )
        self._project = self._ifc.createIfcProject(
            self._guid(), None, name, None, None, None, None, [self._ctx], units
        )
        p0 = self._world_placement()
        self._site = self._ifc.createIfcSite(
            self._guid(), None, "Site", None, None, p0, None, None,
            "ELEMENT", None, None, None, None, None
        )
        self._building = self._ifc.createIfcBuilding(
            self._guid(), None, "Building", None, None, p0, None, None,
            "ELEMENT", None, None, None
        )
        self._storey = self._ifc.createIfcBuildingStorey(
            self._guid(), None, "Level 0", None, None, p0, None, None,
            "ELEMENT", 0.0
        )
        self._agg(self._project,  [self._site])
        self._agg(self._site,     [self._building])
        self._agg(self._building, [self._storey])

    def _agg(self, parent, children):
        self._ifc.createIfcRelAggregates(self._guid(), None, None, None, parent, children)


# ─── Clash Extractor ─────────────────────────────────────────────────────────

class ClashExtractor:
    """
    Runs all clash tests and collects results.
    Links each clash element to its pnt_id via (nwc_stem, cx, cy, cz) lookup.
    """

    def __init__(self, bbox_index: dict, doc):
        self._bix = bbox_index
        self._model_stems = {}
        for i in range(doc.Models.Count):
            model = doc.Models[i]
            self._model_stems[model.RootItem] = Path(model.FileName).stem

    def run(self, doc) -> tuple:
        clash_doc  = CastUtils.CastTo[DocumentClash](doc.Clash)
        tests_data = clash_doc.TestsData

        # Guard: running the clash engine with no tests defined crashes Navisworks. Check first.
        all_tests = list(tests_data.Value.TestsRoot.Children)
        if not all_tests:
            print("  No clash tests defined — skipping clash extraction.")
            return [], []

        if RUN_CLASH_TESTS:
            print("  Running all clash tests...")
            t0 = datetime.now()
            tests_data.TestsRunAllTests()
            elapsed = (datetime.now() - t0).total_seconds()
            print(f"  Tests computed in {elapsed:.1f}s")
        else:
            print("  RUN_CLASH_TESTS=False — exporting existing results without recomputing.")

        # result.Distance is in DOCUMENT units (feet only if the model is in feet) -> metres
        to_m = UnitConversion.ScaleFactor(doc.Models.First.Units, Units.Meters)
        tests_summary = []
        all_clashes   = []
        n_tests       = len(all_tests)

        for ti, test in enumerate(all_tests, 1):
            print(f"  [{ti}/{n_tests}] {test.DisplayName}...", end="")
            t0      = datetime.now()
            results = list(self._iter_results(test))
            count   = len(results)

            status_counts = {}
            for r in results:
                s = str(r.Status)
                status_counts[s] = status_counts.get(s, 0) + 1
            dominant = max(status_counts, key=status_counts.get) if status_counts else "New"
            elapsed = (datetime.now() - t0).total_seconds()
            print(f" {count} clashes ({elapsed:.1f}s)")
            tests_summary.append({"name": test.DisplayName, "clashes": count, "status": dominant})

            for result in results:
                item_a = result.Item1
                item_b = result.Item2
                center = result.Center
                all_clashes.append({
                    "Test":         test.DisplayName,
                    "Discipline":   self._discipline(test.DisplayName),
                    "Clash":        result.DisplayName,
                    "Status":       str(result.Status),
                    "Distance (m)": round(float(result.Distance) * to_m, 4) if result.Distance else 0,
                    "X": round(float(center.X), 3) if center else None,
                    "Y": round(float(center.Y), 3) if center else None,
                    "Z": round(float(center.Z), 3) if center else None,
                    "Element A": self._item_name(item_a),
                    "ID A":      self._element_id(item_a),
                    "Source A":  self._nwc_stem(item_a),
                    "Type A":    self._revit_category(item_a),
                    "Element B": self._item_name(item_b),
                    "ID B":      self._element_id(item_b),
                    "Source B":  self._nwc_stem(item_b),
                    "Type B":    self._revit_category(item_b),
                    "pnt_id_a":  self._resolve(item_a),
                    "pnt_id_b":  self._resolve(item_b),
                    "Comment":   self._last_comment(result),
                })

        return tests_summary, all_clashes

    @staticmethod
    def _item_name(item) -> str:
        if item is None:
            return ""
        try:
            node = item.Parent
            while node is not None:
                if node.DisplayName:
                    return node.DisplayName
                node = node.Parent
        except Exception:
            pass
        return ""

    def _nwc_stem(self, item) -> str:
        if item is None:
            return ""
        try:
            node = item
            while node.Parent is not None:
                node = node.Parent
            return self._model_stems.get(node, "")
        except Exception:
            return ""

    @staticmethod
    def _revit_category(item) -> str:
        if item is None:
            return ""
        parent = item.Parent
        if parent is None:
            return ""
        try:
            for cat in parent.PropertyCategories:
                if cat.DisplayName == "Tipo de Revit":
                    for prop in cat.Properties:
                        if prop.DisplayName == "Categoría":
                            val = str(prop.Value.ToDisplayString())
                            if val and val != "?":
                                return val
        except Exception:
            pass
        return ""

    def _resolve(self, item):
        if item is None:
            return None
        try:
            node = item
            while node.Parent is not None:
                node = node.Parent
            stem = self._model_stems.get(node, "")

            candidates = [item]
            if item.Parent is not None:
                candidates.append(item.Parent)
            for target in candidates:
                bb  = target.BoundingBox()
                key = (stem,
                       round(float(bb.Center.X), 3),
                       round(float(bb.Center.Y), 3),
                       round(float(bb.Center.Z), 3))
                found = self._bix.get(key)
                if found is not None:
                    return found
        except Exception:
            pass
        return None

    @staticmethod
    def _iter_results(test):
        for child in test.Children:
            if child.IsGroup:
                for r in child.Children:
                    yield r
            else:
                yield child

    @staticmethod
    def _element_id(item) -> str:
        if item is None:
            return ""
        try:
            parent = item.Parent
            if parent is not None:
                for cat in parent.PropertyCategories:
                    if cat.DisplayName.lower() == "id de elemento":
                        for prop in cat.Properties:
                            if prop.DisplayName == "Valor":
                                val = prop.Value.ToDisplayString()
                                if val and val != "?":
                                    return val
        except Exception:
            pass
        return ""

    @staticmethod
    def _last_comment(result) -> str:
        try:
            last = ""
            for c in result.Comments:
                body = str(c.Body)
                last = body.split("] ", 1)[-1] if "] " in body else body
            return last
        except Exception:
            return ""

    @staticmethod
    def _discipline(test_name: str) -> str:
        m = re.search(r'Instalaciones_([^_]+)', test_name)
        return m.group(1) if m else "Estructura"


# ─── Classification Analyser ─────────────────────────────────────────────────

class ClassificationAnalyzer:
    """Reports classification coverage by reusing whatever SearchSets already exist in
    the document — never a hardcoded parameter name. Each project defines its own
    classification strategy (PYNET_Classification, native Category, discipline, or
    anything else) by creating SearchSets for it (see the ClashDetection skill); this
    analyzer just runs those same searches and measures how much geometry they cover,
    so it works unchanged for any project's strategy.
    """

    @staticmethod
    def _collect_search_sets(root) -> list:
        """Recursively collect (code_name, Search) for every SelectionSet under root —
        skips plain folders (no .Search attribute)."""
        found = []
        for item in root.Children:
            try:
                search = item.Search
                found.append((item.DisplayName, search))
            except Exception:
                pass
            if item.IsGroup:
                found.extend(ClassificationAnalyzer._collect_search_sets(item))
        return found

    @staticmethod
    def _source_file(item):
        node = item
        depth = 0
        while node is not None and depth < 6:
            try:
                for cat in node.PropertyCategories:
                    if cat.DisplayName != "Elemento":
                        continue
                    for prop in cat.Properties:
                        if prop.DisplayName == "Archivo de origen":
                            val = prop.Value.ToDisplayString()
                            if val:
                                return val
            except Exception:
                pass
            node = node.Parent
            depth += 1
        return None

    @staticmethod
    def run(doc, model_indices=None) -> list:
        """model_indices restricts the walk to the selected models — without it, this
        silently re-walks the whole federation (including unselected, possibly much
        larger models) on every single-model export."""
        indices = model_indices if model_indices is not None else range(doc.Models.Count)

        model_names        = {}
        total_geo_by_model = {}
        for i in indices:
            model = doc.Models[i]
            name  = Path(model.FileName).stem
            model_names[i] = name
            total_geo_by_model[name] = sum(1 for it in model.RootItem.Descendants if it.HasGeometry)

        search_sets = ClassificationAnalyzer._collect_search_sets(doc.SelectionSets.RootItem)

        covered_geo_by_model       = {name: set() for name in model_names.values()}
        elements_per_code_by_model = {name: defaultdict(int) for name in model_names.values()}

        for code_name, search in search_sets:
            try:
                matches = list(search.FindAll(doc, False))
            except Exception:
                continue
            for m in matches:
                src_file = ClassificationAnalyzer._source_file(m)
                if src_file is None:
                    continue
                src_stem = Path(src_file).stem
                model_name = next((n for n in model_names.values() if n == src_stem), None)
                if model_name is None:
                    continue
                for desc in m.Descendants:
                    if desc.HasGeometry:
                        h = hash(desc)
                        if h not in covered_geo_by_model[model_name]:
                            covered_geo_by_model[model_name].add(h)
                            elements_per_code_by_model[model_name][code_name] += 1

        basis = f"{len(search_sets)} SearchSets (" + ", ".join(c for c, _ in search_sets[:8]) + (", ..." if len(search_sets) > 8 else "") + ")" if search_sets else "no SearchSets found"

        results = []
        for name in model_names.values():
            total_geo      = total_geo_by_model[name]
            classified_geo = len(covered_geo_by_model[name])
            coverage_pct   = round(classified_geo / total_geo * 100, 1) if total_geo > 0 else 0.0
            results.append({
                "model":                   name,
                "total_geometry_elements": total_geo,
                "classified_geo":          classified_geo,
                "unclassified_geo":        total_geo - classified_geo,
                "coverage_pct":            coverage_pct,
                "elements_per_code":       dict(sorted(elements_per_code_by_model[name].items())),
                "basis":                   basis,
            })
        return results


# ─── PNT Packager ─────────────────────────────────────────────────────────────

class PNTPackager:
    def pack(self, ifc_files: list, clash_data: dict,
             properties: dict, manifest: dict, out_path: Path) -> Path:
        with zipfile.ZipFile(out_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
            z.writestr("manifest.json",   json.dumps(manifest,   ensure_ascii=False, indent=2))
            z.writestr("clashes.json",    json.dumps(clash_data, ensure_ascii=False, indent=2))
            z.writestr("properties.json", json.dumps(properties, ensure_ascii=False, indent=2))
            for ifc_path in ifc_files:
                z.write(ifc_path, f"models/{ifc_path.name}")
        return out_path


# ─── Export Manager ───────────────────────────────────────────────────────────

class ExportManager:

    def __init__(self, doc, work_dir: Path, model_indices: list = None):
        self._doc = doc
        self._model_indices = model_indices if model_indices is not None else list(range(doc.Models.Count))
        self._tmp = work_dir / "_pnt_tmp"
        self._tmp.mkdir(parents=True, exist_ok=True)

    _ROOT_CATEGORIES = {"elemento", "element", "proyecto", "project", "identidad", "identity"}
    _ROOT_SKIP_PROPS = {"icono", "icon", "tipo interno", "internal type", "material"}

    @staticmethod
    def _variant_value(val):
        """Unwrap a Navisworks VariantData to its plain value — val.ToString()/str(val) includes
        the debug type prefix ("DisplayString:...", "Boolean:False"), which is not what a user
        wants to see. Dispatch on the typed accessor instead, same pattern as WallLinearMeters.py."""
        try:
            if val.IsDisplayString or val.IsIdentifierString:
                return val.ToDisplayString()
            if val.IsBoolean:
                return val.ToBoolean()
            if val.IsInt32:
                return val.ToInt32()
            if val.IsInt64:
                return val.ToInt64()
            if val.IsDoubleLength:
                return round(val.ToDoubleLength(), 4)
            if val.IsDoubleAngle:
                return round(math.degrees(val.ToDoubleAngle()), 4)
            if val.IsDoubleArea:
                return round(val.ToDoubleArea(), 4)
            if val.IsDoubleVolume:
                return round(val.ToDoubleVolume(), 4)
            if val.IsDouble or val.IsAnyDouble:
                return round(val.ToAnyDouble(), 6)
            if val.IsNamedConstant:
                return str(val.ToNamedConstant())
            if val.IsDateTime:
                return str(val.ToDateTime())
            return val.ToDisplayString()
        except Exception:
            return str(val)

    @staticmethod
    def _extract_root_psets(root_item) -> dict:
        """Elemento/Proyecto/Identidad categories from a model's root tree item — project name,
        building name, source file paths (.rvt/.nwc), translation/rotation, version GUIDs.
        Everything a user sees selecting the file node in Navisworks' own Selection Tree,
        mirrored into the .pnt so the viewer's tree can show real data on the model root
        instead of a synthesized "Name + element count" summary."""
        psets = {}
        try:
            for cat in root_item.PropertyCategories:
                cname = (cat.DisplayName or "").strip()
                if cname.lower() not in ExportManager._ROOT_CATEGORIES:
                    continue
                props = {}
                for p in cat.Properties:
                    pname = (p.DisplayName or "").strip()
                    if pname.lower() in ExportManager._ROOT_SKIP_PROPS:
                        continue
                    try:
                        props[pname] = ExportManager._variant_value(p.Value)
                    except Exception:
                        continue
                if props:
                    psets[cname] = props
        except Exception:
            pass
        return psets

    def _read_model_rotation(self):
        """Read the true-north rotation (degrees about Z) from the Navisworks model transform.
        Returns the first non-trivial 'Ángulo de rotación' / 'Rotation Angle' (DoubleAngle),
        or None if unavailable."""
        for i in range(self._doc.Models.Count):
            root = self._doc.Models[i].RootItem
            try:
                for cat in root.PropertyCategories:
                    cn = (cat.DisplayName or "").lower()
                    if cn not in ("transformar", "transform", "elemento", "element"):
                        continue
                    for p in cat.Properties:
                        pn = (p.DisplayName or "").lower()
                        if "rotac" in pn and ("ngulo" in pn or "angle" in pn):
                            try:
                                deg = round(math.degrees(p.Value.ToDoubleAngle()), 4)
                            except Exception:
                                continue
                            if abs(deg) > 1e-6:
                                return deg
            except Exception:
                pass
        return None

    def _unique_stems(self) -> dict:
        """model index → file stem, suffixed _2, _3... when the same file is loaded more than once.
        Without it every copy wrote the same <stem>.ifc (each overwriting the previous) and the
        m_<stem> root entry in properties.json."""
        seen, stems = defaultdict(int), {}
        for i in self._model_indices:
            base = Path(self._doc.Models[i].FileName).stem
            seen[base] += 1
            stems[i] = base if seen[base] == 1 else f"{base}_{seen[base]}"
        return stems

    def run(self) -> Path:
        t_total = datetime.now()
        n = len(self._model_indices)
        proj_label = _doc_path(self._doc).stem

        progress = ProgressWindow(f"{proj_label} ({n} model(s))")
        try:
            return self._run(n, progress, t_total)
        finally:
            progress.close()

    def _run(self, n: int, progress, t_total) -> Path:
        print(f"━━━ PNT/IFC Export — {n} model(s) ━━━")

        extractor   = ElementExtractor()
        ifc_files   = []
        model_infos = []
        properties  = {}
        bbox_index  = {}
        orient      = OrientationEstimator()
        stems       = self._unique_stems()

        for pos, i in enumerate(self._model_indices, 1):
            if progress.cancelled:
                print(f"\nExport cancelled by user before model {pos}/{n}.")
                break

            model = self._doc.Models[i]
            stem  = stems[i]
            print(f"\n[{pos}/{n}] {stem}")
            progress.update(phase=f"{stem} — extracting geometry", detail="")
            t0 = datetime.now()

            elements = extractor.extract(i)
            elapsed  = (datetime.now() - t0).total_seconds()
            print(f"  {len(elements)} elements in {elapsed:.1f}s")
            if extractor.replica_links:
                print(f"  {extractor.replica_links} repeated link(s): {extractor.replicated} elements reused"
                      f" from the first copy, {extractor.replica_fallbacks} re-tessellated")

            if not elements:
                print("  No geometry — skipping")
                continue

            progress.update(phase=f"{stem} — writing IFC", detail="")
            t0       = datetime.now()
            ifc_path = self._tmp / f"{stem}.ifc"
            writer   = IFCWriter(stem)

            for name, sub_meshes, mat, props, cx, cy, cz in elements:
                pnt_id = uuid.uuid4().hex
                writer.add_element(name, sub_meshes, mat, pnt_id)
                for verts, _faces, _color in sub_meshes:
                    orient.add(verts)
                properties[pnt_id] = {
                    "pnt_id": pnt_id,
                    "name":   name,
                    "model":  stem,
                    "psets":  props or {},
                }
                if cx != 0.0 or cy != 0.0 or cz != 0.0:
                    bbox_index[(stem, cx, cy, cz)] = pnt_id

            writer.save(ifc_path)
            elapsed = (datetime.now() - t0).total_seconds()
            mb = ifc_path.stat().st_size / 1_048_576
            print(f"  → {mb:.1f} MB IFC in {elapsed:.1f}s")

            ifc_files.append(ifc_path)
            model_infos.append({
                "name":     stem,
                "fileName": f"{stem}.ifc",
                "fullPath": model.FileName,
            })
            # Model-root psets (Elemento/Proyecto/Identidad from Navisworks' own Selection Tree)
            # keyed like the tree panel's root node id ("m_<stem>") — never collides with a real
            # element pnt_id (those are hex-only uuid4().hex, "m_" is not a hex prefix).
            properties[f"m_{stem}"] = {
                "pnt_id": f"m_{stem}",
                "name":   stem,
                "model":  stem,
                "psets":  self._extract_root_psets(model.RootItem),
            }

        # Prefer Navisworks' authoritative model transform ("Ángulo de rotación", a DoubleAngle
        # about Z) — that IS the true-north rotation baked into the exported world geometry.
        # Fall back to the PCA footprint estimate only if the property is unavailable.
        view_rotation = self._read_model_rotation()
        if view_rotation is None:
            view_rotation = orient.angle_deg()
            print(f"\n  View rotation (PCA estimate): {view_rotation}°  ({orient.n} sampled vertices)")
        else:
            print(f"\n  View rotation (Navisworks transform): {view_rotation}°")
        properties["__meta__"] = {"viewRotationDeg": view_rotation}

        print(f"\n━━━ Clash extraction ({len(model_infos)} models) ━━━")
        if EXPORT_CLASHES:
            progress.update(phase="Running clash tests", detail="")
            try:
                clash_extractor         = ClashExtractor(bbox_index, self._doc)
                tests_summary, all_clashes = clash_extractor.run(self._doc)
                print(f"  Total: {len(all_clashes)} results across {len(tests_summary)} tests")
            except Exception as e:
                tests_summary, all_clashes = [], []
                print(f"  Clash extraction failed ({e}) — continuing without clashes.")
        else:
            tests_summary, all_clashes = [], []
            print("  (skipped — EXPORT_CLASHES=False)")

        progress.update(phase="Analysing classification coverage", detail="")
        t0             = datetime.now()
        classification = ClassificationAnalyzer.run(self._doc, self._model_indices)
        elapsed        = (datetime.now() - t0).total_seconds()
        basis_label    = classification[0]["basis"] if classification else "no SearchSets found"
        print(f"\n━━━ Classification coverage — basis: {basis_label} ━━━")
        for r in classification:
            print(f"  {r['model']}: {r['coverage_pct']}% coverage"
                  f"  ({r['classified_geo']}/{r['total_geometry_elements']} geometry elements)")
        print(f"  → done in {elapsed:.1f}s")

        clash_data = {
            "models":         model_infos,
            "tests":          tests_summary,
            "clashes":        all_clashes,
            "classification": classification,
            "summary": {
                "totalClashes": len(all_clashes),
                "activeTests":  sum(1 for t in tests_summary if t["clashes"] > 0),
                "totalModels":  len(model_infos),
            },
        }

        out_dir = _doc_path(self._doc).parent
        project = _doc_path(self._doc).stem

        manifest = {
            "version":       "1.0",
            "format":        "pnt-ifc",
            "project":       project,
            "created":       datetime.now().isoformat(),
            "models":        [m["fileName"] for m in model_infos],
            "element_count": len(properties),
            "clash_count":   len(all_clashes),
        }

        out_path = out_dir / f"{project}.pnt"
        print(f"\n━━━ Packaging → {out_path.name} ━━━")
        progress.update(phase="Packaging .pnt archive", detail="")
        t0 = datetime.now()
        PNTPackager().pack(ifc_files, clash_data, properties, manifest, out_path)
        mb_out       = out_path.stat().st_size / 1_048_576
        elapsed_pack = (datetime.now() - t0).total_seconds()
        print(f"  → {mb_out:.1f} MB in {elapsed_pack:.1f}s")

        for f in ifc_files:
            try:
                f.unlink()
            except Exception:
                pass
        try:
            self._tmp.rmdir()
        except Exception:
            pass

        total_s = (datetime.now() - t_total).total_seconds()
        m, s = divmod(int(total_s), 60)
        print(f"\nDone → {out_path}  (total {m}m {s}s)")
        return out_path


def _doc_path(doc) -> Path:
    """The .nwf/.nwd path, or — for a new, unsaved document (FileName is "") — the first model's
    file, so the .pnt lands next to the models instead of in Navisworks' working directory."""
    name = str(doc.FileName or "")
    if not name and doc.Models.Count > 0:
        name = str(doc.Models[0].FileName)
    return Path(name) if name else Path.home() / "project"


# ─── Entry point ──────────────────────────────────────────────────────────────

doc = Application.ActiveDocument
if doc.Models.Count == 0:
    print("No models loaded.")
else:
    selection_form = ModelSelectionForm(doc)
    dialog_result = selection_form.ShowDialog()

    if dialog_result == DialogResult.OK and selection_form.SelectedIndices:
        work_dir = _doc_path(doc).parent / "PNT_IFC_Export"

        ExportManager(doc, work_dir, selection_form.SelectedIndices).run()
    else:
        print("Export cancelled — no models selected.")
