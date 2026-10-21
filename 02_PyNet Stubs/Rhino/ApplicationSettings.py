# Auto-generated — Rhino 8 — Rhino.ApplicationSettings

class AppearanceSettings:
    """.NET: Rhino.ApplicationSettings.AppearanceSettings"""
    def __init__(self, *args) -> None: ...
    DefaultFontFaceName: str
    UsePaintColors: bool
    DefaultLayerColor: Color
    SelectedObjectColor: Color
    LockedObjectColor: Color
    SelectionWindowStrokeColor: Color
    SelectionWindowFillColor: Color
    SelectionWindowCrossingStrokeColor: Color
    SelectionWindowCrossingFillColor: Color
    WorldCoordIconXAxisColor: Color
    WorldCoordIconYAxisColor: Color
    WorldCoordIconZAxisColor: Color
    TrackingColor: Color
    FeedbackColor: Color
    DefaultObjectColor: Color
    ViewportBackgroundColor: Color
    FrameBackgroundColor: Color
    CommandPromptTextColor: Color
    CommandPromptHypertextColor: Color
    CommandPromptBackgroundColor: Color
    CrosshairColor: Color
    PageviewPaperColor: Color
    CurrentLayerBackgroundColor: Color
    EditCandidateColor: Color
    GridThinLineColor: Color
    GridThickLineColor: Color
    GridXAxisLineColor: Color
    GridYAxisLineColor: Color
    GridZAxisLineColor: Color
    DirectionArrowIconShaftSize: int
    DirectionArrowIconHeadSize: int
    CommandPromptPosition: CommandPromptPosition
    CommandPromptFontSize: int
    EchoPromptsToHistoryWindow: bool
    EchoCommandsToHistoryWindow: bool
    ShowFullPathInTitleBar: bool
    ShowCrosshairs: bool
    ShowSideBar: bool
    ShowOsnapBar: bool
    ShowSelectionFilterBar: bool
    ShowStatusBar: bool
    ShowViewportTitles: bool
    ShowTitleBar: bool
    MenuVisible: bool
    ShowLayoutDropShadow: bool
    ViewportTabsVisibleAtStart: bool
    LanguageIdentifier: int
    PreviousLanguageIdentifier: int
    @staticmethod
    def DefaultPaintColor(whichColor: PaintColor, darkMode: bool) -> Color: ...
    @staticmethod
    def DefaultWidgetColor(whichColor: WidgetColor) -> Color: ...
    @staticmethod
    def GetCurrentState() -> AppearanceSettingsState: ...
    @staticmethod
    def GetDefaultState(darkMode: bool) -> AppearanceSettingsState: ...
    @staticmethod
    def GetPaintColor(whichColor: PaintColor, compute: bool) -> Color: ...
    @staticmethod
    def GetWidgetColor(whichColor: WidgetColor) -> Color: ...
    @staticmethod
    def InitialMainWindowPosition(bounds: Rectangle) -> bool: ...
    @staticmethod
    def RestoreDefaults() -> None: ...
    @staticmethod
    def SetPaintColor(whichColor: PaintColor, c: Color, forceUiUpdate: bool) -> None: ...
    @staticmethod
    def SetToDarkMode() -> bool: ...
    @staticmethod
    def SetToLightMode() -> bool: ...
    @staticmethod
    def SetWidgetColor(whichColor: WidgetColor, c: Color, forceUiUpdate: bool) -> None: ...
    @staticmethod
    def UpdateFromState(state: AppearanceSettingsState) -> None: ...
    @staticmethod
    def UsingDefaultDarkModeColors() -> bool: ...
    @staticmethod
    def UsingDefaultLightModeColors() -> bool: ...

