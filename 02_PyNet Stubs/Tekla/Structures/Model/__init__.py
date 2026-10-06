# Auto-generated — Tekla 2026 — Tekla.Structures.Model

class Assembly(ModelObject):
    """.NET: Tekla.Structures.Model.Assembly"""
    def __init__(self, *args) -> None: ...
    Name: str
    AssemblyNumber: NumberingSeries
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Add(self, Object: IAssemblable) -> bool: ...
    def CompareTo(self, AssemblyToCompare: Assembly) -> bool: ...
    def Delete(self, ) -> bool: ...
    def DeleteUserDefinedCoordSys(self, ) -> bool: ...
    def GetAssembly(self, ) -> Assembly: ...
    def GetAssemblyType(self, ) -> AssemblyTypeEnum: ...
    def GetFatherPour(self, ) -> PourObject: ...
    def GetFatherPourUnit(self, ) -> PourUnit: ...
    def GetMainObject(self, ) -> ModelObject: ...
    def GetMainPart(self, ) -> ModelObject: ...
    def GetSecondaries(self, ) -> ArrayList: ...
    def GetSubAssemblies(self, ) -> ArrayList: ...
    def HasUserDefinedCoordSys(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Remove(self, Object: ModelObject) -> bool: ...
    def Select(self, ) -> bool: ...
    def SetMainObject(self, mainObject: ModelObject) -> bool: ...
    def SetMainPart(self, Part: Part) -> bool: ...
    def SetUserDefinedCoordSys(self, coordinateSystem: CoordinateSystem) -> bool: ...

class BaseComponent(ModelObject):
    """.NET: Tekla.Structures.Model.BaseComponent"""
    def __init__(self, *args) -> None: ...
    Name: str
    Number: int
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def GetAttribute(self, AttrName: str, StrValue: str) -> bool: ...
    def LoadAttributesFromFile(self, Filename: str) -> bool: ...
    def SetAttribute(self, AttrName: str, StrValue: str) -> None: ...

class BasePoint:
    """.NET: Tekla.Structures.Model.BasePoint"""
    def __init__(self, *args) -> None: ...
    Id: int
    Guid: Guid
    InitialGuid: str
    Name: str
    Description: str
    CoordinateSystem: str
    NorthSouth: float
    EastWest: float
    Elevation: float
    Latitude: float
    Longitude: float
    LocationInModelX: float
    LocationInModelY: float
    LocationInModelZ: float
    AngleToNorth: float
    IsProjectBasePoint: bool
    IsCurrentBasePoint: bool
    IsLocked: bool
    IsScopedCurrentBasePoint: bool
    @staticmethod
    def ConvertFromBasePoint(basePoint: BasePoint, point: Point) -> Point: ...
    @staticmethod
    def ConvertToBasePoint(basePoint: BasePoint, point: Point) -> Point: ...
    def Delete(self, ) -> bool: ...
    def GetCompoundPlaneAngleLatitude(self, ) -> Tuple: ...
    def GetCompoundPlaneAngleLongitude(self, ) -> Tuple: ...
    def GetCoordinateSystem(self, CoordsysType: CoordinateSystemType) -> CoordinateSystem: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def SetAsCurrent(self, ) -> IDisposable: ...

class BaseRebarGroup(Reinforcement):
    """.NET: Tekla.Structures.Model.BaseRebarGroup"""
    def __init__(self, *args) -> None: ...
    Size: str
    StartHook: RebarHookData
    EndHook: RebarHookData
    FromPlaneOffset: float
    StartFromPlaneOffset: float
    EndFromPlaneOffset: float
    ExcludeType: ExcludeTypeEnum
    SpacingType: RebarGroupSpacingTypeEnum
    Spacings: ArrayList
    StartPoint: Point
    EndPoint: Point
    Father: ModelObject
    Grade: str
    Name: str
    Class: int
    NumberingSeries: NumberingSeries
    OnPlaneOffsets: ArrayList
    StartPointOffsetType: RebarOffsetTypeEnum
    StartPointOffsetValue: float
    EndPointOffsetType: RebarOffsetTypeEnum
    EndPointOffsetValue: float
    RadiusValues: ArrayList
    InputPointDeformingState: DeformingType
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier

class BaseRebarModifier(ModelObject):
    """.NET: Tekla.Structures.Model.BaseRebarModifier"""
    def __init__(self, *args) -> None: ...
    Father: RebarSet
    Curve: Contour
    BarsAffected: BarsAffectedEnum
    FirstAffectedBar: int
    FollowEdges: bool
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class BaseWeld(ModelObject):
    """.NET: Tekla.Structures.Model.BaseWeld"""
    def __init__(self, *args) -> None: ...
    MainObject: ModelObject
    SecondaryObject: ModelObject
    SizeAbove: float
    AdditionalSizeAbove: float
    TypeAbove: WeldTypeEnum
    AngleAbove: float
    LengthAbove: float
    ContourAbove: WeldContourEnum
    FinishAbove: WeldFinishEnum
    PitchAbove: float
    SizeBelow: float
    AdditionalSizeBelow: float
    TypeBelow: WeldTypeEnum
    AngleBelow: float
    LengthBelow: float
    ContourBelow: WeldContourEnum
    FinishBelow: WeldFinishEnum
    PitchBelow: float
    ShopWeld: bool
    AroundWeld: bool
    StitchWeld: bool
    RootOpeningAbove: float
    RootFaceAbove: float
    EffectiveThroatAbove: float
    IncrementAmountAbove: int
    RootOpeningBelow: float
    RootFaceBelow: float
    EffectiveThroatBelow: float
    IncrementAmountBelow: int
    ElectrodeClassification: WeldElectrodeClassificationEnum
    ElectrodeStrength: float
    ElectrodeCoefficient: float
    ProcessType: WeldProcessTypeEnum
    NDTInspection: WeldNDTInspectionEnum
    ConnectAssemblies: bool
    ReferenceText: str
    PrefixAboveLine: str
    PrefixBelowLine: str
    Standard: str
    WeldNumber: int
    WeldNumberPrefix: str
    IntermittentType: WeldIntermittentTypeEnum
    Placement: WeldPlacementTypeEnum
    Preparation: WeldPreparationTypeEnum
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def GetSolid(self, ) -> Solid: ...
    def GetWeldGeometries(self, ) -> ArrayList: ...

class Beam(Part):
    """.NET: Tekla.Structures.Model.Beam"""
    def __init__(self, *args) -> None: ...
    StartPoint: Point
    EndPoint: Point
    StartPointOffset: Offset
    EndPointOffset: Offset
    Type: BeamTypeEnum
    StartLevelName: str
    EndLevelName: str
    StartLevelOffset: float
    EndLevelOffset: float
    Profile: Profile
    Material: Material
    DeformingData: DeformingData
    PartNumber: NumberingSeries
    AssemblyNumber: NumberingSeries
    Name: str
    Class: str
    Finish: str
    CastUnitType: CastUnitTypeEnum
    PourPhase: int
    Position: Position
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class BendSurface:
    """.NET: Tekla.Structures.Model.BendSurface"""
    def __init__(self, *args) -> None: ...
    InwardCurved: bool
    IntersectionLine: Line
    EndFaceNormal1: Vector
    EndFaceNormal2: Vector
    CenterLine: Line
    RotationAxis: Vector
    LateralBoundary1: List
    LateralBoundary2: List
    SideBoundary1: LineSegment
    SideBoundary2: LineSegment

class BendSurfaceNode:
    """.NET: Tekla.Structures.Model.BendSurfaceNode"""
    def __init__(self, *args) -> None: ...
    IsAutomatic: bool
    Surface: BendSurface
    def AcceptVisitor(self, visitor: IGeometryNodeVisitor) -> None: ...
    def Clone(self, ) -> IGeometryNode: ...

class BentPlate(Part):
    """.NET: Tekla.Structures.Model.BentPlate"""
    def __init__(self, *args) -> None: ...
    Geometry: ConnectiveGeometry
    Thickness: float
    Profile: Profile
    Material: Material
    DeformingData: DeformingData
    PartNumber: NumberingSeries
    AssemblyNumber: NumberingSeries
    Name: str
    Class: str
    Finish: str
    CastUnitType: CastUnitTypeEnum
    PourPhase: int
    Position: Position
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class BentPlateGeometrySolver:
    """.NET: Tekla.Structures.Model.BentPlateGeometrySolver"""
    def __init__(self, *args) -> None: ...
    def AddLeg(self, geometry: ConnectiveGeometry, segment1: LineSegment, polygon: Contour, segment2: LineSegment, largestRadius: float, halfAperture: float) -> ConnectiveGeometry: ...
    def ModifyBendSurface(self, geometry: ConnectiveGeometry, bendSection: GeometrySection, surface: BendSurface) -> ConnectiveGeometry: ...
    def ModifyConicalRadiuses(self, geometry: ConnectiveGeometry, conicalSection: GeometrySection, radius1: float, radius2: float) -> ConnectiveGeometry: ...
    def ModifyCylindricalSurface(self, geometry: ConnectiveGeometry, cylindricalSection: GeometrySection, surface: CylindricalSurface) -> ConnectiveGeometry: ...
    def ModifyPolygon(self, geometry: ConnectiveGeometry, polygonSection: GeometrySection, points: Contour) -> ConnectiveGeometry: ...
    def ModifyRadius(self, geometry: ConnectiveGeometry, cylindricalSection: GeometrySection, radius: float) -> ConnectiveGeometry: ...
    def RemoveLeg(self, geometry: ConnectiveGeometry, legSection: GeometrySection) -> ConnectiveGeometry: ...
    def ScaleConeSection(self, geometry: ConnectiveGeometry, conicalSection: GeometrySection, scale: float) -> ConnectiveGeometry: ...
    def SetBendAngle(self, angle: float, sectionToSetAngle: GeometrySection, sectionToMove: GeometrySection, geometry: ConnectiveGeometry) -> ConnectiveGeometry: ...
    def SetMainSection(self, newMainSection: GeometrySection, geometry: ConnectiveGeometry) -> ConnectiveGeometry: ...
    def Split(self, geometry: ConnectiveGeometry, geometrySection: GeometrySection) -> IList: ...

class BoltArray(BoltGroup):
    """.NET: Tekla.Structures.Model.BoltArray"""
    def __init__(self, *args) -> None: ...
    BoltSize: float
    BoltStandard: str
    BoltType: BoltTypeEnum
    ThreadInMaterial: BoltThreadInMaterialEnum
    Length: float
    CutLength: float
    ExtraLength: float
    Tolerance: float
    HoleType: BoltHoleTypeEnum
    SlottedHoleX: float
    SlottedHoleY: float
    SlotOffsetX: float
    SlotOffsetY: float
    BlindHoleDepth: float
    PlainHoleType: BoltPlainHoleTypeEnum
    RotateSlots: BoltRotateSlotsEnum
    Position: Position
    StartPointOffset: Offset
    EndPointOffset: Offset
    Washer1: bool
    Washer2: bool
    Washer3: bool
    Nut1: bool
    Nut2: bool
    Bolt: bool
    Hole1: bool
    Hole2: bool
    Hole3: bool
    Hole4: bool
    Hole5: bool
    PartToBoltTo: Part
    PartToBeBolted: Part
    OtherPartsToBolt: ArrayList
    BoltHolesAttributes: IList
    FirstPosition: Point
    SecondPosition: Point
    ConnectAssemblies: bool
    BoltPositions: ArrayList
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def AddBoltDistX(self, DistX: float) -> bool: ...
    def AddBoltDistY(self, DistY: float) -> bool: ...
    def Delete(self, ) -> bool: ...
    def GetBoltDistX(self, Index: int) -> float: ...
    def GetBoltDistXCount(self, ) -> int: ...
    def GetBoltDistY(self, Index: int) -> float: ...
    def GetBoltDistYCount(self, ) -> int: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def RemoveBoltDistX(self, Index: int) -> bool: ...
    def RemoveBoltDistY(self, Index: int) -> bool: ...
    def Select(self, ) -> bool: ...
    def SetBoltDistX(self, Index: int, DistX: float) -> bool: ...
    def SetBoltDistY(self, Index: int, DistY: float) -> bool: ...

class BoltCircle(BoltGroup):
    """.NET: Tekla.Structures.Model.BoltCircle"""
    def __init__(self, *args) -> None: ...
    NumberOfBolts: float
    Diameter: float
    BoltSize: float
    BoltStandard: str
    BoltType: BoltTypeEnum
    ThreadInMaterial: BoltThreadInMaterialEnum
    Length: float
    CutLength: float
    ExtraLength: float
    Tolerance: float
    HoleType: BoltHoleTypeEnum
    SlottedHoleX: float
    SlottedHoleY: float
    SlotOffsetX: float
    SlotOffsetY: float
    BlindHoleDepth: float
    PlainHoleType: BoltPlainHoleTypeEnum
    RotateSlots: BoltRotateSlotsEnum
    Position: Position
    StartPointOffset: Offset
    EndPointOffset: Offset
    Washer1: bool
    Washer2: bool
    Washer3: bool
    Nut1: bool
    Nut2: bool
    Bolt: bool
    Hole1: bool
    Hole2: bool
    Hole3: bool
    Hole4: bool
    Hole5: bool
    PartToBoltTo: Part
    PartToBeBolted: Part
    OtherPartsToBolt: ArrayList
    BoltHolesAttributes: IList
    FirstPosition: Point
    SecondPosition: Point
    ConnectAssemblies: bool
    BoltPositions: ArrayList
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class BoltGroup(ModelObject):
    """.NET: Tekla.Structures.Model.BoltGroup"""
    def __init__(self, *args) -> None: ...
    BoltSize: float
    BoltStandard: str
    BoltType: BoltTypeEnum
    ThreadInMaterial: BoltThreadInMaterialEnum
    Length: float
    CutLength: float
    ExtraLength: float
    Tolerance: float
    HoleType: BoltHoleTypeEnum
    SlottedHoleX: float
    SlottedHoleY: float
    SlotOffsetX: float
    SlotOffsetY: float
    BlindHoleDepth: float
    PlainHoleType: BoltPlainHoleTypeEnum
    RotateSlots: BoltRotateSlotsEnum
    Position: Position
    StartPointOffset: Offset
    EndPointOffset: Offset
    Washer1: bool
    Washer2: bool
    Washer3: bool
    Nut1: bool
    Nut2: bool
    Bolt: bool
    Hole1: bool
    Hole2: bool
    Hole3: bool
    Hole4: bool
    Hole5: bool
    PartToBoltTo: Part
    PartToBeBolted: Part
    OtherPartsToBolt: ArrayList
    BoltHolesAttributes: IList
    FirstPosition: Point
    SecondPosition: Point
    ConnectAssemblies: bool
    BoltPositions: ArrayList
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def AddOtherPartToBolt(self, M: Part) -> bool: ...
    def GetFatherPour(self, ) -> PourObject: ...
    def GetFatherPourUnit(self, ) -> PourUnit: ...
    def GetOtherPartsToBolt(self, ) -> ArrayList: ...
    def GetSolid(self, withHighAccuracy: bool) -> Solid: ...
    def RemoveOtherPartToBolt(self, M: Part) -> bool: ...

class BoltHoleAttributes:
    """.NET: Tekla.Structures.Model.BoltHoleAttributes"""
    def __init__(self, *args) -> None: ...
    HoleType: BoltHoleTypeEnum
    LongHoleX: float
    LongHoleY: float
    SlotOffsetX: float
    SlotOffsetY: float

class BoltXYList(BoltGroup):
    """.NET: Tekla.Structures.Model.BoltXYList"""
    def __init__(self, *args) -> None: ...
    BoltSize: float
    BoltStandard: str
    BoltType: BoltTypeEnum
    ThreadInMaterial: BoltThreadInMaterialEnum
    Length: float
    CutLength: float
    ExtraLength: float
    Tolerance: float
    HoleType: BoltHoleTypeEnum
    SlottedHoleX: float
    SlottedHoleY: float
    SlotOffsetX: float
    SlotOffsetY: float
    BlindHoleDepth: float
    PlainHoleType: BoltPlainHoleTypeEnum
    RotateSlots: BoltRotateSlotsEnum
    Position: Position
    StartPointOffset: Offset
    EndPointOffset: Offset
    Washer1: bool
    Washer2: bool
    Washer3: bool
    Nut1: bool
    Nut2: bool
    Bolt: bool
    Hole1: bool
    Hole2: bool
    Hole3: bool
    Hole4: bool
    Hole5: bool
    PartToBoltTo: Part
    PartToBeBolted: Part
    OtherPartsToBolt: ArrayList
    BoltHolesAttributes: IList
    FirstPosition: Point
    SecondPosition: Point
    ConnectAssemblies: bool
    BoltPositions: ArrayList
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def AddBoltDistX(self, DistX: float) -> bool: ...
    def AddBoltDistY(self, DistY: float) -> bool: ...
    def Delete(self, ) -> bool: ...
    def GetBoltDistX(self, Index: int) -> float: ...
    def GetBoltDistXCount(self, ) -> int: ...
    def GetBoltDistY(self, Index: int) -> float: ...
    def GetBoltDistYCount(self, ) -> int: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class Boolean(ModelObject):
    """.NET: Tekla.Structures.Model.Boolean"""
    def __init__(self, *args) -> None: ...
    Father: ModelObject
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier

class BooleanPart(bool):
    """.NET: Tekla.Structures.Model.BooleanPart"""
    def __init__(self, *args) -> None: ...
    Type: BooleanTypeEnum
    OperativePart: Part
    Father: ModelObject
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...
    def SetOperativePart(self, Part: Part) -> bool: ...

class Brep(Part):
    """.NET: Tekla.Structures.Model.Brep"""
    def __init__(self, *args) -> None: ...
    StartPoint: Point
    EndPoint: Point
    StartPointOffset: Offset
    EndPointOffset: Offset
    Profile: Profile
    Material: Material
    DeformingData: DeformingData
    PartNumber: NumberingSeries
    AssemblyNumber: NumberingSeries
    Name: str
    Class: str
    Finish: str
    CastUnitType: CastUnitTypeEnum
    PourPhase: int
    Position: Position
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class Chamfer:
    """.NET: Tekla.Structures.Model.Chamfer"""
    def __init__(self, *args) -> None: ...
    Type: ChamferTypeEnum
    X: float
    Y: float
    DZ1: float
    DZ2: float

class ChangeData:
    """.NET: Tekla.Structures.Model.ChangeData"""
    def __init__(self, *args) -> None: ...
    Object: ModelObject
    Type: ChangeTypeEnum
    Source: ChangeSourceTypeEnum

class CircleRebarGroup(BaseRebarGroup):
    """.NET: Tekla.Structures.Model.CircleRebarGroup"""
    def __init__(self, *args) -> None: ...
    Polygon: Polygon
    StirrupType: CircleRebarGroupStirrupTypeEnum
    Size: str
    StartHook: RebarHookData
    EndHook: RebarHookData
    FromPlaneOffset: float
    StartFromPlaneOffset: float
    EndFromPlaneOffset: float
    ExcludeType: ExcludeTypeEnum
    SpacingType: RebarGroupSpacingTypeEnum
    Spacings: ArrayList
    StartPoint: Point
    EndPoint: Point
    Father: ModelObject
    Grade: str
    Name: str
    Class: int
    NumberingSeries: NumberingSeries
    OnPlaneOffsets: ArrayList
    StartPointOffsetType: RebarOffsetTypeEnum
    StartPointOffsetValue: float
    EndPointOffsetType: RebarOffsetTypeEnum
    EndPointOffsetValue: float
    RadiusValues: ArrayList
    InputPointDeformingState: DeformingType
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class ClashCheckData:
    """.NET: Tekla.Structures.Model.ClashCheckData"""
    def __init__(self, *args) -> None: ...
    Object1: ModelObject
    Object2: ModelObject
    Type: ClashTypeEnum
    Overlap: float

class ClashCheckHandler:
    """.NET: Tekla.Structures.Model.ClashCheckHandler"""
    def __init__(self, *args) -> None: ...
    def GetIntersectionBoundingBoxes(self, ID1: Identifier, ID2: Identifier) -> ArrayList: ...
    def RunClashCheck(self, ) -> bool: ...
    def RunClashCheckWithOptions(self, betweenReferenceModels: bool, betweenReferenceModelsAndComponents: bool, objectsInsideReferenceModels: bool, minDistance: float, betweenParts: bool) -> bool: ...
    def StopClashCheck(self, ) -> bool: ...

class Component(BaseComponent):
    """.NET: Tekla.Structures.Model.Component"""
    def __init__(self, *args) -> None: ...
    Name: str
    Number: int
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def GetAssembly(self, ) -> Assembly: ...
    def GetBooleans(self, ) -> ModelObjectEnumerator: ...
    def GetComponentInput(self, ) -> ComponentInput: ...
    def GetComponents(self, ) -> ModelObjectEnumerator: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...
    def SetComponentInput(self, I: ComponentInput) -> bool: ...

class ComponentInput:
    """.NET: Tekla.Structures.Model.ComponentInput"""
    def __init__(self, *args) -> None: ...
    Count: int
    IsSynchronized: bool
    SyncRoot: object
    def AddInputObject(self, M: ModelObject) -> bool: ...
    def AddInputObjects(self, Objects: ArrayList) -> bool: ...
    def AddInputPolygon(self, P: Polygon) -> bool: ...
    def AddOneInputPosition(self, P: Point) -> bool: ...
    def AddTwoInputPositions(self, Position1: Point, Position2: Point) -> bool: ...
    def CopyTo(self, array: Array, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...

class ConicalSurface(BendSurface):
    """.NET: Tekla.Structures.Model.ConicalSurface"""
    def __init__(self, *args) -> None: ...
    Radiuses: Tuple
    Apex: Point
    InwardCurved: bool
    IntersectionLine: Line
    EndFaceNormal1: Vector
    EndFaceNormal2: Vector
    CenterLine: Line
    RotationAxis: Vector
    LateralBoundary1: List
    LateralBoundary2: List
    SideBoundary1: LineSegment
    SideBoundary2: LineSegment

class ConicalSurfaceNode(BendSurfaceNode):
    """.NET: Tekla.Structures.Model.ConicalSurfaceNode"""
    def __init__(self, *args) -> None: ...
    Surface: ConicalSurface
    IsAutomatic: bool
    def AcceptVisitor(self, visitor: IGeometryNodeVisitor) -> None: ...
    def Clone(self, ) -> IGeometryNode: ...

class Connection(BaseComponent):
    """.NET: Tekla.Structures.Model.Connection"""
    def __init__(self, *args) -> None: ...
    Class: int
    UpVector: Vector
    AutoDirectionType: AutoDirectionTypeEnum
    PositionType: PositionTypeEnum
    Code: str
    Status: ConnectionStatusEnum
    Name: str
    Number: int
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def GetPrimaryObject(self, ) -> ModelObject: ...
    def GetSecondaryObjects(self, ) -> ArrayList: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...
    def SetPrimaryObject(self, M: ModelObject) -> bool: ...
    def SetSecondaryObject(self, M: ModelObject) -> bool: ...
    def SetSecondaryObjects(self, Secondaries: ArrayList) -> bool: ...

class ConnectiveGeometry:
    """.NET: Tekla.Structures.Model.ConnectiveGeometry"""
    def __init__(self, *args) -> None: ...
    def GetConnection(self, geometrySection1: GeometrySection, geometrySection2: GeometrySection) -> IList: ...
    def GetGeometryEnumerator(self, ) -> GeometrySectionEnumerator: ...
    def GetGeometryLegSections(self, ) -> IList: ...
    def GetNeighborSections(self, geometrySection: GeometrySection) -> IList: ...
    def IsEmpty(self, ) -> bool: ...

class ConnectiveGeometryException(Exception):
    """.NET: Tekla.Structures.Model.ConnectiveGeometryException"""
    def __init__(self, *args) -> None: ...
    Message: str
    Data: IDictionary
    InnerException: Exception
    TargetSite: MethodBase
    StackTrace: str
    HelpLink: str
    Source: str
    HResult: int

class Contour:
    """.NET: Tekla.Structures.Model.Contour"""
    def __init__(self, *args) -> None: ...
    ContourPoints: ArrayList
    def AddContourPoint(self, Point: ContourPoint) -> None: ...
    def CalculatePolygon(self, polygon: Polygon) -> bool: ...
    def GetPolycurve(self, ) -> Polycurve: ...

class ContourPlate(Part):
    """.NET: Tekla.Structures.Model.ContourPlate"""
    def __init__(self, *args) -> None: ...
    Type: ContourPlateTypeEnum
    Contour: Contour
    LevelName: str
    LevelOffset: float
    Profile: Profile
    Material: Material
    DeformingData: DeformingData
    PartNumber: NumberingSeries
    AssemblyNumber: NumberingSeries
    Name: str
    Class: str
    Finish: str
    CastUnitType: CastUnitTypeEnum
    PourPhase: int
    Position: Position
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def AddContourPoint(self, contourPoint: ContourPoint) -> bool: ...
    def Delete(self, ) -> bool: ...
    def GetContourPolycurve(self, ) -> Polycurve: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class ContourPoint(Point):
    """.NET: Tekla.Structures.Model.ContourPoint"""
    def __init__(self, *args) -> None: ...
    Chamfer: Chamfer
    def SetPoint(self, P: Point) -> None: ...

class ControlArc(ModelObject):
    """.NET: Tekla.Structures.Model.ControlArc"""
    def __init__(self, *args) -> None: ...
    Color: ControlObjectColorEnum
    LineType: ControlObjectLineType
    Geometry: Arc
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class ControlCircle(ModelObject):
    """.NET: Tekla.Structures.Model.ControlCircle"""
    def __init__(self, *args) -> None: ...
    Extension: float
    Color: ControlCircleColorEnum
    LineType: ControlObjectLineType
    Point1: Point
    Point2: Point
    Point3: Point
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class ControlLine(ModelObject):
    """.NET: Tekla.Structures.Model.ControlLine"""
    def __init__(self, *args) -> None: ...
    Line: LineSegment
    IsMagnetic: bool
    Extension: float
    Color: ControlLineColorEnum
    LineType: ControlObjectLineType
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class ControlObjectColorEnum:
    """.NET: Tekla.Structures.Model.ControlObjectColorEnum"""
    def __init__(self, *args) -> None: ...
    ...

class ControlObjectLineType:
    """.NET: Tekla.Structures.Model.ControlObjectLineType"""
    def __init__(self, *args) -> None: ...
    ...

class ControlPlane(ModelObject):
    """.NET: Tekla.Structures.Model.ControlPlane"""
    def __init__(self, *args) -> None: ...
    Plane: Plane
    IsMagnetic: bool
    Name: str
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class ControlPoint(ModelObject):
    """.NET: Tekla.Structures.Model.ControlPoint"""
    def __init__(self, *args) -> None: ...
    Point: Point
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class ControlPolycurve(ModelObject):
    """.NET: Tekla.Structures.Model.ControlPolycurve"""
    def __init__(self, *args) -> None: ...
    Color: ControlObjectColorEnum
    LineType: ControlObjectLineType
    Geometry: Polycurve
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class CurvedRebarGroup(BaseRebarGroup):
    """.NET: Tekla.Structures.Model.CurvedRebarGroup"""
    def __init__(self, *args) -> None: ...
    Polygon: Polygon
    Size: str
    StartHook: RebarHookData
    EndHook: RebarHookData
    FromPlaneOffset: float
    StartFromPlaneOffset: float
    EndFromPlaneOffset: float
    ExcludeType: ExcludeTypeEnum
    SpacingType: RebarGroupSpacingTypeEnum
    Spacings: ArrayList
    StartPoint: Point
    EndPoint: Point
    Father: ModelObject
    Grade: str
    Name: str
    Class: int
    NumberingSeries: NumberingSeries
    OnPlaneOffsets: ArrayList
    StartPointOffsetType: RebarOffsetTypeEnum
    StartPointOffsetValue: float
    EndPointOffsetType: RebarOffsetTypeEnum
    EndPointOffsetValue: float
    RadiusValues: ArrayList
    InputPointDeformingState: DeformingType
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class CustomPart(BaseComponent):
    """.NET: Tekla.Structures.Model.CustomPart"""
    def __init__(self, *args) -> None: ...
    Position: Position
    Name: str
    Number: int
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def GetAssembly(self, ) -> Assembly: ...
    def GetBooleans(self, ) -> ModelObjectEnumerator: ...
    def GetComponents(self, ) -> ModelObjectEnumerator: ...
    def GetStartAndEndPositions(self, StartPoint: Point, EndPoint: Point) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...
    def SetInputPositions(self, StartPoint: Point, EndPoint: Point) -> bool: ...

class CutPlane(bool):
    """.NET: Tekla.Structures.Model.CutPlane"""
    def __init__(self, *args) -> None: ...
    Plane: Plane
    Father: ModelObject
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class CylindricalSurface(BendSurface):
    """.NET: Tekla.Structures.Model.CylindricalSurface"""
    def __init__(self, *args) -> None: ...
    Radius: float
    InwardCurved: bool
    IntersectionLine: Line
    EndFaceNormal1: Vector
    EndFaceNormal2: Vector
    CenterLine: Line
    RotationAxis: Vector
    LateralBoundary1: List
    LateralBoundary2: List
    SideBoundary1: LineSegment
    SideBoundary2: LineSegment

class CylindricalSurfaceNode(BendSurfaceNode):
    """.NET: Tekla.Structures.Model.CylindricalSurfaceNode"""
    def __init__(self, *args) -> None: ...
    Surface: CylindricalSurface
    IsAutomatic: bool
    def AcceptVisitor(self, visitor: IGeometryNodeVisitor) -> None: ...
    def Clone(self, ) -> IGeometryNode: ...

class DeformingData:
    """.NET: Tekla.Structures.Model.DeformingData"""
    def __init__(self, *args) -> None: ...
    Angle: float
    Angle2: float
    Cambering: float
    Shortening: float

class Detail(BaseComponent):
    """.NET: Tekla.Structures.Model.Detail"""
    def __init__(self, *args) -> None: ...
    Class: int
    UpVector: Vector
    AutoDirectionType: AutoDirectionTypeEnum
    PositionType: PositionTypeEnum
    DetailType: DetailTypeEnum
    Code: str
    Status: ConnectionStatusEnum
    Name: str
    Number: int
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def GetPrimaryObject(self, ) -> ModelObject: ...
    def GetReferencePoint(self, ) -> Point: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...
    def SetPrimaryObject(self, M: ModelObject) -> bool: ...
    def SetReferencePoint(self, ReferencePoint: Point) -> bool: ...

class DisposableToken:
    """.NET: Tekla.Structures.Model.DisposableToken"""
    def __init__(self, *args) -> None: ...
    def Dispose(self, ) -> None: ...

class EdgeChamfer(bool):
    """.NET: Tekla.Structures.Model.EdgeChamfer"""
    def __init__(self, *args) -> None: ...
    Chamfer: Chamfer
    FirstEnd: Point
    SecondEnd: Point
    FirstChamferEndType: ChamferEndTypeEnum
    SecondChamferEndType: ChamferEndTypeEnum
    SecondBevelDimension: float
    FirstBevelDimension: float
    Name: str
    Father: ModelObject
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class Events(MarshalByRefObject):
    """.NET: Tekla.Structures.Model.Events"""
    def __init__(self, *args) -> None: ...
    def Dispose(self, ) -> None: ...
    def InitializeLifetimeService(self, ) -> object: ...
    def OnAnnotationSelectionChange(self, eventName: str, parameters: list) -> None: ...
    def OnClashCheckDone(self, eventName: str, parameters: list) -> None: ...
    def OnClashDetected(self, eventName: str, parameters: list) -> None: ...
    def OnClipBoxChanged(self, eventName: str, parameters: list) -> None: ...
    def OnClipPlaneChanged(self, eventName: str, parameters: list) -> None: ...
    def OnCommandStatusChange(self, eventName: str, parameters: list) -> None: ...
    def OnDbCommit(self, eventName: str, parameters: list) -> None: ...
    def OnHiddenObjectsChanged(self, ) -> None: ...
    def OnInterrupted(self, ) -> None: ...
    def OnModelLoad(self, eventName: str, parameters: list) -> None: ...
    def OnModelLoadInfo(self, eventName: str, parameters: list) -> None: ...
    def OnModelObjectChanged(self, eventName: str, parameters: list) -> None: ...
    def OnModelObjectNumbered(self, eventName: str, parameters: list) -> None: ...
    def OnModelSave(self, eventName: str, parameters: list) -> None: ...
    def OnModelSaveAs(self, eventName: str, parameters: list) -> None: ...
    def OnModelSaveInfo(self, eventName: str, parameters: list) -> None: ...
    def OnModelUnloading(self, eventName: str, parameters: list) -> None: ...
    def OnModelUnloadingSync(self, eventName: str, parameters: list) -> None: ...
    def OnModelViewDrawn(self, viewId: int) -> None: ...
    def OnNumbering(self, eventName: str, parameters: list) -> None: ...
    def OnPointInputChangedEvent(self, eventName: str, parameters: list) -> None: ...
    def OnProjectInfoChanged(self, eventName: str, parameters: list) -> None: ...
    def OnSelectionChange(self, eventName: str, parameters: list) -> None: ...
    def OnTeklaStructuresExit(self, eventName: str, parameters: list) -> None: ...
    def OnTemporaryStatesChanged(self, ) -> None: ...
    def OnTrackEvent(self, eventName: str, parameters: list) -> None: ...
    def OnTsEventOccurred(self, eventInfo: str) -> None: ...
    def OnUndoClicked(self, ) -> None: ...
    def OnViewCameraChangedEvent(self, eventName: str, parameters: list) -> None: ...
    def OnViewClosed(self, viewId: int) -> None: ...
    def OnViewCreated(self, viewId: int) -> None: ...
    def OnViewDeleted(self, viewId: int) -> None: ...
    def OnViewModified(self, viewId: int) -> None: ...
    def OnViewOpened(self, viewId: int) -> None: ...
    def Register(self, ) -> None: ...
    def UnRegister(self, ) -> None: ...

class ExtensionIntersectsWithPlateException(ConnectiveGeometryException):
    """.NET: Tekla.Structures.Model.ExtensionIntersectsWithPlateException"""
    def __init__(self, *args) -> None: ...
    Message: str
    Data: IDictionary
    InnerException: Exception
    TargetSite: MethodBase
    StackTrace: str
    HelpLink: str
    Source: str
    HResult: int

class FacePerpendicularToIntersectionLineException(ConnectiveGeometryException):
    """.NET: Tekla.Structures.Model.FacePerpendicularToIntersectionLineException"""
    def __init__(self, *args) -> None: ...
    Message: str
    Data: IDictionary
    InnerException: Exception
    TargetSite: MethodBase
    StackTrace: str
    HelpLink: str
    Source: str
    HResult: int

class FacesAtAnObtuseAngleException(ConnectiveGeometryException):
    """.NET: Tekla.Structures.Model.FacesAtAnObtuseAngleException"""
    def __init__(self, *args) -> None: ...
    Message: str
    Data: IDictionary
    InnerException: Exception
    TargetSite: MethodBase
    StackTrace: str
    HelpLink: str
    Source: str
    HResult: int

class FacesTooNearEachOtherException(ConnectiveGeometryException):
    """.NET: Tekla.Structures.Model.FacesTooNearEachOtherException"""
    def __init__(self, *args) -> None: ...
    Message: str
    Data: IDictionary
    InnerException: Exception
    TargetSite: MethodBase
    StackTrace: str
    HelpLink: str
    Source: str
    HResult: int

class Fitting(bool):
    """.NET: Tekla.Structures.Model.Fitting"""
    def __init__(self, *args) -> None: ...
    Plane: Plane
    Father: ModelObject
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class GeneralConnectiveGeometryException(ConnectiveGeometryException):
    """.NET: Tekla.Structures.Model.GeneralConnectiveGeometryException"""
    def __init__(self, *args) -> None: ...
    Message: str
    Data: IDictionary
    InnerException: Exception
    TargetSite: MethodBase
    StackTrace: str
    HelpLink: str
    Source: str
    HResult: int

class GeometrySection:
    """.NET: Tekla.Structures.Model.GeometrySection"""
    def __init__(self, *args) -> None: ...
    Index: int
    GeometryNode: IGeometryNode

class GeometrySectionEnumerator:
    """.NET: Tekla.Structures.Model.GeometrySectionEnumerator"""
    def __init__(self, *args) -> None: ...
    Current: GeometrySection
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class Grid(GridBase):
    """.NET: Tekla.Structures.Model.Grid"""
    def __init__(self, *args) -> None: ...
    CoordinateX: str
    CoordinateY: str
    CoordinateZ: str
    LabelX: str
    LabelY: str
    LabelZ: str
    ExtensionLeftX: float
    ExtensionLeftY: float
    ExtensionLeftZ: float
    ExtensionRightX: float
    ExtensionRightY: float
    ExtensionRightZ: float
    ExtensionForMagneticArea: float
    Color: int
    IsMagnetic: bool
    Name: str
    FontSize: int
    FontColor: Color
    Origin: Point
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier

class GridBase(ModelObject):
    """.NET: Tekla.Structures.Model.GridBase"""
    def __init__(self, *args) -> None: ...
    IsMagnetic: bool
    Name: str
    FontSize: int
    FontColor: Color
    Origin: Point
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class GridCylindricalSurface(GridSurface):
    """.NET: Tekla.Structures.Model.GridCylindricalSurface"""
    def __init__(self, *args) -> None: ...
    CylinderBase: Arc
    CylinderHeight: float
    Parent: GridBase
    Label: str
    IsMagnetic: bool
    ExtensionLeft: float
    ExtensionRight: float
    ExtensionBelow: float
    ExtensionAbove: float
    DrawingVisibility: bool
    IsManual: bool
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Modify(self, ) -> bool: ...

class GridPlane(GridSurface):
    """.NET: Tekla.Structures.Model.GridPlane"""
    def __init__(self, *args) -> None: ...
    Plane: Plane
    Father: Grid
    Label: str
    IsMagnetic: bool
    ExtensionLeft: float
    ExtensionRight: float
    ExtensionBelow: float
    ExtensionAbove: float
    DrawingVisibility: bool
    Color: int
    ExtensionForMagneticArea: float
    Parent: GridBase
    IsManual: bool
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class GridSurface(ModelObject):
    """.NET: Tekla.Structures.Model.GridSurface"""
    def __init__(self, *args) -> None: ...
    Parent: GridBase
    Label: str
    IsMagnetic: bool
    ExtensionLeft: float
    ExtensionRight: float
    ExtensionBelow: float
    ExtensionAbove: float
    DrawingVisibility: bool
    IsManual: bool
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class HierarchicDefinition(ModelObject):
    """.NET: Tekla.Structures.Model.HierarchicDefinition"""
    def __init__(self, *args) -> None: ...
    Name: str
    CustomType: str
    HierarchyType: HierarchicDefinitionTypeEnum
    Father: HierarchicDefinition
    HierarchyIdentifier: str
    Drawable: bool
    HierarchicChildren: ArrayList
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def AddObjects(self, Objects: ArrayList) -> bool: ...
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def RemoveObjects(self, Objects: ArrayList) -> bool: ...
    def Select(self, ) -> bool: ...

class HierarchicDefinitionTypeEnum:
    """.NET: Tekla.Structures.Model.HierarchicDefinitionTypeEnum"""
    def __init__(self, *args) -> None: ...
    ...

class HierarchicObject(ModelObject):
    """.NET: Tekla.Structures.Model.HierarchicObject"""
    def __init__(self, *args) -> None: ...
    Name: str
    Definition: HierarchicDefinition
    Father: HierarchicObject
    HierarchicChildren: ArrayList
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def AddObjects(self, Objects: ArrayList) -> bool: ...
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def RemoveObjects(self, Objects: ArrayList) -> bool: ...
    def Select(self, ) -> bool: ...

class IAssemblable:
    """.NET: Tekla.Structures.Model.IAssemblable"""
    def __init__(self, *args) -> None: ...
    def GetAssembly(self, ) -> Assembly: ...

class IEvents:
    """.NET: Tekla.Structures.Model.IEvents"""
    def __init__(self, *args) -> None: ...
    def OnAnnotationSelectionChange(self, eventName: str, parameters: list) -> None: ...
    def OnClashCheckDone(self, eventName: str, parameters: list) -> None: ...
    def OnClashDetected(self, eventName: str, parameters: list) -> None: ...
    def OnClipBoxChanged(self, eventName: str, parameters: list) -> None: ...
    def OnClipPlaneChanged(self, eventName: str, parameters: list) -> None: ...
    def OnCommandStatusChange(self, eventName: str, parameters: list) -> None: ...
    def OnDbCommit(self, eventName: str, parameters: list) -> None: ...
    def OnHiddenObjectsChanged(self, ) -> None: ...
    def OnInterrupted(self, ) -> None: ...
    def OnModelLoad(self, eventName: str, parameters: list) -> None: ...
    def OnModelLoadInfo(self, eventName: str, parameters: list) -> None: ...
    def OnModelObjectChanged(self, eventName: str, parameters: list) -> None: ...
    def OnModelObjectNumbered(self, eventName: str, parameters: list) -> None: ...
    def OnModelSave(self, eventName: str, parameters: list) -> None: ...
    def OnModelSaveAs(self, eventName: str, parameters: list) -> None: ...
    def OnModelSaveInfo(self, eventName: str, parameters: list) -> None: ...
    def OnModelUnloading(self, eventName: str, parameters: list) -> None: ...
    def OnModelUnloadingSync(self, eventName: str, parameters: list) -> None: ...
    def OnModelViewDrawn(self, viewId: int) -> None: ...
    def OnNumbering(self, eventName: str, parameters: list) -> None: ...
    def OnPointInputChangedEvent(self, eventName: str, parameters: list) -> None: ...
    def OnProjectInfoChanged(self, eventName: str, parameters: list) -> None: ...
    def OnSelectionChange(self, eventName: str, parameters: list) -> None: ...
    def OnTeklaStructuresExit(self, eventName: str, parameters: list) -> None: ...
    def OnTemporaryStatesChanged(self, ) -> None: ...
    def OnTrackEvent(self, eventName: str, parameters: list) -> None: ...
    def OnTsEventOccurred(self, eventInfo: str) -> None: ...
    def OnUndoClicked(self, ) -> None: ...
    def OnViewCameraChangedEvent(self, eventName: str, parameters: list) -> None: ...
    def OnViewClosed(self, viewId: int) -> None: ...
    def OnViewCreated(self, viewId: int) -> None: ...
    def OnViewDeleted(self, viewId: int) -> None: ...
    def OnViewModified(self, viewId: int) -> None: ...
    def OnViewOpened(self, viewId: int) -> None: ...
    def Register(self, ) -> None: ...
    def UnRegister(self, ) -> None: ...

class IGeometryNode:
    """.NET: Tekla.Structures.Model.IGeometryNode"""
    def __init__(self, *args) -> None: ...
    IsAutomatic: bool
    def AcceptVisitor(self, visitor: IGeometryNodeVisitor) -> None: ...
    def Clone(self, ) -> IGeometryNode: ...

class IGeometryNodeVisitor:
    """.NET: Tekla.Structures.Model.IGeometryNodeVisitor"""
    def __init__(self, *args) -> None: ...
    def Visit(self, node: PolygonNode) -> None: ...

class ISharedModel:
    """.NET: Tekla.Structures.Model.ISharedModel"""
    def __init__(self, *args) -> None: ...
    Id: Guid
    Name: str
    Code: str
    Description: str
    Owner: str
    CreatedAt: DateTime
    CurrentUserRole: SharingRole

class ISharedModelState:
    """.NET: Tekla.Structures.Model.ISharedModelState"""
    def __init__(self, *args) -> None: ...
    State: SharedModelStateEnum
    SetBy: str
    LockOwner: str
    IsLockOwner: bool
    Comment: str
    PendingVersionsCount: Nullable

class ISharingEvents:
    """.NET: Tekla.Structures.Model.ISharingEvents"""
    def __init__(self, *args) -> None: ...
    ...

class ISharingLocation:
    """.NET: Tekla.Structures.Model.ISharingLocation"""
    def __init__(self, *args) -> None: ...
    Id: Guid
    Name: str
    DisplayName: str

class ISharingLocationsInformation:
    """.NET: Tekla.Structures.Model.ISharingLocationsInformation"""
    def __init__(self, *args) -> None: ...
    Locations: IReadOnlyList
    DefaultLocation: Guid

class ISharingResult:
    """.NET: Tekla.Structures.Model.ISharingResult | Tekla.Structures.Model.ISharingResult`1"""
    def __init__(self, *args) -> None: ...
    Code: SharingResultCode
    ErrorDetails: str
    State: SharingResultState
    Notifications: IEnumerable
    ErrorPath: str
    PathLengthLimit: int
    Data: T

class ISharingUpdate:
    """.NET: Tekla.Structures.Model.ISharingUpdate"""
    def __init__(self, *args) -> None: ...
    Id: Guid
    Type: SharingUpdateType
    Number: int
    Code: str
    Comment: str
    CreatedAt: DateTime
    CreatedBy: str

class InputItem:
    """.NET: Tekla.Structures.Model.InputItem"""
    def __init__(self, *args) -> None: ...
    def GetData(self, ) -> object: ...
    def GetInputType(self, ) -> InputTypeEnum: ...

class InvalidCurveCombinationException(LoftedPlateOperationException):
    """.NET: Tekla.Structures.Model.InvalidCurveCombinationException"""
    def __init__(self, *args) -> None: ...
    Message: str
    Data: IDictionary
    InnerException: Exception
    TargetSite: MethodBase
    StackTrace: str
    HelpLink: str
    Source: str
    HResult: int

class InvalidFacePointsException(ConnectiveGeometryException):
    """.NET: Tekla.Structures.Model.InvalidFacePointsException"""
    def __init__(self, *args) -> None: ...
    Message: str
    Data: IDictionary
    InnerException: Exception
    TargetSite: MethodBase
    StackTrace: str
    HelpLink: str
    Source: str
    HResult: int

class InvalidRadiusException(ConnectiveGeometryException):
    """.NET: Tekla.Structures.Model.InvalidRadiusException"""
    def __init__(self, *args) -> None: ...
    Message: str
    Data: IDictionary
    InnerException: Exception
    TargetSite: MethodBase
    StackTrace: str
    HelpLink: str
    Source: str
    HResult: int

class Load(ModelObject):
    """.NET: Tekla.Structures.Model.Load"""
    def __init__(self, *args) -> None: ...
    FatherId: Identifier
    Spanning: LoadSpanningEnum
    PrimaryAxisDirection: Vector
    AutomaticPrimaryAxisWeight: bool
    Weight: float
    LoadDispersionAngle: float
    CreateFixedSupportConditionsAutomatically: bool
    LoadAttachment: LoadAttachmentEnum
    PartNames: LoadPartNamesEnum
    PartFilter: str
    BoundingBoxDx: float
    BoundingBoxDy: float
    BoundingBoxDz: float
    Group: LoadGroup
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier

class LoadArea(Load):
    """.NET: Tekla.Structures.Model.LoadArea"""
    def __init__(self, *args) -> None: ...
    Position1: Point
    Position2: Point
    Position3: Point
    P1: Vector
    P2: Vector
    P3: Vector
    P4: Vector
    LoadForm: AreaLoadFormEnum
    DistanceA: float
    FatherId: Identifier
    Spanning: LoadSpanningEnum
    PrimaryAxisDirection: Vector
    AutomaticPrimaryAxisWeight: bool
    Weight: float
    LoadDispersionAngle: float
    CreateFixedSupportConditionsAutomatically: bool
    LoadAttachment: LoadAttachmentEnum
    PartNames: LoadPartNamesEnum
    PartFilter: str
    BoundingBoxDx: float
    BoundingBoxDy: float
    BoundingBoxDz: float
    Group: LoadGroup
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class LoadGroup(ModelObject):
    """.NET: Tekla.Structures.Model.LoadGroup"""
    def __init__(self, *args) -> None: ...
    GroupName: str
    GroupType: LoadGroupType
    Direction: LoadGroupDirection
    Compatible: int
    Incompatible: int
    Color: Colors
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class LoadLine(Load):
    """.NET: Tekla.Structures.Model.LoadLine"""
    def __init__(self, *args) -> None: ...
    Position1: Point
    Position2: Point
    P1: Vector
    P2: Vector
    Torsion1: float
    Torsion2: float
    LoadForm: LineLoadFormEnum
    DistanceA: float
    DistanceB: float
    FatherId: Identifier
    Spanning: LoadSpanningEnum
    PrimaryAxisDirection: Vector
    AutomaticPrimaryAxisWeight: bool
    Weight: float
    LoadDispersionAngle: float
    CreateFixedSupportConditionsAutomatically: bool
    LoadAttachment: LoadAttachmentEnum
    PartNames: LoadPartNamesEnum
    PartFilter: str
    BoundingBoxDx: float
    BoundingBoxDy: float
    BoundingBoxDz: float
    Group: LoadGroup
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class LoadPoint(Load):
    """.NET: Tekla.Structures.Model.LoadPoint"""
    def __init__(self, *args) -> None: ...
    Position: Point
    P: Vector
    Moment: Vector
    FatherId: Identifier
    Spanning: LoadSpanningEnum
    PrimaryAxisDirection: Vector
    AutomaticPrimaryAxisWeight: bool
    Weight: float
    LoadDispersionAngle: float
    CreateFixedSupportConditionsAutomatically: bool
    LoadAttachment: LoadAttachmentEnum
    PartNames: LoadPartNamesEnum
    PartFilter: str
    BoundingBoxDx: float
    BoundingBoxDy: float
    BoundingBoxDz: float
    Group: LoadGroup
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class LoadTemperature(Load):
    """.NET: Tekla.Structures.Model.LoadTemperature"""
    def __init__(self, *args) -> None: ...
    Spanning: LoadSpanningEnum
    PrimaryAxisDirection: Vector
    AutomaticPrimaryAxisWeight: bool
    Weight: float
    LoadDispersionAngle: float
    CreateFixedSupportConditionsAutomatically: bool
    Position1: Point
    Position2: Point
    TemperatureChangeForAxialElongation: float
    TemperatureDifferentialTopToBottom: float
    TemperatureDifferentialSideToSide: float
    InitialAxialElongation: float
    FatherId: Identifier
    LoadAttachment: LoadAttachmentEnum
    PartNames: LoadPartNamesEnum
    PartFilter: str
    BoundingBoxDx: float
    BoundingBoxDy: float
    BoundingBoxDz: float
    Group: LoadGroup
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class LoadUniform(Load):
    """.NET: Tekla.Structures.Model.LoadUniform"""
    def __init__(self, *args) -> None: ...
    Polygon: Polygon
    P1: Vector
    DistanceA: float
    FatherId: Identifier
    Spanning: LoadSpanningEnum
    PrimaryAxisDirection: Vector
    AutomaticPrimaryAxisWeight: bool
    Weight: float
    LoadDispersionAngle: float
    CreateFixedSupportConditionsAutomatically: bool
    LoadAttachment: LoadAttachmentEnum
    PartNames: LoadPartNamesEnum
    PartFilter: str
    BoundingBoxDx: float
    BoundingBoxDy: float
    BoundingBoxDz: float
    Group: LoadGroup
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class LoftedPlate(Part):
    """.NET: Tekla.Structures.Model.LoftedPlate"""
    def __init__(self, *args) -> None: ...
    BaseCurves: List
    FaceType: LoftedPlateFaceTypeEnum
    Profile: Profile
    Material: Material
    DeformingData: DeformingData
    PartNumber: NumberingSeries
    AssemblyNumber: NumberingSeries
    Name: str
    Class: str
    Finish: str
    CastUnitType: CastUnitTypeEnum
    PourPhase: int
    Position: Position
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class LoftedPlateOperationException(Exception):
    """.NET: Tekla.Structures.Model.LoftedPlateOperationException"""
    def __init__(self, *args) -> None: ...
    Message: str
    Data: IDictionary
    InnerException: Exception
    TargetSite: MethodBase
    StackTrace: str
    HelpLink: str
    Source: str
    HResult: int

class LogicalWeld(BaseWeld):
    """.NET: Tekla.Structures.Model.LogicalWeld"""
    def __init__(self, *args) -> None: ...
    MainObject: ModelObject
    SecondaryObject: ModelObject
    SizeAbove: float
    AdditionalSizeAbove: float
    TypeAbove: WeldTypeEnum
    AngleAbove: float
    LengthAbove: float
    ContourAbove: WeldContourEnum
    FinishAbove: WeldFinishEnum
    PitchAbove: float
    SizeBelow: float
    AdditionalSizeBelow: float
    TypeBelow: WeldTypeEnum
    AngleBelow: float
    LengthBelow: float
    ContourBelow: WeldContourEnum
    FinishBelow: WeldFinishEnum
    PitchBelow: float
    ShopWeld: bool
    AroundWeld: bool
    StitchWeld: bool
    RootOpeningAbove: float
    RootFaceAbove: float
    EffectiveThroatAbove: float
    IncrementAmountAbove: int
    RootOpeningBelow: float
    RootFaceBelow: float
    EffectiveThroatBelow: float
    IncrementAmountBelow: int
    ElectrodeClassification: WeldElectrodeClassificationEnum
    ElectrodeStrength: float
    ElectrodeCoefficient: float
    ProcessType: WeldProcessTypeEnum
    NDTInspection: WeldNDTInspectionEnum
    ConnectAssemblies: bool
    ReferenceText: str
    PrefixAboveLine: str
    PrefixBelowLine: str
    Standard: str
    WeldNumber: int
    WeldNumberPrefix: str
    IntermittentType: WeldIntermittentTypeEnum
    Placement: WeldPlacementTypeEnum
    Preparation: WeldPreparationTypeEnum
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def AddWeld(self, Weld: BaseWeld) -> bool: ...
    def Delete(self, ) -> bool: ...
    def Explode(self, ) -> bool: ...
    def GetMainWeld(self, ) -> BaseWeld: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def RemoveWeld(self, Weld: BaseWeld) -> bool: ...
    def Select(self, ChildWeld: BaseWeld) -> bool: ...
    def SetMainWeld(self, Weld: BaseWeld) -> bool: ...

class Material:
    """.NET: Tekla.Structures.Model.Material"""
    def __init__(self, *args) -> None: ...
    MaterialString: str

class Model:
    """.NET: Tekla.Structures.Model.Model"""
    def __init__(self, *args) -> None: ...
    def CommitChanges(self, Message: str) -> bool: ...
    def FetchModelObjects(self, Guids: List, SelectInstances: bool) -> List: ...
    def GetClashCheckHandler(self, ) -> ClashCheckHandler: ...
    def GetConnectionStatus(self, ) -> bool: ...
    def GetGUIDByIdentifier(self, identifier: Identifier) -> str: ...
    def GetIdentifierByGUID(self, guid: str) -> Identifier: ...
    def GetInfo(self, ) -> ModelInfo: ...
    def GetModelObjectSelector(self, ) -> ModelObjectSelector: ...
    def GetPhases(self, ) -> PhaseCollection: ...
    def GetProjectInfo(self, ) -> ProjectInfo: ...
    def GetReportPropertyDouble(self, identifiers: IList, property: str) -> List: ...
    def GetReportPropertyInt(self, identifiers: IList, property: str) -> List: ...
    def GetReportPropertyStr(self, identifiers: IList, property: str) -> List: ...
    def GetWorkPlaneHandler(self, ) -> WorkPlaneHandler: ...
    def SelectModelObject(self, ID: Identifier) -> ModelObject: ...

class ModelHandler:
    """.NET: Tekla.Structures.Model.ModelHandler"""
    def __init__(self, *args) -> None: ...
    def Close(self, ) -> None: ...
    def CreateNewMultiUserModel(self, ModelName: str, ModelFolder: str, ServerName: str) -> bool: ...
    def CreateNewSingleUserModel(self, ModelName: str, ModelFolder: str, TemplateNameOrTemplatePath: str) -> bool: ...
    def IsModelAutoSaved(self, ModelFolder: str) -> bool: ...
    def IsModelSaved(self, ) -> bool: ...
    def Open(self, ModelFolder: str, OpenAutoSaved: bool) -> bool: ...
    def Save(self, Comment: str, User: str, Reason: str) -> bool: ...

class ModelInfo:
    """.NET: Tekla.Structures.Model.ModelInfo"""
    def __init__(self, *args) -> None: ...
    NorthDirection: float
    ModelPath: str
    ModelName: str
    CurrentPhase: int
    SharedModel: bool
    SingleUserModel: bool

class ModelObject(object):
    """.NET: Tekla.Structures.Model.ModelObject"""
    def __init__(self, *args) -> None: ...
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def CompareTo(self, obj: object) -> int: ...
    def Delete(self, ) -> bool: ...
    def Equals(self, other: ModelObject) -> bool: ...
    def GetAllReportProperties(self, stringNames: ArrayList, doubleNames: ArrayList, integerNames: ArrayList, values: Hashtable) -> bool: ...
    def GetAllUserProperties(self, values: Hashtable) -> bool: ...
    def GetChildren(self, ) -> ModelObjectEnumerator: ...
    def GetCoordinateSystem(self, ) -> CoordinateSystem: ...
    def GetCustomObjectType(self, ) -> str: ...
    def GetDoubleReportProperties(self, names: ArrayList, values: Hashtable) -> bool: ...
    def GetDoubleUserProperties(self, values: Hashtable) -> bool: ...
    def GetDynamicStringProperty(self, name: str, value: str) -> bool: ...
    def GetFatherComponent(self, ) -> BaseComponent: ...
    def GetHierarchicObjects(self, ) -> ModelObjectEnumerator: ...
    def GetIntegerReportProperties(self, names: ArrayList, values: Hashtable) -> bool: ...
    def GetIntegerUserProperties(self, values: Hashtable) -> bool: ...
    def GetPhase(self, phase: Phase) -> bool: ...
    def GetReportProperty(self, name: str, value: str) -> bool: ...
    def GetStringReportProperties(self, names: ArrayList, values: Hashtable) -> bool: ...
    def GetStringUserProperties(self, values: Hashtable) -> bool: ...
    def GetUserProperty(self, name: str, value: str) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...
    def SetCustomObjectType(self, type: str) -> bool: ...
    def SetDynamicStringProperty(self, name: str, value: str) -> bool: ...
    def SetLabel(self, label: str) -> bool: ...
    def SetPhase(self, phase: Phase) -> bool: ...
    def SetUserProperties(self, stringPropertyNames: List, stringValues: List, doublePropertyNames: List, doubleValues: List, intPropertyNames: List, intValues: List) -> bool: ...
    def SetUserProperty(self, name: str, value: str) -> bool: ...

class ModelObjectEnumerator:
    """.NET: Tekla.Structures.Model.ModelObjectEnumerator"""
    def __init__(self, *args) -> None: ...
    SelectInstances: bool
    AutoFetch: bool
    Current: ModelObject
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetSize(self, ) -> int: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class ModelObjectSelector:
    """.NET: Tekla.Structures.Model.ModelObjectSelector"""
    def __init__(self, *args) -> None: ...
    def GetAllObjects(self, ) -> ModelObjectEnumerator: ...
    def GetAllObjectsWithType(self, Enum: ModelObjectEnum) -> ModelObjectEnumerator: ...
    def GetEnumerator(self, ) -> ModelObjectEnumerator: ...
    def GetFilteredObjectsWithType(self, Enum: ModelObjectEnum, FilterName: str) -> ModelObjectEnumerator: ...
    def GetObjectsByBoundingBox(self, MinPoint: Point, MaxPoint: Point) -> ModelObjectEnumerator: ...
    def GetObjectsByFilter(self, FilterExpression: FilterExpression) -> ModelObjectEnumerator: ...
    def GetObjectsByFilterName(self, FilterName: str) -> ModelObjectEnumerator: ...

class ModelSharingHandler:
    """.NET: Tekla.Structures.Model.ModelSharingHandler"""
    def __init__(self, *args) -> None: ...
    def CreateBaselineAsync(self, code: str, comment: str, releaseNextWriteOutComment: str) -> Task: ...
    def ExcludeAndOpen(self, modelPath: str) -> ISharingResult: ...
    def GetLocationsAsync(self, ) -> Task: ...
    def GetModelsAsync(self, ) -> Task: ...
    def GetSharingEvents(self, ) -> ISharingEvents: ...
    def GetUpdatesAsync(self, modelId: Nullable) -> Task: ...
    def InviteUserAsync(self, userEmail: str, role: SharingRole, sendEmail: bool, customEmailMessage: str, modelId: Nullable) -> Task: ...
    def JoinAsync(self, modelId: Guid, joinFolder: str, targetUpdate: Nullable) -> Task: ...
    def ReadInAsync(self, targetUpdate: Nullable) -> Task: ...
    def ReleaseNextWriteOutAsync(self, comment: str) -> Task: ...
    def RemoveModelAsync(self, modelId: Guid) -> Task: ...
    def ReserveNextWriteOutAsync(self, comment: str) -> Task: ...
    def StartSharingAsync(self, code: str, description: str, location: Nullable) -> Task: ...
    def WriteOutAsync(self, code: str, comment: str, releaseNextWriteOutComment: str) -> Task: ...

class NullRulingException(LoftedPlateOperationException):
    """.NET: Tekla.Structures.Model.NullRulingException"""
    def __init__(self, *args) -> None: ...
    Message: str
    Data: IDictionary
    InnerException: Exception
    TargetSite: MethodBase
    StackTrace: str
    HelpLink: str
    Source: str
    HResult: int

class NumberingSeries:
    """.NET: Tekla.Structures.Model.NumberingSeries"""
    def __init__(self, *args) -> None: ...
    Prefix: str
    StartNumber: int

class NumberingSeriesNullable:
    """.NET: Tekla.Structures.Model.NumberingSeriesNullable"""
    def __init__(self, *args) -> None: ...
    Prefix: str
    StartNumber: Nullable

class Object:
    """.NET: Tekla.Structures.Model.Object"""
    def __init__(self, *args) -> None: ...
    Identifier: Identifier

class Offset:
    """.NET: Tekla.Structures.Model.Offset"""
    def __init__(self, *args) -> None: ...
    Dx: float
    Dy: float
    Dz: float

class Part(ModelObject):
    """.NET: Tekla.Structures.Model.Part"""
    def __init__(self, *args) -> None: ...
    Profile: Profile
    Material: Material
    DeformingData: DeformingData
    PartNumber: NumberingSeries
    AssemblyNumber: NumberingSeries
    Name: str
    Class: str
    Finish: str
    CastUnitType: CastUnitTypeEnum
    PourPhase: int
    Position: Position
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def CompareTo(self, partToCompare: Part) -> bool: ...
    def GetAssembly(self, ) -> Assembly: ...
    def GetBolts(self, ) -> ModelObjectEnumerator: ...
    def GetBooleans(self, ) -> ModelObjectEnumerator: ...
    def GetCenterLine(self, withCutsFittings: bool) -> ArrayList: ...
    def GetComponents(self, ) -> ModelObjectEnumerator: ...
    def GetDSTVCoordinateSystem(self, ) -> CoordinateSystem: ...
    def GetPartMark(self, ) -> str: ...
    def GetPours(self, ) -> ModelObjectEnumerator: ...
    def GetReferenceLine(self, withCutsFittings: bool) -> ArrayList: ...
    def GetReinforcements(self, ) -> ModelObjectEnumerator: ...
    def GetSolid(self, solidCreationType: SolidCreationTypeEnum) -> Solid: ...
    def GetSurfaceObjects(self, ) -> ModelObjectEnumerator: ...
    def GetSurfaceTreatments(self, ) -> ModelObjectEnumerator: ...
    def GetWelds(self, ) -> ModelObjectEnumerator: ...

class Phase:
    """.NET: Tekla.Structures.Model.Phase"""
    def __init__(self, *args) -> None: ...
    PhaseNumber: int
    PhaseName: str
    PhaseComment: str
    IsCurrentPhase: int
    def Delete(self, ) -> bool: ...
    def GetUserProperty(self, Name: str, Value: str) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...
    def SetUserProperty(self, Name: str, Value: str) -> bool: ...

class PhaseCollection:
    """.NET: Tekla.Structures.Model.PhaseCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    IsSynchronized: bool
    SyncRoot: object
    def CopyTo(self, Array: Array, Index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...

class Plane:
    """.NET: Tekla.Structures.Model.Plane"""
    def __init__(self, *args) -> None: ...
    Origin: Point
    AxisX: Vector
    AxisY: Vector

class PlateIntersectsWithIntersectionLineException(ConnectiveGeometryException):
    """.NET: Tekla.Structures.Model.PlateIntersectsWithIntersectionLineException"""
    def __init__(self, *args) -> None: ...
    Message: str
    Data: IDictionary
    InnerException: Exception
    TargetSite: MethodBase
    StackTrace: str
    HelpLink: str
    Source: str
    HResult: int

class PointCloud:
    """.NET: Tekla.Structures.Model.PointCloud"""
    def __init__(self, *args) -> None: ...
    Guid: Guid
    OriginalPath: str
    Url: str
    TcProjectId: str
    TcPointCloudGuid: str
    Name: str
    LocationBy: Guid
    UseAutoCreatedBasePoint: bool
    BoundingBox: AABB
    Scale: float
    OffsetX: float
    OffsetY: float
    OffsetZ: float
    RotationZ: float
    def Attach(self, ) -> bool: ...
    def AttachComplete(self, ) -> bool: ...
    def Detach(self, ) -> bool: ...
    @staticmethod
    def GetPointClouds() -> List: ...
    def GetVisibleInViews(self, ) -> List: ...
    def Select(self, ) -> bool: ...
    def SetVisibility(self, views: List, visible: bool) -> bool: ...

class PolyBeam(Part):
    """.NET: Tekla.Structures.Model.PolyBeam"""
    def __init__(self, *args) -> None: ...
    Type: PolyBeamTypeEnum
    Contour: Contour
    StartLevelName: str
    EndLevelName: str
    StartLevelOffset: float
    EndLevelOffset: float
    Profile: Profile
    Material: Material
    DeformingData: DeformingData
    PartNumber: NumberingSeries
    AssemblyNumber: NumberingSeries
    Name: str
    Class: str
    Finish: str
    CastUnitType: CastUnitTypeEnum
    PourPhase: int
    Position: Position
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def AddContourPoint(self, contourPoint: ContourPoint) -> bool: ...
    def Delete(self, ) -> bool: ...
    def GetCenterLinePolycurve(self, ) -> Polycurve: ...
    def GetPolybeamCoordinateSystems(self, ) -> ArrayList: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class Polygon:
    """.NET: Tekla.Structures.Model.Polygon"""
    def __init__(self, *args) -> None: ...
    Points: ArrayList

class PolygonNode:
    """.NET: Tekla.Structures.Model.PolygonNode"""
    def __init__(self, *args) -> None: ...
    IsAutomatic: bool
    Contour: Contour
    def AcceptVisitor(self, visitor: IGeometryNodeVisitor) -> None: ...
    def Clone(self, ) -> IGeometryNode: ...

class PolygonWeld(BaseWeld):
    """.NET: Tekla.Structures.Model.PolygonWeld"""
    def __init__(self, *args) -> None: ...
    Polygon: Polygon
    MainObject: ModelObject
    SecondaryObject: ModelObject
    SizeAbove: float
    AdditionalSizeAbove: float
    TypeAbove: WeldTypeEnum
    AngleAbove: float
    LengthAbove: float
    ContourAbove: WeldContourEnum
    FinishAbove: WeldFinishEnum
    PitchAbove: float
    SizeBelow: float
    AdditionalSizeBelow: float
    TypeBelow: WeldTypeEnum
    AngleBelow: float
    LengthBelow: float
    ContourBelow: WeldContourEnum
    FinishBelow: WeldFinishEnum
    PitchBelow: float
    ShopWeld: bool
    AroundWeld: bool
    StitchWeld: bool
    RootOpeningAbove: float
    RootFaceAbove: float
    EffectiveThroatAbove: float
    IncrementAmountAbove: int
    RootOpeningBelow: float
    RootFaceBelow: float
    EffectiveThroatBelow: float
    IncrementAmountBelow: int
    ElectrodeClassification: WeldElectrodeClassificationEnum
    ElectrodeStrength: float
    ElectrodeCoefficient: float
    ProcessType: WeldProcessTypeEnum
    NDTInspection: WeldNDTInspectionEnum
    ConnectAssemblies: bool
    ReferenceText: str
    PrefixAboveLine: str
    PrefixBelowLine: str
    Standard: str
    WeldNumber: int
    WeldNumberPrefix: str
    IntermittentType: WeldIntermittentTypeEnum
    Placement: WeldPlacementTypeEnum
    Preparation: WeldPreparationTypeEnum
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def GetLogicalWeld(self, LogicalWeld: LogicalWeld) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class Polymesh:
    """.NET: Tekla.Structures.Model.Polymesh"""
    def __init__(self, *args) -> None: ...
    Brep: FacetedBrep
    @staticmethod
    def CompareFingerprints(fingerprint1: str, fingerprint2: str) -> bool: ...
    @staticmethod
    def Convert(input: dotPolymesh_t) -> List: ...
    @staticmethod
    def ConvertInvalidInfoFromStruct(input: dotPolymeshValidateInvalidInfo_t) -> List: ...
    @staticmethod
    def ConvertToStruct(brep: FacetedBrep, output: dotPolymesh_t) -> None: ...
    @staticmethod
    def Fingerprint(brep: FacetedBrep) -> str: ...
    def FromStruct(self, input: dotPolymesh_t) -> None: ...
    @staticmethod
    def GetSolidBrep(inBrep: FacetedBrep, outBrep: FacetedBrep) -> bool: ...
    def ToStruct(self, output: dotPolymesh_t) -> None: ...
    @staticmethod
    def Validate(brep: FacetedBrep, checkCriteria: PolymeshCheckerFlags, invalidInfo: List) -> bool: ...

class PolymeshEnumerator:
    """.NET: Tekla.Structures.Model.PolymeshEnumerator"""
    def __init__(self, *args) -> None: ...
    Current: object
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class Position:
    """.NET: Tekla.Structures.Model.Position"""
    def __init__(self, *args) -> None: ...
    PlaneOffset: float
    DepthOffset: float
    RotationOffset: float
    Plane: PlaneEnum
    Depth: DepthEnum
    Rotation: RotationEnum

class PourBreak(ModelObject):
    """.NET: Tekla.Structures.Model.PourBreak"""
    def __init__(self, *args) -> None: ...
    Polymesh: FacetedBrep
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class PourObject(ModelObject):
    """.NET: Tekla.Structures.Model.PourObject"""
    def __init__(self, *args) -> None: ...
    Class: int
    PourNumber: str
    PourType: str
    ConcreteMixture: str
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def GetAssembly(self, ) -> Assembly: ...
    def GetFatherPourUnit(self, ) -> PourUnit: ...
    def GetObjects(self, ) -> ModelObjectEnumerator: ...
    def GetParts(self, ) -> ModelObjectEnumerator: ...
    def GetPourPolymeshes(self, ) -> PolymeshEnumerator: ...
    def GetSolid(self, ) -> Solid: ...
    def GetSurfaceObjects(self, ) -> ModelObjectEnumerator: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class PourUnit(ModelObject):
    """.NET: Tekla.Structures.Model.PourUnit"""
    def __init__(self, *args) -> None: ...
    Name: str
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def GetObjects(self, ) -> ModelObjectEnumerator: ...
    def GetPourObject(self, ) -> PourObject: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class Profile:
    """.NET: Tekla.Structures.Model.Profile"""
    def __init__(self, *args) -> None: ...
    ProfileString: str
    @staticmethod
    def FormatProfileString(profileString: str) -> str: ...
    @staticmethod
    def ParseProfileString(profileString: str) -> str: ...

class ProjectInfo:
    """.NET: Tekla.Structures.Model.ProjectInfo"""
    def __init__(self, *args) -> None: ...
    Description: str
    StartDate: str
    EndDate: str
    Object: str
    Designer: str
    Location: str
    Address: str
    PostalBox: str
    Town: str
    Region: str
    PostalCode: str
    Country: str
    Builder: str
    Name: str
    ProjectNumber: str
    ModelSharingLocalPath: DirectoryInfo
    ModelSharingServerPath: Uri
    Info1: str
    Info2: str
    GUID: str
    @staticmethod
    def GetBasePointByGuid(guid: Guid) -> BasePoint: ...
    @staticmethod
    def GetBasePointByName(name: str) -> BasePoint: ...
    @staticmethod
    def GetBasePoints() -> List: ...
    @staticmethod
    def GetCurrentCoordsysBasePoint() -> BasePoint: ...
    def GetDoubleUserProperties(self, Values: Hashtable) -> bool: ...
    def GetDynamicStringProperty(self, Name: str, Value: str) -> bool: ...
    def GetIntegerUserProperties(self, Values: Hashtable) -> bool: ...
    @staticmethod
    def GetProjectBasePoint() -> BasePoint: ...
    def GetStringUserProperties(self, Values: Hashtable) -> bool: ...
    def GetUserProperty(self, Name: str, Value: str) -> bool: ...
    def Modify(self, ) -> bool: ...
    @staticmethod
    def SetCurrentCoordsysToBasePoint(basePoint: BasePoint) -> bool: ...
    def SetDynamicStringProperty(self, Name: str, Value: str) -> bool: ...
    def SetUserProperty(self, Name: str, Value: str) -> bool: ...

class RadialGrid(GridBase):
    """.NET: Tekla.Structures.Model.RadialGrid"""
    def __init__(self, *args) -> None: ...
    IsMagnetic: bool
    RadialCoordinates: str
    AngularCoordinates: str
    CoordinateZ: str
    RadialLabels: str
    AngularLabels: str
    LabelZ: str
    ArcStartExtension: float
    AngularLinesStartExtension: float
    ExtensionBelowZ: float
    ArcEndExtension: float
    AngularLinesEndExtension: float
    ExtensionAboveZ: float
    Color: Color
    Name: str
    FontSize: int
    FontColor: Color
    Origin: Point
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier

class RebarComplexGeometry:
    """.NET: Tekla.Structures.Model.RebarComplexGeometry"""
    def __init__(self, *args) -> None: ...
    Legs: List
    Diameter: float
    BendingRadiuses: List
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToString(self, ) -> str: ...

class RebarCranking:
    """.NET: Tekla.Structures.Model.RebarCranking"""
    def __init__(self, *args) -> None: ...
    CrankSide: CrankSideEnum
    CrankRotation: float
    CrankStraightLength: float
    CrankedLengthType: CrankedLengthTypeEnum
    CrankedRatio: float
    CrankedDistance: float
    CrankedOffset: float
    CrankingType: CrankingTypeEnum

class RebarCrankingNullable:
    """.NET: Tekla.Structures.Model.RebarCrankingNullable"""
    def __init__(self, *args) -> None: ...
    CrankRotation: Nullable
    CrankStraightLength: Nullable
    CrankedLengthType: Nullable
    CrankedRatio: Nullable
    CrankedDistance: Nullable
    CrankedOffset: Nullable
    CrankingType: Nullable

class RebarEndDetailModifier(BaseRebarModifier):
    """.NET: Tekla.Structures.Model.RebarEndDetailModifier"""
    def __init__(self, *args) -> None: ...
    RebarHook: RebarHookDataNullable
    RebarThreading: RebarThreadingDataNullable
    RebarLengthAdjustment: RebarLengthAdjustmentDataNullable
    RebarCranking: RebarCrankingNullable
    EndType: Nullable
    Father: RebarSet
    Curve: Contour
    BarsAffected: BarsAffectedEnum
    FirstAffectedBar: int
    FollowEdges: bool
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def GetAffectedBars(self, whichEnd: AffectedRebarEnum) -> ModelObjectEnumerator: ...

class RebarGeometry:
    """.NET: Tekla.Structures.Model.RebarGeometry"""
    def __init__(self, *args) -> None: ...
    Shape: PolyLine
    Diameter: float
    BendingRadiuses: ArrayList

class RebarGroup(BaseRebarGroup):
    """.NET: Tekla.Structures.Model.RebarGroup"""
    def __init__(self, *args) -> None: ...
    Polygons: ArrayList
    StirrupType: RebarGroupStirrupTypeEnum
    Size: str
    StartHook: RebarHookData
    EndHook: RebarHookData
    FromPlaneOffset: float
    StartFromPlaneOffset: float
    EndFromPlaneOffset: float
    ExcludeType: ExcludeTypeEnum
    SpacingType: RebarGroupSpacingTypeEnum
    Spacings: ArrayList
    StartPoint: Point
    EndPoint: Point
    Father: ModelObject
    Grade: str
    Name: str
    Class: int
    NumberingSeries: NumberingSeries
    OnPlaneOffsets: ArrayList
    StartPointOffsetType: RebarOffsetTypeEnum
    StartPointOffsetValue: float
    EndPointOffsetType: RebarOffsetTypeEnum
    EndPointOffsetValue: float
    RadiusValues: ArrayList
    InputPointDeformingState: DeformingType
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class RebarGuideline:
    """.NET: Tekla.Structures.Model.RebarGuideline"""
    def __init__(self, *args) -> None: ...
    Id: int
    Curve: Contour
    Spacing: RebarSpacing
    FollowEdges: bool
    ChamferType: GuidelineChamferTypeEnum

class RebarHookData:
    """.NET: Tekla.Structures.Model.RebarHookData"""
    def __init__(self, *args) -> None: ...
    Shape: RebarHookShapeEnum
    Angle: float
    Radius: float
    Length: float

class RebarHookDataNullable:
    """.NET: Tekla.Structures.Model.RebarHookDataNullable"""
    def __init__(self, *args) -> None: ...
    Shape: Nullable
    Angle: Nullable
    Radius: Nullable
    Length: Nullable
    Rotation: Nullable

class RebarLapping:
    """.NET: Tekla.Structures.Model.RebarLapping"""
    def __init__(self, *args) -> None: ...
    LapLength: float
    LapSide: LapSideEnum
    LapPlacement: LapPlacementEnum
    LappingType: LappingTypeEnum

class RebarLeg:
    """.NET: Tekla.Structures.Model.RebarLeg"""
    def __init__(self, *args) -> None: ...
    Curve: ICurve
    Origin: OriginEnum

class RebarLegFace:
    """.NET: Tekla.Structures.Model.RebarLegFace"""
    def __init__(self, *args) -> None: ...
    Id: int
    OffsetType: OffsetTypeEnum
    Offset: float
    AdditonalOffset: float
    LayerOrderNumber: int
    Reversed: bool
    Contour: Contour
    Frozen: bool

class RebarLegSurfaceObject(SurfaceObject):
    """.NET: Tekla.Structures.Model.RebarLegSurfaceObject"""
    def __init__(self, *args) -> None: ...
    RebarSet: RebarSet
    LayerNumber: int
    OffsetType: OffsetTypeEnum
    Offset: float
    AdditionalOffset: float
    Frozen: bool
    Polymesh: FacetedBrep
    Class: str
    Name: str
    CreateHoles: bool
    Type: str
    Father: ModelObject
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class RebarLengthAdjustmentDataNullable:
    """.NET: Tekla.Structures.Model.RebarLengthAdjustmentDataNullable"""
    def __init__(self, *args) -> None: ...
    AdjustmentType: Nullable
    AdjustmentLength: Nullable

class RebarMesh(Reinforcement):
    """.NET: Tekla.Structures.Model.RebarMesh"""
    def __init__(self, *args) -> None: ...
    MeshType: RebarMeshTypeEnum
    LongitudinalSpacingMethod: RebarMeshSpacingMethodEnum
    Polygon: Polygon
    LongitudinalDistances: ArrayList
    CrossDistances: ArrayList
    FromPlaneOffset: float
    StartFromPlaneOffset: float
    EndFromPlaneOffset: float
    StartPoint: Point
    EndPoint: Point
    LeftOverhangLongitudinal: float
    LeftOverhangCross: float
    RightOverhangLongitudinal: float
    RightOverhangCross: float
    LongitudinalSize: str
    CrossSize: str
    Width: float
    Length: float
    CutByFatherPartCuts: bool
    CatalogName: str
    CrossBarLocation: RebarMeshCrossBarLocationEnum
    StartHook: RebarHookData
    EndHook: RebarHookData
    Father: ModelObject
    Grade: str
    Name: str
    Class: int
    NumberingSeries: NumberingSeries
    OnPlaneOffsets: ArrayList
    StartPointOffsetType: RebarOffsetTypeEnum
    StartPointOffsetValue: float
    EndPointOffsetType: RebarOffsetTypeEnum
    EndPointOffsetValue: float
    RadiusValues: ArrayList
    InputPointDeformingState: DeformingType
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class RebarOffsets:
    """.NET: Tekla.Structures.Model.RebarOffsets"""
    def __init__(self, *args) -> None: ...
    AtDepth: Nullable
    Start: Nullable
    End: Nullable

class RebarProperties:
    """.NET: Tekla.Structures.Model.RebarProperties"""
    def __init__(self, *args) -> None: ...
    Size: str
    Grade: str
    Name: str
    Class: int
    NumberingSeries: NumberingSeries
    BendingRadius: float

class RebarPropertiesNullable:
    """.NET: Tekla.Structures.Model.RebarPropertiesNullable"""
    def __init__(self, *args) -> None: ...
    Size: str
    Grade: str
    Name: str
    Class: Nullable
    NumberingSeries: NumberingSeriesNullable
    BendingRadius: Nullable

class RebarPropertyModifier(BaseRebarModifier):
    """.NET: Tekla.Structures.Model.RebarPropertyModifier"""
    def __init__(self, *args) -> None: ...
    AffectsWholeBarPlane: bool
    RebarProperties: RebarPropertiesNullable
    GroupingType: Nullable
    SpacingOverride: RebarSpacing
    FatherPart: Part
    Father: RebarSet
    Curve: Contour
    BarsAffected: BarsAffectedEnum
    FirstAffectedBar: int
    FollowEdges: bool
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def GetAffectedBars(self, ) -> ModelObjectEnumerator: ...

class RebarSet(ModelObject):
    """.NET: Tekla.Structures.Model.RebarSet"""
    def __init__(self, *args) -> None: ...
    RebarProperties: RebarProperties
    LegFaces: List
    Guidelines: List
    LayerOrderNumber: int
    BarOrientation: LineSegment
    FatherPart: Part
    CloseShape: bool
    FrozenState: FrozenStateEnum
    Offsets: RebarOffsets
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def GetAssembly(self, ) -> Assembly: ...
    def GetRebarLegSurfaces(self, ) -> ModelObjectEnumerator: ...
    def GetRebarModifiers(self, ) -> ModelObjectEnumerator: ...
    def GetRebarSetAdditions(self, ) -> ModelObjectEnumerator: ...
    def GetReinforcements(self, ) -> ModelObjectEnumerator: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class RebarSetAddition(ModelObject):
    """.NET: Tekla.Structures.Model.RebarSetAddition"""
    def __init__(self, *args) -> None: ...
    LegFaces: List
    Father: RebarSet
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class RebarSpacing:
    """.NET: Tekla.Structures.Model.RebarSpacing"""
    def __init__(self, *args) -> None: ...
    Type: SpacingType
    NumberOfBars: int
    TargetSpace: float
    ExactSpace: float
    ExactElements: List
    Zones: List
    StartOffset: float
    EndOffset: float
    StartOffsetType: OffsetEnum
    EndOffsetType: OffsetEnum
    StartOffsetIsAutomatic: bool
    EndOffsetIsAutomatic: bool
    ExcludeType: ExcludeTypeEnum
    InheritFromPrimary: bool
    InheritOffsetsFromPrimary: bool
    def Clone(self, ) -> RebarSpacing: ...
    @staticmethod
    def Create(type: SpacingType, startOffset: Offset, endOffset: Offset, distance: float) -> RebarSpacing: ...
    @staticmethod
    def IsExactFlexibleType(type: SpacingType) -> bool: ...

class RebarSpacingZone:
    """.NET: Tekla.Structures.Model.RebarSpacingZone"""
    def __init__(self, *args) -> None: ...
    NumberOfSpaces: int
    Spacing: float
    Length: float
    NumberOfSpacesType: SpacingEnum
    SpacingType: SpacingEnum
    LengthType: LengthEnum

class RebarSplice(ModelObject):
    """.NET: Tekla.Structures.Model.RebarSplice"""
    def __init__(self, *args) -> None: ...
    RebarGroup1: Reinforcement
    RebarGroup2: Reinforcement
    Type: RebarSpliceTypeEnum
    LapLength: float
    Offset: float
    Clearance: float
    BarPositions: RebarSpliceBarPositionsEnum
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class RebarSplitter(BaseRebarModifier):
    """.NET: Tekla.Structures.Model.RebarSplitter"""
    def __init__(self, *args) -> None: ...
    StaggerType: StaggerTypeEnum
    StaggerOffset: float
    SplitOffset: float
    SplitType: SplitTypeEnum
    Lapping: RebarLapping
    Cranking: RebarCranking
    Father: RebarSet
    Curve: Contour
    BarsAffected: BarsAffectedEnum
    FirstAffectedBar: int
    FollowEdges: bool
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def GetAffectedBars(self, whichEnd: AffectedRebarEnum) -> ModelObjectEnumerator: ...

class RebarStrand(Reinforcement):
    """.NET: Tekla.Structures.Model.RebarStrand"""
    def __init__(self, *args) -> None: ...
    Size: str
    PullPerStrand: float
    Patterns: ArrayList
    Unbondings: ArrayList
    StartPoint: Point
    EndPoint: Point
    OnPlaneOffsets: ArrayList
    Father: ModelObject
    Grade: str
    Name: str
    Class: int
    NumberingSeries: NumberingSeries
    FromPlaneOffset: float
    StartPointOffsetType: RebarOffsetTypeEnum
    StartPointOffsetValue: float
    EndPointOffsetType: RebarOffsetTypeEnum
    EndPointOffsetValue: float
    RadiusValues: ArrayList
    InputPointDeformingState: DeformingType
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class RebarThreadingDataNullable:
    """.NET: Tekla.Structures.Model.RebarThreadingDataNullable"""
    def __init__(self, *args) -> None: ...
    ThreadingType: str
    Length: Nullable
    ExtraFabricationLength: Nullable

class ReferenceModel(ModelObject):
    """.NET: Tekla.Structures.Model.ReferenceModel"""
    def __init__(self, *args) -> None: ...
    Filename: str
    ActiveFilePath: str
    Title: str
    Position: Point
    Scale: float
    Visibility: VisibilityEnum
    BasePointGuid: Guid
    UseWorkplane: bool
    Rotation: float
    Rotation3D: Rotation3D
    ProjectGUID: Guid
    ModelGUID: Guid
    VersionGUID: Guid
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def GetChildren(self, ) -> ModelObjectEnumerator: ...
    def GetConvertedObjects(self, ) -> ModelObjectEnumerator: ...
    def GetCurrentRevision(self, ) -> Revision: ...
    def GetReferenceModelObjectByExternalGuid(self, externalGuid: str) -> ReferenceModelObject: ...
    def GetReferenceModelObjectGuidsByExternalGuids(self, externalGuids: List) -> List: ...
    def GetRevisions(self, ) -> List: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def RefreshFile(self, ) -> bool: ...
    def RemoveRevision(self, revision: Revision) -> bool: ...
    def Select(self, ) -> bool: ...
    def SetAsCurrentRevision(self, modelId: int, revisionId: int) -> bool: ...

class ReferenceModelObject(ModelObject):
    """.NET: Tekla.Structures.Model.ReferenceModelObject"""
    def __init__(self, *args) -> None: ...
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def GetFather(self, ) -> ReferenceModelObject: ...
    def GetReferenceModel(self, ) -> ReferenceModel: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class Reinforcement(ModelObject):
    """.NET: Tekla.Structures.Model.Reinforcement"""
    def __init__(self, *args) -> None: ...
    Father: ModelObject
    Grade: str
    Name: str
    Class: int
    NumberingSeries: NumberingSeries
    OnPlaneOffsets: ArrayList
    FromPlaneOffset: float
    StartPointOffsetType: RebarOffsetTypeEnum
    StartPointOffsetValue: float
    EndPointOffsetType: RebarOffsetTypeEnum
    EndPointOffsetValue: float
    RadiusValues: ArrayList
    InputPointDeformingState: DeformingType
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def GetAssembly(self, ) -> Assembly: ...
    def GetFatherPour(self, ) -> PourObject: ...
    def GetFatherPourUnit(self, ) -> PourUnit: ...
    def GetNumberOfRebars(self, ) -> int: ...
    def GetRebarComplexGeometries(self, withHooks: bool, withoutClashes: bool, lengthAdjustments: bool, simplified: RebarGeometrySimplificationTypeEnum) -> List: ...
    def GetRebarGeometries(self, options: RebarGeometryOptionEnum) -> ArrayList: ...
    def GetRebarGeometriesWithoutClashes(self, withHooks: bool) -> ArrayList: ...
    def GetSingleRebar(self, index: int, withHooks: bool) -> RebarGeometry: ...
    def GetSingleRebarWithoutClash(self, index: int, withHooks: bool) -> RebarGeometry: ...
    def GetSolid(self, ) -> Solid: ...
    def IsGeometryValid(self, ) -> bool: ...

class Seam(BaseComponent):
    """.NET: Tekla.Structures.Model.Seam"""
    def __init__(self, *args) -> None: ...
    UpVector: Vector
    AutoDirectionType: AutoDirectionTypeEnum
    AutoPosition: bool
    Code: str
    Class: int
    Status: ConnectionStatusEnum
    Name: str
    Number: int
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def GetInputPolygon(self, ) -> Polygon: ...
    def GetPrimaryObject(self, ) -> ModelObject: ...
    def GetSecondaryObjects(self, ) -> ArrayList: ...
    def GetStartAndEndPositions(self, StartPoint: Point, EndPoint: Point) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...
    def SetInputPolygon(self, InputPolygon: Polygon) -> bool: ...
    def SetInputPositions(self, StartPoint: Point, EndPoint: Point) -> bool: ...
    def SetPrimaryObject(self, M: ModelObject) -> bool: ...
    def SetSecondaryObject(self, M: ModelObject) -> bool: ...
    def SetSecondaryObjects(self, Secondaries: ArrayList) -> bool: ...

class SelfIntersectingSurfaceException(LoftedPlateOperationException):
    """.NET: Tekla.Structures.Model.SelfIntersectingSurfaceException"""
    def __init__(self, *args) -> None: ...
    Message: str
    Data: IDictionary
    InnerException: Exception
    TargetSite: MethodBase
    StackTrace: str
    HelpLink: str
    Source: str
    HResult: int

class SharedModelStateEnum:
    """.NET: Tekla.Structures.Model.SharedModelStateEnum"""
    def __init__(self, *args) -> None: ...
    ...

class SharingResultCode:
    """.NET: Tekla.Structures.Model.SharingResultCode"""
    def __init__(self, *args) -> None: ...
    ...

class SharingResultState:
    """.NET: Tekla.Structures.Model.SharingResultState"""
    def __init__(self, *args) -> None: ...
    ...

class SharingRole:
    """.NET: Tekla.Structures.Model.SharingRole"""
    def __init__(self, *args) -> None: ...
    ...

class SharingUpdateType:
    """.NET: Tekla.Structures.Model.SharingUpdateType"""
    def __init__(self, *args) -> None: ...
    ...

class SingleRebar(Reinforcement):
    """.NET: Tekla.Structures.Model.SingleRebar"""
    def __init__(self, *args) -> None: ...
    Size: str
    StartHook: RebarHookData
    EndHook: RebarHookData
    Polygon: Polygon
    Father: ModelObject
    Grade: str
    Name: str
    Class: int
    NumberingSeries: NumberingSeries
    OnPlaneOffsets: ArrayList
    FromPlaneOffset: float
    StartPointOffsetType: RebarOffsetTypeEnum
    StartPointOffsetValue: float
    EndPointOffsetType: RebarOffsetTypeEnum
    EndPointOffsetValue: float
    RadiusValues: ArrayList
    InputPointDeformingState: DeformingType
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def GetRebarSet(self, ) -> RebarSet: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class Solid:
    """.NET: Tekla.Structures.Model.Solid"""
    def __init__(self, *args) -> None: ...
    MinimumPoint: Point
    MaximumPoint: Point
    def GetAllIntersectionPoints(self, point1: Point, point2: Point, point3: Point) -> IEnumerator: ...
    def GetCutPart(self, CuttingPart: Solid) -> ShellEnumerator: ...
    def GetEdgeEnumerator(self, ) -> EdgeEnumerator: ...
    def GetFaceEnumerator(self, ) -> FaceEnumerator: ...
    def Intersect(self, point1: Point, point2: Point, point3: Point) -> ArrayList: ...
    def IntersectAllFaces(self, point1: Point, point2: Point, point3: Point) -> IEnumerator: ...
    def IsValid(self, ) -> bool: ...

class SpiralBeam(Part):
    """.NET: Tekla.Structures.Model.SpiralBeam"""
    def __init__(self, *args) -> None: ...
    StartPoint: Point
    RotationAxisBasePoint: Point
    RotationAxisUpPoint: Point
    TotalRise: float
    RotationAngle: float
    TwistAngleStart: float
    TwistAngleEnd: float
    RotationCenterPoint: Point
    RotationAxisDirection: Vector
    EndPoint: Point
    Profile: Profile
    Material: Material
    DeformingData: DeformingData
    PartNumber: NumberingSeries
    AssemblyNumber: NumberingSeries
    Name: str
    Class: str
    Finish: str
    CastUnitType: CastUnitTypeEnum
    PourPhase: int
    Position: Position
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class SpiralBeamDataException(Exception):
    """.NET: Tekla.Structures.Model.SpiralBeamDataException"""
    def __init__(self, *args) -> None: ...
    Message: str
    Data: IDictionary
    InnerException: Exception
    TargetSite: MethodBase
    StackTrace: str
    HelpLink: str
    Source: str
    HResult: int

class StrandUnbondingData:
    """.NET: Tekla.Structures.Model.StrandUnbondingData"""
    def __init__(self, *args) -> None: ...
    StrandIndex: int
    FromStart: float
    MiddleToStart: float
    MiddleToEnd: float
    FromEnd: float

class SurfaceObject(ModelObject):
    """.NET: Tekla.Structures.Model.SurfaceObject"""
    def __init__(self, *args) -> None: ...
    Polymesh: FacetedBrep
    Class: str
    Name: str
    CreateHoles: bool
    Type: str
    Father: ModelObject
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class SurfaceTreatment(ModelObject):
    """.NET: Tekla.Structures.Model.SurfaceTreatment"""
    def __init__(self, *args) -> None: ...
    Type: SurfaceTypeEnum
    Color: SurfaceColorEnum
    Material: Material
    Position: Position
    Polygon: Contour
    StartPoint: Point
    EndPoint: Point
    Father: Part
    Thickness: float
    Name: str
    Class: str
    CutByFatherBooleans: bool
    TypeName: str
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class Task(ModelObject):
    """.NET: Tekla.Structures.Model.Task"""
    def __init__(self, *args) -> None: ...
    Name: str
    Completeness: int
    Critical: bool
    Local: bool
    Scenario: HierarchicObject
    Description: str
    Url: str
    PlannedStartDate: DateTime
    PlannedEndDate: DateTime
    PlannedWorkAmount: float
    ActualStartDate: DateTime
    ActualEndDate: DateTime
    ActualWorkAmount: float
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def AddObjectsToTask(self, ModelObjects: ArrayList) -> bool: ...
    def Delete(self, ) -> bool: ...
    @staticmethod
    def GetAllTasksOfSelectedObjects() -> ModelObjectEnumerator: ...
    def GetDependencies(self, ) -> ModelObjectEnumerator: ...
    def GetFathers(self, ) -> ModelObjectEnumerator: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def RemoveObjectsFromTask(self, ModelObjects: ArrayList) -> bool: ...
    def Select(self, ) -> bool: ...

class TaskDependency(ModelObject):
    """.NET: Tekla.Structures.Model.TaskDependency"""
    def __init__(self, *args) -> None: ...
    Lag: int
    Local: bool
    Primary: Task
    Secondary: Task
    DependencyType: DependencyTypeEnum
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class TaskWorktype(ModelObject):
    """.NET: Tekla.Structures.Model.TaskWorktype"""
    def __init__(self, *args) -> None: ...
    Name: str
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class TransformationPlane:
    """.NET: Tekla.Structures.Model.TransformationPlane"""
    def __init__(self, *args) -> None: ...
    TransformationMatrixToGlobal: Matrix
    TransformationMatrixToLocal: Matrix
    def ToString(self, ) -> str: ...

class UndefinedCurveDirectionException(ConnectiveGeometryException):
    """.NET: Tekla.Structures.Model.UndefinedCurveDirectionException"""
    def __init__(self, *args) -> None: ...
    Message: str
    Data: IDictionary
    InnerException: Exception
    TargetSite: MethodBase
    StackTrace: str
    HelpLink: str
    Source: str
    HResult: int

class UnknownLoftedPlateErrorException(LoftedPlateOperationException):
    """.NET: Tekla.Structures.Model.UnknownLoftedPlateErrorException"""
    def __init__(self, *args) -> None: ...
    Message: str
    Data: IDictionary
    InnerException: Exception
    TargetSite: MethodBase
    StackTrace: str
    HelpLink: str
    Source: str
    HResult: int

class UnsupportedChamferException(ConnectiveGeometryException):
    """.NET: Tekla.Structures.Model.UnsupportedChamferException"""
    def __init__(self, *args) -> None: ...
    Message: str
    Data: IDictionary
    InnerException: Exception
    TargetSite: MethodBase
    StackTrace: str
    HelpLink: str
    Source: str
    HResult: int

class Weld(BaseWeld):
    """.NET: Tekla.Structures.Model.Weld"""
    def __init__(self, *args) -> None: ...
    Position: WeldPositionEnum
    Direction: Vector
    MainObject: ModelObject
    SecondaryObject: ModelObject
    SizeAbove: float
    AdditionalSizeAbove: float
    TypeAbove: WeldTypeEnum
    AngleAbove: float
    LengthAbove: float
    ContourAbove: WeldContourEnum
    FinishAbove: WeldFinishEnum
    PitchAbove: float
    SizeBelow: float
    AdditionalSizeBelow: float
    TypeBelow: WeldTypeEnum
    AngleBelow: float
    LengthBelow: float
    ContourBelow: WeldContourEnum
    FinishBelow: WeldFinishEnum
    PitchBelow: float
    ShopWeld: bool
    AroundWeld: bool
    StitchWeld: bool
    RootOpeningAbove: float
    RootFaceAbove: float
    EffectiveThroatAbove: float
    IncrementAmountAbove: int
    RootOpeningBelow: float
    RootFaceBelow: float
    EffectiveThroatBelow: float
    IncrementAmountBelow: int
    ElectrodeClassification: WeldElectrodeClassificationEnum
    ElectrodeStrength: float
    ElectrodeCoefficient: float
    ProcessType: WeldProcessTypeEnum
    NDTInspection: WeldNDTInspectionEnum
    ConnectAssemblies: bool
    ReferenceText: str
    PrefixAboveLine: str
    PrefixBelowLine: str
    Standard: str
    WeldNumber: int
    WeldNumberPrefix: str
    IntermittentType: WeldIntermittentTypeEnum
    Placement: WeldPlacementTypeEnum
    Preparation: WeldPreparationTypeEnum
    ModificationTime: Nullable
    IsUpToDate: bool
    Identifier: Identifier
    def Delete(self, ) -> bool: ...
    def GetLogicalWeld(self, LogicalWeld: LogicalWeld) -> bool: ...
    def Insert(self, ) -> bool: ...
    def Modify(self, ) -> bool: ...
    def Select(self, ) -> bool: ...

class WorkPlaneHandler:
    """.NET: Tekla.Structures.Model.WorkPlaneHandler"""
    def __init__(self, *args) -> None: ...
    def GetCurrentTransformationPlane(self, ) -> TransformationPlane: ...
    def SetCurrentTransformationPlane(self, TransformationPlane: TransformationPlane) -> bool: ...
