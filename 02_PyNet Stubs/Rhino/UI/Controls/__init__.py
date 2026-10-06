# Auto-generated — Rhino 8 — Rhino.UI.Controls

class AddRemoveButton(SegmentedButton):
    """.NET: Rhino.UI.Controls.AddRemoveButton"""
    def __init__(self, *args) -> None: ...
    AddEnabled: bool
    AddCommand: Command
    RemoveEnabled: bool
    RemoveCommand: Command
    AddToolTip: str
    RemoveToolTip: str
    Items: SegmentedItemCollection
    SelectionMode: SegmentedSelectionMode
    SelectedItems: IEnumerable
    SelectedItem: SegmentedItem
    SelectedIndexes: IEnumerable
    SelectedIndex: int
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
    def InsertButton(self, resourceId: str, toolTip: str, click: Action) -> ButtonSegmentedItem: ...

class ButtonDrawable(Drawable):
    """.NET: Rhino.UI.Controls.ButtonDrawable"""
    def __init__(self, *args) -> None: ...
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

class CollapsibleSectionContainerHandler(ThemedContainerHandler):
    """.NET: Rhino.UI.Controls.CollapsibleSectionContainerHandler"""
    def __init__(self, *args) -> None: ...
    Collapsible: bool
    Caption: str
    Expanded: bool
    Header: Control
    Content: Control
    Divider: Divider
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
    Widget: SectionContainer
    ID: str
    NativeHandle: IntPtr
    def AddButtons(self, hbh: IHeaderButtonHandler) -> None: ...
    def AddHeaderButtons(self, buttonDrawables: List) -> None: ...
    def AttachEvent(self, id: str) -> None: ...

class CollapsibleSectionHolderImpl:
    """.NET: Rhino.UI.Controls.CollapsibleSectionHolderImpl"""
    def __init__(self, *args) -> None: ...
    CppPointer: IntPtr
    def Dispose(self, ) -> None: ...
    @staticmethod
    def Find(cpp: IntPtr) -> ICollapsibleSectionHolder: ...
    def IsSameObject(self, cpp: IntPtr) -> bool: ...
    @staticmethod
    def NewNativeWrapper(cpp: IntPtr) -> ICollapsibleSectionHolder: ...

class CollapsibleSectionImpl:
    """.NET: Rhino.UI.Controls.CollapsibleSectionImpl"""
    def __init__(self, *args) -> None: ...
    CppPointer: IntPtr
    ViewModel: IRdkViewModel
    @staticmethod
    def CreateHostedSection(section: ICollapsibleSection) -> None: ...
    def Dispose(self, ) -> None: ...
    @staticmethod
    def Find(cpp: IntPtr) -> ICollapsibleSection: ...
    @staticmethod
    def GetSibling(section: ICollapsibleSection, siblingSectionId: Guid) -> ICollapsibleSection: ...
    @staticmethod
    def GetSiblings(section: ICollapsibleSection) -> list: ...
    def IsSameObject(self, cpp: IntPtr) -> bool: ...
    @staticmethod
    def NewNativeWrapper(cpp: IntPtr) -> ICollapsibleSection: ...
    def ReplaceClient(self, client: ICollapsibleSection) -> None: ...
    def __InternalSetParent(self, parent: IntPtr) -> None: ...

class CollapsibleSectionViewModel:
    """.NET: Rhino.UI.Controls.CollapsibleSectionViewModel"""
    def __init__(self, *args) -> None: ...
    CppPointer: IntPtr
    def Commit(self, uuidDataType: Guid) -> None: ...
    def Discard(self, uuidDataType: Guid) -> None: ...
    def GetData(self, uuidDataType: Guid, bForWrite: bool, bAutoChangeBracket: bool) -> object: ...
    def UndoHelper(self, description: str) -> UndoRecord: ...

class ContentUI:
    """.NET: Rhino.UI.Controls.ContentUI"""
    def __init__(self, *args) -> None: ...
    CppPointer: IntPtr
    def ContentUIHolder(self, ) -> ICollapsibleSectionHolder: ...
    def Dispose(self, ) -> None: ...
    def EditorUuid(self, ) -> Guid: ...
    def IsCreated(self, ) -> bool: ...
    def IsShown(self, ) -> bool: ...
    def Uuid(self, ) -> Guid: ...

