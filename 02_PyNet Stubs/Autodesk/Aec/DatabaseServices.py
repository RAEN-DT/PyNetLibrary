# Auto-generated — Civil 26 — Autodesk.Aec.DatabaseServices

class ADTDwgVersion:
    """.NET enum: Autodesk.Aec.DatabaseServices.ADTDwgVersion"""
    def __init__(self, *args) -> None: ...
    NoADTObjects: int  # = 0
    R1: int  # = 1
    R2: int  # = 2
    R3: int  # = 3
    R4: int  # = 4
    R5: int  # = 5
    R6: int  # = 6
    Current: int  # = 8
    Future: int  # = 32767
class AecXReferenceSubcommandActivities:
    """.NET enum: Autodesk.Aec.DatabaseServices.AecXReferenceSubcommandActivities"""
    def __init__(self, *args) -> None: ...
    Start: int  # = 0
    StartItem: int  # = 2
    EndItem: int  # = 3
    End: int  # = 4
    WillAbort: int  # = 5
    Aborted: int  # = 6
    StartXBindBlock: int  # = 7
    StartXBindSymbol: int  # = 8
class Anchor(DBObject):
    """.NET: Autodesk.Aec.DatabaseServices.Anchor"""
    def __init__(self, *args) -> None: ...
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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

class AnchorContext:
    """.NET enum: Autodesk.Aec.DatabaseServices.AnchorContext"""
    def __init__(self, *args) -> None: ...
    NewAttachment: int  # = 0
    AlreadyAttached: int  # = 1
class AnchorEntityToCurve(AnchorToReference):
    """.NET: Autodesk.Aec.DatabaseServices.AnchorEntityToCurve"""
    def __init__(self, *args) -> None: ...
    CurveNormal: Vector3d
    CurveWidth: float
    CurveThickness: float
    RotationAroundX: float
    Rotation: float
    CurveId: ObjectId
    FlipZ: bool
    FlipY: bool
    FlipX: bool
    AnchorZ: AnchorToCurveZ
    AnchorY: AnchorToCurveY
    AnchorX: AnchorToCurveX
    SingleReferenceId: ObjectId
    ReferenceObjectCount: int
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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
    def CalculateCurveNormal(self, curve: Curve) -> Vector3d: ...
    def CalculateCurveThickness(self, curve: Curve) -> float: ...
    def CalculateCurveWidth(self, curve: Curve) -> float: ...
    def GetEntityExtents(self, geo: Geo) -> BoundBlock3d: ...
    def ReverseParameters(self, ) -> None: ...
    def SwitchAnchoredEnd(self, geo: Geo) -> None: ...

class AnchorEntityToEntity(AnchorToReference):
    """.NET: Autodesk.Aec.DatabaseServices.AnchorEntityToEntity"""
    def __init__(self, *args) -> None: ...
    ReferencedEntityId: ObjectId
    SingleReferenceId: ObjectId
    ReferenceObjectCount: int
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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
    def SetReferencedEntity(self, geo: Geo) -> None: ...
    def SetReferencedEntityOldEcs(self, mat: Matrix3d) -> None: ...

class AnchorEntityToGridAssembly(AnchorToReference):
    """.NET: Autodesk.Aec.DatabaseServices.AnchorEntityToGridAssembly"""
    def __init__(self, *args) -> None: ...
    YAlignment: YAlignment
    YOffset: float
    AllowVariesFromInfillDefinition: bool
    RightOffset: float
    LeftOffset: float
    TopOffset: float
    BottomOffset: float
    HasSizingOffsets: bool
    GridAssemblyCellId: int
    GridAssemblyId: ObjectId
    SingleReferenceId: ObjectId
    ReferenceObjectCount: int
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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
    def GetOrientation(self, flipX: bool, flipY: bool, flipZ: bool) -> None: ...
    def SetOrientation(self, flipX: bool, flipY: bool, flipZ: bool) -> None: ...

class AnchorEntityToLayoutCell(AnchorEntityToLayoutNode):
    """.NET: Autodesk.Aec.DatabaseServices.AnchorEntityToLayoutCell"""
    def __init__(self, *args) -> None: ...
    ApplyResize: bool
    ResizeOffset: float
    OffsetToCenter: bool
    UseLocalCoordinateSystem: bool
    FlipZ: bool
    FlipY: bool
    FlipX: bool
    NormalVector: Vector3d
    OffsetVector: Vector3d
    ZRotation: float
    YRotation: float
    XRotation: float
    LayoutNodeIndex: int
    LayoutNodeId: int
    LayoutToolId: ObjectId
    SingleReferenceId: ObjectId
    ReferenceObjectCount: int
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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

class AnchorEntityToLayoutNode(AnchorToReference):
    """.NET: Autodesk.Aec.DatabaseServices.AnchorEntityToLayoutNode"""
    def __init__(self, *args) -> None: ...
    OffsetToCenter: bool
    UseLocalCoordinateSystem: bool
    FlipZ: bool
    FlipY: bool
    FlipX: bool
    NormalVector: Vector3d
    OffsetVector: Vector3d
    ZRotation: float
    YRotation: float
    XRotation: float
    LayoutNodeIndex: int
    LayoutNodeId: int
    LayoutToolId: ObjectId
    SingleReferenceId: ObjectId
    ReferenceObjectCount: int
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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

class AnchorEntityToLayoutVolume(AnchorEntityToLayoutCell):
    """.NET: Autodesk.Aec.DatabaseServices.AnchorEntityToLayoutVolume"""
    def __init__(self, *args) -> None: ...
    ApplyResize: bool
    ResizeOffset: float
    OffsetToCenter: bool
    UseLocalCoordinateSystem: bool
    FlipZ: bool
    FlipY: bool
    FlipX: bool
    NormalVector: Vector3d
    OffsetVector: Vector3d
    ZRotation: float
    YRotation: float
    XRotation: float
    LayoutNodeIndex: int
    LayoutNodeId: int
    LayoutToolId: ObjectId
    SingleReferenceId: ObjectId
    ReferenceObjectCount: int
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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

class AnchorLeaderToNode(AnchorEntityToLayoutNode):
    """.NET: Autodesk.Aec.DatabaseServices.AnchorLeaderToNode"""
    def __init__(self, *args) -> None: ...
    Vectors: AnchorLeaderToNodeVectorCollection
    Angle: float
    SecondExtension: float
    FirstExtension: float
    OffsetToCenter: bool
    UseLocalCoordinateSystem: bool
    FlipZ: bool
    FlipY: bool
    FlipX: bool
    NormalVector: Vector3d
    OffsetVector: Vector3d
    ZRotation: float
    YRotation: float
    XRotation: float
    LayoutNodeIndex: int
    LayoutNodeId: int
    LayoutToolId: ObjectId
    SingleReferenceId: ObjectId
    ReferenceObjectCount: int
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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

class AnchorLeaderToNodeVectorCollection:
    """.NET: Autodesk.Aec.DatabaseServices.AnchorLeaderToNodeVectorCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: Vector2d
    def Add(self, value: Vector2d) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: Vector2d) -> bool: ...
    def CopyTo(self, array: list, start: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: Vector2d) -> int: ...
    def Insert(self, index: int, value: Vector2d) -> None: ...
    def Remove(self, value: Vector2d) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class AnchorToCurveX(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.AnchorToCurveX"""
    def __init__(self, *args) -> None: ...
    OffsetDistance: float
    MeasureToType: CurveXMeasureToType
    OffsetType: CurveXOffsetType
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CalculatePosition(self, curve: Curve, entityLength: float, insertionOffset: float, position: Point3d, directionX: Vector3d, directionY: Vector3d, directionZ: Vector3d) -> None: ...
    def ReverseParameters(self, ) -> None: ...