class AppearanceSettingsState:
    """.NET: Rhino.ApplicationSettings.AppearanceSettingsState"""
    def __init__(self, *args) -> None: ...
    DefaultFontFaceName: str
    DefaultLayerColor: Color
    SelectedObjectColor: Color
    LockedObjectColor: Color
    SelectionWindowStrokeColor: Color
    SelectionWindowFillColor: Color
    SelectionWindowCrossingStrokeColor: Color
    SelectionWindowCrossingFillColor: Color
    WorldCoordIconXAxisColor: Color
    WorldCoordIconYAxisColor: Color
    WorldCoordIconZAxisColor: Color
    TrackingColor: Color
    FeedbackColor: Color
    DefaultObjectColor: Color
    ViewportBackgroundColor: Color
    FrameBackgroundColor: Color
    CommandPromptTextColor: Color
    CommandPromptHypertextColor: Color
    CommandPromptBackgroundColor: Color
    CommandPromptFontSize: int
    CommandPromptFontName: str
    CrosshairColor: Color
    PageviewPaperColor: Color
    CurrentLayerBackgroundColor: Color
    EditCandidateColor: Color
    EchoPromptsToHistoryWindow: bool
    EchoCommandsToHistoryWindow: bool
    ShowTitleBar: bool
    ShowFullPathInTitleBar: bool
    ShowCrosshairs: bool
    ShowLayoutDropShadow: bool
    MenuVisible: bool
    ShowStatusBar: bool
    ShowViewportTitles: bool
    ViewportTabsVisibleAtStart: bool
    DirectionArrowIconShaftSize: int
    DirectionArrowIconHeadSize: int
    GridThinLineColor: Color
    GridThickLineColor: Color
    GridXAxisLineColor: Color
    GridYAxisLineColor: Color
    GridZAxisLineColor: Color

class ChooseOneObjectSettings:
    """.NET: Rhino.ApplicationSettings.ChooseOneObjectSettings"""
    def __init__(self, *args) -> None: ...
    FollowCursor: bool
    XOffset: int
    YOffset: int
    AutomaticResize: bool
    MaxAutoResizeItems: int
    ShowTitlebarAndBorder: bool
    ShowObjectName: bool
    ShowObjectType: bool
    ShowObjectColor: bool
    ShowObjectLayer: bool
    DynamicHighlight: bool
    UseCustomColor: bool
    HighlightColor: Color
    ShowAllOption: bool
    ShowObjectTypeDetails: bool
    @staticmethod
    def GetCurrentState() -> ChooseOneObjectSettingsState: ...
    @staticmethod
    def GetDefaultState() -> ChooseOneObjectSettingsState: ...
    @staticmethod
    def RestoreDefaults() -> None: ...
    @staticmethod
    def UpdateFromState(state: ChooseOneObjectSettingsState) -> None: ...

class ChooseOneObjectSettingsState:
    """.NET: Rhino.ApplicationSettings.ChooseOneObjectSettingsState"""
    def __init__(self, *args) -> None: ...
    FollowCursor: bool
    XOffset: int
    YOffset: int
    AutomaticResize: bool
    MaxAutoResizeItems: int
    ShowTitlebarAndBorder: bool
    ShowObjectName: bool
    ShowObjectType: bool
    ShowObjectColor: bool
    ShowObjectLayer: bool
    DynamicHighlight: bool
    UseCustomColor: bool
    HighlightColor: Color
    ShowAllOption: bool
    ShowObjectTypeDetails: bool

class ClipboardState:
    """.NET: Rhino.ApplicationSettings.ClipboardState"""
    def __init__(self, *args) -> None: ...
    ...

class CommandAliasList:
    """.NET: Rhino.ApplicationSettings.CommandAliasList"""
    def __init__(self, *args) -> None: ...
    Count: int
    @staticmethod
    def Add(alias: str, macro: str) -> bool: ...
    @staticmethod
    def Clear() -> None: ...
    @staticmethod
    def Delete(alias: str) -> bool: ...
    @staticmethod
    def GetDefaults() -> Dictionary: ...
    @staticmethod
    def GetMacro(alias: str) -> str: ...
    @staticmethod
    def GetNames() -> list: ...
    @staticmethod
    def IsAlias(alias: str) -> bool: ...
    @staticmethod
    def IsDefault() -> bool: ...
    @staticmethod
    def SetMacro(alias: str, macro: str) -> bool: ...
    @staticmethod
    def ToDictionary() -> Dictionary: ...

class CommandPromptPosition:
    """.NET: Rhino.ApplicationSettings.CommandPromptPosition"""
    def __init__(self, *args) -> None: ...
    ...

class CursorMode:
    """.NET: Rhino.ApplicationSettings.CursorMode"""
    def __init__(self, *args) -> None: ...
    ...

