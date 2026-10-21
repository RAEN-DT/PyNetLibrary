# Auto-generated — Rhino 8 — Rhino.UI.ObjectProperties

class ColorPatch(ImageButton):
    """.NET: Rhino.UI.ObjectProperties.ColorPatch"""
    def __init__(self, *args) -> None: ...
    Varies: bool
    IsCustom: bool
    IsPerFace: bool
    SelectedIconIndex: int
    IsPrintColor: bool
    Color: Color
    HoverBrush: Brush
    HoverBorderPen: Pen
    HighlightBrush: Brush
    HighlightBorderPen: Pen
    Image: Image
    DisabledImage: Image
    Size: Size
    MaskImageWithBackgroundColorWhenDisabled: bool
    SupportsCreateGraphics: bool
    CanFocus: bool
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

class LayerDropDown(DropDown):
    """.NET: Rhino.UI.ObjectProperties.LayerDropDown"""
    def __init__(self, *args) -> None: ...
    DocumentSerialNumber: int
    LayerIndex: int
    LayerVaries: bool
    Refresh: bool
    ItemImageBinding: IIndirectBinding
    ShowBorder: bool
    ItemTextBinding: IIndirectBinding
    ItemKeyBinding: IIndirectBinding
    TextBinding: IIndirectBinding
    KeyBinding: IIndirectBinding
    Items: ListItemCollection
    DataStore: IEnumerable
    SelectedIndex: int
    SelectedValue: object
    SelectedKey: str
    TextColor: Color
    SelectedIndexBinding: BindableBinding
    SelectedKeyBinding: BindableBinding
    SelectedValueBinding: BindableBinding
    Font: Font
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
    ContextMenu: ContextMenu
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
    def CloseForm(self, setFocus: bool) -> None: ...

class PlotWeightComboBox(ComboBox):
    """.NET: Rhino.UI.ObjectProperties.PlotWeightComboBox"""
    def __init__(self, *args) -> None: ...
    PlotWeightSource: ObjectPlotWeightSource
    PlotWeight: float
    PlotWidthText: str
    PlotWeightVaries: bool
    Text: str
    ReadOnly: bool
    AutoComplete: bool
    ItemImageBinding: IIndirectBinding
    ShowBorder: bool
    ItemTextBinding: IIndirectBinding
    ItemKeyBinding: IIndirectBinding
    TextBinding: IIndirectBinding
    KeyBinding: IIndirectBinding
    Items: ListItemCollection
    DataStore: IEnumerable
    SelectedIndex: int
    SelectedValue: object
    SelectedKey: str
    TextColor: Color
    SelectedIndexBinding: BindableBinding
    SelectedKeyBinding: BindableBinding
    SelectedValueBinding: BindableBinding
    Font: Font
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
    ContextMenu: ContextMenu
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
    def RefreshPlotWeightList(self, ) -> None: ...

class PropertiesEditorPanel(Panel):
    """.NET: Rhino.UI.ObjectProperties.PropertiesEditorPanel"""
    def __init__(self, *args) -> None: ...
    ChildPadding: int
    RuntimeId: Guid
    HelpUrl: str
    IsObjectProperties: bool
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
    def OnClick(self, id: Guid) -> None: ...
    def PanelClosing(self, documentSerialNumber: int, onCloseDocument: bool) -> None: ...
    def PanelHidden(self, documentSerialNumber: int, reason: ShowPanelReason) -> None: ...
    def PanelShown(self, documentSerialNumber: int, reason: ShowPanelReason) -> None: ...
    @staticmethod
    def Register() -> None: ...

class TextureMappingPropertiesPage(ObjectPropertiesPage):
    """.NET: Rhino.UI.ObjectProperties.TextureMappingPropertiesPage"""
    def __init__(self, *args) -> None: ...
    EnglishPageTitle: str
    LocalPageTitle: str
    Index: int
    PageIconEmbeddedResourceString: str
    PageType: PropertyPageType
    SupportedTypes: ObjectType
    PageControl: object
    Icon: Icon
    AllObjectsMustBeSupported: bool
    SupportsSubObjects: bool
    SelectedObjects: list
    def Dispose(self, ) -> None: ...
    def OnActivate(self, active: bool) -> bool: ...
    def PageIcon(self, sizeInPixels: Size) -> Icon: ...
    def RunScript(self, e: ObjectPropertiesPageEventArgs) -> Result: ...
    def ShouldDisplay(self, e: ObjectPropertiesPageEventArgs) -> bool: ...
    def UpdateDisplay(self, ) -> None: ...
    def UpdatePage(self, e: ObjectPropertiesPageEventArgs) -> None: ...

class UserStringItem:
    """.NET: Rhino.UI.ObjectProperties.UserStringItem"""
    def __init__(self, *args) -> None: ...
    Key: str
    Value: str
    Formula: str
    IsBlockAttribute: bool
    Guid: Guid
    DocumentText: bool
    FxImage: Image
    IsFunction: bool
    KeyCount: int
    AppliesToAll: bool
    AppliesToAllIcon: Image
    ReplaceExistingKey: str

class UserStringsDocumentOptionsPage(OptionsDialogPage):
    """.NET: Rhino.UI.ObjectProperties.UserStringsDocumentOptionsPage"""
    def __init__(self, *args) -> None: ...
    LocalPageTitle: str
    PageControl: object
    PageImage: Image
    OptionsPageType: PageType
    Children: List
    HasChildren: bool
    Modified: bool
    Handle: IntPtr
    EnglishPageTitle: str
    ShowDefaultsButton: bool
    ShowApplyButton: bool
    NavigationTextIsBold: bool
    NavigationTextColor: Color
    def OnApply(self, ) -> bool: ...
    def OnHelp(self, ) -> None: ...

class UserStringsPanelControl(Panel):
    """.NET: Rhino.UI.ObjectProperties.UserStringsPanelControl"""
    def __init__(self, *args) -> None: ...
    SelectedObjects: list
    Document: RhinoDoc
    IsLayoutText: bool
    LayoutId: Guid
    DocumentPanelActive: bool
    PanelId: Guid
    IsFxHosted: bool
    EnableEventWatchers: bool
    SelectedRows: IEnumerable
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
    def ActivateEventWatchers(self, ) -> None: ...
    def DeactivateEventWatchers(self, ) -> None: ...
    def GetSelectedObjectUserText(self, selectedObjects: list, sortOnCompletion: bool) -> None: ...
    def InitializeControls(self, rhObjs: list) -> None: ...
    def LoadLayoutStrings(self, ) -> None: ...
    def OnApply(self, ) -> bool: ...
    @staticmethod
    def Panel(documentSerialNumber: int) -> UserStringsPanelControl: ...
    def PanelClosing(self, documentSerialNumber: int, onCloseDocument: bool) -> None: ...
    def PanelHidden(self, documentSerialNumber: int, reason: ShowPanelReason) -> None: ...
    def PanelShown(self, documentSerialNumber: int, reason: ShowPanelReason) -> None: ...
