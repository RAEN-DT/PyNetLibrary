# Auto-generated — Tekla 2026 — Tekla.Structures.Dialog

class ApplicationFormBase(FormBase):
    """.NET: Tekla.Structures.Dialog.ApplicationFormBase"""
    def __init__(self, *args) -> None: ...
    Localization: Localization
    AcceptButton: IButtonControl
    ActiveMdiChild: Form
    AllowTransparency: bool
    AutoScale: bool
    AutoScaleBaseSize: Size
    AutoScroll: bool
    AutoSize: bool
    AutoSizeMode: AutoSizeMode
    AutoValidate: AutoValidate
    BackColor: Color
    FormBorderStyle: FormBorderStyle
    CancelButton: IButtonControl
    ClientSize: Size
    ControlBox: bool
    DesktopBounds: Rectangle
    DesktopLocation: Point
    DialogResult: DialogResult
    HelpButton: bool
    Icon: Icon
    IsMdiChild: bool
    IsMdiContainer: bool
    IsRestrictedWindow: bool
    KeyPreview: bool
    Location: Point
    MaximumSize: Size
    MainMenuStrip: MenuStrip
    Margin: Padding
    Menu: MainMenu
    MinimumSize: Size
    MaximizeBox: bool
    MdiChildren: list
    MdiParent: Form
    MergedMenu: MainMenu
    MinimizeBox: bool
    Modal: bool
    Opacity: float
    OwnedForms: list
    Owner: Form
    RestoreBounds: Rectangle
    RightToLeftLayout: bool
    ShowInTaskbar: bool
    ShowIcon: bool
    Size: Size
    SizeGripStyle: SizeGripStyle
    StartPosition: FormStartPosition
    TabIndex: int
    TabStop: bool
    Text: str
    TopLevel: bool
    TopMost: bool
    TransparencyKey: Color
    WindowState: FormWindowState
    AutoScaleDimensions: SizeF
    AutoScaleMode: AutoScaleMode
    BindingContext: BindingContext
    ActiveControl: Control
    CurrentAutoScaleDimensions: SizeF
    ParentForm: Form
    AutoScrollMargin: Size
    AutoScrollPosition: Point
    AutoScrollMinSize: Size
    DisplayRectangle: Rectangle
    HorizontalScroll: HScrollProperties
    VerticalScroll: VScrollProperties
    DockPadding: DockPaddingEdges
    AccessibilityObject: AccessibleObject
    AccessibleDefaultActionDescription: str
    AccessibleDescription: str
    AccessibleName: str
    AccessibleRole: AccessibleRole
    AllowDrop: bool
    Anchor: AnchorStyles
    AutoScrollOffset: Point
    LayoutEngine: LayoutEngine
    BackgroundImage: Image
    BackgroundImageLayout: ImageLayout
    Bottom: int
    Bounds: Rectangle
    CanFocus: bool
    CanSelect: bool
    Capture: bool
    CausesValidation: bool
    ClientRectangle: Rectangle
    CompanyName: str
    ContainsFocus: bool
    ContextMenu: ContextMenu
    ContextMenuStrip: ContextMenuStrip
    Controls: ControlCollection
    Created: bool
    Cursor: Cursor
    DataBindings: ControlBindingsCollection
    DeviceDpi: int
    IsDisposed: bool
    Disposing: bool
    Dock: DockStyle
    Enabled: bool
    Focused: bool
    Font: Font
    ForeColor: Color
    Handle: IntPtr
    HasChildren: bool
    Height: int
    IsHandleCreated: bool
    InvokeRequired: bool
    IsAccessible: bool
    IsMirrored: bool
    Left: int
    Name: str
    Parent: Control
    ProductName: str
    ProductVersion: str
    RecreatingHandle: bool
    Region: Region
    Right: int
    RightToLeft: RightToLeft
    Site: ISite
    Tag: object
    Top: int
    TopLevelControl: Control
    UseWaitCursor: bool
    Visible: bool
    Width: int
    WindowTarget: IWindowTarget
    PreferredSize: Size
    Padding: Padding
    ImeMode: ImeMode
    Container: IContainer

