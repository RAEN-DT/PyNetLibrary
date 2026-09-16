# Auto-generated — Civil 26 — Autodesk.Aec.PropertyData.DatabaseServices

class AnchorExtendedTagToEntity(AnchorTagToEntity):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.AnchorExtendedTagToEntity"""
    def __init__(self, *args) -> None: ...
    AllowIndependentUpdate: bool
    ForceHorizontal: bool
    ReferencedEntityId: ObjectId
    EntityId: ObjectId
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
    def SetReferencedEntityId(self, geo: Geo) -> None: ...
    def SetReferencedEntityOldEcs(self, mat: Matrix3d) -> None: ...

class AnchorTagToEntity(AnchorToReference):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.AnchorTagToEntity"""
    def __init__(self, *args) -> None: ...
    EntityId: ObjectId
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
    def SetOverride(self, entityId: ObjectId, blockReferencePath: ObjectIdCollection) -> None: ...

class AutomaticPropertyData:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.AutomaticPropertyData"""
    def __init__(self, *args) -> None: ...
    SourceName: str
    ClassName: str

class CaseType:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.CaseType"""
    def __init__(self, *args) -> None: ...
    ...

class DictionaryPropertyDataFormat(Dictionary):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.DictionaryPropertyDataFormat"""
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
    def GetStandardFormat(db: Database) -> ObjectId: ...

class DictionaryPropertySetDefinitions(Dictionary):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.DictionaryPropertySetDefinitions"""
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

class DictionaryScheduleTableStyle(Dictionary):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.DictionaryScheduleTableStyle"""
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

class DisplayThemeScheduleDataRule(DisplayThemeRuleBase):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.DisplayThemeScheduleDataRule"""
    def __init__(self, *args) -> None: ...
    PropertyDefinitionId: int
    PropertySetDefinitionId: ObjectId
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
    @staticmethod
    def GetValidPropertySetDefinitions(db: Database, validAvailablePropertyDefinitionSets: NameObjectIdPairCollection) -> bool: ...
    def SetPropertyDefinitionId(self, id: int, isUpdate: bool) -> None: ...
    def SetPropertySetDefinitionId(self, id: ObjectId, isUpdate: bool) -> None: ...

class DisplayThemeScheduleDataRuleParameter:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.DisplayThemeScheduleDataRuleParameter"""
    def __init__(self, *args) -> None: ...
    ...

class DxfData:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.DxfData"""
    def __init__(self, *args) -> None: ...
    ...

class ForwardedType:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.ForwardedType"""
    def __init__(self, *args) -> None: ...
    ...

class FractionType:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.FractionType"""
    def __init__(self, *args) -> None: ...
    ...

class GraphicType:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.GraphicType"""
    def __init__(self, *args) -> None: ...
    ...

class INodeOperation:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.INodeOperation"""
    def __init__(self, *args) -> None: ...
    def Add(self, A_0: ScheduleTableStyleHeaderNode) -> int: ...
    def Contains(self, A_0: ScheduleTableStyleHeaderNode) -> bool: ...
    def GetAt(self, A_0: int) -> ScheduleTableStyleHeaderNode: ...
    def GetCount(self, ) -> int: ...
    def IndexOf(self, A_0: ScheduleTableStyleHeaderNode) -> int: ...
    def Insert(self, A_0: int, A_1: ScheduleTableStyleHeaderNode) -> None: ...
    def Prepend(self, A_0: ScheduleTableStyleHeaderNode) -> None: ...
    def Remove(self, A_0: ScheduleTableStyleHeaderNode) -> None: ...
    def RemoveAll(self, ) -> None: ...
    def RemoveAt(self, A_0: int) -> None: ...
    def SetAt(self, A_0: int, A_1: ScheduleTableStyleHeaderNode) -> None: ...
    def Shift(self, A_0: ScheduleTableStyleHeaderNode, A_1: int) -> None: ...

class IScheduleTablePageMaxHeightOperation:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.IScheduleTablePageMaxHeightOperation"""
    def __init__(self, *args) -> None: ...
    def Add(self, A_0: float) -> int: ...
    def GetAt(self, A_0: int) -> float: ...
    def GetCount(self, ) -> int: ...
    def IndexOf(self, A_0: float) -> int: ...
    def Insert(self, index: int, value: float) -> None: ...
    def RemoveAll(self, ) -> None: ...
    def RemoveAt(self, A_0: int) -> None: ...
    def SetAt(self, A_0: int, A_1: float) -> None: ...

class IScheduleTableSortingOperation:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.IScheduleTableSortingOperation"""
    def __init__(self, *args) -> None: ...
    def Add(self, A_0: ScheduleTableSorting) -> int: ...
    def GetAt(self, A_0: int) -> ScheduleTableSorting: ...
    def GetCount(self, ) -> int: ...
    def IndexOf(self, A_0: ScheduleTableSorting) -> int: ...
    def Insert(self, index: int, value: ScheduleTableSorting) -> None: ...
    def RemoveAll(self, ) -> None: ...
    def RemoveAt(self, A_0: int) -> None: ...
    def Swap(self, index1: int, index2: int) -> None: ...

