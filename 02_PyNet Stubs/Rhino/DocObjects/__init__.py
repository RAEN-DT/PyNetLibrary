# Auto-generated — Rhino 8 — Rhino.DocObjects

class ActiveSpace:
    """.NET: Rhino.DocObjects.ActiveSpace"""
    def __init__(self, *args) -> None: ...
    ...

class AngleDisplayMode:
    """.NET: Rhino.DocObjects.AngleDisplayMode"""
    def __init__(self, *args) -> None: ...
    ...

class AngularDimensionObject(DimensionObject):
    """.NET: Rhino.DocObjects.AngularDimensionObject"""
    def __init__(self, *args) -> None: ...
    AngularDimensionGeometry: AngularDimension
    DimensionStyle: DimensionStyle
    DisplayText: str
    AnnotationGeometry: AnnotationBase
    HasMeasurableTextFields: bool
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary

class AnimationProperties:
    """.NET: Rhino.DocObjects.AnimationProperties"""
    def __init__(self, *args) -> None: ...
    CaptureType: CaptureTypes
    FileExtension: str
    CaptureMethod: str
    ViewportName: str
    AnimationName: str
    DisplayMode: Guid
    CameraPoints: list
    TargetPoints: list
    FrameCount: int
    CurrentFrame: int
    CameraPathId: Guid
    TargetPathId: Guid
    Latitude: float
    Longitude: float
    NorthAngle: float
    StartDay: int
    StartMonth: int
    StartYear: int
    StartHour: int
    StartMinutes: int
    StartSeconds: int
    EndDay: int
    EndMonth: int
    EndYear: int
    EndHour: int
    EndMinutes: int
    EndSeconds: int
    DaysBetweenFrames: int
    MinutesBetweenFrames: int
    LightIndex: int
    FolderName: str
    HtmlFileName: str
    HtmlFullPath: str
    Images: list
    Dates: list
    RenderFull: bool
    RenderPreview: bool
    def Dispose(self, ) -> None: ...

class AnnotationObjectBase(RhinoObject):
    """.NET: Rhino.DocObjects.AnnotationObjectBase"""
    def __init__(self, *args) -> None: ...
    DisplayText: str
    AnnotationGeometry: AnnotationBase
    HasMeasurableTextFields: bool
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary

class BasepointZero:
    """.NET: Rhino.DocObjects.BasepointZero"""
    def __init__(self, *args) -> None: ...
    ...

class BitmapEntry(ModelComponent):
    """.NET: Rhino.DocObjects.BitmapEntry"""
    def __init__(self, *args) -> None: ...
    ComponentType: ModelComponentType
    IsReference: bool
    FileName: str
    IsSystemComponent: bool
    IsDeleted: bool
    Id: Guid
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    Name: str
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def Save(self, fileName: str) -> bool: ...

class BrepObject(RhinoObject):
    """.NET: Rhino.DocObjects.BrepObject"""
    def __init__(self, *args) -> None: ...
    BrepGeometry: Brep
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def DuplicateBrepGeometry(self, ) -> Brep: ...

class CentermarkObject(DimensionObject):
    """.NET: Rhino.DocObjects.CentermarkObject"""
    def __init__(self, *args) -> None: ...
    CentermarkGeometry: Centermark
    DimensionStyle: DimensionStyle
    DisplayText: str
    AnnotationGeometry: AnnotationBase
    HasMeasurableTextFields: bool
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary

class ClippingPlaneObject(RhinoObject):
    """.NET: Rhino.DocObjects.ClippingPlaneObject"""
    def __init__(self, *args) -> None: ...
    ClippingPlaneGeometry: ClippingPlaneSurface
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def AddClipViewport(self, viewport: RhinoViewport, commit: bool) -> bool: ...
    def RemoveClipViewport(self, viewport: RhinoViewport, commit: bool) -> bool: ...

class ConstructionPlane:
    """.NET: Rhino.DocObjects.ConstructionPlane"""
    def __init__(self, *args) -> None: ...
    Plane: Plane
    GridSpacing: float
    SnapSpacing: float
    GridLineCount: int
    ThickLineFrequency: int
    DepthBuffered: bool
    Name: str
    ShowGrid: bool
    ShowAxes: bool
    ShowZAxis: bool
    ThinLineColor: Color
    ThickLineColor: Color
    GridXColor: Color
    GridYColor: Color
    GridZColor: Color

class ConstructionPlaneGridDefaults:
    """.NET: Rhino.DocObjects.ConstructionPlaneGridDefaults"""
    def __init__(self, *args) -> None: ...
    GridSpacing: float
    SnapSpacing: float
    GridLineCount: int
    GridThickFrequency: int
    ShowGrid: bool
    ShowGridAxes: bool
    ShowWorldAxes: bool

class CoordinateSystem:
    """.NET: Rhino.DocObjects.CoordinateSystem"""
    def __init__(self, *args) -> None: ...
    ...

class CurveObject(RhinoObject):
    """.NET: Rhino.DocObjects.CurveObject"""
    def __init__(self, *args) -> None: ...
    CurveGeometry: Curve
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def DuplicateCurveGeometry(self, ) -> Curve: ...
    def GetLinetypeSegments(self, viewport: RhinoViewport) -> list: ...

class DetailViewObject(RhinoObject):
    """.NET: Rhino.DocObjects.DetailViewObject"""
    def __init__(self, *args) -> None: ...
    DetailGeometry: DetailView
    IsActive: bool
    Viewport: RhinoViewport
    DescriptiveTitle: str
    WorldToPageTransform: Transform
    PageToWorldTransform: Transform
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def CommitViewportChanges(self, ) -> bool: ...
    def GetFormattedScale(self, format: ScaleFormat, value: str) -> bool: ...
    def TryGetModelLength(self, paper: float, model: float) -> bool: ...
    def TryGetPaperLength(self, model: float, paper: float) -> bool: ...

class DimensionObject(AnnotationObjectBase):
    """.NET: Rhino.DocObjects.DimensionObject"""
    def __init__(self, *args) -> None: ...
    DimensionStyle: DimensionStyle
    DisplayText: str
    AnnotationGeometry: AnnotationBase
    HasMeasurableTextFields: bool
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary

class DimensionStyle(ModelComponent):
    """.NET: Rhino.DocObjects.DimensionStyle"""
    def __init__(self, *args) -> None: ...
    ComponentType: ModelComponentType
    IsReference: bool
    IsDeleted: bool
    Font: Font
    ArrowBlockId1: Guid
    ArrowBlockId2: Guid
    LeaderArrowBlockId: Guid
    SuppressExtension1: bool
    SuppressExtension2: bool
    SuppressArrow1: bool
    SuppressArrow2: bool
    AlternateUnitsDisplay: bool
    AlternateBelowLine: bool
    DrawTextMask: bool
    FixedExtensionOn: bool
    LeaderHasLanding: bool
    DrawForward: bool
    TextUnderlined: bool
    MaskOffset: float
    ExtensionLineExtension: float
    ExtensionLineOffset: float
    DimensionLineExtension: float
    ArrowLength: float
    LeaderArrowLength: float
    CentermarkSize: float
    TextGap: float
    TextHeight: float
    LengthFactor: float
    AlternateLengthFactor: float
    ToleranceUpperValue: float
    ToleranceLowerValue: float
    ToleranceHeightScale: float
    BaselineSpacing: float
    DimensionScale: float
    FixedExtensionLength: float
    TextRotation: float
    StackHeightScale: float
    Roundoff: float
    AlternateRoundoff: float
    AngularRoundoff: float
    LeaderLandingLength: float
    LeaderTextRotationRadians: float
    LeaderTextRotationDegrees: float
    DimensionScaleValue: ScaleValue
    ScaleLeftLengthMillimeters: float
    ScaleRightLengthMillimeters: float
    FitText: TextFit
    FitArrow: ArrowFit
    ForceDimensionLineBetweenExtensionLines: bool
    DimensionLengthDisplay: LengthDisplay
    AlternateDimensionLengthDisplay: LengthDisplay
    UnitSystem: UnitSystem
    AngleFormat: AngleDisplayFormat
    ToleranceFormat: ToleranceDisplayFormat
    MaskColorSource: MaskType
    MaskFrameType: MaskFrame
    StackFractionFormat: StackDisplayFormat
    ZeroSuppress: ZeroSuppression
    AlternateZeroSuppress: ZeroSuppression
    ToleranceZeroSuppress: ZeroSuppression
    AngleZeroSuppress: ZeroSuppression
    ArrowType1: ArrowType
    ArrowType2: ArrowType
    LeaderArrowType: ArrowType
    TextMoveLeader: int
    ArcLengthSymbol: int
    CenterMarkType: CenterMarkStyle
    LeaderContentAngleType: LeaderContentAngleStyle
    TextVerticalAlignment: TextVerticalAlignment
    TextHorizontalAlignment: TextHorizontalAlignment
    LeaderTextVerticalAlignment: TextVerticalAlignment
    LeaderTextHorizontalAlignment: TextHorizontalAlignment
    DimTextLocation: TextLocation
    DimRadialTextLocation: TextLocation
    LeaderCurveType: LeaderCurveStyle
    DimTextAngleType: LeaderContentAngleStyle
    DimRadialTextAngleType: LeaderContentAngleStyle
    TextOrientation: TextOrientation
    LeaderTextOrientation: TextOrientation
    DimTextOrientation: TextOrientation
    DimRadialTextOrientation: TextOrientation
    LengthResolution: int
    AlternateLengthResolution: int
    AngleResolution: int
    ToleranceResolution: int
    AlternateToleranceResolution: int
    MaskColor: Color
    DecimalSeparator: str
    Prefix: str
    Suffix: str
    AlternatePrefix: str
    AlternateSuffix: str
    HasFieldOverrides: bool
    IsChild: bool
    ParentId: Guid
    UserStringCount: int
    IsSystemComponent: bool
    Id: Guid
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    Name: str
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def AlternateDimensionLengthDisplayUnit(self, model_serial_number: int) -> UnitSystem: ...
    def ClearAllFieldOverrides(self, ) -> None: ...
    def ClearFieldOverride(self, field: Field) -> None: ...
    def CopyFrom(self, source: DimensionStyle) -> None: ...
    def CreatePreviewBitmap(self, width: int, height: int) -> Bitmap: ...
    def DeleteAllUserStrings(self, ) -> None: ...
    def DeleteUserString(self, key: str) -> bool: ...
    def DimensionLengthDisplayUnit(self, model_serial_number: int) -> UnitSystem: ...
    def Duplicate(self, newName: str, newId: Guid, newParentId: Guid) -> DimensionStyle: ...
    def GetUserString(self, key: str) -> str: ...
    def GetUserStrings(self, ) -> NameValueCollection: ...
    def IsChildOf(self, parentId: Guid) -> bool: ...
    def IsFieldOverriden(self, field: Field) -> bool: ...
    def ScaleLengthValues(self, scale: float) -> None: ...
    def SetFieldOverride(self, field: Field) -> None: ...
    def SetUserString(self, key: str, value: str) -> bool: ...