class ControlGridLayout(Panel):
    """.NET: Rhino.UI.Controls.ControlGridLayout"""
    def __init__(self, *args) -> None: ...
    GridWrapMode: GridWrapMode
    ArrangeControls: bool
    ItemSize: Size
    ItemPadding: Padding
    Items: Collection
    CenterAlign: bool
    Rows: int
    Columns: int
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

class Delegates:
    """.NET: Rhino.UI.Controls.Delegates"""
    def __init__(self, *args) -> None: ...
    ...

class Divider(Drawable):
    """.NET: Rhino.UI.Controls.Divider"""
    def __init__(self, *args) -> None: ...
    UnsetColor: Color
    Color: Color
    ForceHorizontalLine: bool
    Orientation: Orientation
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

class EtoCollapsibleSection(Panel):
    """.NET: Rhino.UI.Controls.EtoCollapsibleSection"""
    def __init__(self, *args) -> None: ...
    Caption: LocalizeStringPair
    SectionHeight: int
    Collapsible: bool
    Hidden: bool
    InitiallyExpanded: bool
    SettingsTag: str
    ViewModel: IRdkViewModel
    CppPointer: IntPtr
    CommandOptionName: LocalizeStringPair
    PlugInId: Guid
    ViewModelId: Guid
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
    def ApplyStyles(self, ) -> None: ...
    def CurrentRendererDependent(self, bValue: bool) -> None: ...
    def ReplaceCallback(self, callback: ICollapsibleSection) -> None: ...
    def RunScript(self, vm: IRdkViewModel) -> int: ...

class EtoCollapsibleSection2(EtoCollapsibleSection):
    """.NET: Rhino.UI.Controls.EtoCollapsibleSection2"""
    def __init__(self, *args) -> None: ...
    Caption: LocalizeStringPair
    SectionHeight: int
    Collapsible: bool
    Hidden: bool
    InitiallyExpanded: bool
    SettingsTag: str
    ViewModel: IRdkViewModel
    CppPointer: IntPtr
    CommandOptionName: LocalizeStringPair
    PlugInId: Guid
    ViewModelId: Guid
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
    def EnableHeaderButton(self, index: int, bEnable: bool) -> bool: ...
    def HolderVisible(self, visible: bool) -> None: ...
    def NewHeaderButtonHandler(self, ) -> IHeaderButtonHandler: ...
    def OnAttachedToHolder(self, holder: ICollapsibleSectionHolder2) -> None: ...
    def OnAttachingToHolder(self, holder: ICollapsibleSectionHolder2) -> None: ...
    def OnDetachedFromHolder(self, holder: ICollapsibleSectionHolder2) -> None: ...
    def OnDetachingFromHolder(self, holder: ICollapsibleSectionHolder2) -> None: ...
    def ShowHeaderButton(self, index: int, bShow: bool) -> bool: ...

class EtoCollapsibleSection3(EtoCollapsibleSection2):
    """.NET: Rhino.UI.Controls.EtoCollapsibleSection3"""
    def __init__(self, *args) -> None: ...
    Caption: LocalizeStringPair
    SectionHeight: int
    Collapsible: bool
    Hidden: bool
    InitiallyExpanded: bool
    SettingsTag: str
    ViewModel: IRdkViewModel
    CppPointer: IntPtr
    CommandOptionName: LocalizeStringPair
    PlugInId: Guid
    ViewModelId: Guid
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
    def UpdateView(self, flags: int) -> None: ...

class EtoCollapsibleSectionHolder(Panel):
    """.NET: Rhino.UI.Controls.EtoCollapsibleSectionHolder"""
    def __init__(self, *args) -> None: ...
    UseCheckBoxes: bool
    UseScrollbars: bool
    Uuid: Guid
    Sections: IEnumerable
    HolderParent: IntPtr
    Shown: bool
    Enabled: bool
    Created: bool
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
    def Add(self, section: ICollapsibleSection) -> None: ...
    def FindSectionIndex(self, section: ICollapsibleSection) -> int: ...
    def Move(self, rect: Rectangle, bRepaint: bool, bRepaintNC: bool) -> None: ...
    def RegisterSectionCheckBoxes(self, ) -> None: ...
    def Remove(self, section: ICollapsibleSection) -> None: ...
    def SectionAt(self, index: int) -> ICollapsibleSection: ...
    def SectionCheckBox(self, caption: str) -> CheckBox: ...
    def UnRegisterSectionCheckBoxes(self, ) -> None: ...