class CursorTooltipSettings:
    """.NET: Rhino.ApplicationSettings.CursorTooltipSettings"""
    def __init__(self, *args) -> None: ...
    TooltipsEnabled: bool
    Offset: Point
    BackgroundColor: Color
    TextColor: Color
    OsnapPane: bool
    DistancePane: bool
    PointPane: bool
    RelativePointPane: bool
    CommandPromptPane: bool
    AutoSuppress: bool
    EnableGumballToolTips: bool
    @staticmethod
    def GetCurrentState() -> CursorTooltipSettingsState: ...
    @staticmethod
    def GetDefaultState() -> CursorTooltipSettingsState: ...

class CursorTooltipSettingsState:
    """.NET: Rhino.ApplicationSettings.CursorTooltipSettingsState"""
    def __init__(self, *args) -> None: ...
    TooltipsEnabled: bool
    Offset: Point
    BackgroundColor: Color
    TextColor: Color
    OsnapPane: bool
    DistancePane: bool
    PointPane: bool
    RelativePointPane: bool
    CommandPromptPane: bool
    AutoSuppress: bool
    EnableGumballToolTips: bool

class CurvatureAnalysisSettings:
    """.NET: Rhino.ApplicationSettings.CurvatureAnalysisSettings"""
    def __init__(self, *args) -> None: ...
    GaussRange: Interval
    MeanRange: Interval
    MinRadiusRange: Interval
    MaxRadiusRange: Interval
    Style: CurvatureStyle
    @staticmethod
    def CalculateCurvatureAutoRange(meshes: IEnumerable, settings: CurvatureAnalysisSettingsState) -> bool: ...
    @staticmethod
    def GetCurrentState() -> CurvatureAnalysisSettingsState: ...
    @staticmethod
    def GetDefaultState() -> CurvatureAnalysisSettingsState: ...
    @staticmethod
    def RestoreDefaults() -> None: ...
    @staticmethod
    def UpdateFromState(state: CurvatureAnalysisSettingsState) -> None: ...

class CurvatureAnalysisSettingsState:
    """.NET: Rhino.ApplicationSettings.CurvatureAnalysisSettingsState"""
    def __init__(self, *args) -> None: ...
    GaussRange: Interval
    MeanRange: Interval
    MinRadiusRange: Interval
    MaxRadiusRange: Interval
    Style: CurvatureStyle

class CurvatureGraphSettings:
    """.NET: Rhino.ApplicationSettings.CurvatureGraphSettings"""
    def __init__(self, *args) -> None: ...
    CurveHairColor: Color
    SurfaceUHairColor: Color
    SurfaceVHairColor: Color
    SrfUHair: bool
    SrfVHair: bool
    HairScale: int
    HairDensity: int
    SampleDensity: int
    @staticmethod
    def GetCurrentState() -> CurvatureGraphSettingsState: ...
    @staticmethod
    def GetDefaultState() -> CurvatureGraphSettingsState: ...
    @staticmethod
    def RestoreDefaults() -> None: ...
    @staticmethod
    def UpdateFromState(state: CurvatureGraphSettingsState) -> None: ...

class CurvatureGraphSettingsState:
    """.NET: Rhino.ApplicationSettings.CurvatureGraphSettingsState"""
    def __init__(self, *args) -> None: ...
    CurveHairColor: Color
    SurfaceUHairColor: Color
    SurfaceVHairColor: Color
    SrfUHair: bool
    SrfVHair: bool
    HairScale: int
    HairDensity: int
    SampleDensity: int

class DraftAngleAnalysisSettings:
    """.NET: Rhino.ApplicationSettings.DraftAngleAnalysisSettings"""
    def __init__(self, *args) -> None: ...
    AngleRange: Interval
    ShowIsoCurves: bool
    UpDirection: Vector3d
    @staticmethod
    def GetCurrentState() -> DraftAngleAnalysisSettingsState: ...
    @staticmethod
    def GetDefaultState() -> DraftAngleAnalysisSettingsState: ...
    @staticmethod
    def RestoreDefaults() -> None: ...
    @staticmethod
    def UpdateFromState(state: DraftAngleAnalysisSettingsState) -> None: ...

