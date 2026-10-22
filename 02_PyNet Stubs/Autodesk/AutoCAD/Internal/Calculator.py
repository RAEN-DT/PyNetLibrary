# Auto-generated — Civil 26 — Autodesk.AutoCAD.Internal.Calculator

class AngleUnitsEnum:
    """.NET enum: Autodesk.AutoCAD.Internal.Calculator.AngleUnitsEnum"""
    def __init__(self, *args) -> None: ...
    Degree: int  # = 0
    DegreeMinSec: int  # = 1
    Grad: int  # = 2
    Radian: int  # = 3
    Surveyor: int  # = 4
    None_: int  # = -1
class CalcContext(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Internal.Calculator.CalcContext"""
    def __init__(self, *args) -> None: ...
    AngleUnits: AngleUnitsEnum
    HostServices: CalcHostServices
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class CalcEngine(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Internal.Calculator.CalcEngine"""
    def __init__(self, *args) -> None: ...
    GlobalVariableCollection: CalcGlobalVariableBag
    GlobalVariableServices: CalcGlobalVariableServices
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddGlobalVariable(self, variableName: str, variableValue: CalcValueType) -> bool: ...
    def EvaluateExpression(self, expression: str, context: CalcContext, result: CalcResult) -> bool: ...
    def EvaluateExpressionDisableSnap(self, expression: str, context: CalcContext, result: CalcResult) -> bool: ...
    @staticmethod
    def GetEngine() -> CalcEngine: ...
    def RemoveGlobalVariable(self, variableName: str) -> bool: ...

class CalcGlobalVariableBag(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Internal.Calculator.CalcGlobalVariableBag"""
    def __init__(self, *args) -> None: ...
    Current: object
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetEnumerator(self, ) -> IEnumerator: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class CalcGlobalVariableServices(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Internal.Calculator.CalcGlobalVariableServices"""
    def __init__(self, *args) -> None: ...
    GlobalVariableModifiedEvent: OnGlobalVariableModifiedHandler
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class CalcHostServices(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Internal.Calculator.CalcHostServices"""
    def __init__(self, *args) -> None: ...
    FuncEpilogEvent: OnInteractiveFunctionEpilogEventHandler
    FuncPrologEvent: OnInteractiveFunctionPrologEventHandler
    WriteStringEvent: OnWriteStringEventHandler
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetQCState(self, value: bool) -> None: ...

class CalcResult(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Internal.Calculator.CalcResult"""
    def __init__(self, *args) -> None: ...
    DWGResultString: str
    ResultString: str
    Result: CalcValueType
    Type: ValueTypeEnum
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class CalcValueType:
    """.NET: Autodesk.AutoCAD.Internal.Calculator.CalcValueType"""
    def __init__(self, *args) -> None: ...
    DistanceUnitType: DistanceBaseUnitType
    DistanceUnit: float
    R: float
    V: XYZPoint
    Type: ValueTypeEnum
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    @staticmethod
    def Parse(string: str) -> CalcValueType: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class FuncPrologEpilogEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.Internal.Calculator.FuncPrologEpilogEventArgs"""
    def __init__(self, *args) -> None: ...
    ...

class GlobalVariable(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Internal.Calculator.GlobalVariable"""
    def __init__(self, *args) -> None: ...
    Value: CalcValueType
    Name: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class GlobalVariableEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.Internal.Calculator.GlobalVariableEventArgs"""
    def __init__(self, *args) -> None: ...
    ...

class IOStringEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.Internal.Calculator.IOStringEventArgs"""
    def __init__(self, *args) -> None: ...
    IOString: str

class OnGlobalVariableModifiedHandler:
    """.NET: Autodesk.AutoCAD.Internal.Calculator.OnGlobalVariableModifiedHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, e: GlobalVariableEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, e: GlobalVariableEventArgs) -> None: ...

class OnInteractiveFunctionEpilogEventHandler:
    """.NET: Autodesk.AutoCAD.Internal.Calculator.OnInteractiveFunctionEpilogEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, e: FuncPrologEpilogEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, e: FuncPrologEpilogEventArgs) -> None: ...

class OnInteractiveFunctionPrologEventHandler:
    """.NET: Autodesk.AutoCAD.Internal.Calculator.OnInteractiveFunctionPrologEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, e: FuncPrologEpilogEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, e: FuncPrologEpilogEventArgs) -> None: ...

class OnWriteStringEventHandler:
    """.NET: Autodesk.AutoCAD.Internal.Calculator.OnWriteStringEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, e: IOStringEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, e: IOStringEventArgs) -> None: ...

class Unit:
    """.NET: Autodesk.AutoCAD.Internal.Calculator.Unit"""
    def __init__(self, *args) -> None: ...
    ...

class ValueTypeEnum:
    """.NET enum: Autodesk.AutoCAD.Internal.Calculator.ValueTypeEnum"""
    def __init__(self, *args) -> None: ...
    VectorType: int  # = 0
    RealType: int  # = 1
    IntType: int  # = 2
    NoType: int  # = 3
class XYZPoint:
    """.NET: Autodesk.AutoCAD.Internal.Calculator.XYZPoint"""
    def __init__(self, *args) -> None: ...
    Z: float
    Y: float
    X: float
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
