# Auto-generated — Rhino 8 — Eto.Forms.ThemedControls

class ThemedAboutDialogHandler(WidgetHandler):
    """.NET: Eto.Forms.ThemedControls.ThemedAboutDialogHandler"""
    def __init__(self, *args) -> None: ...
    Copyright: str
    Designers: list
    Developers: list
    Documenters: list
    License: str
    Logo: Image
    ProgramDescription: str
    ProgramName: str
    Title: str
    Version: str
    Website: Uri
    WebsiteLabel: str
    Callback: ICallback
    Control: Dialog
    HasControl: bool
    Widget: AboutDialog
    ID: str
    NativeHandle: IntPtr
    def ShowDialog(self, parent: Window) -> DialogResult: ...

class ThemedButtonSegmentedItemHandler(ThemedSegmentedItemHandler):
    """.NET: Eto.Forms.ThemedControls.ThemedButtonSegmentedItemHandler"""
    def __init__(self, *args) -> None: ...
    Enabled: bool
    Visible: bool
    ToolTip: str
    Width: int
    Text: str
    Image: Image
    Selected: bool
    Callback: ICallback
    Control: ToggleButton
    HasControl: bool
    Widget: ButtonSegmentedItem
    ID: str
    NativeHandle: IntPtr

class ThemedCollectionEditor(Panel):
    """.NET: Eto.Forms.ThemedControls.ThemedCollectionEditor"""
    def __init__(self, *args) -> None: ...
    DataStore: IEnumerable
    ElementType: Type
    ExtraContent: Control
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

class ThemedCollectionEditorHandler(ThemedControlHandler):
    """.NET: Eto.Forms.ThemedControls.ThemedCollectionEditorHandler"""
    def __init__(self, *args) -> None: ...
    DataStore: IEnumerable
    ElementType: Type
    BackgroundColor: Color
    VisualControls: IEnumerable
    PropagateLoadEvents: bool
    Size: Size
    Width: int
    Height: int
    Enabled: bool
    HasFocus: bool
    Visible: bool
    SupportedPlatformCommands: IEnumerable
    Location: Point
    ToolTip: str
    Cursor: Cursor
    ControlObject: object
    TabIndex: int
    AllowDrop: bool
    IsMouseCaptured: bool
    ContextMenu: ContextMenu
    Callback: ICallback
    Control: ThemedCollectionEditor
    HasControl: bool
    Widget: CollectionEditor
    ID: str
    NativeHandle: IntPtr

class ThemedColorPickerHandler(ThemedControlHandler):
    """.NET: Eto.Forms.ThemedControls.ThemedColorPickerHandler"""
    def __init__(self, *args) -> None: ...
    Color: Color
    AllowAlpha: bool
    SupportsAllowAlpha: bool
    BackgroundColor: Color
    VisualControls: IEnumerable
    PropagateLoadEvents: bool
    Size: Size
    Width: int
    Height: int
    Enabled: bool
    HasFocus: bool
    Visible: bool
    SupportedPlatformCommands: IEnumerable
    Location: Point
    ToolTip: str
    Cursor: Cursor
    ControlObject: object
    TabIndex: int
    AllowDrop: bool
    IsMouseCaptured: bool
    ContextMenu: ContextMenu
    Callback: ICallback
    Control: Control
    HasControl: bool
    Widget: ColorPicker
    ID: str
    NativeHandle: IntPtr
    def AttachEvent(self, id: str) -> None: ...

