<!-- SPDX-License-Identifier: MIT -->
<!-- Copyright (c) 2024-2026 RAEN Digital Tools SL - PyNET Platform -->

# Guide: cloud models, worksharing, batch and NWC export (Revit)

Read [revit.md](revit.md) first. Reference workflows: `02_Revit/00_Workflow/` (`OpenModels.py`,
`UpdateModels.py`, `SyncModels.py`, `NwcExporter.py`, `KeynotesManager.py`, `TransferData.py`) and
`16_WindowsForms/OpenModelsCreateWallTest.py`.

---

## Opening ACC / BIM 360 models

```python
from System import Guid

opts = OpenOptions()
opts.SetOpenWorksetsConfiguration(WorksetConfiguration(WorksetConfigurationOption.CloseAllWorksets))
try:
    path = ModelPathUtils.ConvertCloudGUIDsToCloudPath(ModelPathUtils.CloudRegionEMEA,
                                                      Guid(project_guid), Guid(model_guid))
    uidoc = uiapp.OpenAndActivateDocument(path, opts, False)        # opens in the UI
except Exception:
    path = ModelPathUtils.ConvertCloudGUIDsToCloudPath(ModelPathUtils.CloudRegionUS,
                                                      Guid(project_guid), Guid(model_guid))
    uidoc = uiapp.OpenAndActivateDocument(path, opts, False)
```

- The **region** is not in the GUIDs — try EMEA, fall back to US.
- `OpenAndActivateDocument` shows the model; `app.OpenDocumentFile(path, opts)` opens it **in the
  background** (no tab) — right for batch work, and always `doc.Close(False)` afterwards.
- Worksets: `CloseAllWorksets` (fast), `OpenAllWorksets`, `OpenLastViewed`.
- Skip models already open: compare with `[d.Title for d in app.Documents if not d.IsLinked]`.

## Synchronise with central, relinquishing everything

```python
class SyncLockCallback(ICentralLockedCallback):      # a .NET interface implemented in Python
    def ShouldWaitForLockAvailability(self):
        return False                                  # don't block if central is locked

twc = TransactWithCentralOptions()
twc.SetLockCallback(SyncLockCallback())
rel = RelinquishOptions(False)
rel.CheckedOutElements = rel.FamilyWorksets = rel.StandardWorksets = True
rel.UserWorksets = rel.ViewWorksets = True
swc = SynchronizeWithCentralOptions()
swc.SetRelinquishOptions(rel)
swc.Comment = "PyNET synchronize"
doc.SynchronizeWithCentral(twc, swc)
```

Only `doc.IsWorkshared and not doc.IsLinked` documents. Relinquishing everything is destructive for
colleagues' borrowed elements — show a warning dialog before running it.

## Batch-editing local RVT files without the UI

```python
mp = ModelPathUtils.ConvertUserVisiblePathToModelPath(path_str)
d = app.OpenDocumentFile(mp, OpenOptions())
t = Transaction(d, "PyNET - batch edit"); t.Start()
try:
    ...; t.Commit()
except Exception:
    t.RollBack(); raise
d.Save()
d.Close(False)
```

## NWC export

```python
opts = NavisworksExportOptions()
opts.Coordinates = NavisworksCoordinates.Shared          # or .Internal
opts.ExportScope = NavisworksExportScope.View            # or .Model
opts.ViewId = view3d.Id                                  # per view when scope = View
opts.ConvertElementProperties = True
opts.DivideFileIntoLevels = True
opts.ExportElementIds = True
opts.ExportRoomAsAttribute = True
doc.Export(folder, file_name_without_ext, opts)
```

Other flags: `ExportLinks`, `ExportParts`, `ExportRoomGeometry`, `ExportUrls`,
`FindMissingMaterials`, `ConvertLights`, `ConvertLinkedCADFormats`. A 3D view with no model geometry
exports an empty NWC — filter those views out first.

## Keynotes

```python
ref = ExternalResourceReference.CreateLocalResource(
    doc, ExternalResourceTypes.BuiltInExternalResourceTypes.KeynoteTable,
    FilePath(txt_path), PathType.Absolute)
t = Transaction(doc, "Load keynotes"); t.Start()
KeynoteTable.GetKeynoteTable(doc).LoadFrom(ref, KeyBasedTreeEntriesLoadResults())
t.Commit()
```

Write the value with `get_Parameter(BuiltInParameter.KEYNOTE_PARAM)` on types and materials — never
`LookupParameter("Keynote")`, which is the English UI name.

## Copying data between open models

Match elements across documents by **name** (types: `Element.Name.__get__(t)`), not by id — ids
differ between files. `ProjectInformation.GetOrderedParameters()` gives the project info parameters
in UI order. Built-in parameters have `Definition.BuiltInParameter != BuiltInParameter.INVALID`.
One transaction per target document.