class DisplayMode:
    """.NET: Rhino.DocObjects.DisplayMode"""
    def __init__(self, *args) -> None: ...
    ...

class DistanceDisplayMode:
    """.NET: Rhino.DocObjects.DistanceDisplayMode"""
    def __init__(self, *args) -> None: ...
    ...

class EarthAnchorPoint:
    """.NET: Rhino.DocObjects.EarthAnchorPoint"""
    def __init__(self, *args) -> None: ...
    EarthBasepointLatitude: float
    EarthBasepointLongitude: float
    EarthBasepointElevation: float
    EarthBasepointElevationCoordinateSystem: EarthCoordinateSystem
    EarthBasepointElevationZero: BasepointZero
    KMLOrientationHeadingAngleDegrees: float
    KMLOrientationTiltAngleDegrees: float
    KMLOrientationRollAngleDegrees: float
    KMLOrientationHeadingAngleRadians: float
    KMLOrientationTiltAngleRadians: float
    KMLOrientationRollAngleRadians: float
    ModelBasePoint: Point3d
    ModelNorth: Vector3d
    ModelEast: Vector3d
    Name: str
    Description: str
    def Dispose(self, ) -> None: ...
    def EarthLocationIsSet(self, ) -> bool: ...
    def GetEarthAnchorPlane(self, anchorNorth: Vector3d) -> Plane: ...
    def GetModelCompass(self, ) -> Plane: ...
    def GetModelToEarthTransform(self, modelUnitSystem: UnitSystem) -> Transform: ...
    def ModelLocationIsSet(self, ) -> bool: ...

class EarthCoordinateSystem:
    """.NET: Rhino.DocObjects.EarthCoordinateSystem"""
    def __init__(self, *args) -> None: ...
    ...

class Environment(CommonObject):
    """.NET: Rhino.DocObjects.Environment"""
    def __init__(self, *args) -> None: ...
    BackgroundColor: Color
    BackgroundImage: Texture
    BackgroundProjection: BackgroundProjections
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary

class ExtrusionObject(RhinoObject):
    """.NET: Rhino.DocObjects.ExtrusionObject"""
    def __init__(self, *args) -> None: ...
    ExtrusionGeometry: Extrusion
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def DuplicateExtrusionGeometry(self, ) -> Extrusion: ...

class Font:
    """.NET: Rhino.DocObjects.Font"""
    def __init__(self, *args) -> None: ...
    QuartetName: str
    EnglishQuartetName: str
    FaceName: str
    EnglishFaceName: str
    LogfontName: str
    FamilyPlusFaceName: str
    PostScriptName: str
    RichTextFontName: str
    Description: str
    Bold: bool
    Italic: bool
    Underlined: bool
    Strikeout: bool
    IsEngravingFont: bool
    IsSymbolFont: bool
    IsSingleStrokeFont: bool
    IsSimulated: bool
    Style: FontStyle
    Weight: FontWeight
    Stretch: FontStretch
    PointSize: float
    FamilyName: str
    EnglishFamilyName: str
    IsInstalled: bool
    @staticmethod
    def AvailableFontFaceNames() -> list: ...
    @staticmethod
    def FromQuartetProperties(quartetName: str, bold: bool, italic: bool) -> Font: ...
    @staticmethod
    def FromRichTextProperties(richTextFontName: str, bold: bool, italic: bool, underlined: bool, strikethrough: bool) -> Font: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...
    def GetSubstituteFont(self, ) -> Font: ...
    @staticmethod
    def InstalledFonts(familyName: str) -> list: ...
    @staticmethod
    def InstalledFontsAsQuartets() -> list: ...

class FontQuartet:
    """.NET: Rhino.DocObjects.FontQuartet"""
    def __init__(self, *args) -> None: ...
    QuartetName: str
    HasRegularFont: bool
    HasBoldFont: bool
    HasItalicFont: bool
    HasBoldItalicFont: bool
    def ToString(self, ) -> str: ...

class GripObject(RhinoObject):
    """.NET: Rhino.DocObjects.GripObject"""
    def __init__(self, *args) -> None: ...
    CurrentLocation: Point3d
    OriginalLocation: Point3d
    Moved: bool
    Weight: float
    OwnerId: Guid
    Index: int
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def GetCageParameters(self, u: float, v: float, w: float) -> bool: ...
    def GetCurveCVIndices(self, cvIndices: list) -> int: ...
    def GetCurveParameters(self, t: float) -> bool: ...
    def GetGripDirections(self, u: Vector3d, v: Vector3d, normal: Vector3d) -> bool: ...
    def GetSurfaceCVIndices(self, cvIndices: list) -> int: ...
    def GetSurfaceParameters(self, u: float, v: float) -> bool: ...
    def Move(self, xform: Transform) -> None: ...
    def NeighborGrip(self, directionR: int, directionS: int, directionT: int, wrap: bool) -> GripObject: ...
    def UndoMove(self, ) -> None: ...

class Group(ModelComponent):
    """.NET: Rhino.DocObjects.Group"""
    def __init__(self, *args) -> None: ...
    ComponentType: ModelComponentType
    UserStringCount: int
    IsSystemComponent: bool
    IsDeleted: bool
    IsReference: bool
    Id: Guid
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    Name: str
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def DeleteAllUserStrings(self, ) -> None: ...
    def DeleteUserString(self, key: str) -> bool: ...
    def GetUserString(self, key: str) -> str: ...
    def GetUserStrings(self, ) -> NameValueCollection: ...
    def SetUserString(self, key: str, value: str) -> bool: ...

class HatchLine:
    """.NET: Rhino.DocObjects.HatchLine"""
    def __init__(self, *args) -> None: ...
    IsValid: bool
    Angle: float
    BasePoint: Point2d
    Offset: Vector2d
    DashCount: int
    GetDashes: IEnumerable
    PatternLength: float
    def AppendDash(self, dash: float) -> None: ...
    def DashAt(self, dashIndex: int) -> float: ...
    def Dispose(self, ) -> None: ...
    def SetDashes(self, dashes: IEnumerable) -> None: ...

class HatchObject(RhinoObject):
    """.NET: Rhino.DocObjects.HatchObject"""
    def __init__(self, *args) -> None: ...
    HatchGeometry: Hatch
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary

class HatchPattern(ModelComponent):
    """.NET: Rhino.DocObjects.HatchPattern"""
    def __init__(self, *args) -> None: ...
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    InUse: bool
    Index: int
    Description: str
    FillType: HatchPatternFillType
    HatchLineCount: int
    HatchLines: IEnumerable
    UserStringCount: int
    IsSystemComponent: bool
    Id: Guid
    HasId: bool
    IdIsLocked: bool
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    Name: str
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def AddHatchLine(self, hatchLine: HatchLine) -> int: ...
    def CreatePreviewGeometry(self, width: int, height: int, angle: float) -> list: ...
    def DeleteAllUserStrings(self, ) -> None: ...
    def DeleteUserString(self, key: str) -> bool: ...
    def GetUserString(self, key: str) -> str: ...
    def GetUserStrings(self, ) -> NameValueCollection: ...
    def HatchLineAt(self, hatchLineIndex: int) -> HatchLine: ...
    @staticmethod
    def ReadFromFile(filename: str, quiet: bool) -> list: ...
    def RemoveAllHatchLines(self, ) -> None: ...
    def RemoveHatchLine(self, hatchLineIndex: int) -> bool: ...
    def SetHatchLines(self, hatchLines: IEnumerable) -> int: ...
    def SetUserString(self, key: str, value: str) -> bool: ...
    @staticmethod
    def WriteToFile(filename: str, hatchPattern: HatchPattern) -> bool: ...

class HatchPatternFillType:
    """.NET: Rhino.DocObjects.HatchPatternFillType"""
    def __init__(self, *args) -> None: ...
    ...