class ThemedDocumentControlHandler(ThemedContainerHandler):
    """.NET: Eto.Forms.ThemedControls.ThemedDocumentControlHandler"""
    def __init__(self, *args) -> None: ...
    TabPadding: Padding
    AllowNavigationButtons: bool
    Font: Font
    BackgroundColor: Color
    DisabledForegroundColor: Color
    CloseBackgroundColor: Color
    CloseHighlightBackgroundColor: Color
    CloseCornerRadius: int
    CloseForegroundColor: Color
    CloseHighlightForegroundColor: Color
    TabBackgroundColor: Color
    TabHighlightBackgroundColor: Color
    TabHoverBackgroundColor: Color
    TabForegroundColor: Color
    TabHighlightForegroundColor: Color
    TabHoverForegroundColor: Color
    UnsavedBackgroundColor: Color
    UseFixedTabHeight: bool
    SelectedIndex: int
    AllowReordering: bool
    Enabled: bool
    ClientSize: Size
    RecurseToChildren: bool
    VisualControls: IEnumerable
    PropagateLoadEvents: bool
    Size: Size
    Width: int
    Height: int
    HasFocus: bool
    Visible: bool
    SupportedPlatformCommands: IEnumerable
    Location: Point
    ToolTip: str
    Cursor: Cursor
    ControlObject: object
    TabIndex: int
    AllowDrop: bool
    IsMouseCaptured: bool
    ContextMenu: ContextMenu
    Callback: ICallback
    Control: TableLayout
    HasControl: bool
    Widget: DocumentControl
    ID: str
    NativeHandle: IntPtr
    def AttachEvent(self, id: str) -> None: ...
    def GetPage(self, index: int) -> DocumentPage: ...
    def GetPageCount(self, ) -> int: ...
    def InsertPage(self, index: int, page: DocumentPage) -> None: ...
    def OnLoad(self, e: EventArgs) -> None: ...
    def RemovePage(self, index: int) -> None: ...

class ThemedDocumentPageHandler(ThemedContainerHandler):
    """.NET: Eto.Forms.ThemedControls.ThemedDocumentPageHandler"""
    def __init__(self, *args) -> None: ...
    Closable: bool
    Content: Control
    ContextMenu: ContextMenu
    Image: Image
    MinimumSize: Size
    Padding: Padding
    Text: str
    HasUnsavedChanges: bool
    PropagateLoadEvents: bool
    ClientSize: Size
    RecurseToChildren: bool
    BackgroundColor: Color
    VisualControls: IEnumerable
    Size: Size
    Width: int
    Height: int
    Enabled: bool
    HasFocus: bool
    Visible: bool
    SupportedPlatformCommands: IEnumerable
    Location: Point
    ToolTip: str
    Cursor: Cursor
    ControlObject: object
    TabIndex: int
    AllowDrop: bool
    IsMouseCaptured: bool
    Callback: ICallback
    Control: Panel
    HasControl: bool
    Widget: DocumentPage
    ID: str
    NativeHandle: IntPtr

class ThemedExpanderHandler(ThemedContainerHandler):
    """.NET: Eto.Forms.ThemedControls.ThemedExpanderHandler"""
    def __init__(self, *args) -> None: ...
    ExpandedButtonText: str
    CollapsedButtonText: str
    Expanded: bool
    Header: Control
    Content: Control
    Padding: Padding
    MinimumSize: Size
    ContextMenu: ContextMenu
    ClientSize: Size
    RecurseToChildren: bool
    BackgroundColor: Color
    VisualControls: IEnumerable
    PropagateLoadEvents: bool
    Size: Size
    Width: int
    Height: int
    Enabled: bool
    HasFocus: bool
    Visible: bool
    SupportedPlatformCommands: IEnumerable
    Location: Point
    ToolTip: str
    Cursor: Cursor
    ControlObject: object
    TabIndex: int
    AllowDrop: bool
    IsMouseCaptured: bool
    Callback: ICallback
    Control: StackLayout
    HasControl: bool
    Widget: Expander
    ID: str
    NativeHandle: IntPtr
    def AttachEvent(self, id: str) -> None: ...

