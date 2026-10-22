# Auto-generated — Civil 26 — Autodesk.Civil.Settings

class AbbreviationAlignmentEnhancedType:
    """.NET enum: Autodesk.Civil.Settings.AbbreviationAlignmentEnhancedType"""
    def __init__(self, *args) -> None: ...
    AlignmentBeginningPoint: int  # = 402706556
    AlignmentEndPoint: int  # = 402706557
    LineBeginning: int  # = 402706558
    LineEnd: int  # = 402706559
    CurveBeginning: int  # = 402706560
    CurveEnd: int  # = 402706561
    SimpleSpiralLargeRadiusAtBeginning: int  # = 402706562
    SimpleSpiralLargeRadiusAtEnd: int  # = 402706563
    SimpleSpiralSmallRadiusAtBeginning: int  # = 402706564
    SimpleSpiralSmallRadiusAtEnd: int  # = 402706565
    CompoundSpiralLargeRadiusAtBeginning: int  # = 402706566
    CompoundSpiralLargeRadiusAtEnd: int  # = 402706567
    CompoundSpiralSmallRadiusAtBeginning: int  # = 402706568
    CompoundSpiralSmallRadiusAtEnd: int  # = 402706569
class AbbreviationAlignmentType:
    """.NET enum: Autodesk.Civil.Settings.AbbreviationAlignmentType"""
    def __init__(self, *args) -> None: ...
    TangentTangentIntersect: int  # = 67162194
    TangentCurveIntersect: int  # = 67162195
    CurveTangentIntersect: int  # = 67162196
    CompoundCurveCurveIntersect: int  # = 67162197
    ReverseCurveCurveIntersect: int  # = 67162198
    TangentSpiralIntersect: int  # = 67162199
    SpiralTangentIntersect: int  # = 67162200
    CurveSpiralIntersect: int  # = 67162201
    SpiralCurveIntersect: int  # = 67162202
    SpiralSpiralIntersect: int  # = 67162203
    ReverseSpiralIntersect: int  # = 67162204
    AlignmentEnd: int  # = 67162234
    AlignmentBeginning: int  # = 67162235
    StationEquationIncreasing: int  # = 67162252
    StationEquationDecreasing: int  # = 67162253
    MidCurvePoint: int  # = 67162254
class AbbreviationCantType:
    """.NET enum: Autodesk.Civil.Settings.AbbreviationCantType"""
    def __init__(self, *args) -> None: ...
    EndLevelRail: int  # = 67163508
    BeginLevelRail: int  # = 67163509
    BeginFullCant: int  # = 67163510
    EndFullCant: int  # = 67163511
    Manual: int  # = 67163512
    BeginAlignment: int  # = 67163513
    EndAlignment: int  # = 67163514
class AbbreviationProfileType:
    """.NET enum: Autodesk.Civil.Settings.AbbreviationProfileType"""
    def __init__(self, *args) -> None: ...
    PointOfVerticalIntersection: int  # = 67173888
    GradeBreak: int  # = 67173889
    BeginVerticalCurve: int  # = 67173890
    BeginVerticalCurveStation: int  # = 67173891
    BeginVerticalCurveElevation: int  # = 67173892
    EndVerticalCurve: int  # = 67173893
    EndVerticalCurveStation: int  # = 67173894
    EndVerticalCurveElevation: int  # = 67173895
    HighPoint: int  # = 67173896
    LowPoint: int  # = 67173897
    CurveCoefficient: int  # = 67173898
    GradeChange: int  # = 67173899
    ProfileStart: int  # = 67173901
    ProfileEnd: int  # = 67173902
    VerticalCompoundCurveIntersect: int  # = 67173903
    VerticalReverseCurveIntersect: int  # = 67173904
    VerticalCompoundCurveIntersectStation: int  # = 67173905
    VerticalCompoundCurveIntersectElevation: int  # = 67173906
    VerticalReverseCurveIntersectStation: int  # = 67173907
    VerticalReverseCurveIntersectElevation: int  # = 67173908
    OverallHighPoint: int  # = 67173909
    OverallLowPoint: int  # = 67173910
class AbbreviationSuperelevationType:
    """.NET enum: Autodesk.Civil.Settings.AbbreviationSuperelevationType"""
    def __init__(self, *args) -> None: ...
    BeginOfAlignment: int  # = 67163474
    EndOfAlignment: int  # = 67163475
    BeginNormalCrown: int  # = 67163476
    EndNormalCrown: int  # = 67163477
    BeginFullSuper: int  # = 67163478
    EndFullSuper: int  # = 67163479
    BeginNormalShoulder: int  # = 67163480
    EndNormalShoulder: int  # = 67163481
    LevelCrown: int  # = 67163482
    LowShoulderMatch: int  # = 67163483
    ReverseCrown: int  # = 67163484
    ShoulderBreakover: int  # = 67163485
    Manual: int  # = 67163486
    BeginShoulderRollover: int  # = 67163506
    EndShoulderRollover: int  # = 67163507
class AutomaticManual:
    """.NET enum: Autodesk.Civil.Settings.AutomaticManual"""
    def __init__(self, *args) -> None: ...
    Automatic: int  # = 0
    AutomaticObject: int  # = 1
    Manual: int  # = 2
    None_: int  # = 3
class DrawingUnitType:
    """.NET enum: Autodesk.Civil.Settings.DrawingUnitType"""
    def __init__(self, *args) -> None: ...
    Meters: int  # = 2
    Feet: int  # = 30
class GeographicCoordinateType:
    """.NET enum: Autodesk.Civil.Settings.GeographicCoordinateType"""
    def __init__(self, *args) -> None: ...
    LatLong: int  # = 0
    LongLat: int  # = 1
class GridCoordinateType:
    """.NET enum: Autodesk.Civil.Settings.GridCoordinateType"""
    def __init__(self, *args) -> None: ...
    EastingNorthing: int  # = 0
    NorthingEasting: int  # = 1
class GridScaleFactorType:
    """.NET enum: Autodesk.Civil.Settings.GridScaleFactorType"""
    def __init__(self, *args) -> None: ...
    Unity: int  # = 0
    UserDefined: int  # = 1
    ReferencePoint: int  # = 2
    PrismodialFormula: int  # = 3
class ImperialToMetricConversionType:
    """.NET enum: Autodesk.Civil.Settings.ImperialToMetricConversionType"""
    def __init__(self, *args) -> None: ...
    InternationalFoot: int  # = 536870912
    UsSurveyFoot: int  # = 1073741824
class LandXMLAngularUnits:
    """.NET enum: Autodesk.Civil.Settings.LandXMLAngularUnits"""
    def __init__(self, *args) -> None: ...
    DegreesDecimal: int  # = 0
    DegreesDms: int  # = 1
    Grads: int  # = 2
    Radians: int  # = 3
class LandXMLAttributeExportType:
    """.NET enum: Autodesk.Civil.Settings.LandXMLAttributeExportType"""
    def __init__(self, *args) -> None: ...
    Disabled: int  # = 0
    RawDescription: int  # = 1
    FullDescription: int  # = 2
class LandXMLConflictResolutionType:
    """.NET enum: Autodesk.Civil.Settings.LandXMLConflictResolutionType"""
    def __init__(self, *args) -> None: ...
    Skip: int  # = 0
    Update: int  # = 1
    Append: int  # = 2
class LandXMLImperialUnitType:
    """.NET enum: Autodesk.Civil.Settings.LandXMLImperialUnitType"""
    def __init__(self, *args) -> None: ...
    Foot: int  # = 30
    Inch: int  # = 31
    Yard: int  # = 33
    Mile: int  # = 44
class LandXMLLinearUnits:
    """.NET enum: Autodesk.Civil.Settings.LandXMLLinearUnits"""
    def __init__(self, *args) -> None: ...
    InternationalFoot: int  # = 30
    SurveyFoot: int  # = 54
class LandXMLMetricUnitType:
    """.NET enum: Autodesk.Civil.Settings.LandXMLMetricUnitType"""
    def __init__(self, *args) -> None: ...
    Meter: int  # = 2
    KiloMeter: int  # = 20
    DeciMeter: int  # = 23
    CentiMeter: int  # = 24
    MilliMeter: int  # = 25
class LandXMLPointDescriptionType:
    """.NET enum: Autodesk.Civil.Settings.LandXMLPointDescriptionType"""
    def __init__(self, *args) -> None: ...
    UseCodeValue: int  # = 0
    UseDescValue: int  # = 1
    UseCodeThenDesc: int  # = 2
    UseDescThenCode: int  # = 3
class LandXMLSurfaceDataExportType:
    """.NET enum: Autodesk.Civil.Settings.LandXMLSurfaceDataExportType"""
    def __init__(self, *args) -> None: ...
    PointsOnly: int  # = 0
    PointsAndFaces: int  # = 1
class LandXMLSurfaceDataImportType:
    """.NET enum: Autodesk.Civil.Settings.LandXMLSurfaceDataImportType"""
    def __init__(self, *args) -> None: ...
    QuickImport: int  # = 0
    FullImport: int  # = 1
class LocalCoordinateType:
    """.NET enum: Autodesk.Civil.Settings.LocalCoordinateType"""
    def __init__(self, *args) -> None: ...
    EastingNorthing: int  # = 0
    NorthingEasting: int  # = 1
    XY: int  # = 2
    YX: int  # = 3
class MapcheckAngleType:
    """.NET enum: Autodesk.Civil.Settings.MapcheckAngleType"""
    def __init__(self, *args) -> None: ...
    Direction: int  # = 0
    Angle: int  # = 1
    DeflectionAngle: int  # = 2
class MapcheckCurveDirectionType:
    """.NET enum: Autodesk.Civil.Settings.MapcheckCurveDirectionType"""
    def __init__(self, *args) -> None: ...
    Clockwise: int  # = 0
    CounterClockwise: int  # = 1
class MapcheckSideType:
    """.NET enum: Autodesk.Civil.Settings.MapcheckSideType"""
    def __init__(self, *args) -> None: ...
    Line: int  # = 0
    Curve: int  # = 1
class MapcheckTraverseMethodType:
    """.NET enum: Autodesk.Civil.Settings.MapcheckTraverseMethodType"""
    def __init__(self, *args) -> None: ...
    AcrossChord: int  # = 0
    ThroughRadius: int  # = 1
