# Auto-generated — Civil 26 — Autodesk.Civil

class AccelerationUnitType:
    """.NET enum: Autodesk.Civil.AccelerationUnitType"""
    def __init__(self, *args) -> None: ...
    MeterPerSecSquared: int  # = 202
    FootPerSecSquared: int  # = 203
class AlignmentDesignCheck(DesignCheck):
    """.NET: Autodesk.Civil.AlignmentDesignCheck"""
    def __init__(self, *args) -> None: ...
    DesignCheckType: AlignmentDesignCheckType
    Expression: str
    Description: str
    Name: str

class AlignmentDesignCheckCollection(DesignCheckCollection<Autodesk::Civil::AlignmentDesignCheck ^>):
    """.NET: Autodesk.Civil.AlignmentDesignCheckCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: AlignmentDesignCheck
    Item: AlignmentDesignCheck
    def Add(self, name: str, description: str, expression: str) -> AlignmentDesignCheck: ...
    def Clear(self, ) -> None: ...
    def Remove(self, name: str) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class AlignmentDesignCheckRoot:
    """.NET: Autodesk.Civil.AlignmentDesignCheckRoot"""
    def __init__(self, *args) -> None: ...
    TangentIntersectionDesignChecks: AlignmentDesignCheckCollection
    SuperelevationDesignChecks: AlignmentDesignCheckCollection
    SpiralDesignChecks: AlignmentDesignCheckCollection
    CurveDesignChecks: AlignmentDesignCheckCollection
    LineDesignChecks: AlignmentDesignCheckCollection

class AlignmentDesignCheckType:
    """.NET enum: Autodesk.Civil.AlignmentDesignCheckType"""
    def __init__(self, *args) -> None: ...
    TangentIntersection: int  # = 251704641
    Line: int  # = 251704642
    Spiral: int  # = 251704643
    Curve: int  # = 251704644
    Superelevation: int  # = 251704647
class AlignmentDividedPivotType:
    """.NET enum: Autodesk.Civil.AlignmentDividedPivotType"""
    def __init__(self, *args) -> None: ...
    Center: int  # = 3073
    InsideOfCurve: int  # = 3074
    OutsideOfCurve: int  # = 3075
    LeftSide: int  # = 3076
    RightSide: int  # = 3077
    MedianEdges: int  # = 3078
    Baseline: int  # = 3079
class AlignmentLockModeType:
    """.NET enum: Autodesk.Civil.AlignmentLockModeType"""
    def __init__(self, *args) -> None: ...
    Geometry: int  # = 1
    Station: int  # = 2
class AlignmentMedianTreatmentType:
    """.NET enum: Autodesk.Civil.AlignmentMedianTreatmentType"""
    def __init__(self, *args) -> None: ...
    MaintainMedian: int  # = 3079
    DistortedMedian: int  # = 3080
class AlignmentPointType:
    """.NET enum: Autodesk.Civil.AlignmentPointType"""
    def __init__(self, *args) -> None: ...
    Begin: int  # = 257
    End: int  # = 258
    TanTan: int  # = 259
    TanCurve: int  # = 260
    CurveTan: int  # = 261
    CompCurveCurve: int  # = 262
    RevCurveCurve: int  # = 263
    TanSpiral: int  # = 264
    SpiralTan: int  # = 265
    CurveSpiral: int  # = 266
    SpiralCurve: int  # = 267
    SpiralSpiral: int  # = 268
    RevSpiral: int  # = 269
    CurveMidPt: int  # = 285
class AlignmentTransitionSegmentType:
    """.NET enum: Autodesk.Civil.AlignmentTransitionSegmentType"""
    def __init__(self, *args) -> None: ...
    Lines: int  # = 0
    Arcs: int  # = 1
class AlignmentUndividedPivotType:
    """.NET enum: Autodesk.Civil.AlignmentUndividedPivotType"""
    def __init__(self, *args) -> None: ...
    Center: int  # = 3073
    InsideOfCurve: int  # = 3074
    OutsideOfCurve: int  # = 3075
    LeftSide: int  # = 3076
    RightSide: int  # = 3077
class AlignmentUpdateModeType:
    """.NET enum: Autodesk.Civil.AlignmentUpdateModeType"""
    def __init__(self, *args) -> None: ...
    Dynamic: int  # = 1
    Static: int  # = 2
class AnchorLocationType:
    """.NET enum: Autodesk.Civil.AnchorLocationType"""
    def __init__(self, *args) -> None: ...
    Start: int  # = 134263041
    Middle: int  # = 134263042
    End: int  # = 134263043
    TopLeft: int  # = 134263044
    TopCenter: int  # = 134263045
    TopRight: int  # = 134263046
    MiddleLeft: int  # = 134263047
    MiddleCenter: int  # = 134263048
    MiddleRight: int  # = 134263049
    BottomLeft: int  # = 134263050
    BottomCenter: int  # = 134263051
    BottomRight: int  # = 134263052
    InsertionPoint: int  # = 134263053
    Station: int  # = 134263072
    LabelLocation: int  # = 134263073
    PI: int  # = 134263074
    PVI: int  # = 134263088
    CurveStart: int  # = 134263089
    CurveEnd: int  # = 134263090
    PVIExtension: int  # = 134263091
    CurveStartExtension: int  # = 134263092
    CurveMiddleExtension: int  # = 134263093
    CurveEndExtension: int  # = 134263094
    CurveHighPoint: int  # = 134263095
    CurveLowPoint: int  # = 134263096
    TangentStart: int  # = 134263097
    TangentMiddle: int  # = 134263098
    TangentEnd: int  # = 134263099
    TangentStartExtension: int  # = 134263100
    TangentMiddleExtension: int  # = 134263101
    TangentEndExtension: int  # = 134263102
    StationExtension: int  # = 134263103
    BandTop: int  # = 134263104
    BandMiddle: int  # = 134263105
    BandBottom: int  # = 134263106
    StartExtension: int  # = 134263107
    MiddleExtension: int  # = 134263108
    EndExtension: int  # = 134263109
    Offset: int  # = 134263152
    GradeBreak: int  # = 134263154
    GradeBreakExtension: int  # = 134263155
class AnchorPointType:
    """.NET enum: Autodesk.Civil.AnchorPointType"""
    def __init__(self, *args) -> None: ...
    Start: int  # = 134263041
    Middle: int  # = 134263042
    End: int  # = 134263043
    TopLeft: int  # = 134263044
    TopCenter: int  # = 134263045
    TopRight: int  # = 134263046
    MiddleLeft: int  # = 134263047
    MiddleCenter: int  # = 134263048
    MiddleRight: int  # = 134263049
    BottomLeft: int  # = 134263050
    BottomCenter: int  # = 134263051
    BottomRight: int  # = 134263052
    InsertionPoint: int  # = 134263053
    Center: int  # = 134263054
    PointOfIntersection: int  # = 134263055
    Station: int  # = 134263072
    PI: int  # = 134263074
    TangentInStart: int  # = 134263075
    TangentInMiddle: int  # = 134263076
    TangentOutMiddle: int  # = 134263078
    TangentOutEnd: int  # = 134263079
    PVI: int  # = 134263088
    CurveStart: int  # = 134263089
    CurveEnd: int  # = 134263090
    PVIDimension: int  # = 134263091
    CurveStartDimension: int  # = 134263092
    CurveMidDimension: int  # = 134263093
    CurveEndDimension: int  # = 134263094
    CurveHighPoint: int  # = 134263095
    CurveLowPoint: int  # = 134263096
    TangentStart: int  # = 134263097
    TangentMiddle: int  # = 134263098
    TangentEnd: int  # = 134263099
    TangentStartDimension: int  # = 134263100
    TangentMiddleDimension: int  # = 134263101
    TangentEndDimension: int  # = 134263102
    StationExtension: int  # = 134263103
    BandTop: int  # = 134263104
    BandMiddle: int  # = 134263105
    BandBottom: int  # = 134263106
    StartExtension: int  # = 134263107
    MiddleExtension: int  # = 134263108
    EndExtension: int  # = 134263109
    PVIStart: int  # = 134263120
    PVIEnd: int  # = 134263121
    PVIStartDimension: int  # = 134263122
    PVIEndDimension: int  # = 134263123
    CurveMid: int  # = 134263128
    CurveHighPointDimension: int  # = 134263129
    CurveLowPointDimension: int  # = 134263130
    Offset: int  # = 134263152
    OffsetExtension: int  # = 134263153
    GradeBreak: int  # = 134263154
    GradeBreakExtension: int  # = 134263155
    Centerline: int  # = 134263156
    TopOuterDiameter: int  # = 134263157
    TopInnerDiameter: int  # = 134263158
    BottomOuterDiameter: int  # = 134263159
    BottomInnerDiameter: int  # = 134263160
    PipeDimension: int  # = 134263161
    StructureDimension: int  # = 134263162
    SectionViewTop: int  # = 134263168
    SectionViewBottom: int  # = 134263169
    SectionViewTopAtStart: int  # = 134263170
    SectionViewBottomAtStart: int  # = 134263171
    SectionViewTopAtMiddle: int  # = 134263172
    SectionViewBottomAtMiddle: int  # = 134263173
    SectionViewTopAtEnd: int  # = 134263174
    SectionViewBottomAtEnd: int  # = 134263175
    CurveStartInView: int  # = 134263184
    CurveEndInView: int  # = 134263185
    CurveStartInViewDimension: int  # = 134263186
    CurveEndInViewDimension: int  # = 134263187
    TangentStartInView: int  # = 134263188
    TangentEndInView: int  # = 134263189
    TangentStartInViewDimension: int  # = 134263190
    TangentEndInViewDimension: int  # = 134263191
    PVIStartInView: int  # = 134263192
    PVIEndInView: int  # = 134263193
    PVIStartInViewDimension: int  # = 134263194
    PVIEndInViewDimension: int  # = 134263195
    LabelLocation: int  # = 134263296
    SegmentMiddleSuperelevationBand: int  # = 134264080
    SegmentStartAndBandTop: int  # = 134264082
    SegmentStartAndBandMiddle: int  # = 134264083
    SegmentStartAndBandBot: int  # = 134264084
    SegmentMiddleAndBandTop: int  # = 134264085
    SegmentMiddleAndBandMiddle: int  # = 134264086
    SegmentMiddleAndBandBot: int  # = 134264087
    SegmentEndAndBandTop: int  # = 134264088
    SegmentEndAndBandMiddle: int  # = 134264089
    SegmentEndAndBandBot: int  # = 134264090
    SchematicLineStart: int  # = 134264091
    SchematicLineMid: int  # = 134264092
    SchematicLineEnd: int  # = 134264093
    PreviousOffsetBandTop: int  # = 134264144
    PreviousOffsetBandMiddle: int  # = 134264145
    PreviousOffsetBandBottom: int  # = 134264146
    NextOffsetBandTop: int  # = 134264150
    NextOffsetBandMiddle: int  # = 134264151
    NextOffsetBandBottom: int  # = 134264152
    PreviousStationBandTop: int  # = 134264160
    PreviousStationBandMiddle: int  # = 134264161
    PreviousStationBandBottom: int  # = 134264162
    LengthMidBandTop: int  # = 134264163
    LengthMidBandMiddle: int  # = 134264164
    LengthMidBandBottom: int  # = 134264165
    NextStationBandTop: int  # = 134264166
    NextStationBandMiddle: int  # = 134264167
    NextStationBandBottom: int  # = 134264168
    Insertion: int  # = 134264184
    Dimension: int  # = 134264185
class AngleFormatType:
    """.NET enum: Autodesk.Civil.AngleFormatType"""
    def __init__(self, *args) -> None: ...
    Decimal: int  # = 2468
    MinuteSecond: int  # = 2469
    MinuteSecondSpaced: int  # = 2470
    DegreeMinuteSecond: int  # = 2471
class AngleUnitType:
    """.NET enum: Autodesk.Civil.AngleUnitType"""
    def __init__(self, *args) -> None: ...
    Radian: int  # = 178
    Degree: int  # = 179
    Grad: int  # = 180
class AreaUnitType:
    """.NET enum: Autodesk.Civil.AreaUnitType"""
    def __init__(self, *args) -> None: ...
    SquareMeter: int  # = 55
    SquareFoot: int  # = 56
    Acre: int  # = 57
    Hectare: int  # = 61
    SquareKilometer: int  # = 75
    SquareMile: int  # = 83
    SquareYard: int  # = 93
class ArrowHeadFitType:
    """.NET enum: Autodesk.Civil.ArrowHeadFitType"""
    def __init__(self, *args) -> None: ...
    Shrink: int  # = 256
    Omit: int  # = 257
    AlwaysDraw: int  # = 258
class ArrowHeadSizeType:
    """.NET enum: Autodesk.Civil.ArrowHeadSizeType"""
    def __init__(self, *args) -> None: ...
    UseDrawScale: int  # = 4096
    UseFixedScale: int  # = 4097
    UseSizeInAbsUnits: int  # = 4098
    UseSizeInRelUnits: int  # = 4099
class ArrowHeadType:
    """.NET enum: Autodesk.Civil.ArrowHeadType"""
    def __init__(self, *args) -> None: ...
    ClosedFilled: int  # = 0
    ClosedBlank: int  # = 1
    Closed: int  # = 2
    Dot: int  # = 3
    ArchTick: int  # = 4
    Oblique: int  # = 5
    Open: int  # = 6
    Origin: int  # = 7
    Origin2: int  # = 8
    Open90: int  # = 9
    Open30: int  # = 10
    DotSmall: int  # = 11
    DotBlank: int  # = 12
    Small: int  # = 13
    BoxBlank: int  # = 14
    BoxFilled: int  # = 15
    DatumBlank: int  # = 16
    DatumFilled: int  # = 17
    Integral: int  # = 18
    None_: int  # = 19
    UserDefined: int  # = 20
class AssemblyDisplayStyleType:
    """.NET enum: Autodesk.Civil.AssemblyDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    InsertionPoint: int  # = 0
    Baseline: int  # = 1
    BaselineOrigin: int  # = 2
    OffsetBaseline: int  # = 3
    OffsetBaselineOrigin: int  # = 4