class EtoCollapsibleSectionHolder2(EtoCollapsibleSectionHolder):
    """.NET: Rhino.UI.Controls.EtoCollapsibleSectionHolder2"""
    def __init__(self, *args) -> None: ...
    UseCheckBoxes: bool
    UseScrollbars: bool
    Uuid: Guid
    Sections: IEnumerable
    HolderParent: IntPtr
    Shown: bool
    Enabled: bool
    Created: bool
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
    def EnableHeaderButton(self, s: ICollapsibleSection, index: int, bEnable: bool) -> bool: ...
    def SetFullHeightSection(self, sec: ICollapsibleSection) -> None: ...
    def ShowHeaderButton(self, s: ICollapsibleSection, index: int, bShow: bool) -> bool: ...

class EtoContentUISection(EtoCollapsibleSection):
    """.NET: Rhino.UI.Controls.EtoContentUISection"""
    def __init__(self, *args) -> None: ...
    Caption: LocalizeStringPair
    SectionHeight: int
    Collapsible: bool
    Hidden: bool
    InitiallyExpanded: bool
    SettingsTag: str
    ViewModel: IRdkViewModel
    CppPointer: IntPtr
    CommandOptionName: LocalizeStringPair
    PlugInId: Guid
    ViewModelId: Guid
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
    def GetSelection(self, ) -> RenderContentCollection: ...
    def SetSelection(self, collection: RenderContentCollection) -> bool: ...

class EtoContentUISection2(EtoCollapsibleSection2):
    """.NET: Rhino.UI.Controls.EtoContentUISection2"""
    def __init__(self, *args) -> None: ...
    Hidden: bool
    Caption: LocalizeStringPair
    SectionHeight: int
    Collapsible: bool
    InitiallyExpanded: bool
    SettingsTag: str
    ViewModel: IRdkViewModel
    CppPointer: IntPtr
    CommandOptionName: LocalizeStringPair
    PlugInId: Guid
    ViewModelId: Guid
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
    def GetSelection(self, ) -> RenderContentCollection: ...
    def SetSelection(self, collection: RenderContentCollection) -> bool: ...

class EtoContentUISection3(EtoCollapsibleSection3):
    """.NET: Rhino.UI.Controls.EtoContentUISection3"""
    def __init__(self, *args) -> None: ...
    Hidden: bool
    Caption: LocalizeStringPair
    SectionHeight: int
    Collapsible: bool
    InitiallyExpanded: bool
    SettingsTag: str
    ViewModel: IRdkViewModel
    CppPointer: IntPtr
    CommandOptionName: LocalizeStringPair
    PlugInId: Guid
    ViewModelId: Guid
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
    def GetSelection(self, ) -> RenderContentCollection: ...
    def SetSelection(self, collection: RenderContentCollection) -> bool: ...

class EtoExpanderHandler(ThemedContainerHandler):
    """.NET: Rhino.UI.Controls.EtoExpanderHandler"""
    def __init__(self, *args) -> None: ...
    Expanded: bool
    Header: Control
    Content: Control
    Divider: Divider
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

class EtoPostEffectCollapsibleSection(EtoCollapsibleSection):
    """.NET: Rhino.UI.Controls.EtoPostEffectCollapsibleSection"""
    def __init__(self, *args) -> None: ...
    PostEffects: list
    PostEffectId: Guid
    Caption: LocalizeStringPair
    SectionHeight: int
    Collapsible: bool
    Hidden: bool
    InitiallyExpanded: bool
    SettingsTag: str
    ViewModel: IRdkViewModel
    CppPointer: IntPtr
    CommandOptionName: LocalizeStringPair
    PlugInId: Guid
    ViewModelId: Guid
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
    def GetParameter(self, paramName: str, defaultValue: object) -> object: ...
    def GetPostEffects(self, type: PostEffectType) -> list: ...
    def SetParameter(self, paramName: str, value: object) -> bool: ...

class ExpandableContentUI(ContentUI):
    """.NET: Rhino.UI.Controls.ExpandableContentUI"""
    def __init__(self, *args) -> None: ...
    CppPointer: IntPtr
    def AddSection(self, pSection: ICollapsibleSection, vm: IRdkViewModel) -> None: ...

class FactoryBase:
    """.NET: Rhino.UI.Controls.FactoryBase"""
    def __init__(self, *args) -> None: ...
    def Get(self, id: Guid) -> IntPtr: ...
    @staticmethod
    def Register(plugin: PlugIn) -> list: ...