class ApplicationWindowBase(WindowBase):
    """.NET: Tekla.Structures.Dialog.ApplicationWindowBase"""
    def __init__(self, *args) -> None: ...
    UseDefaultStyle: bool
    Localization: Localization
    LocExtension: LocExtension
    TaskbarItemInfo: TaskbarItemInfo
    AllowsTransparency: bool
    Title: str
    Icon: ImageSource
    SizeToContent: SizeToContent
    Top: float
    Left: float
    RestoreBounds: Rect
    WindowStartupLocation: WindowStartupLocation
    ShowInTaskbar: bool
    IsActive: bool
    Owner: Window
    OwnedWindows: WindowCollection
    DialogResult: Nullable
    WindowStyle: WindowStyle
    WindowState: WindowState
    ResizeMode: ResizeMode
    Topmost: bool
    ShowActivated: bool
    Content: object
    HasContent: bool
    ContentTemplate: DataTemplate
    ContentTemplateSelector: DataTemplateSelector
    ContentStringFormat: str
    BorderBrush: Brush
    BorderThickness: Thickness
    Background: Brush
    Foreground: Brush
    FontFamily: FontFamily
    FontSize: float
    FontStretch: FontStretch
    FontStyle: FontStyle
    FontWeight: FontWeight
    HorizontalContentAlignment: HorizontalAlignment
    VerticalContentAlignment: VerticalAlignment
    TabIndex: int
    IsTabStop: bool
    Padding: Thickness
    Template: ControlTemplate
    Style: Style
    OverridesDefaultStyle: bool
    UseLayoutRounding: bool
    Triggers: TriggerCollection
    TemplatedParent: DependencyObject
    Resources: ResourceDictionary
    DataContext: object
    BindingGroup: BindingGroup
    Language: XmlLanguage
    Name: str
    Tag: object
    InputScope: InputScope
    ActualWidth: float
    ActualHeight: float
    LayoutTransform: Transform
    Width: float
    MinWidth: float
    MaxWidth: float
    Height: float
    MinHeight: float
    MaxHeight: float
    FlowDirection: FlowDirection
    Margin: Thickness
    HorizontalAlignment: HorizontalAlignment
    VerticalAlignment: VerticalAlignment
    FocusVisualStyle: Style
    Cursor: Cursor
    ForceCursor: bool
    IsInitialized: bool
    IsLoaded: bool
    ToolTip: object
    ContextMenu: ContextMenu
    Parent: DependencyObject
    HasAnimatedProperties: bool
    InputBindings: InputBindingCollection
    CommandBindings: CommandBindingCollection
    AllowDrop: bool
    DesiredSize: Size
    IsMeasureValid: bool
    IsArrangeValid: bool
    RenderSize: Size
    RenderTransform: Transform
    RenderTransformOrigin: Point
    IsMouseDirectlyOver: bool
    IsMouseOver: bool
    IsStylusOver: bool
    IsKeyboardFocusWithin: bool
    IsMouseCaptured: bool
    IsMouseCaptureWithin: bool
    IsStylusDirectlyOver: bool
    IsStylusCaptured: bool
    IsStylusCaptureWithin: bool
    IsKeyboardFocused: bool
    IsInputMethodEnabled: bool
    Opacity: float
    OpacityMask: Brush
    BitmapEffect: BitmapEffect
    Effect: Effect
    BitmapEffectInput: BitmapEffectInput
    CacheMode: CacheMode
    Uid: str
    Visibility: Visibility
    ClipToBounds: bool
    Clip: Geometry
    SnapsToDevicePixels: bool
    IsFocused: bool
    IsEnabled: bool
    IsHitTestVisible: bool
    IsVisible: bool
    Focusable: bool
    PersistId: int
    IsManipulationEnabled: bool
    AreAnyTouchesOver: bool
    AreAnyTouchesDirectlyOver: bool
    AreAnyTouchesCapturedWithin: bool
    AreAnyTouchesCaptured: bool
    TouchesCaptured: IEnumerable
    TouchesCapturedWithin: IEnumerable
    TouchesOver: IEnumerable
    TouchesDirectlyOver: IEnumerable
    DependencyObjectType: DependencyObjectType
    IsSealed: bool
    Dispatcher: Dispatcher
    def InitializeDataStorage(self, ViewModel: object) -> None: ...

class AttributeTypeNameEditor(UITypeEditor):
    """.NET: Tekla.Structures.Dialog.AttributeTypeNameEditor"""
    def __init__(self, *args) -> None: ...
    IsDropDownResizable: bool
    def EditValue(self, context: ITypeDescriptorContext, provider: IServiceProvider, value: object) -> object: ...
    def GetEditStyle(self, context: ITypeDescriptorContext) -> UITypeEditorEditStyle: ...

class BindPropertyNameEditor(UITypeEditor):
    """.NET: Tekla.Structures.Dialog.BindPropertyNameEditor"""
    def __init__(self, *args) -> None: ...
    IsDropDownResizable: bool
    def EditValue(self, context: ITypeDescriptorContext, provider: IServiceProvider, value: object) -> object: ...
    def GetEditStyle(self, context: ITypeDescriptorContext) -> UITypeEditorEditStyle: ...

