# Auto-generated — Rhino 8 — Rhino.UI.DialogPanels

class CommandHelpPanel(Panel):
    """.NET: Rhino.UI.DialogPanels.CommandHelpPanel"""
    def __init__(self, *args) -> None: ...
    Id: Guid
    TextBox: TextBox
    Instance: CommandHelpPanel
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
    def CommandHelpUrl(self, path: str, url: str, forContextHelp: bool, helpIsLocal: bool) -> None: ...
    def FindCommand(self, commandname: str, bClicked: bool) -> bool: ...
    def GetLanguageString(self, language_id: int) -> str: ...
    def OnCloseDocument(self, sender: object, args: DocumentEventArgs) -> None: ...
    def PanelClosing(self, documentSerialNumber: int, onCloseDocument: bool) -> None: ...
    def PanelHidden(self, documentSerialNumber: int, reason: ShowPanelReason) -> None: ...
    def PanelShown(self, documentSerialNumber: int, reason: ShowPanelReason) -> None: ...
    @staticmethod
    def Register() -> None: ...

class CommandHistoryPanel(Panel):
    """.NET: Rhino.UI.DialogPanels.CommandHistoryPanel"""
    def __init__(self, *args) -> None: ...
    HelpUrl: str
    PanelId: Guid
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
    def PanelClosing(self, documentSerialNumber: int, onCloseDocument: bool) -> None: ...
    def PanelHidden(self, documentSerialNumber: int, reason: ShowPanelReason) -> None: ...
    def PanelShown(self, documentSerialNumber: int, reason: ShowPanelReason) -> None: ...

class DetailedMeshPropertiesDialog(CommandDialog):
    """.NET: Rhino.UI.DialogPanels.DetailedMeshPropertiesDialog"""
    def __init__(self, *args) -> None: ...
    Content: Control
    ButtonOptions: Control
    ShowHelpButton: bool
    SavePosition: bool
    UpdateSourceOnApply: bool
    Buttons: ShowButtons
    FocusDefaultButtonOnLoad: bool
    Result: Result
    DisplayMode: DialogDisplayMode
    AbortButton: Button
    DefaultButton: Button
    PositiveButtons: Collection
    NegativeButtons: Collection
    Title: str
    Location: Point
    Bounds: Rectangle
    ToolBar: ToolBar
    Opacity: float
    Owner: Window
    Screen: Screen
    Menu: MenuBar
    Icon: Icon
    Resizable: bool
    Maximizable: bool
    Minimizable: bool
    Closeable: bool
    ShowInTaskbar: bool
    Topmost: bool
    WindowState: WindowState
    RestoreBounds: Rectangle
    WindowStyle: WindowStyle
    LogicalPixelSize: float
    MovableByWindowBackground: bool
    AutoSize: bool
    Controls: IEnumerable
    Padding: Padding
    MinimumSize: Size
    ContextMenu: ContextMenu
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

class DisplayPropertiesPanel(Panel):
    """.NET: Rhino.UI.DialogPanels.DisplayPropertiesPanel"""
    def __init__(self, *args) -> None: ...
    ViewModel: DisplayPropertiesViewModel
    PanelId: Guid
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
    def PanelClosing(self, documentSerialNumber: int, onCloseDocument: bool) -> None: ...
    def PanelHidden(self, documentSerialNumber: int, reason: ShowPanelReason) -> None: ...
    def PanelShown(self, documentSerialNumber: int, reason: ShowPanelReason) -> None: ...

