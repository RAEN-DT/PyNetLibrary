# Auto-generated — Civil 26 — Autodesk.Aec.ApplicationServices

class AecApplicationVersion(DisposableWrapper):
    """.NET: Autodesk.Aec.ApplicationServices.AecApplicationVersion"""
    def __init__(self, *args) -> None: ...
    BuildMinor: int
    BuildMajor: int
    Minor: int
    Major: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Base() -> AecApplicationVersion: ...
    def DwgInFields(self, filer: DwgFiler) -> None: ...
    def DwgOutFields(self, filer: DwgFiler) -> None: ...
    @staticmethod
    def Specific(major: int, minor: int, buildMajor: int, buildMinor: int) -> AecApplicationVersion: ...

class DBVariables(DictionaryRecord):
    """.NET: Autodesk.Aec.ApplicationServices.DBVariables"""
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

class DatabaseDataManager(RXObject):
    """.NET: Autodesk.Aec.ApplicationServices.DatabaseDataManager"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetAllDatabaseData(self, ) -> list: ...
    def GetDatabaseData(self, database: Database) -> DatabaseData: ...

class DatabaseDataManagerDictionary(RXObject):
    """.NET: Autodesk.Aec.ApplicationServices.DatabaseDataManagerDictionary"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def GetManager(keyName: str) -> DatabaseDataManager: ...
    @staticmethod
    def GetManagers() -> DBObjectCollection: ...
    @staticmethod
    def RegisterPacketType(keyName: str, packetClassType: RXClass) -> None: ...
    @staticmethod
    def UnRegisterPacketType(keyName: str) -> None: ...

class DrawingSetupVariables(DBVariables):
    """.NET: Autodesk.Aec.ApplicationServices.DrawingSetupVariables"""
    def __init__(self, *args) -> None: ...
    GeometrySharingEnabled: bool
    BlockBasedLayerOffBehavior: bool
    XrefOverlaysUseOwnDisplayConfig: bool
    CreateDimOverride: bool
    AlwaysUpdateLayerKeyStyle: bool
    LastLayerStyleUpdate: int
    CurrentDimUnit: BuiltInUnit
    ElevationLabelPlusMinus: bool
    ElevationLabelPlus: bool
    SuperScriptZeroSupression: bool
    SuperScript: bool
    LayerFile: str
    MaxFacetsOnCircle: int
    FacetDeviation: float
    IsMetric: bool
    LayerStandardLegacy: str
    LayerStandard: str
    ProjectName: str
    CivilDimaltf: float
    CivilDimscale: float
    CivilDimexo: float
    CivilDimapost: str
    CivilDimpost: str
    CivilTextStyle: str
    CivilDimaltd: int
    CivilStateFlag3: int
    CivilStateFlag2: int
    CivilStateFlag1: int
    VolumeSuffix: str
    VolumePrecision: int
    VolumeDisplayUnit: BuiltInUnit
    AreaSuffix: str
    AreaPrecision: int
    AreaDisplayUnit: BuiltInUnit
    TextHeight: float
    VerticalScale: float
    DwgScale: float
    AecNorthRotation: float
    AecBasePtNE: Point3d
    AecDwgBasePt: Point3d
    CoordinatePrecision: int
    ElevationPrecision: int
    AngularPrecision: int
    AngularAzimuth: int
    AngularDisplayFormat: int
    LinearPrecision: int
    LinearDisplayFormat: int
    LinearUnit: BuiltInUnit
    ScaleOnInsert: bool
    UnitType: MeasurementValue
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
    def ConvertToCurrentAreaDisplay(self, area: float) -> float: ...
    def ConvertToCurrentVolumeDisplay(self, volume: float) -> float: ...
    @staticmethod
    def GetInstance(db: Database, createIfNotFound: bool) -> ObjectId: ...
    def SaveAsDefault(self, ) -> None: ...

class LegacyDrawingUnitMode:
    """.NET enum: Autodesk.Aec.ApplicationServices.LegacyDrawingUnitMode"""
    def __init__(self, *args) -> None: ...
    Automatic: int  # = 0
    Imperial: int  # = 1
    Metric: int  # = 2