class AnchorToCurveY(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.AnchorToCurveY"""
    def __init__(self, *args) -> None: ...
    MeasureToType: CurveYMeasureToType
    OffsetType: CurveYOffsetType
    OffsetDistance: float
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CalculateYOffset(self, curveThickness: float, entityThickness: float, insertionOffset: float) -> float: ...

class AnchorToCurveZ(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.AnchorToCurveZ"""
    def __init__(self, *args) -> None: ...
    OffsetFromType: CurveZOffsetFromType
    OffsetToType: CurveZOffsetToType
    OffsetDistance: float
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CalculateZOffset(self, curveHeight: float, entityHeight: float, insertionOffset: float) -> float: ...

class AnchorToReference(Anchor):
    """.NET: Autodesk.Aec.DatabaseServices.AnchorToReference"""
    def __init__(self, *args) -> None: ...
    SingleReferenceId: ObjectId
    ReferenceObjectCount: int
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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
    def AppendNestedReferenceObject(self, id: ObjectId, db: Database, relationType: RelationType) -> None: ...
    def AppendReferenceObject(self, id: ObjectId, relationType: RelationType) -> None: ...
    def GetNestedReferenceObjectAt(self, index: int, relationType: RelationType) -> ObjectId: ...
    def GetNestedSingleReference(self, relationType: RelationType) -> ObjectId: ...
    def GetReferenceObjectAt(self, index: int, relationType: RelationType) -> ObjectId: ...
    def GetSingleReference(self, relationType: RelationType) -> ObjectId: ...
    def IsReferenced(self, id: ObjectId, relationType: RelationType) -> bool: ...
    def IsReferencedNested(self, aecId: ObjectId, db: Database, relationType: RelationType) -> bool: ...
    def MirrorParameters(self, referenceWasMirrored: bool, geo: Geo, transform: Matrix3d) -> None: ...
    def RemoveAllReferenceObjects(self, ) -> None: ...
    def RemoveNestedReferenceObject(self, id: ObjectId, db: Database) -> None: ...
    def RemoveReferenceObject(self, id: ObjectId) -> None: ...
    def SetNestedSingleReference(self, aecId: ObjectId, db: Database, relationType: RelationType) -> None: ...
    def SetSingleReference(self, id: ObjectId, relationType: RelationType) -> None: ...

class AngularUnit:
    """.NET enum: Autodesk.Aec.DatabaseServices.AngularUnit"""
    def __init__(self, *args) -> None: ...
    Degrees: int  # = 0
    DegMinSec: int  # = 1
    Grads: int  # = 2
    Radians: int  # = 3
    Surveyor: int  # = 4
    CurrentAU: int  # = -1
class ApplyToFlags:
    """.NET enum: Autodesk.Aec.DatabaseServices.ApplyToFlags"""
    def __init__(self, *args) -> None: ...
    ApplyToInfill: int  # = 1
    ApplyToBoundaryEdges: int  # = 2
    ApplyToInteriorEdges: int  # = 4
class Attribute(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.Attribute"""
    def __init__(self, *args) -> None: ...
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Copy(self, ) -> Attribute: ...

class AttributeId(Attribute):
    """.NET: Autodesk.Aec.DatabaseServices.AttributeId"""
    def __init__(self, *args) -> None: ...
    Id: ObjectId
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class AutomaticSpaceBoundary:
    """.NET enum: Autodesk.Aec.DatabaseServices.AutomaticSpaceBoundary"""
    def __init__(self, *args) -> None: ...
    Yes: int  # = 0
    No: int  # = 1
    ByStyle: int  # = 2
    NotApplicableToThisObject: int  # = -1
class AxisReference:
    """.NET enum: Autodesk.Aec.DatabaseServices.AxisReference"""
    def __init__(self, *args) -> None: ...
    Start: int  # = 0
    Mid: int  # = 1
    End: int  # = 2
class BlockReference(Geo):
    """.NET: Autodesk.Aec.DatabaseServices.BlockReference"""
    def __init__(self, *args) -> None: ...
    Scale: Scale3d
    BlockDefId: ObjectId
    IsAnchored: bool
    AnchorId: ObjectId
    CanBeAnchored: bool
    GeoEcsIsDirty: bool
    GeoEcs: Matrix3d
    ZDir: Vector3d
    YDir: Vector3d
    XDir: Vector3d
    Normal: Vector3d
    Rotation: float
    Direction: Vector3d
    Location: Point3d
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    StyleId: ObjectId
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    Description: str
    TypeIcon: Icon
    DisplayName: str
    Overrides: OverrideCollection
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

class BoundaryFlags:
    """.NET enum: Autodesk.Aec.DatabaseServices.BoundaryFlags"""
    def __init__(self, *args) -> None: ...
    Top: int  # = 1
    Left: int  # = 2
    Bottom: int  # = 4
    Right: int  # = 8
class ByMaterialDisplayComponentType:
    """.NET enum: Autodesk.Aec.DatabaseServices.ByMaterialDisplayComponentType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Linework: int  # = 1
    Elevation2dSection: int  # = 2
    Body: int  # = 3
    PlanHatch: int  # = 4
    SurfaceHatch: int  # = 5
    SectionHatch: int  # = 6
    SectionBoundary: int  # = 7
    SectionedBody: int  # = 8
class CellLayoutTool(LayoutTool):
    """.NET: Autodesk.Aec.DatabaseServices.CellLayoutTool"""
    def __init__(self, *args) -> None: ...
    LayoutCellIds: IntegerCollection
    LayoutNodeIds: IntegerCollection
    IsAnchored: bool
    AnchorId: ObjectId
    CanBeAnchored: bool
    GeoEcsIsDirty: bool
    GeoEcs: Matrix3d
    ZDir: Vector3d
    YDir: Vector3d
    XDir: Vector3d
    Normal: Vector3d
    Rotation: float
    Direction: Vector3d
    Location: Point3d
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    StyleId: ObjectId
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    Description: str
    TypeIcon: Icon
    DisplayName: str
    Overrides: OverrideCollection
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
    def GetClosestLayoutCell(self, location: Point3d) -> int: ...
    def GetLayoutCellCentroid(self, cellId: int) -> Matrix3d: ...
    def GetLayoutCellProfile(self, cellId: int, toWcs: Matrix3d) -> Profile: ...

class Classification(DictionaryRecord):
    """.NET: Autodesk.Aec.DatabaseServices.Classification"""
    def __init__(self, *args) -> None: ...
    OwningSystemName: str
    NameAndDescription: str
    OwningSystemId: ObjectId
    Translator: DictionaryRecordNameTranslator
    Classifications: ClassificationCollection
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    KeynoteValue: str
    Keynote: str
    IsLocked: bool
    AlternateName: str
    LocalizedName: str
    Name: str
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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

class ClassificationCollection(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.ClassificationCollection"""
    def __init__(self, *args) -> None: ...
    AllowDuplicateDefinitions: bool
    Item: ObjectId
    Count: int
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, item: ObjectId) -> int: ...
    @staticmethod
    def AreDifferent(a: ClassificationCollection, b: ClassificationCollection) -> bool: ...
    def Clear(self, ) -> None: ...
    def Contains(self, item: ObjectId) -> bool: ...
    def CopyTo(self, array: list, start: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetIdForDefinition(self, idOwningSystemDefinition: ObjectId) -> ObjectId: ...
    def IndexOf(self, item: ObjectId) -> int: ...
    def Insert(self, index: int, item: ObjectId) -> None: ...
    def Remove(self, item: ObjectId) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class ClassificationDefinition(DictionaryRecord):
    """.NET: Autodesk.Aec.DatabaseServices.ClassificationDefinition"""
    def __init__(self, *args) -> None: ...
    ClassificationTree: ClassificationTree
    AppliesToAll: bool
    AppliesToFilter: StringCollection
    Translator: DictionaryRecordNameTranslator
    Classifications: ClassificationCollection
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    KeynoteValue: str
    Keynote: str
    IsLocked: bool
    AlternateName: str
    LocalizedName: str
    Name: str
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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
    def AppliesTo(self, className: str) -> bool: ...
    @staticmethod
    def FilterEntitySet(entityIds: ObjectIdCollection, classificationIds: ClassificationCollection, runToCompletion: bool) -> None: ...
    @staticmethod
    def GetClassification(dictionaryRecord: DictionaryRecord, classificationDefinitionId: ObjectId) -> ObjectId: ...
    @staticmethod
    def IsAClassifiedAsB(a: ClassificationCollection, b: ClassificationCollection, exclusive: bool) -> bool: ...
    @staticmethod
    def IsClassified(id: ObjectId, classificationIds: ClassificationCollection) -> bool: ...

class ClassificationTree(ImpTree):
    """.NET: Autodesk.Aec.DatabaseServices.ClassificationTree"""
    def __init__(self, *args) -> None: ...
    Id: ObjectId
    Children: ImpTreeCollection
    ParentTree: ImpTree
    IsRoot: bool
    Root: ImpTree
    AllowChildren: bool
    SubObjectsMightHaveReferences: bool
    AllowNullObjects: bool
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddBranch(self, idParent: ObjectId, branch: ClassificationTree) -> None: ...
    def AddNode(self, name: str) -> ObjectId: ...
    def AddNodeToParent(self, idParent: ObjectId, name: str) -> ObjectId: ...
    def Contains(self, idClassification: ObjectId) -> bool: ...
    def CopyBranch(self, from_: ObjectId, to: ObjectId) -> None: ...
    def DeleteBranch(self, idClassification: ObjectId) -> None: ...
    def GetBranch(self, name: str) -> ClassificationTree: ...
    def GetIdAt(self, index: int) -> ObjectId: ...
    def IsInDictionary(self, dbDictionary: DBDictionary) -> bool: ...
    def MoveBranch(self, from_: ObjectId, to: ObjectId) -> None: ...
    def RemoveBranch(self, idClassification: ObjectId) -> ClassificationTree: ...
    def RemoveFromDictionary(self, ) -> None: ...
    def Rename(self, idClassification: ObjectId, newName: str) -> None: ...
    def SetClass(self, rxClass: RXClass) -> None: ...
    def SynchDictionary(self, ) -> None: ...

class ClipVolume(LayoutTool):
    """.NET: Autodesk.Aec.DatabaseServices.ClipVolume"""
    def __init__(self, *args) -> None: ...
    Name: str
    Subdivisions: DoubleCollection
    IncludedEntities: ObjectIdCollection
    UseModelExtentsForHeight: bool
    LowerExtension: float
    Height: float
    LengthB: float
    LengthA: float
    AngleB: float
    AngleA: float
    ViewSetId: ObjectId
    EcsVertices: Point2dCollection
    Vertices: Point3dCollection
    LayoutNodeIds: IntegerCollection
    IsAnchored: bool
    AnchorId: ObjectId
    CanBeAnchored: bool
    GeoEcsIsDirty: bool
    GeoEcs: Matrix3d
    ZDir: Vector3d
    YDir: Vector3d
    XDir: Vector3d
    Normal: Vector3d
    Rotation: float
    Direction: Vector3d
    Location: Point3d
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    StyleId: ObjectId
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    Description: str
    TypeIcon: Icon
    DisplayName: str
    Overrides: OverrideCollection
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
    def GetBody(self, id: ObjectId) -> Body: ...
    def Reverse(self, ) -> None: ...
    def SetVertices(self, points: Point3dCollection, sectionPlane: Plane) -> None: ...

class ClipVolumeResult(Geo):
    """.NET: Autodesk.Aec.DatabaseServices.ClipVolumeResult"""
    def __init__(self, *args) -> None: ...
    ClipVolumeId: ObjectId
    IsAnchored: bool
    AnchorId: ObjectId
    CanBeAnchored: bool
    GeoEcsIsDirty: bool
    GeoEcs: Matrix3d
    ZDir: Vector3d
    YDir: Vector3d
    XDir: Vector3d
    Normal: Vector3d
    Rotation: float
    Direction: Vector3d
    Location: Point3d
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    StyleId: ObjectId
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    Description: str
    TypeIcon: Icon
    DisplayName: str
    Overrides: OverrideCollection
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

class ClippingRectangleInfo:
    """.NET: Autodesk.Aec.DatabaseServices.ClippingRectangleInfo"""
    def __init__(self, *args) -> None: ...
    ...

class CommandStatus:
    """.NET enum: Autodesk.Aec.DatabaseServices.CommandStatus"""
    def __init__(self, *args) -> None: ...
    CommandAllowedAlways: int  # = 0
    CommandNotAllowed: int  # = 1
    CommandAllowedOnlyOnPickFirstSet: int  # = 2
class ComponentType:
    """.NET enum: Autodesk.Aec.DatabaseServices.ComponentType"""
    def __init__(self, *args) -> None: ...
    DefiningLine: int  # = 0
    Hidden: int  # = 1
    Erased: int  # = 2
    SubDivision1: int  # = 3
    SubDivision2: int  # = 4
    SubDivision3: int  # = 5
    SubDivision4: int  # = 6
    SubDivision5: int  # = 7
    SubDivision6: int  # = 8
    SubDivision7: int  # = 9
    SubDivision8: int  # = 10
    SubDivision9: int  # = 11
    SubDivision10: int  # = 12
    OuterShrinkwrap: int  # = 13
    InnerShrinkwrap: int  # = 14
    UserDefined: int  # = 15
class ConnectionComponent(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.ConnectionComponent"""
    def __init__(self, *args) -> None: ...
    BoundBox: BoundBox3d
    MaxSimultaneousConnections: int
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def ConnectsWith(self, component: ConnectionComponent) -> bool: ...

class ConstraintUtility:
    """.NET: Autodesk.Aec.DatabaseServices.ConstraintUtility"""
    def __init__(self, *args) -> None: ...
    DraggingState: AssocDraggingState
    IsDragging: bool
    HideInternalConstraint: bool
    IsConstraintEvaluationRelaxed: bool
    IsActionEvaluationInProgress: bool
    @staticmethod
    def AddConstraintGeometry(subentityPath: FullSubentityPath) -> ConstrainedGeometry: ...
    @staticmethod
    def AddDistanceConstraint(entity: Entity, subEntityId1: SubentityId, subEntityId2: SubentityId, valueDependencyId: ObjectId) -> None: ...
    @staticmethod
    def AddFixConstraintOnSubent(path: FullSubentityPath, newlyAddedConstraintGeometry: list) -> list: ...
    @staticmethod
    def AddGeomConstraintToSubents(entity: Entity, subEntityId1: SubentityId, subEntityId2: SubentityId, constraintType: ConstraintType, setToImplied: bool) -> None: ...
    @staticmethod
    def AddInternalConstraint(entity: Entity, subEntityId: SubentityId) -> None: ...
    @staticmethod
    def AutoCoincidentConstraint(fullSubentityPaths: list, newlyAddedGeometries: list) -> list: ...
    @staticmethod
    def CreateAllEdgeVerticesSubentIds(entity: Entity) -> list: ...
    @staticmethod
    def CreateEdgeVertexSubentId(edgeSubentityId: SubentityId, vertexType: EdgeVertexType) -> SubentityId: ...
    @staticmethod
    def DeleteConstraint(constraint: GeometricalConstraint) -> None: ...
    @staticmethod
    def DeleteGeometryDependencyOnSubentity(entity: Entity, subEntityId: SubentityId) -> None: ...
    @staticmethod
    def DeleteGeometryNodeInConstraintGroup(constrainedGeometry: ConstrainedGeometry) -> None: ...
    @staticmethod
    def Get2dConstraintsOnConstrainedGeometry(constraintGeometry: ConstrainedGeometry, constraints: list, includeExplicitConstraints: bool) -> bool: ...
    @staticmethod
    def Get2dConstraintsOnImplicitPoint(implicitPoint: ConstrainedImplicitPoint, constraints: list, includeExplicitConstraints: bool) -> bool: ...
    @staticmethod
    def Get2dConstraintsOnImplicitPoints(points: list, constraints: list, includeExplicitConstraints: bool) -> bool: ...
    @staticmethod
    def Get2dConstraintsOnObject(entityId: ObjectId, constraints: list, includeExplicitConstraints: bool) -> bool: ...
    @staticmethod
    def Get2dConstraintsOnSubent(subentityPath: FullSubentityPath, constraints: list, includeExplicitConstraints: bool) -> bool: ...
    @staticmethod
    def GetAcDbAssocValueDependencyIds(entity: Entity) -> ObjectIdCollection: ...
    @staticmethod
    def GetAllConstraintedGeometryOnEntity(entity: Entity, geometries: list) -> bool: ...
    @staticmethod
    def GetAllImplicitPointsOnObject(entity: Entity, implicitPoints: list) -> bool: ...
    @staticmethod
    def GetAllStartEndImplicitPointsOnObject(entity: Entity, implicitPoints: list) -> bool: ...
    @staticmethod
    def GetAllSubEntitiesInEntity(entityId: ObjectId) -> list: ...
    @staticmethod
    def GetAssocPersSubentityIdPE(object: RXObject) -> AssocPersSubentityIdPE: ...
    @staticmethod
    def GetClosestEdgeSubentity(entity: Entity, fullPathObjectIds: ObjectIdCollection, inputPoint: Point3d, subentityType: SubentityType) -> SubentityId: ...
    @staticmethod
    def GetClosetVertexSubentityId(entity: Entity, objectIds: ObjectIdCollection, pickPoint: Point3d, edgeSubentityId: SubentityId, closestVertexSubentityId: SubentityId) -> bool: ...
    @staticmethod
    def GetConstraintedGeometryOnSubent(subentityPath: FullSubentityPath) -> ConstrainedGeometry: ...
    @staticmethod
    def GetCurrentSpaceNetwork(createIfNotExist: bool) -> ObjectId: ...
    @staticmethod
    def GetEdgeBasedFullSubentityPath(path: FullSubentityPath) -> FullSubentityPath: ...
    @staticmethod
    def GetEdgeBasedSubentity(subEntityId: SubentityId) -> SubentityId: ...
    @staticmethod
    def GetEdgeSubentIdFromEdgeVertexSubentId(vertexSubentity: SubentityId) -> SubentityId: ...
    @staticmethod
    def GetEdgeVertexSubentType(vertexSubentityId: SubentityId) -> EdgeVertexType: ...
    @staticmethod
    def GetEdgeVertexSubentities(entity: Entity, edgeSubentityId: SubentityId, startVertexSubentityId: SubentityId, endVertexSubentityId: SubentityId, middleSubentityId: SubentityId, centerSubentityId: SubentityId) -> None: ...
    @staticmethod
    def GetGeometryDependencyIdsOnEntity(entity: Entity) -> ObjectIdCollection: ...
    @staticmethod
    def GetSpaceModelConstraintGroup(database: Database, createIfDoesNotExist: bool, plane: Plane) -> ObjectId: ...
    @staticmethod
    def GetSubentGeomDependency(entity: Entity, subEntityId: SubentityId) -> ObjectId: ...
    @staticmethod
    def GetSubentGeometryXform(objectIds: ObjectIdCollection) -> Matrix3d: ...
    @staticmethod
    def GetValueDependencyByName(entity: Entity, valueName: str) -> ObjectId: ...
    @staticmethod
    def GetVertexSubentityFullPathOfImplicitPoint(implicitPoint: ConstrainedImplicitPoint) -> FullSubentityPath: ...
    @staticmethod
    def IsAecDbEntityConstrBarVisible(geometricalConstraint: GeometricalConstraint) -> bool: ...
    @staticmethod
    def IsEntityHasEdgeSubent(entityId: ObjectId) -> bool: ...
    @staticmethod
    def IsSubentityFixed(path: FullSubentityPath) -> bool: ...
    @staticmethod
    def IsValidSubentity(entity: Entity, subEntityId: SubentityId) -> bool: ...
    @staticmethod
    def ObjectHasConstraint(entityId: ObjectId) -> bool: ...
    @staticmethod
    def ObjectHasFixConstraint(entityId: ObjectId) -> bool: ...
    @staticmethod
    def ObjectHasGeomDependency(id: ObjectId) -> bool: ...
    @staticmethod
    def OnAcDbAssocGeometryDependencyAppended(dependencyObjectId: ObjectId) -> None: ...
    @staticmethod
    def ProjectToXYPlanCurve(curve3d: Curve3d) -> Curve3d: ...
    @staticmethod
    def RecordForDelayRegen(id: ObjectId) -> None: ...
    @staticmethod
    def RecordForDelayRegen2ndRound(id: ObjectId) -> None: ...
    @staticmethod
    def RelaxConstraintEvaluation() -> None: ...
    @staticmethod
    def RemoveEntityRedundantInternalConstraints(entity: Entity) -> None: ...
    @staticmethod
    def RemoveGeometryConstraintsOnObjects(object: DBObject) -> None: ...
    @staticmethod
    def RestoreConstraintEvaluation() -> None: ...
    @staticmethod
    def SetDelayUpdateSpaceEnabledForCurDwg(value: bool) -> None: ...
    @staticmethod
    def SubentHasGeomDependency(entity: Entity, subEntityId: SubentityId) -> bool: ...
    @staticmethod
    def SubentityHasConstraint(entity: Entity, subEntityId: SubentityId) -> bool: ...

class CurveXMeasureToType:
    """.NET enum: Autodesk.Aec.DatabaseServices.CurveXMeasureToType"""
    def __init__(self, *args) -> None: ...
    ToCenter: int  # = 0
    ToStartEdge: int  # = 1
    ToEndEdge: int  # = 2
class CurveXOffsetType:
    """.NET enum: Autodesk.Aec.DatabaseServices.CurveXOffsetType"""
    def __init__(self, *args) -> None: ...
    FromStartOfCurve: int  # = 0
    FromEndOfCurve: int  # = 1
    FromMidpointOfCurve: int  # = 2
class CurveYMeasureToType:
    """.NET enum: Autodesk.Aec.DatabaseServices.CurveYMeasureToType"""
    def __init__(self, *args) -> None: ...
    ToCenter: int  # = 0
    ToFrontEdge: int  # = 1
    ToBackEdge: int  # = 2
class CurveYOffsetType:
    """.NET enum: Autodesk.Aec.DatabaseServices.CurveYOffsetType"""
    def __init__(self, *args) -> None: ...
    FromCenterCurve: int  # = 0
    FromLeftEdge: int  # = 1
    FromRightEdge: int  # = 2
class CurveZOffsetFromType:
    """.NET enum: Autodesk.Aec.DatabaseServices.CurveZOffsetFromType"""
    def __init__(self, *args) -> None: ...
    FromBottom: int  # = 0
    FromTop: int  # = 1
    FromCenter: int  # = 2
class CurveZOffsetToType:
    """.NET enum: Autodesk.Aec.DatabaseServices.CurveZOffsetToType"""
    def __init__(self, *args) -> None: ...
    ToTop: int  # = 0
    ToCenter: int  # = 1
    ToBottom: int  # = 2
class DBObject(DBObject):
    """.NET: Autodesk.Aec.DatabaseServices.DBObject"""
    def __init__(self, *args) -> None: ...
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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
    def GetMaterialComponents(self, componentIds: IntegerCollection, componentNames: StringCollection, materialIds: ObjectIdCollection) -> None: ...
    def SetMaterialComponents(self, componentIds: IntegerCollection, materialIds: ObjectIdCollection) -> None: ...
    def SetToStandard(self, db: Database) -> None: ...
    def SubSetDatabaseDefaults(self, db: Database) -> None: ...

class DBObjectRelationship:
    """.NET: Autodesk.Aec.DatabaseServices.DBObjectRelationship"""
    def __init__(self, *args) -> None: ...
    ...

class DBObjectRelationshipCollection(List):
    """.NET: Autodesk.Aec.DatabaseServices.DBObjectRelationshipCollection"""
    def __init__(self, *args) -> None: ...
    Capacity: int
    Count: int
    Item: DBObjectRelationship

class DBObjectRelationshipManager:
    """.NET: Autodesk.Aec.DatabaseServices.DBObjectRelationshipManager"""
    def __init__(self, *args) -> None: ...
    Database: Database
    IsNotificationSuppressed: bool
    ObjectsWithEnhancedReferencesIncludingErased: ObjectIdCollection
    ObjectsWithEnhancedReferences: ObjectIdCollection
    def ForceUpdate(self, ids: ObjectIdCollection) -> None: ...
    def GetAllReferences(self, object: DBObject) -> DBObjectRelationshipCollection: ...
    def GetAllReferencesIncludingErased(self, object: DBObject) -> DBObjectRelationshipCollection: ...
    def GetClassReferencesToThisObject(self, object: DBObject) -> DBObjectRelationshipCollection: ...
    def GetClassReferencesToThisObjectIncludErased(self, object: DBObject) -> DBObjectRelationshipCollection: ...
    def GetObjectsOfType(self, type: RXClass, verifyObject: bool) -> ObjectIdCollection: ...
    def GetObjectsOfTypeIncludingErased(self, type: RXClass, verifyObject: bool) -> ObjectIdCollection: ...
    def GetReferencesFromThisObject(self, object: DBObject) -> DBObjectRelationshipCollection: ...
    def GetReferencesFromThisObjectIncludeErased(self, object: DBObject) -> DBObjectRelationshipCollection: ...
    def GetReferencesToThisObject(self, object: DBObject) -> DBObjectRelationshipCollection: ...
    def GetReferencesToThisObjectIncludeErased(self, object: DBObject) -> DBObjectRelationshipCollection: ...
    def GetReferencesToThisObjectRecursive(self, object: DBObject, relationshipTypeFilter: int, includeFilter: bool) -> DBObjectRelationshipCollection: ...
    def GetReferencesToThisObjectRecursiveIncludeErased(self, object: DBObject, relationshipTypeFilter: int, includeFilter: bool) -> DBObjectRelationshipCollection: ...
    def ObjectContainsEnhancedReferences(self, id: ObjectId) -> bool: ...
    def SupressNotificationOff(self, ) -> None: ...
    def SupressNotificationOn(self, ) -> None: ...

class DatabaseData(RXObject):
    """.NET: Autodesk.Aec.DatabaseServices.DatabaseData"""
    def __init__(self, *args) -> None: ...
    DrawingInitializedAndPromoted: bool
    Database: Database
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class DatabaseDataAecBase(DatabaseData):
    """.NET: Autodesk.Aec.DatabaseServices.DatabaseDataAecBase"""
    def __init__(self, *args) -> None: ...
    ProgressiveUpdateCondition: int
    DelaySpaceUpdateEnabled: bool
    DisableObjectUpdateDuringModify: bool
    ReferenceCloseCommandActive: bool
    ReferenceEditCommandActive: bool
    UnhidingObjectsIsActive: bool
    HidingObjectsIsActive: bool
    IsGsMarkerComponentSelectionActive: bool
    IsGsMarkerUnhighlightingEnabled: bool
    IsGsMarkerHighlightingEnabled: bool
    PreKyotoSectionElevationLinesRequiringUpdate: ObjectIdCollection
    InsertedBlockName: str
    RestoreInsUnitsOnBTRAfterInsert: bool
    XreferenceIds: ObjectIdCollection
    XrefSubcommandType: XReferenceSubCommandType
    LastXrefSubcommandActivity: AecXReferenceSubcommandActivities
    InplaceEditorMap: InplaceEditorMap
    StyleManagerCloningActive: bool
    PostProcessDictionaryMergeInfo: DBObjectCollection
    InitDwgCalled: bool
    DwgInFieldsTriggered: bool
    DxfInFieldsTriggered: bool
    PartialOpenVetoed: bool
    DetectedMunichStairDisplayProperties: int
    RecoverActive: bool
    DidDictionaryAuditPass2: bool
    DidDictionaryAuditPass1: bool
    DwgReadIsActive: bool
    DwgSaveIsActive: bool
    CloningMixedVersionOfObjects: bool
    CloneToSameDatabaseActive: bool
    LayoutCopyIsActive: bool
    InsertIsActive: bool
    FastWblockIsActive: bool
    WblockIsActive: bool
    DxfOutIsActive: bool
    DxfInIsActive: bool
    DeepCloneIsActive: bool
    LayoutCopyHandPurgeDictionaryIds: ObjectIdCollection
    ReferenceEditPostUpdateEcsSet: ObjectIdCollection
    LongTransactionSet: ObjectIdCollection
    DeepClonedSet: ObjectIdCollection
    CachedLayerZeroId: ObjectId
    CachedVariableId: ObjectId
    DisplayRepresentationManager: DisplayRepresentationManager
    ObjectRelationGraph: DBObjectRelationshipManager
    DrawingInitializedAndPromoted: bool
    Database: Database
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddNestedWblockCloneDictionary(self, mainLevelDictionary: str, destinationDictionary: DBDictionary) -> None: ...
    def AddToEndDeepCloneMvBlockProcessingArray(self, idMvBlockReference: ObjectId) -> None: ...
    def AddToEndDeepCloneUpdateViewBlockArray(self, idMvBlockReference: ObjectId) -> None: ...
    def AppendCopiedObject(self, sourceId: ObjectId, destinationId: ObjectId) -> None: ...
    def AppendPreKyotoSectionElevationLinesRequiringUpdate(self, id: ObjectId) -> None: ...
    def DoDictionaryAuditHack(self, info: AuditInfo) -> None: ...
    def GetNestedWblockCloneDictionary(self, mainLevelDictionary: str) -> DBDictionary: ...
    def LayoutCopyDoPostPurge(self, ) -> None: ...
    def NotifySpatialTreeMessageObject(self, ) -> None: ...
    def PopAnnotationScaleFromStream(self, ) -> None: ...
    def RemoveAllKyotoSectionElevationLinesRequiringUpdate(self, ) -> None: ...
    def RemoveFromKyotoSectionElevationLinesRequiringUpdate(self, id: ObjectId) -> None: ...
    def RemoveNestedWblockCloneDictionary(self, mainLevelDictionary: str) -> None: ...
    def ResetAuditFlags(self, ) -> None: ...
    def ResetEndDeepCloneMvBlockProcessingArray(self, ) -> None: ...
    def ResetEndDeepCloneUpdateViewBlockArray(self, ) -> None: ...
    def ResetPostProcessDictionaryMergeInfo(self, ) -> None: ...
    def SetGsMarkerComponentSelectionActive(self, componentSelectionActive: bool) -> None: ...
    def SetGsMarkerHighlightingEnabled(self, enableHighlighting: bool) -> None: ...
    def SetGsMarkerUnhighlightingEnabled(self, enableUnhighlighting: bool) -> None: ...

class Dictionary(RXObject):
    """.NET: Autodesk.Aec.DatabaseServices.Dictionary"""
    def __init__(self, *args) -> None: ...
    InternalName: str
    Database: Database
    ObjectType: RXClass
    RecordType: RXClass
    DictionaryId: ObjectId
    DisplayName: str
    NamesInUse: StringCollection
    Records: ObjectIdCollection
    HasStandardEntries: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddNewRecord(self, name: str, newRecord: DictionaryRecord) -> None: ...
    def CloneEntry(self, copyFromRecord: DictionaryRecord, newName: str) -> ObjectId: ...
    def ExtraPurgeCheck(self, idsToPurge: ObjectIdCollection) -> None: ...
    def GetAlternateAt(self, name: str) -> ObjectId: ...
    def GetAt(self, name: str) -> ObjectId: ...
    def Has(self, name: str, trans: Transaction) -> bool: ...
    def NameAlternateAt(self, id: ObjectId) -> str: ...
    def NameAt(self, id: ObjectId) -> str: ...
    def NewEntry(self, ) -> DictionaryRecord: ...
    def Rename(self, oldName: str, newName: str, trans: Transaction) -> None: ...

class DictionaryClassificationDefinition(Dictionary):
    """.NET: Autodesk.Aec.DatabaseServices.DictionaryClassificationDefinition"""
    def __init__(self, *args) -> None: ...
    InternalName: str
    Database: Database
    ObjectType: RXClass
    RecordType: RXClass
    DictionaryId: ObjectId
    DisplayName: str
    NamesInUse: StringCollection
    Records: ObjectIdCollection
    HasStandardEntries: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class DictionaryDisplayConfiguration(Dictionary):
    """.NET: Autodesk.Aec.DatabaseServices.DictionaryDisplayConfiguration"""
    def __init__(self, *args) -> None: ...
    InternalName: str
    Database: Database
    ObjectType: RXClass
    RecordType: RXClass
    DictionaryId: ObjectId
    DisplayName: str
    NamesInUse: StringCollection
    Records: ObjectIdCollection
    HasStandardEntries: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetStandardDisplayConfiguration(db: Database) -> ObjectId: ...

class DictionaryDisplaySet(Dictionary):
    """.NET: Autodesk.Aec.DatabaseServices.DictionaryDisplaySet"""
    def __init__(self, *args) -> None: ...
    StandardModelHighDetailName: str
    StandardModelLowDetailName: str
    StandardPlanHighDetailName: str
    StandardPlanLowDetailName: str
    StandardSectionElevName: str
    StandardReflectedName: str
    StandardModelName: str
    StandardPlanName: str
    DictionaryName: str
    InternalName: str
    Database: Database
    ObjectType: RXClass
    RecordType: RXClass
    DictionaryId: ObjectId
    DisplayName: str
    NamesInUse: StringCollection
    Records: ObjectIdCollection
    HasStandardEntries: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def CheckForMatchingEntries(db: Database, displaySetType: StandardDisplaySetType) -> None: ...
    @staticmethod
    def Exists(db: Database) -> bool: ...
    @staticmethod
    def GetStandardDisplaySetName(untranslatedName: str, db: Database) -> str: ...
    @staticmethod
    def GetStandardModelHighDetailId(db: Database) -> ObjectId: ...
    @staticmethod
    def GetStandardModelHighDetailName(db: Database) -> str: ...
    @staticmethod
    def GetStandardModelId(db: Database) -> ObjectId: ...
    @staticmethod
    def GetStandardModelLowDetailId(db: Database) -> ObjectId: ...
    @staticmethod
    def GetStandardModelLowDetailName(db: Database) -> str: ...
    @staticmethod
    def GetStandardModelName(db: Database) -> str: ...
    @staticmethod
    def GetStandardPlanHighDetailId(db: Database) -> ObjectId: ...
    @staticmethod
    def GetStandardPlanHighDetailName(db: Database) -> str: ...
    @staticmethod
    def GetStandardPlanId(db: Database) -> ObjectId: ...
    @staticmethod
    def GetStandardPlanLowDetailId(db: Database) -> ObjectId: ...
    @staticmethod
    def GetStandardPlanLowDetailName(db: Database) -> str: ...
    @staticmethod
    def GetStandardPlanName(db: Database) -> str: ...
    @staticmethod
    def GetStandardReflectedId(db: Database) -> ObjectId: ...
    @staticmethod
    def GetStandardReflectedName(db: Database) -> str: ...
    @staticmethod
    def GetStandardSectionElevId(db: Database) -> ObjectId: ...
    @staticmethod
    def GetStandardSectionElevName(db: Database) -> str: ...
    @staticmethod
    def GetStandardSet(name: str, db: Database) -> ObjectId: ...
    @staticmethod
    def ScanAndRemoveDuplicateStandardSets(db: Database) -> bool: ...

class DictionaryDisplayThemeStyle(Dictionary):
    """.NET: Autodesk.Aec.DatabaseServices.DictionaryDisplayThemeStyle"""
    def __init__(self, *args) -> None: ...
    InternalName: str
    Database: Database
    ObjectType: RXClass
    RecordType: RXClass
    DictionaryId: ObjectId
    DisplayName: str
    NamesInUse: StringCollection
    Records: ObjectIdCollection
    HasStandardEntries: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetStandardStyle(db: Database) -> ObjectId: ...

class DictionaryEntryInformation:
    """.NET: Autodesk.Aec.DatabaseServices.DictionaryEntryInformation"""
    def __init__(self, *args) -> None: ...
    DictionaryEntryClass: RXClass
    Dictionary: Dictionary

class DictionaryLayerKeyStyle(Dictionary):
    """.NET: Autodesk.Aec.DatabaseServices.DictionaryLayerKeyStyle"""
    def __init__(self, *args) -> None: ...
    InternalName: str
    Database: Database
    ObjectType: RXClass
    RecordType: RXClass
    DictionaryId: ObjectId
    DisplayName: str
    NamesInUse: StringCollection
    Records: ObjectIdCollection
    HasStandardEntries: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GenerateLayer(self, layerKey: str) -> ObjectId: ...
    @staticmethod
    def GetStandardStyle(db: Database) -> ObjectId: ...

class DictionaryListDefinition(Dictionary):
    """.NET: Autodesk.Aec.DatabaseServices.DictionaryListDefinition"""
    def __init__(self, *args) -> None: ...
    InternalName: str
    Database: Database
    ObjectType: RXClass
    RecordType: RXClass
    DictionaryId: ObjectId
    DisplayName: str
    NamesInUse: StringCollection
    Records: ObjectIdCollection
    HasStandardEntries: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetStandardDefinition(database: Database) -> ObjectId: ...

class DictionaryMaskBlockDefinition(Dictionary):
    """.NET: Autodesk.Aec.DatabaseServices.DictionaryMaskBlockDefinition"""
    def __init__(self, *args) -> None: ...
    InternalName: str
    Database: Database
    ObjectType: RXClass
    RecordType: RXClass
    DictionaryId: ObjectId
    DisplayName: str
    NamesInUse: StringCollection
    Records: ObjectIdCollection
    HasStandardEntries: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetStandardDefinition(db: Database) -> ObjectId: ...

class DictionaryMassElementStyle(Dictionary):
    """.NET: Autodesk.Aec.DatabaseServices.DictionaryMassElementStyle"""
    def __init__(self, *args) -> None: ...
    InternalName: str
    Database: Database
    ObjectType: RXClass
    RecordType: RXClass
    DictionaryId: ObjectId
    DisplayName: str
    NamesInUse: StringCollection
    Records: ObjectIdCollection
    HasStandardEntries: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetStandardStyle(db: Database) -> ObjectId: ...

class DictionaryMaterialDefinition(Dictionary):
    """.NET: Autodesk.Aec.DatabaseServices.DictionaryMaterialDefinition"""
    def __init__(self, *args) -> None: ...
    InternalName: str
    Database: Database
    ObjectType: RXClass
    RecordType: RXClass
    DictionaryId: ObjectId
    DisplayName: str
    NamesInUse: StringCollection
    Records: ObjectIdCollection
    HasStandardEntries: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetStandardDefinition(db: Database) -> ObjectId: ...

class DictionaryMultiViewBlockDefinition(Dictionary):
    """.NET: Autodesk.Aec.DatabaseServices.DictionaryMultiViewBlockDefinition"""
    def __init__(self, *args) -> None: ...
    InternalName: str
    Database: Database
    ObjectType: RXClass
    RecordType: RXClass
    DictionaryId: ObjectId
    DisplayName: str
    NamesInUse: StringCollection
    Records: ObjectIdCollection
    HasStandardEntries: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetStandardDefinition(db: Database) -> ObjectId: ...

class DictionaryPolygonStyle(Dictionary):
    """.NET: Autodesk.Aec.DatabaseServices.DictionaryPolygonStyle"""
    def __init__(self, *args) -> None: ...
    InternalName: str
    Database: Database
    ObjectType: RXClass
    RecordType: RXClass
    DictionaryId: ObjectId
    DisplayName: str
    NamesInUse: StringCollection
    Records: ObjectIdCollection
    HasStandardEntries: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetStandardStyle(db: Database) -> ObjectId: ...

class DictionaryProfileDefinition(Dictionary):
    """.NET: Autodesk.Aec.DatabaseServices.DictionaryProfileDefinition"""
    def __init__(self, *args) -> None: ...
    InternalName: str
    Database: Database
    ObjectType: RXClass
    RecordType: RXClass
    DictionaryId: ObjectId
    DisplayName: str
    NamesInUse: StringCollection
    Records: ObjectIdCollection
    HasStandardEntries: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetStandardDefinition(db: Database) -> ObjectId: ...

class DictionaryRecord(DBObject):
    """.NET: Autodesk.Aec.DatabaseServices.DictionaryRecord"""
    def __init__(self, *args) -> None: ...
    Translator: DictionaryRecordNameTranslator
    Classifications: ClassificationCollection
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    KeynoteValue: str
    Keynote: str
    IsLocked: bool
    AlternateName: str
    LocalizedName: str
    Name: str
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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

class DictionaryRecordAlternateNameTranslator(DictionaryRecordNameTranslator):
    """.NET: Autodesk.Aec.DatabaseServices.DictionaryRecordAlternateNameTranslator"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(unmanagedPointer: IntPtr, autoDelete: bool) -> DictionaryRecordAlternateNameTranslator: ...

class DictionaryRecordNameTranslator(NameTranslator):
    """.NET: Autodesk.Aec.DatabaseServices.DictionaryRecordNameTranslator"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(unmanagedPointer: IntPtr, autoDelete: bool) -> DictionaryRecordNameTranslator: ...

class DictionarySection2dStyle(Dictionary):
    """.NET: Autodesk.Aec.DatabaseServices.DictionarySection2dStyle"""
    def __init__(self, *args) -> None: ...
    InternalName: str
    Database: Database
    ObjectType: RXClass
    RecordType: RXClass
    DictionaryId: ObjectId
    DisplayName: str
    NamesInUse: StringCollection
    Records: ObjectIdCollection
    HasStandardEntries: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetStandardStyle(database: Database) -> ObjectId: ...

class DisplayComponent(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.DisplayComponent"""
    def __init__(self, *args) -> None: ...
    IsInherited: bool
    IsApplicable: bool
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Reset(self, ) -> None: ...

class DisplayComponentEntity(DisplayComponent):
    """.NET: Autodesk.Aec.DatabaseServices.DisplayComponentEntity"""
    def __init__(self, *args) -> None: ...
    ByMaterial: bool
    AllowByMaterial: bool
    LinetypeScale: float
    LineWeight: LineWeight
    LinetypeId: ObjectId
    ColorIndex: int
    Color: Color
    LayerId: ObjectId
    IsVisible: bool
    IsInherited: bool
    IsApplicable: bool
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetPlotStyleNameId(self, ) -> ObjectId: ...
    def GetPlotStyleNameType(self, ) -> PlotStyleNameType: ...
    def ResetEnt(self, ) -> None: ...
    def SetPlotStyleName(self, type: PlotStyleNameType, id: ObjectId) -> None: ...

class DisplayComponentHatch(DisplayComponentEntity):
    """.NET: Autodesk.Aec.DatabaseServices.DisplayComponentHatch"""
    def __init__(self, *args) -> None: ...
    IsDoubleHatch: bool
    VOffset: float
    UOffset: float
    Spacing: float
    UseAngleOfObject: bool
    Angle: float
    Scale: float
    PatternName: str
    HatchType: HatchType
    ByMaterial: bool
    AllowByMaterial: bool
    LinetypeScale: float
    LineWeight: LineWeight
    LinetypeId: ObjectId
    ColorIndex: int
    Color: Color
    LayerId: ObjectId
    IsVisible: bool
    IsInherited: bool
    IsApplicable: bool
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def ResetHatch(self, ) -> None: ...
    def SetHatchParams(self, hatch: Hatch, angleOfObject: float, ucsXAngleOffset: float) -> None: ...
    @staticmethod
    def SetHatchParamsToAcadSettings(hatch: Hatch) -> None: ...

class DisplayComponentPushPopData(DisposableWrapper):
    """.NET: Autodesk.Aec.DatabaseServices.DisplayComponentPushPopData"""
    def __init__(self, *args) -> None: ...
    MaterialInformation: DisplayMaterialInformation
    DisplayComponentEntity: DisplayComponentEntity
    HasName: bool
    DisplayComponentName: str
    HasMaterial: bool
    MaterialId: ObjectId
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetDisplayComponentData(self, entity: DisplayComponentEntity, name: str) -> None: ...
    def SetMaterialDisplayComponentData(self, entity: DisplayComponentEntity, name: str) -> None: ...

class DisplayConfiguration(DictionaryRecord):
    """.NET: Autodesk.Aec.DatabaseServices.DisplayConfiguration"""
    def __init__(self, *args) -> None: ...
    DisplayTheme: ObjectId
    CutPlaneBelowRange: float
    CutPlaneAboveRange: float
    CutPlaneOffsetFromWcsZero: float
    StateImageIndex: DisplayConfigurationImageIndex
    StateIcon: Icon
    HardViewDirectionType: ViewDirection
    HardViewDirection: Vector3d
    UseViewportViewDirection: bool
    HardViewSet: ObjectId
    ViewDependentCombinations: ViewDependentCombinationCollection
    DefaultViewDependentViewSet: ObjectId
    IsViewDependent: bool
    Translator: DictionaryRecordNameTranslator
    Classifications: ClassificationCollection
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    KeynoteValue: str
    Keynote: str
    IsLocked: bool
    AlternateName: str
    LocalizedName: str
    Name: str
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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
    def AttachDisplayTheme(self, themeId: ObjectId) -> None: ...
    def DetachDisplayTheme(self, ) -> None: ...
    def FindViewDependentViewSet(self, direction: Vector3d) -> int: ...
    def GetStateIcon(self, index: DisplayConfigurationImageIndex) -> Icon: ...
    def ResolveViewSet(self, viewportDirection: Vector3d) -> ViewDependentCombination: ...
    @staticmethod
    def VectorToViewDirectionType(direction: Vector3d) -> ViewDirection: ...
    @staticmethod
    def ViewDirectionTypeToVector(type: ViewDirection) -> Vector3d: ...

class DisplayConfigurationImageIndex:
    """.NET enum: Autodesk.Aec.DatabaseServices.DisplayConfigurationImageIndex"""
    def __init__(self, *args) -> None: ...
    FirstImage: int  # = 0
    MultiView: int  # = 0
    MultiViewDefault: int  # = 1
    FixedView: int  # = 2
    FixedViewDefault: int  # = 3
    LastImage: int  # = 3
class DisplayConfigurationParameter:
    """.NET enum: Autodesk.Aec.DatabaseServices.DisplayConfigurationParameter"""
    def __init__(self, *args) -> None: ...
    DefaultViewDependentSet: int  # = 0
    HardSet: int  # = 1
    ViewDependentSet: int  # = 2
    UseViewportViewDirection: int  # = 3
    HardViewDirection: int  # = 4
    HardViewDirectionType: int  # = 5
    CutPlaneOffset: int  # = 6
    CutPlaneAbove: int  # = 7
    CutPlaneBelow: int  # = 8
class DisplayMaterialInformation(DisposableWrapper):
    """.NET: Autodesk.Aec.DatabaseServices.DisplayMaterialInformation"""
    def __init__(self, *args) -> None: ...
    MaterialLocation: MaterialInformationLocation
    IsFromObjectOverride: bool
    ComponentId: int
    LocationStyleId: ObjectId
    LocationId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Clone(self, ) -> object: ...
    @staticmethod
    def Create(unmanagedPointer: IntPtr, autoDelete: bool) -> DisplayMaterialInformation: ...

class DisplayProperties(DictionaryRecord):
    """.NET: Autodesk.Aec.DatabaseServices.DisplayProperties"""
    def __init__(self, *args) -> None: ...
    OwnerObjectId: ObjectId
    IsStyleOverride: bool
    IsDrawingDefault: bool
    OwningDisplayRepClass: RXClass
    OwningDisplayRep: ObjectId
    Translator: DictionaryRecordNameTranslator
    Classifications: ClassificationCollection
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    KeynoteValue: str
    Keynote: str
    IsLocked: bool
    AlternateName: str
    LocalizedName: str
    Name: str
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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
    def DeprecateOverride(self, newObject: DBObject, deprecatedDisplayRepId: ObjectId, oldDisplayRepId: ObjectId) -> ObjectId: ...
    def GetApplicableDisplayComponents(self, componentNames: StringCollection) -> list: ...
    def GetDisplayComponents(self, componentNames: StringCollection) -> list: ...
    @staticmethod
    def GetDisplayPropertiesFromOverride(id: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def GetDisplayPropertiesOverrideClassType(id: ObjectId) -> RXClass: ...
    @staticmethod
    def GetDisplayPropsExistsInDrawingDefaultDictionary(dispPropsClass: RXClass, db: Database) -> ObjectId: ...
    @staticmethod
    def GetDisplayRepsForOverride(id: ObjectId) -> ObjectIdCollection: ...
    def GetDisplayRepsWhichWorksWithThisDisplayProps(self, ignoreOwnerDisplayRep: bool) -> ObjectIdCollection: ...
    @staticmethod
    def GetDisplayRepsWhichWorksWithThisDisplayPropsClass(db: Database, displayPropsClass: RXClass, ignoreDerivedDispProps: bool) -> ObjectIdCollection: ...
    @staticmethod
    def RemoveDisplayPropsFromDrawingDefaultDictionary(objectId: ObjectId) -> bool: ...
    def SetDisplayRepDefaults(self, displayRep: DisplayRepresentation) -> None: ...

class DisplayPropertiesMaterial(DisplayProperties):
    """.NET: Autodesk.Aec.DatabaseServices.DisplayPropertiesMaterial"""
    def __init__(self, *args) -> None: ...
    SurfaceHatchLocationFlags: SurfaceHatchFlags
    SurfaceRenderMaterialMapping: SurfaceMappingType
    SectionedBodyRenderingMaterialId: ObjectId
    SectionRenderingMaterialId: ObjectId
    SurfaceRenderingMaterialId: ObjectId
    KeepAllHiddenLinework: bool
    MergeCommonMaterials: bool
    ExcludeFrom2dSectionShrinkwrap: bool
    SectionedBoundaryProperties: DisplayComponentEntity
    OutsideBodyProperties: DisplayComponentEntity
    SectionHatch: DisplayComponentHatch
    PlanHatch: DisplayComponentHatch
    SectionElevationLineworkProperties: DisplayComponentEntity
    BodyProperties: DisplayComponentEntity
    LineworkProperties: DisplayComponentEntity
    SurfaceHatch: DisplayComponentHatch
    OwnerObjectId: ObjectId
    IsStyleOverride: bool
    IsDrawingDefault: bool
    OwningDisplayRepClass: RXClass
    OwningDisplayRep: ObjectId
    Translator: DictionaryRecordNameTranslator
    Classifications: ClassificationCollection
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    KeynoteValue: str
    Keynote: str
    IsLocked: bool
    AlternateName: str
    LocalizedName: str
    Name: str
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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
    def DisplayComponentForDisplayComponentType(self, materialDisplayComponentType: ByMaterialDisplayComponentType) -> DisplayComponentEntity: ...
    def DisplayComponentTypeForDisplayComponent(self, component: DisplayComponentEntity) -> ByMaterialDisplayComponentType: ...
    @staticmethod
    def GetDisplayPropertiesForMaterial(materialDisplayRepresentId: ObjectId, materialId: ObjectId) -> ObjectId: ...
    @staticmethod
    def MaterialComponentType(componentName: str) -> ByMaterialDisplayComponentType: ...
    @staticmethod
    def MaterialDisplayComponentName(materialDisplayComponentType: ByMaterialDisplayComponentType) -> str: ...

class DisplayRepresentation(DictionaryRecord):
    """.NET: Autodesk.Aec.DatabaseServices.DisplayRepresentation"""
    def __init__(self, *args) -> None: ...
    CanBeDeleted: bool
    SymbolName: str
    IsNewToThisDrawing: bool
    IsUserDisplayRepresentation: bool
    CurrentMaterialComponentDisplayInformation: DisplayMaterialInformation
    DefaultRecordName: str
    StateImageIndex: DisplayRepresentationImageIndex
    StateIcon: Icon
    BaseGsMarkerValue: int
    HasReliableGsMarkers: bool
    IsSimilarTo: str
    UseObjectSnapCache: bool
    DisplayPropertiesClass: RXClass
    DefaultDisplayPropertiesId: ObjectId
    DisplayRepresentationName: str
    ViewTypeDisplayName: str
    DefaultVisibility: bool
    WorksWith: RXClass
    Translator: DictionaryRecordNameTranslator
    Classifications: ClassificationCollection
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    KeynoteValue: str
    Keynote: str
    IsLocked: bool
    AlternateName: str
    LocalizedName: str
    Name: str
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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
    def CreateNewDisplayProperties(self, ) -> DisplayProperties: ...
    def CreateRecordName(self, symbolName: str) -> str: ...
    def CreateUniqueRecordName(self, db: Database) -> str: ...
    def FindDisplayPropertiesOverride(self, object: DBObject) -> ObjectId: ...
    def GetDisplayPropertiesId(self, objects: DBObjectCollection) -> ObjectId: ...
    def GetDisplayPropertiesLocationIds(self, object: DBObject) -> ObjectIdCollection: ...
    def GetDisplayPropertiesLocationLabels(self, object: DBObject) -> StringCollection: ...
    def GetGripGeometryIds(self, entity: Entity) -> IntegerCollection: ...
    def GetGripOnapModes(self, entity: Entity) -> IntegerCollection: ...
    def GetGripPoints(self, entity: Entity) -> Point3dCollection: ...
    def GetStateIcon(self, value: DisplayRepresentationImageIndex) -> Icon: ...
    def GetStretchPoints(self, entity: Entity) -> Point3dCollection: ...
    @staticmethod
    def IsVisible(representation: RXClass, id: ObjectId) -> bool: ...
    def MoveGripPointsAt(self, entity: Entity, indices: IntegerCollection, offset: Vector3d) -> None: ...
    def MoveStretchPointsAt(self, entity: Entity, indices: IntegerCollection, offset: Vector3d) -> None: ...
    def SetEnforcedOverridenDisplayPropertiesValues(self, properties: DisplayProperties) -> None: ...
    def SetOverriddenDisplayPropertiesDefaults(self, properties: DisplayProperties) -> None: ...
    @staticmethod
    def StandardDisplayRepresentationTypeName(type: DisplayRepresentationTypeName) -> str: ...

class DisplayRepresentationIdCollection:
    """.NET: Autodesk.Aec.DatabaseServices.DisplayRepresentationIdCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: ObjectId
    def Add(self, item: ObjectId) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, item: ObjectId) -> bool: ...
    def CopyTo(self, array: list, start: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, item: ObjectId) -> int: ...
    def Insert(self, index: int, item: ObjectId) -> None: ...
    def Remove(self, item: ObjectId) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class DisplayRepresentationImageIndex:
    """.NET enum: Autodesk.Aec.DatabaseServices.DisplayRepresentationImageIndex"""
    def __init__(self, *args) -> None: ...
    FirstImage: int  # = 0
    Normal: int  # = 0
    WithoutProperties: int  # = 1
    UserDefined: int  # = 2
    LastImage: int  # = 2
class DisplayRepresentationManager:
    """.NET: Autodesk.Aec.DatabaseServices.DisplayRepresentationManager"""
    def __init__(self, *args) -> None: ...
    Initialization: bool
    DisplayDxfName: bool
    DisplayRepresentaionToObjectTypeMap: RXClassToObjectIdCollection
    DisplayRepresentationsDictionaryId: ObjectId
    DefaultDisplayConfigurationId: ObjectId
    DisplayConfigurationIdForCurrentViewport: ObjectId
    def ActualDisplayRepresentationDirection(self, viewportId: ObjectId, viewDirection: Vector3d) -> Vector3d: ...
    def CopyOverridenDisplayProperties(self, sourceId: ObjectId, userId: ObjectId) -> ObjectIdCollection: ...
    def CreateUserDefaultDisplayProperty(self, id: ObjectId, name: str, flags: int) -> ObjectId: ...
    def CreateUserDisplayRepresentation(self, id: ObjectId, name: str, flags: int) -> ObjectId: ...
    def DisplayConfigurationId(self, viewportId: ObjectId, viewDirection: Vector3d) -> ObjectId: ...
    def DisplayRepresentationSet(self, viewportId: ObjectId, viewDirection: Vector3d) -> ObjectId: ...
    def EnsureDisplayRepresentaionsHaveUniqueDictionaryNames(self, ) -> None: ...
    @staticmethod
    def GetActiveDisplayRepresentationSets(db: Database) -> ObjectIdCollection: ...
    def GetAllDisplayRepresentationsWorkForSpecifiedClass(self, worksWithClass: RXClass) -> ObjectIdCollection: ...
    @staticmethod
    def GetConfigurationOverrideFromInsertPath(blockStack: ObjectIdCollection) -> ObjectId: ...
    def GetDisplayConfigurationId(self, id: ObjectId) -> ObjectId: ...
    def GetDisplayRepresentationId(self, viewClass: RXClass) -> ObjectId: ...
    def GetDisplayRepresentationIdFromXref(self, view: DisplayRepresentation, db: Database) -> ObjectId: ...
    def GetDisplayRepresentationIdsFromCurrentViewport(self, classType: RXClass, anchorType: RXClass) -> ObjectIdCollection: ...
    @staticmethod
    def GetDisplayRepresentationsDictionary(db: Database) -> ObjectId: ...
    @staticmethod
    def GetXrefInsertConfigurationOverride(reference: BlockReference) -> ObjectId: ...
    @staticmethod
    def GetXrefInsertOverlayDabase(blockRef: BlockReference) -> Database: ...
    @staticmethod
    def IsGSViewportDraw(draw: ViewportDraw) -> bool: ...
    def PopInitialization(self, ) -> None: ...
    def PushInitialization(self, doInitialization: bool) -> None: ...
    @staticmethod
    def RegisterDisplayRepresentation(viewClass: RXClass, viewSetNames: StringCollection) -> None: ...
    @staticmethod
    def RemoveXrefInsertConfigurationOverride(blockReference: BlockReference) -> None: ...
    def SetDisplayConfigurationId(self, id: ObjectId, configurationId: ObjectId) -> None: ...
    @staticmethod
    def SetXrefInsertConfigurationOverride(blockReference: BlockReference, configurationId: ObjectId, inverseOverlayOverride: bool) -> None: ...
    @staticmethod
    def UnregisterDisplayRepresentation(viewClass: RXClass) -> None: ...
    def UpdateMaskBlockDisplayRepresentations(self, sourceId: ObjectId, userId: ObjectId) -> None: ...

class DisplayRepresentationSetParameter:
    """.NET enum: Autodesk.Aec.DatabaseServices.DisplayRepresentationSetParameter"""
    def __init__(self, *args) -> None: ...
    DisplayRepresentation: int  # = 0
    ClippedMaterials: int  # = 1
    SurfaceHatching: int  # = 2
    SectionBodyDisplay: int  # = 3
    Classification: int  # = 4
    SectionByDisplayRange: int  # = 5
    LiveSectionClipVolumes: int  # = 6
class DisplayRepresentationTData(RXObject):
    """.NET: Autodesk.Aec.DatabaseServices.DisplayRepresentationTData"""
    def __init__(self, *args) -> None: ...
    Properties: DisplayProperties
    MaskProfilePushCount: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class DisplayRepresentationTypeName:
    """.NET enum: Autodesk.Aec.DatabaseServices.DisplayRepresentationTypeName"""
    def __init__(self, *args) -> None: ...
    General: int  # = 0
    Plan: int  # = 1
    Model: int  # = 2
    Sketch: int  # = 3
    Reflected: int  # = 4
    Elevation: int  # = 5
    PlanLowDetail: int  # = 6
    PlanHighDetail: int  # = 7
    ModelLowDetail: int  # = 8
    ModelHighDetail: int  # = 9
    Nominal: int  # = 10
class DisplaySet(DictionaryRecord):
    """.NET: Autodesk.Aec.DatabaseServices.DisplaySet"""
    def __init__(self, *args) -> None: ...
    ClassificationFilter: ClassificationCollection
    DisableSectionedBodyDisplay: bool
    DisableSurfaceHatching: bool
    ShowClippedMaterials: bool
    ClipModelGeometry: bool
    HasTransientLiveSectionBody: bool
    LiveSectionClipVolumes: ObjectIdCollection
    LiveSectionBody: Body
    HasLiveClippingBody: bool
    IsStandardSet: bool
    DisplayRepresentationIds: DisplayRepresentationIdCollection
    Translator: DictionaryRecordNameTranslator
    Classifications: ClassificationCollection
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    KeynoteValue: str
    Keynote: str
    IsLocked: bool
    AlternateName: str
    LocalizedName: str
    Name: str
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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
    def GetCombinedDisplayRangeAndLiveSectionBody(self, configuration: DisplayConfiguration) -> Body: ...
    def GetDisplayRangeSectionBody(self, configuration: DisplayConfiguration) -> Body: ...
    def GetStandardType(self, ) -> StandardDisplaySetType: ...
    def SetStandardType(self, type: StandardDisplaySetType, db: Database) -> None: ...
    def SetTransientLiveSectionBody(self, body: Body) -> None: ...
    def UpdateMergedClassifications(self, oldSystemDefinition: ObjectId, oldClassId: ObjectId, newSystemDefinition: ObjectId, newClassId: ObjectId) -> None: ...
    def WorksWith(self, type: RXClass) -> ObjectIdCollection: ...

class DisplayTheme(Geo):
    """.NET: Autodesk.Aec.DatabaseServices.DisplayTheme"""
    def __init__(self, *args) -> None: ...
    IsActive: bool
    ParticipatesInDynamicUCS: bool
    Scale: float
    SupportsVisualStyle: bool
    IsAnchored: bool
    AnchorId: ObjectId
    CanBeAnchored: bool
    GeoEcsIsDirty: bool
    GeoEcs: Matrix3d
    ZDir: Vector3d
    YDir: Vector3d
    XDir: Vector3d
    Normal: Vector3d
    Rotation: float
    Direction: Vector3d
    Location: Point3d
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    StyleId: ObjectId
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    Description: str
    TypeIcon: Icon
    DisplayName: str
    Overrides: OverrideCollection
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
    def GetDimensionHeight(self, style: DisplayThemeStyle) -> float: ...
    def GetDimensionRowHeight(self, style: DisplayThemeStyle) -> float: ...
    def GetDimensionWidth(self, style: DisplayThemeStyle) -> float: ...
    def GetExtentBoundBox(self, ) -> BoundBox3d: ...
    def GetTransformMatrix(self, ) -> Matrix3d: ...

class DisplayThemeCellFormat(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.DisplayThemeCellFormat"""
    def __init__(self, *args) -> None: ...
    ThemeSymbolType: ThemeSymbolType
    RotationType: RotationType
    Gap: float
    Height: float
    TextStyleIdString: str
    TextStyleId: ObjectId
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetActualTextHeight(self, text: str, textHeightScale: float) -> float: ...
    def GetCellHeight(self, text: str) -> float: ...
    def GetCellHeightWithFixedWidth(self, text: str, fixedWidth: float) -> float: ...
    def GetCellWidth(self, text: str) -> float: ...
    def GetHeight(self, text: str) -> float: ...
    def GetRotatedTextCellWidth(self, text: str, fixedWidth: float) -> float: ...
    def GetSymbolHeight(self, count: int) -> float: ...
    def GetSymbolWidth(self, count: int) -> float: ...
    def GetWidth(self, text: str) -> float: ...
    def ScaleBy(self, dScale: float) -> None: ...

class DisplayThemeComponentBase(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.DisplayThemeComponentBase"""
    def __init__(self, *args) -> None: ...
    Rules: DisplayThemeRuleBase
    Name: str
    DisplayProperties: DisplayComponentHatch
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetDisplayString(self, ) -> str: ...
    def SupportsEntity(self, entity: Entity) -> bool: ...

class DisplayThemeComponentCollection:
    """.NET: Autodesk.Aec.DatabaseServices.DisplayThemeComponentCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: DisplayThemeComponentBase
    def Add(self, value: DisplayThemeComponentBase) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: DisplayThemeComponentBase) -> bool: ...
    def CopyTo(self, array: list, start: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: DisplayThemeComponentBase) -> int: ...
    def Insert(self, index: int, value: DisplayThemeComponentBase) -> None: ...
    def Remove(self, value: DisplayThemeComponentBase) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class DisplayThemeNextNodeOperator:
    """.NET enum: Autodesk.Aec.DatabaseServices.DisplayThemeNextNodeOperator"""
    def __init__(self, *args) -> None: ...
    NextNodeOperatorAnd: int  # = 0
    NextNodeOperatorOr: int  # = 1
class DisplayThemeRuleBase(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.DisplayThemeRuleBase"""
    def __init__(self, *args) -> None: ...
    Value: object
    FormattedValue: str
    ValueAsString: str
    DataType: PropertyDataType
    NextNodeOperator: DisplayThemeNextNodeOperator
    ComparisonOperator: DisplayThemeRuleComparisonOperator
    Precision: int
    Units: int
    PropertyName: str
    PropertyOwnerName: str
    PropertyOwnerTypeName: str
    DisplayString: str
    DisplayThemeRules: DisplayThemeRuleCollection
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetCollectProperties(self, ) -> StringCollection: ...
    def GetCollectPropertiesDefaultIndex(self, ) -> int: ...
    def GetCollectPropertyOwners(self, ) -> StringCollection: ...
    def GetCollectPropertyOwnersDefaultIndex(self, ) -> int: ...
    def GetTrueFalseText(self, isFormatted: bool) -> StringCollection: ...
    def SupportsEntity(self, entity: Entity) -> bool: ...

class DisplayThemeRuleCollection:
    """.NET: Autodesk.Aec.DatabaseServices.DisplayThemeRuleCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: DisplayThemeRuleBase
    def Add(self, value: DisplayThemeRuleBase) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: DisplayThemeRuleBase) -> bool: ...
    def CopyTo(self, array: list, start: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: DisplayThemeRuleBase) -> int: ...
    def Insert(self, index: int, value: DisplayThemeRuleBase) -> None: ...
    def Remove(self, value: DisplayThemeRuleBase) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class DisplayThemeRuleComparisonOperator:
    """.NET enum: Autodesk.Aec.DatabaseServices.DisplayThemeRuleComparisonOperator"""
    def __init__(self, *args) -> None: ...
    RuleComparisonOperatorIsNone: int  # = 0
    RuleComparisonOperatorEqualTo: int  # = 1
    RuleComparisonOperatorNotEqualTo: int  # = 2
    RuleComparisonOperatorLessThan: int  # = 3
    RuleComparisonOperatorLessThanEqualTo: int  # = 4
    RuleComparisonOperatorGreaterThan: int  # = 5
    RuleComparisonOperatorGreaterThanEqualTo: int  # = 6
    RuleComparisonOperatorInRange: int  # = 7
class DisplayThemeStyle(DictionaryRecord):
    """.NET: Autodesk.Aec.DatabaseServices.DisplayThemeStyle"""
    def __init__(self, *args) -> None: ...
    Title: str
    CellFormat: DisplayThemeCellFormat
    DisplayThemeComponents: DisplayThemeComponentCollection
    Translator: DictionaryRecordNameTranslator
    Classifications: ClassificationCollection
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    KeynoteValue: str
    Keynote: str
    IsLocked: bool
    AlternateName: str
    LocalizedName: str
    Name: str
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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
    def GetDisplayThemeDisplayPropsForEntity(self, entity: Entity, componentIndex: int) -> DisplayComponentHatch: ...

class DistributionFlags:
    """.NET enum: Autodesk.Aec.DatabaseServices.DistributionFlags"""
    def __init__(self, *args) -> None: ...
    DistributeEvenlyToAll: int  # = 0
    DistributeToFirst: int  # = 1
    DistributeToLast: int  # = 2
    DistributeToMiddle: int  # = 4
    NeverExceedCellSize: int  # = 8
    MaintainAtLeastHalfCellSize: int  # = 16
class DivisionDirection:
    """.NET enum: Autodesk.Aec.DatabaseServices.DivisionDirection"""
    def __init__(self, *args) -> None: ...
    AlongXAxis: int  # = 0
    AlongYAxis: int  # = 1
class EditInPlaceProfile(Geo):
    """.NET: Autodesk.Aec.DatabaseServices.EditInPlaceProfile"""
    def __init__(self, *args) -> None: ...
    UseMoveGrip: bool
    UseDefaultMenus: bool
    UseDefaultGrips: bool
    DrawDefaultGraphics: bool
    UsesInsertionPoint: bool
    EditingContext: EditingContext
    EditingConstraint: EditingConstraint
    InvalidProfile: Profile
    BaseProfile: Profile
    InsertionPoint: Point3d
    EcsInsertionPoint: Point2d
    IsAnchored: bool
    AnchorId: ObjectId
    CanBeAnchored: bool
    GeoEcsIsDirty: bool
    GeoEcs: Matrix3d
    ZDir: Vector3d
    YDir: Vector3d
    XDir: Vector3d
    Normal: Vector3d
    Rotation: float
    Direction: Vector3d
    Location: Point3d
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    StyleId: ObjectId
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    Description: str
    TypeIcon: Icon
    DisplayName: str
    Overrides: OverrideCollection
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
    def AddEcsVertex(self, ecsVertex: Point2d) -> None: ...
    def AddVertex(self, vertex: Point3d) -> None: ...
    def RemoveEcsVertex(self, ecsVertex: Point2d) -> None: ...
    def RemoveVertex(self, vertex: Point3d) -> None: ...
    def SetEcsVertices(self, ecsPoints: Point2dCollection) -> None: ...
    def SetVertices(self, ecsPoints: Point3dCollection, plane: Plane) -> None: ...

class EditState(RXObject):
    """.NET: Autodesk.Aec.DatabaseServices.EditState"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def RegisterState(self, id: ObjectId) -> None: ...
    def UnregisterState(self, id: ObjectId) -> None: ...

class EditStateManager(RXObject):
    """.NET: Autodesk.Aec.DatabaseServices.EditStateManager"""
    def __init__(self, *args) -> None: ...
    Instance: EditStateManager
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def CurrentState(id: ObjectId) -> EditState: ...
    def GripStatus(self, entity: Entity, status: GripStatus) -> None: ...
    def UnregisterState(self, id: ObjectId) -> None: ...
    def UnregisterStateForEntitiesInDatabase(self, database: Database) -> None: ...

class EditingConstraint:
    """.NET enum: Autodesk.Aec.DatabaseServices.EditingConstraint"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    WidthFixed: int  # = 1
    DepthFixed: int  # = 2
    WidthDepthFixed: int  # = 3
    RectangularShape: int  # = 4
class EditingContext:
    """.NET enum: Autodesk.Aec.DatabaseServices.EditingContext"""
    def __init__(self, *args) -> None: ...
    ClosedShape: int  # = 0
    OpenShape: int  # = 1
class Entity(Curve):
    """.NET: Autodesk.Aec.DatabaseServices.Entity"""
    def __init__(self, *args) -> None: ...
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    StyleId: ObjectId
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    Description: str
    TypeIcon: Icon
    DisplayName: str
    Overrides: OverrideCollection
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
    def GetAutomaticallyBoundSpaces(self, blockRefPath: ObjectIdCollection, boundSpaces: AutomaticSpaceBoundary) -> None: ...
    def GetBaseProfile(self, toWcs: Matrix3d) -> Profile: ...
    def GetLocalExtents(self, extents: BoundBlock3d) -> None: ...
    def GetLocalModelCachedExtents(self, ext: BoundBlock3d) -> None: ...
    def GetMaterialComponents(self, componentIds: IntegerCollection, componentNames: StringCollection, materialIds: ObjectIdCollection) -> None: ...
    def GetMaterialLocations(self, locationIds: IntegerCollection, styleIdArray: ObjectIdCollection) -> None: ...
    def GetProfile(self, cutPlane: Plane) -> Profile: ...
    def GetUsageArea(self, cutPlane: Plane) -> Profile: ...
    def GetWorldExtents(self, extents: BoundBlock3d) -> None: ...
    def SetAutomaticallyBoundSpaces(self, blockRefPath: ObjectIdCollection, boundSpaces: AutomaticSpaceBoundary) -> None: ...
    def SetBaseProfile(self, profile: Profile, matrix: Matrix3d) -> None: ...
    def SetDefaultLayer(self, ) -> None: ...
    def SetLocalExtents(self, extents: BoundBlock3d, flags: int) -> None: ...
    def SetLocalModelExtentsDirty(self, ) -> None: ...
    def SetMaterialComponents(self, componentIds: IntegerCollection, materialIds: ObjectIdCollection) -> None: ...
    def SetToStandard(self, db: Database) -> None: ...
    def SetWorldExtents(self, extents: BoundBlock3d) -> None: ...

class EntityBodyModifier(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.EntityBodyModifier"""
    def __init__(self, *args) -> None: ...
    OperationType: EntityBodyModifierOperationType
    ComponentId: int
    Body: Body
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetBodyAsMassElement(self, ) -> MassElement: ...
    def SetBodyFromMassElement(self, massElement: MassElement, wcsToEcs: Matrix3d) -> None: ...
    def TransformBy(self, matrix: Matrix3d) -> None: ...

class EntityBodyModifierOperationType:
    """.NET enum: Autodesk.Aec.DatabaseServices.EntityBodyModifierOperationType"""
    def __init__(self, *args) -> None: ...
    Additive: int  # = 0
    Subtractive: int  # = 1
    Replace: int  # = 2
class EntityCollectorData(DisposableWrapper):
    """.NET: Autodesk.Aec.DatabaseServices.EntityCollectorData"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(unmanagedPointer: IntPtr, autoDelete: bool) -> EntityCollectorData: ...

class EntityCollectorFilter(DisposableWrapper):
    """.NET: Autodesk.Aec.DatabaseServices.EntityCollectorFilter"""
    def __init__(self, *args) -> None: ...
    CheckRecurseBlock: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AllowEntity(self, entity: Entity, idArrayBlockReferencePath: ObjectIdCollection, dataToAdd: EntityCollectorData) -> bool: ...
    @staticmethod
    def Create(unmanagedPointer: IntPtr, autoDelete: bool) -> EntityCollectorFilter: ...
    def RecurseBlock(self, blockReference: BlockReference, idArrayBlockReferencePath: ObjectIdCollection) -> bool: ...

class EntityInterference(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.EntityInterference"""
    def __init__(self, *args) -> None: ...
    BlockReferenceBroken: bool
    FromBlockReference: bool
    Body: Body
    ShrinkWrapEffect: EntityInterferenceShrinkWrapEffect
    EntityId: ObjectId
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetEntityBlockRefPath(self, ) -> ObjectIdCollection: ...
    def SetEntityBlockRefPath(self, id: ObjectId, blockRefPath: ObjectIdCollection, pDb: Database) -> None: ...
    def UpdateBody(self, ) -> None: ...

class EntityInterferenceShrinkWrapEffect:
    """.NET enum: Autodesk.Aec.DatabaseServices.EntityInterferenceShrinkWrapEffect"""
    def __init__(self, *args) -> None: ...
    Ignore: int  # = 0
    Additive: int  # = 1
    Subtractive: int  # = 2
class EntityReference(BlockReference):
    """.NET: Autodesk.Aec.DatabaseServices.EntityReference"""
    def __init__(self, *args) -> None: ...
    ReferredEntityEcsInverse: Matrix3d
    ReferredEntityEcs: Matrix3d
    InsertionPointOfReferredEntity: Point3d
    InsertionPointOffset: Vector3d
    UseOffset: bool
    Scale: Scale3d
    BlockDefId: ObjectId
    IsAnchored: bool
    AnchorId: ObjectId
    CanBeAnchored: bool
    GeoEcsIsDirty: bool
    GeoEcs: Matrix3d
    ZDir: Vector3d
    YDir: Vector3d
    XDir: Vector3d
    Normal: Vector3d
    Rotation: float
    Direction: Vector3d
    Location: Point3d
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    StyleId: ObjectId
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    Description: str
    TypeIcon: Icon
    DisplayName: str
    Overrides: OverrideCollection
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

class EntitySelectedComponentInformation(RXObject):
    """.NET: Autodesk.Aec.DatabaseServices.EntitySelectedComponentInformation"""
    def __init__(self, *args) -> None: ...
    DisplayedMaterialWarningMessage: bool
    DisplayedSystemOverrideWarningMessage: bool
    DisplayedStyleOverrideWarningMessage: bool
    DisplayedDrawingDefaultWarningMessage: bool
    DisplayProperties: ObjectId
    ComponentName: str
    CurrentByMaterialStatus: bool
    HasMaterialInformation: bool
    MaterialInformation: MaterialInformation
    MaterialDisplayRepresentationId: ObjectId
    MaterialDisplayPropertiesId: ObjectId
    ViewportNumber: int
    ViewportId: ObjectId
    DisplayRepresentationId: ObjectId
    DisplayPropertiesId: ObjectId
    DisplayComponentName: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ExtendedStringCollection:
    """.NET: Autodesk.Aec.DatabaseServices.ExtendedStringCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: str
    def Add(self, value: str) -> int: ...
    def AddBatch(self, stringList: StringCollection) -> None: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: str) -> bool: ...
    def CopyTo(self, array: list, start: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: str) -> int: ...
    def Insert(self, index: int, value: str) -> None: ...
    def Remove(self, value: str) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class FaceScanResults:
    """.NET: Autodesk.Aec.DatabaseServices.FaceScanResults"""
    def __init__(self, *args) -> None: ...
    ExactHit: bool
    FaceCoordinateSystem: Matrix3d
    PickedFace: Face
    MaterialId: ObjectId

class Geo(Entity):
    """.NET: Autodesk.Aec.DatabaseServices.Geo"""
    def __init__(self, *args) -> None: ...
    IsAnchored: bool
    AnchorId: ObjectId
    CanBeAnchored: bool
    GeoEcsIsDirty: bool
    GeoEcs: Matrix3d
    ZDir: Vector3d
    YDir: Vector3d
    XDir: Vector3d
    Normal: Vector3d
    Rotation: float
    Direction: Vector3d
    Location: Point3d
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    StyleId: ObjectId
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    Description: str
    TypeIcon: Icon
    DisplayName: str
    Overrides: OverrideCollection
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
    def MoveInXY(self, offset: Vector3d) -> None: ...
    def MoveInZ(self, dist: float) -> None: ...
    def OnGeoEcsModified(self, previousEcs: Matrix3d) -> None: ...
    def ReleaseAnchor(self, ) -> None: ...
    def SetAnchor(self, newAnchor: Anchor) -> None: ...
    def TranslateBy(self, offset: Vector3d) -> None: ...
    def UpdateFromAnchor(self, anchor: Anchor) -> None: ...
    def UpdateGeoEcs(self, forceUpdate: bool) -> None: ...

class GraphicsStorage(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.GraphicsStorage"""
    def __init__(self, *args) -> None: ...
    GeometryExtents: Extents3d
    PlotStyleNameId: ObjectId
    PlotStyleNameType: PlotStyleNameType
    MaterialId: ObjectId
    LineTypeScale: float
    LineWeight: LineWeight
    GsMarker: IntPtr
    Color: Color
    ColorIndex: int
    LinetypeId: ObjectId
    LayerId: ObjectId
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class GraphicsStorageArc(GraphicsStorage):
    """.NET: Autodesk.Aec.DatabaseServices.GraphicsStorageArc"""
    def __init__(self, *args) -> None: ...
    Arc: CircularArc3d
    GeometryExtents: Extents3d
    PlotStyleNameId: ObjectId
    PlotStyleNameType: PlotStyleNameType
    MaterialId: ObjectId
    LineTypeScale: float
    LineWeight: LineWeight
    GsMarker: IntPtr
    Color: Color
    ColorIndex: int
    LinetypeId: ObjectId
    LayerId: ObjectId
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class GraphicsStorageBody(GraphicsStorage):
    """.NET: Autodesk.Aec.DatabaseServices.GraphicsStorageBody"""
    def __init__(self, *args) -> None: ...
    DiscardedEdgeFaceMask: int
    Body: Body
    GeometryExtents: Extents3d
    PlotStyleNameId: ObjectId
    PlotStyleNameType: PlotStyleNameType
    MaterialId: ObjectId
    LineTypeScale: float
    LineWeight: LineWeight
    GsMarker: IntPtr
    Color: Color
    ColorIndex: int
    LinetypeId: ObjectId
    LayerId: ObjectId
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class GraphicsStorageFace(GraphicsStorage):
    """.NET: Autodesk.Aec.DatabaseServices.GraphicsStorageFace"""
    def __init__(self, *args) -> None: ...
    EdgeVisibility: list
    Points: Point3dCollection
    GeometryExtents: Extents3d
    PlotStyleNameId: ObjectId
    PlotStyleNameType: PlotStyleNameType
    MaterialId: ObjectId
    LineTypeScale: float
    LineWeight: LineWeight
    GsMarker: IntPtr
    Color: Color
    ColorIndex: int
    LinetypeId: ObjectId
    LayerId: ObjectId
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class GraphicsStorageHatch(GraphicsStorage):
    """.NET: Autodesk.Aec.DatabaseServices.GraphicsStorageHatch"""
    def __init__(self, *args) -> None: ...
    HatchType: GraphicsStorageHatchType
    Vectors: list
    GeometryExtents: Extents3d
    PlotStyleNameId: ObjectId
    PlotStyleNameType: PlotStyleNameType
    MaterialId: ObjectId
    LineTypeScale: float
    LineWeight: LineWeight
    GsMarker: IntPtr
    Color: Color
    ColorIndex: int
    LinetypeId: ObjectId
    LayerId: ObjectId
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class GraphicsStorageHatchType:
    """.NET enum: Autodesk.Aec.DatabaseServices.GraphicsStorageHatchType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    SurfaceHatch: int  # = 1
    SectionHatch: int  # = 2
class GraphicsStoragePolyline(GraphicsStorage):
    """.NET: Autodesk.Aec.DatabaseServices.GraphicsStoragePolyline"""
    def __init__(self, *args) -> None: ...
    Points: Point3dCollection
    GeometryExtents: Extents3d
    PlotStyleNameId: ObjectId
    PlotStyleNameType: PlotStyleNameType
    MaterialId: ObjectId
    LineTypeScale: float
    LineWeight: LineWeight
    GsMarker: IntPtr
    Color: Color
    ColorIndex: int
    LinetypeId: ObjectId
    LayerId: ObjectId
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class GraphicsStorageShell(GraphicsStorage):
    """.NET: Autodesk.Aec.DatabaseServices.GraphicsStorageShell"""
    def __init__(self, *args) -> None: ...
    EdgeData: EdgeData
    FaceData: FaceData
    FaceList: list
    Vertices: Point3dCollection
    GeometryExtents: Extents3d
    PlotStyleNameId: ObjectId
    PlotStyleNameType: PlotStyleNameType
    MaterialId: ObjectId
    LineTypeScale: float
    LineWeight: LineWeight
    GsMarker: IntPtr
    Color: Color
    ColorIndex: int
    LinetypeId: ObjectId
    LayerId: ObjectId
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class GraphicsStorageVisibility:
    """.NET enum: Autodesk.Aec.DatabaseServices.GraphicsStorageVisibility"""
    def __init__(self, *args) -> None: ...
    Invisible: int  # = 0
    Visible: int  # = 1
    Silhouette: int  # = 2
class GraphicsSystemEntityDrawData(DisposableWrapper):
    """.NET: Autodesk.Aec.DatabaseServices.GraphicsSystemEntityDrawData"""
    def __init__(self, *args) -> None: ...
    GsMarkerInformationTree: GsMarkerInformationTree
    IsBusy: bool
    DbObject: DBObject
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def FreeDrawData(self, ) -> None: ...

class GridAssembly(CellLayoutTool):
    """.NET: Autodesk.Aec.DatabaseServices.GridAssembly"""
    def __init__(self, *args) -> None: ...
    HasEdgeProfile: bool
    IsStyleBased: bool
    IsManualGridDivision: bool
    InterferencesCount: int
    CustomLineworkProfile: Profile
    EditDepth: int
    ClippingProfile: Profile
    ClippingRectangle: ClippingRectangleInfo
    HasClippingRectangle: bool
    HasClippingProfile: bool
    HasClippingBoundary: bool
    EdgeCount: int
    CellCount: int
    NestedGridDivisionOverrides: NestedGridDivisionOverrideCollection
    NestedGridEdgeProfileOverrides: NestedGridEdgeProfileOverrideCollection
    NestedGridEdgeOverrides: NestedGridEdgeOverrideCollection
    NestedGridCellOverrides: NestedGridCellOverrideCollection
    NestedGridCellMergeData: NestedGridCellMergeDataCollection
    Interferences: GridAssemblyInterferenceCollection
    SupportsInterference: bool
    EndMiterAngle: float
    StartMiterAngle: float
    YAxisOffset: float
    YAxisLength: float
    XAxisLength: float
    BaseCurveRadius: float
    ComponentSet: GridAssemblyComponentSet
    GridAssemblyDefinition: GridAssemblyDefinition
    GridDefinitionLocation: GridDefinitionLocationType
    SupportsStyleBasedGridDefinition: bool
    SupportsInstanceBasedGridDefinition: bool
    LayoutCellIds: IntegerCollection
    LayoutNodeIds: IntegerCollection
    IsAnchored: bool
    AnchorId: ObjectId
    CanBeAnchored: bool
    GeoEcsIsDirty: bool
    GeoEcs: Matrix3d
    ZDir: Vector3d
    YDir: Vector3d
    XDir: Vector3d
    Normal: Vector3d
    Rotation: float
    Direction: Vector3d
    Location: Point3d
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    StyleId: ObjectId
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    Description: str
    TypeIcon: Icon
    DisplayName: str
    Overrides: OverrideCollection
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
    def GetAnchoredObjectsFor(self, collectRecursive: bool) -> ObjectIdCollection: ...
    def GetCell(self, cellId: int) -> GridAssemblyCell: ...
    def GetCellAt(self, index: int) -> GridAssemblyCell: ...
    def GetEdge(self, path: IntegerCollection, edgeIndex: int) -> GridAssemblyEdge: ...
    def GetEdgeAt(self, index: int) -> GridAssemblyEdge: ...
    def GetMaterialIds(self, component: GridAssemblyComponentType, materialIdsCollection: ObjectIdCollection) -> None: ...
    def GetMinAndMaxElevation(self, minElevation: float, maxElevation: float, componentSet: GridAssemblyComponentSet) -> None: ...
    def GetRightAndLeftExtents(self, leftOffset: float, rightOffset: float, componentSet: GridAssemblyComponentSet) -> None: ...
    def HasEndMiterAngle(self, angle: float) -> bool: ...
    def HasStartMiterAngle(self, angle: float) -> bool: ...
    def IncrementCellAssignmentId(self, ) -> int: ...
    def IncrementEdgeAssignmentId(self, ) -> int: ...
    def RemoveClippingBoundary(self, ) -> None: ...
    def SetGridDirty(self, value: bool) -> None: ...
    def SetHasEndMiterAngle(self, value: bool, angle: float) -> None: ...
    def SetHasStartMiterAngle(self, value: bool, angle: float) -> None: ...
    def UpdateGridContents(self, ) -> None: ...

class GridAssemblyCell(LayoutCell):
    """.NET: Autodesk.Aec.DatabaseServices.GridAssemblyCell"""
    def __init__(self, *args) -> None: ...
    ContainedEntityId: ObjectId
    NetEndY: float
    NetEndX: float
    NetStartY: float
    NetStartX: float
    NetCellProfile: Profile
    HasNetProfile: bool
    InfillOverrideId: int
    WasTransfered: bool
    IsVoid: bool
    AtEntityEnd: bool
    AtEntityStart: bool
    IsOverridden: bool
    IsLeafCell: bool
    GrossEndY: float
    GrossEndX: float
    GrossStartY: float
    GrossStartX: float
    CellAssignmentId: int
    NestingPath: IntegerCollection
    CellId: int
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetInfillDefinition(self, componentSet: GridAssemblyComponentSet, gridDefinition: GridAssemblyDefinition) -> NestedGridInfillDefinition: ...
    def IntersectsCutPlane(self, elevation: float) -> bool: ...

class GridAssemblyComponentSet(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.GridAssemblyComponentSet"""
    def __init__(self, *args) -> None: ...
    InteriorEdgeComponents: NestedGridInteriorEdgeComponentCollection
    BoundaryEdgeComponents: NestedGridBoundaryEdgeComponentCollection
    DivisionComponents: NestedGridDivisionComponentCollection
    InfillComponents: NestedGridInfillComponentCollection
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def IncrementComponentDefinitionId(self, ) -> int: ...

class GridAssemblyComponentType:
    """.NET enum: Autodesk.Aec.DatabaseServices.GridAssemblyComponentType"""
    def __init__(self, *args) -> None: ...
    Frame: int  # = 1
    Mullion: int  # = 2
    Infill: int  # = 3
class GridAssemblyCustomDefinition(GridAssemblyDefinition):
    """.NET: Autodesk.Aec.DatabaseServices.GridAssemblyCustomDefinition"""
    def __init__(self, *args) -> None: ...
    CustomGridDefinition: GridCustom
    Name: str
    SpecificCellAssignments: NestedGridCellAssignmentCollection
    SpecificInteriorEdgeAssignments: NestedGridInteriorEdgeAssignmentCollection
    SpecificBoundaryEdgeAssignments: NestedGridBoundaryEdgeAssignmentCollection
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class GridAssemblyDefinition(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.GridAssemblyDefinition"""
    def __init__(self, *args) -> None: ...
    Name: str
    SpecificCellAssignments: NestedGridCellAssignmentCollection
    SpecificInteriorEdgeAssignments: NestedGridInteriorEdgeAssignmentCollection
    SpecificBoundaryEdgeAssignments: NestedGridBoundaryEdgeAssignmentCollection
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def MaxCellAssignmentId(self, maxId: int) -> int: ...
    def MaxEdgeAssignmentId(self, maxId: int) -> int: ...

class GridAssemblyEdge(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.GridAssemblyEdge"""
    def __init__(self, *args) -> None: ...
    EdgeCurve: Curve2d
    ProfileOverrideId: ObjectId
    EdgeOverrideId: int
    EndAtEntityEnd: bool
    StartAtEntityEnd: bool
    EndAtEntityStart: bool
    StartAtEntityStart: bool
    IsVoid: bool
    HasProfileOverride: bool
    IsOverridden: bool
    IsInternalEdge: bool
    EdgeId: int
    EdgeAssignmentId: int
    NestingPath: IntegerCollection
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetEdgeDefinition(self, componentSet: GridAssemblyComponentSet, gridDef: GridAssemblyDefinition) -> NestedGridEdgeDefinition: ...
    def IntersectsCutPlane(self, elevation: float, edgeDefinition: NestedGridEdgeDefinition) -> bool: ...

class GridAssemblyInterference(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.GridAssemblyInterference"""
    def __init__(self, *args) -> None: ...
    AppliesToFlags: ApplyToFlags
    EntityId: ObjectId
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class GridAssemblyInterferenceCollection:
    """.NET: Autodesk.Aec.DatabaseServices.GridAssemblyInterferenceCollection"""
    def __init__(self, *args) -> None: ...
    Item: GridAssemblyInterference
    Count: int
    def Add(self, value: GridAssemblyInterference) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: GridAssemblyInterference) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: GridAssemblyInterference) -> int: ...
    def Insert(self, index: int, value: GridAssemblyInterference) -> None: ...
    def Remove(self, value: GridAssemblyInterference) -> None: ...
    def RemoveAt(self, index: int) -> None: ...
    def RemoveId(self, id: ObjectId) -> None: ...

class GridAssemblyStyle(DictionaryRecord):
    """.NET: Autodesk.Aec.DatabaseServices.GridAssemblyStyle"""
    def __init__(self, *args) -> None: ...
    NestedGridDivisionOverrides: NestedGridDivisionOverrideCollection
    NestedGridEdgeProfileOverrides: NestedGridEdgeProfileOverrideCollection
    NestedGridEdgeOverrides: NestedGridEdgeOverrideCollection
    NestedGridCellOverrides: NestedGridCellOverrideCollection
    NestedGridCellMergeData: NestedGridCellMergeDataCollection
    ComponentSet: GridAssemblyComponentSet
    GridAssemblyDefinition: GridAssemblyDefinition
    Translator: DictionaryRecordNameTranslator
    Classifications: ClassificationCollection
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    KeynoteValue: str
    Keynote: str
    IsLocked: bool
    AlternateName: str
    LocalizedName: str
    Name: str
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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
    def GetMaterialIds(self, component: GridAssemblyComponentType, componentIds: IntegerCollection, materialIdsCollection: ObjectIdCollection) -> None: ...
    def IncrementCellAssignmentId(self, ) -> int: ...
    def IncrementEdgeAssignmentId(self, ) -> int: ...
    def SetFromGridAssemblyEntity(self, gridAssembly: GridAssembly, copyMergers: bool, copyCellOverrides: bool, copyEdgeOverrides: bool, copyProfileOverrides: bool, copyDivisionOverrides: bool) -> None: ...

class GridCustom(GridAssemblyDefinition):
    """.NET: Autodesk.Aec.DatabaseServices.GridCustom"""
    def __init__(self, *args) -> None: ...
    TransientExteriorCell: GridCustomCell
    PersistentSolution: bool
    RequiresUpdate: bool
    CellCount: int
    NodeCount: int
    Segments: GridCustomSegmentCollection
    LayoutCellIds: IntegerCollection
    LayoutNodeIds: IntegerCollection
    Name: str
    SpecificCellAssignments: NestedGridCellAssignmentCollection
    SpecificInteriorEdgeAssignments: NestedGridInteriorEdgeAssignmentCollection
    SpecificBoundaryEdgeAssignments: NestedGridBoundaryEdgeAssignmentCollection
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CustomGridCell(self, id: int) -> GridCustomCell: ...
    def CustomGridCellAt(self, index: int) -> GridCustomCell: ...
    def CustomGridNode(self, id: int) -> GridCustomNode: ...
    def CustomGridNodeAt(self, index: int) -> GridCustomNode: ...
    def DeleteTransientData(self, ) -> None: ...
    def GetLayoutCellProfile(self, cellId: int, profileToWcs: Matrix3d) -> Profile: ...
    def GetLayoutNodeCoordinateSystem(self, nodeId: int) -> Matrix3d: ...
    def GetLayoutNodeLocation(self, nodeId: int) -> Point3d: ...
    def UpdateParameters(self, ) -> None: ...

class GridCustomCell(LayoutCell):
    """.NET: Autodesk.Aec.DatabaseServices.GridCustomCell"""
    def __init__(self, *args) -> None: ...
    CalculateCellProfile: Profile
    NodeInformationCollection: list
    ExtractNodeCount: int
    CellId: int
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class GridCustomNode(LayoutNode):
    """.NET: Autodesk.Aec.DatabaseServices.GridCustomNode"""
    def __init__(self, *args) -> None: ...
    SegmentId: int
    NodeLocation: NodeLocationType
    NodeId: int
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetIntersectionIds(self, segmentIds: IntegerCollection, segmentParameters: DoubleCollection) -> None: ...

class GridCustomSegment(Segment2d):
    """.NET: Autodesk.Aec.DatabaseServices.GridCustomSegment"""
    def __init__(self, *args) -> None: ...
    Id: int
    Attribute: Attribute
    IsCurveCircularArc2d: bool
    IsCurveLineSegment2d: bool
    CurveDirectionPositive: bool
    IsClosed: bool
    EndParameter: float
    StartParameter: float
    Interval: Interval
    MidPoint: Point2d
    BoundBox2d: BoundBox2d
    SegmentPosition: SegmentPosition
    Visible: bool
    Bulge: float
    Length: float
    EndPoint: Point2d
    StartPoint: Point2d
    Curve: Curve2d
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class GridCustomSegmentCollection:
    """.NET: Autodesk.Aec.DatabaseServices.GridCustomSegmentCollection"""
    def __init__(self, *args) -> None: ...
    Item: GridCustomSegment
    Count: int
    def Add(self, value: GridCustomSegment) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: GridCustomSegment) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def FindById(self, id: int) -> GridCustomSegment: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: GridCustomSegment) -> int: ...
    def Insert(self, index: int, value: GridCustomSegment) -> None: ...
    def Remove(self, value: GridCustomSegment) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class GridDefinitionLocationType:
    """.NET enum: Autodesk.Aec.DatabaseServices.GridDefinitionLocationType"""
    def __init__(self, *args) -> None: ...
    InstanceBased: int  # = 0
    StyleBased: int  # = 1
class GridType:
    """.NET enum: Autodesk.Aec.DatabaseServices.GridType"""
    def __init__(self, *args) -> None: ...
    UVRectangular: int  # = 0
    UVRadial: int  # = 1
    UVWRectangular: int  # = 2
    UVCustom: int  # = 3
class GridUv(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.GridUv"""
    def __init__(self, *args) -> None: ...
    VParameters: DoubleCollection
    UParameters: DoubleCollection
    VLayoutMode: UVLayoutModeType
    ULayoutMode: UVLayoutModeType
    VEndOffset: float
    UEndOffset: float
    VStartOffset: float
    UStartOffset: float
    VSpacing: float
    USpacing: float
    VAxisLength: float
    UAxisLength: float
    LayoutCellIds: IntegerCollection
    CellCount: int
    LayoutNodeIds: IntegerCollection
    NodeCount: int
    GridType: GridType
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddNode(self, parameterU: float, parameterV: float) -> None: ...
    def AppendGridColumn(self, parameterU: float) -> None: ...
    def AppendGridRow(self, parameterV: float) -> None: ...
    def GetLayoutCellProfile(self, cellId: int, toWcs: Matrix3d) -> Profile: ...
    def GetLayoutGrid2dCell(self, id: int) -> LayoutGrid2dCell: ...
    def GetLayoutGrid2dCellAt(self, index: int) -> LayoutGrid2dCell: ...
    def GetLayoutGrid2dNode(self, id: int) -> LayoutGrid2dNode: ...
    def GetLayoutGrid2dNodeAt(self, index: int) -> LayoutGrid2dNode: ...
    def GetLayoutNodeCoordinateSystem(self, nodeId: int) -> Matrix3d: ...
    def GetLayoutNodeLocation(self, nodeId: int) -> Point3d: ...
    def MoveGridColumn(self, oldParameter: float, newParameter: float) -> None: ...
    def MoveGridRow(self, oldParameter: float, newParameter: float) -> None: ...
    def RemoveGridColumn(self, parameterU: float) -> None: ...
    def RemoveGridRow(self, parameterV: float) -> None: ...
    def UpdateParameters(self, ) -> None: ...

class GridUvRadial(GridUv):
    """.NET: Autodesk.Aec.DatabaseServices.GridUvRadial"""
    def __init__(self, *args) -> None: ...
    VEndAngleOffset: float
    VStartAngleOffset: float
    VAngleSpacing: float
    VAxisAngle: float
    UInsideRadius: float
    VParameters: DoubleCollection
    UParameters: DoubleCollection
    VLayoutMode: UVLayoutModeType
    ULayoutMode: UVLayoutModeType
    VEndOffset: float
    UEndOffset: float
    VStartOffset: float
    UStartOffset: float
    VSpacing: float
    USpacing: float
    VAxisLength: float
    UAxisLength: float
    LayoutCellIds: IntegerCollection
    CellCount: int
    LayoutNodeIds: IntegerCollection
    NodeCount: int
    GridType: GridType
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class GridUvRectangular(GridUv):
    """.NET: Autodesk.Aec.DatabaseServices.GridUvRectangular"""
    def __init__(self, *args) -> None: ...
    VParameters: DoubleCollection
    UParameters: DoubleCollection
    VLayoutMode: UVLayoutModeType
    ULayoutMode: UVLayoutModeType
    VEndOffset: float
    UEndOffset: float
    VStartOffset: float
    UStartOffset: float
    VSpacing: float
    USpacing: float
    VAxisLength: float
    UAxisLength: float
    LayoutCellIds: IntegerCollection
    CellCount: int
    LayoutNodeIds: IntegerCollection
    NodeCount: int
    GridType: GridType
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class GridUvw(GridUv):
    """.NET: Autodesk.Aec.DatabaseServices.GridUvw"""
    def __init__(self, *args) -> None: ...
    WParameters: DoubleCollection
    WLayoutMode: UVLayoutModeType
    WEndOffset: float
    WStartOffset: float
    WSpacing: float
    WAxisLength: float
    LayoutVolumeIds: IntegerCollection
    VolumeCount: int
    VParameters: DoubleCollection
    UParameters: DoubleCollection
    VLayoutMode: UVLayoutModeType
    ULayoutMode: UVLayoutModeType
    VEndOffset: float
    UEndOffset: float
    VStartOffset: float
    UStartOffset: float
    VSpacing: float
    USpacing: float
    VAxisLength: float
    UAxisLength: float
    LayoutCellIds: IntegerCollection
    CellCount: int
    LayoutNodeIds: IntegerCollection
    NodeCount: int
    GridType: GridType
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddNode(self, parameterU: float, parameterV: float, parameterW: float) -> None: ...
    def AppendGridLevel(self, parameterW: float) -> None: ...
    def GetLayoutGrid3dCell(self, id: int) -> LayoutGrid3dCell: ...
    def GetLayoutGrid3dCellAt(self, index: int) -> LayoutGrid3dCell: ...
    def GetLayoutGrid3dNode(self, id: int) -> LayoutGrid3dNode: ...
    def GetLayoutGrid3dNodeAt(self, index: int) -> LayoutGrid3dNode: ...
    def GetLayoutGrid3dVolume(self, id: int) -> LayoutGrid3dVolume: ...
    def GetLayoutGrid3dVolumeAt(self, index: int) -> LayoutGrid3dVolume: ...
    def GetLayoutVolumeBody(self, volumeId: int, toWcs: Matrix3d) -> Body: ...
    def GetLayoutVolumeCentroid(self, volumeId: int) -> Matrix3d: ...
    def GetLayoutVolumeExtent(self, volumeId: int, length: float, width: float, height: float, toWcs: Matrix3d) -> None: ...
    def MoveGridLevel(self, oldParameter: float, newParameter: float) -> None: ...
    def RemoveGridLevel(self, parameterW: float) -> None: ...

class GsMarkerDisplayComponentInformationNode(GsMarkerInformationNode):
    """.NET: Autodesk.Aec.DatabaseServices.GsMarkerDisplayComponentInformationNode"""
    def __init__(self, *args) -> None: ...
    DisplayRepresentationId: ObjectId
    DisplayPropertiesId: ObjectId
    ParentDisplayRepresentationInformationNode: GsMarkerDisplayRepresentationInformationNode
    DisplayComponentName: str
    Name: str
    ParentTree: GsMarkerInformationTree
    ParentNode: GsMarkerInformationNode
    GsMarker: IntPtr
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class GsMarkerDisplayRepresentationInformationNode(GsMarkerInformationNode):
    """.NET: Autodesk.Aec.DatabaseServices.GsMarkerDisplayRepresentationInformationNode"""
    def __init__(self, *args) -> None: ...
    DisplayPropertiesId: ObjectId
    DisplayRepresentationId: ObjectId
    Name: str
    ParentTree: GsMarkerInformationTree
    ParentNode: GsMarkerInformationNode
    GsMarker: IntPtr
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetDisplayComponentId(self, component: DisplayComponentEntity) -> int: ...
    def GetDisplayComponentName(self, component: DisplayComponentEntity) -> str: ...
    def ResetTransientDisplayPropertiesInformation(self, ) -> None: ...
    def SetDisplayPropertiesInformation(self, properties: DisplayProperties) -> None: ...

class GsMarkerInformationNode(RXObject):
    """.NET: Autodesk.Aec.DatabaseServices.GsMarkerInformationNode"""
    def __init__(self, *args) -> None: ...
    Name: str
    ParentTree: GsMarkerInformationTree
    ParentNode: GsMarkerInformationNode
    GsMarker: IntPtr
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, node: GsMarkerInformationNode) -> None: ...
    def Clear(self, ) -> None: ...
    def CollectInformationNodes(self, nodeClass: RXClass, recursive: bool) -> list: ...
    def CollectLeafNodeGsMarkers(self, collectAll3DBodyGsMarkers: bool) -> list: ...
    def ContentToString(self, getName: bool, continueWithNextLevelNodes: bool) -> StringCollection: ...
    def InformationNodeForGsMarker(self, value: IntPtr) -> GsMarkerInformationNode: ...
    def InformationNodesForGsMarker(self, value: IntPtr) -> list: ...
    @staticmethod
    def ObjectIdFromOldId(oldId: int) -> ObjectId: ...

class GsMarkerInformationTree(GsMarkerInformationNode):
    """.NET: Autodesk.Aec.DatabaseServices.GsMarkerInformationTree"""
    def __init__(self, *args) -> None: ...
    IsEntity2dSectionType: bool
    IsDrawingWithDisplayTheme: bool
    SelectedObjectDisplayRepresentationId: ObjectId
    GsMarkersForHoverHighlighting: list
    HasGsMarkersForHoverHighlighting: bool
    AreComponentsSelected: bool
    IsDrawingCustomBlock: bool
    CustomBlockGsMarker: IntPtr
    CustomBlockOwnerEntityId: ObjectId
    EntityIsFromCustomBlock: bool
    PushCustomOverrideNode: bool
    PopulateTree: bool
    CurrentGsMarkerInformationNode: GsMarkerInformationNode
    ObjectId: ObjectId
    CurrentGsMarker: IntPtr
    NextGsMarker: IntPtr
    StartGsMarker: IntPtr
    Name: str
    ParentTree: GsMarkerInformationTree
    ParentNode: GsMarkerInformationNode
    GsMarker: IntPtr
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddBranchInformationNode(self, pushIntoCurrentNodeStack: bool) -> None: ...
    def AddCustomBlockInformationNode(self, pushIntoCurrentNodeStack: bool) -> None: ...
    def AddCustomInformationNode(self, nGsMarker: IntPtr, pushIntoCurrentNodeStack: bool) -> None: ...
    def AddDisplayComponentInformationNode(self, componentName: str, pushIntoCurrentNodeStack: bool) -> None: ...
    def AddDisplayRepresentationInformationNode(self, id: ObjectId, pushIntoCurrentNodeStack: bool) -> None: ...
    def AddDisplayThemeInformationNode(self, id: ObjectId, componentIndex: int, pushIntoCurrentNodeStack: bool) -> None: ...
    def AddGsMarkerInformationNode(self, node: GsMarkerInformationNode, pushIntoCurrentNodeStack: bool) -> None: ...
    def AddSelectedComponentInformation(self, information: EntitySelectedComponentInformation) -> None: ...
    def AddUnsupportedGraphicsInformationNode(self, pushIntoCurrentNodeStack: bool) -> None: ...
    def CleanupGsMarkersForHoverHighliting(self, ) -> None: ...
    def ClearSelectedComponentsGsMarkers(self, ) -> None: ...
    def ClearSelectedObjectDisplayRepresentationInformation(self, ) -> None: ...
    def CollectNonViewportInformationNodesInViewport(self, id: ObjectId, viewportIndex: int, nodeClass: RXClass, recursive: bool) -> list: ...
    def CustomBlockInformationToString(self, ) -> StringCollection: ...
    def GetDisplayComponentNodesInCurrentViewport(self, gsMarkers: IntPtrCollection, id: ObjectId, viewportNumber: int) -> list: ...
    def GetSelectedComponentGsMarkersForHighligting(self, ) -> IntPtrCollection: ...
    def GetSelectedComponentGsMarkersOnByMaterialChange(self, information: EntitySelectedComponentInformation) -> IntPtrCollection: ...
    def GetSelectedComponentsInformation(self, ) -> list: ...
    def GetViewportIdFromViewportNode(self, gsMarker: IntPtr) -> ObjectId: ...
    def GetViewportNumberFromViewportNode(self, gsMarker: IntPtr) -> int: ...
    def HasDatabaseReferencePath(self, path: ObjectIdCollection) -> bool: ...
    def InformationNodeForGsMarkerAndInformationType(self, value: IntPtr, nodeType: RXClass, doIsKindOfTest: bool) -> GsMarkerInformationNode: ...
    def PopCurrentGsMarkerInformationNode(self, nodeClass: RXClass, checkForDerivedTypes: bool) -> None: ...
    def PopViewportInformationNode(self, ) -> None: ...
    def PushCurrentGsMarkerInformationNode(self, node: GsMarkerInformationNode) -> None: ...
    def ResetCurrentNodeStack(self, ) -> None: ...
    def ResetTransientDisplayPropertiesInformationForCurrentDisplayInformationNode(self, ) -> None: ...
    def SetDisplayPropertiesForCurrentDisplayInformationNode(self, properties: DisplayProperties) -> None: ...
    def SetParentCustomBlockOwnerInformation(self, id: ObjectId, customBlockGsMarker: IntPtr) -> None: ...
    def UpdateSelectedComponentInformation(self, id: ObjectId, index: int) -> None: ...

class HatchType:
    """.NET enum: Autodesk.Aec.DatabaseServices.HatchType"""
    def __init__(self, *args) -> None: ...
    UserDefined: int  # = 0
    PreDefined: int  # = 1
    CustomDefined: int  # = 2
    SolidFill: int  # = 3
class IDisplayThemeComponentOperation:
    """.NET: Autodesk.Aec.DatabaseServices.IDisplayThemeComponentOperation"""
    def __init__(self, *args) -> None: ...
    def Add(self, A_0: DisplayThemeComponentBase) -> int: ...
    def GetAt(self, A_0: int) -> DisplayThemeComponentBase: ...
    def GetCount(self, ) -> int: ...
    def Insert(self, A_0: int, A_1: DisplayThemeComponentBase) -> None: ...
    def RemoveAll(self, ) -> None: ...
    def RemoveAt(self, A_0: int) -> None: ...

class IDisplayThemeRuleOperation:
    """.NET: Autodesk.Aec.DatabaseServices.IDisplayThemeRuleOperation"""
    def __init__(self, *args) -> None: ...
    def Add(self, A_0: DisplayThemeRuleBase) -> int: ...
    def GetAt(self, A_0: int) -> DisplayThemeRuleBase: ...
    def GetCount(self, ) -> int: ...
    def Insert(self, A_0: int, A_1: DisplayThemeRuleBase) -> None: ...
    def RemoveAll(self, ) -> None: ...
    def RemoveAt(self, A_0: int) -> None: ...

class IImpTreeOperation:
    """.NET: Autodesk.Aec.DatabaseServices.IImpTreeOperation"""
    def __init__(self, *args) -> None: ...
    def Add(self, A_0: ImpTree) -> int: ...
    def GetAt(self, A_0: int) -> ImpTree: ...
    def GetCount(self, ) -> int: ...
    def Insert(self, A_0: int, A_1: ImpTree) -> None: ...
    def RemoveAll(self, ) -> None: ...
    def RemoveAt(self, A_0: int) -> None: ...

class ILayerKeyDefinitionOperation:
    """.NET: Autodesk.Aec.DatabaseServices.ILayerKeyDefinitionOperation"""
    def __init__(self, *args) -> None: ...
    def Add(self, A_0: LayerKeyDefinition) -> int: ...
    def GetAt(self, A_0: str) -> LayerKeyDefinition: ...
    def GetCount(self, ) -> int: ...
    def IndexOf(self, A_0: LayerKeyDefinition) -> int: ...
    def Insert(self, A_0: int, A_1: LayerKeyDefinition) -> None: ...
    def RemoveAll(self, ) -> None: ...
    def RemoveAt(self, A_0: int) -> None: ...
    def SetAt(self, A_0: int, A_1: LayerKeyDefinition) -> None: ...

class IOverrideOperation:
    """.NET: Autodesk.Aec.DatabaseServices.IOverrideOperation"""
    def __init__(self, *args) -> None: ...
    def Add(self, A_0: Override) -> int: ...
    def GetAt(self, A_0: int) -> Override: ...
    def GetCount(self, ) -> int: ...
    def RemoveAll(self, ) -> None: ...
    def RemoveAt(self, A_0: int) -> None: ...

class IStringOperation:
    """.NET: Autodesk.Aec.DatabaseServices.IStringOperation"""
    def __init__(self, *args) -> None: ...
    def Add(self, A_0: str) -> int: ...
    def AddBatch(self, A_0: StringCollection) -> None: ...
    def Contains(self, A_0: str) -> bool: ...
    def GetAt(self, A_0: int) -> str: ...
    def GetCount(self, ) -> int: ...
    def IndexOf(self, A_0: str) -> int: ...
    def Insert(self, A_0: int, A_1: str) -> None: ...
    def Remove(self, value: str) -> None: ...
    def RemoveAll(self, ) -> None: ...
    def RemoveAt(self, A_0: int) -> None: ...
    def SetAt(self, A_0: int, A_1: str) -> None: ...

class IStringPairOperation:
    """.NET: Autodesk.Aec.DatabaseServices.IStringPairOperation"""
    def __init__(self, *args) -> None: ...
    def Add(self, A_0: StringPair) -> int: ...
    def Contains(self, strLeft: str) -> bool: ...
    def Get(self, strLeft: str) -> str: ...
    def GetAt(self, A_0: int) -> StringPair: ...
    def GetCount(self, ) -> int: ...
    def IndexOf(self, A_0: StringPair) -> int: ...
    def Insert(self, A_0: int, A_1: StringPair) -> None: ...
    def Remove(self, strLeft: str) -> None: ...
    def RemoveAll(self, ) -> None: ...
    def RemoveAt(self, A_0: int) -> None: ...
    def SetAt(self, A_0: int, A_1: StringPair) -> None: ...

class ImpArray(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.ImpArray`1"""
    def __init__(self, *args) -> None: ...
    AllowNullObjects: bool
    Item: T
    Count: int
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, item: T) -> None: ...
    def Clear(self, ) -> None: ...
    def Contains(self, item: T) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def DeleteAt(self, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, item: T) -> int: ...
    def Insert(self, index: int, item: T) -> None: ...
    def Remove(self, item: T) -> bool: ...
    def RemoveAll(self, ) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class ImpObject(RXObject):
    """.NET: Autodesk.Aec.DatabaseServices.ImpObject"""
    def __init__(self, *args) -> None: ...
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetToStandard(self, db: Database) -> None: ...
    def SubSetDatabaseDefaults(self, db: Database) -> None: ...

class ImpObjectCollection(DisposableWrapper):
    """.NET: Autodesk.Aec.DatabaseServices.ImpObjectCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: ImpObject
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, value: ImpObject) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: ImpObject) -> bool: ...
    def CopyTo(self, arr: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: ImpObject) -> int: ...
    def Insert(self, index: int, value: ImpObject) -> None: ...
    def Remove(self, value: ImpObject) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class ImpTree(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.ImpTree"""
    def __init__(self, *args) -> None: ...
    Children: ImpTreeCollection
    ParentTree: ImpTree
    IsRoot: bool
    Root: ImpTree
    AllowChildren: bool
    SubObjectsMightHaveReferences: bool
    AllowNullObjects: bool
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ImpTreeCollection:
    """.NET: Autodesk.Aec.DatabaseServices.ImpTreeCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: ImpTree
    def Add(self, value: ImpTree) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: ImpTree) -> bool: ...
    def CopyTo(self, array: list, start: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: ImpTree) -> int: ...
    def Insert(self, index: int, value: ImpTree) -> None: ...
    def Remove(self, value: ImpTree) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class IndexSpecifier(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.IndexSpecifier"""
    def __init__(self, *args) -> None: ...
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AppliesToIndex(self, index: int, startIndex: int, endIndex: int) -> bool: ...

class IndexSpecifierBoundaryEdge(IndexSpecifier):
    """.NET: Autodesk.Aec.DatabaseServices.IndexSpecifierBoundaryEdge"""
    def __init__(self, *args) -> None: ...
    BoundaryFlags: BoundaryFlags
    OnRight: bool
    OnBottom: bool
    OnLeft: bool
    OnTop: bool
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class IndexSpecifierExplicit(IndexSpecifier):
    """.NET: Autodesk.Aec.DatabaseServices.IndexSpecifierExplicit"""
    def __init__(self, *args) -> None: ...
    IndexArray: IntegerCollection
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AppendToIndexArray(self, index: int) -> None: ...
    def ClearIndexArray(self, ) -> None: ...
    def RemoveFromIndexArray(self, index: int) -> None: ...

class IndexSpecifierLocation(IndexSpecifier):
    """.NET: Autodesk.Aec.DatabaseServices.IndexSpecifierLocation"""
    def __init__(self, *args) -> None: ...
    AppliesToMiddleIndex: bool
    AppliesToEndIndex: bool
    AppliesToStartIndex: bool
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class InplaceEditor(DictionaryRecord):
    """.NET: Autodesk.Aec.DatabaseServices.InplaceEditor"""
    def __init__(self, *args) -> None: ...
    IsSingleComponentEditor: bool
    ActiveInplaceEditorComponentCount: int
    InplaceEditorComponentCount: int
    Entity: Entity
    OldEntityEcs: Matrix3d
    LongTransactionId: ObjectId
    EntityId: ObjectId
    OldUcsMatrix: Matrix3d
    Translator: DictionaryRecordNameTranslator
    Classifications: ClassificationCollection
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    KeynoteValue: str
    Keynote: str
    IsLocked: bool
    AlternateName: str
    LocalizedName: str
    Name: str
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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
    def GetInplaceEditEntities(self, ) -> ObjectIdCollection: ...
    def InvalidCommandInInPlaceEditMode(self, commandName: str, status: CommandStatus) -> bool: ...
    def IsCurrentEditorInplaceEditEntity(self, id: ObjectId) -> bool: ...

class InplaceEditorClassInformation:
    """.NET: Autodesk.Aec.DatabaseServices.InplaceEditorClassInformation"""
    def __init__(self, *args) -> None: ...
    InplaceEditorClassType: RXClass
    InplaceEditorId: ObjectId

class InplaceEditorMap(DisposableWrapper):
    """.NET: Autodesk.Aec.DatabaseServices.InplaceEditorMap"""
    def __init__(self, *args) -> None: ...
    Size: int
    FirstInplaceEditorId: ObjectId
    FirstParentEntityId: ObjectId
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddInplaceEditor(self, oldId: IntPtr, editorDataId: ObjectId) -> bool: ...
    def FindInplaceEditor(self, oldId: IntPtr) -> ObjectId: ...
    def FindInplaceEditorIdForInplaceEditEntityId(self, inplaceEditEntityId: ObjectId) -> ObjectId: ...
    def FindParentEntityIdForInplaceEditEntityId(self, inplaceEditEntityId: ObjectId) -> ObjectId: ...
    def FindParentEntityIdForInplaceEditorId(self, inplaceEditorId: ObjectId) -> ObjectId: ...
    def GetEntityIdsInInplaceEditMode(self, ) -> ObjectIdCollection: ...
    def GetObjectIdsInInplaceEditMode(self, ) -> ObjectIdCollection: ...
    def RemoveInplaceEditor(self, id: IntPtr) -> bool: ...
    def RemoveInplaceEditorAll(self, ) -> None: ...

class InplaceEditorUtilities:
    """.NET: Autodesk.Aec.DatabaseServices.InplaceEditorUtilities"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def AddEditorToExtentionDictionaryAndClose(objectToSegOn: DBObject, newEditorToAdd: InplaceEditor) -> ObjectId: ...
    @staticmethod
    def AddInplaceEditorToEntity(entity: Entity, inplaceEditorId: ObjectId) -> None: ...
    @staticmethod
    def CreateNewDictionaryEntryFromOldDictionaryEntry(oldDictionaryId: ObjectId, dictionary: Dictionary) -> ObjectId: ...
    @staticmethod
    def CreateNewInplaceEditDictionaryEntryFromOldDictionaryEntry(oldDictionaryId: ObjectId, dictionary: Dictionary) -> ObjectId: ...
    @staticmethod
    def CreateNewInplaceEditProfileDefinitionFromOldProfileDefinition(oldProfileId: ObjectId) -> ObjectId: ...
    @staticmethod
    def CreateNewProfileDefinitionFromOldProfileDefinition(oldProfileDefinition: ObjectId) -> ObjectId: ...
    @staticmethod
    def CurrentInplaceEditLongTransactionId(selectedObjectIds: ObjectIdCollection) -> ObjectId: ...
    @staticmethod
    def CurrentInplaceEditorId(selectedEntityId: ObjectId) -> ObjectId: ...
    @staticmethod
    def DeleteInplaceEditorFromEntity(entity: Entity, inplaceEditorId: ObjectId) -> None: ...
    @staticmethod
    def EntityIdInInPlaceEditMode(db: Database) -> ObjectId: ...
    @staticmethod
    def FindParentEntityIdForInplaceEditEntityId(inplaceEditEntityId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetInplaceEditEntitiesInInPlaceEditMode(db: Database) -> ObjectIdCollection: ...
    @staticmethod
    def GetInplaceEditorMap(db: Database) -> InplaceEditorMap: ...
    @staticmethod
    def HandleInplaceEditorMapOperation(entityId: ObjectId, inplaceEditorId: ObjectId, add: bool) -> None: ...
    @staticmethod
    def HandledModifiedMessageFromInplaceEditEntity(fromObj: DBObject, toEntity: Entity, messageId: int, allowedFromClass: RXClass) -> None: ...
    @staticmethod
    def InplaceEditorIdInInPlaceEditMode(db: Database) -> ObjectId: ...
    @staticmethod
    def InvalidCommandInInPlaceEditMode(db: Database, command: str, status: CommandStatus) -> bool: ...
    @staticmethod
    def IsInplaceEditSessionInProgress(db: Database) -> bool: ...
    @staticmethod
    def PurgeInplaceEditProfiles(db: Database, profileIds: ObjectIdCollection) -> None: ...
    @staticmethod
    def RemoveEditorFromExtentionDictionary(objectToRemoveFrom: DBObject, entryId: ObjectId) -> None: ...
    @staticmethod
    def SelectionSetHasEntitiesFromInPlaceEditSession(selectedObjIds: ObjectIdCollection, inplaceEditEntities: ObjectIdCollection) -> bool: ...
    @staticmethod
    def UpdateAnchoredObjectsForInplaceEditOperation(db: Database, commandName: str) -> bool: ...

class LayerKeyDefinition(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.LayerKeyDefinition"""
    def __init__(self, *args) -> None: ...
    Overrides: ExtendedStringCollection
    Removable: bool
    IsPlottable: bool
    Plotstyle: str
    Lineweight: LineWeight
    Linetype: str
    Color: Color
    LayerName: str
    Key: str
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LayerKeyDefinitionCollection:
    """.NET: Autodesk.Aec.DatabaseServices.LayerKeyDefinitionCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: LayerKeyDefinition
    Item: LayerKeyDefinition
    def Add(self, value: LayerKeyDefinition) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: LayerKeyDefinition) -> bool: ...
    def CopyTo(self, array: list, start: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: LayerKeyDefinition) -> int: ...
    def Insert(self, index: int, value: LayerKeyDefinition) -> None: ...
    def Remove(self, value: LayerKeyDefinition) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class LayerKeyStyle(DictionaryRecord):
    """.NET: Autodesk.Aec.DatabaseServices.LayerKeyStyle"""
    def __init__(self, *args) -> None: ...
    OverridesEnabled: bool
    Standard: str
    OverrideCount: int
    KeyDefinitions: LayerKeyDefinitionCollection
    Translator: DictionaryRecordNameTranslator
    Classifications: ClassificationCollection
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    KeynoteValue: str
    Keynote: str
    IsLocked: bool
    AlternateName: str
    LocalizedName: str
    Name: str
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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
    def GetOverrideAt(self, index: int, name: str, value: str) -> str: ...
    def OverrideExists(self, name: str) -> bool: ...
    def SetOverrideAt(self, index: int, value: str) -> None: ...

class LayoutCell(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.LayoutCell"""
    def __init__(self, *args) -> None: ...
    CellId: int
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LayoutCurve(LayoutTool):
    """.NET: Autodesk.Aec.DatabaseServices.LayoutCurve"""
    def __init__(self, *args) -> None: ...
    Spacing: float
    EndOffset: float
    StartOffset: float
    NodePositions: DoubleCollection
    NodeCount: int
    LayoutMode: LayoutModeType
    CurveId: ObjectId
    LayoutNodeIds: IntegerCollection
    IsAnchored: bool
    AnchorId: ObjectId
    CanBeAnchored: bool
    GeoEcsIsDirty: bool
    GeoEcs: Matrix3d
    ZDir: Vector3d
    YDir: Vector3d
    XDir: Vector3d
    Normal: Vector3d
    Rotation: float
    Direction: Vector3d
    Location: Point3d
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    StyleId: ObjectId
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    Description: str
    TypeIcon: Icon
    DisplayName: str
    Overrides: OverrideCollection
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
    def AppendLayoutNode(self, position: float) -> None: ...
    def GetLayoutCurveNode(self, id: int) -> LayoutCurveNode: ...
    def GetLayoutCurveNodeAt(self, index: int) -> LayoutCurveNode: ...
    def GetNodePositionAt(self, index: int) -> float: ...
    def MoveLayoutNode(self, oldParameter: float, newParameter: float) -> None: ...
    def RemoveLayoutNode(self, id: int) -> None: ...
    def RemoveLayoutNodeAt(self, index: int) -> None: ...
    def SetLayoutNodeLocation(self, node: LayoutCurveNode, location: Point3d) -> None: ...
    def UpdateParameters(self, ) -> None: ...

class LayoutCurveNode(LayoutNode):
    """.NET: Autodesk.Aec.DatabaseServices.LayoutCurveNode"""
    def __init__(self, *args) -> None: ...
    UPosition: float
    NodeId: int
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LayoutGrid2d(CellLayoutTool):
    """.NET: Autodesk.Aec.DatabaseServices.LayoutGrid2d"""
    def __init__(self, *args) -> None: ...
    BoundaryHoles: ObjectIdCollection
    BoundaryProfile: Profile
    BoundaryId: ObjectId
    GridType: GridType
    CustomGrid: GridCustom
    BaseGrid: GridUv
    LayoutCellIds: IntegerCollection
    LayoutNodeIds: IntegerCollection
    IsAnchored: bool
    AnchorId: ObjectId
    CanBeAnchored: bool
    GeoEcsIsDirty: bool
    GeoEcs: Matrix3d
    ZDir: Vector3d
    YDir: Vector3d
    XDir: Vector3d
    Normal: Vector3d
    Rotation: float
    Direction: Vector3d
    Location: Point3d
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    StyleId: ObjectId
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    Description: str
    TypeIcon: Icon
    DisplayName: str
    Overrides: OverrideCollection
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
    def AppendBoundaryHole(self, id: ObjectId) -> None: ...
    def OppositeLayoutNode(self, nodeId: int, angleOffset: float, oppositeNodeId: int, oppositeAngleOffset: float) -> bool: ...
    def RemoveBoundaryHole(self, id: ObjectId) -> None: ...

class LayoutGrid2dCell(LayoutCell):
    """.NET: Autodesk.Aec.DatabaseServices.LayoutGrid2dCell"""
    def __init__(self, *args) -> None: ...
    VIndex: int
    UIndex: int
    CellId: int
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LayoutGrid2dNode(LayoutCurveNode):
    """.NET: Autodesk.Aec.DatabaseServices.LayoutGrid2dNode"""
    def __init__(self, *args) -> None: ...
    VPosition: float
    UPosition: float
    NodeId: int
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LayoutGrid3d(VolumeLayoutTool):
    """.NET: Autodesk.Aec.DatabaseServices.LayoutGrid3d"""
    def __init__(self, *args) -> None: ...
    GridType: GridType
    BaseGrid: GridUvw
    LayoutVolumeIds: IntegerCollection
    LayoutCellIds: IntegerCollection
    LayoutNodeIds: IntegerCollection
    IsAnchored: bool
    AnchorId: ObjectId
    CanBeAnchored: bool
    GeoEcsIsDirty: bool
    GeoEcs: Matrix3d
    ZDir: Vector3d
    YDir: Vector3d
    XDir: Vector3d
    Normal: Vector3d
    Rotation: float
    Direction: Vector3d
    Location: Point3d
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    StyleId: ObjectId
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    Description: str
    TypeIcon: Icon
    DisplayName: str
    Overrides: OverrideCollection
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

class LayoutGrid3dCell(LayoutGrid2dCell):
    """.NET: Autodesk.Aec.DatabaseServices.LayoutGrid3dCell"""
    def __init__(self, *args) -> None: ...
    Plane: PlaneType
    WIndex: int
    VIndex: int
    UIndex: int
    CellId: int
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LayoutGrid3dNode(LayoutGrid2dNode):
    """.NET: Autodesk.Aec.DatabaseServices.LayoutGrid3dNode"""
    def __init__(self, *args) -> None: ...
    WPosition: float
    VPosition: float
    UPosition: float
    NodeId: int
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LayoutGrid3dVolume(LayoutVolume):
    """.NET: Autodesk.Aec.DatabaseServices.LayoutGrid3dVolume"""
    def __init__(self, *args) -> None: ...
    WIndex: int
    VIndex: int
    UIndex: int
    VolumeId: int
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LayoutModeType:
    """.NET enum: Autodesk.Aec.DatabaseServices.LayoutModeType"""
    def __init__(self, *args) -> None: ...
    Manual: int  # = 0
    Repeat: int  # = 1
    SpaceOut: int  # = 2
class LayoutNode(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.LayoutNode"""
    def __init__(self, *args) -> None: ...
    NodeId: int
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LayoutTool(Geo):
    """.NET: Autodesk.Aec.DatabaseServices.LayoutTool"""
    def __init__(self, *args) -> None: ...
    LayoutNodeIds: IntegerCollection
    IsAnchored: bool
    AnchorId: ObjectId
    CanBeAnchored: bool
    GeoEcsIsDirty: bool
    GeoEcs: Matrix3d
    ZDir: Vector3d
    YDir: Vector3d
    XDir: Vector3d
    Normal: Vector3d
    Rotation: float
    Direction: Vector3d
    Location: Point3d
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    StyleId: ObjectId
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    Description: str
    TypeIcon: Icon
    DisplayName: str
    Overrides: OverrideCollection
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
    def GetClosestLayoutNode(self, location: Point3d) -> int: ...
    def GetLayoutNodeCoordinateSystem(self, nodeId: int) -> Matrix3d: ...
    def GetLayoutNodeLocation(self, nodeId: int) -> Point3d: ...

class LayoutVolume(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.LayoutVolume"""
    def __init__(self, *args) -> None: ...
    VolumeId: int
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LineWorkComponent(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.LineWorkComponent"""
    def __init__(self, *args) -> None: ...
    Description: str
    Name: str
    Id: int
    Database: Database
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LineWorkComponentCollection:
    """.NET: Autodesk.Aec.DatabaseServices.LineWorkComponentCollection"""
    def __init__(self, *args) -> None: ...
    Item: LineWorkComponent
    Count: int
    def Add(self, value: LineWorkComponent) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: LineWorkComponent) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: LineWorkComponent) -> int: ...
    def Insert(self, index: int, value: LineWorkComponent) -> None: ...
    def Remove(self, value: LineWorkComponent) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class LineWorkRule(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.LineWorkRule"""
    def __init__(self, *args) -> None: ...
    Description: str
    ComponentId: int
    FilterFlags: int
    Color: Color
    Database: Database
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LineWorkRuleCollection:
    """.NET: Autodesk.Aec.DatabaseServices.LineWorkRuleCollection"""
    def __init__(self, *args) -> None: ...
    Item: LineWorkRule
    Count: int
    def Add(self, value: LineWorkRule) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: LineWorkRule) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: LineWorkRule) -> int: ...
    def Insert(self, index: int, value: LineWorkRule) -> None: ...
    def Remove(self, value: LineWorkRule) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class LineWorkType:
    """.NET enum: Autodesk.Aec.DatabaseServices.LineWorkType"""
    def __init__(self, *args) -> None: ...
    LineWork: int  # = 0
    SurfaceHatching: int  # = 1
    SectionHatching: int  # = 2
class LinearUnit:
    """.NET enum: Autodesk.Aec.DatabaseServices.LinearUnit"""
    def __init__(self, *args) -> None: ...
    Scientific: int  # = 1
    Decimal: int  # = 2
    Engineering: int  # = 3
    Architectural: int  # = 4
    Fractional: int  # = 5
    CurrentLU: int  # = -1
class ListDefinition(ClassificationDefinition):
    """.NET: Autodesk.Aec.DatabaseServices.ListDefinition"""
    def __init__(self, *args) -> None: ...
    AllowToVary: bool
    ClassificationTree: ClassificationTree
    AppliesToAll: bool
    AppliesToFilter: StringCollection
    Translator: DictionaryRecordNameTranslator
    Classifications: ClassificationCollection
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    KeynoteValue: str
    Keynote: str
    IsLocked: bool
    AlternateName: str
    LocalizedName: str
    Name: str
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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
    def AddListItem(self, name: str) -> ObjectId: ...
    def DeleteListItem(self, id: ObjectId) -> None: ...
    def GetListItem(self, name: str) -> ObjectId: ...
    def GetListItems(self, ) -> ObjectIdCollection: ...
    def RenameList(self, listId: ObjectId, newName: str) -> None: ...

class ListItem(Classification):
    """.NET: Autodesk.Aec.DatabaseServices.ListItem"""
    def __init__(self, *args) -> None: ...
    OwningSystemName: str
    NameAndDescription: str
    OwningSystemId: ObjectId
    Translator: DictionaryRecordNameTranslator
    Classifications: ClassificationCollection
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    KeynoteValue: str
    Keynote: str
    IsLocked: bool
    AlternateName: str
    LocalizedName: str
    Name: str
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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

class Listener(DisposableWrapper):
    """.NET: Autodesk.Aec.DatabaseServices.Listener"""
    def __init__(self, *args) -> None: ...
    Enabled: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def addClassNotToNotify(self, type: RXClass) -> None: ...
    def addClassParam(self, paramId: int, type: RXClass) -> None: ...
    def addClassToNotify(self, type: RXClass) -> None: ...
    def allowByClass(self, type: RXClass) -> bool: ...
    def objectAppended(self, pObjAppended: DBObject) -> None: ...
    def objectErased(self, pObjErased: DBObject) -> None: ...
    def objectModified(self, pObj: DBObject) -> None: ...

class MaskBlockDefinition(DictionaryRecord):
    """.NET: Autodesk.Aec.DatabaseServices.MaskBlockDefinition"""
    def __init__(self, *args) -> None: ...
    ExtraGraphicsBlockId: ObjectId
    CutProfile: Profile
    Translator: DictionaryRecordNameTranslator
    Classifications: ClassificationCollection
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    KeynoteValue: str
    Keynote: str
    IsLocked: bool
    AlternateName: str
    LocalizedName: str
    Name: str
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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

class MaskBlockReference(BlockReference):
    """.NET: Autodesk.Aec.DatabaseServices.MaskBlockReference"""
    def __init__(self, *args) -> None: ...
    CutProfile: Profile
    Scale: Scale3d
    BlockDefId: ObjectId
    IsAnchored: bool
    AnchorId: ObjectId
    CanBeAnchored: bool
    GeoEcsIsDirty: bool
    GeoEcs: Matrix3d
    ZDir: Vector3d
    YDir: Vector3d
    XDir: Vector3d
    Normal: Vector3d
    Rotation: float
    Direction: Vector3d
    Location: Point3d
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    StyleId: ObjectId
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    Description: str
    TypeIcon: Icon
    DisplayName: str
    Overrides: OverrideCollection
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

class MassElement(Geo):
    """.NET: Autodesk.Aec.DatabaseServices.MassElement"""
    def __init__(self, *args) -> None: ...
    Volume: float
    Profile: Profile
    ProfileId: ObjectId
    ShapeSubType: ShapeSubType
    ShapeType: ShapeType
    Body: Body
    Deviation: float
    Rise: float
    Radius: float
    Height: float
    Depth: float
    Width: float
    SubType: str
    IsAnchored: bool
    AnchorId: ObjectId
    CanBeAnchored: bool
    GeoEcsIsDirty: bool
    GeoEcs: Matrix3d
    ZDir: Vector3d
    YDir: Vector3d
    XDir: Vector3d
    Normal: Vector3d
    Rotation: float
    Direction: Vector3d
    Location: Point3d
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    StyleId: ObjectId
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    Description: str
    TypeIcon: Icon
    DisplayName: str
    Overrides: OverrideCollection
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
    def ChangeTo(self, type: ShapeType, profile: Profile) -> None: ...
    @staticmethod
    def Create(type: ShapeType, profile: Profile) -> MassElement: ...
    def GetMaterialId(self, component: int, wasOverridden: bool) -> ObjectId: ...
    def ParentMassing(self, id: ObjectId, operation: Operation) -> None: ...
    def SetBody(self, body: Body, centerToLcs: bool) -> None: ...

class MassElementStyle(DictionaryRecord):
    """.NET: Autodesk.Aec.DatabaseServices.MassElementStyle"""
    def __init__(self, *args) -> None: ...
    MaterialId: ObjectId
    Translator: DictionaryRecordNameTranslator
    Classifications: ClassificationCollection
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    KeynoteValue: str
    Keynote: str
    IsLocked: bool
    AlternateName: str
    LocalizedName: str
    Name: str
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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

class MassGroup(Geo):
    """.NET: Autodesk.Aec.DatabaseServices.MassGroup"""
    def __init__(self, *args) -> None: ...
    SupportsAnchoring: bool
    RootNode: ObjectId
    Entities: ObjectIdCollection
    Volume: float
    Nodes: ObjectIdCollection
    NodeCount: int
    Body: Body
    SubType: str
    IsAnchored: bool
    AnchorId: ObjectId
    CanBeAnchored: bool
    GeoEcsIsDirty: bool
    GeoEcs: Matrix3d
    ZDir: Vector3d
    YDir: Vector3d
    XDir: Vector3d
    Normal: Vector3d
    Rotation: float
    Direction: Vector3d
    Location: Point3d
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    StyleId: ObjectId
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    Description: str
    TypeIcon: Icon
    DisplayName: str
    Overrides: OverrideCollection
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
    def AddNode(self, entity: Entity, operation: Operation) -> None: ...
    def Contains(self, id: ObjectId, operation: Operation, recursive: bool) -> bool: ...
    def GetMaterialId(self, componentId: int) -> ObjectId: ...
    def GetOperation(self, id: ObjectId) -> Operation: ...
    @staticmethod
    def GetSupportsAnchoring(massGroupId: ObjectId) -> bool: ...
    def MoveNodeToAfter(self, id: ObjectId, afterId: ObjectId) -> None: ...
    def MoveNodeToBefore(self, id: ObjectId, beforeId: ObjectId) -> None: ...
    def MoveNodeToBeginning(self, id: ObjectId) -> None: ...
    def MoveNodeToEnd(self, id: ObjectId) -> None: ...
    def ParentMassing(self, operation: Operation) -> ObjectId: ...
    def RemoveAllNodes(self, ) -> None: ...
    def RemoveNode(self, entity: Entity) -> None: ...
    def SaveBody(self, filename: str) -> None: ...
    def SetOperation(self, id: ObjectId, operation: Operation) -> None: ...
    @staticmethod
    def SetSupportsAnchoring(massGroupId: ObjectId, supports: bool) -> None: ...

class MaterialDefinition(DictionaryRecord):
    """.NET: Autodesk.Aec.DatabaseServices.MaterialDefinition"""
    def __init__(self, *args) -> None: ...
    Translator: DictionaryRecordNameTranslator
    Classifications: ClassificationCollection
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    KeynoteValue: str
    Keynote: str
    IsLocked: bool
    AlternateName: str
    LocalizedName: str
    Name: str
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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

class MaterialInformation(DisplayMaterialInformation):
    """.NET: Autodesk.Aec.DatabaseServices.MaterialInformation"""
    def __init__(self, *args) -> None: ...
    MaterialId: ObjectId
    ComponentName: str
    MaterialLocation: MaterialInformationLocation
    IsFromObjectOverride: bool
    ComponentId: int
    LocationStyleId: ObjectId
    LocationId: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CopyTo(self, information: MaterialInformation) -> None: ...

class MaterialInformationLocation:
    """.NET enum: Autodesk.Aec.DatabaseServices.MaterialInformationLocation"""
    def __init__(self, *args) -> None: ...
    MaterialFromObject: int  # = 0
    MaterialFromStyle: int  # = 1
    MaterialFromObjectOverride: int  # = 2
class MaterialUtility:
    """.NET: Autodesk.Aec.DatabaseServices.MaterialUtility"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetMaterialOverrides(entity: Entity, locationIds: IntegerCollection, materialIdArray: ObjectIdCollection) -> None: ...
    @staticmethod
    def GetResolvedMaterials(entity: Entity) -> ResolvedMaterialCollection: ...

class MultiViewBlockAttributeReference(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.MultiViewBlockAttributeReference"""
    def __init__(self, *args) -> None: ...
    MText: MText
    NeedsUpdate: bool
    Attribute: AttributeReference
    Prompt: str
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CopyToMText(self, ) -> None: ...
    def DeleteMText(self, ) -> None: ...

class MultiViewBlockAttributeReferenceCollection:
    """.NET: Autodesk.Aec.DatabaseServices.MultiViewBlockAttributeReferenceCollection"""
    def __init__(self, *args) -> None: ...
    Item: MultiViewBlockAttributeReference
    Count: int
    def Add(self, item: MultiViewBlockAttributeReference) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, item: MultiViewBlockAttributeReference) -> bool: ...
    def CopyTo(self, array: list, start: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, item: MultiViewBlockAttributeReference) -> int: ...
    def Insert(self, index: int, item: MultiViewBlockAttributeReference) -> None: ...
    def Remove(self, item: MultiViewBlockAttributeReference) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class MultiViewBlockDefinition(DictionaryRecord):
    """.NET: Autodesk.Aec.DatabaseServices.MultiViewBlockDefinition"""
    def __init__(self, *args) -> None: ...
    InterferenceBlockId: ObjectId
    DisplayRepresentationDefinitions: MultiViewBlockDisplayRepresentationDefinitionCollection
    Translator: DictionaryRecordNameTranslator
    Classifications: ClassificationCollection
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    KeynoteValue: str
    Keynote: str
    IsLocked: bool
    AlternateName: str
    LocalizedName: str
    Name: str
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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
    def GetAllBlocksReferenced(self, ) -> ObjectIdCollection: ...
    def SetAttributeGripsDisabled(self, disable: bool) -> None: ...

class MultiViewBlockDisplayRepresentationDefinition(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.MultiViewBlockDisplayRepresentationDefinition"""
    def __init__(self, *args) -> None: ...
    ViewDefinitions: MultiViewBlockViewDefinitionCollection
    DisplayRepresentationId: ObjectId
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetAttributeGripsDisabled(self, disable: bool) -> None: ...

class MultiViewBlockDisplayRepresentationDefinitionCollection:
    """.NET: Autodesk.Aec.DatabaseServices.MultiViewBlockDisplayRepresentationDefinitionCollection"""
    def __init__(self, *args) -> None: ...
    Item: MultiViewBlockDisplayRepresentationDefinition
    Count: int
    def Add(self, item: MultiViewBlockDisplayRepresentationDefinition) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, item: MultiViewBlockDisplayRepresentationDefinition) -> bool: ...
    def CopyTo(self, array: list, start: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, item: MultiViewBlockDisplayRepresentationDefinition) -> int: ...
    def Insert(self, index: int, item: MultiViewBlockDisplayRepresentationDefinition) -> None: ...
    def Remove(self, item: MultiViewBlockDisplayRepresentationDefinition) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class MultiViewBlockReference(BlockReference):
    """.NET: Autodesk.Aec.DatabaseServices.MultiViewBlockReference"""
    def __init__(self, *args) -> None: ...
    ScaleDependentOffset: Vector3d
    AnnotationScaleUniqueIdentifier: IntPtr
    AnnotationScale: AnnotationScale
    NumberOfAnnotationScaleContexts: int
    HasAttributes: bool
    ViewInstances: MultiViewBlockViewInstanceCollection
    Scale: Scale3d
    BlockDefId: ObjectId
    IsAnchored: bool
    AnchorId: ObjectId
    CanBeAnchored: bool
    GeoEcsIsDirty: bool
    GeoEcs: Matrix3d
    ZDir: Vector3d
    YDir: Vector3d
    XDir: Vector3d
    Normal: Vector3d
    Rotation: float
    Direction: Vector3d
    Location: Point3d
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    StyleId: ObjectId
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    Description: str
    TypeIcon: Icon
    DisplayName: str
    Overrides: OverrideCollection
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
    def UpdateAnnotative(self, ) -> bool: ...
    def UpdateViewInstances(self, ) -> None: ...
    def UpdateViewInstancesAttributes(self, includeTextStyle: bool) -> None: ...
    def UpdateViewInstancesAttributesIncludeWidth(self, includeTextStyle: bool) -> None: ...

class MultiViewBlockViewDefinition(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.MultiViewBlockViewDefinition"""
    def __init__(self, *args) -> None: ...
    AttributeGripsDisabled: bool
    BlockId: ObjectId
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def IsViewOn(self, viewDirectionType: ViewDirection) -> bool: ...
    def SetAllViews(self, isOn: bool) -> None: ...
    def SetViewOn(self, viewDirectionType: ViewDirection, isOn: bool) -> None: ...

class MultiViewBlockViewDefinitionCollection:
    """.NET: Autodesk.Aec.DatabaseServices.MultiViewBlockViewDefinitionCollection"""
    def __init__(self, *args) -> None: ...
    Item: MultiViewBlockViewDefinition
    Count: int
    def Add(self, item: MultiViewBlockViewDefinition) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, item: MultiViewBlockViewDefinition) -> bool: ...
    def CopyTo(self, array: list, start: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, item: MultiViewBlockViewDefinition) -> int: ...
    def Insert(self, index: int, item: MultiViewBlockViewDefinition) -> None: ...
    def Remove(self, item: MultiViewBlockViewDefinition) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class MultiViewBlockViewInstance(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.MultiViewBlockViewInstance"""
    def __init__(self, *args) -> None: ...
    AttributeReferences: MultiViewBlockAttributeReferenceCollection
    NeedsAttributeUpdate: bool
    Offset: Vector3d
    BlockId: ObjectId
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def EnsureConsistentAttributes(self, ) -> None: ...
    def EnsureConsistentAttributesAndUpdateExisting(self, includeTextStyle: bool) -> None: ...
    def EnsureConsistentAttributesAndUpdateExistingIncludeWidth(self, includeTextStyle: bool) -> None: ...
    def NeedsAttributeUpdateFullCheck(self, includeTextStyle: bool) -> bool: ...
    def NeedsAttributeUpdateFullCheckIncludeWidth(self, includeTextStyle: bool) -> bool: ...
    def ResetAttributes(self, blockId: ObjectId) -> None: ...

class MultiViewBlockViewInstanceCollection:
    """.NET: Autodesk.Aec.DatabaseServices.MultiViewBlockViewInstanceCollection"""
    def __init__(self, *args) -> None: ...
    Item: MultiViewBlockViewInstance
    Count: int
    def CopyTo(self, array: list, start: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...

class NameObjectIdPair:
    """.NET: Autodesk.Aec.DatabaseServices.NameObjectIdPair"""
    def __init__(self, *args) -> None: ...
    ObjectId: ObjectId
    Name: str

class NameObjectIdPairCollection(DisposableWrapper):
    """.NET: Autodesk.Aec.DatabaseServices.NameObjectIdPairCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: NameObjectIdPair
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, value: NameObjectIdPair) -> int: ...
    def AddAlpha(self, value: NameObjectIdPair) -> int: ...
    def AddHead(self, value: NameObjectIdPair) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: NameObjectIdPair) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetMatchFor(self, objectId: ObjectId) -> str: ...
    def IndexOf(self, objectId: ObjectId) -> int: ...
    def Insert(self, index: int, value: NameObjectIdPair) -> None: ...
    def Remove(self, value: NameObjectIdPair) -> None: ...
    def RemoveAt(self, index: int) -> None: ...
    def RemoveHead(self, ) -> None: ...
    def RemoveTail(self, ) -> None: ...
    def Rename(self, oldName: str, newName: str) -> bool: ...

class NameTranslator(DisposableWrapper):
    """.NET: Autodesk.Aec.DatabaseServices.NameTranslator"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, globalName: str, localName: str) -> bool: ...
    @staticmethod
    def Create(unmanagedPointer: IntPtr, autoDelete: bool) -> NameTranslator: ...
    def Get(self, globalName: str) -> str: ...
    @staticmethod
    def IsTranslatorManaged(translator: NameTranslator) -> bool: ...
    @staticmethod
    def ManageTranslator(translator: NameTranslator) -> bool: ...

class NestedGridBoundaryEdgeAssignmentCollection:
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridBoundaryEdgeAssignmentCollection"""
    def __init__(self, *args) -> None: ...
    Default: NestedGridEdgeAssignment
    Item: NestedGridEdgeAssignment
    Count: int
    def Add(self, value: NestedGridEdgeAssignment) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: NestedGridEdgeAssignment) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetId(self, id: int) -> NestedGridEdgeAssignment: ...
    def IndexOf(self, value: NestedGridEdgeAssignment) -> int: ...
    def Insert(self, index: int, value: NestedGridEdgeAssignment) -> None: ...
    def Remove(self, value: NestedGridEdgeAssignment) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class NestedGridBoundaryEdgeComponentCollection:
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridBoundaryEdgeComponentCollection"""
    def __init__(self, *args) -> None: ...
    Item: NestedGridEdgeDefinition
    Count: int
    def Add(self, value: NestedGridEdgeDefinition) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: NestedGridEdgeDefinition) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetId(self, id: int) -> NestedGridEdgeDefinition: ...
    def IndexOf(self, value: NestedGridEdgeDefinition) -> int: ...
    def Insert(self, index: int, value: NestedGridEdgeDefinition) -> None: ...
    def Remove(self, value: NestedGridEdgeDefinition) -> None: ...
    def RemoveAt(self, index: int) -> None: ...
    def RemoveId(self, id: int) -> None: ...

class NestedGridCellAssignment(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridCellAssignment"""
    def __init__(self, *args) -> None: ...
    ParentGrid: GridAssemblyDefinition
    IsVoid: bool
    Id: int
    CellSpecifier: IndexSpecifier
    NestedGridDefinition: NestedGridDefinition
    InfillDefinitionId: int
    Name: str
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetVoid(self, ) -> None: ...

class NestedGridCellAssignmentCollection:
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridCellAssignmentCollection"""
    def __init__(self, *args) -> None: ...
    Default: NestedGridCellAssignment
    Item: NestedGridCellAssignment
    Count: int
    def Add(self, value: NestedGridCellAssignment) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: NestedGridCellAssignment) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetId(self, id: int) -> NestedGridCellAssignment: ...
    def IndexOf(self, value: NestedGridCellAssignment) -> int: ...
    def Insert(self, index: int, value: NestedGridCellAssignment) -> None: ...
    def Remove(self, value: NestedGridCellAssignment) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class NestedGridCellMergeData(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridCellMergeData"""
    def __init__(self, *args) -> None: ...
    IsStyleBased: bool
    SecondaryCellPath: IntegerCollection
    PrimaryCellPath: IntegerCollection
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class NestedGridCellMergeDataCollection:
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridCellMergeDataCollection"""
    def __init__(self, *args) -> None: ...
    Item: NestedGridCellMergeData
    Count: int
    def Add(self, value: NestedGridCellMergeData) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: NestedGridCellMergeData) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: NestedGridCellMergeData) -> int: ...
    def Insert(self, index: int, value: NestedGridCellMergeData) -> None: ...
    def Remove(self, value: NestedGridCellMergeData) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class NestedGridCellOverride(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridCellOverride"""
    def __init__(self, *args) -> None: ...
    FrameRemovedLeft: bool
    FrameRemovedRight: bool
    FrameRemovedBottom: bool
    FrameRemovedTop: bool
    IsStyleBased: bool
    IsVoid: bool
    InfillDefinitionId: int
    CellPath: IntegerCollection
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetVoid(self, ) -> None: ...

class NestedGridCellOverrideCollection:
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridCellOverrideCollection"""
    def __init__(self, *args) -> None: ...
    Item: NestedGridCellOverride
    Count: int
    def Add(self, value: NestedGridCellOverride) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: NestedGridCellOverride) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: NestedGridCellOverride) -> int: ...
    def Insert(self, index: int, value: NestedGridCellOverride) -> None: ...
    def Remove(self, value: NestedGridCellOverride) -> None: ...
    def RemoveAt(self, index: int) -> None: ...
    def RemoveEntity(self, objectId: ObjectId) -> None: ...

class NestedGridDefinition(GridAssemblyDefinition):
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridDefinition"""
    def __init__(self, *args) -> None: ...
    GridDivisionId: int
    Name: str
    SpecificCellAssignments: NestedGridCellAssignmentCollection
    SpecificInteriorEdgeAssignments: NestedGridInteriorEdgeAssignmentCollection
    SpecificBoundaryEdgeAssignments: NestedGridBoundaryEdgeAssignmentCollection
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class NestedGridDivision(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridDivision"""
    def __init__(self, *args) -> None: ...
    EndOffset: float
    StartOffset: float
    Name: str
    Id: int
    DivisionDirection: DivisionDirection
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetEdgePositions(self, startPosition: float, endPosition: float, edgePositions: DoubleCollection, baseCurveRadius: float, gridAssembly: GridAssembly) -> None: ...

class NestedGridDivisionComponentCollection:
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridDivisionComponentCollection"""
    def __init__(self, *args) -> None: ...
    Item: NestedGridDivision
    Count: int
    def Add(self, value: NestedGridDivision) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: NestedGridDivision) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetId(self, id: int) -> NestedGridDivision: ...
    def IndexOf(self, value: NestedGridDivision) -> int: ...
    def Insert(self, index: int, value: NestedGridDivision) -> None: ...
    def Remove(self, value: NestedGridDivision) -> None: ...
    def RemoveAt(self, index: int) -> None: ...
    def RemoveId(self, id: int) -> None: ...
    def ReplaceAt(self, index: int, value: NestedGridDivision) -> None: ...

class NestedGridDivisionDivideBy(NestedGridDivision):
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridDivisionDivideBy"""
    def __init__(self, *args) -> None: ...
    DivideByCount: int
    EndOffset: float
    StartOffset: float
    Name: str
    Id: int
    DivisionDirection: DivisionDirection
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class NestedGridDivisionManual(NestedGridDivision):
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridDivisionManual"""
    def __init__(self, *args) -> None: ...
    ManualEdgeDefinitionCount: int
    EndOffset: float
    StartOffset: float
    Name: str
    Id: int
    DivisionDirection: DivisionDirection
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddManualEdgeDefinition(self, edgeDefinition: NestedGridDivisionManualEdgeDefinition) -> None: ...
    def ManualEdgeDefinitionAt(self, index: int) -> NestedGridDivisionManualEdgeDefinition: ...
    def RemoveManualEdgeDefinitionAt(self, index: int) -> None: ...

class NestedGridDivisionManualEdgeDefinition(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridDivisionManualEdgeDefinition"""
    def __init__(self, *args) -> None: ...
    Offset: float
    AxisReference: AxisReference
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CopyFrom(self, other: RXObject) -> None: ...

class NestedGridDivisionOverride(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridDivisionOverride"""
    def __init__(self, *args) -> None: ...
    IsStyleBased: bool
    DivisionDefinitionId: int
    GridAssignmentId: int
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class NestedGridDivisionOverrideCollection:
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridDivisionOverrideCollection"""
    def __init__(self, *args) -> None: ...
    Item: NestedGridDivisionOverride
    Count: int
    def Add(self, value: NestedGridDivisionOverride) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: NestedGridDivisionOverride) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: NestedGridDivisionOverride) -> int: ...
    def Insert(self, index: int, value: NestedGridDivisionOverride) -> None: ...
    def Remove(self, value: NestedGridDivisionOverride) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class NestedGridDivisionRepeat(NestedGridDivision):
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridDivisionRepeat"""
    def __init__(self, *args) -> None: ...
    DistributionFlags: DistributionFlags
    DistributeSlack: bool
    CellSize: float
    EndOffset: float
    StartOffset: float
    Name: str
    Id: int
    DivisionDirection: DivisionDirection
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class NestedGridEdgeAssignment(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridEdgeAssignment"""
    def __init__(self, *args) -> None: ...
    ParentGrid: GridAssemblyDefinition
    EdgeDefinitionId: int
    IsVoid: bool
    Id: int
    EdgeSpecifier: IndexSpecifier
    Name: str
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetVoid(self, ) -> None: ...

class NestedGridEdgeDefinition(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridEdgeDefinition"""
    def __init__(self, *args) -> None: ...
    MaterialId: ObjectId
    ProfileRotation: float
    MirrorProfileY: bool
    MirrorProfileX: bool
    CleanupInternalEdges: bool
    ScaleProfileY: bool
    ScaleProfileX: bool
    ProfileId: ObjectId
    EndOffset: float
    StartOffset: float
    DepthOffset: float
    EdgeOffset: float
    EdgeDepth: float
    EdgeWidth: float
    Name: str
    Id: int
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class NestedGridEdgeOverride(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridEdgeOverride"""
    def __init__(self, *args) -> None: ...
    IsStyleBased: bool
    IsVoid: bool
    EdgeDefinitionId: int
    EdgePath: IntegerCollection
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CopyFrom(self, other: RXObject) -> None: ...
    def SetVoid(self, ) -> None: ...

class NestedGridEdgeOverrideCollection:
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridEdgeOverrideCollection"""
    def __init__(self, *args) -> None: ...
    Item: NestedGridEdgeOverride
    Count: int
    def Add(self, value: NestedGridEdgeOverride) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: NestedGridEdgeOverride) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: NestedGridEdgeOverride) -> int: ...
    def Insert(self, index: int, value: NestedGridEdgeOverride) -> None: ...
    def Remove(self, value: NestedGridEdgeOverride) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class NestedGridEdgeProfileOverride(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridEdgeProfileOverride"""
    def __init__(self, *args) -> None: ...
    IsStyleBased: bool
    ProfileId: ObjectId
    EdgePath: IntegerCollection
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CopyFrom(self, other: RXObject) -> None: ...

class NestedGridEdgeProfileOverrideCollection:
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridEdgeProfileOverrideCollection"""
    def __init__(self, *args) -> None: ...
    Item: NestedGridEdgeProfileOverride
    Count: int
    def Add(self, value: NestedGridEdgeProfileOverride) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: NestedGridEdgeProfileOverride) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: NestedGridEdgeProfileOverride) -> int: ...
    def Insert(self, index: int, value: NestedGridEdgeProfileOverride) -> None: ...
    def Remove(self, value: NestedGridEdgeProfileOverride) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class NestedGridInfillComponentCollection:
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridInfillComponentCollection"""
    def __init__(self, *args) -> None: ...
    Item: NestedGridInfillDefinition
    Count: int
    def Add(self, value: NestedGridInfillDefinition) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: NestedGridInfillDefinition) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetId(self, id: int) -> NestedGridInfillDefinition: ...
    def IndexOf(self, value: NestedGridInfillDefinition) -> int: ...
    def Insert(self, index: int, value: NestedGridInfillDefinition) -> None: ...
    def Remove(self, value: NestedGridInfillDefinition) -> None: ...
    def RemoveAt(self, index: int) -> None: ...
    def RemoveId(self, id: int) -> None: ...

class NestedGridInfillDefinition(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridInfillDefinition"""
    def __init__(self, *args) -> None: ...
    MaterialId: ObjectId
    SupportsMaterials: bool
    YAlignment: YAlignment
    YOffset: float
    RightOffset: float
    LeftOffset: float
    SupportsMitre: bool
    Name: str
    Id: int
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetOrientation(self, flipX: bool, flipY: bool, flipZ: bool) -> None: ...
    def ManageAnchoredEntity(self, entity: ObjectId, cell: GridAssemblyCell, context: AnchorContext, styleWasChanged: bool) -> None: ...
    def SetOrientation(self, flipX: bool, flipY: bool, flipZ: bool) -> None: ...

class NestedGridInteriorEdgeAssignmentCollection:
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridInteriorEdgeAssignmentCollection"""
    def __init__(self, *args) -> None: ...
    Default: NestedGridEdgeAssignment
    Item: NestedGridEdgeAssignment
    Count: int
    def Add(self, value: NestedGridEdgeAssignment) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: NestedGridEdgeAssignment) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetId(self, id: int) -> NestedGridEdgeAssignment: ...
    def IndexOf(self, value: NestedGridEdgeAssignment) -> int: ...
    def Insert(self, index: int, value: NestedGridEdgeAssignment) -> None: ...
    def Remove(self, value: NestedGridEdgeAssignment) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class NestedGridInteriorEdgeComponentCollection:
    """.NET: Autodesk.Aec.DatabaseServices.NestedGridInteriorEdgeComponentCollection"""
    def __init__(self, *args) -> None: ...
    Item: NestedGridEdgeDefinition
    Count: int
    def Add(self, value: NestedGridEdgeDefinition) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: NestedGridEdgeDefinition) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetId(self, id: int) -> NestedGridEdgeDefinition: ...
    def IndexOf(self, value: NestedGridEdgeDefinition) -> int: ...
    def Insert(self, index: int, value: NestedGridEdgeDefinition) -> None: ...
    def Remove(self, value: NestedGridEdgeDefinition) -> None: ...
    def RemoveAt(self, index: int) -> None: ...
    def RemoveId(self, id: int) -> None: ...

class NodeInformation:
    """.NET: Autodesk.Aec.DatabaseServices.NodeInformation"""
    def __init__(self, *args) -> None: ...
    ...

class NodeLocationType:
    """.NET enum: Autodesk.Aec.DatabaseServices.NodeLocationType"""
    def __init__(self, *args) -> None: ...
    Start: int  # = 0
    End: int  # = 1
    Intersection: int  # = 2
class NodeLoopType:
    """.NET enum: Autodesk.Aec.DatabaseServices.NodeLoopType"""
    def __init__(self, *args) -> None: ...
    Void: int  # = 0
    NonVoid: int  # = 1
class ObjectId(DisposableWrapper):
    """.NET: Autodesk.Aec.DatabaseServices.ObjectId"""
    def __init__(self, *args) -> None: ...
    WorldToModelTransform: Matrix3d
    ModelToWorldTransform: Matrix3d
    BlockRefPath: ObjectIdCollection
    Id: ObjectId
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Clone(self, ) -> object: ...
    @staticmethod
    def Create(unmanagedPointer: IntPtr, autoDelete: bool) -> ObjectId: ...
    @staticmethod
    def Equals(objId1: ObjectId, objId2: ObjectId) -> bool: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class ObjectIdAndBlockReferencePath:
    """.NET: Autodesk.Aec.DatabaseServices.ObjectIdAndBlockReferencePath"""
    def __init__(self, *args) -> None: ...
    BlockReferencePath: ObjectIdCollection
    Id: ObjectId

class ObjectIdAndBlockReferencePathCollection(DisposableWrapper):
    """.NET: Autodesk.Aec.DatabaseServices.ObjectIdAndBlockReferencePathCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: ObjectIdAndBlockReferencePath
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, ObjectIdAndBlockReferencePath: ObjectIdAndBlockReferencePath, bypassCheck: bool) -> int: ...
    def Append(self, containerToAppend: ObjectIdAndBlockReferencePathCollection, bypassCheck: bool) -> None: ...
    def Clear(self, ) -> None: ...
    def Contains(self, ObjectIdAndBlockReferencePath: ObjectIdAndBlockReferencePath) -> bool: ...
    @staticmethod
    def Create(unmanagedPointer: IntPtr, autoDelete: bool) -> ObjectIdAndBlockReferencePathCollection: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, ObjectIdAndBlockReferencePath: ObjectIdAndBlockReferencePath) -> int: ...
    def Remove(self, ObjectIdAndBlockReferencePath: ObjectIdAndBlockReferencePath) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class ObjectIdCollection(DisposableWrapper):
    """.NET: Autodesk.Aec.DatabaseServices.ObjectIdCollection"""
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

class Operation:
    """.NET enum: Autodesk.Aec.DatabaseServices.Operation"""
    def __init__(self, *args) -> None: ...
    Additive: int  # = 0
    Subtractive: int  # = 1
    Intersect: int  # = 2
    Combine: int  # = 3
    Unknown: int  # = -1
class Override(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.Override"""
    def __init__(self, *args) -> None: ...
    ExtensionDictionaryName: str
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def AddToOverrideExtensionDictionaryAndClose(objectToSetOn: DBObject, newObjectToAdd: DBObject) -> ObjectId: ...

class OverrideCollection:
    """.NET: Autodesk.Aec.DatabaseServices.OverrideCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: Override
    def Add(self, value: Override) -> int: ...
    def Clear(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def RemoveAt(self, index: int) -> None: ...

class OverrideDisplayProperties(Override):
    """.NET: Autodesk.Aec.DatabaseServices.OverrideDisplayProperties"""
    def __init__(self, *args) -> None: ...
    DisplayPropertyId: ObjectId
    ViewId: ObjectId
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def VerifyReferences(self, fullCheck: bool) -> int: ...

class OverrideMask(Override):
    """.NET: Autodesk.Aec.DatabaseServices.OverrideMask"""
    def __init__(self, *args) -> None: ...
    ViewId: ObjectId
    MaskId: ObjectId
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class OverrideMaterialAssignment(Override):
    """.NET: Autodesk.Aec.DatabaseServices.OverrideMaterialAssignment"""
    def __init__(self, *args) -> None: ...
    LocationId: int
    ComponentId: int
    MaterialId: ObjectId
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ParameterChangeListenerManager:
    """.NET: Autodesk.Aec.DatabaseServices.ParameterChangeListenerManager"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def RegisterListener(pListener: Listener) -> None: ...
    @staticmethod
    def UnRegisterListener(pListener: Listener) -> None: ...

class PlaneType:
    """.NET enum: Autodesk.Aec.DatabaseServices.PlaneType"""
    def __init__(self, *args) -> None: ...
    UV: int  # = 0
    UW: int  # = 1
    VW: int  # = 2
class Polygon(CellLayoutTool):
    """.NET: Autodesk.Aec.DatabaseServices.Polygon"""
    def __init__(self, *args) -> None: ...
    HasHiddenEdge: bool
    InfillPerimeter: float
    EdgePerimeter: float
    InfillArea: float
    GrossArea: float
    LayoutCellIds: IntegerCollection
    LayoutNodeIds: IntegerCollection
    IsAnchored: bool
    AnchorId: ObjectId
    CanBeAnchored: bool
    GeoEcsIsDirty: bool
    GeoEcs: Matrix3d
    ZDir: Vector3d
    YDir: Vector3d
    XDir: Vector3d
    Normal: Vector3d
    Rotation: float
    Direction: Vector3d
    Location: Point3d
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    StyleId: ObjectId
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    Description: str
    TypeIcon: Icon
    DisplayName: str
    Overrides: OverrideCollection
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
    def AddEcsVertex(self, point2d: Point2d) -> None: ...
    def AddVertex(self, point3d: Point3d) -> None: ...
    def RemoveEcsVertex(self, point2d: Point2d) -> None: ...
    def RemoveVertex(self, point3d: Point3d) -> None: ...
    def SetEcsVertices(self, points: Point2dCollection) -> None: ...
    def SetVertices(self, points: Point3dCollection, plane: Plane) -> None: ...

class PolygonStyle(DictionaryRecord):
    """.NET: Autodesk.Aec.DatabaseServices.PolygonStyle"""
    def __init__(self, *args) -> None: ...
    EdgeWidthJustifyType: PolygonStyleEdgeWidthJustify
    EdgeWidth: float
    Translator: DictionaryRecordNameTranslator
    Classifications: ClassificationCollection
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    KeynoteValue: str
    Keynote: str
    IsLocked: bool
    AlternateName: str
    LocalizedName: str
    Name: str
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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

class PolygonStyleEdgeWidthJustify:
    """.NET enum: Autodesk.Aec.DatabaseServices.PolygonStyleEdgeWidthJustify"""
    def __init__(self, *args) -> None: ...
    In: int  # = 0
    Center: int  # = 1
    Out: int  # = 2
class ProfileDefinition(DictionaryRecord):
    """.NET: Autodesk.Aec.DatabaseServices.ProfileDefinition"""
    def __init__(self, *args) -> None: ...
    ExtrusionDirection: ProfileExtrusionDirection
    InsertionPoint: Point2d
    Profile: Profile
    Translator: DictionaryRecordNameTranslator
    Classifications: ClassificationCollection
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    KeynoteValue: str
    Keynote: str
    IsLocked: bool
    AlternateName: str
    LocalizedName: str
    Name: str
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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
    def CalculateSegmentPositions(self, direction: ProfileExtrusionDirection) -> None: ...
    def ModifySegmentPositions(self, oldDirection: ProfileExtrusionDirection, newDirection: ProfileExtrusionDirection) -> None: ...
    def SetProfile(self, profileToCopy: Profile, translateInsertion: bool, insertionPoint: Point2d) -> None: ...

class ProjectState:
    """.NET enum: Autodesk.Aec.DatabaseServices.ProjectState"""
    def __init__(self, *args) -> None: ...
    New: int  # = 0
    Existing: int  # = 1
    Demolition: int  # = 2
class PropertyBase(RXObject):
    """.NET: Autodesk.Aec.DatabaseServices.PropertyBase"""
    def __init__(self, *args) -> None: ...
    Name: str
    DataType: PropertyDataType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PropertyDataType:
    """.NET enum: Autodesk.Aec.DatabaseServices.PropertyDataType"""
    def __init__(self, *args) -> None: ...
    kBoolean: int  # = 0
    kInteger: int  # = 1
    kReal: int  # = 2
    kString: int  # = 3
    kDistance: int  # = 4
    kArea: int  # = 5
    kAngle: int  # = 6
    kVolume: int  # = 7
    kSymbolId: int  # = 8
class RXClassToObjectId:
    """.NET: Autodesk.Aec.DatabaseServices.RXClassToObjectId"""
    def __init__(self, *args) -> None: ...
    Ids: ObjectIdCollection
    Type: RXClass

class RXClassToObjectIdCollection(DisposableWrapper):
    """.NET: Autodesk.Aec.DatabaseServices.RXClassToObjectIdCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: RXClassToObjectId
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, item: RXClassToObjectId) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, item: RXClassToObjectId) -> bool: ...
    def CopyTo(self, array: list, start: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, item: RXClassToObjectId) -> int: ...
    def Insert(self, index: int, item: RXClassToObjectId) -> None: ...
    def Lookup(self, type: RXClass) -> ObjectIdCollection: ...
    def Remove(self, item: RXClassToObjectId) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class ReferenceDocument(DBObject):
    """.NET: Autodesk.Aec.DatabaseServices.ReferenceDocument"""
    def __init__(self, *args) -> None: ...
    ExtensionDictionaryName: str
    FileFullPath: str
    FilePath: str
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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

class RelationType:
    """.NET enum: Autodesk.Aec.DatabaseServices.RelationType"""
    def __init__(self, *args) -> None: ...
    DisplayReferenceOf: int  # = 0
    DisplayReferenceFor: int  # = 1
    LocationReferenceOf: int  # = 2
    LocationReferenceFor: int  # = 3
    OwnerOf: int  # = 4
    OwnedBy: int  # = 5
    TwoWayReference: int  # = 6
    NotApplicable: int  # = -1
class RenderModeType:
    """.NET enum: Autodesk.Aec.DatabaseServices.RenderModeType"""
    def __init__(self, *args) -> None: ...
    WireFrame: int  # = 0
    Shade: int  # = 1
    Explode: int  # = 2
class ResolvedMaterial:
    """.NET: Autodesk.Aec.DatabaseServices.ResolvedMaterial"""
    def __init__(self, *args) -> None: ...
    IsOverride: bool
    StyleName: str
    StyleClassName: str
    EntityClassName: str
    ComponentName: str
    ComponentId: int
    MaterialId: ObjectId

class ResolvedMaterialCollection(List):
    """.NET: Autodesk.Aec.DatabaseServices.ResolvedMaterialCollection"""
    def __init__(self, *args) -> None: ...
    Capacity: int
    Count: int
    Item: ResolvedMaterial

class RotationType:
    """.NET enum: Autodesk.Aec.DatabaseServices.RotationType"""
    def __init__(self, *args) -> None: ...
    CellRotationHorizontal: int  # = 0
    CellRotationVertical: int  # = 1
class Section2d(Geo):
    """.NET: Autodesk.Aec.DatabaseServices.Section2d"""
    def __init__(self, *args) -> None: ...
    HatchRegionsCount: int
    HasObjectDisplayPropertyInformation: bool
    HasUserEdits: bool
    HatchRegions: Section2dHatchRegionCollection
    ShrinkWrapProfile: Profile
    MainSectionId: ObjectId
    ClipVolumeId: ObjectId
    ShrinkWrapSegmentGroup: Section2dSegmentGroup
    SegmentGroups: Section2dSegmentGroupCollection
    Segments: SectionSegmentCollection
    Vertices: SectionVertexCollection
    SingleSegmentId: int
    SingleSegment: SectionSegment
    IsSingleSegment: bool
    IsSavedEdits: bool
    IsAnchored: bool
    AnchorId: ObjectId
    CanBeAnchored: bool
    GeoEcsIsDirty: bool
    GeoEcs: Matrix3d
    ZDir: Vector3d
    YDir: Vector3d
    XDir: Vector3d
    Normal: Vector3d
    Rotation: float
    Direction: Vector3d
    Location: Point3d
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    StyleId: ObjectId
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    Description: str
    TypeIcon: Icon
    DisplayName: str
    Overrides: OverrideCollection
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
    def HasAssociatedModelSpaceView(self, viewTableRecordId: ObjectId) -> bool: ...
    def IntegrateLineWork(self, startPoint: Point2d, endPoint: Point2d, materialId: ObjectId, componentType: ComponentType, userComponentId: int, lineWorkType: LineWorkType, isManual: bool, isEdit: bool) -> None: ...
    def MergeLineWork(self, startPoint: Point2d, endPoint: Point2d, componentId: int, materialId: ObjectId, lineWorkType: LineWorkType, mergeExactOnly: bool) -> None: ...
    def MergeSection2d(self, section: Section2d, doComponentEdits: bool, doMergeEdits: bool, removeSegments: bool) -> None: ...
    def RemoveAllButUserEdits(self, ) -> None: ...
    def RemoveAllLineWork(self, ) -> None: ...
    def RemoveObjectPropertyDependencies(self, ) -> None: ...
    def SaveEditInPlaceChanges(self, ) -> None: ...
    def SetAssociatedModelSpaceView(self, viewTableRecord: ViewTableRecord) -> None: ...
    def SetIsSingleSegment(self, value: bool, segmentId: int) -> None: ...

class Section2dHatchRegion(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.Section2dHatchRegion"""
    def __init__(self, *args) -> None: ...
    IsSubtractive: bool
    AppliesToShrinkWrapHatch: bool
    AppliesToShrinkWrapLineWork: bool
    AppliesToMaterialLineWork: bool
    AppliesToSectionHatch: bool
    AppliesToSurfaceHatch: bool
    Id: int
    MaterialFilter: ObjectIdCollection
    HasMaterialFilter: bool
    HatchProfile: Profile
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Section2dHatchRegionCollection:
    """.NET: Autodesk.Aec.DatabaseServices.Section2dHatchRegionCollection"""
    def __init__(self, *args) -> None: ...
    Item: Section2dHatchRegion
    Count: int
    def Add(self, value: Section2dHatchRegion) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: Section2dHatchRegion) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: Section2dHatchRegion) -> int: ...
    def Insert(self, index: int, value: Section2dHatchRegion) -> None: ...
    def Remove(self, value: Section2dHatchRegion) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class Section2dSegmentGroup(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.Section2dSegmentGroup"""
    def __init__(self, *args) -> None: ...
    HasUserEdits: bool
    LineWorkSegments: SectionSegmentCollection
    SectionHatchingSegments: SectionSegmentCollection
    SurfaceHatchingSegments: SectionSegmentCollection
    MaterialId: ObjectId
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def RemoveAllButUserEdits(self, ) -> None: ...

class Section2dSegmentGroupCollection:
    """.NET: Autodesk.Aec.DatabaseServices.Section2dSegmentGroupCollection"""
    def __init__(self, *args) -> None: ...
    Item: Section2dSegmentGroup
    Count: int
    def Add(self, value: Section2dSegmentGroup) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: Section2dSegmentGroup) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: Section2dSegmentGroup) -> int: ...
    def Insert(self, index: int, value: Section2dSegmentGroup) -> None: ...
    def Remove(self, value: Section2dSegmentGroup) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class Section2dStyle(DictionaryRecord):
    """.NET: Autodesk.Aec.DatabaseServices.Section2dStyle"""
    def __init__(self, *args) -> None: ...
    KeepAllHiddenLineWork: bool
    LineWorkRules: LineWorkRuleCollection
    LineWorkComponents: LineWorkComponentCollection
    UseObjectDisplayProperty: bool
    Translator: DictionaryRecordNameTranslator
    Classifications: ClassificationCollection
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    KeynoteValue: str
    Keynote: str
    IsLocked: bool
    AlternateName: str
    LocalizedName: str
    Name: str
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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

class Section2dStyleParameter:
    """.NET enum: Autodesk.Aec.DatabaseServices.Section2dStyleParameter"""
    def __init__(self, *args) -> None: ...
    Component: int  # = 0
    LineWorkRule: int  # = 1
    KeepHiddenLineWork: int  # = 2
    UseObjectDisplayProperties: int  # = 3
class SectionSegment(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.SectionSegment"""
    def __init__(self, *args) -> None: ...
    LineWorkType: LineWorkType
    EndPoint: Point2d
    StartPoint: Point2d
    ComponentId: int
    IsAPoint: bool
    MarkedFromEdit: bool
    IsMergedSegment: bool
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SectionSegmentCollection:
    """.NET: Autodesk.Aec.DatabaseServices.SectionSegmentCollection"""
    def __init__(self, *args) -> None: ...
    Item: SectionSegment
    Count: int
    def Add(self, value: SectionSegment) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: SectionSegment) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: SectionSegment) -> int: ...
    def Insert(self, index: int, value: SectionSegment) -> None: ...
    def Remove(self, value: SectionSegment) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class SectionVertex(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.SectionVertex"""
    def __init__(self, *args) -> None: ...
    Location: Point2d
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SectionVertexCollection:
    """.NET: Autodesk.Aec.DatabaseServices.SectionVertexCollection"""
    def __init__(self, *args) -> None: ...
    Item: SectionVertex
    Count: int
    def Add(self, value: SectionVertex) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: SectionVertex) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: SectionVertex) -> int: ...
    def Insert(self, index: int, value: SectionVertex) -> None: ...
    def Remove(self, value: SectionVertex) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class ShapeSubType:
    """.NET enum: Autodesk.Aec.DatabaseServices.ShapeSubType"""
    def __init__(self, *args) -> None: ...
    ProfileInternal: int  # = 0
    ProfileExternal: int  # = 1
    Unspecified: int  # = -1
class ShapeType:
    """.NET enum: Autodesk.Aec.DatabaseServices.ShapeType"""
    def __init__(self, *args) -> None: ...
    Box: int  # = 0
    Arch: int  # = 1
    BarrelVault: int  # = 2
    Doric: int  # = 3
    Cone: int  # = 4
    Cylinder: int  # = 5
    Dome: int  # = 6
    Gable: int  # = 7
    IsoscelesTriangle: int  # = 8
    RightTriangle: int  # = 9
    Pyramid: int  # = 10
    Sphere: int  # = 11
    Extrusion: int  # = 12
    Revolution: int  # = 13
    BoundaryRepresentation: int  # = 14
    Unknown: int  # = -2
    Error: int  # = -1
class SkipPushPopDisplayPropertiesType:
    """.NET enum: Autodesk.Aec.DatabaseServices.SkipPushPopDisplayPropertiesType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Color: int  # = 1
    Layer: int  # = 2
    LineType: int  # = 4
    LineWeight: int  # = 8
    LineTypeScale: int  # = 16
    PlotStyle: int  # = 32
    VisualStyle: int  # = 64
    AutoCADRenderMaterial: int  # = 128
class Slice(LayoutTool):
    """.NET: Autodesk.Aec.DatabaseServices.Slice"""
    def __init__(self, *args) -> None: ...
    Profile: Profile
    PlaneDepth: float
    PlaneWidth: float
    LayoutNodeIds: IntegerCollection
    IsAnchored: bool
    AnchorId: ObjectId
    CanBeAnchored: bool
    GeoEcsIsDirty: bool
    GeoEcs: Matrix3d
    ZDir: Vector3d
    YDir: Vector3d
    XDir: Vector3d
    Normal: Vector3d
    Rotation: float
    Direction: Vector3d
    Location: Point3d
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    StyleId: ObjectId
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    Description: str
    TypeIcon: Icon
    DisplayName: str
    Overrides: OverrideCollection
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
    def AppendObject(self, objectId: ObjectId) -> None: ...
    def GetEntities(self, ) -> ObjectIdCollection: ...
    def RemoveObject(self, objectId: ObjectId) -> None: ...

class StandardDisplaySetType:
    """.NET enum: Autodesk.Aec.DatabaseServices.StandardDisplaySetType"""
    def __init__(self, *args) -> None: ...
    NotStandard: int  # = 0
    Standard: int  # = 1
    Model: int  # = 3
    Plan: int  # = 5
    Reflected: int  # = 9
    NumberOfStandardSets: int  # = 9
    Section: int  # = 17
    PlanLowDetail: int  # = 33
    PlanHighDetail: int  # = 65
    ModelLowDetail: int  # = 129
    ModelHighDetail: int  # = 131
class StreamAcad(RXObject):
    """.NET: Autodesk.Aec.DatabaseServices.StreamAcad"""
    def __init__(self, *args) -> None: ...
    UseBodyInternalDeviation: bool
    EnablePushPopXform: bool
    IgnoreLiveSections: bool
    IndependentLayerOffControl: bool
    ResolveByLayerTraits: bool
    ResolveByBlockTraits: bool
    FilterFrozenLayers: bool
    FilterOffLayers: bool
    AttenuateColor: bool
    SuppressShellAndMeshExtendedData: bool
    UseLayerPropertyOverridePerViewportIfExists: bool
    SkipPushPopDisplayPropertiesFlags: int
    GsMarkersValid: bool
    AnnotationScale: AnnotationScale
    ViewportId: ObjectId
    AutoCADRenderMaterial: ObjectId
    VisualStyle: ObjectId
    InverseInsertXform: Matrix3d
    CurrentInsertXform: Matrix3d
    InverseSubObjectXform: Matrix3d
    CurrentSubObjectXform: Matrix3d
    Material: MaterialDefinition
    LineTypeScale: float
    LineWeight: LineWeight
    Scale: Scale3d
    IsUniScaled: bool
    IsScaled: bool
    IsXform: bool
    InverseXform: Matrix3d
    CurrentXform: Matrix3d
    LiveSectionRequired: bool
    MaskingRequired: bool
    DisplayDirection: Vector3d
    DisplaySetId: ObjectId
    CurrentGsMarkerInfoTree: GsMarkerInformationTree
    CurrentEntityDrawData: GraphicsSystemEntityDrawData
    Entity: DBObject
    GsMarker: IntPtr
    BodyFaceColorMode: StreamBodyColorModeType
    BodyEdgeColorMode: StreamBodyColorModeType
    RenderMode: RenderModeType
    FillType: FillType
    Linetype: ObjectId
    TrueColor: Color
    ColorIndex: int
    AlwaysResolveByLayerPlotStyles: bool
    IsPerspectiveView: bool
    BackfaceCullSurfaceHatching: bool
    ApplySurfaceHatching: bool
    Layer: ObjectId
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddToSkipPushPopDisplayPropertiesFlags(self, newDisplayPropertiesToSkipFlagsToAdd: int) -> None: ...
    def AlreadyDrawing(self, object: DBObject) -> bool: ...
    def GetPlotStyleId(self, ) -> ObjectId: ...
    def GetPlotStyleNameType(self, ) -> PlotStyleNameType: ...
    def IsVisible(self, properties: DisplayComponentEntity) -> bool: ...
    def PopAutoCADRenderMaterial(self, ) -> None: ...
    def PopBodyEdgeColorMode(self, ) -> None: ...
    def PopBodyFaceColorMode(self, ) -> None: ...
    def PopColor(self, ) -> None: ...
    def PopDisplayDirection(self, ) -> None: ...
    def PopDisplayParameters(self, ) -> None: ...
    def PopEntity(self, ) -> None: ...
    def PopFillType(self, ) -> None: ...
    def PopGsMarker(self, ) -> None: ...
    def PopInsertXform(self, ) -> None: ...
    def PopLayer(self, ) -> None: ...
    def PopLineTypeScale(self, ) -> None: ...
    def PopLineWeight(self, ) -> None: ...
    def PopLinetype(self, ) -> None: ...
    def PopMaterial(self, closeIt: bool) -> None: ...
    def PopPlotStyle(self, ) -> None: ...
    def PopProperties(self, ) -> None: ...
    def PopRenderMode(self, ) -> None: ...
    def PopSubObjectCoordinateSystem(self, ) -> None: ...
    def PopVisualStyle(self, ) -> None: ...
    def PopXform(self, ) -> None: ...
    def PushAutoCADRenderMaterial(self, id: ObjectId) -> None: ...
    def PushBodyEdgeColorMode(self, mode: StreamBodyColorModeType) -> None: ...
    def PushBodyFaceColorMode(self, mode: StreamBodyColorModeType) -> None: ...
    def PushColor(self, trueColor: Color) -> None: ...
    def PushDisplayDirection(self, displayDirection: Vector3d) -> None: ...
    def PushDisplayParameters(self, displayConfigurationId: ObjectId, transaction: Transaction) -> None: ...
    def PushEntity(self, object: DBObject) -> None: ...
    def PushFillType(self, fillType: FillType) -> None: ...
    def PushGsMarker(self, id: IntPtr) -> None: ...
    def PushInsertXform(self, matrix: Matrix3d) -> None: ...
    def PushLayer(self, id: ObjectId) -> None: ...
    def PushLineTypeScale(self, thickness: float) -> None: ...
    def PushLineWeight(self, lineWeight: LineWeight) -> None: ...
    def PushLinetype(self, lineTypeId: ObjectId) -> None: ...
    def PushMaterial(self, materialDefinition: MaterialDefinition) -> None: ...
    def PushPlotStyle(self, type: PlotStyleNameType, id: ObjectId) -> None: ...
    def PushProperties(self, properties: DisplayComponentEntity) -> None: ...
    def PushRenderMode(self, mode: RenderModeType) -> None: ...
    def PushSubObjectCoordinateSystem(self, matrix: Matrix3d) -> None: ...
    def PushVisualStyle(self, id: ObjectId) -> None: ...
    def PushXform(self, matrix: Matrix3d) -> None: ...
    def RemoveFromSkipPushPopDisplayPropertiesFlags(self, newDisplayPropertiesToSkipFlagsToRemove: int) -> None: ...
    def SetSkipPushPopDisplayProperties(self, skip: bool) -> None: ...
    def Stream(self, points: list, closed: bool, intendedType: StreamEntityType, normal: Vector3d) -> None: ...
    def StreamBlock(self, blockRecord: BlockTableRecord, nonDbAttributes: DBObjectCollection) -> None: ...
    def StreamByMaterialHatch(self, ecsToWcs: Matrix3d, hatchInformation: DisplayComponentHatch, materialId: ObjectId, points: list, bulges: list) -> None: ...
    def StreamDrawable(self, drawable: Drawable) -> None: ...
    def StreamHatch(self, ecsToWcs: Matrix3d, hatchInformation: DisplayComponentHatch, points: list, bulges: list) -> None: ...
    def StreamWcs(self, points: list, closed: bool, intendedType: StreamEntityType, normal: Vector3d) -> None: ...
    def StreamWireframeBodyWcs(self, body: Body) -> None: ...

class StreamBodyColorModeType:
    """.NET enum: Autodesk.Aec.DatabaseServices.StreamBodyColorModeType"""
    def __init__(self, *args) -> None: ...
    Ignore: int  # = 0
    UseAsColor: int  # = 1
    UseAsGsMarker: int  # = 2
    UseAsMapIndex: int  # = 3
class StreamCollectBodies(StreamAcad):
    """.NET: Autodesk.Aec.DatabaseServices.StreamCollectBodies"""
    def __init__(self, *args) -> None: ...
    UseBodyInternalDeviation: bool
    EnablePushPopXform: bool
    IgnoreLiveSections: bool
    IndependentLayerOffControl: bool
    ResolveByLayerTraits: bool
    ResolveByBlockTraits: bool
    FilterFrozenLayers: bool
    FilterOffLayers: bool
    AttenuateColor: bool
    SuppressShellAndMeshExtendedData: bool
    UseLayerPropertyOverridePerViewportIfExists: bool
    SkipPushPopDisplayPropertiesFlags: int
    GsMarkersValid: bool
    AnnotationScale: AnnotationScale
    ViewportId: ObjectId
    AutoCADRenderMaterial: ObjectId
    VisualStyle: ObjectId
    InverseInsertXform: Matrix3d
    CurrentInsertXform: Matrix3d
    InverseSubObjectXform: Matrix3d
    CurrentSubObjectXform: Matrix3d
    Material: MaterialDefinition
    LineTypeScale: float
    LineWeight: LineWeight
    Scale: Scale3d
    IsUniScaled: bool
    IsScaled: bool
    IsXform: bool
    InverseXform: Matrix3d
    CurrentXform: Matrix3d
    LiveSectionRequired: bool
    MaskingRequired: bool
    DisplayDirection: Vector3d
    DisplaySetId: ObjectId
    CurrentGsMarkerInfoTree: GsMarkerInformationTree
    CurrentEntityDrawData: GraphicsSystemEntityDrawData
    Entity: DBObject
    GsMarker: IntPtr
    BodyFaceColorMode: StreamBodyColorModeType
    BodyEdgeColorMode: StreamBodyColorModeType
    RenderMode: RenderModeType
    FillType: FillType
    Linetype: ObjectId
    TrueColor: Color
    ColorIndex: int
    AlwaysResolveByLayerPlotStyles: bool
    IsPerspectiveView: bool
    BackfaceCullSurfaceHatching: bool
    ApplySurfaceHatching: bool
    Layer: ObjectId
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetBody(self, ) -> Body: ...
    def GetBodyCopy(self, ) -> Body: ...
    def InitializeBody(self, ) -> None: ...

class StreamCollectClipBodies(StreamAcad):
    """.NET: Autodesk.Aec.DatabaseServices.StreamCollectClipBodies"""
    def __init__(self, *args) -> None: ...
    CalculateShrinkwrap: bool
    ShrinkwrapProfile: Profile
    BackfaceCullSurfaceHatching: bool
    UseBodyInternalDeviation: bool
    EnablePushPopXform: bool
    IgnoreLiveSections: bool
    IndependentLayerOffControl: bool
    ResolveByLayerTraits: bool
    ResolveByBlockTraits: bool
    FilterFrozenLayers: bool
    FilterOffLayers: bool
    AttenuateColor: bool
    SuppressShellAndMeshExtendedData: bool
    UseLayerPropertyOverridePerViewportIfExists: bool
    SkipPushPopDisplayPropertiesFlags: int
    GsMarkersValid: bool
    AnnotationScale: AnnotationScale
    ViewportId: ObjectId
    AutoCADRenderMaterial: ObjectId
    VisualStyle: ObjectId
    InverseInsertXform: Matrix3d
    CurrentInsertXform: Matrix3d
    InverseSubObjectXform: Matrix3d
    CurrentSubObjectXform: Matrix3d
    Material: MaterialDefinition
    LineTypeScale: float
    LineWeight: LineWeight
    Scale: Scale3d
    IsUniScaled: bool
    IsScaled: bool
    IsXform: bool
    InverseXform: Matrix3d
    CurrentXform: Matrix3d
    LiveSectionRequired: bool
    MaskingRequired: bool
    DisplayDirection: Vector3d
    DisplaySetId: ObjectId
    CurrentGsMarkerInfoTree: GsMarkerInformationTree
    CurrentEntityDrawData: GraphicsSystemEntityDrawData
    Entity: DBObject
    GsMarker: IntPtr
    BodyFaceColorMode: StreamBodyColorModeType
    BodyEdgeColorMode: StreamBodyColorModeType
    RenderMode: RenderModeType
    FillType: FillType
    Linetype: ObjectId
    TrueColor: Color
    ColorIndex: int
    AlwaysResolveByLayerPlotStyles: bool
    IsPerspectiveView: bool
    ApplySurfaceHatching: bool
    Layer: ObjectId
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetCollectedGraphics(self, ) -> list: ...
    def SetBodyClipVolume(self, bodyFilter: Body) -> None: ...
    def SetCalculateShrinkwrap(self, value: bool, toShrinkwrapPlane: Matrix3d, continueExistingShrinkwrap: bool) -> None: ...
    def SetRetainBodies(self, value: bool) -> None: ...
    def SetSkipAnnotationObjects(self, value: bool) -> None: ...

class StreamCollectMaterials(StreamAcad):
    """.NET: Autodesk.Aec.DatabaseServices.StreamCollectMaterials"""
    def __init__(self, *args) -> None: ...
    MaterialIds: ObjectIdCollection
    MaterialFilter: ObjectIdCollection
    CombineBodies: bool
    UseBodyInternalDeviation: bool
    EnablePushPopXform: bool
    IgnoreLiveSections: bool
    IndependentLayerOffControl: bool
    ResolveByLayerTraits: bool
    ResolveByBlockTraits: bool
    FilterFrozenLayers: bool
    FilterOffLayers: bool
    AttenuateColor: bool
    SuppressShellAndMeshExtendedData: bool
    UseLayerPropertyOverridePerViewportIfExists: bool
    SkipPushPopDisplayPropertiesFlags: int
    GsMarkersValid: bool
    AnnotationScale: AnnotationScale
    ViewportId: ObjectId
    AutoCADRenderMaterial: ObjectId
    VisualStyle: ObjectId
    InverseInsertXform: Matrix3d
    CurrentInsertXform: Matrix3d
    InverseSubObjectXform: Matrix3d
    CurrentSubObjectXform: Matrix3d
    Material: MaterialDefinition
    LineTypeScale: float
    LineWeight: LineWeight
    Scale: Scale3d
    IsUniScaled: bool
    IsScaled: bool
    IsXform: bool
    InverseXform: Matrix3d
    CurrentXform: Matrix3d
    LiveSectionRequired: bool
    MaskingRequired: bool
    DisplayDirection: Vector3d
    DisplaySetId: ObjectId
    CurrentGsMarkerInfoTree: GsMarkerInformationTree
    CurrentEntityDrawData: GraphicsSystemEntityDrawData
    Entity: DBObject
    GsMarker: IntPtr
    BodyFaceColorMode: StreamBodyColorModeType
    BodyEdgeColorMode: StreamBodyColorModeType
    RenderMode: RenderModeType
    FillType: FillType
    Linetype: ObjectId
    TrueColor: Color
    ColorIndex: int
    AlwaysResolveByLayerPlotStyles: bool
    IsPerspectiveView: bool
    BackfaceCullSurfaceHatching: bool
    ApplySurfaceHatching: bool
    Layer: ObjectId
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetBody(self, materialId: ObjectId) -> Body: ...
    def GetFaceOnPoint(self, wcsPickPoint: Point3d, materialId: ObjectId, flags: SurfaceHatchFlags) -> FaceScanResults: ...
    def GetFaceScanResults(self, ) -> FaceScanResults: ...
    def GetLineworkScanResult(self, ) -> ObjectId: ...
    def GetVolume(self, materialId: ObjectId) -> float: ...
    def ResetBodies(self, ) -> None: ...
    def SetupFaceScan(self, point: Point3d) -> None: ...
    def SetupLineworkScan(self, point: Point3d) -> None: ...

class StreamColorToPropertiesMap(DisposableWrapper):
    """.NET: Autodesk.Aec.DatabaseServices.StreamColorToPropertiesMap"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def DeleteAll(self, ) -> None: ...
    def Lookup(self, key: int) -> DisplayComponentEntity: ...
    def SetAt(self, key: int, value: DisplayComponentEntity, deleteExisting: bool) -> None: ...

class StreamCurves(StreamAcad):
    """.NET: Autodesk.Aec.DatabaseServices.StreamCurves"""
    def __init__(self, *args) -> None: ...
    CollectDisplayPropertiesInfomationFor2dSection: bool
    DisplayComponentEntityArcs: list
    DisplayComponentEntityLines: list
    BackfaceCullSurfaceHatching: bool
    ApplySurfaceHatching: bool
    CollectArcs: bool
    IgnoreHatch: bool
    IgnoreText: bool
    NestedEntityFilter: ObjectIdCollection
    Arcs: list
    Lines: list
    UseBodyInternalDeviation: bool
    EnablePushPopXform: bool
    IgnoreLiveSections: bool
    IndependentLayerOffControl: bool
    ResolveByLayerTraits: bool
    ResolveByBlockTraits: bool
    FilterFrozenLayers: bool
    FilterOffLayers: bool
    AttenuateColor: bool
    SuppressShellAndMeshExtendedData: bool
    UseLayerPropertyOverridePerViewportIfExists: bool
    SkipPushPopDisplayPropertiesFlags: int
    GsMarkersValid: bool
    AnnotationScale: AnnotationScale
    ViewportId: ObjectId
    AutoCADRenderMaterial: ObjectId
    VisualStyle: ObjectId
    InverseInsertXform: Matrix3d
    CurrentInsertXform: Matrix3d
    InverseSubObjectXform: Matrix3d
    CurrentSubObjectXform: Matrix3d
    Material: MaterialDefinition
    LineTypeScale: float
    LineWeight: LineWeight
    Scale: Scale3d
    IsUniScaled: bool
    IsScaled: bool
    IsXform: bool
    InverseXform: Matrix3d
    CurrentXform: Matrix3d
    LiveSectionRequired: bool
    MaskingRequired: bool
    DisplayDirection: Vector3d
    DisplaySetId: ObjectId
    CurrentGsMarkerInfoTree: GsMarkerInformationTree
    CurrentEntityDrawData: GraphicsSystemEntityDrawData
    Entity: DBObject
    GsMarker: IntPtr
    BodyFaceColorMode: StreamBodyColorModeType
    BodyEdgeColorMode: StreamBodyColorModeType
    RenderMode: RenderModeType
    FillType: FillType
    Linetype: ObjectId
    TrueColor: Color
    ColorIndex: int
    AlwaysResolveByLayerPlotStyles: bool
    IsPerspectiveView: bool
    Layer: ObjectId
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CollectDisplayPropertiesForCurves(self, curveIsALine: bool) -> None: ...

class StreamEntityType:
    """.NET enum: Autodesk.Aec.DatabaseServices.StreamEntityType"""
    def __init__(self, *args) -> None: ...
    Pline: int  # = 0
    Line: int  # = 1
    CircularArc: int  # = 2
    EllipticalArc: int  # = 3
    Face: int  # = 4
class StreamExplode(StreamAcad):
    """.NET: Autodesk.Aec.DatabaseServices.StreamExplode"""
    def __init__(self, *args) -> None: ...
    UseFaceAndEdgeParamsWhileDrawingMesh: bool
    IsVisualExplode: bool
    UseBodyInternalDeviation: bool
    EnablePushPopXform: bool
    IgnoreLiveSections: bool
    IndependentLayerOffControl: bool
    ResolveByLayerTraits: bool
    ResolveByBlockTraits: bool
    FilterFrozenLayers: bool
    FilterOffLayers: bool
    AttenuateColor: bool
    SuppressShellAndMeshExtendedData: bool
    UseLayerPropertyOverridePerViewportIfExists: bool
    SkipPushPopDisplayPropertiesFlags: int
    GsMarkersValid: bool
    AnnotationScale: AnnotationScale
    ViewportId: ObjectId
    AutoCADRenderMaterial: ObjectId
    VisualStyle: ObjectId
    InverseInsertXform: Matrix3d
    CurrentInsertXform: Matrix3d
    InverseSubObjectXform: Matrix3d
    CurrentSubObjectXform: Matrix3d
    Material: MaterialDefinition
    LineTypeScale: float
    LineWeight: LineWeight
    Scale: Scale3d
    IsUniScaled: bool
    IsScaled: bool
    IsXform: bool
    InverseXform: Matrix3d
    CurrentXform: Matrix3d
    LiveSectionRequired: bool
    MaskingRequired: bool
    DisplayDirection: Vector3d
    DisplaySetId: ObjectId
    CurrentGsMarkerInfoTree: GsMarkerInformationTree
    CurrentEntityDrawData: GraphicsSystemEntityDrawData
    Entity: DBObject
    GsMarker: IntPtr
    BodyFaceColorMode: StreamBodyColorModeType
    BodyEdgeColorMode: StreamBodyColorModeType
    RenderMode: RenderModeType
    FillType: FillType
    Linetype: ObjectId
    TrueColor: Color
    ColorIndex: int
    AlwaysResolveByLayerPlotStyles: bool
    IsPerspectiveView: bool
    BackfaceCullSurfaceHatching: bool
    ApplySurfaceHatching: bool
    Layer: ObjectId
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddExplodedEntitiesToCurrentSpace(self, ) -> None: ...
    def PackageExplodedEntities(self, ) -> None: ...
    def PackageExplodedEntitiesAndReturnBlockId(self, ) -> ObjectId: ...
    def ResetEntityArrays(self, ) -> None: ...
    def SetForBoundarySearch(self, value: bool) -> None: ...
    def SetLocalTransform(self, matrix: Matrix3d) -> None: ...

class StreamExtent(StreamAcad):
    """.NET: Autodesk.Aec.DatabaseServices.StreamExtent"""
    def __init__(self, *args) -> None: ...
    AllowMText: bool
    TextStrokingStatus: bool
    Extents: BoundBox3d
    UseBodyInternalDeviation: bool
    EnablePushPopXform: bool
    IgnoreLiveSections: bool
    IndependentLayerOffControl: bool
    ResolveByLayerTraits: bool
    ResolveByBlockTraits: bool
    FilterFrozenLayers: bool
    FilterOffLayers: bool
    AttenuateColor: bool
    SuppressShellAndMeshExtendedData: bool
    UseLayerPropertyOverridePerViewportIfExists: bool
    SkipPushPopDisplayPropertiesFlags: int
    GsMarkersValid: bool
    AnnotationScale: AnnotationScale
    ViewportId: ObjectId
    AutoCADRenderMaterial: ObjectId
    VisualStyle: ObjectId
    InverseInsertXform: Matrix3d
    CurrentInsertXform: Matrix3d
    InverseSubObjectXform: Matrix3d
    CurrentSubObjectXform: Matrix3d
    Material: MaterialDefinition
    LineTypeScale: float
    LineWeight: LineWeight
    Scale: Scale3d
    IsUniScaled: bool
    IsScaled: bool
    IsXform: bool
    InverseXform: Matrix3d
    CurrentXform: Matrix3d
    LiveSectionRequired: bool
    MaskingRequired: bool
    DisplayDirection: Vector3d
    DisplaySetId: ObjectId
    CurrentGsMarkerInfoTree: GsMarkerInformationTree
    CurrentEntityDrawData: GraphicsSystemEntityDrawData
    Entity: DBObject
    GsMarker: IntPtr
    BodyFaceColorMode: StreamBodyColorModeType
    BodyEdgeColorMode: StreamBodyColorModeType
    RenderMode: RenderModeType
    FillType: FillType
    Linetype: ObjectId
    TrueColor: Color
    ColorIndex: int
    AlwaysResolveByLayerPlotStyles: bool
    IsPerspectiveView: bool
    BackfaceCullSurfaceHatching: bool
    ApplySurfaceHatching: bool
    Layer: ObjectId
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def PopTextStrokingStatus(self, ) -> None: ...
    def PushTextStrokingStatus(self, isTextStrokingOn: bool) -> None: ...
    def SetIncludeLiveSectionInExtent(self, isInclude: bool) -> None: ...

class StreamIntersect(StreamAcad):
    """.NET: Autodesk.Aec.DatabaseServices.StreamIntersect"""
    def __init__(self, *args) -> None: ...
    GsSelectionMarker: IntPtr
    UseBodyInternalDeviation: bool
    EnablePushPopXform: bool
    IgnoreLiveSections: bool
    IndependentLayerOffControl: bool
    ResolveByLayerTraits: bool
    ResolveByBlockTraits: bool
    FilterFrozenLayers: bool
    FilterOffLayers: bool
    AttenuateColor: bool
    SuppressShellAndMeshExtendedData: bool
    UseLayerPropertyOverridePerViewportIfExists: bool
    SkipPushPopDisplayPropertiesFlags: int
    GsMarkersValid: bool
    AnnotationScale: AnnotationScale
    ViewportId: ObjectId
    AutoCADRenderMaterial: ObjectId
    VisualStyle: ObjectId
    InverseInsertXform: Matrix3d
    CurrentInsertXform: Matrix3d
    InverseSubObjectXform: Matrix3d
    CurrentSubObjectXform: Matrix3d
    Material: MaterialDefinition
    LineTypeScale: float
    LineWeight: LineWeight
    Scale: Scale3d
    IsUniScaled: bool
    IsScaled: bool
    IsXform: bool
    InverseXform: Matrix3d
    CurrentXform: Matrix3d
    LiveSectionRequired: bool
    MaskingRequired: bool
    DisplayDirection: Vector3d
    DisplaySetId: ObjectId
    CurrentGsMarkerInfoTree: GsMarkerInformationTree
    CurrentEntityDrawData: GraphicsSystemEntityDrawData
    Entity: DBObject
    GsMarker: IntPtr
    BodyFaceColorMode: StreamBodyColorModeType
    BodyEdgeColorMode: StreamBodyColorModeType
    RenderMode: RenderModeType
    FillType: FillType
    Linetype: ObjectId
    TrueColor: Color
    ColorIndex: int
    AlwaysResolveByLayerPlotStyles: bool
    IsPerspectiveView: bool
    BackfaceCullSurfaceHatching: bool
    ApplySurfaceHatching: bool
    Layer: ObjectId
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def IntersectWith(self, otherPipe: StreamIntersect, points: Point3dCollection) -> int: ...

class StreamSlice(StreamCollectBodies):
    """.NET: Autodesk.Aec.DatabaseServices.StreamSlice"""
    def __init__(self, *args) -> None: ...
    UseBodyInternalDeviation: bool
    EnablePushPopXform: bool
    IgnoreLiveSections: bool
    IndependentLayerOffControl: bool
    ResolveByLayerTraits: bool
    ResolveByBlockTraits: bool
    FilterFrozenLayers: bool
    FilterOffLayers: bool
    AttenuateColor: bool
    SuppressShellAndMeshExtendedData: bool
    UseLayerPropertyOverridePerViewportIfExists: bool
    SkipPushPopDisplayPropertiesFlags: int
    GsMarkersValid: bool
    AnnotationScale: AnnotationScale
    ViewportId: ObjectId
    AutoCADRenderMaterial: ObjectId
    VisualStyle: ObjectId
    InverseInsertXform: Matrix3d
    CurrentInsertXform: Matrix3d
    InverseSubObjectXform: Matrix3d
    CurrentSubObjectXform: Matrix3d
    Material: MaterialDefinition
    LineTypeScale: float
    LineWeight: LineWeight
    Scale: Scale3d
    IsUniScaled: bool
    IsScaled: bool
    IsXform: bool
    InverseXform: Matrix3d
    CurrentXform: Matrix3d
    LiveSectionRequired: bool
    MaskingRequired: bool
    DisplayDirection: Vector3d
    DisplaySetId: ObjectId
    CurrentGsMarkerInfoTree: GsMarkerInformationTree
    CurrentEntityDrawData: GraphicsSystemEntityDrawData
    Entity: DBObject
    GsMarker: IntPtr
    BodyFaceColorMode: StreamBodyColorModeType
    BodyEdgeColorMode: StreamBodyColorModeType
    RenderMode: RenderModeType
    FillType: FillType
    Linetype: ObjectId
    TrueColor: Color
    ColorIndex: int
    AlwaysResolveByLayerPlotStyles: bool
    IsPerspectiveView: bool
    BackfaceCullSurfaceHatching: bool
    ApplySurfaceHatching: bool
    Layer: ObjectId
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetProfile(self, ) -> Profile: ...
    def SetCopyAttributes(self, yesNo: bool) -> None: ...
    def SetPlane(self, plane: Plane) -> None: ...
    def SetReconstructArcs(self, yesNo: bool) -> None: ...

class StreamVector(StreamAcad):
    """.NET: Autodesk.Aec.DatabaseServices.StreamVector"""
    def __init__(self, *args) -> None: ...
    Lines: list
    BackfaceCullSurfaceHatching: bool
    ApplySurfaceHatching: bool
    UseBodyInternalDeviation: bool
    EnablePushPopXform: bool
    IgnoreLiveSections: bool
    IndependentLayerOffControl: bool
    ResolveByLayerTraits: bool
    ResolveByBlockTraits: bool
    FilterFrozenLayers: bool
    FilterOffLayers: bool
    AttenuateColor: bool
    SuppressShellAndMeshExtendedData: bool
    UseLayerPropertyOverridePerViewportIfExists: bool
    SkipPushPopDisplayPropertiesFlags: int
    GsMarkersValid: bool
    AnnotationScale: AnnotationScale
    ViewportId: ObjectId
    AutoCADRenderMaterial: ObjectId
    VisualStyle: ObjectId
    InverseInsertXform: Matrix3d
    CurrentInsertXform: Matrix3d
    InverseSubObjectXform: Matrix3d
    CurrentSubObjectXform: Matrix3d
    Material: MaterialDefinition
    LineTypeScale: float
    LineWeight: LineWeight
    Scale: Scale3d
    IsUniScaled: bool
    IsScaled: bool
    IsXform: bool
    InverseXform: Matrix3d
    CurrentXform: Matrix3d
    LiveSectionRequired: bool
    MaskingRequired: bool
    DisplayDirection: Vector3d
    DisplaySetId: ObjectId
    CurrentGsMarkerInfoTree: GsMarkerInformationTree
    CurrentEntityDrawData: GraphicsSystemEntityDrawData
    Entity: DBObject
    GsMarker: IntPtr
    BodyFaceColorMode: StreamBodyColorModeType
    BodyEdgeColorMode: StreamBodyColorModeType
    RenderMode: RenderModeType
    FillType: FillType
    Linetype: ObjectId
    TrueColor: Color
    ColorIndex: int
    AlwaysResolveByLayerPlotStyles: bool
    IsPerspectiveView: bool
    Layer: ObjectId
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class StringPair:
    """.NET: Autodesk.Aec.DatabaseServices.StringPair"""
    def __init__(self, *args) -> None: ...
    Right: str
    Left: str

class StringPairCollection:
    """.NET: Autodesk.Aec.DatabaseServices.StringPairCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: StringPair
    def Add(self, value: StringPair) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, strLeft: str) -> bool: ...
    def CopyTo(self, array: list, start: int) -> None: ...
    def Get(self, strLeft: str) -> str: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: StringPair) -> int: ...
    def Insert(self, index: int, value: StringPair) -> None: ...
    def Remove(self, strLeft: str) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class SurfaceHatchFlags:
    """.NET enum: Autodesk.Aec.DatabaseServices.SurfaceHatchFlags"""
    def __init__(self, *args) -> None: ...
    NoHatch: int  # = 0
    Top: int  # = 1
    Bottom: int  # = 2
    Right: int  # = 4
    Left: int  # = 8
    Front: int  # = 16
    Back: int  # = 32
    Section: int  # = 64
    Discard: int  # = 128
class SurfaceMappingType:
    """.NET enum: Autodesk.Aec.DatabaseServices.SurfaceMappingType"""
    def __init__(self, *args) -> None: ...
    DefaultMapping: int  # = 0
    FaceMapping: int  # = 1
    AsSurfaceHatch: int  # = 2
class TextNote(DBObject):
    """.NET: Autodesk.Aec.DatabaseServices.TextNote"""
    def __init__(self, *args) -> None: ...
    ExtensionDictionaryName: str
    Note: str
    SwappingReferences: bool
    Overrides: OverrideCollection
    Description: str
    TypeIcon: Icon
    DisplayName: str
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
    def GetStandardNote(instance: DBObject) -> str: ...
    @staticmethod
    def SetStandardNote(instance: DBObject, note: str) -> None: ...

class ThemeSymbolType:
    """.NET enum: Autodesk.Aec.DatabaseServices.ThemeSymbolType"""
    def __init__(self, *args) -> None: ...
    ThemeSymbolSquare: int  # = 0
    ThemeSymbolCircle: int  # = 1
class UVLayoutModeType:
    """.NET enum: Autodesk.Aec.DatabaseServices.UVLayoutModeType"""
    def __init__(self, *args) -> None: ...
    Manual: int  # = 0
    Repeat: int  # = 1
    SpaceEvenly: int  # = 2
class UnitType(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.UnitType"""
    def __init__(self, *args) -> None: ...
    IsImperial: bool
    IsMetric: bool
    InternalName: str
    Type: BuiltInType
    Status: UnitStatus
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetTypeDisplayName(self, getLocalized: bool) -> str: ...
    def IsCompatible(self, value: UnitType) -> bool: ...
    def IsSimpleUnit(self, unit: BuiltInUnit) -> bool: ...
    def PluralName(self, getLocalized: bool) -> str: ...
    def SingularName(self, getLocalized: bool) -> str: ...

class UnitVariable(ImpObject):
    """.NET: Autodesk.Aec.DatabaseServices.UnitVariable"""
    def __init__(self, *args) -> None: ...
    Type: UnitType
    Value: float
    Status: UnitStatus
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Convert(from_: UnitVariable, toUnit: UnitType) -> UnitVariable: ...
    def ConvertTo(self, toUnit: UnitType) -> UnitStatus: ...
    def IsCompatible(self, type: UnitType) -> bool: ...

class Utility:
    """.NET: Autodesk.Aec.DatabaseServices.Utility"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def CanDeleteCurrentAnnotationScale(A_0: ObjectId) -> bool: ...
    @staticmethod
    def FindAnonymousBlockLastCreated(db: Database) -> ObjectId: ...
    @staticmethod
    def GetAutomaticallyBoundSpaces(object: DBObject, blockRefPath: ObjectIdCollection, boundSpaces: AutomaticSpaceBoundary) -> None: ...
    @staticmethod
    def GetCurrentSupportedAnnotationScales(A_0: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def IsSectionedBodyDisplayDisabled(db: Database) -> bool: ...
    @staticmethod
    def MassElementHasFacesToJoin(massElementId: ObjectId) -> bool: ...
    @staticmethod
    def SetAutomaticallyBoundSpaces(object: DBObject, blockRefPath: ObjectIdCollection, boundSpaces: AutomaticSpaceBoundary) -> None: ...
    @staticmethod
    def SetLayer(entity: Entity, layerKey: str) -> None: ...

class ViewDependentCombination:
    """.NET: Autodesk.Aec.DatabaseServices.ViewDependentCombination"""
    def __init__(self, *args) -> None: ...
    Direction: Vector3d
    SetId: ObjectId

class ViewDependentCombinationCollection:
    """.NET: Autodesk.Aec.DatabaseServices.ViewDependentCombinationCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: ViewDependentCombination
    def Add(self, item: ViewDependentCombination) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, item: ViewDependentCombination) -> bool: ...
    def CopyTo(self, array: list, start: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, item: ViewDependentCombination) -> int: ...
    def Insert(self, index: int, item: ViewDependentCombination) -> None: ...
    def Remove(self, item: ViewDependentCombination) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class ViewDirection:
    """.NET enum: Autodesk.Aec.DatabaseServices.ViewDirection"""
    def __init__(self, *args) -> None: ...
    Top: int  # = 0
    Bottom: int  # = 1
    Front: int  # = 2
    Back: int  # = 3
    Left: int  # = 4
    Right: int  # = 5
    Other: int  # = 6
class VolumeLayoutTool(CellLayoutTool):
    """.NET: Autodesk.Aec.DatabaseServices.VolumeLayoutTool"""
    def __init__(self, *args) -> None: ...
    LayoutVolumeIds: IntegerCollection
    LayoutCellIds: IntegerCollection
    LayoutNodeIds: IntegerCollection
    IsAnchored: bool
    AnchorId: ObjectId
    CanBeAnchored: bool
    GeoEcsIsDirty: bool
    GeoEcs: Matrix3d
    ZDir: Vector3d
    YDir: Vector3d
    XDir: Vector3d
    Normal: Vector3d
    Rotation: float
    Direction: Vector3d
    Location: Point3d
    IsHighlighting: bool
    AutomaticallyBoundSpaces: AutomaticSpaceBoundary
    SwappingReferences: bool
    NeedsPromoting: bool
    SupportsProfileCommands: bool
    BaseCurve: Curve
    SupportsBaseCurveCommands: bool
    StyleId: ObjectId
    Classifications: ClassificationCollection
    LayerKey: str
    ProjectState: ProjectState
    Description: str
    TypeIcon: Icon
    DisplayName: str
    Overrides: OverrideCollection
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
    def GetClosestLayoutVolume(self, location: Point3d) -> int: ...
    def GetLayoutVolumeBody(self, volumeId: int, toWcs: Matrix3d) -> Body: ...
    def GetLayoutVolumeCentroid(self, volumeId: int) -> Matrix3d: ...
    def GetLayoutVolumeExtent(self, volumeId: int, length: float, width: float, height: float, toWcs: Matrix3d) -> None: ...

class XReferenceSubCommandType:
    """.NET enum: Autodesk.Aec.DatabaseServices.XReferenceSubCommandType"""
    def __init__(self, *args) -> None: ...
    Attach: int  # = 0
    Bind: int  # = 1
    Path: int  # = 2
    Detach: int  # = 3
    Overlay: int  # = 4
    Reload: int  # = 5
    Unload: int  # = 6
    NoSubCommand: int  # = 7
class YAlignment:
    """.NET enum: Autodesk.Aec.DatabaseServices.YAlignment"""
    def __init__(self, *args) -> None: ...
    Centered: int  # = 0
    FrontFlush: int  # = 1
    BackFlush: int  # = 2
