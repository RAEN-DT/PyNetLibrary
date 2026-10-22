# Auto-generated — Civil 26 — Autodesk.Civil.DataShortcuts

class DataShortcutEntityType:
    """.NET enum: Autodesk.Civil.DataShortcuts.DataShortcutEntityType"""
    def __init__(self, *args) -> None: ...
    Unknown: int  # = 0
    Alignment: int  # = 1
    PipeNetwork: int  # = 2
    PressurePipeNetwork: int  # = 3
    Corridor: int  # = 4
    Profile: int  # = 5
    SampleLineGroup: int  # = 6
    ViewFrameGroup: int  # = 7
    Surface: int  # = 8
    Pond: int  # = 9
class DataShortcutKey(DisposableWrapper):
    """.NET: Autodesk.Civil.DataShortcuts.DataShortcutKey"""
    def __init__(self, *args) -> None: ...
    IsSourceDrawingExistent: bool
    SourceDrawing: str
    HandleHigh: int
    HandleLow: int
    Type: DataShortcutEntityType
    Name: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