class IScheduleTableStyleColumnOperation:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.IScheduleTableStyleColumnOperation"""
    def __init__(self, *args) -> None: ...
    def Add(self, A_0: ScheduleTableStyleColumn) -> int: ...
    def GetAt(self, A_0: int) -> ScheduleTableStyleColumn: ...
    def GetCount(self, ) -> int: ...
    def IndexOf(self, propSetDefId: ObjectId, propId: int) -> int: ...
    def Insert(self, A_0: int, A_1: ScheduleTableStyleColumn) -> None: ...
    def Prepend(self, A_0: ScheduleTableStyleColumn) -> None: ...
    def RemoveAll(self, ) -> None: ...
    def RemoveAt(self, A_0: int) -> None: ...
    def SetAt(self, A_0: int, A_1: ScheduleTableStyleColumn) -> None: ...

class MatrixSymbolType:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.MatrixSymbolType"""
    def __init__(self, *args) -> None: ...
    ...

class PageDirectionType:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.PageDirectionType"""
    def __init__(self, *args) -> None: ...
    ...

class Precision:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.Precision"""
    def __init__(self, *args) -> None: ...
    ...

class ProjectDataType:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.ProjectDataType"""
    def __init__(self, *args) -> None: ...
    ...

class PropertyDataFormat(DictionaryRecord):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.PropertyDataFormat"""
    def __init__(self, *args) -> None: ...
    BuiltinType: BuiltInType
    UnitType: UnitType
    Scale: float
    RoundingMode: RoundingType
    SeparatorComma: SeparatorType
    NotApplicable: str
    Undefined: str
    FalseText: str
    TrueText: str
    ZeroPadding: int
    RoundOff: float
    ZeroInches: bool
    ZeroFeet: bool
    TrailingZeros: bool
    LeadingZeros: bool
    Fraction: FractionType
    Separator: SeparatorType
    Precision: int
    Units: UnitsType
    Case: CaseType
    Suffix: str
    Prefix: str
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
    @staticmethod
    def Convert(data: object, currentUnitType: UnitType, targetUnitType: UnitType) -> object: ...
    def DoRoundOff(self, value: float) -> float: ...
    def FormatObject(self, object: object, unitType: UnitType, es: ErrorStatus, plainText: bool) -> str: ...
    def FormatObjectExtend(self, object: object, unitType: UnitType, plainText: bool) -> str: ...
    def FormatToObject(self, object: object, unitType: UnitType) -> object: ...
    @staticmethod
    def FormatValues(readStatus: ErrorStatus, idPropertyFormat: ObjectId, unitType: UnitType, propValue: object, propFormatted: object) -> bool: ...
    @staticmethod
    def ReadErrorValueMessage() -> str: ...

