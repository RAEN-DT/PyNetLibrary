# Auto-generated — Civil 26 — Autodesk.Civil.Runtime

class CorridorError:
    """.NET enum: Autodesk.Civil.Runtime.CorridorError"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Success: int  # = -2147221504
    Failure: int  # = -2147221503
    CouldNotSolveInLayoutMode: int  # = -2147221502
    ParameterNotFound: int  # = -2147221501
    LogicalNameNotFound: int  # = -2147221500
    NoSideslopeIntersectFound: int  # = -2147221499
    NoSubgradeIntersectFound: int  # = -2147221498
    ScriptModuleNotFound: int  # = -2147221497
    ScriptMacroNotFound: int  # = -2147221496
    CorridorStateNotFound: int  # = -2147221495
    ScriptPossibleSyntaxError: int  # = -2147221494
    StopProcessingGroup: int  # = -2147221493
    StopProcessingAssembly: int  # = -2147221492
    StopProcessingRegion: int  # = -2147221491
    StopProcessingBaseline: int  # = -2147221490
    StopProcessingCorridor: int  # = -2147221489
    ElevationAtStationNotFound: int  # = -2147221488
    ScriptModulePathUpdated: int  # = -2147221487
    CorridorOutOfDate: int  # = -2147221486
    ValueShouldNotBeLessThanOrEqualToZero: int  # = -2147221485
    ValueShouldNotBeLessThanZero: int  # = -2147221484
    ValueShouldNotBeZero: int  # = -2147221483
    ValueInABadPosition: int  # = -2147221482
    ValueTooSmall: int  # = -2147221481
    ValueTooLarge: int  # = -2147221480
    NoLinkIntersectFound: int  # = -2147221479
    NoMarkedPointFound: int  # = -2147221478
    ValueShouldNotBeOdd: int  # = -2147221477
    InvalidArraySpecifiedForLinkDefinition: int  # = -2147221476
    InvalidArraySpecifiedForLinkDefinitionFormat: int  # = -2147221475
    InvalidArraySpecifiedForShapeDefinition: int  # = -2147221474
    InvalidArraySpecifiedForShapeDefinitionFormat: int  # = -2147221473
    InvalidCorridorStateObjectId: int  # = -2147221472
    InvalidSubassemblyCOMClassId: int  # = -2147221471
    StopProcessingConditional: int  # = -2147221469
    ReprocessSubassembly: int  # = -2147221468
    ReprocessAssembly: int  # = -2147221467
    ReprocessRegion: int  # = -2147221466
    ReprocessBaseline: int  # = -2147221465
class CorridorErrorLevel:
    """.NET enum: Autodesk.Civil.Runtime.CorridorErrorLevel"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Informational: int  # = 1
    AsWarning: int  # = 2
    Severe: int  # = 3
class CorridorLayoutModeDisplay:
    """.NET enum: Autodesk.Civil.Runtime.CorridorLayoutModeDisplay"""
    def __init__(self, *args) -> None: ...
    General: int  # = 0
    None_: int  # = 1
    Subgrade: int  # = 2
    Sideslope: int  # = 3
    Conditional: int  # = 4
    DaylightBench: int  # = 5
