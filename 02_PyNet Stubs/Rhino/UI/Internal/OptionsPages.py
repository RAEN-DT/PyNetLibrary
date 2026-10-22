# Auto-generated — Rhino 8 — Rhino.UI.Internal.OptionsPages

class AppearancePage(Scrollable):
    """.NET: Rhino.UI.Internal.OptionsPages.AppearancePage"""
    def __init__(self, *args) -> None: ...
    HelpUrl: str
    ScrollPosition: Point
    ScrollSize: Size
    Border: BorderType
    VisibleRect: Rectangle
    ExpandContentWidth: bool
    ExpandContentHeight: bool
    MinimumZoom: float
    MaximumZoom: float
    Zoom: float
    Controls: IEnumerable
    Padding: Padding
    MinimumSize: Size
    ContextMenu: ContextMenu
    Content: Control
    ClientSize: Size
    Children: IEnumerable
    VisualChildren: IEnumerable
    StyleProvider: IStyleProvider
    Styles: DefaultStyleProvider
    Loaded: bool
    VisualControls: IEnumerable
    Tag: object
    LogicalParent: Container
    IsVisualControl: bool
    Size: Size
    IsMouseCaptured: bool
    Width: int
    Height: int
    Enabled: bool
    Visible: bool
    Parent: Container
    VisualParent: Container
    IsAttached: bool
    BackgroundColor: Color
    HasFocus: bool
    IsSuspended: bool
    ParentWindow: Window
    SupportedPlatformCommands: IEnumerable
    Bounds: Rectangle
    Location: Point
    Cursor: Cursor
    ToolTip: str
    TabIndex: int
    AllowDrop: bool
    Parents: IEnumerable
    DataContext: object
    Bindings: BindingCollection
    IsDataContextChanging: bool
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    def OnApply(self, ) -> bool: ...
    def OnCancel(self, ) -> None: ...
    def OnDefaults(self, ) -> None: ...
    def OnHelp(self, ) -> None: ...
    def OnHidePage(self, ) -> bool: ...
    def OnShowPage(self, ) -> bool: ...
    def RunScript(self, doc: RhinoDoc, mode: RunMode) -> Result: ...

class AppearanceViewModel(ViewModel):
    """.NET: Rhino.UI.Internal.OptionsPages.AppearanceViewModel"""
    def __init__(self, *args) -> None: ...
    FontQuartets: List
    SelectedFontName: str
    Languages: List
    LanguageIndex: int
    CommandTextSize: int
    BackgroundColor: Color
    TextColor: Color
    HoverColor: Color
    EchoPromptsToHistory: bool
    AutocompleteCommands: bool
    UseFuzzyAutocomplete: bool
    ArrowIconShaftSize: int
    ArrowIconHeadSize: int
    ShowMenu: bool
    ShowCommandPrompt: bool
    ShowStatusBar: bool
    ShowViewportTitles: bool
    ShowTitleBar: bool
    ShowFullPath: bool
    ShowCrosshairs: bool
    ViewportTabsAtStart: bool
    Document: RhinoDoc
    ModelUnitSystem: UnitSystem
    PageUnitSystem: UnitSystem
    ModelDistanceDisplayMode: DistanceDisplayMode
    PageDistanceDisplayMode: DistanceDisplayMode
    ModelDistanceDisplayPrecision: int
    PageDistanceDisplayPrecision: int
    def IsValidFontName(self, fontName: str) -> bool: ...
    def OnApply(self, ) -> None: ...
    def OnCancel(self, ) -> None: ...
    def OnDefaults(self, ) -> None: ...
    def OnShowPage(self, ) -> None: ...
    def RunCommandPromptFontAndSizeScript(self, doc: RhinoDoc, mode: RunMode) -> Result: ...
    def RunCommandPromptFontScript(self, doc: RhinoDoc, mode: RunMode) -> Result: ...
    def RunCommandPromptScript(self, doc: RhinoDoc, mode: RunMode) -> Result: ...
    def RunDirArrowScript(self, doc: RhinoDoc, mode: RunMode) -> Result: ...
    def RunMacScript(self, doc: RhinoDoc, mode: RunMode) -> Result: ...
    def RunScript(self, doc: RhinoDoc, mode: RunMode) -> Result: ...
    def RunVisibleScript(self, doc: RhinoDoc, mode: RunMode) -> Result: ...
    def RunWindowsScript(self, doc: RhinoDoc, mode: RunMode) -> Result: ...