class DraftAngleAnalysisSettingsState:
    """.NET: Rhino.ApplicationSettings.DraftAngleAnalysisSettingsState"""
    def __init__(self, *args) -> None: ...
    AngleRange: Interval
    ShowIsoCurves: bool
    UpDirection: Vector3d

class EdgeAnalysisSettings:
    """.NET: Rhino.ApplicationSettings.EdgeAnalysisSettings"""
    def __init__(self, *args) -> None: ...
    ShowEdgeColor: Color
    ShowEdges: int
    @staticmethod
    def GetCurrentState() -> EdgeAnalysisSettingsState: ...
    @staticmethod
    def GetDefaultState() -> EdgeAnalysisSettingsState: ...
    @staticmethod
    def RestoreDefaults() -> None: ...
    @staticmethod
    def UpdateFromState(state: EdgeAnalysisSettingsState) -> None: ...

class EdgeAnalysisSettingsState:
    """.NET: Rhino.ApplicationSettings.EdgeAnalysisSettingsState"""
    def __init__(self, *args) -> None: ...
    ShowEdgeColor: Color
    ShowEdges: int

class FileSettings:
    """.NET: Rhino.ApplicationSettings.FileSettings"""
    def __init__(self, *args) -> None: ...
    SearchPathCount: int
    WorkingFolder: str
    TemplateFolder: str
    TemplateFile: str
    AutoSaveFile: str
    AutoSaveInterval: TimeSpan
    AutoSaveEnabled: bool
    AutoSaveMeshes: bool
    SaveViewChanges: bool
    FileLockingEnabled: bool
    FileLockingOpenWarning: bool
    CreateBackupFiles: bool
    ClipboardCopyToPreviousRhinoVersion: bool
    ClipboardOnExit: ClipboardState
    ExecutableFolder: str
    InstallFolder: DirectoryInfo
    HelpFilePath: str
    LocalProfileDataFolder: str
    DefaultRuiFile: str
    @staticmethod
    def AddSearchPath(folder: str, index: int) -> int: ...
    @staticmethod
    def AutoSaveBeforeCommands() -> list: ...
    @staticmethod
    def DefaultTemplateFolderForLanguageID(languageID: int) -> str: ...
    @staticmethod
    def DeleteSearchPath(folder: str) -> bool: ...
    @staticmethod
    def FindFile(fileName: str) -> str: ...
    @staticmethod
    def GetCurrentState() -> FileSettingsState: ...
    @staticmethod
    def GetDataFolder(currentUser: bool) -> str: ...
    @staticmethod
    def GetDefaultState() -> FileSettingsState: ...
    @staticmethod
    def GetSearchPaths() -> list: ...
    @staticmethod
    def RecentlyOpenedFiles() -> list: ...
    @staticmethod
    def SetAutoSaveBeforeCommands(commands: list) -> None: ...
    @staticmethod
    def UpdateFromState(state: FileSettingsState) -> None: ...

class FileSettingsState:
    """.NET: Rhino.ApplicationSettings.FileSettingsState"""
    def __init__(self, *args) -> None: ...
    AutoSaveInterval: TimeSpan
    AutoSaveEnabled: bool
    AutoSaveMeshes: bool
    SaveViewChanges: bool
    FileLockingEnabled: bool
    FileLockingOpenWarning: bool
    ClipboardCopyToPreviousRhinoVersion: bool
    ClipboardOnExit: ClipboardState
    CreateBackupFiles: bool
    TemplateFileDir: str

class GeneralSettings:
    """.NET: Rhino.ApplicationSettings.GeneralSettings"""
    def __init__(self, *args) -> None: ...
    UseExtrusions: bool
    MouseSelectMode: MouseSelectMode
    MaximumPopupMenuLines: int
    MinimumUndoSteps: int
    MaximumUndoMemoryMb: int
    NewObjectIsoparmCount: int
    MiddleMouseMode: MiddleMouseMode
    MiddleMousePopupToolbar: str
    MiddleMouseMacro: str
    EnableContextMenu: bool
    ContextMenuDelay: TimeSpan
    AutoUpdateCommandHelp: bool
    @staticmethod
    def GetCurrentState() -> GeneralSettingsState: ...
    @staticmethod
    def GetDefaultState() -> GeneralSettingsState: ...