class CorridorMode:
    """.NET enum: Autodesk.Civil.Runtime.CorridorMode"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Layout: int  # = 1
    Design: int  # = 2
class CorridorState(RuntimeState):
    """.NET: Autodesk.Civil.Runtime.CorridorState"""
    def __init__(self, *args) -> None: ...
    ResourceString: str
    ResourceString: str
    CurrentAssemblyElevation: float
    CurrentAssemblyOffset: float
    CurrentSubassemblyElevation: float
    CurrentSubassemblyOffset: float
    CurrentAssemblyFixedElevation: float
    CurrentAssemblyFixedOffset: float
    CurrentAssemblyOffsetIsFixed: bool
    CurrentAlignmentIsOffsetAlignment: bool
    CurrentCorridorName: str
    CurrentCorridorId: ObjectId
    CurrentAssemblyName: str
    CurrentAssemblyId: ObjectId
    CurrentSubassemblyVersion: str
    CurrentSubassemblyName: str
    CurrentSubassemblyId: ObjectId
    CurrentProfileId: ObjectId
    CurrentAlignmentId: ObjectId
    CurrentBaselineId: ObjectId
    CurrentElevation: float
    CurrentOffset: float
    CurrentStation: float
    CurrentRegionEndStation: float
    CurrentRegionStartStation: float
    Mode: CorridorMode
    LayoutModeDisplayType: CorridorLayoutModeDisplay
    Shapes: ShapeCollection
    Links: LinkCollection
    Points: PointCollection
    ParamsElevationTargetGlobal: ParamElevationTargetCollection
    ParamsOffsetTargetGlobal: ParamOffsetTargetCollection
    ParamsProfileGlobal: ParamProfileCollection
    ParamsAlignmentGlobal: ParamAlignmentCollection
    ParamsSurfaceGlobal: ParamSurfaceCollection
    ParamsPointGlobal: ParamPointCollection
    ParamsStringGlobal: ParamStringCollection
    ParamsBoolGlobal: ParamBoolCollection
    ParamsDoubleGlobal: ParamDoubleCollection
    ParamsLongGlobal: ParamLongCollection
    ParamsElevationTarget: ParamElevationTargetCollection
    ParamsOffsetTarget: ParamOffsetTargetCollection
    ParamsProfile: ParamProfileCollection
    ParamsAlignment: ParamAlignmentCollection
    ParamsSurface: ParamSurfaceCollection
    ParamsPoint: ParamPointCollection
    ParamsString: ParamStringCollection
    ParamsBool: ParamBoolCollection
    ParamsDouble: ParamDoubleCollection
    ParamsLong: ParamLongCollection
    CurrentMacroName: str
    CurrentMacroProject: str
    def IntersectAlignment(self, targetAlignmentId: ObjectId, alignmentId: ObjectId, origin: IPoint, lookRight: bool, maxDistance: float) -> IPoint: ...
    def IntersectLink(self, origin: IPoint, lookRight: bool, slope: float, linkCode: str) -> IPoint: ...
    def IntersectSurface(self, surfaceId: ObjectId, alignmentId: ObjectId, origin: IPoint, lookRight: bool, slope: float, pointsRequired: int) -> list: ...
    def IsAboveSurface(self, surfaceId: ObjectId, alignmentId: ObjectId, point: IPoint, minimumAmountAbove: float) -> bool: ...
    def RecordError(self, error: CorridorError, errorLevel: CorridorErrorLevel, description: str, source: str, showInEventViewer: bool) -> None: ...
    def SampleSection(self, surfaceId: ObjectId, alignmentId: ObjectId, point1: IPoint, point2: IPoint) -> SampledSectionLinkCollection: ...
    def SetAxisOfRotationCrownPoint(self, nCrownPointIndex: int) -> None: ...
    def SetAxisOfRotationInformation(self, isPotentialPivot: bool, superElevationSlope: float, superElevationSlopeType: SuperelevationCrossSegmentType, isReversedSlope: bool) -> None: ...
    def SetAxisOfRotationSERange(self, dApplySE_StartOffset: float, dApplySE_EndOffset: float) -> None: ...
    def SoeToXyz(self, alignmentId: ObjectId, station: float, offset: float, elevation: float, X: float, Y: float, Z: float) -> None: ...
    def XyzToSoe(self, alignmentId: ObjectId, X: float, Y: float, Z: float, station: float, offset: float, elevation: float) -> None: ...

class IParam:
    """.NET: Autodesk.Civil.Runtime.IParam"""
    def __init__(self, *args) -> None: ...
    Value: object
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType

class Param:
    """.NET: Autodesk.Civil.Runtime.Param"""
    def __init__(self, *args) -> None: ...
    ...

class ParamAccessType:
    """.NET enum: Autodesk.Civil.Runtime.ParamAccessType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Input: int  # = 1
    Output: int  # = 2
    InputAndOutput: int  # = 3