class AssemblyGroupNameType:
    """.NET enum: Autodesk.Civil.AssemblyGroupNameType"""
    def __init__(self, *args) -> None: ...
    GroupSide: int  # = 0
    GroupNameTemplate: int  # = 1
class BandLocationType:
    """.NET enum: Autodesk.Civil.BandLocationType"""
    def __init__(self, *args) -> None: ...
    Top: int  # = 0
    Bottom: int  # = 1
class BandType:
    """.NET enum: Autodesk.Civil.BandType"""
    def __init__(self, *args) -> None: ...
    ProfileData: int  # = 66
    VerticalGeometry: int  # = 67
    HorizontalGeometry: int  # = 68
    SuperelevationData: int  # = 69
    SectionData: int  # = 120
    SectionSegment: int  # = 121
    PipeNetwork: int  # = 320
    SectionalData: int  # = 328
    PressureNetwork: int  # = 402
    CantData: int  # = 403
class BearingQuadrantType:
    """.NET enum: Autodesk.Civil.BearingQuadrantType"""
    def __init__(self, *args) -> None: ...
    Northeast: int  # = 0
    Southeast: int  # = 1
    Southwest: int  # = 2
    Northwest: int  # = 3
class BlockAttachmentType:
    """.NET enum: Autodesk.Civil.BlockAttachmentType"""
    def __init__(self, *args) -> None: ...
    TopLeft: int  # = 0
    TopCenter: int  # = 1
    TopRight: int  # = 2
    MiddleLeft: int  # = 3
    MiddleCenter: int  # = 4
    MiddleRight: int  # = 5
    BottomLeft: int  # = 6
    BottomCenter: int  # = 7
    BottomRight: int  # = 8
    InsertionPoint: int  # = 9
class CantPivotMethodType:
    """.NET enum: Autodesk.Civil.CantPivotMethodType"""
    def __init__(self, *args) -> None: ...
    LowSideRail: int  # = 3074
    HighSideRail: int  # = 3075
    CenterBaseline: int  # = 3079
class CantPointType:
    """.NET enum: Autodesk.Civil.CantPointType"""
    def __init__(self, *args) -> None: ...
    BeginOfAlignment: int  # = 513
    EndOfAlignment: int  # = 520
    Manual: int  # = 524
    EndLevelRail: int  # = 768
    BeginLevelRail: int  # = 769
    BeginFullCant: int  # = 770
    EndFullCant: int  # = 771
class CantStationRoundingType:
    """.NET enum: Autodesk.Civil.CantStationRoundingType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 2833
    PointOne: int  # = 2834
    One: int  # = 2835
    Five: int  # = 2836
    Ten: int  # = 2837
class CantViewDisplayStyleType:
    """.NET enum: Autodesk.Civil.CantViewDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    GraphTitle: int  # = 0
    LeftAxis: int  # = 1
    LeftAxisAnnotation: int  # = 3
    LeftAxisTicksMajor: int  # = 5
    RightAxis: int  # = 7
    RightAxisAnnotation: int  # = 9
    RightAxisTicksMajor: int  # = 11
    TopAxis: int  # = 13
    TopAxisAnnotation: int  # = 15
    TopAxisTicks: int  # = 17
    BottomAxis: int  # = 19
    BottomAxisAnnotation: int  # = 21
    BottomAxisTicks: int  # = 23
    TopAxisTransitionRegion: int  # = 55
    BottomAxisTransitionRegion: int  # = 56
    TopAxisCurveDetails: int  # = 57
    BottomAxisCurveDetails: int  # = 58
    CriticalStationTicks: int  # = 59
    CriticalStationText: int  # = 60
    TopAxisCriticalStationAnnotation: int  # = 61
    BottomAxisCriticalStationAnnotation: int  # = 62
    AppliedCantAnnotation: int  # = 65
    LeftRailAppliedCantLine: int  # = 66
    RightRailAppliedCantLine: int  # = 67
    CenterLine: int  # = 68
    EquilibriumCantLine: int  # = 69
    EquilibriumCantAnnotation: int  # = 70
class CapitalizationType:
    """.NET enum: Autodesk.Civil.CapitalizationType"""
    def __init__(self, *args) -> None: ...
    MeterPerSecSquared: int  # = 202
    FootPerSecSquared: int  # = 203
class CatchmentObjectType:
    """.NET enum: Autodesk.Civil.CatchmentObjectType"""
    def __init__(self, *args) -> None: ...
    Polyline2D: int  # = 0
    Polyline3D: int  # = 1
class CatchmentRainfallTravelTimeUnitType:
    """.NET enum: Autodesk.Civil.CatchmentRainfallTravelTimeUnitType"""
    def __init__(self, *args) -> None: ...
    Second: int  # = 300
    Minute: int  # = 301
    Hour: int  # = 302
class CatchmentShallowConcentratedFlowSurfaceType:
    """.NET enum: Autodesk.Civil.CatchmentShallowConcentratedFlowSurfaceType"""
    def __init__(self, *args) -> None: ...
    Paved: int  # = 0
    Unpaved: int  # = 1
class CatchmentTimeOfConcentrationMethodType:
    """.NET enum: Autodesk.Civil.CatchmentTimeOfConcentrationMethodType"""
    def __init__(self, *args) -> None: ...
    TR55: int  # = 1
    UserDefined: int  # = 2
class CatchmentWatershedObjectType:
    """.NET enum: Autodesk.Civil.CatchmentWatershedObjectType"""
    def __init__(self, *args) -> None: ...
    Polyline2D: int  # = 0
    Polyline3D: int  # = 1
class CivilException(Exception):
    """.NET: Autodesk.Civil.CivilException"""
    def __init__(self, *args) -> None: ...
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str
    @staticmethod
    def ErrorHandler(es: ErrorStatus, message: str) -> None: ...

class CivilVersion:
    """.NET enum: Autodesk.Civil.CivilVersion"""
    def __init__(self, *args) -> None: ...
    Civil2009: int  # = 2009
    Civil2010: int  # = 2010
    Civil2011: int  # = 2011
    Civil2012: int  # = 2012
    Civil2013: int  # = 2013
    Civil2014: int  # = 2014
    Civil2016: int  # = 2016
    Civil2020: int  # = 2020
    Civil2021: int  # = 2021
    Civil2022: int  # = 2022
    Civil2023: int  # = 2023
    Civil2024: int  # = 2024
    Civil2025: int  # = 2025
    Civil2026: int  # = 2026
class Constant:
    """.NET: Autodesk.Civil.Constant"""
    def __init__(self, *args) -> None: ...
    ...

class CorridorAlongCurveOption:
    """.NET enum: Autodesk.Civil.CorridorAlongCurveOption"""
    def __init__(self, *args) -> None: ...
    CurveAtIncrement: int  # = 0
    CurveByCurvature: int  # = 1
    CurveBoth: int  # = 2
class CorridorAlongOffsetTargetCurveOption:
    """.NET enum: Autodesk.Civil.CorridorAlongOffsetTargetCurveOption"""
    def __init__(self, *args) -> None: ...
    TargetCurveNone: int  # = 0
    TargetCurveAtIncrement: int  # = 1
    TargetCurveByCurvature: int  # = 2
class CorridorRegionLockType:
    """.NET enum: Autodesk.Civil.CorridorRegionLockType"""
    def __init__(self, *args) -> None: ...
    GeometryLock: int  # = 1
    StationLock: int  # = 2
class CrossSectionShapeType:
    """.NET enum: Autodesk.Civil.CrossSectionShapeType"""
    def __init__(self, *args) -> None: ...
    Planar: int  # = 1793
    Crowned: int  # = 1794
class CrossingBreaklinesElevationType:
    """.NET enum: Autodesk.Civil.CrossingBreaklinesElevationType"""
    def __init__(self, *args) -> None: ...
    UseFirst: int  # = 0
    UseLast: int  # = 1
    UseAverage: int  # = 2
    UseNone: int  # = 3
class CurbReturnCurveGroupType:
    """.NET enum: Autodesk.Civil.CurbReturnCurveGroupType"""
    def __init__(self, *args) -> None: ...
    Arc: int  # = 2
    CCC: int  # = 3
    SCS: int  # = 4
    SSCS: int  # = 5
    SCSS: int  # = 6
    SSCSS: int  # = 7
class CurbReturnType:
    """.NET enum: Autodesk.Civil.CurbReturnType"""
    def __init__(self, *args) -> None: ...
    Chamfer: int  # = 1
    CircularFillet: int  # = 2
    ThreeCenteredArcs: int  # = 3
class DecimalCharacterType:
    """.NET enum: Autodesk.Civil.DecimalCharacterType"""
    def __init__(self, *args) -> None: ...
    Period: int  # = 2657
    Comma: int  # = 2658
class DeprecatedVersionAttribute(Attribute):
    """.NET: Autodesk.Civil.DeprecatedVersionAttribute"""
    def __init__(self, *args) -> None: ...
    Version: CivilVersion
    TypeId: object

class DesignCheck(CivilWrapper<AcDbDatabase>):
    """.NET: Autodesk.Civil.DesignCheck"""
    def __init__(self, *args) -> None: ...
    Expression: str
    Description: str
    Name: str

class DesignCheckCollection<Autodesk::Civil::AlignmentDesignCheck ^>:
    """.NET: Autodesk.Civil.DesignCheckCollection<Autodesk::Civil::AlignmentDesignCheck ^>"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: AlignmentDesignCheck
    Item: AlignmentDesignCheck
    def Add(self, name: str, description: str, expression: str) -> AlignmentDesignCheck: ...
    def Clear(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, name: str) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class DesignCheckCollection<Autodesk::Civil::ProfileDesignCheck ^>:
    """.NET: Autodesk.Civil.DesignCheckCollection<Autodesk::Civil::ProfileDesignCheck ^>"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: ProfileDesignCheck
    Item: ProfileDesignCheck
    def Add(self, name: str, description: str, expression: str) -> ProfileDesignCheck: ...
    def Clear(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, name: str) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class DesignSpeedLookupMethodType:
    """.NET enum: Autodesk.Civil.DesignSpeedLookupMethodType"""
    def __init__(self, *args) -> None: ...
    Interpolate: int  # = 2049
    Nearest: int  # = 2050
    RoundToNearest: int  # = 2051
