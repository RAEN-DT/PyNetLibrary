# Auto-generated — Rhino 8 — Eto.Threading

class Thread(Widget):
    """.NET: Eto.Threading.Thread"""
    def __init__(self, *args) -> None: ...
    CurrentThread: Thread
    MainThread: Thread
    IsAlive: bool
    IsMain: bool
    IsMainThread: bool
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    def Abort(self, ) -> None: ...
    def Start(self, ) -> None: ...