class PropertyDataServices:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.PropertyDataServices"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def AddExtendedClasses(entityFilter: StringCollection) -> None: ...
    @staticmethod
    def AddPropertySet(id: ObjectId, idOverrideContainerOwner: ObjectId, blockRefPath: ObjectIdCollection, propertySetDefinitionId: ObjectId) -> None: ...
    @staticmethod
    def DataToString(variantObject: object) -> str: ...
    @staticmethod
    def ExtractExtendedObjects(id: ObjectId) -> ObjectIdCollection: ...
    @staticmethod
    def FindAutomaticSourceNames(objectName: str, db: Database) -> list: ...
    @staticmethod
    def FindEligibleClassNames() -> list: ...
    @staticmethod
    def FindOverrideContainer(idBlockReference: ObjectId, createIfNotFound: bool) -> ObjectId: ...
    @staticmethod
    def FormatValue(idPropertyFormat: ObjectId, unitType: UnitType, propertyValue: object, readStatus: ErrorStatus) -> object: ...
    @staticmethod
    def GetAllPropertySetsUsingDefinition(propertySetDefinition: ObjectId, allowErased: bool) -> ObjectIdCollection: ...
    @staticmethod
    def GetNearestPropertySet(objectInstance: DBObject, blockRefPath: ObjectIdCollection, propertySetDefinitionId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetPropertySet(id: ObjectId, idOverrideContainerOwner: ObjectId, blockRefPath: ObjectIdCollection, propertySetDefinitionId: ObjectId) -> ObjectId: ...
    @staticmethod
    def GetPropertySetDefinitionsUsed(id: ObjectId, idOverrideContainerOwner: ObjectId, blockRefPath: ObjectIdCollection) -> ObjectIdCollection: ...
    @staticmethod
    def GetPropertySets(id: ObjectId, idOverrideContainerOwner: ObjectId, blockRefPath: ObjectIdCollection) -> ObjectIdCollection: ...
    @staticmethod
    def GetPropertyValueExt(dbObject: DBObject, blockReferencePath: ObjectIdCollection, propertySetDefinitionId: ObjectId, propertyId: int) -> object: ...
    @staticmethod
    def GetPropertyValueUnitExt(dbObject: DBObject, blockReferencePath: ObjectIdCollection, propertySetDefinitionId: ObjectId, propertyId: int, searchByName: bool) -> PropertyValueUnitPair: ...
    @staticmethod
    def PropertyExists(db: Database, fullPropertyName: str, propertyId: int) -> ObjectId: ...
    @staticmethod
    def PurgeDuplicatePropertySets(obj: DBObject, verbose: bool) -> None: ...
    @staticmethod
    def RemovePropertySet(id: ObjectId, idOverrideContainerOwner: ObjectId, blockRefPath: ObjectIdCollection, propertySetDefinitionId: ObjectId) -> None: ...
    @staticmethod
    def ResolvePropertySetLocations(originalIds: ObjectIdCollection, resolvedIds: ObjectIdCollection, forwardedIds: ObjectIdCollection, duplicateIds: ObjectIdCollection) -> None: ...
    @staticmethod
    def ResolvePropertySetLocationsAndFilterLockedLayers(originalIds: ObjectIdCollection, resolvedIds: ObjectIdCollection, forwardedIds: ObjectIdCollection, duplicateIds: ObjectIdCollection, lockedIds: ObjectIdCollection, speak: bool) -> None: ...
    @staticmethod
    def SearchPathForPropertySet(entityId: ObjectId, blockRefPathIds: ObjectIdCollection, propertySetName: str) -> ObjectId: ...
    @staticmethod
    def UsePropertySetExclusive(propertySetDefinitionId: ObjectId, entityFilter: StringCollection, filterReadOnlySets: bool, filterHiddenSets: bool, includeExtendedClasses: bool, matchTypes: bool, entitiesAreStyles: bool) -> bool: ...
    @staticmethod
    def UsePropertySetExclusiveMatchClassifications(propertySetDefinitionId: ObjectId, entityFilter: StringCollection, matchingClassifications: ClassificationCollection, filterReadOnlySets: bool, filterHiddenSets: bool, includeExtendedClasses: bool, matchTypes: bool, entitiesAreStyles: bool) -> bool: ...
    @staticmethod
    def UsePropertySetExclusiveMatchEntityClassifications(propertySetDefinitionId: ObjectId, entityFilter: StringCollection, matchingEntities: ObjectIdCollection, filterReadOnlySets: bool, filterHiddenSets: bool, includeExtendedClasses: bool, matchTypes: bool, entitiesAreStyles: bool) -> bool: ...
    @staticmethod
    def UsePropertySetInclusive(propertySetDefinitionId: ObjectId, entityFilter: StringCollection, filterReadOnlySets: bool, filterHiddenSets: bool, includeExtendedClasses: bool, matchTypes: bool, entitiesAreStyles: bool) -> bool: ...
    @staticmethod
    def UsePropertySetInclusiveMatchClassifications(propertySetDefinitionId: ObjectId, entityFilter: StringCollection, matchingClassifications: ClassificationCollection, filterReadOnlySets: bool, filterHiddenSets: bool, includeExtendedClasses: bool, matchTypes: bool, entitiesAreStyles: bool) -> bool: ...

class PropertyDefinition(ImpObject):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.PropertyDefinition"""
    def __init__(self, *args) -> None: ...
    DisplayOrder: int
    IsVisible: bool
    IsReadOnly: bool
    FieldBucketId: str
    ContainsFields: bool
    UnitType: UnitType
    IsLocked: bool
    DefaultIsUnspecified: bool
    Automatic: bool
    ListDefinitionId: ObjectId
    ExampleString: str
    FormatString: str
    FormatId: ObjectId
    DefaultData: object
    DataType: DataType
    Id: int
    GlobalName: str
    Name: str
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def ClearAutomaticData(self, ) -> None: ...
    def ClearFieldData(self, ) -> None: ...
    def GetAutomaticData(self, ) -> list: ...
    def GetFieldGeneratedData(self, asFieldCode: bool) -> object: ...
    def GetFieldId(self, ) -> ObjectId: ...
    def GetSampleValue(self, unitType: UnitType) -> object: ...
    @staticmethod
    def References(propertySetDefinitionId: ObjectId, propertyDefinitionId: int, propertySetDefinitionId2: ObjectId, propertyDefinitionId2: int) -> bool: ...
    def RemoveAutomaticData(self, className: str) -> None: ...
    def SetAutomaticData(self, className: str, sourceName: str) -> None: ...
    def Synchronize(self, propertySet: PropertySet, definition: PropertySetDefinition, attachedTo: DBObject) -> None: ...
    def Value(self, dbObject: DBObject, blockRefPath: ObjectIdCollection) -> object: ...

class PropertyDefinitionAnchor(PropertyDefinition):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.PropertyDefinitionAnchor"""
    def __init__(self, *args) -> None: ...
    DisplayString: str
    Valid: bool
    UsePropertyDefinitionNamesForDescription: bool
    PropertyDefinitionId: int
    PropertySetDefinitionId: ObjectId
    DisplayOrder: int
    IsVisible: bool
    IsReadOnly: bool
    FieldBucketId: str
    ContainsFields: bool
    UnitType: UnitType
    IsLocked: bool
    DefaultIsUnspecified: bool
    Automatic: bool
    ListDefinitionId: ObjectId
    ExampleString: str
    FormatString: str
    FormatId: ObjectId
    DefaultData: object
    DataType: DataType
    Id: int
    GlobalName: str
    Name: str
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def ExtractAnchoredToObject(A_0: Geo) -> ObjectId: ...

class PropertyDefinitionClassification(PropertyDefinition):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.PropertyDefinitionClassification"""
    def __init__(self, *args) -> None: ...
    Valid: bool
    UseClassificationNamesForDescription: bool
    PropertyDefinitionId: int
    PropertySetDefinitionId: ObjectId
    ClassificationDefinitionId: ObjectId
    DisplayOrder: int
    IsVisible: bool
    IsReadOnly: bool
    FieldBucketId: str
    ContainsFields: bool
    UnitType: UnitType
    IsLocked: bool
    DefaultIsUnspecified: bool
    Automatic: bool
    ListDefinitionId: ObjectId
    ExampleString: str
    FormatString: str
    FormatId: ObjectId
    DefaultData: object
    DataType: DataType
    Id: int
    GlobalName: str
    Name: str
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PropertyDefinitionCollection:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.PropertyDefinitionCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: PropertyDefinition
    def Add(self, value: PropertyDefinition) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: PropertyDefinition) -> bool: ...
    def CopyTo(self, array: list, start: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, propertyName: str) -> int: ...
    def Insert(self, index: int, value: PropertyDefinition) -> None: ...
    def Remove(self, value: PropertyDefinition) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class PropertyDefinitionFormula(PropertyDefinition):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.PropertyDefinitionFormula"""
    def __init__(self, *args) -> None: ...
    DataItems: list
    EnableQuantity: bool
    HasQuantity: bool
    DisplayStringClean: str
    DisplayString: str
    UseFormulaForDescription: bool
    FormulaString: str
    DisplayOrder: int
    IsVisible: bool
    IsReadOnly: bool
    FieldBucketId: str
    ContainsFields: bool
    UnitType: UnitType
    IsLocked: bool
    DefaultIsUnspecified: bool
    Automatic: bool
    ListDefinitionId: ObjectId
    ExampleString: str
    FormatString: str
    FormatId: ObjectId
    DefaultData: object
    DataType: DataType
    Id: int
    GlobalName: str
    Name: str
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetFormulaString(self, ) -> str: ...
    def SetFormulaString(self, formulaString: str) -> bool: ...
    def Value(self, dbObject: DBObject, blockRefPath: ObjectIdCollection, quantity: int) -> object: ...

class PropertyDefinitionFormulaDataItem(ImpObject):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.PropertyDefinitionFormulaDataItem"""
    def __init__(self, *args) -> None: ...
    DisplayString: str
    FormatId: ObjectId
    Sample: object
    IsProperty: bool
    IsQuantity: bool
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetSampleToDefault(self, ) -> None: ...

class PropertyDefinitionGraphic(PropertyDefinition):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.PropertyDefinitionGraphic"""
    def __init__(self, *args) -> None: ...
    SupportedImageTypes: str
    UsePropertyDefinitionNamesForDescription: bool
    Rotation: float
    LayerKey: str
    ImageFileNameStripped: str
    ImageFileName: str
    BlockId: ObjectId
    BlockName: str
    GraphicType: GraphicType
    DisplayOrder: int
    IsVisible: bool
    IsReadOnly: bool
    FieldBucketId: str
    ContainsFields: bool
    UnitType: UnitType
    IsLocked: bool
    DefaultIsUnspecified: bool
    Automatic: bool
    ListDefinitionId: ObjectId
    ExampleString: str
    FormatString: str
    FormatId: ObjectId
    DefaultData: object
    DataType: DataType
    Id: int
    GlobalName: str
    Name: str
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetDisplayString(self, graphicType: GraphicType) -> str: ...
    def SetImageFileName(self, fileName: str, fileNameStripped: str) -> None: ...

class PropertyDefinitionLocation(PropertyDefinition):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.PropertyDefinitionLocation"""
    def __init__(self, *args) -> None: ...
    DisplayString: str
    Valid: bool
    UsePropertyDefinitionNamesForDescription: bool
    PropertyDefinitionId: int
    PropertySetDefinitionId: ObjectId
    AppliesTo: RXClass
    DisplayOrder: int
    IsVisible: bool
    IsReadOnly: bool
    FieldBucketId: str
    ContainsFields: bool
    UnitType: UnitType
    IsLocked: bool
    DefaultIsUnspecified: bool
    Automatic: bool
    ListDefinitionId: ObjectId
    ExampleString: str
    FormatString: str
    FormatId: ObjectId
    DefaultData: object
    DataType: DataType
    Id: int
    GlobalName: str
    Name: str
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetAppliesTo(self, A_0: str) -> None: ...

class PropertyDefinitionProject(PropertyDefinition):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.PropertyDefinitionProject"""
    def __init__(self, *args) -> None: ...
    UseProjectInfoForDescription: bool
    ProjectDetailName: str
    ProjectDetailCategory: str
    ProjectDataType: ProjectDataType
    DisplayOrder: int
    IsVisible: bool
    IsReadOnly: bool
    FieldBucketId: str
    ContainsFields: bool
    UnitType: UnitType
    IsLocked: bool
    DefaultIsUnspecified: bool
    Automatic: bool
    ListDefinitionId: ObjectId
    ExampleString: str
    FormatString: str
    FormatId: ObjectId
    DefaultData: object
    DataType: DataType
    Id: int
    GlobalName: str
    Name: str
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetDisplayString(self, dataType: ProjectDataType) -> str: ...

class PropertySet(DictionaryRecord):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.PropertySet"""
    def __init__(self, *args) -> None: ...
    PropertySetData: PropertySetDataCollection
    PropertySetDefinitionName: str
    PropertySetDefinition: ObjectId
    ObjectAttachedTo: ObjectId
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
    @staticmethod
    def CompareAlphaIncrementValues(string1: str, string2: str) -> int: ...
    def GetAt(self, dbObject: DBObject, blockRefPath: ObjectIdCollection, propertyId: int, unitType: UnitType) -> object: ...
    def GetCurrentAlphaIncrementValue(self, propertySetDefinition: PropertySetDefinition, propertyId: int) -> str: ...
    def GetCurrentAutoIncrementValue(self, propertySetDefinition: PropertySetDefinition, propertyId: int) -> int: ...
    def GetPropertySetDataAt(self, propertyId: int) -> PropertySetData: ...
    def GetValueAndUnitAt(self, id: ObjectId, blockRefPath: ObjectIdCollection, propertyId: int) -> PropertyValueUnitPair: ...
    @staticmethod
    def IncrementAlphaValue(alpha: str) -> str: ...
    def PropertyIdToName(self, propertyId: int) -> str: ...
    def PropertyNameToId(self, name: str) -> int: ...
    def SetAt(self, propertyId: int, data: float, unitType: UnitType) -> None: ...
    def Synchronize(self, propertySetDefinition: PropertySetDefinition, db: DBObject) -> None: ...
    def UpdateAutoIncrementProperties(self, ) -> None: ...
    def UpdateReferencingAttributes(self, ) -> None: ...

class PropertySetData(ImpObject):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.PropertySetData"""
    def __init__(self, *args) -> None: ...
    UnitType: UnitType
    FieldBucketId: str
    ContainsFields: bool
    IsUnspecified: bool
    DataType: DataType
    Id: int
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def ClearFieldData(self, ) -> None: ...
    def CopyFrom(self, other: RXObject) -> None: ...
    def GetData(self, unitType: UnitType) -> object: ...
    def GetFieldGeneratedData(self, asFieldCode: bool) -> object: ...
    def GetFieldId(self, ) -> ObjectId: ...
    def SetData(self, data: object, unitType: UnitType) -> None: ...

class PropertySetDataCollection:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.PropertySetDataCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: PropertySetData
    def Add(self, value: PropertySetData) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: PropertySetData) -> bool: ...
    def CopyTo(self, array: list, start: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: PropertySetData) -> int: ...
    def Insert(self, index: int, value: PropertySetData) -> None: ...
    def Remove(self, value: PropertySetData) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class PropertySetDefinition(DictionaryRecord):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.PropertySetDefinition"""
    def __init__(self, *args) -> None: ...
    Definitions: PropertyDefinitionCollection
    IsStyleBased: bool
    IsWriteable: bool
    IsVisible: bool
    ClassificationFilter: ClassificationCollection
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
    def GetValue(self, propId: int, obj: DBObject, blockRefPath: ObjectIdCollection) -> object: ...
    def IsEquivalent(self, otherDef: PropertySetDefinition) -> bool: ...
    def RecordAsModified(self, ) -> None: ...
    def SetAppliesToFilter(self, filter: StringCollection, byStyle: bool) -> None: ...
    def SetDisplayOrder(self, propertyDef: PropertyDefinition, order: int) -> None: ...

class PropertyValueUnitPair(DisposableWrapper):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.PropertyValueUnitPair"""
    def __init__(self, *args) -> None: ...
    Value: object
    UnitType: UnitType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class RotationType:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.RotationType"""
    def __init__(self, *args) -> None: ...
    ...

class RoundingType:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.RoundingType"""
    def __init__(self, *args) -> None: ...
    ...