class HistoryRecord:
    """.NET: Rhino.DocObjects.HistoryRecord"""
    def __init__(self, *args) -> None: ...
    Handle: IntPtr
    CopyOnReplaceObject: bool
    def Dispose(self, ) -> None: ...
    def SetBool(self, id: int, value: bool) -> bool: ...
    def SetBools(self, id: int, values: IEnumerable) -> bool: ...
    def SetBrep(self, id: int, value: Brep) -> bool: ...
    def SetColor(self, id: int, value: Color) -> bool: ...
    def SetColors(self, id: int, values: IEnumerable) -> bool: ...
    def SetCurve(self, id: int, value: Curve) -> bool: ...
    def SetDouble(self, id: int, value: float) -> bool: ...
    def SetDoubles(self, id: int, values: IEnumerable) -> bool: ...
    def SetGuid(self, id: int, value: Guid) -> bool: ...
    def SetGuids(self, id: int, values: IEnumerable) -> bool: ...
    def SetHistoryVersion(self, historyVersion: int) -> bool: ...
    def SetInt(self, id: int, value: int) -> bool: ...
    def SetInts(self, id: int, values: IEnumerable) -> bool: ...
    def SetMesh(self, id: int, value: Mesh) -> bool: ...
    def SetObjRef(self, id: int, value: ObjRef) -> bool: ...
    def SetPoint3d(self, id: int, value: Point3d) -> bool: ...
    def SetPoint3dOnObject(self, id: int, objref: ObjRef, value: Point3d) -> bool: ...
    def SetPoint3ds(self, id: int, values: IEnumerable) -> bool: ...
    def SetString(self, id: int, value: str) -> bool: ...
    def SetStrings(self, id: int, values: IEnumerable) -> bool: ...
    def SetSurface(self, id: int, value: Surface) -> bool: ...
    def SetTransorm(self, id: int, value: Transform) -> bool: ...
    def SetVector3d(self, id: int, value: Vector3d) -> bool: ...
    def SetVector3ds(self, id: int, values: IEnumerable) -> bool: ...

class InstanceDefinition(InstanceDefinitionGeometry):
    """.NET: Rhino.DocObjects.InstanceDefinition"""
    def __init__(self, *args) -> None: ...
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectCount: int
    UpdateType: InstanceDefinitionUpdateType
    Index: int
    IsTenuous: bool
    SkipNestedLinkedDefinitions: bool
    LayerStyle: InstanceDefinitionLayerStyle
    UnitSystem: UnitSystem
    SourceArchive: str
    ArchiveFileStatus: InstanceDefinitionArchiveFileStatus
    Description: str
    Url: str
    UrlDescription: str
    UserStringCount: int
    IsSystemComponent: bool
    Id: Guid
    HasId: bool
    IdIsLocked: bool
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    Name: str
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def CreatePreviewBitmap(self, displayModeId: Guid, viewportProjection: DefinedViewportProjection, isometricCamera: IsometricCamera, drawDecorations: bool, bitmapSize: Size, applyDpiScaling: bool) -> Bitmap: ...
    def Equals(self, obj: object) -> bool: ...
    def GetContainers(self, ) -> list: ...
    def GetHashCode(self, ) -> int: ...
    def GetObjects(self, ) -> list: ...
    def GetReferences(self, wheretoLook: int) -> list: ...
    def InUse(self, wheretoLook: int) -> bool: ...
    def Object(self, index: int) -> RhinoObject: ...
    def UseCount(self, topLevelReferenceCount: int, nestedReferenceCount: int) -> int: ...
    def UsesDefinition(self, otherIdefIndex: int) -> int: ...
    def UsesLayer(self, layerIndex: int) -> bool: ...
    def UsesLinetype(self, linetypeIndex: int) -> bool: ...

class InstanceDefinitionArchiveFileStatus:
    """.NET: Rhino.DocObjects.InstanceDefinitionArchiveFileStatus"""
    def __init__(self, *args) -> None: ...
    ...

class InstanceDefinitionLayerStyle:
    """.NET: Rhino.DocObjects.InstanceDefinitionLayerStyle"""
    def __init__(self, *args) -> None: ...
    ...

class InstanceDefinitionUpdateType:
    """.NET: Rhino.DocObjects.InstanceDefinitionUpdateType"""
    def __init__(self, *args) -> None: ...
    ...

class InstanceObject(RhinoObject):
    """.NET: Rhino.DocObjects.InstanceObject"""
    def __init__(self, *args) -> None: ...
    InstanceXform: Transform
    InsertionPoint: Point3d
    InstanceDefinition: InstanceDefinition
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def Explode(self, skipHiddenPieces: bool, viewportId: Guid, explodeNestedInstances: bool, pieces: list, pieceAttributes: list, pieceTransforms: list) -> None: ...
    def SubObjectFromComponentIndex(self, ci: ComponentIndex) -> RhinoObject: ...
    def UsesDefinition(self, definitionIndex: int, nestingLevel: int) -> bool: ...

class Layer(ModelComponent):
    """.NET: Rhino.DocObjects.Layer"""
    def __init__(self, *args) -> None: ...
    ComponentType: ModelComponentType
    ComponentStatus: ComponentStatus
    IsDeleted: bool
    IsReference: bool
    Name: str
    FullPath: str
    LayerIndex: int
    Id: Guid
    ParentLayerId: Guid
    IgesLevel: int
    Color: Color
    PlotColor: Color
    PlotWeight: float
    LinetypeIndex: int
    RenderMaterialIndex: int
    IsVisible: bool
    IsLocked: bool
    PersistentVisibility: bool
    ModelIsVisible: bool
    ModelPersistentVisibility: bool
    IsExpanded: bool
    IsCurrent: bool
    IsReferenceParentLayer: bool
    IsVisibleInUserInterface: bool
    RenderMaterial: RenderMaterial
    SortIndex: int
    PathSeparator: str
    PerViewportIsVisibleInNewDetails: bool
    UserStringCount: int
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def CommitChanges(self, ) -> bool: ...
    def CopyAttributesFrom(self, otherLayer: Layer) -> None: ...
    def Default(self, ) -> None: ...
    def DeleteAllUserStrings(self, ) -> None: ...
    def DeleteModelVisible(self, ) -> None: ...
    def DeletePerViewportColor(self, viewportId: Guid) -> None: ...
    def DeletePerViewportPlotColor(self, viewportId: Guid) -> None: ...
    def DeletePerViewportPlotWeight(self, viewportId: Guid) -> None: ...
    def DeletePerViewportSettings(self, viewportId: Guid) -> None: ...
    def DeletePerViewportVisible(self, viewportId: Guid) -> None: ...
    def DeletePlotColor(self, ) -> None: ...
    def DeleteUserString(self, key: str) -> bool: ...
    def Equals(self, other: Layer) -> bool: ...
    def GetChildren(self, allChildren: bool) -> list: ...
    def GetCustomSectionStyle(self, ) -> SectionStyle: ...
    @staticmethod
    def GetDefaultLayerProperties() -> Layer: ...
    def GetHashCode(self, ) -> int: ...
    @staticmethod
    def GetLeafName(fullPath: str) -> str: ...
    @staticmethod
    def GetParentName(fullPath: str) -> str: ...
    def GetPersistentLocking(self, ) -> bool: ...
    def GetPersistentVisibility(self, ) -> bool: ...
    def GetUserString(self, key: str) -> str: ...
    def GetUserStrings(self, ) -> NameValueCollection: ...
    def HasPerViewportSettings(self, viewportId: Guid) -> bool: ...
    def HasSelectedObjects(self, checkSubObjects: bool) -> bool: ...
    def IsChildOf(self, layerIndex: int) -> bool: ...
    def IsParentOf(self, layerIndex: int) -> bool: ...
    @staticmethod
    def IsValidName(name: str) -> bool: ...
    def ParentLayer(self, rootLevelParent: bool) -> Layer: ...
    def PerViewportColor(self, viewportId: Guid) -> Color: ...
    def PerViewportIsVisible(self, viewportId: Guid) -> bool: ...
    def PerViewportPersistentVisibility(self, viewportId: Guid) -> bool: ...
    def PerViewportPlotColor(self, viewportId: Guid) -> Color: ...
    def PerViewportPlotWeight(self, viewportId: Guid) -> float: ...
    def RemoveCustomSectionStyle(self, ) -> None: ...
    def SetCustomSectionStyle(self, sectionStyle: SectionStyle) -> None: ...
    def SetPerViewportColor(self, viewportId: Guid, color: Color) -> None: ...
    def SetPerViewportPersistentVisibility(self, viewportId: Guid, persistentVisibility: bool) -> None: ...
    def SetPerViewportPlotColor(self, viewportId: Guid, color: Color) -> None: ...
    def SetPerViewportPlotWeight(self, viewportId: Guid, plotWeight: float) -> None: ...
    def SetPerViewportVisible(self, viewportId: Guid, visible: bool) -> None: ...
    def SetPersistentLocking(self, persistentLocking: bool) -> None: ...
    def SetPersistentVisibility(self, persistentVisibility: bool) -> None: ...
    def SetUserString(self, key: str, value: str) -> bool: ...
    def ToString(self, ) -> str: ...
    def UnsetModelPersistentVisibility(self, ) -> None: ...
    def UnsetPerViewportPersistentVisibility(self, viewportId: Guid) -> None: ...
    def UnsetPersistentLocking(self, ) -> None: ...
    def UnsetPersistentVisibility(self, ) -> None: ...

