# Auto-generated — Rhino 8 — Eto.Forms

class AboutDialog(CommonDialog):
    """.NET: Eto.Forms.AboutDialog"""
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
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool

class AddValueEventArgs(EventArgs):
    """.NET: Eto.Forms.AddValueEventArgs`1"""
    def __init__(self, *args) -> None: ...
    Value: T
    ShouldAdd: bool

class Application(Widget):
    """.NET: Eto.Forms.Application"""
    def __init__(self, *args) -> None: ...
    Instance: Application
    MainForm: Form
    Windows: IEnumerable
    Name: str
    UIThreadCheckMode: UIThreadCheckMode
    IsUIThread: bool
    QuitIsSupported: bool
    CommonModifier: Keys
    AlternateModifier: Keys
    BadgeLabel: str
    IsActive: bool
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    def AsyncInvoke(self, action: Action) -> None: ...
    def Attach(self, context: object) -> Application: ...
    def EnsureUIThread(self, ) -> None: ...
    def Invoke(self, action: Action) -> None: ...
    def InvokeAsync(self, func: Func) -> Task: ...
    def Localize(self, source: object, text: str) -> str: ...
    def Open(self, url: str) -> None: ...
    def Quit(self, ) -> None: ...
    def Restart(self, ) -> None: ...
    def Run(self, mainForm: Form) -> None: ...
    def RunIteration(self, ) -> None: ...

class AutoSelectMode:
    """.NET: Eto.Forms.AutoSelectMode"""
    def __init__(self, *args) -> None: ...
    ...

class BindableBinding(ObjectBinding):
    """.NET: Eto.Forms.BindableBinding`2"""
    def __init__(self, *args) -> None: ...
    InnerBinding: IndirectBinding
    DataItem: T
    GetDataItem: Func
    SettingNullValue: TValue
    GettingNullValue: TValue
    DataValue: TValue
    def Bind(self, sourceBinding: DirectBinding, mode: DualBindingMode) -> DualBinding: ...
    def BindDataContext(self, getValue: Func, setValue: Action, addChangeEvent: Action, removeChangeEvent: Action, mode: DualBindingMode, defaultGetValue: TValue, defaultSetValue: TValue) -> DualBinding: ...
    def Cast(self, ) -> BindableBinding: ...
    def CatchException(self, exceptionHandler: Func) -> BindableBinding: ...
    def Child(self, property: Expression) -> BindableBinding: ...
    def Convert(self, toValue: Func, fromValue: Func) -> BindableBinding: ...

class BindableExtensions:
    """.NET: Eto.Forms.BindableExtensions"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def Bind(bindable: IBindable, controlBinding: IndirectBinding, objectValue: object, objectBinding: IndirectBinding, mode: DualBindingMode, defaultControlValue: T, defaultContextValue: T) -> DualBinding: ...
    @staticmethod
    def BindDataContext(bindable: IBindable, controlPropertyName: str, dataContextPropertyName: str, mode: DualBindingMode, defaultControlValue: T, defaultContextValue: T) -> DualBinding: ...
    @staticmethod
    def DefaultIfNull(binding: BindableBinding, defaultValue: Nullable) -> BindableBinding: ...
    @staticmethod
    def Inverse(binding: BindableBinding) -> BindableBinding: ...

class BindableWidget(Widget):
    """.NET: Eto.Forms.BindableWidget"""
    def __init__(self, *args) -> None: ...
    Parent: Widget
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
    def FindParent(self, type: Type, id: str) -> Widget: ...
    def Unbind(self, ) -> None: ...
    def UpdateBindings(self, mode: BindingUpdateMode) -> None: ...

class Binding:
    """.NET: Eto.Forms.Binding"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def AddPropertyEvent(obj: object, propertyName: str, eh: EventHandler) -> None: ...
    @staticmethod
    def Delegate(getValue: Func, setValue: Action, addChangeEvent: Action, removeChangeEvent: Action, defaultGetValue: TValue, defaultSetValue: TValue) -> IndirectBinding: ...
    @staticmethod
    def ExecuteCommand(dataContext: object, commandBinding: IndirectBinding, parameter: object) -> None: ...
    @staticmethod
    def Property(model: T, propertyExpression: Expression) -> DirectBinding: ...
    @staticmethod
    def RemovePropertyEvent(obj: T, propertyExpression: Expression, eh: EventHandler) -> None: ...
    def Unbind(self, ) -> None: ...
    def Update(self, mode: BindingUpdateMode) -> None: ...

class BindingChangedEventArgs(EventArgs):
    """.NET: Eto.Forms.BindingChangedEventArgs"""
    def __init__(self, *args) -> None: ...
    Value: object

class BindingChangingEventArgs(CancelEventArgs):
    """.NET: Eto.Forms.BindingChangingEventArgs"""
    def __init__(self, *args) -> None: ...
    Value: object
    Cancel: bool

class BindingCollection(Collection):
    """.NET: Eto.Forms.BindingCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: IBinding
    def Unbind(self, ) -> None: ...
    def Update(self, mode: BindingUpdateMode) -> None: ...

class BindingExtensions:
    """.NET: Eto.Forms.BindingExtensions"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def WhenLostFocus(binding: BindableBinding) -> BindableBinding: ...

class BindingUpdateMode:
    """.NET: Eto.Forms.BindingUpdateMode"""
    def __init__(self, *args) -> None: ...
    ...

class BorderType:
    """.NET: Eto.Forms.BorderType"""
    def __init__(self, *args) -> None: ...
    ...

class Button(TextControl):
    """.NET: Eto.Forms.Button"""
    def __init__(self, *args) -> None: ...
    Command: ICommand
    CommandParameter: object
    Image: Image
    ImagePosition: ButtonImagePosition
    MinimumSize: Size
    Size: Size
    Width: int
    Height: int
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
    IsMouseCaptured: bool
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
    def PerformClick(self, ) -> None: ...
    def Unbind(self, ) -> None: ...

class ButtonImagePosition:
    """.NET: Eto.Forms.ButtonImagePosition"""
    def __init__(self, *args) -> None: ...
    ...

class ButtonMenuItem(MenuItem):
    """.NET: Eto.Forms.ButtonMenuItem"""
    def __init__(self, *args) -> None: ...
    Items: MenuItemCollection
    Trim: bool
    Image: Image
    Order: int
    Command: ICommand
    CommandParameter: object
    Text: str
    Tag: object
    ToolTip: str
    Enabled: bool
    Shortcut: Keys
    Visible: bool
    Parent: Widget
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

class ButtonSegmentedItem(SegmentedItem):
    """.NET: Eto.Forms.ButtonSegmentedItem"""
    def __init__(self, *args) -> None: ...
    Parent: SegmentedButton
    Text: str
    ToolTip: str
    Image: Image
    Enabled: bool
    Visible: bool
    Selected: bool
    Width: int
    Command: ICommand
    CommandParameter: object
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

class ButtonToolItem(ToolItem):
    """.NET: Eto.Forms.ButtonToolItem"""
    def __init__(self, *args) -> None: ...
    Command: ICommand
    CommandParameter: object
    Order: int
    Text: str
    ToolTip: str
    Image: Image
    Enabled: bool
    Visible: bool
    Tag: object
    Parent: Widget
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

class Calendar(Control):
    """.NET: Eto.Forms.Calendar"""
    def __init__(self, *args) -> None: ...
    MinDate: DateTime
    MaxDate: DateTime
    SelectedDate: DateTime
    SelectedRange: Range
    Mode: CalendarMode
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

class CalendarMode:
    """.NET: Eto.Forms.CalendarMode"""
    def __init__(self, *args) -> None: ...
    ...

class Cell(Widget):
    """.NET: Eto.Forms.Cell"""
    def __init__(self, *args) -> None: ...
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool

class CellEventArgs(EventArgs):
    """.NET: Eto.Forms.CellEventArgs"""
    def __init__(self, *args) -> None: ...
    CellState: CellStates
    Item: object
    Row: int
    Column: int
    GridColumn: GridColumn
    Cell: Cell
    Grid: Grid
    Control: Control
    Handled: bool
    CellTextColor: Color
    IsEditing: bool
    IsSelected: bool

class CellPaintEventArgs(PaintEventArgs):
    """.NET: Eto.Forms.CellPaintEventArgs"""
    def __init__(self, *args) -> None: ...
    CellState: CellStates
    Item: object
    IsEditing: bool
    IsSelected: bool
    Graphics: Graphics
    ClipRectangle: RectangleF

class CellStates:
    """.NET: Eto.Forms.CellStates"""
    def __init__(self, *args) -> None: ...
    ...

class CheckBox(TextControl):
    """.NET: Eto.Forms.CheckBox"""
    def __init__(self, *args) -> None: ...
    Checked: Nullable
    ThreeState: bool
    CheckedBinding: BindableBinding
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

class CheckBoxCell(SingleValueCell):
    """.NET: Eto.Forms.CheckBoxCell"""
    def __init__(self, *args) -> None: ...
    Binding: IIndirectBinding
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool

class CheckBoxList(Panel):
    """.NET: Eto.Forms.CheckBoxList"""
    def __init__(self, *args) -> None: ...
    ItemTextBinding: IIndirectBinding
    ItemToolTipBinding: IIndirectBinding
    ItemKeyBinding: IIndirectBinding
    SelectedKeys: IEnumerable
    Enabled: bool
    SelectedValues: IEnumerable
    TextColor: Color
    Orientation: Orientation
    Spacing: Size
    Items: ListItemCollection
    DataStore: IEnumerable
    SelectedValuesBinding: BindableBinding
    SelectedKeysBinding: BindableBinding
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

class CheckCommand(Command):
    """.NET: Eto.Forms.CheckCommand"""
    def __init__(self, *args) -> None: ...
    Checked: bool
    ID: str
    Enabled: bool
    Tag: object
    MenuText: str
    ToolBarText: str
    ToolTip: str
    Image: Image
    Shortcut: Keys
    Properties: PropertyStore
    DelegatedCommand: ICommand
    CommandParameter: object
    Parent: IBindable
    DataContext: object
    IsDataContextChanging: bool
    Bindings: BindingCollection
    def CreateMenuItem(self, ) -> MenuItem: ...
    def CreateToolItem(self, ) -> ToolItem: ...

class CheckMenuItem(MenuItem):
    """.NET: Eto.Forms.CheckMenuItem"""
    def __init__(self, *args) -> None: ...
    Checked: bool
    Order: int
    Command: ICommand
    CommandParameter: object
    Text: str
    Tag: object
    ToolTip: str
    Enabled: bool
    Shortcut: Keys
    Visible: bool
    Parent: Widget
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
    def PerformClick(self, ) -> None: ...

class CheckToolItem(ToolItem):
    """.NET: Eto.Forms.CheckToolItem"""
    def __init__(self, *args) -> None: ...
    Checked: bool
    Command: ICommand
    CommandParameter: object
    Order: int
    Text: str
    ToolTip: str
    Image: Image
    Enabled: bool
    Visible: bool
    Tag: object
    Parent: Widget
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
    def OnCheckedChanged(self, e: EventArgs) -> None: ...

class Clipboard(Widget):
    """.NET: Eto.Forms.Clipboard"""
    def __init__(self, *args) -> None: ...
    Instance: Clipboard
    Types: list
    ContainsText: bool
    ContainsHtml: bool
    ContainsImage: bool
    ContainsUris: bool
    Text: str
    Html: str
    Image: Image
    Uris: list
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    def Clear(self, ) -> None: ...
    def Contains(self, type: str) -> bool: ...
    def GetData(self, type: str) -> list: ...
    def GetDataStream(self, type: str) -> Stream: ...
    def GetObject(self, type: str, objectType: Type) -> object: ...
    def GetString(self, type: str) -> str: ...
    def SetData(self, value: list, type: str) -> None: ...
    def SetDataStream(self, stream: Stream, type: str) -> None: ...
    def SetObject(self, value: object, type: str) -> None: ...
    def SetString(self, value: str, type: str) -> None: ...

class CollectionEditor(Control):
    """.NET: Eto.Forms.CollectionEditor"""
    def __init__(self, *args) -> None: ...
    DataStore: IEnumerable
    ElementType: Type
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

class ColorDialog(CommonDialog):
    """.NET: Eto.Forms.ColorDialog"""
    def __init__(self, *args) -> None: ...
    Color: Color
    AllowAlpha: bool
    SupportsAllowAlpha: bool
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool

class ColorPicker(Control):
    """.NET: Eto.Forms.ColorPicker"""
    def __init__(self, *args) -> None: ...
    Value: Color
    AllowAlpha: bool
    SupportsAllowAlpha: bool
    ValueBinding: BindableBinding
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

class ColumnBinding(IndirectBinding):
    """.NET: Eto.Forms.ColumnBinding`1"""
    def __init__(self, *args) -> None: ...
    Column: int

class ComboBox(DropDown):
    """.NET: Eto.Forms.ComboBox"""
    def __init__(self, *args) -> None: ...
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

class ComboBoxCell(SingleValueCell):
    """.NET: Eto.Forms.ComboBoxCell"""
    def __init__(self, *args) -> None: ...
    ComboTextBinding: IIndirectBinding
    ComboKeyBinding: IIndirectBinding
    DataStore: IEnumerable
    Binding: IIndirectBinding
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool

class Command:
    """.NET: Eto.Forms.Command"""
    def __init__(self, *args) -> None: ...
    ID: str
    Enabled: bool
    Tag: object
    MenuText: str
    ToolBarText: str
    ToolTip: str
    Image: Image
    Shortcut: Keys
    Properties: PropertyStore
    DelegatedCommand: ICommand
    CommandParameter: object
    Parent: IBindable
    DataContext: object
    IsDataContextChanging: bool
    Bindings: BindingCollection
    def CreateMenuItem(self, ) -> MenuItem: ...
    def CreateToolItem(self, ) -> ToolItem: ...
    def Execute(self, ) -> None: ...

class CommonControl(Control):
    """.NET: Eto.Forms.CommonControl"""
    def __init__(self, *args) -> None: ...
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

class CommonDialog(Widget):
    """.NET: Eto.Forms.CommonDialog"""
    def __init__(self, *args) -> None: ...
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    def ShowDialog(self, parent: Control) -> DialogResult: ...

class Container(Control):
    """.NET: Eto.Forms.Container"""
    def __init__(self, *args) -> None: ...
    ClientSize: Size
    Controls: IEnumerable
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
    def FindChild(self, type: Type, id: str) -> Control: ...
    def Remove(self, controls: IEnumerable) -> None: ...
    def RemoveAll(self, ) -> None: ...

class ContextMenu(Menu):
    """.NET: Eto.Forms.ContextMenu"""
    def __init__(self, *args) -> None: ...
    Items: MenuItemCollection
    Trim: bool
    Parent: Widget
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
    def Show(self, relativeTo: Control, location: Nullable) -> None: ...

class Control(BindableWidget):
    """.NET: Eto.Forms.Control"""
    def __init__(self, *args) -> None: ...
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
    def AttachNative(self, ) -> None: ...
    def CaptureMouse(self, ) -> bool: ...
    def Detach(self, ) -> None: ...
    def DetachNative(self, ) -> None: ...
    def DoDragDrop(self, data: DataObject, allowedEffects: DragEffects, image: Image, cursorOffset: PointF) -> None: ...
    def FindParent(self, type: Type, id: str) -> Container: ...
    def Focus(self, ) -> None: ...
    def GetPreferredSize(self, availableSize: SizeF) -> SizeF: ...
    def Invalidate(self, rect: Rectangle, invalidateChildren: bool) -> None: ...
    def MapPlatformCommand(self, systemCommand: str, command: Command) -> None: ...
    def PointFromScreen(self, point: PointF) -> PointF: ...
    def PointToScreen(self, point: PointF) -> PointF: ...
    def Print(self, ) -> None: ...
    def RectangleFromScreen(self, rect: RectangleF) -> RectangleF: ...
    def RectangleToScreen(self, rect: RectangleF) -> RectangleF: ...
    def ReleaseMouseCapture(self, ) -> None: ...
    def ResumeLayout(self, ) -> None: ...
    def SuspendLayout(self, ) -> None: ...
    def TriggerStyleChanged(self, ) -> None: ...
    def UpdateLayout(self, ) -> None: ...

class ControlBinding(BindableBinding):
    """.NET: Eto.Forms.ControlBinding`2"""
    def __init__(self, *args) -> None: ...
    InnerBinding: IndirectBinding
    DataItem: T
    GetDataItem: Func
    SettingNullValue: TValue
    GettingNullValue: TValue
    DataValue: TValue

class CreateNativeControlArgs(EventArgs):
    """.NET: Eto.Forms.CreateNativeControlArgs"""
    def __init__(self, *args) -> None: ...
    NativeControl: object

class Cursor(Widget):
    """.NET: Eto.Forms.Cursor"""
    def __init__(self, *args) -> None: ...
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    @staticmethod
    def FromResource(resourceName: str, assembly: Assembly) -> Cursor: ...

class CursorType:
    """.NET: Eto.Forms.CursorType"""
    def __init__(self, *args) -> None: ...
    ...

class Cursors:
    """.NET: Eto.Forms.Cursors"""
    def __init__(self, *args) -> None: ...
    Default: Cursor
    Arrow: Cursor
    Crosshair: Cursor
    Pointer: Cursor
    Move: Cursor
    IBeam: Cursor
    VerticalSplit: Cursor
    HorizontalSplit: Cursor
    SizeAll: Cursor
    SizeLeft: Cursor
    SizeTop: Cursor
    SizeRight: Cursor
    SizeBottom: Cursor
    SizeTopLeft: Cursor
    SizeTopRight: Cursor
    SizeBottomLeft: Cursor
    SizeBottomRight: Cursor
    NotAllowed: Cursor
    @staticmethod
    def Cached(type: CursorType) -> Cursor: ...
    @staticmethod
    def ClearCache() -> None: ...

class CustomCell(Cell):
    """.NET: Eto.Forms.CustomCell"""
    def __init__(self, *args) -> None: ...
    SupportsControlView: bool
    CreateCell: Func
    GetIdentifier: Func
    GetPreferredWidth: Func
    ConfigureCell: Action
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    @staticmethod
    def Create() -> CustomCell: ...

class DataFormats:
    """.NET: Eto.Forms.DataFormats"""
    def __init__(self, *args) -> None: ...
    Text: str
    Html: str
    Color: str

class DataObject(Widget):
    """.NET: Eto.Forms.DataObject"""
    def __init__(self, *args) -> None: ...
    Types: list
    ContainsText: bool
    ContainsHtml: bool
    ContainsImage: bool
    ContainsUris: bool
    Text: str
    Html: str
    Image: Image
    Uris: list
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    def Clear(self, ) -> None: ...
    def Contains(self, type: str) -> bool: ...
    def GetData(self, type: str) -> list: ...
    def GetDataStream(self, type: str) -> Stream: ...
    def GetObject(self, type: str, objectType: Type) -> object: ...
    def GetString(self, type: str) -> str: ...
    def SetData(self, value: list, type: str) -> None: ...
    def SetDataStream(self, stream: Stream, type: str) -> None: ...
    def SetObject(self, value: object, type: str) -> None: ...
    def SetString(self, value: str, type: str) -> None: ...

class DataStoreCollection(ExtendedObservableCollection):
    """.NET: Eto.Forms.DataStoreCollection`1"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: T

class DataStoreExtensions:
    """.NET: Eto.Forms.DataStoreExtensions"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetExpandedRowCount(store: IDataStore, index: int) -> int: ...
    @staticmethod
    def GetRowOfIndexPath(store: IDataStore, indexPath: list) -> int: ...

class DataStoreVirtualCollection:
    """.NET: Eto.Forms.DataStoreVirtualCollection`1"""
    def __init__(self, *args) -> None: ...
    Item: T
    Count: int
    IsReadOnly: bool
    IsFixedSize: bool
    IsSynchronized: bool
    SyncRoot: object
    def Add(self, item: T) -> None: ...
    def Clear(self, ) -> None: ...
    def Contains(self, item: T) -> bool: ...
    def CopyTo(self, array: list, arrayIndex: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, item: T) -> int: ...
    def Insert(self, index: int, item: T) -> None: ...
    def Remove(self, item: T) -> bool: ...
    def RemoveAt(self, index: int) -> None: ...

class DateTimePicker(CommonControl):
    """.NET: Eto.Forms.DateTimePicker"""
    def __init__(self, *args) -> None: ...
    MinDate: DateTime
    MaxDate: DateTime
    Value: Nullable
    ValueBinding: BindableBinding
    Mode: DateTimePickerMode
    TextColor: Color
    ShowBorder: bool
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

class DateTimePickerMode:
    """.NET: Eto.Forms.DateTimePickerMode"""
    def __init__(self, *args) -> None: ...
    ...

class DelegateBinding(DirectBinding):
    """.NET: Eto.Forms.DelegateBinding`1 | Eto.Forms.DelegateBinding`2"""
    def __init__(self, *args) -> None: ...
    GetValue: Func
    SetValue: Action
    AddChangeEvent: Action
    RemoveChangeEvent: Action
    DataValue: TValue
    DefaultGetValue: TValue
    DefaultSetValue: TValue
    def AddValueChangedHandler(self, dataItem: object, handler: EventHandler) -> object: ...
    def RemoveValueChangedHandler(self, bindingReference: object, handler: EventHandler) -> None: ...

class Dialog(Window):
    """.NET: Eto.Forms.Dialog | Eto.Forms.Dialog`1"""
    def __init__(self, *args) -> None: ...
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
    Result: T
    def Close(self, result: T) -> None: ...
    def ShowModal(self, owner: Control) -> None: ...
    def ShowModalAsync(self, owner: Control) -> Task: ...

class DialogDisplayMode:
    """.NET: Eto.Forms.DialogDisplayMode"""
    def __init__(self, *args) -> None: ...
    ...

class DialogResult:
    """.NET: Eto.Forms.DialogResult"""
    def __init__(self, *args) -> None: ...
    ...

class DirectBinding(Binding):
    """.NET: Eto.Forms.DirectBinding`1"""
    def __init__(self, *args) -> None: ...
    DataValue: T
    def Cast(self, ) -> DirectBinding: ...
    def CatchException(self, exceptionHandler: Func) -> DirectBinding: ...
    def Child(self, property: Expression) -> DirectBinding: ...
    def Convert(self, toValue: Func, fromValue: Func) -> DirectBinding: ...
    def ToBool(self, trueValue: T, falseValue: T, nullValue: T) -> DirectBinding: ...
    def ToType(self, invalidGetValue: Func, invalidSetValue: Func) -> DirectBinding: ...

class DockPosition:
    """.NET: Eto.Forms.DockPosition"""
    def __init__(self, *args) -> None: ...
    ...

class DocumentControl(Container):
    """.NET: Eto.Forms.DocumentControl"""
    def __init__(self, *args) -> None: ...
    Controls: IEnumerable
    SelectedIndex: int
    SelectedPage: DocumentPage
    Pages: IList
    AllowReordering: bool
    SelectedIndexBinding: BindableBinding
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
    def Remove(self, child: Control) -> None: ...

class DocumentPage(Panel):
    """.NET: Eto.Forms.DocumentPage"""
    def __init__(self, *args) -> None: ...
    Closable: bool
    HasUnsavedChanges: bool
    Image: Image
    Text: str
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

class DocumentPageClosingEventArgs(CancelEventArgs):
    """.NET: Eto.Forms.DocumentPageClosingEventArgs"""
    def __init__(self, *args) -> None: ...
    Page: DocumentPage
    Cancel: bool

class DocumentPageEventArgs(EventArgs):
    """.NET: Eto.Forms.DocumentPageEventArgs"""
    def __init__(self, *args) -> None: ...
    Page: DocumentPage

class DocumentPageReorderEventArgs(DocumentPageEventArgs):
    """.NET: Eto.Forms.DocumentPageReorderEventArgs"""
    def __init__(self, *args) -> None: ...
    OldIndex: int
    NewIndex: int
    Page: DocumentPage

class DragEffects:
    """.NET: Eto.Forms.DragEffects"""
    def __init__(self, *args) -> None: ...
    ...

class DragEventArgs(EventArgs):
    """.NET: Eto.Forms.DragEventArgs"""
    def __init__(self, *args) -> None: ...
    Source: Control
    Data: DataObject
    AllowedEffects: DragEffects
    Effects: DragEffects
    Location: PointF
    Modifiers: Keys
    Buttons: MouseButtons
    ControlObject: object
    SupportsDropDescription: bool
    def SetDropDescription(self, format: str, inner: str) -> None: ...

class Drawable(Panel):
    """.NET: Eto.Forms.Drawable"""
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
    def CreateGraphics(self, ) -> Graphics: ...
    def Update(self, region: Rectangle) -> None: ...

class DrawableCell(Cell):
    """.NET: Eto.Forms.DrawableCell"""
    def __init__(self, *args) -> None: ...
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool

class DrawableCellPaintEventArgs(CellPaintEventArgs):
    """.NET: Eto.Forms.DrawableCellPaintEventArgs"""
    def __init__(self, *args) -> None: ...
    CellState: CellStates
    Item: object
    IsEditing: bool
    IsSelected: bool
    Graphics: Graphics
    ClipRectangle: RectangleF

class DrawableCellStates:
    """.NET: Eto.Forms.DrawableCellStates"""
    def __init__(self, *args) -> None: ...
    Selected: DrawableCellStates
    None: DrawableCellStates
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class DropDown(ListControl):
    """.NET: Eto.Forms.DropDown"""
    def __init__(self, *args) -> None: ...
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

class DropDownFormatEventArgs(EventArgs):
    """.NET: Eto.Forms.DropDownFormatEventArgs"""
    def __init__(self, *args) -> None: ...
    Font: Font
    IsFontSet: bool
    Item: object
    Row: int

class DropDownToolItem(ToolItem):
    """.NET: Eto.Forms.DropDownToolItem"""
    def __init__(self, *args) -> None: ...
    ShowDropArrow: bool
    Items: MenuItemCollection
    Command: ICommand
    CommandParameter: object
    Order: int
    Text: str
    ToolTip: str
    Image: Image
    Enabled: bool
    Visible: bool
    Tag: object
    Parent: Widget
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