class ScheduleTable(Geo):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.ScheduleTable"""
    def __init__(self, *args) -> None: ...
    IsModelGeometry: bool
    ScheduleDrawing: bool
    MinimumRowHeight: float
    BasePageWidth: float
    PageMaxHeights: ScheduleTablePageMaxHeightCollection
    PageMaxHeight: float
    UseManualHeights: bool
    RepeatHeaders: bool
    RepeatTitle: bool
    PageSpacing: float
    PageDirection: PageDirectionType
    TitleWidthOffset: float
    TitleHeightOffset: float
    TitleWidth: float
    TitleIsHorizontal: bool
    TitleHeight: float
    TableHeight: float
    TableWidth: float
    CenterPoint: Point3d
    LowerRightPoint: Point3d
    UpperRightPoint: Point3d
    LowerLeftPoint: Point3d
    UpperLeftPoint: Point3d
    TotalRowHeight: float
    HeaderHeight: float
    MatrixHeaderHeight: float
    TotalRow: bool
    RowCount: int
    ColumnCount: int
    XFormMatrix: Matrix3d
    Scale: float
    IsOutOfDate: bool
    AutomaticUpdate: bool
    ScanExternalReferences: bool
    ScanBlockReferences: bool
    AddNewEntriesAutomatically: bool
    SelectionSet: ObjectIdCollection
    LayerWildcard: str
    Title: str
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
    def AddToSelectionSet(self, entityIds: ObjectIdCollection) -> ObjectIdCollection: ...
    def CellData(self, row: int, column: int) -> object: ...
    def CellText(self, row: int, column: int) -> str: ...
    def EvaluateFieldCodes(self, ) -> None: ...
    def ForceUseCachedData(self, forceUseCache: bool) -> None: ...
    def GetColumn(self, pickedMarker: IntPtr) -> int: ...
    def GetColumnMatrix(self, index: int) -> ScheduleTableUniqueVariantCollection: ...
    def GetHeaderPosition(self, node: ScheduleTableStyleHeaderNode) -> ScheduleTableHeaderPosition: ...
    def GetHeaderPositionIterator(self, ) -> ScheduleTableHeaderPositionIterator: ...
    def GetMarker(self, row: int, column: int) -> IntPtr: ...
    def GetPageBreaks(self, ) -> IntegerCollection: ...
    def GetPageHeights(self, ) -> DoubleCollection: ...
    def GetPageWidths(self, ) -> DoubleCollection: ...
    def GetRasterImageId(self, varValue: object) -> ObjectId: ...
    def GetRow(self, pickedMarker: IntPtr) -> int: ...
    def GetRowMarkers(self, row: int) -> IntPtrCollection: ...
    def GetScheduleDrawingName(self, fullPathIfRelative: bool) -> str: ...
    def ObjectsAtRow(self, row: int) -> ObjectIdAndBlockReferencePathCollection: ...
    def RegenerateSampleTable(self, forceUpdate: bool) -> None: ...
    def RegenerateTable(self, forceUpdate: bool) -> None: ...
    def RemoveFromSelectionSet(self, entityId: ObjectId) -> None: ...
    def RowHeight(self, row: int) -> float: ...
    def RowHeightSum(self, row: int) -> float: ...
    def SetCellData(self, row: int, column: int, cvar: object) -> None: ...
    def SetScheduleDrawingName(self, scheduleDrawingName: str) -> None: ...
    def SetSelectionSet(self, entityIds: ObjectIdCollection, entityFiltered: ObjectIdCollection) -> None: ...

class ScheduleTableCellFormat(ImpObject):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.ScheduleTableCellFormat"""
    def __init__(self, *args) -> None: ...
    UseMatrixForTrueFalse: bool
    MatrixSymbolType: MatrixSymbolType
    RotationType: RotationType
    Gap: float
    Height: float
    Width: float
    Alignment: AttachmentPoint
    TextStyleIdString: str
    TextStyleId: ObjectId
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CellHeight(self, string: str, fixedWidth: float) -> float: ...
    def ExtentsCellHeight(self, string: str) -> float: ...
    def ExtentsCellWidth(self, string: str) -> float: ...
    def ExtentsHeight(self, string: str) -> float: ...
    def ExtentsWidth(self, string: str) -> float: ...
    def GetRotatedTextCellWidth(self, string: str, fixedWidth: float) -> float: ...
    def MatrixExtentsCellHeight(self, count: int) -> float: ...
    def MatrixExtentsCellWidth(self, count: int) -> float: ...