class LeaderObject(AnnotationObjectBase):
    """.NET: Rhino.DocObjects.LeaderObject"""
    def __init__(self, *args) -> None: ...
    LeaderGeometry: Leader
    DisplayText: str
    AnnotationGeometry: AnnotationBase
    HasMeasurableTextFields: bool
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary

class LightObject(RhinoObject):
    """.NET: Rhino.DocObjects.LightObject"""
    def __init__(self, *args) -> None: ...
    ComponentType: ModelComponentType
    LightGeometry: Light
    Index: int
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def DuplicateLightGeometry(self, ) -> Light: ...

class LineCapStyle:
    """.NET: Rhino.DocObjects.LineCapStyle"""
    def __init__(self, *args) -> None: ...
    ...

class LineJoinStyle:
    """.NET: Rhino.DocObjects.LineJoinStyle"""
    def __init__(self, *args) -> None: ...
    ...

class LinearDimensionObject(DimensionObject):
    """.NET: Rhino.DocObjects.LinearDimensionObject"""
    def __init__(self, *args) -> None: ...
    LinearDimensionGeometry: LinearDimension
    DimensionStyle: DimensionStyle
    DisplayText: str
    AnnotationGeometry: AnnotationBase
    HasMeasurableTextFields: bool
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary

class Linetype(ModelComponent):
    """.NET: Rhino.DocObjects.Linetype"""
    def __init__(self, *args) -> None: ...
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    Name: str
    LinetypeIndex: int
    PatternLength: float
    SegmentCount: int
    IsModified: bool
    InUse: bool
    LineCapStyle: LineCapStyle
    LineJoinStyle: LineJoinStyle
    Width: float
    WidthUnits: UnitSystem
    AlwaysModelDistances: bool
    IsPatternLocked: bool
    UserStringCount: int
    IsSystemComponent: bool
    Id: Guid
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def AppendSegment(self, length: float, isSolid: bool) -> int: ...
    def CommitChanges(self, ) -> bool: ...
    @staticmethod
    def CreateFromPatternString(patternString: str, millimeters: bool) -> Linetype: ...
    def Default(self, ) -> None: ...
    def DeleteAllUserStrings(self, ) -> None: ...
    def DeleteUserString(self, key: str) -> bool: ...
    def DuplicateLinetype(self, ) -> Linetype: ...
    def GetSegment(self, index: int, length: float, isSolid: bool) -> None: ...
    def GetTaperPoints(self, ) -> list: ...
    def GetUserString(self, key: str) -> str: ...
    def GetUserStrings(self, ) -> NameValueCollection: ...
    def PatternString(self, millimeters: bool) -> str: ...
    @staticmethod
    def ReadFromFile(path: str) -> list: ...
    def RemoveSegment(self, index: int) -> bool: ...
    def RemoveTaper(self, ) -> None: ...
    def SetSegment(self, index: int, length: float, isSolid: bool) -> bool: ...
    def SetSegments(self, segments: IEnumerable) -> bool: ...
    def SetTaper(self, startWidth: float, taperPoint: Point2d, endWidth: float) -> None: ...
    def SetUserString(self, key: str, value: str) -> bool: ...

class Material(ModelComponent):
    """.NET: Rhino.DocObjects.Material"""
    def __init__(self, *args) -> None: ...
    DefaultMaterial: Material
    RenderMaterialInstanceId: Guid
    RenderMaterial: RenderMaterial
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    RenderPlugInId: Guid
    IsDefaultMaterial: bool
    MaterialIndex: int
    UseCount: int
    IsDocumentControlled: bool
    Name: str
    MaxShine: float
    Shine: float
    Transparency: float
    IndexOfRefraction: float
    FresnelIndexOfRefraction: float
    RefractionGlossiness: float
    ReflectionGlossiness: float
    FresnelReflections: bool
    DisableLighting: bool
    AlphaTransparency: bool
    IsPhysicallyBased: bool
    PhysicallyBased: PhysicallyBasedMaterial
    Reflectivity: float
    PreviewColor: Color
    RDKMaterialID: Guid
    DiffuseColor: Color
    AmbientColor: Color
    EmissionColor: Color
    SpecularColor: Color
    ReflectionColor: Color
    TransparentColor: Color
    UserStringCount: int
    IsSystemComponent: bool
    Id: Guid
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def ClearMaterialChannels(self, ) -> None: ...
    def CommitChanges(self, ) -> bool: ...
    def CopyFrom(self, other: Material) -> None: ...
    def Default(self, ) -> None: ...
    def GetBitmapTexture(self, ) -> Texture: ...
    def GetBumpTexture(self, ) -> Texture: ...
    def GetEnvironmentTexture(self, ) -> Texture: ...
    def GetTexture(self, which: TextureType) -> Texture: ...
    def GetTextures(self, ) -> list: ...
    def GetTransparencyTexture(self, ) -> Texture: ...
    def GetUserString(self, key: str) -> str: ...
    def GetUserStrings(self, ) -> NameValueCollection: ...
    def MaterialChannelIdFromIndex(self, material_channel_index: int) -> Guid: ...
    def MaterialChannelIndexFromId(self, material_channel_id: Guid, bAddIdIfNotPresent: bool) -> int: ...
    def SetBitmapTexture(self, filename: str) -> bool: ...
    def SetBumpTexture(self, filename: str) -> bool: ...
    def SetEnvironmentTexture(self, filename: str) -> bool: ...
    def SetTexture(self, texture: Texture, which: TextureType) -> bool: ...
    def SetTransparencyTexture(self, filename: str) -> bool: ...
    def SetUserString(self, key: str, value: str) -> bool: ...
    def ToPhysicallyBased(self, ) -> None: ...

class MaterialRef:
    """.NET: Rhino.DocObjects.MaterialRef"""
    def __init__(self, *args) -> None: ...
    MaterialSource: ObjectMaterialSource
    PlugInId: Guid
    FrontFaceMaterialId: Guid
    BackFaceMaterialId: Guid
    FrontFaceMaterialIndex: int
    BackFaceMaterialIndex: int
    def Dispose(self, ) -> None: ...

class MaterialRefCreateParams:
    """.NET: Rhino.DocObjects.MaterialRefCreateParams"""
    def __init__(self, *args) -> None: ...
    PlugInId: Guid
    MaterialSource: ObjectMaterialSource
    FrontFaceMaterialId: Guid
    FrontFaceMaterialIndex: int
    BackFaceMaterialId: Guid
    BackFaceMaterialIndex: int

class MaterialRefs:
    """.NET: Rhino.DocObjects.MaterialRefs"""
    def __init__(self, *args) -> None: ...
    Count: int
    IsReadOnly: bool
    Item: MaterialRef
    Keys: ICollection
    Values: ICollection
    def Add(self, key: Guid, value: MaterialRef) -> None: ...
    def Clear(self, ) -> None: ...
    def Contains(self, item: KeyValuePair) -> bool: ...
    def ContainsKey(self, key: Guid) -> bool: ...
    def CopyTo(self, array: list, arrayIndex: int) -> None: ...
    def Create(self, createParams: MaterialRefCreateParams) -> MaterialRef: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, item: KeyValuePair) -> bool: ...
    def TryGetValue(self, key: Guid, value: MaterialRef) -> bool: ...

class MeshObject(RhinoObject):
    """.NET: Rhino.DocObjects.MeshObject"""
    def __init__(self, *args) -> None: ...
    IsCustomObject: bool
    MeshGeometry: Mesh
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    @staticmethod
    def CheckMeshes(meshObjects: IEnumerable, textLog: TextLog, parameters: MeshCheckParameters) -> bool: ...
    def DuplicateMeshGeometry(self, ) -> Mesh: ...

class ModelComponent(CommonObject):
    """.NET: Rhino.DocObjects.ModelComponent"""
    def __init__(self, *args) -> None: ...
    IsSystemComponent: bool
    IsDeleted: bool
    IsReference: bool
    Id: Guid
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    Name: str
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    NamePathSeparator: str
    ModelSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    ComponentType: ModelComponentType
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def ClearId(self, ) -> None: ...
    def ClearIndex(self, ) -> None: ...
    def ClearName(self, ) -> None: ...
    def DataCRC(self, currentRemainder: int) -> int: ...
    @staticmethod
    def IsValidComponentName(name: str) -> bool: ...
    def LockId(self, ) -> None: ...
    def LockIndex(self, ) -> None: ...
    def LockName(self, ) -> None: ...
    @staticmethod
    def ModelComponentTypeIgnoresCase(type: ModelComponentType) -> bool: ...
    @staticmethod
    def ModelComponentTypeIncludesParent(type: ModelComponentType) -> bool: ...
    @staticmethod
    def ModelComponentTypeRequiresUniqueName(type: ModelComponentType) -> bool: ...
    def ToString(self, ) -> str: ...

class ModelComponentType:
    """.NET: Rhino.DocObjects.ModelComponentType"""
    def __init__(self, *args) -> None: ...
    ...

class MorphControlObject(RhinoObject):
    """.NET: Rhino.DocObjects.MorphControlObject"""
    def __init__(self, *args) -> None: ...
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary

class NamedViewWidgetObject(RhinoObject):
    """.NET: Rhino.DocObjects.NamedViewWidgetObject"""
    def __init__(self, *args) -> None: ...
    AssociatedNamedView: str
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary

class ObjRef:
    """.NET: Rhino.DocObjects.ObjRef"""
    def __init__(self, *args) -> None: ...
    Document: RhinoDoc
    ObjectId: Guid
    RuntimeSerialNumber: int
    GeometryComponentIndex: ComponentIndex
    def Brep(self, ) -> Brep: ...
    def ClippingPlaneSurface(self, ) -> ClippingPlaneSurface: ...
    def Curve(self, ) -> Curve: ...
    def CurveParameter(self, parameter: float) -> Curve: ...
    def Dispose(self, ) -> None: ...
    def Edge(self, ) -> BrepEdge: ...
    def Face(self, ) -> BrepFace: ...
    def Geometry(self, ) -> GeometryBase: ...
    def Hatch(self, ) -> Hatch: ...
    def InstanceDefinitionPart(self, ) -> RhinoObject: ...
    def Light(self, ) -> Light: ...
    def Mesh(self, ) -> Mesh: ...
    def Object(self, ) -> RhinoObject: ...
    def Point(self, ) -> Point: ...
    def PointCloud(self, ) -> PointCloud: ...
    def SelectionMethod(self, ) -> SelectionMethod: ...
    def SelectionPoint(self, ) -> Point3d: ...
    def SelectionView(self, ) -> RhinoView: ...
    def SelectionViewDetailSerialNumber(self, ) -> int: ...
    def SetSelectionComponent(self, componentIndex: ComponentIndex) -> None: ...
    def SubD(self, ) -> SubD: ...
    def SubDEdge(self, ) -> SubDEdge: ...
    def SubDFace(self, ) -> SubDFace: ...
    def SubDVertex(self, ) -> SubDVertex: ...
    def Surface(self, ) -> Surface: ...
    def SurfaceParameter(self, u: float, v: float) -> Surface: ...
    def TextDot(self, ) -> TextDot: ...
    def TextEntity(self, ) -> TextEntity: ...
    def Trim(self, ) -> BrepTrim: ...

class ObjectAttributes(CommonObject):
    """.NET: Rhino.DocObjects.ObjectAttributes"""
    def __init__(self, *args) -> None: ...
    IsDocumentControlled: bool
    Mode: ObjectMode
    IsInstanceDefinitionObject: bool
    Visible: bool
    CastsShadows: bool
    ReceivesShadows: bool
    LinetypeSource: ObjectLinetypeSource
    ColorSource: ObjectColorSource
    PlotColorSource: ObjectPlotColorSource
    PlotWeightSource: ObjectPlotWeightSource
    SectionAttributesSource: ObjectSectionAttributesSource
    LinetypePatternScale: float
    HatchBackgroundFillColor: Color
    HatchBoundaryVisible: bool
    ClippingPlaneLabelStyle: SectionLabelStyle
    CustomMeshingParameters: MeshingParameters
    EnableCustomMeshingParameters: bool
    ObjectId: Guid
    Name: str
    Url: str
    LayerIndex: int
    LinetypeIndex: int
    MaterialIndex: int
    MaterialSource: ObjectMaterialSource
    RenderMaterial: RenderMaterial
    Decals: Decals
    OCSMappingChannelId: int
    File3dmMeshModifiers: File3dmMeshModifiers
    MaterialRefs: MaterialRefs
    ObjectColor: Color
    PlotColor: Color
    HasMapping: bool
    DisplayOrder: int
    PlotWeight: float
    ObjectDecoration: ObjectDecoration
    WireDensity: int
    ViewportId: Guid
    Space: ActiveSpace
    GroupCount: int
    UserStringCount: int
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def AddHideInDetailOverride(self, detailId: Guid) -> bool: ...
    def AddToGroup(self, groupIndex: int) -> None: ...
    def ClearRenderingAttributes(self, ) -> None: ...
    def ComputedPlotColor(self, document: RhinoDoc, viewportId: Guid) -> Color: ...
    def ComputedPlotWeight(self, document: RhinoDoc, viewportId: Guid) -> float: ...
    def DeleteAllUserStrings(self, ) -> None: ...
    def DeleteUserString(self, key: str) -> bool: ...
    def DrawColor(self, document: RhinoDoc, viewportId: Guid) -> Color: ...
    def Duplicate(self, ) -> ObjectAttributes: ...
    def GetCustomLinetype(self, ) -> Linetype: ...
    def GetCustomSectionStyle(self, ) -> SectionStyle: ...
    def GetDisplayModeOverride(self, viewportId: Guid) -> Guid: ...
    def GetGroupList(self, ) -> list: ...
    def GetHideInDetailOverrides(self, ) -> list: ...
    def GetUserString(self, key: str) -> str: ...
    def GetUserStrings(self, ) -> NameValueCollection: ...
    def HasDisplayModeOverride(self, viewportId: Guid) -> bool: ...
    def HasHideInDetailOverrideSet(self, detailId: Guid) -> bool: ...
    def IsInGroup(self, groupIndex: int) -> bool: ...
    def ObjectFrame(self, ) -> Plane: ...
    def RemoveCustomLinetype(self, ) -> None: ...
    def RemoveCustomSectionStyle(self, ) -> None: ...
    def RemoveDisplayModeOverride(self, rhinoViewportId: Guid) -> None: ...
    def RemoveFromAllGroups(self, ) -> None: ...
    def RemoveFromGroup(self, groupIndex: int) -> None: ...
    def RemoveHideInDetailOverride(self, detailId: Guid) -> bool: ...
    def SetCustomLinetype(self, linetype: Linetype) -> None: ...
    def SetCustomSectionStyle(self, sectionStyle: SectionStyle) -> None: ...
    def SetDisplayModeOverride(self, mode: DisplayModeDescription, rhinoViewportId: Guid) -> bool: ...
    def SetObjectFrame(self, xform: Transform) -> None: ...
    def SetUserString(self, key: str, value: str) -> bool: ...
    def Transform(self, xform: Transform) -> bool: ...

class ObjectColorSource:
    """.NET: Rhino.DocObjects.ObjectColorSource"""
    def __init__(self, *args) -> None: ...
    ...

class ObjectDecoration:
    """.NET: Rhino.DocObjects.ObjectDecoration"""
    def __init__(self, *args) -> None: ...
    ...

class ObjectEnumeratorSettings:
    """.NET: Rhino.DocObjects.ObjectEnumeratorSettings"""
    def __init__(self, *args) -> None: ...
    NormalObjects: bool
    LockedObjects: bool
    HiddenObjects: bool
    IdefObjects: bool
    DeletedObjects: bool
    SubObjectSelected: bool
    ActiveObjects: bool
    ReferenceObjects: bool
    IncludeLights: bool
    IncludeGrips: bool
    IncludePhantoms: bool
    SelectedObjectsFilter: bool
    VisibleFilter: bool
    ObjectTypeFilter: ObjectType
    ClassTypeFilter: Type
    LayerIndexFilter: int
    MaterialIndexFilter: int
    NameFilter: str
    ViewportFilter: RhinoViewport

class ObjectLinetypeSource:
    """.NET: Rhino.DocObjects.ObjectLinetypeSource"""
    def __init__(self, *args) -> None: ...
    ...

class ObjectMaterialSource:
    """.NET: Rhino.DocObjects.ObjectMaterialSource"""
    def __init__(self, *args) -> None: ...
    ...

class ObjectMode:
    """.NET: Rhino.DocObjects.ObjectMode"""
    def __init__(self, *args) -> None: ...
    ...

class ObjectPlotColorSource:
    """.NET: Rhino.DocObjects.ObjectPlotColorSource"""
    def __init__(self, *args) -> None: ...
    ...

class ObjectPlotWeightSource:
    """.NET: Rhino.DocObjects.ObjectPlotWeightSource"""
    def __init__(self, *args) -> None: ...
    ...

class ObjectSectionAttributesSource:
    """.NET: Rhino.DocObjects.ObjectSectionAttributesSource"""
    def __init__(self, *args) -> None: ...
    ...

class ObjectSectionFillRule:
    """.NET: Rhino.DocObjects.ObjectSectionFillRule"""
    def __init__(self, *args) -> None: ...
    ...

class ObjectType:
    """.NET: Rhino.DocObjects.ObjectType"""
    def __init__(self, *args) -> None: ...
    ...

class OrdinateDimensionObject(DimensionObject):
    """.NET: Rhino.DocObjects.OrdinateDimensionObject"""
    def __init__(self, *args) -> None: ...
    OrdinateDimensionGeometry: OrdinateDimension
    DimensionStyle: DimensionStyle
    DisplayText: str
    AnnotationGeometry: AnnotationBase
    HasMeasurableTextFields: bool
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary

class PageSettings:
    """.NET: Rhino.DocObjects.PageSettings"""
    def __init__(self, *args) -> None: ...
    PageNumber: int
    WidthMillimeters: float
    HeightMillimeters: float
    LeftMarginMillimeters: float
    RightMarginMillimeters: float
    TopMarginMillimeters: float
    BottomMarginMillimeters: float
    PrinterName: str