class Dialogs(MarshalByRefObject):
    """.NET: Tekla.Structures.Dialog.Dialogs"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def ClosePluginDialogs() -> None: ...
    @staticmethod
    def GetPluginFormBaseByPluginFormName(pluginFormName: str) -> PluginFormBase: ...
    @staticmethod
    def GetPluginWindowBaseByPluginFormName(pluginFormName: str) -> PluginWindowBase: ...
    @staticmethod
    def LoadAttributeFileNameToDialogAndApply(attributeFileName: str, pluginFormName: str) -> bool: ...
    @staticmethod
    def LoadAttributeFileNameToDialogAndModify(attributeFileName: str, pluginFormName: str) -> bool: ...
    @staticmethod
    def LoadAttributeFileNameToDialogAndSave(param: str) -> int: ...
    @staticmethod
    def LoadAttributeFileToStack(param: str) -> int: ...
    @staticmethod
    def LoadDialogs(param: str) -> int: ...
    @staticmethod
    def OpenDialog(param: str) -> int: ...
    @staticmethod
    def OpenDialogAndGet(param: str) -> int: ...
    @staticmethod
    def ReloadDialogs(param: str) -> int: ...
    @staticmethod
    def SetSettings(param: str) -> int: ...

class ErrorDialog(Form):
    """.NET: Tekla.Structures.Dialog.ErrorDialog"""
    def __init__(self, *args) -> None: ...
    AcceptButton: IButtonControl
    ActiveMdiChild: Form
    AllowTransparency: bool
    AutoScale: bool
    AutoScaleBaseSize: Size
    AutoScroll: bool
    AutoSize: bool
    AutoSizeMode: AutoSizeMode
    AutoValidate: AutoValidate
    BackColor: Color
    FormBorderStyle: FormBorderStyle
    CancelButton: IButtonControl
    ClientSize: Size
    ControlBox: bool
    DesktopBounds: Rectangle
    DesktopLocation: Point
    DialogResult: DialogResult
    HelpButton: bool
    Icon: Icon
    IsMdiChild: bool
    IsMdiContainer: bool
    IsRestrictedWindow: bool
    KeyPreview: bool
    Location: Point
    MaximumSize: Size
    MainMenuStrip: MenuStrip
    Margin: Padding
    Menu: MainMenu
    MinimumSize: Size
    MaximizeBox: bool
    MdiChildren: list
    MdiParent: Form
    MergedMenu: MainMenu
    MinimizeBox: bool
    Modal: bool
    Opacity: float
    OwnedForms: list
    Owner: Form
    RestoreBounds: Rectangle
    RightToLeftLayout: bool
    ShowInTaskbar: bool
    ShowIcon: bool
    Size: Size
    SizeGripStyle: SizeGripStyle
    StartPosition: FormStartPosition
    TabIndex: int
    TabStop: bool
    Text: str
    TopLevel: bool
    TopMost: bool
    TransparencyKey: Color
    WindowState: FormWindowState
    AutoScaleDimensions: SizeF
    AutoScaleMode: AutoScaleMode
    BindingContext: BindingContext
    ActiveControl: Control
    CurrentAutoScaleDimensions: SizeF
    ParentForm: Form
    AutoScrollMargin: Size
    AutoScrollPosition: Point
    AutoScrollMinSize: Size
    DisplayRectangle: Rectangle
    HorizontalScroll: HScrollProperties
    VerticalScroll: VScrollProperties
    DockPadding: DockPaddingEdges
    AccessibilityObject: AccessibleObject
    AccessibleDefaultActionDescription: str
    AccessibleDescription: str
    AccessibleName: str
    AccessibleRole: AccessibleRole
    AllowDrop: bool
    Anchor: AnchorStyles
    AutoScrollOffset: Point
    LayoutEngine: LayoutEngine
    BackgroundImage: Image
    BackgroundImageLayout: ImageLayout
    Bottom: int
    Bounds: Rectangle
    CanFocus: bool
    CanSelect: bool
    Capture: bool
    CausesValidation: bool
    ClientRectangle: Rectangle
    CompanyName: str
    ContainsFocus: bool
    ContextMenu: ContextMenu
    ContextMenuStrip: ContextMenuStrip
    Controls: ControlCollection
    Created: bool
    Cursor: Cursor
    DataBindings: ControlBindingsCollection
    DeviceDpi: int
    IsDisposed: bool
    Disposing: bool
    Dock: DockStyle
    Enabled: bool
    Focused: bool
    Font: Font
    ForeColor: Color
    Handle: IntPtr
    HasChildren: bool
    Height: int
    IsHandleCreated: bool
    InvokeRequired: bool
    IsAccessible: bool
    IsMirrored: bool
    Left: int
    Name: str
    Parent: Control
    ProductName: str
    ProductVersion: str
    RecreatingHandle: bool
    Region: Region
    Right: int
    RightToLeft: RightToLeft
    Site: ISite
    Tag: object
    Top: int
    TopLevelControl: Control
    UseWaitCursor: bool
    Visible: bool
    Width: int
    WindowTarget: IWindowTarget
    PreferredSize: Size
    Padding: Padding
    ImeMode: ImeMode
    Container: IContainer
    @staticmethod
    def Show(Message: str, Details: str, Severity: Severity) -> None: ...

class FormBase(Form):
    """.NET: Tekla.Structures.Dialog.FormBase"""
    def __init__(self, *args) -> None: ...
    Localization: Localization
    AcceptButton: IButtonControl
    ActiveMdiChild: Form
    AllowTransparency: bool
    AutoScale: bool
    AutoScaleBaseSize: Size
    AutoScroll: bool
    AutoSize: bool
    AutoSizeMode: AutoSizeMode
    AutoValidate: AutoValidate
    BackColor: Color
    FormBorderStyle: FormBorderStyle
    CancelButton: IButtonControl
    ClientSize: Size
    ControlBox: bool
    DesktopBounds: Rectangle
    DesktopLocation: Point
    DialogResult: DialogResult
    HelpButton: bool
    Icon: Icon
    IsMdiChild: bool
    IsMdiContainer: bool
    IsRestrictedWindow: bool
    KeyPreview: bool
    Location: Point
    MaximumSize: Size
    MainMenuStrip: MenuStrip
    Margin: Padding
    Menu: MainMenu
    MinimumSize: Size
    MaximizeBox: bool
    MdiChildren: list
    MdiParent: Form
    MergedMenu: MainMenu
    MinimizeBox: bool
    Modal: bool
    Opacity: float
    OwnedForms: list
    Owner: Form
    RestoreBounds: Rectangle
    RightToLeftLayout: bool
    ShowInTaskbar: bool
    ShowIcon: bool
    Size: Size
    SizeGripStyle: SizeGripStyle
    StartPosition: FormStartPosition
    TabIndex: int
    TabStop: bool
    Text: str
    TopLevel: bool
    TopMost: bool
    TransparencyKey: Color
    WindowState: FormWindowState
    AutoScaleDimensions: SizeF
    AutoScaleMode: AutoScaleMode
    BindingContext: BindingContext
    ActiveControl: Control
    CurrentAutoScaleDimensions: SizeF
    ParentForm: Form
    AutoScrollMargin: Size
    AutoScrollPosition: Point
    AutoScrollMinSize: Size
    DisplayRectangle: Rectangle
    HorizontalScroll: HScrollProperties
    VerticalScroll: VScrollProperties
    DockPadding: DockPaddingEdges
    AccessibilityObject: AccessibleObject
    AccessibleDefaultActionDescription: str
    AccessibleDescription: str
    AccessibleName: str
    AccessibleRole: AccessibleRole
    AllowDrop: bool
    Anchor: AnchorStyles
    AutoScrollOffset: Point
    LayoutEngine: LayoutEngine
    BackgroundImage: Image
    BackgroundImageLayout: ImageLayout
    Bottom: int
    Bounds: Rectangle
    CanFocus: bool
    CanSelect: bool
    Capture: bool
    CausesValidation: bool
    ClientRectangle: Rectangle
    CompanyName: str
    ContainsFocus: bool
    ContextMenu: ContextMenu
    ContextMenuStrip: ContextMenuStrip
    Controls: ControlCollection
    Created: bool
    Cursor: Cursor
    DataBindings: ControlBindingsCollection
    DeviceDpi: int
    IsDisposed: bool
    Disposing: bool
    Dock: DockStyle
    Enabled: bool
    Focused: bool
    Font: Font
    ForeColor: Color
    Handle: IntPtr
    HasChildren: bool
    Height: int
    IsHandleCreated: bool
    InvokeRequired: bool
    IsAccessible: bool
    IsMirrored: bool
    Left: int
    Name: str
    Parent: Control
    ProductName: str
    ProductVersion: str
    RecreatingHandle: bool
    Region: Region
    Right: int
    RightToLeft: RightToLeft
    Site: ISite
    Tag: object
    Top: int
    TopLevelControl: Control
    UseWaitCursor: bool
    Visible: bool
    Width: int
    WindowTarget: IWindowTarget
    PreferredSize: Size
    Padding: Padding
    ImeMode: ImeMode
    Container: IContainer
    def ApplyValues(self, FileName: str) -> None: ...
    def GetConnectionStatus(self, ) -> bool: ...
    @staticmethod
    def GetUnitDecimals(unit: dotdiaUnitTypes_e) -> int: ...
    @staticmethod
    def InitializeAngleUnitDecimals() -> bool: ...
    @staticmethod
    def InitializeDistanceUnitDecimals() -> bool: ...
    def InitializeForm(self, ) -> None: ...
    @staticmethod
    def InitializeUnitDecimals() -> bool: ...
    def LoadValues(self, FileName: str) -> None: ...
    def ModifyValues(self, FileName: str) -> None: ...
    def SaveValues(self, fileName: str) -> None: ...
    def SetAttributeValue(self, Ctrl: Control, Value: object) -> None: ...
    def ShowForm(self, ) -> None: ...
    def UpdateValues(self, ) -> None: ...

class FormBorders:
    """.NET: Tekla.Structures.Dialog.FormBorders"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def CheckScreenPosition(form: Form) -> None: ...
    @staticmethod
    def IsOnActiveDisplays(form: Form) -> bool: ...
    @staticmethod
    def RestoreFormSizeAndLocation(form: Form) -> None: ...
    @staticmethod
    def StoreFormSizeAndLocation(form: Form) -> None: ...