class DisplayPropertiesViewModel(ViewModel):
    """.NET: Rhino.UI.DialogPanels.DisplayPropertiesViewModel"""
    def __init__(self, *args) -> None: ...
    DocumentSerialNumber: int
    Document: RhinoDoc
    ActiveViewport: str
    DisplayModeDescriptions: List
    SelectedDisplayModeIndex: int
    FlairModeDescriptions: List
    CurveTaperDescriptions: List
    CurveTaperSelectedIndex: int
    SelectedFlairModeIndex: int
    EndWidth: float
    TaperWidth: float
    TaperPosition: float
    CurveWidth: float
    BackgroundModeDescriptions: List
    SelectedBackgroundModeIndex: int
    FlatShading: bool
    ShadeVertexColors: bool
    Shadows: bool
    SurfaceIsoCurves: bool
    SurfaceEdges: bool
    TangentEdges: bool
    TangentSeams: bool
    SubDWires: bool
    SubDCreases: bool
    SubDBoundaries: bool
    SubDSymmetry: bool
    MeshWires: bool
    Curves: bool
    Lights: bool
    ClippingPlanes: bool
    Text: bool
    Annotations: bool
    Points: bool
    PointClouds: bool
    Transparency: int
    Grid: bool
    CPlaneAxes: bool
    ZAxis: bool
    WorldIcon: bool
    ColorBackFaces: bool
    BackFaceColor: Color
    BBoxDisplay: bool
    ShowEdges: bool
    ActiveViewId: Guid
    ModelUnitSystem: UnitSystem
    PageUnitSystem: UnitSystem
    ModelDistanceDisplayMode: DistanceDisplayMode
    PageDistanceDisplayMode: DistanceDisplayMode
    ModelDistanceDisplayPrecision: int
    PageDistanceDisplayPrecision: int
    def StartDocumentEventWatchers(self, ) -> None: ...
    def StopDocumentEventWatchers(self, ) -> None: ...

class EtoCommandHistoryPanel(CommandHistoryPanel):
    """.NET: Rhino.UI.DialogPanels.EtoCommandHistoryPanel"""
    def __init__(self, *args) -> None: ...
    PanelId: Guid
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
    @staticmethod
    def Register() -> None: ...

class HatchImport(ViewModel):
    """.NET: Rhino.UI.DialogPanels.HatchImport"""
    def __init__(self, *args) -> None: ...
    HatchPattern: HatchPattern
    Checked: bool
    CheckIcon: Image
    ModelUnitSystem: UnitSystem
    PageUnitSystem: UnitSystem
    ModelDistanceDisplayMode: DistanceDisplayMode
    PageDistanceDisplayMode: DistanceDisplayMode
    ModelDistanceDisplayPrecision: int
    PageDistanceDisplayPrecision: int

class HatchImportUi(CommandDialog):
    """.NET: Rhino.UI.DialogPanels.HatchImportUi"""
    def __init__(self, *args) -> None: ...
    Content: Control
    ButtonOptions: Control
    ShowHelpButton: bool
    SavePosition: bool
    UpdateSourceOnApply: bool
    Buttons: ShowButtons
    FocusDefaultButtonOnLoad: bool
    Result: Result
    DisplayMode: DialogDisplayMode
    AbortButton: Button
    DefaultButton: Button
    PositiveButtons: Collection
    NegativeButtons: Collection
    Title: str
    Location: Point
    Bounds: Rectangle
    ToolBar: ToolBar
    Opacity: float
    Owner: Window
    Screen: Screen
    Menu: MenuBar
    Icon: Icon
    Resizable: bool
    Maximizable: bool
    Minimizable: bool
    Closeable: bool
    ShowInTaskbar: bool
    Topmost: bool
    WindowState: WindowState
    RestoreBounds: Rectangle
    WindowStyle: WindowStyle
    LogicalPixelSize: float
    MovableByWindowBackground: bool
    AutoSize: bool
    Controls: IEnumerable
    Padding: Padding
    MinimumSize: Size
    ContextMenu: ContextMenu
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

class LayersPanel(Panel):
    """.NET: Rhino.UI.DialogPanels.LayersPanel"""
    def __init__(self, *args) -> None: ...
    PanelId: Guid
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
    def PanelClosing(self, documentSerialNumber: int, onCloseDocument: bool) -> None: ...
    def PanelHidden(self, documentSerialNumber: int, reason: ShowPanelReason) -> None: ...
    def PanelShown(self, documentSerialNumber: int, reason: ShowPanelReason) -> None: ...
    @staticmethod
    def Register() -> None: ...

