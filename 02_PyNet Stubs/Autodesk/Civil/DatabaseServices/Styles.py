# Auto-generated — Civil 26 — Autodesk.Civil.DatabaseServices.Styles

class AlignmentDesignCheckSet(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AlignmentDesignCheckSet"""
    def __init__(self, *args) -> None: ...
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def AddDesignCheck(self, type: AlignmentDesignCheckType, name: str) -> AlignmentDesignCheck: ...
    def GetAllDesignChecks(self, ) -> list: ...
    def RemoveAllDesignCheck(self, ) -> None: ...
    def RemoveDesignCheck(self, type: AlignmentDesignCheckType, name: str) -> None: ...

class AlignmentDesignCheckSetCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AlignmentDesignCheckSetCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class AlignmentDisplayStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.AlignmentDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    Line: int  # = 0
    Curve: int  # = 1
    Spiral: int  # = 2
    Arrow: int  # = 3
    LineExtensions: int  # = 4
    CurveExtensions: int  # = 5
    TangentExtensions: int  # = 11
    WarningSymbol: int  # = 20
class AlignmentLabelSetItem(BaseLabelSetItem):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AlignmentLabelSetItem"""
    def __init__(self, *args) -> None: ...
    Increment: float
    LabelStyleName: str
    LabelStyleId: ObjectId
    LabelStyleType: LabelStyleType
    def GetLabeledAlignmentGeometryPoints(self, ) -> Dictionary: ...
    def GetLabeledProfileGeometryPoints(self, ) -> Dictionary: ...
    def GetLabeledSuperelevationTransitionPoints(self, ) -> Dictionary: ...
    def SetLabeledAlignmentGeometryPoints(self, pointTypes: Dictionary) -> None: ...
    def SetLabeledProfileGeometryPoints(self, pointTypes: Dictionary) -> None: ...
    def SetLabeledSuperelevationTransitionPoints(self, pointTypes: Dictionary) -> None: ...

class AlignmentLabelSetStyle(BaseLabelSetStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AlignmentLabelSetStyle"""
    def __init__(self, *args) -> None: ...
    Item: AlignmentLabelSetItem
    Count: int
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class AlignmentLabelSetStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AlignmentLabelSetStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class AlignmentStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AlignmentStyle"""
    def __init__(self, *args) -> None: ...
    ArrowHeadOption: ArrowHeadOption
    LineMarkerDisplayStyleSection: DisplayStyle
    CurveSpiralIntersectPointMarkerStyle: ObjectId
    EndPointMarkerStyle: ObjectId
    SpiralCurveIntersectPointMarkerStyle: ObjectId
    LineCurveIntersectPointMarkerStyle: ObjectId
    LineSpiralIntersectPointMarkerStyle: ObjectId
    SpiralLineIntersectPointMarkerStyle: ObjectId
    StationReferencePointMarkerStyle: ObjectId
    RadiusSnapValue: float
    CompoundCurveIntersectPointMarkerStyle: ObjectId
    ThroughPointMarkerStyle: ObjectId
    EnableRadiusSnap: bool
    BeginPointMarkerStyle: ObjectId
    ReverseSpiralIntersectPointMarkerStyle: ObjectId
    SpiralSpiralIntersectPointMarkerStyle: ObjectId
    ReverseCurveIntersectPointMarkerStyle: ObjectId
    IntersectionPointMarkerStyle: ObjectId
    CurveLineIntersectPointMarkerStyle: ObjectId
    MidPointMarkerStyle: ObjectId
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStyleModel(self, type: AlignmentDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, type: AlignmentDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStyleSection(self, ) -> DisplayStyle: ...
    def GetLineMarkerDisplayStyleSection(self, ) -> DisplayStyle: ...

class AlignmentStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AlignmentStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class ArrowHeadOption(CivilWrapper<AeccDbStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ArrowHeadOption"""
    def __init__(self, *args) -> None: ...
    FixedScaleZ: float
    FixedScaleY: float
    FixedScaleX: float
    Fit: ArrowHeadFitType
    SizeValue: float
    SizeOption: ArrowHeadSizeType
    ArrowBlockName: str
    ArrowType: ArrowHeadType

class AssemblyStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AssemblyStyle"""
    def __init__(self, *args) -> None: ...
    MarkerStyleAtOffsetBaselineOriginId: ObjectId
    MarkerStyleAtOffsetBaselineId: ObjectId
    MarkerStyleAtMainBaselineOriginId: ObjectId
    MarkerStyleAtMainBaselineId: ObjectId
    MarkerStyleAtAssemblyOriginId: ObjectId
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStyleModel(self, type: AssemblyDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, type: AssemblyDisplayStyleType) -> DisplayStyle: ...

class AssemblyStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AssemblyStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class AxisPosition:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.AxisPosition"""
    def __init__(self, *args) -> None: ...
    Top: int  # = 0
    Middle: int  # = 1
    Bottom: int  # = 2
    Left: int  # = 3
    Center: int  # = 4
    Right: int  # = 5
class AxisStyle(CivilWrapper<AeccDbGraphStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AxisStyle"""
    def __init__(self, *args) -> None: ...
    HorizontalGeometryTickStyle: AxisTickStyle
    MinorTickStyle: AxisTickStyle
    MajorTickStyle: AxisTickStyle
    TitleStyle: AxisTitleStyle
    ShowTickAndLabel: bool

class AxisTickJustificationType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.AxisTickJustificationType"""
    def __init__(self, *args) -> None: ...
    TopOrLeft: int  # = 0
    BottomOrRight: int  # = 1
    Center: int  # = 2
class AxisTickStyle(CivilWrapper<AeccDbGraphStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AxisTickStyle"""
    def __init__(self, *args) -> None: ...
    TickAndLabelStartElevation: bool
    OffsetY: float
    OffsetX: float
    Rotation: float
    Justification: AxisTickJustificationType
    TextHeight: float
    TextStyle: str
    LabelText: str
    Size: float
    Interval: float

class AxisTickType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.AxisTickType"""
    def __init__(self, *args) -> None: ...
    Major: int  # = 0
    Minor: int  # = 1
    HorizontalGeometry: int  # = 2
class AxisTitleLocationType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.AxisTitleLocationType"""
    def __init__(self, *args) -> None: ...
    BottomOrRight: int  # = 0
    Center: int  # = 1
    TopOrLeft: int  # = 2
class AxisTitleStyle(CivilWrapper<AeccDbGraphStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.AxisTitleStyle"""
    def __init__(self, *args) -> None: ...
    OffsetY: float
    OffsetX: float
    Rotation: float
    Location: AxisTitleLocationType
    TextHeight: float
    TextStyle: str
    Text: str

class BandLabelStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.BandLabelStyleType"""
    def __init__(self, *args) -> None: ...
    ProfileDataMajorIncrement: int  # = 268546560
    ProfileDataMinorIncrement: int  # = 268546576
    ProfileDataHGP: int  # = 268546592
    ProfileDataVGP: int  # = 268546608
    ProfileDataStationEquation: int  # = 268546624
    ProfileDataIncrementalDistance: int  # = 268546640
    VerticalGeometryUphillTangent: int  # = 268546816
    VerticalGeometryDownhillTangent: int  # = 268546832
    VerticalGeometryCrestCurve: int  # = 268546848
    VerticalGeometrySagCurve: int  # = 268546864
    HorizontalGeometryTangent: int  # = 268547072
    HorizontalGeometryCurve: int  # = 268547088
    HorizontalGeometrySpiral: int  # = 268547104
    SuperelevationDataNormalCrown: int  # = 268547328
    SuperelevationDataReverseCrown: int  # = 268547360
    SuperelevationDataFullSuper: int  # = 268547376
    SuperelevationDataLevelCrown: int  # = 268547392
    SuperelevationDataSlopeTransition: int  # = 268547408
    SuperelevationDataShoulderCritical: int  # = 268547616
    PipeNetworkStructureLocation: int  # = 268547632
    PipeNetworkPipeLocation: int  # = 268547648
    SectionalDataSampleLineLocation: int  # = 268547664
    SectionalDataIncrementalSectionData: int  # = 268547680
    SectionDataMajorIncrement: int  # = 268562944
    SectionDataMinorIncrement: int  # = 268562960
    SectionDataCenterline: int  # = 268562976
    SectionDataSampleLineVertices: int  # = 268562992
    SectionDataGradeBreaks: int  # = 268563008
    SectionDataIncrementalDistance: int  # = 268563024
    SectionSegmentSurfaceLabels: int  # = 268563200
class BandSetItem:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.BandSetItem"""
    def __init__(self, *args) -> None: ...
    StaggerLineHeight: float
    StaggerLabel: StaggerLabelType
    Weeding: float
    Gap: float
    ShowLabels: bool
    BandStyleId: ObjectId
    BandType: BandType
    MinorInterval: float
    MajorInterval: float
    Location: BandLocationType

class BandSetItemCollection:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.BandSetItemCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Location: BandLocationType
    def Add(self, bandStyleId: ObjectId) -> None: ...
    def Dispose(self, ) -> None: ...
    def RemoveAll(self, ) -> None: ...
    def RemoveAt(self, index: int) -> None: ...
    def Swap(self, index1: int, index2: int) -> None: ...

class BandSetStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.BandSetStyle"""
    def __init__(self, *args) -> None: ...
    MatchIncrementToGridIntervals: bool
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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

class BandStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.BandStyle"""
    def __init__(self, *args) -> None: ...
    WeedingFactor: float
    TextHeight: float
    TextLocation: BandTitleTextLocation
    TextBoxPosition: BandTitleBoxPosition
    OffsetFromBand: float
    TextBoxWidth: float
    BandHeight: float
    Text: str
    TextStyle: str
    TitleTextLabelStyleId: ObjectId
    BandType: BandType
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetBandStyleId(database: Database, bandType: BandType, bandStyleName: str) -> ObjectId: ...

class BandStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.BandStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class BandStylesRoot(TreeOidWrapper):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.BandStylesRoot"""
    def __init__(self, *args) -> None: ...
    SectionViewSegmentsBandStyles: BandStyleCollection
    SectionViewSectionDataBandStyles: BandStyleCollection
    ProfileViewPipeNetworkBandStyles: BandStyleCollection
    ProfileViewVerticalGeometryBandStyles: BandStyleCollection
    ProfileViewSuperElevationBandStyles: BandStyleCollection
    ProfileViewSectionalDataBandStyles: BandStyleCollection
    ProfileViewProfileDataBandStyles: BandStyleCollection
    ProfileViewHorizontalGeometryBandStyles: BandStyleCollection
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class BandTickStyle(CivilWrapper<AeccDbGraphStyleBands>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.BandTickStyle"""
    def __init__(self, *args) -> None: ...
    SmallTicksAtBottomSize: float
    SmallTicksAtMiddleSize: float
    SmallTicksAtTopSize: float
    IncrementSmallTicksAtBottom: bool
    IncrementSmallTicksAtMiddle: bool
    IncrementSmallTicksAtTop: bool
    IncrementTicksToFullHeight: bool

class BandTitleBoxPosition:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.BandTitleBoxPosition"""
    def __init__(self, *args) -> None: ...
    LeftOfBand: int  # = 0
    RightOfBand: int  # = 1
class BandTitleTextLocation:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.BandTitleTextLocation"""
    def __init__(self, *args) -> None: ...
    Right: int  # = 0
    Center: int  # = 1
    Left: int  # = 2
class BaseLabelSetItem(CivilWrapper<AeccDbAlignStnLabelsDlgTemplate>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.BaseLabelSetItem"""
    def __init__(self, *args) -> None: ...
    LabelStyleName: str
    LabelStyleId: ObjectId
    LabelStyleType: LabelStyleType

class BaseLabelSetStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.BaseLabelSetStyle"""
    def __init__(self, *args) -> None: ...
    Count: int
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def Add(self, majorStation: BaseLabelSetItem, minorStationLabelStyleName: str) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class BuildingSiteDisplayStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.BuildingSiteDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    BuildingFootprint: int  # = 0
    PropertyLines: int  # = 1
    Utilities: int  # = 2
    SiteModel: int  # = 3
    BuildingModel: int  # = 4
class BuildingSiteStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.BuildingSiteStyle"""
    def __init__(self, *args) -> None: ...
    MarkerStyleName: str
    MarkerStyleId: ObjectId
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStyleModel(self, type: BuildingSiteDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, type: BuildingSiteDisplayStyleType) -> DisplayStyle: ...

class BuildingSiteStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.BuildingSiteStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class CantViewStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.CantViewStyle"""
    def __init__(self, *args) -> None: ...
    UseSmallTicksAtBottom: bool
    UseSmallTicksAtMiddle: bool
    UseSmallTicksAtTop: bool
    UseFullHeightTick: bool
    AxisBottomMajorTickInterval: float
    AxisTopMajorTickInterval: float
    VerticalExaggeration: float
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStylePlan(self, type: CantViewDisplayStyleType) -> DisplayStyle: ...

class CantViewStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.CantViewStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class CatchmentDisplayStylePlanType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.CatchmentDisplayStylePlanType"""
    def __init__(self, *args) -> None: ...
    CatchmentBoundary: int  # = 0
    CatchmentFlowPath: int  # = 1
class CatchmentStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.CatchmentStyle"""
    def __init__(self, *args) -> None: ...
    FlowSegmentStartPointMarkerStyle: ObjectId
    MostDistantPointMarkerStyle: ObjectId
    DischargePointMarkerStyle: ObjectId
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStylePlan(self, type: CatchmentDisplayStylePlanType) -> DisplayStyle: ...

class CatchmentStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.CatchmentStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class CenterMarkerSizeType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.CenterMarkerSizeType"""
    def __init__(self, *args) -> None: ...
    PercentageOfScreen: int  # = 0
    Plotted: int  # = 1
    Fixed: int  # = 2
class CodeSetStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.CodeSetStyle"""
    def __init__(self, *args) -> None: ...
    SubentityStyleType: SubassemblySubentityStyleType
    Item: CodeSetStyleItem
    Count: int
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def Add(self, code: str, styleId: ObjectId) -> CodeSetStyleItem: ...
    @staticmethod
    def GetCurrentStyleSetId() -> ObjectId: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetItemBy(self, itemType: CodeSetStyleItemType, code: str) -> CodeSetStyleItem: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Remove(self, code: str) -> None: ...

class CodeSetStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.CodeSetStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class CodeSetStyleItem(CivilWrapper<AeccDbRoadwayStyleSet>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.CodeSetStyleItem"""
    def __init__(self, *args) -> None: ...
    PayItems: list
    RenderMaterialStyleName: str
    RenderMaterialStyleId: ObjectId
    MaterialAreaFillStyleName: str
    MaterialAreaFillStyleId: ObjectId
    FeatureLineStyleName: str
    FeatureLineStyleId: ObjectId
    LabelStyleName: str
    LabelStyleId: ObjectId
    ItemType: CodeSetStyleItemType
    StyleType: SubassemblySubentityStyleType
    Description: str
    Classification: str
    CodeStyleName: str
    CodeStyleId: ObjectId
    Code: str

class CodeSetStyleItemType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.CodeSetStyleItemType"""
    def __init__(self, *args) -> None: ...
    NormalItemType: int  # = 0
    DefaultItemType: int  # = 1
    NoCodeItemType: int  # = 2
class ColorSchemeType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.ColorSchemeType"""
    def __init__(self, *args) -> None: ...
    Blues: int  # = 0
    Greens: int  # = 1
    Hydro: int  # = 2
    Land: int  # = 3
    Pastels: int  # = 4
    Rainbow: int  # = 5
    Reds: int  # = 6
class ColumnStyle(CivilWrapper<AeccDbScheduleTableStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ColumnStyle"""
    def __init__(self, *args) -> None: ...
    ContentJustification: TextJustificationType
    ContentStringFormatted: str
    ContentString: str
    HeaderJustification: TextJustificationType
    HeaderStringFormatted: str
    HeaderString: str
    ColumnWidth: float

class ColumnStyleCollection(CivilWrapper<AeccDbScheduleTableStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ColumnStyleCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: ColumnStyle
    def Add(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def RemoveAt(self, index: int) -> None: ...

class ContourSmoothingType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.ContourSmoothingType"""
    def __init__(self, *args) -> None: ...
    AddVertices: int  # = 0
    SplineCurve: int  # = 1
class ContourValues:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ContourValues"""
    def __init__(self, *args) -> None: ...
    MinorLineWeight: LineWeight
    MajorLineWeight: LineWeight
    MinorLineTypeId: ObjectId
    MajorLineTypeId: ObjectId
    MinorColor: Color
    MajorColor: Color

class CorridorDisplayStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.CorridorDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    RegionBoundaries: int  # = 0
    ParameterOverrideStations: int  # = 1
    GeometricOverrideStations: int  # = 2
    AssemblyInsertionStations: int  # = 3
class CorridorStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.CorridorStyle"""
    def __init__(self, *args) -> None: ...
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStyleModel(self, type: CorridorDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, type: CorridorDisplayStyleType) -> DisplayStyle: ...

class CorridorStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.CorridorStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class CustomMarkerSuperimposeType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.CustomMarkerSuperimposeType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Square: int  # = 1
    Circle: int  # = 2
    SquareCircle: int  # = 3
class CustomMarkerType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.CustomMarkerType"""
    def __init__(self, *args) -> None: ...
    CustomMarkerDot: int  # = 0
    CustomMarkerBlank: int  # = 1
    CustomMarkerPlus: int  # = 2
    CustomMarkerX: int  # = 3
    CustomMarkerVLine: int  # = 4
class DataBandingType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.DataBandingType"""
    def __init__(self, *args) -> None: ...
    NumberOfRanges: int  # = 0
    RangesInterval: int  # = 1
    RangesIntervalWithDatum: int  # = 2
class DataPartFamily:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.DataPartFamily"""
    def __init__(self, *args) -> None: ...
    SweptShape: SweptShapeType
    BoundingShape: BoundingShapeType
    Domain: DomainType
    PartType: PartType
    GUID: str
    Description: str

class DisplayStyle(CivilWrapper<AeccDbStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.DisplayStyle"""
    def __init__(self, *args) -> None: ...
    Color: Color
    PlotStyle: str
    LinetypeScale: float
    Lineweight: LineWeight
    Linetype: str
    Layer: str
    Visible: bool

class Expression:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.Expression"""
    def __init__(self, *args) -> None: ...
    FormatResultAs: ExpressionFormatedType
    ReferenceString: str
    ExpressionString: str
    Description: str
    Name: str

class ExpressionCollection:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ExpressionCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: Expression
    Item: Expression
    def Add(self, name: str, description: str, expression: str) -> Expression: ...
    def Clear(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def RemoveAt(self, index: int) -> None: ...

class ExpressionFormatedType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.ExpressionFormatedType"""
    def __init__(self, *args) -> None: ...
    Angle: int  # = 0
    Area: int  # = 1
    Azimuth: int  # = 2
    Coordinate: int  # = 3
    Dimension: int  # = 4
    Direction: int  # = 5
    Distance: int  # = 6
    Double: int  # = 7
    Elevation: int  # = 8
    GradeSlope: int  # = 9
    Latitude: int  # = 10
    Longitude: int  # = 11
    Percent: int  # = 12
    Station: int  # = 13
    Volume: int  # = 14
class FeatureLineDisplayStyleProfileType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.FeatureLineDisplayStyleProfileType"""
    def __init__(self, *args) -> None: ...
    FeatureLine: int  # = 0
    BeginningVertex: int  # = 2
    InternalVertex: int  # = 3
    EndingVertex: int  # = 4
class FeatureLineStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.FeatureLineStyle"""
    def __init__(self, *args) -> None: ...
    ProfileEndingVertexMarkerStyleName: str
    ProfileEndingVertexMarkerStyleId: ObjectId
    ProfileInternalVertexMarkerStyleName: str
    ProfileInternalVertexMarkerStyleId: ObjectId
    ProfileBeginningVertexMarkerStyleName: str
    ProfileBeginningVertexMarkerStyleId: ObjectId
    SectionMarkerStyleName: str
    SectionMarkerStyleId: ObjectId
    SectionMarkerDisplayStyleSection: DisplayStyle
    FeatureLineDisplayStyleModel: DisplayStyle
    FeatureLineDisplayStylePlan: DisplayStyle
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStyleProfile(self, type: FeatureLineDisplayStyleProfileType) -> DisplayStyle: ...
    def GetFeatureLineDisplayStyleModel(self, ) -> DisplayStyle: ...
    def GetFeatureLineDisplayStylePlan(self, ) -> DisplayStyle: ...
    def GetSectionMarkerDisplayStyleSection(self, ) -> DisplayStyle: ...

class FeatureLineStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.FeatureLineStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class GradingCriteria(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GradingCriteria"""
    def __init__(self, *args) -> None: ...
    InteriorCornerOverlap: PropertyEnum
    Slope: PropertyDouble
    SlopeFormatType: PropertyEnum
    FillSlope: PropertyDouble
    FillSlopeFormatType: PropertyEnum
    CutSlope: PropertyDouble
    CutSlopeFormatType: PropertyEnum
    ProjectionDistance: PropertyDouble
    Distance: PropertyDouble
    Elevation: PropertyDouble
    RelativeElevation: PropertyDouble
    ProjectionRelativeElevation: PropertyDouble
    SearchOrder: PropertyEnum
    DistanceProjectionType: GradingDistanceProjectionType
    RelativeElevationProjectionType: GradingRelativeElevationProjectionType
    ElevationProjectionType: GradingElevationProjectionType
    SurfaceProjectionType: GradingSurfaceProjectionType
    Target: GradingTargetType
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def CopyAsSibling(self, criteriaName: str) -> ObjectId: ...

class GradingCriteriaSet(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GradingCriteriaSet"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def AddCriteria(self, criteriaName: str) -> None: ...
    def GradingCriteriaIds(self, ) -> ObjectIdCollection: ...
    def MoveCriteria(self, criteriaName: str, criteriaSetName: str) -> None: ...
    def RemoveCriteria(self, index: int) -> None: ...

class GradingCriteriaSetCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GradingCriteriaSetCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class GradingDisplayStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.GradingDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    CentroidMarker: int  # = 0
    TargetLine: int  # = 1
    Projection: int  # = 2
    InternalEdges: int  # = 3
    SolidShading: int  # = 4
    SlopePat: int  # = 5
class GradingStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GradingStyle"""
    def __init__(self, *args) -> None: ...
    SlopeRangeMax: float
    SlopeRangeMin: float
    UseSlopeRange: bool
    SlopePatternStyleName: str
    SlopePatternStyleId: ObjectId
    UseSlopePatternStyle: bool
    FixedSize: float
    PlottedSize: float
    PercentageOfScreen: float
    CenterMarker: CenterMarkerSizeType
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStyleModel(self, type: GradingDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, type: GradingDisplayStyleType) -> DisplayStyle: ...

class GradingStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GradingStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...
    def SetCenterMarkerVisable(self, isVisable: bool) -> None: ...
    def SetSlopePatternVisable(self, isVisable: bool) -> None: ...

class GraphDirectionType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.GraphDirectionType"""
    def __init__(self, *args) -> None: ...
    LeftToRight: int  # = 0
    RightToLeft: int  # = 1
class GraphStyle(CivilWrapper<AeccDbGraphStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GraphStyle"""
    def __init__(self, *args) -> None: ...
    TitleStyle: GraphTitleStyle
    Direction: GraphDirectionType
    VerticalExaggeration: float
    CurrentHorizontalScale: float
    VerticalScale: float

class GraphTitleJustificationType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.GraphTitleJustificationType"""
    def __init__(self, *args) -> None: ...
    TopOrLeft: int  # = 0
    MiddleOrCenter: int  # = 1
    BottomOrRight: int  # = 2
class GraphTitleLocationType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.GraphTitleLocationType"""
    def __init__(self, *args) -> None: ...
    Top: int  # = 0
    Bottom: int  # = 1
    Left: int  # = 2
    Right: int  # = 3
class GraphTitleStyle(CivilWrapper<AeccDbGraphStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GraphTitleStyle"""
    def __init__(self, *args) -> None: ...
    BorderGap: float
    Border: bool
    OffsetY: float
    OffsetX: float
    Justification: GraphTitleJustificationType
    Location: GraphTitleLocationType
    TextHeight: float
    TextStyle: str
    Text: str

class GridOptions(CivilWrapper<AeccDbGraphStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GridOptions"""
    def __init__(self, *args) -> None: ...
    OmitGridInPaddingAreas: bool
    ClipToHighestProfile: bool
    UseClipGrid: bool

class GridStyle(CivilWrapper<AeccDbGraphStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GridStyle"""
    def __init__(self, *args) -> None: ...
    AxisOffsetRight: float
    AxisOffsetLeft: float
    AxisOffsetBottom: float
    AxisOffsetAbove: float
    GridPaddingRight: float
    GridPaddingLeft: float
    GridPaddingBottom: float
    GridPaddingAbove: float
    HorizontalGridOptions: GridOptions
    VerticalGridOptions: GridOptions

class GridType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.GridType"""
    def __init__(self, *args) -> None: ...
    Vertical: int  # = 0
    Horizontal: int  # = 1
class GroupPlotAlignType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.GroupPlotAlignType"""
    def __init__(self, *args) -> None: ...
    Left: int  # = 0
    Centerline: int  # = 1
    Right: int  # = 2
class GroupPlotCellSizeType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.GroupPlotCellSizeType"""
    def __init__(self, *args) -> None: ...
    UniformForAll: int  # = 0
    UniformPerRowOrColumn: int  # = 1
class GroupPlotDisplayStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.GroupPlotDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    MajorHorizontalGrid: int  # = 0
    MinorHorizontalGrid: int  # = 1
    MajorVerticalGrid: int  # = 2
    MinorVerticalGrid: int  # = 3
    PrintArea: int  # = 4
    Border: int  # = 5
class GroupPlotStartCornerType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.GroupPlotStartCornerType"""
    def __init__(self, *args) -> None: ...
    LowerLeft: int  # = 0
    UpperLeft: int  # = 1
    LowerRight: int  # = 2
    UpperRight: int  # = 3
class GroupPlotStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GroupPlotStyle"""
    def __init__(self, *args) -> None: ...
    GridVerticalMinor: float
    GridVerticalMajor: float
    GridHorizontalMinor: float
    GridHorizontalMajor: float
    GapBetweenPages: float
    SpaceRow: float
    SpaceColumn: float
    CellSizeType: GroupPlotCellSizeType
    AlignType: GroupPlotAlignType
    StartCorner: GroupPlotStartCornerType
    MaximumInColumn: int
    MaximumInRow: int
    PlotRule: SectionViewPlotRuleType
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayPlan(self, type: GroupPlotDisplayStyleType) -> DisplayStyle: ...

class GroupPlotStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.GroupPlotStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class HatchDisplayStyle(CivilWrapper<AeccDbStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.HatchDisplayStyle"""
    def __init__(self, *args) -> None: ...
    IsDoubleHatch: bool
    VOffset: float
    UOffset: float
    Spacing: float
    UseAngleOfObject: bool
    Angle: float
    ScaleFactor: float
    Pattern: str
    HatchType: HatchType

class HatchType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.HatchType"""
    def __init__(self, *args) -> None: ...
    UserDefined: int  # = 0
    PreDefined: int  # = 1
    CustomDefined: int  # = 2
    SolidFill: int  # = 3
class HorizontalGeometryBandStyle(BandStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.HorizontalGeometryBandStyle"""
    def __init__(self, *args) -> None: ...
    PointOfIntersectionTickStyle: BandTickStyle
    SpiralTickStyle: BandTickStyle
    CurveTickStyle: BandTickStyle
    TangentTickStyle: BandTickStyle
    PointOfIntersectionLabelStyleId: ObjectId
    SpiralLabelStyleId: ObjectId
    CurveLabelStyleId: ObjectId
    TangentLabelStyleId: ObjectId
    SchematicLineType: SchematicLineOption
    TitleTextLabelStyleId: ObjectId
    BandType: BandType
    WeedingFactor: float
    TextHeight: float
    TextLocation: BandTitleTextLocation
    TextBoxPosition: BandTitleBoxPosition
    OffsetFromBand: float
    TextBoxWidth: float
    BandHeight: float
    Text: str
    TextStyle: str
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStylePlan(self, type: HorizontalGeometryDisplayStyleType) -> DisplayStyle: ...

class HorizontalGeometryDisplayStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.HorizontalGeometryDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    Border: int  # = 0
    TitleBox: int  # = 1
    TitleBoxText: int  # = 2
    Ticks: int  # = 3
    TangentLabels: int  # = 4
    CurveLabels: int  # = 5
    SpiralLabels: int  # = 6
    TangentGeometry: int  # = 7
    CurveGeometry: int  # = 8
    SpiralGeometry: int  # = 9
    TicksAtPI: int  # = 13
    PILabels: int  # = 14
class InterferenceDisplayStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.InterferenceDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    Symbol: int  # = 0
    Solid: int  # = 1
class InterferenceModelSizeOptionType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.InterferenceModelSizeOptionType"""
    def __init__(self, *args) -> None: ...
    UseAbsoluteUnits: int  # = 0
    UseDrawingUnits: int  # = 1
class InterferenceModelSizeType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.InterferenceModelSizeType"""
    def __init__(self, *args) -> None: ...
    SolidExtents: int  # = 0
    UserSpecified: int  # = 1
class InterferenceModelType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.InterferenceModelType"""
    def __init__(self, *args) -> None: ...
    TrueSolid: int  # = 0
    Sphere: int  # = 1
class InterferenceStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.InterferenceStyle"""
    def __init__(self, *args) -> None: ...
    DrawingScaleModelSize: float
    AbsoluteModelSize: float
    ModelSizeOptions: InterferenceModelSizeOptionType
    ModelSizeType: InterferenceModelSizeType
    ModelOptions: InterferenceModelType
    MarkerStyle: ObjectId
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStyleModel(self, component: InterferenceDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, component: InterferenceDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStyleSection(self, component: InterferenceDisplayStyleType) -> DisplayStyle: ...

class InterferenceStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.InterferenceStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class IntersectionStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.IntersectionStyle"""
    def __init__(self, *args) -> None: ...
    MarkerStyleId: ObjectId
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStyleModel(self, ) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, ) -> DisplayStyle: ...

class IntersectionStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.IntersectionStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class LabelDisplayModeType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.LabelDisplayModeType"""
    def __init__(self, *args) -> None: ...
    Label: int  # = 0
    Tag: int  # = 1
class LabelSetStylesRoot(TreeOidWrapper):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelSetStylesRoot"""
    def __init__(self, *args) -> None: ...
    SectionLabelSetStyles: SectionLabelSetStyleCollection
    ProfileLabelSetStyles: ProfileLabelSetStyleCollection
    AlignmentLabelSetStyles: AlignmentLabelSetStyleCollection
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStyle"""
    def __init__(self, *args) -> None: ...
    ChildrenCount: int
    Item: ObjectId
    Item: ObjectId
    ParentLabelStyleId: ObjectId
    Properties: LabelStyleBase
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def AddChild(self, labelStyleName: str) -> ObjectId: ...
    def AddComponent(self, name: str, type: LabelStyleComponentType) -> ObjectId: ...
    def AddReferenceTextComponent(self, name: str, selectedType: ReferenceTextComponentSelectedType) -> ObjectId: ...
    def AddTextForEachComponent(self, name: str, selectedType: TextForEachComponentSelectedType) -> ObjectId: ...
    def GetComponents(self, type: LabelStyleComponentType) -> ObjectIdCollection: ...
    def GetComponentsCount(self, type: LabelStyleComponentType) -> int: ...
    def GetComponentsDrawOrder(self, ) -> list: ...
    def GetDescendantIds(self, ) -> ObjectIdCollection: ...
    def IsSupportedComponent(self, type: LabelStyleComponentType) -> bool: ...
    def RemoveAllDescendants(self, ) -> None: ...
    def RemoveChild(self, index: int) -> None: ...
    def RemoveComponent(self, name: str) -> None: ...
    def SetComponentsDrawOrder(self, componentIds: list) -> None: ...
    def SwitchComponentsDrawOrder(self, index1: int, index2: int) -> None: ...

class LabelStyleBase(CivilWrapper<AeccDbLabelStyleCollector>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStyleBase"""
    def __init__(self, *args) -> None: ...
    DraggedStateComponents: BaseDraggedStateComponents
    Leader: BaseLeader
    PlanReadability: BasePlanReadability
    Behavior: BaseBehavior
    Label: BaseLabel

class LabelStyleBlockComponent(LabelStyleComponent):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStyleBlockComponent"""
    def __init__(self, *args) -> None: ...
    Block: StyleBlock
    General: StyleGeneral
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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

class LabelStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStyleCollection"""
    def __init__(self, *args) -> None: ...
    Expressions: ExpressionCollection
    DefaultLabelStyle: LabelStyleDefault
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...
    def GetDescendantIds(self, ) -> ObjectIdCollection: ...
    def Remove(self, styleName: str) -> None: ...

class LabelStyleComponent(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStyleComponent"""
    def __init__(self, *args) -> None: ...
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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

class LabelStyleComponentType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.LabelStyleComponentType"""
    def __init__(self, *args) -> None: ...
    Text: int  # = 1
    Line: int  # = 2
    Block: int  # = 4
    Tick: int  # = 8
    ReferenceText: int  # = 16
    DirectionArrow: int  # = 32
    TextForEach: int  # = 64
class LabelStyleDefault(TreeOidWrapper):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStyleDefault"""
    def __init__(self, *args) -> None: ...
    DraggedStateComponents: DefaultDraggedStateComponents
    Leader: DefaultLeader
    Components: DefaultComponents
    PlanReadability: DefaultPlanReadability
    Behavior: DefaultBehavior
    Label: DefaultLabel
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStyleDirectionArrowComponent(LabelStyleComponent):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStyleDirectionArrowComponent"""
    def __init__(self, *args) -> None: ...
    DirectionArrow: StyleDirectionArrow
    General: StyleGeneral
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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

class LabelStyleLineComponent(LabelStyleComponent):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStyleLineComponent"""
    def __init__(self, *args) -> None: ...
    Line: StyleLine
    General: StyleGeneral
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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

class LabelStyleReferenceTextComponent(LabelStyleComponent):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStyleReferenceTextComponent"""
    def __init__(self, *args) -> None: ...
    Border: StyleBorder
    Text: StyleText
    General: StyleGeneral
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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

class LabelStyleTextComponent(LabelStyleComponent):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStyleTextComponent"""
    def __init__(self, *args) -> None: ...
    Border: StyleBorder
    Text: StyleText
    General: StyleGeneral
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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

class LabelStyleTextForEachComponent(LabelStyleComponent):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStyleTextForEachComponent"""
    def __init__(self, *args) -> None: ...
    Border: StyleBorder
    Text: StyleText
    General: StyleGeneral
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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

class LabelStyleTickComponent(LabelStyleComponent):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStyleTickComponent"""
    def __init__(self, *args) -> None: ...
    Tick: StyleTick
    General: StyleGeneral
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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

class LabelStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.LabelStyleType"""
    def __init__(self, *args) -> None: ...
    AlignmentMajorStation: int  # = 251704321
    AlignmentMinorStation: int  # = 251704322
    AlignmentGeometryPoint: int  # = 251704323
    AlignmentStationEquation: int  # = 251704324
    AlignmentDesignSpeed: int  # = 251704325
    AlignmentStationOffset: int  # = 251704326
    AlignmentTangentIntersection: int  # = 251704327
    AlignmentLine: int  # = 251704328
    AlignmentSpiral: int  # = 251704329
    AlignmentCurve: int  # = 251704330
    AlignmentSuperelevationCriticalPoints: int  # = 251704331
    ProfileMajorStation: int  # = 251704333
    ProfileMinorStation: int  # = 251704334
    ProfileHorizontalGeometryPoint: int  # = 251704335
    ProfileLine: int  # = 251704338
    ProfileCurve: int  # = 251704339
    ProfileGradeBreaks: int  # = 251704340
    ProfileSagCurve: int  # = 251704341
    ProfileCrestCurve: int  # = 251704342
    ProfileViewStationElevation: int  # = 251704346
    ProfileViewDepth: int  # = 251704347
    SurfaceContour: int  # = 251704366
    SurfaceSlope: int  # = 251704367
    SurfaceSpotElevation: int  # = 251704369
    ParcelArea: int  # = 251704370
    ParcelLine: int  # = 251704371
    ParcelCurve: int  # = 251704372
    GeneralNote: int  # = 251704374
    GeneralLine: int  # = 251704375
    GeneralCurve: int  # = 251704376
    PipePlanProfile: int  # = 251704379
    StructureLabelStyle: int  # = 251704380
    SurfaceWatershed: int  # = 251704397
    SectionMajorOffset: int  # = 251704399
    SectionMinorOffset: int  # = 251704400
    SectionGradeBreak: int  # = 251704401
    SectionSegment: int  # = 251704402
    SectionViewOffsetElevation: int  # = 251704403
    SectionViewGrade: int  # = 251704404
    GeneralLink: int  # = 251704406
    GeneralMarker: int  # = 251704407
    GeneralShape: int  # = 251704408
    PipeCrossSection: int  # = 251704412
    ViewFrame: int  # = 251704607
    MatchLineLeft: int  # = 251704608
    MatchLineRight: int  # = 251704609
    ProfileViewProjection: int  # = 251704694
    SectionViewProjection: int  # = 251704695
    IntersectionLocationLabels: int  # = 251704697
    CatchmentArea: int  # = 251704720
    CatchmentFlowSegment: int  # = 251704721
    PressurePipe: int  # = 251704725
    Fitting: int  # = 251704726
    Appurtenance: int  # = 251704727
    SectionCorridorPoint: int  # = 251704729
    AlignmentProfileGeometryPoint: int  # = 251704832
    AlignmentPointOfIntersection: int  # = 251704833
    Point: int  # = 268481548
    ProfileBandMajorIncrement: int  # = 268546560
    ProfileBandMinorIncrement: int  # = 268546576
    ProfileBandHGP: int  # = 268546592
    ProfileBandVGP: int  # = 268546608
    ProfileBandStationEquation: int  # = 268546624
    ProfileBandIncrementalDistance: int  # = 268546640
    ProfileBandVerticalGeometryUphillTangent: int  # = 268546816
    ProfileBandVerticalGeometryDownhillTangent: int  # = 268546832
    ProfileBandVerticalGeometryCrestCurve: int  # = 268546848
    ProfileBandVerticalGeometrySagCurve: int  # = 268546864
    ProfileBandHorizontalGeometryTangent: int  # = 268547072
    ProfileBandHorizontalGeometryCurve: int  # = 268547088
    ProfileBandHorizontalGeometrySpiral: int  # = 268547104
    ProfileBandHorizontalGeometryPointOfIntersection: int  # = 268547120
    ProfileBandSuperelevationDataNormalCrown: int  # = 268547328
    ProfileBandSuperelevationDataReverseCrown: int  # = 268547360
    ProfileBandSuperelevationDataFullSuper: int  # = 268547376
    ProfileBandSuperelevationDataLevelCrown: int  # = 268547392
    ProfileBandSuperelevationDataSlopeTransition: int  # = 268547408
    ProfileBandSuperelevationDataShoulderCritical: int  # = 268547616
    ProfileBandPipeNetworkStructureLocation: int  # = 268547632
    ProfileBandPipeNetworkPipeLocation: int  # = 268547648
    ProfileBandSectionalDataSampleLineLocation: int  # = 268547664
    ProfileBandSectionalDataIncrementalSectionData: int  # = 268547680
    SectionBandMajorIncrement: int  # = 268562944
    SectionBandMinorIncrement: int  # = 268562960
    SectionBandCenterline: int  # = 268562976
    SectionBandSampleLineVertices: int  # = 268562992
    SectionBandGradeBreaks: int  # = 268563008
    SectionBandIncrementalDistance: int  # = 268563024
    SectionBandSegmentSurfaceLabels: int  # = 268563200
    SampleLineLabelStyles: int  # = 268607503
class LabelStylesAlignmentRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesAlignmentRoot"""
    def __init__(self, *args) -> None: ...
    PointOfIntersectionLabelStyles: LabelStyleCollection
    VerticalGeometryPointLabelStyles: LabelStyleCollection
    CantCriticalPointsLabelStyles: LabelStyleCollection
    SuperelevationCriticalPointsLabelStyles: LabelStyleCollection
    TangentIntersectionLabelStyles: LabelStyleCollection
    StationOffsetLabelStyles: LabelStyleCollection
    StationEquationLabelStyles: LabelStyleCollection
    SpiralLabelStyles: LabelStyleCollection
    MinorStationLabelStyles: LabelStyleCollection
    MajorStationLabelStyles: LabelStyleCollection
    LineLabelStyles: LabelStyleCollection
    GeometryPointLabelStyles: LabelStyleCollection
    DesignSpeedLabelStyles: LabelStyleCollection
    CurveLabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesCatchmentRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesCatchmentRoot"""
    def __init__(self, *args) -> None: ...
    FlowSegmentLabelStyles: LabelStyleCollection
    AreaLabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesIntersectionRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesIntersectionRoot"""
    def __init__(self, *args) -> None: ...
    LocationLabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesMatchLineRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesMatchLineRoot"""
    def __init__(self, *args) -> None: ...
    RightLabelStyles: LabelStyleCollection
    LeftLabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesNode(TreeOidWrapper):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesNode"""
    def __init__(self, *args) -> None: ...
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesParcelRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesParcelRoot"""
    def __init__(self, *args) -> None: ...
    LineLabelStyles: LabelStyleCollection
    AreaLabelStyles: LabelStyleCollection
    CurveLabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesPipeRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesPipeRoot"""
    def __init__(self, *args) -> None: ...
    CrossProfileLabelStyles: LabelStyleCollection
    CrossSectionLabelStyles: LabelStyleCollection
    PlanProfileLabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesPointRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesPointRoot"""
    def __init__(self, *args) -> None: ...
    LabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesProfileRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesProfileRoot"""
    def __init__(self, *args) -> None: ...
    MinorStationLabelStyles: LabelStyleCollection
    MajorStationLabelStyles: LabelStyleCollection
    LineLabelStyles: LabelStyleCollection
    HorizontalGeometryPointLabelStyles: LabelStyleCollection
    GradeBreakLabelStyles: LabelStyleCollection
    GradeBreadLabelStyles: LabelStyleCollection
    CurveLabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesProfileViewRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesProfileViewRoot"""
    def __init__(self, *args) -> None: ...
    StationElevationLabelStyles: LabelStyleCollection
    DepthLabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesProjectionRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesProjectionRoot"""
    def __init__(self, *args) -> None: ...
    SectionViewProjectionLabelStyles: LabelStyleCollection
    ProfileViewProjectionLabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesRoot"""
    def __init__(self, *args) -> None: ...
    GeneralShapeLabelStyles: LabelStyleCollection
    GeneralLinkLabelStyles: LabelStyleCollection
    GeneralMarkerLabelStyles: LabelStyleCollection
    GeneralCurveLabelStyles: LabelStyleCollection
    GeneralLineLabelStyles: LabelStyleCollection
    GeneralNoteLabelStyles: LabelStyleCollection
    ProjectionLabelStyles: LabelStylesProjectionRoot
    PointLabelStyles: LabelStylesPointRoot
    MatchLineLabelStyles: LabelStylesMatchLineRoot
    ViewFrameLabelStyles: LabelStylesViewFrameRoot
    IntersectionLabelStyles: LabelStylesIntersectionRoot
    SampleLineLabelStyles: LabelStylesSampleLineRoot
    SectionViewLabelStyles: LabelStylesSectionViewRoot
    CatchmentLabelStyles: LabelStylesCatchmentRoot
    StructureLabelStyles: LabelStylesStructureRoot
    PipeLabelStyles: LabelStylesPipeRoot
    SectionLabelStyles: LabelStylesSectionRoot
    ProfileViewLabelStyles: LabelStylesProfileViewRoot
    ProfileLabelStyles: LabelStylesProfileRoot
    ParcelLabelStyles: LabelStylesParcelRoot
    SurfaceLabelStyles: LabelStylesSurfaceRoot
    AlignmentLabelStyles: LabelStylesAlignmentRoot
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetSurveyLabelStyles(self, ) -> LabelStylesSurveyRoot: ...

class LabelStylesSampleLineRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesSampleLineRoot"""
    def __init__(self, *args) -> None: ...
    LabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesSectionRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesSectionRoot"""
    def __init__(self, *args) -> None: ...
    CorridorPointLabelStyles: LabelStyleCollection
    SegmentLabelStyles: LabelStyleCollection
    MinorOffsetLabelStyles: LabelStyleCollection
    MajorOffsetLabelStyles: LabelStyleCollection
    GradeBreakLabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesSectionViewRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesSectionViewRoot"""
    def __init__(self, *args) -> None: ...
    OffsetElevationLabelStyles: LabelStyleCollection
    GradeLabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesStructureRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesStructureRoot"""
    def __init__(self, *args) -> None: ...
    LabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesSurfaceRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesSurfaceRoot"""
    def __init__(self, *args) -> None: ...
    WatershedLabelStyles: LabelStyleCollection
    SpotElevationLabelStyles: LabelStyleCollection
    SlopeLabelStyles: LabelStyleCollection
    ContourLabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesSurveyRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesSurveyRoot"""
    def __init__(self, *args) -> None: ...
    LineLabelStyles: LabelStyleCollection
    FigureLabelStyles: LabelStyleCollection
    CurveLabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LabelStylesViewFrameRoot(LabelStylesNode):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LabelStylesViewFrameRoot"""
    def __init__(self, *args) -> None: ...
    LabelStyles: LabelStyleCollection
    DefaultLabelStyle: LabelStyleDefault
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class LinkStyle(SubassemblySubentityStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LinkStyle"""
    def __init__(self, *args) -> None: ...
    StyleType: SubassemblySubentityStyleType
    LinkDisplayStyleModel: DisplayStyle
    LinkDisplayStylePlan: DisplayStyle
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStyleModel(self, ) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, ) -> DisplayStyle: ...
    def GetDisplayStyleSection(self, ) -> DisplayStyle: ...
    def GetLinkDisplayStyleModel(self, ) -> DisplayStyle: ...
    def GetLinkDisplayStylePlan(self, ) -> DisplayStyle: ...

class LinkStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.LinkStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class MarkerDisplayType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.MarkerDisplayType"""
    def __init__(self, *args) -> None: ...
    UsePointForMarker: int  # = 0
    UseCustomMarker: int  # = 1
    UseSymbolForMarker: int  # = 2
    UseVerticalLineForMarker: int  # = 3
class MarkerOrientationType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.MarkerOrientationType"""
    def __init__(self, *args) -> None: ...
    OrientToObject: int  # = 0
    OrientToWCS: int  # = 1
    OrientToView: int  # = 2
class MarkerSizeType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.MarkerSizeType"""
    def __init__(self, *args) -> None: ...
    DrawingScale: int  # = 0
    RelativeToScreen: int  # = 1
    AbsoluteUnits: int  # = 2
    FixedScale: int  # = 3
class MarkerStyle(MarkerStyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.MarkerStyle"""
    def __init__(self, *args) -> None: ...
    MarkerDisplayStyleSection: DisplayStyle
    MarkerDisplayStyleProfile: DisplayStyle
    MarkerType: MarkerDisplayType
    MarkerDisplayStyleModel: DisplayStyle
    MarkerDisplayStylePlan: DisplayStyle
    Orientation: MarkerOrientationType
    MarkerFixedScale: Point3d
    MarkerSize: float
    SizeType: MarkerSizeType
    MarkerRotationAngle: float
    MarkerSymbolName: str
    CustomMarkerSuperimposeStyle: CustomMarkerSuperimposeType
    CustomMarkerStyle: CustomMarkerType
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetMarkerDisplayStyleProfile(self, ) -> DisplayStyle: ...
    def GetMarkerDisplayStyleSection(self, ) -> DisplayStyle: ...

class MarkerStyleBase(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.MarkerStyleBase"""
    def __init__(self, *args) -> None: ...
    MarkerDisplayStyleModel: DisplayStyle
    MarkerDisplayStylePlan: DisplayStyle
    Orientation: MarkerOrientationType
    MarkerFixedScale: Point3d
    MarkerSize: float
    SizeType: MarkerSizeType
    MarkerRotationAngle: float
    MarkerSymbolName: str
    CustomMarkerSuperimposeStyle: CustomMarkerSuperimposeType
    CustomMarkerStyle: CustomMarkerType
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetMarkerDisplayStyleModel(self, ) -> DisplayStyle: ...
    def GetMarkerDisplayStylePlan(self, ) -> DisplayStyle: ...

class MarkerStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.MarkerStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class MassHaulLineStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.MassHaulLineStyle"""
    def __init__(self, *args) -> None: ...
    FreeHaulOption: FreeHaulDisplayType
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStyleProfile(self, type: MassHaulLineDisplayStyleType) -> DisplayStyle: ...
    def GetHatchDisplayStyleProfile(self, type: MassHaulLineHatchDisplayStyleType) -> HatchDisplayStyle: ...

class MassHaulLineStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.MassHaulLineStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class MassHaulViewStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.MassHaulViewStyle"""
    def __init__(self, *args) -> None: ...
    RightAxis: AxisStyle
    LeftAxis: AxisStyle
    BottomAxis: AxisStyle
    MiddleAxis: AxisStyle
    TopAxis: AxisStyle
    GridStyle: GridStyle
    GraphStyle: GraphStyle
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStylePlan(self, type: MassHaulViewDisplayStyleType) -> DisplayStyle: ...

class MassHaulViewStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.MassHaulViewStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class MatchLineStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.MatchLineStyle"""
    def __init__(self, *args) -> None: ...
    MatchLineMaskHatchDisplayStyle: HatchDisplayStyle
    MatchLineMaskDisplayStylePlan: DisplayStyle
    LinesDisplayStylePlan: DisplayStyle
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetLinesDisplayStylePlan(self, ) -> DisplayStyle: ...
    def GetMatchLineMaskDisplayStylePlan(self, ) -> DisplayStyle: ...
    def GetMatchLineMaskHatchDisplayStyle(self, ) -> HatchDisplayStyle: ...

class MatchLineStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.MatchLineStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class NetworkRuleSetStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.NetworkRuleSetStyle"""
    def __init__(self, *args) -> None: ...
    RulesCount: int
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def CloneAndAddRule(self, sourceRuleId: ObjectId) -> None: ...
    def GetRuleIds(self, ) -> ObjectIdCollection: ...
    def RemoveAllRules(self, ) -> None: ...
    def RemoveRule(self, ruleId: ObjectId) -> None: ...

class ParcelDisplayStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.ParcelDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    Segments: int  # = 0
    AreaFill: int  # = 1
class ParcelStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ParcelStyle"""
    def __init__(self, *args) -> None: ...
    AreaFillHatchDisplayStyleModel: HatchDisplayStyle
    AreaFillHatchDisplayStylePlan: HatchDisplayStyle
    ParcelSegmentsMarkerStyle: ObjectId
    NameTemplate: str
    PatternFillDistance: float
    ObservePatternFillDistance: bool
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetAreaFillHatchDisplayStyleModel(self, ) -> HatchDisplayStyle: ...
    def GetAreaFillHatchDisplayStylePlan(self, ) -> HatchDisplayStyle: ...
    def GetDisplayStyleModel(self, type: ParcelDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, type: ParcelDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStyleSection(self, ) -> DisplayStyle: ...

class ParcelStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ParcelStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class PartDataSourceType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.PartDataSourceType"""
    def __init__(self, *args) -> None: ...
    Undefined: int  # = 0
    BasicTable: int  # = 1
    FixedList: int  # = 2
    RangeList: int  # = 3
    Constant: int  # = 4
    Calculation: int  # = 5
    Optional: int  # = 6
class PartFamily(DBObject):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PartFamily"""
    def __init__(self, *args) -> None: ...
    PartSizeFilter: SizeFilterRecord
    Item: ObjectId
    Item: ObjectId
    PartSizeCount: int
    SweptShape: SweptShapeType
    BoundingShape: BoundingShapeType
    PartType: PartType
    Description: str
    GUID: str
    Domain: DomainType
    IsUsed: bool
    Name: str
    Document: object
    Application: object
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
    def AddPartSize(self, partSizeFilter: SizeFilterRecord) -> None: ...
    def RemovePartSize(self, partSizeId: ObjectId) -> None: ...

class PartSize(DBObject):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PartSize"""
    def __init__(self, *args) -> None: ...
    PayItems: list
    SizeDataRecord: PartDataRecord
    PartStyleId: ObjectId
    RulesStyleId: ObjectId
    MaterialStyleId: ObjectId
    IsUsed: bool
    Description: str
    Name: str
    Document: object
    Application: object
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

class PartsList(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PartsList"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    PartFamilyCount: int
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def AddPartFamilyByDescription(self, domain: DomainType, description: str) -> None: ...
    def AddPartFamilyByGuid(self, domain: DomainType, guid: str) -> None: ...
    @staticmethod
    def GetAvailablePartFamilies(domain: DomainType) -> list: ...
    def GetPartFamilyIdsByDomain(self, domain: DomainType) -> ObjectIdCollection: ...
    def RemovePartFamily(self, partFamilyId: ObjectId) -> None: ...

class PartsListCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PartsListCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class PipeCenterlineType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.PipeCenterlineType"""
    def __init__(self, *args) -> None: ...
    ByLineWeight: int  # = 0
    SpecifyWidth: int  # = 1
class PipeCenterlineWidthType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.PipeCenterlineWidthType"""
    def __init__(self, *args) -> None: ...
    DrawToInnerWalls: int  # = 0
    DrawToOuterWalls: int  # = 1
    UseDrawingScale: int  # = 2
    UseAbsoluteUnits: int  # = 3
    UseSizeAsPercentageOfScreen: int  # = 4
class PipeDisplayStylePlanType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.PipeDisplayStylePlanType"""
    def __init__(self, *args) -> None: ...
    Centerline: int  # = 0
    InsideWalls: int  # = 1
    OutsideWalls: int  # = 2
    EndLine: int  # = 3
    Hatch: int  # = 4
    Solid: int  # = 5
class PipeDisplayStyleProfileType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.PipeDisplayStyleProfileType"""
    def __init__(self, *args) -> None: ...
    Centerline: int  # = 0
    InsideWalls: int  # = 1
    OutsideWalls: int  # = 2
    EndLine: int  # = 3
    Hatch: int  # = 4
    CrossingPipeInsideWall: int  # = 6
    CrossingPipeOutsideWall: int  # = 7
    CrossingPipeHatch: int  # = 8
    HydraulicGradeLine: int  # = 9
    EnergyGradeLine: int  # = 10
class PipeDisplayStyleSectionType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.PipeDisplayStyleSectionType"""
    def __init__(self, *args) -> None: ...
    CrossingPipeInsideWall: int  # = 6
    CrossingPipeOutsideWall: int  # = 7
    CrossingPipeHatch: int  # = 8
class PipeEndSizeType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.PipeEndSizeType"""
    def __init__(self, *args) -> None: ...
    DrawToInnerWall: int  # = 0
    DrawToOuterWall: int  # = 1
    UserDefinedEndSize: int  # = 2
class PipeHatchStyleProfileType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.PipeHatchStyleProfileType"""
    def __init__(self, *args) -> None: ...
    Hatch: int  # = 0
    CrossingPipeHatch: int  # = 1
class PipeHatchType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.PipeHatchType"""
    def __init__(self, *args) -> None: ...
    HatchToInnerWalls: int  # = 0
    HatchToOuterWalls: int  # = 1
    HatchWallsOnly: int  # = 2
class PipeNetworkBandStyle(BandStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeNetworkBandStyle"""
    def __init__(self, *args) -> None: ...
    PipeTickStyle: BandTickStyle
    StructureTickStyle: BandTickStyle
    PipeLabelStyleId: ObjectId
    StructureLabelStyleId: ObjectId
    TitleTextLabelStyleId: ObjectId
    BandType: BandType
    WeedingFactor: float
    TextHeight: float
    TextLocation: BandTitleTextLocation
    TextBoxPosition: BandTitleBoxPosition
    OffsetFromBand: float
    TextBoxWidth: float
    BandHeight: float
    Text: str
    TextStyle: str
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStylePlan(self, type: PipeNetworkDisplayStyleType) -> DisplayStyle: ...

class PipeNetworkDisplayStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.PipeNetworkDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    Border: int  # = 0
    TitleBox: int  # = 1
    TitleBoxText: int  # = 2
    TicksAtStructureLocation: int  # = 3
    TicksAtPipeEnds: int  # = 4
    LabelsAtStructureLocation: int  # = 5
    LabelsForPipe: int  # = 6
    LinePipeSchematic: int  # = 7
class PipeRuleSetStyle(NetworkRuleSetStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeRuleSetStyle"""
    def __init__(self, *args) -> None: ...
    RulesCount: int
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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

class PipeRuleSetStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeRuleSetStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class PipeStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeStyle"""
    def __init__(self, *args) -> None: ...
    SectionCrossingHatch: PipeHatchType
    ProfileOption: PipeStyleProfileOption
    PlanOption: PipeStylePlanOption
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStyleModel(self, ) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, component: PipeDisplayStylePlanType) -> DisplayStyle: ...
    def GetDisplayStyleProfile(self, component: PipeDisplayStyleProfileType) -> DisplayStyle: ...
    def GetDisplayStyleSection(self, component: PipeDisplayStyleSectionType) -> DisplayStyle: ...
    def GetHatchStylePlan(self, ) -> HatchDisplayStyle: ...
    def GetHatchStyleProfile(self, component: PipeHatchStyleProfileType) -> HatchDisplayStyle: ...
    def GetHatchStyleSection(self, ) -> HatchDisplayStyle: ...

class PipeStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class PipeStyleOptionBase(CivilWrapper<AeccDbPipeStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeStyleOptionBase"""
    def __init__(self, *args) -> None: ...
    PipeToPipeEndCleanup: bool
    AlignHatchToPipe: bool
    EndSizeOptions: PipeUserDefinedType
    WallSizeOptions: PipeUserDefinedType
    EndSizeType: PipeEndSizeType
    WallSizeType: PipeWallSizeType
    HatchOptions: PipeHatchType
    EndLineSizePercent: float
    EndLineSize: float
    OuterDiameterPercent: float
    OuterDiameter: float
    InnerDiameterPercent: float
    InnerDiameter: float

class PipeStylePlanOption(PipeStyleOptionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeStylePlanOption"""
    def __init__(self, *args) -> None: ...
    CenterlineOptions: PipeCenterlineType
    CenterlineWidthOptions: PipeCenterlineWidthType
    CenterlineSizePercent: float
    CenterlineSize: float
    PipeToPipeEndCleanup: bool
    AlignHatchToPipe: bool
    EndSizeOptions: PipeUserDefinedType
    WallSizeOptions: PipeUserDefinedType
    EndSizeType: PipeEndSizeType
    WallSizeType: PipeWallSizeType
    HatchOptions: PipeHatchType
    EndLineSizePercent: float
    EndLineSize: float
    OuterDiameterPercent: float
    OuterDiameter: float
    InnerDiameterPercent: float
    InnerDiameter: float

class PipeStyleProfileOption(PipeStyleOptionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PipeStyleProfileOption"""
    def __init__(self, *args) -> None: ...
    CrossingHatch: PipeHatchType
    PipeToPipeEndCleanup: bool
    AlignHatchToPipe: bool
    EndSizeOptions: PipeUserDefinedType
    WallSizeOptions: PipeUserDefinedType
    EndSizeType: PipeEndSizeType
    WallSizeType: PipeWallSizeType
    HatchOptions: PipeHatchType
    EndLineSizePercent: float
    EndLineSize: float
    OuterDiameterPercent: float
    OuterDiameter: float
    InnerDiameterPercent: float
    InnerDiameter: float

class PipeUserDefinedType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.PipeUserDefinedType"""
    def __init__(self, *args) -> None: ...
    UseDrawingScale: int  # = 0
    UseAbsoluteUnits: int  # = 1
    UseSizeAsPercentageOfScreen: int  # = 2
class PipeWallSizeType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.PipeWallSizeType"""
    def __init__(self, *args) -> None: ...
    UsePartDimensions: int  # = 0
    UserDefinedWallSize: int  # = 1
class PointCloudClassificationInfo:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PointCloudClassificationInfo"""
    def __init__(self, *args) -> None: ...
    LayerId: ObjectId
    Color: Color
    Selected: bool
    def Dispose(self, ) -> None: ...

class PointCloudClassificationInfoCollection:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PointCloudClassificationInfoCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: PointCloudClassificationInfo
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class PointCloudPointStyle:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PointCloudPointStyle"""
    def __init__(self, *args) -> None: ...
    ScaleFactor: float
    PointElevation: float
    Display3dType: PointDisplay3dType
    ElevationRangeInterval: float
    NumberOfElevationRanges: int
    RangesColorScheme: PointCloudRangeColorSchemeType
    ElevatinoRangeCreationType: PointCloudElevationRangeCreationType
    SingleColor: Color
    IntensityRangeMaximum: float
    IntensityRangeMinimum: float
    ScaledColorIntensityScheme: PointCloudRangeColorSchemeType
    PointsColorScheme: PointCouldColorSchemeType
    SizeInPixels: int

class PointCloudStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PointCloudStyle"""
    def __init__(self, *args) -> None: ...
    ClassificationInfos: PointCloudClassificationInfoCollection
    PointStyle: PointCloudPointStyle
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStyleModel(self, type: PointCloudDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, type: PointCloudDisplayStyleType) -> DisplayStyle: ...

class PointCloudStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PointCloudStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class PointDisplay3dType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.PointDisplay3dType"""
    def __init__(self, *args) -> None: ...
    UsePointElevation: int  # = 0
    FlattenPointElevations: int  # = 1
    ExaggeratePointElevations: int  # = 2
class PointDisplayStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.PointDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    Marker: int  # = 0
    Label: int  # = 1
class PointMarkerDisplayType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.PointMarkerDisplayType"""
    def __init__(self, *args) -> None: ...
    UsePointForMarker: int  # = 0
    UseCustomMarker: int  # = 1
    UseSymbolForMarker: int  # = 2
class PointStyle(MarkerStyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PointStyle"""
    def __init__(self, *args) -> None: ...
    LabelDisplayStyleModel: DisplayStyle
    LabelDisplayStylePlan: DisplayStyle
    MarkerType: PointMarkerDisplayType
    ScaleFactor: float
    Elevation: float
    Display3dType: PointDisplay3dType
    MarkerDisplayStyleModel: DisplayStyle
    MarkerDisplayStylePlan: DisplayStyle
    Orientation: MarkerOrientationType
    MarkerFixedScale: Point3d
    MarkerSize: float
    SizeType: MarkerSizeType
    MarkerRotationAngle: float
    MarkerSymbolName: str
    CustomMarkerSuperimposeStyle: CustomMarkerSuperimposeType
    CustomMarkerStyle: CustomMarkerType
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStyleModel(self, type: PointDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, type: PointDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStyleProfile(self, ) -> DisplayStyle: ...
    def GetDisplayStyleSection(self, ) -> DisplayStyle: ...
    def GetLabelDisplayStyleModel(self, ) -> DisplayStyle: ...
    def GetLabelDisplayStylePlan(self, ) -> DisplayStyle: ...

class PointStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.PointStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class PointSymbolType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.PointSymbolType"""
    def __init__(self, *args) -> None: ...
    K0: int  # = 0
    K1: int  # = 1
    K2: int  # = 2
    K3: int  # = 3
    K4: int  # = 4
    K32: int  # = 32
    K33: int  # = 33
    K34: int  # = 34
    K35: int  # = 35
    K36: int  # = 36
    K64: int  # = 64
    K65: int  # = 65
    K66: int  # = 66
    K67: int  # = 67
    K68: int  # = 68
    K96: int  # = 96
    K97: int  # = 97
    K98: int  # = 98
    K99: int  # = 99
    K100: int  # = 100
class PrecisionRangeType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.PrecisionRangeType"""
    def __init__(self, *args) -> None: ...
    Precision000001: int  # = 0
    Precision00001: int  # = 1
    Precision0001: int  # = 2
    Precision001: int  # = 3
    Precision01: int  # = 4
    Precision1: int  # = 5
    Precision10: int  # = 6
    Precision100: int  # = 7
    Precision1000: int  # = 8
    Precision10000: int  # = 9
    Precision100000: int  # = 10
    Precision1000000: int  # = 11
class ProfileDataBandStyle(BandStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileDataBandStyle"""
    def __init__(self, *args) -> None: ...
    StationEquationTickStyle: BandTickStyle
    VGPTickStyle: BandTickStyle
    HGPTickStyle: BandTickStyle
    MinorIncrementTickStyle: BandTickStyle
    MajorIncrementTickStyle: BandTickStyle
    IncrementalDistanceLabelStyleId: ObjectId
    StationEquationLabelStyleId: ObjectId
    VGPLabelStyleId: ObjectId
    HGPLabelStyleId: ObjectId
    MinorIncrementLabelStyleId: ObjectId
    MajorIncrementLabelStyleId: ObjectId
    TitleTextLabelStyleId: ObjectId
    BandType: BandType
    WeedingFactor: float
    TextHeight: float
    TextLocation: BandTitleTextLocation
    TextBoxPosition: BandTitleBoxPosition
    OffsetFromBand: float
    TextBoxWidth: float
    BandHeight: float
    Text: str
    TextStyle: str
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStylePlan(self, type: ProfileDataDisplayStyleType) -> DisplayStyle: ...

class ProfileDataDisplayStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.ProfileDataDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    Border: int  # = 0
    TitleBox: int  # = 1
    TitleBoxText: int  # = 2
    MajorTicks: int  # = 3
    MinorTicks: int  # = 4
    TicksAtVGP: int  # = 5
    TicksAtHGP: int  # = 6
    TicksAtStationEquations: int  # = 7
    MajorStationLabel: int  # = 8
    MinorStationLabel: int  # = 9
    LabelsAtVGP: int  # = 10
    LabelsAtHGP: int  # = 11
    LabelsAtStationEquations: int  # = 12
    LabelsAtIncrementalDistance: int  # = 13
class ProfileDesignCheckCurveType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.ProfileDesignCheckCurveType"""
    def __init__(self, *args) -> None: ...
    CrestSagCurves: int  # = 0
    CrestCurvesOnly: int  # = 1
    SagCurvesOnly: int  # = 2
class ProfileDesignCheckSet(AlignmentDesignCheckSet):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileDesignCheckSet"""
    def __init__(self, *args) -> None: ...
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def AddDesignCheck(self, type: AlignmentDesignCheckType, name: str) -> AlignmentDesignCheck: ...
    def GetAllDesignChecks(self, ) -> list: ...
    def GetCurveDesignCheckType(self, name: str) -> ProfileDesignCheckCurveType: ...
    def RemoveAllDesignCheck(self, ) -> None: ...
    def RemoveDesignCheck(self, type: AlignmentDesignCheckType, name: str) -> None: ...
    def SetCurveDesignCheckType(self, name: str, type: ProfileDesignCheckCurveType) -> None: ...

class ProfileDesignCheckSetCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileDesignCheckSetCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class ProfileDisplayStyleProfileType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.ProfileDisplayStyleProfileType"""
    def __init__(self, *args) -> None: ...
    Line: int  # = 0
    Curve: int  # = 1
    SymmetricalParabola: int  # = 2
    AsymmetricalParabola: int  # = 3
    Arrow: int  # = 4
    LineExtension: int  # = 5
    ParabolicCurveExtension: int  # = 6
    WarningSymbol: int  # = 11
class ProfileLabelSetItem(BaseLabelSetItem):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileLabelSetItem"""
    def __init__(self, *args) -> None: ...
    StaggerLabel: StaggerLabelType
    StaggerLineHeight2: float
    StaggerLineHeight1: float
    Weeding: float
    DimensionAnchorOption: DimensionAnchorType
    DimensionAnchorValue: float
    Increment: float
    LabelStyleName: str
    LabelStyleId: ObjectId
    LabelStyleType: LabelStyleType
    def GetLabeledAlignmentGeometryPoints(self, ) -> Dictionary: ...
    def SetLabeledAlignmentGeometryPoints(self, pointTypes: Dictionary) -> None: ...

class ProfileLabelSetStyle(BaseLabelSetStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileLabelSetStyle"""
    def __init__(self, *args) -> None: ...
    Item: ProfileLabelSetItem
    Count: int
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def AddCrestCurve(self, labelStyleId: ObjectId) -> None: ...
    def AddSagCurve(self, labelStyleId: ObjectId) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class ProfileLabelSetStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileLabelSetStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class ProfileStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileStyle"""
    def __init__(self, *args) -> None: ...
    ArrowHeadOption: ArrowHeadOption
    ProfileMarkerDisplayStyleSection: DisplayStyle
    Chain3DDisplayStyleModel: DisplayStyle
    ProfileMarkerSectionViewMarkerStyle: ObjectId
    LowPointMarkerStyle: ObjectId
    HighPointMarkerStyle: ObjectId
    VCurveTangentIntersectPointMarkerStyle: ObjectId
    VReverseCurveIntersectPointMarkerStyle: ObjectId
    VCompoundCurveIntersectPointMarkerStyle: ObjectId
    VTangentCurveIntersectPointMarkerStyle: ObjectId
    EndPointMarkerStyle: ObjectId
    BeginPointMarkerStyle: ObjectId
    VIntersectionPointMarkerStyle: ObjectId
    ThroughPointMarkerStyle: ObjectId
    ChainTessellationDistance3D: float
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetChain3DDisplayStyleModel(self, ) -> DisplayStyle: ...
    def GetDisplayStyleProfile(self, type: ProfileDisplayStyleProfileType) -> DisplayStyle: ...
    def GetProfileMarkerDisplayStyleSection(self, ) -> DisplayStyle: ...

class ProfileStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class ProfileViewBandSetItem(BandSetItem):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileViewBandSetItem"""
    def __init__(self, *args) -> None: ...
    LabelAtEndStation: bool
    LabelAtStartStation: bool
    BandStyleId: ObjectId
    MinorInterval: float
    MajorInterval: float
    StaggerLineHeight: float
    StaggerLabel: StaggerLabelType
    Weeding: float
    Gap: float
    ShowLabels: bool
    BandType: BandType
    Location: BandLocationType
    def GetHorizontalGeometryPointsOptions(self, ) -> GeometryPointSelector: ...
    def GetVerticalGeometryPointsOptions(self, ) -> GeometryPointSelector: ...
    def SetHorizontalGeometryPointsOptions(self, alignmentGeometryPoints: GeometryPointSelector) -> None: ...
    def SetVerticalGeometryPointsOptions(self, alignmentVerticalGeometryPoints: GeometryPointSelector) -> None: ...

class ProfileViewBandSetItemCollection(BandSetItemCollection):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileViewBandSetItemCollection"""
    def __init__(self, *args) -> None: ...
    Item: ProfileViewBandSetItem
    Count: int
    Location: BandLocationType
    def Add(self, database: Database, bandType: BandType, profileBandStyleName: str) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class ProfileViewBandSetStyle(BandSetStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileViewBandSetStyle"""
    def __init__(self, *args) -> None: ...
    MatchIncrementToGridIntervals: bool
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetBottomBandSetItems(self, ) -> ProfileViewBandSetItemCollection: ...
    def GetTopBandSetItems(self, ) -> ProfileViewBandSetItemCollection: ...
    def SetBottomBandSetItems(self, bandSetItems: ProfileViewBandSetItemCollection) -> None: ...
    def SetTopBandSetItems(self, bandSetItems: ProfileViewBandSetItemCollection) -> None: ...

class ProfileViewBandSetStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileViewBandSetStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class ProfileViewDisplayStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.ProfileViewDisplayStyleType"""
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
    GridHorizontalMajor: int  # = 37
    GridHorizontalMinor: int  # = 38
    GridVerticalMajor: int  # = 39
    GridVerticalMinor: int  # = 40
    GridAtHGP: int  # = 44
    TopAxisAnnotationHGP: int  # = 47
    TopAxisTicksHGP: int  # = 48
    BottomAxisAnnotationHGP: int  # = 49
    BottomAxisTicksHGP: int  # = 50
    GridAtSampleLineStations: int  # = 53
    ProfileHatch: int  # = 54
class ProfileViewStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileViewStyle"""
    def __init__(self, *args) -> None: ...
    RightAxis: AxisStyle
    LeftAxis: AxisStyle
    BottomAxis: AxisStyle
    TopAxis: AxisStyle
    GridStyle: GridStyle
    GraphStyle: GraphStyle
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStylePlan(self, type: ProfileViewDisplayStyleType) -> DisplayStyle: ...

class ProfileViewStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProfileViewStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class ProjectionBlockDisplayType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.ProjectionBlockDisplayType"""
    def __init__(self, *args) -> None: ...
    NativeEntity: int  # = 0
    Marker: int  # = 1
    Block: int  # = 2
class ProjectionDisplayStyleProfileType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.ProjectionDisplayStyleProfileType"""
    def __init__(self, *args) -> None: ...
    SolidProfile: int  # = 0
    PointProfile: int  # = 1
    ThreeDPolylineSegmentsProfile: int  # = 2
    ThreeDPolylineBeginVertexProfile: int  # = 3
    ThreeDPolylineInternalVertexProfile: int  # = 4
    ThreeDPolylineEndVertexProfile: int  # = 5
    BlockProfile: int  # = 6
    MvBlockProfile: int  # = 7
class ProjectionDisplayStyleSectionType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.ProjectionDisplayStyleSectionType"""
    def __init__(self, *args) -> None: ...
    SolidSection: int  # = 8
    PointSection: int  # = 9
    ThreeDPolylineSection: int  # = 10
    BlockSection: int  # = 11
    MvBlockSection: int  # = 12
class ProjectionEntityDisplayType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.ProjectionEntityDisplayType"""
    def __init__(self, *args) -> None: ...
    NativeEntity: int  # = 0
    Marker: int  # = 1
class ProjectionProfileOptions(CivilWrapper<AeccDbProfileSectionEntityStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProjectionProfileOptions"""
    def __init__(self, *args) -> None: ...
    VerticallyExaggerateMultiViewBlocks: bool
    MultiViewBlockSymbolBlockName: str
    MultiViewBlockSymbolBlockId: ObjectId
    MultiViewBlockDirection: ViewDirection
    MultiViewBlockDisplayRepresentationName: str
    MultiViewBlockDisplayRepresentationId: ObjectId
    MultiViewBlockMarkerStyleName: str
    MultiViewBlockMarkerStyleId: ObjectId
    MultiViewBlockDisplayOptions: ProjectionBlockDisplayType
    VerticallyExaggerateBlocks: bool
    AutoCADBlockSymbolBlockName: str
    AutoCADBlockSymbolBlockId: ObjectId
    AutoCADBlockMarkerStyleName: str
    AutoCADBlockMarkerStyleId: ObjectId
    AutoCADBlockDisplayOptions: ProjectionBlockDisplayType
    AutoCAD3dPolylineEndVertexMarkerStyleName: str
    AutoCAD3dPolylineEndVertexMarkerStyleId: ObjectId
    AutoCAD3dPolylineInternalVertexMarkerStyleName: str
    AutoCAD3dPolylineInternalVertexMarkerStyleId: ObjectId
    AutoCAD3dPolylineBeginVertexMarkerStyleName: str
    AutoCAD3dPolylineBeginVertexMarkerStyleId: ObjectId
    VerticallyExaggerateSolids: bool
    AutoCADSolidMarkerStyleName: str
    AutoCADSolidMarkerStyleId: ObjectId
    AutoCADSolidDisplayOptions: ProjectionEntityDisplayType
    AutoCADPointMarkerStyleName: str
    AutoCADPointMarkerStyleId: ObjectId
    AutoCADPointDisplayOptions: ProjectionEntityDisplayType

class ProjectionSectionOptions(CivilWrapper<AeccDbProfileSectionEntityStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProjectionSectionOptions"""
    def __init__(self, *args) -> None: ...
    VerticallyExaggerateMultiViewBlocks: bool
    MultiViewBlockSymbolBlockName: str
    MultiViewBlockSymbolBlockId: ObjectId
    MultiViewBlockDirection: ViewDirection
    MultiViewBlockDisplayRepresentationName: str
    MultiViewBlockDisplayRepresentationId: ObjectId
    MultiViewBlockMarkerStyleName: str
    MultiViewBlockMarkerStyleId: ObjectId
    MultiViewBlockDisplayOptions: ProjectionBlockDisplayType
    VerticallyExaggerateBlocks: bool
    AutoCADBlockSymbolBlockName: str
    AutoCADBlockSymbolBlockId: ObjectId
    AutoCADBlockMarkerStyleName: str
    AutoCADBlockMarkerStyleId: ObjectId
    AutoCADBlockDisplayOptions: ProjectionBlockDisplayType
    AutoCAD3dPolylineCrossingMarkerStyleName: str
    AutoCAD3dPolylineCrossingMarkerStyleId: ObjectId
    VerticallyExaggerateSolids: bool
    AutoCADSolidMarkerStyleName: str
    AutoCADSolidMarkerStyleId: ObjectId
    AutoCADSolidDisplayAsTrueSection: bool
    AutoCADSolidDisplayOptions: ProjectionEntityDisplayType
    AutoCADPointMarkerStyleName: str
    AutoCADPointMarkerStyleId: ObjectId
    AutoCADPointDisplayOptions: ProjectionEntityDisplayType

class ProjectionStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProjectionStyle"""
    def __init__(self, *args) -> None: ...
    SectionOptions: ProjectionSectionOptions
    ProfileOptions: ProjectionProfileOptions
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStyleProfile(self, type: ProjectionDisplayStyleProfileType) -> DisplayStyle: ...
    def GetDisplayStyleSection(self, type: ProjectionDisplayStyleSectionType) -> DisplayStyle: ...

class ProjectionStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ProjectionStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class QuantityTakeoffCriteria(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.QuantityTakeoffCriteria"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: QuantityTakeoffCriteriaItem
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def AddMaterial(self, materialName: str) -> None: ...
    def Clear(self, ) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class QuantityTakeoffCriteriaCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.QuantityTakeoffCriteriaCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class QuantityTakeoffCriteriaData(CivilWrapper<AeccDbQuantityTakeoffCriteria>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.QuantityTakeoffCriteriaData"""
    def __init__(self, *args) -> None: ...
    ItemType: MaterialItemType
    Condition: MaterialConditionType
    Name: str

class QuantityTakeoffCriteriaItem(CivilWrapper<AeccDbQuantityTakeoffCriteria>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.QuantityTakeoffCriteriaItem"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: QuantityTakeoffCriteriaData
    ShapeStyleName: str
    ShapeStyleId: ObjectId
    ReFillFactor: float
    FillFactor: float
    CutFactor: float
    QuantityType: MaterialQuantityType
    MaterialName: str
    def AddCorridorShape(self, shapeName: str) -> None: ...
    def AddSurface(self, surfaceName: str) -> None: ...
    def RemoveCorridorShape(self, shapeName: str) -> None: ...
    def RemoveSurface(self, surfaceName: str) -> None: ...

class ReferenceTextComponentSelectedType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.ReferenceTextComponentSelectedType"""
    def __init__(self, *args) -> None: ...
    Alignment: int  # = 0
    CogoPoint: int  # = 1
    Parcel: int  # = 2
    Profile: int  # = 3
    Surface: int  # = 4
class SampleLineDisplayStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.SampleLineDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    Lines: int  # = 0
    Vertices: int  # = 1
class SampleLineStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SampleLineStyle"""
    def __init__(self, *args) -> None: ...
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStyleModel(self, type: SampleLineDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, type: SampleLineDisplayStyleType) -> DisplayStyle: ...

class SampleLineStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SampleLineStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class ScaleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.ScaleType"""
    def __init__(self, *args) -> None: ...
    UseDrawingScale: int  # = 0
    SizeRelativeToScreen: int  # = 1
    SizeInAbsoluteUnits: int  # = 2
class ScalingMethodType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.ScalingMethodType"""
    def __init__(self, *args) -> None: ...
    UseDrawingScale: int  # = 0
    SizeRelativeToScreen: int  # = 1
    SizeInAbsoluteUnits: int  # = 2
class SchematicLineOption:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.SchematicLineOption"""
    def __init__(self, *args) -> None: ...
    Geometry: int  # = 0
    Radius: int  # = 1
    Curvature: int  # = 2
class SectionDataBandStyle(BandStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionDataBandStyle"""
    def __init__(self, *args) -> None: ...
    GradeBreaksTickStyle: BandTickStyle
    SampleLineVerticesTickStyle: BandTickStyle
    CenterlineTickStyle: BandTickStyle
    MinorIncrementTickStyle: BandTickStyle
    MajorIncrementTickStyle: BandTickStyle
    IncrementalDistanceLabelStyleId: ObjectId
    GradeBreaksLabelStyleId: ObjectId
    SampleLineVerticesLabelStyleId: ObjectId
    CenterlineLabelStyleId: ObjectId
    MinorIncrementLabelStyleId: ObjectId
    MajorIncrementLabelStyleId: ObjectId
    TitleTextLabelStyleId: ObjectId
    BandType: BandType
    WeedingFactor: float
    TextHeight: float
    TextLocation: BandTitleTextLocation
    TextBoxPosition: BandTitleBoxPosition
    OffsetFromBand: float
    TextBoxWidth: float
    BandHeight: float
    Text: str
    TextStyle: str
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStylePlan(self, type: SectionDataDisplayStyleType) -> DisplayStyle: ...

class SectionDataDisplayStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.SectionDataDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    Border: int  # = 0
    TitleBox: int  # = 1
    TitleBoxText: int  # = 2
    TicksAtMajorOffsets: int  # = 3
    TicksAtMinorOffsets: int  # = 4
    TicksAtCenterline: int  # = 5
    TicksAtSampleLineVertices: int  # = 6
    TicksAtGradeBreaks: int  # = 7
    LabelsAtMajorOffsets: int  # = 8
    LabelsAtMinorOffsets: int  # = 9
    LabelsAtCenterline: int  # = 10
    LabelsAtSampleLineVertices: int  # = 11
    LabelsAtGradeBreaks: int  # = 12
    LabelsAtIncrementalDistance: int  # = 13
class SectionDisplayStyleSectionType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.SectionDisplayStyleSectionType"""
    def __init__(self, *args) -> None: ...
    Segments: int  # = 0
    Points: int  # = 1
class SectionLabelSetItem(BaseLabelSetItem):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionLabelSetItem"""
    def __init__(self, *args) -> None: ...
    StaggerLabel: StaggerLabelType
    StaggerLineHeight2: float
    StaggerLineHeight1: float
    Weeding: float
    DimensionAnchorOption: DimensionAnchorType
    DimensionAnchorValue: float
    Increment: float
    LabelStyleName: str
    LabelStyleId: ObjectId
    LabelStyleType: LabelStyleType

class SectionLabelSetStyle(BaseLabelSetStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionLabelSetStyle"""
    def __init__(self, *args) -> None: ...
    Item: SectionLabelSetItem
    Count: int
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class SectionLabelSetStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionLabelSetStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class SectionSegmentBandStyle(BandStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionSegmentBandStyle"""
    def __init__(self, *args) -> None: ...
    SegmentLabelsTickStyle: BandTickStyle
    SegmentsLabelStyleId: ObjectId
    TitleTextLabelStyleId: ObjectId
    BandType: BandType
    WeedingFactor: float
    TextHeight: float
    TextLocation: BandTitleTextLocation
    TextBoxPosition: BandTitleBoxPosition
    OffsetFromBand: float
    TextBoxWidth: float
    BandHeight: float
    Text: str
    TextStyle: str
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStylePlan(self, type: SectionSegmentDisplayStyleType) -> DisplayStyle: ...

class SectionSegmentDisplayStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.SectionSegmentDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    Border: int  # = 0
    TitleBox: int  # = 1
    TitleBoxText: int  # = 2
    Ticks: int  # = 3
    Labels: int  # = 4
    Lines: int  # = 5
class SectionStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionStyle"""
    def __init__(self, *args) -> None: ...
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStyleSection(self, type: SectionDisplayStyleSectionType) -> DisplayStyle: ...

class SectionStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class SectionViewBandSetItem(BandSetItem):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionViewBandSetItem"""
    def __init__(self, *args) -> None: ...
    LabelAtEndOffset: bool
    LabelAtStartOffset: bool
    BandStyleId: ObjectId
    MinorInterval: float
    MajorInterval: float
    StaggerLineHeight: float
    StaggerLabel: StaggerLabelType
    Weeding: float
    Gap: float
    ShowLabels: bool
    BandType: BandType
    Location: BandLocationType

class SectionViewBandSetItemCollection(BandSetItemCollection):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionViewBandSetItemCollection"""
    def __init__(self, *args) -> None: ...
    Item: SectionViewBandSetItem
    Count: int
    Location: BandLocationType
    def Add(self, database: Database, bandType: BandType, sectionBandStyleName: str) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...

class SectionViewBandSetStyle(BandSetStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionViewBandSetStyle"""
    def __init__(self, *args) -> None: ...
    MatchIncrementToGridIntervals: bool
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetBottomBandSetItems(self, ) -> SectionViewBandSetItemCollection: ...
    def GetTopBandSetItems(self, ) -> SectionViewBandSetItemCollection: ...
    def SetBottomBandSetItems(self, bandSetItems: SectionViewBandSetItemCollection) -> None: ...
    def SetTopBandSetItems(self, bandSetItems: SectionViewBandSetItemCollection) -> None: ...

class SectionViewBandSetStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionViewBandSetStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class SectionViewDisplayStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.SectionViewDisplayStyleType"""
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
    CenterAxis: int  # = 31
    CenterAxisTitle: int  # = 32
    CenterAxisAnnotationMajor: int  # = 33
    CenterAxisAnnotationMinor: int  # = 34
    CenterAxisTicksMajor: int  # = 35
    CenterAxisTicksMinor: int  # = 36
    GridHorizontalMajor: int  # = 37
    GridHorizontalMinor: int  # = 38
    GridVerticalMajor: int  # = 39
    GridVerticalMinor: int  # = 40
    GridAtSampleLineStations: int  # = 41
    GridAtPGP: int  # = 43
class SectionViewPlotRuleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.SectionViewPlotRuleType"""
    def __init__(self, *args) -> None: ...
    ByRows: int  # = 0
    ByColumns: int  # = 1
class SectionViewStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionViewStyle"""
    def __init__(self, *args) -> None: ...
    RightAxis: AxisStyle
    CenterAxis: AxisStyle
    LeftAxis: AxisStyle
    BottomAxis: AxisStyle
    TopAxis: AxisStyle
    GridStyle: GridStyle
    GraphStyle: GraphStyle
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStylePlan(self, type: SectionViewDisplayStyleType) -> DisplayStyle: ...

class SectionViewStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionViewStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class SectionalDataBandStyle(BandStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SectionalDataBandStyle"""
    def __init__(self, *args) -> None: ...
    IncrementalSectionDataTickStyle: BandTickStyle
    SampleLineStationTickStyle: BandTickStyle
    IncrementalSectionDataLabelStyleId: ObjectId
    SampleLineStationLabelStyleId: ObjectId
    TitleTextLabelStyleId: ObjectId
    BandType: BandType
    WeedingFactor: float
    TextHeight: float
    TextLocation: BandTitleTextLocation
    TextBoxPosition: BandTitleBoxPosition
    OffsetFromBand: float
    TextBoxWidth: float
    BandHeight: float
    Text: str
    TextStyle: str
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStylePlan(self, type: SectionalDataDisplayStyleType) -> DisplayStyle: ...

class SectionalDataDisplayStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.SectionalDataDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    Border: int  # = 0
    TitleBox: int  # = 1
    TitleBoxText: int  # = 2
    TicksAtSampleLineStation: int  # = 3
    SampleLineStationLabels: int  # = 4
    IncrementalStationRegionLabels: int  # = 5
class SegmentColumnStyle(ColumnStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SegmentColumnStyle"""
    def __init__(self, *args) -> None: ...
    ContentJustification: TextJustificationType
    ContentStringFormatted: str
    ContentString: str
    HeaderJustification: TextJustificationType
    HeaderStringFormatted: str
    HeaderString: str
    ColumnWidth: float
    def GetContentString(self, type: TableSegmentDataType) -> str: ...
    def GetContentStringFormatted(self, type: TableSegmentDataType) -> str: ...
    def SetContentString(self, type: TableSegmentDataType, newVal: str) -> None: ...
    def SetContentStringFormatted(self, type: TableSegmentDataType, newVal: str) -> None: ...

class ShapeDisplayStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.ShapeDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    Border: int  # = 0
    AreaFill: int  # = 1
class ShapeStyle(SubassemblySubentityStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ShapeStyle"""
    def __init__(self, *args) -> None: ...
    AreaFillHatchDisplayStyleModel: HatchDisplayStyle
    AreaFillHatchDisplayStylePlan: HatchDisplayStyle
    StyleType: SubassemblySubentityStyleType
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStyleModel(self, type: ShapeDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, type: ShapeDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStyleProfile(self, type: ShapeDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStyleSection(self, type: ShapeDisplayStyleType) -> DisplayStyle: ...
    def GetHatchDisplayStyleModel(self, ) -> HatchDisplayStyle: ...
    def GetHatchDisplayStylePlan(self, ) -> HatchDisplayStyle: ...
    def GetHatchDisplayStyleProfile(self, ) -> HatchDisplayStyle: ...
    def GetHatchDisplayStyleSection(self, ) -> HatchDisplayStyle: ...

class ShapeStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ShapeStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class SheetDisplayStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.SheetDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    MajorHorizontalGrid: int  # = 0
    MinorHorizontalGrid: int  # = 1
    MajorVerticalGrid: int  # = 2
    MinorVerticalGrid: int  # = 3
    PrintArea: int  # = 4
    Border: int  # = 5
class SheetStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SheetStyle"""
    def __init__(self, *args) -> None: ...
    PageMarginRight: float
    PageMarginLeft: float
    PageMarginBottom: float
    PageMarginTop: float
    PageLayoutId: ObjectId
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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

class SheetStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SheetStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class SizeFilterField(PartDataField):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SizeFilterField"""
    def __init__(self, *args) -> None: ...
    DataSource: PartDataSourceType
    IsMultipleSelect: bool
    Units: str
    Index: int
    Context: PartContextType
    ContextString: str
    Description: str
    Name: str
    Value: object
    IsReadOnly: bool
    ValueRange: PartDataRange
    ValueList: PartDataList
    IsFromRange: bool
    IsFromList: bool
    DataType: PartCatalogDataType

class SizeFilterRecord:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SizeFilterRecord"""
    def __init__(self, *args) -> None: ...
    PartFamilyGuid: str
    Item: SizeFilterField
    Item: SizeFilterField
    ParamCount: int
    def Dispose(self, ) -> None: ...
    def GetParamByContextAndIndex(self, context: PartContextType, index: int) -> SizeFilterField: ...

class SlopeArrowType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.SlopeArrowType"""
    def __init__(self, *args) -> None: ...
    Filled: int  # = 0
    Closed: int  # = 1
    Open: int  # = 2
    Double: int  # = 3
class SlopePatternComponent(CivilWrapper<AeccDbSlopePatternStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SlopePatternComponent"""
    def __init__(self, *args) -> None: ...
    SlopeLineSymbol: SlopePatternLineSymbol
    SlopeLineOffset: SlopePatternLineOffset
    SlopeLine: SlopePatternLine

class SlopePatternLine(CivilWrapper<AeccDbSlopePatternStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SlopePatternLine"""
    def __init__(self, *args) -> None: ...
    Color: Color
    LineWeight: LineWeight
    Linetype: str
    Grade2: float
    Grade1: float
    PercentofLength2: float
    PercentofLength1: float
    Length: float
    MaximumLength: float
    PercentofLength: float
    LengthType: SlopePatternLengthType
    StartType: SlopePatternStartType

class SlopePatternLineOffset(CivilWrapper<AeccDbSlopePatternStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SlopePatternLineOffset"""
    def __init__(self, *args) -> None: ...
    Numberoflines: int
    Distance: float
    RadialOffsetAngle: float
    MaximumDistance: float
    MinimumDistance: float
    PercentofLength: float
    OffsetType: SlopePatternOffsetType

class SlopePatternLineSymbol(CivilWrapper<AeccDbSlopePatternStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SlopePatternLineSymbol"""
    def __init__(self, *args) -> None: ...
    Numberoflines: int
    Color: Color
    LineWeight: LineWeight
    Linetype: str
    WidthRatio: float
    Length: float
    PercentofLength: float
    LengthType: SlopePatternLengthType
    BlockName: str
    SymbolType: SlopePatternSymbolType

class SlopePatternStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SlopePatternStyle"""
    def __init__(self, *args) -> None: ...
    PreviewSlope: float
    PreviewSlopeLength: float
    PreviewFeatureLength: float
    MinDisplayLength: float
    Count: int
    Item: SlopePatternComponent
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def AddComponent(self, position: int) -> None: ...
    def CopyComponent(self, index: int, insertPosition: int) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class SlopePatternStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SlopePatternStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class StaggerLabelType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.StaggerLabelType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Both: int  # = 1
    Right: int  # = 2
    Left: int  # = 3
class StructureColumnComponentData(CivilWrapper<tableCellComponentVec>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureColumnComponentData"""
    def __init__(self, *args) -> None: ...
    ComponentType: StructureColumnComponentType
    Content: str
    Name: str

class StructureColumnComponents(CivilWrapper<tableCellComponentVec>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureColumnComponents"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: StructureColumnComponentData
    def AddComponent(self, name: str, componentType: StructureColumnComponentType) -> None: ...
    def Clear(self, ) -> None: ...
    def RemoveAt(self, name: str) -> None: ...
    def SwitchComponentsOrder(self, index1: int, index2: int) -> None: ...

class StructureColumnStyle(ColumnStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureColumnStyle"""
    def __init__(self, *args) -> None: ...
    ContentJustification: TextJustificationType
    ContentStringFormatted: str
    ContentString: str
    HeaderJustification: TextJustificationType
    HeaderStringFormatted: str
    HeaderString: str
    ColumnWidth: float
    def GetComponents(self, ) -> StructureColumnComponents: ...
    def SetComponents(self, componentDatas: StructureColumnComponents) -> None: ...

class StructureDisplayStylePlanType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.StructureDisplayStylePlanType"""
    def __init__(self, *args) -> None: ...
    Structure: int  # = 0
    StructureHatch: int  # = 1
    Solid: int  # = 2
class StructureDisplayStyleProfileType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.StructureDisplayStyleProfileType"""
    def __init__(self, *args) -> None: ...
    Structure: int  # = 0
    StructureHatch: int  # = 1
    StructurePipeOutlines: int  # = 3
class StructureDisplayStyleSectionType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.StructureDisplayStyleSectionType"""
    def __init__(self, *args) -> None: ...
    Structure: int  # = 0
    StructureHatch: int  # = 1
    StructurePipeOutlines: int  # = 3
class StructureInsertionLocation:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.StructureInsertionLocation"""
    def __init__(self, *args) -> None: ...
    Rim: int  # = 0
    Sump: int  # = 1
class StructureModelViewOptionType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.StructureModelViewOptionType"""
    def __init__(self, *args) -> None: ...
    UseCatalogDefined3DPart: int  # = 0
    UseSimple3DPart: int  # = 1
class StructurePlanViewType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.StructurePlanViewType"""
    def __init__(self, *args) -> None: ...
    UseOuterPartBoundary: int  # = 0
    UserDefinedPart: int  # = 1
class StructureRuleSetStyle(NetworkRuleSetStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureRuleSetStyle"""
    def __init__(self, *args) -> None: ...
    RulesCount: int
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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

class StructureRuleSetStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureRuleSetStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class StructureSimpleSolidType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.StructureSimpleSolidType"""
    def __init__(self, *args) -> None: ...
    Box: int  # = 0
    Cylinder: int  # = 1
    Sphere: int  # = 2
    PartDefinedShape: int  # = 3
class StructureSizeOptionsType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.StructureSizeOptionsType"""
    def __init__(self, *args) -> None: ...
    UseDrawingScale: int  # = 0
    UseFixedScale: int  # = 1
    UseAbsoluteUnits: int  # = 2
    UseSizeAsPercentageOfScreen: int  # = 3
    UseFixedScaleFromPartSize: int  # = 4
class StructureStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureStyle"""
    def __init__(self, *args) -> None: ...
    SectionOption: StructureStyleSectionOption
    ModelOption: StructureStyleModelOption
    ProfileOption: StructureStyleProfileOption
    PlanOption: StructureStylePlanOption
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStyleModel(self, ) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, component: StructureDisplayStylePlanType) -> DisplayStyle: ...
    def GetDisplayStyleProfile(self, component: StructureDisplayStyleProfileType) -> DisplayStyle: ...
    def GetDisplayStyleSection(self, component: StructureDisplayStyleSectionType) -> DisplayStyle: ...
    def GetHatchStylePlan(self, ) -> HatchDisplayStyle: ...
    def GetHatchStyleProfile(self, ) -> HatchDisplayStyle: ...
    def GetHatchStyleSection(self, ) -> HatchDisplayStyle: ...

class StructureStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class StructureStyleModelOption(CivilWrapper<AeccDbStructureStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureStyleModelOption"""
    def __init__(self, *args) -> None: ...
    SimpleSolidType: StructureSimpleSolidType
    ModelViewOptions: StructureModelViewOptionType

class StructureStyleOptionBase(CivilWrapper<AeccDbStructureStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureStyleOptionBase"""
    def __init__(self, *args) -> None: ...
    MaskConnectedObjects: bool
    YSizePercent: float
    YSize: float
    XSizePercent: float
    XSize: float
    SymbolBlockZScale: float
    SymbolBlockYScale: float
    SymbolBlockXScale: float
    SymbolBlockName: str
    BlockInsertLocation: StructureInsertionLocation
    SizeType: StructureSizeOptionsType
    ViewOptions: StructureViewType

class StructureStylePlanOption(CivilWrapper<AeccDbStructureStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureStylePlanOption"""
    def __init__(self, *args) -> None: ...
    SizePercent: float
    Size: float
    MaskConnectedObjects: bool
    SymbolBlockZScale: float
    SymbolBlockYScale: float
    SymbolBlockXScale: float
    SymbolBlockName: str
    SizeType: StructureSizeOptionsType
    PlanViewOptions: StructurePlanViewType

class StructureStyleProfileOption(StructureStyleOptionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureStyleProfileOption"""
    def __init__(self, *args) -> None: ...
    MaskConnectedObjects: bool
    YSizePercent: float
    YSize: float
    XSizePercent: float
    XSize: float
    SymbolBlockZScale: float
    SymbolBlockYScale: float
    SymbolBlockXScale: float
    SymbolBlockName: str
    BlockInsertLocation: StructureInsertionLocation
    SizeType: StructureSizeOptionsType
    ViewOptions: StructureViewType

class StructureStyleSectionOption(StructureStyleOptionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StructureStyleSectionOption"""
    def __init__(self, *args) -> None: ...
    MaskConnectedObjects: bool
    YSizePercent: float
    YSize: float
    XSizePercent: float
    XSize: float
    SymbolBlockZScale: float
    SymbolBlockYScale: float
    SymbolBlockXScale: float
    SymbolBlockName: str
    BlockInsertLocation: StructureInsertionLocation
    SizeType: StructureSizeOptionsType
    ViewOptions: StructureViewType

class StructureViewType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.StructureViewType"""
    def __init__(self, *args) -> None: ...
    DisplayAsBoundary: int  # = 0
    DisplayAsBlock: int  # = 1
    DisplayAsSolid: int  # = 2
class StyleBase(DBObject):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StyleBase"""
    def __init__(self, *args) -> None: ...
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def CopyAsSibling(self, styleName: str) -> ObjectId: ...
    @staticmethod
    def ExportTo(styleIds: ObjectIdCollection, destinationDatabase: Database, conflictResolution: StyleConflictResolverType) -> None: ...

class StyleCollectionBase(TreeNodeCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StyleCollectionBase"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...
    def Remove(self, style: StyleBase) -> None: ...

class StylesRoot(TreeOidWrapper):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.StylesRoot"""
    def __init__(self, *args) -> None: ...
    ProfileDesignCheckSets: ProfileDesignCheckSetCollection
    AlignmentDesignCheckSets: AlignmentDesignCheckSetCollection
    ProjectionStyles: ProjectionStyleCollection
    SurveyNetworkStyles: SurveyNetworkStyleCollection
    SurveyFigureStyles: SurveyFigureStyleCollection
    QuantityTakeoffCriterias: QuantityTakeoffCriteriaCollection
    IntersectionStyles: IntersectionStyleCollection
    CorridorStyles: CorridorStyleCollection
    AssemblyStyles: AssemblyStyleCollection
    CodeSetStyles: CodeSetStyleCollection
    ShapeStyles: ShapeStyleCollection
    LinkStyles: LinkStyleCollection
    PartsListSet: PartsListCollection
    StructureRuleSetStyles: StructureRuleSetStyleCollection
    PipeRuleSetStyles: PipeRuleSetStyleCollection
    InterferenceStyles: InterferenceStyleCollection
    StructureStyles: StructureStyleCollection
    PipeStyles: PipeStyleCollection
    CatchmentStyles: CatchmentStyleCollection
    CantViewStyles: CantViewStyleCollection
    SuperelevationViewStyles: SuperelevationViewStyleCollection
    PointCloudStyles: PointCloudStyleCollection
    GradingCriteriaSets: GradingCriteriaSetCollection
    BuildingSiteStyles: BuildingSiteStyleCollection
    SlopePatternStyles: SlopePatternStyleCollection
    MassHaulViewStyles: MassHaulViewStyleCollection
    MassHaulLineStyles: MassHaulLineStyleCollection
    SectionViewBandSetStyles: SectionViewBandSetStyleCollection
    ProfileViewBandSetStyles: ProfileViewBandSetStyleCollection
    ProfileViewStyles: ProfileViewStyleCollection
    ProfileStyles: ProfileStyleCollection
    ViewFrameStyles: ViewFrameStyleCollection
    SheetStyles: SheetStyleCollection
    MatchLineStyles: MatchLineStyleCollection
    GroupPlotStyles: GroupPlotStyleCollection
    GradingStyles: GradingStyleCollection
    FeatureLineStyles: FeatureLineStyleCollection
    SurfaceStyles: SurfaceStyleCollection
    SectionViewStyles: SectionViewStyleCollection
    SectionStyles: SectionStyleCollection
    SampleLineStyles: SampleLineStyleCollection
    PointStyles: PointStyleCollection
    ParcelStyles: ParcelStyleCollection
    AlignmentStyles: AlignmentStyleCollection
    MarkerStyles: MarkerStyleCollection
    BandStyles: BandStylesRoot
    LabelSetStyles: LabelSetStylesRoot
    LabelStyles: LabelStylesRoot
    TableStyles: TableStylesRoot
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SubassemblySubentityStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SubassemblySubentityStyle"""
    def __init__(self, *args) -> None: ...
    StyleType: SubassemblySubentityStyleType
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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

class SubassemblySubentityStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.SubassemblySubentityStyleType"""
    def __init__(self, *args) -> None: ...
    MarkerType: int  # = 0
    LinkType: int  # = 1
    ShapeType: int  # = 2
class SuperelevationDataBandStyle(BandStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SuperelevationDataBandStyle"""
    def __init__(self, *args) -> None: ...
    SlopeTransitionRegionTickStyle: BandTickStyle
    ShoulderCriticalPointsTickStyle: BandTickStyle
    FullSuperTickStyle: BandTickStyle
    ReverseCrownTickStyle: BandTickStyle
    LevelCrownTickStyle: BandTickStyle
    NormalCrownTickStyle: BandTickStyle
    SlopeTransitionRegionLabelStyleId: ObjectId
    ShoulderCriticalPointsLabelStyleId: ObjectId
    FullSuperLabelStyleId: ObjectId
    ReverseCrownLabelStyleId: ObjectId
    LevelCrownLabelStyleId: ObjectId
    NormalCrownLabelStyleId: ObjectId
    TitleTextLabelStyleId: ObjectId
    BandType: BandType
    WeedingFactor: float
    TextHeight: float
    TextLocation: BandTitleTextLocation
    TextBoxPosition: BandTitleBoxPosition
    OffsetFromBand: float
    TextBoxWidth: float
    BandHeight: float
    Text: str
    TextStyle: str
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStylePlan(self, type: SuperelevationDataDisplayStyleType) -> DisplayStyle: ...

class SuperelevationDataDisplayStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.SuperelevationDataDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    Border: int  # = 0
    TitleBox: int  # = 1
    TitleBoxText: int  # = 2
    TicksAtNormalCrown: int  # = 3
    TicksAtShoulderBreakOver: int  # = 4
    TicksAtLevelCrown: int  # = 5
    TicksAtReverseCrown: int  # = 6
    TicksAtFullSuper: int  # = 7
    LabelsAtNormalCrown: int  # = 8
    LabelsAtShoulderBreakOver: int  # = 9
    LabelsAtLevelCrown: int  # = 10
    LabelsAtReverseCrown: int  # = 11
    LabelsAtFullSuper: int  # = 12
    LabelsAlongTransitionSegment: int  # = 13
    ReferenceLine: int  # = 14
    LineLeftOutsideShoulder: int  # = 15
    LineLeftOutsidePavement: int  # = 16
    LineLeftInsidePavement: int  # = 17
    LineLeftInsideShoulder: int  # = 18
    LineRightInsideShoulder: int  # = 19
    LineRightInsidePavement: int  # = 20
    LineRightOutsidePavement: int  # = 21
    LineRightOutsideShoulder: int  # = 22
class SuperelevationViewStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SuperelevationViewStyle"""
    def __init__(self, *args) -> None: ...
    UseSmallTicksAtBottom: bool
    UseSmallTicksAtMiddle: bool
    UseSmallTicksAtTop: bool
    UseFullHeightTick: bool
    AxisBottomMajorTickInterval: float
    AxisTopMajorTickInterval: float
    VerticalUnitHeight: float
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStylePlan(self, type: SuperElevationViewDisplayStyleType) -> DisplayStyle: ...

class SuperelevationViewStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SuperelevationViewStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class SurfaceBaseStyle(CivilWrapper<AeccDbSurfaceStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceBaseStyle"""
    def __init__(self, *args) -> None: ...
    ExaggerateElevationBy: float
    FlattenToElevationBy: float
    DisplayMode: SurfaceDisplay3dType

class SurfaceBoundaryStyle(SurfaceBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceBoundaryStyle"""
    def __init__(self, *args) -> None: ...
    DatumElevation: float
    ProjectGridToDatum: bool
    UseDatum: bool
    DisplayInteriorBoundaries: bool
    DisplayExteriorBoundaries: bool
    ExaggerateElevationBy: float
    FlattenToElevationBy: float
    DisplayMode: SurfaceDisplay3dType

class SurfaceContourStyle(SurfaceBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceContourStyle"""
    def __init__(self, *args) -> None: ...
    SmoothingFactor: int
    SmoothingType: ContourSmoothingType
    SmoothContours: bool
    DepressionTickMarkLength: float
    DepressionTickMarkInterval: float
    DisplayDepressions: bool
    MinorContourColorScheme: ColorSchemeType
    MajorContourColorScheme: ColorSchemeType
    UseColorScheme: bool
    RangePrecision: PrecisionRangeType
    NumberOfRanges: int
    GroupRangeValuesBy: SurfaceGroupValuesByType
    MinorContourInterval: float
    MajorContourInterval: float
    BaseElevationInterval: float
    LegendStyleId: ObjectId
    LegendStyleName: str
    ExaggerateElevationBy: float
    FlattenToElevationBy: float
    DisplayMode: SurfaceDisplay3dType
    def GetContourValues(self, ) -> list: ...
    def SetContourValues(self, contourValuesArray: list) -> None: ...

class SurfaceDirectionStyle(SurfaceBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceDirectionStyle"""
    def __init__(self, *args) -> None: ...
    LegendStyleId: ObjectId
    LegendStyleName: str
    ColorScheme: ColorSchemeType
    DisplayEntityMode: SurfaceDisplayType
    RangePrecision: PrecisionRangeType
    NumberOfRanges: int
    GroupValuesBy: SurfaceGroupValuesByType
    ExaggerateElevationBy: float
    FlattenToElevationBy: float
    DisplayMode: SurfaceDisplay3dType

class SurfaceDisplay3dType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.SurfaceDisplay3dType"""
    def __init__(self, *args) -> None: ...
    UseSurfaceElevation: int  # = 1
    FlattenElevations: int  # = 2
    ExaggerateElevations: int  # = 4
class SurfaceDisplayStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.SurfaceDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    Points: int  # = 0
    Triangles: int  # = 1
    Boundary: int  # = 2
    MajorContour: int  # = 3
    MinorContour: int  # = 4
    UserContours: int  # = 5
    Gridded: int  # = 6
    Directions: int  # = 7
    Elevations: int  # = 8
    Slopes: int  # = 9
    SlopeArrows: int  # = 10
    Watersheds: int  # = 11
class SurfaceDisplayType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.SurfaceDisplayType"""
    def __init__(self, *args) -> None: ...
    Solid2d: int  # = 1
    Faces3d: int  # = 2
    HatchSolid: int  # = 4
    PolyMesh: int  # = 8
class SurfaceElevationStyle(SurfaceBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceElevationStyle"""
    def __init__(self, *args) -> None: ...
    IntervalLength: float
    DataBandingMode: DataBandingType
    LegendStyleId: ObjectId
    LegendStyleName: str
    FillScheme: ColorSchemeType
    CutScheme: ColorSchemeType
    ColorScheme: ColorSchemeType
    DisplayEntityMode: SurfaceDisplayType
    RangePrecision: PrecisionRangeType
    NumberOfRanges: int
    GroupValuesBy: SurfaceGroupValuesByType
    ExaggerateElevationBy: float
    FlattenToElevationBy: float
    DisplayMode: SurfaceDisplay3dType

class SurfaceGridStyle(SurfaceBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceGridStyle"""
    def __init__(self, *args) -> None: ...
    SecondaryGridOrientation: float
    SecondaryGridInterval: float
    UseSecondaryGrid: bool
    PrimaryGridOrientation: float
    PrimaryGridInterval: float
    UsePrimaryGrid: bool
    ExaggerateElevationBy: float
    FlattenToElevationBy: float
    DisplayMode: SurfaceDisplay3dType

class SurfaceGroupValuesByType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.SurfaceGroupValuesByType"""
    def __init__(self, *args) -> None: ...
    EqualInterval: int  # = 0
    Quantile: int  # = 1
    StandardDeviation: int  # = 2
class SurfaceHatchInfo:
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceHatchInfo"""
    def __init__(self, *args) -> None: ...
    PatternDouble: bool
    PatternSpace: float
    PatternAngle: float
    PatternScaleType: bool
    PatternScale: float
    PatternName: str
    PatternType: HatchPatternType
    def SetHatchPattern(self, patternType: HatchPatternType, patternName: str) -> None: ...

class SurfacePointStyle(SurfaceBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfacePointStyle"""
    def __init__(self, *args) -> None: ...
    NondestructivePointsColor: Color
    NondestructivePointsSymbol: PointSymbolType
    DerivedPointsColor: Color
    DerivedPointsSymbol: PointSymbolType
    DataPointsColor: Color
    DataPointsSymbol: PointSymbolType
    Units: float
    ScalingMethodType: ScaleType
    ExaggerateElevationBy: float
    FlattenToElevationBy: float
    DisplayMode: SurfaceDisplay3dType

class SurfaceSlopeArrowStyle(SurfaceBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceSlopeArrowStyle"""
    def __init__(self, *args) -> None: ...
    LegendStyleName: str
    LegendStyleId: ObjectId
    ColorScheme: ColorSchemeType
    ArrowScale: float
    ArrowType: SlopeArrowType
    RangePrecision: PrecisionRangeType
    NumberOfRanges: int
    GroupValuesBy: SurfaceGroupValuesByType
    ExaggerateElevationBy: float
    FlattenToElevationBy: float
    DisplayMode: SurfaceDisplay3dType

class SurfaceSlopeStyle(SurfaceBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceSlopeStyle"""
    def __init__(self, *args) -> None: ...
    LegendStyleName: str
    LegendStyleId: ObjectId
    ColorScheme: ColorSchemeType
    RangePrecision: PrecisionRangeType
    NumberOfRanges: int
    GroupValuesBy: SurfaceGroupValuesByType
    DisplayEntityMode: SurfaceDisplayType
    ExaggerateElevationBy: float
    FlattenToElevationBy: float
    DisplayMode: SurfaceDisplay3dType

class SurfaceStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceStyle"""
    def __init__(self, *args) -> None: ...
    TriangleStyle: SurfaceTriangleStyle
    WatershedStyle: SurfaceWatershedStyle
    SlopeStyle: SurfaceSlopeStyle
    SlopeArrowStyle: SurfaceSlopeArrowStyle
    PointStyle: SurfacePointStyle
    GridStyle: SurfaceGridStyle
    ElevationStyle: SurfaceElevationStyle
    DirectionStyle: SurfaceDirectionStyle
    ContourStyle: SurfaceContourStyle
    BoundaryStyle: SurfaceBoundaryStyle
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStyleModel(self, type: SurfaceDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, type: SurfaceDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStyleSection(self, ) -> DisplayStyle: ...

class SurfaceStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class SurfaceTriangleStyle(SurfaceBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceTriangleStyle"""
    def __init__(self, *args) -> None: ...
    ExaggerateElevationBy: float
    FlattenToElevationBy: float
    DisplayMode: SurfaceDisplay3dType

class SurfaceWatershedStyle(SurfaceBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurfaceWatershedStyle"""
    def __init__(self, *args) -> None: ...
    MultipleDrainNotchStyle: WatershedMultipleDrainNotchStyle
    MultipleDrainStyle: WatershedMultipleDrainStyle
    FlatAreaStyle: WatershedFlatAreaStyle
    DepressionStyle: WatershedDepressionStyle
    BoundarySegmentStyle: WatershedBoundarySegmentStyle
    BoundaryPointStyle: WatershedBoundaryPointStyle
    LabelStyleId: ObjectId
    LabelStyleName: str
    LegendStyleId: ObjectId
    LegendStyleName: str
    PointScalingMethod: ScalingMethodType
    PointUnits: float
    ExaggerateElevationBy: float
    FlattenToElevationBy: float
    DisplayMode: SurfaceDisplay3dType

class SurveyElevationDisplayType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.SurveyElevationDisplayType"""
    def __init__(self, *args) -> None: ...
    UseElevation: int  # = 0
    FlattenElevation: int  # = 1
    ExaggerateElevations: int  # = 2
class SurveyFigureDisplayType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.SurveyFigureDisplayType"""
    def __init__(self, *args) -> None: ...
    FigureLines: int  # = 0
    VertexMarkers: int  # = 1
    MidpointMarkers: int  # = 2
    EndpointMarkers: int  # = 3
    AdditionalMarkers: int  # = 4
class SurveyFigureMarkerPlacementType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.SurveyFigureMarkerPlacementType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    AtInterval: int  # = 1
    DivideFigure: int  # = 2
    Continuous: int  # = 3
class SurveyFigureProfileDisplayType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.SurveyFigureProfileDisplayType"""
    def __init__(self, *args) -> None: ...
    FigureLines: int  # = 0
    BeginningVertexMarker: int  # = 6
    InternalVertexMarker: int  # = 7
    EndingVertexMarker: int  # = 8
class SurveyFigureSectionDisplayType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.SurveyFigureSectionDisplayType"""
    def __init__(self, *args) -> None: ...
    CrossingMarker: int  # = 5
class SurveyFigureStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurveyFigureStyle"""
    def __init__(self, *args) -> None: ...
    CrossingMarkerStyleId: ObjectId
    EndingVertexMarkerStyleId: ObjectId
    InternalVertexMarkerStyleId: ObjectId
    BeginningVertexMarkerStyleId: ObjectId
    ExaggerateElevationBy: float
    FlattenToElevationBy: float
    NetworkDisplayMode: SurveyElevationDisplayType
    PlaceAdditionalMarkerAtFigureEndPoint: bool
    PlaceAdditionalMarkerAtFigureStartPoint: bool
    AdditionalMarkerDivideFigureBy: int
    AdditionalMarkerInterval: float
    AdditionalMarkerPlacementMethod: SurveyFigureMarkerPlacementType
    AlignAdditionalMarkersWithFigure: bool
    AlignEndpointMarkersWithFigure: bool
    AlignMidpointMarkersWithFigure: bool
    AlignVertexMarkersWithFigure: bool
    AdditionalMarkerStyleId: ObjectId
    EndPointMarkerStyleId: ObjectId
    StartPointMarkerStyleId: ObjectId
    MidpointMarkerStyleId: ObjectId
    VertexMarkerStyleId: ObjectId
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStyleModel(self, displayType: SurveyFigureDisplayType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, displayType: SurveyFigureDisplayType) -> DisplayStyle: ...
    def GetDisplayStyleProfile(self, displayType: SurveyFigureProfileDisplayType) -> DisplayStyle: ...
    def GetDisplayStyleSection(self, displayType: SurveyFigureSectionDisplayType) -> DisplayStyle: ...

class SurveyFigureStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurveyFigureStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class SurveyNetworkDisplayStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.SurveyNetworkDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    KnownControlPoints: int  # = 0
    UnknownControlPoints: int  # = 1
    NonControlPoints: int  # = 2
    SideshotPoints: int  # = 3
    NetworkLines: int  # = 4
    DirectionLines: int  # = 5
    SideshotLines: int  # = 6
    ErrorEllipses: int  # = 7
    ToleranceErrorPoints: int  # = 8
    ToleranceErrorLines: int  # = 9
class SurveyNetworkStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurveyNetworkStyle"""
    def __init__(self, *args) -> None: ...
    ExaggerateElevationBy: float
    FlattenToElevationBy: float
    NetworkDisplayMode: SurveyElevationDisplayType
    ErrorEllipseScaleFactor: float
    ToleranceErrorPointsMarkerStyleId: ObjectId
    SideshotPointsMarkerStyleId: ObjectId
    NonControlPointsMarkerStyleId: ObjectId
    UnknownControlPointsMarkerStyleId: ObjectId
    KnownControlPointsMarkerStyleId: ObjectId
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStyleModel(self, type: SurveyNetworkDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, type: SurveyNetworkDisplayStyleType) -> DisplayStyle: ...

class SurveyNetworkStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.SurveyNetworkStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class TableDisplayStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.TableDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    Border: int  # = 0
    TitleSeparator: int  # = 1
    HeaderSeparator: int  # = 2
    DataSeparator: int  # = 3
    DataDivider: int  # = 4
    TitleAreaFill: int  # = 5
    HeaderAreaFill: int  # = 6
    DataAreaFill: int  # = 7
    TitleText: int  # = 8
    HeaderText: int  # = 9
    DataText: int  # = 10
class TableSortingOrderType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.TableSortingOrderType"""
    def __init__(self, *args) -> None: ...
    Descending: int  # = 0
    Ascending: int  # = 1
class TableStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.TableStyle"""
    def __init__(self, *args) -> None: ...
    DataTextDisplayStyleModel: DisplayStyle
    DataTextDisplayStylePlan: DisplayStyle
    HeaderTextDisplayStyleModel: DisplayStyle
    HeaderTextDisplayStylePlan: DisplayStyle
    TitleTextDisplayStyleModel: DisplayStyle
    TitleTextDisplayStylePlan: DisplayStyle
    DataAreaFillDisplayStyleModel: DisplayStyle
    DataAreaFillDisplayStylePlan: DisplayStyle
    HeaderAreaFillDisplayStyleModel: DisplayStyle
    HeaderAreaFillDisplayStylePlan: DisplayStyle
    TitleAreaFillDisplayStyleModel: DisplayStyle
    TitleAreaFillDisplayStylePlan: DisplayStyle
    DataDividerDisplayStyleModel: DisplayStyle
    DataDividerDisplayStylePlan: DisplayStyle
    DataSeparatorDisplayStyleModel: DisplayStyle
    DataSeparatorDisplayStylePlan: DisplayStyle
    HeaderSeparatorDisplayStyleModel: DisplayStyle
    HeaderSeparatorDisplayStylePlan: DisplayStyle
    TitleSeparatorDisplayStyleModel: DisplayStyle
    TitleSeparatorDisplayStylePlan: DisplayStyle
    BorderDisplayStyleModel: DisplayStyle
    BorderDisplayStylePlan: DisplayStyle
    ColumnStyles: ColumnStyleCollection
    DataTextHeight: float
    HeaderTextHeight: float
    TitleTextHeight: float
    DataTextStyle: str
    HeaderTextStyle: str
    TitleTextStyle: str
    MaintainViewOrientation: bool
    EnableWordWrapping: bool
    SortingColumn: int
    SortingOrder: TableSortingOrderType
    SortData: bool
    TransposeSectionViewTable: bool
    RepeatHeaderInSplitTables: bool
    RepeatTitleInSplitTables: bool
    TitleJustification: TextJustificationType
    TitleUnformatted: str
    Title: str
    TableType: TableStyleType
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStyleModel(self, type: TableDisplayStyleType) -> DisplayStyle: ...
    def GetDisplayStylePlan(self, type: TableDisplayStyleType) -> DisplayStyle: ...

class TableStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.TableStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class TableStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.TableStyleType"""
    def __init__(self, *args) -> None: ...
    ParcelArea: int  # = 2
    Point: int  # = 6
    ParcelLine: int  # = 7
    ParcelCurve: int  # = 8
    AlignmentSegment: int  # = 37
    SurfaceDirection: int  # = 41
    SurfaceElevation: int  # = 42
    SurfaceSlope: int  # = 43
    SurfaceSlopeArrow: int  # = 44
    SurfaceContour: int  # = 91
    ParcelSegment: int  # = 131
    AlignmentLine: int  # = 132
    AlignmentCurve: int  # = 133
    AlignmentSpiral: int  # = 134
    Pipe: int  # = 332
    SectionViewTotalVolume: int  # = 333
    SectionViewMaterial: int  # = 334
    Structure: int  # = 335
    SurfaceContoursUser: int  # = 3081
    SurfaceWatershed: int  # = 3083
    QuantityTakeoffTotalVolume: int  # = 3777
    QuantityTakeoffMaterial: int  # = 3778
class TableStylesRoot(TreeOidWrapper):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.TableStylesRoot"""
    def __init__(self, *args) -> None: ...
    SectionViewMaterialTableStyles: TableStyleCollection
    SectionViewTotalVolumeTableStyles: TableStyleCollection
    QuantityTakeoffMaterialTableStyles: TableStyleCollection
    QuantityTakeoffTotalVolumeTableStyles: TableStyleCollection
    StructureTableStyles: TableStyleCollection
    PipeTableStyles: TableStyleCollection
    PointTableStyles: TableStyleCollection
    SurfaceUserDefinedContourTableStyles: TableStyleCollection
    SurfaceWatershedTableStyles: TableStyleCollection
    SurfaceDirectionTableStyles: TableStyleCollection
    SurfaceSlopeArrowContourTableStyles: TableStyleCollection
    SurfaceElevationTableStyles: TableStyleCollection
    SurfaceSlopeTableStyles: TableStyleCollection
    SurfaceContourTableStyles: TableStyleCollection
    ParcelSegmentTableStyles: TableStyleCollection
    ParcelLineTableStyles: TableStyleCollection
    ParcelAreaTableStyles: TableStyleCollection
    ParcelCurveTableStyles: TableStyleCollection
    AlignmentLineTableStyles: TableStyleCollection
    AlignmentSpiralTableStyles: TableStyleCollection
    AlignmentSegmentTableStyles: TableStyleCollection
    AlignmentCurveTableStyles: TableStyleCollection
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class TextForEachComponentSelectedType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.TextForEachComponentSelectedType"""
    def __init__(self, *args) -> None: ...
    Curve: int  # = 419485521
    CurveOrSpiral: int  # = 419485522
    Spiral: int  # = 419485523
    StructureAllPipes: int  # = 419811620
    StructureInFlowPipes: int  # = 419811621
    StructureOutFlowPipes: int  # = 419811622
    IntersectionAllAlignment: int  # = 419930112
class VerticalGeometryBandStyle(BandStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.VerticalGeometryBandStyle"""
    def __init__(self, *args) -> None: ...
    LabelOnlyTangents: bool
    SagCurveTickStyle: BandTickStyle
    CrestCurveTickStyle: BandTickStyle
    DownhillTangentTickStyle: BandTickStyle
    UphillTangentTickStyle: BandTickStyle
    SagCurveLabelStyleId: ObjectId
    CrestCurveLabelStyleId: ObjectId
    DownhillTangentLabelStyleId: ObjectId
    UphillTangentLabelStyleId: ObjectId
    TitleTextLabelStyleId: ObjectId
    BandType: BandType
    WeedingFactor: float
    TextHeight: float
    TextLocation: BandTitleTextLocation
    TextBoxPosition: BandTitleBoxPosition
    OffsetFromBand: float
    TextBoxWidth: float
    BandHeight: float
    Text: str
    TextStyle: str
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetDisplayStylePlan(self, type: VerticalGeometryDisplayStyleType) -> DisplayStyle: ...

class VerticalGeometryDisplayStyleType:
    """.NET enum: Autodesk.Civil.DatabaseServices.Styles.VerticalGeometryDisplayStyleType"""
    def __init__(self, *args) -> None: ...
    Border: int  # = 0
    TitleBox: int  # = 1
    TitleBoxText: int  # = 2
    Ticks: int  # = 3
    TangentLabels: int  # = 4
    CurveLabels: int  # = 5
    TangentGeometry: int  # = 6
    CurveGeometry: int  # = 7
class ViewFrameStyle(StyleBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ViewFrameStyle"""
    def __init__(self, *args) -> None: ...
    ViewFrameBoundaryDisplayStylePlan: DisplayStyle
    DateModified: str
    DateCreated: str
    ModifiedBy: str
    CreateBy: str
    Name: str
    IsUsed: bool
    Description: str
    Document: object
    Application: object
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
    def GetViewFrameBoundaryDisplayStylePlan(self, ) -> DisplayStyle: ...

class ViewFrameStyleCollection(StyleCollectionBase):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.ViewFrameStyleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ObjectId
    Item: ObjectId
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, name: str) -> ObjectId: ...

class WatershedBaseStyle(CivilWrapper<AeccDbSurfaceStyle>):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.WatershedBaseStyle"""
    def __init__(self, *args) -> None: ...
    Hatch: SurfaceHatchInfo
    HatchPattern: str
    UseHatching: bool
    LinetypeId: ObjectId
    LinetypeName: str
    Color: Color

class WatershedBoundaryPointStyle(WatershedDrainPointStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.WatershedBoundaryPointStyle"""
    def __init__(self, *args) -> None: ...
    PointColor: Color
    PointDisplayType: PointSymbolType
    DrawDrainPoint: bool
    Hatch: SurfaceHatchInfo
    HatchPattern: str
    UseHatching: bool
    LinetypeId: ObjectId
    LinetypeName: str
    Color: Color

class WatershedBoundarySegmentStyle(WatershedDrainSegmentStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.WatershedBoundarySegmentStyle"""
    def __init__(self, *args) -> None: ...
    SegmentColor: Color
    SegmentLinetypeId: ObjectId
    SegmentLinetypeName: str
    DrawDrainSegment: bool
    Hatch: SurfaceHatchInfo
    HatchPattern: str
    UseHatching: bool
    LinetypeId: ObjectId
    LinetypeName: str
    Color: Color

class WatershedDepressionStyle(WatershedDrainPointSegmentStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.WatershedDepressionStyle"""
    def __init__(self, *args) -> None: ...
    SegmentColor: Color
    SegmentLinetypeId: ObjectId
    SegmentLinetypeName: str
    DrawDrainSegment: bool
    PointColor: Color
    PointDisplayType: PointSymbolType
    DrawDrainPoint: bool
    Hatch: SurfaceHatchInfo
    HatchPattern: str
    UseHatching: bool
    LinetypeId: ObjectId
    LinetypeName: str
    Color: Color

class WatershedDrainPointSegmentStyle(WatershedBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.WatershedDrainPointSegmentStyle"""
    def __init__(self, *args) -> None: ...
    SegmentColor: Color
    SegmentLinetypeId: ObjectId
    SegmentLinetypeName: str
    DrawDrainSegment: bool
    PointColor: Color
    PointDisplayType: PointSymbolType
    DrawDrainPoint: bool
    Hatch: SurfaceHatchInfo
    HatchPattern: str
    UseHatching: bool
    LinetypeId: ObjectId
    LinetypeName: str
    Color: Color

class WatershedDrainPointStyle(WatershedBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.WatershedDrainPointStyle"""
    def __init__(self, *args) -> None: ...
    PointColor: Color
    PointDisplayType: PointSymbolType
    DrawDrainPoint: bool
    Hatch: SurfaceHatchInfo
    HatchPattern: str
    UseHatching: bool
    LinetypeId: ObjectId
    LinetypeName: str
    Color: Color

class WatershedDrainSegmentStyle(WatershedBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.WatershedDrainSegmentStyle"""
    def __init__(self, *args) -> None: ...
    SegmentColor: Color
    SegmentLinetypeId: ObjectId
    SegmentLinetypeName: str
    DrawDrainSegment: bool
    Hatch: SurfaceHatchInfo
    HatchPattern: str
    UseHatching: bool
    LinetypeId: ObjectId
    LinetypeName: str
    Color: Color

class WatershedFlatAreaStyle(WatershedBaseStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.WatershedFlatAreaStyle"""
    def __init__(self, *args) -> None: ...
    Hatch: SurfaceHatchInfo
    HatchPattern: str
    UseHatching: bool
    LinetypeId: ObjectId
    LinetypeName: str
    Color: Color

class WatershedMultipleDrainNotchStyle(WatershedDrainSegmentStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.WatershedMultipleDrainNotchStyle"""
    def __init__(self, *args) -> None: ...
    SegmentColor: Color
    SegmentLinetypeId: ObjectId
    SegmentLinetypeName: str
    DrawDrainSegment: bool
    Hatch: SurfaceHatchInfo
    HatchPattern: str
    UseHatching: bool
    LinetypeId: ObjectId
    LinetypeName: str
    Color: Color

class WatershedMultipleDrainStyle(WatershedDrainPointStyle):
    """.NET: Autodesk.Civil.DatabaseServices.Styles.WatershedMultipleDrainStyle"""
    def __init__(self, *args) -> None: ...
    PointColor: Color
    PointDisplayType: PointSymbolType
    DrawDrainPoint: bool
    Hatch: SurfaceHatchInfo
    HatchPattern: str
    UseHatching: bool
    LinetypeId: ObjectId
    LinetypeName: str
    Color: Color