class Preferences:
    """.NET: Autodesk.Aec.ApplicationServices.Preferences"""
    def __init__(self, *args) -> None: ...
    EnableProgressiveUpdate: bool
    DisableOsnapGsMarkerOptimization: bool
    AllowSnapToSurfaceHatch: bool
    ExportExplodedToAcadExportFormat: DwgVersion
    ExportExplodedToAcadInsertWhenBinding: bool
    ExportExplodedToAcadBindXrefs: bool
    ExportExplodedToAcadFileSuffix: str
    ExportExplodedToAcadFilePrefix: str
    PlotOrPublishWarningSymbol: bool
    DraftWarningSymbol: bool
    LegacyDrawingUnitMode: LegacyDrawingUnitMode
    MaintainExplodedObjectBlockProperties: bool
    GeometryDiagnostics: bool
    ViewManagementSystemDiagnostics: bool
    ApplyCommonProperties: bool
    QuickOsnapMode: bool
    DisplayEnhancedReferenceObjectRelationshipGraphMessages: bool
    ObjectRelationshipGraphDiagnostics: bool
    @staticmethod
    def GetApplyCommonProperties(fromRegistry: bool) -> bool: ...
    @staticmethod
    def GetDisplayEnhancedReferenceObjectRelationshipGraphMessages(fromRegistry: bool) -> bool: ...
    @staticmethod
    def GetDraftWarningSymbol(fromRegistry: bool) -> bool: ...
    @staticmethod
    def GetEnableProgressiveUpdate(fromRegistry: bool) -> bool: ...
    @staticmethod
    def GetExportExplodedToAcadBindXrefs(fromRegistry: bool) -> bool: ...
    @staticmethod
    def GetExportExplodedToAcadExportFormat(fromRegistry: bool) -> DwgVersion: ...
    @staticmethod
    def GetExportExplodedToAcadFilePrefix(fromRegistry: bool) -> str: ...
    @staticmethod
    def GetExportExplodedToAcadFileSuffix(fromRegistry: bool) -> str: ...
    @staticmethod
    def GetExportExplodedToAcadInsertWhenBinding(fromRegistry: bool) -> bool: ...
    @staticmethod
    def GetGeometryDiagnostics(fromRegistry: bool) -> bool: ...
    @staticmethod
    def GetLegacyDrawingUnitMode(fromRegistry: bool) -> LegacyDrawingUnitMode: ...
    @staticmethod
    def GetMaintainExplodedObjectBlockProperties(fromRegistry: bool) -> bool: ...
    @staticmethod
    def GetObjectRelationshipGraphDiagnostics(fromRegistry: bool) -> bool: ...
    @staticmethod
    def GetPlotOrPublishWarningSymbol(fromRegistry: bool) -> bool: ...
    @staticmethod
    def GetQuickOsnapMode(fromRegistry: bool) -> bool: ...
    @staticmethod
    def GetViewManagementSystemDiagnostics(fromRegistry: bool) -> bool: ...
    @staticmethod
    def SetApplyCommonProperties(enabled: bool, updateVariable: bool, updateRegistry: bool) -> None: ...
    @staticmethod
    def SetDisplayEnhancedReferenceObjectRelationshipGraphMessages(enabled: bool, updateVariable: bool, updateRegistry: bool) -> None: ...
    @staticmethod
    def SetDraftWarningSymbol(enabled: bool, updateVariable: bool, updateRegistry: bool) -> None: ...
    @staticmethod
    def SetEnableProgressiveUpdate(enable: bool, updateVar: bool, updateReg: bool) -> None: ...
    @staticmethod
    def SetExportExplodedToAcadBindXrefs(enabled: bool, updateVariable: bool, updateRegistry: bool) -> None: ...
    @staticmethod
    def SetExportExplodedToAcadExportFormat(dwgFormat: DwgVersion, updateVariable: bool, updateRegistry: bool) -> None: ...
    @staticmethod
    def SetExportExplodedToAcadFilePrefix(prefix: str, updateVariable: bool, updateRegistry: bool) -> None: ...
    @staticmethod
    def SetExportExplodedToAcadFileSuffix(suffix: str, updateVariable: bool, updateRegistry: bool) -> None: ...
    @staticmethod
    def SetExportExplodedToAcadInsertWhenBinding(enabled: bool, updateVariable: bool, updateRegistry: bool) -> None: ...
    @staticmethod
    def SetGeometryDiagnostics(enabled: bool, updateVariable: bool, updateRegistry: bool) -> None: ...
    @staticmethod
    def SetLegacyDrawingUnitMode(mode: LegacyDrawingUnitMode, updateVariable: bool, updateRegistry: bool) -> None: ...
    @staticmethod
    def SetMaintainExplodedObjectBlockProperties(enabled: bool, updateVariable: bool, updateRegistry: bool) -> None: ...
    @staticmethod
    def SetObjectRelationshipGraphDiagnostics(enabled: bool, updateVariable: bool, updateRegistry: bool) -> None: ...
    @staticmethod
    def SetPlotOrPublishWarningSymbol(enabled: bool, updateVariable: bool, updateRegistry: bool) -> None: ...
    @staticmethod
    def SetQuickOsnapMode(enabled: bool, updateVariable: bool, updateRegistry: bool) -> None: ...
    @staticmethod
    def SetViewManagementSystemDiagnostics(enabled: bool, updateVariable: bool, updateRegistry: bool) -> None: ...