class HelpViewer:
    """.NET: Tekla.Structures.Dialog.HelpViewer"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def DisplayHelpTopic(helpTopic: str) -> bool: ...
    @staticmethod
    def DisplayHelpTopicIndependent(helpViewerFilePath: str, helpTopic: str, language: str) -> bool: ...

class LocExtension(Binding):
    """.NET: Tekla.Structures.Dialog.LocExtension"""
    def __init__(self, *args) -> None: ...
    ValidationRules: Collection
    ValidatesOnExceptions: bool
    ValidatesOnDataErrors: bool
    ValidatesOnNotifyDataErrors: bool
    Path: PropertyPath
    XPath: str
    Mode: BindingMode
    UpdateSourceTrigger: UpdateSourceTrigger
    NotifyOnSourceUpdated: bool
    NotifyOnTargetUpdated: bool
    NotifyOnValidationError: bool
    Converter: IValueConverter
    ConverterParameter: object
    ConverterCulture: CultureInfo
    Source: object
    RelativeSource: RelativeSource
    ElementName: str
    IsAsync: bool
    AsyncState: object
    BindsDirectlyToSource: bool
    UpdateSourceExceptionFilter: UpdateSourceExceptionFilterCallback
    FallbackValue: object
    StringFormat: str
    TargetNullValue: object
    BindingGroupName: str
    Delay: int

class Localization(MarshalByRefObject):
    """.NET: Tekla.Structures.Dialog.Localization"""
    def __init__(self, *args) -> None: ...
    DefaultLocalizationFile: str
    DefaultLocalizationPath: str
    Language: str
    @staticmethod
    def GetLocalizationFileFullPath(fileName: str) -> str: ...
    def GetText(self, name: str) -> str: ...
    def LoadAidFile(self, fileName: str) -> None: ...
    def LoadAilFile(self, fileName: str) -> None: ...
    def LoadFile(self, fileName: str) -> None: ...
    def LoadXMLFile(self, fileName: str) -> None: ...
    def Localize(self, menuItem: MenuItem) -> None: ...
    def LocalizeToolTip(self, control: Control, toolTip: ToolTip) -> None: ...
    def RegisterLocalizationCallback(self, cb: LocalizationCallback, types: list) -> None: ...

class MainWindow:
    """.NET: Tekla.Structures.Dialog.MainWindow"""
    def __init__(self, *args) -> None: ...
    Handle: IntPtr
    def AddExternalWindow(self, Name: str, Handle: IntPtr) -> None: ...
    def RemoveExternalWindow(self, Name: str, Handle: IntPtr) -> None: ...

class PluginFormBase(FormBase):
    """.NET: Tekla.Structures.Dialog.PluginFormBase"""
    def __init__(self, *args) -> None: ...
    ShowInTaskbar: bool
    Localization: Localization
    AcceptButton: IButtonControl
    ActiveMdiChild: Form
    AllowTransparency: bool
    AutoScale: bool
    AutoScaleBaseSize: Size
    AutoScroll: bool
    AutoSize: bool
    AutoSizeMode: AutoSizeMode
    AutoValidate: AutoValidate
    BackColor: Color
    FormBorderStyle: FormBorderStyle
    CancelButton: IButtonControl
    ClientSize: Size
    ControlBox: bool
    DesktopBounds: Rectangle
    DesktopLocation: Point
    DialogResult: DialogResult
    HelpButton: bool
    Icon: Icon
    IsMdiChild: bool
    IsMdiContainer: bool
    IsRestrictedWindow: bool
    KeyPreview: bool
    Location: Point
    MaximumSize: Size
    MainMenuStrip: MenuStrip
    Margin: Padding
    Menu: MainMenu
    MinimumSize: Size
    MaximizeBox: bool
    MdiChildren: list
    MdiParent: Form
    MergedMenu: MainMenu
    MinimizeBox: bool
    Modal: bool
    Opacity: float
    OwnedForms: list
    Owner: Form
    RestoreBounds: Rectangle
    RightToLeftLayout: bool
    ShowIcon: bool
    Size: Size
    SizeGripStyle: SizeGripStyle
    StartPosition: FormStartPosition
    TabIndex: int
    TabStop: bool
    Text: str
    TopLevel: bool
    TopMost: bool
    TransparencyKey: Color
    WindowState: FormWindowState
    AutoScaleDimensions: SizeF
    AutoScaleMode: AutoScaleMode
    BindingContext: BindingContext
    ActiveControl: Control
    CurrentAutoScaleDimensions: SizeF
    ParentForm: Form
    AutoScrollMargin: Size
    AutoScrollPosition: Point
    AutoScrollMinSize: Size
    DisplayRectangle: Rectangle
    HorizontalScroll: HScrollProperties
    VerticalScroll: VScrollProperties
    DockPadding: DockPaddingEdges
    AccessibilityObject: AccessibleObject
    AccessibleDefaultActionDescription: str
    AccessibleDescription: str
    AccessibleName: str
    AccessibleRole: AccessibleRole
    AllowDrop: bool
    Anchor: AnchorStyles
    AutoScrollOffset: Point
    LayoutEngine: LayoutEngine
    BackgroundImage: Image
    BackgroundImageLayout: ImageLayout
    Bottom: int
    Bounds: Rectangle
    CanFocus: bool
    CanSelect: bool
    Capture: bool
    CausesValidation: bool
    ClientRectangle: Rectangle
    CompanyName: str
    ContainsFocus: bool
    ContextMenu: ContextMenu
    ContextMenuStrip: ContextMenuStrip
    Controls: ControlCollection
    Created: bool
    Cursor: Cursor
    DataBindings: ControlBindingsCollection
    DeviceDpi: int
    IsDisposed: bool
    Disposing: bool
    Dock: DockStyle
    Enabled: bool
    Focused: bool
    Font: Font
    ForeColor: Color
    Handle: IntPtr
    HasChildren: bool
    Height: int
    IsHandleCreated: bool
    InvokeRequired: bool
    IsAccessible: bool
    IsMirrored: bool
    Left: int
    Name: str
    Parent: Control
    ProductName: str
    ProductVersion: str
    RecreatingHandle: bool
    Region: Region
    Right: int
    RightToLeft: RightToLeft
    Site: ISite
    Tag: object
    Top: int
    TopLevelControl: Control
    UseWaitCursor: bool
    Visible: bool
    Width: int
    WindowTarget: IWindowTarget
    PreferredSize: Size
    Padding: Padding
    ImeMode: ImeMode
    Container: IContainer
    def Get(self, ) -> None: ...
    def ReloadForm(self, ) -> None: ...

class PluginWindowBase(WindowBase):
    """.NET: Tekla.Structures.Dialog.PluginWindowBase"""
    def __init__(self, *args) -> None: ...
    ShowInTaskbar: bool
    UseDefaultStyle: bool
    Localization: Localization
    LocExtension: LocExtension
    TaskbarItemInfo: TaskbarItemInfo
    AllowsTransparency: bool
    Title: str
    Icon: ImageSource
    SizeToContent: SizeToContent
    Top: float
    Left: float
    RestoreBounds: Rect
    WindowStartupLocation: WindowStartupLocation
    IsActive: bool
    Owner: Window
    OwnedWindows: WindowCollection
    DialogResult: Nullable
    WindowStyle: WindowStyle
    WindowState: WindowState
    ResizeMode: ResizeMode
    Topmost: bool
    ShowActivated: bool
    Content: object
    HasContent: bool
    ContentTemplate: DataTemplate
    ContentTemplateSelector: DataTemplateSelector
    ContentStringFormat: str
    BorderBrush: Brush
    BorderThickness: Thickness
    Background: Brush
    Foreground: Brush
    FontFamily: FontFamily
    FontSize: float
    FontStretch: FontStretch
    FontStyle: FontStyle
    FontWeight: FontWeight
    HorizontalContentAlignment: HorizontalAlignment
    VerticalContentAlignment: VerticalAlignment
    TabIndex: int
    IsTabStop: bool
    Padding: Thickness
    Template: ControlTemplate
    Style: Style
    OverridesDefaultStyle: bool
    UseLayoutRounding: bool
    Triggers: TriggerCollection
    TemplatedParent: DependencyObject
    Resources: ResourceDictionary
    DataContext: object
    BindingGroup: BindingGroup
    Language: XmlLanguage
    Name: str
    Tag: object
    InputScope: InputScope
    ActualWidth: float
    ActualHeight: float
    LayoutTransform: Transform
    Width: float
    MinWidth: float
    MaxWidth: float
    Height: float
    MinHeight: float
    MaxHeight: float
    FlowDirection: FlowDirection
    Margin: Thickness
    HorizontalAlignment: HorizontalAlignment
    VerticalAlignment: VerticalAlignment
    FocusVisualStyle: Style
    Cursor: Cursor
    ForceCursor: bool
    IsInitialized: bool
    IsLoaded: bool
    ToolTip: object
    ContextMenu: ContextMenu
    Parent: DependencyObject
    HasAnimatedProperties: bool
    InputBindings: InputBindingCollection
    CommandBindings: CommandBindingCollection
    AllowDrop: bool
    DesiredSize: Size
    IsMeasureValid: bool
    IsArrangeValid: bool
    RenderSize: Size
    RenderTransform: Transform
    RenderTransformOrigin: Point
    IsMouseDirectlyOver: bool
    IsMouseOver: bool
    IsStylusOver: bool
    IsKeyboardFocusWithin: bool
    IsMouseCaptured: bool
    IsMouseCaptureWithin: bool
    IsStylusDirectlyOver: bool
    IsStylusCaptured: bool
    IsStylusCaptureWithin: bool
    IsKeyboardFocused: bool
    IsInputMethodEnabled: bool
    Opacity: float
    OpacityMask: Brush
    BitmapEffect: BitmapEffect
    Effect: Effect
    BitmapEffectInput: BitmapEffectInput
    CacheMode: CacheMode
    Uid: str
    Visibility: Visibility
    ClipToBounds: bool
    Clip: Geometry
    SnapsToDevicePixels: bool
    IsFocused: bool
    IsEnabled: bool
    IsHitTestVisible: bool
    IsVisible: bool
    Focusable: bool
    PersistId: int
    IsManipulationEnabled: bool
    AreAnyTouchesOver: bool
    AreAnyTouchesDirectlyOver: bool
    AreAnyTouchesCapturedWithin: bool
    AreAnyTouchesCaptured: bool
    TouchesCaptured: IEnumerable
    TouchesCapturedWithin: IEnumerable
    TouchesOver: IEnumerable
    TouchesDirectlyOver: IEnumerable
    DependencyObjectType: DependencyObjectType
    IsSealed: bool
    Dispatcher: Dispatcher
    def Dispose(self, ) -> None: ...
    def Get(self, ) -> None: ...
    def ReloadWindow(self, ) -> None: ...

class ProfileConversion:
    """.NET: Tekla.Structures.Dialog.ProfileConversion"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def ConvertFromCurrentUnits(Profile: str, ConvertedProfile: str) -> bool: ...
    @staticmethod
    def ConvertToCurrentUnits(Profile: str, ConvertedProfile: str) -> bool: ...