class DimensionAnchorOptionType:
    """.NET enum: Autodesk.Civil.DimensionAnchorOptionType"""
    def __init__(self, *args) -> None: ...
    Elevation: int  # = 0
    Above: int  # = 1
    Below: int  # = 2
    Default: int  # = 3
    ViewTop: int  # = 4
    ViewBottom: int  # = 5
class DimensionAnchorType:
    """.NET enum: Autodesk.Civil.DimensionAnchorType"""
    def __init__(self, *args) -> None: ...
    FixedElevation: int  # = 0
    DistanceAbove: int  # = 1
    DistanceBelow: int  # = 2
    GraphViewTop: int  # = 4
    GraphViewBottom: int  # = 5
class DirectionDisplayType:
    """.NET enum: Autodesk.Civil.DirectionDisplayType"""
    def __init__(self, *args) -> None: ...
    ShortName: int  # = 2549
    LongName: int  # = 2550
    ShortNameSpaced: int  # = 2556
    LongNameSpaced: int  # = 2557
class DirectionNameDisplayType:
    """.NET enum: Autodesk.Civil.DirectionNameDisplayType"""
    def __init__(self, *args) -> None: ...
    PreserveCase: int  # = 2449
    UpperCase: int  # = 2450
    LowerCase: int  # = 2451
    TitleCaps: int  # = 2452
class DistanceScaleFactorType:
    """.NET enum: Autodesk.Civil.DistanceScaleFactorType"""
    def __init__(self, *args) -> None: ...
    Distance: int  # = 0
    ScaleFactor: int  # = 1
class DrivingDirectionType:
    """.NET enum: Autodesk.Civil.DrivingDirectionType"""
    def __init__(self, *args) -> None: ...
    RightSideOfTheRoad: int  # = 0
    LeftSideOfTheRoad: int  # = 1
class DropDecimalWholeType:
    """.NET enum: Autodesk.Civil.DropDecimalWholeType"""
    def __init__(self, *args) -> None: ...
    Yes: int  # = 2705
    No: int  # = 2706
class DropLeadingZeroType:
    """.NET enum: Autodesk.Civil.DropLeadingZeroType"""
    def __init__(self, *args) -> None: ...
    Yes: int  # = 2707
    No: int  # = 2708
class ElevationSourceType:
    """.NET enum: Autodesk.Civil.ElevationSourceType"""
    def __init__(self, *args) -> None: ...
    Surface: int  # = 0
    Grading: int  # = 1
    FixedElevation: int  # = 2
class ElevationToUseType:
    """.NET enum: Autodesk.Civil.ElevationToUseType"""
    def __init__(self, *args) -> None: ...
    UseFirst: int  # = 0
    UseLast: int  # = 1
    UseAverage: int  # = 2
class EntityNotFoundException(CivilException):
    """.NET: Autodesk.Civil.EntityNotFoundException"""
    def __init__(self, *args) -> None: ...
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str

class EntitySideType:
    """.NET enum: Autodesk.Civil.EntitySideType"""
    def __init__(self, *args) -> None: ...
    Left: int  # = 1
    Right: int  # = 2
class ErrorStatus:
    """.NET enum: Autodesk.Civil.ErrorStatus"""
    def __init__(self, *args) -> None: ...
    Ok: int  # = 0
    PointNotOnEntity: int  # = 1
    EntityNotFound: int  # = 2
    ObjectNotOverridable: int  # = 3
    PropertyNotInheritable: int  # = 4
    PropertyLockedByAncestor: int  # = 5
    AlignmentError: int  # = 5000
    NoPrevAlignmentEntity: int  # = 5001
    NoNextAlignmentEntity: int  # = 5002
    ProfileError: int  # = 6000
    SurfaceError: int  # = 7000
    NoSurfaceFound: int  # = 7001
    ProcessingInterrupted: int  # = 7002
    NoPointsInSurface: int  # = 7003
    NoTrianglesInSurface: int  # = 7004
    NoTriangleFound: int  # = 7005
    PointOutsideSurface: int  # = 7006
    TriangleIsDeleted: int  # = 7007
    NoBorderFound: int  # = 7008
    NoRangePointsFound: int  # = 7009
    TrianglesAreNotNeeghbors: int  # = 7010
    NoIntersectionFound: int  # = 7011
    DuplicatePoint: int  # = 7012
    NoPointFound: int  # = 7013
    UnableToReadFile: int  # = 7014
    NoEdgeFound: int  # = 7015
    EdgeIsLocked: int  # = 7016
    CantSwap: int  # = 7017
    LoadFailed: int  # = 7018
    DuplicateName: int  # = 7019
    IllegalBoundary: int  # = 7020
    InvalidFileFormat: int  # = 7021
    SnapshotNotFound: int  # = 7022
    GradingPasteToTargetSurfRejected: int  # = 7023
    CorridorError: int  # = 8000
    SurveyError: int  # = 9000
    PrjStatusInsertError: int  # = 9001
    PrjStatusWrongSvProject: int  # = 9002
    PrjStatusWrongVaultProject: int  # = 9003
    MetaQueryStatusNoName: int  # = 9004
    MetaQueryStatusDuplicateName: int  # = 9005
    MetaQueryStatusNotFound: int  # = 9006
    MetaQueryStatusQueryDataFileMissing: int  # = 9007
    SdxStatusDatabaseNotOpen: int  # = 9008
    SdxStatusDatabaseNotReadable: int  # = 9009
    SdxStatusDatabaseNotWritable: int  # = 9010
    SdxStatusDefFileNotAvailable: int  # = 9011
    SdxStatusDatabaseNotAvailable: int  # = 9012
    SdxStatusActiveDrawingRequiredToOpen: int  # = 9013
    SdbStatusCorruption: int  # = 9014
    SdbStatusDatabaseDoesNotExist: int  # = 9015
    SdbStatusDatabaseDirectoryNotWritable: int  # = 9016
    SdbStatusDatabaseNotReadable: int  # = 9017
    SdbStatusDatabaseNotWritable: int  # = 9018
    SdbStatusDatabaseNotOpen: int  # = 9019
    SdbStatusDatabaseVersionNewerThanSupported: int  # = 9020
    SdbStatusDatabaseVersionCanNotBeUpgraded: int  # = 9021
    SdbStatusDatabaseNeedMigration: int  # = 9022
    SdbStatusDatabaseAccessPermissionDenied: int  # = 9023
    SdbStatusDatabaseCreateCacheCopyFailed: int  # = 9024
    SdbStatusDatabaseDuplicateProjectGUID: int  # = 9025
    SdbStatusDatabaseProjectInfoMissingOrFailedToCreate: int  # = 9026
    UnknownError: int  # = -1
class ErrorStatusText:
    """.NET: Autodesk.Civil.ErrorStatusText"""
    def __init__(self, *args) -> None: ...
    Text: str

class ExportDetermineElevationType:
    """.NET enum: Autodesk.Civil.ExportDetermineElevationType"""
    def __init__(self, *args) -> None: ...
    SampleSurfaceAtGridPoint: int  # = 0
    Average: int  # = 1
class FeatureLineConnectDirectionType:
    """.NET enum: Autodesk.Civil.FeatureLineConnectDirectionType"""
    def __init__(self, *args) -> None: ...
    Inward: int  # = 0
    Outward: int  # = 1
class FeatureLineLayerSettingType:
    """.NET enum: Autodesk.Civil.FeatureLineLayerSettingType"""
    def __init__(self, *args) -> None: ...
    UseLayerSetting: int  # = 0
    UseCurrentLayer: int  # = 1
    UserEntityLayer: int  # = 2
class FeatureLineLayerType:
    """.NET enum: Autodesk.Civil.FeatureLineLayerType"""
    def __init__(self, *args) -> None: ...
    LayerSetting: int  # = 0
    CurrentLayer: int  # = 1
class FeatureLinePointType:
    """.NET enum: Autodesk.Civil.FeatureLinePointType"""
    def __init__(self, *args) -> None: ...
    PIPoint: int  # = 0
    ElevationPoint: int  # = 1
    AllPoints: int  # = 2
class FlowUnitType:
    """.NET enum: Autodesk.Civil.FlowUnitType"""
    def __init__(self, *args) -> None: ...
    CubicMeterPerSec: int  # = 204
    CubicFootPerSec: int  # = 208
class FreeHaulDisplayType:
    """.NET enum: Autodesk.Civil.FreeHaulDisplayType"""
    def __init__(self, *args) -> None: ...
    GradePoint: int  # = 0
    BalancePoint: int  # = 1
class GeometryPointLabelOption:
    """.NET: Autodesk.Civil.GeometryPointLabelOption`1"""
    def __init__(self, *args) -> None: ...
    Selected: bool
    PointType: T

class GeometryPointSelector:
    """.NET: Autodesk.Civil.GeometryPointSelector`1"""
    def __init__(self, *args) -> None: ...
    Item: GeometryPointLabelOption
    def SelectAll(self, ) -> None: ...
    def UnSelectAll(self, ) -> None: ...

class GradeFormatType:
    """.NET enum: Autodesk.Civil.GradeFormatType"""
    def __init__(self, *args) -> None: ...
    Percent: int  # = 2467
    Decimal: int  # = 2468
    PerMille: int  # = 2476
class GradeSlopeFormatType:
    """.NET enum: Autodesk.Civil.GradeSlopeFormatType"""
    def __init__(self, *args) -> None: ...
    RiseRun: int  # = 2465
    RunRise: int  # = 2466
    Percent: int  # = 2467
    Decimal: int  # = 2468
    PerMille: int  # = 2476
class GradingDistanceProjectionType:
    """.NET enum: Autodesk.Civil.GradingDistanceProjectionType"""
    def __init__(self, *args) -> None: ...
    Slope: int  # = 3
    RelativeElevation: int  # = 5
class GradingElevationProjectionType:
    """.NET enum: Autodesk.Civil.GradingElevationProjectionType"""
    def __init__(self, *args) -> None: ...
    CutFillSlope: int  # = 0
    CutSlope: int  # = 1
    FillSlope: int  # = 2
class GradingInteriorCornerOverlapSolutionType:
    """.NET enum: Autodesk.Civil.GradingInteriorCornerOverlapSolutionType"""
    def __init__(self, *args) -> None: ...
    UseAverageSlope: int  # = 0
    HoldSlopeAsMinimum: int  # = 1
    HoldSlopeAsMaximum: int  # = 2
class GradingRelativeElevationProjectionType:
    """.NET enum: Autodesk.Civil.GradingRelativeElevationProjectionType"""
    def __init__(self, *args) -> None: ...
    Slope: int  # = 3
    Distance: int  # = 6
class GradingSearchOrderType:
    """.NET enum: Autodesk.Civil.GradingSearchOrderType"""
    def __init__(self, *args) -> None: ...
    CutFirst: int  # = 0
    FillFirst: int  # = 1
class GradingSlopeFormatType:
    """.NET enum: Autodesk.Civil.GradingSlopeFormatType"""
    def __init__(self, *args) -> None: ...
    Slope: int  # = 0
    Grade: int  # = 1
class GradingSurfaceProjectionType:
    """.NET enum: Autodesk.Civil.GradingSurfaceProjectionType"""
    def __init__(self, *args) -> None: ...
    CutFillSlope: int  # = 0
    CutSlope: int  # = 1
    FillSlope: int  # = 2
class GradingTargetType:
    """.NET enum: Autodesk.Civil.GradingTargetType"""
    def __init__(self, *args) -> None: ...
    Surface: int  # = 0
    Elevation: int  # = 1
    RelativeElevation: int  # = 2
    Distance: int  # = 3
class HighSideShoulderMethodType:
    """.NET enum: Autodesk.Civil.HighSideShoulderMethodType"""
    def __init__(self, *args) -> None: ...
    DefaultSlope: int  # = 2561
    MatchLaneSlope: int  # = 2562