class Linetype(Panel):
    """.NET: Rhino.UI.DialogPanels.Linetype"""
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
    def Register() -> None: ...

class LinetypeTempItem(ViewModel):
    """.NET: Rhino.UI.DialogPanels.LinetypeTempItem"""
    def __init__(self, *args) -> None: ...
    DocumentRuntimeSerial: int
    ConvertRequired: bool
    LineType: Linetype
    Width: float
    TaperEnabled: bool
    TaperEndWidth: float
    TaperWidth: float
    TaperPosition: float
    AlwaysModelDistances: bool
    Name: str
    Pattern: str
    CanDelete: bool
    DeleteImage: Image
    SelectedPatternUnitIndex: int
    SelectedCapStyleIndex: int
    SelectedJoinStyleIndex: int
    WidthUnitSystem: UnitSystem
    SelectedWidthUnitIndex: int
    IsMillimeter: bool
    BlockUsage: int
    ObjectUsage: int
    LayerUsage: int
    ToolTip: str
    Usage: Image
    UsageIndex: int
    ModelUnitSystem: UnitSystem
    PageUnitSystem: UnitSystem
    ModelDistanceDisplayMode: DistanceDisplayMode
    PageDistanceDisplayMode: DistanceDisplayMode
    ModelDistanceDisplayPrecision: int
    PageDistanceDisplayPrecision: int

class LinetypesCommandPanel(Panel):
    """.NET: Rhino.UI.DialogPanels.LinetypesCommandPanel"""
    def __init__(self, *args) -> None: ...
    PanelId: Guid
    SetupMode: bool
    HelpUrl: str
    ViewModel: LinetypesCommandPanelViewModel
    DocumentSerial: int
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
    def PanelClosing(self, documentSerialNumber: int, onCloseDocument: bool) -> None: ...
    def PanelHidden(self, documentSerialNumber: int, reason: ShowPanelReason) -> None: ...
    def PanelShown(self, documentSerialNumber: int, reason: ShowPanelReason) -> None: ...

class LinetypesCommandPanelViewModel(ViewModel):
    """.NET: Rhino.UI.DialogPanels.LinetypesCommandPanelViewModel"""
    def __init__(self, *args) -> None: ...
    LineTypeCollection: FilterCollection
    FilterText: str
    CurrentLineTypeItem: LinetypeTempItem
    DocumentSerial: int
    LinetypeScaleValue: float
    Pattern: str
    PatternIsMillimeter: bool
    SelectedGridViewIndex: int
    SelectedRow: int
    SelectedPatternUnitIndex: int
    SortByName: bool
    SortByPattern: bool
    SortIndex: int
    UnitList: IEnumerable
    ModelUnitSystem: UnitSystem
    PageUnitSystem: UnitSystem
    ModelDistanceDisplayMode: DistanceDisplayMode
    PageDistanceDisplayMode: DistanceDisplayMode
    ModelDistanceDisplayPrecision: int
    PageDistanceDisplayPrecision: int
    def AddCommand(self, ) -> None: ...
    def CopyCommand(self, ) -> None: ...
    def DeleteCommand(self, ) -> None: ...
    def ImportButtonCommand(self, ) -> None: ...
    def LoadLineTypeCollection(self, reset: bool, reloadDeleted: bool) -> None: ...
    def ReloadDeletedDefaultLinetypes(self, ) -> None: ...
    def ReloadLinetypes(self, doc: RhinoDoc) -> None: ...
    def SortLinetypes(self, e: GridColumnEventArgs) -> None: ...
    def SortLinetypesByName(self, ascending: bool, reset: bool) -> None: ...
    def SortLinetypesByPattern(self, ascending: bool, reset: bool) -> None: ...
    def StartEventWatchers(self, ) -> None: ...
    def StopEventWatchers(self, ) -> None: ...