class StructuresDialogArrayAttribute(Attribute):
    """.NET: Tekla.Structures.Dialog.StructuresDialogArrayAttribute"""
    def __init__(self, *args) -> None: ...
    AttributeName: str
    TypeId: object
    def ToString(self, ) -> str: ...

class StructuresDialogAttribute(Attribute):
    """.NET: Tekla.Structures.Dialog.StructuresDialogAttribute"""
    def __init__(self, *args) -> None: ...
    AttributeName: str
    AttributeType: Type
    TypeId: object
    @staticmethod
    def GetCorrectDialogAttributeType(attributeType: str) -> Type: ...
    def ToString(self, ) -> str: ...

class StructuresDialogFilterAttribute(Attribute):
    """.NET: Tekla.Structures.Dialog.StructuresDialogFilterAttribute"""
    def __init__(self, *args) -> None: ...
    AttributeName: str
    TypeId: object
    def ToString(self, ) -> str: ...

class StructuresExtender(Component):
    """.NET: Tekla.Structures.Dialog.StructuresExtender"""
    def __init__(self, *args) -> None: ...
    Site: ISite
    Container: IContainer
    def CanExtend(self, extendee: object) -> bool: ...
    def GetAttributeName(self, control: Control) -> str: ...
    def GetAttributeTypeName(self, control: Control) -> str: ...
    def GetBindPropertyName(self, control: Control) -> str: ...
    def GetIsFilter(self, control: Control) -> bool: ...
    def SetAttributeName(self, control: Control, value: str) -> None: ...
    def SetAttributeTypeName(self, control: Control, value: str) -> None: ...
    def SetBindPropertyName(self, control: Control, value: str) -> None: ...
    def SetIsFilter(self, control: Control, value: bool) -> None: ...