class HighsideLocationType:
    """.NET enum: Autodesk.Civil.HighsideLocationType"""
    def __init__(self, *args) -> None: ...
    LeftEdge: int  # = 2817
    Level: int  # = 2818
    RightEdge: int  # = 2819
class IProperty:
    """.NET: Autodesk.Civil.IProperty"""
    def __init__(self, *args) -> None: ...
    Value: object
    IsOverridable: bool
    Overridden: bool
    Locked: bool

class ImpliedPointOfIntersectionDisplayType:
    """.NET enum: Autodesk.Civil.ImpliedPointOfIntersectionDisplayType"""
    def __init__(self, *args) -> None: ...
    ByChangeInDirection: int  # = 1
    ByIndividualCurves: int  # = 2
    DoNotDisplayImpliedPI: int  # = 3
class InternalC3DPipesToStmMigration:
    """.NET: Autodesk.Civil.InternalC3DPipesToStmMigration"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def Migrate(pDwgDb: Database, stmFileName: str, pipeNetworkIds: ObjectIdCollection) -> bool: ...

class KrigingSemivariogramType:
    """.NET enum: Autodesk.Civil.KrigingSemivariogramType"""
    def __init__(self, *args) -> None: ...
    Linear: int  # = 2048
    Monomial: int  # = 4096
    Spherical: int  # = 8192
    Exponential: int  # = 16384
    Gaussian: int  # = 32768
class LabelContentDisplayType:
    """.NET enum: Autodesk.Civil.LabelContentDisplayType"""
    def __init__(self, *args) -> None: ...
    Composed: int  # = 0
    StackedText: int  # = 1
class LabelInsertionType:
    """.NET enum: Autodesk.Civil.LabelInsertionType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Top: int  # = 1
    Bottom: int  # = 2
class LabelInsideCurveType:
    """.NET enum: Autodesk.Civil.LabelInsideCurveType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Inside: int  # = 1
    Outside: int  # = 2
class LabelMaskType:
    """.NET enum: Autodesk.Civil.LabelMaskType"""
    def __init__(self, *args) -> None: ...
    FromLabelStyle: int  # = 0
    ObjectOnly: int  # = 1
class LabelRotationType:
    """.NET enum: Autodesk.Civil.LabelRotationType"""
    def __init__(self, *args) -> None: ...
    NotSupported: int  # = 0
    Dragged: int  # = 1
    NonDragged: int  # = 2
    Both: int  # = 3
class LabelStyleLengthType:
    """.NET enum: Autodesk.Civil.LabelStyleLengthType"""
    def __init__(self, *args) -> None: ...
    FixedLength: int  # = 0
    PercentLength: int  # = 1
class LabelTextAttachmentType:
    """.NET enum: Autodesk.Civil.LabelTextAttachmentType"""
    def __init__(self, *args) -> None: ...
    TopLeft: int  # = 0
    TopCenter: int  # = 1
    TopRight: int  # = 2
    MiddleLeft: int  # = 3
    MiddleCenter: int  # = 4
    MiddleRight: int  # = 5
    BottomLeft: int  # = 6
    BottomCenter: int  # = 7
    BottomRight: int  # = 8
class LabelingPromptType:
    """.NET enum: Autodesk.Civil.LabelingPromptType"""
    def __init__(self, *args) -> None: ...
    Suppress: int  # = 0
    CommandLine: int  # = 1
    Dialog: int  # = 2
class LandXMLImportAlignmentType:
    """.NET enum: Autodesk.Civil.LandXMLImportAlignmentType"""
    def __init__(self, *args) -> None: ...
    FixedOnly: int  # = 0
    FloatingOffFirstElement: int  # = 1
    FreeAndFloatingCurveGroups: int  # = 2
class LandXMLImportFeatureLineSite:
    """.NET enum: Autodesk.Civil.LandXMLImportFeatureLineSite"""
    def __init__(self, *args) -> None: ...
    FeatureLineSiteUsingSourceFile: int  # = 0
    FeatureLineSiteUsingDialogUI: int  # = 1
class LatLongDirectionType:
    """.NET enum: Autodesk.Civil.LatLongDirectionType"""
    def __init__(self, *args) -> None: ...
    PrefixShortName: int  # = 2545
    PrefixLongName: int  # = 2546
    SuffixLongName: int  # = 2548
    LongName: int  # = 2550
    PrefixShortNameSpaced: int  # = 2552
    PrefixLongNameSpaced: int  # = 2553
    SuffixLongNameSpaced: int  # = 2555
    LongNameSpaced: int  # = 2557
class LayoutModeType:
    """.NET enum: Autodesk.Civil.LayoutModeType"""
    def __init__(self, *args) -> None: ...
    Label: int  # = 1
    Tag: int  # = 2
    LabelTag: int  # = 3
class LeaderAttachmentBehaviorType:
    """.NET enum: Autodesk.Civil.LeaderAttachmentBehaviorType"""
    def __init__(self, *args) -> None: ...
    ToPoint: int  # = 0
    ToMarkerExtents: int  # = 1
    FromMarkerStyle: int  # = 2
class LeaderAttachmentType:
    """.NET enum: Autodesk.Civil.LeaderAttachmentType"""
    def __init__(self, *args) -> None: ...
    LeaderTopOfTopLine: int  # = 0
    LeaderMiddleOfTopLine: int  # = 1
    LeaderMiddle: int  # = 2
    LeaderMiddleOfBottomLine: int  # = 3
    LeaderBottomOfBottomLine: int  # = 4
class LeaderShapeType:
    """.NET enum: Autodesk.Civil.LeaderShapeType"""
    def __init__(self, *args) -> None: ...
    Straight: int  # = 0
    Spline: int  # = 1
class LeaderTailVisibilityType:
    """.NET enum: Autodesk.Civil.LeaderTailVisibilityType"""
    def __init__(self, *args) -> None: ...
    FromLabelStyle: int  # = 0
    AlwaysHide: int  # = 1
class LeaderVisibilityType:
    """.NET enum: Autodesk.Civil.LeaderVisibilityType"""
    def __init__(self, *args) -> None: ...
    FromLabelStyle: int  # = 0
    AlwaysHide: int  # = 1
class LinearUnitType:
    """.NET enum: Autodesk.Civil.LinearUnitType"""
    def __init__(self, *args) -> None: ...
    Meter: int  # = 2
    Kilometer: int  # = 20
    Decimeter: int  # = 23
    Centimeter: int  # = 24
    Millimeter: int  # = 25
    Foot: int  # = 30
    Inch: int  # = 31
    Yard: int  # = 33
    Mile: int  # = 44
class LinkCreationType:
    """.NET enum: Autodesk.Civil.LinkCreationType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Single: int  # = 1
    Multiple: int  # = 2
class LowSideShoulderMethodType:
    """.NET enum: Autodesk.Civil.LowSideShoulderMethodType"""
    def __init__(self, *args) -> None: ...
    DefaultSlope: int  # = 2561
    MatchLaneSlope: int  # = 2562
    BreakoverRemoval: int  # = 2564
class MassHaulLineDisplayStyleType:
    """.NET enum: Autodesk.Civil.MassHaulLineDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    MassHaulLine: int  # = 0
    FreeHaulLine: int  # = 1
    FreeHaulAreaHatch: int  # = 2
    OverHaulAreaHatch: int  # = 3
class MassHaulLineHatchDisplayStyleType:
    """.NET enum: Autodesk.Civil.MassHaulLineHatchDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    FreeHaulAreaHatch: int  # = 0
    OverHaulAreaHatch: int  # = 1
class MassHaulViewDisplayStyleType:
    """.NET enum: Autodesk.Civil.MassHaulViewDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    GraphTitle: int  # = 0
    LeftAxis: int  # = 1
    LeftAxisTitle: int  # = 2
    LeftAxisAnnotationMajor: int  # = 3
    LeftAxisAnnotationMinor: int  # = 4
    LeftAxisTicksMajor: int  # = 5
    LeftAxisTicksMinor: int  # = 6
    RightAxis: int  # = 7
    RightAxisTitle: int  # = 8
    RightAxisAnnotationMajor: int  # = 9
    RightAxisAnnotationMinor: int  # = 10
    RightAxisTicksMajor: int  # = 11
    RightAxisTicksMinor: int  # = 12
    TopAxis: int  # = 13
    TopAxisTitle: int  # = 14
    TopAxisAnnotationMajor: int  # = 15
    TopAxisAnnotationMinor: int  # = 16
    TopAxisTicksMajor: int  # = 17
    TopAxisTicksMinor: int  # = 18
    BottomAxis: int  # = 19
    BottomAxisTitle: int  # = 20
    BottomAxisAnnotationMajor: int  # = 21
    BottomAxisAnnotationMinor: int  # = 22
    BottomAxisTicksMajor: int  # = 23
    BottomAxisTicksMinor: int  # = 24
    MiddleAxis: int  # = 25
    MiddleAxisTitle: int  # = 26
    MiddleAxisAnnotationMajor: int  # = 27
    MiddleAxisAnnotationMinor: int  # = 28
    MiddleAxisTicksMajor: int  # = 29
    MiddleAxisTicksMinor: int  # = 30
    GridHorizontalMajor: int  # = 37
    GridHorizontalMinor: int  # = 38
    GridVerticalMajor: int  # = 39
    GridVerticalMinor: int  # = 40
    GridAtHGP: int  # = 44
    TopAxisAnnotationHGP: int  # = 47
    TopAxisTicksHGP: int  # = 48
    BottomAxisAnnotationHGP: int  # = 49
    BottomAxisTicksHGP: int  # = 50
    MiddleAxisAnnotationHGP: int  # = 51
    MiddleAxisTicksHGP: int  # = 52
    GridAtSampleLineStations: int  # = 53
class MatchLineLabelLocationType:
    """.NET enum: Autodesk.Civil.MatchLineLabelLocationType"""
    def __init__(self, *args) -> None: ...
    Start: int  # = 1
    Middle: int  # = 2
    End: int  # = 3
    Intersection: int  # = 4
class NetworkDefaultLayoutCommandType:
    """.NET enum: Autodesk.Civil.NetworkDefaultLayoutCommandType"""
    def __init__(self, *args) -> None: ...
    PipesAndStrucutres: int  # = 100
    PipesOnly: int  # = 101
    StrucutresOnly: int  # = 102
class OrientationReferenceType:
    """.NET enum: Autodesk.Civil.OrientationReferenceType"""
    def __init__(self, *args) -> None: ...
    Object: int  # = 0
    View: int  # = 1
    WorldCoordinateSystem: int  # = 2
class ParcelAnalysisType:
    """.NET enum: Autodesk.Civil.ParcelAnalysisType"""
    def __init__(self, *args) -> None: ...
    Inverse: int  # = 0
    Mapcheck: int  # = 1
class ParcelRemainderDistributionType:
    """.NET enum: Autodesk.Civil.ParcelRemainderDistributionType"""
    def __init__(self, *args) -> None: ...
    CreateRemainderParcel: int  # = 0
    PlaceRemainderInLastParcel: int  # = 1
    RedistributeRemainder: int  # = 2
class ParcelSelectionType:
    """.NET enum: Autodesk.Civil.ParcelSelectionType"""
    def __init__(self, *args) -> None: ...
    PickPointWithinParcel: int  # = 0
    SelectParcelAreaLabel: int  # = 1
class ParcelSolutionType:
    """.NET enum: Autodesk.Civil.ParcelSolutionType"""
    def __init__(self, *args) -> None: ...
    UseShortestFrontage: int  # = 0
    UseSmallestArea: int  # = 1
class PipeNetworkPartDisplayType:
    """.NET enum: Autodesk.Civil.PipeNetworkPartDisplayType"""
    def __init__(self, *args) -> None: ...
    OnlySelected: int  # = 0
    All: int  # = 1
class PipeSectionLabelPlacementType:
    """.NET enum: Autodesk.Civil.PipeSectionLabelPlacementType"""
    def __init__(self, *args) -> None: ...
    AtPipeTop: int  # = 0
    AtPipeMiddle: int  # = 1
    AtPipeBottom: int  # = 2
class PlacementOptionType:
    """.NET enum: Autodesk.Civil.PlacementOptionType"""
    def __init__(self, *args) -> None: ...
    Draft: int  # = 0
    Production: int  # = 2
class PlanViewAlignType:
    """.NET enum: Autodesk.Civil.PlanViewAlignType"""
    def __init__(self, *args) -> None: ...
    Start: int  # = 0
    Center: int  # = 1
    End: int  # = 2
class PlottedUnitDisplayType:
    """.NET enum: Autodesk.Civil.PlottedUnitDisplayType"""
    def __init__(self, *args) -> None: ...
    Decimal: int  # = 0
    Fractional: int  # = 1
class PointCloudDefaultFileExtensionType:
    """.NET enum: Autodesk.Civil.PointCloudDefaultFileExtensionType"""
    def __init__(self, *args) -> None: ...
    LAS: int  # = 0
    ASCIIXYZ: int  # = 1
    GEOTIFF: int  # = 2
    USGSDEM: int  # = 3
    ERSIASC: int  # = 4
    ERSIFLT: int  # = 5
    USGSDTS: int  # = 6
    POINTCLOUDDATABASE: int  # = 7
    PTS: int  # = 8
    PTX: int  # = 9
    TOPCONCLR: int  # = 10
    TOPCONCL3: int  # = 11
    ERSIADF: int  # = 12
    PTG: int  # = 13
class PointCloudDisplayStyleType:
    """.NET enum: Autodesk.Civil.PointCloudDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    BoundingBox: int  # = 0
    Points: int  # = 1