class ParamAlignment(ParamBase<6\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpAlignmentId>):
    """.NET: Autodesk.Civil.Runtime.ParamAlignment"""
    def __init__(self, *args) -> None: ...
    Value: ObjectId
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType
    Key: str

class ParamAlignmentCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamAlignment\,Autodesk::Civil::Runtime::ParamAlignment ^>):
    """.NET: Autodesk.Civil.Runtime.ParamAlignmentCollection"""
    def __init__(self, *args) -> None: ...
    Item: ParamAlignment
    Item: ParamAlignment
    Count: int

class ParamBase<10\,Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >:
    """.NET: Autodesk.Civil.Runtime.ParamBase<10\,Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >"""
    def __init__(self, *args) -> None: ...
    Key: str
    Value: SlopeElevationTarget
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType

class ParamBase<1\,bool\,bool\,Autodesk::Civil::Runtime::CastOp<bool\,bool> >:
    """.NET: Autodesk.Civil.Runtime.ParamBase<1\,bool\,bool\,Autodesk::Civil::Runtime::CastOp<bool\,bool> >"""
    def __init__(self, *args) -> None: ...
    Key: str
    Value: bool
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType

class ParamBase<2\,long\,long\,Autodesk::Civil::Runtime::CastOp<long\,long> >:
    """.NET: Autodesk.Civil.Runtime.ParamBase<2\,long\,long\,Autodesk::Civil::Runtime::CastOp<long\,long> >"""
    def __init__(self, *args) -> None: ...
    Key: str
    Value: int
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType

class ParamBase<3\,double\,double\,Autodesk::Civil::Runtime::CastOp<double\,double> >:
    """.NET: Autodesk.Civil.Runtime.ParamBase<3\,double\,double\,Autodesk::Civil::Runtime::CastOp<double\,double> >"""
    def __init__(self, *args) -> None: ...
    Key: str
    Value: float
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType

class ParamBase<4\,System::String ^\,AecRmCString\,Autodesk::Civil::Runtime::CastOp<System::String ^\,AecRmCString> >:
    """.NET: Autodesk.Civil.Runtime.ParamBase<4\,System::String ^\,AecRmCString\,Autodesk::Civil::Runtime::CastOp<System::String ^\,AecRmCString> >"""
    def __init__(self, *args) -> None: ...
    Key: str
    Value: str
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType

class ParamBase<5\,Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d\,Autodesk::Civil::Runtime::CastOp<Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d> >:
    """.NET: Autodesk.Civil.Runtime.ParamBase<5\,Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d\,Autodesk::Civil::Runtime::CastOp<Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d> >"""
    def __init__(self, *args) -> None: ...
    Key: str
    Value: Point3d
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType

class ParamBase<6\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpAlignmentId>:
    """.NET: Autodesk.Civil.Runtime.ParamBase<6\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpAlignmentId>"""
    def __init__(self, *args) -> None: ...
    Key: str
    Value: ObjectId
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType

class ParamBase<7\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpProfileId>:
    """.NET: Autodesk.Civil.Runtime.ParamBase<7\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpProfileId>"""
    def __init__(self, *args) -> None: ...
    Key: str
    Value: ObjectId
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType

class ParamBase<8\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpSurfaceId>:
    """.NET: Autodesk.Civil.Runtime.ParamBase<8\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpSurfaceId>"""
    def __init__(self, *args) -> None: ...
    Key: str
    Value: ObjectId
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType

class ParamBase<9\,Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >:
    """.NET: Autodesk.Civil.Runtime.ParamBase<9\,Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >"""
    def __init__(self, *args) -> None: ...
    Key: str
    Value: WidthOffsetTarget
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType

class ParamBool(ParamBase<1\,bool\,bool\,Autodesk::Civil::Runtime::CastOp<bool\,bool> >):
    """.NET: Autodesk.Civil.Runtime.ParamBool"""
    def __init__(self, *args) -> None: ...
    TypeInfo: TypeInfoBool
    Value: bool
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType
    Key: str

class ParamBoolCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamBool\,Autodesk::Civil::Runtime::ParamBool ^>):
    """.NET: Autodesk.Civil.Runtime.ParamBoolCollection"""
    def __init__(self, *args) -> None: ...
    Item: ParamBool
    Item: ParamBool
    Count: int
    def Add(self, name: str, value: bool) -> ParamBool: ...

class ParamCollectionBase<Autodesk::Civil::Runtime::ParamAlignment\,Autodesk::Civil::Runtime::ParamAlignment ^>:
    """.NET: Autodesk.Civil.Runtime.ParamCollectionBase<Autodesk::Civil::Runtime::ParamAlignment\,Autodesk::Civil::Runtime::ParamAlignment ^>"""
    def __init__(self, *args) -> None: ...
    Item: ParamAlignment
    Item: ParamAlignment
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Value(self, index: str) -> ObjectId: ...

class ParamCollectionBase<Autodesk::Civil::Runtime::ParamBool\,Autodesk::Civil::Runtime::ParamBool ^>:
    """.NET: Autodesk.Civil.Runtime.ParamCollectionBase<Autodesk::Civil::Runtime::ParamBool\,Autodesk::Civil::Runtime::ParamBool ^>"""
    def __init__(self, *args) -> None: ...
    Item: ParamBool
    Item: ParamBool
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Value(self, index: str) -> bool: ...

class ParamCollectionBase<Autodesk::Civil::Runtime::ParamDouble\,Autodesk::Civil::Runtime::ParamDouble ^>:
    """.NET: Autodesk.Civil.Runtime.ParamCollectionBase<Autodesk::Civil::Runtime::ParamDouble\,Autodesk::Civil::Runtime::ParamDouble ^>"""
    def __init__(self, *args) -> None: ...
    Item: ParamDouble
    Item: ParamDouble
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Value(self, index: str) -> float: ...

class ParamCollectionBase<Autodesk::Civil::Runtime::ParamElevationTarget\,Autodesk::Civil::Runtime::ParamElevationTarget ^>:
    """.NET: Autodesk.Civil.Runtime.ParamCollectionBase<Autodesk::Civil::Runtime::ParamElevationTarget\,Autodesk::Civil::Runtime::ParamElevationTarget ^>"""
    def __init__(self, *args) -> None: ...
    Item: ParamElevationTarget
    Item: ParamElevationTarget
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Value(self, index: str) -> SlopeElevationTarget: ...

class ParamCollectionBase<Autodesk::Civil::Runtime::ParamLong\,Autodesk::Civil::Runtime::ParamLong ^>:
    """.NET: Autodesk.Civil.Runtime.ParamCollectionBase<Autodesk::Civil::Runtime::ParamLong\,Autodesk::Civil::Runtime::ParamLong ^>"""
    def __init__(self, *args) -> None: ...
    Item: ParamLong
    Item: ParamLong
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Value(self, index: str) -> int: ...

class ParamCollectionBase<Autodesk::Civil::Runtime::ParamOffsetTarget\,Autodesk::Civil::Runtime::ParamOffsetTarget ^>:
    """.NET: Autodesk.Civil.Runtime.ParamCollectionBase<Autodesk::Civil::Runtime::ParamOffsetTarget\,Autodesk::Civil::Runtime::ParamOffsetTarget ^>"""
    def __init__(self, *args) -> None: ...
    Item: ParamOffsetTarget
    Item: ParamOffsetTarget
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Value(self, index: str) -> WidthOffsetTarget: ...

class ParamCollectionBase<Autodesk::Civil::Runtime::ParamPoint\,Autodesk::Civil::Runtime::ParamPoint ^>:
    """.NET: Autodesk.Civil.Runtime.ParamCollectionBase<Autodesk::Civil::Runtime::ParamPoint\,Autodesk::Civil::Runtime::ParamPoint ^>"""
    def __init__(self, *args) -> None: ...
    Item: ParamPoint
    Item: ParamPoint
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Value(self, index: str) -> Point3d: ...