class StructuresInstallation:
    """.NET: Tekla.Structures.Dialog.StructuresInstallation"""
    def __init__(self, *args) -> None: ...
    BinFolder: str
    EnvBaseFolder: str
    InstallFolder: str
    MessageFolder: str
    MessagesFolder: SortedSet
    @staticmethod
    def GetLocalizationFile(subPath: str, messageFile: str) -> str: ...

class TeklaProgressBar(Form):
    """.NET: Tekla.Structures.Dialog.TeklaProgressBar"""
    def __init__(self, *args) -> None: ...
    Value: int
    Text: str
    AcceptButton: IButtonControl
    ActiveMdiChild: Form
    AllowTransparency: bool
    AutoScale: bool
    AutoScaleBaseSize: Size
    AutoScroll: bool
    AutoSize: bool
    AutoSizeMode: AutoSizeMode
    AutoValidate: AutoValidate
    BackColor: Color
    FormBorderStyle: FormBorderStyle
    CancelButton: IButtonControl
    ClientSize: Size
    ControlBox: bool
    DesktopBounds: Rectangle
    DesktopLocation: Point
    DialogResult: DialogResult
    HelpButton: bool
    Icon: Icon
    IsMdiChild: bool
    IsMdiContainer: bool
    IsRestrictedWindow: bool
    KeyPreview: bool
    Location: Point
    MaximumSize: Size
    MainMenuStrip: MenuStrip
    Margin: Padding
    Menu: MainMenu
    MinimumSize: Size
    MaximizeBox: bool
    MdiChildren: list
    MdiParent: Form
    MergedMenu: MainMenu
    MinimizeBox: bool
    Modal: bool
    Opacity: float
    OwnedForms: list
    Owner: Form
    RestoreBounds: Rectangle
    RightToLeftLayout: bool
    ShowInTaskbar: bool
    ShowIcon: bool
    Size: Size
    SizeGripStyle: SizeGripStyle
    StartPosition: FormStartPosition
    TabIndex: int
    TabStop: bool
    TopLevel: bool
    TopMost: bool
    TransparencyKey: Color
    WindowState: FormWindowState
    AutoScaleDimensions: SizeF
    AutoScaleMode: AutoScaleMode
    BindingContext: BindingContext
    ActiveControl: Control
    CurrentAutoScaleDimensions: SizeF
    ParentForm: Form
    AutoScrollMargin: Size
    AutoScrollPosition: Point
    AutoScrollMinSize: Size
    DisplayRectangle: Rectangle
    HorizontalScroll: HScrollProperties
    VerticalScroll: VScrollProperties
    DockPadding: DockPaddingEdges
    AccessibilityObject: AccessibleObject
    AccessibleDefaultActionDescription: str
    AccessibleDescription: str
    AccessibleName: str
    AccessibleRole: AccessibleRole
    AllowDrop: bool
    Anchor: AnchorStyles
    AutoScrollOffset: Point
    LayoutEngine: LayoutEngine
    BackgroundImage: Image
    BackgroundImageLayout: ImageLayout
    Bottom: int
    Bounds: Rectangle
    CanFocus: bool
    CanSelect: bool
    Capture: bool
    CausesValidation: bool
    ClientRectangle: Rectangle
    CompanyName: str
    ContainsFocus: bool
    ContextMenu: ContextMenu
    ContextMenuStrip: ContextMenuStrip
    Controls: ControlCollection
    Created: bool
    Cursor: Cursor
    DataBindings: ControlBindingsCollection
    DeviceDpi: int
    IsDisposed: bool
    Disposing: bool
    Dock: DockStyle
    Enabled: bool
    Focused: bool
    Font: Font
    ForeColor: Color
    Handle: IntPtr
    HasChildren: bool
    Height: int
    IsHandleCreated: bool
    InvokeRequired: bool
    IsAccessible: bool
    IsMirrored: bool
    Left: int
    Name: str
    Parent: Control
    ProductName: str
    ProductVersion: str
    RecreatingHandle: bool
    Region: Region
    Right: int
    RightToLeft: RightToLeft
    Site: ISite
    Tag: object
    Top: int
    TopLevelControl: Control
    UseWaitCursor: bool
    Visible: bool
    Width: int
    WindowTarget: IWindowTarget
    PreferredSize: Size
    Padding: Padding
    ImeMode: ImeMode
    Container: IContainer