class DualBinding(Binding):
    """.NET: Eto.Forms.DualBinding`1"""
    def __init__(self, *args) -> None: ...
    Source: DirectBinding
    Destination: DirectBinding
    Mode: DualBindingMode
    def SetDestination(self, ) -> None: ...
    def SetSource(self, ) -> None: ...
    def ToString(self, ) -> str: ...
    def Unbind(self, ) -> None: ...
    def Update(self, mode: BindingUpdateMode) -> None: ...

class DualBindingMode:
    """.NET: Eto.Forms.DualBindingMode"""
    def __init__(self, *args) -> None: ...
    ...

class DynamicControl(DynamicItem):
    """.NET: Eto.Forms.DynamicControl"""
    def __init__(self, *args) -> None: ...
    Control: Control
    XScale: Nullable
    YScale: Nullable
    def Create(self, layout: DynamicLayout) -> Control: ...

class DynamicGroup(DynamicTable):
    """.NET: Eto.Forms.DynamicGroup"""
    def __init__(self, *args) -> None: ...
    Title: str
    GroupBox: GroupBox
    Rows: Collection
    Table: TableLayout
    Parent: DynamicTable
    Padding: Nullable
    Spacing: Nullable
    Visible: bool
    XScale: Nullable
    YScale: Nullable
    def Create(self, layout: DynamicLayout) -> Control: ...

class DynamicItem:
    """.NET: Eto.Forms.DynamicItem"""
    def __init__(self, *args) -> None: ...
    XScale: Nullable
    YScale: Nullable
    def Create(self, layout: DynamicLayout, parent: TableLayout, x: int, y: int) -> None: ...

class DynamicLayout(Panel):
    """.NET: Eto.Forms.DynamicLayout"""
    def __init__(self, *args) -> None: ...
    Rows: Collection
    IsCreated: bool
    Padding: Nullable
    Spacing: Nullable
    DefaultPadding: Nullable
    DefaultSpacing: Nullable
    Controls: IEnumerable
    VisualControls: IEnumerable
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
    def Add(self, control: Control, xscale: Nullable, yscale: Nullable) -> DynamicControl: ...
    def AddAutoSized(self, control: Control, padding: Nullable, spacing: Nullable, xscale: Nullable, yscale: Nullable, centered: bool) -> None: ...
    def AddCentered(self, control: Control, padding: Nullable, spacing: Nullable, xscale: Nullable, yscale: Nullable, horizontalCenter: bool, verticalCenter: bool) -> None: ...
    def AddColumn(self, controls: list) -> None: ...
    def AddRange(self, controls: IEnumerable) -> None: ...
    def AddRow(self, controls: list) -> DynamicRow: ...
    def AddSeparateColumn(self, padding: Nullable, spacing: Nullable, xscale: Nullable, yscale: Nullable, controls: IEnumerable) -> DynamicTable: ...
    def AddSeparateRow(self, padding: Nullable, spacing: Nullable, xscale: Nullable, yscale: Nullable, controls: IEnumerable) -> DynamicRow: ...
    def AddSpace(self, xscale: Nullable, yscale: Nullable) -> DynamicControl: ...
    def BeginCentered(self, padding: Nullable, spacing: Nullable, xscale: Nullable, yscale: Nullable) -> None: ...
    def BeginGroup(self, title: str, padding: Nullable, spacing: Nullable, xscale: Nullable, yscale: Nullable) -> DynamicGroup: ...
    def BeginHorizontal(self, yscale: Nullable) -> DynamicRow: ...
    def BeginScrollable(self, border: BorderType, padding: Nullable, spacing: Nullable, xscale: Nullable, yscale: Nullable) -> DynamicScrollable: ...
    def BeginVertical(self, padding: Nullable, spacing: Nullable, xscale: Nullable, yscale: Nullable) -> DynamicTable: ...
    def Clear(self, ) -> None: ...
    def Create(self, ) -> None: ...
    def EndBeginHorizontal(self, yscale: Nullable) -> DynamicRow: ...
    def EndBeginVertical(self, padding: Nullable, spacing: Nullable, xscale: Nullable, yscale: Nullable) -> DynamicTable: ...
    def EndCentered(self, ) -> None: ...
    def EndGroup(self, ) -> None: ...
    def EndHorizontal(self, ) -> None: ...
    def EndScrollable(self, ) -> None: ...
    def EndVertical(self, ) -> None: ...

class DynamicRow(Collection):
    """.NET: Eto.Forms.DynamicRow"""
    def __init__(self, *args) -> None: ...
    Table: DynamicTable
    Items: Collection
    Count: int
    Item: DynamicItem
    def Add(self, controls: IEnumerable, xscale: Nullable, yscale: Nullable) -> None: ...

class DynamicScrollable(DynamicTable):
    """.NET: Eto.Forms.DynamicScrollable"""
    def __init__(self, *args) -> None: ...
    Border: BorderType
    Scrollable: Scrollable
    Rows: Collection
    Table: TableLayout
    Parent: DynamicTable
    Padding: Nullable
    Spacing: Nullable
    Visible: bool
    XScale: Nullable
    YScale: Nullable
    def Create(self, layout: DynamicLayout) -> Control: ...

class DynamicTable(DynamicItem):
    """.NET: Eto.Forms.DynamicTable"""
    def __init__(self, *args) -> None: ...
    Rows: Collection
    Table: TableLayout
    Parent: DynamicTable
    Padding: Nullable
    Spacing: Nullable
    Visible: bool
    XScale: Nullable
    YScale: Nullable
    def Add(self, item: DynamicItem) -> None: ...
    def AddRow(self, item: DynamicItem) -> None: ...
    def Create(self, layout: DynamicLayout) -> Control: ...

class EnumCheckBoxList(CheckBoxList):
    """.NET: Eto.Forms.EnumCheckBoxList`1"""
    def __init__(self, *args) -> None: ...
    SelectedValues: IEnumerable
    IncludeNoneFlag: bool
    GetText: Func
    SortAlphabetically: bool
    SelectedValuesBinding: BindableBinding
    ItemTextBinding: IIndirectBinding
    ItemToolTipBinding: IIndirectBinding
    ItemKeyBinding: IIndirectBinding
    SelectedKeys: IEnumerable
    Enabled: bool
    TextColor: Color
    Orientation: Orientation
    Spacing: Size
    Items: ListItemCollection
    DataStore: IEnumerable
    SelectedKeysBinding: BindableBinding
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

class EnumDropDown(DropDown):
    """.NET: Eto.Forms.EnumDropDown`1"""
    def __init__(self, *args) -> None: ...
    SelectedValue: T
    GetText: Func
    SortAlphabetically: bool
    SelectedValueBinding: BindableBinding
    ItemImageBinding: IIndirectBinding
    ShowBorder: bool
    ItemTextBinding: IIndirectBinding
    ItemKeyBinding: IIndirectBinding
    TextBinding: IIndirectBinding
    KeyBinding: IIndirectBinding
    Items: ListItemCollection
    DataStore: IEnumerable
    SelectedIndex: int
    SelectedKey: str
    TextColor: Color
    SelectedIndexBinding: BindableBinding
    SelectedKeyBinding: BindableBinding
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

class EnumRadioButtonList(RadioButtonList):
    """.NET: Eto.Forms.EnumRadioButtonList`1"""
    def __init__(self, *args) -> None: ...
    SelectedValue: T
    GetText: Func
    SortAlphabetically: bool
    SelectedValueBinding: BindableBinding
    ItemTextBinding: IIndirectBinding
    ItemKeyBinding: IIndirectBinding
    ItemToolTipBinding: IIndirectBinding
    TextBinding: IIndirectBinding
    KeyBinding: IIndirectBinding
    SelectedKey: str
    Enabled: bool
    SelectedIndex: int
    TextColor: Color
    Orientation: Orientation
    Spacing: Size
    Items: ListItemCollection
    DataStore: IEnumerable
    SelectedIndexBinding: BindableBinding
    SelectedKeyBinding: BindableBinding
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

class Expander(Panel):
    """.NET: Eto.Forms.Expander"""
    def __init__(self, *args) -> None: ...
    Controls: IEnumerable
    Expanded: bool
    Header: Control
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

class FileDialog(CommonDialog):
    """.NET: Eto.Forms.FileDialog"""
    def __init__(self, *args) -> None: ...
    FileName: str
    Filters: Collection
    CurrentFilterIndex: int
    CurrentFilter: FileFilter
    CheckFileExists: bool
    Title: str
    Directory: Uri
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool

class FileDialogFilter(FileFilter):
    """.NET: Eto.Forms.FileDialogFilter"""
    def __init__(self, *args) -> None: ...
    Name: str
    Extensions: list

class FileFilter:
    """.NET: Eto.Forms.FileFilter"""
    def __init__(self, *args) -> None: ...
    Name: str
    Extensions: list
    def GetHashCode(self, ) -> int: ...
    def ToString(self, ) -> str: ...

class FilePicker(Control):
    """.NET: Eto.Forms.FilePicker"""
    def __init__(self, *args) -> None: ...
    CurrentFilterIndex: int
    CurrentFilter: FileFilter
    Filters: Collection
    FileAction: FileAction
    FilePath: str
    Title: str
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

class FilterCollection:
    """.NET: Eto.Forms.FilterCollection`1"""
    def __init__(self, *args) -> None: ...
    Change: Func
    Filter: Func
    Sort: Comparison
    Item: T
    Count: int
    IsReadOnly: bool
    def Add(self, item: T) -> None: ...
    def AddRange(self, items: IEnumerable) -> None: ...
    def Clear(self, ) -> None: ...
    def Contains(self, item: T) -> bool: ...
    def CopyTo(self, array: list, arrayIndex: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, item: T) -> int: ...
    def Insert(self, index: int, item: T) -> None: ...
    def InsertRange(self, index: int, items: IEnumerable) -> None: ...
    def Refresh(self, ) -> None: ...
    def Remove(self, item: T) -> bool: ...
    def RemoveAt(self, index: int) -> None: ...

class FixedMaskedTextProvider:
    """.NET: Eto.Forms.FixedMaskedTextProvider | Eto.Forms.FixedMaskedTextProvider`1"""
    def __init__(self, *args) -> None: ...
    Culture: CultureInfo
    Mask: str
    AllowPromptAsInput: bool
    PromptChar: str
    PasswordChar: str
    AsciiOnly: bool
    DisplayText: str
    Text: str
    MaskCompleted: bool
    IsPassword: bool
    IncludeLiterals: bool
    IncludePrompt: bool
    SkipLiterals: bool
    AutoAdvance: bool
    EditPositions: IEnumerable
    IsEmpty: bool
    MaskFull: bool
    ConvertToValue: Func
    ConvertToText: Func
    Value: T
    def Clear(self, position: int, length: int, forward: bool) -> bool: ...
    def Delete(self, position: int, length: int, forward: bool) -> bool: ...
    def Insert(self, character: str, position: int) -> bool: ...
    def Replace(self, character: str, position: int) -> bool: ...

class FloatingForm(Form):
    """.NET: Eto.Forms.FloatingForm"""
    def __init__(self, *args) -> None: ...
    ShowActivated: bool
    CanFocus: bool
    Visible: bool
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

class FontDialog(CommonDialog):
    """.NET: Eto.Forms.FontDialog"""
    def __init__(self, *args) -> None: ...
    Font: Font
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool

class FontPicker(Control):
    """.NET: Eto.Forms.FontPicker"""
    def __init__(self, *args) -> None: ...
    Value: Font
    ValueBinding: BindableBinding
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

class Form(Window):
    """.NET: Eto.Forms.Form"""
    def __init__(self, *args) -> None: ...
    ShowActivated: bool
    CanFocus: bool
    Visible: bool
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
    def Show(self, ) -> None: ...
    def ShowAsync(self, ) -> Task: ...

class Grid(Control):
    """.NET: Eto.Forms.Grid"""
    def __init__(self, *args) -> None: ...
    Columns: GridColumnCollection
    ShowHeader: bool
    AllowColumnReordering: bool
    AllowMultipleSelection: bool
    SelectedItems: IEnumerable
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
    def BeginEdit(self, row: int, column: int) -> None: ...
    def CancelEdit(self, ) -> bool: ...
    def CommitEdit(self, ) -> bool: ...
    def ScrollToRow(self, row: int) -> None: ...
    def SelectAll(self, ) -> None: ...
    def SelectRow(self, row: int) -> None: ...
    def UnselectAll(self, ) -> None: ...
    def UnselectRow(self, row: int) -> None: ...

class GridCell:
    """.NET: Eto.Forms.GridCell"""
    def __init__(self, *args) -> None: ...
    Item: object
    RowIndex: int
    Column: GridColumn
    ColumnIndex: int
    Type: GridCellType

class GridCellFormatEventArgs(EventArgs):
    """.NET: Eto.Forms.GridCellFormatEventArgs"""
    def __init__(self, *args) -> None: ...
    Column: GridColumn
    Item: object
    Row: int
    Font: Font
    BackgroundColor: Color
    ForegroundColor: Color

class GridCellMouseEventArgs(MouseEventArgs):
    """.NET: Eto.Forms.GridCellMouseEventArgs"""
    def __init__(self, *args) -> None: ...
    GridColumn: GridColumn
    Row: int
    Column: int
    Item: object
    Modifiers: Keys
    Buttons: MouseButtons
    Location: PointF
    Handled: bool
    Pressure: float
    Delta: SizeF