class ParamCollectionBase<Autodesk::Civil::Runtime::ParamProfile\,Autodesk::Civil::Runtime::ParamProfile ^>:
    """.NET: Autodesk.Civil.Runtime.ParamCollectionBase<Autodesk::Civil::Runtime::ParamProfile\,Autodesk::Civil::Runtime::ParamProfile ^>"""
    def __init__(self, *args) -> None: ...
    Item: ParamProfile
    Item: ParamProfile
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Value(self, index: str) -> ObjectId: ...

class ParamCollectionBase<Autodesk::Civil::Runtime::ParamString\,Autodesk::Civil::Runtime::ParamString ^>:
    """.NET: Autodesk.Civil.Runtime.ParamCollectionBase<Autodesk::Civil::Runtime::ParamString\,Autodesk::Civil::Runtime::ParamString ^>"""
    def __init__(self, *args) -> None: ...
    Item: ParamString
    Item: ParamString
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Value(self, index: str) -> str: ...

class ParamCollectionBase<Autodesk::Civil::Runtime::ParamSurface\,Autodesk::Civil::Runtime::ParamSurface ^>:
    """.NET: Autodesk.Civil.Runtime.ParamCollectionBase<Autodesk::Civil::Runtime::ParamSurface\,Autodesk::Civil::Runtime::ParamSurface ^>"""
    def __init__(self, *args) -> None: ...
    Item: ParamSurface
    Item: ParamSurface
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Value(self, index: str) -> ObjectId: ...

class ParamDouble(ParamBase<3\,double\,double\,Autodesk::Civil::Runtime::CastOp<double\,double> >):
    """.NET: Autodesk.Civil.Runtime.ParamDouble"""
    def __init__(self, *args) -> None: ...
    TypeInfo: TypeInfoDouble
    Value: float
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType
    Key: str

class ParamDoubleCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamDouble\,Autodesk::Civil::Runtime::ParamDouble ^>):
    """.NET: Autodesk.Civil.Runtime.ParamDoubleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ParamDouble
    Item: ParamDouble
    Count: int
    def Add(self, name: str, value: float) -> ParamDouble: ...

class ParamElevationTarget(ParamBase<10\,Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >):
    """.NET: Autodesk.Civil.Runtime.ParamElevationTarget"""
    def __init__(self, *args) -> None: ...
    Value: SlopeElevationTarget
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType
    Key: str

class ParamElevationTargetCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamElevationTarget\,Autodesk::Civil::Runtime::ParamElevationTarget ^>):
    """.NET: Autodesk.Civil.Runtime.ParamElevationTargetCollection"""
    def __init__(self, *args) -> None: ...
    Item: ParamElevationTarget
    Item: ParamElevationTarget
    Count: int

class ParamLogicalNameType:
    """.NET enum: Autodesk.Civil.Runtime.ParamLogicalNameType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Surface: int  # = 1
    Alignment: int  # = 2
    Profile: int  # = 3
    OffsetTarget: int  # = 4
    ElevationTarget: int  # = 5
    OffsetTargetPipe: int  # = 6
    ElevationTargetPipe: int  # = 7
class ParamLong(ParamBase<2\,long\,long\,Autodesk::Civil::Runtime::CastOp<long\,long> >):
    """.NET: Autodesk.Civil.Runtime.ParamLong"""
    def __init__(self, *args) -> None: ...
    TypeInfo: TypeInfoLong
    Value: int
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType
    Key: str
    def AddEnumData(self, name: str, displayName: str, value: int) -> None: ...
    def EnumCount(self, ) -> int: ...
    def GetEnumData(self, index: int, name: str, displayName: str, value: int) -> None: ...

class ParamLongCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamLong\,Autodesk::Civil::Runtime::ParamLong ^>):
    """.NET: Autodesk.Civil.Runtime.ParamLongCollection"""
    def __init__(self, *args) -> None: ...
    Item: ParamLong
    Item: ParamLong
    Count: int
    def Add(self, name: str, value: int) -> ParamLong: ...

class ParamOffsetTarget(ParamBase<9\,Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >):
    """.NET: Autodesk.Civil.Runtime.ParamOffsetTarget"""
    def __init__(self, *args) -> None: ...
    Value: WidthOffsetTarget
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType
    Key: str

class ParamOffsetTargetCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamOffsetTarget\,Autodesk::Civil::Runtime::ParamOffsetTarget ^>):
    """.NET: Autodesk.Civil.Runtime.ParamOffsetTargetCollection"""
    def __init__(self, *args) -> None: ...
    Item: ParamOffsetTarget
    Item: ParamOffsetTarget
    Count: int

class ParamPoint(ParamBase<5\,Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d\,Autodesk::Civil::Runtime::CastOp<Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d> >):
    """.NET: Autodesk.Civil.Runtime.ParamPoint"""
    def __init__(self, *args) -> None: ...
    Elevation: float
    Offset: float
    Station: float
    Value: Point3d
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType
    Key: str
    def GetPoint(self, station: float, offset: float, elevation: float) -> None: ...
    def SetPoint(self, station: float, offset: float, elevation: float) -> None: ...

class ParamPointCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamPoint\,Autodesk::Civil::Runtime::ParamPoint ^>):
    """.NET: Autodesk.Civil.Runtime.ParamPointCollection"""
    def __init__(self, *args) -> None: ...
    Item: ParamPoint
    Item: ParamPoint
    Count: int
    def Add(self, name: str, value: Point3d) -> ParamPoint: ...

class ParamProfile(ParamBase<7\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpProfileId>):
    """.NET: Autodesk.Civil.Runtime.ParamProfile"""
    def __init__(self, *args) -> None: ...
    Value: ObjectId
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType
    Key: str

class ParamProfileCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamProfile\,Autodesk::Civil::Runtime::ParamProfile ^>):
    """.NET: Autodesk.Civil.Runtime.ParamProfileCollection"""
    def __init__(self, *args) -> None: ...
    Item: ParamProfile
    Item: ParamProfile
    Count: int

class ParamScope:
    """.NET enum: Autodesk.Civil.Runtime.ParamScope"""
    def __init__(self, *args) -> None: ...
    Local: int  # = 0
    Global: int  # = 1
class ParamString(ParamBase<4\,System::String ^\,AecRmCString\,Autodesk::Civil::Runtime::CastOp<System::String ^\,AecRmCString> >):
    """.NET: Autodesk.Civil.Runtime.ParamString"""
    def __init__(self, *args) -> None: ...
    Value: str
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType
    Key: str

class ParamStringCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamString\,Autodesk::Civil::Runtime::ParamString ^>):
    """.NET: Autodesk.Civil.Runtime.ParamStringCollection"""
    def __init__(self, *args) -> None: ...
    Item: ParamString
    Item: ParamString
    Count: int
    def Add(self, name: str, value: str) -> ParamString: ...

class ParamSurface(ParamBase<8\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpSurfaceId>):
    """.NET: Autodesk.Civil.Runtime.ParamSurface"""
    def __init__(self, *args) -> None: ...
    Value: ObjectId
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType
    Key: str

class ParamSurfaceCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamSurface\,Autodesk::Civil::Runtime::ParamSurface ^>):
    """.NET: Autodesk.Civil.Runtime.ParamSurfaceCollection"""
    def __init__(self, *args) -> None: ...
    Item: ParamSurface
    Item: ParamSurface
    Count: int

class ParamType:
    """.NET enum: Autodesk.Civil.Runtime.ParamType"""
    def __init__(self, *args) -> None: ...
    Unknown: int  # = 0
    Bool: int  # = 1
    Int: int  # = 2
    Double: int  # = 3
    String: int  # = 4
    Point3d: int  # = 5
    Alignment: int  # = 6
    Profile: int  # = 7
    Surface: int  # = 8
    OffsetTarget: int  # = 9
    ElevationTarget: int  # = 10
class ParamsOwnerType:
    """.NET enum: Autodesk.Civil.Runtime.ParamsOwnerType"""
    def __init__(self, *args) -> None: ...
    Subassembly: int  # = 0
    RoadwayState: int  # = 1
    PipeNetworkPart: int  # = 2
    PipeNetworkState: int  # = 3
    PipeNetworkRule: int  # = 4
