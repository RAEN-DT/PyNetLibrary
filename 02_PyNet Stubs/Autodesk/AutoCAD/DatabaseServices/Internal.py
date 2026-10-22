# Auto-generated — Civil 26 — Autodesk.AutoCAD.DatabaseServices.Internal

class CompareReturnStatus:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.Internal.CompareReturnStatus"""
    def __init__(self, *args) -> None: ...
    UnableToCompare: int  # = 0
    HistoryCompare: int  # = 1
    RawBinaryCompare: int  # = 2
class DcDocsFile:
    """.NET: Autodesk.AutoCAD.DatabaseServices.Internal.DcDocsFile"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def getPermissions(sFilepath: str) -> Permissions: ...
    @staticmethod
    def isDCDOCSFileSource(sFilepath: str) -> bool: ...

class DrawingCompare:
    """.NET: Autodesk.AutoCAD.DatabaseServices.Internal.DrawingCompare"""
    def __init__(self, *args) -> None: ...
    def CompareDwgFiles(self, file1name: str, file2name: str) -> CompareReturnStatus: ...
    def OnDiffDetected(self, drawingId: int, handle: int, changeType: int) -> None: ...

class FieldEngine:
    """.NET: Autodesk.AutoCAD.DatabaseServices.Internal.FieldEngine"""
    def __init__(self, *args) -> None: ...
    EvaluationOption: int

class ObjectDiffEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Internal.ObjectDiffEventArgs"""
    def __init__(self, *args) -> None: ...
    ChangeType: int
    DrawingId: int
    ObjHandle: Handle

class ObjectDiffEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.Internal.ObjectDiffEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: ObjectDiffEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: ObjectDiffEventArgs) -> None: ...

class Permissions:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.Internal.Permissions"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    View: int  # = 1
    Create: int  # = 2
    Delete: int  # = 4
    Rename: int  # = 8
    Move: int  # = 16
    Edit: int  # = 32
    Publish: int  # = 64
    Download: int  # = 128
    Collaborate: int  # = 256
    Control: int  # = 512
    AdminAccess: int  # = 1024
    All: int  # = 2047
