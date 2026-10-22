# Auto-generated — Civil 26 — Autodesk.AutoCAD.DatabaseServices

class AbstractViewTable(SymbolTable):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AbstractViewTable"""
    def __init__(self, *args) -> None: ...
    IncludingErased: SymbolTable
    Item: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AbstractViewTableRecord(SymbolTableRecord):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AbstractViewTableRecord"""
    def __init__(self, *args) -> None: ...
    ToneOperatorParameters: ToneOperatorParameters
    VisualStyleId: ObjectId
    Background: ObjectId
    ViewOrthographic: OrthographicView
    Elevation: float
    UcsName: ObjectId
    UcsOrthographic: OrthographicView
    Ucs: CoordinateSystem3d
    SunId: ObjectId
    AmbientLightColor: Color
    Contrast: float
    Brightness: float
    DefaultLightingType: DefaultLightingType
    DefaultLightingOn: bool
    FrontClipAtEye: bool
    BackClipEnabled: bool
    FrontClipEnabled: bool
    PerspectiveEnabled: bool
    BackClipDistance: float
    FrontClipDistance: float
    LensLength: float
    ViewTwist: float
    ViewDirection: Vector3d
    Target: Point3d
    Width: float
    Height: float
    CenterPoint: Point2d
    IsResolved: bool
    IsDependent: bool
    Name: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetSun(self, sun: DBObject) -> ObjectId: ...
    def SetUcs(self, origin: Point3d, x: Vector3d, y: Vector3d) -> None: ...
    def SetUcsToWorld(self, ) -> None: ...
    def SetViewDirection(self, view: OrthographicView) -> None: ...

class ActionsToEvaluateCallback:
    """.NET: Autodesk.AutoCAD.DatabaseServices.ActionsToEvaluateCallback"""
    def __init__(self, *args) -> None: ...
    def Dispose(self, ) -> None: ...
    def NeedsToEvaluate(self, objectId: ObjectId, newStatus: AssocStatus, ownedActionsAlso: bool) -> None: ...

class AddObjectSnapInfo:
    """.NET: Autodesk.AutoCAD.DatabaseServices.AddObjectSnapInfo"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, context: ObjectSnapContext, result: ObjectSnapInfo, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, context: ObjectSnapContext, result: ObjectSnapInfo) -> None: ...

class AlignedDimension(Dimension):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AlignedDimension"""
    def __init__(self, *args) -> None: ...
    Oblique: float
    DimLinePoint: Point3d
    XLine2Point: Point3d
    XLine1Point: Point3d
    Dimaltmzf: float
    Dimmzf: float
    Dimaltmzs: str
    Dimmzs: str
    Dimblk2: ObjectId
    Dimblk1: ObjectId
    Dimblk: ObjectId
    Dimpost: str
    Dimapost: str
    Dimzin: int
    Dimupt: bool
    Dimtzin: int
    Dimtxtdirection: bool
    Dimtxt: float
    TextStyleId: ObjectId
    Dimtvp: float
    Dimtsz: float
    Dimtp: float
    Dimtolj: int
    Dimtol: bool
    Dimtoh: bool
    Dimtofl: bool
    Dimtmove: int
    Dimtm: float
    Dimtix: bool
    Dimtih: bool
    Dimtfillclr: Color
    Dimtfill: int
    Dimtfac: float
    Dimtdec: int
    Dimtad: int
    Dimsoxd: bool
    Dimse2: bool
    Dimse1: bool
    Dimsd2: bool
    Dimsd1: bool
    Dimscale: float
    Dimsah: bool
    Dimrnd: float
    DimensionStyleName: str
    CenterMarkSize: float
    CenterMarkType: DimensionCenterMarkType
    ToleranceSuppressZeroInches: bool
    ToleranceSuppressZeroFeet: bool
    ToleranceSuppressTrailingZeros: bool
    ToleranceSuppressLeadingZeros: bool
    AltToleranceSuppressZeroInches: bool
    AltToleranceSuppressZeroFeet: bool
    AltToleranceSuppressTrailingZeros: bool
    AltToleranceSuppressLeadingZeros: bool
    AltSuppressZeroInches: bool
    AltSuppressZeroFeet: bool
    AltSuppressTrailingZeros: bool
    AltSuppressLeadingZeros: bool
    AlternateSuffix: str
    AlternatePrefix: str
    SuppressZeroInches: bool
    SuppressZeroFeet: bool
    SuppressTrailingZeros: bool
    SuppressLeadingZeros: bool
    SuppressAngularTrailingZeros: bool
    SuppressAngularLeadingZeros: bool
    Suffix: str
    Prefix: str
    Dimlwe: LineWeight
    Dimlwd: LineWeight
    Dimlunit: int
    Dimltype: ObjectId
    Dimltex2: ObjectId
    Dimltex1: ObjectId
    Dimlim: bool
    Dimlfac: float
    Dimldrblk: ObjectId
    Dimjust: int
    Dimjogang: float
    Dimgap: float
    Dimfxlen: float
    DimfxlenOn: bool
    Dimfrac: int
    Dimexo: float
    Dimexe: float
    Dimdsep: str
    Dimdli: float
    Dimdle: float
    Dimdec: int
    Dimclrt: Color
    Dimclre: Color
    Dimclrd: Color
    Dimcen: float
    Dimazin: int
    Dimaunit: int
    Dimatfit: int
    Dimasz: float
    Dimarcsym: int
    Dimaltz: int
    Dimaltu: int
    Dimalttz: int
    Dimalttd: int
    Dimaltrnd: float
    Dimaltf: float
    Dimaltd: int
    Dimalt: bool
    Dimadec: int
    DynamicDimension: bool
    Measurement: float
    DimBlockPosition: Point3d
    DimBlockId: ObjectId
    HorizontalRotation: float
    TextLineSpacingFactor: float
    TextLineSpacingStyle: LineSpacingStyle
    TextAttachment: AttachmentPoint
    DimensionStyle: ObjectId
    TextRotation: float
    DimensionText: str
    Elevation: float
    Normal: Vector3d
    UsingDefaultTextPosition: bool
    TextPosition: Point3d
    TextDefinedSize: Vector2d
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AngleConstraint:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.AngleConstraint"""
    def __init__(self, *args) -> None: ...
    DegreesAny: int  # = 0
    Degrees015: int  # = 1
    Degrees030: int  # = 2
    Degrees045: int  # = 3
    Degrees060: int  # = 4
    Degrees090: int  # = 6
    DegreesHorz: int  # = 12
class AngularConstraint(ExplicitConstraint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AngularConstraint"""
    def __init__(self, *args) -> None: ...
    SectorType: AngularSectorType
    MeasuredValue: float
    DimDependencyId: ObjectId
    ValueDependencyId: ObjectId
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def AngleMultiplier() -> float: ...
    @staticmethod
    def SetAngleMultiplier(multiplier: float) -> None: ...

class AnnotationScale(ObjectContext):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AnnotationScale"""
    def __init__(self, *args) -> None: ...
    IsTemporaryScale: bool
    Scale: float
    DrawingUnits: float
    PaperUnits: float
    CollectionName: str
    UniqueIdentifier: IntPtr
    Name: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AnnotationType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.AnnotationType"""
    def __init__(self, *args) -> None: ...
    MText: int  # = 0
    FeatureControlFrame: int  # = 1
    BlockRef: int  # = 2
    NoAnnotation: int  # = 3
class AnnotativeStates:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.AnnotativeStates"""
    def __init__(self, *args) -> None: ...
    True_: int  # = 0
    False_: int  # = 1
    NotApplicable: int  # = 2
class ApplicationLoadReasons:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.ApplicationLoadReasons"""
    def __init__(self, *args) -> None: ...
    OnProxyDetection: int  # = 1
    OnAutoCADStartup: int  # = 2
    OnCommandInvocation: int  # = 4
    OnLoadRequest: int  # = 8
    LoadDisabled: int  # = 16
    TransparentlyLoadable: int  # = 32
class Arc(Curve):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Arc"""
    def __init__(self, *args) -> None: ...
    TotalAngle: float
    Length: float
    Normal: Vector3d
    Thickness: float
    EndAngle: float
    StartAngle: float
    Radius: float
    Center: Point3d
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ArcDimension(Dimension):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ArcDimension"""
    def __init__(self, *args) -> None: ...
    HasLeader: bool
    IsPartial: bool
    ArcSymbolType: int
    XLine2Point: Point3d
    XLine1Point: Point3d
    Leader2Point: Point3d
    Leader1Point: Point3d
    CenterPoint: Point3d
    ArcPoint: Point3d
    ArcEndParam: float
    ArcStartParam: float
    Dimaltmzf: float
    Dimmzf: float
    Dimaltmzs: str
    Dimmzs: str
    Dimblk2: ObjectId
    Dimblk1: ObjectId
    Dimblk: ObjectId
    Dimpost: str
    Dimapost: str
    Dimzin: int
    Dimupt: bool
    Dimtzin: int
    Dimtxtdirection: bool
    Dimtxt: float
    TextStyleId: ObjectId
    Dimtvp: float
    Dimtsz: float
    Dimtp: float
    Dimtolj: int
    Dimtol: bool
    Dimtoh: bool
    Dimtofl: bool
    Dimtmove: int
    Dimtm: float
    Dimtix: bool
    Dimtih: bool
    Dimtfillclr: Color
    Dimtfill: int
    Dimtfac: float
    Dimtdec: int
    Dimtad: int
    Dimsoxd: bool
    Dimse2: bool
    Dimse1: bool
    Dimsd2: bool
    Dimsd1: bool
    Dimscale: float
    Dimsah: bool
    Dimrnd: float
    DimensionStyleName: str
    CenterMarkSize: float
    CenterMarkType: DimensionCenterMarkType
    ToleranceSuppressZeroInches: bool
    ToleranceSuppressZeroFeet: bool
    ToleranceSuppressTrailingZeros: bool
    ToleranceSuppressLeadingZeros: bool
    AltToleranceSuppressZeroInches: bool
    AltToleranceSuppressZeroFeet: bool
    AltToleranceSuppressTrailingZeros: bool
    AltToleranceSuppressLeadingZeros: bool
    AltSuppressZeroInches: bool
    AltSuppressZeroFeet: bool
    AltSuppressTrailingZeros: bool
    AltSuppressLeadingZeros: bool
    AlternateSuffix: str
    AlternatePrefix: str
    SuppressZeroInches: bool
    SuppressZeroFeet: bool
    SuppressTrailingZeros: bool
    SuppressLeadingZeros: bool
    SuppressAngularTrailingZeros: bool
    SuppressAngularLeadingZeros: bool
    Suffix: str
    Prefix: str
    Dimlwe: LineWeight
    Dimlwd: LineWeight
    Dimlunit: int
    Dimltype: ObjectId
    Dimltex2: ObjectId
    Dimltex1: ObjectId
    Dimlim: bool
    Dimlfac: float
    Dimldrblk: ObjectId
    Dimjust: int
    Dimjogang: float
    Dimgap: float
    Dimfxlen: float
    DimfxlenOn: bool
    Dimfrac: int
    Dimexo: float
    Dimexe: float
    Dimdsep: str
    Dimdli: float
    Dimdle: float
    Dimdec: int
    Dimclrt: Color
    Dimclre: Color
    Dimclrd: Color
    Dimcen: float
    Dimazin: int
    Dimaunit: int
    Dimatfit: int
    Dimasz: float
    Dimarcsym: int
    Dimaltz: int
    Dimaltu: int
    Dimalttz: int
    Dimalttd: int
    Dimaltrnd: float
    Dimaltf: float
    Dimaltd: int
    Dimalt: bool
    Dimadec: int
    DynamicDimension: bool
    Measurement: float
    DimBlockPosition: Point3d
    DimBlockId: ObjectId
    HorizontalRotation: float
    TextLineSpacingFactor: float
    TextLineSpacingStyle: LineSpacingStyle
    TextAttachment: AttachmentPoint
    DimensionStyle: ObjectId
    TextRotation: float
    DimensionText: str
    Elevation: float
    Normal: Vector3d
    UsingDefaultTextPosition: bool
    TextPosition: Point3d
    TextDefinedSize: Vector2d
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Assoc2dConstraintCallback:
    """.NET: Autodesk.AutoCAD.DatabaseServices.Assoc2dConstraintCallback"""
    def __init__(self, *args) -> None: ...
    def CanBeRelaxed(self, constraint: ExplicitConstraint) -> bool: ...
    def ConstraintDeactivated(self, constraint: ExplicitConstraint, deactivated: bool) -> None: ...
    def Dispose(self, ) -> None: ...

class Assoc2dConstraintGroup(AssocAction):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Assoc2dConstraintGroup"""
    def __init__(self, *args) -> None: ...
    Constraints: list
    ConstrainedGeometries: list
    GetDOF: int
    WorkPlane: Plane
    CurrentEvaluationCallback: AssocEvaluationCallback
    IsActionEvaluationInProgress: bool
    OwningNetwork: ObjectId
    Status: AssocStatus
    IsActionBodyAProxy: bool
    ActionBody: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add3PointAngularConstraint(self, consPoint1: ConstrainedPoint, consPoint2: ConstrainedPoint, consPoint3: ConstrainedPoint, sectorType: AngularSectorType, valueDependencyId: ObjectId, dimDependencyId: ObjectId) -> ThreePointAngleConstraint: ...
    def AddAngularConstraint(self, consLine1: ConstrainedLine, consLine2: ConstrainedLine, sectorType: AngularSectorType, valueDependencyId: ObjectId, dimDependencyId: ObjectId) -> AngularConstraint: ...
    def AddConstrainedGeometry(self, subentPath: FullSubentityPath) -> ConstrainedGeometry: ...
    def AddDistanceConstraint(self, consGeom1: ConstrainedGeometry, consGeom2: ConstrainedGeometry, directionType: DistanceDirectionType, valueDependencyId: ObjectId, dimDependencyId: ObjectId, fixedDirection: Vector3d, directionLine: ConstrainedLine) -> DistanceConstraint: ...
    def AddGeometricalConstraint(self, type: ConstraintType, consGeoms: list) -> GeometricalConstraint: ...
    @staticmethod
    def AddGlobalCallback(callback: Assoc2dConstraintCallback) -> None: ...
    def AddRadiusDiameterConstraint(self, consGeom: ConstrainedGeometry, type: RadDiaConstrType, valueDependencyId: ObjectId, dimDependencyId: ObjectId) -> RadiusDiameterConstraint: ...
    def AutoConstrain(self, paths: list, tol: Tolerance, callback: AutoConstrainEvaluationCallback) -> None: ...
    def ConstraintStatus(self, constraint: GeometricalConstraint) -> SolutionStatusType: ...
    def DeleteConstrainedGeometry(self, geomDependencyId: ObjectId) -> None: ...
    def DeleteConstraint(self, geomConst: GeometricalConstraint) -> None: ...
    def GeometryMirrored(self, geomDependency: AssocGeomDependency) -> None: ...
    def GeometryStatus(self, consGeom: ConstrainedGeometry) -> SolutionStatusType: ...
    def GetAllConnectedGeomDependencies(self, srcGeomDependencyIds: ObjectIdCollection) -> ObjectIdCollection: ...
    def GetConstrainedGeometry(self, geomDependency: AssocGeomDependency, ptType: ImplicitPointType, defPtIndex: int, bCreateArcLineMid: bool) -> ConstrainedGeometry: ...
    def GetGroupNode(self, nodeId: int) -> ConstraintGroupNode: ...
    @staticmethod
    def GlobalCallback() -> Assoc2dConstraintCallback: ...
    def RegenDimensionSystem(self, ) -> None: ...
    @staticmethod
    def RemoveGlobalCallback(callback: Assoc2dConstraintCallback) -> None: ...
    def SolutionStatus(self, alsoCheckForConstraints: bool) -> SolutionStatusType: ...
    def TransformActionBy(self, transform: Matrix3d) -> None: ...

class AssocAction(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocAction"""
    def __init__(self, *args) -> None: ...
    CurrentEvaluationCallback: AssocEvaluationCallback
    IsActionEvaluationInProgress: bool
    OwningNetwork: ObjectId
    Status: AssocStatus
    IsActionBodyAProxy: bool
    ActionBody: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddDependency(self, dependencyId: ObjectId, setThisActionAsOwningAction: bool) -> None: ...
    def AddMoreObjectsToDeepClone(self, idMap: IdMapping, additionalObjectsToClone: ObjectIdCollection) -> None: ...
    def AreDependenciesEqual(self, dependency1: AssocDependency, dependency2: AssocDependency) -> bool: ...
    def AreDependenciesOnTheSameThing(self, dependency1: AssocDependency, dependency2: AssocDependency) -> bool: ...
    def DependentObjectCloned(self, dependency: AssocDependency, dbObj: DBObject, newObj: DBObject) -> None: ...
    def DragStatus(self, status: DragStatus) -> None: ...
    def Evaluate(self, evaluationCallback: AssocEvaluationCallback) -> None: ...
    def EvaluateDependencies(self, ) -> None: ...
    def EvaluateDependency(self, dependency: AssocDependency) -> None: ...
    def EvaluationPriority(self, ) -> AssocEvaluationPriority: ...
    @staticmethod
    def GetActionBody(actionId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetActionsDependentOnObject(dbObj: DBObject, readDependenciesWanted: bool, writeDependenciesWanted: bool, actionIds: ObjectIdCollection) -> None: ...
    def GetDependencies(self, readDependenciesWanted: bool, writeDependenciesWanted: bool) -> ObjectIdCollection: ...
    def GetDependentActionsToEvaluate(self, actionsToEvaluateCallback: ActionsToEvaluateCallback) -> None: ...
    def GetDependentObjects(self, readDependenciesWanted: bool, writeDependenciesWanted: bool) -> ObjectIdCollection: ...
    def HasDependencyCachedValue(self, dependency: AssocDependency) -> bool: ...
    def IsEqualTo(self, otherAction: AssocAction) -> bool: ...
    def IsExternalDependency(self, dependency: AssocDependency) -> bool: ...
    def IsOwnedDependency(self, dependency: AssocDependency) -> bool: ...
    def IsRelevantDependencyChange(self, dependency: AssocDependency) -> bool: ...
    def ObjectThatOwnsNetworkInstance(self, ) -> ObjectId: ...
    def OwnedDependencyStatusChanged(self, ownedDependency: AssocDependency, previousStatus: AssocStatus) -> None: ...
    def PostProcessAfterDeepClone(self, idMap: IdMapping) -> None: ...
    def PostProcessAfterDeepCloneCancel(self, idMap: IdMapping) -> None: ...
    @staticmethod
    def RemoveActionsControllingObject(objID: ObjectId, readOnlyDependencyHandling: int, objectToRedirectReadOnlyDependenciesTo: ObjectId) -> None: ...
    def RemoveAllDependencies(self, alsoEraseThem: bool) -> None: ...
    def RemoveDependency(self, dependencyId: ObjectId, alsoEraseIt: bool) -> None: ...
    def SetOwningNetwork(self, networkId: ObjectId, alsoSetAsDatabaseOwner: bool) -> None: ...
    def SetStatus(self, newStatus: AssocStatus, notifyOwningNetwork: bool, setInOwnedActions: bool) -> None: ...
    def TransformActionBy(self, transform: Matrix3d) -> None: ...

class AssocActionBody(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocActionBody"""
    def __init__(self, *args) -> None: ...
    OwnedParams: ObjectIdCollection
    ParamCount: int
    OwningNetwork: ObjectId
    Status: AssocStatus
    ParentAction: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddDependency(self, dependencyId: ObjectId, setThisActionAsOwningAction: bool) -> None: ...
    def AddMoreObjectsToDeepCloneOverride(self, idMap: IdMapping, additionalObjectsToClone: ObjectIdCollection) -> None: ...
    def AddParam(self, paramId: ObjectId, paramIndex: int) -> None: ...
    def AreDependenciesEqualOverride(self, dependency1: AssocDependency, dependency2: AssocDependency) -> bool: ...
    def AreDependenciesOnTheSameThingOverride(self, dependency1: AssocDependency, dependency2: AssocDependency) -> bool: ...
    @staticmethod
    def CreateActionAndActionBodyAndPostToDatabase(pActionBodyClass: RXClass, objectId: ObjectId, createdActionId: ObjectId, createdActionBodyId: ObjectId) -> None: ...
    def DependentObjectClonedOverride(self, pDependency: AssocDependency, dbObj: DBObject, dbNewObj: DBObject) -> None: ...
    def DragStatusOverride(self, status: DragStatus) -> None: ...
    def DwgInFields(self, filer: DwgFiler) -> ErrorStatus: ...
    def DwgOutFields(self, filer: DwgFiler) -> ErrorStatus: ...
    def DxfInFields(self, filer: DxfFiler) -> ErrorStatus: ...
    def DxfOutFields(self, filer: DxfFiler) -> ErrorStatus: ...
    def EvaluateDependencies(self, ) -> None: ...
    def EvaluateDependencyOverride(self, dependency: AssocDependency) -> bool: ...
    def EvaluateOverride(self, ) -> None: ...
    def EvaluationPriorityOverride(self, priority: AssocEvaluationPriority) -> None: ...
    @staticmethod
    def GetActionBodiesOnObject(pObject: DBObject, ignoreInternalActions: bool, ignoreSuppressedActions: bool, creationActionBodyId: ObjectId, modificationActionBodyIds: ObjectIdCollection, readOnlyActionBodyIds: ObjectIdCollection) -> None: ...
    def GetDependencies(self, readDependenciesWanted: bool, writeDependenciesWanted: bool) -> ObjectIdCollection: ...
    def GetDependenciesOverride(self, readDependenciesWanted: bool, writeDependenciesWanted: bool) -> ObjectIdCollection: ...
    def GetDependentActionsToEvaluateOverride(self, actionsToEvaluateCallback: ActionsToEvaluateCallback) -> None: ...
    def GetDependentObjectsOverride(self, readDependenciesWanted: bool, writeDependenciesWanted: bool) -> ObjectIdCollection: ...
    @staticmethod
    def GetParentAction(actionBodyId: ObjectId) -> ObjectId: ...
    def GetValueParam(self, paramName: str, paramIndex: int) -> ValueParam: ...
    def GetValueParamArray(self, paramName: str) -> list: ...
    def GetValueParamUnitType(self, paramName: str) -> UnitType: ...
    def HasAnyErasedOrBrokenDependencies(self, ) -> bool: ...
    def HasDependencyCachedValueOverride(self, dependency: AssocDependency) -> bool: ...
    def IsActionEvaluationInProgress(self, ) -> bool: ...
    def IsEqualToOverride(self, otherAction: AssocAction) -> bool: ...
    def IsExternalDependencyOverride(self, dependency: AssocDependency) -> bool: ...
    def IsOwnedDependencyOverride(self, dependency: AssocDependency) -> bool: ...
    def IsRelevantDependencyChangeOverride(self, dependency: AssocDependency) -> bool: ...
    def OwnedDependencyStatusChangedOverride(self, ownedDependency: AssocDependency, previousStatus: AssocStatus) -> None: ...
    def OwnedValueParamNames(self, ) -> list: ...
    def ParamAtIndex(self, paramIndex: int) -> ObjectId: ...
    def ParamAtName(self, paramName: str, index: int) -> ObjectId: ...
    def ParamsAtName(self, paramName: str) -> ObjectIdCollection: ...
    def PostProcessAfterDeepCloneCancelOverride(self, idMap: IdMapping) -> None: ...
    def PostProcessAfterDeepCloneOverride(self, idMap: IdMapping) -> None: ...
    def RemoveAllDependencies(self, alsoEraseThem: bool) -> None: ...
    def RemoveAllDependenciesOverride(self, alsoEraseThem: bool) -> None: ...
    def RemoveAllParams(self, alsoEraseThem: bool) -> None: ...
    def RemoveDependency(self, dependencyId: ObjectId, alsoEraseIt: bool) -> None: ...
    def RemoveParam(self, paramId: ObjectId, alsoEraseIt: bool) -> None: ...
    def RemoveValueParam(self, paramName: str) -> None: ...
    def SetStatus(self, newStatus: AssocStatus, notifyOwningNetwork: bool, setInOwnedActions: bool) -> None: ...
    def SetValueParam(self, paramName: str, param: ValueParam, silentMode: bool, paramIndex: int) -> str: ...
    def SetValueParamArray(self, paramName: str, valueParams: list, silentMode: bool) -> list: ...
    def SetValueParamUnitType(self, paramName: str, unitType: UnitType) -> None: ...
    def TransformActionByOverride(self, A_0: Matrix3d) -> None: ...
    def ValueParamInputVariables(self, paramName: str) -> ObjectIdCollection: ...
    def currentEvaluationCallback(self, ) -> AssocEvaluationCallback: ...

class AssocActionParam(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocActionParam"""
    def __init__(self, *args) -> None: ...
    Name: str
    ParentAction: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def DetachDependencies(self, ) -> None: ...
    def GetDependencies(self, readDependenciesWanted: bool, writeDependenciesWanted: bool) -> ObjectIdCollection: ...
    def MakeParamConstant(self, ) -> None: ...
    def MakeParamEmpty(self, alsoEraseOwnedObjects: bool) -> None: ...
    def TransformConstantGeometry(self, transform: Matrix3d) -> None: ...

class AssocArray:
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocArray"""
    def __init__(self, *args) -> None: ...
    SourceEntities: ObjectIdCollection
    EntityId: ObjectId
    def AddSourceEntity(self, sourceEntity: ObjectId, basePoint: Point3d) -> None: ...
    @staticmethod
    def CreateArray(sourceEntities: ObjectIdCollection, basePoint: VertexRef, parameters: AssocArrayParameters) -> AssocArray: ...
    def DeleteItem(self, index: ItemLocator, bErase: bool) -> None: ...
    @staticmethod
    def Explode(entity: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def GetAssociativeArray(entity: ObjectId) -> AssocArray: ...
    def GetItemTransform(self, index: ItemLocator) -> Matrix3d: ...
    def GetParameters(self, ) -> AssocArrayParameters: ...
    @staticmethod
    def IsAssociativeArray(entity: ObjectId) -> bool: ...
    def IsErased(self, index: ItemLocator) -> bool: ...
    def RemoveSourceEntity(self, sourceEntity: ObjectId) -> None: ...
    def ReplaceItems(self, indices: list, substEntities: ObjectIdCollection, basePoint: VertexRef) -> None: ...
    def ResetItems(self, ) -> None: ...
    def TransformItemBy(self, index: ItemLocator, transform: Matrix3d) -> None: ...
    @staticmethod
    def getItemLocators(subPaths: list) -> list: ...
    def getItems(self, skipErased: bool) -> list: ...

class AssocArrayCommonParameters(AssocArrayParameters):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocArrayCommonParameters"""
    def __init__(self, *args) -> None: ...
    BasePoint: VertexRef
    BaseNormal: Vector3d
    BasePlane: FaceRef
    LevelSpacing: float
    LevelCount: int
    RowElevation: float
    RowSpacing: float
    RowCount: int
    Owner: AssocArray
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetLevelCount(self, expression: str, evaluatorId: str) -> int: ...
    def GetLevelSpacing(self, expression: str, evaluatorId: str) -> float: ...
    def GetRowCount(self, expression: str, evaluatorId: str) -> int: ...
    def GetRowElevation(self, expression: str, evaluatorId: str) -> float: ...
    def GetRowSpacing(self, expression: str, evaluatorId: str) -> float: ...
    def SetLevelCount(self, count: int, expression: str, evaluatorId: str) -> None: ...
    def SetLevelSpacing(self, spacing: float, expression: str, evaluatorId: str) -> None: ...
    def SetRowCount(self, count: int, expression: str, evaluatorId: str) -> None: ...
    def SetRowElevation(self, value: float, expression: str, evaluatorId: str) -> None: ...
    def SetRowSpacing(self, spacing: float, expression: str, evaluatorId: str) -> None: ...

class AssocArrayParameters(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocArrayParameters"""
    def __init__(self, *args) -> None: ...
    Owner: AssocArray
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Commit(self, ) -> None: ...

class AssocArrayPathParameters(AssocArrayCommonParameters):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocArrayPathParameters"""
    def __init__(self, *args) -> None: ...
    PathDirection: bool
    EndOffset: float
    StartOffset: float
    AlignItems: bool
    Path: EdgeRef
    ItemSpacing: float
    ItemCount: int
    Method: MethodType
    BasePoint: VertexRef
    BaseNormal: Vector3d
    BasePlane: FaceRef
    LevelSpacing: float
    LevelCount: int
    RowElevation: float
    RowSpacing: float
    RowCount: int
    Owner: AssocArray
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetEndOffset(self, expression: str, evaluatorId: str) -> float: ...
    def GetItemCount(self, expression: str, evaluatorId: str) -> int: ...
    def GetItemSpacing(self, expression: str, evaluatorId: str) -> float: ...
    def GetStartOffset(self, expression: str, evaluatorId: str) -> float: ...
    def SetEndOffset(self, offset: float, expression: str, evaluatorId: str) -> None: ...
    def SetItemCount(self, count: int, expression: str, evaluatorId: str) -> None: ...
    def SetItemSpacing(self, spacing: float, expression: str, evaluatorId: str) -> None: ...
    def SetStartOffset(self, offset: float, expression: str, evaluatorId: str) -> None: ...

class AssocArrayPolarParameters(AssocArrayCommonParameters):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocArrayPolarParameters"""
    def __init__(self, *args) -> None: ...
    RotateItems: bool
    Radius: float
    Direction: ArcDirection
    StartAngle: float
    FillAngle: float
    AngleBetweenItems: float
    ItemCount: int
    BasePoint: VertexRef
    BaseNormal: Vector3d
    BasePlane: FaceRef
    LevelSpacing: float
    LevelCount: int
    RowElevation: float
    RowSpacing: float
    RowCount: int
    Owner: AssocArray
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetAngleBetweenItems(self, expression: str, evaluatorId: str) -> float: ...
    def GetFillAngle(self, expression: str, evaluatorId: str) -> float: ...
    def GetItemCount(self, expression: str, evaluatorId: str) -> int: ...
    def GetRadius(self, expression: str, evaluatorId: str) -> float: ...
    def GetStartAngle(self, expression: str, evaluatorId: str) -> float: ...
    def SetAngleBetweenItems(self, val: float, expression: str, evaluatorId: str) -> None: ...
    def SetFillAngle(self, val: float, expression: str, evaluatorId: str) -> None: ...
    def SetItemCount(self, count: int, expression: str, evaluatorId: str) -> None: ...
    def SetRadius(self, val: float, expression: str, evaluatorId: str) -> None: ...
    def SetStartAngle(self, val: float, expression: str, evaluatorId: str) -> None: ...

class AssocArrayRectangularParameters(AssocArrayCommonParameters):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocArrayRectangularParameters"""
    def __init__(self, *args) -> None: ...
    YAxisDirection: Vector3d
    XAxisDirection: Vector3d
    AxesAngle: float
    ColumnSpacing: float
    ColumnCount: int
    BasePoint: VertexRef
    BaseNormal: Vector3d
    BasePlane: FaceRef
    LevelSpacing: float
    LevelCount: int
    RowElevation: float
    RowSpacing: float
    RowCount: int
    Owner: AssocArray
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetAxesAngle(self, expression: str, evaluatorId: str) -> float: ...
    def GetColumnCount(self, expression: str, evaluatorId: str) -> int: ...
    def GetColumnSpacing(self, expression: str, evaluatorId: str) -> float: ...
    def SetAxesAngle(self, val: float, expression: str, evaluatorId: str) -> None: ...
    def SetColumnCount(self, count: int, expression: str, evaluatorId: str) -> None: ...
    def SetColumnSpacing(self, spacing: float, expression: str, evaluatorId: str) -> None: ...

class AssocAsmBodyActionParam(AssocActionParam):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocAsmBodyActionParam"""
    def __init__(self, *args) -> None: ...
    DependentOnCompoundObject: CompoundObjectId
    Name: str
    ParentAction: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetBody(self, bodyId: ObjectId, isReadDep: bool, isWriteDep: bool) -> None: ...

class AssocBlendSurfaceActionBody(AssocPathBasedSurfaceActionBody):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocBlendSurfaceActionBody"""
    def __init__(self, *args) -> None: ...
    BlendOption: BlendOptions
    EndEdgeBulge: float
    StartEdgeBulge: float
    EndEdgeContinuity: int
    StartEdgeContinuity: int
    InputVertexParams: ObjectIdCollection
    InputPathParams: ObjectIdCollection
    IsSemiAssociative: bool
    ResultingSurface: ObjectId
    OwnedParams: ObjectIdCollection
    ParamCount: int
    OwningNetwork: ObjectId
    Status: AssocStatus
    ParentAction: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def CreateInstance(resultingSurfaceId: ObjectId, startProfile: LoftProfile, endProfile: LoftProfile, blendOptions: BlendOptions, enable: bool) -> ObjectId: ...
    def GetContinuityGripPoints(self, startEdgePt: Point3d, endEdgePt: Point3d) -> None: ...
    def GetEndEdgeBulge(self, expression: str, evaluatorId: str) -> float: ...
    def GetEndEdgeContinuity(self, expression: str, evaluatorId: str) -> int: ...
    def GetProfiles(self, startProfile: LoftProfile, endProfile: LoftProfile) -> None: ...
    def GetStartEdgeBulge(self, expression: str, evaluatorId: str) -> float: ...
    def GetStartEdgeContinuity(self, expression: str, evaluatorId: str) -> int: ...
    def SetEndEdgeBulge(self, value: float, expression: str, evaluatorId: str) -> None: ...
    def SetEndEdgeContinuity(self, value: int, expression: str, evaluatorId: str) -> None: ...
    def SetStartEdgeBulge(self, value: float, expression: str, evaluatorId: str) -> None: ...
    def SetStartEdgeContinuity(self, value: int, expression: str, evaluatorId: str) -> None: ...

class AssocCompoundActionParam(AssocActionParam):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocCompoundActionParam"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    OwnedParams: ObjectIdCollection
    ParamCount: int
    Name: str
    ParentAction: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddParam(self, paramId: ObjectId) -> int: ...
    def ParamAtIndex(self, index: int) -> ObjectId: ...
    def ParamAtName(self, paramName: str, index: int) -> ObjectId: ...
    def ParamsAtName(self, paramName: str) -> ObjectIdCollection: ...
    def RemoveAllParams(self, alsoEraseThem: bool) -> None: ...
    def RemoveParam(self, paramId: ObjectId, alsoEraseIt: bool) -> None: ...

class AssocConstraintType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.AssocConstraintType"""
    def __init__(self, *args) -> None: ...
    NoneAssocConstraintType: int  # = 0
    DistanceAssocConstraintType: int  # = 1
    HorizontalDistanceAssocConstraintType: int  # = 2
    VerticalDistanceAssocConstraintType: int  # = 3
    Angle0AssocConstraintType: int  # = 4
    Angle1AssocConstraintType: int  # = 5
    Angle2AssocConstraintType: int  # = 6
    Angle3AssocConstraintType: int  # = 7
    RadiusAssocConstraintType: int  # = 8
    DiameterAssocConstraintType: int  # = 9
class AssocDependency(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocDependency"""
    def __init__(self, *args) -> None: ...
    CurrentEvaluationCallback: AssocEvaluationCallback
    IsActionEvaluationInProgress: bool
    IsDependentOnObjectReadOnly: bool
    IsRelevantChange: bool
    HasCachedValue: bool
    IsDelegatingToOwningAction: bool
    DependentOnObjectStatus: ErrorStatus
    IsAttachedToObject: bool
    NextDependencyOnObject: ObjectId
    PrevDependencyOnObject: ObjectId
    IsDependentOnCompoundObject: bool
    DependentOnCompoundObject: CompoundObjectId
    DependentOnObject: ObjectId
    OwningAction: ObjectId
    Order: int
    IsObjectStateDependent: bool
    IsWriteDependency: bool
    IsReadDependency: bool
    Status: AssocStatus
    DependencyBody: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AttachToObject(self, compoundId: CompoundObjectId) -> None: ...
    def DetachFromObject(self, ) -> None: ...
    def Evaluate(self, ) -> None: ...
    @staticmethod
    def GetDependenciesOnObject(dbObj: DBObject, readDependenciesWanted: bool, writeDependenciesWanted: bool) -> ObjectIdCollection: ...
    @staticmethod
    def GetFirstDependencyOnObject(dbObj: DBObject) -> ObjectId: ...
    def IsDependentOnTheSameThingAs(self, otherDependency: AssocDependency) -> bool: ...
    def IsEqualTo(self, otherDependency: AssocDependency) -> bool: ...
    @staticmethod
    def NotifyDependenciesOnObject(dbObj: DBObject, newStatus: AssocStatus) -> None: ...
    def SetDependentOnObject(self, compoundId: CompoundObjectId) -> None: ...
    def SetStatus(self, newStatus: AssocStatus, notifyOwningNetwork: bool) -> None: ...
    def UpdateDependentOnObject(self, ) -> None: ...

class AssocDependencyBody(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocDependencyBody"""
    def __init__(self, *args) -> None: ...
    IsRelevantChangeOverride: bool
    HasCachedValueOverride: bool
    IsActionEvaluationInProgress: bool
    IsAttachedToObject: bool
    DependentOnObject: ObjectId
    OwningAction: ObjectId
    Status: AssocStatus
    ParentDependency: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def ClonedOverride(self, dbObj: DBObject, newObj: DBObject) -> None: ...
    def DwgInFields(self, filer: DwgFiler) -> ErrorStatus: ...
    def DwgOutFields(self, filer: DwgFiler) -> ErrorStatus: ...
    def DxfInFields(self, filer: DxfFiler) -> ErrorStatus: ...
    def DxfOutFields(self, filer: DxfFiler) -> ErrorStatus: ...
    def ErasedOverride(self, dbObj: DBObject, IsErasing: bool) -> None: ...
    def EvaluateOverride(self, ) -> None: ...
    def IsDependentOnTheSameThingAsOverride(self, otherDependency: AssocDependency) -> bool: ...
    def IsEqualToOverride(self, otherDependency: AssocDependency) -> bool: ...
    def ModifiedOverride(self, dbObj: DBObject) -> None: ...
    def SetStatus(self, newStatus: AssocStatus, notifyOwningAction: bool) -> None: ...
    def UpdateDependentOnObjectOverride(self, ) -> None: ...
    def currentEvaluationCallback(self, ) -> AssocEvaluationCallback: ...

class AssocDependencyPE(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocDependencyPE"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AllowsDependencies(self, dbObj: DBObject, isWriteDependency: bool) -> bool: ...

class AssocDimDependencyBody(AssocDimDependencyBodyBase):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocDimDependencyBody"""
    def __init__(self, *args) -> None: ...
    IsEntityAttachmentChangedOverride: bool
    EntityMeasurementOverride: float
    EntityTextOverride: str
    IsRelevantChangeOverride: bool
    GetCurrentlyUsedEntityNameFormat: int
    IsReferenceOnly: bool
    GetMeasuredValue: float
    IsConstraintActive: bool
    SubentityConstrainedGeoms: list
    ConstrainedGeoms: list
    Variable: ObjectId
    HasCachedValueOverride: bool
    IsActionEvaluationInProgress: bool
    IsAttachedToObject: bool
    DependentOnObject: ObjectId
    OwningAction: ObjectId
    Status: AssocStatus
    ParentDependency: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def CreateAndPostToDatabase(dimId: ObjectId, dimDepId: ObjectId, dimDepBodyId: ObjectId) -> None: ...
    def UpdateDependentOnObjectOverride(self, ) -> None: ...

class AssocDimDependencyBodyBase(AssocDependencyBody):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocDimDependencyBodyBase"""
    def __init__(self, *args) -> None: ...
    IsRelevantChangeOverride: bool
    GetCurrentlyUsedEntityNameFormat: int
    IsReferenceOnly: bool
    GetMeasuredValue: float
    IsConstraintActive: bool
    SubentityConstrainedGeoms: list
    ConstrainedGeoms: list
    Variable: ObjectId
    IsEntityAttachmentChangedOverride: bool
    EntityMeasurementOverride: float
    EntityTextOverride: str
    HasCachedValueOverride: bool
    IsActionEvaluationInProgress: bool
    IsAttachedToObject: bool
    DependentOnObject: ObjectId
    OwningAction: ObjectId
    Status: AssocStatus
    ParentDependency: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def ComposeEntityText(self, requiredNameFormat: int) -> str: ...
    def Constraint(self, ) -> ExplicitConstraint: ...
    def DeactivateConstraint(self, ) -> None: ...
    def DragStatus(self, status: DragStatus) -> None: ...
    def DwgInFields(self, filer: DwgFiler) -> ErrorStatus: ...
    def DwgOutFields(self, filer: DwgFiler) -> ErrorStatus: ...
    def DxfInFields(self, filer: DxfFiler) -> ErrorStatus: ...
    def DxfOutFields(self, filer: DxfFiler) -> ErrorStatus: ...
    def EntityAttachmentPointMoved(self, newAttachedGeometries: list, measurement: float) -> None: ...
    def ErasedOverride(self, dbObj: DBObject, isErasing: bool) -> None: ...
    def EvaluateOverride(self, ) -> None: ...
    @staticmethod
    def FormatToCurrentPrecision(expression: str, isAngular: bool) -> str: ...
    def GetEntityNameAndExpression(self, name: str, expression: str) -> None: ...
    @staticmethod
    def GetEraseDimensionIfDependencyIsErased() -> bool: ...
    @staticmethod
    def GetFromEntity(entityId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetNameAndExpressionFromEntityText(entityText: str, useMeasurementIfNoText: bool, measurement: float, isAngular: bool, name: str, expression: str) -> None: ...
    def GetSubentityGeoms(self, distanceDirection: Vector3d) -> list: ...
    def GetVariableNameAndExpression(self, name: str, expression: str, value: str) -> None: ...
    def ModifiedOverride(self, dbObj: DBObject) -> None: ...
    def ReactivateConstraint(self, ) -> None: ...
    def SetEntityNameAndExpression(self, name: str, expression: str, value: str) -> None: ...
    @staticmethod
    def SetEraseDimensionIfDependencyIsErased(yesNo: bool) -> bool: ...
    def SetNameAndExpression(self, name: str, expression: str) -> None: ...
    def SetVariableNameAndExpression(self, name: str, expression: str) -> None: ...
    def SetVariableValueToMeasuredValue(self, ) -> None: ...
    def SubErase(self, erasing: bool) -> None: ...
    def UpdateDependentOnObjectOverride(self, ) -> None: ...
    def ValidateEntityText(self, entityTextToValidate: str) -> str: ...

class AssocDraggingState:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.AssocDraggingState"""
    def __init__(self, *args) -> None: ...
    NotDraggingAssocDraggingState: int  # = 0
    FirstSampleAssocDraggingState: int  # = 1
    IntermediateSampleAssocDraggingState: int  # = 2
    LastSampleAssocDraggingState: int  # = 3
class AssocEdgeActionParam(AssocActionParam):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocEdgeActionParam"""
    def __init__(self, *args) -> None: ...
    DependentOnCompoundObject: CompoundObjectId
    Name: str
    ParentAction: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetEdgeRef(self, ) -> list: ...
    def SetEdgeRef(self, edgeRef: EdgeRef, isReadDep: bool, isWriteDep: bool) -> None: ...

class AssocEdgeChamferActionBody(AssocPathBasedSurfaceActionBody):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocEdgeChamferActionBody"""
    def __init__(self, *args) -> None: ...
    OtherDistance: float
    BaseDistance: float
    InputVertexParams: ObjectIdCollection
    InputPathParams: ObjectIdCollection
    IsSemiAssociative: bool
    ResultingSurface: ObjectId
    OwnedParams: ObjectIdCollection
    ParamCount: int
    OwningNetwork: ObjectId
    Status: AssocStatus
    ParentAction: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def CreateInstance(chamferEdges: list, baseFace: SubentityId, baseDistance: float, otherDistance: float, enable: bool) -> ObjectId: ...
    def GetBaseDistance(self, expression: str, evaluatorId: str) -> float: ...
    def GetOtherDistance(self, expression: str, evaluatorId: str) -> float: ...
    def SetBaseDistance(self, distance: float, expression: str, evaluatorId: str) -> None: ...
    def SetOtherDistance(self, distance: float, expression: str, evaluatorId: str) -> None: ...

class AssocEdgeFilletActionBody(AssocSurfaceActionBody):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocEdgeFilletActionBody"""
    def __init__(self, *args) -> None: ...
    Radius: float
    IsSemiAssociative: bool
    ResultingSurface: ObjectId
    OwnedParams: ObjectIdCollection
    ParamCount: int
    OwningNetwork: ObjectId
    Status: AssocStatus
    ParentAction: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def CreateInstance(filletEdges: list, radius: float, enable: bool) -> ObjectId: ...
    def GetRadius(self, expression: str, evaluatorId: str) -> float: ...
    def SetRadius(self, radius: float, expression: str, evaluatorId: str) -> None: ...

class AssocEvaluationCallback:
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocEvaluationCallback"""
    def __init__(self, *args) -> None: ...
    def BeginActionEvaluation(self, action: AssocAction) -> None: ...
    def BeginActionEvaluationUsingObject(self, pAction: AssocAction, objectId: ObjectId, objectIsGoingToBeUsed: bool, objectIsGoingToBeModified: bool, substituteObject: DBObject) -> None: ...
    def CancelActionEvaluation(self, ) -> bool: ...
    def Dispose(self, ) -> None: ...
    def DraggingState(self, ) -> AssocDraggingState: ...
    def EndActionEvaluation(self, action: AssocAction) -> None: ...
    def EndActionEvaluationUsingObject(self, action: AssocAction, objectId: ObjectId, obj: DBObject) -> None: ...
    def EvaluationMode(self, ) -> AssocEvaluationMode: ...
    def GetTransformationType(self, ) -> AssocTransformationType: ...
    def SetActionEvaluationErrorStatus(self, action: AssocAction, errorStatus: ErrorStatus, objectId: ObjectId, obj: DBObject, errorInfo: IntPtr) -> None: ...

class AssocEvaluationMode:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.AssocEvaluationMode"""
    def __init__(self, *args) -> None: ...
    ModifyObjectsAssocEvaluationMode: int  # = 0
    ModifyActionAssocEvaluationMode: int  # = 1
class AssocEvaluationPriority:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.AssocEvaluationPriority"""
    def __init__(self, *args) -> None: ...
    CannotDermineAssocEvaluationPriority: int  # = 0
    CanBeEvaluatedAssocEvaluationPriority: int  # = 1000
    CannotBeEvaluatedAssocEvaluationPriority: int  # = -1000
class AssocExtendSurfaceActionBody(AssocPathBasedSurfaceActionBody):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocExtendSurfaceActionBody"""
    def __init__(self, *args) -> None: ...
    Distance: float
    InputVertexParams: ObjectIdCollection
    InputPathParams: ObjectIdCollection
    IsSemiAssociative: bool
    ResultingSurface: ObjectId
    OwnedParams: ObjectIdCollection
    ParamCount: int
    OwningNetwork: ObjectId
    Status: AssocStatus
    ParentAction: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def CreateInstance(resultingSurfaceId: ObjectId, extendEdges: list, distance: float, extendOption: EdgeExtensionType, enabled: bool) -> ObjectId: ...
    def GetDistance(self, expression: str, evaluatorId: str) -> float: ...
    def SetDistance(self, distance: float, expression: str, evaluatorId: str) -> None: ...

class AssocExtrudedSurfaceActionBody(AssocPathBasedSurfaceActionBody):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocExtrudedSurfaceActionBody"""
    def __init__(self, *args) -> None: ...
    Height: float
    TaperAngle: float
    InputVertexParams: ObjectIdCollection
    InputPathParams: ObjectIdCollection
    IsSemiAssociative: bool
    ResultingSurface: ObjectId
    OwnedParams: ObjectIdCollection
    ParamCount: int
    OwningNetwork: ObjectId
    Status: AssocStatus
    ParentAction: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def CreateInstance(resultingSurfaceId: ObjectId, inputPath: PathRef, directionVec: Vector3d, sweepOptions: SweepOptions, enable: bool) -> ObjectId: ...
    def GetHeight(self, expression: str, evaluatorId: str) -> float: ...
    def GetTaperAngle(self, expression: str, evaluatorId: str) -> float: ...
    def SetHeight(self, height: float, expression: str, evaluatorId: str) -> None: ...
    def SetTaperAngle(self, taperAngle: float, expression: str, evaluatorId: str) -> None: ...

class AssocFaceActionParam(AssocActionParam):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocFaceActionParam"""
    def __init__(self, *args) -> None: ...
    DependentOnCompoundObject: CompoundObjectId
    Name: str
    ParentAction: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetFaceRef(self, ) -> list: ...
    def SetFaceRef(self, faceRef: FaceRef, isReadDependency: bool, isWriteDependency: bool) -> None: ...

class AssocFilletSurfaceActionBody(AssocSurfaceActionBody):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocFilletSurfaceActionBody"""
    def __init__(self, *args) -> None: ...
    TrimMode: FilletTrimMode
    Radius: float
    IsSemiAssociative: bool
    ResultingSurface: ObjectId
    OwnedParams: ObjectIdCollection
    ParamCount: int
    OwningNetwork: ObjectId
    Status: AssocStatus
    ParentAction: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def CreateInstance(resultingSurfaceId: ObjectId, inputSurfaceId1: ObjectId, pickPt1: Point3d, inputSurfaceId2: ObjectId, pickPt2: Point3d, radius: float, trimMode: FilletTrimMode, viewDir: Vector3d, bEnable: bool) -> ObjectId: ...
    def GetFilletHandleData(self, pt: Point3d, dir: Vector3d, cenPt: Point3d, normal: Vector3d) -> None: ...
    def GetHintPoints(self, ) -> list: ...
    def GetRadius(self, expression: str, evaluatorId: str) -> float: ...
    def SetHintPoints(self, hintPoints: list, viewDir: Vector3d) -> None: ...
    def SetRadius(self, radius: float, expression: str, evaluatorId: str) -> None: ...

class AssocGeomDependency(AssocDependency):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocGeomDependency"""
    def __init__(self, *args) -> None: ...
    FaceSubentityGeometry: list
    EdgeSubentityGeometry: list
    VertexSubentityGeometry: list
    IsCachingSubentityGeometry: bool
    TransientSubentCount: int
    SubentityType: int
    Subentity: SubentityId
    TransientSubentIds: list
    PersistentSubentId: AssocPersSubentityId
    CurrentEvaluationCallback: AssocEvaluationCallback
    IsActionEvaluationInProgress: bool
    IsDependentOnObjectReadOnly: bool
    IsRelevantChange: bool
    HasCachedValue: bool
    IsDelegatingToOwningAction: bool
    DependentOnObjectStatus: ErrorStatus
    IsAttachedToObject: bool
    NextDependencyOnObject: ObjectId
    PrevDependencyOnObject: ObjectId
    IsDependentOnCompoundObject: bool
    DependentOnCompoundObject: CompoundObjectId
    DependentOnObject: ObjectId
    OwningAction: ObjectId
    Order: int
    IsObjectStateDependent: bool
    IsWriteDependency: bool
    IsReadDependency: bool
    Status: AssocStatus
    DependencyBody: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def DependentOnObjectMirrored(self, ) -> None: ...
    @staticmethod
    def RedirectToAnotherSubentity(oldObjectId: ObjectId, oldSubentId: SubentityId, newObjectId: ObjectId, newSubentId: SubentityId) -> None: ...

class AssocGlobalUtility:
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocGlobalUtility"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def EvaluationRequestSeverityLevel(status: AssocStatus) -> int: ...
    @staticmethod
    def IsDraggingProvidingSubstituteObjects(evaluationCallback: AssocEvaluationCallback) -> bool: ...
    @staticmethod
    def IsEvaluationRequest(status: AssocStatus) -> bool: ...
    @staticmethod
    def IsToBeSkipped(status: AssocStatus) -> bool: ...

class AssocLoftedSurfaceActionBody(AssocPathBasedSurfaceActionBody):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocLoftedSurfaceActionBody"""
    def __init__(self, *args) -> None: ...
    InputVertexParams: ObjectIdCollection
    InputPathParams: ObjectIdCollection
    IsSemiAssociative: bool
    ResultingSurface: ObjectId
    OwnedParams: ObjectIdCollection
    ParamCount: int
    OwningNetwork: ObjectId
    Status: AssocStatus
    ParentAction: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def CreateInstance(resultingSurfaceId: ObjectId, crossSections: list, guideCurves: list, pathCurve: PathRef, loftOptions: LoftOptions, continuityArray: list, bulgeArray: list, bEnable: bool) -> ObjectId: ...
    def GetBulge(self, type: ProfileType, expression: str, evaluatorId: str) -> float: ...
    def GetContinuity(self, type: ProfileType, expression: str, evaluatorId: str) -> int: ...
    def SetBulge(self, type: ProfileType, value: float, expression: str, evaluatorId: str) -> None: ...
    def SetContinuity(self, type: ProfileType, value: int, expression: str, evaluatorId: str) -> None: ...

class AssocManager(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocManager"""
    def __init__(self, *args) -> None: ...
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def AddGlobalEvaluationCallback(callback: AssocEvaluationCallback, order: int) -> None: ...
    @staticmethod
    def AuditAssociativeData(database: Database, traverseWholeDatabase: bool) -> None: ...
    @staticmethod
    def EvaluateTopLevelNetwork(database: Database, callback: AssocEvaluationCallback, callbackOrder: int) -> bool: ...
    @staticmethod
    def GetGlobalEvaluationCallbacks(callbacks: ArrayList, orders: ArrayList) -> None: ...
    @staticmethod
    def GlobalEvaluationMultiCallback() -> AssocEvaluationCallback: ...
    @staticmethod
    def HasAssocNetwork(database: Database) -> bool: ...
    @staticmethod
    def Initialize() -> None: ...
    @staticmethod
    def RemoveGlobalEvaluationCallback(callback: AssocEvaluationCallback) -> None: ...

class AssocNetwork(AssocAction):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocNetwork"""
    def __init__(self, *args) -> None: ...
    GetActions: ObjectIdCollection
    CurrentEvaluationCallback: AssocEvaluationCallback
    IsActionEvaluationInProgress: bool
    OwningNetwork: ObjectId
    Status: AssocStatus
    IsActionBodyAProxy: bool
    ActionBody: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddAction(self, actionId: ObjectId, alsoSetAsDatabaseOwner: bool) -> None: ...
    def AddActions(self, actionIds: ObjectIdCollection, alsoSetAsDatabaseOwner: bool) -> None: ...
    @staticmethod
    def GetInstanceFromDatabase(database: Database, createIfDoesNotExist: bool, dictionaryKey: str) -> ObjectId: ...
    @staticmethod
    def GetInstanceFromObject(owningObjectId: ObjectId, createIfDoesNotExist: bool, addToTopLevelNetwork: bool, dictionaryKey: str) -> ObjectId: ...
    def OwnedActionStatusChanged(self, ownedAction: AssocAction, previousStatus: AssocStatus) -> None: ...
    def RemoveAction(self, actionId: ObjectId, alsoEraseIt: bool) -> None: ...
    def RemoveAllActions(self, alsoEraseThem: bool) -> None: ...
    @staticmethod
    def RemoveInstanceFromDatabase(database: Database, alsoEraseIt: bool, dictionaryKey: str) -> None: ...
    @staticmethod
    def RemoveInstanceFromObject(owningObjectId: ObjectId, alsoEraseIt: bool, dictionaryKey: str) -> None: ...

class AssocNetworkSurfaceActionBody(AssocPathBasedSurfaceActionBody):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocNetworkSurfaceActionBody"""
    def __init__(self, *args) -> None: ...
    InputVertexParams: ObjectIdCollection
    InputPathParams: ObjectIdCollection
    IsSemiAssociative: bool
    ResultingSurface: ObjectId
    OwnedParams: ObjectIdCollection
    ParamCount: int
    OwningNetwork: ObjectId
    Status: AssocStatus
    ParentAction: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def CreateInstance(resultingSurfaceId: ObjectId, crossSections: list, guideCurves: list, continuityArray: list, bulgeArray: list, bEnable: bool) -> ObjectId: ...
    def GetBulge(self, type: ProfileType, expression: str, evaluatorId: str) -> float: ...
    def GetContinuity(self, type: ProfileType, expression: str, evaluatorId: str) -> int: ...
    def SetBulge(self, type: ProfileType, value: float, expression: str, evaluatorId: str) -> None: ...
    def SetContinuity(self, type: ProfileType, value: int, expression: str, evaluatorId: str) -> None: ...

class AssocObjectTransaction:
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocObjectTransaction"""
    def __init__(self, *args) -> None: ...
    def Dispose(self, ) -> None: ...
    def GetDBObject(self, objectId: ObjectId, openMode: OpenMode, openErased: bool, openOnLockedLayer: bool) -> DBObject: ...
    def IsSubstituteObject(self, dbObject: DBObject) -> bool: ...

class AssocOffsetSurfaceActionBody(AssocSurfaceActionBody):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocOffsetSurfaceActionBody"""
    def __init__(self, *args) -> None: ...
    Distance: float
    IsSemiAssociative: bool
    ResultingSurface: ObjectId
    OwnedParams: ObjectIdCollection
    ParamCount: int
    OwningNetwork: ObjectId
    Status: AssocStatus
    ParentAction: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def CreateInstance(resultingSurfaceId: ObjectId, inputSurfaceId: ObjectId, distance: float, bEnable: bool) -> ObjectId: ...
    def GetDistance(self, expression: str, evaluatorId: str) -> float: ...
    def SetDistance(self, distance: float, expression: str, evaluatorId: str) -> None: ...

class AssocParamBasedActionBody(AssocActionBody):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocParamBasedActionBody"""
    def __init__(self, *args) -> None: ...
    OwnedParams: ObjectIdCollection
    ParamCount: int
    OwningNetwork: ObjectId
    Status: AssocStatus
    ParentAction: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AssocPatchSurfaceActionBody(AssocPathBasedSurfaceActionBody):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocPatchSurfaceActionBody"""
    def __init__(self, *args) -> None: ...
    ContinuityGripPoint: Point3d
    Bulge: float
    Continuity: int
    InputVertexParams: ObjectIdCollection
    InputPathParams: ObjectIdCollection
    IsSemiAssociative: bool
    ResultingSurface: ObjectId
    OwnedParams: ObjectIdCollection
    ParamCount: int
    OwningNetwork: ObjectId
    Status: AssocStatus
    ParentAction: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def CreateInstance(patchSurfaceId: ObjectId, edgeCurves: list, constraintCurves: list, constraintPoints: list, nContinuity: int, dBulge: float, bEnabled: bool) -> ObjectId: ...
    def GetBulge(self, expression: str, evaluatorId: str) -> float: ...
    def GetContinuity(self, expression: str, evaluatorId: str) -> int: ...
    def SetBulge(self, value: float, expression: str, evaluatorId: str) -> None: ...
    def SetConstraintCurves(self, constraintCurves: list) -> None: ...
    def SetConstraintPoints(self, constraintPoints: list) -> None: ...
    def SetContinuity(self, value: int, expression: str, evaluatorId: str) -> None: ...

class AssocPathActionParam(AssocCompoundActionParam):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocPathActionParam"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    OwnedParams: ObjectIdCollection
    ParamCount: int
    Name: str
    ParentAction: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetEdgeRefArray(self, ) -> list: ...
    def SetEdgeRefArray(self, edgeRef: list) -> None: ...
    def UpdateEdgeRef(self, index: int, edge: EdgeRef) -> None: ...

class AssocPathBasedSurfaceActionBody(AssocSurfaceActionBody):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocPathBasedSurfaceActionBody"""
    def __init__(self, *args) -> None: ...
    InputVertexParams: ObjectIdCollection
    InputPathParams: ObjectIdCollection
    IsSemiAssociative: bool
    ResultingSurface: ObjectId
    OwnedParams: ObjectIdCollection
    ParamCount: int
    OwningNetwork: ObjectId
    Status: AssocStatus
    ParentAction: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetInputPaths(self, paths: list) -> None: ...
    def GetInputPoints(self, ) -> list: ...
    def MakeInputPathsDrawOnTopOfResultingSurface(self, ) -> None: ...
    def RemoveAllPathParams(self, ) -> None: ...
    def RemoveAllVertexParams(self, ) -> None: ...
    def SetInputPaths(self, paths: list) -> None: ...
    def SetInputPoints(self, points: list) -> None: ...
    def UpdateInputPath(self, index: int, pathRef: PathRef) -> None: ...

class AssocPersSubentityId(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocPersSubentityId"""
    def __init__(self, *args) -> None: ...
    IsNull: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Audit(self, auditInfo: AuditInfo) -> None: ...
    @staticmethod
    def CreateObjectAndDwgInFields(database: Database, filer: DwgFiler, createdPersSubentId: AssocPersSubentityId) -> None: ...
    @staticmethod
    def CreateObjectAndDxfInFields(filer: DxfFiler, createdPersSubentId: AssocPersSubentityId) -> None: ...
    def DwgInFields(self, filer: DwgFiler) -> None: ...
    def DwgOutFields(self, filer: DwgFiler) -> None: ...
    def DxfInFields(self, filer: DxfFiler) -> None: ...
    def DxfOutFields(self, filer: DxfFiler) -> None: ...
    def GetTransientSubentIds(self, entity: Entity) -> list: ...
    def IsEqualTo(self, entity: Entity, other: AssocPersSubentityId) -> bool: ...
    def Mirror(self, mirroredEntity: Entity) -> None: ...
    def SubentType(self, entity: Entity) -> SubentityType: ...
    def TransientSubentCount(self, entity: Entity) -> int: ...

class AssocPersSubentityIdPE(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocPersSubentityIdPE"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CreateNewPersSubent(self, entity: Entity, compId: CompoundObjectId, subentId: SubentityId) -> AssocPersSubentityId: ...
    def GetAllSubentities(self, entity: Entity, subentType: SubentityType) -> list: ...
    def GetEdgeSubentityGeometry(self, entity: Entity, edgeSubentId: SubentityId) -> Curve3d: ...
    def GetEdgeVertexSubentities(self, entity: Entity, edgeSubentId: SubentityId, startVertexSubentId: SubentityId, endVertexSubentId: SubentityId, otherVertexSubentIds: list) -> None: ...
    def GetFaceSubentityGeometry(self, entity: Entity, faceSubentId: SubentityId) -> Surface: ...
    def GetRigidSetState(self, entity: Entity) -> int: ...
    def GetRigidSetTransform(self, entity: Entity) -> Matrix3d: ...
    def GetSplineEdgeVertexSubentities(self, entity: Entity, edgeSubentId: SubentityId, startVertexSubentId: SubentityId, endVertexSubentId: SubentityId, controlPointSubentIds: list, fitPointSubentIds: list) -> None: ...
    def GetSubentGeometryXform(self, entity: Entity, fullSubentPath: list) -> Matrix3d: ...
    def GetTransientSubentityIds(self, entity: Entity, perSubentId: AssocPersSubentityId) -> list: ...
    def GetVertexSubentityGeometry(self, entity: Entity, vertexSubentId: SubentityId) -> Point3d: ...
    def MirrorPersSubent(self, mirroredEntity: Entity, persSubentIdToMirror: AssocPersSubentityId) -> None: ...
    def SetEdgeSubentityGeometry(self, entity: Entity, edgeSubentId: SubentityId, newEdgeCurve: Curve3d) -> None: ...
    def SetFaceSubentityGeometry(self, entity: Entity, faceSubentId: SubentityId, newFaceSurface: Surface) -> None: ...
    def SetRigidSetTransform(self, entity: Entity, trans: Matrix3d) -> None: ...
    def SetVertexSubentityGeometry(self, entity: Entity, vertexSubentId: SubentityId, newVertexPosition: Point3d) -> None: ...

class AssocPlaneSurfaceActionBody(AssocPathBasedSurfaceActionBody):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocPlaneSurfaceActionBody"""
    def __init__(self, *args) -> None: ...
    InputVertexParams: ObjectIdCollection
    InputPathParams: ObjectIdCollection
    IsSemiAssociative: bool
    ResultingSurface: ObjectId
    OwnedParams: ObjectIdCollection
    ParamCount: int
    OwningNetwork: ObjectId
    Status: AssocStatus
    ParentAction: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def CreateInstance(resultingSurfaceId: ObjectId, inputPath: PathRef, enable: bool) -> ObjectId: ...

class AssocRevolvedSurfaceActionBody(AssocPathBasedSurfaceActionBody):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocRevolvedSurfaceActionBody"""
    def __init__(self, *args) -> None: ...
    RevolveAngle: float
    InputVertexParams: ObjectIdCollection
    InputPathParams: ObjectIdCollection
    IsSemiAssociative: bool
    ResultingSurface: ObjectId
    OwnedParams: ObjectIdCollection
    ParamCount: int
    OwningNetwork: ObjectId
    Status: AssocStatus
    ParentAction: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def CreateInstance(resultingSurfaceId: ObjectId, revolvePath: PathRef, axisPath: PathRef, angle: float, startAngle: float, revolveOptions: RevolveOptions, flipAxisDirection: bool, enable: bool) -> ObjectId: ...
    def GetRevolveAngle(self, expression: str, evaluatorId: str) -> float: ...
    def SetRevolveAngle(self, value: float, expression: str, evaluatorId: str) -> None: ...

class AssocSimplePersSubentId(AssocPersSubentityId):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocSimplePersSubentId"""
    def __init__(self, *args) -> None: ...
    IsNull: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Audit(self, auditInfo: AuditInfo) -> None: ...
    def DwgInFields(self, filer: DwgFiler) -> None: ...
    def DwgOutFields(self, filer: DwgFiler) -> None: ...
    def DxfInFields(self, filer: DxfFiler) -> None: ...
    def DxfOutFields(self, filer: DxfFiler) -> None: ...
    def IsEqualTo(self, entity: Entity, other: AssocPersSubentityId) -> bool: ...
    def SubentId(self, entity: Entity) -> SubentityId: ...
    def SubentType(self, entity: Entity) -> SubentityType: ...
    def TransientSubentCount(self, entity: Entity) -> int: ...

class AssocSingleEdgePersSubentId(AssocPersSubentityId):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocSingleEdgePersSubentId"""
    def __init__(self, *args) -> None: ...
    IsNull: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def IsEqualTo(self, entity: Entity, other: AssocPersSubentityId) -> bool: ...
    def SubentType(self, entity: Entity) -> SubentityType: ...
    def TransientSubentCount(self, entity: Entity) -> int: ...

class AssocStatus:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.AssocStatus"""
    def __init__(self, *args) -> None: ...
    IsUpToDateAssocStatus: int  # = 0
    ChangedDirectlyAssocStatus: int  # = 1
    ChangedTransitivelyAssocStatus: int  # = 2
    ChangedNoDifferenceAssocStatus: int  # = 3
    FailedToEvaluateAssocStatus: int  # = 4
    ErasedAssocStatus: int  # = 5
    SuppressedAssocStatus: int  # = 6
class AssocSurfaceActionBody(AssocParamBasedActionBody):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocSurfaceActionBody"""
    def __init__(self, *args) -> None: ...
    IsSemiAssociative: bool
    ResultingSurface: ObjectId
    OwnedParams: ObjectIdCollection
    ParamCount: int
    OwningNetwork: ObjectId
    Status: AssocStatus
    ParentAction: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def EvaluateOverride(self, ) -> None: ...
    @staticmethod
    def FindActionsThatAffectedTopologicalSubentity(entity: Entity, subEntityId: SubentityId) -> ObjectIdCollection: ...
    def ResultingSurfaceDep(self, createIfDoesNotExist: bool, isWriteOnlyDependency: bool) -> ObjectId: ...
    def SetResultingSurface(self, surfaceId: ObjectId, isWriteOnlyDependency: bool) -> None: ...

class AssocSweptSurfaceActionBody(AssocPathBasedSurfaceActionBody):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocSweptSurfaceActionBody"""
    def __init__(self, *args) -> None: ...
    TwistAngle: float
    AlignAngle: float
    ScaleFactor: float
    InputVertexParams: ObjectIdCollection
    InputPathParams: ObjectIdCollection
    IsSemiAssociative: bool
    ResultingSurface: ObjectId
    OwnedParams: ObjectIdCollection
    ParamCount: int
    OwningNetwork: ObjectId
    Status: AssocStatus
    ParentAction: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def CreateInstance(resultingSurfaceId: ObjectId, sweptPath: PathRef, path: PathRef, sweptOptions: SweepOptions, enable: bool) -> ObjectId: ...
    def GetAlignAngle(self, expression: str, evaluatorId: str) -> float: ...
    def GetScaleFactor(self, expression: str, evaluatorId: str) -> float: ...
    def GetTwistAngle(self, expression: str, evaluatorId: str) -> float: ...
    def SetAlignAngle(self, value: float, expression: str, evaluatorId: str) -> None: ...
    def SetScaleFactor(self, value: float, expression: str, evaluatorId: str) -> None: ...
    def SetTwistAngle(self, value: float, expression: str, evaluatorId: str) -> None: ...

class AssocTransformationType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.AssocTransformationType"""
    def __init__(self, *args) -> None: ...
    NotSpecified: int  # = 0
    Stretch: int  # = 1
    Rotate: int  # = 2
    Move: int  # = 3
class AssocTrimSurfaceActionBody(AssocPathBasedSurfaceActionBody):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocTrimSurfaceActionBody"""
    def __init__(self, *args) -> None: ...
    TrimmedArea: float
    InputVertexParams: ObjectIdCollection
    InputPathParams: ObjectIdCollection
    IsSemiAssociative: bool
    ResultingSurface: ObjectId
    OwnedParams: ObjectIdCollection
    ParamCount: int
    OwningNetwork: ObjectId
    Status: AssocStatus
    ParentAction: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def CreateInstance(resultingSurfaceId: ObjectId, trimInfo: list, autoExtend: bool, enable: bool) -> ObjectIdCollection: ...
    def MakeTrimPermanent(self, ) -> None: ...
    def SetTrimInfo(self, trimInfoArray: list, autoExtend: bool) -> None: ...
    def Untrim(self, ) -> None: ...

class AssocValueDependency(AssocDependency):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocValueDependency"""
    def __init__(self, *args) -> None: ...
    DependentOnObjectValue: ResultBuffer
    ValueName: str
    CurrentEvaluationCallback: AssocEvaluationCallback
    IsActionEvaluationInProgress: bool
    IsDependentOnObjectReadOnly: bool
    IsRelevantChange: bool
    HasCachedValue: bool
    IsDelegatingToOwningAction: bool
    DependentOnObjectStatus: ErrorStatus
    IsAttachedToObject: bool
    NextDependencyOnObject: ObjectId
    PrevDependencyOnObject: ObjectId
    IsDependentOnCompoundObject: bool
    DependentOnCompoundObject: CompoundObjectId
    DependentOnObject: ObjectId
    OwningAction: ObjectId
    Order: int
    IsObjectStateDependent: bool
    IsWriteDependency: bool
    IsReadDependency: bool
    Status: AssocStatus
    DependencyBody: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AssocValueProviderPE(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocValueProviderPE"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CanGetValue(self, dbObj: DBObject, valueName: str) -> bool: ...
    def CanSetValue(self, dbObj: DBObject, valueName: str) -> bool: ...
    def GetValue(self, dbObj: DBObject, valueName: str) -> ResultBuffer: ...
    def SetValue(self, dbObj: DBObject, valueName: str, newValue: ResultBuffer) -> None: ...

class AssocVariable(AssocAction):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocVariable"""
    def __init__(self, *args) -> None: ...
    EvaluatorId: str
    Description: str
    Value: ResultBuffer
    Expression: str
    Name: str
    CurrentEvaluationCallback: AssocEvaluationCallback
    IsActionEvaluationInProgress: bool
    OwningNetwork: ObjectId
    Status: AssocStatus
    IsActionBodyAProxy: bool
    ActionBody: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def AddGlobalCallback(callback: AssocVariableCallback) -> None: ...
    def EvaluateExpression(self, objectIds: ObjectIdCollection, objectValues: list, evaluatedExpressionValue: ResultBuffer) -> str: ...
    def FindObjectByName(self, objectName: str, pObjectClass: RXClass) -> ObjectId: ...
    @staticmethod
    def RemoveGlobalCallback(callback: AssocVariableCallback) -> None: ...
    def SetExpression(self, newExpression: str, evaluatorId: str, checkForCyclicalDependencies: bool, updateDependenciesOnReferencedSymbols: bool, errorMessage: str, silentMode: bool) -> None: ...
    def SetName(self, newName: str, updateReferencingExpressions: bool) -> None: ...
    def ValidateNameAndExpression(self, nameToValidate: str, expressionToValidate: str, errorMessage: str) -> None: ...
    @staticmethod
    def globalCallback() -> AssocVariableCallback: ...

class AssocVariableCallback:
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocVariableCallback"""
    def __init__(self, *args) -> None: ...
    def CanBeErased(self, variable: AssocVariable) -> bool: ...
    def Dispose(self, ) -> None: ...
    def ValidateNameAndExpression(self, variable: AssocVariable, nameToValidate: str, expressionToValidate: str) -> str: ...

class AssocVertexActionParam(AssocActionParam):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AssocVertexActionParam"""
    def __init__(self, *args) -> None: ...
    DependentOnCompoundObject: CompoundObjectId
    Name: str
    ParentAction: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetVertexRef(self, ) -> VertexRef: ...
    def SetVertexRef(self, pointRef: VertexRef, isReadDep: bool, isWriteDep: bool) -> None: ...

class AttachmentPoint:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.AttachmentPoint"""
    def __init__(self, *args) -> None: ...
    TopLeft: int  # = 1
    TopCenter: int  # = 2
    TopRight: int  # = 3
    MiddleLeft: int  # = 4
    MiddleCenter: int  # = 5
    MiddleRight: int  # = 6
    BottomLeft: int  # = 7
    BottomCenter: int  # = 8
    BottomRight: int  # = 9
    BaseLeft: int  # = 10
    BaseCenter: int  # = 11
    BaseRight: int  # = 12
    BaseAlign: int  # = 13
    BottomAlign: int  # = 14
    MiddleAlign: int  # = 15
    TopAlign: int  # = 16
    BaseFit: int  # = 17
    BottomFit: int  # = 18
    MiddleFit: int  # = 19
    TopFit: int  # = 20
    BaseMid: int  # = 21
    BottomMid: int  # = 22
    MiddleMid: int  # = 23
    TopMid: int  # = 24
class AttributeCollection:
    """.NET: Autodesk.AutoCAD.DatabaseServices.AttributeCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Count: int
    def AppendAttribute(self, attributeToAddToBlockReference: AttributeReference) -> ObjectId: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...

class AttributeDefinition(DBText):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AttributeDefinition"""
    def __init__(self, *args) -> None: ...
    MTextAttributeDefinition: MText
    IsMTextAttributeDefinition: bool
    LockPositionInBlock: bool
    FieldLength: int
    Preset: bool
    Verifiable: bool
    Constant: bool
    Invisible: bool
    Tag: str
    Prompt: str
    Justify: AttachmentPoint
    VerticalMode: TextVerticalMode
    HorizontalMode: TextHorizontalMode
    IsMirroredInY: bool
    IsMirroredInX: bool
    TextStyleId: ObjectId
    TextStyleName: str
    TextString: str
    WidthFactor: float
    Height: float
    Rotation: float
    Oblique: float
    Thickness: float
    Normal: Vector3d
    IsDefaultAlignment: bool
    AlignmentPoint: Point3d
    Position: Point3d
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def UpdateMTextAttributeDefinition(self, ) -> None: ...

class AttributeReference(DBText):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AttributeReference"""
    def __init__(self, *args) -> None: ...
    MTextAttribute: MText
    IsMTextAttribute: bool
    LockPositionInBlock: bool
    FieldLength: int
    IsPreset: bool
    IsVerifiable: bool
    IsConstant: bool
    Invisible: bool
    Tag: str
    Justify: AttachmentPoint
    VerticalMode: TextVerticalMode
    HorizontalMode: TextHorizontalMode
    IsMirroredInY: bool
    IsMirroredInX: bool
    TextStyleId: ObjectId
    TextStyleName: str
    TextString: str
    WidthFactor: float
    Height: float
    Rotation: float
    Oblique: float
    Thickness: float
    Normal: Vector3d
    IsDefaultAlignment: bool
    AlignmentPoint: Point3d
    Position: Point3d
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetAttributeFromBlock(self, definition: AttributeDefinition, blockTransform: Matrix3d) -> None: ...
    def UpdateMTextAttribute(self, ) -> None: ...

class AuditInfo(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.AuditInfo"""
    def __init__(self, *args) -> None: ...
    NumEntities: int
    AuditPass: AuditPass
    NumFixes: int
    NumErrors: int
    FixErrors: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def ErrorsFixed(self, count: int) -> None: ...
    def ErrorsFound(self, count: int) -> None: ...
    def IncNumEntities(self, ) -> None: ...
    def PrintError(self, value: DBObject, value2: str, validation: str, defaultValue: str) -> None: ...
    def PrintNumEntities(self, msg: str) -> None: ...
    def RequestRegen(self, ) -> None: ...
    def ResetNumEntities(self, ) -> None: ...

class AuditPass:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.AuditPass"""
    def __init__(self, *args) -> None: ...
    Pass1: int  # = 1
    Pass2: int  # = 2
class AutoConstrainEvaluationCallback:
    """.NET: Autodesk.AutoCAD.DatabaseServices.AutoConstrainEvaluationCallback"""
    def __init__(self, *args) -> None: ...
    IsEvaluationCancelled: bool
    def Dispose(self, ) -> None: ...
    def GetAutoConstrainPriority(self, ) -> list: ...
    def GetConstraintPriorityOverride(self, type: ConstraintType, geometries: list) -> int: ...
    def GetTotalConstraints(self, constraints: list) -> int: ...

class Background(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Background"""
    def __init__(self, *args) -> None: ...
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetBackgroundDictionaryId(database: Database, createIfNotPresent: bool) -> ObjectId: ...

class BeginInsertEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.BeginInsertEventArgs"""
    def __init__(self, *args) -> None: ...
    From: Database

class BeginInsertEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.BeginInsertEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: BeginInsertEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: BeginInsertEventArgs) -> None: ...

class BeginWblockBlockEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.BeginWblockBlockEventArgs"""
    def __init__(self, *args) -> None: ...
    BlockId: ObjectId
    From: Database

class BeginWblockBlockEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.BeginWblockBlockEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: BeginWblockBlockEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: BeginWblockBlockEventArgs) -> None: ...

class BeginWblockEntireDatabaseEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.BeginWblockEntireDatabaseEventArgs"""
    def __init__(self, *args) -> None: ...
    From: Database

class BeginWblockEntireDatabaseEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.BeginWblockEntireDatabaseEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: BeginWblockEntireDatabaseEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: BeginWblockEntireDatabaseEventArgs) -> None: ...

class BeginWblockObjectsEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.BeginWblockObjectsEventArgs"""
    def __init__(self, *args) -> None: ...
    IdMapping: IdMapping
    From: Database

class BeginWblockObjectsEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.BeginWblockObjectsEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: BeginWblockObjectsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: BeginWblockObjectsEventArgs) -> None: ...

class BeginWblockSelectedObjectsEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.BeginWblockSelectedObjectsEventArgs"""
    def __init__(self, *args) -> None: ...
    InsertionPoint: Point3d
    From: Database

class BeginWblockSelectedObjectsEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.BeginWblockSelectedObjectsEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: BeginWblockSelectedObjectsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: BeginWblockSelectedObjectsEventArgs) -> None: ...

class BlendOptions(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.BlendOptions"""
    def __init__(self, *args) -> None: ...
    DriveMode: DriveModeType
    CoplanarDirection: Nullable
    CoplanarPoint: Nullable
    Quality: int
    Solid: bool
    Simplify: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Clone(self, ) -> object: ...

class BlendOptionsBuilder:
    """.NET: Autodesk.AutoCAD.DatabaseServices.BlendOptionsBuilder"""
    def __init__(self, *args) -> None: ...
    DriveMode: DriveModeType
    CoplanarDirection: Nullable
    CoplanarPoint: Nullable
    Quality: int
    Solid: bool
    Simplify: bool
    def ToBlendOptions(self, ) -> BlendOptions: ...

class BlockBegin(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.BlockBegin"""
    def __init__(self, *args) -> None: ...
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class BlockConnectionType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.BlockConnectionType"""
    def __init__(self, *args) -> None: ...
    ConnectExtents: int  # = 0
    ConnectBase: int  # = 1
class BlockEnd(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.BlockEnd"""
    def __init__(self, *args) -> None: ...
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class BlockInsertionPointsEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.BlockInsertionPointsEventArgs"""
    def __init__(self, *args) -> None: ...
    AlignmentVectors: Vector3dCollection
    InsertionPoints: Point3dCollection
    BlockTableRecord: BlockTableRecord

class BlockInsertionPointsEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.BlockInsertionPointsEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: BlockInsertionPointsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: BlockInsertionPointsEventArgs) -> None: ...

class BlockPropertiesTable(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.BlockPropertiesTable"""
    def __init__(self, *args) -> None: ...
    IsDisabledInDrawingEditor: bool
    ContainsRuntimeParametersOnly: bool
    MustMatch: bool
    DefaultActiveRowIndex: int
    Columns: BlockPropertiesTableColumnCollection
    Rows: BlockPropertiesTableRowCollection
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Audit(self, ) -> list: ...

class BlockPropertiesTableColumn:
    """.NET: Autodesk.AutoCAD.DatabaseServices.BlockPropertiesTableColumn"""
    def __init__(self, *args) -> None: ...
    Table: BlockPropertiesTable
    Parameter: IParameter
    CustomProperties: ObjectId
    Format: str
    Removable: bool
    Editable: bool
    Constant: bool
    UnmatchedValue: ResultBuffer
    DefaultValue: ResultBuffer

class BlockPropertiesTableColumnCollection:
    """.NET: Autodesk.AutoCAD.DatabaseServices.BlockPropertiesTableColumnCollection"""
    def __init__(self, *args) -> None: ...
    SyncRoot: object
    IsSynchronized: bool
    Count: int
    Item: BlockPropertiesTableColumn
    def AddAt(self, id: ObjectId, parameterName: str, index: int) -> None: ...
    def AddItem(self, id: ObjectId, parameterName: str) -> None: ...
    def Clear(self, ) -> None: ...
    def ContainsColumn(self, id: ObjectId, parameterName: str) -> bool: ...
    def CopyTo(self, array: Array, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetIndex(self, column: BlockPropertiesTableColumn) -> int: ...
    def Move(self, index: int, newIndex: int) -> None: ...
    def Remove(self, column: BlockPropertiesTableColumn) -> None: ...

class BlockPropertiesTableRow:
    """.NET: Autodesk.AutoCAD.DatabaseServices.BlockPropertiesTableRow"""
    def __init__(self, *args) -> None: ...
    Table: BlockPropertiesTable
    SyncRoot: object
    IsSynchronized: bool
    Count: int
    Item: ResultBuffer
    Item: ResultBuffer
    def CopyTo(self, __unnamed000: Array, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...

class BlockPropertiesTableRowCollection:
    """.NET: Autodesk.AutoCAD.DatabaseServices.BlockPropertiesTableRowCollection"""
    def __init__(self, *args) -> None: ...
    SyncRoot: object
    IsSynchronized: bool
    Count: int
    Item: BlockPropertiesTableRow
    def AddAt(self, index: int) -> None: ...
    def AddItem(self, ) -> None: ...
    def Clear(self, ) -> None: ...
    def CopyTo(self, array: Array, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetIndex(self, row: BlockPropertiesTableRow) -> int: ...
    def Move(self, index: int, newIndex: int) -> None: ...
    def Remove(self, row: BlockPropertiesTableRow) -> None: ...
    def Sort(self, column: BlockPropertiesTableColumn, ascending: bool) -> None: ...

class BlockReference(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.BlockReference"""
    def __init__(self, *args) -> None: ...
    UnitFactor: float
    BlockUnit: UnitsValue
    Name: str
    AnonymousBlockTableRecord: ObjectId
    DynamicBlockTableRecord: ObjectId
    IsDynamicBlock: bool
    DynamicBlockReferencePropertyCollection: DynamicBlockReferencePropertyCollection
    TreatAsBlockRefForExplode: bool
    AttributeCollection: AttributeCollection
    BlockTransform: Matrix3d
    Normal: Vector3d
    Rotation: float
    ScaleFactors: Scale3d
    Position: Point3d
    BlockTableRecord: ObjectId
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def ConvertToStaticBlock(self, newBlockName: str) -> None: ...
    def ExplodeToOwnerSpace(self, ) -> None: ...
    def GeometryExtentsBestFit(self, parentTransform: Matrix3d) -> Extents3d: ...
    def ResetBlock(self, ) -> None: ...

class BlockScaling:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.BlockScaling"""
    def __init__(self, *args) -> None: ...
    Any: int  # = 0
    Uniform: int  # = 1
class BlockTable(SymbolTable):
    """.NET: Autodesk.AutoCAD.DatabaseServices.BlockTable"""
    def __init__(self, *args) -> None: ...
    IncludingErased: SymbolTable
    Item: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class BlockTableRecord(SymbolTableRecord):
    """.NET: Autodesk.AutoCAD.DatabaseServices.BlockTableRecord"""
    def __init__(self, *args) -> None: ...
    Hyperlinks: HyperLinkCollection
    IncludingErased: BlockTableRecord
    Units: UnitsValue
    IsDynamicBlock: bool
    BlockScaling: BlockScaling
    Explodable: bool
    DrawOrderTableId: ObjectId
    XrefStatus: XrefStatus
    IsUnloaded: bool
    LayoutId: ObjectId
    IsLayout: bool
    IsFromOverlayReference: bool
    IsFromExternalReference: bool
    IsAnonymous: bool
    PreviewIcon: Bitmap
    HasPreviewIcon: bool
    HasAttributeDefinitions: bool
    BlockEndId: ObjectId
    BlockBeginId: ObjectId
    Origin: Point3d
    PathName: str
    Comments: str
    IsResolved: bool
    IsDependent: bool
    Name: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AppendEntity(self, entity: Entity) -> ObjectId: ...
    def AssumeOwnershipOf(self, entitiesToMove: ObjectIdCollection) -> None: ...
    def GetAnonymousBlockIds(self, ) -> ObjectIdCollection: ...
    def GetBlockReferenceIds(self, directOnly: bool, forceValidity: bool) -> ObjectIdCollection: ...
    def GetEnumerator(self, ) -> BlockTableRecordEnumerator: ...
    def GetErasedBlockReferenceIds(self, ) -> ObjectIdCollection: ...
    def GetXrefDatabase(self, incrementUnresolved: bool) -> Database: ...
    def UpdateAnonymousBlocks(self, ) -> None: ...

class BlockTableRecordEnumerator(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.BlockTableRecordEnumerator"""
    def __init__(self, *args) -> None: ...
    Current: ObjectId
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class Body(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Body"""
    def __init__(self, *args) -> None: ...
    NumChanges: int
    UsesGraphicsCache: bool
    IsNull: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def AcisIn(fileName: str) -> DBObjectCollection: ...
    @staticmethod
    def AcisOut(fileName: str, entitiesOutToFile: DBObjectCollection) -> None: ...

class BooleanOperationType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.BooleanOperationType"""
    def __init__(self, *args) -> None: ...
    BoolUnite: int  # = 0
    BoolIntersect: int  # = 1
    BoolSubtract: int  # = 2
class BulgeVertex:
    """.NET: Autodesk.AutoCAD.DatabaseServices.BulgeVertex"""
    def __init__(self, *args) -> None: ...
    Bulge: float
    Vertex: Point2d

class BulgeVertexCollection(CollectionBase):
    """.NET: Autodesk.AutoCAD.DatabaseServices.BulgeVertexCollection"""
    def __init__(self, *args) -> None: ...
    Item: BulgeVertex
    Capacity: int
    Count: int
    def Add(self, value: BulgeVertex) -> int: ...
    def Contains(self, value: BulgeVertex) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def IndexOf(self, value: BulgeVertex) -> int: ...
    def Insert(self, index: int, value: BulgeVertex) -> None: ...
    def Remove(self, value: BulgeVertex) -> None: ...

class CallerMustCloseAttribute(Attribute):
    """.NET: Autodesk.AutoCAD.DatabaseServices.CallerMustCloseAttribute"""
    def __init__(self, *args) -> None: ...
    TypeId: object

class Cell(CellRange):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Cell"""
    def __init__(self, *args) -> None: ...
    Value: object
    ToolTip: str
    TextString: str
    DataLink: ObjectId
    ContentTypes: CellContentTypes
    FieldId: ObjectId
    BlockTableRecordId: ObjectId
    AttachmentPoint: Point3d
    CellType: TableCellType
    Column: int
    Row: int
    Contents: CellContentsCollection
    IsMerged: Nullable
    IsSingleCell: bool
    Item: Cell
    Borders: CellBorders
    CanInsertColumn: bool
    CanInsertRow: bool
    CanDeleteColumns: bool
    CanDeleteRows: bool
    IsEmpty: Nullable
    IsFormatEditable: Nullable
    IsContentEditable: Nullable
    IsLinked: Nullable
    TextStyleId: Nullable
    TextHeight: Nullable
    IsMergeAllEnabled: Nullable
    DataType: Nullable
    DataFormat: str
    ContentLayout: Nullable
    State: Nullable
    ContentColor: Color
    BackgroundColor: Color
    IsBackgroundColorNone: Nullable
    Alignment: Nullable
    Style: str
    BottomRightPlusOne: Cell
    BottomRight: Cell
    TopLeft: Cell
    RightColumn: int
    BottomRow: int
    LeftColumn: int
    TopRow: int
    IsNull: bool
    ParentTable: Table
    def GetBlockAttributeValue(self, attDefId: ObjectId) -> str: ...
    def GetDataLinkRange(self, ) -> CellRange: ...
    def GetExtents(self, ) -> Point3dCollection: ...
    def GetMergeRange(self, ) -> CellRange: ...
    def GetTextString(self, formatOption: FormatOption) -> str: ...
    def GetValue(self, formatOption: FormatOption) -> object: ...
    def RemoveDataLink(self, ) -> None: ...
    def ResetValue(self, ) -> None: ...
    def SetBlockAttributeValue(self, attDefId: ObjectId, value: str) -> None: ...
    def SetValue(self, value: object, parseOption: ParseOption) -> None: ...
    def UpdateDataLink(self, dir: UpdateDirection, option: UpdateOption) -> None: ...

class CellAlignment:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.CellAlignment"""
    def __init__(self, *args) -> None: ...
    TopLeft: int  # = 1
    TopCenter: int  # = 2
    TopRight: int  # = 3
    MiddleLeft: int  # = 4
    MiddleCenter: int  # = 5
    MiddleRight: int  # = 6
    BottomLeft: int  # = 7
    BottomCenter: int  # = 8
    BottomRight: int  # = 9
class CellBorder:
    """.NET: Autodesk.AutoCAD.DatabaseServices.CellBorder"""
    def __init__(self, *args) -> None: ...
    Overrides: Nullable
    Margin: Nullable
    Linetype: Nullable
    LineWeight: Nullable
    IsVisible: Nullable
    LineStyle: Nullable
    DoubleLineSpacing: Nullable
    Color: Color

class CellBorders:
    """.NET: Autodesk.AutoCAD.DatabaseServices.CellBorders"""
    def __init__(self, *args) -> None: ...
    Vertical: CellBorder
    Horizontal: CellBorder
    Bottom: CellBorder
    Right: CellBorder
    Top: CellBorder
    Left: CellBorder

class CellClass:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.CellClass"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Label: int  # = 1
    Data: int  # = 2
class CellContent:
    """.NET: Autodesk.AutoCAD.DatabaseServices.CellContent"""
    def __init__(self, *args) -> None: ...
    Overrides: CellProperties
    Value: object
    TextStyleId: ObjectId
    TextString: str
    TextHeight: float
    Scale: float
    Rotation: float
    IsAutoScale: bool
    Formula: str
    HasFormula: bool
    DataFormat: str
    ContentTypes: CellContentTypes
    FieldId: ObjectId
    DataType: DataTypeParameter
    BlockTableRecordId: ObjectId
    ContentColor: Color
    def DeleteContent(self, ) -> None: ...
    def GetBlockAttributeValue(self, attDefId: ObjectId) -> str: ...
    def GetTextString(self, formatOption: FormatOption) -> str: ...
    def GetValue(self, formatOption: FormatOption) -> object: ...
    def SetBlockAttributeValue(self, attDefId: ObjectId, value: str) -> None: ...
    def SetValue(self, value: object, parseOption: ParseOption) -> None: ...

class CellContentLayout:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.CellContentLayout"""
    def __init__(self, *args) -> None: ...
    Flow: int  # = 1
    StackedHorizontal: int  # = 2
    StackedVertical: int  # = 4
class CellContentTypes:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.CellContentTypes"""
    def __init__(self, *args) -> None: ...
    Unknown: int  # = 0
    Value: int  # = 1
    Field: int  # = 2
    Block: int  # = 4
class CellContentsCollection:
    """.NET: Autodesk.AutoCAD.DatabaseServices.CellContentsCollection"""
    def __init__(self, *args) -> None: ...
    Item: CellContent
    Count: int
    def Add(self, ) -> None: ...
    def Clear(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def InsertAt(self, index: int) -> None: ...
    def Move(self, fromIndex: int, toIndex: int) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class CellEdgeMasks:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.CellEdgeMasks"""
    def __init__(self, *args) -> None: ...
    TopMask: int  # = 1
    RightMask: int  # = 2
    BottomMask: int  # = 4
    LeftMask: int  # = 8
class CellMargins:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.CellMargins"""
    def __init__(self, *args) -> None: ...
    Top: int  # = 1
    Left: int  # = 2
    Bottom: int  # = 4
    Right: int  # = 8
class CellOption:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.CellOption"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    InheritCellFormat: int  # = 1
class CellProperties:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.CellProperties"""
    def __init__(self, *args) -> None: ...
    Invalid: int  # = 0
    DataType: int  # = 1
    DataFormat: int  # = 2
    Rotation: int  # = 4
    Scale: int  # = 8
    Alignment: int  # = 16
    ContentColor: int  # = 32
    TextStyle: int  # = 64
    TextHeight: int  # = 128
    AutoScale: int  # = 256
    BackgroundColor: int  # = 512
    MarginLeft: int  # = 1024
    MarginTop: int  # = 2048
    MarginRight: int  # = 4096
    MarginBottom: int  # = 8192
    ContentLayout: int  # = 16384
    MergeAll: int  # = 32768
    FlowDirBtoT: int  # = 65536
    MarginHorzSpacing: int  # = 131072
    MarginVertSpacing: int  # = 262144
class CellRange:
    """.NET: Autodesk.AutoCAD.DatabaseServices.CellRange"""
    def __init__(self, *args) -> None: ...
    IsMerged: Nullable
    IsSingleCell: bool
    Item: Cell
    Borders: CellBorders
    CanInsertColumn: bool
    CanInsertRow: bool
    CanDeleteColumns: bool
    CanDeleteRows: bool
    IsEmpty: Nullable
    IsFormatEditable: Nullable
    IsContentEditable: Nullable
    IsLinked: Nullable
    TextStyleId: Nullable
    TextHeight: Nullable
    IsMergeAllEnabled: Nullable
    DataType: Nullable
    DataFormat: str
    ContentLayout: Nullable
    State: Nullable
    ContentColor: Color
    BackgroundColor: Color
    IsBackgroundColorNone: Nullable
    Alignment: Nullable
    Style: str
    BottomRightPlusOne: Cell
    BottomRight: Cell
    TopLeft: Cell
    RightColumn: int
    BottomRow: int
    LeftColumn: int
    TopRow: int
    IsNull: bool
    ParentTable: Table
    def ClearStyleOverrides(self, ) -> None: ...
    @staticmethod
    def Create(table: Table, topRow: int, leftColumn: int, bottomRow: int, rightColumn: int) -> CellRange: ...
    def DeleteContent(self, ) -> None: ...
    def Equals(self, pRange: object) -> bool: ...
    def GetCustomData(self, key: str) -> object: ...
    def GetDataLink(self, ) -> ObjectIdCollection: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetHashCode(self, ) -> int: ...
    def GetStyleOverrides(self, ) -> list: ...
    def IEnumerableGetEnumerator(self, ) -> IEnumerator: ...
    def SetCustomData(self, key: str, value: object) -> None: ...
    def SetDataLink(self, dataLinkId: ObjectId, bUpdate: bool) -> None: ...

class CellReference:
    """.NET: Autodesk.AutoCAD.DatabaseServices.CellReference"""
    def __init__(self, *args) -> None: ...
    Column: int
    Row: int

class CellStates:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.CellStates"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    ContentLocked: int  # = 1
    ContentReadOnly: int  # = 2
    Linked: int  # = 4
    ContentModifiedAfterUpdate: int  # = 8
    FormatLocked: int  # = 16
    FormatReadOnly: int  # = 32
    FormatModifiedAfterUpdate: int  # = 64
class CellType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.CellType"""
    def __init__(self, *args) -> None: ...
    Unknown: int  # = 0
    Integer: int  # = 1
    Double: int  # = 2
    CharPtr: int  # = 3
    Point: int  # = 4
    ObjectId: int  # = 5
    HardOwnerId: int  # = 6
    SoftOwnerId: int  # = 7
    HardPtrId: int  # = 8
    SoftPtrId: int  # = 9
    Bool: int  # = 10
    Vector: int  # = 11
class CenterPointConstraint(ConcentricConstraint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.CenterPointConstraint"""
    def __init__(self, *args) -> None: ...
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Circle(Curve):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Circle"""
    def __init__(self, *args) -> None: ...
    Diameter: float
    Circumference: float
    Normal: Vector3d
    Thickness: float
    Radius: float
    Center: Point3d
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ClipBoundaryType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.ClipBoundaryType"""
    def __init__(self, *args) -> None: ...
    Invalid: int  # = 0
    Rectangle: int  # = 1
    Poly: int  # = 2
class ColinearConstraint(GeometricalConstraint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ColinearConstraint"""
    def __init__(self, *args) -> None: ...
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class CollisionType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.CollisionType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Solid: int  # = 1
class Column(CellRange):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Column"""
    def __init__(self, *args) -> None: ...
    Name: str
    MinimumWidth: float
    Width: float
    IsMerged: Nullable
    IsSingleCell: bool
    Item: Cell
    Borders: CellBorders
    CanInsertColumn: bool
    CanInsertRow: bool
    CanDeleteColumns: bool
    CanDeleteRows: bool
    IsEmpty: Nullable
    IsFormatEditable: Nullable
    IsContentEditable: Nullable
    IsLinked: Nullable
    TextStyleId: Nullable
    TextHeight: Nullable
    IsMergeAllEnabled: Nullable
    DataType: Nullable
    DataFormat: str
    ContentLayout: Nullable
    State: Nullable
    ContentColor: Color
    BackgroundColor: Color
    IsBackgroundColorNone: Nullable
    Alignment: Nullable
    Style: str
    BottomRightPlusOne: Cell
    BottomRight: Cell
    TopLeft: Cell
    RightColumn: int
    BottomRow: int
    LeftColumn: int
    TopRow: int
    IsNull: bool
    ParentTable: Table

class ColumnType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.ColumnType"""
    def __init__(self, *args) -> None: ...
    NoColumns: int  # = 0
    StaticColumns: int  # = 1
    DynamicColumns: int  # = 2
class ColumnsCollection:
    """.NET: Autodesk.AutoCAD.DatabaseServices.ColumnsCollection"""
    def __init__(self, *args) -> None: ...
    Item: Column
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...

class CompositeConstraint(GeometricalConstraint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.CompositeConstraint"""
    def __init__(self, *args) -> None: ...
    OwnedConstraints: list
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class CompoundObjectId(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.CompoundObjectId"""
    def __init__(self, *args) -> None: ...
    Transform: Matrix3d
    Status: StatusType
    IsSimpleObjectId: bool
    IsExternal: bool
    IsEmpty: bool
    Path: ObjectIdCollection
    FullPath: ObjectIdCollection
    LeafId: ObjectId
    TopId: ObjectId
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def DwgInFields(self, filer: DwgFiler, ownerVersion: int) -> None: ...
    def DwgOutFields(self, filer: DwgFiler, hostDatabase: Database) -> None: ...
    def DxfInFields(self, filer: DxfFiler, hostDatabase: Database, ownerVersion: int) -> None: ...
    def DxfOutFields(self, filer: DxfFiler, hostDatabase: Database) -> None: ...
    def IsValid(self, validityCheckingLevel: int) -> bool: ...
    @staticmethod
    def NullId() -> CompoundObjectId: ...
    def Remap(self, idMap: IdMapping) -> bool: ...
    def Set(self, id: ObjectId, path: ObjectIdCollection, hostDatabase: Database) -> None: ...
    def SetEmpty(self, ) -> None: ...
    def SetFullPath(self, fullPath: ObjectIdCollection, hostDatabase: Database) -> None: ...

class ConcentricConstraint(GeometricalConstraint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ConcentricConstraint"""
    def __init__(self, *args) -> None: ...
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ConstrainType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.ConstrainType"""
    def __init__(self, *args) -> None: ...
    TurnHeight: int  # = 0
    Turns: int  # = 1
    Height: int  # = 2
class Constrained2PointsConstructionLine(ConstrainedConstructionLine):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Constrained2PointsConstructionLine"""
    def __init__(self, *args) -> None: ...
    Direction: Vector3d
    PointOnLine: Point3d
    ConstrainedImplicitPoints: list
    IsBounded: bool
    FullSubentityPaths: list
    ConnectedGeometries: list
    ConnectedConstraints: list
    OwningRigidSet: ConstrainedRigidSet
    GeomDependencyId: ObjectId
    IsReadOnly: bool
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ConstrainedArc(ConstrainedCircle):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ConstrainedArc"""
    def __init__(self, *args) -> None: ...
    MidPoint: Point3d
    EndPoint: Point3d
    StartPoint: Point3d
    CenterPoint: Point3d
    Radius: float
    ConstrainedImplicitPoints: list
    IsBounded: bool
    FullSubentityPaths: list
    ConnectedGeometries: list
    ConnectedConstraints: list
    OwningRigidSet: ConstrainedRigidSet
    GeomDependencyId: ObjectId
    IsReadOnly: bool
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ConstrainedBoundedEllipse(ConstrainedEllipse):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ConstrainedBoundedEllipse"""
    def __init__(self, *args) -> None: ...
    EndPoint: Point3d
    StartPoint: Point3d
    CenterPoint: Point3d
    MinorRadius: float
    MajorRadius: float
    Direction: Vector3d
    ConstrainedImplicitPoints: list
    IsBounded: bool
    FullSubentityPaths: list
    ConnectedGeometries: list
    ConnectedConstraints: list
    OwningRigidSet: ConstrainedRigidSet
    GeomDependencyId: ObjectId
    IsReadOnly: bool
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ConstrainedBoundedLine(ConstrainedLine):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ConstrainedBoundedLine"""
    def __init__(self, *args) -> None: ...
    MidPoint: Point3d
    EndPoint: Point3d
    StartPoint: Point3d
    IsRay: bool
    Direction: Vector3d
    PointOnLine: Point3d
    ConstrainedImplicitPoints: list
    IsBounded: bool
    FullSubentityPaths: list
    ConnectedGeometries: list
    ConnectedConstraints: list
    OwningRigidSet: ConstrainedRigidSet
    GeomDependencyId: ObjectId
    IsReadOnly: bool
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ConstrainedCircle(ConstrainedCurve):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ConstrainedCircle"""
    def __init__(self, *args) -> None: ...
    CenterPoint: Point3d
    Radius: float
    ConstrainedImplicitPoints: list
    IsBounded: bool
    FullSubentityPaths: list
    ConnectedGeometries: list
    ConnectedConstraints: list
    OwningRigidSet: ConstrainedRigidSet
    GeomDependencyId: ObjectId
    IsReadOnly: bool
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ConstrainedConstructionLine(ConstrainedLine):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ConstrainedConstructionLine"""
    def __init__(self, *args) -> None: ...
    Direction: Vector3d
    PointOnLine: Point3d
    ConstrainedImplicitPoints: list
    IsBounded: bool
    FullSubentityPaths: list
    ConnectedGeometries: list
    ConnectedConstraints: list
    OwningRigidSet: ConstrainedRigidSet
    GeomDependencyId: ObjectId
    IsReadOnly: bool
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ConstrainedCurve(ConstrainedGeometry):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ConstrainedCurve"""
    def __init__(self, *args) -> None: ...
    ConstrainedImplicitPoints: list
    IsBounded: bool
    FullSubentityPaths: list
    ConnectedGeometries: list
    ConnectedConstraints: list
    OwningRigidSet: ConstrainedRigidSet
    GeomDependencyId: ObjectId
    IsReadOnly: bool
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ConstrainedDatumLine(ConstrainedConstructionLine):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ConstrainedDatumLine"""
    def __init__(self, *args) -> None: ...
    Direction: Vector3d
    PointOnLine: Point3d
    ConstrainedImplicitPoints: list
    IsBounded: bool
    FullSubentityPaths: list
    ConnectedGeometries: list
    ConnectedConstraints: list
    OwningRigidSet: ConstrainedRigidSet
    GeomDependencyId: ObjectId
    IsReadOnly: bool
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ConstrainedEllipse(ConstrainedCurve):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ConstrainedEllipse"""
    def __init__(self, *args) -> None: ...
    CenterPoint: Point3d
    MinorRadius: float
    MajorRadius: float
    Direction: Vector3d
    ConstrainedImplicitPoints: list
    IsBounded: bool
    FullSubentityPaths: list
    ConnectedGeometries: list
    ConnectedConstraints: list
    OwningRigidSet: ConstrainedRigidSet
    GeomDependencyId: ObjectId
    IsReadOnly: bool
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ConstrainedGeometry(ConstraintGroupNode):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ConstrainedGeometry"""
    def __init__(self, *args) -> None: ...
    FullSubentityPaths: list
    ConnectedGeometries: list
    ConnectedConstraints: list
    OwningRigidSet: ConstrainedRigidSet
    GeomDependencyId: ObjectId
    IsReadOnly: bool
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CommonConstraints(self, otherConsGeom: ConstrainedGeometry) -> list: ...

class ConstrainedImplicitPoint(ConstrainedPoint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ConstrainedImplicitPoint"""
    def __init__(self, *args) -> None: ...
    Point: Point3d
    ConstrainedCurveId: int
    PointIndex: int
    PointType: ImplicitPointType
    FullSubentityPaths: list
    ConnectedGeometries: list
    ConnectedConstraints: list
    OwningRigidSet: ConstrainedRigidSet
    GeomDependencyId: ObjectId
    IsReadOnly: bool
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ConstrainedLine(ConstrainedCurve):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ConstrainedLine"""
    def __init__(self, *args) -> None: ...
    Direction: Vector3d
    PointOnLine: Point3d
    ConstrainedImplicitPoints: list
    IsBounded: bool
    FullSubentityPaths: list
    ConnectedGeometries: list
    ConnectedConstraints: list
    OwningRigidSet: ConstrainedRigidSet
    GeomDependencyId: ObjectId
    IsReadOnly: bool
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ConstrainedPoint(ConstrainedGeometry):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ConstrainedPoint"""
    def __init__(self, *args) -> None: ...
    Point: Point3d
    FullSubentityPaths: list
    ConnectedGeometries: list
    ConnectedConstraints: list
    OwningRigidSet: ConstrainedRigidSet
    GeomDependencyId: ObjectId
    IsReadOnly: bool
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ConstrainedRigidSet(ConstrainedGeometry):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ConstrainedRigidSet"""
    def __init__(self, *args) -> None: ...
    Transform: Matrix3d
    NumOfConstrainedGeoms: int
    FullSubentityPaths: list
    ConnectedGeometries: list
    ConnectedConstraints: list
    OwningRigidSet: ConstrainedRigidSet
    GeomDependencyId: ObjectId
    IsReadOnly: bool
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetConstrainedGeomAt(self, index: int) -> ConstrainedGeometry: ...

class ConstrainedSpline(ConstrainedCurve):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ConstrainedSpline"""
    def __init__(self, *args) -> None: ...
    NumOfDefinePoints: int
    NurbSpline: NurbCurve3d
    ConstrainedImplicitPoints: list
    IsBounded: bool
    FullSubentityPaths: list
    ConnectedGeometries: list
    ConnectedConstraints: list
    OwningRigidSet: ConstrainedRigidSet
    GeomDependencyId: ObjectId
    IsReadOnly: bool
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def DefinePointAt(self, index: int) -> Point3d: ...

class ConstraintGroupNode(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ConstraintGroupNode"""
    def __init__(self, *args) -> None: ...
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ContentType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.ContentType"""
    def __init__(self, *args) -> None: ...
    NoneContent: int  # = 0
    BlockContent: int  # = 1
    MTextContent: int  # = 2
    ToleranceContent: int  # = 3
class Curve(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Curve"""
    def __init__(self, *args) -> None: ...
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def CreateFromGeCurve(geCurve: Curve3d, __unnamed001: Vector3d, tolerance: Tolerance) -> Curve: ...
    def Extend(self, extendStart: bool, toPoint: Point3d) -> None: ...
    def GetClosestPointTo(self, givenPoint: Point3d, direction: Vector3d, extend: bool) -> Point3d: ...
    def GetDistAtPoint(self, point: Point3d) -> float: ...
    def GetDistanceAtParameter(self, value: float) -> float: ...
    def GetFirstDerivative(self, point: Point3d) -> Vector3d: ...
    def GetGeCurve(self, tolerance: Tolerance) -> Curve3d: ...
    def GetOffsetCurves(self, offsetDist: float) -> DBObjectCollection: ...
    def GetOffsetCurvesGivenPlaneNormal(self, normal: Vector3d, offsetDist: float) -> DBObjectCollection: ...
    def GetOrthoProjectedCurve(self, planeToProjectOn: Plane) -> Curve: ...
    def GetParameterAtDistance(self, dist: float) -> float: ...
    def GetParameterAtPoint(self, point: Point3d) -> float: ...
    def GetPointAtDist(self, value: float) -> Point3d: ...
    def GetPointAtParameter(self, value: float) -> Point3d: ...
    def GetProjectedCurve(self, planeToProjectOn: Plane, projectionDirection: Vector3d) -> Curve: ...
    def GetSecondDerivative(self, point: Point3d) -> Vector3d: ...
    def GetSplitCurves(self, points: Point3dCollection) -> DBObjectCollection: ...
    def ReverseCurve(self, ) -> None: ...
    def SetFromGeCurve(self, geCurve: Curve3d, __unnamed001: Vector3d, tolerance: Tolerance) -> None: ...

class CustomObjectSnapMode(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.CustomObjectSnapMode"""
    def __init__(self, *args) -> None: ...
    DisplayString: str
    Bitmap: Bitmap
    GlyphSize: int
    ToolTipText: str
    Glyph: Glyph
    GlobalModeString: str
    LocalModeString: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Activate(mode: str) -> None: ...
    def ApplyToEntityType(self, entity: RXClass, callback: AddObjectSnapInfo) -> None: ...
    @staticmethod
    def Deactivate(mode: str) -> None: ...
    @staticmethod
    def IsActive(mode: str) -> bool: ...
    def RemoveFromEntityType(self, entity: RXClass) -> None: ...

class CustomScale:
    """.NET: Autodesk.AutoCAD.DatabaseServices.CustomScale"""
    def __init__(self, *args) -> None: ...
    Denominator: float
    Numerator: float
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def IsEqualTo(self, a: CustomScale, tolerance: Tolerance) -> bool: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class DBDictionary(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DBDictionary"""
    def __init__(self, *args) -> None: ...
    IncludingErased: DBDictionary
    Item: object
    Count: int
    MergeStyle: DuplicateRecordCloning
    TreatElementsAsHard: bool
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Contains(self, objId: ObjectId) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetAt(self, entryName: str) -> ObjectId: ...
    def GetEnumerator(self, ) -> DbDictionaryEnumerator: ...
    def NameAt(self, objId: ObjectId) -> str: ...
    def Remove(self, objId: ObjectId) -> None: ...
    def SetAt(self, searchKey: str, newValue: DBObject) -> ObjectId: ...
    def SetName(self, oldName: str, newName: str) -> None: ...

class DBDictionaryEntry:
    """.NET: Autodesk.AutoCAD.DatabaseServices.DBDictionaryEntry"""
    def __init__(self, *args) -> None: ...
    Value: ObjectId
    Key: str
    def ToString(self, provider: IFormatProvider) -> str: ...

class DBObject(Drawable):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DBObject"""
    def __init__(self, *args) -> None: ...
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddContext(self, context: ObjectContext) -> None: ...
    def ApplyPaperOrientationTransform(self, viewport: Viewport) -> None: ...
    def ApplyPartialUndo(self, undoFiler: DwgFiler, classObj: RXClass) -> None: ...
    def Audit(self, auditInfo: AuditInfo) -> None: ...
    def Cancel(self, ) -> None: ...
    def Close(self, ) -> None: ...
    def CloseAndPage(self, onlyWhenClean: bool) -> None: ...
    def CreateExtensionDictionary(self, ) -> None: ...
    def DecomposeForSave(self, version: DwgVersion) -> DecomposeForSaveReplacementRecord: ...
    def DeepClone(self, ownerPointer: DBObject, idMap: IdMapping, isPrimary: bool) -> DBObject: ...
    def DisableUndoRecording(self, disable: bool) -> None: ...
    def DowngradeOpen(self, ) -> None: ...
    def DowngradeToNotify(self, wasWritable: bool) -> None: ...
    def DwgIn(self, filer: DwgFiler) -> None: ...
    def DwgOut(self, filer: DwgFiler) -> None: ...
    def DxfIn(self, filer: DxfFiler) -> None: ...
    def DxfOut(self, filer: DxfFiler) -> None: ...
    def Erase(self, erasing: bool) -> None: ...
    @staticmethod
    def FromAcadObject(acadObj: object) -> ObjectId: ...
    def GetBinaryDataForKey(self, key: str) -> list: ...
    def GetEventExtender(self, create: bool) -> DBObjectEventExtender: ...
    def GetField(self, propertyName: str) -> ObjectId: ...
    def GetObjectSaveVersion(self, filer: DxfFiler) -> FullDwgVersion: ...
    def GetParameterInterface(self, name: str, runtimeInterface: bool) -> IParameter: ...
    def GetPersistentReactorIds(self, ) -> ObjectIdCollection: ...
    def GetReactors(self, ) -> List: ...
    def GetTransientReactors(self, ) -> List: ...
    def GetXDataForApplication(self, applicationName: str) -> ResultBuffer: ...
    def HandOverTo(self, newPointer: DBObject, keepXData: bool, keepExtensionDictionary: bool) -> None: ...
    def HasContext(self, context: ObjectContext) -> bool: ...
    def HasPersistentReactor(self, objId: ObjectId) -> bool: ...
    @staticmethod
    def IsCustomObject(id: ObjectId) -> bool: ...
    def ReleaseExtensionDictionary(self, ) -> None: ...
    def RemoveContext(self, context: ObjectContext) -> None: ...
    def RemoveField(self, id: ObjectId) -> None: ...
    def ResetScaleDependentProperties(self, ) -> None: ...
    def SetBinaryDataForKey(self, key: str, chunk: list) -> None: ...
    def SetField(self, propertyName: str, field: Field) -> ObjectId: ...
    def SetFromStyle(self, ) -> bool: ...
    def SetObjectIdsInFlux(self, ) -> None: ...
    def SetPaperOrientation(self, bPaperOrientation: bool) -> None: ...
    def SupportsCollection(self, collectionName: str) -> bool: ...
    def SwapIdWith(self, otherId: ObjectId, swapExtendedData: bool, swapExtensionDictionary: bool) -> None: ...
    def SwapReferences(self, idMap: IdMapping) -> None: ...
    def UpgradeFromNotify(self, ) -> bool: ...
    def UpgradeOpen(self, ) -> None: ...
    def WblockClone(self, ownerPointer: RXObject, idMap: IdMapping, isPrimary: bool) -> DBObject: ...
    def XDataTransformBy(self, transform: Matrix3d) -> None: ...

class DBObjectCollection(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DBObjectCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: DBObject
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, value: DBObject) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: DBObject) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: DBObject) -> int: ...
    def Insert(self, index: int, value: DBObject) -> None: ...
    def Remove(self, value: DBObject) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class DBObjectReference:
    """.NET: Autodesk.AutoCAD.DatabaseServices.DBObjectReference"""
    def __init__(self, *args) -> None: ...
    Kind: int
    ObjectId: ObjectId

class DBObjectReferenceCollection(CollectionBase):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DBObjectReferenceCollection"""
    def __init__(self, *args) -> None: ...
    Item: DBObjectReference
    Capacity: int
    Count: int
    def Add(self, value: DBObjectReference) -> int: ...
    def Contains(self, value: DBObjectReference) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def IndexOf(self, value: DBObjectReference) -> int: ...
    def Insert(self, index: int, value: DBObjectReference) -> None: ...
    def Remove(self, value: DBObjectReference) -> None: ...

class DBPoint(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DBPoint"""
    def __init__(self, *args) -> None: ...
    EcsRotation: float
    Normal: Vector3d
    Thickness: float
    Position: Point3d
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class DBText(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DBText"""
    def __init__(self, *args) -> None: ...
    Justify: AttachmentPoint
    VerticalMode: TextVerticalMode
    HorizontalMode: TextHorizontalMode
    IsMirroredInY: bool
    IsMirroredInX: bool
    TextStyleId: ObjectId
    TextStyleName: str
    TextString: str
    WidthFactor: float
    Height: float
    Rotation: float
    Oblique: float
    Thickness: float
    Normal: Vector3d
    IsDefaultAlignment: bool
    AlignmentPoint: Point3d
    Position: Point3d
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AdjustAlignment(self, alternateDatabaseToUse: Database) -> None: ...
    def ConvertFieldToText(self, ) -> None: ...
    def CorrectSpelling(self, ) -> int: ...
    def getTextWithFieldCodes(self, ) -> str: ...

class DBVisualStyle(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DBVisualStyle"""
    def __init__(self, *args) -> None: ...
    InternalUseOnly: bool
    Type: VisualStyleType
    Description: str
    Name: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CopyFrom(self, pSrc: VisualStyle) -> None: ...
    def CopyTo(self, pDest: VisualStyle) -> None: ...
    def GetTrait(self, prop: VisualStyleProperty) -> object: ...
    def GetTraitFlag(self, prop: VisualStyleProperty, flagVal: int) -> bool: ...
    def SetTrait(self, prop: VisualStyleProperty, red: float, green: float, blue: float, op: VisualStyleOperation) -> None: ...
    def SetTraitFlag(self, prop: VisualStyleProperty, flagVal: int, bEnable: bool) -> None: ...

class DataAdapter(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DataAdapter"""
    def __init__(self, *args) -> None: ...
    Description: str
    Name: str
    DataAdapterId: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CreateDataObject(self, dataLink: DataLink) -> LinkedData: ...
    def GetSourceFiles(self, dataLink: DataLink, nContext: DataLinkGetSourceContext) -> ArrayList: ...
    def IsValid(self, dataLink: DataLink) -> bool: ...
    def RepathSourceFiles(self, dataLink: DataLink, sBasePath: str, nOption: PathOption) -> None: ...
    def SourceFileModified(self, dataLink: DataLink, sModifiedFile: str, pAction: UpdateAction) -> None: ...
    def Update(self, dataLink: DataLink, data: LinkedData, direction: UpdateDirection, option: UpdateOption) -> None: ...

class DataAdapterManager(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DataAdapterManager"""
    def __init__(self, *args) -> None: ...
    AdapterProviderCount: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetAdapterProvider(index: int) -> DataAdapterProvider: ...
    @staticmethod
    def GetDataAdapter(adapterId: str) -> DataAdapter: ...
    @staticmethod
    def RegisterAdapterProvider(provider: DataAdapterProvider) -> None: ...
    @staticmethod
    def UnregisterAdapterProvider(provider: DataAdapterProvider) -> None: ...

class DataAdapterProvider(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DataAdapterProvider"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetDataAdapter(self, adapterId: str) -> DataAdapter: ...

class DataAdapterSourceFilesException(Exception):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DataAdapterSourceFilesException"""
    def __init__(self, *args) -> None: ...
    FileNameList: ArrayList
    ErrorStatus: ErrorStatus
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class DataCell(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DataCell"""
    def __init__(self, *args) -> None: ...
    CellType: CellType
    Value: object
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Init(self, ) -> None: ...
    def SetBool(self, value: bool) -> None: ...
    def SetDouble(self, value: float) -> None: ...
    def SetHardOwnershipId(self, value: ObjectId) -> None: ...
    def SetHardPointerId(self, value: ObjectId) -> None: ...
    def SetInteger(self, value: int) -> None: ...
    def SetObjectId(self, value: ObjectId) -> None: ...
    def SetPoint(self, value: Point3d) -> None: ...
    def SetSoftOwnershipId(self, value: ObjectId) -> None: ...
    def SetSoftPointerId(self, value: ObjectId) -> None: ...
    def SetString(self, value: str) -> None: ...
    def SetVector(self, value: Vector3d) -> None: ...

class DataCellCollection(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DataCellCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: DataCell
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, value: DataCell) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: DataCell) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: DataCell) -> int: ...
    def Insert(self, index: int, value: DataCell) -> None: ...
    def Remove(self, value: DataCell) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class DataColumn(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DataColumn"""
    def __init__(self, *args) -> None: ...
    NumCells: int
    ColumnName: str
    ColumnType: CellType
    GrowLength: int
    PhysicalLength: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AppendCell(self, cell: DataCell) -> None: ...
    def Assign(self, col: DataColumn) -> None: ...
    def GetCellAt(self, index: int) -> DataCell: ...
    def GetIndexAtCell(self, cell: DataCell) -> int: ...
    def InsertCellAt(self, index: int, cell: DataCell) -> None: ...
    def RemoveCellAt(self, index: int) -> None: ...
    def SetCellAt(self, index: int, cell: DataCell) -> None: ...

class DataLink(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DataLink"""
    def __init__(self, *args) -> None: ...
    IsValid: bool
    UpdateOption: int
    DataLinkOption: DataLinkOption
    ToolTip: str
    Description: str
    Name: str
    ConnectionString: str
    DataAdapterId: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetSourceFiles(self, nContext: DataLinkGetSourceContext) -> ArrayList: ...
    def GetTargets(self, ) -> ObjectIdCollection: ...
    def GetUpdateStatus(self, pDir: UpdateDirection, pTime: DateTime, errMessage: str) -> ErrorStatus: ...
    def RepathSourceFiles(self, sBasePath: str, nOption: PathOption) -> None: ...
    def Update(self, dir: UpdateDirection, option: UpdateOption) -> None: ...

class DataLinkGetSourceContext:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.DataLinkGetSourceContext"""
    def __init__(self, *args) -> None: ...
    Unknown: int  # = 0
    Etransmit: int  # = 1
    XrefManager: int  # = 2
    FileWatcher: int  # = 3
    Other: int  # = 4
    OrignalPath: int  # = 256
class DataLinkManager(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DataLinkManager"""
    def __init__(self, *args) -> None: ...
    DataLinkCount: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddDataLink(self, dataLink: DataLink) -> ObjectId: ...
    def GetDataLink(self, name: str) -> ObjectId: ...
    def RemoveDataLink(self, idDataLink: ObjectId) -> None: ...
    def Update(self, dataIds: ObjectIdCollection, direction: UpdateDirection, option: UpdateOption) -> None: ...

class DataLinkOption:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.DataLinkOption"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Anonymous: int  # = 1
    PersistCache: int  # = 2
class DataTable(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DataTable"""
    def __init__(self, *args) -> None: ...
    TableName: str
    NumColsGrowSize: int
    NumColsPhysicalSize: int
    NumRowsGrowSize: int
    NumRowsPhysicalSize: int
    NumRows: int
    NumColumns: int
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AppendColumn(self, type: CellType, columnName: str) -> None: ...
    def AppendRow(self, row: DataCellCollection, validate: bool) -> None: ...
    def Assign(self, other: DataTable) -> None: ...
    def GetCellAt(self, row: int, col: int) -> DataCell: ...
    def GetColumnAt(self, index: int) -> DataColumn: ...
    def GetColumnIndexAtName(self, name: str) -> int: ...
    def GetColumnNameAt(self, index: int) -> str: ...
    def GetColumnTypeAt(self, index: int) -> CellType: ...
    def GetRowAt(self, index: int) -> DataCellCollection: ...
    def InsertColumnAt(self, index: int, type: CellType, columnName: str) -> None: ...
    def InsertRowAt(self, index: int, row: DataCellCollection, validate: bool) -> None: ...
    def RemoveColumnAt(self, index: int) -> None: ...
    def RemoveRowAt(self, index: int) -> None: ...
    def SetCellAt(self, row: int, col: int, cell: DataCell) -> None: ...
    def SetRowAt(self, index: int, row: DataCellCollection, validate: bool) -> None: ...

class DataType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.DataType"""
    def __init__(self, *args) -> None: ...
    Unknown: int  # = 0
    Long: int  # = 1
    Double: int  # = 2
    String: int  # = 4
    Date: int  # = 8
    Point: int  # = 16
    Point3d: int  # = 32
    ObjectId: int  # = 64
    Buffer: int  # = 128
    Resbuf: int  # = 256
    General: int  # = 512
class DataTypeParameter:
    """.NET: Autodesk.AutoCAD.DatabaseServices.DataTypeParameter"""
    def __init__(self, *args) -> None: ...
    UnitType: UnitType
    DataType: DataType
    def Equals(self, other: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class Database(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Database"""
    def __init__(self, *args) -> None: ...
    HomeView: DbHomeView
    GeoDataObject: ObjectId
    UpdateThumbnail: int
    MsOleScale: float
    LayerNotify: int
    LayerEval: int
    Indexctl: int
    PdfFrame: int
    DgnFrame: int
    DwfFrame: int
    MsLtScale: bool
    AnnotativeDwg: bool
    AnnoAllVisible: bool
    ShadowPlaneLocation: float
    Cmaterial: ObjectId
    Cshadow: int
    TimeZone: TimeZone
    LoftMag2: float
    LoftMag1: float
    LoftAng2: float
    LoftAng1: float
    LoftNormals: int
    LoftParam: int
    PsolHeight: float
    PsolWidth: float
    ShowHist: int
    SolidHist: int
    DxEval: int
    StepSize: float
    StepsPerSec: float
    CameraDisplay: bool
    LensLength: float
    CameraHeight: float
    LayerFilters: LayerFilterTree
    DrawOrderCtl: int
    SummaryInfo: DatabaseSummaryInfo
    Dimzin: int
    Dimupt: bool
    Dimtzin: int
    Dimtxtdirection: bool
    Dimtxt: float
    Dimtxsty: ObjectId
    Dimtvp: float
    Dimtsz: float
    Dimtp: float
    Dimtolj: int
    Dimtol: bool
    Dimtoh: bool
    Dimtofl: bool
    Dimtmove: int
    Dimtm: float
    Dimtix: bool
    Dimtih: bool
    Dimtfillclr: Color
    Dimtfill: int
    Dimtfac: float
    Dimtdec: int
    Dimtad: int
    Dimsoxd: bool
    Dimse2: bool
    Dimse1: bool
    Dimsd2: bool
    Dimsd1: bool
    Dimscale: float
    Dimsah: bool
    Dimrnd: float
    Dimlwe: LineWeight
    Dimlwd: LineWeight
    Dimlunit: int
    Dimltype: ObjectId
    Dimltex2: ObjectId
    Dimltex1: ObjectId
    Dimlim: bool
    Dimlfac: float
    Dimldrblk: ObjectId
    Dimjust: int
    Dimjogang: float
    Dimgap: float
    Dimfxlen: float
    DimfxlenOn: bool
    Dimfrac: int
    Dimexo: float
    Dimexe: float
    Dimdsep: str
    Dimdli: float
    Dimdle: float
    Dimdec: int
    Dimclrt: Color
    Dimclre: Color
    Dimclrd: Color
    Dimcen: float
    Dimazin: int
    Dimaunit: int
    Dimatfit: int
    Dimasz: float
    Dimarcsym: int
    Dimapost: str
    Dimaltz: int
    Dimaltu: int
    Dimalttz: int
    Dimalttd: int
    Dimaltrnd: float
    Dimaltf: float
    Dimaltd: int
    Dimalt: bool
    Dimadec: int
    AcadDatabase: object
    Cannoscale: AnnotationScale
    dragvs: ObjectId
    LightsInBlocks: bool
    LightingUnits: int
    TileModeLightSynch: int
    LightGlyphDisplay: int
    NorthDirection: float
    Longitude: float
    Latitude: float
    AllowExtendedNames: bool
    IntersectColor: int
    IntersectDisplay: int
    ObscuredLineType: int
    ObscuredColor: int
    HaloGap: int
    HideText: int
    DimAssoc: int
    SortEnts: int
    DwgFileWasSavedByAutodeskSoftware: bool
    ViewportScaleDefault: float
    CurrentViewportTableRecordId: ObjectId
    PlotStyleMode: bool
    Insunits: UnitsValue
    TstackSize: int
    TStackAlign: int
    VersionGuid: str
    FingerprintGuid: str
    IsPartiallyOpened: bool
    IsBeingDestroyed: bool
    Filename: str
    StyleSheet: str
    HyperlinkBase: str
    ProjectName: str
    Dimblk2: ObjectId
    Dimblk1: ObjectId
    Dimblk: ObjectId
    Dimpost: str
    UcsOrthographic: OrthographicView
    UcsBase: ObjectId
    Ucsname: ObjectId
    Ucs: CoordinateSystem3d
    Ucsydir: Vector3d
    Ucsxdir: Vector3d
    Ucsorg: Point3d
    Elevation: float
    Limmax: Point2d
    Limmin: Point2d
    Extmax: Point3d
    Extmin: Point3d
    Insbase: Point3d
    PucsOrthographic: OrthographicView
    PucsBase: ObjectId
    Pucsname: ObjectId
    Pucs: CoordinateSystem3d
    Pucsydir: Vector3d
    Pucsxdir: Vector3d
    Pucsorg: Point3d
    Pelevation: float
    Plimmax: Point2d
    Plimmin: Point2d
    Pextmax: Point3d
    Pextmin: Point3d
    Pinsbase: Point3d
    Celtscale: float
    Cmlscale: float
    Cmljust: int
    CmlstyleID: ObjectId
    Interferecolor: Color
    Interferevpvs: ObjectId
    Interfereobjvs: ObjectId
    DetailViewStyle: ObjectId
    SectionViewStyle: ObjectId
    MLeaderscale: float
    MLeaderstyle: ObjectId
    Tablestyle: ObjectId
    Dimstyle: ObjectId
    Celtype: ObjectId
    Textstyle: ObjectId
    PlotStyleNameId: PlotStyleDescriptor
    Handseed: Handle
    Cetransparency: Transparency
    Cecolor: Color
    Tdusrtimer: TimeSpan
    Tdindwg: TimeSpan
    Tduupdate: DateTime
    Tducreate: DateTime
    Tdupdate: DateTime
    Tdcreate: DateTime
    HpOrigin: Point2d
    HpInherit: bool
    Menu: str
    Facetres: float
    Chamferd: float
    Chamferc: float
    Chamferb: float
    Chamfera: float
    Userr5: float
    Userr4: float
    Userr3: float
    Userr2: float
    Userr1: float
    Plinewid: float
    Pdsize: float
    Angbase: float
    OleStartUp: bool
    XrefEditEnabled: bool
    LineWeightDisplay: bool
    JoinStyle: JoinStyle
    EndCaps: EndCap
    Celweight: LineWeight
    Thickness: float
    Filletrad: float
    Sketchinc: float
    Tracewid: float
    Textsize: float
    Ltscale: float
    Isolines: int
    Maxactvp: int
    Unitmode: int
    Measurement: MeasurementValue
    Shadedif: int
    Shadedge: int
    Splinetype: int
    Surftab2: int
    Surftab1: int
    Surftype: int
    Surfv: int
    Surfu: int
    Splinesegs: int
    Useri5: int
    Useri4: int
    Useri3: int
    Useri2: int
    Useri1: int
    Pdmode: int
    Attmode: int
    Auprec: int
    Aunits: int
    Luprec: int
    Lunits: int
    Treedepth: int
    Visretain: bool
    Plimcheck: bool
    Worldview: bool
    Mirrtext: bool
    XclipFrame: int
    Splframe: bool
    Angdir: bool
    Skpoly: bool
    Usrtimer: bool
    PlineEllipse: bool
    DispSilh: bool
    Saveproxygraphics: int
    Limcheck: bool
    Psltscale: bool
    Qtextmode: bool
    Fillmode: bool
    Regenmode: bool
    Orthomode: bool
    Plinegen: bool
    Dimsho: bool
    Dimaso: bool
    SecurityParameters: SecurityParameters
    IsEmr: bool
    RetainOriginalThumbnailBitmap: bool
    ThumbnailBitmap: Bitmap
    XrefBlockId: ObjectId
    MaintenanceReleaseVersion: int
    UndoRecording: bool
    OriginalFileSavedByMaintenanceVersion: MaintenanceReleaseVersion
    OriginalFileMaintenanceVersion: MaintenanceReleaseVersion
    LastSavedAsMaintenanceVersion: MaintenanceReleaseVersion
    OriginalFileSavedByVersion: DwgVersion
    OriginalFileVersion: DwgVersion
    LastSavedAsVersion: DwgVersion
    OriginalFileName: str
    NumberOfSaves: int
    ApproxNumObjects: int
    NeedsRecovery: bool
    DataLinkManager: DataLinkManager
    DataLinkDictionaryId: ObjectId
    SectionManagerId: ObjectId
    DetailViewStyleDictionaryId: ObjectId
    SectionViewStyleDictionaryId: ObjectId
    MLeaderStyleDictionaryId: ObjectId
    TableStyleDictionaryId: ObjectId
    CurrentSpaceId: ObjectId
    PaperSpaceVportId: ObjectId
    ByBlockLinetype: ObjectId
    ByLayerLinetype: ObjectId
    ContinuousLinetype: ObjectId
    LayerZero: ObjectId
    PlotSettingsDictionaryId: ObjectId
    NamedObjectsDictionaryId: ObjectId
    ColorDictionaryId: ObjectId
    VisualStyleDictionaryId: ObjectId
    MaterialDictionaryId: ObjectId
    PlotStyleNameDictionaryId: ObjectId
    LayoutDictionaryId: ObjectId
    GroupDictionaryId: ObjectId
    MLStyleDictionaryId: ObjectId
    DimStyleTableId: ObjectId
    RegAppTableId: ObjectId
    ViewportTableId: ObjectId
    UcsTableId: ObjectId
    ViewTableId: ObjectId
    TextStyleTableId: ObjectId
    BlockTableId: ObjectId
    Clayer: ObjectId
    TileMode: bool
    ObjectContextManager: ObjectContextManager
    LayerStateManager: LayerStateManager
    TransactionManager: TransactionManager
    LinetypeTableId: ObjectId
    LayerTableId: ObjectId
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AbortDeepClone(self, idMap: IdMapping) -> None: ...
    def AddDBObject(self, appendIt: DBObject) -> ObjectId: ...
    def ApplyPartialOpenFilters(self, spatialFilter: SpatialFilter, layerFilter: LayerFilter) -> None: ...
    def AttachXref(self, fileName: str, blockName: str) -> ObjectId: ...
    def AuditXData(self, info: AuditInfo) -> None: ...
    def BindXrefs(self, xrefIds: ObjectIdCollection, insertBind: bool) -> None: ...
    def ClassDxfName(self, getMyDxfName: RXClass) -> str: ...
    def CloseInput(self, closeFile: bool) -> None: ...
    def CountEmptyObjects(self, flags: int) -> int: ...
    def CountHardReferences(self, ids: ObjectIdCollection, count: list) -> None: ...
    @staticmethod
    def DbFromId(id: int) -> Database: ...
    def DeepCloneObjects(self, identifiers: ObjectIdCollection, id: ObjectId, mapping: IdMapping, deferTranslation: bool) -> None: ...
    def DetachXref(self, xrefId: ObjectId) -> None: ...
    def DisablePartialOpen(self, ) -> None: ...
    def DisableUndoRecording(self, disable: bool) -> None: ...
    def DxfIn(self, fileName: str, logFilename: str) -> None: ...
    def DxfOut(self, fileName: str, precision: int, version: DwgVersion) -> None: ...
    def DxfOutEx(self, fileName: str, precision: int, version: DwgVersion, saveThumbnailImage: bool, nCodePage: int) -> None: ...
    @staticmethod
    def Equals(db1: Database, db2: Database) -> bool: ...
    def EraseEmptyObjects(self, flags: int) -> int: ...
    def EvaluateFields(self, context: FieldEvaluationContext, prop: str) -> FieldEvaluationResult: ...
    def ForceWblockDatabaseCopy(self, ) -> None: ...
    @staticmethod
    def FromAcadDatabase(acadDatabase: object) -> Database: ...
    @staticmethod
    def GetAllDatabases() -> List: ...
    def GetDimRecentStyleList(self, ) -> ObjectIdCollection: ...
    def GetDimensionStyleChildData(self, classDescriptor: RXClass) -> DimStyleTableRecord: ...
    def GetDimensionStyleChildId(self, classDescriptor: RXClass, parentStyle: ObjectId) -> ObjectId: ...
    def GetDimensionStyleParentId(self, childStyle: ObjectId) -> ObjectId: ...
    def GetDimstyleData(self, ) -> DimStyleTableRecord: ...
    def GetHashCode(self, ) -> int: ...
    def GetHostDwgXrefGraph(self, includeGhosts: bool) -> XrefGraph: ...
    def GetMetaObject(self, parameter: Expression) -> DynamicMetaObject: ...
    def GetNearestLineWeight(self, weight: int) -> LineWeight: ...
    def GetObjectId(self, createIfNotFound: bool, objHandle: Handle, identifier: int) -> ObjectId: ...
    def GetSupportedDxfOutVersions(self, ) -> list: ...
    def GetSupportedSaveVersions(self, ) -> list: ...
    def GetViewports(self, bGetPaperspaceVports: bool) -> ObjectIdCollection: ...
    def GetVisualStyleList(self, ) -> StringCollection: ...
    @staticmethod
    def IdFromDb(dataBase: Database) -> int: ...
    def Insert(self, sourceBlockName: str, destinationBlockName: str, dataBase: Database, preserveSourceDatabase: bool) -> ObjectId: ...
    @staticmethod
    def IsObjectNonPersistent(id: ObjectId) -> bool: ...
    def IsValidLineWeight(self, weight: int) -> bool: ...
    def LoadLineTypeFile(self, lineTypeName: str, filename: str) -> None: ...
    def LoadMlineStyleFile(self, mlineStyleName: str, fileName: str) -> None: ...
    @staticmethod
    def MarkObjectNonPersistent(id: ObjectId, value: bool) -> None: ...
    def OverlayXref(self, fileName: str, blockName: str) -> ObjectId: ...
    def Purge(self, idGraph: ObjectIdGraph) -> None: ...
    def ReadDwgFile(self, fileName: str, mode: FileOpenMode, allowCPConversion: bool, password: str) -> None: ...
    def ReclaimMemoryFromErasedObjects(self, ids: ObjectIdCollection) -> None: ...
    def ReloadXrefs(self, xrefIds: ObjectIdCollection) -> None: ...
    def ResetTimes(self, ) -> None: ...
    def ResolveXrefs(self, useThreadEngine: bool, doNewOnly: bool) -> None: ...
    def RestoreForwardingXrefSymbols(self, ) -> None: ...
    def RestoreOriginalXrefSymbols(self, ) -> None: ...
    def RuntimeId(self, ) -> int: ...
    def Save(self, ) -> None: ...
    def SaveAs(self, fileName: str, bBakAndRename: bool, version: DwgVersion, security: SecurityParameters) -> None: ...
    def SetDimstyleData(self, style: DimStyleTableRecord) -> None: ...
    def SetTimeZoneAsUtcOffset(self, offset: float) -> TimeZone: ...
    def SetWorldPaperspaceUcsBaseOrigin(self, origin: Point3d, orthoView: OrthographicView) -> None: ...
    def SetWorldUcsBaseOrigin(self, origin: Point3d, orthoView: OrthographicView) -> None: ...
    def TimeZoneDescription(self, tz: TimeZone) -> str: ...
    def TimeZoneOffset(self, tz: TimeZone) -> float: ...
    def TryGetObjectId(self, objHandle: Handle, id: ObjectId) -> bool: ...
    def UnloadXrefs(self, xrefIds: ObjectIdCollection) -> None: ...
    def UpdateExt(self, doBestFit: bool) -> None: ...
    def Wblock(self, outputDataBase: Database, outObjIds: ObjectIdCollection, basePoint: Point3d, cloning: DuplicateRecordCloning) -> None: ...
    def WblockCloneObjects(self, identifiers: ObjectIdCollection, id: ObjectId, mapping: IdMapping, cloning: DuplicateRecordCloning, deferTranslation: bool) -> None: ...
    def WorldPaperspaceUcsBaseOrigin(self, orthoView: OrthographicView) -> Point3d: ...
    def WorldUcsBaseOrigin(self, orthoView: OrthographicView) -> Point3d: ...
    def XBindXrefs(self, xrefSymbolIds: ObjectIdCollection, insertBind: bool) -> None: ...

class DatabaseIOEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DatabaseIOEventArgs"""
    def __init__(self, *args) -> None: ...
    FileName: str

class DatabaseIOEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.DatabaseIOEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: DatabaseIOEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: DatabaseIOEventArgs) -> None: ...

class DatabaseSummaryInfo:
    """.NET: Autodesk.AutoCAD.DatabaseServices.DatabaseSummaryInfo"""
    def __init__(self, *args) -> None: ...
    CustomProperties: IDictionaryEnumerator
    HyperlinkBase: str
    RevisionNumber: str
    LastSavedBy: str
    Comments: str
    Keywords: str
    Author: str
    Subject: str
    Title: str
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class DatabaseSummaryInfoBuilder:
    """.NET: Autodesk.AutoCAD.DatabaseServices.DatabaseSummaryInfoBuilder"""
    def __init__(self, *args) -> None: ...
    CustomPropertyTable: IDictionary
    CustomProperties: StringDictionary
    HyperlinkBase: str
    RevisionNumber: str
    LastSavedBy: str
    Comments: str
    Keywords: str
    Author: str
    Subject: str
    Title: str
    def ToDatabaseSummaryInfo(self, ) -> DatabaseSummaryInfo: ...

class DbDictionaryEnumerator(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DbDictionaryEnumerator"""
    def __init__(self, *args) -> None: ...
    Value: ObjectId
    Key: str
    Current: DBDictionaryEntry
    Entry: DBDictionaryEntry
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class DbHomeView(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DbHomeView"""
    def __init__(self, *args) -> None: ...
    Perspective: bool
    Height: float
    Width: float
    Up: Vector3d
    Center: Point3d
    Eye: Point3d
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Clone(self, ) -> object: ...
    def Equals(self, obj: object) -> bool: ...
    def ToggleDefaultSettings(self, ) -> None: ...

class DecomposeForSaveReplacementRecord:
    """.NET: Autodesk.AutoCAD.DatabaseServices.DecomposeForSaveReplacementRecord"""
    def __init__(self, *args) -> None: ...
    ExchangeXData: bool
    ReplacementId: ObjectId
    ReplacementObject: DBObject

class DeepCloneType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.DeepCloneType"""
    def __init__(self, *args) -> None: ...
    Copy: int  # = 0
    Explode: int  # = 1
    Block: int  # = 2
    XrefBind: int  # = 3
    SymbolTableMerge: int  # = 4
    Insert: int  # = 6
    Wblock: int  # = 7
    Objects: int  # = 8
    XrefInsert: int  # = 9
    InsertCopy: int  # = 10
    WblockObjects: int  # = 11
class DefaultLightingType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.DefaultLightingType"""
    def __init__(self, *args) -> None: ...
    OneDistantLight: int  # = 0
    TwoDistantLights: int  # = 1
class DetailSymbol(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DetailSymbol"""
    def __init__(self, *args) -> None: ...
    IdentifierPosition: Point3d
    ModelEdgeDirection: Vector3d
    ModelEdgeOrigin: Point3d
    BoundarySize: Vector2d
    Direction: Vector3d
    Origin: Point3d
    DetailViewScale: float
    OwningViewScale: float
    DisplayIdentifier: bool
    ModelEdgeType: DetailViewModelEdge
    BoundaryType: DetailSymbolBoundaryType
    Identifier: str
    Scale: float
    SymbolStyleId: ObjectId
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def IsOverriddenProperty(self, propertyToCheck: DetailSymbolOverriddenProperty) -> bool: ...

class DetailSymbolBoundaryType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.DetailSymbolBoundaryType"""
    def __init__(self, *args) -> None: ...
    CircularBoundary: int  # = 0
    RectangularBoundary: int  # = 1
    CustomBoundary: int  # = 2
class DetailSymbolOverriddenProperty:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.DetailSymbolOverriddenProperty"""
    def __init__(self, *args) -> None: ...
    ModelEdge: int  # = 1
    IdentifierPosition: int  # = 2
class DetailViewIdentifierPlacement:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.DetailViewIdentifierPlacement"""
    def __init__(self, *args) -> None: ...
    OutsideBoundary: int  # = 0
    OutsideBoundaryWithLeader: int  # = 1
    OnBoundary: int  # = 2
    OnBoundaryWithLeader: int  # = 3
class DetailViewModelEdge:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.DetailViewModelEdge"""
    def __init__(self, *args) -> None: ...
    Smooth: int  # = 0
    SmoothWithBorder: int  # = 1
    SmoothWithConnectionLine: int  # = 2
    Jagged: int  # = 3
class DetailViewStyle(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DetailViewStyle"""
    def __init__(self, *args) -> None: ...
    BorderLineTypeId: ObjectId
    BorderLineColor: Color
    BorderLineWeight: LineWeight
    ModelEdge: DetailViewModelEdge
    ShowViewLabel: bool
    ViewLabelPattern: str
    ViewLabelAlignment: ModelDocViewLabelAlignmentType
    ViewLabelAttachment: ModelDocViewLabelAttachmentPoint
    ViewLabelOffset: float
    ViewLabelTextHeight: float
    ViewLabelTextColor: Color
    ViewLabelTextStyleId: ObjectId
    ConnectionLineTypeId: ObjectId
    ConnectionLineColor: Color
    ConnectionLineWeight: LineWeight
    BoundaryLineTypeId: ObjectId
    BoundaryLineColor: Color
    BoundaryLineWeight: LineWeight
    ShowArrowheads: bool
    ArrowSymbolSize: float
    ArrowSymbolColor: Color
    ArrowSymbolId: ObjectId
    IdentifierPlacement: DetailViewIdentifierPlacement
    IdentifierOffset: float
    IdentifierHeight: float
    IdentifierColor: Color
    IdentifierStyleId: ObjectId
    IsModifiedForRecompute: bool
    Description: str
    Name: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def DefaultViewName(self, index: int) -> str: ...
    def GetViewLabelPattern(self, field: Field) -> str: ...
    def PostViewStyleToDb(self, dataBasePointer: Database, styleName: str) -> ObjectId: ...
    def SetDatabaseDefaults(self, dataBasePointer: Database) -> None: ...
    def SetViewLabelPattern(self, pattern: str, field: Field) -> None: ...
    def ValidateViewName(self, name: str) -> bool: ...

class DgnDefinition(UnderlayDefinition):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DgnDefinition"""
    def __init__(self, *args) -> None: ...
    SetShowRasterRef: bool
    ShowRasterRef: bool
    XrefDepth: int
    UseMasterUnits: bool
    Loaded: bool
    UnderlayItem: UnderlayItem
    ItemName: str
    ActiveFileName: str
    SourceFileName: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class DgnReference(UnderlayReference):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DgnReference"""
    def __init__(self, *args) -> None: ...
    IsClipInverted: bool
    Path: str
    NameOfSheet: str
    Name: str
    Width: float
    Height: float
    AdjustColorForBackground: bool
    UnderlayLayerCollection: UnderlayLayerCollection
    Monochrome: bool
    Fade: int
    Contrast: int
    IsOn: bool
    IsClipped: bool
    Transform: Matrix3d
    DefinitionId: ObjectId
    Normal: Vector3d
    Rotation: float
    ScaleFactors: Scale3d
    Position: Point3d
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class DgnUnderlayItem(UnderlayItem):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DgnUnderlayItem"""
    def __init__(self, *args) -> None: ...
    SetShowRasterRef: bool
    ShowRasterRef: bool
    UseMasterUnits: bool
    UsingPartialContent: bool
    Thumbnail: Bitmap
    Units: UnitsValue
    Extents: Extents2d
    Name: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class DiametricDimension(Dimension):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DiametricDimension"""
    def __init__(self, *args) -> None: ...
    FarChordPoint: Point3d
    ChordPoint: Point3d
    LeaderLength: float
    Dimaltmzf: float
    Dimmzf: float
    Dimaltmzs: str
    Dimmzs: str
    Dimblk2: ObjectId
    Dimblk1: ObjectId
    Dimblk: ObjectId
    Dimpost: str
    Dimapost: str
    Dimzin: int
    Dimupt: bool
    Dimtzin: int
    Dimtxtdirection: bool
    Dimtxt: float
    TextStyleId: ObjectId
    Dimtvp: float
    Dimtsz: float
    Dimtp: float
    Dimtolj: int
    Dimtol: bool
    Dimtoh: bool
    Dimtofl: bool
    Dimtmove: int
    Dimtm: float
    Dimtix: bool
    Dimtih: bool
    Dimtfillclr: Color
    Dimtfill: int
    Dimtfac: float
    Dimtdec: int
    Dimtad: int
    Dimsoxd: bool
    Dimse2: bool
    Dimse1: bool
    Dimsd2: bool
    Dimsd1: bool
    Dimscale: float
    Dimsah: bool
    Dimrnd: float
    DimensionStyleName: str
    CenterMarkSize: float
    CenterMarkType: DimensionCenterMarkType
    ToleranceSuppressZeroInches: bool
    ToleranceSuppressZeroFeet: bool
    ToleranceSuppressTrailingZeros: bool
    ToleranceSuppressLeadingZeros: bool
    AltToleranceSuppressZeroInches: bool
    AltToleranceSuppressZeroFeet: bool
    AltToleranceSuppressTrailingZeros: bool
    AltToleranceSuppressLeadingZeros: bool
    AltSuppressZeroInches: bool
    AltSuppressZeroFeet: bool
    AltSuppressTrailingZeros: bool
    AltSuppressLeadingZeros: bool
    AlternateSuffix: str
    AlternatePrefix: str
    SuppressZeroInches: bool
    SuppressZeroFeet: bool
    SuppressTrailingZeros: bool
    SuppressLeadingZeros: bool
    SuppressAngularTrailingZeros: bool
    SuppressAngularLeadingZeros: bool
    Suffix: str
    Prefix: str
    Dimlwe: LineWeight
    Dimlwd: LineWeight
    Dimlunit: int
    Dimltype: ObjectId
    Dimltex2: ObjectId
    Dimltex1: ObjectId
    Dimlim: bool
    Dimlfac: float
    Dimldrblk: ObjectId
    Dimjust: int
    Dimjogang: float
    Dimgap: float
    Dimfxlen: float
    DimfxlenOn: bool
    Dimfrac: int
    Dimexo: float
    Dimexe: float
    Dimdsep: str
    Dimdli: float
    Dimdle: float
    Dimdec: int
    Dimclrt: Color
    Dimclre: Color
    Dimclrd: Color
    Dimcen: float
    Dimazin: int
    Dimaunit: int
    Dimatfit: int
    Dimasz: float
    Dimarcsym: int
    Dimaltz: int
    Dimaltu: int
    Dimalttz: int
    Dimalttd: int
    Dimaltrnd: float
    Dimaltf: float
    Dimaltd: int
    Dimalt: bool
    Dimadec: int
    DynamicDimension: bool
    Measurement: float
    DimBlockPosition: Point3d
    DimBlockId: ObjectId
    HorizontalRotation: float
    TextLineSpacingFactor: float
    TextLineSpacingStyle: LineSpacingStyle
    TextAttachment: AttachmentPoint
    DimensionStyle: ObjectId
    TextRotation: float
    DimensionText: str
    Elevation: float
    Normal: Vector3d
    UsingDefaultTextPosition: bool
    TextPosition: Point3d
    TextDefinedSize: Vector2d
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class DictionaryWithDefaultDictionary(DBDictionary):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DictionaryWithDefaultDictionary"""
    def __init__(self, *args) -> None: ...
    ObjectBirthVersion: FullDwgVersion
    DefaultId: ObjectId
    IncludingErased: DBDictionary
    Item: object
    Count: int
    MergeStyle: DuplicateRecordCloning
    TreatElementsAsHard: bool
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class DimArrowFlag:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.DimArrowFlag"""
    def __init__(self, *args) -> None: ...
    FirstArrow: int  # = 0
    SecondArrow: int  # = 1
class DimStyleTable(SymbolTable):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DimStyleTable"""
    def __init__(self, *args) -> None: ...
    IncludingErased: SymbolTable
    Item: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class DimStyleTableRecord(SymbolTableRecord):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DimStyleTableRecord"""
    def __init__(self, *args) -> None: ...
    Dimblk2: ObjectId
    Dimblk1: ObjectId
    Dimblk: ObjectId
    Dimfxlen: float
    DimfxlenOn: bool
    Dimpost: str
    Dimapost: str
    Dimzin: int
    Dimupt: bool
    Dimtzin: int
    Dimtxtdirection: bool
    Dimtxt: float
    Dimtxsty: ObjectId
    Dimtvp: float
    Dimtsz: float
    Dimtp: float
    Dimtolj: int
    Dimtol: bool
    Dimtoh: bool
    Dimtofl: bool
    Dimtmove: int
    Dimtm: float
    Dimtix: bool
    Dimtih: bool
    Dimtfillclr: Color
    Dimtfill: int
    Dimtfac: float
    Dimtdec: int
    Dimtad: int
    Dimsoxd: bool
    Dimse2: bool
    Dimse1: bool
    Dimsd2: bool
    Dimsd1: bool
    Dimscale: float
    Dimsah: bool
    Dimrnd: float
    Dimlwe: LineWeight
    Dimlwd: LineWeight
    Dimlunit: int
    Dimltype: ObjectId
    Dimltex2: ObjectId
    Dimltex1: ObjectId
    Dimlim: bool
    Dimlfac: float
    Dimldrblk: ObjectId
    Dimjust: int
    Dimjogang: float
    Dimgap: float
    Dimfrac: int
    Dimexo: float
    Dimexe: float
    Dimdsep: str
    Dimdli: float
    Dimdle: float
    Dimdec: int
    Dimclrt: Color
    Dimclre: Color
    Dimclrd: Color
    Dimcen: float
    Dimazin: int
    Dimaunit: int
    Dimatfit: int
    Dimasz: float
    Dimarcsym: int
    Dimaltz: int
    Dimaltu: int
    Dimalttz: int
    Dimalttd: int
    Dimaltrnd: float
    Dimaltf: float
    Dimaltd: int
    Dimalt: bool
    Dimadec: int
    IsModifiedForRecompute: bool
    IsResolved: bool
    IsDependent: bool
    Name: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetArrowId(self, whichArrow: DimArrowFlag) -> ObjectId: ...

class Dimension(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Dimension"""
    def __init__(self, *args) -> None: ...
    Dimaltmzf: float
    Dimmzf: float
    Dimaltmzs: str
    Dimmzs: str
    Dimblk2: ObjectId
    Dimblk1: ObjectId
    Dimblk: ObjectId
    Dimpost: str
    Dimapost: str
    Dimzin: int
    Dimupt: bool
    Dimtzin: int
    Dimtxtdirection: bool
    Dimtxt: float
    TextStyleId: ObjectId
    Dimtvp: float
    Dimtsz: float
    Dimtp: float
    Dimtolj: int
    Dimtol: bool
    Dimtoh: bool
    Dimtofl: bool
    Dimtmove: int
    Dimtm: float
    Dimtix: bool
    Dimtih: bool
    Dimtfillclr: Color
    Dimtfill: int
    Dimtfac: float
    Dimtdec: int
    Dimtad: int
    Dimsoxd: bool
    Dimse2: bool
    Dimse1: bool
    Dimsd2: bool
    Dimsd1: bool
    Dimscale: float
    Dimsah: bool
    Dimrnd: float
    DimensionStyleName: str
    CenterMarkSize: float
    CenterMarkType: DimensionCenterMarkType
    ToleranceSuppressZeroInches: bool
    ToleranceSuppressZeroFeet: bool
    ToleranceSuppressTrailingZeros: bool
    ToleranceSuppressLeadingZeros: bool
    AltToleranceSuppressZeroInches: bool
    AltToleranceSuppressZeroFeet: bool
    AltToleranceSuppressTrailingZeros: bool
    AltToleranceSuppressLeadingZeros: bool
    AltSuppressZeroInches: bool
    AltSuppressZeroFeet: bool
    AltSuppressTrailingZeros: bool
    AltSuppressLeadingZeros: bool
    AlternateSuffix: str
    AlternatePrefix: str
    SuppressZeroInches: bool
    SuppressZeroFeet: bool
    SuppressTrailingZeros: bool
    SuppressLeadingZeros: bool
    SuppressAngularTrailingZeros: bool
    SuppressAngularLeadingZeros: bool
    Suffix: str
    Prefix: str
    Dimlwe: LineWeight
    Dimlwd: LineWeight
    Dimlunit: int
    Dimltype: ObjectId
    Dimltex2: ObjectId
    Dimltex1: ObjectId
    Dimlim: bool
    Dimlfac: float
    Dimldrblk: ObjectId
    Dimjust: int
    Dimjogang: float
    Dimgap: float
    Dimfxlen: float
    DimfxlenOn: bool
    Dimfrac: int
    Dimexo: float
    Dimexe: float
    Dimdsep: str
    Dimdli: float
    Dimdle: float
    Dimdec: int
    Dimclrt: Color
    Dimclre: Color
    Dimclrd: Color
    Dimcen: float
    Dimazin: int
    Dimaunit: int
    Dimatfit: int
    Dimasz: float
    Dimarcsym: int
    Dimaltz: int
    Dimaltu: int
    Dimalttz: int
    Dimalttd: int
    Dimaltrnd: float
    Dimaltf: float
    Dimaltd: int
    Dimalt: bool
    Dimadec: int
    DynamicDimension: bool
    Measurement: float
    DimBlockPosition: Point3d
    DimBlockId: ObjectId
    HorizontalRotation: float
    TextLineSpacingFactor: float
    TextLineSpacingStyle: LineSpacingStyle
    TextAttachment: AttachmentPoint
    DimensionStyle: ObjectId
    TextRotation: float
    DimensionText: str
    Elevation: float
    Normal: Vector3d
    UsingDefaultTextPosition: bool
    TextPosition: Point3d
    TextDefinedSize: Vector2d
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def FieldFromMText(self, dimMText: MText) -> None: ...
    def FieldToMText(self, dimMText: MText) -> None: ...
    def FormatMeasurement(self, measurement: float, dimensionText: str) -> str: ...
    def GenerateLayout(self, ) -> None: ...
    def GetDimstyleData(self, ) -> DimStyleTableRecord: ...
    def RecomputeDimensionBlock(self, forceUpdate: bool) -> None: ...
    def RemoveTextField(self, ) -> None: ...
    def ResetTextDefinedSize(self, ) -> None: ...
    def SetDimstyleData(self, style: DimStyleTableRecord) -> None: ...

class DimensionCenterMarkType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.DimensionCenterMarkType"""
    def __init__(self, *args) -> None: ...
    Mark: int  # = 0
    Line: int  # = 1
    None_: int  # = 2
class DimensionStyleOverrule(Overrule):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DimensionStyleOverrule"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def DimensionStyle(self, dimension: Dimension) -> ObjectId: ...
    def GetDimstyleData(self, dimension: Dimension, style: DimStyleTableRecord) -> None: ...
    def SetCustomFilter(self, ) -> None: ...
    def SetDimensionStyle(self, dimension: Dimension, id: ObjectId) -> None: ...
    def SetDimstyleData(self, dimension: Dimension, dimstyleId: ObjectId) -> None: ...
    def SetExtensionDictionaryEntryFilter(self, entryName: str) -> None: ...
    def SetIdFilter(self, ids: list) -> None: ...
    def SetNoFilter(self, ) -> None: ...
    def SetXDataFilter(self, registeredApplicationName: str) -> None: ...

class DistanceConstraint(ExplicitConstraint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DistanceConstraint"""
    def __init__(self, *args) -> None: ...
    ConstrainedLineId: int
    Direction: Vector3d
    DirectionType: DistanceDirectionType
    MeasuredValue: float
    DimDependencyId: ObjectId
    ValueDependencyId: ObjectId
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class DragStatus:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.DragStatus"""
    def __init__(self, *args) -> None: ...
    DragStart: int  # = 0
    DragEnd: int  # = 1
    DragAbort: int  # = 2
class DrawLeaderOrderType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.DrawLeaderOrderType"""
    def __init__(self, *args) -> None: ...
    DrawLeaderHeadFirst: int  # = 0
    DrawLeaderTailFirst: int  # = 1
class DrawMLeaderOrderType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.DrawMLeaderOrderType"""
    def __init__(self, *args) -> None: ...
    DrawContentFirst: int  # = 0
    DrawLeaderFirst: int  # = 1
class DrawOrderTable(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DrawOrderTable"""
    def __init__(self, *args) -> None: ...
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def FirstEntityIsDrawnBeforeSecond(self, first: ObjectId, second: ObjectId) -> bool: ...
    def GetFullDrawOrder(self, honorSortEntitiesMask: int) -> ObjectIdCollection: ...
    def GetRelativeDrawOrder(self, honorSortEntitiesMask: int) -> ObjectIdCollection: ...
    def GetSortHandle(self, id: ObjectId) -> Handle: ...
    def MoveAbove(self, collection: ObjectIdCollection, target: ObjectId) -> None: ...
    def MoveBelow(self, collection: ObjectIdCollection, target: ObjectId) -> None: ...
    def MoveToBottom(self, collection: ObjectIdCollection) -> None: ...
    def MoveToTop(self, collection: ObjectIdCollection) -> None: ...
    def SetRelativeDrawOrder(self, collection: ObjectIdCollection) -> None: ...
    def SwapOrder(self, id1: ObjectId, id2: ObjectId) -> None: ...

class DuplicateRecordCloning:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.DuplicateRecordCloning"""
    def __init__(self, *args) -> None: ...
    NotApplicable: int  # = 0
    Ignore: int  # = 1
    Replace: int  # = 2
    RefMangleName: int  # = 3
    MangleName: int  # = 4
    UnmangleName: int  # = 5
class DwfDefinition(UnderlayDefinition):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DwfDefinition"""
    def __init__(self, *args) -> None: ...
    isDWFx: bool
    Loaded: bool
    UnderlayItem: UnderlayItem
    ItemName: str
    ActiveFileName: str
    SourceFileName: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class DwfReference(UnderlayReference):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DwfReference"""
    def __init__(self, *args) -> None: ...
    IsClipInverted: bool
    Path: str
    NameOfSheet: str
    Name: str
    Width: float
    Height: float
    AdjustColorForBackground: bool
    UnderlayLayerCollection: UnderlayLayerCollection
    Monochrome: bool
    Fade: int
    Contrast: int
    IsOn: bool
    IsClipped: bool
    Transform: Matrix3d
    DefinitionId: ObjectId
    Normal: Vector3d
    Rotation: float
    ScaleFactors: Scale3d
    Position: Point3d
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class DwgFiler(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DwgFiler"""
    def __init__(self, *args) -> None: ...
    Position: int
    ExtendedMinorVersion: MaintenanceReleaseVersion
    DwgVersion: FullDwgVersion
    FilerType: FilerType
    FilerStatus: ErrorStatus
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def ReadAddress(self, ) -> IntPtr: ...
    def ReadBinaryChunk(self, ) -> list: ...
    def ReadBoolean(self, ) -> bool: ...
    def ReadByte(self, ) -> int: ...
    def ReadBytes(self, value: list) -> None: ...
    def ReadDouble(self, ) -> float: ...
    def ReadHandle(self, ) -> Handle: ...
    def ReadHardOwnershipId(self, ) -> ObjectId: ...
    def ReadHardPointerId(self, ) -> ObjectId: ...
    def ReadInt16(self, ) -> int: ...
    def ReadInt32(self, ) -> int: ...
    def ReadInt64(self, ) -> int: ...
    def ReadPoint2d(self, ) -> Point2d: ...
    def ReadPoint3d(self, ) -> Point3d: ...
    def ReadScale3d(self, ) -> Scale3d: ...
    def ReadSoftOwnershipId(self, ) -> ObjectId: ...
    def ReadSoftPointerId(self, ) -> ObjectId: ...
    def ReadString(self, ) -> str: ...
    def ReadUInt16(self, ) -> int: ...
    def ReadUInt32(self, ) -> int: ...
    def ReadUInt64(self, ) -> int: ...
    def ReadVector2d(self, ) -> Vector2d: ...
    def ReadVector3d(self, ) -> Vector3d: ...
    def ResetFilerStatus(self, ) -> None: ...
    def Seek(self, offset: int, method: int) -> None: ...
    def WriteAddress(self, value: IntPtr) -> None: ...
    def WriteBinaryChunk(self, chunk: list) -> None: ...
    def WriteBoolean(self, value: bool) -> None: ...
    def WriteByte(self, value: int) -> None: ...
    def WriteBytes(self, value: list) -> None: ...
    def WriteDouble(self, value: float) -> None: ...
    def WriteHandle(self, handle: Handle) -> None: ...
    def WriteHardOwnershipId(self, value: ObjectId) -> None: ...
    def WriteHardPointerId(self, value: ObjectId) -> None: ...
    def WriteInt16(self, value: int) -> None: ...
    def WriteInt32(self, value: int) -> None: ...
    def WriteInt64(self, value: int) -> None: ...
    def WritePoint2d(self, value: Point2d) -> None: ...
    def WritePoint3d(self, value: Point3d) -> None: ...
    def WriteScale3d(self, value: Scale3d) -> None: ...
    def WriteSoftOwnershipId(self, value: ObjectId) -> None: ...
    def WriteSoftPointerId(self, value: ObjectId) -> None: ...
    def WriteString(self, value: str) -> None: ...
    def WriteUInt16(self, value: int) -> None: ...
    def WriteUInt32(self, value: int) -> None: ...
    def WriteUInt64(self, value: int) -> None: ...
    def WriteVector2d(self, value: Vector2d) -> None: ...
    def WriteVector3d(self, value: Vector3d) -> None: ...

class DwgVersion:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.DwgVersion"""
    def __init__(self, *args) -> None: ...
    MC0To0: int  # = 0
    AC1To2: int  # = 1
    AC1To40: int  # = 2
    AC1To50: int  # = 3
    AC2To20: int  # = 4
    AC2To10: int  # = 5
    AC2To21: int  # = 6
    AC2To22: int  # = 7
    AC1001: int  # = 8
    AC1002: int  # = 9
    AC1003: int  # = 10
    AC1004: int  # = 11
    AC1005: int  # = 12
    AC1006: int  # = 13
    AC1007: int  # = 14
    AC1008: int  # = 15
    AC1009: int  # = 16
    AC1010: int  # = 17
    AC1011: int  # = 18
    AC1012: int  # = 19
    AC1013: int  # = 20
    AC1014: int  # = 21
    AC1500: int  # = 22
    AC1015: int  # = 23
    AC1800a: int  # = 24
    AC1800: int  # = 25
    AC2100a: int  # = 26
    AC1021: int  # = 27
    AC2400a: int  # = 28
    AC1024: int  # = 29
    AC2700a: int  # = 30
    AC1027: int  # = 31
    AC3200a: int  # = 32
    AC1032: int  # = 33
    Current: int  # = 33
    Newest: int  # = 33
    Unknown: int  # = 254
    Max: int  # = 255
class DxfCode:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.DxfCode"""
    def __init__(self, *args) -> None: ...
    Start: int  # = 0
    Text: int  # = 1
    XRefPath: int  # = 1
    BlockName: int  # = 2
    ShapeName: int  # = 2
    SymbolTableRecordName: int  # = 2
    AttributeTag: int  # = 2
    SymbolTableName: int  # = 2
    MlineStyleName: int  # = 2
    DimPostString: int  # = 3
    Description: int  # = 3
    TextFontFile: int  # = 3
    LinetypeProse: int  # = 3
    DimStyleName: int  # = 3
    AttributePrompt: int  # = 3
    TextBigFontFile: int  # = 4
    CLShapeName: int  # = 4
    SymbolTableRecordComments: int  # = 4
    DimensionAlternativePrefixSuffix: int  # = 4
    Handle: int  # = 5
    DimensionBlock: int  # = 5
    DimBlk1: int  # = 6
    LinetypeName: int  # = 6
    DimBlk2: int  # = 7
    TextStyleName: int  # = 7
    LayerName: int  # = 8
    CLShapeText: int  # = 9
    XCoordinate: int  # = 10
    YCoordinate: int  # = 20
    ZCoordinate: int  # = 30
    Elevation: int  # = 38
    Thickness: int  # = 39
    TxtSize: int  # = 40
    ViewportHeight: int  # = 40
    Real: int  # = 40
    ViewportAspect: int  # = 41
    ViewWidth: int  # = 41
    TxtStyleXScale: int  # = 41
    TxtStylePSize: int  # = 42
    ViewLensLength: int  # = 42
    ViewFrontClip: int  # = 43
    ViewBackClip: int  # = 44
    ShapeXOffset: int  # = 44
    ShapeYOffset: int  # = 45
    ViewHeight: int  # = 45
    ShapeScale: int  # = 46
    PixelScale: int  # = 47
    LinetypeScale: int  # = 48
    DashLength: int  # = 49
    MlineOffset: int  # = 49
    LinetypeElement: int  # = 49
    ViewportSnapAngle: int  # = 50
    Angle: int  # = 50
    ViewportTwist: int  # = 51
    Visibility: int  # = 60
    LayerLinetype: int  # = 61
    Color: int  # = 62
    HasSubentities: int  # = 66
    ViewportVisibility: int  # = 67
    ViewportActive: int  # = 68
    ViewportNumber: int  # = 69
    Int16: int  # = 70
    RegAppFlags: int  # = 71
    TxtStyleFlags: int  # = 71
    ViewMode: int  # = 71
    LinetypeAlign: int  # = 72
    CircleSides: int  # = 72
    ViewportZoom: int  # = 73
    LinetypePdc: int  # = 73
    ViewportIcon: int  # = 74
    ViewportSnap: int  # = 75
    ViewportGrid: int  # = 76
    ViewportSnapStyle: int  # = 77
    ViewportSnapPair: int  # = 78
    Int32: int  # = 90
    Subclass: int  # = 100
    EmbeddedObjectStart: int  # = 101
    ControlString: int  # = 102
    DimVarHandle: int  # = 105
    UcsOrg: int  # = 110
    UcsOrientationX: int  # = 111
    UcsOrientationY: int  # = 112
    XReal: int  # = 140
    ViewBrightness: int  # = 141
    ViewContrast: int  # = 142
    Int64: int  # = 160
    XInt16: int  # = 170
    NormalX: int  # = 210
    NormalY: int  # = 220
    NormalZ: int  # = 230
    XXInt16: int  # = 270
    Int8: int  # = 280
    RenderMode: int  # = 281
    Bool: int  # = 290
    XTextString: int  # = 300
    BinaryChunk: int  # = 310
    ArbitraryHandle: int  # = 320
    SoftPointerId: int  # = 330
    HardPointerId: int  # = 340
    SoftOwnershipId: int  # = 350
    HardOwnershipId: int  # = 360
    LineWeight: int  # = 370
    PlotStyleNameType: int  # = 380
    PlotStyleNameId: int  # = 390
    ExtendedInt16: int  # = 400
    LayoutName: int  # = 410
    ColorRgb: int  # = 420
    ColorName: int  # = 430
    Alpha: int  # = 440
    GradientObjType: int  # = 450
    GradientPatType: int  # = 451
    GradientTintType: int  # = 452
    GradientColCount: int  # = 453
    GradientAngle: int  # = 460
    GradientShift: int  # = 461
    GradientTintVal: int  # = 462
    GradientColVal: int  # = 463
    GradientName: int  # = 470
    Comment: int  # = 999
    ExtendedDataAsciiString: int  # = 1000
    ExtendedDataRegAppName: int  # = 1001
    ExtendedDataControlString: int  # = 1002
    ExtendedDataLayerName: int  # = 1003
    ExtendedDataBinaryChunk: int  # = 1004
    ExtendedDataHandle: int  # = 1005
    ExtendedDataXCoordinate: int  # = 1010
    ExtendedDataWorldXCoordinate: int  # = 1011
    ExtendedDataWorldXDisp: int  # = 1012
    ExtendedDataWorldXDir: int  # = 1013
    ExtendedDataYCoordinate: int  # = 1020
    ExtendedDataWorldYCoordinate: int  # = 1021
    ExtendedDataWorldYDisp: int  # = 1022
    ExtendedDataWorldYDir: int  # = 1023
    ExtendedDataZCoordinate: int  # = 1030
    ExtendedDataWorldZCoordinate: int  # = 1031
    ExtendedDataWorldZDisp: int  # = 1032
    ExtendedDataWorldZDir: int  # = 1033
    ExtendedDataReal: int  # = 1040
    ExtendedDataDist: int  # = 1041
    ExtendedDataScale: int  # = 1042
    ExtendedDataInteger16: int  # = 1070
    ExtendedDataInteger32: int  # = 1071
    Invalid: int  # = -9999
    XDictionary: int  # = -6
    PReactors: int  # = -5
    Operator: int  # = -4
    XDataStart: int  # = -3
    FirstEntityId: int  # = -2
    HeaderId: int  # = -2
    End: int  # = -1
class DxfFiler(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DxfFiler"""
    def __init__(self, *args) -> None: ...
    IsModifyingExistingObject: bool
    Thickness: float
    Elevation: float
    AtEmbeddedObjectStart: bool
    AtEndOfObject: bool
    AtExtendedData: bool
    AtEndOfFile: bool
    IncludesDefaultValues: bool
    Precision: int
    ExtendedMinorVersion: MaintenanceReleaseVersion
    DwgVersion: FullDwgVersion
    Database: Database
    FilerType: FilerType
    ErrorMessage: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AtSubclassData(self, value: str) -> bool: ...
    def FilerStatus(self, ) -> None: ...
    def HaltAtClassBoundaries(self, value: bool) -> None: ...
    def PushBackItem(self, ) -> None: ...
    def ReadResultBuffer(self, ) -> ResultBuffer: ...
    def ResetFilerStatus(self, ) -> None: ...
    def RewindFiler(self, ) -> int: ...
    def SetError(self, value: ErrorStatus, format: str, values: list) -> None: ...
    def WriteBool(self, opCode: DxfCode, value: bool) -> None: ...
    def WriteBoolean(self, opCode: DxfCode, value: bool) -> None: ...
    def WriteByte(self, opCode: DxfCode, value: int) -> None: ...
    def WriteBytes(self, opCode: DxfCode, chunk: list) -> None: ...
    def WriteDouble(self, opCode: DxfCode, value: float, precision: int) -> None: ...
    def WriteEmbeddedObjectStart(self, ) -> None: ...
    def WriteHandle(self, opCode: DxfCode, value: Handle) -> None: ...
    def WriteInt16(self, opCode: DxfCode, value: int) -> None: ...
    def WriteInt32(self, opCode: DxfCode, value: int) -> None: ...
    def WriteInt64(self, opCode: DxfCode, value: int) -> None: ...
    def WriteObjectId(self, opCode: DxfCode, value: ObjectId) -> None: ...
    def WritePoint2d(self, opCode: DxfCode, value: Point2d, precision: int) -> None: ...
    def WritePoint3d(self, opCode: DxfCode, value: Point3d, precision: int) -> None: ...
    def WriteResultBuffer(self, buffer: ResultBuffer) -> None: ...
    def WriteScale3d(self, opCode: DxfCode, value: Scale3d, precision: int) -> None: ...
    def WriteString(self, opCode: DxfCode, value: str) -> None: ...
    def WriteUInt16(self, opCode: DxfCode, value: int) -> None: ...
    def WriteUInt32(self, opCode: DxfCode, value: int) -> None: ...
    def WriteUInt64(self, opCode: DxfCode, value: int) -> None: ...
    def WriteVector2d(self, opCode: DxfCode, value: Vector2d, precision: int) -> None: ...
    def WriteVector3d(self, opCode: DxfCode, value: Vector3d, precision: int) -> None: ...
    def WriteXDataStart(self, ) -> None: ...

class DynamicBlockReferenceProperty:
    """.NET: Autodesk.AutoCAD.DatabaseServices.DynamicBlockReferenceProperty"""
    def __init__(self, *args) -> None: ...
    Value: object
    UnitsType: DynamicBlockReferencePropertyUnitsType
    Description: str
    VisibleInCurrentVisibilityState: bool
    Show: bool
    ReadOnly: bool
    PropertyTypeCode: int
    PropertyName: str
    BlockId: ObjectId
    def GetAllowedValues(self, ) -> list: ...

class DynamicBlockReferencePropertyCollection(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DynamicBlockReferencePropertyCollection"""
    def __init__(self, *args) -> None: ...
    Item: DynamicBlockReferenceProperty
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...

class DynamicBlockReferencePropertyCollectionEnumerator:
    """.NET: Autodesk.AutoCAD.DatabaseServices.DynamicBlockReferencePropertyCollectionEnumerator"""
    def __init__(self, *args) -> None: ...
    Current: object
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class DynamicBlockReferencePropertyUnitsType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.DynamicBlockReferencePropertyUnitsType"""
    def __init__(self, *args) -> None: ...
    NoUnits: int  # = 0
    Angular: int  # = 1
    Distance: int  # = 2
    Area: int  # = 3
class DynamicDimensionChangedEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DynamicDimensionChangedEventArgs"""
    def __init__(self, *args) -> None: ...
    Value: float
    Index: int

class DynamicDimensionData(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DynamicDimensionData"""
    def __init__(self, *args) -> None: ...
    ApplicationData: object
    HideIfValueIsZero: bool
    Visible: bool
    Editable: bool
    Focal: bool
    Dimension: Dimension
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(unmanagedPointer: IntPtr, autoDelete: bool) -> DynamicDimensionData: ...

class DynamicDimensionDataCollection(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.DynamicDimensionDataCollection"""
    def __init__(self, *args) -> None: ...
    Item: DynamicDimensionData
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, data: DynamicDimensionData) -> int: ...
    def Clear(self, ) -> None: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def RemoveAt(self, i: int) -> None: ...

class EdgeRef(SubentRef):
    """.NET: Autodesk.AutoCAD.DatabaseServices.EdgeRef"""
    def __init__(self, *args) -> None: ...
    Curve: Curve3d
    FaceSubentity: SubentityId
    SubentId: SubentityId
    Entity: CompoundObjectId
    IsEmpty: bool
    IsValid: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Ellipse(Curve):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Ellipse"""
    def __init__(self, *args) -> None: ...
    MinorRadius: float
    MajorRadius: float
    IsNull: bool
    EndParam: float
    StartParam: float
    EndAngle: float
    StartAngle: float
    RadiusRatio: float
    MinorAxis: Vector3d
    MajorAxis: Vector3d
    Normal: Vector3d
    Center: Point3d
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetAngleAtParameter(self, value: float) -> float: ...
    def GetParameterAtAngle(self, angle: float) -> float: ...
    def Set(self, center: Point3d, unitNormal: Vector3d, majorAxis: Vector3d, radiusRatio: float, startAngle: float, endAngle: float) -> None: ...

class EndCap:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.EndCap"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Round: int  # = 1
    Angle: int  # = 2
    Square: int  # = 3
class Entity(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Entity"""
    def __init__(self, *args) -> None: ...
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddSubentityPaths(self, subPaths: list) -> None: ...
    def BoundingBoxIntersectWith(self, entityPointer: Entity, intersectType: Intersect, projectionPlane: Plane, points: Point3dCollection, thisGraphicSystemMarker: IntPtr, otherGraphicSystemMarker: IntPtr) -> None: ...
    def DeleteSubentityPaths(self, subPaths: list) -> None: ...
    def Draw(self, ) -> None: ...
    def Explode(self, entitySet: DBObjectCollection) -> None: ...
    def GetGraphicsMarkersAtSubentityPathIntPtr(self, subPath: FullSubentityPath) -> IntPtrCollection: ...
    def GetGripPoints(self, grips: GripDataCollection, curViewUnitSize: float, gripSize: int, curViewDir: Vector3d, bitFlags: GetGripPointsFlags) -> bool: ...
    def GetGripPointsAtSubentityPath(self, subPath: FullSubentityPath, grips: GripDataCollection, curViewUnitSize: float, gripSize: int, curViewDir: Vector3d, bitFlags: GetGripPointsFlags) -> bool: ...
    def GetObjectSnapPoints(self, snapMode: ObjectSnapModes, gsSelectionMark: int, pickPoint: Point3d, lastPoint: Point3d, viewTransform: Matrix3d, snapPoints: Point3dCollection, geometryIds: IntegerCollection, insertionMat: Matrix3d) -> None: ...
    def GetPlane(self, ) -> Plane: ...
    def GetStretchPoints(self, stretchPoints: Point3dCollection) -> None: ...
    def GetSubentity(self, id: FullSubentityPath) -> Entity: ...
    def GetSubentityGeometricExtents(self, subPath: FullSubentityPath) -> Extents3d: ...
    def GetSubentityPathsAtGraphicsMarker(self, type: SubentityType, gsMark: int, pickPoint: Point3d, viewTransform: Matrix3d, numInserts: int, entityAndInsertStack: list) -> list: ...
    def GetTransformedCopy(self, transform: Matrix3d) -> Entity: ...
    def Highlight(self, subId: FullSubentityPath, highlightAll: bool) -> None: ...
    def HighlightState(self, subId: FullSubentityPath) -> HighlightStyle: ...
    def IntersectWith(self, entityPointer: Entity, intersectType: Intersect, projectionPlane: Plane, points: Point3dCollection, thisGraphicSystemMarker: IntPtr, otherGraphicSystemMarker: IntPtr) -> None: ...
    def IsContentSnappable(self, ) -> bool: ...
    def JoinEntities(self, otherEntities: list) -> IntegerCollection: ...
    def JoinEntity(self, secondaryEntity: Entity) -> None: ...
    def List(self, ) -> None: ...
    def MoveGripPointsAt(self, grips: GripDataCollection, offset: Vector3d, bitFlags: MoveGripPointsFlags) -> None: ...
    def MoveGripPointsAtSubentityPaths(self, subPaths: list, appData: list, offset: Vector3d, bitFlags: MoveGripPointsFlags) -> None: ...
    def MoveStretchPointsAt(self, indices: IntegerCollection, offset: Vector3d) -> None: ...
    def PopHighlight(self, subId: FullSubentityPath) -> None: ...
    def PushHighlight(self, subId: FullSubentityPath, highlightStyle: HighlightStyle) -> None: ...
    def RecordGraphicsModified(self, setModified: bool) -> None: ...
    def SaveAs(self, mode: WorldDraw, st: SaveType) -> None: ...
    def SetDatabaseDefaults(self, sourceDatabase: Database) -> None: ...
    def SetDragStatus(self, status: DragStatus) -> None: ...
    def SetGripStatus(self, status: GripStatus) -> None: ...
    def SetLayerId(self, newValue: ObjectId, allowHidden: bool) -> None: ...
    def SetPropertiesFrom(self, entityPointer: Entity) -> None: ...
    def SetSubentityGripStatus(self, status: GripStatus, subentity: FullSubentityPath) -> None: ...
    def TransformBy(self, transform: Matrix3d) -> None: ...
    def TransformSubentityPathsBy(self, subPaths: list, transform: Matrix3d) -> None: ...
    def Unhighlight(self, subId: FullSubentityPath, highlightAll: bool) -> None: ...

class EntityAlignmentEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.EntityAlignmentEventArgs"""
    def __init__(self, *args) -> None: ...
    Direction: Vector3d
    ClosestPoint: Point3d
    Normal: Vector3d
    PickPoint: Point3d
    Entity: Entity
    def GetPickedEntities(self, ) -> list: ...

class EntityAlignmentEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.EntityAlignmentEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: EntityAlignmentEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: EntityAlignmentEventArgs) -> None: ...

class EntityVisualStyleType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.EntityVisualStyleType"""
    def __init__(self, *args) -> None: ...
    FullVisualStyle: int  # = 0
    FaceVisualStyle: int  # = 1
    EdgeVisualStyle: int  # = 2
class EnumConverter(EnumConverter):
    """.NET: Autodesk.AutoCAD.DatabaseServices.EnumConverter"""
    def __init__(self, *args) -> None: ...
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool: ...
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object: ...
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object: ...

class EqualCurvatureConstraint(GeometricalConstraint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.EqualCurvatureConstraint"""
    def __init__(self, *args) -> None: ...
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class EqualDistanceConstraint(GeometricalConstraint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.EqualDistanceConstraint"""
    def __init__(self, *args) -> None: ...
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class EqualHelpParameterConstraint(GeometricalConstraint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.EqualHelpParameterConstraint"""
    def __init__(self, *args) -> None: ...
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetEqualHelpParameters(self, helpParameter1: HelpParameter, helpParameter2: HelpParameter) -> None: ...

class EqualLengthConstraint(GeometricalConstraint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.EqualLengthConstraint"""
    def __init__(self, *args) -> None: ...
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class EqualRadiusConstraint(GeometricalConstraint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.EqualRadiusConstraint"""
    def __init__(self, *args) -> None: ...
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class EraseFlags:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.EraseFlags"""
    def __init__(self, *args) -> None: ...
    ZeroLengthCurve: int  # = 1
    EmptyText: int  # = 2
    AllEmptyObj: int  # = -1
class ExplicitConstraint(GeometricalConstraint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ExplicitConstraint"""
    def __init__(self, *args) -> None: ...
    MeasuredValue: float
    DimDependencyId: ObjectId
    ValueDependencyId: ObjectId
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Extents2d:
    """.NET: Autodesk.AutoCAD.DatabaseServices.Extents2d"""
    def __init__(self, *args) -> None: ...
    MaxPoint: Point2d
    MinPoint: Point2d
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def IsEqualTo(self, a: Extents2d, tolerance: Tolerance) -> bool: ...
    def ToString(self, format: str, provider: IFormatProvider) -> str: ...

class Extents3d:
    """.NET: Autodesk.AutoCAD.DatabaseServices.Extents3d"""
    def __init__(self, *args) -> None: ...
    MaxPoint: Point3d
    MinPoint: Point3d
    def AddBlockExtents(self, pointerToBlockTableRecord: BlockTableRecord) -> None: ...
    def AddExtents(self, source: Extents3d) -> None: ...
    def AddPoint(self, pt: Point3d) -> None: ...
    def Equals(self, obj: object) -> bool: ...
    def ExpandBy(self, vector: Vector3d) -> None: ...
    def GetHashCode(self, ) -> int: ...
    def IsEqualTo(self, a: Extents3d, tolerance: Tolerance) -> bool: ...
    def Set(self, min: Point3d, max: Point3d) -> None: ...
    def ToString(self, format: str, provider: IFormatProvider) -> str: ...
    def TransformBy(self, mat: Matrix3d) -> None: ...

class ExtrudedSurface(Surface):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ExtrudedSurface"""
    def __init__(self, *args) -> None: ...
    TaperAngle: float
    SweepOptions: SweepOptions
    Height: float
    SweepVec: Vector3d
    SweepProfile: Profile3d
    SweepEntity: Entity
    GeometricExtents: Extents3d
    UsesGraphicsCache: bool
    Perimeter: float
    WireframeType: WireframeTypeEnum
    VIsoLineDensity: int
    UIsoLineDensity: int
    ModificationActionBodyIds: ObjectIdCollection
    CreationActionBodyId: ObjectId
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CreateExtrudedSurface(self, sweepEnt: Entity, directionVec: Vector3d, sweepOptions: SweepOptions) -> None: ...
    def SetExtrude(self, sweepVec: Vector3d, sweepOptions: SweepOptions) -> None: ...

class Face(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Face"""
    def __init__(self, *args) -> None: ...
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetVertexAt(self, value: int) -> Point3d: ...
    def IsEdgeVisibleAt(self, vertexIndex: int) -> bool: ...
    def MakeEdgeInvisibleAt(self, vertexIndex: int) -> None: ...
    def MakeEdgeVisibleAt(self, vertexIndex: int) -> None: ...
    def SetVertexAt(self, vertexIndex: int, vertexPosition: Point3d) -> None: ...

class FaceRecord(Vertex):
    """.NET: Autodesk.AutoCAD.DatabaseServices.FaceRecord"""
    def __init__(self, *args) -> None: ...
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetVertexAt(self, faceIndex: int) -> int: ...
    def IsEdgeVisibleAt(self, faceIndex: int) -> bool: ...
    def MakeEdgeInvisibleAt(self, faceIndex: int) -> None: ...
    def MakeEdgeVisibleAt(self, faceIndex: int) -> None: ...
    def SetVertexAt(self, faceIndex: int, vertexIndex: int) -> None: ...

class FaceRef(SubentRef):
    """.NET: Autodesk.AutoCAD.DatabaseServices.FaceRef"""
    def __init__(self, *args) -> None: ...
    SubentId: SubentityId
    Entity: CompoundObjectId
    IsEmpty: bool
    IsValid: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class FeatureControlFrame(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.FeatureControlFrame"""
    def __init__(self, *args) -> None: ...
    TextStyleName: str
    TextStyleId: ObjectId
    DimensionStyleName: str
    Dimtxt: float
    Dimtxsty: ObjectId
    Dimscale: float
    Dimgap: float
    Dimclrt: Color
    Dimclrd: Color
    DimensionStyle: ObjectId
    Direction: Vector3d
    Normal: Vector3d
    Location: Point3d
    Text: str
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetBoundingPoints(self, ) -> Point3dCollection: ...
    def GetBoundingPolyline(self, ) -> Point3dCollection: ...
    def GetDimstyleData(self, ) -> DimStyleTableRecord: ...
    def SetDimstyleData(self, style: DimStyleTableRecord) -> None: ...
    def SetOrientation(self, norm: Vector3d, dir: Vector3d) -> None: ...

class Field(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Field"""
    def __init__(self, *args) -> None: ...
    HyperLink: HyperLink
    Value: object
    DataType: DataType
    Format: str
    IsTextField: bool
    EvaluatorId: str
    FilingOption: FieldFilingOptions
    EvaluationOption: FieldEvaluationOptions
    EvaluationStatus: FieldEvaluationStatusResult
    State: FieldState
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def ConvertToTextField(self, ) -> None: ...
    def Evaluate(self, evaluationOptions: int, database: Database) -> None: ...
    @staticmethod
    def FindField(text: str, iSearchFrom: int, nStartPos: int, nEndPos: int) -> bool: ...
    def GetChildren(self, ) -> list: ...
    def GetChildrenIds(self, ) -> list: ...
    def GetData(self, key: str) -> object: ...
    def GetFieldCode(self, flags: FieldCodeFlags) -> str: ...
    def GetFieldCodeWithChildren(self, flags: FieldCodeFlags) -> FieldCodeWithChildren: ...
    def GetStringValue(self, ) -> str: ...
    def SetData(self, key: str, data: object, recursive: bool) -> None: ...
    def SetFieldCode(self, fieldCode: str) -> None: ...
    def SetFieldCodeWithChildren(self, flag: FieldCodeFlags, fieldCode: FieldCodeWithChildren) -> None: ...

class FieldCodeFlags:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.FieldCodeFlags"""
    def __init__(self, *args) -> None: ...
    FieldCode: int  # = 1
    EvaluatedText: int  # = 2
    EvaluatedChildren: int  # = 4
    ObjectReference: int  # = 8
    AddMarkers: int  # = 16
    EscapeBackslash: int  # = 32
    StripOptions: int  # = 64
    PreserveFields: int  # = 128
    TextField: int  # = 256
class FieldCodeWithChildren:
    """.NET: Autodesk.AutoCAD.DatabaseServices.FieldCodeWithChildren"""
    def __init__(self, *args) -> None: ...
    Children: list
    FieldCode: str
    def Add(self, i: int, field: Field) -> None: ...
    def Dispose(self, ) -> None: ...

class FieldEvaluationContext:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.FieldEvaluationContext"""
    def __init__(self, *args) -> None: ...
    Open: int  # = 1
    Save: int  # = 2
    Plot: int  # = 4
    Etransmit: int  # = 8
    Regen: int  # = 16
    Demand: int  # = 32
    Preview: int  # = 64
class FieldEvaluationOptions:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.FieldEvaluationOptions"""
    def __init__(self, *args) -> None: ...
    Disable: int  # = 0
    OnOpen: int  # = 1
    OnSave: int  # = 2
    OnPlot: int  # = 4
    OnEtransmit: int  # = 8
    OnRegen: int  # = 16
    OnDemand: int  # = 32
    Automatic: int  # = 63
class FieldEvaluationResult:
    """.NET: Autodesk.AutoCAD.DatabaseServices.FieldEvaluationResult"""
    def __init__(self, *args) -> None: ...
    Evaluated: int
    Found: int

class FieldEvaluationStatus:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.FieldEvaluationStatus"""
    def __init__(self, *args) -> None: ...
    NotYetEvaluated: int  # = 1
    Success: int  # = 2
    EvaluatorNotFound: int  # = 4
    SyntaxError: int  # = 8
    InvalidCode: int  # = 16
    InvalidContext: int  # = 32
    OtherError: int  # = 64
class FieldEvaluationStatusResult:
    """.NET: Autodesk.AutoCAD.DatabaseServices.FieldEvaluationStatusResult"""
    def __init__(self, *args) -> None: ...
    ErrorMessage: str
    ErrorCode: int
    Status: FieldEvaluationStatus

class FieldFilingOptions:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.FieldFilingOptions"""
    def __init__(self, *args) -> None: ...
    SkipFilingResult: int  # = 1
class FieldState:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.FieldState"""
    def __init__(self, *args) -> None: ...
    Initialized: int  # = 1
    Compiled: int  # = 2
    Modified: int  # = 4
    Evaluated: int  # = 8
    HasCache: int  # = 16
    HasFormattedString: int  # = 32
class FileOpenMode:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.FileOpenMode"""
    def __init__(self, *args) -> None: ...
    OpenForReadAndReadShare: int  # = 1
    OpenForReadAndWriteNoShare: int  # = 2
    OpenForReadAndAllShare: int  # = 3
    OpenTryForReadShare: int  # = 4
class FilerType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.FilerType"""
    def __init__(self, *args) -> None: ...
    FileFiler: int  # = 0
    CopyFiler: int  # = 1
    UndoFiler: int  # = 2
    BagFiler: int  # = 3
    IdTranslateFiler: int  # = 4
    PageFiler: int  # = 5
    DeepCloneFiler: int  # = 6
    IdFiler: int  # = 7
    PurgeFiler: int  # = 8
    WblockCloneFiler: int  # = 9
class FilletTrimMode:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.FilletTrimMode"""
    def __init__(self, *args) -> None: ...
    TrimNone: int  # = 0
    TrimStart: int  # = 1
    TrimSecond: int  # = 2
    TrimBoth: int  # = 3
class FindFileHint:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.FindFileHint"""
    def __init__(self, *args) -> None: ...
    Default: int  # = 0
    FontFile: int  # = 1
    CompiledShapeFile: int  # = 2
    TrueTypeFontFile: int  # = 3
    EmbeddedImageFile: int  # = 4
    XRefDrawing: int  # = 5
    PatternFile: int  # = 6
    ArxApplication: int  # = 7
    FontMapFile: int  # = 8
    UnderlayFile: int  # = 9
class FitData:
    """.NET: Autodesk.AutoCAD.DatabaseServices.FitData"""
    def __init__(self, *args) -> None: ...
    Periodic: bool
    KnotParam: KnotParameterizationEnum
    EndTangent: Vector3d
    StartTangent: Vector3d
    TangentsExist: bool
    FitTolerance: float
    Degree: int
    def Equals(self, obj: object) -> bool: ...
    def GetFitPoints(self, ) -> Point3dCollection: ...
    def GetHashCode(self, ) -> int: ...
    def IsEqualTo(self, other: FitData, tolerance: Tolerance) -> bool: ...

class FixedConstraint(GeometricalConstraint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.FixedConstraint"""
    def __init__(self, *args) -> None: ...
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class FlowDirection:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.FlowDirection"""
    def __init__(self, *args) -> None: ...
    NotSet: int  # = 0
    LeftToRight: int  # = 1
    RightToLeft: int  # = 2
    TopToBottom: int  # = 3
    BottomToTop: int  # = 4
    ByStyle: int  # = 5
class Font:
    """.NET: Autodesk.AutoCAD.DatabaseServices.Font"""
    def __init__(self, *args) -> None: ...
    IsTrueType: bool
    Name: str

class FormatOption:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.FormatOption"""
    def __init__(self, *args) -> None: ...
    FormatOptionNone: int  # = 0
    ForEditing: int  # = 1
    ForExpression: int  # = 2
    UseMaximumPrecision: int  # = 4
    IgnoreMtextFormat: int  # = 8
class FormattedTableData(LinkedTableData):
    """.NET: Autodesk.AutoCAD.DatabaseServices.FormattedTableData"""
    def __init__(self, *args) -> None: ...
    NumberOfRows: int
    NumberOfColumns: int
    Name: str
    IsEmpty: bool
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetAlignment(self, row: int, column: int) -> CellAlignment: ...
    def GetBackgroundColor(self, row: int, column: int) -> Color: ...
    def GetContentColor(self, row: int, column: int) -> Color: ...
    def GetGridColor(self, row: int, column: int, gridLinetype: GridLineType) -> Color: ...
    def GetGridLineWeight(self, row: int, column: int, gridLinetype: GridLineType) -> LineWeight: ...
    def GetGridLinetype(self, row: int, column: int, gridLinetype: GridLineType) -> ObjectId: ...
    def GetGridVisibility(self, row: int, column: int, gridLinetype: GridLineType) -> Visibility: ...
    def GetMargin(self, row: int, column: int, margin: CellMargins) -> float: ...
    def GetMergeRange(self, row: int, column: int) -> CellRange: ...
    def GetOverride(self, row: int, column: int, gridLinetype: GridLineType) -> GridProperties: ...
    def GetRotation(self, row: int, column: int) -> float: ...
    def GetScale(self, row: int, column: int) -> float: ...
    def GetTextHeight(self, row: int, column: int) -> float: ...
    def GetTextStyle(self, row: int, column: int) -> ObjectId: ...
    def IsFormatEditable(self, row: int, column: int) -> bool: ...
    def IsMerged(self, row: int, column: int) -> bool: ...
    def Merge(self, range: CellRange) -> None: ...
    def RemoveAllOverrides(self, row: int, column: int) -> None: ...
    def SetAlignment(self, row: int, column: int, value: CellAlignment) -> None: ...
    def SetBackgroundColor(self, row: int, column: int, value: Color) -> None: ...
    def SetContentColor(self, row: int, column: int, value: Color) -> None: ...
    def SetGridColor(self, row: int, column: int, gridLinetype: GridLineType, value: Color) -> None: ...
    def SetGridLineWeight(self, row: int, column: int, gridLinetype: GridLineType, value: LineWeight) -> None: ...
    def SetGridLinetype(self, row: int, column: int, gridLinetype: GridLineType, value: ObjectId) -> None: ...
    def SetGridVisibility(self, row: int, column: int, gridLinetype: GridLineType, value: Visibility) -> None: ...
    def SetMargin(self, row: int, column: int, margin: CellMargins, value: float) -> None: ...
    def SetOverride(self, row: int, column: int, gridLinetype: GridLineType, gridProperty: GridProperties) -> None: ...
    def SetRotation(self, row: int, column: int, value: float) -> None: ...
    def SetScale(self, row: int, column: int, value: float) -> None: ...
    def SetTextHeight(self, row: int, column: int, value: float) -> None: ...
    def SetTextStyle(self, row: int, column: int, value: ObjectId) -> None: ...
    def Unmerge(self, range: CellRange) -> None: ...

class FrameSetting:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.FrameSetting"""
    def __init__(self, *args) -> None: ...
    ImageFrameOff: int  # = 0
    ImageFrameAbove: int  # = 1
    ImageFrameBelow: int  # = 2
    ImageFrameOnNoPlot: int  # = 3
    ImageFrameInvalid: int  # = -1
class FullDwgVersion:
    """.NET: Autodesk.AutoCAD.DatabaseServices.FullDwgVersion"""
    def __init__(self, *args) -> None: ...
    MinorVersion: MaintenanceReleaseVersion
    MajorVersion: DwgVersion
    def Equals(self, other: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToString(self, ) -> str: ...

class FullSubentityPath:
    """.NET: Autodesk.AutoCAD.DatabaseServices.FullSubentityPath"""
    def __init__(self, *args) -> None: ...
    SubentId: SubentityId
    IsNull: bool
    Null: FullSubentityPath
    def CopyToUnmanagedObject(self, unmanagedPointer: IntPtr) -> None: ...
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def GetObjectIds(self, ) -> list: ...

class G2SmoothConstraint(CompositeConstraint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.G2SmoothConstraint"""
    def __init__(self, *args) -> None: ...
    OwnedConstraints: list
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class GeoCSProjectionCode:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.GeoCSProjectionCode"""
    def __init__(self, *args) -> None: ...
    Unknown: int  # = 0
    LL: int  # = 1
    Tm: int  # = 3
    Alber: int  # = 4
    OblqM: int  # = 5
    Mrcat: int  # = 6
    Azmed: int  # = 7
    Lmtan: int  # = 8
    Plycn: int  # = 9
    Modpc: int  # = 10
    Azmea: int  # = 11
    Edcnc: int  # = 12
    Miller: int  # = 13
    Mstero: int  # = 15
    Nzealand: int  # = 16
    Sinus: int  # = 17
    Ortho: int  # = 18
    Gnomonic: int  # = 19
    Edcyl: int  # = 20
    Vdgrntn: int  # = 21
    Cassini: int  # = 22
    Robinson: int  # = 23
    Bonne: int  # = 24
    Eckert4: int  # = 25
    Eckert6: int  # = 26
    Mollweid: int  # = 27
    Goode: int  # = 28
    Neacyl: int  # = 29
    Teacyl: int  # = 30
    Bipolar: int  # = 31
    Swiss: int  # = 32
    Pstro: int  # = 33
    Ostro: int  # = 34
    Sstro: int  # = 35
    Lm1sp: int  # = 36
    Lm2sp: int  # = 37
    Lmblg: int  # = 38
    Wccsl: int  # = 39
    Wccst: int  # = 40
    Mndotl: int  # = 41
    Mndott: int  # = 42
    Sotrm: int  # = 43
    Utm: int  # = 44
    Trmrs: int  # = 45
    GaussK: int  # = 46
    Krovak: int  # = 47
    MrcatK: int  # = 49
    Krvk95: int  # = 51
    Pstrosl: int  # = 53
    Trmeraf: int  # = 54
    Nerth: int  # = 55
    Obqcyl: int  # = 56
    Sys34: int  # = 57
    Ostn97: int  # = 58
    Azede: int  # = 59
    Ostn02: int  # = 60
    Sys34_99: int  # = 61
    Trmrkrg: int  # = 62
    Winkl: int  # = 63
    Nrthsrt: int  # = 64
    Lmbrtaf: int  # = 65
    Sys34_01: int  # = 66
    EdcylE: int  # = 67
    PlateCarree: int  # = 68
    PvMercator: int  # = 69
    Hom1uv: int  # = 1281
    Hom1xy: int  # = 1282
    Hom2uv: int  # = 1283
    Hom2xy: int  # = 1284
    Rskew: int  # = 1285
    Rskewc: int  # = 1286
    Rskewo: int  # = 1287
class GeoCSType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.GeoCSType"""
    def __init__(self, *args) -> None: ...
    Unknown: int  # = 0
    Arbitrary: int  # = 1
    Geographic: int  # = 2
    Projected: int  # = 3
class GeoCSUnit:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.GeoCSUnit"""
    def __init__(self, *args) -> None: ...
    Unknown: int  # = 0
    Meter: int  # = 1
    Foot: int  # = 2
    Inch: int  # = 3
    IFoot: int  # = 4
    ClarkeFoot: int  # = 5
    IInch: int  # = 6
    Centimeter: int  # = 7
    Kilometer: int  # = 8
    Yard: int  # = 9
    SearsYard: int  # = 10
    Mile: int  # = 11
    IYard: int  # = 12
    IMile: int  # = 13
    Knot: int  # = 14
    NautM: int  # = 15
    Lat66: int  # = 16
    Lat83: int  # = 17
    Decimeter: int  # = 18
    Millimeter: int  # = 19
    Dekameter: int  # = 20
    Hectometer: int  # = 21
    GermanMeter: int  # = 22
    CaGrid: int  # = 23
    ClarkeChain: int  # = 24
    GunterChain: int  # = 25
    BenoitChain: int  # = 26
    SearsChain: int  # = 27
    ClarkeLink: int  # = 28
    GunterLink: int  # = 29
    BenoitLink: int  # = 30
    SearsLink: int  # = 31
    Rod: int  # = 32
    Perch: int  # = 33
    Pole: int  # = 34
    Furlong: int  # = 35
    Rood: int  # = 36
    CapeRood: int  # = 37
    Brealey: int  # = 38
    SearsFoot: int  # = 39
    GoldCoastFoot: int  # = 40
    MicroInch: int  # = 41
    IndianYard: int  # = 42
    IndianFoot: int  # = 43
    IndianFt37: int  # = 44
    IndianFt62: int  # = 45
    IndianFt75: int  # = 46
    IndianYd37: int  # = 47
    Decameter: int  # = 48
    InternationalChain: int  # = 49
    InternationalLink: int  # = 50
    Degree: int  # = 1001
    Grad: int  # = 1002
    Grade: int  # = 1003
    MapInfo: int  # = 1004
    Mil: int  # = 1005
    Minute: int  # = 1006
    Radian: int  # = 1007
    Second: int  # = 1008
    Decisec: int  # = 1009
    Centisec: int  # = 1010
    Millisec: int  # = 1011
class GeoCoordinateCategory(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.GeoCoordinateCategory"""
    def __init__(self, *args) -> None: ...
    ID: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def CreateAll() -> list: ...
    def GetCoordinateAt(self, index: int) -> GeoCoordinateSystem: ...
    def NumOfCoordinate(self, ) -> int: ...

class GeoCoordinateSystem(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.GeoCoordinateSystem"""
    def __init__(self, *args) -> None: ...
    WktRepresentation: str
    XmlRepresentation: str
    GeodeticExtents: Extents2d
    CartesianExtents: Extents2d
    Offset: Vector2d
    Ellipsoid: GeoEllipsoid
    Datum: GeoDatum
    UnitScale: float
    GeoUnit: GeoCSUnit
    Unit: UnitsValue
    ProjectionCode: GeoCSProjectionCode
    Description: str
    Type: GeoCSType
    EPSGcode: int
    ID: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(coordSysIdOrFullDef: str) -> GeoCoordinateSystem: ...
    @staticmethod
    def CreateAll(coordCategory: GeoCoordinateCategory) -> list: ...
    def GetProjectionParamList(self, includeSpecialParams: bool) -> list: ...

class GeoCoordinateTransformer(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.GeoCoordinateTransformer"""
    def __init__(self, *args) -> None: ...
    TargetCSid: str
    SourceCSid: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(source: str, target: str) -> GeoCoordinateTransformer: ...
    @staticmethod
    def TransformPoint(source: str, target: str, sourcePt: Point3d) -> Point3d: ...
    @staticmethod
    def TransformPoints(source: str, target: str, sourcePts: Point3dCollection) -> Point3dCollection: ...

class GeoLocationData(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.GeoLocationData"""
    def __init__(self, *args) -> None: ...
    CoordinateProjectionRadius: float
    SeaLevelElevation: float
    DoSeaLevelCorrection: bool
    ScaleFactor: float
    ScaleEstimationMethod: ScaleEstimationMethod
    GeoRSSTag: str
    CoordinateSystem: str
    NumMeshPoints: int
    NorthDirectionVector: Vector2d
    NorthDirection: float
    UpDirection: Vector3d
    DesignPoint: Point3d
    VerticalUnitsScale: float
    HorizontalUnitsScale: float
    VerticalUnits: UnitsValue
    HorizontalUnits: UnitsValue
    ReferencePoint: Point3d
    TypeOfCoordinates: TypeOfCoordinates
    BlockTableRecordId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddMeshPointMap(self, index: int, sourcePt: Point2d, destPt: Point2d) -> None: ...
    def EraseFromDb(self, ) -> None: ...
    def GetMeshPointMap(self, index: int) -> MeshPointMap: ...
    def GetMeshPointMaps(self, ) -> MeshPointMaps: ...
    def PostToDb(self, ) -> ObjectId: ...
    def ResetMeshPointMaps(self, ) -> None: ...
    def SetMeshPointMaps(self, sourcePts: Point2dCollection, destPts: Point2dCollection) -> None: ...
    def TransformFromLonLatAlt(self, geoPt: Point3d) -> Point3d: ...
    def TransformToLonLatAlt(self, x: float, y: float, z: float) -> GeoDataLonLatAltInfo: ...
    def UpdateTransformationMatrix(self, ) -> None: ...

class GeoPositionMarker(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.GeoPositionMarker"""
    def __init__(self, *args) -> None: ...
    TextStyle: ObjectId
    Normal: Vector3d
    GeoPosition: Point3d
    Notes: str
    TextAlignmentType: TextAlignment
    EnableFrameText: bool
    MTextVisible: bool
    MText: MText
    Text: str
    LandingGap: float
    Radius: float
    Position: Point3d
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class GeomRef(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.GeomRef"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    IsValid: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Reset(self, ) -> None: ...

class GeomapImage(RasterImage):
    """.NET: Autodesk.AutoCAD.DatabaseServices.GeomapImage"""
    def __init__(self, *args) -> None: ...
    Fade: int
    Contrast: int
    Brightness: int
    IsOutOfDate: bool
    MapType: GeomapType
    LOD: int
    Resolution: GeomapResolution
    ImageWidth: float
    ImageHeight: float
    ImageBottomLeftPoint: Point3d
    Width: float
    Height: float
    BottomLeftPoint: Point3d
    ImageTransparency: bool
    ShowImage: bool
    Rotation: float
    Position: Point3d
    Path: str
    Name: str
    DisplayOptions: ImageDisplayOptions
    PixelToModelTransform: Matrix3d
    IsClipped: bool
    ClipBoundaryType: ClipBoundaryType
    Scale: Vector2d
    Orientation: CoordinateSystem3d
    ReactorId: ObjectId
    ImageDefId: ObjectId
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetImageVertices(self, ) -> Point3dCollection: ...
    def GetVertices(self, ) -> Point3dCollection: ...
    def ImageSize(self, ) -> Vector2d: ...
    def UpdateMapImage(self, Reset: bool) -> bool: ...

class GeometricalConstraint(ConstraintGroupNode):
    """.NET: Autodesk.AutoCAD.DatabaseServices.GeometricalConstraint"""
    def __init__(self, *args) -> None: ...
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Deactivate(self, ) -> None: ...
    def GetConnectedHelpParameterFor(self, consGeom: ConstrainedGeometry) -> HelpParameter: ...
    def Reactivate(self, ) -> None: ...

class GeometryOverrule(Overrule):
    """.NET: Autodesk.AutoCAD.DatabaseServices.GeometryOverrule"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetGeomExtents(self, entity: Entity) -> Extents3d: ...
    def IntersectWith(self, entity: Entity, ent: Entity, intType: Intersect, projPlane: Plane, points: Point3dCollection, thisGsMarker: IntPtr, otherGsMarker: IntPtr) -> None: ...
    def SetCustomFilter(self, ) -> None: ...
    def SetExtensionDictionaryEntryFilter(self, entryName: str) -> None: ...
    def SetIdFilter(self, ids: list) -> None: ...
    def SetNoFilter(self, ) -> None: ...
    def SetXDataFilter(self, registeredApplicationName: str) -> None: ...

class GetGripPointsFlags:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.GetGripPointsFlags"""
    def __init__(self, *args) -> None: ...
    GripPointsOnly: int  # = 1
    CyclableGripsOnly: int  # = 2
    DynamicDimensionMode: int  # = 4
class GradientBackground(Background):
    """.NET: Autodesk.AutoCAD.DatabaseServices.GradientBackground"""
    def __init__(self, *args) -> None: ...
    Rotation: float
    Height: float
    Horizon: float
    ColorBottom: EntityColor
    ColorMiddle: EntityColor
    ColorTop: EntityColor
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class GradientColor:
    """.NET: Autodesk.AutoCAD.DatabaseServices.GradientColor"""
    def __init__(self, *args) -> None: ...
    def get_Color(self, ) -> Color: ...
    def get_Value(self, ) -> float: ...

class GradientPatternType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.GradientPatternType"""
    def __init__(self, *args) -> None: ...
    PreDefinedGradient: int  # = 0
    UserDefinedGradient: int  # = 1
class Graph(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Graph"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    NumNodes: int
    RootNode: GraphNode
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddEdge(self, from_: GraphNode, toPointer: GraphNode) -> None: ...
    def AddNode(self, nodeToAdd: GraphNode) -> None: ...
    def BreakCycleEdge(self, from_: GraphNode, toPointer: GraphNode) -> None: ...
    def ClearAll(self, flags: int) -> None: ...
    @staticmethod
    def Create(unmanagedPointer: IntPtr, autoDelete: bool) -> Graph: ...
    def DelNode(self, nodeToDelete: GraphNode) -> None: ...
    def FindCycles(self, start: GraphNode) -> bool: ...
    def GetOutgoing(self, ) -> GraphNodeCollection: ...
    def Node(self, index: int) -> GraphNode: ...
    def Reset(self, ) -> None: ...
    def SetNodeGrowthRate(self, rate: int) -> None: ...

class GraphNode(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.GraphNode"""
    def __init__(self, *args) -> None: ...
    IsCycleNode: bool
    NumCycleIn: int
    NumCycleOut: int
    Owner: Graph
    NextCycleNode: GraphNode
    NumIn: int
    NumOut: int
    Data: IntPtr
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddRefTo(self, outGoingNode: GraphNode) -> None: ...
    def Clear(self, flags: int) -> None: ...
    @staticmethod
    def Create(unmanagedPointer: IntPtr, autoDelete: bool) -> GraphNode: ...
    def CycleIn(self, index: int) -> GraphNode: ...
    def CycleOut(self, index: int) -> GraphNode: ...
    def DisconnectAll(self, ) -> None: ...
    def In(self, index: int) -> GraphNode: ...
    def IsMarkedAs(self, flag: int) -> bool: ...
    def MarkAs(self, flags: int) -> None: ...
    def MarkTree(self, flags: int, appendedTo: GraphNodeCollection) -> None: ...
    def Out(self, index: int) -> GraphNode: ...
    def RemoveRefTo(self, nodeToRemoveReference: GraphNode) -> None: ...
    def SetEdgeGrowthRate(self, outEdgeRate: int, inEdgeRate: int) -> None: ...

class GraphNodeCollection(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.GraphNodeCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: GraphNode
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, value: GraphNode) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: GraphNode) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: GraphNode) -> int: ...
    def Insert(self, index: int, value: GraphNode) -> None: ...
    def Remove(self, value: GraphNode) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class GraphicsMetafileType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.GraphicsMetafileType"""
    def __init__(self, *args) -> None: ...
    NoMetafile: int  # = 0
    BoundingBox: int  # = 1
    FullGraphics: int  # = 2
class GridLineStyle:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.GridLineStyle"""
    def __init__(self, *args) -> None: ...
    Single: int  # = 1
    Double: int  # = 2
class GridLineType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.GridLineType"""
    def __init__(self, *args) -> None: ...
    InvalidGridLine: int  # = 0
    HorizontalTop: int  # = 1
    HorizontalInside: int  # = 2
    HorizontalBottom: int  # = 4
    HorizontalGridLines: int  # = 7
    VerticalLeft: int  # = 8
    VerticalInside: int  # = 16
    InnerGridLines: int  # = 18
    VerticalRight: int  # = 32
    OuterGridLines: int  # = 45
    VerticalGridLines: int  # = 56
    AllGridLines: int  # = 63
class GridProperties:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.GridProperties"""
    def __init__(self, *args) -> None: ...
    Invalid: int  # = 0
    LineStyle: int  # = 1
    LineWeight: int  # = 2
    Linetype: int  # = 4
    Color: int  # = 8
    Visibility: int  # = 16
    DoubleLineSpacing: int  # = 32
class GridPropertyParameter:
    """.NET: Autodesk.AutoCAD.DatabaseServices.GridPropertyParameter"""
    def __init__(self, *args) -> None: ...
    ...

class GripData(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.GripData"""
    def __init__(self, *args) -> None: ...
    IsPerViewport: bool
    GizmosEnabled: bool
    HotGripInvokesRightClick: bool
    ForcedPickOn: bool
    TriggerGrip: bool
    DrawAtDragImageGripPoint: bool
    ModeKeywordsDisabled: bool
    RubberBandLineDisabled: bool
    SkipWhenShared: bool
    AlternateBasePoint: Nullable
    GripPoint: Point3d
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetHotGripDimensionData(self, id: ObjectId, dimScale: float) -> DynamicDimensionDataCollection: ...
    def GetHoverDimensionData(self, id: ObjectId, dimScale: float) -> DynamicDimensionDataCollection: ...
    def GetTooltip(self, ) -> str: ...
    def OnGripStatusChanged(self, entityId: ObjectId, newStatus: Status) -> None: ...
    def OnHotGrip(self, entityId: ObjectId, contextFlags: Context) -> ReturnValue: ...
    def OnHover(self, entityId: ObjectId, contextFlags: Context) -> ReturnValue: ...
    def OnRightClick(self, hotGrips: GripDataCollection, entities: ObjectIdCollection) -> IEnumerable: ...
    def ViewportDraw(self, worldDraw: ViewportDraw, entityId: ObjectId, type: DrawType, imageGripPoint: Nullable, gripSizeInPixels: int) -> bool: ...
    def WorldDraw(self, worldDraw: WorldDraw, entityId: ObjectId, type: DrawType, imageGripPoint: Nullable, dGripSize: float) -> bool: ...

class GripDataCollection(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.GripDataCollection"""
    def __init__(self, *args) -> None: ...
    Item: GripData
    IsReadOnly: bool
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, gripData: GripData) -> None: ...
    def Clear(self, ) -> None: ...
    def Contains(self, gripData: GripData) -> bool: ...
    def CopyTo(self, A_0: list, A_1: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, gripData: GripData) -> bool: ...

class GripMode(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.GripMode"""
    def __init__(self, *args) -> None: ...
    CommandString: str
    Action: ActionType
    Cursor: CursorType
    CLIKeywordList: str
    CLIPromptString: str
    CLIDisplayString: str
    ToolTip: str
    DisplayString: str
    ModeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class GripModeCollection(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.GripModeCollection"""
    def __init__(self, *args) -> None: ...
    Item: GripMode
    IsReadOnly: bool
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, gripMode: GripMode) -> None: ...
    def Clear(self, ) -> None: ...
    def Contains(self, gripMode: GripMode) -> bool: ...
    def CopyTo(self, A_0: list, A_1: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, gripMode: GripMode) -> bool: ...

class GripOverrule(Overrule):
    """.NET: Autodesk.AutoCAD.DatabaseServices.GripOverrule"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetGripPoints(self, entity: Entity, grips: GripDataCollection, curViewUnitSize: float, gripSize: int, curViewDir: Vector3d, bitFlags: GetGripPointsFlags) -> None: ...
    def GetStretchPoints(self, entity: Entity, stretchPoints: Point3dCollection) -> None: ...
    def MoveGripPointsAt(self, entity: Entity, grips: GripDataCollection, offset: Vector3d, bitFlags: MoveGripPointsFlags) -> None: ...
    def MoveStretchPointsAt(self, entity: Entity, indices: IntegerCollection, offset: Vector3d) -> None: ...
    def OnGripStatusChanged(self, entity: Entity, status: GripStatus) -> None: ...
    def SetCustomFilter(self, ) -> None: ...
    def SetExtensionDictionaryEntryFilter(self, entryName: str) -> None: ...
    def SetIdFilter(self, ids: list) -> None: ...
    def SetNoFilter(self, ) -> None: ...
    def SetXDataFilter(self, registeredApplicationName: str) -> None: ...

class GripStatus:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.GripStatus"""
    def __init__(self, *args) -> None: ...
    GripsDone: int  # = 0
    GripsToBeDeleted: int  # = 1
    DimDataToBeDeleted: int  # = 2
class GroundPlaneBackground(Background):
    """.NET: Autodesk.AutoCAD.DatabaseServices.GroundPlaneBackground"""
    def __init__(self, *args) -> None: ...
    ColorGroundPlaneFar: EntityColor
    ColorGroundPlaneNear: EntityColor
    ColorUndergroundAzimuth: EntityColor
    ColorUndergroundHorizon: EntityColor
    ColorSkyHorizon: EntityColor
    ColorSkyZenith: EntityColor
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Group(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Group"""
    def __init__(self, *args) -> None: ...
    NumEntities: int
    IsAnonymous: bool
    IsNotAccessible: bool
    Name: str
    Selectable: bool
    Description: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Append(self, ids: ObjectIdCollection) -> None: ...
    def Clear(self, ) -> None: ...
    def GetAllEntityIds(self, ) -> list: ...
    def GetIndex(self, id: ObjectId) -> int: ...
    def Has(self, entity: Entity) -> bool: ...
    def InsertAt(self, index: int, ids: ObjectIdCollection) -> None: ...
    def Prepend(self, ids: ObjectIdCollection) -> None: ...
    def Remove(self, ids: ObjectIdCollection) -> None: ...
    def RemoveAt(self, index: int, ids: ObjectIdCollection) -> None: ...
    def Replace(self, oldId: ObjectId, newId: ObjectId) -> None: ...
    def Reverse(self, ) -> None: ...
    def SetAnonymous(self, ) -> None: ...
    def SetColor(self, color: Color) -> None: ...
    def SetColorIndex(self, color: int) -> None: ...
    def SetHighlight(self, value: bool) -> None: ...
    def SetLayer(self, value: ObjectId) -> None: ...
    def SetLinetype(self, value: ObjectId) -> None: ...
    def SetLinetypeScale(self, value: float) -> None: ...
    def SetVisibility(self, value: bool) -> None: ...
    def Transfer(self, fromIndex: int, toIndex: int, numItems: int) -> None: ...

class GsMarkType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.GsMarkType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    ArrowMark: int  # = 1
    LeaderLineMark: int  # = 5001
    DoglegMark: int  # = 10001
    MTextMark: int  # = 15001
    MTextUnderLineMark: int  # = 15002
    ToleranceMark: int  # = 15003
    BlockMark: int  # = 15004
class Handle:
    """.NET: Autodesk.AutoCAD.DatabaseServices.Handle"""
    def __init__(self, *args) -> None: ...
    IsOne: bool
    Value: int
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class Hatch(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Hatch"""
    def __init__(self, *args) -> None: ...
    Origin: Point2d
    Area: float
    NumberOfHatchLines: int
    HatchStyle: HatchStyle
    NumberOfPatternDefinitions: int
    PatternDouble: bool
    PatternScale: float
    PatternSpace: float
    PatternAngle: float
    PatternName: str
    PatternType: HatchPatternType
    GradientShift: float
    ShadeTintValue: float
    GradientOneColorMode: bool
    GradientAngle: float
    GradientName: str
    GradientType: GradientPatternType
    IsSolidFill: bool
    IsHatch: bool
    IsGradient: bool
    HatchObjectType: HatchObjectType
    Associative: bool
    NumberOfLoops: int
    BackgroundColor: Color
    Normal: Vector3d
    Elevation: float
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AppendLoop(self, loopType: HatchLoopTypes, vertexCollection: Point2dCollection, bulgeCollection: DoubleCollection) -> None: ...
    def EvaluateGradientColorAt(self, value: float) -> Color: ...
    def EvaluateHatch(self, underEstimateNumLines: bool) -> None: ...
    def GetAssociatedObjectIds(self, ) -> ObjectIdCollection: ...
    def GetAssociatedObjectIdsAt(self, loopIndex: int) -> ObjectIdCollection: ...
    def GetGradientColors(self, ) -> list: ...
    def GetHatchLineDataAt(self, index: int) -> Line2d: ...
    def GetHatchLinesData(self, ) -> Line2dCollection: ...
    def GetLoopAt(self, loopIndex: int) -> HatchLoop: ...
    def GetPatternDefinitionAt(self, index: int) -> PatternDefinition: ...
    def InsertLoopAt(self, loopIndex: int, loopType: HatchLoopTypes, dbObjIds: ObjectIdCollection) -> None: ...
    def LoopTypeAt(self, loopIndex: int) -> HatchLoopTypes: ...
    def RemoveAssociatedObjectIds(self, ) -> None: ...
    def RemoveLoopAt(self, loopIndex: int) -> None: ...
    def SetGradient(self, gradientType: GradientPatternType, gradientName: str) -> None: ...
    def SetGradientColors(self, value: list) -> None: ...
    def SetHatchPattern(self, patternType: HatchPatternType, patternName: str) -> None: ...

class HatchEdgeType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.HatchEdgeType"""
    def __init__(self, *args) -> None: ...
    Line: int  # = 1
    CircularArc: int  # = 2
    EllipticalArc: int  # = 3
    Spline: int  # = 4
class HatchLoop:
    """.NET: Autodesk.AutoCAD.DatabaseServices.HatchLoop"""
    def __init__(self, *args) -> None: ...
    Curves: Curve2dCollection
    Polyline: BulgeVertexCollection
    LoopType: HatchLoopTypes
    IsPolyline: bool

class HatchLoopTypes:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.HatchLoopTypes"""
    def __init__(self, *args) -> None: ...
    Default: int  # = 0
    External: int  # = 1
    Polyline: int  # = 2
    Derived: int  # = 4
    Textbox: int  # = 8
    Outermost: int  # = 16
    NotClosed: int  # = 32
    SelfIntersecting: int  # = 64
    TextIsland: int  # = 128
    Duplicate: int  # = 256
class HatchObjectType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.HatchObjectType"""
    def __init__(self, *args) -> None: ...
    HatchObject: int  # = 0
    GradientObject: int  # = 1
class HatchPatternType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.HatchPatternType"""
    def __init__(self, *args) -> None: ...
    UserDefined: int  # = 0
    PreDefined: int  # = 1
    CustomDefined: int  # = 2
class HatchStyle:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.HatchStyle"""
    def __init__(self, *args) -> None: ...
    Normal: int  # = 0
    Outer: int  # = 1
    Ignore: int  # = 2
class Helix(Spline):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Helix"""
    def __init__(self, *args) -> None: ...
    TotalLength: float
    TurnSlope: float
    Constrain: ConstrainType
    Twist: bool
    TurnHeight: float
    Turns: float
    TopRadius: float
    BaseRadius: float
    Height: float
    AxisVector: Vector3d
    StartPoint: Point3d
    Type: SplineType
    IsPlanar: bool
    NurbsData: NurbsData
    FitData: FitData
    HasFitData: bool
    EndFitTangent: Vector3d
    StartFitTangent: Vector3d
    FitTolerance: float
    NumFitPoints: int
    NumControlPoints: int
    Degree: int
    IsRational: bool
    IsNull: bool
    Area: float
    Spline: Spline
    EndPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CreateHelix(self, ) -> None: ...
    def GetAxisPoint(self, ) -> Point3d: ...
    def SetAxisPoint(self, axisPoint: Point3d, moveStartPoint: bool) -> None: ...

class HelpParameter(ConstraintGroupNode):
    """.NET: Autodesk.AutoCAD.DatabaseServices.HelpParameter"""
    def __init__(self, *args) -> None: ...
    Value: float
    ConnectedEqualparamConstraints: list
    ConnectedConstraint: GeometricalConstraint
    ConnectedGeometry: ConstrainedGeometry
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class HighlightOverrule(Overrule):
    """.NET: Autodesk.AutoCAD.DatabaseServices.HighlightOverrule"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Highlight(self, entity: Entity, subId: FullSubentityPath, highlightAll: bool) -> None: ...
    def SetCustomFilter(self, ) -> None: ...
    def SetExtensionDictionaryEntryFilter(self, entryName: str) -> None: ...
    def SetIdFilter(self, ids: list) -> None: ...
    def SetNoFilter(self, ) -> None: ...
    def SetXDataFilter(self, registeredApplicationName: str) -> None: ...
    def Unhighlight(self, entity: Entity, subId: FullSubentityPath, highlightAll: bool) -> None: ...

class HighlightStateOverrule(Overrule):
    """.NET: Autodesk.AutoCAD.DatabaseServices.HighlightStateOverrule"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def HighlightState(self, entity: Entity, subId: FullSubentityPath) -> HighlightStyle: ...
    def PopHighlight(self, entity: Entity, subId: FullSubentityPath) -> None: ...
    def PushHighlight(self, entity: Entity, subId: FullSubentityPath, highlightStyle: HighlightStyle) -> None: ...
    def SetCustomFilter(self, ) -> None: ...
    def SetExtensionDictionaryEntryFilter(self, entryName: str) -> None: ...
    def SetIdFilter(self, ids: list) -> None: ...
    def SetNoFilter(self, ) -> None: ...
    def SetXDataFilter(self, registeredApplicationName: str) -> None: ...

class HorizontalConstraint(ParallelConstraint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.HorizontalConstraint"""
    def __init__(self, *args) -> None: ...
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class HostApplicationServices(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.HostApplicationServices"""
    def __init__(self, *args) -> None: ...
    ColorBookLocation: str
    ModelerFlavor: ModelerFlavor
    FontMapFileName: str
    AlternateFontName: str
    AllUsersRootFolder: str
    LocalRootFolder: str
    RoamableRootFolder: str
    WorkingDatabase: Database
    releaseMarketVersion: str
    UserRegistryProductRootKey: str
    MachineRegistryProductRootKey: str
    CompanyName: str
    Product: str
    Program: str
    Current: HostApplicationServices
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def FatalError(self, message: str) -> None: ...
    def FindFile(self, fileName: str, database: Database, hint: FindFileHint) -> str: ...
    def GetEnvironmentVariable(self, name: str) -> str: ...
    def GetPassword(self, dwgName: str, options: PasswordOptions) -> str: ...
    def GetRemoteFile(self, url: Uri, ignoreCache: bool) -> str: ...
    def GetUrl(self, localFile: str) -> Uri: ...
    def IsUrl(self, filePath: str) -> bool: ...
    def LoadApplication(self, appName: str, why: ApplicationLoadReasons, printIt: bool, asCmd: bool) -> None: ...
    def NotifyCorruptDrawingFoundOnOpen(self, id: ObjectId, es: ErrorStatus) -> bool: ...
    def PutRemoteFile(self, url: Uri, localFile: str) -> None: ...
    def UserBreak(self, ) -> bool: ...

class HyperLink(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.HyperLink"""
    def __init__(self, *args) -> None: ...
    NestedLevel: int
    IsOutermostContainer: bool
    DisplayString: str
    SubLocation: str
    Description: str
    Name: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Equals(self, other: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class HyperLinkCollection(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.HyperLinkCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: HyperLink
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, value: HyperLink) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: HyperLink) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: HyperLink) -> int: ...
    def Insert(self, index: int, value: HyperLink) -> None: ...
    def Remove(self, value: HyperLink) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class IBLBackground(Background):
    """.NET: Autodesk.AutoCAD.DatabaseServices.IBLBackground"""
    def __init__(self, *args) -> None: ...
    SecondaryBackground: ObjectId
    DisplayImage: bool
    Rotation: float
    IBLImageName: str
    Enable: bool
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class IParameter:
    """.NET: Autodesk.AutoCAD.DatabaseServices.IParameter"""
    def __init__(self, *args) -> None: ...
    ParameterObject: DBObject
    Angular: bool
    DataType: DxfCode
    ReadOnly: bool
    ValueSet: ParameterValueSet
    Value: ResultBuffer
    Description: str
    Expression: str
    Name: str
    def IsNameUnique(self, name: str) -> bool: ...

class ISpecialValueConverter:
    """.NET: Autodesk.AutoCAD.DatabaseServices.ISpecialValueConverter"""
    def __init__(self, *args) -> None: ...
    def ConvertToGlobal(self, o: object, value: str, converted: bool) -> str: ...
    def ConvertToLocal(self, o: object, value: str, converted: bool) -> str: ...
    def GetSpecialValues(self, ) -> list: ...

class ISubObject:
    """.NET: Autodesk.AutoCAD.DatabaseServices.ISubObject"""
    def __init__(self, *args) -> None: ...
    Parent: object

class ITextEditorSelectable:
    """.NET: Autodesk.AutoCAD.DatabaseServices.ITextEditorSelectable"""
    def __init__(self, *args) -> None: ...
    EndOfText: TextEditorLocation
    StartOfText: TextEditorLocation

class IdMapping(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.IdMapping"""
    def __init__(self, *args) -> None: ...
    DuplicateRecordCloning: DuplicateRecordCloning
    DeepCloneContext: DeepCloneType
    OriginalDatabase: Database
    DestinationDatabase: Database
    Item: IdPair
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, pairToAdd: IdPair) -> None: ...
    def Change(self, pairToChange: IdPair) -> None: ...
    def Contains(self, key: ObjectId) -> bool: ...
    def Delete(self, key: ObjectId) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Lookup(self, key: ObjectId) -> IdPair: ...

class IdMappingEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.IdMappingEventArgs"""
    def __init__(self, *args) -> None: ...
    IdMapping: IdMapping

class IdMappingEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.IdMappingEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: IdMappingEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: IdMappingEventArgs) -> None: ...

class IdPair:
    """.NET: Autodesk.AutoCAD.DatabaseServices.IdPair"""
    def __init__(self, *args) -> None: ...
    IsOwnerTranslated: bool
    IsPrimary: bool
    IsCloned: bool
    Value: ObjectId
    Key: ObjectId
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class Image(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Image"""
    def __init__(self, *args) -> None: ...
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ImageBackground(Background):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ImageBackground"""
    def __init__(self, *args) -> None: ...
    Scale: Scale2d
    Offset: Vector2d
    UseTiling: bool
    MaintainAspectRatio: bool
    FitToScreen: bool
    ImageFileName: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ImageDisplayOptions:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.ImageDisplayOptions"""
    def __init__(self, *args) -> None: ...
    Show: int  # = 1
    ShowUnaligned: int  # = 2
    Clip: int  # = 4
    Transparent: int  # = 8
class ImageQuality:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.ImageQuality"""
    def __init__(self, *args) -> None: ...
    Draft: int  # = 0
    High: int  # = 1
    Invalid: int  # = -1
class ImplicitPointType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.ImplicitPointType"""
    def __init__(self, *args) -> None: ...
    StartImplicit: int  # = 0
    EndImplicit: int  # = 1
    MidImplicit: int  # = 2
    CenterImplicit: int  # = 3
    DefineImplicit: int  # = 4
class IndexCreation:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.IndexCreation"""
    def __init__(self, *args) -> None: ...
    NoIndex: int  # = 0
    IndexByLayer: int  # = 1
    IndexSpatially: int  # = 2
class InterferenceProtocolExtension(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.InterferenceProtocolExtension"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CreateInterferenceObjects(self, ent1: Entity, ent2: Entity, flags: int) -> list: ...

class Intersect:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.Intersect"""
    def __init__(self, *args) -> None: ...
    OnBothOperands: int  # = 0
    ExtendThis: int  # = 1
    ExtendArgument: int  # = 2
    ExtendBoth: int  # = 3
class ItemLocator:
    """.NET: Autodesk.AutoCAD.DatabaseServices.ItemLocator"""
    def __init__(self, *args) -> None: ...
    LevelIndex: int
    RowIndex: int
    ItemIndex: int

class JoinStyle:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.JoinStyle"""
    def __init__(self, *args) -> None: ...
    StyleNone: int  # = 0
    StyleRound: int  # = 1
    StyleAngle: int  # = 2
    StyleFlat: int  # = 3
class LampColorPreset:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.LampColorPreset"""
    def __init__(self, *args) -> None: ...
    D65White: int  # = 0
    Fluorescent: int  # = 1
    CoolWhite: int  # = 2
    WhiteFluorescent: int  # = 3
    DaylightFluorescent: int  # = 4
    Incandescent: int  # = 5
    Xenon: int  # = 6
    Halogen: int  # = 7
    Quartz: int  # = 8
    MetalHalide: int  # = 9
    Mercury: int  # = 10
    PhosphorMercury: int  # = 11
    HighPressureSodium: int  # = 12
    LowPressureSodium: int  # = 13
    Custom: int  # = 14
class LampColorType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.LampColorType"""
    def __init__(self, *args) -> None: ...
    Kelvin: int  # = 0
    Preset: int  # = 1
class LayerEvaluation:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.LayerEvaluation"""
    def __init__(self, *args) -> None: ...
    NoNewLayerEvaluation: int  # = 0
    EvalNewXrefLayers: int  # = 1
    EvalAllNewLayers: int  # = 2
class LayerStateDeletedEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.LayerStateDeletedEventArgs"""
    def __init__(self, *args) -> None: ...
    Name: str

class LayerStateDeletedEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.LayerStateDeletedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: LayerStateDeletedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: LayerStateDeletedEventArgs) -> None: ...

class LayerStateEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.LayerStateEventArgs"""
    def __init__(self, *args) -> None: ...
    Name: str
    Id: ObjectId

class LayerStateEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.LayerStateEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: LayerStateEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: LayerStateEventArgs) -> None: ...

class LayerStateManager(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.LayerStateManager"""
    def __init__(self, *args) -> None: ...
    LastRestoredLayerState: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CompareLayerStateToDb(self, name: str, idVp: ObjectId) -> bool: ...
    def DeleteLayerState(self, name: str) -> None: ...
    def ExportLayerState(self, nameToExport: str, fileName: str) -> None: ...
    def GetLayerStateDescription(self, name: str) -> str: ...
    def GetLayerStateLayers(self, name: str, bInvert: bool) -> ArrayList: ...
    def GetLayerStateMask(self, name: str) -> LayerStateMasks: ...
    def GetLayerStateNames(self, bIncludeHidden: bool, bIncludeXref: bool) -> ArrayList: ...
    def HasLayerState(self, name: str) -> bool: ...
    def ImportLayerState(self, fileName: str) -> None: ...
    def ImportLayerStateFromDb(self, name: str, database: Database) -> None: ...
    def LayerStateHasViewportData(self, name: str) -> bool: ...
    def LayerStatesDictionaryId(self, createIfNotPresent: bool) -> ObjectId: ...
    def RenameLayerState(self, name: str, newName: str) -> None: ...
    def RestoreLayerState(self, name: str, id: ObjectId, undefinedLayerStatePolicy: int, clientMask: LayerStateMasks) -> None: ...
    def SaveLayerState(self, name: str, mask: LayerStateMasks, id: ObjectId) -> None: ...
    def SetLayerStateDescription(self, name: str, description: str) -> None: ...
    def SetLayerStateMask(self, name: str, mask: LayerStateMasks) -> None: ...

class LayerStateMasks:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.LayerStateMasks"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    On: int  # = 1
    Frozen: int  # = 2
    Locked: int  # = 4
    Plot: int  # = 8
    NewViewport: int  # = 16
    Color: int  # = 32
    LineType: int  # = 64
    LineWeight: int  # = 128
    PlotStyle: int  # = 256
    CurrentViewport: int  # = 512
    Transparency: int  # = 1024
    LastRestored: int  # = 65536
class LayerStateRenameEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.LayerStateRenameEventArgs"""
    def __init__(self, *args) -> None: ...
    NewName: str
    Name: str

class LayerStateRenameEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.LayerStateRenameEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: LayerStateRenameEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: LayerStateRenameEventArgs) -> None: ...

class LayerTable(SymbolTable):
    """.NET: Autodesk.AutoCAD.DatabaseServices.LayerTable"""
    def __init__(self, *args) -> None: ...
    SkippingReconciled: LayerTable
    IncludingHidden: LayerTable
    HasUnreconciledLayers: bool
    IncludingErased: SymbolTable
    Item: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GenerateUsageData(self, ) -> None: ...
    def GetEnumerator(self, ) -> SymbolTableEnumerator: ...
    def GetUnreconciledLayers(self, ) -> ObjectIdCollection: ...

class LayerTableRecord(SymbolTableRecord):
    """.NET: Autodesk.AutoCAD.DatabaseServices.LayerTableRecord"""
    def __init__(self, *args) -> None: ...
    HasOverrides: bool
    IsReconciled: bool
    IsHidden: bool
    Description: str
    PlotStyleNameId: ObjectId
    PlotStyleName: str
    LineWeight: LineWeight
    IsPlottable: bool
    MaterialId: ObjectId
    LinetypeObjectId: ObjectId
    Transparency: Transparency
    EntityColor: EntityColor
    Color: Color
    IsLocked: bool
    ViewportVisibilityDefault: bool
    IsOff: bool
    IsFrozen: bool
    IsUsed: bool
    IsResolved: bool
    IsDependent: bool
    Name: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetViewportOverrides(self, viewportId: ObjectId) -> LayerViewportProperties: ...
    def HasViewportOverrides(self, viewportId: ObjectId) -> bool: ...
    def RemoveAllOverrides(self, ) -> None: ...

class LayerViewportProperties:
    """.NET: Autodesk.AutoCAD.DatabaseServices.LayerViewportProperties"""
    def __init__(self, *args) -> None: ...
    IsPlotStyleOverridden: bool
    PlotStyleNameId: ObjectId
    PlotStyleName: str
    IsTransparencyOverridden: bool
    Transparency: Transparency
    IsLineWeightOverridden: bool
    LineWeight: LineWeight
    IsLinetypeOverridden: bool
    LinetypeObjectId: ObjectId
    IsColorOverridden: bool
    Color: Color
    def RemoveOverrides(self, ) -> None: ...

class Layout(PlotSettings):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Layout"""
    def __init__(self, *args) -> None: ...
    Thumbnail: Bitmap
    Extents: Extents3d
    Limits: Extents2d
    AnnoAllVisible: bool
    TabSelected: bool
    TabOrder: int
    LayoutName: str
    BlockTableRecordId: ObjectId
    PlotAsRaster: bool
    PlotWireframe: bool
    ShadePlotId: ObjectId
    ModelType: bool
    DrawViewportsFirst: bool
    PrintLineweights: bool
    ScaleLineweights: bool
    StdScale: float
    StdScaleType: StdScaleType
    CurrentStyleSheet: str
    CustomPrintScale: CustomScale
    UseStandardScale: bool
    PlotViewName: str
    PlotWindowArea: Extents2d
    PlotType: PlotType
    ShadePlotCustomDpi: int
    ShadePlotResLevel: ShadePlotResLevel
    ShadePlot: PlotSettingsShadePlotType
    PlotHidden: bool
    PlotCentered: bool
    PlotRotation: PlotRotation
    ShowPlotStyles: bool
    PlotPlotStyles: bool
    PlotTransparency: bool
    PlotViewportBorders: bool
    PlotPaperUnits: PlotPaperUnit
    PlotOrigin: Point2d
    CanonicalMediaName: str
    PlotPaperSize: Point2d
    PlotPaperMargins: Extents2d
    PlotConfigurationName: str
    PlotSettingsName: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddToLayoutDictionary(self, toWhichDatabase: Database, blockTableRecordId: ObjectId) -> None: ...
    def GetViewports(self, ) -> ObjectIdCollection: ...
    def Initialize(self, ) -> ObjectId: ...

class LayoutCopiedEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.LayoutCopiedEventArgs"""
    def __init__(self, *args) -> None: ...
    NewName: str
    Name: str
    NewId: ObjectId
    Id: ObjectId

class LayoutCopiedEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.LayoutCopiedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: LayoutCopiedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: LayoutCopiedEventArgs) -> None: ...

class LayoutEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.LayoutEventArgs"""
    def __init__(self, *args) -> None: ...
    Name: str
    Id: ObjectId

class LayoutEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.LayoutEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: LayoutEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: LayoutEventArgs) -> None: ...

class LayoutManager(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.LayoutManager"""
    def __init__(self, *args) -> None: ...
    LayoutCount: int
    CurrentLayout: str
    Current: LayoutManager
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CloneLayout(self, copyName: str, newName: str, newTabOrder: int) -> None: ...
    def CopyLayout(self, copyName: str, newName: str) -> None: ...
    def CreateLayout(self, newName: str) -> ObjectId: ...
    def DeleteLayout(self, deleteName: str) -> None: ...
    def GetLayoutId(self, name: str) -> ObjectId: ...
    def GetNonRectangularViewportIdFromClipId(self, clipId: ObjectId) -> ObjectId: ...
    def LayoutExists(self, name: str) -> bool: ...
    def RenameLayout(self, oldName: str, newName: str) -> None: ...
    def SetCurrentLayoutId(self, layoutId: ObjectId) -> None: ...

class LayoutRenamedEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.LayoutRenamedEventArgs"""
    def __init__(self, *args) -> None: ...
    NewName: str
    Name: str
    Id: ObjectId

class LayoutRenamedEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.LayoutRenamedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: LayoutRenamedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: LayoutRenamedEventArgs) -> None: ...

class Leader(Curve):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Leader"""
    def __init__(self, *args) -> None: ...
    DimensionStyleName: str
    Dimtxt: float
    TextStyleId: ObjectId
    Dimtad: int
    Dimscale: float
    Dimsah: bool
    Dimldrblk: ObjectId
    Dimlwd: LineWeight
    Dimgap: float
    Dimclrd: Color
    Dimasz: float
    AnnoWidth: float
    AnnoHeight: float
    AnnoType: AnnotationType
    AnnotationOffset: Vector3d
    Annotation: ObjectId
    DimensionStyle: ObjectId
    IsSplined: bool
    HasHookLine: bool
    HasArrowHead: bool
    LastVertex: Point3d
    FirstVertex: Point3d
    NumVertices: int
    Normal: Vector3d
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AppendVertex(self, pointToAdd: Point3d) -> bool: ...
    def EvaluateLeader(self, ) -> None: ...
    def GetDimstyleData(self, ) -> DimStyleTableRecord: ...
    def RemoveLastVertex(self, ) -> None: ...
    def SetDimstyleData(self, style: DimStyleTableRecord) -> None: ...
    def SetPlane(self, value: Plane) -> None: ...
    def SetVertexAt(self, index: int, pointValue: Point3d) -> bool: ...
    def VertexAt(self, value: int) -> Point3d: ...

class LeaderDirectionType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.LeaderDirectionType"""
    def __init__(self, *args) -> None: ...
    UnknownLeader: int  # = 0
    LeftLeader: int  # = 1
    RightLeader: int  # = 2
    TopLeader: int  # = 3
    BottomLeader: int  # = 4
class LeaderType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.LeaderType"""
    def __init__(self, *args) -> None: ...
    InVisibleLeader: int  # = 0
    StraightLeader: int  # = 1
    SplineLeader: int  # = 2
class Light(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Light"""
    def __init__(self, *args) -> None: ...
    HasTarget: bool
    WebRotation: Vector3d
    WebFile: str
    LampColorRGB: ColorRGB
    LampColorPreset: LampColorPreset
    LampColorTemp: float
    LampColorType: LampColorType
    IlluminanceDistance: float
    PhysicalIntensity: float
    PhysicalIntensityMethod: PhysicalIntensityMethod
    Softness: int
    ShadowType: ShadowType
    MapSize: int
    UseLimits: bool
    EndLimitOffset: float
    StartLimitOffset: float
    AttenuationType: AttenuationType
    Name: str
    Direction: Vector3d
    FalloffAngle: float
    HotspotAngle: float
    TargetLocation: Point3d
    Position: Point3d
    Attenuation: LightAttenuation
    Shadow: ShadowParameters
    Intensity: float
    LightColor: Color
    IsPlottable: bool
    IsOn: bool
    LightType: DrawableType
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def ResultingColor(self, ) -> Color: ...
    def SetHotspotAndFalloff(self, hotspot: float, falloff: float) -> None: ...

class LightingUnits:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.LightingUnits"""
    def __init__(self, *args) -> None: ...
    LightingUnitsGeneric: int  # = 0
    LightingUnitsAmerican: int  # = 1
    LightingUnitsInternational: int  # = 2
class Line(Curve):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Line"""
    def __init__(self, *args) -> None: ...
    Length: float
    Angle: float
    Delta: Vector3d
    Normal: Vector3d
    Thickness: float
    EndPoint: Point3d
    StartPoint: Point3d
    Area: float
    Spline: Spline
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LineAngularDimension2(Dimension):
    """.NET: Autodesk.AutoCAD.DatabaseServices.LineAngularDimension2"""
    def __init__(self, *args) -> None: ...
    XLine2End: Point3d
    XLine2Start: Point3d
    XLine1End: Point3d
    XLine1Start: Point3d
    ArcPoint: Point3d
    Dimaltmzf: float
    Dimmzf: float
    Dimaltmzs: str
    Dimmzs: str
    Dimblk2: ObjectId
    Dimblk1: ObjectId
    Dimblk: ObjectId
    Dimpost: str
    Dimapost: str
    Dimzin: int
    Dimupt: bool
    Dimtzin: int
    Dimtxtdirection: bool
    Dimtxt: float
    TextStyleId: ObjectId
    Dimtvp: float
    Dimtsz: float
    Dimtp: float
    Dimtolj: int
    Dimtol: bool
    Dimtoh: bool
    Dimtofl: bool
    Dimtmove: int
    Dimtm: float
    Dimtix: bool
    Dimtih: bool
    Dimtfillclr: Color
    Dimtfill: int
    Dimtfac: float
    Dimtdec: int
    Dimtad: int
    Dimsoxd: bool
    Dimse2: bool
    Dimse1: bool
    Dimsd2: bool
    Dimsd1: bool
    Dimscale: float
    Dimsah: bool
    Dimrnd: float
    DimensionStyleName: str
    CenterMarkSize: float
    CenterMarkType: DimensionCenterMarkType
    ToleranceSuppressZeroInches: bool
    ToleranceSuppressZeroFeet: bool
    ToleranceSuppressTrailingZeros: bool
    ToleranceSuppressLeadingZeros: bool
    AltToleranceSuppressZeroInches: bool
    AltToleranceSuppressZeroFeet: bool
    AltToleranceSuppressTrailingZeros: bool
    AltToleranceSuppressLeadingZeros: bool
    AltSuppressZeroInches: bool
    AltSuppressZeroFeet: bool
    AltSuppressTrailingZeros: bool
    AltSuppressLeadingZeros: bool
    AlternateSuffix: str
    AlternatePrefix: str
    SuppressZeroInches: bool
    SuppressZeroFeet: bool
    SuppressTrailingZeros: bool
    SuppressLeadingZeros: bool
    SuppressAngularTrailingZeros: bool
    SuppressAngularLeadingZeros: bool
    Suffix: str
    Prefix: str
    Dimlwe: LineWeight
    Dimlwd: LineWeight
    Dimlunit: int
    Dimltype: ObjectId
    Dimltex2: ObjectId
    Dimltex1: ObjectId
    Dimlim: bool
    Dimlfac: float
    Dimldrblk: ObjectId
    Dimjust: int
    Dimjogang: float
    Dimgap: float
    Dimfxlen: float
    DimfxlenOn: bool
    Dimfrac: int
    Dimexo: float
    Dimexe: float
    Dimdsep: str
    Dimdli: float
    Dimdle: float
    Dimdec: int
    Dimclrt: Color
    Dimclre: Color
    Dimclrd: Color
    Dimcen: float
    Dimazin: int
    Dimaunit: int
    Dimatfit: int
    Dimasz: float
    Dimarcsym: int
    Dimaltz: int
    Dimaltu: int
    Dimalttz: int
    Dimalttd: int
    Dimaltrnd: float
    Dimaltf: float
    Dimaltd: int
    Dimalt: bool
    Dimadec: int
    DynamicDimension: bool
    Measurement: float
    DimBlockPosition: Point3d
    DimBlockId: ObjectId
    HorizontalRotation: float
    TextLineSpacingFactor: float
    TextLineSpacingStyle: LineSpacingStyle
    TextAttachment: AttachmentPoint
    DimensionStyle: ObjectId
    TextRotation: float
    DimensionText: str
    Elevation: float
    Normal: Vector3d
    UsingDefaultTextPosition: bool
    TextPosition: Point3d
    TextDefinedSize: Vector2d
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LineSpacingStyle:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.LineSpacingStyle"""
    def __init__(self, *args) -> None: ...
    AtLeast: int  # = 1
    Exactly: int  # = 2
class LineWeight:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.LineWeight"""
    def __init__(self, *args) -> None: ...
    LineWeight000: int  # = 0
    LineWeight005: int  # = 5
    LineWeight009: int  # = 9
    LineWeight013: int  # = 13
    LineWeight015: int  # = 15
    LineWeight018: int  # = 18
    LineWeight020: int  # = 20
    LineWeight025: int  # = 25
    LineWeight030: int  # = 30
    LineWeight035: int  # = 35
    LineWeight040: int  # = 40
    LineWeight050: int  # = 50
    LineWeight053: int  # = 53
    LineWeight060: int  # = 60
    LineWeight070: int  # = 70
    LineWeight080: int  # = 80
    LineWeight090: int  # = 90
    LineWeight100: int  # = 100
    LineWeight106: int  # = 106
    LineWeight120: int  # = 120
    LineWeight140: int  # = 140
    LineWeight158: int  # = 158
    LineWeight200: int  # = 200
    LineWeight211: int  # = 211
    ByDIPs: int  # = -4
    ByLineWeightDefault: int  # = -3
    ByBlock: int  # = -2
    ByLayer: int  # = -1
class LineWeightConverter(TypeConverter):
    """.NET: Autodesk.AutoCAD.DatabaseServices.LineWeightConverter"""
    def __init__(self, *args) -> None: ...
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool: ...
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object: ...
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object: ...

class LinetypeTable(SymbolTable):
    """.NET: Autodesk.AutoCAD.DatabaseServices.LinetypeTable"""
    def __init__(self, *args) -> None: ...
    IncludingErased: SymbolTable
    Item: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LinetypeTableRecord(SymbolTableRecord):
    """.NET: Autodesk.AutoCAD.DatabaseServices.LinetypeTableRecord"""
    def __init__(self, *args) -> None: ...
    IsScaledToFit: bool
    NumDashes: int
    PatternLength: float
    AsciiDescription: str
    Comments: str
    IsResolved: bool
    IsDependent: bool
    Name: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def DashLengthAt(self, index: int) -> float: ...
    def SetDashLengthAt(self, index: int, value: float) -> None: ...
    def SetShapeIsUcsOrientedAt(self, index: int, isOriented: bool) -> None: ...
    def SetShapeIsUprightAt(self, index: int, isUpright: bool) -> None: ...
    def SetShapeNumberAt(self, index: int, shapeNumber: int) -> None: ...
    def SetShapeOffsetAt(self, index: int, offset: Vector2d) -> None: ...
    def SetShapeRotationAt(self, index: int, rotation: float) -> None: ...
    def SetShapeScaleAt(self, index: int, scale: float) -> None: ...
    def SetShapeStyleAt(self, index: int, id: ObjectId) -> None: ...
    def SetTextAt(self, index: int, value: str) -> None: ...
    def ShapeIsUcsOrientedAt(self, index: int) -> bool: ...
    def ShapeIsUprightAt(self, index: int) -> bool: ...
    def ShapeNumberAt(self, index: int) -> int: ...
    def ShapeOffsetAt(self, index: int) -> Vector2d: ...
    def ShapeRotationAt(self, index: int) -> float: ...
    def ShapeScaleAt(self, index: int) -> float: ...
    def ShapeStyleAt(self, index: int) -> ObjectId: ...
    def TextAt(self, index: int) -> str: ...

class LinkedData(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.LinkedData"""
    def __init__(self, *args) -> None: ...
    Name: str
    IsEmpty: bool
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Clear(self, ) -> None: ...

class LinkedTableData(LinkedData):
    """.NET: Autodesk.AutoCAD.DatabaseServices.LinkedTableData"""
    def __init__(self, *args) -> None: ...
    NumberOfRows: int
    NumberOfColumns: int
    Name: str
    IsEmpty: bool
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AppendColumn(self, columnsNumber: int) -> int: ...
    def AppendRow(self, rowsNumber: int) -> int: ...
    def DataType(self, row: int, column: int) -> DataType: ...
    def DeleteColumn(self, index: int, columnsNumberToDelete: int) -> None: ...
    def DeleteContent(self, row: int, column: int) -> None: ...
    def DeleteRow(self, index: int, rowsNumberToDelete: int) -> None: ...
    def GetBlockAttributeValue(self, row: int, column: int, attributeDefinitionId: ObjectId) -> str: ...
    def GetBlockTableRecordId(self, row: int, column: int) -> ObjectId: ...
    def GetCellState(self, row: int, column: int) -> CellStates: ...
    def GetColumnName(self, index: int) -> str: ...
    def GetContentTypes(self, row: int, column: int) -> CellContentTypes: ...
    def GetCustomData(self, row: int, column: int, key: str) -> object: ...
    def GetDataFormat(self, row: int, column: int) -> str: ...
    def GetDataLink(self, row: int, column: int) -> ObjectId: ...
    def GetEnumerator(self, option: TableEnumeratorOption) -> TableEnumerator: ...
    def GetFieldId(self, row: int, column: int) -> ObjectId: ...
    def GetToolTip(self, row: int, column: int) -> str: ...
    def GetValue(self, row: int, column: int, content: int, formatOption: FormatOption) -> object: ...
    def InsertColumn(self, index: int, columnsNumber: int) -> int: ...
    def InsertRow(self, index: int, rowsNumber: int) -> int: ...
    def IsContentEditable(self, row: int, column: int) -> bool: ...
    def IsLinked(self, row: int, column: int) -> bool: ...
    def SetBlockAttributeValue(self, row: int, column: int, attributeDefinitionId: ObjectId, value: str) -> None: ...
    def SetBlockTableRecordId(self, row: int, column: int, value: ObjectId) -> None: ...
    def SetCellState(self, row: int, column: int, value: CellStates) -> None: ...
    def SetColumnName(self, index: int, name: str) -> None: ...
    def SetCustomData(self, row: int, column: int, key: str, value: object) -> None: ...
    def SetDataFormat(self, row: int, column: int, format: str) -> None: ...
    def SetDataLink(self, row: int, column: int, dataLinkId: ObjectId, bUpdate: bool) -> None: ...
    def SetDataType(self, row: int, column: int, dataType: DataType, unitType: UnitType) -> None: ...
    def SetFieldId(self, row: int, column: int, value: ObjectId) -> None: ...
    def SetSize(self, numRows: int, numCols: int) -> None: ...
    def SetToolTip(self, row: int, column: int, value: str) -> None: ...
    def SetValue(self, row: int, column: int, content: int, value: object, parseOption: ParseOption) -> None: ...
    def UnitType(self, row: int, column: int) -> UnitType: ...
    def UpdateDataLink(self, row: int, column: int, dir: UpdateDirection, option: UpdateOption) -> None: ...

class LoftOptions(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.LoftOptions"""
    def __init__(self, *args) -> None: ...
    NormalOption: LoftOptionsNormalOption
    VirtualGuide: bool
    Ruled: bool
    Closed: bool
    Simplify: bool
    AlignDirection: bool
    NoTwist: bool
    ArcLengthParam: bool
    DraftEndMag: float
    DraftStartMag: float
    DraftEnd: float
    DraftStart: float
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CheckCrossSectionCurves(self, crossSectionCurves: list, displayErrorMessages: bool) -> LoftOptionsCheckCurvesOut: ...
    def CheckGuideCurves(self, guideCurves: list, displayErrorMessages: bool) -> None: ...
    def CheckLoftCurves(self, crossSectionCurves: list, guideCurves: list, pPathCurve: Entity, displayErrorMessages: bool) -> LoftOptionsCheckCurvesOut: ...
    def CheckPathCurve(self, pathCurve: Entity, displayErrorMessages: bool) -> None: ...
    def Clone(self, ) -> object: ...

class LoftOptionsBuilder:
    """.NET: Autodesk.AutoCAD.DatabaseServices.LoftOptionsBuilder"""
    def __init__(self, *args) -> None: ...
    NormalOption: LoftOptionsNormalOption
    VirtualGuide: bool
    Ruled: bool
    Closed: bool
    Simplify: bool
    AlignDirection: bool
    NoTwist: bool
    ArcLengthParam: bool
    DraftEndMag: float
    DraftStartMag: float
    DraftEnd: float
    DraftStart: float
    def SetOptionsFromSysvars(self, ) -> None: ...
    def ToLoftOptions(self, ) -> LoftOptions: ...

class LoftOptionsCheckCurvesOut:
    """.NET: Autodesk.AutoCAD.DatabaseServices.LoftOptionsCheckCurvesOut"""
    def __init__(self, *args) -> None: ...
    AllPlanar: bool
    AllClosed: bool
    AllOpen: bool

class LoftOptionsNormalOption:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.LoftOptionsNormalOption"""
    def __init__(self, *args) -> None: ...
    NoNormal: int  # = 0
    FirstNormal: int  # = 1
    LastNormal: int  # = 2
    EndsNormal: int  # = 3
    AllNormal: int  # = 4
    UseDraftAngles: int  # = 5
class LoftProfile(Profile3d):
    """.NET: Autodesk.AutoCAD.DatabaseServices.LoftProfile"""
    def __init__(self, *args) -> None: ...
    Magnitude: float
    Continuity: int
    IsValid: bool
    IsEdge: bool
    IsFace: bool
    IsSubent: bool
    IsPlanar: bool
    IsClosed: bool
    ProfileVertexRef: VertexRef
    ProfilePathRef: PathRef
    Entity: Entity
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CopyFrom(self, source: Profile3d) -> None: ...

class LoftedSurface(Surface):
    """.NET: Autodesk.AutoCAD.DatabaseServices.LoftedSurface"""
    def __init__(self, *args) -> None: ...
    EndCrossSectionMagnitude: float
    EndGuideCurveMagnitude: float
    StartCrossSectionMagnitude: float
    StartGuideCurveMagnitude: float
    EndCrossSectionContinuity: int
    EndGuideCurveContinuity: int
    StartCrossSectionContinuity: int
    StartGuideCurveContinuity: int
    PathProfile: LoftProfile
    GuideProfiles: list
    CrossSectionProfiles: list
    NumberOfGuideCurves: int
    NumberOfCrossSections: int
    Closed: bool
    SurfaceType: LoftSurfaceType
    LoftOptions: LoftOptions
    PathEntity: Entity
    GuideCurves: list
    CrossSections: list
    GeometricExtents: Extents3d
    UsesGraphicsCache: bool
    Perimeter: float
    WireframeType: WireframeTypeEnum
    VIsoLineDensity: int
    UIsoLineDensity: int
    ModificationActionBodyIds: ObjectIdCollection
    CreationActionBodyId: ObjectId
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CreateLoftedSurface(self, crossSections: list, guideCurves: list, pathCurve: Entity, loftOptions: LoftOptions) -> None: ...
    def GetCrossSectionProfile(self, idx: int) -> LoftProfile: ...
    def GetGuideProfile(self, idx: int) -> LoftProfile: ...

class LongTransaction(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.LongTransaction"""
    def __init__(self, *args) -> None: ...
    DisallowDrawOrder: bool
    ActiveIdMap: IdMapping
    LongTransactionName: str
    DestinationBlock: ObjectId
    OriginBlock: ObjectId
    Type: LongTransactionType
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddToWorkSet(self, id: ObjectId) -> None: ...
    def OriginObject(self, id: ObjectId) -> ObjectId: ...
    def RegenWorkSetWithDrawOrder(self, ) -> None: ...
    def RemoveFromWorkSet(self, id: ObjectId) -> None: ...
    def SyncWorkSet(self, ) -> None: ...
    def WorkSetHas(self, id: ObjectId, includeErased: bool) -> bool: ...

class LongTransactionType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.LongTransactionType"""
    def __init__(self, *args) -> None: ...
    SameDb: int  # = 0
    XRefDb: int  # = 1
    UnrelatedDb: int  # = 2
class MInsertBlock(BlockReference):
    """.NET: Autodesk.AutoCAD.DatabaseServices.MInsertBlock"""
    def __init__(self, *args) -> None: ...
    RowSpacing: float
    ColumnSpacing: float
    Rows: int
    Columns: int
    UnitFactor: float
    BlockUnit: UnitsValue
    Name: str
    AnonymousBlockTableRecord: ObjectId
    DynamicBlockTableRecord: ObjectId
    IsDynamicBlock: bool
    DynamicBlockReferencePropertyCollection: DynamicBlockReferencePropertyCollection
    TreatAsBlockRefForExplode: bool
    AttributeCollection: AttributeCollection
    BlockTransform: Matrix3d
    Normal: Vector3d
    Rotation: float
    ScaleFactors: Scale3d
    Position: Point3d
    BlockTableRecord: ObjectId
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class MLeader(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.MLeader"""
    def __init__(self, *args) -> None: ...
    ExtendLeaderToText: bool
    TextAttachmentDirection: TextAttachmentDirection
    MText: MText
    ToleranceLocation: Point3d
    TextLocation: Point3d
    BlockPosition: Point3d
    MLeaderStyle: ObjectId
    EnableAnnotationScale: bool
    BlockConnectionType: BlockConnectionType
    BlockRotation: float
    BlockScale: Scale3d
    BlockColor: Color
    BlockContentId: ObjectId
    EnableFrameText: bool
    TextHeight: float
    TextColor: Color
    TextAlignmentType: TextAlignmentType
    TextAngleType: TextAngleType
    TextAttachmentType: TextAttachmentType
    TextStyleId: ObjectId
    ContentType: ContentType
    ArrowSize: float
    ArrowSymbolId: ObjectId
    DoglegLength: float
    EnableDogleg: bool
    EnableLanding: bool
    LandingGap: float
    LeaderLineWeight: LineWeight
    LeaderLineTypeId: ObjectId
    LeaderLineColor: Color
    LeaderLineType: LeaderType
    LeaderLineCount: int
    LeaderCount: int
    Scale: float
    Normal: Vector3d
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddFirstVertex(self, leaderLineIndex: int, point: Point3d) -> None: ...
    def AddLastVertex(self, leaderLineIndex: int, point: Point3d) -> None: ...
    def AddLeader(self, ) -> int: ...
    def AddLeaderLine(self, point: Point3d) -> int: ...
    def ConnectionPoint(self, direction: Vector3d, textAttachmentDirection: TextAttachmentDirection) -> Point3d: ...
    def GetArrowSize(self, leaderLineIndex: int) -> float: ...
    def GetArrowSymbolId(self, leaderLineIndex: int) -> ObjectId: ...
    def GetBlockAttribute(self, attDefId: ObjectId) -> AttributeReference: ...
    def GetContentGeomExtents(self, ) -> Extents3d: ...
    def GetDogleg(self, leaderIndex: int) -> Vector3d: ...
    def GetDoglegLength(self, leaderIndex: int) -> float: ...
    def GetFirstVertex(self, leaderLineIndex: int) -> Point3d: ...
    def GetLastVertex(self, leaderLineIndex: int) -> Point3d: ...
    def GetLeaderIndex(self, leaderLineIndex: int) -> int: ...
    def GetLeaderIndexes(self, ) -> ArrayList: ...
    def GetLeaderLineColor(self, leaderLineIndex: int) -> Color: ...
    def GetLeaderLineIndexes(self, leaderIndex: int) -> ArrayList: ...
    def GetLeaderLineType(self, leaderLineIndex: int) -> LeaderType: ...
    def GetLeaderLineTypeId(self, leaderLineIndex: int) -> ObjectId: ...
    def GetLeaderLineWeight(self, leaderLineIndex: int) -> LineWeight: ...
    def GetPlane(self, ) -> Plane: ...
    def GetTextAttachmentType(self, leaderDirection: LeaderDirectionType) -> TextAttachmentType: ...
    def GetVertex(self, leaderLineIndex: int, index: int) -> Point3d: ...
    def HasContent(self, ) -> bool: ...
    def MoveMLeader(self, vec: Vector3d, type: MoveType) -> None: ...
    def PostMLeaderToDb(self, db: Database) -> None: ...
    def RemoveFirstVertex(self, leaderLineIndex: int) -> None: ...
    def RemoveLastVertex(self, leaderLineIndex: int) -> None: ...
    def RemoveLeader(self, index: int) -> None: ...
    def RemoveLeaderLine(self, leaderLineIndex: int) -> None: ...
    def SetArrowSize(self, leaderLineIndex: int, arrowSize: float) -> None: ...
    def SetArrowSymbolId(self, leaderLineIndex: int, id: ObjectId) -> None: ...
    def SetBlockAttribute(self, attDefId: ObjectId, attributeValue: AttributeReference) -> None: ...
    def SetContextDataManager(self, contextDataManager: IntPtr) -> None: ...
    def SetDogleg(self, leaderIndex: int, vector: Vector3d) -> None: ...
    def SetDoglegLength(self, leaderIndex: int, doglegLength: float) -> None: ...
    def SetFirstVertex(self, leaderLineIndex: int, point: Point3d) -> None: ...
    def SetLastVertex(self, leaderLineIndex: int, point: Point3d) -> None: ...
    def SetLeaderLineColor(self, leaderLineIndex: int, leaderLineTypeId: Color) -> None: ...
    def SetLeaderLineType(self, leaderLineIndex: int, leaderLineType: LeaderType) -> None: ...
    def SetLeaderLineTypeId(self, leaderLineIndex: int, leaderLineTypeId: ObjectId) -> None: ...
    def SetLeaderLineWeight(self, leaderLineIndex: int, leaderLineWeight: LineWeight) -> None: ...
    def SetPlane(self, value: Plane) -> None: ...
    def SetTextAttachmentType(self, textAttachmentType: TextAttachmentType, leaderDirection: LeaderDirectionType) -> None: ...
    def SetVertex(self, leaderLineIndex: int, index: int, point: Point3d) -> None: ...
    def VerticesCount(self, leaderLineIndex: int) -> int: ...
    def getContextDataManager(self, ) -> IntPtr: ...
    def getOverridedMLeaderStyle(self, mleaderStyle: MLeaderStyle) -> None: ...
    def recomputeBreakPoints(self, ) -> None: ...

class MLeaderStyle(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.MLeaderStyle"""
    def __init__(self, *args) -> None: ...
    ExtendLeaderToText: bool
    TextAttachmentDirection: TextAttachmentDirection
    Name: str
    BreakSize: float
    Scale: float
    BlockConnectionType: BlockConnectionType
    EnableBlockRotation: bool
    BlockRotation: float
    EnableBlockScale: bool
    BlockScale: Scale3d
    BlockColor: Color
    BlockId: ObjectId
    EnableFrameText: bool
    TextHeight: float
    TextColor: Color
    TextAlignAlwaysLeft: bool
    TextAlignmentType: TextAlignmentType
    TextAngleType: TextAngleType
    TextAttachmentType: TextAttachmentType
    TextStyleId: ObjectId
    DefaultMText: MText
    ArrowSize: float
    ArrowSymbolId: ObjectId
    DoglegLength: float
    EnableDogleg: bool
    LandingGap: float
    EnableLanding: bool
    LeaderLineWeight: LineWeight
    LeaderLineTypeId: ObjectId
    LeaderLineColor: Color
    LeaderLineType: LeaderType
    SecondSegmentAngleConstraint: AngleConstraint
    FirstSegmentAngleConstraint: AngleConstraint
    MaxLeaderSegmentsPoints: int
    DrawLeaderOrderType: DrawLeaderOrderType
    DrawMLeaderOrderType: DrawMLeaderOrderType
    ContentType: ContentType
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetTextAttachmentType(self, leaderDirection: LeaderDirectionType) -> TextAttachmentType: ...
    def OverwritePropChanged(self, ) -> bool: ...
    def PostMLeaderStyleToDb(self, db: Database, styleName: str) -> ObjectId: ...
    def SetTextAttachmentType(self, textAttachmentType: TextAttachmentType, leaderDirection: LeaderDirectionType) -> None: ...

class MText(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.MText"""
    def __init__(self, *args) -> None: ...
    Height: float
    ColumnFlowReversed: bool
    ColumnGutterWidth: float
    ColumnWidth: float
    ColumnAutoHeight: bool
    ColumnCount: int
    ColumnType: ColumnType
    LineSpaceDistance: float
    ShowBorders: bool
    UseBackgroundColor: bool
    BackgroundTransparency: Transparency
    BackgroundScaleFactor: float
    BackgroundFillColor: Color
    BackgroundFill: bool
    LineSpacingFactor: float
    LineSpacingStyle: LineSpacingStyle
    BlockEnd: str
    BlockBegin: str
    AlignChange: str
    StackStart: str
    ParagraphBreak: str
    LineBreak: str
    TrackChange: str
    ObliqueChange: str
    WidthChange: str
    HeightChange: str
    FontChange: str
    ColorChange: str
    StrikethroughOff: str
    StrikethroughOn: str
    UnderlineOff: str
    UnderlineOn: str
    OverlineOff: str
    OverlineOn: str
    NonBreakSpace: str
    ActualWidth: float
    ActualHeight: float
    Text: str
    ContentsRTF: str
    Contents: str
    FlowDirection: FlowDirection
    Attachment: AttachmentPoint
    TextHeight: float
    TextStyleName: str
    TextStyleId: ObjectId
    Descent: float
    Ascent: float
    Width: float
    Rotation: float
    Direction: Vector3d
    Normal: Vector3d
    Location: Point3d
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def ConvertFieldToText(self, ) -> None: ...
    def CorrectSpelling(self, ) -> int: ...
    def ExplodeFragments(self, enumerator: MTextFragmentCallback, userData: object, context: WorldDraw) -> None: ...
    def GetBoundingPoints(self, ) -> Point3dCollection: ...
    def GetColumnHeight(self, index: int) -> float: ...
    def SetAttachmentMovingLocation(self, value: AttachmentPoint) -> None: ...
    def SetColumnHeight(self, index: int, height: float) -> None: ...
    def SetContentsRtf(self, value: str) -> int: ...
    def SetDynamicColumns(self, width: float, gutter: float, auto_height: bool) -> None: ...
    def SetStaticColumns(self, width: float, gutter: float, count: int) -> None: ...
    def getMTextWithFieldCodes(self, ) -> str: ...

class MTextFragment(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.MTextFragment"""
    def __init__(self, *args) -> None: ...
    Italic: bool
    Bold: bool
    TrueTypeFont: str
    Strikethrough: bool
    Overlined: bool
    Underlined: bool
    StackBottom: bool
    StackTop: bool
    Color: EntityColor
    TrackingFactor: float
    ObliqueAngle: float
    WidthFactor: float
    CapsHeight: float
    Extents: Point2d
    BigFont: str
    ShxFont: str
    Text: str
    Direction: Vector3d
    Normal: Vector3d
    Location: Point3d
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetOverLinePoints(self, ) -> list: ...
    def GetStrikethroughPoints(self, ) -> list: ...
    def GetUnderLinePoints(self, ) -> list: ...

class MTextFragmentCallback:
    """.NET: Autodesk.AutoCAD.DatabaseServices.MTextFragmentCallback"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, __unnamed000: MTextFragment, __unnamed001: object, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> MTextFragmentCallbackStatus: ...
    def Invoke(self, A_0: MTextFragment, A_1: object) -> MTextFragmentCallbackStatus: ...

class MTextFragmentCallbackStatus:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.MTextFragmentCallbackStatus"""
    def __init__(self, *args) -> None: ...
    Terminate: int  # = 0
    Continue: int  # = 1
class MaintenanceReleaseVersion:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.MaintenanceReleaseVersion"""
    def __init__(self, *args) -> None: ...
    Release0: int  # = 0
    ReleaseExtendedNewest: int  # = 1
    Release1: int  # = 1
    Release2: int  # = 2
    Release3: int  # = 3
    Release4: int  # = 4
    Release5: int  # = 5
    Release6: int  # = 6
    Release7: int  # = 7
    Release8: int  # = 8
    Release9: int  # = 9
    Release10: int  # = 10
    Release11: int  # = 11
    Release12: int  # = 12
    Release13: int  # = 13
    Release14: int  # = 14
    Release15: int  # = 15
    Release16: int  # = 16
    Release17: int  # = 17
    Release18: int  # = 18
    Release19: int  # = 19
    Release20: int  # = 20
    Release21: int  # = 21
    Release22: int  # = 22
    Release23: int  # = 23
    Release24: int  # = 24
    Release25: int  # = 25
    Release26: int  # = 26
    Release27: int  # = 27
    Release28: int  # = 28
    Release29: int  # = 29
    Release30: int  # = 30
    Release31: int  # = 31
    Release32: int  # = 32
    Release33: int  # = 33
    Release34: int  # = 34
    Release35: int  # = 35
    Release36: int  # = 36
    Release37: int  # = 37
    Release38: int  # = 38
    Release39: int  # = 39
    Release40: int  # = 40
    Release41: int  # = 41
    Release42: int  # = 42
    Release43: int  # = 43
    Release44: int  # = 44
    Release45: int  # = 45
    Release46: int  # = 46
    Release47: int  # = 47
    Release48: int  # = 48
    Release49: int  # = 49
    Release50: int  # = 50
    Release51: int  # = 51
    Release52: int  # = 52
    Release53: int  # = 53
    Release54: int  # = 54
    Release55: int  # = 55
    Release56: int  # = 56
    Release57: int  # = 57
    Release58: int  # = 58
    Release59: int  # = 59
    Release60: int  # = 60
    Release61: int  # = 61
    Release62: int  # = 62
    Release63: int  # = 63
    Release64: int  # = 64
    Release65: int  # = 65
    Release66: int  # = 66
    Release67: int  # = 67
    Release68: int  # = 68
    Release69: int  # = 69
    Release70: int  # = 70
    Release71: int  # = 71
    Release72: int  # = 72
    Release73: int  # = 73
    Release74: int  # = 74
    Release75: int  # = 75
    Release76: int  # = 76
    Release77: int  # = 77
    Release78: int  # = 78
    Release79: int  # = 79
    Release80: int  # = 80
    Release81: int  # = 81
    Release82: int  # = 82
    Release83: int  # = 83
    Release84: int  # = 84
    Release85: int  # = 85
    Release86: int  # = 86
    Release87: int  # = 87
    Release88: int  # = 88
    Release89: int  # = 89
    Release90: int  # = 90
    Release91: int  # = 91
    Release92: int  # = 92
    Release93: int  # = 93
    Release94: int  # = 94
    Release95: int  # = 95
    Release96: int  # = 96
    Release97: int  # = 97
    Release98: int  # = 98
    Release99: int  # = 99
    Release100: int  # = 100
    Release101: int  # = 101
    Release102: int  # = 102
    Release103: int  # = 103
    Release104: int  # = 104
    Release105: int  # = 105
    Release106: int  # = 106
    Release107: int  # = 107
    Release108: int  # = 108
    Release109: int  # = 109
    Release110: int  # = 110
    Release111: int  # = 111
    Release112: int  # = 112
    Release113: int  # = 113
    Release114: int  # = 114
    Release115: int  # = 115
    Release116: int  # = 116
    Release117: int  # = 117
    Release118: int  # = 118
    Release119: int  # = 119
    Release120: int  # = 120
    Release121: int  # = 121
    Release122: int  # = 122
    Release123: int  # = 123
    Release124: int  # = 124
    ReleaseCheckExtended: int  # = 125
    Release125: int  # = 125
    Release126: int  # = 126
    Release127: int  # = 127
    Release128: int  # = 128
    Release129: int  # = 129
    Release130: int  # = 130
    Release131: int  # = 131
    Release132: int  # = 132
    Release133: int  # = 133
    Release134: int  # = 134
    Release135: int  # = 135
    Release136: int  # = 136
    Release137: int  # = 137
    Release138: int  # = 138
    Release139: int  # = 139
    Release140: int  # = 140
    Release141: int  # = 141
    Release142: int  # = 142
    Release143: int  # = 143
    Release144: int  # = 144
    Release145: int  # = 145
    Release146: int  # = 146
    Release147: int  # = 147
    Release148: int  # = 148
    Release149: int  # = 149
    Release150: int  # = 150
    Release151: int  # = 151
    Release152: int  # = 152
    Release153: int  # = 153
    Release154: int  # = 154
    Release155: int  # = 155
    Release156: int  # = 156
    Release157: int  # = 157
    Release158: int  # = 158
    Release159: int  # = 159
    Release160: int  # = 160
    Release2010Newest: int  # = 226
    Release2010Max: int  # = 255
    ReleaseNewest: int  # = 427
    ReleaseCurrent: int  # = 427
    ReleaseExtendedCurrent: int  # = 477
    ReleaseUnknown: int  # = 2147483646
    ReleaseMax: int  # = 2147483647
class MatchProperties(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.MatchProperties"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CopyProperties(self, sourceEntity: Entity, targetEntity: Entity, flag: int) -> None: ...

class Material(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Material"""
    def __init__(self, *args) -> None: ...
    FinalGather: FinalGatherMode
    GlobalIllumination: GlobalIlluminationMode
    Anonymous: bool
    NormalMap: MaterialNormalMapComponent
    Luminance: float
    LuminanceMode: LuminanceMode
    TwoSided: bool
    TransmittanceScale: float
    ReflectanceScale: float
    IndirectBumpScale: float
    ColorBleedScale: float
    Mode: Mode
    ChannelFlags: ChannelFlags
    IlluminationModel: IlluminationModel
    Reflectivity: float
    SelfIllumination: float
    Translucence: float
    Refraction: MaterialRefractionComponent
    Bump: MaterialMap
    Opacity: MaterialOpacityComponent
    Reflection: MaterialMap
    Specular: MaterialSpecularComponent
    Diffuse: MaterialDiffuseComponent
    Ambient: MaterialColor
    Description: str
    Name: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class MeasurementValue:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.MeasurementValue"""
    def __init__(self, *args) -> None: ...
    English: int  # = 0
    Metric: int  # = 1
class MergeCellStyleOption:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.MergeCellStyleOption"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    CopyDuplicates: int  # = 1
    OverwriteDuplicates: int  # = 2
    ConvertDuplicatesToOverrrides: int  # = 4
    IgnoreNewStyles: int  # = 8
class MeshDataCollection:
    """.NET: Autodesk.AutoCAD.DatabaseServices.MeshDataCollection"""
    def __init__(self, *args) -> None: ...
    MaterialIdArray: ObjectIdCollection
    ColorArray: EntityColorCollection
    FaceArray: Int32Collection
    VertexArray: Point3dCollection

class MeshFaceterData:
    """.NET: Autodesk.AutoCAD.DatabaseServices.MeshFaceterData"""
    def __init__(self, *args) -> None: ...
    FaceterMeshType: int
    FaceterMinVGrid: int
    FaceterMinUGrid: int
    FaceterMaxGrid: int
    FaceterMaxEdgeLength: float
    FaceterGridRatio: float
    FaceterDevNormal: float
    FaceterDevSurface: float

class MeshPointMap:
    """.NET: Autodesk.AutoCAD.DatabaseServices.MeshPointMap"""
    def __init__(self, *args) -> None: ...
    DestPoint: Point2d
    SourcePoint: Point2d

class MeshPointMaps:
    """.NET: Autodesk.AutoCAD.DatabaseServices.MeshPointMaps"""
    def __init__(self, *args) -> None: ...
    DestPonints: Point2dCollection
    SourcePonints: Point2dCollection

class MidPointConstraint(GeometricalConstraint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.MidPointConstraint"""
    def __init__(self, *args) -> None: ...
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Mline(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Mline"""
    def __init__(self, *args) -> None: ...
    NumberOfVertices: int
    SupressEndCaps: bool
    SupressStartCaps: bool
    IsClosed: bool
    Normal: Vector3d
    Scale: float
    Justification: MlineJustification
    Style: ObjectId
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AppendSegment(self, newVertex: Point3d) -> None: ...
    def Element(self, pt: Point3d) -> int: ...
    def GetClosestPointTo(self, givenPoint: Point3d, normal: Vector3d, extend: bool, excludeCaps: bool) -> Point3d: ...
    def MoveVertexAt(self, index: int, newPosition: Point3d) -> None: ...
    def RemoveLastSegment(self, lastVertex: Point3d) -> None: ...
    def VertexAt(self, index: int) -> Point3d: ...

class MlineJustification:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.MlineJustification"""
    def __init__(self, *args) -> None: ...
    Top: int  # = 0
    Zero: int  # = 1
    Bottom: int  # = 2
class MlineStyle(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.MlineStyle"""
    def __init__(self, *args) -> None: ...
    Elements: MlineStyleElementCollection
    EndAngle: float
    StartAngle: float
    Filled: bool
    FillColor: Color
    EndInnerArcs: bool
    EndRoundCap: bool
    EndSquareCap: bool
    StartInnerArcs: bool
    StartRoundCap: bool
    StartSquareCap: bool
    ShowMiters: bool
    Name: str
    Description: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Reset(self, ) -> None: ...
    def Set(self, source: MlineStyle, checkIfReferenced: bool) -> None: ...

class MlineStyleElement:
    """.NET: Autodesk.AutoCAD.DatabaseServices.MlineStyleElement"""
    def __init__(self, *args) -> None: ...
    LinetypeId: ObjectId
    Color: Color
    Offset: float
    def ToString(self, provider: IFormatProvider) -> str: ...

class MlineStyleElementCollection:
    """.NET: Autodesk.AutoCAD.DatabaseServices.MlineStyleElementCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: MlineStyleElement
    def Add(self, element: MlineStyleElement, checkIfReferenced: bool) -> int: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> MlineStyleElementCollectionEnumerator: ...
    def RemoveAt(self, index: int) -> None: ...

class MlineStyleElementCollectionEnumerator:
    """.NET: Autodesk.AutoCAD.DatabaseServices.MlineStyleElementCollectionEnumerator"""
    def __init__(self, *args) -> None: ...
    Current: MlineStyleElement
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ModelDocViewLabelAlignmentType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.ModelDocViewLabelAlignmentType"""
    def __init__(self, *args) -> None: ...
    AlignmentLeft: int  # = 0
    AlignmentCenter: int  # = 1
    AlignmentRight: int  # = 2
class ModelDocViewLabelAttachmentPoint:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.ModelDocViewLabelAttachmentPoint"""
    def __init__(self, *args) -> None: ...
    AboveView: int  # = 0
    BelowView: int  # = 1
class ModelerFlavor:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.ModelerFlavor"""
    def __init__(self, *args) -> None: ...
    Full: int  # = 0
    RegionsOnly: int  # = 1
    ObjectsOnly: int  # = 2
class ModifiesOwnerAttribute(Attribute):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ModifiesOwnerAttribute"""
    def __init__(self, *args) -> None: ...
    TypeId: object

class MoveGripPointsFlags:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.MoveGripPointsFlags"""
    def __init__(self, *args) -> None: ...
    Osnapped: int  # = 1
    Polar: int  # = 2
    ObjectTrack: int  # = 4
    ZDir: int  # = 8
    Keyboard: int  # = 16
class MoveType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.MoveType"""
    def __init__(self, *args) -> None: ...
    MoveAllPoints: int  # = 0
    MoveAllExceptArrowHeaderPoints: int  # = 1
    MoveContentAndDoglegPoints: int  # = 2
class MultiModesGripPE(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.MultiModesGripPE"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CurrentMode(self, entity: Entity, gripData: GripData) -> GripMode: ...
    def CurrentModeId(self, entity: Entity, gripData: GripData) -> int: ...
    def GetGripModes(self, entity: Entity, gripData: GripData, modes: GripModeCollection, curMode: int) -> bool: ...
    def GetGripType(self, entity: Entity, gripData: GripData) -> GripType: ...
    def Reset(self, entity: Entity) -> None: ...
    def SetCurrentMode(self, entity: Entity, gripData: GripData, curMode: int) -> bool: ...

class NewLayerNotification:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.NewLayerNotification"""
    def __init__(self, *args) -> None: ...
    NoNewLayerNotification: int  # = 0
    NotifyOnPlot: int  # = 1
    NotifyOnOpen: int  # = 2
    NotifyOnXrefAttachAndReload: int  # = 4
    NotifyOnLayerStateRestore: int  # = 8
    NotifyOnSave: int  # = 16
    NotifyOnInsert: int  # = 32
class NormalConstraint(GeometricalConstraint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.NormalConstraint"""
    def __init__(self, *args) -> None: ...
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Notifier:
    """.NET: Autodesk.AutoCAD.DatabaseServices.Notifier"""
    def __init__(self, *args) -> None: ...
    def OnPropertyChanged(self, propertyName: str) -> None: ...

class NurbSurface(Surface):
    """.NET: Autodesk.AutoCAD.DatabaseServices.NurbSurface"""
    def __init__(self, *args) -> None: ...
    NumberOfSpansInV: int
    NumberOfSpansInU: int
    IsRational: bool
    PeriodInV: float
    PeriodInU: float
    IsPeriodicInV: bool
    IsPeriodicInU: bool
    IsClosedInV: bool
    IsClosedInU: bool
    DegreeInV: int
    DegreeInU: int
    NumberOfKnotsInV: int
    NumberOfKnotsInU: int
    VKnots: KnotCollection
    UKnots: KnotCollection
    NumberOfControlPointsInV: int
    NumberOfControlPointsInU: int
    ControlPoints: Point3dCollection
    GeometricExtents: Extents3d
    UsesGraphicsCache: bool
    Perimeter: float
    WireframeType: WireframeTypeEnum
    VIsoLineDensity: int
    UIsoLineDensity: int
    ModificationActionBodyIds: ObjectIdCollection
    CreationActionBodyId: ObjectId
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Evaluate(self, u: float, v: float, pos: Point3d, uDeriv: Vector3d, vDeriv: Vector3d, uuDeriv: Vector3d, uvDeriv: Vector3d, vvDeriv: Vector3d) -> None: ...
    def GetControlPointAt(self, uIndex: int, vIndex: int) -> Point3d: ...
    def GetIsolineAtU(self, u: float) -> list: ...
    def GetIsolineAtV(self, v: float) -> list: ...
    def GetNormal(self, u: float, v: float) -> Vector3d: ...
    def GetParameterOfPoint(self, point: Point3d, u: float, v: float) -> None: ...
    def GetWeight(self, uIndex: int, vIndex: int) -> float: ...
    def InsertControlPointsAtU(self, u: float, vCtrlPts: Point3dCollection, vWeights: DoubleCollection) -> None: ...
    def InsertControlPointsAtV(self, v: float, uCtrlPts: Point3dCollection, uWeights: DoubleCollection) -> None: ...
    def InsertKnotAtU(self, u: float) -> None: ...
    def InsertKnotAtV(self, v: float) -> None: ...
    def IsPlanar(self, ptOnSurface: Point3d, normal: Vector3d) -> bool: ...
    def IsPointOnSurface(self, point: Point3d) -> bool: ...
    def ModifyPosition(self, u: float, v: float, point: Point3d) -> None: ...
    def ModifyPositionAndTangent(self, u: float, v: float, point: Point3d, uDeriv: Vector3d, vDeriv: Vector3d) -> None: ...
    def Rebuild(self, uDegree: int, vDegree: int, numUCtrlPts: int, numVCtrlPts: int, bRestore: bool) -> None: ...
    def RemoveControlPointsAtU(self, uIndex: int) -> None: ...
    def RemoveControlPointsAtV(self, vIndex: int) -> None: ...
    def Set(self, uDegree: int, vDegree: int, rational: bool, uNumControlPoints: int, vNumControlPoints: int, ctrlPts: Point3dCollection, weights: DoubleCollection, uKnots: KnotCollection, vKnots: KnotCollection) -> None: ...
    def SetControlPointAt(self, uIndex: int, vIndex: int, point: Point3d) -> None: ...
    def SetControlPoints(self, uCount: int, vCount: int, points: Point3dCollection) -> None: ...
    def SetWeight(self, uIndex: int, vIndex: int, weight: float) -> None: ...

class NurbsData:
    """.NET: Autodesk.AutoCAD.DatabaseServices.NurbsData"""
    def __init__(self, *args) -> None: ...
    KnotTolerance: float
    ControlPointTolerance: float
    Periodic: bool
    Closed: bool
    Rational: bool
    Degree: int
    def Equals(self, obj: object) -> bool: ...
    def GetControlPoints(self, ) -> Point3dCollection: ...
    def GetHashCode(self, ) -> int: ...
    def GetKnots(self, ) -> DoubleCollection: ...
    def GetWeights(self, ) -> DoubleCollection: ...
    def IsEqualTo(self, other: NurbsData, tolerance: Tolerance) -> bool: ...

class ObjectClosedEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ObjectClosedEventArgs"""
    def __init__(self, *args) -> None: ...
    Id: ObjectId

class ObjectClosedEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.ObjectClosedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: ObjectClosedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: ObjectClosedEventArgs) -> None: ...

class ObjectContext(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ObjectContext"""
    def __init__(self, *args) -> None: ...
    CollectionName: str
    UniqueIdentifier: IntPtr
    Name: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ObjectContextCollection(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ObjectContextCollection"""
    def __init__(self, *args) -> None: ...
    CurrentContext: ObjectContext
    Name: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddContext(self, ctxt: ObjectContext) -> None: ...
    def GetContext(self, contextName: str) -> ObjectContext: ...
    def GetEnumerator(self, ) -> ObjectContextCollectionEnumerator: ...
    def HasContext(self, contextName: str) -> bool: ...
    def IEnumerable.GetEnumerator(self, ) -> IEnumerator: ...
    def RemoveContext(self, contextName: str) -> None: ...

class ObjectContextCollectionEnumerator(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ObjectContextCollectionEnumerator"""
    def __init__(self, *args) -> None: ...
    Current: ObjectContext
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def IEnumerator.get_Current(self, ) -> object: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ObjectContextManager(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ObjectContextManager"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetContextCollection(self, collectionName: str) -> ObjectContextCollection: ...
    def RegisterContextCollection(self, collectionName: str, collection: ObjectContextCollection) -> None: ...
    def UnregisterContextCollection(self, collectionName: str) -> None: ...

class ObjectErasedEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ObjectErasedEventArgs"""
    def __init__(self, *args) -> None: ...
    Erased: bool
    DBObject: DBObject

class ObjectErasedEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.ObjectErasedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: ObjectErasedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: ObjectErasedEventArgs) -> None: ...

class ObjectEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ObjectEventArgs"""
    def __init__(self, *args) -> None: ...
    DBObject: DBObject

class ObjectEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.ObjectEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: ObjectEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: ObjectEventArgs) -> None: ...

class ObjectId:
    """.NET: Autodesk.AutoCAD.DatabaseServices.ObjectId"""
    def __init__(self, *args) -> None: ...
    IsResident: bool
    Null: ObjectId
    NonForwardedHandle: Handle
    Handle: Handle
    OriginalDatabase: Database
    ObjectLeftOnDisk: bool
    IsEffectivelyErased: bool
    IsErased: bool
    IsWellBehaved: bool
    IsValid: bool
    IsNull: bool
    Database: Database
    OldIdPtr: IntPtr
    OldId: int
    ObjectClass: RXClass
    def Compare(self, value1: ObjectId) -> bool: ...
    def CompareTo(self, other: ObjectId) -> int: ...
    def ConvertToRedirectedId(self, ) -> ObjectId: ...
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def GetMetaObject(self, parameter: Expression) -> DynamicMetaObject: ...
    def GetObject(self, mode: OpenMode, openErased: bool, forceOpenOnLockedLayer: bool) -> DBObject: ...
    def Open(self, mode: OpenMode, openErased: bool, forceOpenOnLockedLayer: bool) -> DBObject: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class ObjectIdCollection(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ObjectIdCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: ObjectId
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, value: ObjectId) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: ObjectId) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: ObjectId) -> int: ...
    def Insert(self, index: int, value: ObjectId) -> None: ...
    def Remove(self, value: ObjectId) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class ObjectIdGraph(Graph):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ObjectIdGraph"""
    def __init__(self, *args) -> None: ...
    IsEmpty: bool
    NumNodes: int
    RootNode: GraphNode
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddNode(self, nodeToAdd: ObjectIdGraphNode) -> None: ...
    def DelNode(self, nodeToDelete: ObjectIdGraphNode) -> None: ...
    def FindNode(self, id: ObjectId) -> ObjectIdGraphNode: ...
    def IdNode(self, index: int) -> ObjectIdGraphNode: ...

class ObjectIdGraphNode(GraphNode):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ObjectIdGraphNode"""
    def __init__(self, *args) -> None: ...
    Id: ObjectId
    IsCycleNode: bool
    NumCycleIn: int
    NumCycleOut: int
    Owner: Graph
    NextCycleNode: GraphNode
    NumIn: int
    NumOut: int
    Data: IntPtr
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(unmanagedPointer: IntPtr, autoDelete: bool) -> ObjectIdGraphNode: ...

class ObjectOverrule(Overrule):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ObjectOverrule"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Cancel(self, dbObject: DBObject) -> None: ...
    def Close(self, dbObject: DBObject) -> None: ...
    def DeepClone(self, dbObject: DBObject, ownerObject: DBObject, idMap: IdMapping, isPrimary: bool) -> DBObject: ...
    def Erase(self, dbObject: DBObject, erasing: bool) -> None: ...
    def Open(self, dbObject: DBObject, mode: OpenMode) -> None: ...
    def SetCustomFilter(self, ) -> None: ...
    def SetExtensionDictionaryEntryFilter(self, entryName: str) -> None: ...
    def SetIdFilter(self, ids: list) -> None: ...
    def SetNoFilter(self, ) -> None: ...
    def SetXDataFilter(self, registeredApplicationName: str) -> None: ...
    def WblockClone(self, dbObject: DBObject, ownerObject: RXObject, idMap: IdMapping, isPrimary: bool) -> DBObject: ...

class ObjectSnapContext:
    """.NET: Autodesk.AutoCAD.DatabaseServices.ObjectSnapContext"""
    def __init__(self, *args) -> None: ...
    ViewTransform: Matrix3d
    LastPoint: Point3d
    PickPoint: Point3d
    GraphicsSystemSelectionMark: int
    PickedObject: Entity

class ObjectSnapInfo:
    """.NET: Autodesk.AutoCAD.DatabaseServices.ObjectSnapInfo"""
    def __init__(self, *args) -> None: ...
    SnapCurves: Curve3dCollection
    SnapPoints: Point3dCollection

class ObjectSnapModes:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.ObjectSnapModes"""
    def __init__(self, *args) -> None: ...
    ModeEnd: int  # = 1
    ModeMid: int  # = 2
    ModeCenter: int  # = 3
    ModeNode: int  # = 4
    ModeQuad: int  # = 5
    ModeIns: int  # = 7
    ModePerpendicular: int  # = 8
    ModeTangent: int  # = 9
    ModeNear: int  # = 10
class ObjectTypeAttribute(Attribute):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ObjectTypeAttribute"""
    def __init__(self, *args) -> None: ...
    ObjectType: Type
    TypeId: object

class Ole2Frame(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Ole2Frame"""
    def __init__(self, *args) -> None: ...
    OleObject: object
    LockAspect: bool
    ScaleHeight: float
    ScaleWidth: float
    WcsHeight: float
    WcsWidth: float
    Rotation: float
    AutoOutputQuality: int
    OutputQuality: int
    LinkPath: str
    LinkName: str
    IsLinked: bool
    Type: ItemType
    UserType: str
    Position2d: Rectangle
    Position3d: Rectangle3d
    Location: Point3d
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class OpenCloseTransaction(Transaction):
    """.NET: Autodesk.AutoCAD.DatabaseServices.OpenCloseTransaction"""
    def __init__(self, *args) -> None: ...
    TransactionManager: TransactionManager
    NumberOfOpenedObjects: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Abort(self, ) -> None: ...
    def AddNewlyCreatedDBObject(self, obj: DBObject, add: bool) -> None: ...
    def Commit(self, ) -> None: ...
    def GetObject(self, id: ObjectId, mode: OpenMode, openErased: bool, forceOpenOnLockedLayer: bool) -> DBObject: ...

class OpenMode:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.OpenMode"""
    def __init__(self, *args) -> None: ...
    ForRead: int  # = 0
    ForWrite: int  # = 1
    ForNotify: int  # = 2
class OpenModeAttribute(Attribute):
    """.NET: Autodesk.AutoCAD.DatabaseServices.OpenModeAttribute"""
    def __init__(self, *args) -> None: ...
    OpenMode: OpenMode
    TypeId: object

class OrdinateDimension(Dimension):
    """.NET: Autodesk.AutoCAD.DatabaseServices.OrdinateDimension"""
    def __init__(self, *args) -> None: ...
    LeaderEndPoint: Point3d
    DefiningPoint: Point3d
    Origin: Point3d
    UsingXAxis: bool
    UsingYAxis: bool
    Dimaltmzf: float
    Dimmzf: float
    Dimaltmzs: str
    Dimmzs: str
    Dimblk2: ObjectId
    Dimblk1: ObjectId
    Dimblk: ObjectId
    Dimpost: str
    Dimapost: str
    Dimzin: int
    Dimupt: bool
    Dimtzin: int
    Dimtxtdirection: bool
    Dimtxt: float
    TextStyleId: ObjectId
    Dimtvp: float
    Dimtsz: float
    Dimtp: float
    Dimtolj: int
    Dimtol: bool
    Dimtoh: bool
    Dimtofl: bool
    Dimtmove: int
    Dimtm: float
    Dimtix: bool
    Dimtih: bool
    Dimtfillclr: Color
    Dimtfill: int
    Dimtfac: float
    Dimtdec: int
    Dimtad: int
    Dimsoxd: bool
    Dimse2: bool
    Dimse1: bool
    Dimsd2: bool
    Dimsd1: bool
    Dimscale: float
    Dimsah: bool
    Dimrnd: float
    DimensionStyleName: str
    CenterMarkSize: float
    CenterMarkType: DimensionCenterMarkType
    ToleranceSuppressZeroInches: bool
    ToleranceSuppressZeroFeet: bool
    ToleranceSuppressTrailingZeros: bool
    ToleranceSuppressLeadingZeros: bool
    AltToleranceSuppressZeroInches: bool
    AltToleranceSuppressZeroFeet: bool
    AltToleranceSuppressTrailingZeros: bool
    AltToleranceSuppressLeadingZeros: bool
    AltSuppressZeroInches: bool
    AltSuppressZeroFeet: bool
    AltSuppressTrailingZeros: bool
    AltSuppressLeadingZeros: bool
    AlternateSuffix: str
    AlternatePrefix: str
    SuppressZeroInches: bool
    SuppressZeroFeet: bool
    SuppressTrailingZeros: bool
    SuppressLeadingZeros: bool
    SuppressAngularTrailingZeros: bool
    SuppressAngularLeadingZeros: bool
    Suffix: str
    Prefix: str
    Dimlwe: LineWeight
    Dimlwd: LineWeight
    Dimlunit: int
    Dimltype: ObjectId
    Dimltex2: ObjectId
    Dimltex1: ObjectId
    Dimlim: bool
    Dimlfac: float
    Dimldrblk: ObjectId
    Dimjust: int
    Dimjogang: float
    Dimgap: float
    Dimfxlen: float
    DimfxlenOn: bool
    Dimfrac: int
    Dimexo: float
    Dimexe: float
    Dimdsep: str
    Dimdli: float
    Dimdle: float
    Dimdec: int
    Dimclrt: Color
    Dimclre: Color
    Dimclrd: Color
    Dimcen: float
    Dimazin: int
    Dimaunit: int
    Dimatfit: int
    Dimasz: float
    Dimarcsym: int
    Dimaltz: int
    Dimaltu: int
    Dimalttz: int
    Dimalttd: int
    Dimaltrnd: float
    Dimaltf: float
    Dimaltd: int
    Dimalt: bool
    Dimadec: int
    DynamicDimension: bool
    Measurement: float
    DimBlockPosition: Point3d
    DimBlockId: ObjectId
    HorizontalRotation: float
    TextLineSpacingFactor: float
    TextLineSpacingStyle: LineSpacingStyle
    TextAttachment: AttachmentPoint
    DimensionStyle: ObjectId
    TextRotation: float
    DimensionText: str
    Elevation: float
    Normal: Vector3d
    UsingDefaultTextPosition: bool
    TextPosition: Point3d
    TextDefinedSize: Vector2d
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class OrthographicView:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.OrthographicView"""
    def __init__(self, *args) -> None: ...
    NonOrthoView: int  # = 0
    TopView: int  # = 1
    BottomView: int  # = 2
    FrontView: int  # = 3
    BackView: int  # = 4
    LeftView: int  # = 5
    RightView: int  # = 6
class OsnapOverrule(Overrule):
    """.NET: Autodesk.AutoCAD.DatabaseServices.OsnapOverrule"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetObjectSnapPoints(self, entity: Entity, snapMode: ObjectSnapModes, gsSelectionMark: IntPtr, pickPoint: Point3d, lastPoint: Point3d, viewTransform: Matrix3d, snapPoints: Point3dCollection, geometryIds: IntegerCollection, insertionMat: Matrix3d) -> None: ...
    def IsContentSnappable(self, entity: Entity) -> bool: ...
    def SetCustomFilter(self, ) -> None: ...
    def SetExtensionDictionaryEntryFilter(self, entryName: str) -> None: ...
    def SetIdFilter(self, ids: list) -> None: ...
    def SetNoFilter(self, ) -> None: ...
    def SetXDataFilter(self, registeredApplicationName: str) -> None: ...

class PCAdsName:
    """.NET: Autodesk.AutoCAD.DatabaseServices.PCAdsName"""
    def __init__(self, *args) -> None: ...
    ...

class PaperOrientationStates:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.PaperOrientationStates"""
    def __init__(self, *args) -> None: ...
    True_: int  # = 0
    False_: int  # = 1
    NotApplicable: int  # = 2
class ParallelConstraint(GeometricalConstraint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ParallelConstraint"""
    def __init__(self, *args) -> None: ...
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ParameterValueSet(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ParameterValueSet"""
    def __init__(self, *args) -> None: ...
    DataType: DataType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CopyFrom(self, obj: RXObject) -> None: ...
    def GetClosestLegalValue(self, value: ResultBuffer) -> ResultBuffer: ...
    def ValueIsLegal(self, value: ResultBuffer) -> bool: ...

class ParameterValueSetIncrement(ParameterValueSetMinMax):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ParameterValueSetIncrement"""
    def __init__(self, *args) -> None: ...
    Increment: float
    Maximum: float
    Minimum: float
    DataType: DataType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ParameterValueSetList(ParameterValueSet):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ParameterValueSetList"""
    def __init__(self, *args) -> None: ...
    Values: list
    DataType: DataType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ParameterValueSetMinMax(ParameterValueSet):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ParameterValueSetMinMax"""
    def __init__(self, *args) -> None: ...
    Maximum: float
    Minimum: float
    DataType: DataType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ParseOption:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.ParseOption"""
    def __init__(self, *args) -> None: ...
    ParseOptionNone: int  # = 0
    SetDefaultFormat: int  # = 1
    PreserveMtextFormat: int  # = 2
class PasswordOptions:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.PasswordOptions"""
    def __init__(self, *args) -> None: ...
    Default: int  # = 0
    UpperCase: int  # = 1
    IsExternalReference: int  # = 2
class PathOption:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.PathOption"""
    def __init__(self, *args) -> None: ...
    NoPath: int  # = 1
    RelativePath: int  # = 2
    AbsolutePath: int  # = 3
    PathAndFile: int  # = 4
class PathRef(GeomRef):
    """.NET: Autodesk.AutoCAD.DatabaseServices.PathRef"""
    def __init__(self, *args) -> None: ...
    EdgeRefs: list
    IsEmpty: bool
    IsValid: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetEntityArray(self, bConcatenate: bool) -> list: ...
    def IsEqualTo(self, curve: Curve3d) -> bool: ...
    def IsReferencePath(self, ) -> bool: ...

class PatternDefinition:
    """.NET: Autodesk.AutoCAD.DatabaseServices.PatternDefinition"""
    def __init__(self, *args) -> None: ...
    OffsetY: float
    OffsetX: float
    BaseY: float
    BaseX: float
    Angle: float
    def GetDashes(self, ) -> DoubleCollection: ...

class PdfDefinition(UnderlayDefinition):
    """.NET: Autodesk.AutoCAD.DatabaseServices.PdfDefinition"""
    def __init__(self, *args) -> None: ...
    Loaded: bool
    UnderlayItem: UnderlayItem
    ItemName: str
    ActiveFileName: str
    SourceFileName: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PdfReference(UnderlayReference):
    """.NET: Autodesk.AutoCAD.DatabaseServices.PdfReference"""
    def __init__(self, *args) -> None: ...
    IsClipInverted: bool
    Path: str
    NameOfSheet: str
    Name: str
    Width: float
    Height: float
    AdjustColorForBackground: bool
    UnderlayLayerCollection: UnderlayLayerCollection
    Monochrome: bool
    Fade: int
    Contrast: int
    IsOn: bool
    IsClipped: bool
    Transform: Matrix3d
    DefinitionId: ObjectId
    Normal: Vector3d
    Rotation: float
    ScaleFactors: Scale3d
    Position: Point3d
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PerpendicularConstraint(GeometricalConstraint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.PerpendicularConstraint"""
    def __init__(self, *args) -> None: ...
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PhysicalIntensityMethod:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.PhysicalIntensityMethod"""
    def __init__(self, *args) -> None: ...
    PeakIntensity: int  # = 0
    Flux: int  # = 1
    Illuminance: int  # = 2
class PlaceHolder(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.PlaceHolder"""
    def __init__(self, *args) -> None: ...
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Planarity:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.Planarity"""
    def __init__(self, *args) -> None: ...
    NonPlanar: int  # = 0
    Planar: int  # = 1
    Linear: int  # = 2
class PlaneSurface(Surface):
    """.NET: Autodesk.AutoCAD.DatabaseServices.PlaneSurface"""
    def __init__(self, *args) -> None: ...
    GeometricExtents: Extents3d
    UsesGraphicsCache: bool
    Perimeter: float
    WireframeType: WireframeTypeEnum
    VIsoLineDensity: int
    UIsoLineDensity: int
    ModificationActionBodyIds: ObjectIdCollection
    CreationActionBodyId: ObjectId
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CreateFromRegion(self, region: Region) -> None: ...

class PlotPaperUnit:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.PlotPaperUnit"""
    def __init__(self, *args) -> None: ...
    Inches: int  # = 0
    Millimeters: int  # = 1
    Pixels: int  # = 2
class PlotRotation:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.PlotRotation"""
    def __init__(self, *args) -> None: ...
    Degrees000: int  # = 0
    Degrees090: int  # = 1
    Degrees180: int  # = 2
    Degrees270: int  # = 3
class PlotSettings(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.PlotSettings"""
    def __init__(self, *args) -> None: ...
    PlotAsRaster: bool
    PlotWireframe: bool
    ShadePlotId: ObjectId
    ModelType: bool
    DrawViewportsFirst: bool
    PrintLineweights: bool
    ScaleLineweights: bool
    StdScale: float
    StdScaleType: StdScaleType
    CurrentStyleSheet: str
    CustomPrintScale: CustomScale
    UseStandardScale: bool
    PlotViewName: str
    PlotWindowArea: Extents2d
    PlotType: PlotType
    ShadePlotCustomDpi: int
    ShadePlotResLevel: ShadePlotResLevel
    ShadePlot: PlotSettingsShadePlotType
    PlotHidden: bool
    PlotCentered: bool
    PlotRotation: PlotRotation
    ShowPlotStyles: bool
    PlotPlotStyles: bool
    PlotTransparency: bool
    PlotViewportBorders: bool
    PlotPaperUnits: PlotPaperUnit
    PlotOrigin: Point2d
    CanonicalMediaName: str
    PlotPaperSize: Point2d
    PlotPaperMargins: Extents2d
    PlotConfigurationName: str
    PlotSettingsName: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddToPlotSettingsDictionary(self, toWhichDatabase: Database) -> None: ...
    def SetShadePlot(self, type: PlotSettingsShadePlotType, shadePlotId: ObjectId) -> None: ...

class PlotSettingsShadePlotType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.PlotSettingsShadePlotType"""
    def __init__(self, *args) -> None: ...
    AsDisplayed: int  # = 0
    Wireframe: int  # = 1
    Hidden: int  # = 2
    Rendered: int  # = 3
    VisualStyle: int  # = 4
    RenderPreset: int  # = 5
class PlotSettingsValidator(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.PlotSettingsValidator"""
    def __init__(self, *args) -> None: ...
    Current: PlotSettingsValidator
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetCanonicalMediaNameList(self, plotSet: PlotSettings) -> StringCollection: ...
    def GetLocaleMediaName(self, plotSet: PlotSettings, index: int) -> str: ...
    def GetPlotDeviceList(self, ) -> StringCollection: ...
    def GetPlotStyleSheetList(self, ) -> StringCollection: ...
    def RefreshLists(self, plotSet: PlotSettings) -> None: ...
    def SetCanonicalMediaName(self, plotSet: PlotSettings, mediaName: str) -> None: ...
    def SetClosestMediaName(self, plotSet: PlotSettings, paperWidth: float, paperHeight: float, units: PlotPaperUnit, matchPrintableArea: bool) -> None: ...
    def SetCurrentStyleSheet(self, plotSet: PlotSettings, styleSheetName: str) -> None: ...
    def SetCustomPrintScale(self, plotSet: PlotSettings, scale: CustomScale) -> None: ...
    def SetDefaultPlotConfig(self, plotSet: PlotSettings) -> None: ...
    def SetPlotCentered(self, plotSet: PlotSettings, isCentered: bool) -> None: ...
    def SetPlotConfigurationName(self, plotSet: PlotSettings, plotDeviceName: str, mediaName: str) -> None: ...
    def SetPlotOrigin(self, plotSet: PlotSettings, origin: Point2d) -> None: ...
    def SetPlotPaperUnits(self, plotSet: PlotSettings, units: PlotPaperUnit) -> None: ...
    def SetPlotRotation(self, plotSet: PlotSettings, rotationType: PlotRotation) -> None: ...
    def SetPlotType(self, plotSet: PlotSettings, plotAreaType: PlotType) -> None: ...
    def SetPlotViewName(self, plotSet: PlotSettings, viewName: str) -> None: ...
    def SetPlotWindowArea(self, plotSet: PlotSettings, windowArea: Extents2d) -> None: ...
    def SetStdScale(self, plotSet: PlotSettings, standardScale: float) -> None: ...
    def SetStdScaleType(self, plotSet: PlotSettings, scaleType: StdScaleType) -> None: ...
    def SetUseStandardScale(self, plotSet: PlotSettings, useStandard: bool) -> None: ...
    def SetZoomToPaperOnUpdate(self, plotSet: PlotSettings, doZoom: bool) -> None: ...

class PlotStyleDescriptor:
    """.NET: Autodesk.AutoCAD.DatabaseServices.PlotStyleDescriptor"""
    def __init__(self, *args) -> None: ...
    Type: PlotStyleNameType
    Id: ObjectId
    def Equals(self, unmanagedObjPtr: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class PlotStyleNameType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.PlotStyleNameType"""
    def __init__(self, *args) -> None: ...
    PlotStyleNameByLayer: int  # = 0
    PlotStyleNameByBlock: int  # = 1
    PlotStyleNameIsDictionaryDefault: int  # = 2
    PlotStyleNameById: int  # = 3
class PlotStyleTableChangedEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.PlotStyleTableChangedEventArgs"""
    def __init__(self, *args) -> None: ...
    NewName: str
    Id: ObjectId

class PlotStyleTableChangedEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.PlotStyleTableChangedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: PlotStyleTableChangedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: PlotStyleTableChangedEventArgs) -> None: ...

class PlotType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.PlotType"""
    def __init__(self, *args) -> None: ...
    Display: int  # = 0
    Extents: int  # = 1
    Limits: int  # = 2
    View: int  # = 3
    Window: int  # = 4
    Layout: int  # = 5
class Point3AngularDimension(Dimension):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Point3AngularDimension"""
    def __init__(self, *args) -> None: ...
    CenterPoint: Point3d
    XLine2Point: Point3d
    XLine1Point: Point3d
    ArcPoint: Point3d
    Dimaltmzf: float
    Dimmzf: float
    Dimaltmzs: str
    Dimmzs: str
    Dimblk2: ObjectId
    Dimblk1: ObjectId
    Dimblk: ObjectId
    Dimpost: str
    Dimapost: str
    Dimzin: int
    Dimupt: bool
    Dimtzin: int
    Dimtxtdirection: bool
    Dimtxt: float
    TextStyleId: ObjectId
    Dimtvp: float
    Dimtsz: float
    Dimtp: float
    Dimtolj: int
    Dimtol: bool
    Dimtoh: bool
    Dimtofl: bool
    Dimtmove: int
    Dimtm: float
    Dimtix: bool
    Dimtih: bool
    Dimtfillclr: Color
    Dimtfill: int
    Dimtfac: float
    Dimtdec: int
    Dimtad: int
    Dimsoxd: bool
    Dimse2: bool
    Dimse1: bool
    Dimsd2: bool
    Dimsd1: bool
    Dimscale: float
    Dimsah: bool
    Dimrnd: float
    DimensionStyleName: str
    CenterMarkSize: float
    CenterMarkType: DimensionCenterMarkType
    ToleranceSuppressZeroInches: bool
    ToleranceSuppressZeroFeet: bool
    ToleranceSuppressTrailingZeros: bool
    ToleranceSuppressLeadingZeros: bool
    AltToleranceSuppressZeroInches: bool
    AltToleranceSuppressZeroFeet: bool
    AltToleranceSuppressTrailingZeros: bool
    AltToleranceSuppressLeadingZeros: bool
    AltSuppressZeroInches: bool
    AltSuppressZeroFeet: bool
    AltSuppressTrailingZeros: bool
    AltSuppressLeadingZeros: bool
    AlternateSuffix: str
    AlternatePrefix: str
    SuppressZeroInches: bool
    SuppressZeroFeet: bool
    SuppressTrailingZeros: bool
    SuppressLeadingZeros: bool
    SuppressAngularTrailingZeros: bool
    SuppressAngularLeadingZeros: bool
    Suffix: str
    Prefix: str
    Dimlwe: LineWeight
    Dimlwd: LineWeight
    Dimlunit: int
    Dimltype: ObjectId
    Dimltex2: ObjectId
    Dimltex1: ObjectId
    Dimlim: bool
    Dimlfac: float
    Dimldrblk: ObjectId
    Dimjust: int
    Dimjogang: float
    Dimgap: float
    Dimfxlen: float
    DimfxlenOn: bool
    Dimfrac: int
    Dimexo: float
    Dimexe: float
    Dimdsep: str
    Dimdli: float
    Dimdle: float
    Dimdec: int
    Dimclrt: Color
    Dimclre: Color
    Dimclrd: Color
    Dimcen: float
    Dimazin: int
    Dimaunit: int
    Dimatfit: int
    Dimasz: float
    Dimarcsym: int
    Dimaltz: int
    Dimaltu: int
    Dimalttz: int
    Dimalttd: int
    Dimaltrnd: float
    Dimaltf: float
    Dimaltd: int
    Dimalt: bool
    Dimadec: int
    DynamicDimension: bool
    Measurement: float
    DimBlockPosition: Point3d
    DimBlockId: ObjectId
    HorizontalRotation: float
    TextLineSpacingFactor: float
    TextLineSpacingStyle: LineSpacingStyle
    TextAttachment: AttachmentPoint
    DimensionStyle: ObjectId
    TextRotation: float
    DimensionText: str
    Elevation: float
    Normal: Vector3d
    UsingDefaultTextPosition: bool
    TextPosition: Point3d
    TextDefinedSize: Vector2d
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PointCloud(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.PointCloud"""
    def __init__(self, *args) -> None: ...
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def RegenPointClouds() -> None: ...

class PointCloudClassificationColorRamp(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.PointCloudClassificationColorRamp"""
    def __init__(self, *args) -> None: ...
    Name: str
    NumColors: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Color(self, c: int) -> EntityColor: ...
    def SetColor(self, c: int, color: EntityColor) -> None: ...
    def SetFrom(self, source: PointCloudClassificationColorRamp) -> None: ...
    def SetVisibility(self, c: int, bVisible: bool) -> None: ...
    def Visibility(self, c: int) -> bool: ...

class PointCloudColorMap(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.PointCloudColorMap"""
    def __init__(self, *args) -> None: ...
    ClassificationSchemeGUIDs: list
    ColorSchemeGUIDs: list
    DefaultClassificationColorScheme: str
    DefaultElevationColorScheme: str
    DefaultIntensityColorScheme: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def ClassificationColorSchemeInUse(self, ) -> list: ...
    def ClassificationScheme(self, name: str, target: PointCloudClassificationColorRamp) -> bool: ...
    def ColorScheme(self, name: str, target: PointCloudColorRamp) -> bool: ...
    def ColorSchemeInUse(self, ) -> list: ...
    def DeleteClassificationScheme(self, name: str) -> bool: ...
    def DeleteColorScheme(self, name: str) -> bool: ...
    @staticmethod
    def GetColorMapId(hostDatabase: Database) -> ObjectId: ...
    def HasClassificationScheme(self, name: str) -> bool: ...
    def HasColorScheme(self, name: str) -> bool: ...
    def SetClassificationScheme(self, name: str, source: PointCloudClassificationColorRamp) -> bool: ...
    def SetColorScheme(self, name: str, source: PointCloudColorRamp) -> bool: ...

class PointCloudColorRamp(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.PointCloudColorRamp"""
    def __init__(self, *args) -> None: ...
    Name: str
    NumColors: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Color(self, c: int) -> EntityColor: ...
    def SetColor(self, c: int, color: EntityColor) -> None: ...
    def SetFrom(self, source: PointCloudColorRamp) -> None: ...
    def SetVisibility(self, c: int, bVisible: bool) -> None: ...
    def Visibility(self, c: int) -> bool: ...

class PointCloudColorSchemeChangedEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.PointCloudColorSchemeChangedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, __unnamed000: PointCloudColorMap, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, A_0: PointCloudColorMap) -> None: ...

class PointCloudCrop:
    """.NET: Autodesk.AutoCAD.DatabaseServices.PointCloudCrop"""
    def __init__(self, *args) -> None: ...
    Inverted: bool
    Inside: bool
    CropType: PointCloudCropType
    Vertices: Point3dCollection
    CropPlane: Plane
    def Clear(self, ) -> None: ...
    @staticmethod
    def Create(unmanagedObjPtr: IntPtr) -> PointCloudCrop: ...
    def Dispose(self, ) -> None: ...
    def IsValid(self, ) -> bool: ...

class PointCloudCropType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.PointCloudCropType"""
    def __init__(self, *args) -> None: ...
    Invalid: int  # = 0
    Rectangular: int  # = 1
    Polygonal: int  # = 2
    Circular: int  # = 3
class PointCloudDefEx(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.PointCloudDefEx"""
    def __init__(self, *args) -> None: ...
    extents: Extents3d
    defaultHeight: float
    defaultLength: float
    defaultWidth: float
    totalScansCount: int
    totalRegionsCount: int
    totalPointsCount: int
    FileType: str
    ActiveFileName: str
    SourceFileName: str
    EntityCount: int
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def classVersion() -> int: ...
    def getAllRcsFilePaths(self, ) -> list: ...
    def getRcsFilePath(self, guid: str) -> str: ...
    def load(self, ) -> bool: ...
    def unload(self, ) -> bool: ...

class PointCloudDispOptionOutOfRange:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.PointCloudDispOptionOutOfRange"""
    def __init__(self, *args) -> None: ...
    UseMinMaxColors: int  # = 0
    UseRGBScanColors: int  # = 1
    HidePoints: int  # = 2
class PointCloudEx(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.PointCloudEx"""
    def __init__(self, *args) -> None: ...
    NativeExtents: Extents3d
    GeomExtents: Extents3d
    PointCloudDefExId: ObjectId
    ShowCropped: bool
    CroppingInverted: bool
    ActiveFileName: str
    Location: Point3d
    Rotation: float
    Scale: float
    LimitBoxBound: Tuple
    ElevationGradient: bool
    IntensityGradient: bool
    Stylization: PointCloudStylizationType
    ElevationOutOfRangeBehavior: PointCloudDispOptionOutOfRange
    ElevationApplyToFixedRange: bool
    MinMaxElevation: Tuple
    CurrentColorScheme: str
    IntensityOutOfRangeBehavior: PointCloudDispOptionOutOfRange
    MinMaxIntensity: Tuple
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def AttachPointCloud(filename: str, location: Point3d, scale: float, rotation: float, db: Database) -> ObjectId: ...
    def GetColorSchemeForStylization(self, type: PointCloudStylizationType) -> str: ...
    def GetScanViewInfo(self, scanGuid: str, origin: ValueType, extent: ValueType) -> bool: ...
    def HasProperty(self, prop: PointCloudProperty) -> PointCloudPropertyState: ...
    def SetColorSchemeForStylization(self, name: str, type: PointCloudStylizationType) -> None: ...
    def TransformBy(self, xform: Matrix3d) -> bool: ...
    def addCroppingBoundary(self, cropping: PointCloudCrop) -> None: ...
    def clearCropping(self, ) -> bool: ...
    def findRegionItem(self, regionId: int) -> PointCloudItem: ...
    def findScanItem(self, scanGuid: str) -> PointCloudItem: ...
    def getCroppingCount(self, ) -> int: ...
    def getPointCloudCropping(self, index: int) -> PointCloudCrop: ...
    def getPointCloudDataList(self, ) -> List: ...
    def removeLastCropping(self, ) -> bool: ...
    def setAllRegionsVisibility(self, visible: bool, includeUnassigned: bool) -> None: ...
    def setAllScansVisibility(self, visible: bool) -> None: ...
    def setRegionVisibility(self, regionId: int, visible: bool) -> None: ...
    def setScanVisibility(self, scanGuid: str, visible: bool) -> None: ...

class PointCloudItem(Notifier):
    """.NET: Autodesk.AutoCAD.DatabaseServices.PointCloudItem"""
    def __init__(self, *args) -> None: ...
    CurrentAdsName: ValueType
    CategoryId: PointCloudItemType
    Visibility: bool
    Guid: str
    ProjectName: str
    Name: str
    ItemId: int
    def Clone(self, ) -> PointCloudItem: ...
    def CompareTo(self, other: PointCloudItem) -> bool: ...
    @staticmethod
    def CreatePointCloudDataItemCollection(unmanagedObjPtr: IntPtr) -> List: ...
    def ToCmdString(self, ) -> str: ...

class PointCloudItemType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.PointCloudItemType"""
    def __init__(self, *args) -> None: ...
    LegacyPointCloud: int  # = 0
    PointCloudProject: int  # = 1
    IndividualScan: int  # = 2
    Scan: int  # = 3
    Region: int  # = 4
    ScanRootGroup: int  # = 5
    RegionRootGroup: int  # = 6
    UnassignedPoint: int  # = 7
class PointCloudProperty:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.PointCloudProperty"""
    def __init__(self, *args) -> None: ...
    Color: int  # = 1
    Intensity: int  # = 2
    Classification: int  # = 3
    Normal: int  # = 4
    TerrestrialClassification: int  # = 7
class PointCloudPropertyState:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.PointCloudPropertyState"""
    def __init__(self, *args) -> None: ...
    Some: int  # = 0
    All: int  # = 1
    None_: int  # = -1
class PointCloudStylizationType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.PointCloudStylizationType"""
    def __init__(self, *args) -> None: ...
    TrueColor: int  # = 1
    SingleColor: int  # = 2
    NormalRamp: int  # = 3
    HeightRamp: int  # = 4
    IntensityRamp: int  # = 5
    ClassificationRamp: int  # = 6
class PointCoincidenceConstraint(GeometricalConstraint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.PointCoincidenceConstraint"""
    def __init__(self, *args) -> None: ...
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PointCurveConstraint(GeometricalConstraint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.PointCurveConstraint"""
    def __init__(self, *args) -> None: ...
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Poly2dType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.Poly2dType"""
    def __init__(self, *args) -> None: ...
    SimplePoly: int  # = 0
    FitCurvePoly: int  # = 1
    QuadSplinePoly: int  # = 2
    CubicSplinePoly: int  # = 3
class Poly3dType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.Poly3dType"""
    def __init__(self, *args) -> None: ...
    SimplePoly: int  # = 0
    QuadSplinePoly: int  # = 1
    CubicSplinePoly: int  # = 2
class PolyFaceMesh(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.PolyFaceMesh"""
    def __init__(self, *args) -> None: ...
    NumFaces: int
    NumVertices: int
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AppendFaceRecord(self, toAppend: FaceRecord) -> ObjectId: ...
    def AppendVertex(self, vertexToAppend: PolyFaceMeshVertex) -> ObjectId: ...
    def GetEnumerator(self, ) -> IEnumerator: ...

class PolyFaceMeshVertex(Vertex):
    """.NET: Autodesk.AutoCAD.DatabaseServices.PolyFaceMeshVertex"""
    def __init__(self, *args) -> None: ...
    Position: Point3d
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PolyMeshType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.PolyMeshType"""
    def __init__(self, *args) -> None: ...
    SimpleMesh: int  # = 0
    QuadSurfaceMesh: int  # = 5
    CubicSurfaceMesh: int  # = 6
    BezierSurfaceMesh: int  # = 8
class PolygonMesh(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.PolygonMesh"""
    def __init__(self, *args) -> None: ...
    NSurfaceDensity: int
    MSurfaceDensity: int
    IsNClosed: bool
    IsMClosed: bool
    NSize: int
    MSize: int
    PolyMeshType: PolyMeshType
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AppendVertex(self, toAppend: PolygonMeshVertex) -> ObjectId: ...
    def ConvertToPolyMeshType(self, newVal: PolyMeshType) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def MakeMClosed(self, ) -> None: ...
    def MakeMOpen(self, ) -> None: ...
    def MakeNClosed(self, ) -> None: ...
    def MakeNOpen(self, ) -> None: ...
    def Straighten(self, ) -> None: ...
    def SurfaceFit(self, surfType: PolyMeshType, surfU: int, surfV: int) -> None: ...

class PolygonMeshVertex(Vertex):
    """.NET: Autodesk.AutoCAD.DatabaseServices.PolygonMeshVertex"""
    def __init__(self, *args) -> None: ...
    Position: Point3d
    VertexType: Vertex3dType
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Polyline(Curve):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Polyline"""
    def __init__(self, *args) -> None: ...
    Length: float
    HasWidth: bool
    HasBulges: bool
    NumberOfVertices: int
    IsOnlyLines: bool
    Normal: Vector3d
    ConstantWidth: float
    Thickness: float
    Elevation: float
    Plinegen: bool
    Closed: bool
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddVertexAt(self, index: int, pt: Point2d, bulge: float, startWidth: float, endWidth: float) -> None: ...
    def ConvertFrom(self, entity: Entity, transferId: bool) -> None: ...
    def ConvertTo(self, transferId: bool) -> Polyline2d: ...
    def GetArcSegment2dAt(self, index: int) -> CircularArc2d: ...
    def GetArcSegmentAt(self, index: int) -> CircularArc3d: ...
    def GetBulgeAt(self, index: int) -> float: ...
    def GetEndWidthAt(self, index: int) -> float: ...
    def GetLineSegment2dAt(self, index: int) -> LineSegment2d: ...
    def GetLineSegmentAt(self, index: int) -> LineSegment3d: ...
    def GetPoint2dAt(self, index: int) -> Point2d: ...
    def GetPoint3dAt(self, value: int) -> Point3d: ...
    def GetSegmentType(self, index: int) -> SegmentType: ...
    def GetStartWidthAt(self, index: int) -> float: ...
    def MaximizeMemory(self, ) -> None: ...
    def MinimizeMemory(self, ) -> None: ...
    def OnSegmentAt(self, index: int, pt2d: Point2d, value: float) -> bool: ...
    def RemoveVertexAt(self, index: int) -> None: ...
    def Reset(self, reuse: bool, vertices: int) -> None: ...
    def SetBulgeAt(self, index: int, bulge: float) -> None: ...
    def SetEndWidthAt(self, index: int, endWidth: float) -> None: ...
    def SetPointAt(self, index: int, pt: Point2d) -> None: ...
    def SetStartWidthAt(self, index: int, startWidth: float) -> None: ...

class Polyline2d(Curve):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Polyline2d"""
    def __init__(self, *args) -> None: ...
    Length: float
    ConstantWidth: float
    LinetypeGenerationOn: bool
    Elevation: float
    Normal: Vector3d
    Thickness: float
    DefaultEndWidth: float
    DefaultStartWidth: float
    Closed: bool
    PolyType: Poly2dType
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AppendVertex(self, vertexToAppend: Vertex2d) -> ObjectId: ...
    def ConvertToPolyType(self, newVal: Poly2dType) -> None: ...
    def CurveFit(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def InsertVertexAt(self, vertexId: ObjectId, newVertex: Vertex2d) -> ObjectId: ...
    def NonDBAppendVertex(self, vertexToAppend: Vertex2d) -> None: ...
    def SplineFit(self, value: Poly2dType, segments: int) -> None: ...
    def Straighten(self, ) -> None: ...
    def VertexPosition(self, vertex: Vertex2d) -> Point3d: ...

class Polyline3d(Curve):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Polyline3d"""
    def __init__(self, *args) -> None: ...
    Length: float
    PolyType: Poly3dType
    Closed: bool
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AppendVertex(self, vertexToAppend: PolylineVertex3d) -> ObjectId: ...
    def ConvertToPolyType(self, newVal: Poly3dType) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def InsertVertexAt(self, indexVertexId: ObjectId, newVertex: PolylineVertex3d) -> ObjectId: ...
    def SplineFit(self, value: Poly3dType, segments: int) -> None: ...
    def Straighten(self, ) -> None: ...

class PolylineVertex3d(Vertex):
    """.NET: Autodesk.AutoCAD.DatabaseServices.PolylineVertex3d"""
    def __init__(self, *args) -> None: ...
    Position: Point3d
    VertexType: Vertex3dType
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Profile3d(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Profile3d"""
    def __init__(self, *args) -> None: ...
    IsValid: bool
    IsEdge: bool
    IsFace: bool
    IsSubent: bool
    IsPlanar: bool
    IsClosed: bool
    ProfileVertexRef: VertexRef
    ProfilePathRef: PathRef
    Entity: Entity
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def ConvertProfile(self, explodeMultiFaceRegions: bool, convertSurfaceToEdges: bool, nonPlanarOnly: bool, outerLoopOnly: bool) -> list: ...
    def CopyFrom(self, source: Profile3d) -> None: ...
    @staticmethod
    def MergeProfiles(profiles: list, mergeEdges: bool, mergeCurves: bool) -> list: ...

class PropertiesOverrule(Overrule):
    """.NET: Autodesk.AutoCAD.DatabaseServices.PropertiesOverrule"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetClassID(self, entity: DBObject) -> Guid: ...
    def List(self, entity: Entity) -> None: ...
    def SetCustomFilter(self, ) -> None: ...
    def SetExtensionDictionaryEntryFilter(self, entryName: str) -> None: ...
    def SetIdFilter(self, ids: list) -> None: ...
    def SetNoFilter(self, ) -> None: ...
    def SetXDataFilter(self, registeredApplicationName: str) -> None: ...

class ProxyEntity(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ProxyEntity"""
    def __init__(self, *args) -> None: ...
    GraphicsMetafileType: GraphicsMetafileType
    ApplicationDescription: str
    OriginalDxfName: str
    OriginalClassName: str
    ProxyFlags: int
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetReferences(self, ) -> DBObjectReferenceCollection: ...

class ProxyObject(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ProxyObject"""
    def __init__(self, *args) -> None: ...
    ApplicationDescription: str
    OriginalDxfName: str
    OriginalClassName: str
    ProxyFlags: int
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetReferences(self, ) -> DBObjectReferenceCollection: ...
    @staticmethod
    def ResurrectMeNow(id: ObjectId) -> None: ...

class ProxyResurrectionCompletedEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ProxyResurrectionCompletedEventArgs"""
    def __init__(self, *args) -> None: ...
    Ids: ObjectIdCollection
    ApplicationName: str

class ProxyResurrectionCompletedEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.ProxyResurrectionCompletedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: ProxyResurrectionCompletedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: ProxyResurrectionCompletedEventArgs) -> None: ...

class RadialDimension(Dimension):
    """.NET: Autodesk.AutoCAD.DatabaseServices.RadialDimension"""
    def __init__(self, *args) -> None: ...
    ChordPoint: Point3d
    Center: Point3d
    LeaderLength: float
    Dimaltmzf: float
    Dimmzf: float
    Dimaltmzs: str
    Dimmzs: str
    Dimblk2: ObjectId
    Dimblk1: ObjectId
    Dimblk: ObjectId
    Dimpost: str
    Dimapost: str
    Dimzin: int
    Dimupt: bool
    Dimtzin: int
    Dimtxtdirection: bool
    Dimtxt: float
    TextStyleId: ObjectId
    Dimtvp: float
    Dimtsz: float
    Dimtp: float
    Dimtolj: int
    Dimtol: bool
    Dimtoh: bool
    Dimtofl: bool
    Dimtmove: int
    Dimtm: float
    Dimtix: bool
    Dimtih: bool
    Dimtfillclr: Color
    Dimtfill: int
    Dimtfac: float
    Dimtdec: int
    Dimtad: int
    Dimsoxd: bool
    Dimse2: bool
    Dimse1: bool
    Dimsd2: bool
    Dimsd1: bool
    Dimscale: float
    Dimsah: bool
    Dimrnd: float
    DimensionStyleName: str
    CenterMarkSize: float
    CenterMarkType: DimensionCenterMarkType
    ToleranceSuppressZeroInches: bool
    ToleranceSuppressZeroFeet: bool
    ToleranceSuppressTrailingZeros: bool
    ToleranceSuppressLeadingZeros: bool
    AltToleranceSuppressZeroInches: bool
    AltToleranceSuppressZeroFeet: bool
    AltToleranceSuppressTrailingZeros: bool
    AltToleranceSuppressLeadingZeros: bool
    AltSuppressZeroInches: bool
    AltSuppressZeroFeet: bool
    AltSuppressTrailingZeros: bool
    AltSuppressLeadingZeros: bool
    AlternateSuffix: str
    AlternatePrefix: str
    SuppressZeroInches: bool
    SuppressZeroFeet: bool
    SuppressTrailingZeros: bool
    SuppressLeadingZeros: bool
    SuppressAngularTrailingZeros: bool
    SuppressAngularLeadingZeros: bool
    Suffix: str
    Prefix: str
    Dimlwe: LineWeight
    Dimlwd: LineWeight
    Dimlunit: int
    Dimltype: ObjectId
    Dimltex2: ObjectId
    Dimltex1: ObjectId
    Dimlim: bool
    Dimlfac: float
    Dimldrblk: ObjectId
    Dimjust: int
    Dimjogang: float
    Dimgap: float
    Dimfxlen: float
    DimfxlenOn: bool
    Dimfrac: int
    Dimexo: float
    Dimexe: float
    Dimdsep: str
    Dimdli: float
    Dimdle: float
    Dimdec: int
    Dimclrt: Color
    Dimclre: Color
    Dimclrd: Color
    Dimcen: float
    Dimazin: int
    Dimaunit: int
    Dimatfit: int
    Dimasz: float
    Dimarcsym: int
    Dimaltz: int
    Dimaltu: int
    Dimalttz: int
    Dimalttd: int
    Dimaltrnd: float
    Dimaltf: float
    Dimaltd: int
    Dimalt: bool
    Dimadec: int
    DynamicDimension: bool
    Measurement: float
    DimBlockPosition: Point3d
    DimBlockId: ObjectId
    HorizontalRotation: float
    TextLineSpacingFactor: float
    TextLineSpacingStyle: LineSpacingStyle
    TextAttachment: AttachmentPoint
    DimensionStyle: ObjectId
    TextRotation: float
    DimensionText: str
    Elevation: float
    Normal: Vector3d
    UsingDefaultTextPosition: bool
    TextPosition: Point3d
    TextDefinedSize: Vector2d
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class RadialDimensionLarge(Dimension):
    """.NET: Autodesk.AutoCAD.DatabaseServices.RadialDimensionLarge"""
    def __init__(self, *args) -> None: ...
    OverrideCenter: Point3d
    JogPoint: Point3d
    ChordPoint: Point3d
    Center: Point3d
    JogAngle: float
    Dimaltmzf: float
    Dimmzf: float
    Dimaltmzs: str
    Dimmzs: str
    Dimblk2: ObjectId
    Dimblk1: ObjectId
    Dimblk: ObjectId
    Dimpost: str
    Dimapost: str
    Dimzin: int
    Dimupt: bool
    Dimtzin: int
    Dimtxtdirection: bool
    Dimtxt: float
    TextStyleId: ObjectId
    Dimtvp: float
    Dimtsz: float
    Dimtp: float
    Dimtolj: int
    Dimtol: bool
    Dimtoh: bool
    Dimtofl: bool
    Dimtmove: int
    Dimtm: float
    Dimtix: bool
    Dimtih: bool
    Dimtfillclr: Color
    Dimtfill: int
    Dimtfac: float
    Dimtdec: int
    Dimtad: int
    Dimsoxd: bool
    Dimse2: bool
    Dimse1: bool
    Dimsd2: bool
    Dimsd1: bool
    Dimscale: float
    Dimsah: bool
    Dimrnd: float
    DimensionStyleName: str
    CenterMarkSize: float
    CenterMarkType: DimensionCenterMarkType
    ToleranceSuppressZeroInches: bool
    ToleranceSuppressZeroFeet: bool
    ToleranceSuppressTrailingZeros: bool
    ToleranceSuppressLeadingZeros: bool
    AltToleranceSuppressZeroInches: bool
    AltToleranceSuppressZeroFeet: bool
    AltToleranceSuppressTrailingZeros: bool
    AltToleranceSuppressLeadingZeros: bool
    AltSuppressZeroInches: bool
    AltSuppressZeroFeet: bool
    AltSuppressTrailingZeros: bool
    AltSuppressLeadingZeros: bool
    AlternateSuffix: str
    AlternatePrefix: str
    SuppressZeroInches: bool
    SuppressZeroFeet: bool
    SuppressTrailingZeros: bool
    SuppressLeadingZeros: bool
    SuppressAngularTrailingZeros: bool
    SuppressAngularLeadingZeros: bool
    Suffix: str
    Prefix: str
    Dimlwe: LineWeight
    Dimlwd: LineWeight
    Dimlunit: int
    Dimltype: ObjectId
    Dimltex2: ObjectId
    Dimltex1: ObjectId
    Dimlim: bool
    Dimlfac: float
    Dimldrblk: ObjectId
    Dimjust: int
    Dimjogang: float
    Dimgap: float
    Dimfxlen: float
    DimfxlenOn: bool
    Dimfrac: int
    Dimexo: float
    Dimexe: float
    Dimdsep: str
    Dimdli: float
    Dimdle: float
    Dimdec: int
    Dimclrt: Color
    Dimclre: Color
    Dimclrd: Color
    Dimcen: float
    Dimazin: int
    Dimaunit: int
    Dimatfit: int
    Dimasz: float
    Dimarcsym: int
    Dimaltz: int
    Dimaltu: int
    Dimalttz: int
    Dimalttd: int
    Dimaltrnd: float
    Dimaltf: float
    Dimaltd: int
    Dimalt: bool
    Dimadec: int
    DynamicDimension: bool
    Measurement: float
    DimBlockPosition: Point3d
    DimBlockId: ObjectId
    HorizontalRotation: float
    TextLineSpacingFactor: float
    TextLineSpacingStyle: LineSpacingStyle
    TextAttachment: AttachmentPoint
    DimensionStyle: ObjectId
    TextRotation: float
    DimensionText: str
    Elevation: float
    Normal: Vector3d
    UsingDefaultTextPosition: bool
    TextPosition: Point3d
    TextDefinedSize: Vector2d
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class RadiusDiameterConstraint(ExplicitConstraint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.RadiusDiameterConstraint"""
    def __init__(self, *args) -> None: ...
    ConstrType: RadDiaConstrType
    MeasuredValue: float
    DimDependencyId: ObjectId
    ValueDependencyId: ObjectId
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class RapidRTRenderSettings(RenderSettings):
    """.NET: Autodesk.AutoCAD.DatabaseServices.RapidRTRenderSettings"""
    def __init__(self, *args) -> None: ...
    FilterHeight: float
    FilterWidth: float
    FilterType: RapidRTFilterType
    LightingModel: RapidRTLightingMode
    RenderTime: int
    RenderLevel: int
    RenderTarget: RapidRTRenderTarget
    IsPredefined: bool
    PreviewImageFileName: str
    ShadowsEnabled: bool
    BackFacesEnabled: bool
    TextureSampling: bool
    MaterialsEnabled: bool
    DiagnosticBackgroundEnabled: bool
    DisplayIndex: int
    Description: str
    Name: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CopyFrom(self, srcObject: RapidRTRenderSettings) -> None: ...

class RapidRTRenderTarget:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.RapidRTRenderTarget"""
    def __init__(self, *args) -> None: ...
    Level: int  # = 0
    Time: int  # = 1
    Infinite: int  # = 2
class RasterImage(Image):
    """.NET: Autodesk.AutoCAD.DatabaseServices.RasterImage"""
    def __init__(self, *args) -> None: ...
    Width: float
    ImageTransparency: bool
    ShowImage: bool
    Rotation: float
    Position: Point3d
    Path: str
    Name: str
    ImageWidth: float
    ImageHeight: float
    Height: float
    Fade: int
    Contrast: int
    Brightness: int
    DisplayOptions: ImageDisplayOptions
    PixelToModelTransform: Matrix3d
    IsClipped: bool
    ClipBoundaryType: ClipBoundaryType
    Scale: Vector2d
    Orientation: CoordinateSystem3d
    ReactorId: ObjectId
    ImageDefId: ObjectId
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AssociateRasterDef(self, definition: RasterImageDef) -> None: ...
    @staticmethod
    def EnableReactors(enable: bool) -> None: ...
    def GetClipBoundary(self, ) -> Point2dCollection: ...
    def GetVertices(self, ) -> Point3dCollection: ...
    def ImageSize(self, getCachedValue: bool) -> Vector2d: ...
    def SetClipBoundary(self, type: ClipBoundaryType, clipBoundaryVertices: Point2dCollection) -> None: ...
    def SetClipBoundaryToWholeImage(self, ) -> None: ...

class RasterImageDef(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.RasterImageDef"""
    def __init__(self, *args) -> None: ...
    ImageModified: bool
    UndoStoreSize: int
    FileDescCopy: IntPtr
    ResolutionUnits: Unit
    ResolutionMMPerPixel: Vector2d
    FileType: str
    ColorDepth: int
    Organization: ImageOrg
    Size: Vector2d
    IsLoaded: bool
    IsEmbedded: bool
    SearchForActivePath: str
    ActiveFileName: str
    SourceFileName: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CloseImage(self, ) -> None: ...
    @staticmethod
    def CreateImageDictionary(database: Database) -> ObjectId: ...
    def Embed(self, ) -> None: ...
    def GetEntityCount(self, locked: bool) -> int: ...
    @staticmethod
    def GetImageDictionary(database: Database) -> ObjectId: ...
    def ImageCopy(self, forceImageLoad: bool) -> IntPtr: ...
    def Load(self, ) -> None: ...
    def LocateActivePath(self, ) -> str: ...
    def OpenImage(self, ) -> IntPtr: ...
    def SetImage(self, image: IntPtr, fileDescription: IntPtr, modifyDatabase: bool) -> None: ...
    @staticmethod
    def SuggestName(imageDictionary: DBDictionary, newImagePathName: str) -> str: ...
    def Unload(self, modifyDatabase: bool) -> None: ...
    def UpdateEntities(self, ) -> None: ...

class RasterVariables(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.RasterVariables"""
    def __init__(self, *args) -> None: ...
    UserScale: Unit
    ImageQuality: ImageQuality
    ImageFrame: FrameSetting
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Ray(Curve):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Ray"""
    def __init__(self, *args) -> None: ...
    SecondPoint: Point3d
    UnitDir: Vector3d
    BasePoint: Point3d
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Rectangle3d:
    """.NET: Autodesk.AutoCAD.DatabaseServices.Rectangle3d"""
    def __init__(self, *args) -> None: ...
    LowerRight: Point3d
    LowerLeft: Point3d
    UpperRight: Point3d
    UpperLeft: Point3d
    def ToString(self, provider: IFormatProvider) -> str: ...

class RegAppTable(SymbolTable):
    """.NET: Autodesk.AutoCAD.DatabaseServices.RegAppTable"""
    def __init__(self, *args) -> None: ...
    IncludingErased: SymbolTable
    Item: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class RegAppTableRecord(SymbolTableRecord):
    """.NET: Autodesk.AutoCAD.DatabaseServices.RegAppTableRecord"""
    def __init__(self, *args) -> None: ...
    IsResolved: bool
    IsDependent: bool
    Name: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Region(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Region"""
    def __init__(self, *args) -> None: ...
    UsesGraphicsCache: bool
    NumChanges: int
    Normal: Vector3d
    IsNull: bool
    GeometricExtents: Extents3d
    Area: float
    Perimeter: float
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AreaProperties(self, origin: Point3d, xAxis: Vector3d, yAxis: Vector3d) -> RegionAreaProperties: ...
    def BooleanOperation(self, operation: BooleanOperationType, otherRegion: Region) -> None: ...
    @staticmethod
    def CreateFromCurves(curveSegments: DBObjectCollection) -> DBObjectCollection: ...

class RegionAreaProperties:
    """.NET: Autodesk.AutoCAD.DatabaseServices.RegionAreaProperties"""
    def __init__(self, *args) -> None: ...
    Extents: Extents2d
    RadiiOfGyration: Vector2d
    PrincipalAxes: Vector2d
    PrincipalMoments: Vector2d
    ProductOfInertia: float
    MomentsOfInertia: Vector2d
    Centroid: Point2d
    Area: float
    Perimeter: float

class RenderEnvironment(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.RenderEnvironment"""
    def __init__(self, *args) -> None: ...
    EnvironmentImageFileName: str
    EnvironmentImageEnabled: bool
    Distances: DoubleRangeParameter
    FogDensity: DoubleRangeParameter
    FogColor: EntityColor
    FogBackgroundEnabled: bool
    FogEnabled: bool
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class RenderGlobal(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.RenderGlobal"""
    def __init__(self, *args) -> None: ...
    HighInfoLevel: bool
    PredefinedPresetsFirst: bool
    Dimensions: DimensionsParameter
    SaveFileName: str
    SaveEnabled: bool
    ProcedureAndDestination: ProcedureAndDestinationParameter
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class RenderSettings(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.RenderSettings"""
    def __init__(self, *args) -> None: ...
    IsPredefined: bool
    PreviewImageFileName: str
    ShadowsEnabled: bool
    BackFacesEnabled: bool
    TextureSampling: bool
    MaterialsEnabled: bool
    DiagnosticBackgroundEnabled: bool
    DisplayIndex: int
    Description: str
    Name: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ReservedStringEnumType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.ReservedStringEnumType"""
    def __init__(self, *args) -> None: ...
    ByLayer: int  # = 0
    ByBlock: int  # = 1
    None_: int  # = 2
    Continuous: int  # = 3
    Standard: int  # = 4
    Normal: int  # = 5
    DefPoints: int  # = 6
    Default: int  # = 7
    Missing: int  # = 8
    ByColor: int  # = 9
    Model: int  # = 10
    Global: int  # = 11
    VS2DWireframe: int  # = 12
    VS3DWireframe: int  # = 13
    VS3DHidden: int  # = 14
    VSRealistic: int  # = 15
    VSConceptual: int  # = 16
    Title: int  # = 17
    Header: int  # = 18
    Data: int  # = 19
    VSShadesOfGray: int  # = 20
    VSSketchy: int  # = 21
    VSXRay: int  # = 22
    VSShadedWithEdges: int  # = 23
    VSShaded: int  # = 24
class ResultBuffer(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ResultBuffer"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, value: object) -> None: ...
    def AsArray(self, ) -> list: ...
    @staticmethod
    def Create(buffer: IntPtr, autoDelete: bool) -> ResultBuffer: ...
    def Equals(self, obj: object) -> bool: ...
    def GetEnumerator(self, ) -> ResultBufferEnumerator: ...
    def GetHashCode(self, ) -> int: ...
    def ToString(self, format: str, provider: IFormatProvider) -> str: ...

class ResultBufferEnumerator:
    """.NET: Autodesk.AutoCAD.DatabaseServices.ResultBufferEnumerator"""
    def __init__(self, *args) -> None: ...
    Current: TypedValue
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class RevolveOptions(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.RevolveOptions"""
    def __init__(self, *args) -> None: ...
    CloseToAxis: bool
    TwistAngle: float
    DraftAngle: float
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CheckRevolveCurve(self, __unnamed000: Entity, axisPnt: Point3d, axisDir: Vector3d, displayErrorMessages: bool) -> RevolveOptionsCheckRevolveCurveOut: ...
    def Clone(self, ) -> object: ...

class RevolveOptionsBuilder:
    """.NET: Autodesk.AutoCAD.DatabaseServices.RevolveOptionsBuilder"""
    def __init__(self, *args) -> None: ...
    CloseToAxis: bool
    TwistAngle: float
    DraftAngle: float
    def ToRevolveOptions(self, ) -> RevolveOptions: ...

class RevolveOptionsCheckRevolveCurveOut:
    """.NET: Autodesk.AutoCAD.DatabaseServices.RevolveOptionsCheckRevolveCurveOut"""
    def __init__(self, *args) -> None: ...
    Planar: bool
    EndPointsOnAxis: bool
    Closed: bool

class RevolvedSurface(Surface):
    """.NET: Autodesk.AutoCAD.DatabaseServices.RevolvedSurface"""
    def __init__(self, *args) -> None: ...
    RevolveOptions: RevolveOptions
    StartAngle: float
    RevolveAngle: float
    AxisDirection: Vector3d
    AxisPoint: Point3d
    RevolveProfile: Profile3d
    RevolveEntity: Entity
    GeometricExtents: Extents3d
    UsesGraphicsCache: bool
    Perimeter: float
    WireframeType: WireframeTypeEnum
    VIsoLineDensity: int
    UIsoLineDensity: int
    ModificationActionBodyIds: ObjectIdCollection
    CreationActionBodyId: ObjectId
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CreateRevolvedSurface(self, revolveEntity: Entity, axisPoint: Point3d, axisDirection: Vector3d, revolveAngle: float, startAngle: float, revolveOptions: RevolveOptions) -> None: ...
    def SetRevolve(self, axisPoint: Point3d, axisDirection: Vector3d, revolveAngle: float, revolveOptions: RevolveOptions) -> None: ...

class RigidSetTypeInfo:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.RigidSetTypeInfo"""
    def __init__(self, *args) -> None: ...
    NotRigidSet: int  # = 0
    ScalableRigidSet: int  # = 1
    NonScalableRigidSet: int  # = 2
class RotatedDimension(Dimension):
    """.NET: Autodesk.AutoCAD.DatabaseServices.RotatedDimension"""
    def __init__(self, *args) -> None: ...
    Rotation: float
    Oblique: float
    DimLinePoint: Point3d
    XLine2Point: Point3d
    XLine1Point: Point3d
    Dimaltmzf: float
    Dimmzf: float
    Dimaltmzs: str
    Dimmzs: str
    Dimblk2: ObjectId
    Dimblk1: ObjectId
    Dimblk: ObjectId
    Dimpost: str
    Dimapost: str
    Dimzin: int
    Dimupt: bool
    Dimtzin: int
    Dimtxtdirection: bool
    Dimtxt: float
    TextStyleId: ObjectId
    Dimtvp: float
    Dimtsz: float
    Dimtp: float
    Dimtolj: int
    Dimtol: bool
    Dimtoh: bool
    Dimtofl: bool
    Dimtmove: int
    Dimtm: float
    Dimtix: bool
    Dimtih: bool
    Dimtfillclr: Color
    Dimtfill: int
    Dimtfac: float
    Dimtdec: int
    Dimtad: int
    Dimsoxd: bool
    Dimse2: bool
    Dimse1: bool
    Dimsd2: bool
    Dimsd1: bool
    Dimscale: float
    Dimsah: bool
    Dimrnd: float
    DimensionStyleName: str
    CenterMarkSize: float
    CenterMarkType: DimensionCenterMarkType
    ToleranceSuppressZeroInches: bool
    ToleranceSuppressZeroFeet: bool
    ToleranceSuppressTrailingZeros: bool
    ToleranceSuppressLeadingZeros: bool
    AltToleranceSuppressZeroInches: bool
    AltToleranceSuppressZeroFeet: bool
    AltToleranceSuppressTrailingZeros: bool
    AltToleranceSuppressLeadingZeros: bool
    AltSuppressZeroInches: bool
    AltSuppressZeroFeet: bool
    AltSuppressTrailingZeros: bool
    AltSuppressLeadingZeros: bool
    AlternateSuffix: str
    AlternatePrefix: str
    SuppressZeroInches: bool
    SuppressZeroFeet: bool
    SuppressTrailingZeros: bool
    SuppressLeadingZeros: bool
    SuppressAngularTrailingZeros: bool
    SuppressAngularLeadingZeros: bool
    Suffix: str
    Prefix: str
    Dimlwe: LineWeight
    Dimlwd: LineWeight
    Dimlunit: int
    Dimltype: ObjectId
    Dimltex2: ObjectId
    Dimltex1: ObjectId
    Dimlim: bool
    Dimlfac: float
    Dimldrblk: ObjectId
    Dimjust: int
    Dimjogang: float
    Dimgap: float
    Dimfxlen: float
    DimfxlenOn: bool
    Dimfrac: int
    Dimexo: float
    Dimexe: float
    Dimdsep: str
    Dimdli: float
    Dimdle: float
    Dimdec: int
    Dimclrt: Color
    Dimclre: Color
    Dimclrd: Color
    Dimcen: float
    Dimazin: int
    Dimaunit: int
    Dimatfit: int
    Dimasz: float
    Dimarcsym: int
    Dimaltz: int
    Dimaltu: int
    Dimalttz: int
    Dimalttd: int
    Dimaltrnd: float
    Dimaltf: float
    Dimaltd: int
    Dimalt: bool
    Dimadec: int
    DynamicDimension: bool
    Measurement: float
    DimBlockPosition: Point3d
    DimBlockId: ObjectId
    HorizontalRotation: float
    TextLineSpacingFactor: float
    TextLineSpacingStyle: LineSpacingStyle
    TextAttachment: AttachmentPoint
    DimensionStyle: ObjectId
    TextRotation: float
    DimensionText: str
    Elevation: float
    Normal: Vector3d
    UsingDefaultTextPosition: bool
    TextPosition: Point3d
    TextDefinedSize: Vector2d
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class RotationAngle:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.RotationAngle"""
    def __init__(self, *args) -> None: ...
    Degrees000: int  # = 0
    Degrees090: int  # = 1
    Degrees180: int  # = 2
    Degrees270: int  # = 3
    DegreesUnknown: int  # = -1
class Row(CellRange):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Row"""
    def __init__(self, *args) -> None: ...
    MinimumHeight: float
    Height: float
    IsMerged: Nullable
    IsSingleCell: bool
    Item: Cell
    Borders: CellBorders
    CanInsertColumn: bool
    CanInsertRow: bool
    CanDeleteColumns: bool
    CanDeleteRows: bool
    IsEmpty: Nullable
    IsFormatEditable: Nullable
    IsContentEditable: Nullable
    IsLinked: Nullable
    TextStyleId: Nullable
    TextHeight: Nullable
    IsMergeAllEnabled: Nullable
    DataType: Nullable
    DataFormat: str
    ContentLayout: Nullable
    State: Nullable
    ContentColor: Color
    BackgroundColor: Color
    IsBackgroundColorNone: Nullable
    Alignment: Nullable
    Style: str
    BottomRightPlusOne: Cell
    BottomRight: Cell
    TopLeft: Cell
    RightColumn: int
    BottomRow: int
    LeftColumn: int
    TopRow: int
    IsNull: bool
    ParentTable: Table

class RowType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.RowType"""
    def __init__(self, *args) -> None: ...
    UnknownRow: int  # = 0
    DataRow: int  # = 1
    TitleRow: int  # = 2
    HeaderRow: int  # = 4
class RowsCollection:
    """.NET: Autodesk.AutoCAD.DatabaseServices.RowsCollection"""
    def __init__(self, *args) -> None: ...
    Item: Row
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...

class SaveType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.SaveType"""
    def __init__(self, *args) -> None: ...
    NoSave: int  # = 0
    Save12: int  # = 1
    Save13: int  # = 2
    Save14: int  # = 3
    Save2000: int  # = 4
    Save2004: int  # = 5
    Save2007: int  # = 6
    Save2010: int  # = 7
    Save2013: int  # = 8
    Save2018: int  # = 9
class ScaleEstimationMethod:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.ScaleEstimationMethod"""
    def __init__(self, *args) -> None: ...
    ScaleEstMethodUnity: int  # = 1
    ScaleEstMethodUserDefined: int  # = 2
    ScaleEstMethodReferencePoint: int  # = 3
    ScaleEstMethodPrismoidal: int  # = 4
class Section(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Section"""
    def __init__(self, *args) -> None: ...
    SectionPlaneOffset: float
    BottomPlane: float
    TopPlane: float
    Elevation: float
    IsLiveSectionEnabled: bool
    Settings: ObjectId
    Boundary: IList
    Vertices: Point3dCollection
    NumVertices: int
    IndicatorFillColor: Color
    IndicatorTransparency: int
    Normal: Vector3d
    VerticalDirection: Vector3d
    ViewingDirection: Vector3d
    Name: str
    HasJogs: bool
    ThicknessDepth: float
    IsSlice: bool
    State: SectionState
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddVertex(self, nInsertAt: int, pt: Point3d) -> None: ...
    def CreateJog(self, ptOnSection: Point3d) -> None: ...
    def GenerateSectionGeometry(self, pEnt: Entity, pIntFillEnts: Array, pBackgroundEnts: Array, pForegroundEnts: Array, pFurveTangencyEnts: Array, pCurveTangencyEnts: Array) -> None: ...
    def GetVertex(self, nIndex: int) -> Point3d: ...
    def GetVertices(self, pts: Point3dCollection) -> None: ...
    def Height(self, nHeightType: SectionHeight) -> float: ...
    def HitTest(self, ptHit: Point3d) -> SectionHitTestInfo: ...
    def RemoveVertex(self, nIndex: int) -> None: ...
    def SetHeight(self, nHeightType: SectionHeight, fHeight: float) -> None: ...
    def SetVertex(self, nIndex: int, pt: Point3d) -> None: ...

class SectionGeneration:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.SectionGeneration"""
    def __init__(self, *args) -> None: ...
    SourceAllObjects: int  # = 1
    SourceSelectedObjects: int  # = 2
    DestinationNewBlock: int  # = 16
    DestinationReplaceBlock: int  # = 32
    DestinationFile: int  # = 64
class SectionGeometry:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.SectionGeometry"""
    def __init__(self, *args) -> None: ...
    IntersectionBoundary: int  # = 1
    IntersectionFill: int  # = 2
    BackgroundGeometry: int  # = 4
    ForegroundGeometry: int  # = 8
    CurveTangencyLines: int  # = 16
class SectionHeight:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.SectionHeight"""
    def __init__(self, *args) -> None: ...
    HeightAboveSectionLine: int  # = 1
    HeightBelowSectionLine: int  # = 2
class SectionHitTestInfo:
    """.NET: Autodesk.AutoCAD.DatabaseServices.SectionHitTestInfo"""
    def __init__(self, *args) -> None: ...
    SubItem: SectionSubItem
    PtOnSegment: Point3d
    Index: int

class SectionManager(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.SectionManager"""
    def __init__(self, *args) -> None: ...
    NumSections: int
    LiveSection: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetSection(self, pszName: str) -> ObjectId: ...
    def GetUniqueSectionName(self, pszBaseName: str) -> str: ...

class SectionSettings(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.SectionSettings"""
    def __init__(self, *args) -> None: ...
    CurrentSectionType: SectionType
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Color(self, nSecType: SectionType, nGeometry: SectionGeometry) -> Color: ...
    def DestinationBlock(self, nSecType: SectionType) -> ObjectId: ...
    def DestinationFile(self, nSecType: SectionType) -> str: ...
    def DivisionLines(self, nSecType: SectionType, nGeometry: SectionGeometry) -> bool: ...
    def EdgeTransparency(self, nSecType: SectionType, nGeometry: SectionGeometry) -> int: ...
    def FaceTransparency(self, nSecType: SectionType, nGeometry: SectionGeometry) -> int: ...
    def GenerationOptions(self, nSecType: SectionType) -> SectionGeneration: ...
    def GetHatchPatternName(self, nSecType: SectionType, nGeometry: SectionGeometry) -> str: ...
    def GetHatchPatternType(self, nSecType: SectionType, nGeometry: SectionGeometry) -> HatchPatternType: ...
    def GetSourceObjects(self, nSecType: SectionType, ids: ObjectIdCollection) -> None: ...
    def HatchAngle(self, nSecType: SectionType, nGeometry: SectionGeometry) -> float: ...
    def HatchScale(self, nSecType: SectionType, nGeometry: SectionGeometry) -> float: ...
    def HatchSpacing(self, nSecType: SectionType, nGeometry: SectionGeometry) -> float: ...
    def HatchVisibility(self, nSecType: SectionType, nGeometry: SectionGeometry) -> bool: ...
    def HiddenLine(self, nSecType: SectionType, nGeometry: SectionGeometry) -> bool: ...
    def Layer(self, nSecType: SectionType, nGeometry: SectionGeometry) -> str: ...
    def LineWeight(self, nSecType: SectionType, nGeometry: SectionGeometry) -> LineWeight: ...
    def Linetype(self, nSecType: SectionType, nGeometry: SectionGeometry) -> str: ...
    def LinetypeScale(self, nSecType: SectionType, nGeometry: SectionGeometry) -> float: ...
    def PlotStyleName(self, nSecType: SectionType, nGeometry: SectionGeometry) -> str: ...
    def Reset(self, nSecType: SectionType) -> None: ...
    def SetColor(self, nSecType: SectionType, nGeometry: SectionGeometry, color: Color) -> None: ...
    def SetDestinationBlock(self, nSecType: SectionType, id: ObjectId) -> None: ...
    def SetDestinationFile(self, nSecType: SectionType, pszFileName: str) -> None: ...
    def SetDivisionLines(self, nSecType: SectionType, nGeometry: SectionGeometry, bShow: bool) -> None: ...
    def SetEdgeTransparency(self, nSecType: SectionType, nGeometry: SectionGeometry, nTransparency: int) -> None: ...
    def SetFaceTransparency(self, nSecType: SectionType, nGeometry: SectionGeometry, nTransparency: int) -> None: ...
    def SetGenerationOptions(self, nSecType: SectionType, nOptions: SectionGeneration) -> None: ...
    def SetHatchAngle(self, nSecType: SectionType, nGeometry: SectionGeometry, fAngle: float) -> None: ...
    def SetHatchPatternName(self, nSecType: SectionType, nGeometry: SectionGeometry, sNewName: str) -> None: ...
    def SetHatchPatternType(self, nSecType: SectionType, nGeometry: SectionGeometry, nPatternType: HatchPatternType) -> None: ...
    def SetHatchScale(self, nSecType: SectionType, nGeometry: SectionGeometry, fScale: float) -> None: ...
    def SetHatchSpacing(self, nSecType: SectionType, nGeometry: SectionGeometry, fSpacing: float) -> None: ...
    def SetHatchVisibility(self, nSecType: SectionType, nGeometry: SectionGeometry, bVisible: bool) -> None: ...
    def SetHiddenLine(self, nSecType: SectionType, nGeometry: SectionGeometry, bHiddenLine: bool) -> None: ...
    def SetLayer(self, nSecType: SectionType, nGeometry: SectionGeometry, pszLayer: str) -> None: ...
    def SetLineWeight(self, nSecType: SectionType, nGeometry: SectionGeometry, nLineWeight: LineWeight) -> None: ...
    def SetLinetype(self, nSecType: SectionType, nGeometry: SectionGeometry, pszLinetype: str) -> None: ...
    def SetLinetypeScale(self, nSecType: SectionType, nGeometry: SectionGeometry, fScale: float) -> None: ...
    def SetPlotStyleName(self, nSecType: SectionType, nGeometry: SectionGeometry, pszPlotStyleName: str) -> None: ...
    def SetSourceObjects(self, nSecType: SectionType, ids: ObjectIdCollection) -> None: ...
    def SetVisibility(self, nSecType: SectionType, nGeometry: SectionGeometry, bVisible: bool) -> None: ...
    def Visibility(self, nSecType: SectionType, nGeometry: SectionGeometry) -> bool: ...

class SectionState:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.SectionState"""
    def __init__(self, *args) -> None: ...
    Plane: int  # = 1
    Boundary: int  # = 2
    Volume: int  # = 4
class SectionSubItem:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.SectionSubItem"""
    def __init__(self, *args) -> None: ...
    SectionSubItemNone: int  # = 0
    SectionLine: int  # = 1
    SectionLineTop: int  # = 2
    SectionLineBottom: int  # = 4
    BackLine: int  # = 8
    BackLineTop: int  # = 16
    BackLineBottom: int  # = 32
    VerticalLineTop: int  # = 64
    VerticalLineBottom: int  # = 128
class SectionSymbol(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.SectionSymbol"""
    def __init__(self, *args) -> None: ...
    SectionPointsCount: int
    IsHalfSection: bool
    IsViewDirectionLeft: bool
    Identifier: str
    Scale: float
    SymbolStyleId: ObjectId
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddSectionPoint(self, pt: Point3d, bulge: float) -> None: ...
    def GetBulgeAt(self, index: int) -> float: ...
    def GetLabelNameAt(self, index: int) -> str: ...
    def GetLabelOffsetAt(self, index: int) -> Vector3d: ...
    def GetLabelOffsets(self, ) -> Vector3dCollection: ...
    def GetSectionPointAt(self, index: int) -> Point3d: ...
    def GetSectionPoints(self, ) -> Point3dCollection: ...
    def RemoveSectionPointAt(self, index: int) -> None: ...
    def SetLabelNameAt(self, index: int, name: str) -> None: ...
    def SetLabelOffsetAt(self, index: int, offset: Vector3d) -> None: ...
    def SetLabelOffsets(self, offsets: Vector3dCollection) -> None: ...
    def SetSectionPointAt(self, index: int, pt: Point3d, bulge: float) -> None: ...
    def SetSectionPoints(self, points: Point3dCollection, bulges: DoubleCollection) -> None: ...

class SectionType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.SectionType"""
    def __init__(self, *args) -> None: ...
    LiveSection: int  # = 1
    Section2d: int  # = 2
    Section3d: int  # = 4
class SectionViewArrowDirection:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.SectionViewArrowDirection"""
    def __init__(self, *args) -> None: ...
    TowardsCuttingPlane: int  # = 0
    AwayFromCuttingPlane: int  # = 1
class SectionViewIdentifierPosition:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.SectionViewIdentifierPosition"""
    def __init__(self, *args) -> None: ...
    EndCuttingPlane: int  # = 0
    AboveDirectionArrowLine: int  # = 1
    AboveDirectionArrowSymbol: int  # = 2
    StartDirectionArrow: int  # = 3
    EndDirectionArrow: int  # = 4
class SectionViewStyle(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.SectionViewStyle"""
    def __init__(self, *args) -> None: ...
    ShowHatching: bool
    ShowEndAndBendLines: bool
    ShowAllBendIndentifiers: bool
    ShowAllPlaneLines: bool
    ShowViewLabel: bool
    ShowArrowheads: bool
    IsContinuousLabeling: bool
    HatchTransparency: Transparency
    HatchAngles: DoubleCollection
    HatchScale: float
    HatchBackgroundColor: Color
    HatchColor: Color
    HatchPattern: str
    ViewLabelPattern: str
    ViewLabelAlignment: ModelDocViewLabelAlignmentType
    ViewLabelAttachment: ModelDocViewLabelAttachmentPoint
    ViewLabelOffset: float
    ViewLabelTextHeight: float
    ViewLabelTextColor: Color
    ViewLabelTextStyleId: ObjectId
    EndLineLength: float
    BendLineLength: float
    BendLineTypeId: ObjectId
    BendLineWeight: LineWeight
    BendLineColor: Color
    PlaneLineTypeId: ObjectId
    PlaneLineColor: Color
    PlaneLineWeight: LineWeight
    ArrowSymbolExtensionLength: float
    ArrowSymbolSize: float
    ArrowSymbolColor: Color
    ArrowEndSymbolId: ObjectId
    ArrowStartSymbolId: ObjectId
    EndLineOvershoot: float
    ArrowPosition: SectionViewArrowDirection
    IdentifierOffset: float
    IdentifierPosition: SectionViewIdentifierPosition
    IdentifierExcludeCharacters: str
    IdentifierHeight: float
    IdentifierColor: Color
    IdentifierStyleId: ObjectId
    IsModifiedForRecompute: bool
    Description: str
    Name: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def DefaultViewName(self, index: int) -> str: ...
    def GetViewLabelPattern(self, field: Field) -> str: ...
    def PostViewStyleToDb(self, dataBasePointer: Database, styleName: str) -> ObjectId: ...
    def SetDatabaseDefaults(self, dataBasePointer: Database) -> None: ...
    def SetViewLabelPattern(self, pattern: str, field: Field) -> None: ...
    def ValidateIdentifierExcludeCharacters(self, characters: str) -> bool: ...
    def ValidateViewName(self, name: str) -> bool: ...

class SecurityActions:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.SecurityActions"""
    def __init__(self, *args) -> None: ...
    EncryptData: int  # = 1
    EncryptProperties: int  # = 2
    SignData: int  # = 16
    AddTimeStamp: int  # = 32
class SecurityAlgorithm:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.SecurityAlgorithm"""
    def __init__(self, *args) -> None: ...
    RC4: int  # = 26625
class SecurityParameters:
    """.NET: Autodesk.AutoCAD.DatabaseServices.SecurityParameters"""
    def __init__(self, *args) -> None: ...
    TimeServer: str
    Comment: str
    SerialNumber: str
    Issuer: str
    Subject: str
    KeyLength: int
    Algorithm: SecurityAlgorithm
    ProviderName: str
    ProviderType: int
    Password: str
    Action: SecurityActions
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class SegmentType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.SegmentType"""
    def __init__(self, *args) -> None: ...
    Line: int  # = 0
    Arc: int  # = 1
    Coincident: int  # = 2
    Point: int  # = 3
    Empty: int  # = 4
class SelectType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.SelectType"""
    def __init__(self, *args) -> None: ...
    Window: int  # = 1
    Crossing: int  # = 2
class SequenceEnd(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.SequenceEnd"""
    def __init__(self, *args) -> None: ...
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ShadePlotResLevel:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.ShadePlotResLevel"""
    def __init__(self, *args) -> None: ...
    Draft: int  # = 0
    Preview: int  # = 1
    Normal: int  # = 2
    Presentation: int  # = 3
    Maximum: int  # = 4
    Custom: int  # = 5
class ShadePlotType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.ShadePlotType"""
    def __init__(self, *args) -> None: ...
    AsDisplayed: int  # = 0
    Wireframe: int  # = 1
    Hidden: int  # = 2
    Rendered: int  # = 3
    VisualStyle: int  # = 4
    RenderPreset: int  # = 5
class Shape(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Shape"""
    def __init__(self, *args) -> None: ...
    ShapeIndex: ObjectId
    StyleId: ObjectId
    ShapeNumber: int
    Normal: Vector3d
    Thickness: float
    Oblique: float
    WidthFactor: float
    Rotation: float
    Name: str
    Size: float
    Position: Point3d
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SkyBackground(Background):
    """.NET: Autodesk.AutoCAD.DatabaseServices.SkyBackground"""
    def __init__(self, *args) -> None: ...
    SunId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetDrawableType(self, ) -> DrawableType: ...

class Solid(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Solid"""
    def __init__(self, *args) -> None: ...
    Normal: Vector3d
    Thickness: float
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetPointAt(self, index: int) -> Point3d: ...
    def SetPointAt(self, index: int, pointValue: Point3d) -> None: ...

class Solid3d(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Solid3d"""
    def __init__(self, *args) -> None: ...
    UsesGraphicsCache: bool
    ShowHistory: bool
    RecordHistory: bool
    NumChanges: int
    IsNull: bool
    MassProperties: Solid3dMassProperties
    GeometricExtents: Extents3d
    Area: float
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def BooleanOperation(self, operation: BooleanOperationType, solid: Solid3d) -> None: ...
    def ChamferEdges(self, subentityIds: list, baseSubentityId: SubentityId, baseDist: float, otherDist: float) -> None: ...
    def CheckInterference(self, otherSolid: Solid3d) -> bool: ...
    def CleanBody(self, ) -> None: ...
    def ConvertToBrepAtSubentPaths(self, paths: list) -> None: ...
    def CopyEdge(self, subEntityId: SubentityId) -> Entity: ...
    def CopyFace(self, subEntityId: SubentityId) -> Entity: ...
    def CreateBox(self, lengthAlongX: float, lengthAlongY: float, lengthAlongZ: float) -> None: ...
    def CreateExtrudedSolid(self, sweepEntity: Entity, faceSubEntityId: SubentityId, height: float, sweepOptions: SweepOptions) -> None: ...
    def CreateFrom(self, fromEntity: Entity) -> None: ...
    def CreateFrustum(self, height: float, radiusAlongX: float, radiusAlongY: float, topRadius: float) -> None: ...
    def CreateLoftedSolid(self, crossSections: list, guides: list, path: LoftProfile, loftOptions: LoftOptions) -> None: ...
    def CreatePyramid(self, height: float, sides: int, radius: float, topRadius: float) -> None: ...
    def CreateRevolvedSolid(self, profileEntity: Entity, faceSubEntityId: SubentityId, axisPoint: Point3d, axisDir: Vector3d, angleOfRevolution: float, startAngle: float, revolveOptions: RevolveOptions) -> None: ...
    def CreateSculptedSolid(self, limitingBodies: list, limitingFlags: IntegerCollection) -> None: ...
    def CreateSphere(self, radius: float) -> None: ...
    def CreateSweptSolid(self, sweepEntity: Entity, faceSubEntityId: SubentityId, pathEntity: Entity, sweepOptions: SweepOptions) -> None: ...
    def CreateTorus(self, majorRadius: float, minorRadius: float) -> None: ...
    def CreateWedge(self, lengthAlongX: float, lengthAlongY: float, lengthAlongZ: float) -> None: ...
    def Extrude(self, region: Region, height: float, taperAngle: float) -> None: ...
    def ExtrudeAlongPath(self, region: Region, path: Curve, taperAngle: float) -> None: ...
    def ExtrudeFaces(self, subentityIds: list, height: float, taper: float) -> None: ...
    def ExtrudeFacesAlongPath(self, subentityIds: list, path: Curve) -> None: ...
    def FilletEdges(self, subentityIds: list, radius: DoubleCollection, startSetback: DoubleCollection, endSetback: DoubleCollection) -> None: ...
    def GetSection(self, plane: Plane) -> Region: ...
    def GetSubentityColor(self, subEntityId: SubentityId) -> Color: ...
    def GetSubentityMaterial(self, subEntityId: SubentityId) -> ObjectId: ...
    def GetSubentityMaterialMapper(self, subEntityId: SubentityId) -> Mapper: ...
    def ImprintEntity(self, entity: Entity) -> None: ...
    def OffsetBody(self, offsetDistance: float) -> None: ...
    def OffsetFaces(self, subentityIds: list, offsetDistance: float) -> None: ...
    def ProjectOnToSolid(self, entityToProject: Entity, projectionDirection: Vector3d) -> list: ...
    def RemoveFaces(self, subentityIds: list) -> None: ...
    def Revolve(self, region: Region, axisPoint: Point3d, axisDir: Vector3d, angleOfRevolution: float) -> None: ...
    def SeparateBody(self, ) -> list: ...
    def SetSubentityColor(self, subEntityId: SubentityId, color: Color) -> None: ...
    def SetSubentityMaterial(self, subEntityId: SubentityId, materialId: ObjectId) -> None: ...
    def SetSubentityMaterialMapper(self, subEntityId: SubentityId, mapper: Mapper) -> None: ...
    def ShellBody(self, subentityIds: list, offsetDistance: float) -> None: ...
    def Slice(self, surface: Surface, negativeHalfToo: bool) -> Solid3d: ...
    def StlOut(self, fileName: str, asciiFormat: bool) -> None: ...
    def TaperFaces(self, subentityIds: list, basePoint: Point3d, draftVector: Vector3d, draftAngle: float) -> None: ...
    def TransformFaces(self, subentityIds: list, matrix: Matrix3d) -> None: ...

class Solid3dMassProperties:
    """.NET: Autodesk.AutoCAD.DatabaseServices.Solid3dMassProperties"""
    def __init__(self, *args) -> None: ...
    PrincipalAxes: Vector3d
    Extents: Extents3d
    RadiiOfGyration: Vector3d
    PrincipalMoments: Vector3d
    ProductsOfIntertia: Vector3d
    MomentsOfIntertia: Vector3d
    Centroid: Point3d
    Volume: float

class SolidBackground(Background):
    """.NET: Autodesk.AutoCAD.DatabaseServices.SolidBackground"""
    def __init__(self, *args) -> None: ...
    Color: EntityColor
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SourceType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.SourceType"""
    def __init__(self, *args) -> None: ...
    SourceNotDefined: int  # = 0
    InventorSource: int  # = 1
    FusionSource: int  # = 2
    ModelSpaceSource: int  # = 3
class Spline(Curve):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Spline"""
    def __init__(self, *args) -> None: ...
    Type: SplineType
    IsPlanar: bool
    NurbsData: NurbsData
    FitData: FitData
    HasFitData: bool
    EndFitTangent: Vector3d
    StartFitTangent: Vector3d
    FitTolerance: float
    NumFitPoints: int
    NumControlPoints: int
    Degree: int
    IsRational: bool
    IsNull: bool
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def ElevateDegree(self, newDegree: int) -> None: ...
    def GetControlPointAt(self, index: int) -> Point3d: ...
    def GetFitPointAt(self, index: int) -> Point3d: ...
    def InsertControlPointAt(self, knotParam: float, controlPoint: Point3d, weight: float) -> ErrorStatus: ...
    def InsertFitPointAt(self, index: int, point: Point3d) -> None: ...
    def InsertKnot(self, value: float) -> None: ...
    def ModifyPositionAndTangent(self, param: float, point: Point3d, deriv: Vector3d) -> ErrorStatus: ...
    def PurgeFitData(self, ) -> None: ...
    def Rebuild(self, degree: int, numCtrlPts: int) -> ErrorStatus: ...
    def RemoveControlPointAt(self, index: int) -> ErrorStatus: ...
    def RemoveFitPointAt(self, index: int) -> None: ...
    def SetControlPointAt(self, index: int, point: Point3d) -> None: ...
    def SetFitPointAt(self, index: int, point: Point3d) -> None: ...
    def SetWeightAt(self, index: int, weight: float) -> None: ...
    def ToPolyline(self, numOfVertices: int, bConvertAsArcs: bool, bToLWPolyline: bool) -> Curve: ...
    def ToPolylineWithPrecision(self, precision: int, bConvertAsArcs: bool, bToLWPolyline: bool) -> Curve: ...
    def UpdateFitData(self, ) -> None: ...
    def WeightAt(self, index: int) -> float: ...

class SplineType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.SplineType"""
    def __init__(self, *args) -> None: ...
    FitPoints: int  # = 0
    ControlPoints: int  # = 1
class StandardScaleType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.StandardScaleType"""
    def __init__(self, *args) -> None: ...
    ScaleToFit: int  # = 0
    CustomScale: int  # = 1
    Scale1To1: int  # = 2
    Scale1To2: int  # = 3
    Scale1To4: int  # = 4
    Scale1To5: int  # = 5
    Scale1To8: int  # = 6
    Scale1To10: int  # = 7
    Scale1To16: int  # = 8
    Scale1To20: int  # = 9
    Scale1To30: int  # = 10
    Scale1To40: int  # = 11
    Scale1To50: int  # = 12
    Scale1To100: int  # = 13
    Scale2To1: int  # = 14
    Scale4To1: int  # = 15
    Scale8To1: int  # = 16
    Scale10To1: int  # = 17
    Scale100To1: int  # = 18
    Scale1To128inAnd1ft: int  # = 19
    Scale1To64inchAnd1ft: int  # = 20
    Scale1To32inchAnd1ft: int  # = 21
    Scale1To16inchAnd1ft: int  # = 22
    Scale3To32inchAnd1ft: int  # = 23
    Scale1To8inchAnd1ft: int  # = 24
    Scale3To16inchAnd1ft: int  # = 25
    Scale1To4inchAnd1ft: int  # = 26
    Scale3To8inchAnd1ft: int  # = 27
    Scale1To2inchAnd1ft: int  # = 28
    Scale3To4inchAnd1ft: int  # = 29
    Scale1inAnd1ft: int  # = 30
    Scale3inAnd1ft: int  # = 32
    Scale6inAnd1ft: int  # = 33
    Scale1ftAnd1ft: int  # = 34
class StdScaleType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.StdScaleType"""
    def __init__(self, *args) -> None: ...
    ScaleToFit: int  # = 0
    StdScale1To128InchIs1ft: int  # = 1
    StdScale1To64InchIs1ft: int  # = 2
    StdScale1To32InchIs1ft: int  # = 3
    StdScale1To16InchIs1ft: int  # = 4
    StdScale3To32InchIs1ft: int  # = 5
    StdScale1To8InchIs1ft: int  # = 6
    StdScale3To16InchIs1ft: int  # = 7
    StdScale1To4InchIs1ft: int  # = 8
    StdScale3To8InchIs1ft: int  # = 9
    StdScale1To2InchIs1ft: int  # = 10
    StdScale3To4InchIs1ft: int  # = 11
    StdScale1InchIs1ft: int  # = 12
    StdScale3InchIs1ft: int  # = 13
    StdScale6InchIs1ft: int  # = 14
    StdScale1ftIs1ft: int  # = 15
    StdScale1To1: int  # = 16
    StdScale1To2: int  # = 17
    StdScale1To4: int  # = 18
    StdScale1To5: int  # = 19
    StdScale1To8: int  # = 20
    StdScale1To10: int  # = 21
    StdScale1To16: int  # = 22
    StdScale1To20: int  # = 23
    StdScale1To30: int  # = 24
    StdScale1To40: int  # = 25
    StdScale1To50: int  # = 26
    StdScale1To100: int  # = 27
    StdScale2To1: int  # = 28
    StdScale4To1: int  # = 29
    StdScale8To1: int  # = 30
    StdScale10To1: int  # = 31
    StdScale100To1: int  # = 32
    StdScale1000To1: int  # = 33
class SubDMesh(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.SubDMesh"""
    def __init__(self, *args) -> None: ...
    VertexColorArray: list
    VertexTextureArray: Point3dCollection
    VertexNormalArray: Vector3dCollection
    SubDividedNormalArray: Vector3dCollection
    SubDividedFaceArray: Int32Collection
    SubDividedVertices: Point3dCollection
    EdgeArray: Int32Collection
    NormalArray: Vector3dCollection
    FaceArray: Int32Collection
    Vertices: Point3dCollection
    NumberOfEdges: int
    NumberOfSubDividedVertices: int
    NumberOfVertices: int
    NumberOfSubDividedFaces: int
    NumberOfFaces: int
    Watertight: bool
    SmoothLevel: int
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Cap(self, edges: list) -> None: ...
    def Collapse(self, subentityId: SubentityId) -> None: ...
    def ComputeSurfaceArea(self, ) -> float: ...
    def ComputeVolume(self, ) -> float: ...
    def ConvertToSolid(self, convertAsSmooth: bool, optimize: bool) -> Solid3d: ...
    def ConvertToSurface(self, convertAsSmooth: bool, optimize: bool) -> Surface: ...
    def ExtrudeConnectedFaces(self, paths: list, length: float, dir: Vector3d, taper: float) -> None: ...
    def ExtrudeFaces(self, paths: list, length: float, dir: Vector3d, taper: float) -> None: ...
    def GetAdjacentSubentPath(self, path: FullSubentityPath, type: SubentityType) -> list: ...
    def GetCrease(self, subentPaths: list) -> DoubleCollection: ...
    def GetFacePlane(self, subentId: SubentityId) -> Plane: ...
    def GetNumberOfSubDividedFacesAt(self, paths: list) -> int: ...
    @staticmethod
    def GetObjectMesh(dbObj: DBObject, faceterData: MeshFaceterData) -> MeshDataCollection: ...
    def GetSubDividedVertexAt(self, subentId: SubentityId) -> Point3d: ...
    def GetSubentColor(self, subentId: SubentityId) -> Color: ...
    def GetSubentMaterial(self, subentId: SubentityId) -> ObjectId: ...
    def GetSubentMaterialMapper(self, subentId: SubentityId) -> Mapper: ...
    def GetSubentPath(self, index: int, type: SubentityType) -> list: ...
    def GetVertexAt(self, subentId: SubentityId) -> Point3d: ...
    def MergeFaces(self, faces: list) -> None: ...
    def SetCone(self, majorRadius: float, minorRadius: float, height: float, divAxis: int, divHeight: int, divCap: int, radiusRatio: float, smoothLevel: int) -> None: ...
    def SetCrease(self, subentPaths: list, creaseVal: float) -> None: ...
    def SetCylinder(self, majorRadius: float, minorRadius: float, height: float, divAxis: int, divHeight: int, divCap: int, smoothLevel: int) -> None: ...
    def SetDragStatus(self, status: DragStatus) -> None: ...
    def SetPyramid(self, radius: float, height: float, divLength: int, divHeight: int, divCap: int, nSides: int, radiusRatio: float, smoothLevel: int) -> None: ...
    def SetSphere(self, radius: float, divAxis: int, divHeight: int, smoothLevel: int) -> None: ...
    def SetSubDMesh(self, vertexArray: Point3dCollection, indexArray: Int32Collection, smoothLevel: int) -> None: ...
    def SetSubentColor(self, subentId: SubentityId, color: Color) -> None: ...
    def SetSubentMaterial(self, subentId: SubentityId, matId: ObjectId) -> None: ...
    def SetSubentMaterialMapper(self, subentId: SubentityId, mapper: Mapper) -> None: ...
    def SetTorus(self, majorRadius: float, divSection: int, divSweepPath: int, sectionRadiusRatio: float, sectionRotate: float, smoothLevel: int) -> None: ...
    def SetVertexAt(self, subentId: SubentityId, position: Point3d) -> None: ...
    def SetWedge(self, xLen: float, yLen: float, zLen: float, divLength: int, divWidth: int, divHeight: int, divSlope: int, divCap: int, smoothLevel: int) -> None: ...
    def Setbox(self, xlen: float, ylen: float, zlen: float, divx: int, divy: int, divz: int, smoothLevel: int) -> None: ...
    def Spin(self, subentFaceId: SubentityId) -> None: ...
    def SplitFace(self, subentFaceId: SubentityId, subent0: SubentityId, point0: Point3d, subent1: SubentityId, point1: Point3d) -> None: ...
    def SubdDivideDown(self, ) -> None: ...
    def SubdDivideUp(self, ) -> None: ...
    def SubdRefine(self, paths: list) -> None: ...

class SubentRef(GeomRef):
    """.NET: Autodesk.AutoCAD.DatabaseServices.SubentRef"""
    def __init__(self, *args) -> None: ...
    SubentId: SubentityId
    Entity: CompoundObjectId
    IsEmpty: bool
    IsValid: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CopyFrom(self, source: SubentRef) -> None: ...
    def CreateEntity(self, ) -> Entity: ...

class SubentityGeometry:
    """.NET: Autodesk.AutoCAD.DatabaseServices.SubentityGeometry"""
    def __init__(self, *args) -> None: ...
    Curve: Curve3d
    Point: Point3d
    Type: SubentityType

class SubentityId:
    """.NET: Autodesk.AutoCAD.DatabaseServices.SubentityId"""
    def __init__(self, *args) -> None: ...
    TypeClass: RXClass
    IndexPtr: IntPtr
    Index: int
    Type: SubentityType
    Null: SubentityId
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class SubentityOverrule(Overrule):
    """.NET: Autodesk.AutoCAD.DatabaseServices.SubentityOverrule"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddSubentPaths(self, entity: Entity, paths: list) -> None: ...
    def DeleteSubentPaths(self, entity: Entity, paths: list) -> None: ...
    def GetCompoundObjectTransform(self, entity: Entity) -> Matrix3d: ...
    def GetGripPointsAtSubentPath(self, entity: Entity, subPath: FullSubentityPath, grips: GripDataCollection, curViewUnitSize: float, gripSize: int, curViewDir: Vector3d, bitFlags: GetGripPointsFlags) -> None: ...
    def GetGsMarkersAtSubentPath(self, entity: Entity, subPath: FullSubentityPath) -> list: ...
    def GetSubentClassId(self, entity: Entity, path: FullSubentityPath) -> Guid: ...
    def GetSubentPathGeomExtents(self, entity: Entity, path: FullSubentityPath) -> Extents3d: ...
    def GetSubentPathsAtGsMarker(self, entity: Entity, type: SubentityType, gsMark: IntPtr, pickPoint: Point3d, viewXform: Matrix3d, entAndInsertStack: list) -> list: ...
    def MoveGripPointsAtSubentPaths(self, entity: Entity, path: list, grips: GripDataCollection, offset: Vector3d, bitFlags: MoveGripPointsFlags) -> None: ...
    def OnSubentGripStatusChanged(self, entity: Entity, status: GripStatus, subentity: FullSubentityPath) -> None: ...
    def SetCustomFilter(self, ) -> None: ...
    def SetExtensionDictionaryEntryFilter(self, entryName: str) -> None: ...
    def SetIdFilter(self, ids: list) -> None: ...
    def SetNoFilter(self, ) -> None: ...
    def SetXDataFilter(self, registeredApplicationName: str) -> None: ...
    def SubentPtr(self, entity: Entity, id: FullSubentityPath) -> Entity: ...
    def TransformSubentPathsBy(self, entity: Entity, paths: list, xform: Matrix3d) -> None: ...

class SubentityType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.SubentityType"""
    def __init__(self, *args) -> None: ...
    Null: int  # = 0
    Face: int  # = 1
    Edge: int  # = 2
    Vertex: int  # = 3
    MlineCache: int  # = 4
    Class: int  # = 5
class Sun(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Sun"""
    def __init__(self, *args) -> None: ...
    SunDirection: Vector3d
    Altitude: float
    Azimuth: float
    IsDaylightSavingsOn: bool
    DateTime: DateTime
    SkyParameters: SkyParameters
    ShadowParameters: ShadowParameters
    SunColor: Color
    Intensity: float
    IsOn: bool
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Surface(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Surface"""
    def __init__(self, *args) -> None: ...
    GeometricExtents: Extents3d
    UsesGraphicsCache: bool
    Perimeter: float
    WireframeType: WireframeTypeEnum
    VIsoLineDensity: int
    UIsoLineDensity: int
    ModificationActionBodyIds: ObjectIdCollection
    CreationActionBodyId: ObjectId
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def BooleanIntersect(self, solid: Solid3d) -> list: ...
    def BooleanSubtract(self, solid: Solid3d) -> Surface: ...
    def BooleanUnion(self, surface2: Surface) -> Surface: ...
    def ChamferEdges(self, subentityIds: list, baseSubentityId: SubentityId, baseDist: float, otherDist: float, associativeEnabled: bool) -> None: ...
    def ConvertToNurbSurface(self, ) -> list: ...
    def ConvertToRegion(self, ) -> list: ...
    @staticmethod
    def CreateBlendSurface(startProfile: LoftProfile, endProfile: LoftProfile, blendOptions: BlendOptions, associativeEnabled: bool) -> ObjectId: ...
    @staticmethod
    def CreateExtendSurface(sourceSurface: ObjectId, edges: list, extension: float, extOption: EdgeExtensionType, associativeEnabled: bool) -> ObjectId: ...
    @staticmethod
    def CreateExtrudedSurface(pSweep: Profile3d, directionVec: Vector3d, sweepOptions: SweepOptions, associativeEnabled: bool) -> ObjectId: ...
    @staticmethod
    def CreateFilletSurface(surfId1: ObjectId, pickPt1: Point3d, surfId2: ObjectId, pickPt2: Point3d, radius: float, trimMode: FilletTrimMode, projDir: Vector3d, associativeEnabled: bool) -> ObjectId: ...
    @staticmethod
    def CreateFrom(fromEntity: Entity) -> Surface: ...
    def CreateInterferenceObjects(self, ent: Entity, flags: int) -> list: ...
    @staticmethod
    def CreateLoftedSurface(crossSections: list, guides: list, path: LoftProfile, loftOptions: LoftOptions, associativeEnabled: bool) -> ObjectId: ...
    @staticmethod
    def CreateNetworkSurface(uProfiles: list, vProfiles: list, associativeEnabled: bool) -> ObjectId: ...
    @staticmethod
    def CreateOffsetSurface(entity: Entity, offsetDistance: float, associativeEnabled: bool) -> ObjectId: ...
    @staticmethod
    def CreatePatchSurface(inputPathRef: PathRef, constraintIds: ObjectIdCollection, continuity: int, bulge: float, associativeEnabled: bool) -> ObjectId: ...
    @staticmethod
    def CreateRevolvedSurface(rev: Profile3d, axisEnt: Profile3d, flipAxisDirection: bool, revAngle: float, startAngle: float, revolveOptions: RevolveOptions, associativeEnabled: bool) -> ObjectId: ...
    def CreateSectionObjects(self, sectionPlane: Plane) -> list: ...
    @staticmethod
    def CreateSweptSurface(sweep: Profile3d, path: Profile3d, sweepOptions: SweepOptions, associativeEnabled: bool) -> ObjectId: ...
    def ExtendEdges(self, edges: list, extension: float, extOption: EdgeExtensionType, associativeEnabled: bool) -> None: ...
    def FilletEdges(self, subentityIds: list, radius: DoubleCollection, startSetback: DoubleCollection, endSetback: DoubleCollection) -> None: ...
    def GetArea(self, ) -> float: ...
    def GetSubentityColor(self, subEntityId: SubentityId) -> Color: ...
    def GetSubentityMaterial(self, subEntityId: SubentityId) -> ObjectId: ...
    def GetSubentityMaterialMapper(self, subEntityId: SubentityId) -> Mapper: ...
    def ImprintEntity(self, entityToImprint: Entity) -> None: ...
    def ProjectOnToSurface(self, entityToProject: Entity, projectionDirection: Vector3d) -> list: ...
    def RayTest(self, rayBasePoint: Point3d, rayDir: Vector3d, rayRadius: float, subEntIds: list, parameters: DoubleCollection) -> None: ...
    def SetSubentityColor(self, subEntityId: SubentityId, color: Color) -> None: ...
    def SetSubentityMaterial(self, subEntityId: SubentityId, materialId: ObjectId) -> None: ...
    def SetSubentityMaterialMapper(self, subEntityId: SubentityId, mapper: Mapper) -> None: ...
    def SliceByPlane(self, slicePlane: Plane) -> SurfaceSliceResults: ...
    def SliceBySurface(self, slicingSurface: Surface) -> SurfaceSliceResults: ...
    def Thicken(self, thickness: float, bothSides: bool) -> Solid3d: ...
    @staticmethod
    def TrimSurface(blankSurfaceId: ObjectId, toolSurfaceIds: ObjectIdCollection, toolCurveIds: ObjectIdCollection, projVectors: Vector3dCollection, pickPoint: Point3d, viewVector: Vector3d, bAutoExtend: bool, associativeEnabled: bool) -> None: ...

class SurfaceSliceResults:
    """.NET: Autodesk.AutoCAD.DatabaseServices.SurfaceSliceResults"""
    def __init__(self, *args) -> None: ...
    NewSurface: Surface
    NegativeHalfSurface: Surface

class SurfaceTrimInfo(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.SurfaceTrimInfo"""
    def __init__(self, *args) -> None: ...
    ProjVector: Vector3d
    Relation: TrimRelation
    ToolBodyId: CompoundObjectId
    IsCurve: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetTrimInfo(self, surfaceId: CompoundObjectId, relation: TrimRelation, subEntityId: SubentityId) -> None: ...

class SweepOptions(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.SweepOptions"""
    def __init__(self, *args) -> None: ...
    PathEntityTransform: Matrix3d
    SweepEntityTransform: Matrix3d
    CheckIntersections: bool
    Bank: bool
    BasePoint: Point3d
    AlignStart: bool
    Align: SweepOptionsAlignOption
    AlignAngle: float
    ScaleFactor: float
    TwistAngle: float
    EndDraftDist: float
    StartDraftDist: float
    DraftAngle: float
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CheckPathCurve(self, pathEnt: Entity, displayErrorMessages: bool) -> None: ...
    def CheckSweepCurve(self, sweepEnt: Entity, displayErrorMessages: bool) -> SweepOptionsCheckSweepCurveOut: ...
    def Clone(self, ) -> object: ...

class SweepOptionsAlignOption:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.SweepOptionsAlignOption"""
    def __init__(self, *args) -> None: ...
    NoAlignment: int  # = 0
    AlignSweepEntityToPath: int  # = 1
    TranslateSweepEntityToPath: int  # = 2
    TranslatePathToSweepEntity: int  # = 3
class SweepOptionsBuilder:
    """.NET: Autodesk.AutoCAD.DatabaseServices.SweepOptionsBuilder"""
    def __init__(self, *args) -> None: ...
    PathEntityTransform: Matrix3d
    SweepEntityTransform: Matrix3d
    CheckIntersections: bool
    Bank: bool
    BasePoint: Point3d
    AlignStart: bool
    Align: SweepOptionsAlignOption
    AlignAngle: float
    ScaleFactor: float
    TwistAngle: float
    EndDraftDist: float
    StartDraftDist: float
    DraftAngle: float
    def SetPathEntityTransform(self, pathEnt: Entity, displayErrorMessages: bool) -> None: ...
    def SetSweepEntityTransform(self, sweepEntities: list, displayErrorMessages: bool) -> None: ...
    def ToSweepOptions(self, ) -> SweepOptions: ...

class SweepOptionsCheckSweepCurveOut:
    """.NET: Autodesk.AutoCAD.DatabaseServices.SweepOptionsCheckSweepCurveOut"""
    def __init__(self, *args) -> None: ...
    ApproximateArcLength: float
    Closed: bool
    Vector: Vector3d
    Point: Point3d
    Planarity: Planarity

class SweptSurface(Surface):
    """.NET: Autodesk.AutoCAD.DatabaseServices.SweptSurface"""
    def __init__(self, *args) -> None: ...
    TwistAlongPath: float
    ScaleAlongPath: float
    ProfileRotation: float
    Bank: bool
    SweepOptions: SweepOptions
    PathLength: float
    PathProfile: Profile3d
    SweepProfile: Profile3d
    PathEntity: Entity
    SweepEntity: Entity
    GeometricExtents: Extents3d
    UsesGraphicsCache: bool
    Perimeter: float
    WireframeType: WireframeTypeEnum
    VIsoLineDensity: int
    UIsoLineDensity: int
    ModificationActionBodyIds: ObjectIdCollection
    CreationActionBodyId: ObjectId
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CreateSweptSurface(self, sweepEnt: Entity, pathEnt: Entity, sweepOptions: SweepOptions) -> None: ...

class SymbolTable(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.SymbolTable"""
    def __init__(self, *args) -> None: ...
    IncludingErased: SymbolTable
    Item: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, value: SymbolTableRecord) -> ObjectId: ...
    def GetEnumerator(self, ) -> SymbolTableEnumerator: ...
    def Has(self, id: ObjectId) -> bool: ...

class SymbolTableEnumerator(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.SymbolTableEnumerator"""
    def __init__(self, *args) -> None: ...
    Current: ObjectId
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def IEnumerator.get_Current(self, ) -> object: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class SymbolTableRecord(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.SymbolTableRecord"""
    def __init__(self, *args) -> None: ...
    IsResolved: bool
    IsDependent: bool
    Name: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SymbolUtilityServices:
    """.NET: Autodesk.AutoCAD.DatabaseServices.SymbolUtilityServices"""
    def __init__(self, *args) -> None: ...
    ViewportActiveName: str
    TextStyleStandardName: str
    RegAppAcadName: str
    LinetypeContinuousName: str
    LinetypeByLayerName: str
    LinetypeByBlockName: str
    LayerZeroName: str
    LayerDefpointsName: str
    BlockPaperSpaceName: str
    BlockModelSpaceName: str
    @staticmethod
    def GetBlockModelSpaceId(databasePointer: Database) -> ObjectId: ...
    @staticmethod
    def GetBlockNameFromInsertPathName(pathName: str) -> str: ...
    @staticmethod
    def GetBlockPaperSpaceId(databasePointer: Database) -> ObjectId: ...
    @staticmethod
    def GetInsertPathNameFromBlockName(blockName: str) -> str: ...
    @staticmethod
    def GetLayerDefpointsId(database: Database) -> ObjectId: ...
    @staticmethod
    def GetLayerZeroId(database: Database) -> ObjectId: ...
    @staticmethod
    def GetLinetypeByBlockId(databasePointer: Database) -> ObjectId: ...
    @staticmethod
    def GetLinetypeByLayerId(databasePointer: Database) -> ObjectId: ...
    @staticmethod
    def GetLinetypeContinuousId(databasePointer: Database) -> ObjectId: ...
    @staticmethod
    def GetMaxSymbolNameLength(isNewName: bool, compatibilityMode: bool) -> int: ...
    @staticmethod
    def GetPathNameFromSymbolName(symbolName: str, extensions: str) -> str: ...
    @staticmethod
    def GetRegAppAcadId(databasePointer: Database) -> ObjectId: ...
    @staticmethod
    def GetSymbolNameFromPathName(pathName: str, extensions: str) -> str: ...
    @staticmethod
    def GetTextStyleStandardId(databasePointer: Database) -> ObjectId: ...
    @staticmethod
    def IsBlockLayoutName(name: str) -> bool: ...
    @staticmethod
    def IsBlockModelSpaceName(name: str) -> bool: ...
    @staticmethod
    def IsBlockPaperSpaceName(name: str) -> bool: ...
    @staticmethod
    def IsCompatibilityMode(database: Database) -> bool: ...
    @staticmethod
    def IsLayerDefpointsName(name: str) -> bool: ...
    @staticmethod
    def IsLayerZeroName(name: str) -> bool: ...
    @staticmethod
    def IsLinetypeByBlockName(name: str) -> bool: ...
    @staticmethod
    def IsLinetypeByLayerName(name: str) -> bool: ...
    @staticmethod
    def IsLinetypeContinuousName(name: str) -> bool: ...
    @staticmethod
    def IsRegAppAcadName(name: str) -> bool: ...
    @staticmethod
    def IsTextStyleStandardName(name: str) -> bool: ...
    @staticmethod
    def IsViewportActiveName(name: str) -> bool: ...
    @staticmethod
    def MakeDependentName(dwgName: str, symbolName: str) -> str: ...
    @staticmethod
    def PreValidateSymbolName(symbolName: str, preserveCase: bool) -> str: ...
    @staticmethod
    def RepairPreExtendedSymbolName(oldName: str, allowVerticalBar: bool) -> str: ...
    @staticmethod
    def RepairSymbolName(oldName: str, allowVerticalBar: bool) -> str: ...
    @staticmethod
    def ValidateCompatibleSymbolName(name: str, isNewName: bool, allowVerticalBar: bool, compatibilityMode: bool) -> ErrorStatus: ...
    @staticmethod
    def ValidatePreExtendedSymbolName(name: str, allowVerticalBar: bool) -> None: ...
    @staticmethod
    def ValidateSymbolName(name: str, allowVerticalBar: bool) -> None: ...

class SymmetricConstraint(GeometricalConstraint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.SymmetricConstraint"""
    def __init__(self, *args) -> None: ...
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SystemVariableChangedEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.SystemVariableChangedEventArgs"""
    def __init__(self, *args) -> None: ...
    Changed: bool
    Name: str

class SystemVariableChangedEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.SystemVariableChangedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: SystemVariableChangedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: SystemVariableChangedEventArgs) -> None: ...

class SystemVariableChangingEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.SystemVariableChangingEventArgs"""
    def __init__(self, *args) -> None: ...
    Name: str

class SystemVariableChangingEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.SystemVariableChangingEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: SystemVariableChangingEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: SystemVariableChangingEventArgs) -> None: ...

class Table(BlockReference):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Table"""
    def __init__(self, *args) -> None: ...
    Cells: CellRange
    Rows: RowsCollection
    Columns: ColumnsCollection
    BreakOptions: TableBreakOptions
    BreakFlowDirection: TableBreakFlowDirection
    BreakEnabled: bool
    HasSubSelection: bool
    SubSelection: CellRange
    IsHeaderSuppressed: bool
    TableStyleName: str
    IsTitleSuppressed: bool
    FlowDirection: FlowDirection
    VerticalCellMargin: float
    HorizontalCellMargin: float
    MinimumTableHeight: float
    MinimumTableWidth: float
    Height: float
    Width: float
    NumColumns: int
    NumRows: int
    Direction: Vector3d
    TableStyle: ObjectId
    UnitFactor: float
    BlockUnit: UnitsValue
    Name: str
    AnonymousBlockTableRecord: ObjectId
    DynamicBlockTableRecord: ObjectId
    IsDynamicBlock: bool
    DynamicBlockReferencePropertyCollection: DynamicBlockReferencePropertyCollection
    TreatAsBlockRefForExplode: bool
    AttributeCollection: AttributeCollection
    BlockTransform: Matrix3d
    Normal: Vector3d
    Rotation: float
    ScaleFactors: Scale3d
    Position: Point3d
    BlockTableRecord: ObjectId
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Alignment(self, row: int, col: int) -> CellAlignment: ...
    def AttachmentPoint(self, row: int, col: int) -> Point3d: ...
    def BackgroundColor(self, row: int, col: int) -> Color: ...
    def BlockRotation(self, row: int, col: int) -> float: ...
    def BlockScale(self, row: int, col: int) -> float: ...
    def BlockTableRecordId(self, row: int, col: int) -> ObjectId: ...
    def CanDeleteColumns(self, index: int, nCount: int) -> bool: ...
    def CanDeleteRows(self, index: int, nCount: int) -> bool: ...
    def CanInsertColumn(self, index: int) -> bool: ...
    def CanInsertRow(self, index: int) -> bool: ...
    def CellStyleOverrides(self, row: int, col: int) -> list: ...
    def CellType(self, row: int, col: int) -> TableCellType: ...
    def ClearSubSelection(self, ) -> None: ...
    def ClearTableStyleOverrides(self, options: int) -> None: ...
    def ColumnWidth(self, col: int) -> float: ...
    def ContentColor(self, row: int, col: int) -> Color: ...
    def CopyFrom(self, source: Table, options: TableCopyOptions, sourceRange: CellRange, targetRange: CellRange) -> CellRange: ...
    def CreateContent(self, row: int, column: int, contentIndex: int) -> int: ...
    def DataType(self, row: int, col: int) -> DataType: ...
    def DeleteCellContent(self, row: int, col: int) -> None: ...
    def DeleteColumns(self, col: int, columns: int) -> None: ...
    def DeleteContent(self, row: int, column: int, contentIndex: int) -> None: ...
    def DeleteRows(self, row: int, rows: int) -> None: ...
    def FieldId(self, row: int, col: int) -> ObjectId: ...
    def Fill(self, fillRange: CellRange, sourceRange: CellRange, options: TableFillOptions) -> None: ...
    def Format(self, row: int, col: int) -> str: ...
    def GenerateLayout(self, ) -> None: ...
    def GetBlockAttributeValue(self, row: int, column: int, contentIndex: int, attDefId: ObjectId) -> str: ...
    def GetBlockTableRecordId(self, row: int, column: int, contentIndex: int) -> ObjectId: ...
    def GetBreakHeight(self, index: int) -> float: ...
    def GetBreakOffset(self, index: int) -> Vector3d: ...
    def GetBreakSpacing(self, ) -> float: ...
    def GetCellExtents(self, row: int, col: int, isOuterCell: bool, pts: Point3dCollection) -> None: ...
    def GetCellState(self, row: int, column: int) -> CellStates: ...
    def GetCellStyle(self, row: int, column: int) -> str: ...
    def GetColumnName(self, index: int) -> str: ...
    def GetContentColor(self, row: int, column: int, contentIndex: int) -> Color: ...
    def GetContentLayout(self, row: int, column: int) -> CellContentLayout: ...
    def GetContentTypes(self, row: int, column: int, contentIndex: int) -> CellContentTypes: ...
    def GetCustomData(self, row: int, column: int, key: str) -> object: ...
    def GetDataFormat(self, row: int, column: int, contentIndex: int) -> str: ...
    def GetDataLink(self, row: int, column: int) -> ObjectId: ...
    def GetDataLinkRange(self, row: int, column: int) -> CellRange: ...
    def GetDataType(self, row: int, column: int, contentIndex: int) -> DataTypeParameter: ...
    def GetEnumerator(self, range: CellRange, option: TableEnumeratorOption) -> TableEnumerator: ...
    def GetFieldId(self, row: int, column: int, contentIndex: int) -> ObjectId: ...
    def GetFormula(self, row: int, column: int, contentIndex: int) -> str: ...
    def GetGridColor(self, row: int, column: int, gridLineType: GridLineType) -> Color: ...
    def GetGridDoubleLineSpacing(self, row: int, column: int, gridLineType: GridLineType) -> float: ...
    def GetGridLineStyle(self, row: int, column: int, gridLineType: GridLineType) -> GridLineStyle: ...
    def GetGridLineWeight(self, row: int, column: int, gridLineType: GridLineType) -> LineWeight: ...
    def GetGridLinetype(self, row: int, column: int, gridLineType: GridLineType) -> ObjectId: ...
    def GetGridProperty(self, row: int, column: int, gridLineType: GridLineType) -> GridPropertyParameter: ...
    def GetGridVisibility(self, row: int, column: int, gridLineType: GridLineType) -> Visibility: ...
    def GetIsAutoScale(self, row: int, column: int, contentIndex: int) -> bool: ...
    def GetMargin(self, row: int, column: int, margin: CellMargins) -> float: ...
    def GetMergeAllEnabled(self, row: int, column: int) -> bool: ...
    def GetMergeRange(self, row: int, column: int) -> CellRange: ...
    def GetNumberOfContents(self, row: int, column: int) -> int: ...
    def GetOverrides(self, row: int, column: int, gridLineType: GridLineType) -> CellProperties: ...
    def GetRotation(self, row: int, column: int, contentIndex: int) -> float: ...
    def GetScale(self, row: int, column: int, contentIndex: int) -> float: ...
    def GetTextHeight(self, row: int, column: int, contentIndex: int) -> float: ...
    def GetTextString(self, row: int, column: int, contentIndex: int, formatOption: FormatOption) -> str: ...
    def GetTextStyleId(self, row: int, column: int, contentIndex: int) -> ObjectId: ...
    def GetToolTip(self, row: int, column: int) -> str: ...
    def GetValue(self, row: int, column: int, contentIndex: int, formatOption: FormatOption) -> object: ...
    def GridColor(self, row: int, col: int, edge: CellEdgeMasks) -> Color: ...
    def GridLineWeight(self, row: int, col: int, edge: CellEdgeMasks) -> LineWeight: ...
    def GridVisibility(self, row: int, col: int, edge: CellEdgeMasks) -> bool: ...
    def HasFormula(self, row: int, column: int, contentIndex: int) -> bool: ...
    def HitTest(self, point: Point3d, viewVector: Vector3d) -> TableHitTestInfo: ...
    def IEnumerable.GetEnumerator(self, ) -> IEnumerator: ...
    def InsertColumns(self, col: int, width: float, columns: int) -> None: ...
    def InsertColumnsAndInherit(self, col: int, inheritFrom: int, numCols: int) -> None: ...
    def InsertRows(self, row: int, height: float, rows: int) -> None: ...
    def InsertRowsAndInherit(self, index: int, inheritFrom: int, numRows: int) -> None: ...
    def IsAutoScale(self, row: int, col: int) -> bool: ...
    def IsBackgroundColorNone(self, row: int, col: int) -> bool: ...
    def IsContentEditable(self, row: int, column: int) -> bool: ...
    def IsEmpty(self, row: int, column: int) -> bool: ...
    def IsFormatEditable(self, row: int, column: int) -> bool: ...
    def IsLinked(self, row: int, column: int) -> bool: ...
    def IsMergedCell(self, row: int, col: int, range: CellRange) -> bool: ...
    def MergeCells(self, range: CellRange) -> None: ...
    def MinimumColumnWidth(self, col: int) -> float: ...
    def MinimumRowHeight(self, row: int) -> float: ...
    def MoveContent(self, row: int, column: int, fromIndex: int, toIndex: int) -> None: ...
    def RecomputeTableBlock(self, forceUpdate: bool) -> None: ...
    def RemoveAllOverrides(self, row: int, column: int) -> None: ...
    def RemoveDataLink(self, row: int, column: int) -> None: ...
    def ReselectSubRegion(self, paths: list) -> None: ...
    def ResetValue(self, row: int, col: int) -> None: ...
    def RowHeight(self, row: int) -> float: ...
    def RowType(self, row: int) -> RowType: ...
    def Select(self, pickingPoint: Point3d, hitTestViewDirection: Vector3d, hitTestViewOrientation: Vector3d, allowOutside: bool, inPickFirst: bool, paths: list) -> TableHitTestInfo: ...
    def SelectSubRegion(self, cornerPoint1: Point3d, cornerPoint2: Point3d, selectionViewDirection: Vector3d, hitTestViewDirection: Vector3d, selectionType: SelectType, includeCurrentSelection: bool, inPickFirst: bool, paths: list) -> CellRange: ...
    def SetAlignment(self, row: int, col: int, align: CellAlignment) -> None: ...
    def SetAutoScale(self, row: int, col: int, autoFit: bool) -> None: ...
    def SetBackgroundColor(self, row: int, col: int, color: Color) -> None: ...
    def SetBackgroundColorNone(self, row: int, col: int, value: bool) -> None: ...
    def SetBlockAttributeValue(self, row: int, column: int, contentIndex: int, attDefId: ObjectId, value: str) -> None: ...
    def SetBlockRotation(self, row: int, col: int, rotationalAngle: float) -> None: ...
    def SetBlockScale(self, row: int, col: int, scale: float) -> None: ...
    def SetBlockTableRecordId(self, row: int, column: int, contentIndex: int, blockId: ObjectId, autoFit: bool) -> None: ...
    def SetBreakHeight(self, index: int, height: float) -> None: ...
    def SetBreakOffset(self, index: int, offset: Vector3d) -> None: ...
    def SetBreakSpacing(self, spacing: float) -> None: ...
    def SetCellState(self, row: int, column: int, cellState: CellStates) -> None: ...
    def SetCellStyle(self, row: int, column: int, styleName: str) -> None: ...
    def SetCellType(self, row: int, col: int, type: TableCellType) -> None: ...
    def SetColumnName(self, index: int, name: str) -> None: ...
    def SetColumnWidth(self, col: int, width: float) -> None: ...
    def SetContentColor(self, row: int, column: int, contentIndex: int, color: Color) -> None: ...
    def SetContentLayout(self, row: int, column: int, layout: CellContentLayout) -> None: ...
    def SetCustomData(self, row: int, column: int, key: str, value: object) -> None: ...
    def SetDataFormat(self, row: int, column: int, contentIndex: int, format: str) -> None: ...
    def SetDataLink(self, row: int, column: int, dataLinkId: ObjectId, bUpdate: bool) -> None: ...
    def SetDataType(self, row: int, column: int, contentIndex: int, dataType: DataTypeParameter) -> None: ...
    def SetFieldId(self, row: int, column: int, contentIndex: int, fieldId: ObjectId, option: CellOption) -> None: ...
    def SetFormat(self, row: int, col: int, pFormat: str) -> None: ...
    def SetFormula(self, row: int, column: int, contentIndex: int, formula: str) -> None: ...
    def SetGridColor(self, row: int, column: int, gridLineType: GridLineType, color: Color) -> None: ...
    def SetGridDoubleLineSpacing(self, row: int, column: int, gridLineType: GridLineType, spacing: float) -> None: ...
    def SetGridLineStyle(self, row: int, column: int, gridLineType: GridLineType, lineStyle: GridLineStyle) -> None: ...
    def SetGridLineWeight(self, row: int, column: int, gridLineType: GridLineType, lineWeight: LineWeight) -> None: ...
    def SetGridLinetype(self, row: int, column: int, gridLineType: GridLineType, linetype: ObjectId) -> None: ...
    def SetGridProperty(self, row: int, column: int, gridLineType: GridLineType, gridProperty: GridPropertyParameter) -> None: ...
    def SetGridVisibility(self, row: int, column: int, gridLineType: GridLineType, visibility: Visibility) -> None: ...
    def SetIsAutoScale(self, row: int, column: int, contentIndex: int, autoFit: bool) -> None: ...
    def SetMargin(self, row: int, column: int, margin: CellMargins, value: float) -> None: ...
    def SetMergeAllEnabled(self, row: int, column: int, enable: bool) -> None: ...
    def SetOverrides(self, row: int, column: int, gridLineType: GridLineType, override: CellProperties) -> None: ...
    def SetRotation(self, row: int, column: int, contentIndex: int, angle: float) -> None: ...
    def SetRowHeight(self, row: int, height: float) -> None: ...
    def SetScale(self, row: int, column: int, contentIndex: int, scale: float) -> None: ...
    def SetSize(self, numRows: int, numCols: int) -> None: ...
    def SetTextHeight(self, row: int, column: int, contentIndex: int, height: float) -> None: ...
    def SetTextRotation(self, row: int, col: int, rot: RotationAngle) -> None: ...
    def SetTextString(self, row: int, column: int, contentIndex: int, text: str) -> None: ...
    def SetTextStyle(self, row: int, col: int, id: ObjectId) -> None: ...
    def SetTextStyleId(self, row: int, column: int, contentIndex: int, id: ObjectId) -> None: ...
    def SetToolTip(self, row: int, column: int, toolTip: str) -> None: ...
    def SetValue(self, row: int, column: int, contentIndex: int, value: str, parseOption: ParseOption) -> None: ...
    def SuppressRegenerateTable(self, suppress: bool) -> None: ...
    def TableStyleOverrides(self, ) -> list: ...
    def TextHeight(self, row: int, col: int) -> float: ...
    def TextRotation(self, row: int, col: int) -> RotationAngle: ...
    def TextString(self, row: int, col: int, nOption: FormatOption) -> str: ...
    def TextStringConst(self, row: int, col: int) -> str: ...
    def TextStyle(self, row: int, col: int) -> ObjectId: ...
    def UnitType(self, row: int, col: int) -> UnitType: ...
    def UnmergeCells(self, range: CellRange) -> None: ...
    def UpdateDataLink(self, row: int, column: int, dir: UpdateDirection, option: UpdateOption) -> None: ...
    def Value(self, row: int, col: int) -> object: ...

class TableBreakFlowDirection:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.TableBreakFlowDirection"""
    def __init__(self, *args) -> None: ...
    Right: int  # = 1
    DownOrUp: int  # = 2
    Left: int  # = 4
class TableBreakOptions:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.TableBreakOptions"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    EnableBreaking: int  # = 1
    RepeatTopLabels: int  # = 2
    RepeatBottomLabels: int  # = 4
    AllowManualPositions: int  # = 8
    AllowManualHeights: int  # = 16
class TableCellType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.TableCellType"""
    def __init__(self, *args) -> None: ...
    UnknownCell: int  # = 0
    TextCell: int  # = 1
    BlockCell: int  # = 2
    MultipleContentCell: int  # = 3
class TableContent(FormattedTableData):
    """.NET: Autodesk.AutoCAD.DatabaseServices.TableContent"""
    def __init__(self, *args) -> None: ...
    TableStyleId: ObjectId
    NumberOfRows: int
    NumberOfColumns: int
    Name: str
    IsEmpty: bool
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetCellStyle(self, row: int, column: int) -> str: ...
    def GetColumnWidth(self, column: int) -> float: ...
    def GetRowHeight(self, row: int) -> float: ...
    def SetCellStyle(self, row: int, column: int, cellStyle: str) -> None: ...
    def SetColumnWidth(self, column: int, width: float) -> None: ...
    def SetRowHeight(self, row: int, height: float) -> None: ...

class TableCopyOptions:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.TableCopyOptions"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    ExpandOrContractTable: int  # = 1
    SkipContent: int  # = 2
    SkipValue: int  # = 4
    SkipField: int  # = 8
    SkipFormula: int  # = 16
    SkipBlock: int  # = 32
    SkipDataLink: int  # = 64
    SkipLabelCell: int  # = 128
    SkipDataCell: int  # = 256
    SkipFormat: int  # = 512
    SkipCellStyle: int  # = 1024
    ConvertFormatToOverrides: int  # = 2048
    SkipCellState: int  # = 4096
    SkipContentFormat: int  # = 8192
    SkipDissimilarContentFormat: int  # = 16384
    SkipGeometry: int  # = 32768
    SkipMerges: int  # = 65536
    FillTarget: int  # = 131072
    OverwriteReadOnlyContent: int  # = 262144
    OverwriteReadOnlyFormat: int  # = 524288
    OverwriteContentModifiedAfterUpdate: int  # = 1048576
    OverwriteFormatModifiedAfterUpdate: int  # = 2097152
    OnlyContentModifiedAfterUpdate: int  # = 4194304
    OnlyFormatModifiedAfterUpdate: int  # = 8388608
    TableCopyRowHeight: int  # = 16777216
    TableCopyColumnWidth: int  # = 33554432
class TableEnumerator(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.TableEnumerator"""
    def __init__(self, *args) -> None: ...
    Current: Cell
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class TableEnumeratorOption:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.TableEnumeratorOption"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    IterateSelection: int  # = 1
    IterateRows: int  # = 2
    IterateColumns: int  # = 4
    SkipReadOnlyContent: int  # = 16
    SkipReadOnlyFormat: int  # = 32
    SkipMerged: int  # = 64
class TableFillOptions:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.TableFillOptions"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Row: int  # = 1
    Reverse: int  # = 2
    GenerateSeries: int  # = 4
    CopyContent: int  # = 8
    CopyFormat: int  # = 16
    OverwriteReadOnlyContent: int  # = 32
    OverwriteReadOnlyFormat: int  # = 64
class TableHitTestInfo:
    """.NET: Autodesk.AutoCAD.DatabaseServices.TableHitTestInfo"""
    def __init__(self, *args) -> None: ...
    Type: TableHitTestType
    Column: int
    Row: int
    def ToString(self, provider: IFormatProvider) -> str: ...

class TableHitTestType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.TableHitTestType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Cell: int  # = 1
class TableStyle(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.TableStyle"""
    def __init__(self, *args) -> None: ...
    CellStyles: ArrayList
    Template: ObjectId
    IsHeaderSuppressed: bool
    IsTitleSuppressed: bool
    VerticalCellMargin: float
    HorizontalCellMargin: float
    FlowDirection: FlowDirection
    BitFlags: int
    Description: str
    Name: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Alignment(self, rowType: RowType) -> CellAlignment: ...
    def BackgroundColor(self, rowType: RowType) -> Color: ...
    def CellClass(self, styleName: str) -> CellClass: ...
    def Color(self, rowType: RowType) -> Color: ...
    def DataType(self, rowType: RowType) -> DataType: ...
    def Format(self, rowType: RowType) -> str: ...
    def GridColor(self, gridLineType: GridLineType, rowType: RowType) -> Color: ...
    def GridDoubleLineSpacing(self, gridLineType: GridLineType, styleName: str) -> float: ...
    def GridLineStyle(self, gridLineType: GridLineType, styleName: str) -> GridLineStyle: ...
    def GridLineWeight(self, gridLineType: GridLineType, rowType: RowType) -> LineWeight: ...
    def GridLinetype(self, gridLineType: GridLineType, styleName: str) -> ObjectId: ...
    def GridVisibility(self, gridLineType: GridLineType, rowType: RowType) -> bool: ...
    def IsBackgroundColorNone(self, rowType: RowType) -> bool: ...
    def Margin(self, cellMargin: CellMargins, styleName: str) -> float: ...
    def PostTableStyleToDatabase(self, databasePointer: Database, styleName: str) -> ObjectId: ...
    def SetAlignment(self, alignment: CellAlignment, rowTypes: int) -> None: ...
    def SetBackgroundColor(self, color: Color, rowTypes: int) -> None: ...
    def SetBackgroundColorNone(self, value: bool, rowTypes: int) -> None: ...
    def SetCellClass(self, cellClass: CellClass, styleName: str) -> None: ...
    def SetColor(self, color: Color, rowTypes: int) -> None: ...
    def SetDataType(self, nDataType: DataType, nUnitType: UnitType, rowTypes: RowType) -> None: ...
    def SetFormat(self, pFormat: str, rowTypes: RowType) -> None: ...
    def SetGridColor(self, color: Color, gridLineTypes: int, rowTypes: int) -> None: ...
    def SetGridDoubleLineSpacing(self, spacing: float, gridLineTypes: GridLineType, styleName: str) -> None: ...
    def SetGridLineStyle(self, lineStyle: GridLineStyle, gridLineTypes: GridLineType, styleName: str) -> None: ...
    def SetGridLineWeight(self, lineWeight: LineWeight, gridLineTypes: int, rowTypes: int) -> None: ...
    def SetGridLinetype(self, linetype: ObjectId, gridLineTypes: GridLineType, styleName: str) -> None: ...
    def SetGridVisibility(self, visible: bool, gridLineTypes: int, rowTypes: int) -> None: ...
    def SetMargin(self, cellMargin: CellMargins, margin: float, styleName: str) -> None: ...
    def SetTextHeight(self, value: float, cellStyle: str) -> None: ...
    def SetTextStyle(self, id: ObjectId, styleName: str) -> None: ...
    def TextHeight(self, cellStyle: str) -> float: ...
    def TextStyle(self, styleName: str) -> ObjectId: ...
    def UnitType(self, rowType: RowType) -> UnitType: ...

class TableStyleFlags:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.TableStyleFlags"""
    def __init__(self, *args) -> None: ...
    HorizontalInsideLineFirst: int  # = 1
    HorizontalInsideLineSecond: int  # = 2
    HorizontalInsideLineThird: int  # = 4
    TableStyleModified: int  # = 8
class TableStyleOverride:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.TableStyleOverride"""
    def __init__(self, *args) -> None: ...
    TitleSuppressed: int  # = 1
    HeaderSuppressed: int  # = 2
    FlowDirection: int  # = 3
    HorizontalCellMargin: int  # = 4
    VerticalCellMargin: int  # = 5
    TitleRowColor: int  # = 6
    HeaderRowColor: int  # = 7
    DataRowColor: int  # = 8
    TitleRowFillNone: int  # = 9
    HeaderRowFillNone: int  # = 10
    DataRowFillNone: int  # = 11
    TitleRowFillColor: int  # = 12
    HeaderRowFillColor: int  # = 13
    DataRowFillColor: int  # = 14
    TitleRowAlignment: int  # = 15
    HeaderRowAlignment: int  # = 16
    DataRowAlignment: int  # = 17
    TitleRowTextStyle: int  # = 18
    HeaderRowTextStyle: int  # = 19
    DataRowTextStyle: int  # = 20
    TitleRowTextHeight: int  # = 21
    HeaderRowTextHeight: int  # = 22
    DataRowTextHeight: int  # = 23
    TitleRowDataType: int  # = 24
    HeaderRowDataType: int  # = 25
    DataRowDataType: int  # = 26
    TitleHorizontalTopColor: int  # = 40
    TitleHorizontalInsideColor: int  # = 41
    TitleHorizontalBottomColor: int  # = 42
    TitleVerticalLeftColor: int  # = 43
    TitleVerticalInsideColor: int  # = 44
    TitleVerticalRightColor: int  # = 45
    HeaderHorizontalTopColor: int  # = 46
    HeaderHorizontalInsideColor: int  # = 47
    HeaderHorizontalBottomColor: int  # = 48
    HeaderVerticalLeftColor: int  # = 49
    HeaderVerticalInsideColor: int  # = 50
    HeaderVerticalRightColor: int  # = 51
    DataHorizontalTopColor: int  # = 52
    DataHorizontalInsideColor: int  # = 53
    DataHorizontalBottomColor: int  # = 54
    DataVerticalLeftColor: int  # = 55
    DataVerticalInsideColor: int  # = 56
    DataVerticalRightColor: int  # = 57
    TitleHorizontalTopLineWeight: int  # = 70
    TitleHorizontalInsideLineWeight: int  # = 71
    TitleHorizontalBottomLineWeight: int  # = 72
    TitleVerticalLeftLineWeight: int  # = 73
    TitleVerticalInsideLineWeight: int  # = 74
    TitleVerticalRightLineWeight: int  # = 75
    HeaderHorizontalTopLineWeight: int  # = 76
    HeaderHorizontalInsideLineWeight: int  # = 77
    HeaderHorizontalBottomLineWeight: int  # = 78
    HeaderVerticalLeftLineWeight: int  # = 79
    HeaderVerticalInsideLineWeight: int  # = 80
    HeaderVerticalRightLineWeight: int  # = 81
    DataHorizontalTopLineWeight: int  # = 82
    DataHorizontalInsideLineWeight: int  # = 83
    DataHorizontalBottomLineWeight: int  # = 84
    DataVerticalLeftLineWeight: int  # = 85
    DataVerticalInsideLineWeight: int  # = 86
    DataVerticalRightLineWeight: int  # = 87
    TitleHorizontalTopVisibility: int  # = 100
    TitleHorizontalInsideVisibility: int  # = 101
    TitleHorizontalBottomVisibility: int  # = 102
    TitleVerticalLeftVisibility: int  # = 103
    TitleVerticalInsideVisibility: int  # = 104
    TitleVerticalRightVisibility: int  # = 105
    HeaderHorizontalTopVisibility: int  # = 106
    HeaderHorizontalInsideVisibility: int  # = 107
    HeaderHorizontalBottomVisibility: int  # = 108
    HeaderVerticalLeftVisibility: int  # = 109
    HeaderVerticalInsideVisibility: int  # = 110
    HeaderVerticalRightVisibility: int  # = 111
    DataHorizontalTopVisibility: int  # = 112
    DataHorizontalInsideVisibility: int  # = 113
    DataHorizontalBottomVisibility: int  # = 114
    DataVerticalLeftVisibility: int  # = 115
    DataVerticalInsideVisibility: int  # = 116
    DataVerticalRightVisibility: int  # = 117
    CellAlignment: int  # = 130
    CellBackgroundFillNone: int  # = 131
    CellBackgroundColor: int  # = 132
    CellContentColor: int  # = 133
    CellTextStyle: int  # = 134
    CellTextHeight: int  # = 135
    CellTopGridColor: int  # = 136
    CellRightGridColor: int  # = 137
    CellBottomGridColor: int  # = 138
    CellLeftGridColor: int  # = 139
    CellTopGridLineWeight: int  # = 140
    CellRightGridLineWeight: int  # = 141
    CellBottomGridLineWeight: int  # = 142
    CellLeftGridLineWeight: int  # = 143
    CellTopVisibility: int  # = 144
    CellRightVisibility: int  # = 145
    CellBottomVisibility: int  # = 146
    CellLeftVisibility: int  # = 147
    CellDataType: int  # = 148
class TableTemplate(TableContent):
    """.NET: Autodesk.AutoCAD.DatabaseServices.TableTemplate"""
    def __init__(self, *args) -> None: ...
    TableStyleId: ObjectId
    NumberOfRows: int
    NumberOfColumns: int
    Name: str
    IsEmpty: bool
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Capture(self, table: Table, copyOption: TableCopyOptions) -> None: ...
    def CreateTable(self, copyOption: TableCopyOptions) -> Table: ...

class TangentConstraint(GeometricalConstraint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.TangentConstraint"""
    def __init__(self, *args) -> None: ...
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class TextAlignment:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.TextAlignment"""
    def __init__(self, *args) -> None: ...
    LeftAlignment: int  # = 0
    CenterAlignment: int  # = 1
    RightAlignment: int  # = 2
class TextAlignmentType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.TextAlignmentType"""
    def __init__(self, *args) -> None: ...
    LeftAlignment: int  # = 0
    CenterAlignment: int  # = 1
    RightAlignment: int  # = 2
class TextAngleType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.TextAngleType"""
    def __init__(self, *args) -> None: ...
    InsertAngle: int  # = 0
    HorizontalAngle: int  # = 1
    AlwaysRightReadingAngle: int  # = 2
class TextAttachmentDirection:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.TextAttachmentDirection"""
    def __init__(self, *args) -> None: ...
    AttachmentHorizontal: int  # = 0
    AttachmentVertical: int  # = 1
class TextAttachmentType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.TextAttachmentType"""
    def __init__(self, *args) -> None: ...
    AttachmentTopOfTop: int  # = 0
    AttachmentMiddleOfTop: int  # = 1
    AttachmentMiddle: int  # = 2
    AttachmentMiddleOfBottom: int  # = 3
    AttachmentBottomOfBottom: int  # = 4
    AttachmentBottomLine: int  # = 5
    AttachmentBottomOfTopLine: int  # = 6
    AttachmentBottomOfTop: int  # = 7
    AttachmentAllLine: int  # = 8
    AttachmentCenter: int  # = 9
    AttachmentLinedCenter: int  # = 10
class TextEditor(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.TextEditor"""
    def __init__(self, *args) -> None: ...
    EndOfText: TextEditorLocation
    StartOfText: TextEditorLocation
    DefaultStackAlignment: FlowAlign
    DefaultStackScale: float
    StackCount: int
    VerticalTTF: bool
    VerticalSHX: bool
    FontCount: int
    TabOnlyDelimiter: bool
    AutoListEnabled: bool
    NumberingEnabled: bool
    AutoCAPS: bool
    ActualHeight: float
    ActualWidth: float
    TextHeight: float
    DefinedHeight: float
    DefinedWidth: float
    Attachment: AttachmentPoint
    StyleCount: int
    IsAnnotativeStyle: bool
    Style: ObjectId
    Paragraphs: list
    Wipeout: TextEditorWipeout
    Cursor: TextEditorCursor
    Selection: TextEditorSelection
    Columns: TextEditorColumns
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def ClearSelection(self, ) -> None: ...
    def Close(self, stat: ExitStatus) -> None: ...
    @staticmethod
    def CreateTextEditor(mtext: MText) -> TextEditor: ...
    def FindTextW(self, findString: str, findFlags: TextFindFlags, start: TextEditorLocation, end: TextEditorLocation) -> None: ...
    def GetFont(self, index: int) -> Font: ...
    def MakeSelection(self, start: TextEditorLocation, end: TextEditorLocation) -> None: ...
    def Redraw(self, ) -> None: ...
    def SelectAll(self, ) -> None: ...

class TextEditorColumn(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.TextEditorColumn"""
    def __init__(self, *args) -> None: ...
    Height: float
    EndOfText: TextEditorLocation
    StartOfText: TextEditorLocation
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class TextEditorColumns(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.TextEditorColumns"""
    def __init__(self, *args) -> None: ...
    IsFlowReversed: bool
    TotalWidth: float
    Gutter: float
    Width: float
    AutoHeight: bool
    Type: ColumnType
    Item: TextEditorColumn
    Count: int
    MaxCount: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class TextEditorCursor(TextEditorSelectionbase):
    """.NET: Autodesk.AutoCAD.DatabaseServices.TextEditorCursor"""
    def __init__(self, *args) -> None: ...
    Column: TextEditorColumn
    Paragraph: TextEditorParagraph
    Location: TextEditorLocation
    FlowAlignment: FlowAlign
    WidthScale: float
    TrackingFactor: float
    ObliqueAngle: float
    Strikethrough: bool
    Overline: bool
    Underline: bool
    Color: Color
    Height: float
    Italic: bool
    Bold: bool
    Font: Font
    Language: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class TextEditorLocation(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.TextEditorLocation"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class TextEditorParagraph(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.TextEditorParagraph"""
    def __init__(self, *args) -> None: ...
    MaxSpacingValue: float
    MinSpacingValue: float
    MaxLineSpacingFactor: float
    MinLineSpacingFactor: float
    TabsCount: int
    ParaNumberingType: NumberingType
    SpaceAfter: float
    SpaceBefore: float
    LineSpaceFactor: float
    LineSpaceStyle: LineSpacingStyle
    RightIndent: float
    LeftIndent: float
    FirstIndent: float
    Alignment: AlignmentType
    EndOfText: TextEditorLocation
    StartOfText: TextEditorLocation
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddTab(self, tab: TextEditorParagraphTab) -> None: ...
    def ContinueNumbering(self, ) -> None: ...
    def GetTab(self, idx: int) -> TextEditorParagraphTab: ...
    def RemoveTab(self, tab: TextEditorParagraphTab) -> None: ...
    def RestartNumbering(self, ) -> None: ...

class TextEditorParagraphTab:
    """.NET: Autodesk.AutoCAD.DatabaseServices.TextEditorParagraphTab"""
    def __init__(self, *args) -> None: ...
    DecimalChar: str
    Offset: float
    Type: ParagraphTabType

class TextEditorSelection(TextEditorSelectionbase):
    """.NET: Autodesk.AutoCAD.DatabaseServices.TextEditorSelection"""
    def __init__(self, *args) -> None: ...
    FieldObject: Field
    SingleFieldSelected: bool
    SingleStackSelected: bool
    SelectionString: str
    StackSettings: TextEditorStack
    CanChangeCase: bool
    Paragraphs: list
    CanStack: bool
    CanUnStack: bool
    FlowAlignment: FlowAlign
    WidthScale: float
    TrackingFactor: float
    ObliqueAngle: float
    Strikethrough: bool
    Overline: bool
    Underline: bool
    Color: Color
    Height: float
    Italic: bool
    Bold: bool
    Font: Font
    Language: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CanSupportFont(self, font: Font) -> bool: ...
    def CanSupportLanguage(self, charset: int) -> bool: ...
    def ChangeToLowercase(self, ) -> bool: ...
    def ChangeToUppercase(self, ) -> bool: ...
    def CombineParagraphs(self, ) -> None: ...
    def ConvertToPlainText(self, ) -> None: ...
    def RemoveAllFormatting(self, ) -> None: ...
    def RemoveCharacterFormatting(self, ) -> None: ...
    def RemoveParagraphFormatting(self, ) -> None: ...
    def Stack(self, ) -> None: ...
    def UnStack(self, ) -> None: ...
    def UpdateField(self, ) -> None: ...

class TextEditorSelectionbase(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.TextEditorSelectionbase"""
    def __init__(self, *args) -> None: ...
    MaxWidthScale: float
    MinWidthScale: float
    MaxTrackingFactor: float
    MinTrackingFactor: float
    MaxObliqueAngle: float
    MinObliqueAngle: float
    FlowAlignment: FlowAlign
    WidthScale: float
    TrackingFactor: float
    ObliqueAngle: float
    Strikethrough: bool
    Overline: bool
    Underline: bool
    Color: Color
    Height: float
    Italic: bool
    Bold: bool
    Font: Font
    Language: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def InputSpecialChar(self, ch: str) -> None: ...
    def InsertColumnBreak(self, ) -> None: ...
    def InsertImportedText(self, type: InsertTextType, data: list) -> None: ...
    def InsertString(self, string: str) -> None: ...
    def InsertSymbol(self, ch: str, langId: int) -> None: ...

class TextEditorStack:
    """.NET: Autodesk.AutoCAD.DatabaseServices.TextEditorStack"""
    def __init__(self, *args) -> None: ...
    FlowAlign: FlowAlign
    DecimalChar: str
    Scale: float
    Bottom: str
    Top: str
    Type: StackType
    MaxStackScale: float
    MinStackScale: float

class TextEditorWipeout(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.TextEditorWipeout"""
    def __init__(self, *args) -> None: ...
    BackgroundFillColor: Color
    BackgroundScaleFactor: float
    UseBackgroundColor: bool
    BackgroundFillEnabled: bool
    MaxBackgroundScaleFactor: float
    MinBackgroundScaleFactor: float
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class TextHorizontalMode:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.TextHorizontalMode"""
    def __init__(self, *args) -> None: ...
    TextLeft: int  # = 0
    TextCenter: int  # = 1
    TextRight: int  # = 2
    TextAlign: int  # = 3
    TextMid: int  # = 4
    TextFit: int  # = 5
class TextStyleTable(SymbolTable):
    """.NET: Autodesk.AutoCAD.DatabaseServices.TextStyleTable"""
    def __init__(self, *args) -> None: ...
    IncludingErased: SymbolTable
    Item: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class TextStyleTableRecord(SymbolTableRecord):
    """.NET: Autodesk.AutoCAD.DatabaseServices.TextStyleTableRecord"""
    def __init__(self, *args) -> None: ...
    Font: FontDescriptor
    BigFontFileName: str
    FileName: str
    PriorSize: float
    FlagBits: int
    ObliquingAngle: float
    XScale: float
    TextSize: float
    IsVertical: bool
    IsShapeFile: bool
    IsResolved: bool
    IsDependent: bool
    Name: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class TextVerticalMode:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.TextVerticalMode"""
    def __init__(self, *args) -> None: ...
    TextBase: int  # = 0
    TextBottom: int  # = 1
    TextVerticalMid: int  # = 2
    TextTop: int  # = 3
class ThreePointAngleConstraint(AngularConstraint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ThreePointAngleConstraint"""
    def __init__(self, *args) -> None: ...
    SectorType: AngularSectorType
    MeasuredValue: float
    DimDependencyId: ObjectId
    ValueDependencyId: ObjectId
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class TimeZone:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.TimeZone"""
    def __init__(self, *args) -> None: ...
    UTC: int  # = 0
    GMT: int  # = 1
    Monrovia: int  # = 2
    Berlin: int  # = 1000
    Paris: int  # = 1001
    Prague: int  # = 1002
    Sarajevo: int  # = 1003
    WestCentralAfrica: int  # = 1004
    Athens: int  # = 2000
    EasternEurope: int  # = 2001
    Cairo: int  # = 2002
    Harare: int  # = 2003
    Helsinki: int  # = 2004
    Jerusalem: int  # = 2005
    Moscow: int  # = 3000
    Riyadh: int  # = 3001
    Baghdad: int  # = 3002
    EastAfrica: int  # = 3003
    Tehran: int  # = 3300
    AbuDhabi: int  # = 4000
    Caucasus: int  # = 4001
    Kabul: int  # = 4300
    Ekaterinburg: int  # = 5000
    Islamabad: int  # = 5001
    Kolkata: int  # = 5300
    Kathmandu: int  # = 5450
    Almaty: int  # = 6000
    Dhaka: int  # = 6001
    SriLanka: int  # = 6002
    Rangoon: int  # = 6300
    Bangkok: int  # = 7000
    Krasnoyarsk: int  # = 7001
    Beijing: int  # = 8000
    Singapore: int  # = 8001
    Taipei: int  # = 8002
    Irkutsk: int  # = 8003
    Perth: int  # = 8004
    Tokyo: int  # = 9000
    Seoul: int  # = 9001
    Yakutsk: int  # = 9002
    Adelaide: int  # = 9300
    Darwin: int  # = 9301
    Sydney: int  # = 10000
    Guam: int  # = 10001
    Brisbane: int  # = 10002
    Hobart: int  # = 10003
    Vladivostock: int  # = 10004
    Magadan: int  # = 11000
    Wellington: int  # = 12000
    Fiji: int  # = 12001
    Tonga: int  # = 13000
    InternationalDateLine: int  # = -12000
    MidwayIsland: int  # = -11000
    Hawaii: int  # = -10000
    Alaska: int  # = -9000
    Pacific: int  # = -8000
    Mazatlan: int  # = -7002
    Arizona: int  # = -7001
    Mountain: int  # = -7000
    Saskatchewan: int  # = -6003
    MexicoCity: int  # = -6002
    CentralAmerica: int  # = -6001
    Central: int  # = -6000
    Bogota: int  # = -5002
    Indiana: int  # = -5001
    Eastern: int  # = -5000
    Santiago: int  # = -4002
    Caracas: int  # = -4001
    AtlanticCanada: int  # = -4000
    Newfoundland: int  # = -3300
    Greenland: int  # = -3002
    BuenosAires: int  # = -3001
    Brasilia: int  # = -3000
    MidAtlantic: int  # = -2000
    CapeVerde: int  # = -1001
    Azores: int  # = -1000
class Trace(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Trace"""
    def __init__(self, *args) -> None: ...
    Normal: Vector3d
    Thickness: float
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetPointAt(self, index: int) -> Point3d: ...
    def SetPointAt(self, index: int, pointValue: Point3d) -> None: ...

class Transaction(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Transaction"""
    def __init__(self, *args) -> None: ...
    TransactionManager: TransactionManager
    NumberOfOpenedObjects: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Abort(self, ) -> None: ...
    def AddNewlyCreatedDBObject(self, obj: DBObject, add: bool) -> None: ...
    def Commit(self, ) -> None: ...
    def GetAllObjects(self, ) -> DBObjectCollection: ...
    def GetObject(self, id: ObjectId, mode: OpenMode, openErased: bool, forceOpenOnLockedLayer: bool) -> DBObject: ...

class TransactionManager(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.TransactionManager"""
    def __init__(self, *args) -> None: ...
    TopTransaction: Transaction
    NumberOfOpenedObjects: int
    NumberOfActiveTransactions: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddNewlyCreatedDBObject(self, obj: DBObject, add: bool) -> None: ...
    def GetAllObjects(self, ) -> DBObjectCollection: ...
    def GetObject(self, id: ObjectId, mode: OpenMode, openErased: bool, forceOpenOnLockedLayer: bool) -> DBObject: ...
    def QueueForGraphicsFlush(self, ) -> None: ...
    def StartOpenCloseTransaction(self, ) -> OpenCloseTransaction: ...
    def StartTransaction(self, ) -> Transaction: ...

class TransformOverrule(Overrule):
    """.NET: Autodesk.AutoCAD.DatabaseServices.TransformOverrule"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CloneMeForDragging(self, entity: Entity) -> bool: ...
    def Explode(self, entity: Entity, entitySet: DBObjectCollection) -> None: ...
    def GetTransformedCopy(self, entity: Entity, transform: Matrix3d) -> Entity: ...
    def HideMeForDragging(self, entity: Entity) -> bool: ...
    def SetCustomFilter(self, ) -> None: ...
    def SetExtensionDictionaryEntryFilter(self, entryName: str) -> None: ...
    def SetIdFilter(self, ids: list) -> None: ...
    def SetNoFilter(self, ) -> None: ...
    def SetXDataFilter(self, registeredApplicationName: str) -> None: ...
    def TransformBy(self, entity: Entity, transform: Matrix3d) -> None: ...

class TypeOfCoordinates:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.TypeOfCoordinates"""
    def __init__(self, *args) -> None: ...
    CoordinateTypeUnknown: int  # = 0
    CoordinateTypeLocal: int  # = 1
    CoordinateTypeGrid: int  # = 2
    CoordinateTypeGeographic: int  # = 3
class TypedValue:
    """.NET: Autodesk.AutoCAD.DatabaseServices.TypedValue"""
    def __init__(self, *args) -> None: ...
    Value: object
    TypeCode: int
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToString(self, format: str, provider: IFormatProvider) -> str: ...

class UcsTable(SymbolTable):
    """.NET: Autodesk.AutoCAD.DatabaseServices.UcsTable"""
    def __init__(self, *args) -> None: ...
    IncludingErased: SymbolTable
    Item: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class UcsTableRecord(SymbolTableRecord):
    """.NET: Autodesk.AutoCAD.DatabaseServices.UcsTableRecord"""
    def __init__(self, *args) -> None: ...
    YAxis: Vector3d
    XAxis: Vector3d
    Origin: Point3d
    IsResolved: bool
    IsDependent: bool
    Name: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetUcsBaseOrigin(self, view: OrthographicView) -> Point3d: ...
    def SetUcsBaseOrigin(self, origin: Point3d, view: OrthographicView) -> None: ...

class UnderlayDefinition(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.UnderlayDefinition"""
    def __init__(self, *args) -> None: ...
    Loaded: bool
    UnderlayItem: UnderlayItem
    ItemName: str
    ActiveFileName: str
    SourceFileName: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetDictionaryKey(underlayDefinitionType: Type) -> str: ...
    def Load(self, password: str) -> None: ...
    def SetUnderlayItem(self, sourceFileName: str, activeFileName: str, item: UnderlayItem) -> None: ...
    def Unload(self, ) -> None: ...

class UnderlayFile(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.UnderlayFile"""
    def __init__(self, *args) -> None: ...
    Items: UnderlayItemCollection
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class UnderlayHost:
    """.NET: Autodesk.AutoCAD.DatabaseServices.UnderlayHost"""
    def __init__(self, *args) -> None: ...
    PdfHost: UnderlayHost
    DgnDocHost: UnderlayHost
    DgnHost: UnderlayHost
    DwfHost: UnderlayHost
    def GetFile(self, path: str, password: str) -> UnderlayFile: ...

class UnderlayItem(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.UnderlayItem"""
    def __init__(self, *args) -> None: ...
    UsingPartialContent: bool
    Thumbnail: Bitmap
    Units: UnitsValue
    Extents: Extents2d
    Name: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class UnderlayItemCollection:
    """.NET: Autodesk.AutoCAD.DatabaseServices.UnderlayItemCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: UnderlayItem
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...

class UnderlayLayer(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.DatabaseServices.UnderlayLayer"""
    def __init__(self, *args) -> None: ...
    State: UnderlayLayerState
    Name: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class UnderlayLayerCollection:
    """.NET: Autodesk.AutoCAD.DatabaseServices.UnderlayLayerCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: UnderlayLayer
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...

class UnderlayLayerState:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.UnderlayLayerState"""
    def __init__(self, *args) -> None: ...
    Off: int  # = 0
    On: int  # = 1
class UnderlayReference(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.UnderlayReference"""
    def __init__(self, *args) -> None: ...
    IsClipInverted: bool
    Path: str
    NameOfSheet: str
    Name: str
    Width: float
    Height: float
    AdjustColorForBackground: bool
    DefaultFade: int
    FadeUpperLimit: int
    FadeLowerLimit: int
    DefaultContrast: int
    ContrastUpperLimit: int
    ContrastLowerLimit: int
    UnderlayLayerCollection: UnderlayLayerCollection
    Monochrome: bool
    Fade: int
    Contrast: int
    IsOn: bool
    IsClipped: bool
    Transform: Matrix3d
    DefinitionId: ObjectId
    Normal: Vector3d
    Rotation: float
    ScaleFactors: Scale3d
    Position: Point3d
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GenerateClipBoundaryFromPline(self, polyId: ObjectId) -> None: ...
    def GetClipBoundary(self, ) -> list: ...
    def SetClipBoundary(self, points: list) -> None: ...

class Unit:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.Unit"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Millimeter: int  # = 1
    Centimeter: int  # = 2
    Meter: int  # = 3
    Kilometer: int  # = 4
    Inch: int  # = 5
    Foot: int  # = 6
    Yard: int  # = 7
    Mile: int  # = 8
    Microinches: int  # = 9
    Mils: int  # = 10
    Angstroms: int  # = 11
    Nanometers: int  # = 12
    Microns: int  # = 13
    Decimeters: int  # = 14
    Dekameters: int  # = 15
    Hectometers: int  # = 16
    GigaMeters: int  # = 17
    Astronomical: int  # = 18
    LightYears: int  # = 19
    Parsecs: int  # = 20
class UnitType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.UnitType"""
    def __init__(self, *args) -> None: ...
    Unitless: int  # = 0
    Distance: int  # = 1
    Angle: int  # = 2
    Area: int  # = 4
    Volume: int  # = 8
    Currency: int  # = 16
    Percentage: int  # = 32
    AngleNotTransformed: int  # = 65536
class UnitTypeAttribute(Attribute):
    """.NET: Autodesk.AutoCAD.DatabaseServices.UnitTypeAttribute"""
    def __init__(self, *args) -> None: ...
    UnitType: UnitType
    TypeId: object

class UnitsConverter(TypeConverter):
    """.NET: Autodesk.AutoCAD.DatabaseServices.UnitsConverter"""
    def __init__(self, *args) -> None: ...
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool: ...
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object: ...
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object: ...
    @staticmethod
    def GetConversionFactor(from_: UnitsValue, to: UnitsValue) -> float: ...

class UnitsValue:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.UnitsValue"""
    def __init__(self, *args) -> None: ...
    Undefined: int  # = 0
    Inches: int  # = 1
    Feet: int  # = 2
    Miles: int  # = 3
    Millimeters: int  # = 4
    Centimeters: int  # = 5
    Meters: int  # = 6
    Kilometers: int  # = 7
    MicroInches: int  # = 8
    Mils: int  # = 9
    Yards: int  # = 10
    Angstroms: int  # = 11
    Nanometers: int  # = 12
    Microns: int  # = 13
    Decimeters: int  # = 14
    Dekameters: int  # = 15
    Hectometers: int  # = 16
    Gigameters: int  # = 17
    Astronomical: int  # = 18
    LightYears: int  # = 19
    Parsecs: int  # = 20
    USSurveyFeet: int  # = 21
    USSurveyInch: int  # = 22
    USSurveyYard: int  # = 23
    USSurveyMile: int  # = 24
class UpdateAction:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.UpdateAction"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Ignore: int  # = 1
    UpdateRequired: int  # = 2
class UpdateDirection:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.UpdateDirection"""
    def __init__(self, *args) -> None: ...
    SourceToData: int  # = 1
    DataToSource: int  # = 2
class UpdateOption:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.UpdateOption"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    SkipFormat: int  # = 131072
    UpdateRowHeight: int  # = 262144
    UpdateColumnWidth: int  # = 524288
    AllowSourceUpdate: int  # = 1048576
    ForceFullSourceUpdate: int  # = 2097152
    OverwriteContentModifiedAfterUpdate: int  # = 4194304
    OverwriteFormatModifiedAfterUpdate: int  # = 8388608
    ForPreview: int  # = 16777216
    IncludeXrefs: int  # = 33554432
class Vertex(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Vertex"""
    def __init__(self, *args) -> None: ...
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Vertex2d(Vertex):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Vertex2d"""
    def __init__(self, *args) -> None: ...
    Tangent: float
    TangentUsed: bool
    Bulge: float
    EndWidth: float
    StartWidth: float
    Position: Point3d
    VertexType: Vertex2dType
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Vertex2dType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.Vertex2dType"""
    def __init__(self, *args) -> None: ...
    SimpleVertex: int  # = 0
    SplineControlVertex: int  # = 1
    SplineFitVertex: int  # = 2
    CurveFitVertex: int  # = 3
class Vertex3dType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.Vertex3dType"""
    def __init__(self, *args) -> None: ...
    SimpleVertex: int  # = 0
    ControlVertex: int  # = 1
    FitVertex: int  # = 2
class VertexRef(SubentRef):
    """.NET: Autodesk.AutoCAD.DatabaseServices.VertexRef"""
    def __init__(self, *args) -> None: ...
    Point: Point3d
    SubentId: SubentityId
    Entity: CompoundObjectId
    IsEmpty: bool
    IsValid: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class VerticalConstraint(ParallelConstraint):
    """.NET: Autodesk.AutoCAD.DatabaseServices.VerticalConstraint"""
    def __init__(self, *args) -> None: ...
    IsEnabled: bool
    IsInternal: bool
    IsImplied: bool
    IsActive: bool
    OwningCompositeConstraint: CompositeConstraint
    ConnectedHelpParameters: list
    ConnectedGeometries: list
    OwningConstraintGroupId: ObjectId
    NodeId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ViewBorder(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ViewBorder"""
    def __init__(self, *args) -> None: ...
    ShadedDPI: int
    Scale: float
    RotationAngle: float
    ViewportId: ObjectId
    IsFirstAngleProjection: bool
    InventorFileReference: str
    Width: float
    Height: float
    InsertionPoint: Point3d
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetSourceType(self, ) -> SourceType: ...
    def GetViewStyleType(self, ) -> ViewStyleType: ...

class ViewRepBlockReference(BlockReference):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ViewRepBlockReference"""
    def __init__(self, *args) -> None: ...
    OwnerViewportId: ObjectId
    UnitFactor: float
    BlockUnit: UnitsValue
    Name: str
    AnonymousBlockTableRecord: ObjectId
    DynamicBlockTableRecord: ObjectId
    IsDynamicBlock: bool
    DynamicBlockReferencePropertyCollection: DynamicBlockReferencePropertyCollection
    TreatAsBlockRefForExplode: bool
    AttributeCollection: AttributeCollection
    BlockTransform: Matrix3d
    Normal: Vector3d
    Rotation: float
    ScaleFactors: Scale3d
    Position: Point3d
    BlockTableRecord: ObjectId
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ViewStyleType:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.ViewStyleType"""
    def __init__(self, *args) -> None: ...
    FromBase: int  # = 0
    WireframeVisibleEdges: int  # = 1
    WireframeHiddenEdges: int  # = 2
    ShadedVisibleEdges: int  # = 3
    ShadedHiddenEdges: int  # = 4
class ViewTable(SymbolTable):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ViewTable"""
    def __init__(self, *args) -> None: ...
    IncludingErased: SymbolTable
    Item: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ViewTableRecord(AbstractViewTableRecord):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ViewTableRecord"""
    def __init__(self, *args) -> None: ...
    Thumbnail: Bitmap
    AnnotationScale: AnnotationScale
    LiveSection: ObjectId
    ViewAssociatedToViewport: bool
    Layout: ObjectId
    LayerState: str
    CategoryName: str
    IsUcsAssociatedToView: bool
    IsPaperspaceView: bool
    ToneOperatorParameters: ToneOperatorParameters
    VisualStyleId: ObjectId
    Background: ObjectId
    ViewOrthographic: OrthographicView
    Elevation: float
    UcsName: ObjectId
    UcsOrthographic: OrthographicView
    Ucs: CoordinateSystem3d
    SunId: ObjectId
    AmbientLightColor: Color
    Contrast: float
    Brightness: float
    DefaultLightingType: DefaultLightingType
    DefaultLightingOn: bool
    FrontClipAtEye: bool
    BackClipEnabled: bool
    FrontClipEnabled: bool
    PerspectiveEnabled: bool
    BackClipDistance: float
    FrontClipDistance: float
    LensLength: float
    ViewTwist: float
    ViewDirection: Vector3d
    Target: Point3d
    Width: float
    Height: float
    CenterPoint: Point2d
    IsResolved: bool
    IsDependent: bool
    Name: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def DisassociateUcsFromView(self, ) -> None: ...

class Viewport(Entity):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Viewport"""
    def __init__(self, *args) -> None: ...
    Thumbnail: Bitmap
    AnnotationScale: AnnotationScale
    ToneOperatorParameters: ToneOperatorParameters
    LinkedToSheetView: bool
    PlotAsRaster: bool
    PlotWireframe: bool
    ShadePlotId: ObjectId
    Background: ObjectId
    ShadePlot: ShadePlotType
    UcsPerViewport: bool
    ViewOrthographic: OrthographicView
    Ucs: CoordinateSystem3d
    Elevation: float
    UcsName: ObjectId
    UcsOrthographic: OrthographicView
    NonRectClipEntityId: ObjectId
    NonRectClipOn: bool
    EffectivePlotStyleSheet: str
    PlotStyleSheet: str
    StandardScale: StandardScaleType
    CustomScale: float
    Transparent: bool
    Locked: bool
    VisualStyleId: ObjectId
    SunId: ObjectId
    AmbientLightColor: Color
    Contrast: float
    Brightness: float
    DefaultLightingType: DefaultLightingType
    DefaultLightingOn: bool
    GridMajor: int
    GridFollow: bool
    GridSubdivisionRestricted: bool
    GridAdaptive: bool
    GridBoundToLimits: bool
    HiddenLinesRemoved: bool
    GridIncrement: Vector2d
    GridOn: bool
    SnapIsoPair: int
    SnapIncrement: Vector2d
    SnapBasePoint: Point2d
    SnapAngle: float
    SnapIsometric: bool
    SnapOn: bool
    CircleSides: int
    FastZoomOn: bool
    UcsIconAtOrigin: bool
    UcsIconVisible: bool
    UcsFollowModeOn: bool
    PerspectiveOn: bool
    BackClipDistance: float
    FrontClipDistance: float
    FrontClipAtEyeOn: bool
    BackClipOn: bool
    FrontClipOn: bool
    LensLength: float
    TwistAngle: float
    ViewCenter: Point2d
    ViewHeight: float
    ViewDirection: Vector3d
    ViewTarget: Point3d
    On: bool
    Number: int
    CenterPoint: Point3d
    Width: float
    Height: float
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def FreezeLayersInViewport(self, layerIds: IEnumerator) -> None: ...
    def GetFrozenLayers(self, ) -> ObjectIdCollection: ...
    def GetPreviousBackground(self, type: DrawableType) -> ObjectId: ...
    def GetUcs(self, origin: Point3d, x: Vector3d, y: Vector3d) -> None: ...
    def IsLayerFrozenInViewport(self, layerId: ObjectId) -> bool: ...
    def SetPreviousBackground(self, value: ObjectId, type: DrawableType) -> None: ...
    def SetShadePlot(self, type: ShadePlotType, shadePlotId: ObjectId) -> None: ...
    def SetSun(self, sun: DBObject) -> ObjectId: ...
    def SetUcs(self, origin: Point3d, x: Vector3d, y: Vector3d) -> None: ...
    def SetUcsToWorld(self, ) -> None: ...
    def SetViewDirection(self, view: OrthographicView) -> None: ...
    def ThawAllLayersInViewport(self, ) -> None: ...
    def ThawLayersInViewport(self, layerIds: IEnumerator) -> None: ...
    def UpdateDisplay(self, ) -> None: ...

class ViewportTable(SymbolTable):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ViewportTable"""
    def __init__(self, *args) -> None: ...
    IncludingErased: SymbolTable
    Item: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ViewportTableRecord(AbstractViewTableRecord):
    """.NET: Autodesk.AutoCAD.DatabaseServices.ViewportTableRecord"""
    def __init__(self, *args) -> None: ...
    ToneOperatorParameters: ToneOperatorParameters
    Number: int
    GridMajor: int
    GridFollow: bool
    GridSubdivisionRestricted: bool
    GridAdaptive: bool
    GridBoundToLimits: bool
    UcsSavedWithViewport: bool
    SnapIncrements: Point2d
    SnapBase: Point2d
    SnapAngle: float
    SnapPair: int
    IsometricSnapEnabled: bool
    SnapEnabled: bool
    GridIncrements: Point2d
    GridEnabled: bool
    IconAtOrigin: bool
    IconEnabled: bool
    FastZoomsEnabled: bool
    CircleSides: int
    UcsFollowMode: bool
    UpperRightCorner: Point2d
    LowerLeftCorner: Point2d
    VisualStyleId: ObjectId
    Background: ObjectId
    ViewOrthographic: OrthographicView
    Elevation: float
    UcsName: ObjectId
    UcsOrthographic: OrthographicView
    Ucs: CoordinateSystem3d
    SunId: ObjectId
    AmbientLightColor: Color
    Contrast: float
    Brightness: float
    DefaultLightingType: DefaultLightingType
    DefaultLightingOn: bool
    FrontClipAtEye: bool
    BackClipEnabled: bool
    FrontClipEnabled: bool
    PerspectiveEnabled: bool
    BackClipDistance: float
    FrontClipDistance: float
    LensLength: float
    ViewTwist: float
    ViewDirection: Vector3d
    Target: Point3d
    Width: float
    Height: float
    CenterPoint: Point2d
    IsResolved: bool
    IsDependent: bool
    Name: str
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetPreviousBackground(self, type: DrawableType) -> ObjectId: ...
    def SetPreviousBackground(self, value: ObjectId, type: DrawableType) -> None: ...

class Visibility:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.Visibility"""
    def __init__(self, *args) -> None: ...
    Visible: int  # = 0
    Invisible: int  # = 1
class VisibilityOverrule(Overrule):
    """.NET: Autodesk.AutoCAD.DatabaseServices.VisibilityOverrule"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetCustomFilter(self, ) -> None: ...
    def SetExtensionDictionaryEntryFilter(self, entryName: str) -> None: ...
    def SetIdFilter(self, ids: list) -> None: ...
    def SetNoFilter(self, ) -> None: ...
    def SetVisibility(self, entity: Entity, newVal: Visibility, doSubents: bool) -> None: ...
    def SetXDataFilter(self, registeredApplicationName: str) -> None: ...
    def Visibility(self, entity: Entity) -> Visibility: ...

class WblockNoticeEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.WblockNoticeEventArgs"""
    def __init__(self, *args) -> None: ...
    From: Database
    To: Database

class WblockNoticeEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.WblockNoticeEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: WblockNoticeEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: WblockNoticeEventArgs) -> None: ...

class Wipeout(RasterImage):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Wipeout"""
    def __init__(self, *args) -> None: ...
    HasFrame: bool
    Width: float
    ImageTransparency: bool
    ShowImage: bool
    Rotation: float
    Position: Point3d
    Path: str
    Name: str
    ImageWidth: float
    ImageHeight: float
    Height: float
    Fade: int
    Contrast: int
    Brightness: int
    DisplayOptions: ImageDisplayOptions
    PixelToModelTransform: Matrix3d
    IsClipped: bool
    ClipBoundaryType: ClipBoundaryType
    Scale: Vector2d
    Orientation: CoordinateSystem3d
    ReactorId: ObjectId
    ImageDefId: ObjectId
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetFrom(self, points: Point2dCollection, normal: Vector3d) -> None: ...

class Xline(Curve):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Xline"""
    def __init__(self, *args) -> None: ...
    SecondPoint: Point3d
    UnitDir: Vector3d
    BasePoint: Point3d
    Area: float
    Spline: Spline
    EndPoint: Point3d
    StartPoint: Point3d
    EndParam: float
    StartParam: float
    IsPeriodic: bool
    Closed: bool
    EdgeStyleId: ObjectId
    FaceStyleId: ObjectId
    VisualStyleId: ObjectId
    ForceAnnoAllVisible: bool
    BlockName: str
    MaterialMapper: Mapper
    MaterialId: ObjectId
    Material: str
    ReceiveShadows: bool
    CastShadows: bool
    Hyperlinks: HyperLinkCollection
    CloneMeForDragging: bool
    CompoundObjectTransform: Matrix3d
    GeometricExtents: Extents3d
    Ecs: Matrix3d
    IsPlanar: bool
    CollisionType: CollisionType
    LineWeight: LineWeight
    Visible: bool
    LinetypeScale: float
    LinetypeId: ObjectId
    Linetype: str
    LayerId: ObjectId
    Layer: str
    PlotStyleNameId: PlotStyleDescriptor
    PlotStyleName: str
    Transparency: Transparency
    EntityColor: EntityColor
    ColorIndex: int
    Color: Color
    BlockId: ObjectId
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    MergeStyle: DuplicateRecordCloning
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Xrecord(DBObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.Xrecord"""
    def __init__(self, *args) -> None: ...
    MergeStyle: DuplicateRecordCloning
    XlateReferences: bool
    Data: ResultBuffer
    PaperOrientation: PaperOrientationStates
    Annotative: AnnotativeStates
    HasFields: bool
    AcadObject: object
    ClassID: Guid
    ObjectBirthVersion: FullDwgVersion
    HasSaveVersionOverride: bool
    IsObjectIdsInFlux: bool
    UndoFiler: DwgFiler
    IsAProxy: bool
    IsTransactionResident: bool
    IsReallyClosing: bool
    IsCancelling: bool
    IsUndoing: bool
    IsNotifying: bool
    IsNewObject: bool
    IsModifiedGraphics: bool
    IsModifiedXData: bool
    IsModified: bool
    IsNotifyEnabled: bool
    IsWriteEnabled: bool
    IsReadEnabled: bool
    IsErased: bool
    IsEraseStatusToggled: bool
    XData: ResultBuffer
    ExtensionDictionary: ObjectId
    Drawable: Drawable
    Database: Database
    Handle: Handle
    OwnerId: ObjectId
    ObjectId: ObjectId
    Id: ObjectId
    IsPersistent: bool
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Append(self, data: ResultBuffer) -> None: ...
    def GetEnumerator(self, ) -> XrecordEnumerator: ...
    def IEnumerableGetEnumerator(self, ) -> IEnumerator: ...
    def IEnumerableTypedValueGetEnumerator(self, ) -> IEnumerator: ...

class XrecordEnumerator(RXObject):
    """.NET: Autodesk.AutoCAD.DatabaseServices.XrecordEnumerator"""
    def __init__(self, *args) -> None: ...
    Current: TypedValue
    IEnumeratorCurrent: object
    CurrentTypeCode: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def InsertAtCurrent(self, data: ResultBuffer) -> None: ...
    def MoveNext(self, ) -> bool: ...
    def RemoveCurrent(self, ) -> None: ...
    def Reset(self, ) -> None: ...

class XrefBeginOperationEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.XrefBeginOperationEventArgs"""
    def __init__(self, *args) -> None: ...
    FileName: str
    From: Database

class XrefBeginOperationEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.XrefBeginOperationEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: XrefBeginOperationEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: XrefBeginOperationEventArgs) -> None: ...

class XrefComandeeredEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.XrefComandeeredEventArgs"""
    def __init__(self, *args) -> None: ...
    From: Database
    Id: ObjectId

class XrefComandeeredEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.XrefComandeeredEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: XrefComandeeredEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: XrefComandeeredEventArgs) -> None: ...

class XrefGraph(Graph):
    """.NET: Autodesk.AutoCAD.DatabaseServices.XrefGraph"""
    def __init__(self, *args) -> None: ...
    HostDrawing: XrefGraphNode
    IsEmpty: bool
    NumNodes: int
    RootNode: GraphNode
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetXrefNode(self, idx: int) -> XrefGraphNode: ...
    def MarkUnresolvedTrees(self, ) -> bool: ...

class XrefGraphNode(GraphNode):
    """.NET: Autodesk.AutoCAD.DatabaseServices.XrefGraphNode"""
    def __init__(self, *args) -> None: ...
    XrefNotificationStatus: XrefNotificationStatus
    XrefStatus: XrefStatus
    IsNested: bool
    Database: Database
    BlockTableRecordId: ObjectId
    Name: str
    IsCycleNode: bool
    NumCycleIn: int
    NumCycleOut: int
    Owner: Graph
    NextCycleNode: GraphNode
    NumIn: int
    NumOut: int
    Data: IntPtr
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class XrefNotificationStatus:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.XrefNotificationStatus"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    ResolvedMatch: int  # = 1
    ResolvedElsewhere: int  # = 2
    ResolvedWithUpdate: int  # = 3
    ResolvedUpdateAvailable: int  # = 4
class XrefObjectId:
    """.NET: Autodesk.AutoCAD.DatabaseServices.XrefObjectId"""
    def __init__(self, *args) -> None: ...
    Handle: Handle
    ObjectId: ObjectId
    IsNull: bool
    IsXref: bool
    IsValid: bool
    @staticmethod
    def Deserialize(rbStart: ResultBuffer, rbEnd: ResultBuffer) -> XrefObjectId: ...
    def Equals(self, obj: object) -> bool: ...
    def ResolveObjectId(self, ) -> ObjectId: ...
    def Serialize(self, ) -> ResultBuffer: ...

class XrefOperation:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.XrefOperation"""
    def __init__(self, *args) -> None: ...
    XrefAttachOperation: int  # = 0
    XrefBindOperation: int  # = 1
    XrefXBindOperation: int  # = 1
    XrefDetachOperation: int  # = 2
    XrefOverlayOperation: int  # = 3
    XrefPathOperation: int  # = 4
    XrefReloadOperation: int  # = 5
    XrefResolveOperation: int  # = 6
    XrefUnloadOperation: int  # = 7
class XrefPreXrefLockFileEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.XrefPreXrefLockFileEventArgs"""
    def __init__(self, *args) -> None: ...
    btrId: ObjectId

class XrefPreXrefLockFileEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.XrefPreXrefLockFileEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: XrefPreXrefLockFileEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: XrefPreXrefLockFileEventArgs) -> None: ...

class XrefRedirectedEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.XrefRedirectedEventArgs"""
    def __init__(self, *args) -> None: ...
    OldId: ObjectId
    NewId: ObjectId

class XrefRedirectedEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.XrefRedirectedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: XrefRedirectedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: XrefRedirectedEventArgs) -> None: ...

class XrefStatus:
    """.NET enum: Autodesk.AutoCAD.DatabaseServices.XrefStatus"""
    def __init__(self, *args) -> None: ...
    NotAnXref: int  # = 0
    Resolved: int  # = 1
    Unloaded: int  # = 2
    Unreferenced: int  # = 3
    FileNotFound: int  # = 4
    Unresolved: int  # = 5
class XrefSubCommandAbortedEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.XrefSubCommandAbortedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: XrefSubCommandEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: XrefSubCommandEventArgs) -> None: ...

class XrefSubCommandEndEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.XrefSubCommandEndEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: XrefSubCommandEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: XrefSubCommandEventArgs) -> None: ...

class XrefSubCommandEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.XrefSubCommandEventArgs"""
    def __init__(self, *args) -> None: ...
    paths: list
    btrNames: list
    btrIds: ObjectIdCollection
    xrefOp: XrefOperation

class XrefSubCommandStartEventHandler:
    """.NET: Autodesk.AutoCAD.DatabaseServices.XrefSubCommandStartEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: XrefVetoableSubCommandEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: XrefVetoableSubCommandEventArgs) -> None: ...

class XrefVetoableSubCommandEventArgs(XrefSubCommandEventArgs):
    """.NET: Autodesk.AutoCAD.DatabaseServices.XrefVetoableSubCommandEventArgs"""
    def __init__(self, *args) -> None: ...
    abortOp: bool
    paths: list
    btrNames: list
    btrIds: ObjectIdCollection
    xrefOp: XrefOperation