class GridCellType:
    """.NET: Eto.Forms.GridCellType"""
    def __init__(self, *args) -> None: ...
    ...

class GridColumn(Widget):
    """.NET: Eto.Forms.GridColumn"""
    def __init__(self, *args) -> None: ...
    HeaderText: str
    HeaderToolTip: str
    CellToolTipBinding: IIndirectBinding
    Resizable: bool
    AutoSize: bool
    Sortable: bool
    Width: int
    DataCell: Cell
    Editable: bool
    Visible: bool
    Expand: bool
    HeaderTextAlignment: TextAlignment
    MinWidth: int
    MaxWidth: int
    DisplayIndex: int
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool

class GridColumnCollection(ObservableCollection):
    """.NET: Eto.Forms.GridColumnCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: GridColumn

class GridColumnEventArgs(EventArgs):
    """.NET: Eto.Forms.GridColumnEventArgs"""
    def __init__(self, *args) -> None: ...
    Column: GridColumn

class GridDragPosition:
    """.NET: Eto.Forms.GridDragPosition"""
    def __init__(self, *args) -> None: ...
    ...

class GridItem:
    """.NET: Eto.Forms.GridItem"""
    def __init__(self, *args) -> None: ...
    Tag: object
    Values: list
    def GetValue(self, column: int) -> object: ...
    def SetValue(self, column: int, value: object) -> None: ...

class GridLines:
    """.NET: Eto.Forms.GridLines"""
    def __init__(self, *args) -> None: ...
    ...

class GridRowFormatEventArgs(EventArgs):
    """.NET: Eto.Forms.GridRowFormatEventArgs"""
    def __init__(self, *args) -> None: ...
    BackgroundColor: Color
    Item: object
    Row: int

class GridView(Grid):
    """.NET: Eto.Forms.GridView | Eto.Forms.GridView`1"""
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
    def GetCellAt(self, location: PointF) -> GridCell: ...
    def GetDragInfo(self, args: DragEventArgs) -> GridViewDragInfo: ...
    def ReloadData(self, row: int) -> None: ...

class GridViewCellEventArgs(EventArgs):
    """.NET: Eto.Forms.GridViewCellEventArgs"""
    def __init__(self, *args) -> None: ...
    GridColumn: GridColumn
    Row: int
    Column: int
    Item: object

class GridViewDragInfo:
    """.NET: Eto.Forms.GridViewDragInfo"""
    def __init__(self, *args) -> None: ...
    Item: object
    Index: int
    Position: GridDragPosition
    Control: GridView
    IsChanged: bool
    InsertIndex: int
    def RestrictToInsert(self, ) -> None: ...
    def RestrictToOver(self, ) -> None: ...

class GroupBox(Panel):
    """.NET: Eto.Forms.GroupBox"""
    def __init__(self, *args) -> None: ...
    Font: Font
    Text: str
    TextColor: Color
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

class HorizontalAlign:
    """.NET: Eto.Forms.HorizontalAlign"""
    def __init__(self, *args) -> None: ...
    Center: HorizontalAlign
    Left: HorizontalAlign
    Right: HorizontalAlign
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class HorizontalAlignment:
    """.NET: Eto.Forms.HorizontalAlignment"""
    def __init__(self, *args) -> None: ...
    ...

class IBindable:
    """.NET: Eto.Forms.IBindable"""
    def __init__(self, *args) -> None: ...
    DataContext: object
    IsDataContextChanging: bool
    Bindings: BindingCollection

class IBindableWidgetContainer:
    """.NET: Eto.Forms.IBindableWidgetContainer"""
    def __init__(self, *args) -> None: ...
    Children: IEnumerable

class IBinding:
    """.NET: Eto.Forms.IBinding"""
    def __init__(self, *args) -> None: ...
    def Unbind(self, ) -> None: ...
    def Update(self, mode: BindingUpdateMode) -> None: ...

class IColumnItem:
    """.NET: Eto.Forms.IColumnItem"""
    def __init__(self, *args) -> None: ...
    def GetValue(self, column: int) -> object: ...
    def SetValue(self, column: int, value: object) -> None: ...

class ICommandItem:
    """.NET: Eto.Forms.ICommandItem"""
    def __init__(self, *args) -> None: ...
    Text: str
    ToolTip: str
    Enabled: bool

class IContextMenuHost:
    """.NET: Eto.Forms.IContextMenuHost"""
    def __init__(self, *args) -> None: ...
    ContextMenu: ContextMenu

class IDataObject:
    """.NET: Eto.Forms.IDataObject"""
    def __init__(self, *args) -> None: ...
    Types: list
    ContainsText: bool
    ContainsHtml: bool
    ContainsImage: bool
    ContainsUris: bool
    Text: str
    Html: str
    Image: Image
    Uris: list
    def Clear(self, ) -> None: ...
    def Contains(self, type: str) -> bool: ...
    def GetData(self, type: str) -> list: ...
    def GetObject(self, type: str, objectType: Type) -> object: ...
    def GetString(self, type: str) -> str: ...
    def SetData(self, value: list, type: str) -> None: ...
    def SetObject(self, value: object, type: str) -> None: ...
    def SetString(self, value: str, type: str) -> None: ...

class IDataStore:
    """.NET: Eto.Forms.IDataStore`1"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: T

class IImageListItem:
    """.NET: Eto.Forms.IImageListItem"""
    def __init__(self, *args) -> None: ...
    Image: Image

class IIndirectBinding:
    """.NET: Eto.Forms.IIndirectBinding`1"""
    def __init__(self, *args) -> None: ...
    def GetValue(self, dataItem: object) -> T: ...
    def SetValue(self, dataItem: object, value: T) -> None: ...

class IKeyboardInputSource:
    """.NET: Eto.Forms.IKeyboardInputSource"""
    def __init__(self, *args) -> None: ...
    ...

class IListItem:
    """.NET: Eto.Forms.IListItem"""
    def __init__(self, *args) -> None: ...
    Text: str
    Key: str

class IMaskedTextProvider:
    """.NET: Eto.Forms.IMaskedTextProvider | Eto.Forms.IMaskedTextProvider`1"""
    def __init__(self, *args) -> None: ...
    DisplayText: str
    Text: str
    MaskCompleted: bool
    EditPositions: IEnumerable
    IsEmpty: bool
    Value: T
    def Clear(self, position: int, length: int, forward: bool) -> bool: ...
    def Delete(self, position: int, length: int, forward: bool) -> bool: ...
    def Insert(self, character: str, position: int) -> bool: ...
    def Replace(self, character: str, position: int) -> bool: ...

class IMnemonicControl:
    """.NET: Eto.Forms.IMnemonicControl"""
    def __init__(self, *args) -> None: ...
    Text: str
    UseMnemonic: bool
    AlwaysShowMnemonic: bool

class IMouseInputSource:
    """.NET: Eto.Forms.IMouseInputSource"""
    def __init__(self, *args) -> None: ...
    ...

class INavigationItem:
    """.NET: Eto.Forms.INavigationItem"""
    def __init__(self, *args) -> None: ...
    Content: Control

class ISelectable:
    """.NET: Eto.Forms.ISelectable`1"""
    def __init__(self, *args) -> None: ...
    SelectedItems: IEnumerable
    SelectedRows: IEnumerable
    def SelectAll(self, ) -> None: ...
    def SelectRow(self, row: int) -> None: ...
    def UnselectAll(self, ) -> None: ...
    def UnselectRow(self, row: int) -> None: ...

class ISelectableControl:
    """.NET: Eto.Forms.ISelectableControl`1"""
    def __init__(self, *args) -> None: ...
    SelectionPreserver: ISelectionPreserver

class ISelectionPreserver:
    """.NET: Eto.Forms.ISelectionPreserver"""
    def __init__(self, *args) -> None: ...
    SelectedItems: IEnumerable

class ISubmenu:
    """.NET: Eto.Forms.ISubmenu"""
    def __init__(self, *args) -> None: ...
    Items: MenuItemCollection
    Trim: bool

class ITextBuffer:
    """.NET: Eto.Forms.ITextBuffer"""
    def __init__(self, *args) -> None: ...
    SupportedFormats: IEnumerable
    def Clear(self, ) -> None: ...
    def Delete(self, range: Range) -> None: ...
    def Insert(self, position: int, text: str) -> None: ...
    def Load(self, stream: Stream, format: RichTextAreaFormat) -> None: ...
    def Save(self, stream: Stream, format: RichTextAreaFormat) -> None: ...
    def SetBackground(self, range: Range, color: Color) -> None: ...
    def SetBold(self, range: Range, bold: bool) -> None: ...
    def SetFamily(self, range: Range, family: FontFamily) -> None: ...
    def SetFont(self, range: Range, font: Font) -> None: ...
    def SetForeground(self, range: Range, color: Color) -> None: ...
    def SetItalic(self, range: Range, italic: bool) -> None: ...
    def SetStrikethrough(self, range: Range, strikethrough: bool) -> None: ...
    def SetUnderline(self, range: Range, underline: bool) -> None: ...

class ITreeGridItem:
    """.NET: Eto.Forms.ITreeGridItem | Eto.Forms.ITreeGridItem`1"""
    def __init__(self, *args) -> None: ...
    ...

class ITreeGridStore:
    """.NET: Eto.Forms.ITreeGridStore`1"""
    def __init__(self, *args) -> None: ...
    ...

class ITreeItem:
    """.NET: Eto.Forms.ITreeItem | Eto.Forms.ITreeItem`1"""
    def __init__(self, *args) -> None: ...
    Expanded: bool
    Expandable: bool
    Parent: T

class ITreeStore:
    """.NET: Eto.Forms.ITreeStore"""
    def __init__(self, *args) -> None: ...
    ...

class IValueCommand:
    """.NET: Eto.Forms.IValueCommand`1"""
    def __init__(self, *args) -> None: ...
    def GetValue(self, parameter: object) -> T: ...
    def SetValue(self, parameter: object, value: T) -> None: ...