class GridWrapMode:
    """.NET: Rhino.UI.Controls.GridWrapMode"""
    def __init__(self, *args) -> None: ...
    ...

class ICollapsibleSection:
    """.NET: Rhino.UI.Controls.ICollapsibleSection"""
    def __init__(self, *args) -> None: ...
    Height: int
    Hidden: bool
    InitiallyExpanded: bool
    Id: Guid
    SettingsTag: str
    Collapsible: bool
    BackgroundColor: Color
    ViewModel: IRdkViewModel
    PlugInId: Guid
    CommandOptionName: LocalizeStringPair
    ViewModelId: Guid
    def RunScript(self, vm: IRdkViewModel) -> int: ...

class ICollapsibleSection2:
    """.NET: Rhino.UI.Controls.ICollapsibleSection2"""
    def __init__(self, *args) -> None: ...
    def EnableHeaderButton(self, index: int, bEnable: bool) -> bool: ...
    def NewHeaderButtonHandler(self, ) -> IHeaderButtonHandler: ...
    def OnAttachedToHolder(self, holder: ICollapsibleSectionHolder2) -> None: ...
    def OnAttachingToHolder(self, holder: ICollapsibleSectionHolder2) -> None: ...
    def OnDetachedFromHolder(self, holder: ICollapsibleSectionHolder2) -> None: ...
    def OnDetachingFromHolder(self, holder: ICollapsibleSectionHolder2) -> None: ...
    def ShowHeaderButton(self, index: int, bShow: bool) -> bool: ...

class ICollapsibleSection3:
    """.NET: Rhino.UI.Controls.ICollapsibleSection3"""
    def __init__(self, *args) -> None: ...
    def UpdateView(self, flags: int) -> None: ...

class ICollapsibleSectionHolder:
    """.NET: Rhino.UI.Controls.ICollapsibleSectionHolder"""
    def __init__(self, *args) -> None: ...
    Sections: IEnumerable
    SectionCount: int
    BackgroundColor: Color
    EmptyText: str
    TopMargin: int
    BottomMargin: int
    LeftMargin: int
    RightMargin: int
    ScrollPosition: int
    SettingsPathSubKey: str
    def Add(self, section: ICollapsibleSection) -> None: ...
    def ExpandSection(self, section: ICollapsibleSection, expand: bool, ensureVisible: bool) -> None: ...
    def IsSectionExpanded(self, section: ICollapsibleSection) -> bool: ...
    def Remove(self, section: ICollapsibleSection) -> None: ...
    def SectionAt(self, index: int) -> ICollapsibleSection: ...
    def UpdateAllViews(self, flags: int) -> None: ...

class ICollapsibleSectionHolder2:
    """.NET: Rhino.UI.Controls.ICollapsibleSectionHolder2"""
    def __init__(self, *args) -> None: ...
    def EnableHeaderButton(self, s: ICollapsibleSection, index: int, bEnable: bool) -> bool: ...
    def SetFullHeightSection(self, sec: ICollapsibleSection) -> None: ...
    def ShowHeaderButton(self, s: ICollapsibleSection, index: int, bShow: bool) -> bool: ...

class IHasCppImplementation:
    """.NET: Rhino.UI.Controls.IHasCppImplementation"""
    def __init__(self, *args) -> None: ...
    CppPointer: IntPtr

class IHeaderButtonHandler:
    """.NET: Rhino.UI.Controls.IHeaderButtonHandler"""
    def __init__(self, *args) -> None: ...
    def ButtonDetails(self, index: int, iconOut: Bitmap, sToolTipOut: str) -> bool: ...
    def ButtonRect(self, index: int, rectHeader: Rectangle) -> Rectangle: ...
    def DeleteThis(self, ) -> None: ...
    def OnButtonClicked(self, index: int) -> bool: ...

class IRdkViewModel:
    """.NET: Rhino.UI.Controls.IRdkViewModel"""
    def __init__(self, *args) -> None: ...
    def Commit(self, uuidDataType: Guid) -> None: ...
    def Discard(self, uuidDataType: Guid) -> None: ...
    def GetData(self, uuidDataType: Guid, bForWrite: bool, bAutoChangeBracket: bool) -> object: ...