class ScheduleTableCellFormatOverride(ScheduleTableCellFormat):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.ScheduleTableCellFormatOverride"""
    def __init__(self, *args) -> None: ...
    DefaultCellFormat: ScheduleTableCellFormat
    OverrideUseMatrixForTrueFalse: bool
    OverrideMatrixSymbolType: bool
    OverrideRotationType: bool
    OverrideGap: bool
    OverrideHeight: bool
    OverrideWidth: bool
    OverrideAlignment: bool
    OverrideTextStyleId: bool
    HasOverrides: bool
    UseMatrixForTrueFalse: bool
    MatrixSymbolType: MatrixSymbolType
    RotationType: RotationType
    Gap: float
    Height: float
    Width: float
    Alignment: AttachmentPoint
    TextStyleIdString: str
    TextStyleId: ObjectId
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def ClearAlignmentOverride(self, ) -> None: ...
    def ClearGapOverride(self, ) -> None: ...
    def ClearHeightOverride(self, ) -> None: ...
    def ClearMatrixSymbolTypeOverride(self, ) -> None: ...
    def ClearRotationTypeOverride(self, ) -> None: ...
    def ClearTextStyleIdOverride(self, ) -> None: ...
    def ClearUseMatrixForTrueFalseOverride(self, ) -> None: ...
    def ClearWidthOverride(self, ) -> None: ...

class ScheduleTableColumn(DisposableWrapper):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.ScheduleTableColumn"""
    def __init__(self, *args) -> None: ...
    MatrixValues: ScheduleTableUniqueVariantCollection
    CellX: float
    CellWidth: float
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetFixedCellWidth(self, cellWidth: float) -> None: ...

