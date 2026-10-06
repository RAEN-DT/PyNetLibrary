# Auto-generated — Rhino 8 — Rhino.UI.CodeEditor

class EditorConfig:
    """.NET: Rhino.UI.CodeEditor.EditorConfig"""
    def __init__(self, *args) -> None: ...
    ...

class EditorConfigPanel(Panel):
    """.NET: Rhino.UI.CodeEditor.EditorConfigPanel"""
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

class EditorConfigViewModel(ViewModel):
    """.NET: Rhino.UI.CodeEditor.EditorConfigViewModel"""
    def __init__(self, *args) -> None: ...
    EditorConfig: EditorConfig
    DefaultsAreOverridden: bool
    ReplaceTabsWithSpaces: bool
    IndentWidthInChars: int
    ShowWhitespace: bool
    ShowIndentationGuides: bool
    Font: Font
    ModelUnitSystem: UnitSystem
    PageUnitSystem: UnitSystem
    ModelDistanceDisplayMode: DistanceDisplayMode
    PageDistanceDisplayMode: DistanceDisplayMode
    ModelDistanceDisplayPrecision: int
    PageDistanceDisplayPrecision: int
    def RestoreDefaults(self, ) -> None: ...
    def Save(self, ) -> None: ...

class FilesSearchPathPanel(Panel):
    """.NET: Rhino.UI.CodeEditor.FilesSearchPathPanel"""
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

class FilesSearchPathViewModel(ViewModel):
    """.NET: Rhino.UI.CodeEditor.FilesSearchPathViewModel"""
    def __init__(self, *args) -> None: ...
    SearchPaths: IEnumerable
    SelectedSearchPath: str
    HasSelectedUserSearchPath: bool
    ModelUnitSystem: UnitSystem
    PageUnitSystem: UnitSystem
    ModelDistanceDisplayMode: DistanceDisplayMode
    PageDistanceDisplayMode: DistanceDisplayMode
    ModelDistanceDisplayPrecision: int
    PageDistanceDisplayPrecision: int
    def AddSearchPath(self, searchPath: str) -> bool: ...
    def DeleteSelectedSearchPath(self, ) -> bool: ...

class PersistentEditorSettings:
    """.NET: Rhino.UI.CodeEditor.PersistentEditorSettings"""
    def __init__(self, *args) -> None: ...
    def DeleteEditorConfig(self, ) -> None: ...
    def GetCustomSetting(self, key: str, defaultValue: bool) -> bool: ...
    def ReadEditorConfig(self, defaultConfig: EditorConfig) -> EditorConfig: ...
    def SaveEditorConfig(self, config: EditorConfig) -> None: ...
    def SetCustomSetting(self, key: str, value: bool) -> None: ...

class WhichEditor:
    """.NET: Rhino.UI.CodeEditor.WhichEditor"""
    def __init__(self, *args) -> None: ...
    ...