class IWindow:
    """.NET: Rhino.UI.Controls.IWindow"""
    def __init__(self, *args) -> None: ...
    Created: bool
    Shown: bool
    Enabled: bool
    Caption: LocalizeStringPair
    Parent: IntPtr
    Window: IntPtr
    def Move(self, pos: Rectangle, bRepaint: bool, bRepaintBorder: bool) -> None: ...

class ImageButton(Drawable):
    """.NET: Rhino.UI.Controls.ImageButton"""
    def __init__(self, *args) -> None: ...
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

class ImageToolTipButton(ImageButton):
    """.NET: Rhino.UI.Controls.ImageToolTipButton"""
    def __init__(self, *args) -> None: ...
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

class InternalRdkViewModelFactory(FactoryBase):
    """.NET: Rhino.UI.Controls.InternalRdkViewModelFactory"""
    def __init__(self, *args) -> None: ...
    ...

class LabelSeparator(Panel):
    """.NET: Rhino.UI.Controls.LabelSeparator"""
    def __init__(self, *args) -> None: ...
    Text: str
    Color: Color
    UseRhinoColorScheme: bool
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

class LineTypeGridView(GridView):
    """.NET: Rhino.UI.Controls.LineTypeGridView"""
    def __init__(self, *args) -> None: ...
    LineTypeCollection: FilterCollection
    Document: RhinoDoc
    DeleteItemHandler: Func
    CanDeleteItem: Func
    DeleteConfirmationTitle: Func
    DataStore: IEnumerable
    ShowCellBorders: bool
    SelectionPreserver: ISelectionPreserver
    SelectedItems: IEnumerable
    ContextMenu: ContextMenu
    Columns: GridColumnCollection
    ShowHeader: bool
    AllowColumnReordering: bool
    AllowMultipleSelection: bool
    SelectedItem: object
    SelectedItemBinding: BindableBinding
    SelectedRows: IEnumerable
    SelectedRow: int
    RowHeight: int
    GridLines: GridLines
    Border: BorderType
    AllowEmptySelection: bool
    IsEditing: bool
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
    def AddLineTypeItem(self, lt: Linetype, linetypename: str) -> None: ...

class LineTypeItem(ViewModel):
    """.NET: Rhino.UI.Controls.LineTypeItem"""
    def __init__(self, *args) -> None: ...
    Name: str
    Pattern: str
    OriginalPattern: str
    LineTypeId: Guid
    LinetypeIndex: int
    AlwaysModelDistances: bool
    ModelUnitSystem: UnitSystem
    PageUnitSystem: UnitSystem
    ModelDistanceDisplayMode: DistanceDisplayMode
    PageDistanceDisplayMode: DistanceDisplayMode
    ModelDistanceDisplayPrecision: int
    PageDistanceDisplayPrecision: int

class NumericUpDownWithUnitParsing(MaskedTextStepper):
    """.NET: Rhino.UI.Controls.NumericUpDownWithUnitParsing"""
    def __init__(self, *args) -> None: ...
    IsStepping: bool
    IsTextChanging: bool
    UpdateModeWhenInPanel: NumericUpDownWithUnitParsingUpdateMode
    ValueUpdateMode: NumericUpDownWithUnitParsingUpdateMode
    AutoDetectPropertyPanelEmbedding: bool
    ValueBinding: BindableBinding
    Value: float
    HideAlternateTextWhenValueChanges: bool
    IsAlternateTextVisible: bool
    UseDistanceDisplayMode: bool
    InvalidTextColor: Color
    AlternateTextColor: Color
    NumericTextColor: Color
    AlternateText: str
    Prefix: str
    Suffix: str
    Increment: float
    WantReturn: bool
    WantReturnInPanel: bool
    MinValue: float
    MaxValue: float
    DecimalPlaces: int
    MaximumDecimalPlaces: int
    Provider: IMaskedTextProvider
    InsertMode: InsertKeyMode
    IsOverwrite: bool
    ShowPromptOnFocus: bool
    ShowPromptMode: ShowPromptMode
    ShowPlaceholderWhenEmpty: bool
    Text: str
    MaskCompleted: bool
    ValidDirection: StepperValidDirections
    ShowStepper: bool
    ReadOnly: bool
    MaxLength: int
    PlaceholderText: str
    ShowBorder: bool
    TextAlignment: TextAlignment
    CaretIndex: int
    Selection: Range
    SelectedText: str
    AutoSelectMode: AutoSelectMode
    AlwaysShowSelection: bool
    TextColor: Color
    TextBinding: BindableBinding
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
    @staticmethod
    def GetFormatUnitSystem(doc: RhinoDoc, unitSystem: UnitSystem, distanceDisplayMode: DistanceDisplayMode, pageUnits: bool) -> None: ...
    def SetFormatUnitSystem(self, unitSystem: UnitSystem, distanceDisplayMode: DistanceDisplayMode) -> None: ...
    def UseViewModelUnits(self, viewModel: ViewModel) -> None: ...
    def UseViewPageUnits(self, viewModel: ViewModel) -> None: ...