class ObjectLayerModifierType:
    """.NET enum: Autodesk.Civil.Settings.ObjectLayerModifierType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Prefix: int  # = 1
    Suffix: int  # = 2
class SectionViewAnchorType:
    """.NET enum: Autodesk.Civil.Settings.SectionViewAnchorType"""
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
class SettingsAbbreviation(CivilWrapper<AcDbDatabase>):
    """.NET: Autodesk.Civil.Settings.SettingsAbbreviation"""
    def __init__(self, *args) -> None: ...
    Superelevation: SettingsAbbreviationSuperelevation
    Cant: SettingsAbbreviationCant
    Profile: SettingsAbbreviationProfile
    AlignmentGeoPointEntityData: SettingsAbbreviationAlignmentEnhanced
    AlignmentGeoPointText: SettingsAbbreviationAlignment
    GeneralText: SettingsAbbreviationGeneral

class SettingsAbbreviationAlignment(TreeOidWrapper):
    """.NET: Autodesk.Civil.Settings.SettingsAbbreviationAlignment"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetAlignmentAbbreviation(self, type: AbbreviationAlignmentType) -> str: ...
    def SetAlignmentAbbreviation(self, type: AbbreviationAlignmentType, value: str) -> None: ...

class SettingsAbbreviationAlignmentEnhanced(TreeOidWrapper):
    """.NET: Autodesk.Civil.Settings.SettingsAbbreviationAlignmentEnhanced"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetAlignmentEnhancedAbbreviation(self, type: AbbreviationAlignmentEnhancedType) -> str: ...
    def SetAlignmentEnhancedAbbreviation(self, type: AbbreviationAlignmentEnhancedType, newValue: str) -> None: ...

class SettingsAbbreviationCant(TreeOidWrapper):
    """.NET: Autodesk.Civil.Settings.SettingsAbbreviationCant"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetCantAbbreviation(self, type: AbbreviationCantType) -> str: ...
    def SetCantAbbreviation(self, type: AbbreviationCantType, newValue: str) -> None: ...

class SettingsAbbreviationGeneral(TreeOidWrapper):
    """.NET: Autodesk.Civil.Settings.SettingsAbbreviationGeneral"""
    def __init__(self, *args) -> None: ...
    Right: str
    Left: str
    Infinity: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsAbbreviationProfile(TreeOidWrapper):
    """.NET: Autodesk.Civil.Settings.SettingsAbbreviationProfile"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetProfileAbbreviation(self, type: AbbreviationProfileType) -> str: ...
    def SetProfileAbbreviation(self, type: AbbreviationProfileType, newValue: str) -> None: ...

class SettingsAbbreviationSuperelevation(TreeOidWrapper):
    """.NET: Autodesk.Civil.Settings.SettingsAbbreviationSuperelevation"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetSuperelevationAbbreviation(self, type: AbbreviationSuperelevationType) -> str: ...
    def SetSuperelevationAbbreviation(self, type: AbbreviationSuperelevationType, newValue: str) -> None: ...