class PhysicallyBasedMaterial:
    """.NET: Rhino.DocObjects.PhysicallyBasedMaterial"""
    def __init__(self, *args) -> None: ...
    Material: Material
    BaseColor: Color4f
    BRDF: BRDFs
    SubsurfaceScatteringColor: Color4f
    Subsurface: float
    SubsurfaceScatteringRadius: float
    Metallic: float
    Specular: float
    ReflectiveIOR: float
    SpecularTint: float
    Roughness: float
    Anisotropic: float
    AnisotropicRotation: float
    Sheen: float
    SheenTint: float
    Clearcoat: float
    ClearcoatRoughness: float
    OpacityIOR: float
    Opacity: float
    OpacityRoughness: float
    Alpha: float
    UseBaseColorTextureAlphaForObjectAlphaTransparencyTexture: bool
    Emission: Color4f
    def GetTexture(self, which: TextureType) -> Texture: ...
    def GetTextures(self, ) -> list: ...
    def SetTexture(self, texture: Texture, which: TextureType) -> bool: ...
    def SynchronizeLegacyMaterial(self, ) -> None: ...

class PointCloudObject(RhinoObject):
    """.NET: Rhino.DocObjects.PointCloudObject"""
    def __init__(self, *args) -> None: ...
    PointCloudGeometry: PointCloud
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def DuplicatePointCloudGeometry(self, ) -> PointCloud: ...

class PointObject(RhinoObject):
    """.NET: Rhino.DocObjects.PointObject"""
    def __init__(self, *args) -> None: ...
    PointGeometry: Point
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def DuplicatePointGeometry(self, ) -> Point: ...

class ProxyObject(RhinoObject):
    """.NET: Rhino.DocObjects.ProxyObject"""
    def __init__(self, *args) -> None: ...
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def CreateMeshes(self, meshType: MeshType, parameters: MeshingParameters, ignoreCustomParameters: bool) -> int: ...
    def GetMeshes(self, meshType: MeshType) -> list: ...

class RadialDimensionObject(DimensionObject):
    """.NET: Rhino.DocObjects.RadialDimensionObject"""
    def __init__(self, *args) -> None: ...
    RadialDimensionGeometry: RadialDimension
    DimensionStyle: DimensionStyle
    DisplayText: str
    AnnotationGeometry: AnnotationBase
    HasMeasurableTextFields: bool
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary

class ReplayHistoryData:
    """.NET: Rhino.DocObjects.ReplayHistoryData"""
    def __init__(self, *args) -> None: ...
    Document: RhinoDoc
    HistoryVersion: int
    RecordId: Guid
    Results: list
    def AppendHistoryResult(self, ) -> ReplayHistoryResult: ...
    def Dispose(self, ) -> None: ...
    def GetRhinoObjRef(self, id: int) -> ObjRef: ...
    def TryGetBool(self, id: int, value: bool) -> bool: ...
    def TryGetColor(self, id: int, value: Color) -> bool: ...
    def TryGetDouble(self, id: int, value: float) -> bool: ...
    def TryGetDoubles(self, id: int, values: list) -> bool: ...
    def TryGetGuid(self, id: int, value: Guid) -> bool: ...
    def TryGetGuids(self, id: int, values: list) -> bool: ...
    def TryGetInt(self, id: int, value: int) -> bool: ...
    def TryGetPoint3d(self, id: int, value: Point3d) -> bool: ...
    def TryGetPoint3dOnObject(self, id: int, value: Point3d) -> bool: ...
    def TryGetString(self, id: int, value: str) -> bool: ...
    def TryGetTransform(self, id: int, value: Transform) -> bool: ...
    def TryGetVector3d(self, id: int, value: Vector3d) -> bool: ...
    def UpdateResultArray(self, newResults: IEnumerable) -> None: ...

class ReplayHistoryResult:
    """.NET: Rhino.DocObjects.ReplayHistoryResult"""
    def __init__(self, *args) -> None: ...
    ExistingObject: RhinoObject
    def UpdateToAngularDimension(self, dimension: AngularDimension, attributes: ObjectAttributes) -> bool: ...
    def UpdateToArc(self, arc: Arc, attributes: ObjectAttributes) -> bool: ...
    def UpdateToBrep(self, brep: Brep, attributes: ObjectAttributes) -> bool: ...
    def UpdateToCircle(self, circle: Circle, attributes: ObjectAttributes) -> bool: ...
    def UpdateToClippingPlane(self, plane: Plane, uMagnitude: float, vMagnitude: float, clippedViewportId: Guid, attributes: ObjectAttributes) -> bool: ...
    def UpdateToCurve(self, curve: Curve, attributes: ObjectAttributes) -> bool: ...
    def UpdateToEllipse(self, ellipse: Ellipse, attributes: ObjectAttributes) -> bool: ...
    def UpdateToExtrusion(self, extrusion: Extrusion, attributes: ObjectAttributes) -> bool: ...
    def UpdateToHatch(self, hatch: Hatch, attributes: ObjectAttributes) -> bool: ...
    def UpdateToInstanceReferenceGeometry(self, instanceReference: InstanceReferenceGeometry, attributes: ObjectAttributes) -> bool: ...
    def UpdateToLeader(self, leader: Leader, attributes: ObjectAttributes) -> bool: ...
    def UpdateToLine(self, from_: Point3d, to: Point3d, attributes: ObjectAttributes) -> bool: ...
    def UpdateToLinearDimension(self, dimension: LinearDimension, attributes: ObjectAttributes) -> bool: ...
    def UpdateToMesh(self, mesh: Mesh, attributes: ObjectAttributes) -> bool: ...
    def UpdateToPoint(self, point: Point3d, attributes: ObjectAttributes) -> bool: ...
    def UpdateToPointCloud(self, cloud: PointCloud, attributes: ObjectAttributes) -> bool: ...
    def UpdateToPolyline(self, points: IEnumerable, attributes: ObjectAttributes) -> bool: ...
    def UpdateToRadialDimension(self, dimension: RadialDimension, attributes: ObjectAttributes) -> bool: ...
    def UpdateToSphere(self, sphere: Sphere, attributes: ObjectAttributes) -> bool: ...
    def UpdateToSubD(self, subD: SubD, attributes: ObjectAttributes) -> bool: ...
    def UpdateToSurface(self, surface: Surface, attributes: ObjectAttributes) -> bool: ...
    def UpdateToText(self, text: str, plane: Plane, height: float, fontName: str, bold: bool, italic: bool, justification: TextJustification, attributes: ObjectAttributes) -> bool: ...
    def UpdateToTextDot(self, dot: TextDot, attributes: ObjectAttributes) -> bool: ...

class RhinoAfterTransformObjectsEventArgs(EventArgs):
    """.NET: Rhino.DocObjects.RhinoAfterTransformObjectsEventArgs"""
    def __init__(self, *args) -> None: ...
    TransformEventId: int

class RhinoDeselectAllObjectsEventArgs(EventArgs):
    """.NET: Rhino.DocObjects.RhinoDeselectAllObjectsEventArgs"""
    def __init__(self, *args) -> None: ...
    ObjectCount: int
    Document: RhinoDoc

class RhinoModifyObjectAttributesEventArgs(EventArgs):
    """.NET: Rhino.DocObjects.RhinoModifyObjectAttributesEventArgs"""
    def __init__(self, *args) -> None: ...
    Document: RhinoDoc
    RhinoObject: RhinoObject
    OldAttributes: ObjectAttributes
    NewAttributes: ObjectAttributes