class GeneralSettingsState:
    """.NET: Rhino.ApplicationSettings.GeneralSettingsState"""
    def __init__(self, *args) -> None: ...
    MouseSelectMode: MouseSelectMode
    MaximumPopupMenuLines: int
    MinimumUndoSteps: int
    MaximumUndoMemoryMb: int
    NewObjectIsoparmCount: int
    MiddleMouseMode: MiddleMouseMode
    MiddleMousePopupToolbar: str
    MiddleMouseMacro: str
    EnableContextMenu: bool
    ContextMenuDelay: TimeSpan
    AutoUpdateCommandHelp: bool

class HistorySettings:
    """.NET: Rhino.ApplicationSettings.HistorySettings"""
    def __init__(self, *args) -> None: ...
    RecordingEnabled: bool
    RecordNextCommand: bool
    UpdateEnabled: bool
    ObjectLockingEnabled: bool
    BrokenRecordWarningEnabled: bool

class Installation:
    """.NET: Rhino.ApplicationSettings.Installation"""
    def __init__(self, *args) -> None: ...
    ...

class KeyboardShortcut:
    """.NET: Rhino.ApplicationSettings.KeyboardShortcut"""
    def __init__(self, *args) -> None: ...
    Modifier: ModifierKey
    Key: KeyboardKey
    Macro: str

class LicenseNode:
    """.NET: Rhino.ApplicationSettings.LicenseNode"""
    def __init__(self, *args) -> None: ...
    ...

class MiddleMouseMode:
    """.NET: Rhino.ApplicationSettings.MiddleMouseMode"""
    def __init__(self, *args) -> None: ...
    ...

class ModelAidSettings:
    """.NET: Rhino.ApplicationSettings.ModelAidSettings"""
    def __init__(self, *args) -> None: ...
    GridSnap: bool
    Ortho: bool
    Planar: bool
    ProjectSnapToCPlane: bool
    UseHorizontalDialog: bool
    ExtendTrimLines: bool
    ExtendToApparentIntersection: bool
    AltPlusArrow: bool
    DisplayControlPolygon: bool
    HighlightControlPolygon: bool
    Osnap: bool
    SnapToLocked: bool
    SnapToOccluded: bool
    SnapToFiltered: bool
    OnlySnapToSelected: bool
    OrthoUseZ: bool
    UniversalConstructionPlaneMode: bool
    AutoAlignCPlane: bool
    AutoCPlaneAlignment: int
    StickyAutoCPlane: bool
    OrientAutoCPlaneToView: bool
    OrthoAngle: float
    NudgeKeyStep: float
    CtrlNudgeKeyStep: float
    ShiftNudgeKeyStep: float
    OsnapPickboxRadius: int
    NudgeMode: int
    ControlPolygonDisplayDensity: int
    OsnapCursorMode: CursorMode
    OsnapModes: OsnapModes
    MousePickboxRadius: int
    PointDisplay: PointDisplayMode
    AutoGumballEnabled: bool
    SnappyGumballEnabled: bool
    GumballExtrudeMergeFaces: bool
    GumballAutoReset: bool
    @staticmethod
    def GetCurrentState() -> ModelAidSettingsState: ...
    @staticmethod
    def GetDefaultState() -> ModelAidSettingsState: ...
    @staticmethod
    def UpdateFromState(state: ModelAidSettingsState) -> None: ...

class ModelAidSettingsState:
    """.NET: Rhino.ApplicationSettings.ModelAidSettingsState"""
    def __init__(self, *args) -> None: ...
    GridSnap: bool
    Ortho: bool
    Planar: bool
    ProjectSnapToCPlane: bool
    UseHorizontalDialog: bool
    ExtendTrimLines: bool
    ExtendToApparentIntersection: bool
    AltPlusArrow: bool
    DisplayControlPolygon: bool
    HighlightControlPolygon: bool
    Osnap: bool
    SnapToLocked: bool
    UniversalConstructionPlaneMode: bool
    AutoAlignCPlane: bool
    AutoCPlaneAlignment: int
    StickyAutoCPlane: bool
    OrientAutoCPlaneToView: bool
    OrthoAngle: float
    NudgeKeyStep: float
    CtrlNudgeKeyStep: float
    ShiftNudgeKeyStep: float
    OsnapPickboxRadius: int
    NudgeMode: int
    ControlPolygonDisplayDensity: int
    OsnapCursorMode: CursorMode
    OsnapModes: OsnapModes
    MousePickboxRadius: int
    PointDisplay: PointDisplayMode
    OrthoUseZ: bool