class ColorsPage(Scrollable):
    """.NET: Rhino.UI.Internal.OptionsPages.ColorsPage"""
    def __init__(self, *args) -> None: ...
    HelpUrl: str
    ScrollPosition: Point
    ScrollSize: Size
    Border: BorderType
    VisibleRect: Rectangle
    ExpandContentWidth: bool
    ExpandContentHeight: bool
    MinimumZoom: float
    MaximumZoom: float
    Zoom: float
    Controls: IEnumerable
    Padding: Padding
    MinimumSize: Size
    ContextMenu: ContextMenu
    Content: Control
    ClientSize: Size
    Children: IEnumerable
    VisualChildren: IEnumerable
    StyleProvider: IStyleProvider
    Styles: DefaultStyleProvider
    Loaded: bool
    VisualControls: IEnumerable
    Tag: object
    LogicalParent: Container
    IsVisualControl: bool
    Size: Size
    IsMouseCaptured: bool
    Width: int
    Height: int
    Enabled: bool
    Visible: bool
    Parent: Container
    VisualParent: Container
    IsAttached: bool
    BackgroundColor: Color
    HasFocus: bool
    IsSuspended: bool
    ParentWindow: Window
    SupportedPlatformCommands: IEnumerable
    Bounds: Rectangle
    Location: Point
    Cursor: Cursor
    ToolTip: str
    TabIndex: int
    AllowDrop: bool
    Parents: IEnumerable
    DataContext: object
    Bindings: BindingCollection
    IsDataContextChanging: bool
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    def OnApply(self, ) -> bool: ...
    def OnCancel(self, ) -> None: ...
    def OnDefaults(self, ) -> None: ...
    def OnHelp(self, ) -> None: ...
    def OnHidePage(self, ) -> bool: ...
    def OnShowPage(self, ) -> bool: ...
    def RunScript(self, doc: RhinoDoc, mode: RunMode) -> Result: ...

class GridSettingsPage(Panel):
    """.NET: Rhino.UI.Internal.OptionsPages.GridSettingsPage"""
    def __init__(self, *args) -> None: ...
    Document: RhinoDoc
    HelpUrl: str
    Controls: IEnumerable
    Padding: Padding
    MinimumSize: Size
    ContextMenu: ContextMenu
    Content: Control
    ClientSize: Size
    Children: IEnumerable
    VisualChildren: IEnumerable
    StyleProvider: IStyleProvider
    Styles: DefaultStyleProvider
    Loaded: bool
    VisualControls: IEnumerable
    Tag: object
    LogicalParent: Container
    IsVisualControl: bool
    Size: Size
    IsMouseCaptured: bool
    Width: int
    Height: int
    Enabled: bool
    Visible: bool
    Parent: Container
    VisualParent: Container
    IsAttached: bool
    BackgroundColor: Color
    HasFocus: bool
    IsSuspended: bool
    ParentWindow: Window
    SupportedPlatformCommands: IEnumerable
    Bounds: Rectangle
    Location: Point
    Cursor: Cursor
    ToolTip: str
    TabIndex: int
    AllowDrop: bool
    Parents: IEnumerable
    DataContext: object
    Bindings: BindingCollection
    IsDataContextChanging: bool
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    def OnApply(self, ) -> bool: ...
    def OnCancel(self, ) -> None: ...
    def OnDefaults(self, ) -> None: ...
    def OnHelp(self, ) -> None: ...
    def OnHidePage(self, ) -> bool: ...
    def OnShowPage(self, ) -> bool: ...
    def RunScript(self, doc: RhinoDoc, mode: RunMode) -> Result: ...

class GridSettingsViewModel(ViewModel):
    """.NET: Rhino.UI.Internal.OptionsPages.GridSettingsViewModel"""
    def __init__(self, *args) -> None: ...
    Document: RhinoDoc
    Panel: GridSettingsPage
    GridUnits: str
    SnapUnits: str
    GridSpacing: float
    SnapSpacing: float
    GridLineCount: int
    GridThickLineFrequency: int
    ShowGridLines: bool
    ShowGridAxes: bool
    ApplyToIndex: int
    ApplyToAll: bool
    ShowWorldAxes: bool
    ModelUnitSystem: UnitSystem
    PageUnitSystem: UnitSystem
    ModelDistanceDisplayMode: DistanceDisplayMode
    PageDistanceDisplayMode: DistanceDisplayMode
    ModelDistanceDisplayPrecision: int
    PageDistanceDisplayPrecision: int
    def ActiveView(self, ) -> RhinoView: ...
    def Cancel(self, bCurrent: bool) -> None: ...
    def UpdateViews(self, bScriptMode: bool) -> bool: ...