class ThemedFilePickerHandler(ThemedControlHandler):
    """.NET: Eto.Forms.ThemedControls.ThemedFilePickerHandler"""
    def __init__(self, *args) -> None: ...
    FileAction: FileAction
    FilePath: str
    CurrentFilterIndex: int
    Title: str
    BackgroundColor: Color
    VisualControls: IEnumerable
    PropagateLoadEvents: bool
    Size: Size
    Width: int
    Height: int
    Enabled: bool
    HasFocus: bool
    Visible: bool
    SupportedPlatformCommands: IEnumerable
    Location: Point
    ToolTip: str
    Cursor: Cursor
    ControlObject: object
    TabIndex: int
    AllowDrop: bool
    IsMouseCaptured: bool
    ContextMenu: ContextMenu
    Callback: ICallback
    Control: StackLayout
    HasControl: bool
    Widget: FilePicker
    ID: str
    NativeHandle: IntPtr
    def AttachEvent(self, id: str) -> None: ...
    def ClearFilters(self, ) -> None: ...
    def InsertFilter(self, index: int, filter: FileFilter) -> None: ...
    def RemoveFilter(self, index: int) -> None: ...

class ThemedFontPickerHandler(ThemedControlHandler):
    """.NET: Eto.Forms.ThemedControls.ThemedFontPickerHandler"""
    def __init__(self, *args) -> None: ...
    Value: Font
    BackgroundColor: Color
    VisualControls: IEnumerable
    PropagateLoadEvents: bool
    Size: Size
    Width: int
    Height: int
    Enabled: bool
    HasFocus: bool
    Visible: bool
    SupportedPlatformCommands: IEnumerable
    Location: Point
    ToolTip: str
    Cursor: Cursor
    ControlObject: object
    TabIndex: int
    AllowDrop: bool
    IsMouseCaptured: bool
    ContextMenu: ContextMenu
    Callback: ICallback
    Control: Button
    HasControl: bool
    Widget: FontPicker
    ID: str
    NativeHandle: IntPtr
    def AttachEvent(self, id: str) -> None: ...

class ThemedMenuSegmentedItemHandler(ThemedSegmentedItemHandler):
    """.NET: Eto.Forms.ThemedControls.ThemedMenuSegmentedItemHandler"""
    def __init__(self, *args) -> None: ...
    MenuDelay: TimeSpan
    MenuIndicator: str
    Menu: ContextMenu
    CanSelect: bool
    Text: str
    Enabled: bool
    Visible: bool
    ToolTip: str
    Width: int
    Image: Image
    Selected: bool
    Callback: ICallback
    Control: ToggleButton
    HasControl: bool
    Widget: MenuSegmentedItem
    ID: str
    NativeHandle: IntPtr

class ThemedMessageBox(Dialog):
    """.NET: Eto.Forms.ThemedControls.ThemedMessageBox"""
    def __init__(self, *args) -> None: ...
    Result: object
    Text: str
    TextAlignment: TextAlignment
    Image: Image
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
    def AddButton(self, text: str, result: object, isDefault: bool, isAbort: bool) -> None: ...

class ThemedMessageBoxHandler(WidgetHandler):
    """.NET: Eto.Forms.ThemedControls.ThemedMessageBoxHandler"""
    def __init__(self, *args) -> None: ...
    Text: str
    Caption: str
    Type: MessageBoxType
    Buttons: MessageBoxButtons
    DefaultButton: MessageBoxDefaultButton
    Widget: Widget
    ID: str
    NativeHandle: IntPtr
    def ShowDialog(self, parent: Control) -> DialogResult: ...

class ThemedPropertyGrid(Panel):
    """.NET: Eto.Forms.ThemedControls.ThemedPropertyGrid"""
    def __init__(self, *args) -> None: ...
    PropertyCellTypes: IList
    SelectedObjects: IEnumerable
    UseValueTypeDefaults: bool
    SelectedObject: object
    ShowCategories: bool
    ShowDescription: bool
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
    def CreateCellValueBinding(self, ) -> IndirectBinding: ...
    def Refresh(self, ) -> None: ...