class PointCloudElevationRangeCreationType:
    """.NET enum: Autodesk.Civil.PointCloudElevationRangeCreationType"""
    def __init__(self, *args) -> None: ...
    NumberOfRanges: int  # = 0
    RangeInterval: int  # = 1
class PointCloudRangeColorSchemeType:
    """.NET enum: Autodesk.Civil.PointCloudRangeColorSchemeType"""
    def __init__(self, *args) -> None: ...
    Blues: int  # = 0
    Greens: int  # = 1
    Hydro: int  # = 2
    Land: int  # = 3
    Pastels: int  # = 4
    Rainbow: int  # = 5
    Reds: int  # = 6
class PointCloudRegionType:
    """.NET enum: Autodesk.Civil.PointCloudRegionType"""
    def __init__(self, *args) -> None: ...
    PointCloudExtents: int  # = 0
    Window: int  # = 1
    WindowPolygon: int  # = 2
    Object: int  # = 3
class PointCloudSurfaceType:
    """.NET enum: Autodesk.Civil.PointCloudSurfaceType"""
    def __init__(self, *args) -> None: ...
    NewSurface: int  # = 0
    ExistingSurface: int  # = 1
class PointCouldColorSchemeType:
    """.NET enum: Autodesk.Civil.PointCouldColorSchemeType"""
    def __init__(self, *args) -> None: ...
    TrueColor: int  # = 0
    Classification: int  # = 1
    GrayscaleIntensity: int  # = 2
    ScaledColorIntensity: int  # = 3
    ElevationRanges: int  # = 4
    SingleColor: int  # = 5
class PointFileFormatType:
    """.NET enum: Autodesk.Civil.PointFileFormatType"""
    def __init__(self, *args) -> None: ...
    PointFile: int  # = 0
    CogoDatabase: int  # = 1
    PointDatabase: int  # = 2
    Count: int  # = 3
class PointNamesExistType:
    """.NET enum: Autodesk.Civil.PointNamesExistType"""
    def __init__(self, *args) -> None: ...
    UseNameTemplate: int  # = 0
    Counter: int  # = 1
    Notify: int  # = 3
class PointNotOnEntityException(CivilException):
    """.NET: Autodesk.Civil.PointNotOnEntityException"""
    def __init__(self, *args) -> None: ...
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str

class PointNumbersAssignedType:
    """.NET enum: Autodesk.Civil.PointNumbersAssignedType"""
    def __init__(self, *args) -> None: ...
    UseNext: int  # = 0
    SequenceFrom: int  # = 1
class PointNumbersExistType:
    """.NET enum: Autodesk.Civil.PointNumbersExistType"""
    def __init__(self, *args) -> None: ...
    Renumber: int  # = 0
    Merge: int  # = 1
    Overwrite: int  # = 2
    Notify: int  # = 3
class PointNumbersSuppliedType:
    """.NET enum: Autodesk.Civil.PointNumbersSuppliedType"""
    def __init__(self, *args) -> None: ...
    Use: int  # = 0
    Ignore: int  # = 1
    AddOffset: int  # = 2
class PressureUnitType:
    """.NET enum: Autodesk.Civil.PressureUnitType"""
    def __init__(self, *args) -> None: ...
    Pascals: int  # = 13
    Kilopascal: int  # = 240
    Megapascal: int  # = 241
    PoundPerSquareInch: int  # = 242
    Bar: int  # = 261
class ProfileApplyCurveType:
    """.NET enum: Autodesk.Civil.ProfileApplyCurveType"""
    def __init__(self, *args) -> None: ...
    CrestAndSag: int  # = 0
    CrestOnly: int  # = 1
    SagOnly: int  # = 2
class ProfileCircularVerticalConstraintType:
    """.NET enum: Autodesk.Civil.ProfileCircularVerticalConstraintType"""
    def __init__(self, *args) -> None: ...
    CurveLength: int  # = 513
    Radius: int  # = 515
class ProfileCurveType:
    """.NET enum: Autodesk.Civil.ProfileCurveType"""
    def __init__(self, *args) -> None: ...
    Circular: int  # = 258
    SymmetricParabola: int  # = 259
    AsymmetricParabola: int  # = 260
class ProfileDesignCheck(DesignCheck):
    """.NET: Autodesk.Civil.ProfileDesignCheck"""
    def __init__(self, *args) -> None: ...
    DesignCheckType: ProfileDesignCheckType
    Expression: str
    Description: str
    Name: str

class ProfileDesignCheckCollection(DesignCheckCollection<Autodesk::Civil::ProfileDesignCheck ^>):
    """.NET: Autodesk.Civil.ProfileDesignCheckCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: ProfileDesignCheck
    Item: ProfileDesignCheck
    def Add(self, name: str, description: str, expression: str) -> ProfileDesignCheck: ...
    def Clear(self, ) -> None: ...
    def Remove(self, name: str) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class ProfileDesignCheckRoot:
    """.NET: Autodesk.Civil.ProfileDesignCheckRoot"""
    def __init__(self, *args) -> None: ...
    CurveDesignChecks: ProfileDesignCheckCollection
    LineDesignChecks: ProfileDesignCheckCollection

class ProfileDesignCheckType:
    """.NET enum: Autodesk.Civil.ProfileDesignCheckType"""
    def __init__(self, *args) -> None: ...
    Line: int  # = 251704645
    Curve: int  # = 251704646
class ProfileParabolicVerticalConstraintType:
    """.NET enum: Autodesk.Civil.ProfileParabolicVerticalConstraintType"""
    def __init__(self, *args) -> None: ...
    CurveLength: int  # = 513
    KValue: int  # = 514
class ProfilePointType:
    """.NET enum: Autodesk.Civil.ProfilePointType"""
    def __init__(self, *args) -> None: ...
    TanCurve: int  # = 273
    CurveTan: int  # = 274
    CompCurve: int  # = 275
    RevCurve: int  # = 276
    LowPoint: int  # = 277
    HighPoint: int  # = 278
    PVI: int  # = 279
    Start: int  # = 280
    End: int  # = 281
    GradeBreak: int  # = 282
    OverallLowPoint: int  # = 283
    OverallHighPoint: int  # = 284
class ProfileViewDatumType:
    """.NET enum: Autodesk.Civil.ProfileViewDatumType"""
    def __init__(self, *args) -> None: ...
    MinElevation: int  # = 0
    MeanElevation: int  # = 1
class ProfileViewPlotType:
    """.NET enum: Autodesk.Civil.ProfileViewPlotType"""
    def __init__(self, *args) -> None: ...
    ByRows: int  # = 0
    ByColumns: int  # = 1
class ProfileViewSplitDatumType:
    """.NET enum: Autodesk.Civil.ProfileViewSplitDatumType"""
    def __init__(self, *args) -> None: ...
    ExactElevation: int  # = 0
    PreviousMajorGrid: int  # = 1
    PreviousMinorGrid: int  # = 2
class ProfileViewSplitStationType:
    """.NET enum: Autodesk.Civil.ProfileViewSplitStationType"""
    def __init__(self, *args) -> None: ...
    ExactStation: int  # = 0
    PreviousMajorGrid: int  # = 1
    PreviousMinorGrid: int  # = 2
class ProfileViewStartCornerType:
    """.NET enum: Autodesk.Civil.ProfileViewStartCornerType"""
    def __init__(self, *args) -> None: ...
    LowerLeft: int  # = 0
    UpperLeft: int  # = 1
    LowerRight: int  # = 2
    UpperRight: int  # = 3
class ProjecitonPercentageType:
    """.NET enum: Autodesk.Civil.ProjecitonPercentageType"""
    def __init__(self, *args) -> None: ...
    Percentage_0: int  # = 1
    Percentage_25: int  # = 2
    Percentage_50: int  # = 3
    Percentage_75: int  # = 4
    Percentage_100: int  # = 5
class ProjecitonRule:
    """.NET enum: Autodesk.Civil.ProjecitonRule"""
    def __init__(self, *args) -> None: ...
    ByPercentage: int  # = 1
    ByDistance: int  # = 2
class ProjectionUtil:
    """.NET: Autodesk.Civil.ProjectionUtil"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def IsProfileProjectionObject(projectionId: ObjectId, gsMarker: IntPtr) -> bool: ...
    @staticmethod
    def IsSectionProjectionObject(projectionId: ObjectId, gsMarker: IntPtr) -> bool: ...