class NumericUpDownWithUnitParsingEventArgs(EventArgs):
    """.NET: Rhino.UI.Controls.NumericUpDownWithUnitParsingEventArgs"""
    def __init__(self, *args) -> None: ...
    PreviousValue: float
    NewValue: float
    StepperArgs: StepperEventArgs

class NumericUpDownWithUnitParsingUpdateMode:
    """.NET: Rhino.UI.Controls.NumericUpDownWithUnitParsingUpdateMode"""
    def __init__(self, *args) -> None: ...
    ...

class PanelWithBorder(Panel):
    """.NET: Rhino.UI.Controls.PanelWithBorder"""
    def __init__(self, *args) -> None: ...
    BackgroundColor: Color
    BorderColor: Color
    BorderThickness: int
    Content: Control
    Padding: Padding
    Controls: IEnumerable
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

class PrintWidthGridView(GridView):
    """.NET: Rhino.UI.Controls.PrintWidthGridView"""
    def __init__(self, *args) -> None: ...
    DeleteItemHandler: Func
    CanDeleteItem: Func
    DeleteConfirmationTitle: Func
    DataStore: IEnumerable
    ShowCellBorders: bool
    SelectionPreserver: ISelectionPreserver
    SelectedItems: IEnumerable
    ContextMenu: ContextMenu
    Columns: GridColumnCollection
    ShowHeader: bool
    AllowColumnReordering: bool
    AllowMultipleSelection: bool
    SelectedItem: object
    SelectedItemBinding: BindableBinding
    SelectedRows: IEnumerable
    SelectedRow: int
    RowHeight: int
    GridLines: GridLines
    Border: BorderType
    AllowEmptySelection: bool
    IsEditing: bool
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

class RangeDialog(Dialog):
    """.NET: Rhino.UI.Controls.RangeDialog"""
    def __init__(self, *args) -> None: ...
    DefaultSize: Size
    Result: bool
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

