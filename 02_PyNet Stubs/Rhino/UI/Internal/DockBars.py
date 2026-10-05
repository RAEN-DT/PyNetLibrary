# Auto-generated — Rhino 8 — Rhino.Ui.Internal.DockBars

class DragStrengthPanel(Panel):
    """.NET: Rhino.Ui.Internal.DockBars.DragStrengthPanel"""
    def __init__(self, *args) -> None: ...
    DockBarId: Guid
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

class DragStrengthViewModel(ViewModel):
    """.NET: Rhino.Ui.Internal.DockBars.DragStrengthViewModel"""
    def __init__(self, *args) -> None: ...
    Strength: int
    ModelUnitSystem: UnitSystem
    PageUnitSystem: UnitSystem
    ModelDistanceDisplayMode: DistanceDisplayMode
    PageDistanceDisplayMode: DistanceDisplayMode
    ModelDistanceDisplayPrecision: int
    PageDistanceDisplayPrecision: int
    def OnLeft(self, ) -> None: ...
    def OnRight(self, ) -> None: ...