class MouseSelectMode:
    """.NET: Rhino.ApplicationSettings.MouseSelectMode"""
    def __init__(self, *args) -> None: ...
    ...

class NeverRepeatList:
    """.NET: Rhino.ApplicationSettings.NeverRepeatList"""
    def __init__(self, *args) -> None: ...
    UseNeverRepeatList: bool
    @staticmethod
    def CommandNames() -> list: ...
    @staticmethod
    def SetList(commandNames: list) -> int: ...

class OpenGLSettings:
    """.NET: Rhino.ApplicationSettings.OpenGLSettings"""
    def __init__(self, *args) -> None: ...
    AntialiasLevel: AntialiasLevel
    @staticmethod
    def GetCurrentState() -> OpenGLSettingsState: ...
    @staticmethod
    def GetDefaultState() -> OpenGLSettingsState: ...
    @staticmethod
    def RestoreDefaults() -> None: ...
    @staticmethod
    def UpdateFromState(state: OpenGLSettingsState) -> None: ...

class OpenGLSettingsState:
    """.NET: Rhino.ApplicationSettings.OpenGLSettingsState"""
    def __init__(self, *args) -> None: ...
    AntialiasLevel: AntialiasLevel

class OsnapModes:
    """.NET: Rhino.ApplicationSettings.OsnapModes"""
    def __init__(self, *args) -> None: ...
    ...

class PackageManagerSettings:
    """.NET: Rhino.ApplicationSettings.PackageManagerSettings"""
    def __init__(self, *args) -> None: ...
    Sources: str

class PaintColor:
    """.NET: Rhino.ApplicationSettings.PaintColor"""
    def __init__(self, *args) -> None: ...
    ...

class PointDisplayMode:
    """.NET: Rhino.ApplicationSettings.PointDisplayMode"""
    def __init__(self, *args) -> None: ...
    ...

class SelectionFilterSettings:
    """.NET: Rhino.ApplicationSettings.SelectionFilterSettings"""
    def __init__(self, *args) -> None: ...
    GlobalGeometryFilter: ObjectType
    OneShotGeometryFilter: ObjectType
    Enabled: bool
    SubObjectSelect: bool
    @staticmethod
    def GetCurrentState() -> SelectionFilterSettingsState: ...
    @staticmethod
    def GetDefaultState() -> SelectionFilterSettingsState: ...
    @staticmethod
    def RestoreDefaults() -> None: ...
    @staticmethod
    def UpdateFromState(state: SelectionFilterSettingsState) -> None: ...

class SelectionFilterSettingsState:
    """.NET: Rhino.ApplicationSettings.SelectionFilterSettingsState"""
    def __init__(self, *args) -> None: ...
    GlobalGeometryFilter: ObjectType
    OneShotGeometryFilter: ObjectType
    Enabled: bool
    SubObjectSelect: bool

class ShortcutKey:
    """.NET: Rhino.ApplicationSettings.ShortcutKey"""
    def __init__(self, *args) -> None: ...
    ...