class RhinoObject(ModelComponent):
    """.NET: Rhino.DocObjects.RhinoObject"""
    def __init__(self, *args) -> None: ...
    NextRuntimeSerialNumber: int
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def CommitChanges(self, ) -> bool: ...
    def CopyHistoryOnReplace(self, ) -> bool: ...
    def CreateMeshes(self, meshType: MeshType, parameters: MeshingParameters, ignoreCustomParameters: bool) -> int: ...
    def CustomRenderMeshesBoundingBox(self, mt: MeshType, vp: ViewportInfo, flags: Flags, plugin: PlugIn, attrs: DisplayPipelineAttributes, boundingBox: BoundingBox) -> bool: ...
    def Description(self, textLog: TextLog) -> None: ...
    def DuplicateGeometry(self, ) -> GeometryBase: ...
    def EnableCustomGrips(self, customGrips: CustomObjectGrips) -> bool: ...
    def EnableVisualAnalysisMode(self, mode: VisualAnalysisMode, enable: bool) -> bool: ...
    @staticmethod
    def FromRuntimeSerialNumber(serialNumber: int) -> RhinoObject: ...
    def GetActiveVisualAnalysisModes(self, ) -> list: ...
    def GetCustomRenderMeshParameter(self, providerId: Guid, parameterName: str) -> IConvertible: ...
    def GetDynamicTransform(self, transform: Transform) -> bool: ...
    @staticmethod
    def GetFillSurfaces(rhinoObject: RhinoObject, clippingPlaneObjects: IEnumerable, unclippedFills: bool) -> list: ...
    def GetGrips(self, ) -> list: ...
    def GetGroupList(self, ) -> list: ...
    def GetHighlightedSubObjects(self, ) -> list: ...
    def GetMaterial(self, componentIndex: ComponentIndex, plugInId: Guid, attributes: ObjectAttributes) -> Material: ...
    def GetMeshes(self, meshType: MeshType) -> list: ...
    def GetRenderMaterial(self, componentIndex: ComponentIndex, plugInId: Guid, attributes: ObjectAttributes) -> RenderMaterial: ...
    def GetRenderMeshParameters(self, returnDocumentParametersIfUnset: bool) -> MeshingParameters: ...
    @staticmethod
    def GetRenderMeshes(rhinoObjects: IEnumerable, okToCreate: bool, returnAllObjects: bool) -> list: ...
    @staticmethod
    def GetRenderMeshesWithUpdatedTCs(rhinoObjects: IEnumerable, okToCreate: bool, returnAllObjects: bool, skipHiddenObjects: bool, updateMeshTCs: bool) -> list: ...
    def GetRenderPrimitiveList(self, viewport: ViewportInfo, preview: bool) -> RenderPrimitiveList: ...
    def GetSelectedSubObjects(self, ) -> list: ...
    def GetSubObjects(self, ) -> list: ...
    def GetTextureChannels(self, ) -> list: ...
    def GetTextureMapping(self, channel: int, objectTransform: Transform) -> TextureMapping: ...
    @staticmethod
    def GetTightBoundingBox(rhinoObjects: IEnumerable, plane: Plane, boundingBox: BoundingBox) -> bool: ...
    def HasCustomRenderMeshes(self, mt: MeshType, vp: ViewportInfo, flags: Flags, plugin: PlugIn, attrs: DisplayPipelineAttributes) -> bool: ...
    def HasHistoryRecord(self, ) -> bool: ...
    def HasTextureMapping(self, ) -> bool: ...
    def Highlight(self, enable: bool) -> bool: ...
    def HighlightSubObject(self, componentIndex: ComponentIndex, highlight: bool) -> bool: ...
    def HistoryChildren(self, ) -> list: ...
    def HistoryParents(self, ) -> list: ...
    def InVisualAnalysisMode(self, mode: VisualAnalysisMode) -> bool: ...
    def IsActiveInViewport(self, viewport: RhinoViewport) -> bool: ...
    def IsHighlighted(self, checkSubObjects: bool) -> int: ...
    def IsMeshable(self, meshType: MeshType) -> bool: ...
    def IsSelectable(self, ignoreSelectionState: bool, ignoreGripsState: bool, ignoreLayerLocking: bool, ignoreLayerVisibility: bool) -> bool: ...
    def IsSelected(self, checkSubObjects: bool) -> int: ...
    def IsSubObjectHighlighted(self, componentIndex: ComponentIndex) -> bool: ...
    def IsSubObjectSelectable(self, componentIndex: ComponentIndex, ignoreSelectionState: bool) -> bool: ...
    def IsSubObjectSelected(self, componentIndex: ComponentIndex) -> bool: ...
    def MemoryEstimate(self, ) -> int: ...
    def MeshCount(self, meshType: MeshType, parameters: MeshingParameters) -> int: ...
    @staticmethod
    def MeshObjects(rhinoObjects: IEnumerable, parameters: MeshingParameters, uiStyle: int, xform: Transform, meshes: list, attributes: list) -> Result: ...
    def ObjectFrame(self, flags: ObjectFrameFlags) -> Plane: ...
    def RenderMeshes(self, mt: MeshType, vp: ViewportInfo, ancestry: List, flags: Flags, plugin: PlugIn, attrs: DisplayPipelineAttributes) -> RenderMeshes: ...
    def Select(self, on: bool, syncHighlight: bool, persistentSelect: bool, ignoreGripsState: bool, ignoreLayerLocking: bool, ignoreLayerVisibility: bool) -> int: ...
    def SelectSubObject(self, componentIndex: ComponentIndex, select: bool, syncHighlight: bool, persistentSelect: bool) -> int: ...
    def SetCopyHistoryOnReplace(self, bCopy: bool) -> None: ...
    def SetCustomRenderMeshParameter(self, providerId: Guid, parameterName: str, value: object) -> None: ...
    def SetHistory(self, history: HistoryRecord) -> bool: ...
    def SetObjectFrame(self, xform: Transform) -> None: ...
    def SetRenderMeshParameters(self, mp: MeshingParameters) -> bool: ...
    def SetTextureMapping(self, channel: int, tm: TextureMapping, objectTransform: Transform) -> int: ...
    def ShortDescription(self, plural: bool) -> str: ...
    def ShortDescriptionWithClosedStatus(self, prepend: bool, plural: bool, status: int) -> str: ...
    def SupportsRenderPrimitiveList(self, viewport: ViewportInfo, preview: bool) -> bool: ...
    def TryGetGumballFrame(self, frame: GumballFrame) -> bool: ...
    def TryGetRenderPrimitiveBoundingBox(self, viewport: ViewportInfo, preview: bool, boundingBox: BoundingBox) -> bool: ...
    def UnhighlightAllSubObjects(self, ) -> int: ...
    def UnselectAllSubObjects(self, ) -> int: ...

class RhinoObjectEventArgs(EventArgs):
    """.NET: Rhino.DocObjects.RhinoObjectEventArgs"""
    def __init__(self, *args) -> None: ...
    ObjectId: Guid
    TheObject: RhinoObject

class RhinoObjectSelectionEventArgs(EventArgs):
    """.NET: Rhino.DocObjects.RhinoObjectSelectionEventArgs"""
    def __init__(self, *args) -> None: ...
    Selected: bool
    Document: RhinoDoc
    RhinoObjectCount: int
    RhinoObjects: list

class RhinoReplaceObjectEventArgs(EventArgs):
    """.NET: Rhino.DocObjects.RhinoReplaceObjectEventArgs"""
    def __init__(self, *args) -> None: ...
    ObjectId: Guid
    OldRhinoObject: RhinoObject
    NewRhinoObject: RhinoObject
    Document: RhinoDoc

class RhinoTransformObjectsEventArgs(EventArgs):
    """.NET: Rhino.DocObjects.RhinoTransformObjectsEventArgs"""
    def __init__(self, *args) -> None: ...
    TransformEventId: int
    Transform: Transform
    ObjectsWillBeCopied: bool
    ObjectCount: int
    GripCount: int
    GripOwnerCount: int
    Objects: list
    Grips: list
    GripOwners: list

class SectionBackgroundFillMode:
    """.NET: Rhino.DocObjects.SectionBackgroundFillMode"""
    def __init__(self, *args) -> None: ...
    ...

class SectionLabelStyle:
    """.NET: Rhino.DocObjects.SectionLabelStyle"""
    def __init__(self, *args) -> None: ...
    ...

class SectionStyle(ModelComponent):
    """.NET: Rhino.DocObjects.SectionStyle"""
    def __init__(self, *args) -> None: ...
    ComponentType: ModelComponentType
    BackgroundFillMode: SectionBackgroundFillMode
    BackgroundFillColor: Color
    BackgroundFillPrintColor: Color
    BoundaryVisible: bool
    BoundaryWidthScale: float
    BoundaryColor: Color
    BoundaryPrintColor: Color
    SectionFillRule: ObjectSectionFillRule
    HatchIndex: int
    HatchScale: float
    HatchRotationRadians: float
    HatchPatternColor: Color
    HatchPatternPrintColor: Color
    IsSystemComponent: bool
    IsDeleted: bool
    IsReference: bool
    Id: Guid
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    Name: str
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def GetBoundaryLinetype(self, ) -> Linetype: ...
    def RemoveBoundaryLinetype(self, ) -> None: ...
    def SetBoundaryLinetype(self, linetype: Linetype) -> None: ...

class SelectionMethod:
    """.NET: Rhino.DocObjects.SelectionMethod"""
    def __init__(self, *args) -> None: ...
    ...

class SubDObject(RhinoObject):
    """.NET: Rhino.DocObjects.SubDObject"""
    def __init__(self, *args) -> None: ...
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary

class SurfaceObject(RhinoObject):
    """.NET: Rhino.DocObjects.SurfaceObject"""
    def __init__(self, *args) -> None: ...
    SurfaceGeometry: Surface
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def DuplicateSurfaceGeometry(self, ) -> Surface: ...

class TextDisplayAlignment:
    """.NET: Rhino.DocObjects.TextDisplayAlignment"""
    def __init__(self, *args) -> None: ...
    ...

class TextDotObject(RhinoObject):
    """.NET: Rhino.DocObjects.TextDotObject"""
    def __init__(self, *args) -> None: ...
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary

class TextHorizontalAlignment:
    """.NET: Rhino.DocObjects.TextHorizontalAlignment"""
    def __init__(self, *args) -> None: ...
    ...

class TextObject(AnnotationObjectBase):
    """.NET: Rhino.DocObjects.TextObject"""
    def __init__(self, *args) -> None: ...
    TextGeometry: TextEntity
    DisplayText: str
    AnnotationGeometry: AnnotationBase
    HasMeasurableTextFields: bool
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def GetTextCorners(self, viewport: RhinoViewport) -> list: ...

class TextOrientation:
    """.NET: Rhino.DocObjects.TextOrientation"""
    def __init__(self, *args) -> None: ...
    ...

class TextVerticalAlignment:
    """.NET: Rhino.DocObjects.TextVerticalAlignment"""
    def __init__(self, *args) -> None: ...
    ...

class Texture(CommonObject):
    """.NET: Rhino.DocObjects.Texture"""
    def __init__(self, *args) -> None: ...
    FileName: str
    FileReference: FileReference
    Id: Guid
    Enabled: bool
    TextureType: TextureType
    MinFilter: TextureFilter
    MagFilter: TextureFilter
    MappingChannelId: int
    ProjectionMode: TextureProjectionModes
    WcsProjected: bool
    TreatAsLinear: bool
    WcsBoxProjected: bool
    TextureCombineMode: TextureCombineMode
    WrapU: TextureUvwWrapping
    WrapV: TextureUvwWrapping
    WrapW: TextureUvwWrapping
    ApplyUvwTransform: bool
    UvwTransform: Transform
    Repeat: Vector2d
    Offset: Vector2d
    Rotation: float
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def GetAlphaBlendValues(self, constant: float, a0: float, a1: float, a2: float, a3: float) -> None: ...
    def SetAlphaBlendValues(self, constant: float, a0: float, a1: float, a2: float, a3: float) -> None: ...
    def SetRGBBlendValues(self, color: Color, a0: float, a1: float, a2: float, a3: float) -> None: ...