class IValueConverter:
    """.NET: Eto.Forms.IValueConverter"""
    def __init__(self, *args) -> None: ...
    def Convert(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...
    def ConvertBack(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...

class ImageListItem(ListItem):
    """.NET: Eto.Forms.ImageListItem"""
    def __init__(self, *args) -> None: ...
    Image: Image
    Text: str
    Key: str
    Tag: object

class ImageTextCell(Cell):
    """.NET: Eto.Forms.ImageTextCell"""
    def __init__(self, *args) -> None: ...
    TextAlignment: TextAlignment
    VerticalAlignment: VerticalAlignment
    AutoSelectMode: AutoSelectMode
    ImageBinding: IIndirectBinding
    TextBinding: IIndirectBinding
    ImageInterpolation: ImageInterpolation
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool

class ImageView(Control):
    """.NET: Eto.Forms.ImageView"""
    def __init__(self, *args) -> None: ...
    Image: Image
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

class ImageViewCell(SingleValueCell):
    """.NET: Eto.Forms.ImageViewCell"""
    def __init__(self, *args) -> None: ...
    ImageInterpolation: ImageInterpolation
    Binding: IIndirectBinding
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool

class IndirectBinding(Binding):
    """.NET: Eto.Forms.IndirectBinding`1"""
    def __init__(self, *args) -> None: ...
    def AddValueChangedHandler(self, dataItem: object, handler: EventHandler) -> object: ...
    def AfterDelay(self, delay: TimeSpan, reset: bool) -> IndirectBinding: ...
    def Cast(self, ) -> IndirectBinding: ...
    def CatchException(self, exceptionHandler: Func) -> IndirectBinding: ...
    def Child(self, property: Expression) -> IndirectBinding: ...
    def Convert(self, converter: IValueConverter, propertyType: Type, conveterParameter: object, culture: CultureInfo) -> IndirectBinding: ...
    def EnumToString(self, defaultValue: T) -> IndirectBinding: ...
    def GetValue(self, dataItem: object) -> T: ...
    def OfType(self, defaultConvertedValue: TValue, defaultValue: T) -> IndirectBinding: ...
    def RemoveValueChangedHandler(self, bindingReference: object, handler: EventHandler) -> None: ...
    def SetValue(self, dataItem: object, value: T) -> None: ...
    def ToBool(self, trueValue: T, falseValue: T, nullValue: T) -> IndirectBinding: ...
    def ToType(self, invalidGetValue: Func, invalidSetValue: Func) -> IndirectBinding: ...

class InsertKeyMode:
    """.NET: Eto.Forms.InsertKeyMode"""
    def __init__(self, *args) -> None: ...
    ...

class KeyEventArgs(EventArgs):
    """.NET: Eto.Forms.KeyEventArgs"""
    def __init__(self, *args) -> None: ...
    KeyEventType: KeyEventType
    KeyData: Keys
    Key: Keys
    Modifiers: Keys
    IsChar: bool
    Handled: bool
    KeyChar: str
    Shift: bool
    Control: bool
    Alt: bool
    Application: bool
    def IsKeyDown(self, key: Keys, modifier: Nullable) -> bool: ...
    def IsKeyUp(self, key: Keys, modifier: Nullable) -> bool: ...

class KeyEventType:
    """.NET: Eto.Forms.KeyEventType"""
    def __init__(self, *args) -> None: ...
    ...

class Keyboard:
    """.NET: Eto.Forms.Keyboard"""
    def __init__(self, *args) -> None: ...
    SupportedLockKeys: IEnumerable
    Modifiers: Keys
    @staticmethod
    def IsKeyLocked(key: Keys) -> bool: ...

class Keys:
    """.NET: Eto.Forms.Keys"""
    def __init__(self, *args) -> None: ...
    ...

class KeysExtensions:
    """.NET: Eto.Forms.KeysExtensions"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def FromShortcutString(shortcutString: str) -> Keys: ...
    @staticmethod
    def ToShortcutString(key: Keys, separator: str) -> str: ...

class Label(TextControl):
    """.NET: Eto.Forms.Label"""
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

class Layout(Container):
    """.NET: Eto.Forms.Layout"""
    def __init__(self, *args) -> None: ...
    ClientSize: Size
    Controls: IEnumerable
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
    def BeginInit(self, ) -> None: ...
    def EndInit(self, ) -> None: ...
    def Update(self, ) -> None: ...

class LinkButton(TextControl):
    """.NET: Eto.Forms.LinkButton"""
    def __init__(self, *args) -> None: ...
    Command: ICommand
    CommandParameter: object
    DisabledTextColor: Color
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
    def Unbind(self, ) -> None: ...

class ListBox(ListControl):
    """.NET: Eto.Forms.ListBox"""
    def __init__(self, *args) -> None: ...
    ItemImageBinding: IIndirectBinding
    ImageBinding: IIndirectBinding
    ContextMenu: ContextMenu
    Border: BorderType
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

class ListControl(CommonControl):
    """.NET: Eto.Forms.ListControl"""
    def __init__(self, *args) -> None: ...
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

class ListItem:
    """.NET: Eto.Forms.ListItem"""
    def __init__(self, *args) -> None: ...
    Text: str
    Key: str
    Tag: object
    def ToString(self, ) -> str: ...

class ListItemCollection(ExtendedObservableCollection):
    """.NET: Eto.Forms.ListItemCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: IListItem
    def Add(self, text: str, key: str) -> None: ...

class LocalizeEventArgs(EventArgs):
    """.NET: Eto.Forms.LocalizeEventArgs"""
    def __init__(self, *args) -> None: ...
    Text: str
    LocalizedText: str
    Source: object

class MaskedTextBox(TextBox):
    """.NET: Eto.Forms.MaskedTextBox | Eto.Forms.MaskedTextBox`1"""
    def __init__(self, *args) -> None: ...
    Provider: IMaskedTextProvider
    InsertMode: InsertKeyMode
    IsOverwrite: bool
    ShowPromptOnFocus: bool
    ShowPromptMode: ShowPromptMode
    ShowPlaceholderWhenEmpty: bool
    Text: str
    MaskCompleted: bool
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
    Value: T
    ValueBinding: BindableBinding

class MaskedTextStepper(TextStepper):
    """.NET: Eto.Forms.MaskedTextStepper | Eto.Forms.MaskedTextStepper`1"""
    def __init__(self, *args) -> None: ...
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
    Value: T
    ValueBinding: BindableBinding

class Menu(BindableWidget):
    """.NET: Eto.Forms.Menu"""
    def __init__(self, *args) -> None: ...
    Parent: Widget
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

class MenuBar(Menu):
    """.NET: Eto.Forms.MenuBar"""
    def __init__(self, *args) -> None: ...
    Trim: bool
    IncludeSystemItems: MenuBarSystemItems
    SystemCommands: Collection
    Items: MenuItemCollection
    QuitItem: MenuItem
    AboutItem: MenuItem
    ApplicationMenu: ButtonMenuItem
    ApplicationItems: MenuItemCollection
    HelpMenu: ButtonMenuItem
    HelpItems: MenuItemCollection
    Parent: Widget
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

class MenuBarSystemItems:
    """.NET: Eto.Forms.MenuBarSystemItems"""
    def __init__(self, *args) -> None: ...
    ...

class MenuItem(Menu):
    """.NET: Eto.Forms.MenuItem"""
    def __init__(self, *args) -> None: ...
    Order: int
    Command: ICommand
    CommandParameter: object
    Text: str
    Tag: object
    ToolTip: str
    Enabled: bool
    Shortcut: Keys
    Visible: bool
    Parent: Widget
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
    def PerformClick(self, ) -> None: ...
    def PerformValidate(self, ) -> None: ...
    def Unbind(self, ) -> None: ...

class MenuItemCollection(Collection):
    """.NET: Eto.Forms.MenuItemCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: MenuItem
    def Add(self, command: Command, order: int) -> MenuItem: ...
    def AddRange(self, commands: IEnumerable, order: int) -> None: ...
    def AddSeparator(self, order: int) -> None: ...
    def GetSubmenu(self, submenuText: str, order: int, plaintextMatch: bool, create: bool) -> ButtonMenuItem: ...
    def Trim(self, ) -> None: ...

class MenuSegmentedItem(SegmentedItem):
    """.NET: Eto.Forms.MenuSegmentedItem"""
    def __init__(self, *args) -> None: ...
    CanSelect: bool
    Menu: ContextMenu
    Parent: SegmentedButton
    Text: str
    ToolTip: str
    Image: Image
    Enabled: bool
    Visible: bool
    Selected: bool
    Width: int
    Command: ICommand
    CommandParameter: object
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

class MessageBox:
    """.NET: Eto.Forms.MessageBox"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def Show(parent: Control, text: str, caption: str, buttons: MessageBoxButtons, type: MessageBoxType, defaultButton: MessageBoxDefaultButton) -> DialogResult: ...

class MessageBoxButtons:
    """.NET: Eto.Forms.MessageBoxButtons"""
    def __init__(self, *args) -> None: ...
    ...

class MessageBoxDefaultButton:
    """.NET: Eto.Forms.MessageBoxDefaultButton"""
    def __init__(self, *args) -> None: ...
    ...

class MessageBoxType:
    """.NET: Eto.Forms.MessageBoxType"""
    def __init__(self, *args) -> None: ...
    ...

class Mouse:
    """.NET: Eto.Forms.Mouse"""
    def __init__(self, *args) -> None: ...
    IsSupported: bool
    Position: PointF
    Buttons: MouseButtons
    @staticmethod
    def IsAnyButtonPressed(buttons: MouseButtons) -> bool: ...
    @staticmethod
    def SetCursor(cursor: Cursor) -> None: ...

class MouseButtons:
    """.NET: Eto.Forms.MouseButtons"""
    def __init__(self, *args) -> None: ...
    ...

class MouseEventArgs(EventArgs):
    """.NET: Eto.Forms.MouseEventArgs"""
    def __init__(self, *args) -> None: ...
    Modifiers: Keys
    Buttons: MouseButtons
    Location: PointF
    Handled: bool
    Pressure: float
    Delta: SizeF

class NativeControlHost(Control):
    """.NET: Eto.Forms.NativeControlHost"""
    def __init__(self, *args) -> None: ...
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

class Navigation(Container):
    """.NET: Eto.Forms.Navigation"""
    def __init__(self, *args) -> None: ...
    Controls: IEnumerable
    IsSupported: bool
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
    def Pop(self, ) -> None: ...
    def Push(self, content: Control, title: str) -> None: ...
    def Remove(self, child: Control) -> None: ...

class NavigationItem(ListItem):
    """.NET: Eto.Forms.NavigationItem"""
    def __init__(self, *args) -> None: ...
    Content: Control
    Text: str
    Key: str
    Tag: object

class NavigationItemEventArgs(EventArgs):
    """.NET: Eto.Forms.NavigationItemEventArgs"""
    def __init__(self, *args) -> None: ...
    Item: INavigationItem

class Notification(Widget):
    """.NET: Eto.Forms.Notification"""
    def __init__(self, *args) -> None: ...
    Icon: Icon
    ContentImage: Image
    Message: str
    RequiresTrayIndicator: bool
    Title: str
    UserData: str
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    def Show(self, indicator: TrayIndicator) -> None: ...

class NotificationEventArgs(EventArgs):
    """.NET: Eto.Forms.NotificationEventArgs"""
    def __init__(self, *args) -> None: ...
    ID: str
    UserData: str

class NumericMaskedTextBox(MaskedTextBox):
    """.NET: Eto.Forms.NumericMaskedTextBox`1"""
    def __init__(self, *args) -> None: ...
    Provider: NumericMaskedTextProvider
    AllowSign: bool
    AllowDecimal: bool
    Culture: CultureInfo
    Value: T
    ValueBinding: BindableBinding
    InsertMode: InsertKeyMode
    IsOverwrite: bool
    ShowPromptOnFocus: bool
    ShowPromptMode: ShowPromptMode
    ShowPlaceholderWhenEmpty: bool
    Text: str
    MaskCompleted: bool
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

class NumericMaskedTextProvider(VariableMaskedTextProvider):
    """.NET: Eto.Forms.NumericMaskedTextProvider | Eto.Forms.NumericMaskedTextProvider`1"""
    def __init__(self, *args) -> None: ...
    AllowDecimal: bool
    AllowSign: bool
    SignCharacters: list
    Validate: Func
    DecimalCharacter: str
    AltDecimalCharacters: list
    Culture: CultureInfo
    MaskCompleted: bool
    DisplayText: str
    Text: str
    EditPositions: IEnumerable
    IsEmpty: bool
    Value: T
    def Insert(self, character: str, position: int) -> bool: ...
    def Replace(self, character: str, position: int) -> bool: ...

class NumericMaskedTextStepper(MaskedTextStepper):
    """.NET: Eto.Forms.NumericMaskedTextStepper`1"""
    def __init__(self, *args) -> None: ...
    Provider: NumericMaskedTextProvider
    AllowSign: bool
    AllowDecimal: bool
    Culture: CultureInfo
    Value: T
    ValueBinding: BindableBinding
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

class NumericStepper(CommonControl):
    """.NET: Eto.Forms.NumericStepper"""
    def __init__(self, *args) -> None: ...
    ReadOnly: bool
    Value: float
    MinValue: float
    MaxValue: float
    TextColor: Color
    DecimalPlaces: int
    Increment: float
    MaximumDecimalPlaces: int
    FormatString: str
    CultureInfo: CultureInfo
    Wrap: bool
    ValueBinding: BindableBinding
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

class NumericUpDown(NumericStepper):
    """.NET: Eto.Forms.NumericUpDown"""
    def __init__(self, *args) -> None: ...
    ReadOnly: bool
    Value: float
    MinValue: float
    MaxValue: float
    TextColor: Color
    DecimalPlaces: int
    Increment: float
    MaximumDecimalPlaces: int
    FormatString: str
    CultureInfo: CultureInfo
    Wrap: bool
    ValueBinding: BindableBinding
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

class ObjectBinding:
    """.NET: Eto.Forms.ObjectBinding`1 | Eto.Forms.ObjectBinding`2"""
    def __init__(self, *args) -> None: ...
    InnerBinding: IndirectBinding
    DataItem: object
    GetDataItem: Func
    SettingNullValue: TValue
    GettingNullValue: TValue
    DataValue: TValue
    def Bind(self, getValue: Func, setValue: Action, addChangeEvent: Action, removeChangeEvent: Action, mode: DualBindingMode) -> DualBinding: ...
    def ToString(self, ) -> str: ...
    def TriggerDataValueChanged(self, ) -> None: ...
    def Unbind(self, ) -> None: ...

class OpenFileDialog(FileDialog):
    """.NET: Eto.Forms.OpenFileDialog"""
    def __init__(self, *args) -> None: ...
    MultiSelect: bool
    Filenames: IEnumerable
    FileName: str
    Filters: Collection
    CurrentFilterIndex: int
    CurrentFilter: FileFilter
    CheckFileExists: bool
    Title: str
    Directory: Uri
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool

class OpenWithDialog(CommonDialog):
    """.NET: Eto.Forms.OpenWithDialog"""
    def __init__(self, *args) -> None: ...
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool

class Orientation:
    """.NET: Eto.Forms.Orientation"""
    def __init__(self, *args) -> None: ...
    ...

class PageOrientation:
    """.NET: Eto.Forms.PageOrientation"""
    def __init__(self, *args) -> None: ...
    ...

class PageSettings(Widget):
    """.NET: Eto.Forms.PageSettings"""
    def __init__(self, *args) -> None: ...
    PrintableArea: RectangleF
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool

class PaintEventArgs(EventArgs):
    """.NET: Eto.Forms.PaintEventArgs"""
    def __init__(self, *args) -> None: ...
    Graphics: Graphics
    ClipRectangle: RectangleF

class Panel(Container):
    """.NET: Eto.Forms.Panel"""
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
    def Remove(self, child: Control) -> None: ...

class PasswordBox(TextControl):
    """.NET: Eto.Forms.PasswordBox"""
    def __init__(self, *args) -> None: ...
    ReadOnly: bool
    MaxLength: int
    PasswordChar: str
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

class PixelLayout(Layout):
    """.NET: Eto.Forms.PixelLayout"""
    def __init__(self, *args) -> None: ...
    Controls: IEnumerable
    Contents: List
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
    def Add(self, control: Control, x: int, y: int) -> None: ...
    def EndInit(self, ) -> None: ...
    @staticmethod
    def GetLocation(control: Control) -> Point: ...
    def Move(self, control: Control, x: int, y: int) -> None: ...
    def Remove(self, child: Control) -> None: ...
    @staticmethod
    def SetLocation(control: Control, value: Point) -> None: ...

class PrintDialog(CommonDialog):
    """.NET: Eto.Forms.PrintDialog"""
    def __init__(self, *args) -> None: ...
    PrintSettings: PrintSettings
    AllowSelection: bool
    AllowPageRange: bool
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    def ShowDialog(self, parent: Control, document: PrintDocument) -> DialogResult: ...

class PrintDocument(Widget):
    """.NET: Eto.Forms.PrintDocument"""
    def __init__(self, *args) -> None: ...
    Name: str
    PrintSettings: PrintSettings
    PageCount: int
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    def Print(self, ) -> None: ...

class PrintPageEventArgs(EventArgs):
    """.NET: Eto.Forms.PrintPageEventArgs"""
    def __init__(self, *args) -> None: ...
    Graphics: Graphics
    PageSize: SizeF
    CurrentPage: int

class PrintPreviewDialog(CommonDialog):
    """.NET: Eto.Forms.PrintPreviewDialog"""
    def __init__(self, *args) -> None: ...
    Document: PrintDocument
    PrintSettings: PrintSettings
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    def ShowDialog(self, parent: Window) -> DialogResult: ...

class PrintSelection:
    """.NET: Eto.Forms.PrintSelection"""
    def __init__(self, *args) -> None: ...
    ...

class PrintSettings(Widget):
    """.NET: Eto.Forms.PrintSettings"""
    def __init__(self, *args) -> None: ...
    Copies: int
    MaximumPageRange: Range
    SelectedPageRange: Range
    Orientation: PageOrientation
    PrintSelection: PrintSelection
    Collate: bool
    Reverse: bool
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool

class ProgressBar(Control):
    """.NET: Eto.Forms.ProgressBar"""
    def __init__(self, *args) -> None: ...
    MaxValue: int
    MinValue: int
    Value: int
    Indeterminate: bool
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

class ProgressCell(SingleValueCell):
    """.NET: Eto.Forms.ProgressCell"""
    def __init__(self, *args) -> None: ...
    Binding: IIndirectBinding
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool

class PropertyBinding(IndirectBinding):
    """.NET: Eto.Forms.PropertyBinding`1"""
    def __init__(self, *args) -> None: ...
    Property: str
    IgnoreCase: bool
    def AddValueChangedHandler(self, dataItem: object, handler: EventHandler) -> object: ...
    def RemoveValueChangedHandler(self, bindingReference: object, handler: EventHandler) -> None: ...
    def ToString(self, ) -> str: ...

class PropertyBindingException(Exception):
    """.NET: Eto.Forms.PropertyBindingException"""
    def __init__(self, *args) -> None: ...
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str

class PropertyCell(CustomCell):
    """.NET: Eto.Forms.PropertyCell"""
    def __init__(self, *args) -> None: ...
    TypeBinding: IIndirectBinding
    Types: IList
    CreateCell: Func
    GetIdentifier: Func
    GetPreferredWidth: Func
    ConfigureCell: Action
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool

class PropertyCellType:
    """.NET: Eto.Forms.PropertyCellType | Eto.Forms.PropertyCellType`1"""
    def __init__(self, *args) -> None: ...
    Identifier: str
    ItemBinding: IndirectBinding
    def CanDisplay(self, itemType: object) -> bool: ...
    def OnConfigure(self, args: CellEventArgs, control: Control) -> None: ...
    def OnCreate(self, args: CellEventArgs) -> Control: ...
    def OnPaint(self, args: CellPaintEventArgs) -> None: ...

class PropertyCellTypeBoolean(PropertyCellType):
    """.NET: Eto.Forms.PropertyCellTypeBoolean"""
    def __init__(self, *args) -> None: ...
    ItemThreeStateBinding: IndirectBinding
    Identifier: str
    ItemBinding: IndirectBinding
    def OnCreate(self, args: CellEventArgs) -> Control: ...
    def OnPaint(self, args: CellPaintEventArgs) -> None: ...

class PropertyCellTypeColor(PropertyCellType):
    """.NET: Eto.Forms.PropertyCellTypeColor"""
    def __init__(self, *args) -> None: ...
    ShowHex: bool
    ShowAlpha: bool
    HexEditable: bool
    Identifier: str
    ItemBinding: IndirectBinding
    def OnCreate(self, args: CellEventArgs) -> Control: ...
    def OnPaint(self, args: CellPaintEventArgs) -> None: ...

class PropertyCellTypeDateTime(PropertyCellType):
    """.NET: Eto.Forms.PropertyCellTypeDateTime"""
    def __init__(self, *args) -> None: ...
    Mode: DateTimePickerMode
    Identifier: str
    ItemBinding: IndirectBinding
    def OnCreate(self, args: CellEventArgs) -> Control: ...
    def OnPaint(self, args: CellPaintEventArgs) -> None: ...

class PropertyCellTypeDropDown(PropertyCellType):
    """.NET: Eto.Forms.PropertyCellTypeDropDown"""
    def __init__(self, *args) -> None: ...
    ItemsBinding: IndirectBinding
    ItemTextBinding: IndirectBinding
    ItemKeyBinding: IndirectBinding
    Identifier: str
    ItemBinding: IndirectBinding
    def OnCreate(self, args: CellEventArgs) -> Control: ...
    def OnPaint(self, args: CellPaintEventArgs) -> None: ...

class PropertyCellTypeEnum(PropertyCellType):
    """.NET: Eto.Forms.PropertyCellTypeEnum | Eto.Forms.PropertyCellTypeEnum`1"""
    def __init__(self, *args) -> None: ...
    Identifier: str
    ItemTypeBinding: IndirectBinding
    ItemBinding: IndirectBinding
    def CanDisplay(self, itemType: object) -> bool: ...
    def OnConfigure(self, args: CellEventArgs, control: Control) -> None: ...
    def OnCreate(self, args: CellEventArgs) -> Control: ...
    def OnPaint(self, args: CellPaintEventArgs) -> None: ...

class PropertyCellTypeNumber(PropertyCellType):
    """.NET: Eto.Forms.PropertyCellTypeNumber | Eto.Forms.PropertyCellTypeNumber`1"""
    def __init__(self, *args) -> None: ...
    Identifier: str
    ItemTypeBinding: IndirectBinding
    ItemBinding: IndirectBinding
    def CanDisplay(self, itemType: object) -> bool: ...
    def OnConfigure(self, args: CellEventArgs, control: Control) -> None: ...
    def OnCreate(self, args: CellEventArgs) -> Control: ...
    def OnPaint(self, args: CellPaintEventArgs) -> None: ...

class PropertyCellTypeString(PropertyCellType):
    """.NET: Eto.Forms.PropertyCellTypeString"""
    def __init__(self, *args) -> None: ...
    Identifier: str
    ItemBinding: IndirectBinding
    def OnCreate(self, args: CellEventArgs) -> Control: ...
    def OnPaint(self, args: CellPaintEventArgs) -> None: ...

class PropertyGrid(Control):
    """.NET: Eto.Forms.PropertyGrid"""
    def __init__(self, *args) -> None: ...
    SelectedObject: object
    SelectedObjects: IEnumerable
    ShowCategories: bool
    ShowDescription: bool
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

class PropertyGridTypeEditor:
    """.NET: Eto.Forms.PropertyGridTypeEditor"""
    def __init__(self, *args) -> None: ...
    def CreateControl(self, args: CellEventArgs) -> Control: ...
    def PaintCell(self, args: CellPaintEventArgs) -> None: ...

class PropertyValueChangedEventArgs(EventArgs):
    """.NET: Eto.Forms.PropertyValueChangedEventArgs"""
    def __init__(self, *args) -> None: ...
    OldValue: object
    PropertyName: str
    Item: object

class RadioButton(TextControl):
    """.NET: Eto.Forms.RadioButton"""
    def __init__(self, *args) -> None: ...
    Command: ICommand
    CommandParameter: object
    Checked: bool
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
    def Unbind(self, ) -> None: ...

class RadioButtonList(Panel):
    """.NET: Eto.Forms.RadioButtonList"""
    def __init__(self, *args) -> None: ...
    ItemTextBinding: IIndirectBinding
    ItemKeyBinding: IIndirectBinding
    ItemToolTipBinding: IIndirectBinding
    TextBinding: IIndirectBinding
    KeyBinding: IIndirectBinding
    SelectedKey: str
    Enabled: bool
    SelectedValue: object
    SelectedIndex: int
    TextColor: Color
    Orientation: Orientation
    Spacing: Size
    Items: ListItemCollection
    DataStore: IEnumerable
    SelectedValueBinding: BindableBinding
    SelectedIndexBinding: BindableBinding
    SelectedKeyBinding: BindableBinding
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

class RadioButtonListOrientation:
    """.NET: Eto.Forms.RadioButtonListOrientation"""
    def __init__(self, *args) -> None: ...
    Horizontal: RadioButtonListOrientation
    Vertical: RadioButtonListOrientation
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class RadioCommand(CheckCommand):
    """.NET: Eto.Forms.RadioCommand"""
    def __init__(self, *args) -> None: ...
    Controller: RadioCommand
    Checked: bool
    ID: str
    Enabled: bool
    Tag: object
    MenuText: str
    ToolBarText: str
    ToolTip: str
    Image: Image
    Shortcut: Keys
    Properties: PropertyStore
    DelegatedCommand: ICommand
    CommandParameter: object
    Parent: IBindable
    DataContext: object
    IsDataContextChanging: bool
    Bindings: BindingCollection
    def CreateMenuItem(self, ) -> MenuItem: ...
    def CreateToolItem(self, ) -> ToolItem: ...

class RadioMenuItem(MenuItem):
    """.NET: Eto.Forms.RadioMenuItem"""
    def __init__(self, *args) -> None: ...
    Checked: bool
    Order: int
    Command: ICommand
    CommandParameter: object
    Text: str
    Tag: object
    ToolTip: str
    Enabled: bool
    Shortcut: Keys
    Visible: bool
    Parent: Widget
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
    def PerformClick(self, ) -> None: ...

class RadioToolItem(ToolItem):
    """.NET: Eto.Forms.RadioToolItem"""
    def __init__(self, *args) -> None: ...
    Checked: bool
    Command: ICommand
    CommandParameter: object
    Order: int
    Text: str
    ToolTip: str
    Image: Image
    Enabled: bool
    Visible: bool
    Tag: object
    Parent: Widget
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
    def OnCheckedChanged(self, e: EventArgs) -> None: ...

class Range:
    """.NET: Eto.Forms.Range | Eto.Forms.Range`1"""
    def __init__(self, *args) -> None: ...
    Start: T
    End: T
    def Contains(self, value: T) -> bool: ...
    def Equals(self, obj: object) -> bool: ...
    @staticmethod
    def FromLength(start: int, length: int) -> Range: ...
    def GetHashCode(self, ) -> int: ...
    def Intersect(self, range: Range) -> Nullable: ...
    def Intersects(self, range: Range) -> bool: ...
    def Iterate(self, increment: Func) -> IEnumerable: ...
    def ToString(self, ) -> str: ...
    def Touches(self, range: Range, increment: Func) -> bool: ...
    def Union(self, range: Range, increment: Func) -> Nullable: ...
    def WithEnd(self, end: T) -> Range: ...
    def WithStart(self, start: T) -> Range: ...

class RangeExtensions:
    """.NET: Eto.Forms.RangeExtensions"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def Interval(range: Range) -> TimeSpan: ...
    @staticmethod
    def Length(range: Range) -> int: ...
    @staticmethod
    def WithLength(range: Range, length: int) -> Range: ...

class RelayCommand:
    """.NET: Eto.Forms.RelayCommand | Eto.Forms.RelayCommand`1"""
    def __init__(self, *args) -> None: ...
    def CanExecute(self, parameter: object) -> bool: ...
    def Execute(self, parameter: object) -> None: ...
    def UpdateCanExecute(self, ) -> None: ...

class RelayValueCommand:
    """.NET: Eto.Forms.RelayValueCommand`1 | Eto.Forms.RelayValueCommand`2"""
    def __init__(self, *args) -> None: ...
    def GetValue(self, parameter: object) -> TValue: ...
    def SetValue(self, parameter: object, value: TValue) -> None: ...
    def UpdateValue(self, ) -> None: ...

class RichTextArea(TextArea):
    """.NET: Eto.Forms.RichTextArea"""
    def __init__(self, *args) -> None: ...
    SelectionFont: Font
    SelectionForeground: Color
    SelectionBackground: Color
    SelectionBold: bool
    SelectionItalic: bool
    SelectionUnderline: bool
    SelectionStrikethrough: bool
    SelectionFamily: FontFamily
    SelectionTypeface: FontTypeface
    Buffer: ITextBuffer
    Rtf: str
    ReadOnly: bool
    Wrap: bool
    SelectedText: str
    Selection: Range
    CaretIndex: int
    AcceptsTab: bool
    AcceptsReturn: bool
    TextAlignment: TextAlignment
    HorizontalAlign: HorizontalAlign
    SpellCheck: bool
    SpellCheckIsSupported: bool
    TextReplacements: TextReplacements
    SupportedTextReplacements: TextReplacements
    Border: BorderType
    TextLength: int
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

class RichTextAreaFormat:
    """.NET: Eto.Forms.RichTextAreaFormat"""
    def __init__(self, *args) -> None: ...
    ...

class SaveFileDialog(FileDialog):
    """.NET: Eto.Forms.SaveFileDialog"""
    def __init__(self, *args) -> None: ...
    FileName: str
    Filters: Collection
    CurrentFilterIndex: int
    CurrentFilter: FileFilter
    CheckFileExists: bool
    Title: str
    Directory: Uri
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool

class Screen(Widget):
    """.NET: Eto.Forms.Screen"""
    def __init__(self, *args) -> None: ...
    Screens: IEnumerable
    DisplayBounds: RectangleF
    PrimaryScreen: Screen
    DPI: float
    Scale: float
    RealDPI: float
    RealScale: float
    Bounds: RectangleF
    WorkingArea: RectangleF
    BitsPerPixel: int
    IsPrimary: bool
    LogicalPixelSize: float
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    @staticmethod
    def FromPoint(point: PointF) -> Screen: ...
    @staticmethod
    def FromRectangle(rectangle: RectangleF) -> Screen: ...
    def GetImage(self, rect: RectangleF) -> Image: ...

class ScrollEventArgs(EventArgs):
    """.NET: Eto.Forms.ScrollEventArgs"""
    def __init__(self, *args) -> None: ...
    ScrollPosition: Point

class Scrollable(Panel):
    """.NET: Eto.Forms.Scrollable"""
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
    def UpdateScrollSizes(self, ) -> None: ...

class SearchBox(TextBox):
    """.NET: Eto.Forms.SearchBox"""
    def __init__(self, *args) -> None: ...
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

class SegmentedButton(Control):
    """.NET: Eto.Forms.SegmentedButton"""
    def __init__(self, *args) -> None: ...
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
    def ClearSelection(self, ) -> None: ...
    def SelectAll(self, ) -> None: ...

class SegmentedItem(BindableWidget):
    """.NET: Eto.Forms.SegmentedItem"""
    def __init__(self, *args) -> None: ...
    Parent: SegmentedButton
    Text: str
    ToolTip: str
    Image: Image
    Enabled: bool
    Visible: bool
    Selected: bool
    Width: int
    Command: ICommand
    CommandParameter: object
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
    def Unbind(self, ) -> None: ...

class SegmentedItemClickEventArgs(EventArgs):
    """.NET: Eto.Forms.SegmentedItemClickEventArgs"""
    def __init__(self, *args) -> None: ...
    Item: SegmentedItem
    Index: int

class SegmentedItemCollection(ObservableCollection):
    """.NET: Eto.Forms.SegmentedItemCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: SegmentedItem
    def AddRange(self, items: IEnumerable) -> None: ...

class SegmentedSelectionMode:
    """.NET: Eto.Forms.SegmentedSelectionMode"""
    def __init__(self, *args) -> None: ...
    ...

class SelectFolderDialog(CommonDialog):
    """.NET: Eto.Forms.SelectFolderDialog"""
    def __init__(self, *args) -> None: ...
    Title: str
    Directory: str
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool

class SelectableFilterCollection(FilterCollection):
    """.NET: Eto.Forms.SelectableFilterCollection`1"""
    def __init__(self, *args) -> None: ...
    Parent: ISelectableControl
    SelectedItems: IEnumerable
    SelectedRows: IEnumerable
    Change: Func
    Filter: Func
    Sort: Comparison
    Item: T
    Count: int
    IsReadOnly: bool
    def Clear(self, ) -> None: ...
    def Remove(self, item: T) -> bool: ...
    def RemoveAt(self, index: int) -> None: ...
    def SelectAll(self, ) -> None: ...
    def SelectRow(self, row: int) -> None: ...
    def UnselectAll(self, ) -> None: ...
    def UnselectRow(self, row: int) -> None: ...

class SeparatorMenuItem(MenuItem):
    """.NET: Eto.Forms.SeparatorMenuItem"""
    def __init__(self, *args) -> None: ...
    Order: int
    Command: ICommand
    CommandParameter: object
    Text: str
    Tag: object
    ToolTip: str
    Enabled: bool
    Shortcut: Keys
    Visible: bool
    Parent: Widget
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

class SeparatorToolItem(ToolItem):
    """.NET: Eto.Forms.SeparatorToolItem"""
    def __init__(self, *args) -> None: ...
    Type: SeparatorToolItemType
    Command: ICommand
    CommandParameter: object
    Order: int
    Text: str
    ToolTip: str
    Image: Image
    Enabled: bool
    Visible: bool
    Tag: object
    Parent: Widget
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

class SeparatorToolItemType:
    """.NET: Eto.Forms.SeparatorToolItemType"""
    def __init__(self, *args) -> None: ...
    ...

class ShowPromptMode:
    """.NET: Eto.Forms.ShowPromptMode"""
    def __init__(self, *args) -> None: ...
    ...

class SingleValueCell(Cell):
    """.NET: Eto.Forms.SingleValueCell`1"""
    def __init__(self, *args) -> None: ...
    Binding: IIndirectBinding
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool

class Slider(Control):
    """.NET: Eto.Forms.Slider"""
    def __init__(self, *args) -> None: ...
    TickFrequency: int
    SnapToTick: bool
    MaxValue: int
    MinValue: int
    Value: int
    ValueBinding: BindableBinding
    Orientation: Orientation
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

class SliderOrientation:
    """.NET: Eto.Forms.SliderOrientation"""
    def __init__(self, *args) -> None: ...
    Horizontal: SliderOrientation
    Vertical: SliderOrientation
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class Spinner(Control):
    """.NET: Eto.Forms.Spinner"""
    def __init__(self, *args) -> None: ...
    Enabled: bool
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

class Splitter(Container):
    """.NET: Eto.Forms.Splitter"""
    def __init__(self, *args) -> None: ...
    Controls: IEnumerable
    IsSupported: bool
    Orientation: Orientation
    FixedPanel: SplitterFixedPanel
    Position: int
    RelativePosition: float
    SplitterWidth: int
    Panel1: Control
    Panel1MinimumSize: int
    Panel2: Control
    Panel2MinimumSize: int
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
    def Remove(self, child: Control) -> None: ...

class SplitterFixedPanel:
    """.NET: Eto.Forms.SplitterFixedPanel"""
    def __init__(self, *args) -> None: ...
    ...

class SplitterOrientation:
    """.NET: Eto.Forms.SplitterOrientation"""
    def __init__(self, *args) -> None: ...
    Horizontal: SplitterOrientation
    Vertical: SplitterOrientation
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class SplitterPositionChangingEventArgs(CancelEventArgs):
    """.NET: Eto.Forms.SplitterPositionChangingEventArgs"""
    def __init__(self, *args) -> None: ...
    NewPosition: int
    Cancel: bool

class StackLayout(Panel):
    """.NET: Eto.Forms.StackLayout"""
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
    def ResumeLayout(self, ) -> None: ...
    def SuspendLayout(self, ) -> None: ...

class StackLayoutItem:
    """.NET: Eto.Forms.StackLayoutItem"""
    def __init__(self, *args) -> None: ...
    Control: Control
    HorizontalAlignment: Nullable
    VerticalAlignment: Nullable
    Expand: bool

class Stepper(Control):
    """.NET: Eto.Forms.Stepper"""
    def __init__(self, *args) -> None: ...
    ValidDirection: StepperValidDirections
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

class StepperDirection:
    """.NET: Eto.Forms.StepperDirection"""
    def __init__(self, *args) -> None: ...
    ...

class StepperEventArgs(EventArgs):
    """.NET: Eto.Forms.StepperEventArgs"""
    def __init__(self, *args) -> None: ...
    Direction: StepperDirection

class StepperValidDirections:
    """.NET: Eto.Forms.StepperValidDirections"""
    def __init__(self, *args) -> None: ...
    ...

class SubMenuItem(ButtonMenuItem):
    """.NET: Eto.Forms.SubMenuItem"""
    def __init__(self, *args) -> None: ...
    Items: MenuItemCollection
    Trim: bool
    Image: Image
    Order: int
    Command: ICommand
    CommandParameter: object
    Text: str
    Tag: object
    ToolTip: str
    Enabled: bool
    Shortcut: Keys
    Visible: bool
    Parent: Widget
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

class SubmenuExtensions:
    """.NET: Eto.Forms.SubmenuExtensions"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetChildren(submenu: ISubmenu) -> IEnumerable: ...

class TabControl(Container):
    """.NET: Eto.Forms.TabControl"""
    def __init__(self, *args) -> None: ...
    Controls: IEnumerable
    SelectedIndex: int
    SelectedPage: TabPage
    Pages: Collection
    TabPosition: DockPosition
    SelectedIndexBinding: BindableBinding
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
    def Remove(self, child: Control) -> None: ...

class TabPage(Panel):
    """.NET: Eto.Forms.TabPage"""
    def __init__(self, *args) -> None: ...
    Text: str
    Image: Image
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

class TableCell:
    """.NET: Eto.Forms.TableCell"""
    def __init__(self, *args) -> None: ...
    ScaleWidth: bool
    Control: Control

class TableLayout(Layout):
    """.NET: Eto.Forms.TableLayout"""
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
    def Add(self, control: Control, x: int, y: int, xscale: bool, yscale: bool) -> None: ...
    @staticmethod
    def AutoSized(control: Control, padding: Nullable, centered: bool) -> TableLayout: ...
    def EndInit(self, ) -> None: ...
    def GetColumnScale(self, column: int) -> bool: ...
    def GetRowScale(self, row: int) -> bool: ...
    @staticmethod
    def Horizontal(spacing: int, cells: list) -> TableLayout: ...
    @staticmethod
    def HorizontalScaled(spacing: int, cells: list) -> TableLayout: ...
    def Move(self, control: Control, x: int, y: int) -> None: ...
    def Remove(self, child: Control) -> None: ...
    def SetColumnScale(self, column: int, scale: bool) -> None: ...
    def SetRowScale(self, row: int, scale: bool) -> None: ...

class TableRow:
    """.NET: Eto.Forms.TableRow"""
    def __init__(self, *args) -> None: ...
    ScaleHeight: bool
    Cells: Collection
    @staticmethod
    def Scaled(cells: list) -> TableRow: ...

class Taskbar:
    """.NET: Eto.Forms.Taskbar"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def SetProgress(state: TaskbarProgressState, progress: float) -> None: ...

class TaskbarProgressState:
    """.NET: Eto.Forms.TaskbarProgressState"""
    def __init__(self, *args) -> None: ...
    ...

class TextAlignment:
    """.NET: Eto.Forms.TextAlignment"""
    def __init__(self, *args) -> None: ...
    ...

class TextArea(TextControl):
    """.NET: Eto.Forms.TextArea"""
    def __init__(self, *args) -> None: ...
    ReadOnly: bool
    Wrap: bool
    SelectedText: str
    Selection: Range
    CaretIndex: int
    AcceptsTab: bool
    AcceptsReturn: bool
    TextAlignment: TextAlignment
    HorizontalAlign: HorizontalAlign
    SpellCheck: bool
    SpellCheckIsSupported: bool
    TextReplacements: TextReplacements
    SupportedTextReplacements: TextReplacements
    Border: BorderType
    TextLength: int
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
    def Append(self, text: str, scrollToCursor: bool) -> None: ...
    def ScrollTo(self, range: Range) -> None: ...
    def ScrollToEnd(self, ) -> None: ...
    def ScrollToStart(self, ) -> None: ...
    def SelectAll(self, ) -> None: ...

class TextBox(TextControl):
    """.NET: Eto.Forms.TextBox"""
    def __init__(self, *args) -> None: ...
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
    def SelectAll(self, ) -> None: ...

class TextBoxCell(SingleValueCell):
    """.NET: Eto.Forms.TextBoxCell"""
    def __init__(self, *args) -> None: ...
    TextAlignment: TextAlignment
    VerticalAlignment: VerticalAlignment
    AutoSelectMode: AutoSelectMode
    Binding: IIndirectBinding
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool

class TextBufferExtensions:
    """.NET: Eto.Forms.TextBufferExtensions"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetRtf(buffer: ITextBuffer) -> str: ...
    @staticmethod
    def SetRtf(buffer: ITextBuffer, rtf: str) -> None: ...

class TextChangingEventArgs(CancelEventArgs):
    """.NET: Eto.Forms.TextChangingEventArgs"""
    def __init__(self, *args) -> None: ...
    Text: str
    Range: Range
    OldText: str
    NewText: str
    FromUser: bool
    Cancel: bool

class TextControl(CommonControl):
    """.NET: Eto.Forms.TextControl"""
    def __init__(self, *args) -> None: ...
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

class TextInputEventArgs(CancelEventArgs):
    """.NET: Eto.Forms.TextInputEventArgs"""
    def __init__(self, *args) -> None: ...
    Text: str
    Cancel: bool

class TextReplacements:
    """.NET: Eto.Forms.TextReplacements"""
    def __init__(self, *args) -> None: ...
    ...

class TextStepper(TextBox):
    """.NET: Eto.Forms.TextStepper"""
    def __init__(self, *args) -> None: ...
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

class ThemedContainerHandler(ThemedControlHandler):
    """.NET: Eto.Forms.ThemedContainerHandler`3"""
    def __init__(self, *args) -> None: ...
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
    Callback: TCallback
    Control: TControl
    HasControl: bool
    Widget: TWidget
    ID: str
    NativeHandle: IntPtr

class ThemedControlHandler(WidgetHandler):
    """.NET: Eto.Forms.ThemedControlHandler`3"""
    def __init__(self, *args) -> None: ...
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
    Callback: TCallback
    Control: TControl
    HasControl: bool
    Widget: TWidget
    ID: str
    NativeHandle: IntPtr
    def AttachEvent(self, id: str) -> None: ...
    def CaptureMouse(self, ) -> bool: ...
    def DoDragDrop(self, data: DataObject, allowedAction: DragEffects, image: Image, cursorOffset: PointF) -> None: ...
    def Focus(self, ) -> None: ...
    def GetNativeParentWindow(self, ) -> Window: ...
    def GetPreferredSize(self, availableSize: SizeF) -> SizeF: ...
    def Invalidate(self, rect: Rectangle, invalidateChildren: bool) -> None: ...
    def MapPlatformCommand(self, systemAction: str, action: Command) -> None: ...
    def OnLoad(self, e: EventArgs) -> None: ...
    def OnLoadComplete(self, e: EventArgs) -> None: ...
    def OnPreLoad(self, e: EventArgs) -> None: ...
    def OnUnLoad(self, e: EventArgs) -> None: ...
    def PointFromScreen(self, point: PointF) -> PointF: ...
    def PointToScreen(self, point: PointF) -> PointF: ...
    def Print(self, ) -> None: ...
    def ReleaseMouseCapture(self, ) -> None: ...
    def ResumeLayout(self, ) -> None: ...
    def SetParent(self, oldParent: Container, newParent: Container) -> None: ...
    def SuspendLayout(self, ) -> None: ...
    def UpdateLayout(self, ) -> None: ...

class ToggleButton(Button):
    """.NET: Eto.Forms.ToggleButton"""
    def __init__(self, *args) -> None: ...
    Checked: bool
    Command: ICommand
    CommandParameter: object
    Image: Image
    ImagePosition: ButtonImagePosition
    MinimumSize: Size
    Size: Size
    Width: int
    Height: int
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
    IsMouseCaptured: bool
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
    def PerformClick(self, ) -> None: ...

class Tool(BindableWidget):
    """.NET: Eto.Forms.Tool"""
    def __init__(self, *args) -> None: ...
    Parent: Widget
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

class ToolBar(Tool):
    """.NET: Eto.Forms.ToolBar"""
    def __init__(self, *args) -> None: ...
    Dock: ToolBarDock
    Items: ToolItemCollection
    TextAlign: ToolBarTextAlign
    Parent: Widget
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

class ToolBarDock:
    """.NET: Eto.Forms.ToolBarDock"""
    def __init__(self, *args) -> None: ...
    ...

class ToolBarTextAlign:
    """.NET: Eto.Forms.ToolBarTextAlign"""
    def __init__(self, *args) -> None: ...
    ...

class ToolItem(Tool):
    """.NET: Eto.Forms.ToolItem"""
    def __init__(self, *args) -> None: ...
    Command: ICommand
    CommandParameter: object
    Order: int
    Text: str
    ToolTip: str
    Image: Image
    Enabled: bool
    Visible: bool
    Tag: object
    Parent: Widget
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
    def OnClick(self, e: EventArgs) -> None: ...
    def Unbind(self, ) -> None: ...

class ToolItemCollection(Collection):
    """.NET: Eto.Forms.ToolItemCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: ToolItem
    def Add(self, command: Command, order: int) -> None: ...
    def AddRange(self, commands: IEnumerable, order: int) -> None: ...
    def AddSeparator(self, order: int, type: SeparatorToolItemType) -> None: ...

class TrayIndicator(Widget):
    """.NET: Eto.Forms.TrayIndicator"""
    def __init__(self, *args) -> None: ...
    Icon: Icon
    Image: Image
    Title: str
    Visible: bool
    Menu: ContextMenu
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    def Hide(self, ) -> None: ...
    def SetMenu(self, menu: ContextMenu) -> None: ...
    def Show(self, ) -> None: ...

class TreeGridCell:
    """.NET: Eto.Forms.TreeGridCell"""
    def __init__(self, *args) -> None: ...
    Item: object
    Column: GridColumn
    ColumnIndex: int
    Type: GridCellType

class TreeGridItem(GridItem):
    """.NET: Eto.Forms.TreeGridItem"""
    def __init__(self, *args) -> None: ...
    Children: TreeGridItemCollection
    Parent: ITreeGridItem
    Expandable: bool
    Expanded: bool
    Item: ITreeGridItem
    Count: int
    Tag: object
    Values: list

class TreeGridItemCollection(DataStoreCollection):
    """.NET: Eto.Forms.TreeGridItemCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: ITreeGridItem

class TreeGridView(Grid):
    """.NET: Eto.Forms.TreeGridView"""
    def __init__(self, *args) -> None: ...
    SelectedItem: ITreeGridItem
    DataStore: ITreeGridStore
    SelectedItems: IEnumerable
    ContextMenu: ContextMenu
    Columns: GridColumnCollection
    ShowHeader: bool
    AllowColumnReordering: bool
    AllowMultipleSelection: bool
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
    def GetCellAt(self, location: PointF) -> TreeGridCell: ...
    def GetDragInfo(self, args: DragEventArgs) -> TreeGridViewDragInfo: ...
    def ReloadData(self, ) -> None: ...
    def ReloadItem(self, item: ITreeGridItem, reloadChildren: bool) -> None: ...

class TreeGridViewDragInfo:
    """.NET: Eto.Forms.TreeGridViewDragInfo"""
    def __init__(self, *args) -> None: ...
    Parent: object
    ChildIndex: int
    InsertIndex: int
    Position: GridDragPosition
    Control: TreeGridView
    IsChanged: bool
    Item: object
    def RestrictToInsert(self, ) -> None: ...
    def RestrictToNode(self, item: object, childLevels: int) -> bool: ...
    def RestrictToOver(self, ) -> None: ...

class TreeGridViewItemCancelEventArgs(CancelEventArgs):
    """.NET: Eto.Forms.TreeGridViewItemCancelEventArgs"""
    def __init__(self, *args) -> None: ...
    Item: ITreeGridItem
    Cancel: bool

class TreeGridViewItemEventArgs(EventArgs):
    """.NET: Eto.Forms.TreeGridViewItemEventArgs"""
    def __init__(self, *args) -> None: ...
    Item: ITreeGridItem

class TreeItem(ImageListItem):
    """.NET: Eto.Forms.TreeItem"""
    def __init__(self, *args) -> None: ...
    Children: TreeItemCollection
    Parent: ITreeItem
    Expandable: bool
    Expanded: bool
    Item: ITreeItem
    Count: int
    Image: Image
    Text: str
    Key: str
    Tag: object

class TreeItemCollection(DataStoreCollection):
    """.NET: Eto.Forms.TreeItemCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: ITreeItem

class TreeView(Control):
    """.NET: Eto.Forms.TreeView"""
    def __init__(self, *args) -> None: ...
    SelectedItem: ITreeItem
    DataStore: ITreeStore
    TextColor: Color
    LabelEdit: bool
    ContextMenu: ContextMenu
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
    def GetNodeAt(self, point: PointF) -> ITreeItem: ...
    def RefreshData(self, ) -> None: ...
    def RefreshItem(self, item: ITreeItem) -> None: ...

class TreeViewItemCancelEventArgs(CancelEventArgs):
    """.NET: Eto.Forms.TreeViewItemCancelEventArgs"""
    def __init__(self, *args) -> None: ...
    Item: ITreeItem
    Cancel: bool

class TreeViewItemEditEventArgs(TreeViewItemCancelEventArgs):
    """.NET: Eto.Forms.TreeViewItemEditEventArgs"""
    def __init__(self, *args) -> None: ...
    Label: str
    Item: ITreeItem
    Cancel: bool

class TreeViewItemEventArgs(EventArgs):
    """.NET: Eto.Forms.TreeViewItemEventArgs"""
    def __init__(self, *args) -> None: ...
    Item: ITreeItem

class UIThreadAccessException(Exception):
    """.NET: Eto.Forms.UIThreadAccessException"""
    def __init__(self, *args) -> None: ...
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str

class UIThreadCheckMode:
    """.NET: Eto.Forms.UIThreadCheckMode"""
    def __init__(self, *args) -> None: ...
    ...

class UITimer(Widget):
    """.NET: Eto.Forms.UITimer"""
    def __init__(self, *args) -> None: ...
    Interval: float
    Started: bool
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    def Start(self, ) -> None: ...
    def Stop(self, ) -> None: ...

class ValueCommand(Command):
    """.NET: Eto.Forms.ValueCommand`1"""
    def __init__(self, *args) -> None: ...
    Value: T
    ID: str
    Enabled: bool
    Tag: object
    MenuText: str
    ToolBarText: str
    ToolTip: str
    Image: Image
    Shortcut: Keys
    Properties: PropertyStore
    DelegatedCommand: ICommand
    CommandParameter: object
    Parent: IBindable
    DataContext: object
    IsDataContextChanging: bool
    Bindings: BindingCollection

class VariableMaskedTextProvider:
    """.NET: Eto.Forms.VariableMaskedTextProvider"""
    def __init__(self, *args) -> None: ...
    MaskCompleted: bool
    DisplayText: str
    Text: str
    EditPositions: IEnumerable
    IsEmpty: bool
    def Clear(self, position: int, length: int, forward: bool) -> bool: ...
    def Delete(self, position: int, length: int, forward: bool) -> bool: ...
    def Insert(self, character: str, position: int) -> bool: ...
    def Replace(self, character: str, position: int) -> bool: ...

class VerticalAlign:
    """.NET: Eto.Forms.VerticalAlign"""
    def __init__(self, *args) -> None: ...
    Middle: VerticalAlign
    Top: VerticalAlign
    Bottom: VerticalAlign
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class VerticalAlignment:
    """.NET: Eto.Forms.VerticalAlignment"""
    def __init__(self, *args) -> None: ...
    ...

class WebView(Control):
    """.NET: Eto.Forms.WebView"""
    def __init__(self, *args) -> None: ...
    CanGoBack: bool
    CanGoForward: bool
    Url: Uri
    DocumentTitle: str
    BrowserContextMenuEnabled: bool
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
    def ExecuteScript(self, script: str) -> str: ...
    def ExecuteScriptAsync(self, script: str) -> Task: ...
    def GoBack(self, ) -> None: ...
    def GoForward(self, ) -> None: ...
    def LoadHtml(self, stream: Stream, baseUri: Uri) -> None: ...
    def Reload(self, ) -> None: ...
    def ShowPrintDialog(self, ) -> None: ...
    def Stop(self, ) -> None: ...

class WebViewLoadedEventArgs(EventArgs):
    """.NET: Eto.Forms.WebViewLoadedEventArgs"""
    def __init__(self, *args) -> None: ...
    Uri: Uri

class WebViewLoadingEventArgs(WebViewLoadedEventArgs):
    """.NET: Eto.Forms.WebViewLoadingEventArgs"""
    def __init__(self, *args) -> None: ...
    Cancel: bool
    IsMainFrame: bool
    Uri: Uri

class WebViewMessageEventArgs(EventArgs):
    """.NET: Eto.Forms.WebViewMessageEventArgs"""
    def __init__(self, *args) -> None: ...
    Message: str

class WebViewNewWindowEventArgs(WebViewLoadingEventArgs):
    """.NET: Eto.Forms.WebViewNewWindowEventArgs"""
    def __init__(self, *args) -> None: ...
    NewWindowName: str
    Cancel: bool
    IsMainFrame: bool
    Uri: Uri

class WebViewTitleEventArgs(EventArgs):
    """.NET: Eto.Forms.WebViewTitleEventArgs"""
    def __init__(self, *args) -> None: ...
    Title: str

class WidgetExtensions:
    """.NET: Eto.Forms.WidgetExtensions"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def With(widget: T, action: Action) -> T: ...

class Window(Panel):
    """.NET: Eto.Forms.Window"""
    def __init__(self, *args) -> None: ...
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
    def BringToFront(self, ) -> None: ...
    def Close(self, ) -> None: ...
    @staticmethod
    def FromPoint(point: PointF) -> Window: ...
    def Maximize(self, ) -> None: ...
    def Minimize(self, ) -> None: ...
    def SendToBack(self, ) -> None: ...

class WindowState:
    """.NET: Eto.Forms.WindowState"""
    def __init__(self, *args) -> None: ...
    ...

class WindowStyle:
    """.NET: Eto.Forms.WindowStyle"""
    def __init__(self, *args) -> None: ...
    ...

class WrapMode:
    """.NET: Eto.Forms.WrapMode"""
    def __init__(self, *args) -> None: ...
    ...