class ShortcutKeySettings:
    """.NET: Rhino.ApplicationSettings.ShortcutKeySettings"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetDefaults() -> list: ...
    @staticmethod
    def GetLabel(key: ShortcutKey) -> str: ...
    @staticmethod
    def GetMacro(key: ShortcutKey) -> str: ...
    @staticmethod
    def GetShortcuts() -> list: ...
    @staticmethod
    def IsAcceptableKeyCombo(key: KeyboardKey, modifier: ModifierKey) -> bool: ...
    @staticmethod
    def SetMacro(key: KeyboardKey, modifier: ModifierKey, macro: str) -> None: ...
    @staticmethod
    def Update(shortcuts: IEnumerable, replaceAll: bool) -> None: ...

class SmartTrackSettings:
    """.NET: Rhino.ApplicationSettings.SmartTrackSettings"""
    def __init__(self, *args) -> None: ...
    UseSmartTrack: bool
    UseDottedLines: bool
    SmartOrtho: bool
    SmartTangents: bool
    ActivationDelayMilliseconds: int
    MaxSmartPoints: int
    LineColor: Color
    TanPerpLineColor: Color
    PointColor: Color
    ActivePointColor: Color
    GuideColor: Color
    @staticmethod
    def GetCurrentState() -> SmartTrackSettingsState: ...
    @staticmethod
    def GetDefaultState() -> SmartTrackSettingsState: ...
    @staticmethod
    def UpdateFromState(state: SmartTrackSettingsState) -> None: ...

class SmartTrackSettingsState:
    """.NET: Rhino.ApplicationSettings.SmartTrackSettingsState"""
    def __init__(self, *args) -> None: ...
    UseSmartTrack: bool
    UseDottedLines: bool
    SmartOrtho: bool
    SmartTangents: bool
    ActivationDelayMilliseconds: int
    MaxSmartPoints: int
    LineColor: Color
    TanPerpLineColor: Color
    PointColor: Color
    ActivePointColor: Color
    GuideColor: Color

class ViewSettings:
    """.NET: Rhino.ApplicationSettings.ViewSettings"""
    def __init__(self, *args) -> None: ...
    PanScreenFraction: float
    PanReverseKeyboardAction: bool
    AlwaysPanParallelViews: bool
    ZoomScale: float
    ZoomExtentsParallelViewBorder: float
    ZoomExtentsPerspectiveViewBorder: float
    RotateCircleIncrement: int
    RotateReverseKeyboard: bool
    RotateToView: bool
    DefinedViewSetCPlane: bool
    DefinedViewSetProjection: bool
    SingleClickMaximize: bool
    LinkedViewports: bool
    DefinedViewSetClippingPlanes: bool
    DefinedViewSetDisplayMode: bool
    AutoAdjustTargetDepth: bool
    RotateViewAroundAutogumball: bool
    PanPlanParallelViewsWithControlShiftRMB: bool
    RotateViewAroundObjectAtMouseCursor: bool
    ViewRotation: ViewRotationStyle
    ThreePointPerspectiveLensLength: float
    TwoPointPerspectiveLensLength: float
    @staticmethod
    def GetCurrentState() -> ViewSettingsState: ...
    @staticmethod
    def GetDefaultState() -> ViewSettingsState: ...
    @staticmethod
    def RestoreDefaults() -> None: ...
    @staticmethod
    def UpdateFromState(state: ViewSettingsState) -> None: ...

class ViewSettingsState:
    """.NET: Rhino.ApplicationSettings.ViewSettingsState"""
    def __init__(self, *args) -> None: ...
    PanScreenFraction: float
    PanReverseKeyboardAction: bool
    AlwaysPanParallelViews: bool
    ZoomScale: float
    ZoomExtentsParallelViewBorder: float
    ZoomExtentsPerspectiveViewBorder: float
    RotateCircleIncrement: int
    RotateReverseKeyboard: bool
    RotateToView: bool
    DefinedViewSetCPlane: bool
    DefinedViewSetProjection: bool
    SingleClickMaximize: bool
    LinkedViewports: bool
    ViewRotation: ViewRotationStyle
    ThreePointPerspectiveLensLength: float
    TwoPointPerspectiveLensLength: float

class WidgetColor:
    """.NET: Rhino.ApplicationSettings.WidgetColor"""
    def __init__(self, *args) -> None: ...
    ...

class ZebraAnalysisSettings:
    """.NET: Rhino.ApplicationSettings.ZebraAnalysisSettings"""
    def __init__(self, *args) -> None: ...
    VerticalStripes: bool
    ShowIsoCurves: bool
    StripeColor: Color
    StripeThickness: int
    @staticmethod
    def GetCurrentState() -> ZebraAnalysisSettingsState: ...
    @staticmethod
    def GetDefaultState() -> ZebraAnalysisSettingsState: ...
    @staticmethod
    def RestoreDefaults() -> None: ...
    @staticmethod
    def UpdateFromState(state: ZebraAnalysisSettingsState) -> None: ...

class ZebraAnalysisSettingsState:
    """.NET: Rhino.ApplicationSettings.ZebraAnalysisSettingsState"""
    def __init__(self, *args) -> None: ...
    VerticalStripes: bool
    ShowIsoCurves: bool
    StripeColor: Color
    StripeThickness: int