class TextureCombineMode:
    """.NET: Rhino.DocObjects.TextureCombineMode"""
    def __init__(self, *args) -> None: ...
    ...

class TextureFilter:
    """.NET: Rhino.DocObjects.TextureFilter"""
    def __init__(self, *args) -> None: ...
    ...

class TextureProjectionModes:
    """.NET: Rhino.DocObjects.TextureProjectionModes"""
    def __init__(self, *args) -> None: ...
    ...

class TextureType:
    """.NET: Rhino.DocObjects.TextureType"""
    def __init__(self, *args) -> None: ...
    ...

class TextureUvwWrapping:
    """.NET: Rhino.DocObjects.TextureUvwWrapping"""
    def __init__(self, *args) -> None: ...
    ...

class ViewInfo:
    """.NET: Rhino.DocObjects.ViewInfo"""
    def __init__(self, *args) -> None: ...
    Name: str
    Maximized: bool
    NamedViewId: Guid
    DisplayModeId: Guid
    ViewType: ViewType
    ShowConstructionGrid: bool
    ShowConstructionAxes: bool
    ShowConstructionZAxis: bool
    ShowWorldAxes: bool
    LockedProjection: bool
    RenderingSize: Size
    WallpaperFilename: str
    ShowWallpaperInGrayScale: bool
    WallpaperHidden: bool
    FocalBlurDistance: float
    FocalBlurAperture: float
    FocalBlurJitter: float
    FocalBlurSampleCount: int
    FocalBlurMode: ViewInfoFocalBlurModes
    SectionBehavior: ViewSectionBehavior
    ClippingPlanesIds: list
    Viewport: ViewportInfo
    def ClippingPlaneSurfaces(self, ) -> list: ...
    def Dispose(self, ) -> None: ...
    def GetConstructionPlane(self, ) -> ConstructionPlane: ...
    def GetPageSettings(self, ) -> PageSettings: ...
    def GetWindowPosition(self, left: float, right: float, top: float, bottom: float) -> None: ...
    def SetConstructionPlane(self, constructionPlane: ConstructionPlane) -> None: ...
    def SetPageSettings(self, pageSettings: PageSettings) -> None: ...
    def SetWindowPosition(self, left: float, right: float, top: float, bottom: float) -> None: ...

class ViewInfoFocalBlurModes:
    """.NET: Rhino.DocObjects.ViewInfoFocalBlurModes"""
    def __init__(self, *args) -> None: ...
    ...

class ViewSectionBehavior:
    """.NET: Rhino.DocObjects.ViewSectionBehavior"""
    def __init__(self, *args) -> None: ...
    ...

class ViewType:
    """.NET: Rhino.DocObjects.ViewType"""
    def __init__(self, *args) -> None: ...
    ...

class ViewportInfo(CommonObject):
    """.NET: Rhino.DocObjects.ViewportInfo"""
    def __init__(self, *args) -> None: ...
    IsValidCamera: bool
    IsValidFrustum: bool
    IsPerspectiveProjection: bool
    IsParallelProjection: bool
    IsTwoPointPerspectiveProjection: bool
    CameraLocation: Point3d
    CameraDirection: Vector3d
    CameraUp: Vector3d
    IsCameraLocationLocked: bool
    IsCameraDirectionLocked: bool
    IsCameraUpLocked: bool
    IsFrustumLeftRightSymmetric: bool
    IsFrustumTopBottomSymmetric: bool
    CameraX: Vector3d
    CameraY: Vector3d
    CameraZ: Vector3d
    DefaultCameraDirection: Vector3d
    FrustumAspect: float
    FrustumCenter: Point3d
    FrustumLeft: float
    FrustumRight: float
    FrustumBottom: float
    FrustumTop: float
    FrustumNear: float
    FrustumFar: float
    FrustumWidth: float
    FrustumHeight: float
    FrustumMinimumDiameter: float
    FrustumMaximumDiameter: float
    FrustumNearPlane: Plane
    FrustumFarPlane: Plane
    FrustumLeftPlane: Plane
    FrustumRightPlane: Plane
    FrustumBottomPlane: Plane
    FrustumTopPlane: Plane
    ScreenPort: Rectangle
    ScreenPortAspect: float
    CameraAngle: float
    Camera35mmLensLength: float
    ViewScale: SizeF
    TargetPoint: Point3d
    PerspectiveMinNearOverFar: float
    PerspectiveMinNearDist: float
    Id: Guid
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    @staticmethod
    def CalculateCameraRotationAngle(direction: Vector3d, up: Vector3d) -> float: ...
    @staticmethod
    def CalculateCameraUpDirection(location: Point3d, direction: Vector3d, angle: float) -> Vector3d: ...
    def ChangeToParallelProjection(self, symmetricFrustum: bool) -> bool: ...
    def ChangeToParallelReflectedProjection(self, ) -> bool: ...
    def ChangeToPerspectiveProjection(self, targetDistance: float, symmetricFrustum: bool, lensLength: float) -> bool: ...
    def ChangeToSymmetricFrustum(self, isLeftRightSymmetric: bool, isTopBottomSymmetric: bool, targetDistance: float) -> bool: ...
    def ChangeToTwoPointPerspectiveProjection(self, targetDistance: float, up: Vector3d, lensLength: float) -> bool: ...
    def DollyCamera(self, dollyVector: Vector3d) -> bool: ...
    def DollyExtents(self, geometry: IEnumerable, border: float) -> bool: ...
    def DollyFrustum(self, dollyDistance: float) -> bool: ...
    def Extents(self, halfViewAngleRadians: float, bbox: BoundingBox) -> bool: ...
    def FrustumCenterPoint(self, targetDistance: float) -> Point3d: ...
    def GetBoundingBoxDepth(self, bbox: BoundingBox, nearDistance: float, farDistance: float) -> bool: ...
    def GetCameraAngles(self, halfDiagonalAngleRadians: float, halfVerticalAngleRadians: float, halfHorizontalAngleRadians: float) -> bool: ...
    def GetCameraFrame(self, location: Point3d, cameraX: Vector3d, cameraY: Vector3d, cameraZ: Vector3d) -> bool: ...
    def GetDollyCameraVector(self, screenX0: int, screenY0: int, screenX1: int, screenY1: int, projectionPlaneDistance: float) -> Vector3d: ...
    def GetFarPlaneCorners(self, ) -> list: ...
    def GetFramePlaneCorners(self, depth: float) -> list: ...
    def GetFrustum(self, left: float, right: float, bottom: float, top: float, nearDistance: float, farDistance: float) -> bool: ...
    def GetFrustumLine(self, screenX: float, screenY: float) -> Line: ...
    def GetNearPlaneCorners(self, ) -> list: ...
    def GetPointDepth(self, point: Point3d, distance: float) -> bool: ...
    def GetScreenPort(self, near: int, far: int) -> Rectangle: ...
    def GetScreenPortLocation(self, left: int, top: int, right: int, bottom: int) -> None: ...
    def GetSphereDepth(self, sphere: Sphere, nearDistance: float, farDistance: float) -> bool: ...
    def GetViewScale(self, ) -> list: ...
    def GetWorldToScreenScale(self, pointInFrustum: Point3d) -> float: ...
    def GetXform(self, sourceSystem: CoordinateSystem, destinationSystem: CoordinateSystem) -> Transform: ...
    def RotateCamera(self, rotationAngleRadians: float, rotationAxis: Vector3d, rotationCenter: Point3d) -> bool: ...
    def SetCameraDirection(self, direction: Vector3d) -> bool: ...
    def SetCameraLocation(self, location: Point3d) -> bool: ...
    def SetCameraUp(self, up: Vector3d) -> bool: ...
    def SetFrustum(self, left: float, right: float, bottom: float, top: float, nearDistance: float, farDistance: float) -> bool: ...
    def SetFrustumNearFar(self, nearDistance: float, farDistance: float, minNearDistance: float, minNearOverFar: float, targetDistance: float) -> bool: ...
    def SetScreenPort(self, left: int, right: int, bottom: int, top: int, near: int, far: int) -> bool: ...
    def SetViewScale(self, scaleX: float, scaleY: float, scaleZ: float) -> None: ...
    def TargetDistance(self, useFrustumCenterFallback: bool) -> float: ...
    def TransformCamera(self, xform: Transform) -> bool: ...
    def UnlockCamera(self, ) -> None: ...
    def UnlockFrustumSymmetry(self, ) -> None: ...
    def ZoomToScreenRect(self, left: int, top: int, right: int, bottom: int) -> bool: ...

class Worksession:
    """.NET: Rhino.DocObjects.Worksession"""
    def __init__(self, *args) -> None: ...
    Document: RhinoDoc
    RuntimeSerialNumber: int
    FileName: str
    ModelCount: int
    ModelPaths: list
    @staticmethod
    def FileNameFromRuntimeSerialNumber(runtimeSerialNumber: int) -> str: ...
    def ModelPathFromSerialNumber(self, modelSerialNumber: int) -> str: ...
