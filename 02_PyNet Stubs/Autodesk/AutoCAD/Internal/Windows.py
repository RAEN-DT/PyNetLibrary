# Auto-generated — Civil 26 — Autodesk.AutoCAD.Internal.Windows

class ClicFixedUi:
    """.NET: Autodesk.AutoCAD.Internal.Windows.ClicFixedUi"""
    def __init__(self, *args) -> None: ...
    MenuItems: List
    ItemCount: int
    MenuStyle: ClicUiStyle
    Style: ClicUiStyle
    Text: str
    Avatar: str
    Enabled: bool
    Display: bool

class ClicMenuUi:
    """.NET: Autodesk.AutoCAD.Internal.Windows.ClicMenuUi"""
    def __init__(self, *args) -> None: ...
    Action: list
    Enabled: bool
    Text: str

class ClicTemporalUi:
    """.NET: Autodesk.AutoCAD.Internal.Windows.ClicTemporalUi"""
    def __init__(self, *args) -> None: ...
    Action: list
    Style: ClicUiStyle
    Text: str
    Badge: str
    Enabled: bool
    Display: bool

class ClicUi:
    """.NET: Autodesk.AutoCAD.Internal.Windows.ClicUi"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def Instance() -> ClicUi: ...
    def SendUiAction(self, action: list, left: int, top: int, right: int, bottom: int) -> None: ...

class ClicUiDisplayEventHandler:
    """.NET: Autodesk.AutoCAD.Internal.Windows.ClicUiDisplayEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: ClicUiEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: ClicUiEventArgs) -> None: ...

class ClicUiElementColors:
    """.NET: Autodesk.AutoCAD.Internal.Windows.ClicUiElementColors"""
    def __init__(self, *args) -> None: ...
    BackgroundColor: list
    BorderColor: list
    FontColor: list

class ClicUiEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.Internal.Windows.ClicUiEventArgs"""
    def __init__(self, *args) -> None: ...
    FixedUi: ClicFixedUi
    TemporalUi: ClicTemporalUi

class ClicUiStyle:
    """.NET: Autodesk.AutoCAD.Internal.Windows.ClicUiStyle"""
    def __init__(self, *args) -> None: ...
    Hover: ClicUiElementColors
    Normal: ClicUiElementColors
    FontItalic: bool
    FontBold: bool
    FontSize: int
    FontFamily: str

class CommandThroat:
    """.NET: Autodesk.AutoCAD.Internal.Windows.CommandThroat"""
    def __init__(self, *args) -> None: ...
    ...

class CommandToolTipData:
    """.NET: Autodesk.AutoCAD.Internal.Windows.CommandToolTipData"""
    def __init__(self, *args) -> None: ...
    Shortcut: str
    UserTag: str
    ExtendedContentKey: str
    ExtendedContentSource: str
    BasicContent: str
    HelpTopic: str
    HelpSource: str
    Title: str
    Macro: str
    CLICommand: str
    EnableHelp: bool

class InputCharactersQueuedEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.Internal.Windows.InputCharactersQueuedEventArgs"""
    def __init__(self, *args) -> None: ...
    Characters: str

class InputCharactersQueuedEventHandler:
    """.NET: Autodesk.AutoCAD.Internal.Windows.InputCharactersQueuedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: InputCharactersQueuedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: InputCharactersQueuedEventArgs) -> None: ...

class MenuGroupData:
    """.NET: Autodesk.AutoCAD.Internal.Windows.MenuGroupData"""
    def __init__(self, *args) -> None: ...
    DefaultToolTipHelpSource: str
    PartialMenus: List
    MenuGroupType: MenuGroupTypeEnum
    FileName: str
    Name: str
    def Dispose(self, ) -> None: ...
    def GetMenuMacro(self, sId: str) -> RibbonMenuMacro: ...

class MenuGroupTypeEnum:
    """.NET enum: Autodesk.AutoCAD.Internal.Windows.MenuGroupTypeEnum"""
    def __init__(self, *args) -> None: ...
    Enterprise: int  # = 0
    Main: int  # = 1
    Partial: int  # = 2
class ProfileManager:
    """.NET: Autodesk.AutoCAD.Internal.Windows.ProfileManager"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetProfileNode(pNode: _com_ptr_t<_com_IIID<MSXML::IXMLDOMNode\,\&_GUID_2933bf80_7b36_11d2_b20e_00c04f983e60> >, pszNodePath: str, bCreateIfNotExists: bool, bCurrentProfile: bool) -> bool: ...
    @staticmethod
    def LoadData(sNodePath: str, sWSName: str, bCurrentProfile: bool) -> str: ...
    @staticmethod
    def LoadHideableDialogSettingsDictionary() -> bool: ...
    @staticmethod
    def SaveData(sXmlData: str, sNodePath: str, sWorkspaceName: str, bCurrentProfile: bool) -> bool: ...
    @staticmethod
    def SaveHideableDialogSettingsDictionary() -> bool: ...

class RibbonData:
    """.NET: Autodesk.AutoCAD.Internal.Windows.RibbonData"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def CreateHwndControl(sControlName: str, sModule: str, hwndParent: IntPtr) -> IntPtr: ...
    @staticmethod
    def CreateInvalidHwndControl(hWndParent: IntPtr) -> IntPtr: ...
    @staticmethod
    def GetDefaultToolTipContentSources() -> Collection: ...
    @staticmethod
    def GetMenuGroups() -> List: ...
    @staticmethod
    def GetProfileStorageFilename() -> str: ...
    @staticmethod
    def GetWindowSize(hWnd: IntPtr) -> Size: ...
    @staticmethod
    def Load(sImage: str, sModule: str, sGroupName: str, bSmall: bool) -> ImageSource: ...
    @staticmethod
    def LoadXml(sNodeName: str, sWSName: str) -> str: ...
    @staticmethod
    def SaveXml(sData: str, sWSName: str) -> bool: ...

class RibbonMenuMacro:
    """.NET: Autodesk.AutoCAD.Internal.Windows.RibbonMenuMacro"""
    def __init__(self, *args) -> None: ...
    ToolTipData: CommandToolTipData
    LargeImage: ImageSource
    SmallImage: ImageSource
    LargeImageStr: str
    SmallImageStr: str
    UserData: str
    UserTag: str
    Shortcut: str
    CLICommand: str
    Command: str
    ElementID: str
    Name: str