class ThemedPropertyGridHandler(ThemedControlHandler):
    """.NET: Eto.Forms.ThemedControls.ThemedPropertyGridHandler"""
    def __init__(self, *args) -> None: ...
    SelectedObject: object
    SelectedObjects: IEnumerable
    ShowCategories: bool
    ShowDescription: bool
    BackgroundColor: Color
    VisualControls: IEnumerable
    PropagateLoadEvents: bool
    Size: Size
    Width: int
    Height: int
    Enabled: bool
    HasFocus: bool
    Visible: bool
    SupportedPlatformCommands: IEnumerable
    Location: Point
    ToolTip: str
    Cursor: Cursor
    ControlObject: object
    TabIndex: int
    AllowDrop: bool
    IsMouseCaptured: bool
    ContextMenu: ContextMenu
    Callback: ICallback
    Control: ThemedPropertyGrid
    HasControl: bool
    Widget: PropertyGrid
    ID: str
    NativeHandle: IntPtr
    def AttachEvent(self, id: str) -> None: ...
    def Refresh(self, ) -> None: ...

class ThemedSegmentedButtonHandler(ThemedControlHandler):
    """.NET: Eto.Forms.ThemedControls.ThemedSegmentedButtonHandler"""
    def __init__(self, *args) -> None: ...
    SelectionMode: SegmentedSelectionMode
    Spacing: int
    SelectedIndex: int
    SelectedIndexes: IEnumerable
    BackgroundColor: Color
    VisualControls: IEnumerable
    PropagateLoadEvents: bool
    Size: Size
    Width: int
    Height: int
    Enabled: bool
    HasFocus: bool
    Visible: bool
    SupportedPlatformCommands: IEnumerable
    Location: Point
    ToolTip: str
    Cursor: Cursor
    ControlObject: object
    TabIndex: int
    AllowDrop: bool
    IsMouseCaptured: bool
    ContextMenu: ContextMenu
    Callback: ICallback
    Control: Panel
    HasControl: bool
    Widget: SegmentedButton
    ID: str
    NativeHandle: IntPtr
    def AttachEvent(self, id: str) -> None: ...
    def ClearItems(self, ) -> None: ...
    def ClearSelection(self, ) -> None: ...
    def GetPreferredSize(self, availableSize: SizeF) -> SizeF: ...
    def InsertItem(self, index: int, item: SegmentedItem) -> None: ...
    def OnLoad(self, e: EventArgs) -> None: ...
    def OnPreLoad(self, e: EventArgs) -> None: ...
    def RemoveItem(self, index: int, item: SegmentedItem) -> None: ...
    def SelectAll(self, ) -> None: ...
    def SetItem(self, index: int, item: SegmentedItem) -> None: ...

class ThemedSegmentedItemHandler(WidgetHandler):
    """.NET: Eto.Forms.ThemedControls.ThemedSegmentedItemHandler`2"""
    def __init__(self, *args) -> None: ...
    Enabled: bool
    Visible: bool
    ToolTip: str
    Width: int
    Text: str
    Image: Image
    Selected: bool
    Callback: TCallback
    Control: ToggleButton
    HasControl: bool
    Widget: TWidget
    ID: str
    NativeHandle: IntPtr
    def AttachEvent(self, id: str) -> None: ...

class ThemedSpinnerDirection:
    """.NET: Eto.Forms.ThemedControls.ThemedSpinnerDirection"""
    def __init__(self, *args) -> None: ...
    ...

class ThemedSpinnerHandler(ThemedControlHandler):
    """.NET: Eto.Forms.ThemedControls.ThemedSpinnerHandler"""
    def __init__(self, *args) -> None: ...
    Increment: float
    Direction: ThemedSpinnerDirection
    DisabledAlpha: float
    ElementColor: Color
    LineThickness: float
    LineCap: PenLineCap
    ElementSize: float
    Mode: ThemedSpinnerMode
    NumberOfElements: int
    NumberOfVisibleElements: int
    Speed: float
    Enabled: bool
    BackgroundColor: Color
    VisualControls: IEnumerable
    PropagateLoadEvents: bool
    Size: Size
    Width: int
    Height: int
    HasFocus: bool
    Visible: bool
    SupportedPlatformCommands: IEnumerable
    Location: Point
    ToolTip: str
    Cursor: Cursor
    ControlObject: object
    TabIndex: int
    AllowDrop: bool
    IsMouseCaptured: bool
    ContextMenu: ContextMenu
    Callback: ICallback
    Control: Drawable
    HasControl: bool
    Widget: Spinner
    ID: str
    NativeHandle: IntPtr
    def OnLoadComplete(self, e: EventArgs) -> None: ...
    def OnUnLoad(self, e: EventArgs) -> None: ...

