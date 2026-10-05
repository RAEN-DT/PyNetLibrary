# Auto-generated — Rhino 8 — Rhino.UI.ViewModels

class AnnotationException(Exception):
    """.NET: Rhino.UI.ViewModels.AnnotationException"""
    def __init__(self, *args) -> None: ...
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str

class PreviousFilterState:
    """.NET: Rhino.UI.ViewModels.PreviousFilterState"""
    def __init__(self, *args) -> None: ...
    GlobalFilterState: ObjectType
    OneShotFilterState: ObjectType
    Annotation: bool
    Blocks: bool
    ControlPoints: bool
    Curves: bool
    Hatches: bool
    Lights: bool
    Meshes: bool
    Others: bool
    Points: bool
    PointClouds: bool
    PolySurfaces: bool
    Surfaces: bool
    SubD: bool
    LastSelection: int
    OneShot: bool

class SelectionFilterViewModel(ViewModel):
    """.NET: Rhino.UI.ViewModels.SelectionFilterViewModel"""
    def __init__(self, *args) -> None: ...
    EventSet: bool
    LostFocus: bool
    OneShotFilterState: bool
    PersistentFilterState: bool
    DisableCheckBoxVisibilityState: bool
    UiLayoutIsDirty: bool
    Annotations: bool
    Blocks: bool
    ControlPoints: bool
    Curves: bool
    Hatches: bool
    Lights: bool
    Meshes: bool
    Others: bool
    Points: bool
    PointClouds: bool
    PolySurfaces: bool
    SubD: bool
    Surfaces: bool
    Disable: bool
    CheckBoxEnabledState: bool
    SubObjects: bool
    ControlId: str
    LastControlId: str
    ControlIdCheckState: bool
    ModelUnitSystem: UnitSystem
    PageUnitSystem: UnitSystem
    ModelDistanceDisplayMode: DistanceDisplayMode
    PageDistanceDisplayMode: DistanceDisplayMode
    ModelDistanceDisplayPrecision: int
    PageDistanceDisplayPrecision: int
    def Closing(self, ) -> None: ...
    def FilterEvent(self, ) -> None: ...
    def GetAppFilterState(self, ) -> None: ...
    def OneShotSelectionValidateOnLostFocus(self, ) -> None: ...
    def PlayRightClickState(self, obj: Nullable) -> None: ...
    def RecordPreviousState(self, ) -> None: ...
    def Shown(self, ) -> None: ...