class Property<Autodesk::AutoCAD::Colors::Color ^\,AcCmColor\,Autodesk::Civil::CastOp<Autodesk::AutoCAD::Colors::Color ^\,AcCmColor> >(TreeOidWrapper):
    """.NET: Autodesk.Civil.Property<Autodesk::AutoCAD::Colors::Color ^\,AcCmColor\,Autodesk::Civil::CastOp<Autodesk::AutoCAD::Colors::Color ^\,AcCmColor> >"""
    def __init__(self, *args) -> None: ...
    Value: Color
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Property<Autodesk::AutoCAD::DatabaseServices::ObjectIdCollection ^\,std::vector<AeccAttribute\,std::allocator<AeccAttribute> >\,Autodesk::Civil::CastOp<Autodesk::AutoCAD::DatabaseServices::ObjectIdCollection ^\,std::vector<AeccAttribute\,std::allocator<AeccAttribute> > > >(TreeOidWrapper):
    """.NET: Autodesk.Civil.Property<Autodesk::AutoCAD::DatabaseServices::ObjectIdCollection ^\,std::vector<AeccAttribute\,std::allocator<AeccAttribute> >\,Autodesk::Civil::CastOp<Autodesk::AutoCAD::DatabaseServices::ObjectIdCollection ^\,std::vector<AeccAttribute\,std::allocator<AeccAttribute> > > >"""
    def __init__(self, *args) -> None: ...
    Value: ObjectIdCollection
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Property<Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::CastOp<Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId> >(TreeOidWrapper):
    """.NET: Autodesk.Civil.Property<Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::CastOp<Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId> >"""
    def __init__(self, *args) -> None: ...
    Value: ObjectId
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Property<System::String ^\,AecRmCString\,Autodesk::Civil::CastOp<System::String ^\,AecRmCString> >(TreeOidWrapper):
    """.NET: Autodesk.Civil.Property<System::String ^\,AecRmCString\,Autodesk::Civil::CastOp<System::String ^\,AecRmCString> >"""
    def __init__(self, *args) -> None: ...
    Value: str
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Property<bool\,bool\,Autodesk::Civil::CastOp<bool\,bool> >(TreeOidWrapper):
    """.NET: Autodesk.Civil.Property<bool\,bool\,Autodesk::Civil::CastOp<bool\,bool> >"""
    def __init__(self, *args) -> None: ...
    Value: bool
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Property<double\,double\,Autodesk::Civil::CastOp<double\,double> >(TreeOidWrapper):
    """.NET: Autodesk.Civil.Property<double\,double\,Autodesk::Civil::CastOp<double\,double> >"""
    def __init__(self, *args) -> None: ...
    Value: float
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Property<int\,int\,Autodesk::Civil::CastOp<int\,int> >(TreeOidWrapper):
    """.NET: Autodesk.Civil.Property<int\,int\,Autodesk::Civil::CastOp<int\,int> >"""
    def __init__(self, *args) -> None: ...
    Value: int
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Property<unsigned int\,int\,Autodesk::Civil::CastOp<unsigned int\,int> >(TreeOidWrapper):
    """.NET: Autodesk.Civil.Property<unsigned int\,int\,Autodesk::Civil::CastOp<unsigned int\,int> >"""
    def __init__(self, *args) -> None: ...
    Value: int
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PropertyAnchorPoint(Property<int\,int\,Autodesk::Civil::CastOp<int\,int> >):
    """.NET: Autodesk.Civil.PropertyAnchorPoint"""
    def __init__(self, *args) -> None: ...
    Value: AnchorPointType
    Value: int
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PropertyAngle(PropertyDouble):
    """.NET: Autodesk.Civil.PropertyAngle"""
    def __init__(self, *args) -> None: ...
    Value: float
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PropertyArrowhead(PropertyString):
    """.NET: Autodesk.Civil.PropertyArrowhead"""
    def __init__(self, *args) -> None: ...
    Value: str
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PropertyBlock(PropertyString):
    """.NET: Autodesk.Civil.PropertyBlock"""
    def __init__(self, *args) -> None: ...
    Value: str
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PropertyBoolean(Property<bool\,bool\,Autodesk::Civil::CastOp<bool\,bool> >):
    """.NET: Autodesk.Civil.PropertyBoolean"""
    def __init__(self, *args) -> None: ...
    Value: bool
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PropertyColor(Property<Autodesk::AutoCAD::Colors::Color ^\,AcCmColor\,Autodesk::Civil::CastOp<Autodesk::AutoCAD::Colors::Color ^\,AcCmColor> >):
    """.NET: Autodesk.Civil.PropertyColor"""
    def __init__(self, *args) -> None: ...
    Value: Color
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PropertyDouble(Property<double\,double\,Autodesk::Civil::CastOp<double\,double> >):
    """.NET: Autodesk.Civil.PropertyDouble"""
    def __init__(self, *args) -> None: ...
    Value: float
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PropertyEnum(Property<int\,int\,Autodesk::Civil::CastOp<int\,int> >):
    """.NET: Autodesk.Civil.PropertyEnum`1"""
    def __init__(self, *args) -> None: ...
    Value: T
    Value: int
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PropertyExpression(PropertyString):
    """.NET: Autodesk.Civil.PropertyExpression"""
    def __init__(self, *args) -> None: ...
    Value: str
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PropertyFeatureLineStylePriority(Property<Autodesk::AutoCAD::DatabaseServices::ObjectIdCollection ^\,std::vector<AeccAttribute\,std::allocator<AeccAttribute> >\,Autodesk::Civil::CastOp<Autodesk::AutoCAD::DatabaseServices::ObjectIdCollection ^\,std::vector<AeccAttribute\,std::allocator<AeccAttribute> > > >):
    """.NET: Autodesk.Civil.PropertyFeatureLineStylePriority"""
    def __init__(self, *args) -> None: ...
    Value: ObjectIdCollection
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PropertyInt(Property<int\,int\,Autodesk::Civil::CastOp<int\,int> >):
    """.NET: Autodesk.Civil.PropertyInt"""
    def __init__(self, *args) -> None: ...
    Value: int
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PropertyLayer(PropertyString):
    """.NET: Autodesk.Civil.PropertyLayer"""
    def __init__(self, *args) -> None: ...
    Value: str
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PropertyLinetype(PropertyString):
    """.NET: Autodesk.Civil.PropertyLinetype"""
    def __init__(self, *args) -> None: ...
    Value: str
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PropertyMText(PropertyString):
    """.NET: Autodesk.Civil.PropertyMText"""
    def __init__(self, *args) -> None: ...
    Value: str
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PropertyMaterial(PropertyString):
    """.NET: Autodesk.Civil.PropertyMaterial"""
    def __init__(self, *args) -> None: ...
    Value: str
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PropertyNameTemplate(PropertyString):
    """.NET: Autodesk.Civil.PropertyNameTemplate"""
    def __init__(self, *args) -> None: ...
    Value: str
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PropertyObjectId(Property<Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::CastOp<Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId> >):
    """.NET: Autodesk.Civil.PropertyObjectId"""
    def __init__(self, *args) -> None: ...
    Value: ObjectId
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PropertyObjectName(PropertyString):
    """.NET: Autodesk.Civil.PropertyObjectName"""
    def __init__(self, *args) -> None: ...
    Value: str
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PropertyString(Property<System::String ^\,AecRmCString\,Autodesk::Civil::CastOp<System::String ^\,AecRmCString> >):
    """.NET: Autodesk.Civil.PropertyString"""
    def __init__(self, *args) -> None: ...
    Value: str
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PropertyTextStyle(PropertyString):
    """.NET: Autodesk.Civil.PropertyTextStyle"""
    def __init__(self, *args) -> None: ...
    Value: str
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PropertyUInt(Property<unsigned int\,int\,Autodesk::Civil::CastOp<unsigned int\,int> >):
    """.NET: Autodesk.Civil.PropertyUInt"""
    def __init__(self, *args) -> None: ...
    Value: int
    IsOverridable: bool
    Overridden: bool
    Locked: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class QuantityTakeoffLengthComputeType:
    """.NET enum: Autodesk.Civil.QuantityTakeoffLengthComputeType"""
    def __init__(self, *args) -> None: ...
    Compute2D: int  # = 0
    Compute3D: int  # = 1
class QuantityTakeoffPipeLengthType:
    """.NET enum: Autodesk.Civil.QuantityTakeoffPipeLengthType"""
    def __init__(self, *args) -> None: ...
    ToInsideEdges: int  # = 0
    CenterToCenter: int  # = 1
class QuantityTakeoffReportExtentType:
    """.NET enum: Autodesk.Civil.QuantityTakeoffReportExtentType"""
    def __init__(self, *args) -> None: ...
    Drawing: int  # = 0
    Sheet: int  # = 1
    SelectionSet: int  # = 2
class QuantityTakeoffReportType:
    """.NET enum: Autodesk.Civil.QuantityTakeoffReportType"""
    def __init__(self, *args) -> None: ...
    Summary: int  # = 0
    Detailed: int  # = 1
class ROWCleanupType:
    """.NET enum: Autodesk.Civil.ROWCleanupType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Fillet: int  # = 1
    Chamfer: int  # = 2
class RadiusLookupMethodType:
    """.NET enum: Autodesk.Civil.RadiusLookupMethodType"""
    def __init__(self, *args) -> None: ...
    Interpolate: int  # = 2305
    Nearest: int  # = 2306
    RoundToNearest: int  # = 2307
class RailAlignmentPivotType:
    """.NET enum: Autodesk.Civil.RailAlignmentPivotType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    LeftRail: int  # = 1
    RightRail: int  # = 2
    Centerline: int  # = 3
class RoadwaySideType:
    """.NET enum: Autodesk.Civil.RoadwaySideType"""
    def __init__(self, *args) -> None: ...
    Right: int  # = 0
    Left: int  # = 1
class RotationDirType:
    """.NET enum: Autodesk.Civil.RotationDirType"""
    def __init__(self, *args) -> None: ...
    Clockwise: int  # = 0
    Counterclockwise: int  # = 1
class RoundingType:
    """.NET enum: Autodesk.Civil.RoundingType"""
    def __init__(self, *args) -> None: ...
    Normal: int  # = 2433
    Up: int  # = 2434
    Truncate: int  # = 2436
class SectionViewElevationRangeType:
    """.NET enum: Autodesk.Civil.SectionViewElevationRangeType"""
    def __init__(self, *args) -> None: ...
    LowestElevation: int  # = 0
    MeanElevation: int  # = 1
    FollowASection: int  # = 2
class SheetCreateType:
    """.NET enum: Autodesk.Civil.SheetCreateType"""
    def __init__(self, *args) -> None: ...
    NLayoutsPerNewDrawing: int  # = 0
    AllLayoutsInOneNewDrawing: int  # = 1
    AllLayoutsInCurrentDrawing: int  # = 2
class SheetSetType:
    """.NET enum: Autodesk.Civil.SheetSetType"""
    def __init__(self, *args) -> None: ...
    PlanAndProfile: int  # = 0
    PlanOnly: int  # = 1
    ProfileOnly: int  # = 2
class ShoulderMethodType:
    """.NET enum: Autodesk.Civil.ShoulderMethodType"""
    def __init__(self, *args) -> None: ...
    DefaultSlope: int  # = 2561
    MatchLaneSlope: int  # = 2562
    BreakoverRemoval: int  # = 2564
class SignType:
    """.NET enum: Autodesk.Civil.SignType"""
    def __init__(self, *args) -> None: ...
    Negative: int  # = 2593
    BracketNegative: int  # = 2594
    Always: int  # = 2595
class SlopeFormatType:
    """.NET enum: Autodesk.Civil.SlopeFormatType"""
    def __init__(self, *args) -> None: ...
    RiseRun: int  # = 2465
    RunRise: int  # = 2466
class SlopePatternLengthType:
    """.NET enum: Autodesk.Civil.SlopePatternLengthType"""
    def __init__(self, *args) -> None: ...
    PercentOfLength: int  # = 0
    Length: int  # = 1
    SlopeRatio: int  # = 2
    GradeRatio: int  # = 3
class SlopePatternOffsetType:
    """.NET enum: Autodesk.Civil.SlopePatternOffsetType"""
    def __init__(self, *args) -> None: ...
    PercentLength: int  # = 0
    FixedLength: int  # = 1
    Divide: int  # = 2
class SlopePatternStartType:
    """.NET enum: Autodesk.Civil.SlopePatternStartType"""
    def __init__(self, *args) -> None: ...
    Top: int  # = 0
    Bottom: int  # = 1