class ThemedSpinnerMode:
    """.NET: Eto.Forms.ThemedControls.ThemedSpinnerMode"""
    def __init__(self, *args) -> None: ...
    ...

class ThemedSplitterHandler(ThemedContainerHandler):
    """.NET: Eto.Forms.ThemedControls.ThemedSplitterHandler"""
    def __init__(self, *args) -> None: ...
    Orientation: Orientation
    FixedPanel: SplitterFixedPanel
    Position: int
    RelativePosition: float
    SplitterWidth: int
    Panel1: Control
    Panel2: Control
    Splitter: Panel
    Panel1MinimumSize: int
    Panel2MinimumSize: int
    ClientSize: Size
    RecurseToChildren: bool
    BackgroundColor: Color
    VisualControls: IEnumerable
    PropagateLoadEvents: bool
    Size: Size
    Width: int
    Height: int
    Enabled: bool
    HasFocus: bool
    Visible: bool
    SupportedPlatformCommands: IEnumerable
    Location: Point
    ToolTip: str
    Cursor: Cursor
    ControlObject: object
    TabIndex: int
    AllowDrop: bool
    IsMouseCaptured: bool
    ContextMenu: ContextMenu
    Callback: ICallback
    Control: TableLayout
    HasControl: bool
    Widget: Splitter
    ID: str
    NativeHandle: IntPtr

class ThemedStepperHandler(ThemedControlHandler):
    """.NET: Eto.Forms.ThemedControls.ThemedStepperHandler"""
    def __init__(self, *args) -> None: ...
    UpText: str
    DownText: str
    Font: Font
    Orientation: Orientation
    ValidDirection: StepperValidDirections
    Enabled: bool
    BackgroundColor: Color
    VisualControls: IEnumerable
    PropagateLoadEvents: bool
    Size: Size
    Width: int
    Height: int
    HasFocus: bool
    Visible: bool
    SupportedPlatformCommands: IEnumerable
    Location: Point
    ToolTip: str
    Cursor: Cursor
    ControlObject: object
    TabIndex: int
    AllowDrop: bool
    IsMouseCaptured: bool
    ContextMenu: ContextMenu
    Callback: ICallback
    Control: Panel
    HasControl: bool
    Widget: Stepper
    ID: str
    NativeHandle: IntPtr
    def AttachEvent(self, id: str) -> None: ...

class ThemedTextStepperHandler(ThemedControlHandler):
    """.NET: Eto.Forms.ThemedControls.ThemedTextStepperHandler"""
    def __init__(self, *args) -> None: ...
    TextBox: TextBox
    Stepper: Stepper
    CaretIndex: int
    Font: Font
    MaxLength: int
    PlaceholderText: str
    ReadOnly: bool
    Selection: Range
    ShowBorder: bool
    Text: str
    TextColor: Color
    ValidDirection: StepperValidDirections
    TextAlignment: TextAlignment
    ShowStepper: bool
    BackgroundColor: Color
    AutoSelectMode: AutoSelectMode
    HasFocus: bool
    AlwaysShowSelection: bool
    VisualControls: IEnumerable
    PropagateLoadEvents: bool
    Size: Size
    Width: int
    Height: int
    Enabled: bool
    Visible: bool
    SupportedPlatformCommands: IEnumerable
    Location: Point
    ToolTip: str
    Cursor: Cursor
    ControlObject: object
    TabIndex: int
    AllowDrop: bool
    IsMouseCaptured: bool
    ContextMenu: ContextMenu
    Callback: ICallback
    Control: TableLayout
    HasControl: bool
    Widget: TextStepper
    ID: str
    NativeHandle: IntPtr
    def AttachEvent(self, id: str) -> None: ...
    def Focus(self, ) -> None: ...
    def SelectAll(self, ) -> None: ...
