# Auto-generated — Rhino 8 — Rhino.UI.Gumball

class GumballAppearanceSettings:
    """.NET: Rhino.UI.Gumball.GumballAppearanceSettings"""
    def __init__(self, *args) -> None: ...
    RelocateEnabled: bool
    MenuEnabled: bool
    TranslateXEnabled: bool
    TranslateYEnabled: bool
    TranslateZEnabled: bool
    TranslateXYEnabled: bool
    TranslateYZEnabled: bool
    TranslateZXEnabled: bool
    RotateXEnabled: bool
    RotateYEnabled: bool
    RotateZEnabled: bool
    ScaleXEnabled: bool
    ScaleYEnabled: bool
    ScaleZEnabled: bool
    FreeTranslate: int
    ColorX: Color
    ColorY: Color
    ColorZ: Color
    ColorMenuButton: Color
    Radius: int
    ArrowHeadLength: int
    ArrowHeadWidth: int
    ScaleGripSize: int
    PlanarTranslationGripCorner: int
    PlanarTranslationGripSize: int
    AxisThickness: int
    ArcThickness: int
    MenuDistance: int
    MenuSize: int

class GumballDisplayConduit:
    """.NET: Rhino.UI.Gumball.GumballDisplayConduit"""
    def __init__(self, *args) -> None: ...
    Enabled: bool
    InRelocate: bool
    PreTransform: Transform
    GumballTransform: Transform
    TotalTransform: Transform
    BaseGumball: GumballObject
    Gumball: GumballObject
    PickResult: GumballPickResult
    def CheckShiftAndControlKeys(self, ) -> None: ...
    def Dispose(self, ) -> None: ...
    def PickGumball(self, pickContext: PickContext, getPoint: GetPoint) -> bool: ...
    def SetBaseGumball(self, gumball: GumballObject, appearanceSettings: GumballAppearanceSettings) -> None: ...
    def UpdateGumball(self, point: Point3d, worldLine: Line) -> bool: ...

class GumballFrame:
    """.NET: Rhino.UI.Gumball.GumballFrame"""
    def __init__(self, *args) -> None: ...
    Plane: Plane
    ScaleGripDistance: Vector3d
    ScaleMode: GumballScaleMode

class GumballMode:
    """.NET: Rhino.UI.Gumball.GumballMode"""
    def __init__(self, *args) -> None: ...
    ...

class GumballObject:
    """.NET: Rhino.UI.Gumball.GumballObject"""
    def __init__(self, *args) -> None: ...
    Frame: GumballFrame
    def Dispose(self, ) -> None: ...
    def SetFromArc(self, arc: Arc) -> bool: ...
    def SetFromBoundingBox(self, frame: Plane, frameBoundingBox: BoundingBox) -> bool: ...
    def SetFromCircle(self, circle: Circle) -> bool: ...
    def SetFromCurve(self, curve: Curve) -> bool: ...
    def SetFromEllipse(self, ellipse: Ellipse) -> bool: ...
    def SetFromExtrusion(self, extrusion: Extrusion) -> bool: ...
    def SetFromHatch(self, hatch: Hatch) -> bool: ...
    def SetFromLight(self, light: Light) -> bool: ...
    def SetFromLine(self, line: Line) -> bool: ...
    def SetFromPlane(self, plane: Plane) -> bool: ...

class GumballPickResult:
    """.NET: Rhino.UI.Gumball.GumballPickResult"""
    def __init__(self, *args) -> None: ...
    Mode: GumballMode
    def SetToDefault(self, ) -> None: ...

class GumballScaleMode:
    """.NET: Rhino.UI.Gumball.GumballScaleMode"""
    def __init__(self, *args) -> None: ...
    ...
