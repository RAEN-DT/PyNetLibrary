<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: Windows Forms (Revit, AutoCAD & Civil 3D)

Read this guide **before writing any script that shows a form, dialog, or custom UI**. These rules are hard-won; ignoring them causes crashes or silent context loss.

Related: [revit.md](revit.md) · [autocad-civil.md](autocad-civil.md)

---

## Core rules (all hosts)

### Explicit imports — never `import *`

`System.Windows.Forms` has its own `TaskDialog` (.NET 6+). A `from System.Windows.Forms import *`
silently shadows (or is shadowed by) the Revit `TaskDialog`, depending on import order. Import each
type by name and the collision cannot happen:

```python
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
from System.Windows.Forms import Application, Button, DialogResult, Form, Label
from System.Drawing import Point, Size
from Autodesk.Revit.UI import TaskDialog, TaskDialogCommonButtons, TaskDialogIcon
```

### super().__init__() is mandatory

Python.NET 3.x requires explicit `super().__init__()` as the first line of any class inheriting from a .NET type. Without it, accessing `.Text`, `.Location`, etc. crashes with `NullReferenceException`.

```python
class MyForm(Form):
    def __init__(self):
        super().__init__()   # MANDATORY — must be first
        self.Text = "Title"
```

### EnableVisualStyles / SetCompatibleTextRenderingDefault

The host already created Win32 windows, so these may throw. Wrap in try/except and never call `SetCompatibleTextRenderingDefault`:

```python
try:
    Application.EnableVisualStyles()
except Exception:
    pass
# Never call Application.SetCompatibleTextRenderingDefault() — always throws in the host
```

### No host API calls inside form event handlers

Scripts run inside `IExternalEventHandler.Execute()` (Revit) / a command context (AutoCAD). When `form.ShowDialog()` starts the WinForms message loop, the host context is ambiguous. **Any host API call inside a button click handler will fail or crash.**

**Pattern: form is UI-only; all API work happens after `ShowDialog()` returns.**

```python
class MyForm(Form):
    def __init__(self):
        super().__init__()
        self.confirmed = False
        # ... build UI

    def OnExecute(self, sender, args):
        self.confirmed = True
        self.Close()   # just close — no API calls here

    def OnCancel(self, sender, args):
        self.Close()

form = MyForm()
form.ShowDialog()

if form.confirmed:
    # All host API work here — still inside ExternalEventHandler.Execute()
    ...
```

### No Application.DoEvents()

`Application.DoEvents()` inside an ExternalEventHandler causes re-entrancy and crashes. Never use it.

---

## Revit TaskDialog — string hell

`Autodesk.Revit.UI.TaskDialog` is painful with Python.NET 3.x.

**Use plain Python `str` — never `System.String(...)`.** `System.String` has no string constructor, so `System.String("PyNET")` throws "No method matches". Plain `str` is auto-converted.

```python
# WRONG
dlg = TaskDialog(System.String("PyNET"))
dlg.MainInstruction = System.String("Done!")

# CORRECT
dlg = TaskDialog("PyNET")
dlg.MainInstruction = "Done!"
```

Full working pattern:

```python
from Autodesk.Revit.UI import TaskDialog, TaskDialogCommonButtons, TaskDialogIcon

dlg = TaskDialog("PyNET")
dlg.TitleAutoPrefix = False
dlg.MainInstruction = "Done!"
dlg.MainContent = "Both models processed correctly."
dlg.CommonButtons = TaskDialogCommonButtons.Ok
dlg.MainIcon = TaskDialogIcon.TaskDialogIconInformation
dlg.Show()
```

---

## AutoCAD / Civil 3D specifics

The same core rules apply. For opening and saving external DWG files from a form, see the two validated patterns (Background / UI) in [autocad-external-dwg.md](autocad-external-dwg.md).

---

## Form icon — from the running PyNET bundle (all hosts)

Each bundle ships its icon at the **bundle root**, next to a common `Pynet.ico`:

| Host | Icon |
|---|---|
| Navisworks | `manage.ico` |
| Revit | `Revit.ico` |
| AutoCAD / Civil 3D | `C3D.ico` |

Never hardcode `…/ApplicationPlugins/Raen.<Host>.Pynet.bundle/…`: derive the bundle root from the
engine assembly that is executing the script (it lives in `<bundle>/Contents/<year>/`), so the path
is right for any year, any install location and any folder-name casing:

```python
from pathlib import Path
from System import AppDomain
from System.Drawing import Icon

PYNET_BIN = Path(next(a for a in AppDomain.CurrentDomain.GetAssemblies()
                      if a.GetName().Name == "Raen.Core.Pynet.Engine").Location).parent
PYNET_BUNDLE = PYNET_BIN.parent.parent
FORM_ICON = PYNET_BUNDLE / "Revit.ico"          # manage.ico | Revit.ico | C3D.ico

class MyForm(Form):
    def __init__(self):
        super().__init__()
        if FORM_ICON.exists():                   # guard — never crash if missing
            self.Icon = Icon(str(FORM_ICON))
```

---

## Reference scripts

- `01_Scripts/02_Revit/16_WindowsForms/OpenModelsCreateWallTest.py` — Revit: confirmation form, full API work after ShowDialog, TaskDialog result.
- `01_Scripts/03_AutoCAD/04_WinForms/EditDwg_Background.py` — AutoCAD Pattern A.
- `01_Scripts/03_AutoCAD/04_WinForms/EditDwg_WithUI.py` — AutoCAD Pattern B.