class ScheduleTableImage(DisposableWrapper):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.ScheduleTableImage"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddImage(self, imageId: ObjectId) -> bool: ...
    def AddImageDefinition(self, filename: str, definitionId: ObjectId) -> None: ...
    def FindImageDefinition(self, filename: str) -> ObjectId: ...

class ScheduleTablePageMaxHeightCollection:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.ScheduleTablePageMaxHeightCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: float
    def Add(self, value: float) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: float) -> bool: ...
    def CopyTo(self, array: list, start: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: float) -> int: ...
    def Insert(self, index: int, value: float) -> None: ...
    def Remove(self, value: float) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class ScheduleTableSorting(ImpObject):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.ScheduleTableSorting"""
    def __init__(self, *args) -> None: ...
    FormulaColumn: bool
    SubTotalHeader: str
    UseSubTotalHeader: bool
    GroupHeader: str
    UseGroupHeader: bool
    SortOrder: SortOrder
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetColumnPropertyId(self, ) -> int: ...
    def GetColumnPropertySetDefinitionObjectId(self, ) -> ObjectId: ...
    def SetColumn(self, propertySetDefinitionId: ObjectId, propertyId: int, isFormulaColumn: bool) -> None: ...

class ScheduleTableSortingCollection:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.ScheduleTableSortingCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: ScheduleTableSorting
    def Add(self, value: ScheduleTableSorting) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: ScheduleTableSorting) -> bool: ...
    def CopyTo(self, array: list, start: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: ScheduleTableSorting) -> int: ...
    def Insert(self, index: int, value: ScheduleTableSorting) -> None: ...
    def RemoveAt(self, index: int) -> None: ...
    def Swap(self, index1: int, index2: int) -> None: ...

class ScheduleTableStyle(DictionaryRecord):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.ScheduleTableStyle"""
    def __init__(self, *args) -> None: ...
    RepeatFirstColumn: bool
    NextFormulaId: int
    FormulaColumnTotalNumber: int
    QuantityColumnNumber: int
    HasFormulaColumn: bool
    HasQuantityColumn: bool
    QuantityColumnHeading: str
    TitleFormat: ScheduleTableCellFormat
    TotalHeaderFormat: ScheduleTableCellFormat
    GroupHeaderFormat: ScheduleTableCellFormat
    MatrixHeaderFormat: ScheduleTableCellFormat
    ColumnHeaderFormat: ScheduleTableCellFormat
    DefaultCellFormat: ScheduleTableCellFormat
    ClassificationFilter: ClassificationCollection
    AppliesToAll: bool
    Sortings: ScheduleTableSortingCollection
    Columns: ScheduleTableStyleColumnCollection
    Tree: ScheduleTableStyleHeaderTree
    AppliesToFilter: StringCollection
    Title: str
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
    def AddClassification(self, classificationId: ObjectId) -> None: ...
    def AddFormulaColumn(self, column: ScheduleTableStyleColumn) -> None: ...
    def AddQuantityColumn(self, column: ScheduleTableStyleColumn) -> None: ...
    def FormatColumnVariant(self, data: object, formatId: ObjectId, column: int) -> str: ...
    def GetColumnFormat(self, column: int) -> ScheduleTableCellFormat: ...
    def IsFormulaColumn(self, column: ScheduleTableStyleColumn) -> bool: ...
    def IsQuantityColumn(self, column: ScheduleTableStyleColumn) -> bool: ...
    def RemapFormulaColumnIds(self, propertySetDefinition1: PropertySetDefinition, propertySetDefinition2: PropertySetDefinition, definition1PropertyIds: IntegerCollection, definition2PropertyIds: IntegerCollection, actions: IntegerCollection) -> None: ...
    def RemoveClassification(self, classificationId: ObjectId) -> None: ...
    def SetValidityFlags(self, ) -> None: ...

