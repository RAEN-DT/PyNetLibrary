# Auto-generated — Civil 26 — Autodesk.AutoCAD.Internal.PreviousInput

class AcPiMonitorReactorImpl:
    """.NET: Autodesk.AutoCAD.Internal.PreviousInput.AcPiMonitorReactorImpl"""
    def __init__(self, *args) -> None: ...
    ...

class CommandLineMonitor:
    """.NET: Autodesk.AutoCAD.Internal.PreviousInput.CommandLineMonitor"""
    def __init__(self, *args) -> None: ...
    CurrentInputControlFlags: InputControlFlags
    CurrentSSGetConsumedPickfirst: bool
    CurrentSSGetIsManual: bool
    CurrentSSGetKeywordsUsed: ArrayList
    CurrentInitgetKeywords: str
    LastCommandName: str
    LastNotifiedSSGetCount: int
    CurrentSSGetCount: int
    CurrentNestingCount: int
    CurrentPointOut2dFlag: bool
    CurrentPointOut2d: ValueType
    CurrentPointOutFlag: bool
    CurrentPointOut: ValueType
    CurrentDoubleOut: float
    CurrentIntOut: int
    CurrentStringOut: str
    CurrentSSControlsIn: str
    CurrentKeywordsIn: str
    CurrentPointInFlag: bool
    CurrentPointIn: ValueType
    CurrentInitgetFlags: int
    CurrentModes: InputModes
    CurrentMode: InputModes
    CurrentReturnStatus: PromptStatus
    CurrentPrompt: str
    CurrentCommandName: str
    def EnableSsGetFilter(self, on: bool) -> None: ...

class CommandLineMonitorServices:
    """.NET: Autodesk.AutoCAD.Internal.PreviousInput.CommandLineMonitorServices"""
    def __init__(self, *args) -> None: ...
    def ActiveCommandFlags(self, ) -> CommandFlags: ...
    def CommandActiveBits(self, ) -> int: ...
    def CommandNestedDepth(self, ) -> int: ...
    def GetCommandLineMonitor(self, doc: Document) -> CommandLineMonitor: ...
    def GetLocalCommandName(self, globalCmdName: str) -> str: ...
    @staticmethod
    def Instance() -> CommandLineMonitorServices: ...
    def IsCurrentCommandTransparent(self, ) -> bool: ...

class GetAngleEventHandler:
    """.NET: Autodesk.AutoCAD.Internal.PreviousInput.GetAngleEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: GetInputEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: GetInputEventArgs) -> None: ...

class GetDistanceEventHandler:
    """.NET: Autodesk.AutoCAD.Internal.PreviousInput.GetDistanceEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: GetInputEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: GetInputEventArgs) -> None: ...

class GetInputEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.Internal.PreviousInput.GetInputEventArgs"""
    def __init__(self, *args) -> None: ...
    ReturnStatus: PromptStatus
    Value: object
    Mode: InputModes

class GetInputEventHandler:
    """.NET: Autodesk.AutoCAD.Internal.PreviousInput.GetInputEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: GetInputEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: GetInputEventArgs) -> None: ...

class InputControlFlags:
    """.NET enum: Autodesk.AutoCAD.Internal.PreviousInput.InputControlFlags"""
    def __init__(self, *args) -> None: ...
    udNONE: int  # = 0
    udBASE: int  # = 1
    udORTHO: int  # = 2
    udWNOSORT: int  # = 2
    udNULLOK: int  # = 4
    udKWORD: int  # = 8
    udDRAG: int  # = 16
    udSILENTETX: int  # = 32
    udCURSOR: int  # = 64
    udMSG: int  # = 128
    udNOLAST: int  # = 256
    udNOLIM: int  # = 512
    udOTHER: int  # = 1024
    udNOZERO: int  # = 2048
    udNONEG: int  # = 4096
    udENTITY: int  # = 8192
    udGETZ: int  # = 16384
    udNORANGEMSG: int  # = 32768
    udNOPFILT: int  # = 65536
    udNOOSNAP: int  # = 131072
    udFLATCUR: int  # = 262144
    udDISPLPT: int  # = 524288
    udMSGNUM: int  # = 1048576
    udNOSMODE: int  # = 2097152
    ud2DDIST: int  # = 4194304
    udRESCAN: int  # = 8388608
    udPOINTUP: int  # = 16777216
    udANYBLANK: int  # = 33554432
    udFIRSTBLANK: int  # = 67108864
    udIGNOREETX: int  # = 134217728
    udPOINTOK: int  # = 268435456
    udLABELOK: int  # = 536870912
    udBKSL: int  # = 1073741824
    udXCTL: int  # = -2147483648
class InputModes:
    """.NET enum: Autodesk.AutoCAD.Internal.PreviousInput.InputModes"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Point: int  # = 1
    Angle: int  # = 2
    Distance: int  # = 4
    Orientation: int  # = 8
    Corner: int  # = 16
    ScaleFactor: int  # = 32
    String: int  # = 64
    kword: int  # = 128
    Integer: int  # = 256
    Color: int  # = 512
    Real: int  # = 2048
    EntSel: int  # = 4096
    Nentsel: int  # = 8192
    SSGet: int  # = 16384
    Drag: int  # = 32768
    Cmd: int  # = 65536
    UnknownCmd: int  # = 131072
    Vector: int  # = 262144
    ScaleFactor2: int  # = 524288
    DynDimGetPoint: int  # = 1048576
    RawAngle: int  # = 8388608
    AllGetInput: int  # = 16284671
class InputStringEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.Internal.PreviousInput.InputStringEventArgs"""
    def __init__(self, *args) -> None: ...
    Value: str

class InputStringEventHandler:
    """.NET: Autodesk.AutoCAD.Internal.PreviousInput.InputStringEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: InputStringEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: InputStringEventArgs) -> None: ...

class SelectEventHandler:
    """.NET: Autodesk.AutoCAD.Internal.PreviousInput.SelectEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: EventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: EventArgs) -> None: ...

class SelectOperationEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.Internal.PreviousInput.SelectOperationEventArgs"""
    def __init__(self, *args) -> None: ...
    GroupName: str
    SelectionFlags: int
    IsCrossingBox: bool
    IsCancel: bool
    Points: Point3dCollection
    IsSubSelection: bool
    IsAdding: bool
    SelectionMode: SelectionMode

class SelectOperationEventHandler:
    """.NET: Autodesk.AutoCAD.Internal.PreviousInput.SelectOperationEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: SelectOperationEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: SelectOperationEventArgs) -> None: ...
