# Auto-generated — Rhino 8 — Rhino.UI.Internal

class BitmapHelpers:
    """.NET: Rhino.UI.Internal.BitmapHelpers"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def DrawDiamond(bmpSize: Size, drawColor: Color, outlineColor: Color) -> Bitmap: ...
    @staticmethod
    def DrawSquare(bmpSize: Size, drawColor: Color, outlineColor: Color) -> Bitmap: ...
    @staticmethod
    def DrawSquareGraphics(graphics: Graphics, rect: RectangleF, drawColor: Color, outlineColor: Color) -> None: ...
    @staticmethod
    def DrawStarOverlay(image: Bitmap, numberOfStarPoints: int) -> Bitmap: ...
    @staticmethod
    def GetHatchPreviewBmp(size: Size, drawColor: Color, outlineColor: Color, rotationAngle: int, hatchPattern: HatchPattern) -> Bitmap: ...
    @staticmethod
    def GetLinetypePreview(size: Size, lt: Linetype) -> Bitmap: ...

class DwgOptions(ViewModel):
    """.NET: Rhino.UI.Internal.DwgOptions"""
    def __init__(self, *args) -> None: ...
    AcadVersionDropdownIndex: int
    AcadVersion: eVersion
    Name: str
    WriteLinesAsDropdownIndex: int
    WriteLinesAs: eWriteAs
    WriteArcsAsDropdownIndex: int
    WriteArcsAs: eWriteAs
    WriteSplinesAsDropdownIndex: int
    WriteSplinesAs: eWriteAs
    WritePolylinesAsDropdownIndex: int
    WritePolylinesAs: eWriteAs
    WritePolycurvesAsDropdownIndex: int
    WritePolycurvesAs: eWriteAs
    WriteSurfacesAsDropdownIndex: int
    WriteSurfacesAs: eWriteAs
    WriteMeshesAsDropdownIndex: int
    WriteMeshesAs: eWriteAs
    SplitPolycurves: bool
    SplitSplines: bool
    CurveUseMaxAngle: bool
    CurveMaxAngleDegrees: float
    CurveUseChordHeight: bool
    CurveChordHeight: float
    CurveUseSegmentLength: bool
    CurveSegmentLength: float
    FullLayerPathIndex: int
    FullLayerPath: bool
    NoDxfHeader: bool
    Simplify: bool
    SimplifyTolerance: float
    MinPointDistance: float
    FlattenDropdownIndex: int
    Flatten: eFlatten
    IsDefault: bool
    PreserveArcNormalsIndex: int
    PreserveArcNormals: bool
    UseLwPolylines: bool
    ColorMethodIndex: int
    ColorMethod: eColorMethod
    Index: int
    SortIndex: int
    Deleted: bool
    ModelUnitSystem: UnitSystem
    PageUnitSystem: UnitSystem
    ModelDistanceDisplayMode: DistanceDisplayMode
    PageDistanceDisplayMode: DistanceDisplayMode
    ModelDistanceDisplayPrecision: int
    PageDistanceDisplayPrecision: int
    @staticmethod
    def ColorMethodList() -> List: ...
    @staticmethod
    def FlattenList() -> List: ...
    @staticmethod
    def FlattenUIName(input: eFlatten) -> str: ...
    @staticmethod
    def LocalizedDefaultName() -> str: ...
    @staticmethod
    def VersionUIName(input: eVersion) -> str: ...
    @staticmethod
    def VersionsList() -> List: ...
    @staticmethod
    def WriteArcsAsList(ver: eVersion) -> List: ...
    @staticmethod
    def WriteAsUIName(input: eWriteAs) -> str: ...
    @staticmethod
    def WriteLinesAsList(ver: eVersion) -> List: ...
    @staticmethod
    def WriteMeshesAsList() -> List: ...
    @staticmethod
    def WritePolycurvesAsList(ver: eVersion) -> List: ...
    @staticmethod
    def WritePolylinesAsList(ver: eVersion) -> List: ...
    @staticmethod
    def WriteSplinesAsList(ver: eVersion) -> List: ...
    @staticmethod
    def WriteSurfacesAsList() -> List: ...
    def WriteToSettings(self, optionsettings: PersistentSettings) -> bool: ...