class ScheduleTableStyleColumn(ScheduleTableStyleHeaderNode):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.ScheduleTableStyleColumn"""
    def __init__(self, *args) -> None: ...
    Formula: PropertyDefinitionFormula
    HideColumn: bool
    IsPropertyValid: bool
    FullPropertyName: str
    PropertySetDefinitionName: str
    PropertyName: str
    CellFormatOverride: ScheduleTableCellFormatOverride
    ColumnType: ScheduleTableStyleColumnType
    FormulaTotal: bool
    Total: bool
    MaximumMatrixColumns: int
    Matrix: bool
    PropertyId: int
    PropertySetDefinitionId: ObjectId
    FormatId: ObjectId
    Heading: str
    DefaultData: object
    FormatOverride: ScheduleTableCellFormatOverride
    Text: str
    Parent: ScheduleTableStyleHeaderNode
    Children: ScheduleTableStyleHeaderNodeCollection
    Level: int
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CheckPropertyValid(self, ) -> None: ...
    def Evaluate(self, formula: str, quantity: int) -> object: ...

class ScheduleTableStyleColumnCollection:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.ScheduleTableStyleColumnCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: ScheduleTableStyleColumn
    def Add(self, value: ScheduleTableStyleColumn) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: ScheduleTableStyleColumn) -> bool: ...
    def CopyTo(self, array: list, start: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, propSetDefId: ObjectId, propId: int) -> int: ...
    def Insert(self, index: int, value: ScheduleTableStyleColumn) -> None: ...
    def Prepend(self, node: ScheduleTableStyleColumn) -> None: ...
    def Remove(self, value: ScheduleTableStyleColumn) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class ScheduleTableStyleColumnType:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.ScheduleTableStyleColumnType"""
    def __init__(self, *args) -> None: ...
    ...