class IOptionsPage:
    """.NET: Rhino.UI.Internal.OptionsPages.IOptionsPage"""
    def __init__(self, *args) -> None: ...
    def OnApply(self, ) -> bool: ...
    def OnCancel(self, ) -> None: ...
    def OnDefaults(self, ) -> None: ...
    def OnHelp(self, ) -> None: ...
    def OnHidePage(self, ) -> bool: ...
    def OnShowPage(self, ) -> bool: ...
    def RunScript(self, doc: RhinoDoc, mode: RunMode) -> Result: ...

class KeyboardShortcutsPage(Panel):
    """.NET: Rhino.UI.Internal.OptionsPages.KeyboardShortcutsPage"""
    def __init__(self, *args) -> None: ...
    Controls: IEnumerable
    Padding: Padding
    MinimumSize: Size
    ContextMenu: ContextMenu
    Content: Control
    ClientSize: Size
    Children: IEnumerable
    VisualChildren: IEnumerable
    StyleProvider: IStyleProvider
    Styles: DefaultStyleProvider
    Loaded: bool
    VisualControls: IEnumerable
    Tag: object
    LogicalParent: Container
    IsVisualControl: bool
    Size: Size
    IsMouseCaptured: bool
    Width: int
    Height: int
    Enabled: bool
    Visible: bool
    Parent: Container
    VisualParent: Container
    IsAttached: bool
    BackgroundColor: Color
    HasFocus: bool
    IsSuspended: bool
    ParentWindow: Window
    SupportedPlatformCommands: IEnumerable
    Bounds: Rectangle
    Location: Point
    Cursor: Cursor
    ToolTip: str
    TabIndex: int
    AllowDrop: bool
    Parents: IEnumerable
    DataContext: object
    Bindings: BindingCollection
    IsDataContextChanging: bool
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    @staticmethod
    def NewHost() -> OptionsPageHost: ...
    def OnApply(self, ) -> bool: ...
    def OnCancel(self, ) -> None: ...
    def OnDefaults(self, ) -> None: ...
    def OnHelp(self, ) -> None: ...
    def OnHidePage(self, ) -> bool: ...
    def OnShowPage(self, ) -> bool: ...
    def RunScript(self, doc: RhinoDoc, mode: RunMode) -> Result: ...

class OptionsPageHost(OptionsDialogPage):
    """.NET: Rhino.UI.Internal.OptionsPages.OptionsPageHost"""
    def __init__(self, *args) -> None: ...
    PageControl: object
    LocalPageTitle: str
    PageImage: Image
    ShowDefaultsButton: bool
    ShowApplyButton: bool
    OptionsPageType: PageType
    Children: List
    HasChildren: bool
    Modified: bool
    Handle: IntPtr
    EnglishPageTitle: str
    NavigationTextIsBold: bool
    NavigationTextColor: Color
    def OnActivate(self, active: bool) -> bool: ...
    def OnApply(self, ) -> bool: ...
    def OnCancel(self, ) -> None: ...
    def OnDefaults(self, ) -> None: ...
    def OnHelp(self, ) -> None: ...
    def RunScript(self, doc: RhinoDoc, mode: RunMode) -> Result: ...

class SelectionMenuPage(Panel):
    """.NET: Rhino.UI.Internal.OptionsPages.SelectionMenuPage"""
    def __init__(self, *args) -> None: ...
    Document: RhinoDoc
    HelpUrl: str
    Controls: IEnumerable
    Padding: Padding
    MinimumSize: Size
    ContextMenu: ContextMenu
    Content: Control
    ClientSize: Size
    Children: IEnumerable
    VisualChildren: IEnumerable
    StyleProvider: IStyleProvider
    Styles: DefaultStyleProvider
    Loaded: bool
    VisualControls: IEnumerable
    Tag: object
    LogicalParent: Container
    IsVisualControl: bool
    Size: Size
    IsMouseCaptured: bool
    Width: int
    Height: int
    Enabled: bool
    Visible: bool
    Parent: Container
    VisualParent: Container
    IsAttached: bool
    BackgroundColor: Color
    HasFocus: bool
    IsSuspended: bool
    ParentWindow: Window
    SupportedPlatformCommands: IEnumerable
    Bounds: Rectangle
    Location: Point
    Cursor: Cursor
    ToolTip: str
    TabIndex: int
    AllowDrop: bool
    Parents: IEnumerable
    DataContext: object
    Bindings: BindingCollection
    IsDataContextChanging: bool
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    def OnApply(self, ) -> bool: ...
    def OnCancel(self, ) -> None: ...
    def OnDefaults(self, ) -> None: ...
    def OnHelp(self, ) -> None: ...
    def OnHidePage(self, ) -> bool: ...
    def OnShowPage(self, ) -> bool: ...
    def RunScript(self, doc: RhinoDoc, mode: RunMode) -> Result: ...