class SlopePatternSymbolType:
    """.NET enum: Autodesk.Civil.SlopePatternSymbolType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Block: int  # = 1
    Triangle: int  # = 2
    TriangleFilled: int  # = 3
    TaperedLines: int  # = 4
    TaperedLinesNoGap: int  # = 5
class SpeedUnitType:
    """.NET enum: Autodesk.Civil.SpeedUnitType"""
    def __init__(self, *args) -> None: ...
    MeterPerSec: int  # = 185
    KilometerPerHour: int  # = 190
    FootPerSec: int  # = 191
    MilePerHour: int  # = 196
class SpiralType:
    """.NET enum: Autodesk.Civil.SpiralType"""
    def __init__(self, *args) -> None: ...
    Clothoid: int  # = 256
    SineHalfWave: int  # = 257
    JapaneseCubic: int  # = 258
    Bloss: int  # = 259
    CubicParabola: int  # = 260
    Sinusoidal: int  # = 261
    BiQuadratic: int  # = 262
    NSWCubic: int  # = 264
    OffsetClothoid: int  # = 1048832
    OffsetHalfWaveLenDimnTangent: int  # = 1048833
    OffsetJapaneseCubic: int  # = 1048834
    OffsetBloss: int  # = 1048835
    OffsetCubicParabola: int  # = 1048836
    OffsetSinusoidal: int  # = 1048837
    OffsetBiQuadratic: int  # = 1048838
    OffsetHalfWaveLenDimnTangent2: int  # = 1048839
    OffsetInvalidSpiralType: int  # = 268435455
class StationDelimiterCharacterType:
    """.NET enum: Autodesk.Civil.StationDelimiterCharacterType"""
    def __init__(self, *args) -> None: ...
    PlusSign: int  # = 2689
    MinusSign: int  # = 2690
    Automatic: int  # = 2691
    Underscore: int  # = 2692
    None_: int  # = 2694
class StationDelimiterPositionType:
    """.NET enum: Autodesk.Civil.StationDelimiterPositionType"""
    def __init__(self, *args) -> None: ...
    Delimiter10: int  # = 2673
    Delimiter100: int  # = 2674
    Delimiter1000: int  # = 2675
    Delimiter10000: int  # = 2676
    Delimiter100000: int  # = 2677
class StationFormatType:
    """.NET enum: Autodesk.Civil.StationFormatType"""
    def __init__(self, *args) -> None: ...
    StationFormatDecimal: int  # = 2468
    StationFormat: int  # = 2474
    StationIndexFormat: int  # = 2475
class StructureColumnComponentType:
    """.NET enum: Autodesk.Civil.StructureColumnComponentType"""
    def __init__(self, *args) -> None: ...
    Default: int  # = 0
    PipeAll: int  # = 1
    PipeIn: int  # = 2
    PipeOut: int  # = 3
    PressurePipeAll: int  # = 4
class StructureProfileLabelPlacementType:
    """.NET enum: Autodesk.Civil.StructureProfileLabelPlacementType"""
    def __init__(self, *args) -> None: ...
    AtStructureTop: int  # = 0
    AtStructureMiddle: int  # = 1
    AtStructureBottom: int  # = 2
class StyleConflictResolverType:
    """.NET enum: Autodesk.Civil.StyleConflictResolverType"""
    def __init__(self, *args) -> None: ...
    Ignore: int  # = 0
    Rename: int  # = 1
    Override: int  # = 2
    CancelRemaining: int  # = 3
class SubassemblyNameType:
    """.NET enum: Autodesk.Civil.SubassemblyNameType"""
    def __init__(self, *args) -> None: ...
    MacroName: int  # = 0
    NameTemplate: int  # = 1
class SuperElevationViewDisplayStyleType:
    """.NET enum: Autodesk.Civil.SuperElevationViewDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    GraphTitle: int  # = 0
    LeftAxis: int  # = 1
    LeftAxisAnnotation: int  # = 3
    LeftAxisTicksMajor: int  # = 5
    RightAxis: int  # = 7
    RightAxisAnnotation: int  # = 9
    RightAxisTicksMajor: int  # = 11
    TopAxis: int  # = 13
    TopAxisAnnotation: int  # = 15
    TopAxisTicks: int  # = 17
    BottomAxis: int  # = 19
    BottomAxisAnnotation: int  # = 21
    BottomAxisTicks: int  # = 23
    TopAxisTransitionRegion: int  # = 55
    BottomAxisTransitionRegion: int  # = 56
    TopAxisCurveDetails: int  # = 57
    BottomAxisCurveDetails: int  # = 58
    CriticalStationTicks: int  # = 59
    CriticalStationText: int  # = 60
    TopAxisCriticalStationAnnotation: int  # = 61
    BottomAxisCriticalStationAnnotation: int  # = 62
    SuperelevationCrossSlopeAnnotation: int  # = 63
    GraphReferenceLineTitle: int  # = 64
class SuperelevationAttainmentRegionType:
    """.NET enum: Autodesk.Civil.SuperelevationAttainmentRegionType"""
    def __init__(self, *args) -> None: ...
    AutoAttainmentRegionType: int  # = 0
    BeginingAttainmentRegion: int  # = 1
    EndingAttainmentRegion: int  # = 2
class SuperelevationCorridorType:
    """.NET enum: Autodesk.Civil.SuperelevationCorridorType"""
    def __init__(self, *args) -> None: ...
    Undivided: int  # = 1537
    Divided: int  # = 1538
class SuperelevationCriticalStationType:
    """.NET enum: Autodesk.Civil.SuperelevationCriticalStationType"""
    def __init__(self, *args) -> None: ...
    BeginAlignment: int  # = 513
    BeginNormalCrown: int  # = 514
    BeginNormalShoulder: int  # = 515
    BeginFullSuper: int  # = 516
    EndFullSuper: int  # = 517
    EndNormalShoulder: int  # = 518
    EndNormalCrown: int  # = 519
    EndAlignment: int  # = 520
    LevelCrown: int  # = 521
    LowShoulderMatch: int  # = 522
    ReverseCrown: int  # = 523
    Manual: int  # = 524
    ShoulderBreakOver: int  # = 525
    BeginShoulderRollover: int  # = 526
    EndShoulderRollover: int  # = 527
    EndLevelRail: int  # = 768
    BeginLevelRail: int  # = 769
    BeginFullCant: int  # = 770
    EndFullCant: int  # = 771
class SuperelevationCrossSegmentType:
    """.NET enum: Autodesk.Civil.SuperelevationCrossSegmentType"""
    def __init__(self, *args) -> None: ...
    LeftOutShoulderCrossSlope: int  # = 0
    LeftOutLaneCrossSlope: int  # = 1
    LeftInShoulderCrossSlope: int  # = 2
    LeftInLaneCrossSlope: int  # = 3
    RightOutShoulderCrossSlope: int  # = 256
    RightOutLaneCrossSlope: int  # = 257
    RightInShoulderCrossSlope: int  # = 258
    RightInLaneCrossSlope: int  # = 259
class SuperelevationPointType:
    """.NET enum: Autodesk.Civil.SuperelevationPointType"""
    def __init__(self, *args) -> None: ...
    BeginOfAlignment: int  # = 513
    BeginNormalCrown: int  # = 514
    BeginNormalShoulder: int  # = 515
    BeginFullSuper: int  # = 516
    EndFullSuper: int  # = 517
    EndNormalShoulder: int  # = 518
    EndNormalCrown: int  # = 519
    EndOfAlignment: int  # = 520
    LevelCrown: int  # = 521
    LowShoulderMatch: int  # = 522
    ReverseCrown: int  # = 523
    Manual: int  # = 524
    ShoulderBreakOver: int  # = 525
    BeginShoulderRollover: int  # = 526
    EndShoulderRollover: int  # = 527
