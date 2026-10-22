# Auto-generated — Civil 26 — Autodesk.AutoCAD.GraphicsInterface

class ArcType:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.ArcType"""
    def __init__(self, *args) -> None: ...
    ArcSimple: int  # = 0
    ArcSector: int  # = 1
    ArcChord: int  # = 2
class AttenuationType:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.AttenuationType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    InverseLinear: int  # = 1
    InverseSquare: int  # = 2
class AutoTransform:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.AutoTransform"""
    def __init__(self, *args) -> None: ...
    InheritAutoTransform: int  # = 0
    None_: int  # = 1
    TransformObject: int  # = 2
    Model: int  # = 4
class ChannelFlags:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.ChannelFlags"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    UseDiffuse: int  # = 1
    UseSpecular: int  # = 2
    UseReflection: int  # = 4
    UseOpacity: int  # = 8
    UseBump: int  # = 16
    UseRefraction: int  # = 32
    UseAll: int  # = 63
class ClipBoundary(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ClipBoundary"""
    def __init__(self, *args) -> None: ...
    DrawBoundary: bool
    BackClipZ: float
    FrontClipZ: float
    ClippingBack: bool
    ClippingFront: bool
    TransformInverseBlockRefXForm: Matrix3d
    TransformToClipSpace: Matrix3d
    Point: Point3d
    NormalVector: Vector3d
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetAptPoints(self, ) -> Point2dCollection: ...
    def SetAptPoints(self, point: Point2dCollection) -> None: ...

class ColorRGB:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ColorRGB"""
    def __init__(self, *args) -> None: ...
    Blue: float
    Green: float
    Red: float

class ColorRGBA:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ColorRGBA"""
    def __init__(self, *args) -> None: ...
    Alpha: float
    Blue: float
    Green: float
    Red: float

class CommonDraw(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.CommonDraw"""
    def __init__(self, *args) -> None: ...
    NumberOfIsolines: int
    IsDragging: bool
    Context: Context
    RawGeometry: Geometry
    SubEntityTraits: SubEntityTraits
    RegenAbort: bool
    RegenType: RegenType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Deviation(self, deviationType: DeviationType, pointOnCurve: Point3d) -> float: ...

class Context(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.Context"""
    def __init__(self, *args) -> None: ...
    SupportsCurveTrait: bool
    SupportsTrueTypeText: bool
    ByBlockPlotStyleNameId: ObjectId
    ByBlockLineWeight: LineWeight
    EffectiveColor: EntityColor
    IsNesting: bool
    IsBoundaryClipping: bool
    Database: Database
    IsPlotGeneration: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def DisableFastMoveDrag(self, ) -> None: ...

class ContextualColors(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ContextualColors"""
    def __init__(self, *args) -> None: ...
    LightDistanceColor: Color
    LightShapeColor: Color
    WebMeshMissingColor: Color
    WebMeshColor: Color
    CameraClipping: int
    CameraFrustrum: int
    CameraGlyphs: int
    LightEndLimit: int
    LightStartLimit: int
    LightFalloff: int
    LightHotspot: int
    LightGlyphs: int
    GridAxisLineTintXYZ: int
    GridMinorLineTintXYZ: int
    GridMajorLineTintXYZ: int
    GridAxisLines: int
    GridMinorLines: int
    GridMajorLines: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def FlagsSet(self, flag: int) -> bool: ...
    def SetContextFlags(self, flag: int, set: bool) -> None: ...

class DefaultLightingType:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.DefaultLightingType"""
    def __init__(self, *args) -> None: ...
    OneDistantLight: int  # = 0
    TwoDistantLights: int  # = 1
class DeviationType:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.DeviationType"""
    def __init__(self, *args) -> None: ...
    MaxDevForCircle: int  # = 0
    MaxDevForCurve: int  # = 1
    MaxDevForBoundary: int  # = 2
    MaxDevForIsoline: int  # = 3
    MaxDevForFacet: int  # = 4
    MaxDevForHatch: int  # = 5
class DistantLightTraits(StandardLightTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.DistantLightTraits"""
    def __init__(self, *args) -> None: ...
    SkyParameters: SkyParameters
    LampColor: ColorRGB
    PhysicalIntensity: float
    IsSunlight: bool
    LightDirection: Vector3d
    Shadow: ShadowParameters
    LightColor: Color
    Intensity: float
    On: bool
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class DrawFlags:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.DrawFlags"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    DrawBackfaces: int  # = 1
    DrawNoLineWeight: int  # = 32
    DrawFillTextBoundaryStart: int  # = 256
    DrawFillTextBoundaryEnd: int  # = 512
class DrawStream(Drawable):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.DrawStream"""
    def __init__(self, *args) -> None: ...
    Owner: Drawable
    IsValid: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    Id: ObjectId
    IsPersistent: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Drawable(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.Drawable"""
    def __init__(self, *args) -> None: ...
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    Id: ObjectId
    IsPersistent: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetAttributes(self, traits: DrawableTraits) -> int: ...
    def ViewportDraw(self, vd: ViewportDraw) -> None: ...
    def ViewportDrawLogicalFlags(self, vd: ViewportDraw) -> int: ...
    def WorldDraw(self, wd: WorldDraw) -> bool: ...

class DrawableAttributes:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.DrawableAttributes"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    IsAnEntity: int  # = 1
    UsesNesting: int  # = 2
    IsCompoundObject: int  # = 4
    ViewIndependentViewportDraw: int  # = 8
    IsInvisible: int  # = 16
    HasAttributes: int  # = 32
    RegenTypeDependentGeometry: int  # = 64
    IsDimension: int  # = 133
    RegenDraw: int  # = 256
    StandardDisplaySingleLOD: int  # = 512
    ShadedDisplaySingleLOD: int  # = 1024
    ViewDependentViewportDraw: int  # = 2048
    BlockDependentViewportDraw: int  # = 4096
    IsExternalReference: int  # = 8192
    NotPlottable: int  # = 16384
class DrawableOverrule(Overrule):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.DrawableOverrule"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetAttributes(self, drawable: Drawable, traits: DrawableTraits) -> int: ...
    def SetCustomFilter(self, ) -> None: ...
    def SetExtensionDictionaryEntryFilter(self, entryName: str) -> None: ...
    def SetIdFilter(self, ids: list) -> None: ...
    def SetNoFilter(self, ) -> None: ...
    def SetXDataFilter(self, registeredApplicationName: str) -> None: ...
    def ViewportDraw(self, drawable: Drawable, vd: ViewportDraw) -> None: ...
    def ViewportDrawLogicalFlags(self, drawable: Drawable, vd: ViewportDraw) -> int: ...
    def WorldDraw(self, drawable: Drawable, wd: WorldDraw) -> bool: ...

class DrawableTraits(SubEntityTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.DrawableTraits"""
    def __init__(self, *args) -> None: ...
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddLight(self, lightId: ObjectId) -> None: ...
    def GetHighlightProperty(self, propertyType: HighlightProperty) -> object: ...
    def SetHighlightProperty(self, propertyType: HighlightProperty, value: object) -> None: ...
    def SetupForEntity(self, entity: Entity) -> None: ...

class DrawableType:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.DrawableType"""
    def __init__(self, *args) -> None: ...
    Geometry: int  # = 0
    DistantLight: int  # = 1
    PointLight: int  # = 2
    SpotLight: int  # = 3
    AmbientLight: int  # = 4
    SolidBackground: int  # = 5
    GradientBackground: int  # = 6
    ImageBackground: int  # = 7
    GroundPlaneBackground: int  # = 8
    Viewport: int  # = 9
    WebLight: int  # = 10
    SkyBackground: int  # = 11
    ImageBasedLightingBackground: int  # = 12
class EdgeData:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.EdgeData"""
    def __init__(self, *args) -> None: ...
    def GetColors(self, ) -> list: ...
    def GetLayers(self, ) -> list: ...
    def GetLineTypes(self, ) -> list: ...
    def GetSelectionMarkers(self, ) -> list: ...
    def GetTrueColors(self, ) -> list: ...
    def GetVisibility(self, ) -> list: ...
    def SetColors(self, colors: list) -> None: ...
    def SetLayers(self, layers: list) -> None: ...
    def SetLineTypes(self, lineTypes: list) -> None: ...
    def SetSelectionMarkers(self, selectionMarkers: list) -> None: ...
    def SetTrueColors(self, colors: list) -> None: ...
    def SetVisibility(self, visibility: list) -> None: ...

class ExtendedLightShape:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.ExtendedLightShape"""
    def __init__(self, *args) -> None: ...
    Linear: int  # = 0
    Rectangle: int  # = 1
    Disk: int  # = 2
    Cylinder: int  # = 3
    Sphere: int  # = 4
class ExteriorDaylightMode:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.ExteriorDaylightMode"""
    def __init__(self, *args) -> None: ...
    DaylightOff: int  # = 0
    DaylightOn: int  # = 1
    DaylightAuto: int  # = 2
class FaceData:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.FaceData"""
    def __init__(self, *args) -> None: ...
    def GetColors(self, ) -> list: ...
    def GetLayers(self, ) -> list: ...
    def GetMappers(self, ) -> list: ...
    def GetMaterials(self, ) -> list: ...
    def GetNormalVectors(self, ) -> list: ...
    def GetSelectionMarkers(self, ) -> list: ...
    def GetTransparency(self, ) -> list: ...
    def GetTrueColors(self, ) -> list: ...
    def GetVisibility(self, ) -> list: ...
    def SetColors(self, colors: list) -> None: ...
    def SetLayers(self, layers: list) -> None: ...
    def SetMappers(self, mappers: list) -> None: ...
    def SetMaterials(self, materials: list) -> None: ...
    def SetNormalVectors(self, normal: list) -> None: ...
    def SetSelectionMarkers(self, selectionMarker: list) -> None: ...
    def SetTransparency(self, transparency: list) -> None: ...
    def SetTrueColors(self, colors: list) -> None: ...
    def SetVisibility(self, visibility: list) -> None: ...

class Fill(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.Fill"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class FillType:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.FillType"""
    def __init__(self, *args) -> None: ...
    FillAlways: int  # = 1
    FillNever: int  # = 2
class FinalGatherMode:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.FinalGatherMode"""
    def __init__(self, *args) -> None: ...
    FinalGatherNone: int  # = 0
    FinalGatherCast: int  # = 1
    FinalGatherReceive: int  # = 2
    FinalGatherCastAndReceive: int  # = 3
class FontDescriptor:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.FontDescriptor"""
    def __init__(self, *args) -> None: ...
    PitchAndFamily: int
    CharacterSet: int
    Italic: bool
    Bold: bool
    TypeFace: str
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class FrontAndBackClipping:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.FrontAndBackClipping"""
    def __init__(self, *args) -> None: ...
    Back: float
    Front: float
    ClipBack: bool
    ClipFront: bool
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def IsEqualTo(self, a: FrontAndBackClipping, tolerance: Tolerance) -> bool: ...

class GdiDrawObject(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.GdiDrawObject"""
    def __init__(self, *args) -> None: ...
    Height: int
    Width: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Draw(self, hDC: IntPtr, bounds: Rectangle) -> bool: ...

class GenericTexture(ProceduralTexture):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.GenericTexture"""
    def __init__(self, *args) -> None: ...
    Definition: object
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Clone(self, ) -> GenericTexture: ...
    def CopyFrom(self, pSrc: GenericTexture) -> None: ...
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def Set(self, value: GenericTexture) -> None: ...

class Geometry(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.Geometry"""
    def __init__(self, *args) -> None: ...
    WorldToModelTransform: Matrix3d
    ModelToWorldTransform: Matrix3d
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Circle(self, firstPoint: Point3d, secondPoint: Point3d, thirdPoint: Point3d) -> bool: ...
    def CircularArc(self, center: Point3d, radius: float, normal: Vector3d, startVector: Vector3d, sweepAngle: float, arcType: ArcType) -> bool: ...
    def Curve(self, curve3d: Curve3d) -> bool: ...
    def Draw(self, value: Drawable) -> bool: ...
    def Edge(self, e: Curve2dCollection) -> bool: ...
    def EllipticalArc(self, center: Point3d, normal: Vector3d, majorAxisLength: float, minorAxisLength: float, startDegreeInRads: float, endDegreeInRads: float, tiltDegreeInRads: float, arcType: ArcType) -> bool: ...
    def Image(self, imageSource: ImageBGRA32, position: Point3d, u: Vector3d, v: Vector3d, transparencyMode: TransparencyMode) -> bool: ...
    def Mesh(self, rows: int, columns: int, points: Point3dCollection, edgeData: EdgeData, faceData: FaceData, vertexData: VertexData, bAutoGenerateNormals: bool) -> bool: ...
    def OwnerDraw(self, gdiDrawObject: GdiDrawObject, position: Point3d, u: Vector3d, v: Vector3d) -> bool: ...
    def PolyPolygon(self, numPolygonPositions: UInt32Collection, polygonPositions: Point3dCollection, numPolygonPoints: UInt32Collection, polygonPoints: Point3dCollection, outlineColors: EntityColorCollection, outlineTypes: LinetypeCollection, fillColors: EntityColorCollection, fillOpacities: TransparencyCollection) -> bool: ...
    def PolyPolyline(self, polylineCollection: PolylineCollection) -> bool: ...
    def Polygon(self, points: Point3dCollection) -> bool: ...
    def Polyline(self, value: Polyline, fromIndex: int, segments: int) -> bool: ...
    def Polypoint(self, points: Point3dCollection, normals: Vector3dCollection, subentityMarkers: IntPtrCollection) -> bool: ...
    def PopClipBoundary(self, ) -> None: ...
    def PopModelTransform(self, ) -> bool: ...
    def PushClipBoundary(self, boundary: ClipBoundary) -> bool: ...
    def PushModelTransform(self, matrix: Matrix3d) -> bool: ...
    def PushOrientationTransform(self, behavior: OrientationBehavior) -> Matrix3d: ...
    def PushPositionTransform(self, behavior: PositionBehavior, offset: Point2d) -> Matrix3d: ...
    def PushScaleTransform(self, behavior: ScaleBehavior, extents: Point2d) -> Matrix3d: ...
    def Ray(self, point1: Point3d, point2: Point3d) -> bool: ...
    def RowOfDots(self, count: int, start: Point3d, step: Vector3d) -> bool: ...
    def Shell(self, points: Point3dCollection, faces: IntegerCollection, edgeData: EdgeData, faceData: FaceData, vertexData: VertexData, bAutoGenerateNormals: bool) -> bool: ...
    def Text(self, position: Point3d, normal: Vector3d, direction: Vector3d, height: float, width: float, oblique: float, message: str) -> bool: ...
    def WorldLine(self, startPoint: Point3d, endPoint: Point3d) -> bool: ...
    def Xline(self, point1: Point3d, point2: Point3d) -> bool: ...

class GlobalIlluminationMode:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.GlobalIlluminationMode"""
    def __init__(self, *args) -> None: ...
    GlobalIlluminationNone: int  # = 0
    GlobalIlluminationCast: int  # = 1
    GlobalIlluminationReceive: int  # = 2
    GlobalIlluminationCastAndReceive: int  # = 3
class Glyph(Drawable):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.Glyph"""
    def __init__(self, *args) -> None: ...
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetLocation(self, point: Point3d) -> None: ...

class GradientBackgroundTraits(NonEntityTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.GradientBackgroundTraits"""
    def __init__(self, *args) -> None: ...
    Rotation: float
    Height: float
    Horizon: float
    ColorBottom: EntityColor
    ColorMiddle: EntityColor
    ColorTop: EntityColor
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class GradientFill(Fill):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.GradientFill"""
    def __init__(self, *args) -> None: ...
    Type: GradientType
    GradientColors: list
    IsAdjustAspect: bool
    GradientShift: float
    GradientAngle: float
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class GradientType:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.GradientType"""
    def __init__(self, *args) -> None: ...
    Linear: int  # = 0
    Cylinder: int  # = 1
    InvCylinder: int  # = 2
    Spherical: int  # = 3
    Hemispherical: int  # = 4
    Curved: int  # = 5
    InvSpherical: int  # = 6
    InvHemispherical: int  # = 7
    InvCurved: int  # = 8
class GroundPlaneBackgroundTraits(NonEntityTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.GroundPlaneBackgroundTraits"""
    def __init__(self, *args) -> None: ...
    ColorGroundPlaneFar: EntityColor
    ColorGroundPlaneNear: EntityColor
    ColorUndergroundAzimuth: EntityColor
    ColorUndergroundHorizon: EntityColor
    ColorSkyHorizon: EntityColor
    ColorSkyZenith: EntityColor
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class HatchPattern(Fill):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.HatchPattern"""
    def __init__(self, *args) -> None: ...
    PatternLines: list
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class HatchPatternDefinition(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.HatchPatternDefinition"""
    def __init__(self, *args) -> None: ...
    DashList: DoubleCollection
    OffsetY: float
    OffsetX: float
    BaseY: float
    BaseX: float
    Angle: float
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class HighlightStyle:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.HighlightStyle"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Custom: int  # = 1
    DashedAndThicken: int  # = 2
    Dim: int  # = 3
    ThickDim: int  # = 4
    Glow: int  # = 5
class IBLBackgroundTraits(NonEntityTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.IBLBackgroundTraits"""
    def __init__(self, *args) -> None: ...
    SecondaryBackground: ObjectId
    DisplayImage: bool
    Rotation: float
    IBLImageName: str
    Enable: bool
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class IlluminationModel:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.IlluminationModel"""
    def __init__(self, *args) -> None: ...
    BlinnShader: int  # = 0
    MetalShader: int  # = 1
class ImageBGRA32(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ImageBGRA32"""
    def __init__(self, *args) -> None: ...
    Image: IntPtr
    Height: int
    Width: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ImageBackgroundTraits(NonEntityTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ImageBackgroundTraits"""
    def __init__(self, *args) -> None: ...
    YScale: float
    XScale: float
    YOffset: float
    XOffset: float
    UseTiling: bool
    MaintainAspectRatio: bool
    FitToScreen: bool
    ImageFilename: str
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ImageFileTexture(ImageTexture):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ImageFileTexture"""
    def __init__(self, *args) -> None: ...
    SourceFileName: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Clone(self, ) -> object: ...
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class ImageOrg:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.ImageOrg"""
    def __init__(self, *args) -> None: ...
    Bitonal: int  # = 0
    Palette: int  # = 1
    Gray: int  # = 2
    RGBA: int  # = 3
    BGRA: int  # = 4
    ARGB: int  # = 5
    ABGR: int  # = 6
    BGR: int  # = 7
    RGB: int  # = 8
class ImageSource:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.ImageSource"""
    def __init__(self, *args) -> None: ...
    FromDwg: int  # = 0
    FromOleObject: int  # = 1
    FromRender: int  # = 2
class ImageTexture(MaterialTexture):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ImageTexture"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LightAttenuation(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.LightAttenuation"""
    def __init__(self, *args) -> None: ...
    EndLimit: float
    StartLimit: float
    UseLimits: bool
    AttenuationType: AttenuationType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def SetLimits(self, startLimit: float, endLimit: float) -> None: ...

class LightTraits(NonEntityTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.LightTraits"""
    def __init__(self, *args) -> None: ...
    On: bool
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Linetype:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.Linetype"""
    def __init__(self, *args) -> None: ...
    Solid: int  # = 0
    Dashed: int  # = 1
    Dotted: int  # = 2
    DashDot: int  # = 3
    ShortDash: int  # = 4
    MediumDash: int  # = 5
    LongDash: int  # = 6
    ShortDashX2: int  # = 7
    MediumDashX2: int  # = 8
    LongDashX2: int  # = 9
    MediumLongDash: int  # = 10
    MediumDashShortDashShortDash: int  # = 11
    LongDashShortDash: int  # = 12
    LongDashDotDot: int  # = 13
    LongDashDot: int  # = 14
    MediumDashDotShortDashDot: int  # = 15
    SparseDot: int  # = 16
    ISODash: int  # = 17
    ISODashSpace: int  # = 18
    ISOLongDashDot: int  # = 19
    ISOLongDashDoubleDot: int  # = 20
    ISOLongDashTripleDot: int  # = 21
    ISODot: int  # = 22
    ISOLongDashShortDash: int  # = 23
    ISOLongDashDoubleShortDash: int  # = 24
    ISODashDot: int  # = 25
    ISODoubleDashDot: int  # = 26
    ISODashDoubleDot: int  # = 27
    ISODoubleDashDoubleDot: int  # = 28
    ISODashTripleDot: int  # = 29
    ISODoubleDashTripleDot: int  # = 30
    LineTypeNone: int  # = 31
    Solid6PixelsBlank6Pixels: int  # = 32
class LinetypeCollection(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.LinetypeCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: Linetype
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, value: Linetype) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: Linetype) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: Linetype) -> int: ...
    def Insert(self, index: int, value: Linetype) -> None: ...
    def Remove(self, value: Linetype) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class LuminanceMode:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.LuminanceMode"""
    def __init__(self, *args) -> None: ...
    SelfIllumination: int  # = 0
    Luminance: int  # = 1
class MapChannel:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.MapChannel"""
    def __init__(self, *args) -> None: ...
    AllChannels: int  # = 0
    MapChannels: int  # = 1
class MapFilter:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.MapFilter"""
    def __init__(self, *args) -> None: ...
    Default: int  # = 0
    None_: int  # = 1
class Mapper(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.Mapper"""
    def __init__(self, *args) -> None: ...
    VTiling: Tiling
    UTiling: Tiling
    Transform: Matrix3d
    AutoTransform: AutoTransform
    Projection: Projection
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Equals(self, other: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class MarbleTexture(ProceduralTexture):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.MarbleTexture"""
    def __init__(self, *args) -> None: ...
    VeinWidth: float
    VeinSpacing: float
    VeinColor: MaterialColor
    StoneColor: MaterialColor
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Clone(self, ) -> MarbleTexture: ...
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def Set(self, value: MarbleTexture) -> None: ...

class MaterialColor(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.MaterialColor"""
    def __init__(self, *args) -> None: ...
    Color: EntityColor
    Factor: float
    Method: Method
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Equals(self, other: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class MaterialDiffuseComponent:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.MaterialDiffuseComponent"""
    def __init__(self, *args) -> None: ...
    Map: MaterialMap
    Color: MaterialColor
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class MaterialMap(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.MaterialMap"""
    def __init__(self, *args) -> None: ...
    SourceFileName: str
    Mapper: Mapper
    Filter: MapFilter
    BlendFactor: float
    Texture: MaterialTexture
    Source: Source
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Equals(self, other: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class MaterialNormalMapComponent:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.MaterialNormalMapComponent"""
    def __init__(self, *args) -> None: ...
    Strength: float
    Method: NormalMapMethod
    Map: MaterialMap
    def Equals(self, other: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class MaterialOpacityComponent:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.MaterialOpacityComponent"""
    def __init__(self, *args) -> None: ...
    Percentage: float
    Map: MaterialMap
    def Equals(self, other: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class MaterialRefractionComponent:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.MaterialRefractionComponent"""
    def __init__(self, *args) -> None: ...
    Index: float
    Map: MaterialMap
    def Equals(self, other: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class MaterialSpecularComponent:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.MaterialSpecularComponent"""
    def __init__(self, *args) -> None: ...
    Gloss: float
    Map: MaterialMap
    Color: MaterialColor
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class MaterialTexture(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.MaterialTexture"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class MaterialTraits(NonEntityTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.MaterialTraits"""
    def __init__(self, *args) -> None: ...
    FinalGather: FinalGatherMode
    GlobalIllumination: GlobalIlluminationMode
    NormalMap: MaterialNormalMapComponent
    Luminance: float
    LuminanceMode: LuminanceMode
    TwoSided: bool
    TransmittanceScale: float
    ReflectanceScale: float
    IndirectBumpScale: float
    ColorBleedScale: float
    Opacity: MaterialOpacityComponent
    Refraction: MaterialRefractionComponent
    Specular: MaterialSpecularComponent
    Diffuse: MaterialDiffuseComponent
    Mode: Mode
    ChannelFlags: ChannelFlags
    IlluminationModel: IlluminationModel
    Reflectivity: float
    SelfIllumination: float
    Translucence: float
    Bump: MaterialMap
    Reflection: MaterialMap
    Ambient: MaterialColor
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Method:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.Method"""
    def __init__(self, *args) -> None: ...
    Inherit: int  # = 0
    Override: int  # = 1
class Mode:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.Mode"""
    def __init__(self, *args) -> None: ...
    Realistic: int  # = 0
    Advanced: int  # = 1
class NonEntityTraits(DrawableTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.NonEntityTraits"""
    def __init__(self, *args) -> None: ...
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddLight(self, lightId: ObjectId) -> None: ...
    def GetHighlightProperty(self, propertyType: HighlightProperty) -> object: ...
    def SetHighlightProperty(self, propertyType: HighlightProperty, value: object) -> None: ...
    def SetSelectionMarker(self, markerId: IntPtr) -> None: ...
    def SetupForEntity(self, entity: Entity) -> None: ...

class NormalMapMethod:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.NormalMapMethod"""
    def __init__(self, *args) -> None: ...
    TangentSpaceNormalMap: int  # = 0
class OrientationBehavior:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.OrientationBehavior"""
    def __init__(self, *args) -> None: ...
    World: int  # = 0
    Screen: int  # = 1
    ZAxis: int  # = 2
class OrientationType:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.OrientationType"""
    def __init__(self, *args) -> None: ...
    NoOrientation: int  # = 0
    Clockwise: int  # = 1
    CounterClockwise: int  # = -1
class PhotographicExposureParameters(ToneOperatorParameters):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.PhotographicExposureParameters"""
    def __init__(self, *args) -> None: ...
    WhiteColor: Color
    WhitePoint: float
    Exposure: float
    ExteriorDaylight: ExteriorDaylightMode
    MidTones: float
    Contrast: float
    Brightness: float
    ProcessBackground: bool
    ColorDifferentiation: bool
    ChromaticAdaptation: bool
    IsActive: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CopyFrom(self, source: RXObject) -> None: ...
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class PixelBGRA32:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.PixelBGRA32"""
    def __init__(self, *args) -> None: ...
    Alpha: int
    Blue: int
    Green: int
    Red: int
    def init(self, ) -> None: ...

class PointLightTraits(StandardLightTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.PointLightTraits"""
    def __init__(self, *args) -> None: ...
    HasTarget: bool
    TargetLocation: Point3d
    LampColor: ColorRGB
    PhysicalIntensity: float
    Attenuation: LightAttenuation
    Position: Point3d
    Shadow: ShadowParameters
    LightColor: Color
    Intensity: float
    On: bool
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Polyline(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.Polyline"""
    def __init__(self, *args) -> None: ...
    BaseSubEntMarker: IntPtr
    Normal: Vector3d
    Points: Point3dCollection
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PolylineCollection(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.PolylineCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: Polyline
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, value: Polyline) -> int: ...
    def Clear(self, ) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class PositionBehavior:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.PositionBehavior"""
    def __init__(self, *args) -> None: ...
    World: int  # = 0
    Viewport: int  # = 1
    Screen: int  # = 2
    ScreenLocalOrigin: int  # = 3
    WorldWithScreenOffset: int  # = 4
class ProceduralTexture(MaterialTexture):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ProceduralTexture"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ProceduralTextureType:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.ProceduralTextureType"""
    def __init__(self, *args) -> None: ...
    Wood: int  # = 0
    Marble: int  # = 1
    Generic: int  # = 2
class Projection:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.Projection"""
    def __init__(self, *args) -> None: ...
    InheritProjection: int  # = 0
    Planar: int  # = 1
    Box: int  # = 2
    Cylinder: int  # = 3
    Sphere: int  # = 4
class RapidRTFilterType:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.RapidRTFilterType"""
    def __init__(self, *args) -> None: ...
    Box: int  # = 0
    Triangle: int  # = 1
    Gaussian: int  # = 2
    Lanczos: int  # = 3
    Mitchell: int  # = 4
class RapidRTLightingMode:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.RapidRTLightingMode"""
    def __init__(self, *args) -> None: ...
    Simplified: int  # = 0
    Basic: int  # = 1
    Advanced: int  # = 2
class RapidRTQuitCondition:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.RapidRTQuitCondition"""
    def __init__(self, *args) -> None: ...
    ERenderLevel: int  # = 0
    ERenderTime: int  # = 1
class RapidRTRenderSettingsTraits(NonEntityTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.RapidRTRenderSettingsTraits"""
    def __init__(self, *args) -> None: ...
    FilterHeight: float
    FilterWidth: float
    FilterType: RapidRTFilterType
    LightingMode: RapidRTLightingMode
    RenderLevel: int
    RenderTime: int
    QuitCondition: RapidRTQuitCondition
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class RegenType:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.RegenType"""
    def __init__(self, *args) -> None: ...
    Invalid: int  # = 0
    StandardDisplay: int  # = 2
    HideOrShadeCommand: int  # = 3
    RenderCommand: int  # = 4
    ShadedDisplay: int  # = 4
    ForExplode: int  # = 5
    SaveWorldDrawForProxy: int  # = 6
class RenderEnvironmentTraits(NonEntityTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.RenderEnvironmentTraits"""
    def __init__(self, *args) -> None: ...
    EnvironmentMap: MaterialTexture
    FarPercentage: float
    NearPercentage: float
    FarDistance: float
    NearDistance: float
    FogColor: EntityColor
    IsBackground: bool
    Enable: bool
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class RenderSettingsTraits(NonEntityTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.RenderSettingsTraits"""
    def __init__(self, *args) -> None: ...
    ModelScaleFactor: float
    DiagnosticBackgroundEnabled: bool
    ShadowsEnabled: bool
    BackFacesEnabled: bool
    TextureSampling: bool
    MaterialEnabled: bool
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ScaleBehavior:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.ScaleBehavior"""
    def __init__(self, *args) -> None: ...
    World: int  # = 0
    Viewport: int  # = 1
    Screen: int  # = 2
    ViewportLocalOrigin: int  # = 3
    ScreenLocalOrigin: int  # = 4
class SelectionFlags:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.SelectionFlags"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    SelectionIgnore: int  # = 1
class ShadowFlags:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.ShadowFlags"""
    def __init__(self, *args) -> None: ...
    ShadowsCastAndReceive: int  # = 0
    ShadowsDoesNotCast: int  # = 1
    ShadowsDoesNotReceive: int  # = 2
    ShadowsIgnore: int  # = 3
class ShadowParameters(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ShadowParameters"""
    def __init__(self, *args) -> None: ...
    ExtendedLightRadius: float
    ExtendedLightWidth: float
    ExtendedLightLength: float
    ExtendedLightShape: ExtendedLightShape
    ShapeVisibility: bool
    ShadowSamples: int
    ShadowMapSoftness: int
    ShadowMapSize: int
    ShadowType: ShadowType
    ShadowsOn: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class ShadowType:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.ShadowType"""
    def __init__(self, *args) -> None: ...
    RayTraced: int  # = 0
    Maps: int  # = 1
    Sampled: int  # = 2
class SkyBackgroundTraits(NonEntityTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.SkyBackgroundTraits"""
    def __init__(self, *args) -> None: ...
    SkyParameters: SkyParameters
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SkyParameters(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.SkyParameters"""
    def __init__(self, *args) -> None: ...
    Saturation: float
    RedBlueShift: float
    SunDirection: Vector3d
    NightColor: Color
    GroundColor: Color
    SolarDiskSamples: int
    DiskIntensity: float
    GlowIntensity: float
    DiskScale: float
    VisibilityDistance: float
    HorizonBlur: float
    HorizonHeight: float
    Haze: float
    IntensityFactor: float
    AerialPerspective: bool
    Illumination: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class SolidBackgroundTraits(NonEntityTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.SolidBackgroundTraits"""
    def __init__(self, *args) -> None: ...
    ColorSolid: EntityColor
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Source:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.Source"""
    def __init__(self, *args) -> None: ...
    Scene: int  # = 0
    File: int  # = 1
    Procedural: int  # = 2
class SpotLightTraits(StandardLightTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.SpotLightTraits"""
    def __init__(self, *args) -> None: ...
    LampColor: ColorRGB
    PhysicalIntensity: float
    Attenuation: LightAttenuation
    Falloff: float
    Hotspot: float
    TargetLocation: Point3d
    Position: Point3d
    Shadow: ShadowParameters
    LightColor: Color
    Intensity: float
    On: bool
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetHotspotAndFalloff(self, hotspot: float, falloff: float) -> bool: ...

class StandardLightTraits(LightTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.StandardLightTraits"""
    def __init__(self, *args) -> None: ...
    Shadow: ShadowParameters
    LightColor: Color
    Intensity: float
    On: bool
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SubEntityTraits(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.SubEntityTraits"""
    def __init__(self, *args) -> None: ...
    Fill: Fill
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetSelectionMarker(self, markerId: IntPtr) -> None: ...

class TextStyle(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.TextStyle"""
    def __init__(self, *args) -> None: ...
    PreLoaded: bool
    Font: FontDescriptor
    StyleName: str
    BigFontFileName: str
    FileName: str
    Strikethrough: bool
    Overlined: bool
    Underlined: bool
    Vertical: bool
    UpsideDown: bool
    Backward: bool
    TrackingPercent: float
    ObliquingAngle: float
    XScale: float
    TextSize: float
    LoadStyleRec: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(unmanagedPointer: IntPtr, autoDelete: bool) -> TextStyle: ...
    def ExtentsBox(self, value1: str, includeSpaces: bool, raw: bool, context: WorldDraw) -> Extents2d: ...
    def FromTextStyleTableRecord(self, AcDbStyleName: str) -> None: ...
    def SetTrackKerning(self, trackPercent: float) -> None: ...
    def ToTextStyleTableRecord(self, AcDbStyleName: str) -> ObjectId: ...

class Tiling:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.Tiling"""
    def __init__(self, *args) -> None: ...
    InheritTiling: int  # = 0
    Tile: int  # = 1
    Crop: int  # = 2
    Clamp: int  # = 3
    Mirror: int  # = 4
class ToneOperatorParameters(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ToneOperatorParameters"""
    def __init__(self, *args) -> None: ...
    ExteriorDaylight: ExteriorDaylightMode
    WhiteColor: Color
    MidTones: float
    Contrast: float
    Brightness: float
    ProcessBackground: bool
    ColorDifferentiation: bool
    ChromaticAdaptation: bool
    IsActive: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CopyFrom(self, source: RXObject) -> None: ...
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class TransientDrawingMode:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.TransientDrawingMode"""
    def __init__(self, *args) -> None: ...
    Main: int  # = 0
    Sprite: int  # = 1
    DirectShortTerm: int  # = 2
    Highlight: int  # = 3
    DirectTopmost: int  # = 4
    Contrast: int  # = 5
    Count: int  # = 6
class TransientManager(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.TransientManager"""
    def __init__(self, *args) -> None: ...
    CurrentTransientManager: TransientManager
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddChildTransient(self, added: Drawable, parent: Drawable) -> bool: ...
    def AddTransient(self, added: Drawable, mode: TransientDrawingMode, subDrawingMode: int, viewportNumbers: IntegerCollection) -> bool: ...
    def EraseChildTransient(self, erased: Drawable, parent: Drawable) -> bool: ...
    def EraseTransient(self, erased: Drawable, viewportNumbers: IntegerCollection) -> bool: ...
    def EraseTransients(self, mode: TransientDrawingMode, subDrawingMode: int, viewportNumbers: IntegerCollection) -> bool: ...
    def GetFreeSubDrawingMode(self, mode: TransientDrawingMode, viewportNumbers: IntegerCollection, subDrawingMode: int) -> int: ...
    def UpdateChildTransient(self, updated: Drawable, parent: Drawable) -> None: ...
    def UpdateTransient(self, updated: Drawable, viewportNumbers: IntegerCollection) -> None: ...

class TransparencyMode:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.TransparencyMode"""
    def __init__(self, *args) -> None: ...
    TransparencyOff: int  # = 0
    Transparency1Bit: int  # = 1
    Transparency8Bit: int  # = 2
class VSDisplayShadowType:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.VSDisplayShadowType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    GroundPlane: int  # = 1
    Full: int  # = 2
    FullAndGround: int  # = 3
class VSDisplayStyles:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.VSDisplayStyles"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    BackgroundsFlag: int  # = 1
    LightingFlag: int  # = 2
    MaterialsFlag: int  # = 4
    TexturesFlag: int  # = 8
class VSEdgeJitterAmount:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.VSEdgeJitterAmount"""
    def __init__(self, *args) -> None: ...
    JitterLow: int  # = 1
    JitterMedium: int  # = 2
    JitterHigh: int  # = 3
class VSEdgeLinePattern:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.VSEdgeLinePattern"""
    def __init__(self, *args) -> None: ...
    Solid: int  # = 1
    Dashed: int  # = 2
    Dotted: int  # = 3
    ShortDash: int  # = 4
    MediumDash: int  # = 5
    LongDash: int  # = 6
    DoubleShortDash: int  # = 7
    DoubleMediumDash: int  # = 8
    DoubleLongDash: int  # = 9
    MediumLongDash: int  # = 10
    SparseDot: int  # = 11
class VSEdgeModel:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.VSEdgeModel"""
    def __init__(self, *args) -> None: ...
    NoEdges: int  # = 0
    Isolines: int  # = 1
    FacetEdges: int  # = 2
class VSEdgeModifiers:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.VSEdgeModifiers"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    EdgeOverhangFlag: int  # = 1
    EdgeJitterFlag: int  # = 2
    EdgeWidthFlag: int  # = 4
    EdgeColorFlag: int  # = 8
    EdgeHaloGapFlag: int  # = 16
    AlwaysOnTopFlag: int  # = 64
    EdgeOpacityFlag: int  # = 128
class VSEdgeStyles:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.VSEdgeStyles"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    VisibleFlag: int  # = 1
    SilhouetteFlag: int  # = 2
    ObscuredFlag: int  # = 4
    IntersectionFlag: int  # = 8
class VSFaceColorMode:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.VSFaceColorMode"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    ObjectColor: int  # = 1
    BackgroundColor: int  # = 2
    Mono: int  # = 3
    Tint: int  # = 4
    Desaturate: int  # = 5
class VSFaceLightingModel:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.VSFaceLightingModel"""
    def __init__(self, *args) -> None: ...
    Invisible: int  # = 0
    Constant: int  # = 1
    Phong: int  # = 2
    Gooch: int  # = 3
class VSFaceLightingQuality:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.VSFaceLightingQuality"""
    def __init__(self, *args) -> None: ...
    NoLighting: int  # = 0
    PerFaceLighting: int  # = 1
    PerVertexLighting: int  # = 2
    PerPixelLighting: int  # = 3
class VSFaceModifiers:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.VSFaceModifiers"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    FaceOpacityFlag: int  # = 1
    SpecularFlag: int  # = 2
class VariantType:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.VariantType"""
    def __init__(self, *args) -> None: ...
    Undefined: int  # = 0
    Boolean: int  # = 1
    Int: int  # = 2
    Double: int  # = 3
    Color: int  # = 4
    String: int  # = 5
    Table: int  # = 6
class VertexData:
    """.NET: Autodesk.AutoCAD.GraphicsInterface.VertexData"""
    def __init__(self, *args) -> None: ...
    OrientationFlag: OrientationType
    def GetNormalVectors(self, ) -> list: ...
    def GetTrueColors(self, ) -> list: ...
    def SetNormalVectors(self, normal: list) -> None: ...
    def SetTrueColors(self, colors: list) -> None: ...
    def get_MappingCoords(self, mapChannel: MapChannel) -> list: ...
    def set_MappingCoords(self, mapChannel: MapChannel, coords: list) -> None: ...

class Viewport(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.Viewport"""
    def __init__(self, *args) -> None: ...
    ViewDirection: Vector3d
    LinetypeGenerationCriteria: float
    LinetypeScaleMultiplier: float
    FrontAndBackClipping: FrontAndBackClipping
    DeviceContextViewportCorners: Extents2d
    AcadWindowId: int
    ViewportId: IntPtr
    CameraUpVector: Vector3d
    CameraTarget: Point3d
    CameraLocation: Point3d
    IsPerspective: bool
    EyeToWorldTransform: Matrix3d
    WorldToEyeTransform: Matrix3d
    EyeToModelTransform: Matrix3d
    ModelToEyeTransform: Matrix3d
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def DoInversePerspective(self, value: Point3d) -> Point3d: ...
    def DoPerspective(self, value: Point3d) -> Point3d: ...
    def GetNumPixelsInUnitSquare(self, givenWorldPoint: Point3d) -> Point2d: ...
    def LayerVisible(self, idLayer: ObjectId) -> bool: ...

class ViewportDraw(CommonDraw):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ViewportDraw"""
    def __init__(self, *args) -> None: ...
    ViewportObjectId: ObjectId
    SequenceNumber: int
    Geometry: ViewportGeometry
    Viewport: Viewport
    NumberOfIsolines: int
    IsDragging: bool
    Context: Context
    RawGeometry: Geometry
    SubEntityTraits: SubEntityTraits
    RegenAbort: bool
    RegenType: RegenType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def IsValidId(self, id: IntPtr) -> bool: ...

class ViewportGeometry(Geometry):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ViewportGeometry"""
    def __init__(self, *args) -> None: ...
    WorldToModelTransform: Matrix3d
    ModelToWorldTransform: Matrix3d
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def DeviceContextPolygon(self, points: Point3dCollection) -> bool: ...
    def DeviceContextPolyline(self, points: Point3dCollection) -> bool: ...
    def DeviceContextRasterImage(self, origin: Point3d, u: Vector3d, v: Vector3d, pixel: Matrix2d, entityId: ObjectId, imageOrg: ImageOrg, imageWidth: int, imageHeight: int, imageColorDepth: int, transparency: bool, source: ImageSource, unRotated: Vector3d, originalImage: ImageOrg, unRotatedPixel: Matrix2d, unRotatedImageWidth: int, unRotatedImageHeight: int) -> bool: ...
    def PolygonEye(self, points: Point3dCollection) -> bool: ...
    def PolylineEye(self, points: Point3dCollection) -> bool: ...

class ViewportTraits(DrawableTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.ViewportTraits"""
    def __init__(self, *args) -> None: ...
    ToneOperatorParameters: ToneOperatorParameters
    RenderSettings: ObjectId
    RenderEnvironment: ObjectId
    Contrast: float
    Brightness: float
    AmbientLightColor: Color
    DefaultLightingType: DefaultLightingType
    DefaultLightingOn: bool
    Background: ObjectId
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class VisualStyle(RXObject):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.VisualStyle"""
    def __init__(self, *args) -> None: ...
    Type: VisualStyleType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetPropertyType(self, prop: VisualStyleProperty) -> VariantType: ...
    def GetTrait(self, prop: VisualStyleProperty) -> object: ...
    def GetTraitFlag(self, prop: VisualStyleProperty, flagVal: int) -> bool: ...
    def Operation(self, prop: VisualStyleProperty) -> VisualStyleOperation: ...
    def SetTrait(self, prop: VisualStyleProperty, red: float, green: float, blue: float, op: VisualStyleOperation) -> None: ...
    def SetTraitFlag(self, prop: VisualStyleProperty, flagVal: int, bEnable: bool) -> None: ...

class VisualStyleOperation:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.VisualStyleOperation"""
    def __init__(self, *args) -> None: ...
    Inherit: int  # = 0
    Set: int  # = 1
    Disable: int  # = 2
    Enable: int  # = 3
    InvalidOperation: int  # = -1
class VisualStyleProperty:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.VisualStyleProperty"""
    def __init__(self, *args) -> None: ...
    FaceLightingModel: int  # = 0
    FaceLightingQuality: int  # = 1
    FaceColorMode: int  # = 2
    FaceModifier: int  # = 3
    FaceOpacity: int  # = 4
    FaceSpecular: int  # = 5
    FaceMonoColor: int  # = 6
    EdgeModel: int  # = 7
    EdgeStyle: int  # = 8
    EdgeIntersectionColor: int  # = 9
    EdgeObscuredColor: int  # = 10
    EdgeObscuredLinePattern: int  # = 11
    EdgeIntersectionLinePattern: int  # = 12
    EdgeCreaseAngle: int  # = 13
    EdgeModifier: int  # = 14
    EdgeColor: int  # = 15
    EdgeOpacity: int  # = 16
    EdgeWidth: int  # = 17
    EdgeOverhang: int  # = 18
    EdgeJitterAmount: int  # = 19
    EdgeSilhouetteColor: int  # = 20
    EdgeSilhouetteWidth: int  # = 21
    EdgeHaloGap: int  # = 22
    EdgeIsolines: int  # = 23
    EdgeHidePrecision: int  # = 24
    DisplayStyle: int  # = 25
    DisplayBrightness: int  # = 26
    DisplayShadowType: int  # = 27
    UseDrawOrder: int  # = 28
    ViewportTransparency: int  # = 29
    LightingEnabled: int  # = 30
    PosterizeEffect: int  # = 31
    MonoEffect: int  # = 32
    BlurEffect: int  # = 33
    PencilEffect: int  # = 34
    BloomEffect: int  # = 35
    PastelEffect: int  # = 36
    BlurAmount: int  # = 37
    PencilAngle: int  # = 38
    PencilScale: int  # = 39
    PencilPattern: int  # = 40
    PencilColor: int  # = 41
    BloomThreshold: int  # = 42
    BloomRadius: int  # = 43
    TintColor: int  # = 44
    FaceAdjustment: int  # = 45
    PostContrast: int  # = 46
    PostBrightness: int  # = 47
    PostPower: int  # = 48
    TintEffect: int  # = 49
    BloomIntensity: int  # = 50
    Color: int  # = 51
    Transparency: int  # = 52
    EdgeWiggleAmount: int  # = 53
    EdgeTexturePath: int  # = 54
    DepthOfField: int  # = 55
    FocusDistance: int  # = 56
    FocusWidth: int  # = 57
    PropertyCount: int  # = 58
    InvalidProperty: int  # = -1
class VisualStyleTraits(DrawableTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.VisualStyleTraits"""
    def __init__(self, *args) -> None: ...
    AcGiVisualStyle: VisualStyle
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class VisualStyleType:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.VisualStyleType"""
    def __init__(self, *args) -> None: ...
    Flat: int  # = 0
    FlatWithEdges: int  # = 1
    Gouraud: int  # = 2
    GouraudWithEdges: int  # = 3
    Wireframe2D: int  # = 4
    Wireframe3D: int  # = 5
    Hidden: int  # = 6
    Basic: int  # = 7
    Realistic: int  # = 8
    Conceptual: int  # = 9
    Custom: int  # = 10
    Dim: int  # = 11
    Brighten: int  # = 12
    Thicken: int  # = 13
    LinePattern: int  # = 14
    FacePattern: int  # = 15
    ColorChange: int  # = 16
    FaceOnly: int  # = 17
    EdgeOnly: int  # = 18
    DisplayOnly: int  # = 19
    JitterOff: int  # = 20
    OverhangOff: int  # = 21
    EdgeColorOff: int  # = 22
    ShadesOfGray: int  # = 23
    Sketchy: int  # = 24
    XRay: int  # = 25
    ShadedWithEdges: int  # = 26
    Shaded: int  # = 27
    EmptyStyle: int  # = 31
class WebFileType:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.WebFileType"""
    def __init__(self, *args) -> None: ...
    TypeC: int  # = 1
    TypeB: int  # = 2
    TypeA: int  # = 3
class WebLightTraits(PointLightTraits):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.WebLightTraits"""
    def __init__(self, *args) -> None: ...
    WebHorzAng90to270: bool
    WebSymmetry: WebSymmetry
    WebFileType: WebFileType
    WebFlux: float
    WebRotation: Vector3d
    WebFile: str
    HasTarget: bool
    TargetLocation: Point3d
    LampColor: ColorRGB
    PhysicalIntensity: float
    Attenuation: LightAttenuation
    Position: Point3d
    Shadow: ShadowParameters
    LightColor: Color
    Intensity: float
    On: bool
    SelectionFlags: SelectionFlags
    LinePattern: Linetype
    Fill: Fill
    SelectionOnlyGeometry: bool
    ShadowFlags: ShadowFlags
    DrawFlags: int
    VisualStyle: ObjectId
    Sectionable: bool
    Mapper: Mapper
    Material: ObjectId
    PlotStyleDescriptor: PlotStyleDescriptor
    Thickness: float
    LineTypeScale: float
    LineWeight: LineWeight
    FillType: FillType
    LineType: ObjectId
    Layer: ObjectId
    Transparency: Transparency
    TrueColor: EntityColor
    Color: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class WebSymmetry:
    """.NET enum: Autodesk.AutoCAD.GraphicsInterface.WebSymmetry"""
    def __init__(self, *args) -> None: ...
    NoSymmetry: int  # = 0
    SingleSymmetry: int  # = 1
    DoubleSymmetry: int  # = 2
    AxialSymmetry: int  # = 3
class WoodTexture(ProceduralTexture):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.WoodTexture"""
    def __init__(self, *args) -> None: ...
    GrainThickness: float
    AxialNoise: float
    RadialNoise: float
    Color2: MaterialColor
    Color1: MaterialColor
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Clone(self, ) -> WoodTexture: ...
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def Set(self, value: WoodTexture) -> None: ...

class WorldDraw(CommonDraw):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.WorldDraw"""
    def __init__(self, *args) -> None: ...
    Geometry: WorldGeometry
    NumberOfIsolines: int
    IsDragging: bool
    Context: Context
    RawGeometry: Geometry
    SubEntityTraits: SubEntityTraits
    RegenAbort: bool
    RegenType: RegenType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class WorldGeometry(Geometry):
    """.NET: Autodesk.AutoCAD.GraphicsInterface.WorldGeometry"""
    def __init__(self, *args) -> None: ...
    WorldToModelTransform: Matrix3d
    ModelToWorldTransform: Matrix3d
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetExtents(self, extents: Extents3d) -> None: ...
    def StartAttributesSegment(self, ) -> None: ...