class RenderContentMenu:
    """.NET: Rhino.UI.Controls.RenderContentMenu"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def AddMenuItem(plugInId: Guid, menuItemName: str, menuOrder: int, separatorStyle: SeparatorStyle, isToplevel: bool, icon: Icon, executeCommandCallback: Func, isEnabledCallback: Func) -> None: ...

class RhinoButtonRow(StackLayout):
    """.NET: Rhino.UI.Controls.RhinoButtonRow"""
    def __init__(self, *args) -> None: ...
    Orientation: Orientation
    Spacing: int
    HorizontalContentAlignment: HorizontalAlignment
    VerticalContentAlignment: VerticalAlignment
    AlignLabels: bool
    Items: Collection
    Controls: IEnumerable
    VisualControls: IEnumerable
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
    def AddButton(self, image: Image, useOverlay: bool, tooltip: str) -> ImageButton: ...

class RhinoButtonStackLayout(StackLayout):
    """.NET: Rhino.UI.Controls.RhinoButtonStackLayout"""
    def __init__(self, *args) -> None: ...
    Orientation: Orientation
    Spacing: int
    HorizontalContentAlignment: HorizontalAlignment
    VerticalContentAlignment: VerticalAlignment
    AlignLabels: bool
    Items: Collection
    Controls: IEnumerable
    VisualControls: IEnumerable
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

class RhinoButtonTableLayout(TableLayout):
    """.NET: Rhino.UI.Controls.RhinoButtonTableLayout"""
    def __init__(self, *args) -> None: ...
    Controls: IEnumerable
    Rows: Collection
    Dimensions: Size
    Spacing: Size
    Padding: Padding
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

class RhinoDialogPanel(Panel):
    """.NET: Rhino.UI.Controls.RhinoDialogPanel"""
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

class RhinoDialogTableLayout(RhinoTableLayout):
    """.NET: Rhino.UI.Controls.RhinoDialogTableLayout"""
    def __init__(self, *args) -> None: ...
    Controls: IEnumerable
    Rows: Collection
    Dimensions: Size
    Spacing: Size
    Padding: Padding
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

class RhinoGroupBox(Panel):
    """.NET: Rhino.UI.Controls.RhinoGroupBox"""
    def __init__(self, *args) -> None: ...
    Text: str
    BackgroundColor: Color
    Content: Control
    Padding: Padding
    Controls: IEnumerable
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

class RhinoIndentedPanel(Panel):
    """.NET: Rhino.UI.Controls.RhinoIndentedPanel"""
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

class RhinoIndentedTableLayout(TableLayout):
    """.NET: Rhino.UI.Controls.RhinoIndentedTableLayout"""
    def __init__(self, *args) -> None: ...
    Controls: IEnumerable
    Rows: Collection
    Dimensions: Size
    Spacing: Size
    Padding: Padding
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

class RhinoLayout:
    """.NET: Rhino.UI.Controls.RhinoLayout"""
    def __init__(self, *args) -> None: ...
    SplitterWidth: int
    @staticmethod
    def DisablePanelColorStyling(etoControl: Control, colorProperty: DisablePanelColorStylingProperty) -> None: ...
    @staticmethod
    def EnablePanelColorStyling(control: Control, colorProperty: DisablePanelColorStylingProperty, invalidate: bool) -> None: ...
    @staticmethod
    def FixedSize(controlType: WidthControlType) -> Size: ...
    @staticmethod
    def FixedWidth(controlType: WidthControlType) -> int: ...
    @staticmethod
    def LabelRow(text: str, editControl: Control, stretch: bool) -> TableRow: ...
    @staticmethod
    def LabelTableLayout(text: str, editControl: Control, stretch: bool, spacingType: SpacingType) -> TableLayout: ...
    @staticmethod
    def NewFileOpenImageButton() -> ImageButton: ...
    @staticmethod
    def NewLabel(text: str) -> Label: ...
    @staticmethod
    def NewLabelSeparator(text: str, wrapMode: WrapMode) -> Label: ...
    @staticmethod
    def Padding(paddingType: PaddingType) -> Padding: ...
    @staticmethod
    def Spacing(spacingType: SpacingType) -> Size: ...
    @staticmethod
    def StackedSpacing(orientation: Orientation, spacingType: SpacingType) -> int: ...

class RhinoNestedStackLayout(StackLayout):
    """.NET: Rhino.UI.Controls.RhinoNestedStackLayout"""
    def __init__(self, *args) -> None: ...
    Orientation: Orientation
    Spacing: int
    HorizontalContentAlignment: HorizontalAlignment
    VerticalContentAlignment: VerticalAlignment
    AlignLabels: bool
    Items: Collection
    Controls: IEnumerable
    VisualControls: IEnumerable
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

class RhinoNestedTableLayout(TableLayout):
    """.NET: Rhino.UI.Controls.RhinoNestedTableLayout"""
    def __init__(self, *args) -> None: ...
    Controls: IEnumerable
    Rows: Collection
    Dimensions: Size
    Spacing: Size
    Padding: Padding
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

class RhinoPanelScrollable(Scrollable):
    """.NET: Rhino.UI.Controls.RhinoPanelScrollable"""
    def __init__(self, *args) -> None: ...
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

class RhinoPanelStackLayout(StackLayout):
    """.NET: Rhino.UI.Controls.RhinoPanelStackLayout"""
    def __init__(self, *args) -> None: ...
    Orientation: Orientation
    Spacing: int
    HorizontalContentAlignment: HorizontalAlignment
    VerticalContentAlignment: VerticalAlignment
    AlignLabels: bool
    Items: Collection
    Controls: IEnumerable
    VisualControls: IEnumerable
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

class RhinoPanelTableLayout(RhinoTableLayout):
    """.NET: Rhino.UI.Controls.RhinoPanelTableLayout"""
    def __init__(self, *args) -> None: ...
    Controls: IEnumerable
    Rows: Collection
    Dimensions: Size
    Spacing: Size
    Padding: Padding
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

class RhinoPropertiesPageTableLayout(RhinoTableLayout):
    """.NET: Rhino.UI.Controls.RhinoPropertiesPageTableLayout"""
    def __init__(self, *args) -> None: ...
    Controls: IEnumerable
    Rows: Collection
    Dimensions: Size
    Spacing: Size
    Padding: Padding
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

class RhinoScrollableDialogPanel(Scrollable):
    """.NET: Rhino.UI.Controls.RhinoScrollableDialogPanel"""
    def __init__(self, *args) -> None: ...
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

class RhinoTableLayout(TableLayout):
    """.NET: Rhino.UI.Controls.RhinoTableLayout"""
    def __init__(self, *args) -> None: ...
    Controls: IEnumerable
    Rows: Collection
    Dimensions: Size
    Spacing: Size
    Padding: Padding
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

class RichTextAreaWithAlternateText(Panel):
    """.NET: Rhino.UI.Controls.RichTextAreaWithAlternateText"""
    def __init__(self, *args) -> None: ...
    RichTextArea: RichTextArea
    AlternateTextArea: TextArea
    ShowAlternateText: bool
    HideAlternateTextWhenValueChanges: bool
    SelectAllOnGotFocus: bool
    AlternateText: str
    ReadOnly: bool
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

class Slider(TableLayout):
    """.NET: Rhino.UI.Controls.Slider"""
    def __init__(self, *args) -> None: ...
    Height: int
    Enabled: bool
    AlternateText: str
    MarkerPointColor1: Color
    MarkerPointColor2: Color
    DrawNumberUnderPoint: bool
    DrawArrows: bool
    DrawTextOnTop: bool
    DrawTextLabels: bool
    DrawEndLines: bool
    MultipleValues: bool
    AllowValuesToCrossRange: bool
    AllowValuesToCrossMaxRange: bool
    AllowValuesToCrossMinRange: bool
    AllowValuesToCross: bool
    Decimals: int
    Value1: Nullable
    Value2: Nullable
    Controls: IEnumerable
    Rows: Collection
    Dimensions: Size
    Spacing: Size
    Padding: Padding
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
    def SetMinMax(self, min: float, max: float) -> None: ...
    def SetVaries(self, varies: bool, value: float) -> None: ...

class StaticAlignedLabel(Label):
    """.NET: Rhino.UI.Controls.StaticAlignedLabel"""
    def __init__(self, *args) -> None: ...
    Wrap: WrapMode
    TextAlignment: TextAlignment
    HorizontalAlign: HorizontalAlign
    VerticalAlignment: VerticalAlignment
    VerticalAlign: VerticalAlign
    UseMnemonic: bool
    AlwaysShowMnemonic: bool
    Text: str
    TextColor: Color
    TextBinding: BindableBinding
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

class UndoRecord:
    """.NET: Rhino.UI.Controls.UndoRecord"""
    def __init__(self, *args) -> None: ...
    def Dispose(self, ) -> None: ...

class UnitParsingMaskedTextProvider(VariableMaskedTextProvider):
    """.NET: Rhino.UI.Controls.UnitParsingMaskedTextProvider"""
    def __init__(self, *args) -> None: ...
    Parent: TextBox
    PrefixOfset: int
    SuffixOfset: int
    DisplayText: str
    Text: str
    EditPositions: IEnumerable
    IsEmpty: bool
    MaskCompleted: bool
    ShowAlternateText: bool
    FormatText: bool
    HideAlternateTextWhenValueChanges: bool
    AlternateText: str
    TextIsValid: bool
    Prefix: str
    Suffix: str
    Value: float
    PreviousValue: float
    Increment: float
    MinValue: float
    MaxValue: float
    DecimalPlaces: int
    MaximumDecimalPlaces: int
    def Clear(self, position: int, length: int, forward: bool) -> bool: ...
    def Delete(self, position: int, length: int, forward: bool) -> bool: ...
    @staticmethod
    def GetDistanceDisplayMode(rhinoDoc: RhinoDoc, getPageUnits: bool) -> DistanceDisplayMode: ...
    def Insert(self, character: str, position: int) -> bool: ...
    def PopShowAlternateText(self, ) -> None: ...
    def PushShowAlternateText(self, ) -> None: ...
    def Replace(self, character: str, position: int) -> bool: ...
    def RevertValue(self, ) -> None: ...
    def SetFormatUnitSystem(self, unitSystem: UnitSystem, distanceDisplayMode: DistanceDisplayMode) -> None: ...

class ViewportControl(Control):
    """.NET: Rhino.UI.Controls.ViewportControl"""
    def __init__(self, *args) -> None: ...
    Viewport: RhinoViewport
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
    def Refresh(self, ) -> None: ...