class SettingsAlignment(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsAlignment"""
    def __init__(self, *args) -> None: ...
    AutomaticWideningAroundCurves: SettingsAutomaticWideningAroundCurves
    ConstraintEditing: SettingsConstraintEditing
    ImpliedPointOfIntersection: SettingsImpliedPointOfIntersection
    DynamicAlignmentHighlight: SettingsDynamicAlignmentHighlight
    Data: SettingsData
    CriteriaBasedDesignOptions: SettingsCriteriaBasedDesignOptions
    RailOptions: SettingsRailAlignmentOptions
    CantOptions: SettingsCantOptions
    SuperelevationOptions: SettingsSuperelevationOptions
    StationIndexing: SettingsStationIndexing
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsAmbient(TreeOidWrapper):
    """.NET: Autodesk.Civil.Settings.SettingsAmbient"""
    def __init__(self, *args) -> None: ...
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsAssembly(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsAssembly"""
    def __init__(self, *args) -> None: ...
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsBuildingSite(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsBuildingSite"""
    def __init__(self, *args) -> None: ...
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCantView(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsCantView"""
    def __init__(self, *args) -> None: ...
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCatchment(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsCatchment"""
    def __init__(self, *args) -> None: ...
    Styles: SettingsStyles
    NameTemplate: PropertyString
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddAlignPointOfIntLbl(SettingsAlignment):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddAlignPointOfIntLbl"""
    def __init__(self, *args) -> None: ...
    AutomaticWideningAroundCurves: SettingsAutomaticWideningAroundCurves
    ConstraintEditing: SettingsConstraintEditing
    ImpliedPointOfIntersection: SettingsImpliedPointOfIntersection
    DynamicAlignmentHighlight: SettingsDynamicAlignmentHighlight
    Data: SettingsData
    CriteriaBasedDesignOptions: SettingsCriteriaBasedDesignOptions
    RailOptions: SettingsRailAlignmentOptions
    CantOptions: SettingsCantOptions
    SuperelevationOptions: SettingsSuperelevationOptions
    StationIndexing: SettingsStationIndexing
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddAlignPointOfIntLbls(SettingsAlignment):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddAlignPointOfIntLbls"""
    def __init__(self, *args) -> None: ...
    AutomaticWideningAroundCurves: SettingsAutomaticWideningAroundCurves
    ConstraintEditing: SettingsConstraintEditing
    ImpliedPointOfIntersection: SettingsImpliedPointOfIntersection
    DynamicAlignmentHighlight: SettingsDynamicAlignmentHighlight
    Data: SettingsData
    CriteriaBasedDesignOptions: SettingsCriteriaBasedDesignOptions
    RailOptions: SettingsRailAlignmentOptions
    CantOptions: SettingsCantOptions
    SuperelevationOptions: SettingsSuperelevationOptions
    StationIndexing: SettingsStationIndexing
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddAlignSegLbl(SettingsAlignment):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddAlignSegLbl"""
    def __init__(self, *args) -> None: ...
    AutomaticWideningAroundCurves: SettingsAutomaticWideningAroundCurves
    ConstraintEditing: SettingsConstraintEditing
    ImpliedPointOfIntersection: SettingsImpliedPointOfIntersection
    DynamicAlignmentHighlight: SettingsDynamicAlignmentHighlight
    Data: SettingsData
    CriteriaBasedDesignOptions: SettingsCriteriaBasedDesignOptions
    RailOptions: SettingsRailAlignmentOptions
    CantOptions: SettingsCantOptions
    SuperelevationOptions: SettingsSuperelevationOptions
    StationIndexing: SettingsStationIndexing
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddAlignSegLbls(SettingsAlignment):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddAlignSegLbls"""
    def __init__(self, *args) -> None: ...
    AutomaticWideningAroundCurves: SettingsAutomaticWideningAroundCurves
    ConstraintEditing: SettingsConstraintEditing
    ImpliedPointOfIntersection: SettingsImpliedPointOfIntersection
    DynamicAlignmentHighlight: SettingsDynamicAlignmentHighlight
    Data: SettingsData
    CriteriaBasedDesignOptions: SettingsCriteriaBasedDesignOptions
    RailOptions: SettingsRailAlignmentOptions
    CantOptions: SettingsCantOptions
    SuperelevationOptions: SettingsSuperelevationOptions
    StationIndexing: SettingsStationIndexing
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddAlignTagentLbl(SettingsAlignment):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddAlignTagentLbl"""
    def __init__(self, *args) -> None: ...
    AutomaticWideningAroundCurves: SettingsAutomaticWideningAroundCurves
    ConstraintEditing: SettingsConstraintEditing
    ImpliedPointOfIntersection: SettingsImpliedPointOfIntersection
    DynamicAlignmentHighlight: SettingsDynamicAlignmentHighlight
    Data: SettingsData
    CriteriaBasedDesignOptions: SettingsCriteriaBasedDesignOptions
    RailOptions: SettingsRailAlignmentOptions
    CantOptions: SettingsCantOptions
    SuperelevationOptions: SettingsSuperelevationOptions
    StationIndexing: SettingsStationIndexing
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddAlignTagentLbls(SettingsAlignment):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddAlignTagentLbls"""
    def __init__(self, *args) -> None: ...
    AutomaticWideningAroundCurves: SettingsAutomaticWideningAroundCurves
    ConstraintEditing: SettingsConstraintEditing
    ImpliedPointOfIntersection: SettingsImpliedPointOfIntersection
    DynamicAlignmentHighlight: SettingsDynamicAlignmentHighlight
    Data: SettingsData
    CriteriaBasedDesignOptions: SettingsCriteriaBasedDesignOptions
    RailOptions: SettingsRailAlignmentOptions
    CantOptions: SettingsCantOptions
    SuperelevationOptions: SettingsSuperelevationOptions
    StationIndexing: SettingsStationIndexing
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddAlignmentCurveTable(SettingsAlignment):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddAlignmentCurveTable"""
    def __init__(self, *args) -> None: ...
    TableCreation: SettingsCmdTableCreation
    AutomaticWideningAroundCurves: SettingsAutomaticWideningAroundCurves
    ConstraintEditing: SettingsConstraintEditing
    ImpliedPointOfIntersection: SettingsImpliedPointOfIntersection
    DynamicAlignmentHighlight: SettingsDynamicAlignmentHighlight
    Data: SettingsData
    CriteriaBasedDesignOptions: SettingsCriteriaBasedDesignOptions
    RailOptions: SettingsRailAlignmentOptions
    CantOptions: SettingsCantOptions
    SuperelevationOptions: SettingsSuperelevationOptions
    StationIndexing: SettingsStationIndexing
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddAlignmentLineTable(SettingsAlignment):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddAlignmentLineTable"""
    def __init__(self, *args) -> None: ...
    TableCreation: SettingsCmdTableCreation
    AutomaticWideningAroundCurves: SettingsAutomaticWideningAroundCurves
    ConstraintEditing: SettingsConstraintEditing
    ImpliedPointOfIntersection: SettingsImpliedPointOfIntersection
    DynamicAlignmentHighlight: SettingsDynamicAlignmentHighlight
    Data: SettingsData
    CriteriaBasedDesignOptions: SettingsCriteriaBasedDesignOptions
    RailOptions: SettingsRailAlignmentOptions
    CantOptions: SettingsCantOptions
    SuperelevationOptions: SettingsSuperelevationOptions
    StationIndexing: SettingsStationIndexing
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddAlignmentOffLbl(SettingsAlignment):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddAlignmentOffLbl"""
    def __init__(self, *args) -> None: ...
    AutomaticWideningAroundCurves: SettingsAutomaticWideningAroundCurves
    ConstraintEditing: SettingsConstraintEditing
    ImpliedPointOfIntersection: SettingsImpliedPointOfIntersection
    DynamicAlignmentHighlight: SettingsDynamicAlignmentHighlight
    Data: SettingsData
    CriteriaBasedDesignOptions: SettingsCriteriaBasedDesignOptions
    RailOptions: SettingsRailAlignmentOptions
    CantOptions: SettingsCantOptions
    SuperelevationOptions: SettingsSuperelevationOptions
    StationIndexing: SettingsStationIndexing
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddAlignmentOffXYLbl(SettingsAlignment):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddAlignmentOffXYLbl"""
    def __init__(self, *args) -> None: ...
    AutomaticWideningAroundCurves: SettingsAutomaticWideningAroundCurves
    ConstraintEditing: SettingsConstraintEditing
    ImpliedPointOfIntersection: SettingsImpliedPointOfIntersection
    DynamicAlignmentHighlight: SettingsDynamicAlignmentHighlight
    Data: SettingsData
    CriteriaBasedDesignOptions: SettingsCriteriaBasedDesignOptions
    RailOptions: SettingsRailAlignmentOptions
    CantOptions: SettingsCantOptions
    SuperelevationOptions: SettingsSuperelevationOptions
    StationIndexing: SettingsStationIndexing
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddAlignmentSegmentTable(SettingsAlignment):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddAlignmentSegmentTable"""
    def __init__(self, *args) -> None: ...
    TableCreation: SettingsCmdTableCreation
    AutomaticWideningAroundCurves: SettingsAutomaticWideningAroundCurves
    ConstraintEditing: SettingsConstraintEditing
    ImpliedPointOfIntersection: SettingsImpliedPointOfIntersection
    DynamicAlignmentHighlight: SettingsDynamicAlignmentHighlight
    Data: SettingsData
    CriteriaBasedDesignOptions: SettingsCriteriaBasedDesignOptions
    RailOptions: SettingsRailAlignmentOptions
    CantOptions: SettingsCantOptions
    SuperelevationOptions: SettingsSuperelevationOptions
    StationIndexing: SettingsStationIndexing
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddAlignmentSpiralTable(SettingsAlignment):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddAlignmentSpiralTable"""
    def __init__(self, *args) -> None: ...
    TableCreation: SettingsCmdTableCreation
    AutomaticWideningAroundCurves: SettingsAutomaticWideningAroundCurves
    ConstraintEditing: SettingsConstraintEditing
    ImpliedPointOfIntersection: SettingsImpliedPointOfIntersection
    DynamicAlignmentHighlight: SettingsDynamicAlignmentHighlight
    Data: SettingsData
    CriteriaBasedDesignOptions: SettingsCriteriaBasedDesignOptions
    RailOptions: SettingsRailAlignmentOptions
    CantOptions: SettingsCantOptions
    SuperelevationOptions: SettingsSuperelevationOptions
    StationIndexing: SettingsStationIndexing
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddContourLabeling(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddContourLabeling"""
    def __init__(self, *args) -> None: ...
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddContourLabelingGroup(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddContourLabelingGroup"""
    def __init__(self, *args) -> None: ...
    AddContourLabeling: SettingsCmdAddContourLabeling
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddContourLabelingSingle(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddContourLabelingSingle"""
    def __init__(self, *args) -> None: ...
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddIntersectionLabel(SettingsIntersection):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddIntersectionLabel"""
    def __init__(self, *args) -> None: ...
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddLineBetweenPoints(SettingsGeneral):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddLineBetweenPoints"""
    def __init__(self, *args) -> None: ...
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddMaterialVolumeTable(SettingsQuantityTakeoff):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddMaterialVolumeTable"""
    def __init__(self, *args) -> None: ...
    TableCreation: SettingsCmdTableCreation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddNetworkPartPlanLabel(SettingsPipeNetwork):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddNetworkPartPlanLabel"""
    def __init__(self, *args) -> None: ...
    SectionLabelPlacement: SettingsSectionLabelPlacement
    ProfileLabelPlacement: SettingsProfileLabelPlacement
    StormSewersMigration: SettingsStormSewersMigration
    Default: SettingsDefault
    Rules: SettingsRules
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddNetworkPartProfLabel(SettingsPipeNetwork):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddNetworkPartProfLabel"""
    def __init__(self, *args) -> None: ...
    SectionLabelPlacement: SettingsSectionLabelPlacement
    ProfileLabelPlacement: SettingsProfileLabelPlacement
    StormSewersMigration: SettingsStormSewersMigration
    Default: SettingsDefault
    Rules: SettingsRules
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddNetworkPartSectLabel(SettingsPipeNetwork):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddNetworkPartSectLabel"""
    def __init__(self, *args) -> None: ...
    SectionLabelPlacement: SettingsSectionLabelPlacement
    ProfileLabelPlacement: SettingsProfileLabelPlacement
    StormSewersMigration: SettingsStormSewersMigration
    Default: SettingsDefault
    Rules: SettingsRules
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddNetworkPartsToProf(SettingsPipeNetwork):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddNetworkPartsToProf"""
    def __init__(self, *args) -> None: ...
    SectionLabelPlacement: SettingsSectionLabelPlacement
    ProfileLabelPlacement: SettingsProfileLabelPlacement
    StormSewersMigration: SettingsStormSewersMigration
    Default: SettingsDefault
    Rules: SettingsRules
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddNetworkPipeTable(SettingsPipeNetwork):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddNetworkPipeTable"""
    def __init__(self, *args) -> None: ...
    TableCreation: SettingsCmdTableCreation
    SectionLabelPlacement: SettingsSectionLabelPlacement
    ProfileLabelPlacement: SettingsProfileLabelPlacement
    StormSewersMigration: SettingsStormSewersMigration
    Default: SettingsDefault
    Rules: SettingsRules
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddNetworkPlanLabels(SettingsPipeNetwork):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddNetworkPlanLabels"""
    def __init__(self, *args) -> None: ...
    SectionLabelPlacement: SettingsSectionLabelPlacement
    ProfileLabelPlacement: SettingsProfileLabelPlacement
    StormSewersMigration: SettingsStormSewersMigration
    Default: SettingsDefault
    Rules: SettingsRules
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddNetworkProfLabels(SettingsPipeNetwork):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddNetworkProfLabels"""
    def __init__(self, *args) -> None: ...
    SectionLabelPlacement: SettingsSectionLabelPlacement
    ProfileLabelPlacement: SettingsProfileLabelPlacement
    StormSewersMigration: SettingsStormSewersMigration
    Default: SettingsDefault
    Rules: SettingsRules
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddNetworkSectLabels(SettingsPipeNetwork):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddNetworkSectLabels"""
    def __init__(self, *args) -> None: ...
    SectionLabelPlacement: SettingsSectionLabelPlacement
    ProfileLabelPlacement: SettingsProfileLabelPlacement
    StormSewersMigration: SettingsStormSewersMigration
    Default: SettingsDefault
    Rules: SettingsRules
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddNetworkStructTable(SettingsPipeNetwork):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddNetworkStructTable"""
    def __init__(self, *args) -> None: ...
    TableCreation: SettingsCmdTableCreation
    SectionLabelPlacement: SettingsSectionLabelPlacement
    ProfileLabelPlacement: SettingsProfileLabelPlacement
    StormSewersMigration: SettingsStormSewersMigration
    Default: SettingsDefault
    Rules: SettingsRules
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddNoteLabel(SettingsGeneral):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddNoteLabel"""
    def __init__(self, *args) -> None: ...
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddParcelAreaLabel(SettingsParcel):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddParcelAreaLabel"""
    def __init__(self, *args) -> None: ...
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddParcelCurveTable(SettingsParcel):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddParcelCurveTable"""
    def __init__(self, *args) -> None: ...
    TableCreation: SettingsCmdTableCreation
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddParcelLineLabel(SettingsParcel):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddParcelLineLabel"""
    def __init__(self, *args) -> None: ...
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddParcelLineTable(SettingsParcel):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddParcelLineTable"""
    def __init__(self, *args) -> None: ...
    TableCreation: SettingsCmdTableCreation
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddParcelSegmentLabels(SettingsParcel):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddParcelSegmentLabels"""
    def __init__(self, *args) -> None: ...
    Options: SettingsCmdOptions
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddParcelSegmentTable(SettingsParcel):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddParcelSegmentTable"""
    def __init__(self, *args) -> None: ...
    TableCreation: SettingsCmdTableCreation
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddParcelTable(SettingsParcel):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddParcelTable"""
    def __init__(self, *args) -> None: ...
    TableCreation: SettingsCmdTableCreation
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddPointCloudPoints(SettingsPointCloud):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddPointCloudPoints"""
    def __init__(self, *args) -> None: ...
    DefaultFileFormat: PropertyEnum
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddPointTable(SettingsPoint):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddPointTable"""
    def __init__(self, *args) -> None: ...
    TableCreation: SettingsCmdTableCreation
    UpdatePoints: SettingsUpdatePoints
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddPointsToSurface(SettingsPointCloud):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddPointsToSurface"""
    def __init__(self, *args) -> None: ...
    MidOrdinateDistance: PropertyDouble
    RegionOption: PropertyEnum
    SurfaceOption: PropertyEnum
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddProfileViewDepthLbl(SettingsProfileView):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddProfileViewDepthLbl"""
    def __init__(self, *args) -> None: ...
    ProjectionLabelPlacement: SettingsProjectionLabelPlacement
    StackedOptions: SettingsStackedOptions
    SplitOptions: SettingsSplitOptions
    Creation: SettingsCreation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddProfileViewStaElevLbl(SettingsProfileView):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddProfileViewStaElevLbl"""
    def __init__(self, *args) -> None: ...
    ProjectionLabelPlacement: SettingsProjectionLabelPlacement
    StackedOptions: SettingsStackedOptions
    SplitOptions: SettingsSplitOptions
    Creation: SettingsCreation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddSectionViewGradeLbl(SettingsSectionView):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddSectionViewGradeLbl"""
    def __init__(self, *args) -> None: ...
    ProjectionLabelPlacement: SettingsProjectionLabelPlacement
    SectionViewCreation: SettingsSectionViewCreation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddSectionViewOffElevLbl(SettingsSectionView):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddSectionViewOffElevLbl"""
    def __init__(self, *args) -> None: ...
    ProjectionLabelPlacement: SettingsProjectionLabelPlacement
    SectionViewCreation: SettingsSectionViewCreation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddSegmentLabel(SettingsGeneral):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddSegmentLabel"""
    def __init__(self, *args) -> None: ...
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddSegmentLabels(SettingsGeneral):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddSegmentLabels"""
    def __init__(self, *args) -> None: ...
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddSpanningPipePlanLabel(SettingsPipeNetwork):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddSpanningPipePlanLabel"""
    def __init__(self, *args) -> None: ...
    SectionLabelPlacement: SettingsSectionLabelPlacement
    ProfileLabelPlacement: SettingsProfileLabelPlacement
    StormSewersMigration: SettingsStormSewersMigration
    Default: SettingsDefault
    Rules: SettingsRules
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddSpanningPipeProfLabel(SettingsPipeNetwork):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddSpanningPipeProfLabel"""
    def __init__(self, *args) -> None: ...
    SectionLabelPlacement: SettingsSectionLabelPlacement
    ProfileLabelPlacement: SettingsProfileLabelPlacement
    StormSewersMigration: SettingsStormSewersMigration
    Default: SettingsDefault
    Rules: SettingsRules
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddSpotElevLabelsOnGrid(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddSpotElevLabelsOnGrid"""
    def __init__(self, *args) -> None: ...
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddSurfaceBoundaries(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddSurfaceBoundaries"""
    def __init__(self, *args) -> None: ...
    DataOptions: SettingsCmdAddDataOptions
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddSurfaceBreaklines(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddSurfaceBreaklines"""
    def __init__(self, *args) -> None: ...
    DataOptions: SettingsCmdAddDataOptions
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddSurfaceContours(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddSurfaceContours"""
    def __init__(self, *args) -> None: ...
    AddDataOptions: SettingsCmdAddDataOptions
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddSurfaceDemFile(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddSurfaceDemFile"""
    def __init__(self, *args) -> None: ...
    ImportOptions: SettingsCmdImportOptions
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddSurfaceDrawingObjects(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddSurfaceDrawingObjects"""
    def __init__(self, *args) -> None: ...
    DataOptions: SettingsCmdAddDataOptions
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddSurfaceFigSurveyQuery(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddSurfaceFigSurveyQuery"""
    def __init__(self, *args) -> None: ...
    DataOptions: SettingsCmdAddDataOptions
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddSurfacePointSurveyQuery(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddSurfacePointSurveyQuery"""
    def __init__(self, *args) -> None: ...
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddSurfaceSlopeLabel(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddSurfaceSlopeLabel"""
    def __init__(self, *args) -> None: ...
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddSurfaceSpotElevLabel(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddSurfaceSpotElevLabel"""
    def __init__(self, *args) -> None: ...
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddSvFigureLabel(SettingsSurvey):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddSvFigureLabel"""
    def __init__(self, *args) -> None: ...
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddSvFigureSegmentLabel(SettingsSurvey):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddSvFigureSegmentLabel"""
    def __init__(self, *args) -> None: ...
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddSvFigureSegmentLabels(SettingsSurvey):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddSvFigureSegmentLabels"""
    def __init__(self, *args) -> None: ...
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddTotalVolumeTable(SettingsQuantityTakeoff):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddTotalVolumeTable"""
    def __init__(self, *args) -> None: ...
    TableCreation: SettingsCmdTableCreation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAddWidening(SettingsAlignment):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAddWidening"""
    def __init__(self, *args) -> None: ...
    LinearTransitionAroundCurves: SettingsCmdLinearTransitionAroundCurves
    WideningOptions: SettingsCmdWideningOptions
    AutomaticWideningAroundCurves: SettingsAutomaticWideningAroundCurves
    ConstraintEditing: SettingsConstraintEditing
    ImpliedPointOfIntersection: SettingsImpliedPointOfIntersection
    DynamicAlignmentHighlight: SettingsDynamicAlignmentHighlight
    Data: SettingsData
    CriteriaBasedDesignOptions: SettingsCriteriaBasedDesignOptions
    RailOptions: SettingsRailAlignmentOptions
    CantOptions: SettingsCantOptions
    SuperelevationOptions: SettingsSuperelevationOptions
    StationIndexing: SettingsStationIndexing
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdAssignPayItemToArea(SettingsQuantityTakeoff):
    """.NET: Autodesk.Civil.Settings.SettingsCmdAssignPayItemToArea"""
    def __init__(self, *args) -> None: ...
    AssignPayItemToAreaOption: SettingsCmdAssignPayItemToAreaOptions
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCatchmentArea(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCatchmentArea"""
    def __init__(self, *args) -> None: ...
    DischargePointStyleId: PropertyObjectId
    DischargePointStyle: PropertyString
    DisplayDisChargePoint: PropertyBoolean
    ObjectType: PropertyEnum
    Layer: PropertyLayer
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdComputeMaterials(SettingsQuantityTakeoff):
    """.NET: Autodesk.Civil.Settings.SettingsCmdComputeMaterials"""
    def __init__(self, *args) -> None: ...
    DefineMaterialOption: SettingsCmdDefineMaterial
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdConvertPointstoSdskPoints(SettingsPoint):
    """.NET: Autodesk.Civil.Settings.SettingsCmdConvertPointstoSdskPoints"""
    def __init__(self, *args) -> None: ...
    Layer: SettingsCmdLayer
    UpdatePoints: SettingsUpdatePoints
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCorridorExtractSurfaces(SettingsCorridor):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCorridorExtractSurfaces"""
    def __init__(self, *args) -> None: ...
    RegionHighlightGraphics: SettingsRegionHighlightGraphics
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateAlignFromCorridor(SettingsCorridor):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateAlignFromCorridor"""
    def __init__(self, *args) -> None: ...
    CriteriaBasedDesignOptions: SettingsCmdCriteriaBasedDesignOptions
    ProfileCreationOption: SettingsCmdProfileCreationOption
    AlignmentTypeOption: SettingsCmdAlignmentTypeOption
    RegionHighlightGraphics: SettingsRegionHighlightGraphics
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateAlignFromNetwork(SettingsPipeNetwork):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateAlignFromNetwork"""
    def __init__(self, *args) -> None: ...
    AlignmentTypeOption: SettingsCmdAlignmentTypeOption
    SectionLabelPlacement: SettingsSectionLabelPlacement
    ProfileLabelPlacement: SettingsProfileLabelPlacement
    StormSewersMigration: SettingsStormSewersMigration
    Default: SettingsDefault
    Rules: SettingsRules
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateAlignmentEntities(SettingsAlignment):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateAlignmentEntities"""
    def __init__(self, *args) -> None: ...
    AlignmentTypeOption: SettingsCmdAlignmentTypeOption
    CreateFromEntities: SettingsCmdCreateFromEntities
    AutomaticWideningAroundCurves: SettingsAutomaticWideningAroundCurves
    ConstraintEditing: SettingsConstraintEditing
    ImpliedPointOfIntersection: SettingsImpliedPointOfIntersection
    DynamicAlignmentHighlight: SettingsDynamicAlignmentHighlight
    Data: SettingsData
    CriteriaBasedDesignOptions: SettingsCriteriaBasedDesignOptions
    RailOptions: SettingsRailAlignmentOptions
    CantOptions: SettingsCantOptions
    SuperelevationOptions: SettingsSuperelevationOptions
    StationIndexing: SettingsStationIndexing
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateAlignmentLayout(SettingsAlignment):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateAlignmentLayout"""
    def __init__(self, *args) -> None: ...
    AlignmentTypeOption: SettingsCmdAlignmentTypeOption
    RegressionGraphOption: SettingsCmdRegressionGraphOption
    CurveTessellationOption: SettingsCmdCurveTessellationOption
    CurveAndSpiralSettings: SettingsCmdCurveAndSpiralSettings
    AutomaticWideningAroundCurves: SettingsAutomaticWideningAroundCurves
    ConstraintEditing: SettingsConstraintEditing
    ImpliedPointOfIntersection: SettingsImpliedPointOfIntersection
    DynamicAlignmentHighlight: SettingsDynamicAlignmentHighlight
    Data: SettingsData
    CriteriaBasedDesignOptions: SettingsCriteriaBasedDesignOptions
    RailOptions: SettingsRailAlignmentOptions
    CantOptions: SettingsCantOptions
    SuperelevationOptions: SettingsSuperelevationOptions
    StationIndexing: SettingsStationIndexing
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateAlignmentReference(SettingsAlignment):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateAlignmentReference"""
    def __init__(self, *args) -> None: ...
    AutomaticWideningAroundCurves: SettingsAutomaticWideningAroundCurves
    ConstraintEditing: SettingsConstraintEditing
    ImpliedPointOfIntersection: SettingsImpliedPointOfIntersection
    DynamicAlignmentHighlight: SettingsDynamicAlignmentHighlight
    Data: SettingsData
    CriteriaBasedDesignOptions: SettingsCriteriaBasedDesignOptions
    RailOptions: SettingsRailAlignmentOptions
    CantOptions: SettingsCantOptions
    SuperelevationOptions: SettingsSuperelevationOptions
    StationIndexing: SettingsStationIndexing
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateArcByBestFit(SettingsGeneral):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateArcByBestFit"""
    def __init__(self, *args) -> None: ...
    RegressionGraphOption: SettingsCmdRegressionGraphOption
    CurveTessellationOption: SettingsCmdCurveTessellationOption
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateAssembly(SettingsAssembly):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateAssembly"""
    def __init__(self, *args) -> None: ...
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateAssemblyTool(SettingsAssembly):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateAssemblyTool"""
    def __init__(self, *args) -> None: ...
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateCantView(SettingsCantView):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateCantView"""
    def __init__(self, *args) -> None: ...
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateCatchmentFromObject(SettingsCatchment):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateCatchmentFromObject"""
    def __init__(self, *args) -> None: ...
    TimeOfConcentrationMethod: PropertyEnum
    ChannelFlow: SettingsCmdChannelFlow
    ShallowConcentratedFlow: SettingsCmdShallowConcentratedFlow
    SheetFlow: SettingsCmdSheetFlow
    HydrologicalProperties: SettingsCmdHydrologicalProperties
    Catchment: SettingsCmdCatchment
    Styles: SettingsStyles
    NameTemplate: PropertyString
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateCatchmentFromSurface(SettingsCatchment):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateCatchmentFromSurface"""
    def __init__(self, *args) -> None: ...
    TimeOfConcentrationMethod: PropertyEnum
    ChannelFlow: SettingsCmdChannelFlow
    ShallowConcentratedFlow: SettingsCmdShallowConcentratedFlow
    SheetFlow: SettingsCmdSheetFlow
    HydrologicalProperties: SettingsCmdHydrologicalProperties
    Catchment: SettingsCmdCatchment
    Styles: SettingsStyles
    NameTemplate: PropertyString
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateCatchmentGroup(SettingsCatchment):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateCatchmentGroup"""
    def __init__(self, *args) -> None: ...
    Styles: SettingsStyles
    NameTemplate: PropertyString
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateCorridor(SettingsCorridor):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateCorridor"""
    def __init__(self, *args) -> None: ...
    AssemblyInsertion: SettingsCmdAssemblyInsertion
    RegionHighlightGraphics: SettingsRegionHighlightGraphics
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateFeatureLineFromAlign(SettingsGrading):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateFeatureLineFromAlign"""
    def __init__(self, *args) -> None: ...
    FeatureLineCreation: SettingsCmdFeatureLineCreation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateFeatureLines(SettingsGrading):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateFeatureLines"""
    def __init__(self, *args) -> None: ...
    FeatureLineCreation: SettingsCmdFeatureLineCreation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateFlowSegment(SettingsCatchment):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateFlowSegment"""
    def __init__(self, *args) -> None: ...
    ChannelFlow: SettingsCmdChannelFlow
    ShallowConcentratedFlow: SettingsCmdShallowConcentratedFlow
    SheetFlow: SettingsCmdSheetFlow
    Styles: SettingsStyles
    NameTemplate: PropertyString
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateGrading(SettingsGrading):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateGrading"""
    def __init__(self, *args) -> None: ...
    GradingCreation: SettingsCmdGradingCreation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateGradingGroup(SettingsGrading):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateGradingGroup"""
    def __init__(self, *args) -> None: ...
    GradingGroupCreation: SettingsCmdGradingGroupCreation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateInterferenceCheck(SettingsPipeNetwork):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateInterferenceCheck"""
    def __init__(self, *args) -> None: ...
    InterferenceCriteria: SettingsCmdInterferenceCriteria
    SectionLabelPlacement: SettingsSectionLabelPlacement
    ProfileLabelPlacement: SettingsProfileLabelPlacement
    StormSewersMigration: SettingsStormSewersMigration
    Default: SettingsDefault
    Rules: SettingsRules
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateIntersection(SettingsIntersection):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateIntersection"""
    def __init__(self, *args) -> None: ...
    CurbReturnProfileRules: SettingsCmdCurbReturnProfileRules
    SecondaryRoadProfileRules: SettingsCmdSecondaryRoadProfileRules
    WideningParameters: SettingsCmdWideningParameters
    CurbReturnParameters: SettingsCmdCurbReturnParameters
    CrossSlopes: SettingsCmdCrossSlopes
    Offsets: SettingsCmdOffsets
    IntersectionOptions: SettingsCmdIntersectionOptions
    AssemblyInsertion: SettingsCmdAssemblyInsertion
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateLineByBestFit(SettingsGeneral):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateLineByBestFit"""
    def __init__(self, *args) -> None: ...
    RegressionGraphOption: SettingsCmdRegressionGraphOption
    CurveTessellationOption: SettingsCmdCurveTessellationOption
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateMassHaulDiagram(SettingsMassHaulView):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateMassHaulDiagram"""
    def __init__(self, *args) -> None: ...
    MassHaulCreation: SettingsCmdMassHaulCreation
    MassHaulCreation: SettingsMassHaulCreation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateMultipleProfileView(SettingsProfileView):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateMultipleProfileView"""
    def __init__(self, *args) -> None: ...
    MultipleProfileViewCreation: SettingsCmdMultipleProfileViewCreation
    ProjectionLabelPlacement: SettingsProjectionLabelPlacement
    StackedOptions: SettingsStackedOptions
    SplitOptions: SettingsSplitOptions
    Creation: SettingsCreation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateMultipleSectionView(SettingsSectionView):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateMultipleSectionView"""
    def __init__(self, *args) -> None: ...
    MultipleSectionViewCreation: SettingsCmdMultipleSectionViewCreation
    TableCreation: SettingsCmdTableCreation
    ProjectionLabelPlacement: SettingsProjectionLabelPlacement
    SectionViewCreation: SettingsSectionViewCreation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateNetwork(SettingsPipeNetwork):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateNetwork"""
    def __init__(self, *args) -> None: ...
    DefaultLayoutCommand: PropertyEnum
    LabelNewParts: SettingsCmdLabelNewParts
    SectionLabelPlacement: SettingsSectionLabelPlacement
    ProfileLabelPlacement: SettingsProfileLabelPlacement
    StormSewersMigration: SettingsStormSewersMigration
    Default: SettingsDefault
    Rules: SettingsRules
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateNetworkFromObject(SettingsPipeNetwork):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateNetworkFromObject"""
    def __init__(self, *args) -> None: ...
    SectionLabelPlacement: SettingsSectionLabelPlacement
    ProfileLabelPlacement: SettingsProfileLabelPlacement
    StormSewersMigration: SettingsStormSewersMigration
    Default: SettingsDefault
    Rules: SettingsRules
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateNetworkPartsList(SettingsPipeNetwork):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateNetworkPartsList"""
    def __init__(self, *args) -> None: ...
    SectionLabelPlacement: SettingsSectionLabelPlacement
    ProfileLabelPlacement: SettingsProfileLabelPlacement
    StormSewersMigration: SettingsStormSewersMigration
    Default: SettingsDefault
    Rules: SettingsRules
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateNetworkPartsListFull(SettingsPipeNetwork):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateNetworkPartsListFull"""
    def __init__(self, *args) -> None: ...
    SectionLabelPlacement: SettingsSectionLabelPlacement
    ProfileLabelPlacement: SettingsProfileLabelPlacement
    StormSewersMigration: SettingsStormSewersMigration
    Default: SettingsDefault
    Rules: SettingsRules
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateNetworkReference(SettingsPipeNetwork):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateNetworkReference"""
    def __init__(self, *args) -> None: ...
    SectionLabelPlacement: SettingsSectionLabelPlacement
    ProfileLabelPlacement: SettingsProfileLabelPlacement
    StormSewersMigration: SettingsStormSewersMigration
    Default: SettingsDefault
    Rules: SettingsRules
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateOffsetAlignment(SettingsAlignment):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateOffsetAlignment"""
    def __init__(self, *args) -> None: ...
    OffsetAlignmentOptions: SettingsCmdOffsetAlignmentOptions
    AutomaticWideningAroundCurves: SettingsAutomaticWideningAroundCurves
    ConstraintEditing: SettingsConstraintEditing
    ImpliedPointOfIntersection: SettingsImpliedPointOfIntersection
    DynamicAlignmentHighlight: SettingsDynamicAlignmentHighlight
    Data: SettingsData
    CriteriaBasedDesignOptions: SettingsCriteriaBasedDesignOptions
    RailOptions: SettingsRailAlignmentOptions
    CantOptions: SettingsCantOptions
    SuperelevationOptions: SettingsSuperelevationOptions
    StationIndexing: SettingsStationIndexing
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateParabolaByBestFit(SettingsGeneral):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateParabolaByBestFit"""
    def __init__(self, *args) -> None: ...
    RegressionGraphOption: SettingsCmdRegressionGraphOption
    CurveTessellationOption: SettingsCmdCurveTessellationOption
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateParcelByLayout(SettingsParcel):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateParcelByLayout"""
    def __init__(self, *args) -> None: ...
    ConvertFromEntities: SettingsCmdConvertFromEntities
    AutomaticLayout: SettingsCmdAutomaticLayout
    PreviewGraphics: SettingsCmdPreviewGraphics
    ParcelSizing: SettingsCmdParcelSizing
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateParcelFromObjects(SettingsParcel):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateParcelFromObjects"""
    def __init__(self, *args) -> None: ...
    ConvertFromEntities: SettingsCmdConvertFromEntities
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateParcelROW(SettingsParcel):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateParcelROW"""
    def __init__(self, *args) -> None: ...
    CleanupAtAlignmentIntersections: SettingsCmdCleanupAtAlignmentIntersections
    CleanupAtParcelBoundaries: SettingsCmdCleanupAtParcelBoundaries
    CreateParcelRightOfWay: SettingsCmdCreateParcelRightOfWay
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreatePointCloud(SettingsPointCloud):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreatePointCloud"""
    def __init__(self, *args) -> None: ...
    DefaultLayer: SettingsCmdDefaultLayer
    FileFormat: PropertyEnum
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreatePointGroup(SettingsPoint):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreatePointGroup"""
    def __init__(self, *args) -> None: ...
    UpdatePoints: SettingsUpdatePoints
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreatePoints(SettingsPoint):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreatePoints"""
    def __init__(self, *args) -> None: ...
    PointIdentity: SettingsCmdPointIdentity
    PointsCreation: SettingsCmdPointsCreation
    Layer: SettingsCmdLayer
    UpdatePoints: SettingsUpdatePoints
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreatePointsFromCorridor(SettingsCorridor):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreatePointsFromCorridor"""
    def __init__(self, *args) -> None: ...
    RegionHighlightGraphics: SettingsRegionHighlightGraphics
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreatePolylineFromCorridor(SettingsCorridor):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreatePolylineFromCorridor"""
    def __init__(self, *args) -> None: ...
    RegionHighlightGraphics: SettingsRegionHighlightGraphics
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreatePolylineFromSuper(SettingsSuperelevationView):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreatePolylineFromSuper"""
    def __init__(self, *args) -> None: ...
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateProfileFromCorridor(SettingsCorridor):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateProfileFromCorridor"""
    def __init__(self, *args) -> None: ...
    CriteriaBasedDesignOptions: SettingsCmdCriteriaBasedDesignOptions
    RegionHighlightGraphics: SettingsRegionHighlightGraphics
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateProfileFromFile(SettingsProfile):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateProfileFromFile"""
    def __init__(self, *args) -> None: ...
    CriteriaBasedDesignOptions: SettingsCriteriaBasedDesignOptions
    ProfilesCreation: SettingsProfileCreation
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateProfileFromSurface(SettingsProfile):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateProfileFromSurface"""
    def __init__(self, *args) -> None: ...
    Geometry: SettingsCmdGeometry
    CriteriaBasedDesignOptions: SettingsCriteriaBasedDesignOptions
    ProfilesCreation: SettingsProfileCreation
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateProfileLayout(SettingsProfile):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateProfileLayout"""
    def __init__(self, *args) -> None: ...
    RegressionGraphOption: SettingsCmdRegressionGraphOption
    CurveTessellationOption: SettingsCmdCurveTessellationOption
    CriteriaBasedDesignOptions: SettingsCriteriaBasedDesignOptions
    ProfilesCreation: SettingsProfileCreation
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateProfileReference(SettingsProfile):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateProfileReference"""
    def __init__(self, *args) -> None: ...
    CriteriaBasedDesignOptions: SettingsCriteriaBasedDesignOptions
    ProfilesCreation: SettingsProfileCreation
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateProfileView(SettingsProfileView):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateProfileView"""
    def __init__(self, *args) -> None: ...
    ProjectionLabelPlacement: SettingsProjectionLabelPlacement
    StackedOptions: SettingsStackedOptions
    SplitOptions: SettingsSplitOptions
    Creation: SettingsCreation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateQuickProfile(SettingsProfile):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateQuickProfile"""
    def __init__(self, *args) -> None: ...
    QuickProfile: SettingsCmdQuickProfile
    CriteriaBasedDesignOptions: SettingsCriteriaBasedDesignOptions
    ProfilesCreation: SettingsProfileCreation
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateSampleLines(SettingsSampleLine):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateSampleLines"""
    def __init__(self, *args) -> None: ...
    Miscellaneous: SettingsCmdMiscellaneous
    AdditionalSampleControls: SettingsCmdAdditionalSampleControls
    SamplingIncrements: SettingsCmdSamplingIncrements
    SwathWidths: SettingsCmdSwathWidths
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateSectionSheets(SettingsSectionView):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateSectionSheets"""
    def __init__(self, *args) -> None: ...
    SheetCreation: SettingsCmdSheetCreation
    ProjectionLabelPlacement: SettingsProjectionLabelPlacement
    SectionViewCreation: SettingsSectionViewCreation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateSectionView(SettingsSectionView):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateSectionView"""
    def __init__(self, *args) -> None: ...
    TableCreation: SettingsCmdTableCreation
    ProjectionLabelPlacement: SettingsProjectionLabelPlacement
    SectionViewCreation: SettingsSectionViewCreation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateSheets(SettingsViewFrameGroup):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateSheets"""
    def __init__(self, *args) -> None: ...
    SheetCreation: SettingsCmdSheetCreation
    Information: SettingsInformation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateSimpleCorridor(SettingsCorridor):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateSimpleCorridor"""
    def __init__(self, *args) -> None: ...
    AssemblyInsertion: SettingsCmdAssemblyInsertion
    RegionHighlightGraphics: SettingsRegionHighlightGraphics
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateSite(SettingsParcel):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateSite"""
    def __init__(self, *args) -> None: ...
    FeatureLine: SettingsCmdFeatureLine
    Alignment: SettingsCmdAlignment
    Parcel: SettingsCmdParcel
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateSubFromPline(SettingsSubassembly):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateSubFromPline"""
    def __init__(self, *args) -> None: ...
    CreateFromEntities: SettingsCmdCreateFromEntities
    DefaultStyles: SettingsDefaultStyles
    NameFormat: SettingsNameFormat
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateSubassemblyTool(SettingsSubassembly):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateSubassemblyTool"""
    def __init__(self, *args) -> None: ...
    SubassemblyOptions: SettingsCmdSubassemblyOptions
    DefaultStyles: SettingsDefaultStyles
    NameFormat: SettingsNameFormat
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateSuperelevationView(SettingsSuperelevationView):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateSuperelevationView"""
    def __init__(self, *args) -> None: ...
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateSurface(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateSurface"""
    def __init__(self, *args) -> None: ...
    BuildOptions: SettingsCmdBuildOptions
    SurfaceCreation: SettingsCmdSurfaceCreation
    NameFormat: SettingsNameFormat
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateSurfaceFromTIN(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateSurfaceFromTIN"""
    def __init__(self, *args) -> None: ...
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateSurfaceGridFromDEM(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateSurfaceGridFromDEM"""
    def __init__(self, *args) -> None: ...
    BuildOptions: SettingsCmdBuildOptions
    ImportOptions: SettingsCmdImportOptions
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateSurfaceReference(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateSurfaceReference"""
    def __init__(self, *args) -> None: ...
    NameFormat: SettingsNameFormat
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateSurfaceWaterdrop(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateSurfaceWaterdrop"""
    def __init__(self, *args) -> None: ...
    WaterdropMarker: SettingsCmdWaterdropMarker
    WaterdropPath: SettingsCmdWaterdropPath
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdCreateViewFrames(SettingsViewFrameGroup):
    """.NET: Autodesk.Civil.Settings.SettingsCmdCreateViewFrames"""
    def __init__(self, *args) -> None: ...
    ViewFrameCreation: SettingsCmdViewFrameCreation
    Information: SettingsInformation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdDrawFeatureLine(SettingsGrading):
    """.NET: Autodesk.Civil.Settings.SettingsCmdDrawFeatureLine"""
    def __init__(self, *args) -> None: ...
    FeatureLineCreation: SettingsCmdFeatureLineCreation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdEditFlowSegments(SettingsCatchment):
    """.NET: Autodesk.Civil.Settings.SettingsCmdEditFlowSegments"""
    def __init__(self, *args) -> None: ...
    ChannelFlow: SettingsCmdChannelFlow
    ShallowConcentratedFlow: SettingsCmdShallowConcentratedFlow
    SheetFlow: SettingsCmdSheetFlow
    Styles: SettingsStyles
    NameTemplate: PropertyString
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdEditInStormSewers(SettingsPipeNetwork):
    """.NET: Autodesk.Civil.Settings.SettingsCmdEditInStormSewers"""
    def __init__(self, *args) -> None: ...
    SectionLabelPlacement: SettingsSectionLabelPlacement
    ProfileLabelPlacement: SettingsProfileLabelPlacement
    StormSewersMigration: SettingsStormSewersMigration
    Default: SettingsDefault
    Rules: SettingsRules
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdEditSVGroupStyle(SettingsSectionView):
    """.NET: Autodesk.Civil.Settings.SettingsCmdEditSVGroupStyle"""
    def __init__(self, *args) -> None: ...
    ProjectionLabelPlacement: SettingsProjectionLabelPlacement
    SectionViewCreation: SettingsSectionViewCreation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdExportCivilDrawing(SettingsGeneral):
    """.NET: Autodesk.Civil.Settings.SettingsCmdExportCivilDrawing"""
    def __init__(self, *args) -> None: ...
    ExportCivilDrawingOption: SettingsCmdExportCivilDrawingOption
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdExportParcelAnalysis(SettingsParcel):
    """.NET: Autodesk.Civil.Settings.SettingsCmdExportParcelAnalysis"""
    def __init__(self, *args) -> None: ...
    ParcelAnalysis: SettingsCmdParcelAnalysis
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdExportStormSewerData(SettingsPipeNetwork):
    """.NET: Autodesk.Civil.Settings.SettingsCmdExportStormSewerData"""
    def __init__(self, *args) -> None: ...
    SectionLabelPlacement: SettingsSectionLabelPlacement
    ProfileLabelPlacement: SettingsProfileLabelPlacement
    StormSewersMigration: SettingsStormSewersMigration
    Default: SettingsDefault
    Rules: SettingsRules
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdFeatureLinesFromCorridor(SettingsCorridor):
    """.NET: Autodesk.Civil.Settings.SettingsCmdFeatureLinesFromCorridor"""
    def __init__(self, *args) -> None: ...
    FeatureLineCreation: SettingsCmdFeatureLineCreation
    RegionHighlightGraphics: SettingsRegionHighlightGraphics
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdFitCurveFeature(SettingsGrading):
    """.NET: Autodesk.Civil.Settings.SettingsCmdFitCurveFeature"""
    def __init__(self, *args) -> None: ...
    FeatureLineFitCurve: SettingsCmdFeatureLineFitCurve
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdGenerateQuantitiesReport(SettingsQuantityTakeoff):
    """.NET: Autodesk.Civil.Settings.SettingsCmdGenerateQuantitiesReport"""
    def __init__(self, *args) -> None: ...
    DisplayXmlReport: PropertyBoolean
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdGradingElevEditor(SettingsGrading):
    """.NET: Autodesk.Civil.Settings.SettingsCmdGradingElevEditor"""
    def __init__(self, *args) -> None: ...
    GradingElevationEditor: SettingsCmdGradingElevationEditor
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdGradingTools(SettingsGrading):
    """.NET: Autodesk.Civil.Settings.SettingsCmdGradingTools"""
    def __init__(self, *args) -> None: ...
    GradingLayoutTools: SettingsCmdGradingLayoutTools
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdGradingVolumeTools(SettingsGrading):
    """.NET: Autodesk.Civil.Settings.SettingsCmdGradingVolumeTools"""
    def __init__(self, *args) -> None: ...
    LimitFeatureSelectionToCurrentGroup: PropertyBoolean
    RaiseLowerElevationIncrement: PropertyDouble
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdImportBuildingSite(SettingsBuildingSite):
    """.NET: Autodesk.Civil.Settings.SettingsCmdImportBuildingSite"""
    def __init__(self, *args) -> None: ...
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdImportGISData(SettingsGeneral):
    """.NET: Autodesk.Civil.Settings.SettingsCmdImportGISData"""
    def __init__(self, *args) -> None: ...
    PipeNetwork: SettingsCmdPipeNetwork
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdImportStormSewerData(SettingsPipeNetwork):
    """.NET: Autodesk.Civil.Settings.SettingsCmdImportStormSewerData"""
    def __init__(self, *args) -> None: ...
    SectionLabelPlacement: SettingsSectionLabelPlacement
    ProfileLabelPlacement: SettingsProfileLabelPlacement
    StormSewersMigration: SettingsStormSewersMigration
    Default: SettingsDefault
    Rules: SettingsRules
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdJoinFeatures(SettingsGrading):
    """.NET: Autodesk.Civil.Settings.SettingsCmdJoinFeatures"""
    def __init__(self, *args) -> None: ...
    FeatureLineJoin: SettingsCmdFeatureLineJoin
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdLayoutSectionViewGroup(SettingsSectionView):
    """.NET: Autodesk.Civil.Settings.SettingsCmdLayoutSectionViewGroup"""
    def __init__(self, *args) -> None: ...
    ProjectionLabelPlacement: SettingsProjectionLabelPlacement
    SectionViewCreation: SettingsSectionViewCreation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdMapCheck(SettingsGeneral):
    """.NET: Autodesk.Civil.Settings.SettingsCmdMapCheck"""
    def __init__(self, *args) -> None: ...
    Mapcheck: SettingsCmdMapcheck
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdMinimizeSurfaceFlatAreas(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdMinimizeSurfaceFlatAreas"""
    def __init__(self, *args) -> None: ...
    AddPointsToFlatEdges: PropertyBoolean
    AddPointsToFlatTriangles: PropertyBoolean
    SwapEdges: PropertyBoolean
    FillGapsInContour: PropertyBoolean
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdMoveBlocksToSurface(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdMoveBlocksToSurface"""
    def __init__(self, *args) -> None: ...
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdMoveBlockstoAttribElev(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdMoveBlockstoAttribElev"""
    def __init__(self, *args) -> None: ...
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdMoveTextToElevation(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdMoveTextToElevation"""
    def __init__(self, *args) -> None: ...
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdProjectObjectsToMultiSect(SettingsSectionView):
    """.NET: Autodesk.Civil.Settings.SettingsCmdProjectObjectsToMultiSect"""
    def __init__(self, *args) -> None: ...
    ObjectSelectionOptions: SettingsCmdObjectSelectionOptions
    ProjectionLabelPlacement: SettingsProjectionLabelPlacement
    SectionViewCreation: SettingsSectionViewCreation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdProjectObjectsToProf(SettingsProfileView):
    """.NET: Autodesk.Civil.Settings.SettingsCmdProjectObjectsToProf"""
    def __init__(self, *args) -> None: ...
    ProjectionLabelPlacement: SettingsProjectionLabelPlacement
    StackedOptions: SettingsStackedOptions
    SplitOptions: SettingsSplitOptions
    Creation: SettingsCreation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdProjectObjectsToSect(SettingsSectionView):
    """.NET: Autodesk.Civil.Settings.SettingsCmdProjectObjectsToSect"""
    def __init__(self, *args) -> None: ...
    ProjectionLabelPlacement: SettingsProjectionLabelPlacement
    SectionViewCreation: SettingsSectionViewCreation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdReAddParcelAreaLabel(SettingsParcel):
    """.NET: Autodesk.Civil.Settings.SettingsCmdReAddParcelAreaLabel"""
    def __init__(self, *args) -> None: ...
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdReAddParcelSegmentLabels(SettingsParcel):
    """.NET: Autodesk.Civil.Settings.SettingsCmdReAddParcelSegmentLabels"""
    def __init__(self, *args) -> None: ...
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdRenamePipeNetworkParts(SettingsPipeNetwork):
    """.NET: Autodesk.Civil.Settings.SettingsCmdRenamePipeNetworkParts"""
    def __init__(self, *args) -> None: ...
    SectionLabelPlacement: SettingsSectionLabelPlacement
    ProfileLabelPlacement: SettingsProfileLabelPlacement
    StormSewersMigration: SettingsStormSewersMigration
    Default: SettingsDefault
    Rules: SettingsRules
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdResetAnchorPipe(SettingsPipeNetwork):
    """.NET: Autodesk.Civil.Settings.SettingsCmdResetAnchorPipe"""
    def __init__(self, *args) -> None: ...
    SectionLabelPlacement: SettingsSectionLabelPlacement
    ProfileLabelPlacement: SettingsProfileLabelPlacement
    StormSewersMigration: SettingsStormSewersMigration
    Default: SettingsDefault
    Rules: SettingsRules
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdReverseAlignmentDirection(SettingsAlignment):
    """.NET: Autodesk.Civil.Settings.SettingsCmdReverseAlignmentDirection"""
    def __init__(self, *args) -> None: ...
    AutomaticWideningAroundCurves: SettingsAutomaticWideningAroundCurves
    ConstraintEditing: SettingsConstraintEditing
    ImpliedPointOfIntersection: SettingsImpliedPointOfIntersection
    DynamicAlignmentHighlight: SettingsDynamicAlignmentHighlight
    Data: SettingsData
    CriteriaBasedDesignOptions: SettingsCriteriaBasedDesignOptions
    RailOptions: SettingsRailAlignmentOptions
    CantOptions: SettingsCantOptions
    SuperelevationOptions: SettingsSuperelevationOptions
    StationIndexing: SettingsStationIndexing
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdShowGeodeticCalculator(SettingsPoint):
    """.NET: Autodesk.Civil.Settings.SettingsCmdShowGeodeticCalculator"""
    def __init__(self, *args) -> None: ...
    UpdatePoints: SettingsUpdatePoints
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdShowPointGroupProperties(SettingsPoint):
    """.NET: Autodesk.Civil.Settings.SettingsCmdShowPointGroupProperties"""
    def __init__(self, *args) -> None: ...
    UpdatePoints: SettingsUpdatePoints
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdShowSpanningPipes(SettingsPipeNetwork):
    """.NET: Autodesk.Civil.Settings.SettingsCmdShowSpanningPipes"""
    def __init__(self, *args) -> None: ...
    SectionLabelPlacement: SettingsSectionLabelPlacement
    ProfileLabelPlacement: SettingsProfileLabelPlacement
    StormSewersMigration: SettingsStormSewersMigration
    Default: SettingsDefault
    Rules: SettingsRules
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdSimplifySurface(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdSimplifySurface"""
    def __init__(self, *args) -> None: ...
    MaximumChangeInElevation: PropertyDouble
    UseMaximumChangeInElevation: PropertyBoolean
    PercentageOfPointsToRemove: PropertyDouble
    UsePercentageOfPointsToRemove: PropertyBoolean
    RegionOptions: PropertyEnum
    SimplifyMethod: PropertyEnum
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdSuperimposeProfile(SettingsProfile):
    """.NET: Autodesk.Civil.Settings.SettingsCmdSuperimposeProfile"""
    def __init__(self, *args) -> None: ...
    SuperimposeProfile: SettingsCmdSuperimposeProfileOption
    CriteriaBasedDesignOptions: SettingsCriteriaBasedDesignOptions
    ProfilesCreation: SettingsProfileCreation
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdSurfaceExportToDem(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdSurfaceExportToDem"""
    def __init__(self, *args) -> None: ...
    ExportOptions: SettingsCmdExportOptions
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdSurfaceExtractObjects(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdSurfaceExtractObjects"""
    def __init__(self, *args) -> None: ...
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdTakeOff(SettingsQuantityTakeoff):
    """.NET: Autodesk.Civil.Settings.SettingsCmdTakeOff"""
    def __init__(self, *args) -> None: ...
    ComputeTakeOffOption: SettingsCmdComputeTakeOff
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdViewEditCorridorSection(SettingsCorridor):
    """.NET: Autodesk.Civil.Settings.SettingsCmdViewEditCorridorSection"""
    def __init__(self, *args) -> None: ...
    SectionSliderInMultipleViewports: SettingsCmdSectionSliderInMultipleViewports
    GridTextSettings: SettingsCmdGridTextSettings
    GridSettings: SettingsCmdGridSettings
    ViewEditOptions: SettingsCmdViewEditOptions
    RegionHighlightGraphics: SettingsRegionHighlightGraphics
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdVolumesDashboard(SettingsSurface):
    """.NET: Autodesk.Civil.Settings.SettingsCmdVolumesDashboard"""
    def __init__(self, *args) -> None: ...
    DynamicHighlightOptions: SettingsCmdDynamicHighlightOptions
    BoundedVolumeCreation: SettingsCmdBoundedVolumeCreation
    BuildOptions: SettingsCmdBuildOptions
    VolumeSurfaceCreation: SettingsCmdVolumeSurfaceCreation
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCmdWeedFeatures(SettingsGrading):
    """.NET: Autodesk.Civil.Settings.SettingsCmdWeedFeatures"""
    def __init__(self, *args) -> None: ...
    FeatureLineWeed: SettingsCmdFeatureLineWeed
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsCoordinateSystem:
    """.NET: Autodesk.Civil.Settings.SettingsCoordinateSystem"""
    def __init__(self, *args) -> None: ...
    Unit: str
    Datum: str
    Projection: str
    Description: str
    Code: str
    Category: str

class SettingsCorridor(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsCorridor"""
    def __init__(self, *args) -> None: ...
    RegionHighlightGraphics: SettingsRegionHighlightGraphics
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsDrawing(TreeOidWrapper):
    """.NET: Autodesk.Civil.Settings.SettingsDrawing"""
    def __init__(self, *args) -> None: ...
    ObjectLayerSettings: SettingsObjectLayers
    AmbientSettings: SettingsAmbient
    AbbreviationsSettings: SettingsAbbreviation
    TransformationSettings: SettingsTransformation
    ApplyTransformSettings: bool
    UnitZoneSettings: SettingsUnitZone
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsGeneral(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsGeneral"""
    def __init__(self, *args) -> None: ...
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsGrading(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsGrading"""
    def __init__(self, *args) -> None: ...
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsIntersection(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsIntersection"""
    def __init__(self, *args) -> None: ...
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsLandXML(TreeOidWrapper):
    """.NET: Autodesk.Civil.Settings.SettingsLandXML"""
    def __init__(self, *args) -> None: ...
    Export: SettingsLandXMLExport
    Import: SettingsLandXMLImport
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsLandXMLExport(TreeOidWrapper):
    """.NET: Autodesk.Civil.Settings.SettingsLandXMLExport"""
    def __init__(self, *args) -> None: ...
    FeatureLineExport: SettingsFeatureLineExport
    AlignmentExport: SettingsAlignmentExport
    ParcelExport: SettingsParcelExport
    SurfaceExport: SettingsSurfaceExport
    PointExport: SettingsPointExport
    Data: SettingsData
    Identification: SettingsIdentification
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsLandXMLImport(TreeOidWrapper):
    """.NET: Autodesk.Civil.Settings.SettingsLandXMLImport"""
    def __init__(self, *args) -> None: ...
    FeatureLineImport: SettingsFeatureLineImport
    PropertySetData: SettingsPropertySetData
    AlignmentImport: SettingsAlignmentImport
    DiameterUnits: SettingsDiameterUnits
    ConflictResolution: SettingsConflictResolution
    PipeNetwork: SettingsPipeNetwork
    SurfaceImport: SettingsSurfaceImport
    PointImport: SettingsPointImport
    Rotation: SettingsRotation
    Translation: SettingsTranslation
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsMassHaulLine(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsMassHaulLine"""
    def __init__(self, *args) -> None: ...
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsMassHaulView(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsMassHaulView"""
    def __init__(self, *args) -> None: ...
    MassHaulCreation: SettingsMassHaulCreation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsMatchLine(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsMatchLine"""
    def __init__(self, *args) -> None: ...
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsObjectLayer(TreeOidWrapper):
    """.NET: Autodesk.Civil.Settings.SettingsObjectLayer"""
    def __init__(self, *args) -> None: ...
    Locked: bool
    Modifier: ObjectLayerModifierType
    LayerId: ObjectId
    LayerName: str
    ModifierValue: str
    ObjectType: SettingsObjectLayerType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsObjectLayerType:
    """.NET enum: Autodesk.Civil.Settings.SettingsObjectLayerType"""
    def __init__(self, *args) -> None: ...
    Alignment: int  # = 0
    AlignmentLabeling: int  # = 1
    AlignmentTable: int  # = 2
    Assembly: int  # = 3
    Corridor: int  # = 4
    CorridorSection: int  # = 5
    FeatureLine: int  # = 6
    GeneralNoteLabel: int  # = 7
    GeneralSegmentLabel: int  # = 8
    Grading: int  # = 9
    GradingLabeling: int  # = 10
    GridSurface: int  # = 11
    GridSurfaceLabeling: int  # = 12
    Interference: int  # = 13
    MassHaulLine: int  # = 14
    MassHaulView: int  # = 15
    MatchLine: int  # = 16
    MatchLineLabeling: int  # = 17
    MaterialSection: int  # = 18
    MaterialTable: int  # = 19
    Parcel: int  # = 20
    ParcelLabeling: int  # = 21
    ParcelSegment: int  # = 22
    ParcelSegmentLabeling: int  # = 23
    ParcelTable: int  # = 24
    Pipe: int  # = 25
    PipeLabeling: int  # = 26
    PipeAndStructureTable: int  # = 27
    PipeNetworkSection: int  # = 28
    PipeOrStructureProfile: int  # = 29
    PointTable: int  # = 30
    Profile: int  # = 31
    ProfileLabeling: int  # = 32
    ProfileView: int  # = 33
    ProfileViewLabeling: int  # = 34
    SampleLine: int  # = 35
    SampleLineLabeling: int  # = 36
    Section: int  # = 37
    SectionLabeling: int  # = 38
    SectionView: int  # = 39
    SectionViewLabeling: int  # = 40
    SectionViewQuantityTakeoffTable: int  # = 41
    Sheet: int  # = 42
    Structure: int  # = 43
    StructureLabeling: int  # = 44
    Subassembly: int  # = 45
    SurfaceLegendTable: int  # = 46
    SurveyFigure: int  # = 47
    SurveyNetwork: int  # = 48
    TinSurface: int  # = 49
    TinSurfaceLabeling: int  # = 50
    ViewFrame: int  # = 51
    ViewFrameLabeling: int  # = 52
    BuildingSite: int  # = 53
    Intersection: int  # = 54
    IntersectionLabeling: int  # = 55
    Appurtenance: int  # = 56
    AppurtenanceLabeling: int  # = 57
    CantView: int  # = 58
    Catchment: int  # = 59
    CatchmentLabeling: int  # = 60
    Fitting: int  # = 61
    FittingLabeling: int  # = 62
    PressureNetworkSection: int  # = 63
    PressurePartProfile: int  # = 64
    PressurePartTable: int  # = 65
    PressurePipe: int  # = 66
    PressurePipeLabeling: int  # = 67
    SuperelevationView: int  # = 68
    SurveyFigureLabeling: int  # = 69
    SurveyFigureSegmentLable: int  # = 70
    Turnout: int  # = 71
class SettingsObjectLayers(TreeOidWrapper):
    """.NET: Autodesk.Civil.Settings.SettingsObjectLayers"""
    def __init__(self, *args) -> None: ...
    ObjectControlledByLayer: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetObjectLayerSetting(self, settingsType: SettingsObjectLayerType) -> SettingsObjectLayer: ...

class SettingsParcel(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsParcel"""
    def __init__(self, *args) -> None: ...
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsPipe(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsPipe"""
    def __init__(self, *args) -> None: ...
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsPipeNetwork(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsPipeNetwork"""
    def __init__(self, *args) -> None: ...
    SectionLabelPlacement: SettingsSectionLabelPlacement
    ProfileLabelPlacement: SettingsProfileLabelPlacement
    StormSewersMigration: SettingsStormSewersMigration
    Default: SettingsDefault
    Rules: SettingsRules
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsPoint(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsPoint"""
    def __init__(self, *args) -> None: ...
    UpdatePoints: SettingsUpdatePoints
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsPointCloud(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsPointCloud"""
    def __init__(self, *args) -> None: ...
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsProfile(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsProfile"""
    def __init__(self, *args) -> None: ...
    CriteriaBasedDesignOptions: SettingsCriteriaBasedDesignOptions
    ProfilesCreation: SettingsProfileCreation
    DefaultNameFormat: SettingsDefaultNameFormat
    StyleSettings: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsProfileView(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsProfileView"""
    def __init__(self, *args) -> None: ...
    ProjectionLabelPlacement: SettingsProjectionLabelPlacement
    StackedOptions: SettingsStackedOptions
    SplitOptions: SettingsSplitOptions
    Creation: SettingsCreation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsQuantityTakeoff(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsQuantityTakeoff"""
    def __init__(self, *args) -> None: ...
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsRoot(TreeOidWrapper):
    """.NET: Autodesk.Civil.Settings.SettingsRoot"""
    def __init__(self, *args) -> None: ...
    LandXMLSettings: SettingsLandXML
    AssociateShortcutProjectId: str
    DrawingSettings: SettingsDrawing
    TagSettings: SettingsTag
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetSettings(self, ) -> T: ...

class SettingsSampleLine(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsSampleLine"""
    def __init__(self, *args) -> None: ...
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsSection(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsSection"""
    def __init__(self, *args) -> None: ...
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsSectionView(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsSectionView"""
    def __init__(self, *args) -> None: ...
    ProjectionLabelPlacement: SettingsProjectionLabelPlacement
    SectionViewCreation: SettingsSectionViewCreation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsStructure(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsStructure"""
    def __init__(self, *args) -> None: ...
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsSubassembly(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsSubassembly"""
    def __init__(self, *args) -> None: ...
    DefaultStyles: SettingsDefaultStyles
    NameFormat: SettingsNameFormat
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsSuperelevationView(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsSuperelevationView"""
    def __init__(self, *args) -> None: ...
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsSurface(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsSurface"""
    def __init__(self, *args) -> None: ...
    Defaults: SettingsDefaults
    ContourLabeling: SettingsContourLabeling
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsSurvey(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsSurvey"""
    def __init__(self, *args) -> None: ...
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsTag(TreeOidWrapper):
    """.NET: Autodesk.Civil.Settings.SettingsTag"""
    def __init__(self, *args) -> None: ...
    Renumbering: SettingsRenumbering
    Creation: SettingsCreation
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsTransformation(TreeOidWrapper):
    """.NET: Autodesk.Civil.Settings.SettingsTransformation"""
    def __init__(self, *args) -> None: ...
    GridRotationPoint: Point2d
    LocalRotationPoint: Point2d
    GridReferencePoint: Point2d
    LocalReferencePoint: Point2d
    RotationToGridAzimuth: float
    RotationToGridNorth: float
    SpecifyRotationType: SpecifyRotationType
    GridScaleFactor: float
    GridScaleFactorComputation: GridScaleFactorType
    SpheroidRadius: float
    SeaLevelScaleElevation: float
    ApplySeaLevelScaleFactor: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsUnitZone(TreeOidWrapper):
    """.NET: Autodesk.Civil.Settings.SettingsUnitZone"""
    def __init__(self, *args) -> None: ...
    CoordinateSystemCode: str
    MatchAutoCADVariables: bool
    DrawingScale: float
    ScaleObjectsFromOtherDrawings: bool
    AngularUnits: AngleUnitType
    ImperialToMetricConversion: ImperialToMetricConversionType
    DrawingUnits: DrawingUnitType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetAllCodes() -> list: ...
    @staticmethod
    def GetCoordinateSystemByCode(code: str) -> SettingsCoordinateSystem: ...

class SettingsViewFrame(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsViewFrame"""
    def __init__(self, *args) -> None: ...
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SettingsViewFrameGroup(SettingsAmbient):
    """.NET: Autodesk.Civil.Settings.SettingsViewFrameGroup"""
    def __init__(self, *args) -> None: ...
    Information: SettingsInformation
    NameFormat: SettingsNameFormat
    Styles: SettingsStyles
    DegreeOfCurvature: SettingsDegreeOfCurvature
    Pressure: SettingsPressure
    Volume: SettingsVolume
    Speed: SettingsSpeed
    Slope: SettingsSlope
    TransparentCommands: SettingsTransparentCommands
    Acceleration: SettingsAcceleration
    Station: SettingsStation
    LatLong: SettingsLatLong
    Labeling: SettingsLabeling
    GridCoordinate: SettingsGridCoordinate
    GradeSlope: SettingsGradeSlope
    Grade: SettingsGrade
    General: SettingsGeneral
    Elevation: SettingsElevation
    Distance: SettingsDistance
    Direction: SettingsDirection
    Dimension: SettingsDimension
    Coordinate: SettingsCoordinate
    Area: SettingsArea
    Angle: SettingsAngle
    Unitless: SettingsUnitless
    Time: SettingsTime
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SpecifyRotationType:
    """.NET enum: Autodesk.Civil.Settings.SpecifyRotationType"""
    def __init__(self, *args) -> None: ...
    RotationPoint: int  # = 0
    GridRotationAngle: int  # = 1
class TableAnchorType:
    """.NET enum: Autodesk.Civil.Settings.TableAnchorType"""
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
class TableLayoutType:
    """.NET enum: Autodesk.Civil.Settings.TableLayoutType"""
    def __init__(self, *args) -> None: ...
    Horizontal: int  # = 0
    Vertical: int  # = 1
class TileDirectionType:
    """.NET enum: Autodesk.Civil.Settings.TileDirectionType"""
    def __init__(self, *args) -> None: ...
    Across: int  # = 0
    Down: int  # = 1
