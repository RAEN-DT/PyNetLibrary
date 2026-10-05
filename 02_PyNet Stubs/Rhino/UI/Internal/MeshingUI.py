# Auto-generated — Rhino 8 — Rhino.UI.Internal.MeshingUI

class MeshParametersStyle(ViewModel):
    """.NET: Rhino.UI.Internal.MeshingUI.MeshParametersStyle"""
    def __init__(self, *args) -> None: ...
    IsReadOnly: bool
    IsSeparator: bool
    IsCustom: bool
    Id: Guid
    SeparatorId: Guid
    RhinoDefaults: Guid
    RhinoJaggedAndFast: Guid
    RhinoSmoothAndSlower: Guid
    Custom: Guid
    Image: Image
    Name: str
    Parameters: MeshingParameters
    Detailed: bool
    Deleted: bool
    ModelUnitSystem: UnitSystem
    PageUnitSystem: UnitSystem
    ModelDistanceDisplayMode: DistanceDisplayMode
    PageDistanceDisplayMode: DistanceDisplayMode
    ModelDistanceDisplayPrecision: int
    PageDistanceDisplayPrecision: int
    def ToString(self, ) -> str: ...

class MeshSettingsViewModel(ViewModel):
    """.NET: Rhino.UI.Internal.MeshingUI.MeshSettingsViewModel"""
    def __init__(self, *args) -> None: ...
    Document: RhinoDoc
    PreviewMeshingParameters: MeshingParameters
    MeshParameters: MeshingParameters
    Detailed: bool
    DetailedOrSimpleText: str
    PageStyle: PageStyle
    SettingPresetValues: bool
    NurbsMeshingSliderPosition: int
    Density: float
    MaximumAngle: float
    MaximumAspectRatio: float
    MinimumEdgeLength: float
    MaximumEdgeLength: float
    MaxDistanceEdgeToSurface: float
    MinimumInitialGridQuads: int
    RefineMesh: bool
    JaggedSeams: bool
    SimplePlanes: bool
    PackTextures: bool
    PersistentPresets: ObservableCollection
    SelectedPreset: MeshParametersStyle
    SelectedPresetIndex: int
    DefaultControlColor: Color
    LabelDefaultColor: Color
    ChangedValueColor: Color
    DensityChanged: bool
    DensityColor: Color
    MaximumAngleChanged: bool
    MaximumAngleColor: Color
    MaximumAspectRatioChanged: bool
    MaximumAspectRatioColor: Color
    MaximumEdgeLengthChanged: bool
    MaximumEdgeLengthColor: Color
    MinimumEdgeLengthChanged: bool
    MinimumEdgeLengthColor: Color
    MaxDistanceEdgeToSurfaceChanged: bool
    MaxDistanceEdgeToSurfaceColor: Color
    MinimumInitialGridQuadsChanged: bool
    MinimumInitialGridQuadsColor: Color
    RefineMeshChanged: bool
    RefineMeshColor: Color
    JaggedSeamsChanged: bool
    JaggedSeamsColor: Color
    PackTexturesChanged: bool
    PackTexturesColor: Color
    SimplePlanesChanged: bool
    SimplePlanesColor: Color
    DetailedOrSimpleChanged: bool
    DetailedOrSimpleColor: Color
    SubDAbsoluteSliderPositionChanged: bool
    SubDAbsoluteSliderPositionColor: Color
    SubDAdaptiveSliderPositionChanged: bool
    SubDAdaptiveSliderPositionColor: Color
    PreviousSubDAbsoluteSliderPosition: int
    SubDAbsoluteSliderPosition: int
    PreviousSubDAdaptiveSliderPosition: int
    SubDAdaptiveSliderPosition: int
    EnablePreview: bool
    OriginalDetailedView: bool
    OriginalMeshParameters: MeshingParameters
    CancelAnalysisPreviewChanges: bool
    ModelUnitSystem: UnitSystem
    PageUnitSystem: UnitSystem
    ModelDistanceDisplayMode: DistanceDisplayMode
    PageDistanceDisplayMode: DistanceDisplayMode
    ModelDistanceDisplayPrecision: int
    PageDistanceDisplayPrecision: int
    def AddPreset(self, style: MeshParametersStyle) -> bool: ...
    def AddPresetToPersistentPresets(self, preset: MeshParametersStyle) -> bool: ...
    def Defaults(self, ) -> None: ...
    def DeletePreset(self, style: MeshParametersStyle) -> bool: ...
    def DeletePresetFromPersistentSettings(self, styleToDelete: MeshParametersStyle) -> None: ...
    def DeletePresetMenuClick(self, ) -> None: ...
    def ExportPresetMenuClick(self, ) -> None: ...
    def FindPresetAndSelectedIndex(self, ) -> None: ...
    def FindPresetByName(self, name: str) -> Guid: ...
    def FindPresetFromGuid(self, guid: Guid) -> MeshParametersStyle: ...
    def GetPresetsFromPersistentSettings(self, ) -> None: ...
    def ImportPresetsMenuClick(self, windowOwner: Control) -> None: ...
    def LoadPresetsFromFile(self, fileName: str) -> bool: ...
    def PreviewMeshes(self, ) -> Result: ...
    def ReloadPreset(self, ) -> None: ...
    def Reset(self, ) -> None: ...
    def RetrievePresetListFromSettings(self, ) -> ObservableCollection: ...
    def SaveAllPresetsToPersistentSettings(self, ) -> None: ...
    def SavePreset(self, preset: MeshParametersStyle) -> None: ...
    def SavePresetListToFile(self, fileName: str) -> None: ...
    def SavePresetMenuClick(self, ) -> None: ...
    def Set(self, ) -> None: ...
    def SetMpSubDFromSubDSliderPosition(self, ) -> None: ...
    def ShowUpdatePresetMenuItem(self, ) -> bool: ...
    def TurnPreviewOff(self, ) -> None: ...
    def UpdateDetailedOrSimpleButton(self, detailed: bool) -> None: ...
    def UpdatePresetMenuClick(self, ) -> None: ...