class SelectionMenuViewModel(ViewModel):
    """.NET: Rhino.UI.Internal.OptionsPages.SelectionMenuViewModel"""
    def __init__(self, *args) -> None: ...
    Document: RhinoDoc
    XOffset: int
    YOffset: int
    MaxAutomaticHeight: int
    AutomaticResize: bool
    ShowTitlebarAndBorder: bool
    ShowObjectName: bool
    EnableObjectTypeDetails: bool
    ShowObjectType: bool
    ShowObjectLayer: bool
    ShowObjectColor: bool
    ShowObjectTypeDetails: bool
    ShowAllOption: bool
    DynamicHighlight: bool
    UseCustomColor: bool
    HighlightColor: Color
    FollowCursor: bool
    ModelUnitSystem: UnitSystem
    PageUnitSystem: UnitSystem
    ModelDistanceDisplayMode: DistanceDisplayMode
    PageDistanceDisplayMode: DistanceDisplayMode
    ModelDistanceDisplayPrecision: int
    PageDistanceDisplayPrecision: int
    def Cancel(self, ) -> None: ...
    def Defaults(self, ) -> None: ...
    def RunScript(self, doc: RhinoDoc) -> Result: ...
    def SetOriginalValues(self, ) -> None: ...

class UnitsSettingsPage(Panel):
    """.NET: Rhino.UI.Internal.OptionsPages.UnitsSettingsPage"""
    def __init__(self, *args) -> None: ...
    HelpUrl: str
    Controls: IEnumerable
    Padding: Padding
    MinimumSize: Size
    ContextMenu: ContextMenu
    Content: Control
    ClientSize: Size
    Children: IEnumerable
    VisualChildren: IEnumerable
    StyleProvider: IStyleProvider
    Styles: DefaultStyleProvider
    Loaded: bool
    VisualControls: IEnumerable
    Tag: object
    LogicalParent: Container
    IsVisualControl: bool
    Size: Size
    IsMouseCaptured: bool
    Width: int
    Height: int
    Enabled: bool
    Visible: bool
    Parent: Container
    VisualParent: Container
    IsAttached: bool
    BackgroundColor: Color
    HasFocus: bool
    IsSuspended: bool
    ParentWindow: Window
    SupportedPlatformCommands: IEnumerable
    Bounds: Rectangle
    Location: Point
    Cursor: Cursor
    ToolTip: str
    TabIndex: int
    AllowDrop: bool
    Parents: IEnumerable
    DataContext: object
    Bindings: BindingCollection
    IsDataContextChanging: bool
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    def OnApply(self, ) -> bool: ...
    def OnCancel(self, ) -> None: ...
    def OnDefaults(self, ) -> None: ...
    def OnHelp(self, ) -> None: ...
    def OnHidePage(self, ) -> bool: ...
    def OnShowPage(self, ) -> bool: ...
    def RunScript(self, doc: RhinoDoc, mode: RunMode) -> Result: ...

class UnitsSettingsViewModel(ViewModel):
    """.NET: Rhino.UI.Internal.OptionsPages.UnitsSettingsViewModel"""
    def __init__(self, *args) -> None: ...
    IsPageSettings: bool
    Units: UnitSystem
    AllowFeetAndInches: bool
    DisplayPrecision: int
    DisplayDecimal: bool
    DisplayFractional: bool
    DisplayFeetAndInches: bool
    Document: RhinoDoc
    DisplayPrecisionList: List
    UnitsTypeString: str
    AbsoluteTolerance: float
    AngleToleranceInDegrees: float
    UnitsString: str
    CustomUnitsString: str
    MetersPerCustomUnit: float
    CustomEnabled: bool
    ModelUnitSystem: UnitSystem
    PageUnitSystem: UnitSystem
    ModelDistanceDisplayMode: DistanceDisplayMode
    PageDistanceDisplayMode: DistanceDisplayMode
    ModelDistanceDisplayPrecision: int
    PageDistanceDisplayPrecision: int
    def DisplayAbsoluteToleranceMessagebox(self, ) -> None: ...
    def DisplayAngleToleranceMessagebox(self, ) -> None: ...
    def OnApply(self, bScripted: bool) -> None: ...
    def OnCancel(self, ) -> None: ...
    def OnShowPage(self, ) -> None: ...
    def RunScript(self, ) -> Result: ...