class WindowBase(Window):
    """.NET: Tekla.Structures.Dialog.WindowBase"""
    def __init__(self, *args) -> None: ...
    UseDefaultStyle: bool
    Localization: Localization
    LocExtension: LocExtension
    TaskbarItemInfo: TaskbarItemInfo
    AllowsTransparency: bool
    Title: str
    Icon: ImageSource
    SizeToContent: SizeToContent
    Top: float
    Left: float
    RestoreBounds: Rect
    WindowStartupLocation: WindowStartupLocation
    ShowInTaskbar: bool
    IsActive: bool
    Owner: Window
    OwnedWindows: WindowCollection
    DialogResult: Nullable
    WindowStyle: WindowStyle
    WindowState: WindowState
    ResizeMode: ResizeMode
    Topmost: bool
    ShowActivated: bool
    Content: object
    HasContent: bool
    ContentTemplate: DataTemplate
    ContentTemplateSelector: DataTemplateSelector
    ContentStringFormat: str
    BorderBrush: Brush
    BorderThickness: Thickness
    Background: Brush
    Foreground: Brush
    FontFamily: FontFamily
    FontSize: float
    FontStretch: FontStretch
    FontStyle: FontStyle
    FontWeight: FontWeight
    HorizontalContentAlignment: HorizontalAlignment
    VerticalContentAlignment: VerticalAlignment
    TabIndex: int
    IsTabStop: bool
    Padding: Thickness
    Template: ControlTemplate
    Style: Style
    OverridesDefaultStyle: bool
    UseLayoutRounding: bool
    Triggers: TriggerCollection
    TemplatedParent: DependencyObject
    Resources: ResourceDictionary
    DataContext: object
    BindingGroup: BindingGroup
    Language: XmlLanguage
    Name: str
    Tag: object
    InputScope: InputScope
    ActualWidth: float
    ActualHeight: float
    LayoutTransform: Transform
    Width: float
    MinWidth: float
    MaxWidth: float
    Height: float
    MinHeight: float
    MaxHeight: float
    FlowDirection: FlowDirection
    Margin: Thickness
    HorizontalAlignment: HorizontalAlignment
    VerticalAlignment: VerticalAlignment
    FocusVisualStyle: Style
    Cursor: Cursor
    ForceCursor: bool
    IsInitialized: bool
    IsLoaded: bool
    ToolTip: object
    ContextMenu: ContextMenu
    Parent: DependencyObject
    HasAnimatedProperties: bool
    InputBindings: InputBindingCollection
    CommandBindings: CommandBindingCollection
    AllowDrop: bool
    DesiredSize: Size
    IsMeasureValid: bool
    IsArrangeValid: bool
    RenderSize: Size
    RenderTransform: Transform
    RenderTransformOrigin: Point
    IsMouseDirectlyOver: bool
    IsMouseOver: bool
    IsStylusOver: bool
    IsKeyboardFocusWithin: bool
    IsMouseCaptured: bool
    IsMouseCaptureWithin: bool
    IsStylusDirectlyOver: bool
    IsStylusCaptured: bool
    IsStylusCaptureWithin: bool
    IsKeyboardFocused: bool
    IsInputMethodEnabled: bool
    Opacity: float
    OpacityMask: Brush
    BitmapEffect: BitmapEffect
    Effect: Effect
    BitmapEffectInput: BitmapEffectInput
    CacheMode: CacheMode
    Uid: str
    Visibility: Visibility
    ClipToBounds: bool
    Clip: Geometry
    SnapsToDevicePixels: bool
    IsFocused: bool
    IsEnabled: bool
    IsHitTestVisible: bool
    IsVisible: bool
    Focusable: bool
    PersistId: int
    IsManipulationEnabled: bool
    AreAnyTouchesOver: bool
    AreAnyTouchesDirectlyOver: bool
    AreAnyTouchesCapturedWithin: bool
    AreAnyTouchesCaptured: bool
    TouchesCaptured: IEnumerable
    TouchesCapturedWithin: IEnumerable
    TouchesOver: IEnumerable
    TouchesDirectlyOver: IEnumerable
    DependencyObjectType: DependencyObjectType
    IsSealed: bool
    Dispatcher: Dispatcher
    def ApplyValues(self, FileName: str) -> None: ...
    def GetConnectionStatus(self, ) -> bool: ...
    @staticmethod
    def GetUnitDecimals(unit: dotdiaUnitTypes_e) -> int: ...
    @staticmethod
    def InitializeAngleUnitDecimals() -> bool: ...
    @staticmethod
    def InitializeDistanceUnitDecimals() -> bool: ...
    @staticmethod
    def InitializeUnitDecimals() -> bool: ...
    def InitializeWindow(self, ) -> None: ...
    def LoadValues(self, FileName: str) -> None: ...
    def ModifyValues(self, FileName: str) -> None: ...
    def SaveValues(self, fileName: str) -> None: ...
    def ShowWindow(self, ) -> None: ...
    def UpdateDataStorageFromViewModel(self, viewModelClass: object) -> None: ...

class dotdiaUnitTypes_e:
    """.NET: Tekla.Structures.Dialog.dotdiaUnitTypes_e"""
    def __init__(self, *args) -> None: ...
    ...