class ScheduleTableStyleHeaderNode(ImpObject):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.ScheduleTableStyleHeaderNode"""
    def __init__(self, *args) -> None: ...
    FormatOverride: ScheduleTableCellFormatOverride
    Text: str
    Parent: ScheduleTableStyleHeaderNode
    Children: ScheduleTableStyleHeaderNodeCollection
    Level: int
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def SetTreeParent(self, parent: ScheduleTableStyleHeaderNode) -> None: ...

class ScheduleTableStyleHeaderNodeCollection:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.ScheduleTableStyleHeaderNodeCollection"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: ScheduleTableStyleHeaderNode
    def Add(self, value: ScheduleTableStyleHeaderNode) -> int: ...
    def Clear(self, ) -> None: ...
    def Contains(self, value: ScheduleTableStyleHeaderNode) -> bool: ...
    def CopyTo(self, array: list, start: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: ScheduleTableStyleHeaderNode) -> int: ...
    def Insert(self, index: int, value: ScheduleTableStyleHeaderNode) -> None: ...
    def Prepend(self, node: ScheduleTableStyleHeaderNode) -> None: ...
    def Remove(self, value: ScheduleTableStyleHeaderNode) -> None: ...
    def RemoveAt(self, index: int) -> None: ...
    def Shift(self, node: ScheduleTableStyleHeaderNode, amount: int) -> None: ...

class ScheduleTableStyleHeaderTree(ImpObject):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.ScheduleTableStyleHeaderTree"""
    def __init__(self, *args) -> None: ...
    Root: ScheduleTableStyleHeaderNode
    Columns: ScheduleTableStyleColumnCollection
    MaxLevel: int
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Contains(self, node: ScheduleTableStyleHeaderNode) -> bool: ...
    def DeleteNode(self, pNode: ScheduleTableStyleHeaderNode) -> None: ...
    def InsertNode(self, text: str, newIndex: int, parent: ScheduleTableStyleHeaderNode, children: list) -> ScheduleTableStyleHeaderNode: ...
    def IsNodeChildOf(self, node: ScheduleTableStyleHeaderNode, parent: ScheduleTableStyleHeaderNode) -> bool: ...
    def MoveNode(self, node: ScheduleTableStyleHeaderNode, originalParent: ScheduleTableStyleHeaderNode, originalIndex: int, newParent: ScheduleTableStyleHeaderNode, newIndex: int) -> None: ...
    def ShiftNode(self, node: ScheduleTableStyleHeaderNode, amount: int) -> None: ...

class ScheduleTableStyleHeaderTreeIterator(DisposableWrapper):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.ScheduleTableStyleHeaderTreeIterator"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Dump(self, ) -> None: ...
    def GetNext(self, ) -> ScheduleTableStyleHeaderNode: ...
    def Reset(self, ) -> None: ...

class ScheduleTableStyleHeaderTreeNode(ScheduleTableStyleHeaderNode):
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.ScheduleTableStyleHeaderTreeNode"""
    def __init__(self, *args) -> None: ...
    FormatOverride: ScheduleTableCellFormatOverride
    Text: str
    Parent: ScheduleTableStyleHeaderNode
    Children: ScheduleTableStyleHeaderNodeCollection
    Level: int
    Database: Database
    Description: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class SeparatorType:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.SeparatorType"""
    def __init__(self, *args) -> None: ...
    ...

class SortOrder:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.SortOrder"""
    def __init__(self, *args) -> None: ...
    ...

class UnitsType:
    """.NET: Autodesk.Aec.PropertyData.DatabaseServices.UnitsType"""
    def __init__(self, *args) -> None: ...
    ...