class SuperelevationStationRoundingType:
    """.NET enum: Autodesk.Civil.SuperelevationStationRoundingType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 2833
    PointOne: int  # = 2834
    One: int  # = 2835
    Five: int  # = 2836
    Ten: int  # = 2837
class SuperelevationTransitionRegionType:
    """.NET enum: Autodesk.Civil.SuperelevationTransitionRegionType"""
    def __init__(self, *args) -> None: ...
    In: int  # = 0
    Out: int  # = 1
class SurfaceBoundaryType:
    """.NET enum: Autodesk.Civil.SurfaceBoundaryType"""
    def __init__(self, *args) -> None: ...
    Show: int  # = 1
    Hide: int  # = 2
    Outer: int  # = 4
    DataClip: int  # = 8
class SurfaceBreaklineType:
    """.NET enum: Autodesk.Civil.SurfaceBreaklineType"""
    def __init__(self, *args) -> None: ...
    Standard: int  # = 14
    Wall: int  # = 16
    NonDestructive: int  # = 24
class SurfaceDrawObjectType:
    """.NET enum: Autodesk.Civil.SurfaceDrawObjectType"""
    def __init__(self, *args) -> None: ...
    Point: int  # = 0
    Line: int  # = 1
    Block: int  # = 2
    Text: int  # = 3
    Face: int  # = 4
    PolyFace: int  # = 5
class SurfaceException(CivilException):
    """.NET: Autodesk.Civil.SurfaceException"""
    def __init__(self, *args) -> None: ...
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str

class SurfaceExtractionSettingsType:
    """.NET enum: Autodesk.Civil.SurfaceExtractionSettingsType"""
    def __init__(self, *args) -> None: ...
    Plan: int  # = 0
    Model: int  # = 1
class SurfaceOpeartionStatusType:
    """.NET enum: Autodesk.Civil.SurfaceOpeartionStatusType"""
    def __init__(self, *args) -> None: ...
    AllFalse: int  # = 0
    AllTrue: int  # = 1
    Varies: int  # = 2
    None_: int  # = -1
class SurfacePointOutputLocationsType:
    """.NET enum: Autodesk.Civil.SurfacePointOutputLocationsType"""
    def __init__(self, *args) -> None: ...
    GridBased: int  # = 1048576
    Centroids: int  # = 2097152
    RandomPoints: int  # = 4194304
    EdgeMidPoints: int  # = 8388608
class SurfacePointSelectionType:
    """.NET enum: Autodesk.Civil.SurfacePointSelectionType"""
    def __init__(self, *args) -> None: ...
    SelectPoints: int  # = 8
    RandomPoints: int  # = 16
    AllPoints: int  # = 64
class SurfaceRegionOptionsType:
    """.NET enum: Autodesk.Civil.SurfaceRegionOptionsType"""
    def __init__(self, *args) -> None: ...
    SurfBorder: int  # = 0
    SpecifyWindow: int  # = 1
    SelectObjects: int  # = 2
class SurfaceSimplifyType:
    """.NET enum: Autodesk.Civil.SurfaceSimplifyType"""
    def __init__(self, *args) -> None: ...
    PointRemoval: int  # = 0
    EdgeContraction: int  # = 1
class SurfaceSmoothType:
    """.NET enum: Autodesk.Civil.SurfaceSmoothType"""
    def __init__(self, *args) -> None: ...
    Kriging: int  # = 2
    NaturalNeighborInterpolation: int  # = 4
class SurfaceStatus:
    """.NET enum: Autodesk.Civil.SurfaceStatus"""
    def __init__(self, *args) -> None: ...
    Success: int  # = 0
    NoSurfaceFound: int  # = 1
    ProcessingInterrupted: int  # = 2
    NoPointsInSurface: int  # = 3
    NoTrianglesInSurface: int  # = 4
    NoTriangleFound: int  # = 5
    PointOutsideSurface: int  # = 6
    TriangleIsDeleted: int  # = 7
    NoBorderFound: int  # = 8
    NoRangePointsFound: int  # = 9
    TrianglesAreNotNeighbors: int  # = 10
    NoIntersectionFound: int  # = 11
    DuplicatePoint: int  # = 12
    NoPointFound: int  # = 13
    Failure: int  # = 14
    UnimplementedOperation: int  # = 15
    UnableToReadFile: int  # = 16
    NoEdgeFound: int  # = 17
    EdgeIsLocked: int  # = 18
    CantSwap: int  # = 19
    LoadFailed: int  # = 20
    DuplicateName: int  # = 21
    IllegalBoundary: int  # = 22
    InvalidFileFormat: int  # = 23
    FileNotFound: int  # = 24
    SnapshotNotFound: int  # = 25
    GradingPasteToTargetSurfRejected: int  # = 26
    IncompatibleGrids: int  # = 27
    UnableToOpenSurfaceStyle: int  # = 28
    PointOnFlatArea: int  # = 29
    NeighborsNotFullySpecified: int  # = 30
    InconsistentNeighborPointers: int  # = 31
    PointsNotInCcwOrder: int  # = 32
    OutOfMemory: int  # = 33
    BaseSurfaceNotFound: int  # = 34
    ComparisonSurfaceNotFound: int  # = 35
class SurfaceStatusText:
    """.NET: Autodesk.Civil.SurfaceStatusText"""
    def __init__(self, *args) -> None: ...
    Text: str

class SurfaceSurveyQueryType:
    """.NET enum: Autodesk.Civil.SurfaceSurveyQueryType"""
    def __init__(self, *args) -> None: ...
    AddPoint: int  # = 48
    AddFigure: int  # = 49
class SurfaceType:
    """.NET enum: Autodesk.Civil.SurfaceType"""
    def __init__(self, *args) -> None: ...
    TinSurface: int  # = 0
    GridSurface: int  # = 1
    GridVolumeSurface: int  # = 2
    TinVolumeSurface: int  # = 3
class SurveyException(CivilException):
    """.NET: Autodesk.Civil.SurveyException"""
    def __init__(self, *args) -> None: ...
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str

class SurveyProject(DisposableWrapper):
    """.NET: Autodesk.Civil.SurveyProject"""
    def __init__(self, *args) -> None: ...
    ProjectGUID: Guid
    ProjectName: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Close(self, ) -> None: ...
    def GetSurveyQueryCollection(self, ) -> SurveyQueryCollection: ...
    def IsOpen(self, ) -> bool: ...
    def Open(self, openMode: bool) -> None: ...

class SurveyProjectCollection(DisposableWrapper):
    """.NET: Autodesk.Civil.SurveyProjectCollection"""
    def __init__(self, *args) -> None: ...
    Item: SurveyProject
    Count: int
    WorkingFolder: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetCurrentProject(self, ) -> SurveyProject: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetItem(self, surveyProjectPath: str) -> SurveyProject: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class SurveyQuery(DisposableWrapper):
    """.NET: Autodesk.Civil.SurveyQuery"""
    def __init__(self, *args) -> None: ...
    Description: str
    GUID: Guid
    Name: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SurveyQueryCollection(DisposableWrapper):
    """.NET: Autodesk.Civil.SurveyQueryCollection"""
    def __init__(self, *args) -> None: ...
    Item: SurveyQuery
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetItem(self, queryName: str) -> ArrayList: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class SurveyStatus:
    """.NET enum: Autodesk.Civil.SurveyStatus"""
    def __init__(self, *args) -> None: ...
    StatusOk: int  # = 0
    FdbStatusCorruption: int  # = 5
    FdbStatusNoName: int  # = 6
    FdbStatusDuplicateName: int  # = 7
    FdbStatusDatabaseDoesNotExist: int  # = 8
    FdbStatusNotFound: int  # = 9
    FdbStatusDuplicateDbName: int  # = 10
    FdbStatusDbNoName: int  # = 11
    FdbStatusDatabaseDirectoryNotWritable: int  # = 12
    FdbStatusDatabaseNotReadable: int  # = 13
    FdbStatusDatabaseNotWritable: int  # = 14
    EdbStatusCorruption: int  # = 15
    EdbStatusNoName: int  # = 16
    EdbStatusDuplicateName: int  # = 17
    EdbStatusDatabaseDoesNotExist: int  # = 18
    EdbStatusNotFound: int  # = 19
    EdbStatusDuplicateDbName: int  # = 20
    EdbStatusDbNoName: int  # = 21
    EdbStatusDatabaseDirectoryNotWritable: int  # = 22
    EdbStatusDatabaseNotReadable: int  # = 23
    EdbStatusDatabaseNotWritable: int  # = 24
    SdbStatusCorruption: int  # = 25
    SdbStatusDatabaseDoesNotExist: int  # = 26
    SdbStatusDatabaseDirectoryNotWritable: int  # = 27
    SdbStatusDatabaseNotReadable: int  # = 28
    SdbStatusDatabaseNotWritable: int  # = 29
    SdbStatusDatabaseNotOpen: int  # = 30
    SdbStatusDatabaseVersionNewerThanSupported: int  # = 31
    SdbStatusDatabaseVersionCanNotBeUpgraded: int  # = 32
    SdbStatusDatabaseNeedMigration: int  # = 33
    SdbStatusDatabaseAccessPermissionDenied: int  # = 34
    SdbStatusDatabaseCreateCacheCopyFailed: int  # = 35
    SdbStatusDatabaseDuplicateProjectGUID: int  # = 36
    SdbStatusDatabaseProjectInfoMissingOrFailedToCreate: int  # = 37
    FigStatusNoName: int  # = 38
    FigStatusNotFound: int  # = 39
    FigStatusNodeNotFound: int  # = 40
    FigStatusRecalcNotPermitted: int  # = 41
    FigStatusRecalcFailed: int  # = 42
    NetStatusNoName: int  # = 43
    NetStatusDuplicateName: int  # = 44
    NetStatusNotFound: int  # = 45
    NetStatusNoFileSpecified: int  # = 46
    ObsStatusNotFound: int  # = 47
    StpStatusNotFound: int  # = 48
    TrvStatusNoName: int  # = 49
    TrvStatusNotFound: int  # = 50
    TrvStatusNodeNotFound: int  # = 51
    TrvStatusDuplicateName: int  # = 52
    PrjStatusInsertError: int  # = 53
    PrjStatusWrongSvProject: int  # = 54
    PrjStatusWrongVaultProject: int  # = 55
    SdxStatusDatabaseNotOpen: int  # = 56
    SdxStatusDatabaseNotReadable: int  # = 57
    SdxStatusDatabaseNotWritable: int  # = 58
    SdxStatusDefFileNotAvailable: int  # = 59
    SdxStatusDatabaseNotAvailable: int  # = 60
    SdxStatusActiveDrawingRequiredToOpen: int  # = 61
    SdxStatusSchemaNotOpen: int  # = 62
    SdxStatusSchemaNotOpenForWrite: int  # = 63
    SdxStatusSchemaAttributeNotDefined: int  # = 64
    SdxStatusSchemaAttributeInUse: int  # = 65
    SdxStatusSchemaInvalidAttributeDefinitionParameter: int  # = 66
    SdxStatusSchemaDuplicateClassAttributeName: int  # = 67
    SdxStatusSchemaAttributeDefinitionNotFound: int  # = 68
    SdxStatusSchemaInternalError: int  # = 69
    SdxStatusDataObjectNotOpen: int  # = 71
    SdxStatusDataObjectNotOpenForWrite: int  # = 72
    SdxStatusDataWrongAttrClass: int  # = 73
    SdxStatusDataCollectionNotFound: int  # = 74
    SdxStatusDataRecordNotFound: int  # = 75
    SdxStatusDataCreateCollectionFailed: int  # = 76
    SdxStatusDataObjectNotFound: int  # = 77
    SdxStatusDataMultipleRecordsNotSupported: int  # = 78
    SetStatusFileNotAvailable: int  # = 79
    SetStatusFileNotReadable: int  # = 80
    SetStatusFileNotWritable: int  # = 81
    SetStatusFileNotCorrectType: int  # = 82
    GrpStatusNotFound: int  # = 83
    GrpStatusDuplicateName: int  # = 84
    GrpStatusNoName: int  # = 85
    TranslateDbInvalidInput: int  # = 86
    ImpEventStatusNoName: int  # = 87
    ImpEventStatusDuplicateName: int  # = 88
    ImpEventStatusNotFound: int  # = 89
    ImpEventStatusImportDuplicateFileFound: int  # = 90
    ImpEventStatusImportFileNotFound: int  # = 91
    ImpEventStatusPointFormatNotFound: int  # = 92
    ImpEventStatusF2FCodingConventionNotFound: int  # = 93
    PointStatusConflictPointIgnored: int  # = 94
    PointStatusConflictAbortProcess: int  # = 95
    LogStatusLogFileNotFound: int  # = 96
    LogStatusXslFileNotFound: int  # = 97
    LogStatusXmlCouldNotBeGenerated: int  # = 98
    LogStatusHtmlFileNotGenerated: int  # = 99
    LogStatusOldHtmlFileNotDeleted: int  # = 100
    MetaQueryStatusNoName: int  # = 101
    MetaQueryStatusDuplicateName: int  # = 102
    MetaQueryStatusNotFound: int  # = 103
    MetaQueryStatusQueryDataFileMissing: int  # = 104
class SurveyStatusText:
    """.NET: Autodesk.Civil.SurveyStatusText"""
    def __init__(self, *args) -> None: ...
    Text: str

class SweptCurveLocation:
    """.NET enum: Autodesk.Civil.SweptCurveLocation"""
    def __init__(self, *args) -> None: ...
    OnEntireAlignment: int  # = 4
    OnNoWideningCurves: int  # = 8
class TableSegmentDataType:
    """.NET enum: Autodesk.Civil.TableSegmentDataType"""
    def __init__(self, *args) -> None: ...
    Line: int  # = 3
    Curve: int  # = 4
    Spiral: int  # = 5
class TableTitleDirectionType:
    """.NET enum: Autodesk.Civil.TableTitleDirectionType"""
    def __init__(self, *args) -> None: ...
    Across: int  # = 0
    Down: int  # = 1
class TaperInputType:
    """.NET enum: Autodesk.Civil.TaperInputType"""
    def __init__(self, *args) -> None: ...
    ByLength: int  # = 0
    ByTaperRatio: int  # = 1
class TextBorderType:
    """.NET enum: Autodesk.Civil.TextBorderType"""
    def __init__(self, *args) -> None: ...
    Rectangular: int  # = 0
    RoundedRectangular: int  # = 1
    Circular: int  # = 2
class TextJustificationType:
    """.NET enum: Autodesk.Civil.TextJustificationType"""
    def __init__(self, *args) -> None: ...
    Left: int  # = 4
    Center: int  # = 5
    Right: int  # = 6
class TimeUnitType:
    """.NET enum: Autodesk.Civil.TimeUnitType"""
    def __init__(self, *args) -> None: ...
    Second: int  # = 300
    Minute: int  # = 301
    Hour: int  # = 302
    Day: int  # = 303
    Year: int  # = 304
class TransitionInputType:
    """.NET enum: Autodesk.Civil.TransitionInputType"""
    def __init__(self, *args) -> None: ...
    ByLength: int  # = 0
    ByTaperRatio: int  # = 1
class TransitionType:
    """.NET enum: Autodesk.Civil.TransitionType"""
    def __init__(self, *args) -> None: ...
    Linear: int  # = 1
    CurveLineCurve: int  # = 2
    CurveCurveReverseCurve: int  # = 4
    CurveReverseCurve: int  # = 5
class TreeOidWrapper(DisposableWrapper):
    """.NET: Autodesk.Civil.TreeOidWrapper"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class Utility:
    """.NET: Autodesk.Civil.Utility"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def PolarPoint(refPoint: list, angle: float, distance: float) -> list: ...

class VectorMeasurementType:
    """.NET enum: Autodesk.Civil.VectorMeasurementType"""
    def __init__(self, *args) -> None: ...
    Bearings: int  # = 2785
    NorthAzimuth: int  # = 2786
    SouthAzimuth: int  # = 2787
class ViewFrameAngleType:
    """.NET enum: Autodesk.Civil.ViewFrameAngleType"""
    def __init__(self, *args) -> None: ...
    AlongAlignment: int  # = 0
    RotateToNorth: int  # = 1
class ViewFrameLabelLocationType:
    """.NET enum: Autodesk.Civil.ViewFrameLabelLocationType"""
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
class VolumeSurfaceType:
    """.NET enum: Autodesk.Civil.VolumeSurfaceType"""
    def __init__(self, *args) -> None: ...
    Grid: int  # = 2
    Tin: int  # = 3
class VolumeUnitType:
    """.NET enum: Autodesk.Civil.VolumeUnitType"""
    def __init__(self, *args) -> None: ...
    CubicMeter: int  # = 96
    CubicFoot: int  # = 130
    CubicYard: int  # = 153
class WaterdropObjectType:
    """.NET enum: Autodesk.Civil.WaterdropObjectType"""
    def __init__(self, *args) -> None: ...
    Polyline2D: int  # = 0
    Polyline3D: int  # = 1
class WatershedType:
    """.NET enum: Autodesk.Civil.WatershedType"""
    def __init__(self, *args) -> None: ...
    BoundaryPoint: int  # = 0
    BoundarySegment: int  # = 1
    Depression: int  # = 3
    FlatArea: int  # = 4
    MultiDrain: int  # = 5
    MultiDrainNotch: int  # = 7
class WideningByMethod:
    """.NET enum: Autodesk.Civil.WideningByMethod"""
    def __init__(self, *args) -> None: ...
    ThroughDesignStandards: int  # = 1
    Manual: int  # = 2
class WideningSide:
    """.NET enum: Autodesk.Civil.WideningSide"""
    def __init__(self, *args) -> None: ...
    Inside: int  # = 1
    Outside: int  # = 2
    Both: int  # = 3