class PipeNetworkState(RuntimeState):
    """.NET: Autodesk.Civil.Runtime.PipeNetworkState"""
    def __init__(self, *args) -> None: ...
    IsLayoutUpStream: bool
    IsCurrentPartBeingAdd: bool
    IsConnectingToStructure: bool
    IsBreakingPipe: bool
    LastPipeElevation: float
    IsInLayoutMode: bool
    CurrentStructureId: ObjectId
    CurrentPipeId: ObjectId
    ParamsBool: ParamBoolCollection
    ParamsDouble: ParamDoubleCollection
    ParamsLong: ParamLongCollection
    CurrentMacroName: str
    CurrentMacroProject: str
    def RuleResourceString(self, resId: str) -> str: ...
    def SetAlignmentOnPart(self, paramName: str, alignmentId: ObjectId) -> None: ...
    def SetBoolOnPart(self, paramName: str, value: bool) -> None: ...
    def SetDoubleOnCurrentPart(self, paramKey: str, value: float) -> None: ...
    def SetErrorMsgOnCurrentPart(self, paramKey: str, errorMessage: str) -> None: ...
    def SetLongOnPart(self, paramName: str, value: int) -> None: ...
    def SetPointOnPart(self, paramName: str, value: Point3d) -> None: ...
    def SetProfileOnPart(self, paramName: str, profileId: ObjectId) -> None: ...
    def SetStringOnPart(self, paramName: str, value: str) -> None: ...
    def SetSurfaceOnPart(self, paramName: str, surfaceId: ObjectId) -> None: ...

class RuntimeState(CivilWrapper<AeccDbRuntimeState>):
    """.NET: Autodesk.Civil.Runtime.RuntimeState"""
    def __init__(self, *args) -> None: ...
    CurrentMacroName: str
    CurrentMacroProject: str

class TypeInfoBool:
    """.NET enum: Autodesk.Civil.Runtime.TypeInfoBool"""
    def __init__(self, *args) -> None: ...
    Bool: int  # = 0
    NoYes: int  # = 1
    LabelTag: int  # = 2
    StraightSpline: int  # = 3
    StackedText: int  # = 4
    DisabledEnabled: int  # = 5
    OffOn: int  # = 6
    RightLeft: int  # = 7
    DecimalFractional: int  # = 8
    InOutCurve: int  # = 9
class TypeInfoDouble:
    """.NET enum: Autodesk.Civil.Runtime.TypeInfoDouble"""
    def __init__(self, *args) -> None: ...
    Double: int  # = 0
    NonNegativeDouble: int  # = 1
    NonNegativeNonZeroDouble: int  # = 2
    NonPositiveDouble: int  # = 3
    NonPositiveNonZeroDouble: int  # = 4
    NonZeroDouble: int  # = 5
    Station: int  # = 6
    DerivedStation: int  # = 7
    Grade: int  # = 8
    TransparentCmdGrade: int  # = 9
    TransparentCmdSlope: int  # = 10
    Direction: int  # = 11
    LatLong: int  # = 12
    Latitude: int  # = 13
    Angle: int  # = 14
    ConvergenceAngle: int  # = 15
    Distance: int  # = 16
    Dimension: int  # = 17
    Coordinate: int  # = 18
    XYCoordinatePair: int  # = 19
    Area: int  # = 20
    Elevation: int  # = 21
    ElevationPoint: int  # = 22
    PlotHeight: int  # = 23
    Volume: int  # = 24
    Percent: int  # = 25
    Azimuth: int  # = 26
class TypeInfoLong:
    """.NET enum: Autodesk.Civil.Runtime.TypeInfoLong"""
    def __init__(self, *args) -> None: ...
    Long: int  # = 0
    NonZeroLong: int  # = 1
    NonNegativeLong: int  # = 2
    NonNegativeNonZeroLong: int  # = 3
    NonPositiveLong: int  # = 4
    NonPositiveNonZeroLong: int  # = 5
    Color: int  # = 6
    PDMODE: int  # = 7
    LineWeight: int  # = 8