class MeshPropertiesViewModel(ViewModel):
    """.NET: Rhino.UI.DialogPanels.MeshPropertiesViewModel"""
    def __init__(self, *args) -> None: ...
    Document: RhinoDoc
    MeshingParameters: MeshingParameters
    Density: float
    MaximumAngle: float
    MaximumAspectRatio: float
    MinimumEdgeLength: float
    MaximumEdgeLength: float
    MaximumDistanceEdgeToSrf: float
    MinimumInitialGridQuads: float
    RefineMesh: bool
    JaggedSeams: bool
    SimplePlanes: bool
    PackTextures: bool
    SubDDivisionLevel: int
    ModelUnitSystem: UnitSystem
    PageUnitSystem: UnitSystem
    ModelDistanceDisplayMode: DistanceDisplayMode
    PageDistanceDisplayMode: DistanceDisplayMode
    ModelDistanceDisplayPrecision: int
    PageDistanceDisplayPrecision: int

class NotesPanel(Panel):
    """.NET: Rhino.UI.DialogPanels.NotesPanel"""
    def __init__(self, *args) -> None: ...
    Id: Guid
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
    def PanelClosing(self, documentSerialNumber: int, onCloseDocument: bool) -> None: ...
    def PanelHidden(self, documentSerialNumber: int, reason: ShowPanelReason) -> None: ...
    def PanelShown(self, documentSerialNumber: int, reason: ShowPanelReason) -> None: ...
    @staticmethod
    def Register() -> None: ...

class OSnapPanel(Panel):
    """.NET: Rhino.UI.DialogPanels.OSnapPanel"""
    def __init__(self, *args) -> None: ...
    PanelId: Guid
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
    def PanelClosing(self, documentSerialNumber: int, onCloseDocument: bool) -> None: ...
    def PanelHidden(self, documentSerialNumber: int, reason: ShowPanelReason) -> None: ...
    def PanelShown(self, documentSerialNumber: int, reason: ShowPanelReason) -> None: ...

class PlotWidth(Panel):
    """.NET: Rhino.UI.DialogPanels.PlotWidth"""
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
    def Register() -> None: ...

class RhinoDocUndoRecord:
    """.NET: Rhino.UI.DialogPanels.RhinoDocUndoRecord"""
    def __init__(self, *args) -> None: ...
    def Dispose(self, ) -> None: ...

class SelectionFilterUi(Panel):
    """.NET: Rhino.UI.DialogPanels.SelectionFilterUi"""
    def __init__(self, *args) -> None: ...
    ViewModel: SelectionFilterViewModel
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
    def GetCurrentControlLayout(self, ) -> None: ...
    def PanelClosing(self, documentSerialNumber: int, onCloseDocument: bool) -> None: ...
    def PanelHidden(self, documentSerialNumber: int, reason: ShowPanelReason) -> None: ...
    def PanelShown(self, documentSerialNumber: int, reason: ShowPanelReason) -> None: ...

class TutorialsPanel(Panel):
    """.NET: Rhino.UI.DialogPanels.TutorialsPanel"""
    def __init__(self, *args) -> None: ...
    Id: Guid
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
    def PanelClosing(self, documentSerialNumber: int, onCloseDocument: bool) -> None: ...
    def PanelHidden(self, documentSerialNumber: int, reason: ShowPanelReason) -> None: ...
    def PanelShown(self, documentSerialNumber: int, reason: ShowPanelReason) -> None: ...
    @staticmethod
    def Register() -> None: ...

class WebBrowserPanel(Panel):
    """.NET: Rhino.UI.DialogPanels.WebBrowserPanel"""
    def __init__(self, *args) -> None: ...
    PanelId: Guid
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
    def PanelClosing(self, documentSerialNumber: int, onCloseDocument: bool) -> None: ...
    def PanelHidden(self, documentSerialNumber: int, reason: ShowPanelReason) -> None: ...
    def PanelShown(self, documentSerialNumber: int, reason: ShowPanelReason) -> None: ...
    @staticmethod
    def Register() -> None: ...