class MeshingStyleListViewModel(ViewModel):
    """.NET: Rhino.UI.Internal.MeshingUI.MeshingStyleListViewModel"""
    def __init__(self, *args) -> None: ...
    Document: RhinoDoc
    OriginalDetailedView: bool
    MeshParameters: MeshingParameters
    OriginalMeshParameters: MeshingParameters
    SelectedStyleId: Guid
    SelectedStyle: MeshParametersStyle
    ModelUnitSystem: UnitSystem
    PageUnitSystem: UnitSystem
    ModelDistanceDisplayMode: DistanceDisplayMode
    PageDistanceDisplayMode: DistanceDisplayMode
    ModelDistanceDisplayPrecision: int
    PageDistanceDisplayPrecision: int
    def AddStyle(self, style: MeshParametersStyle) -> bool: ...
    def DeleteStyle(self, style: MeshParametersStyle) -> bool: ...
    def DeleteStyleFromSettings(self, styleToDelete: MeshParametersStyle) -> None: ...
    def EditStyle(self, style: MeshParametersStyle) -> bool: ...
    def FindStyle(self, guid: Guid) -> MeshParametersStyle: ...
    def FindStyleGuid(self, name: str, mp: MeshingParameters) -> Guid: ...
    def FindStyleGuidByName(self, name: str) -> Guid: ...
    def RetrievePresetListFromSettings(self, ) -> ObservableCollection: ...
    def RetrieveStyleListFromFile(self, fileName: str) -> bool: ...
    def SavePresetListToFile(self, fileName: str) -> bool: ...
    def SavePresetListToSettings(self, ) -> None: ...

class PageStyle:
    """.NET: Rhino.UI.Internal.MeshingUI.PageStyle"""
    def __init__(self, *args) -> None: ...
    ...
