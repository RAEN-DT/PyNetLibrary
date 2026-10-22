# Auto-generated — Civil 26 — Autodesk.AutoCAD.Runtime

class AngularUnitFormat:
    """.NET enum: Autodesk.AutoCAD.Runtime.AngularUnitFormat"""
    def __init__(self, *args) -> None: ...
    Degrees: int  # = 0
    DegreesMinutesSeconds: int  # = 1
    Grads: int  # = 2
    Radians: int  # = 3
    Surveyor: int  # = 4
    Current: int  # = -1
class CommandClassAttribute(Attribute):
    """.NET: Autodesk.AutoCAD.Runtime.CommandClassAttribute"""
    def __init__(self, *args) -> None: ...
    Type: Type
    TypeId: object

class CommandFlags:
    """.NET enum: Autodesk.AutoCAD.Runtime.CommandFlags"""
    def __init__(self, *args) -> None: ...
    Modal: int  # = 0
    Transparent: int  # = 1
    UsePickSet: int  # = 2
    Redraw: int  # = 4
    NoPerspective: int  # = 8
    NoMultiple: int  # = 16
    NoTileMode: int  # = 32
    NoPaperSpace: int  # = 64
    NoOem: int  # = 256
    Undefined: int  # = 512
    InProgress: int  # = 1024
    Defun: int  # = 2048
    NoNewStack: int  # = 65536
    NoInternalLock: int  # = 131072
    DocReadLock: int  # = 524288
    DocExclusiveLock: int  # = 1048576
    Session: int  # = 2097152
    Interruptible: int  # = 4194304
    NoHistory: int  # = 8388608
    NoUndoMarker: int  # = 16777216
    NoBlockEditor: int  # = 33554432
    NoActionRecording: int  # = 67108864
    ActionMacro: int  # = 134217728
    NoInferConstraint: int  # = 1073741824
    TempShowDynDimension: int  # = -2147483648
class CommandMethodAttribute(Attribute):
    """.NET: Autodesk.AutoCAD.Runtime.CommandMethodAttribute"""
    def __init__(self, *args) -> None: ...
    HelpTopic: str
    HelpFileName: str
    ContextMenuExtensionType: Type
    Flags: CommandFlags
    GroupName: str
    LocalizedNameId: str
    GlobalName: str
    TypeId: object

class Converter:
    """.NET: Autodesk.AutoCAD.Runtime.Converter"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def AngleToString(value: float, units: AngularUnitFormat, precision: int) -> str: ...
    @staticmethod
    def DistanceToString(value: float, units: DistanceUnitFormat, precision: int) -> str: ...
    @staticmethod
    def RawAngleToString(value: float, units: AngularUnitFormat, precision: int) -> str: ...
    @staticmethod
    def StringToAngle(value: str, units: AngularUnitFormat) -> float: ...
    @staticmethod
    def StringToDistance(value: str, units: DistanceUnitFormat) -> float: ...
    @staticmethod
    def StringToRawAngle(value: str, units: AngularUnitFormat) -> float: ...

class DeferredAssemblyLoadEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.Runtime.DeferredAssemblyLoadEventArgs"""
    def __init__(self, *args) -> None: ...
    MayHaveCommands: bool
    MayHaveExtensionApplication: bool
    LoadedAssembly: Assembly

class DeferredAssemblyLoadEventHandler:
    """.NET: Autodesk.AutoCAD.Runtime.DeferredAssemblyLoadEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: DeferredAssemblyLoadEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: DeferredAssemblyLoadEventArgs) -> None: ...

class Dictionary(RXObject):
    """.NET: Autodesk.AutoCAD.Runtime.Dictionary"""
    def __init__(self, *args) -> None: ...
    Item: RXObject
    Count: int
    IsSorted: bool
    IsCaseSensitive: bool
    DeletesObjects: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def At(self, id: int) -> RXObject: ...
    def AtKeyAndIdPut(self, newKey: str, id: int, value: RXObject) -> None: ...
    def AtPut(self, key: str, value: RXObject, retId: int) -> RXObject: ...
    def Contains(self, id: int) -> bool: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IDictionaryEnumerator: ...
    def IdAt(self, key: str) -> int: ...
    def KeyAt(self, id: int) -> str: ...
    def Remove(self, id: int) -> RXObject: ...
    def ResetKey(self, id: int, newKey: str) -> None: ...

class DisposableWrapper(MarshalByRefObject):
    """.NET: Autodesk.AutoCAD.Runtime.DisposableWrapper"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(type: Type, unmanagedPointer: IntPtr, autoDelete: bool) -> DisposableWrapper: ...
    def Dispose(self, ) -> None: ...
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...

class DistanceUnitFormat:
    """.NET enum: Autodesk.AutoCAD.Runtime.DistanceUnitFormat"""
    def __init__(self, *args) -> None: ...
    Scientific: int  # = 1
    Decimal: int  # = 2
    Engineering: int  # = 3
    Architectural: int  # = 4
    Fractional: int  # = 5
    Current: int  # = -1
class DynamicLinker(RXObject):
    """.NET: Autodesk.AutoCAD.Runtime.DynamicLinker"""
    def __init__(self, *args) -> None: ...
    ProductLcid: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetLoadedModules(self, ) -> StringCollection: ...
    def IsAppBusy(self, moduleName: str) -> bool: ...
    def IsAppMdiAware(self, moduleName: str) -> bool: ...
    def IsApplicationLocked(self, moduleName: str) -> bool: ...
    def IsModuleLoaded(self, fileName: str) -> bool: ...
    def LoadApp(self, appName: str, printIt: bool, asCmd: bool) -> None: ...
    def LoadModule(self, fileName: str, printIt: bool, asCmd: bool) -> None: ...
    def SetAppBusy(self, moduleName: str, busyFlag: bool) -> None: ...
    def UnloadApp(self, appName: str, asCmd: bool) -> None: ...
    def UnloadModule(self, fileName: str, asCmd: bool) -> None: ...

class DynamicLinkerEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.Runtime.DynamicLinkerEventArgs"""
    def __init__(self, *args) -> None: ...
    FileName: str

class EnvVarExistsConditionAttribute(Attribute):
    """.NET: Autodesk.AutoCAD.Runtime.EnvVarExistsConditionAttribute"""
    def __init__(self, *args) -> None: ...
    TypeId: object
    def Evaluate(self, ) -> bool: ...

class ErrorStatus:
    """.NET enum: Autodesk.AutoCAD.Runtime.ErrorStatus"""
    def __init__(self, *args) -> None: ...
    OK: int  # = 0
    NotImplementedYet: int  # = 1
    NotApplicable: int  # = 2
    InvalidInput: int  # = 3
    AmbiguousInput: int  # = 4
    AmbiguousOutput: int  # = 5
    OutOfMemory: int  # = 6
    BufferTooSmall: int  # = 7
    InvalidOpenState: int  # = 8
    EntityInInactiveLayout: int  # = 9
    HandleExists: int  # = 10
    NullHandle: int  # = 11
    BrokenHandle: int  # = 12
    UnknownHandle: int  # = 13
    HandleInUse: int  # = 14
    NullObjectPointer: int  # = 15
    NullObjectId: int  # = 16
    NullBlockName: int  # = 17
    ContainerNotEmpty: int  # = 18
    NullEntityPointer: int  # = 20
    IllegalEntityType: int  # = 21
    KeyNotFound: int  # = 22
    DuplicateKey: int  # = 23
    InvalidIndex: int  # = 24
    DuplicateIndex: int  # = 25
    AlreadyInDB: int  # = 26
    OutOfDisk: int  # = 27
    DeletedEntry: int  # = 28
    NegativeValueNotAllowed: int  # = 29
    InvalidExtents: int  # = 30
    InvalidAdsName: int  # = 31
    InvalidSymbolTableName: int  # = 32
    InvalidKey: int  # = 33
    WrongObjectType: int  # = 34
    WrongDatabase: int  # = 35
    ObjectToBeDeleted: int  # = 36
    InvalidDwgVersion: int  # = 37
    AnonymousEntry: int  # = 38
    IllegalReplacement: int  # = 39
    EndOfObject: int  # = 40
    EndOfFile: int  # = 41
    IsReading: int  # = 42
    IsWriting: int  # = 43
    NotOpenForRead: int  # = 44
    NotOpenForWrite: int  # = 45
    NotThatKindOfClass: int  # = 46
    InvalidBlockName: int  # = 47
    MissingDxfField: int  # = 48
    DuplicateDxfField: int  # = 49
    InvalidDxfCode: int  # = 50
    InvalidResultBuffer: int  # = 51
    BadDxfSequence: int  # = 52
    FilerError: int  # = 53
    VertexAfterFace: int  # = 54
    InvalidFaceVertexIndex: int  # = 55
    InvalidMeshVertexIndex: int  # = 56
    OtherObjectsBusy: int  # = 57
    MustFirstAddBlockToDB: int  # = 58
    CannotNestBlockDefinitions: int  # = 59
    DwgRecoveredOK: int  # = 60
    DwgNotRecoverable: int  # = 61
    DxfPartiallyRead: int  # = 62
    DxfReadAborted: int  # = 63
    DxbPartiallyRead: int  # = 64
    DwgCrcDoesNotMatch: int  # = 65
    DwgSentinelDoesNotMatch: int  # = 66
    DwgObjectImproperlyRead: int  # = 67
    NoInputFiler: int  # = 68
    DwgNeedsAFullSave: int  # = 69
    DxbReadAborted: int  # = 70
    FileLockedByAutoCAD: int  # = 71
    FileAccessErr: int  # = 72
    FileSystemErr: int  # = 73
    FileInternalErr: int  # = 74
    FileTooManyOpen: int  # = 75
    FileNotFound: int  # = 76
    DwkLockFileFound: int  # = 77
    WasErased: int  # = 80
    PermanentlyErased: int  # = 81
    WasOpenForRead: int  # = 82
    WasOpenForWrite: int  # = 83
    WasOpenForUndo: int  # = 84
    WasNotifying: int  # = 85
    WasOpenForNotify: int  # = 86
    OnLockedLayer: int  # = 87
    MustOpenThruOwner: int  # = 88
    SubentitiesStillOpen: int  # = 89
    AtMaxReaders: int  # = 90
    IsWriteProtected: int  # = 91
    IsXRefObject: int  # = 92
    NotAnEntity: int  # = 93
    HadMultipleReaders: int  # = 94
    DuplicateRecordName: int  # = 95
    XRefDependent: int  # = 96
    SelfReference: int  # = 97
    MissingSymbolTable: int  # = 98
    MissingSymbolTableRecord: int  # = 99
    WasNotOpenForWrite: int  # = 100
    CloseWasNotifying: int  # = 101
    CloseModifyAborted: int  # = 102
    ClosePartialFailure: int  # = 103
    CloseFailObjectDamaged: int  # = 104
    CannotBeErasedByCaller: int  # = 105
    CannotBeResurrected: int  # = 106
    WasNotErased: int  # = 107
    InsertAfter: int  # = 110
    FixedAllErrors: int  # = 120
    LeftErrorsUnfixed: int  # = 122
    UnrecoverableErrors: int  # = 123
    NoDatabase: int  # = 124
    ExternalDataSizeExceeded: int  # = 125
    RegisteredApplicationIdNotFound: int  # = 126
    RepeatEntity: int  # = 127
    RecordNotInTable: int  # = 128
    IteratorDone: int  # = 129
    NullIterator: int  # = 130
    NotInBlock: int  # = 131
    OwnerNotInDatabase: int  # = 132
    OwnerNotOpenForRead: int  # = 133
    OwnerNotOpenForWrite: int  # = 134
    ExplodeBeforeTransform: int  # = 135
    CannotScaleNonUniformly: int  # = 136
    NotInDatabase: int  # = 137
    NotCurrentDatabase: int  # = 138
    IsAnEntity: int  # = 139
    CannotChangeActiveViewport: int  # = 140
    NotInPaperspace: int  # = 141
    CommandWasInProgress: int  # = 142
    GeneralModelingFailure: int  # = 150
    OutOfRange: int  # = 151
    NonCoplanarGeometry: int  # = 152
    DegenerateGeometry: int  # = 153
    InvalidAxis: int  # = 154
    PointNotOnEntity: int  # = 155
    SingularPoint: int  # = 156
    InvalidOffset: int  # = 157
    NonPlanarEntity: int  # = 158
    CannotExplodeEntity: int  # = 159
    StringTooLong: int  # = 160
    InvalidSymTableFlag: int  # = 161
    UndefinedLineType: int  # = 162
    InvalidTextStyle: int  # = 163
    TooFewLineTypeElements: int  # = 164
    TooManyLineTypeElements: int  # = 165
    ExcessiveItemCount: int  # = 166
    IgnoredLinetypeRedefinition: int  # = 167
    BadUcs: int  # = 168
    BadPaperspaceView: int  # = 169
    SomeInputDataLeftUnread: int  # = 170
    NoInternalSpace: int  # = 171
    InvalidDimStyle: int  # = 172
    InvalidLayer: int  # = 173
    UserBreak: int  # = 180
    DwgNeedsRecovery: int  # = 190
    DeleteEntity: int  # = 191
    InvalidFix: int  # = 192
    FiniteStateMachineError: int  # = 193
    BadLayerName: int  # = 200
    LayerGroupCodeMissing: int  # = 201
    BadColorIndex: int  # = 202
    BadLinetypeName: int  # = 203
    BadLinetypeScale: int  # = 204
    BadVisibilityValue: int  # = 205
    ProperClassSeparatorExpected: int  # = 206
    BadLineWeightValue: int  # = 207
    BadColor: int  # = 208
    PagerError: int  # = 210
    OutOfPagerMemory: int  # = 211
    PagerWriteError: int  # = 212
    WasNotForwarding: int  # = 213
    InvalidIdMap: int  # = 220
    InvalidOwnerObject: int  # = 221
    OwnerNotSet: int  # = 222
    WrongSubentityType: int  # = 230
    TooManyVertices: int  # = 231
    TooFewVertices: int  # = 232
    NoActiveTransactions: int  # = 250
    NotTopTransaction: int  # = 251
    TransactionOpenWhileCommandEnded: int  # = 252
    InProcessOfCommitting: int  # = 253
    NotNewlyCreated: int  # = 254
    LongTransReferenceError: int  # = 255
    NoWorkSet: int  # = 256
    AlreadyInGroup: int  # = 260
    NotInGroup: int  # = 261
    InvalidInterfaceId: int  # = 290
    InvalidNormal: int  # = 291
    InvalidStyle: int  # = 292
    CannotRestoreFromAcisFile: int  # = 300
    MakeMeProxy: int  # = 301
    NlsFileNotAvailable: int  # = 302
    NotAllowedForThisProxy: int  # = 303
    NotSupportedInDwgApi: int  # = 310
    PolyWidthLost: int  # = 311
    NullExtents: int  # = 312
    BadDwgHeader: int  # = 314
    LockViolation: int  # = 320
    LockConflict: int  # = 321
    DatabaseObjectsOpen: int  # = 322
    LockChangeInProgress: int  # = 323
    Vetoed: int  # = 325
    NoDocument: int  # = 330
    NotFromThisDocument: int  # = 331
    LispActive: int  # = 332
    TargetDocNotQuiescent: int  # = 333
    DocumentSwitchDisabled: int  # = 334
    InvalidContext: int  # = 335
    CreateFailed: int  # = 337
    CreateInvalidName: int  # = 338
    SetFailed: int  # = 340
    DelDoesNotExist: int  # = 342
    DelIsModelSpace: int  # = 343
    DelLastLayout: int  # = 344
    DelUnableToSetCurrent: int  # = 345
    DelUnableToFind: int  # = 346
    RenameDoesNotExist: int  # = 348
    RenameIsModelSpace: int  # = 349
    RenameInvalidLayoutName: int  # = 350
    RenameLayoutAlreadyExists: int  # = 351
    RenameInvalidName: int  # = 352
    CopyDoesNotExist: int  # = 354
    CopyIsModelSpace: int  # = 355
    CopyFailed: int  # = 356
    CopyInvalidName: int  # = 357
    CopyNameExists: int  # = 358
    ProfileDoesNotExist: int  # = 359
    InvalidFileExtension: int  # = 360
    InvalidProfileName: int  # = 361
    FileExists: int  # = 362
    ProfileIsInUse: int  # = 363
    CantOpenFile: int  # = 364
    NoFileName: int  # = 365
    RegistryAccessError: int  # = 366
    RegistryCreateError: int  # = 367
    BadDxfFile: int  # = 368
    UnknownDxfFileFormat: int  # = 369
    MissingDxfSection: int  # = 370
    InvalidDxfSectionName: int  # = 371
    NotDxfHeaderGroupCode: int  # = 372
    UndefinedDxfGroupCode: int  # = 373
    NotInitializedYet: int  # = 374
    InvalidDxf2dPoint: int  # = 375
    InvalidDxf3dPoint: int  # = 376
    BadlyNestedAppData: int  # = 378
    IncompleteBlockDefinition: int  # = 379
    IncompleteComplexObject: int  # = 380
    BlockDefInEntitySection: int  # = 381
    NoBlockBegin: int  # = 382
    DuplicateLayerName: int  # = 383
    BadPlotStyleName: int  # = 384
    DuplicateBlockName: int  # = 385
    BadPlotStyleType: int  # = 386
    BadPlotStyleNameHandle: int  # = 387
    UndefineShapeName: int  # = 388
    DuplicateBlockDefinition: int  # = 389
    MissingBlockName: int  # = 390
    BinaryDataSizeExceeded: int  # = 391
    ObjectIsReferenced: int  # = 392
    NoThumbnailBitmap: int  # = 393
    GuidNoAddress: int  # = 394
    MustBe0to2: int  # = 395
    MustBe0to3: int  # = 396
    MustBe0to4: int  # = 397
    MustBe0to5: int  # = 398
    MustBe0to8: int  # = 399
    MustBe1to8: int  # = 400
    MustBe1to15: int  # = 401
    MustBePositive: int  # = 402
    MustBeNonNegative: int  # = 403
    MustBeNonZero: int  # = 404
    MustBe1to6: int  # = 405
    NoPlotStyleTranslationTable: int  # = 406
    PlotStyleInColorDependentMode: int  # = 407
    MaxLayouts: int  # = 408
    NoClassId: int  # = 409
    UndoOperationNotAvailable: int  # = 410
    UndoNoGroupBegin: int  # = 411
    HatchTooDense: int  # = 420
    OpenFileCancelled: int  # = 430
    NotHandled: int  # = 431
    MakeMeProxyAndResurrect: int  # = 432
    FileSharingViolation: int  # = 433
    UnsupportedFileFormat: int  # = 434
    ObsoleteFileFormat: int  # = 435
    FileMissingSections: int  # = 436
    RepeatedDwgRead: int  # = 437
    WrongCellType: int  # = 440
    CannotChangeColumnType: int  # = 441
    RowsMustMatchColumns: int  # = 442
    DwgShareDemandLoad: int  # = 500
    DwgShareReadAccess: int  # = 501
    DwgShareWriteAccess: int  # = 502
    LoadFailed: int  # = 503
    DeviceNotFound: int  # = 504
    NoCurrentConfig: int  # = 505
    NullPtr: int  # = 506
    NoLayout: int  # = 507
    IncompatiblePlotSettings: int  # = 508
    NonePlotDevice: int  # = 509
    NoMatchingMedia: int  # = 510
    InvalidView: int  # = 511
    InvalidWindowArea: int  # = 512
    InvalidPlotArea: int  # = 513
    CustomSizeNotPossible: int  # = 514
    PageCancelled: int  # = 515
    PlotCancelled: int  # = 516
    InvalidEngineState: int  # = 517
    PlotAlreadyStarted: int  # = 518
    NoErrorHandler: int  # = 519
    InvalidPlotInfo: int  # = 520
    NumberOfCopiesNotSupported: int  # = 521
    LayoutNotCurrent: int  # = 522
    GraphicsNotGenerated: int  # = 523
    CannotPlotToFile: int  # = 524
    MustPlotToFile: int  # = 525
    NotMultiPageCapable: int  # = 526
    BackgroundPlotInProgress: int  # = 527
    SubSelectionSetEmpty: int  # = 550
    NoIntersections: int  # = 551
    EmbeddedIntersections: int  # = 552
    InvalidObjectId: int  # = 600
    InvalidXrefObjectId: int  # = 601
    NoViewAssociation: int  # = 602
    NoLabelBlock: int  # = 603
    UnableToSetViewAssociation: int  # = 604
    UnableToGetViewAssociation: int  # = 605
    UnableToSetLabelBlock: int  # = 606
    UnableToGetLabelBlock: int  # = 607
    UnableToRemoveAssociation: int  # = 608
    UnableToSyncModelView: int  # = 609
    DataLinkAdapterNotFound: int  # = 650
    DataLinkInvalidAdapterId: int  # = 651
    DataLinkNotFound: int  # = 652
    DataLinkBadConnectionString: int  # = 653
    DataLinkNotUpdatedYet: int  # = 654
    DataLinkSourceNotFound: int  # = 655
    DataLinkConnectionFailed: int  # = 656
    DataLinkSourceIsWriteProtected: int  # = 658
    DataLinkOtherError: int  # = 660
    SecInitializationFailure: int  # = 1001
    SecErrorReadingFile: int  # = 1002
    SecErrorWritingFile: int  # = 1003
    SecInvalidDigitalId: int  # = 1101
    SecErrorGeneratingTimestamp: int  # = 1102
    SecErrorComputingSignature: int  # = 1103
    SecErrorWritingSignature: int  # = 1104
    SecErrorEncryptingData: int  # = 1201
    SecErrorCipherNotSupported: int  # = 1202
    SecErrorDecryptingData: int  # = 1203
    InternetBase: int  # = 20000
    InternetOK: int  # = 20000
    InternetInCache: int  # = 20001
    InternetFileNotFound: int  # = 20002
    InternetBadPath: int  # = 20003
    InternetTooManyOpenFiles: int  # = 20004
    InternetFileAccessDenied: int  # = 20005
    InternetInvalidFileHandle: int  # = 20006
    InternetDirectoryFull: int  # = 20007
    InternetHardwareError: int  # = 20008
    InternetSharingViolation: int  # = 20009
    InternetDiskFull: int  # = 20010
    InternetFileGenericError: int  # = 20011
    InternetValidUrl: int  # = 20012
    InternetNotAnUrl: int  # = 20013
    InternetNoWinInternet: int  # = 20014
    InternetOldWinInternet: int  # = 20015
    InternetNoInternetSupport: int  # = 20016
    InternetNotImplemented: int  # = 20017
    InternetProtocolNotSupported: int  # = 20018
    InternetCreateInternetSessionFailed: int  # = 20019
    InternetInternetSessionConnectFailed: int  # = 20020
    InternetInternetSessionOpenFailed: int  # = 20021
    InternetInvalidAccessType: int  # = 20022
    InternetFileOpenFailed: int  # = 20023
    InternetHttpOpenRequestFailed: int  # = 20024
    InternetUserCancelledTransfer: int  # = 20025
    InternetHttpBadRequest: int  # = 20026
    InternetHttpAccessDenied: int  # = 20027
    InternetHttpPaymentRequired: int  # = 20028
    InternetHttpRequestForbidden: int  # = 20029
    InternetHttpObjectNotFound: int  # = 20030
    InternetHttpBadMethod: int  # = 20031
    InternetHttpNoAcceptableResponse: int  # = 20032
    InternetHttpProxyAuthorizationRequired: int  # = 20033
    InternetHttpTimedOut: int  # = 20034
    InternetHttpConflict: int  # = 20035
    InternetHttpResourceGone: int  # = 20036
    InternetHttpLengthRequired: int  # = 20037
    InternetHttpPreconditionFailure: int  # = 20038
    InternetHttpRequestTooLarge: int  # = 20039
    InternetHttpUriTooLong: int  # = 20040
    InternetHttpUnsupportedMedia: int  # = 20041
    InternetHttpServerError: int  # = 20042
    InternetHttpNotSupported: int  # = 20043
    InternetHttpBadGateway: int  # = 20044
    InternetHttpServiceUnavailable: int  # = 20045
    InternetHttpGatewayTimeout: int  # = 20046
    InternetHttpVersionNotSupported: int  # = 20047
    InternetInternetError: int  # = 20048
    InternetGenericException: int  # = 20049
    InternetUnknownError: int  # = 20050
    AlreadyActive: int  # = 20051
    AlreadyInactive: int  # = 20052
class Exception(Exception):
    """.NET: Autodesk.AutoCAD.Runtime.Exception"""
    def __init__(self, *args) -> None: ...
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

class ExtensionApplicationAttribute(Attribute):
    """.NET: Autodesk.AutoCAD.Runtime.ExtensionApplicationAttribute"""
    def __init__(self, *args) -> None: ...
    Type: Type
    TypeId: object

class ExtensionLoader(MarshalByRefObject):
    """.NET: Autodesk.AutoCAD.Runtime.ExtensionLoader"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def IsLoaded(fileName: str) -> bool: ...
    @staticmethod
    def Load(fileName: str) -> Assembly: ...

class ExtractOption:
    """.NET: Autodesk.AutoCAD.Runtime.ExtractOption"""
    def __init__(self, *args) -> None: ...
    ...

class ExtractionType:
    """.NET enum: Autodesk.AutoCAD.Runtime.ExtractionType"""
    def __init__(self, *args) -> None: ...
    OutLine: int  # = 0
    AllLine: int  # = 1
class Factory:
    """.NET: Autodesk.AutoCAD.Runtime.Factory"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def Create(type: Type) -> object: ...

class FileExistsConditionAttribute(Attribute):
    """.NET: Autodesk.AutoCAD.Runtime.FileExistsConditionAttribute"""
    def __init__(self, *args) -> None: ...
    TypeId: object
    def Evaluate(self, ) -> bool: ...

class FileHasClosedEventHandler:
    """.NET: Autodesk.AutoCAD.Runtime.FileHasClosedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, e: FileOperationsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, e: FileOperationsEventArgs) -> None: ...

class FileOpenAbortedEventHandler:
    """.NET: Autodesk.AutoCAD.Runtime.FileOpenAbortedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, e: FileOperationsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, e: FileOperationsEventArgs) -> None: ...

class FileOperations:
    """.NET: Autodesk.AutoCAD.Runtime.FileOperations"""
    def __init__(self, *args) -> None: ...
    def Dispose(self, ) -> None: ...

class FileOperationsEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.Runtime.FileOperationsEventArgs"""
    def __init__(self, *args) -> None: ...
    VetoStatus: VetoStatusType
    FilePath: str
    ReloadNested: bool
    ReloadPrimary: bool
    ReferenceFile: bool
    KnownToBeUnmodified: bool
    ReadOnly: bool
    def Dispose(self, ) -> None: ...
    def Veto(self, status: VetoStatusType) -> bool: ...

class FileWillOpenEventHandler:
    """.NET: Autodesk.AutoCAD.Runtime.FileWillOpenEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, e: FileOperationsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, e: FileOperationsEventArgs) -> None: ...

class ICommandLineCallable:
    """.NET: Autodesk.AutoCAD.Runtime.ICommandLineCallable"""
    def __init__(self, *args) -> None: ...
    ContextMenuExtensionType: Type
    HelpTopic: str
    HelpFileName: str
    Flags: CommandFlags
    GroupName: str
    LocalizedNameId: str
    GlobalName: str

class ICondition:
    """.NET: Autodesk.AutoCAD.Runtime.ICondition"""
    def __init__(self, *args) -> None: ...
    def Evaluate(self, ) -> bool: ...

class IExtensionApplication:
    """.NET: Autodesk.AutoCAD.Runtime.IExtensionApplication"""
    def __init__(self, *args) -> None: ...
    def Initialize(self, ) -> None: ...
    def Terminate(self, ) -> None: ...

class IJavaScriptCallable:
    """.NET: Autodesk.AutoCAD.Runtime.IJavaScriptCallable"""
    def __init__(self, *args) -> None: ...
    EntryPoint: str

class IJavaScriptCallableInternal:
    """.NET: Autodesk.AutoCAD.Runtime.IJavaScriptCallableInternal"""
    def __init__(self, *args) -> None: ...
    EntryPoint: str

class IMenuItem:
    """.NET: Autodesk.AutoCAD.Runtime.IMenuItem"""
    def __init__(self, *args) -> None: ...
    Items: IEnumerable
    Icon: Icon
    Checked: bool
    Visible: bool
    Enabled: bool
    Text: str
    def OnClicked(self, eventArgs: EventArgs) -> None: ...

class IPointCloudExtractionProgressCallback:
    """.NET: Autodesk.AutoCAD.Runtime.IPointCloudExtractionProgressCallback"""
    def __init__(self, *args) -> None: ...
    def Cancel(self, ) -> None: ...
    def Cancelled(self, ) -> bool: ...
    def End(self, ) -> None: ...
    def UpdateCaption(self, caption: str) -> None: ...
    def UpdateProgress(self, progress: int) -> None: ...
    def UpdateRemainTime(self, remainTime: float) -> None: ...

class Interop:
    """.NET: Autodesk.AutoCAD.Runtime.Interop"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def AttachUnmanagedObject(obj: DisposableWrapper, unmanagedPointer: IntPtr, autoDelete: bool) -> None: ...
    @staticmethod
    def Check(returnValue: int) -> None: ...
    @staticmethod
    def CheckAds(returnValue: int) -> None: ...
    @staticmethod
    def CheckAdsForCancel(returnValue: int) -> bool: ...
    @staticmethod
    def CheckBool(returnValue: bool) -> None: ...
    @staticmethod
    def CheckBoolean(returnValue: int) -> None: ...
    @staticmethod
    def CheckNull(returnValue: IntPtr) -> None: ...
    @staticmethod
    def DetachUnmanagedObject(obj: DisposableWrapper) -> None: ...
    @staticmethod
    def SetAutoDelete(obj: DisposableWrapper, value: bool) -> None: ...
    @staticmethod
    def ThrowExceptionForErrorStatus(errorStatus: int) -> None: ...

class JSInteropApplicationAttribute(Attribute):
    """.NET: Autodesk.AutoCAD.Runtime.JSInteropApplicationAttribute"""
    def __init__(self, *args) -> None: ...
    Type: Type
    TypeId: object

class JavaScriptCallableInternalAttribute(Attribute):
    """.NET: Autodesk.AutoCAD.Runtime.JavaScriptCallableInternalAttribute"""
    def __init__(self, *args) -> None: ...
    EntryPoint: str
    TypeId: object

class JavaScriptCallbackAttribute(Attribute):
    """.NET: Autodesk.AutoCAD.Runtime.JavaScriptCallbackAttribute"""
    def __init__(self, *args) -> None: ...
    EntryPoint: str
    TypeId: object

class JavaScriptClassAttribute(Attribute):
    """.NET: Autodesk.AutoCAD.Runtime.JavaScriptClassAttribute"""
    def __init__(self, *args) -> None: ...
    Type: Type
    TypeId: object

class LispDataType:
    """.NET enum: Autodesk.AutoCAD.Runtime.LispDataType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 5000
    Double: int  # = 5001
    Point2d: int  # = 5002
    Int16: int  # = 5003
    Angle: int  # = 5004
    Text: int  # = 5005
    ObjectId: int  # = 5006
    SelectionSet: int  # = 5007
    Orientation: int  # = 5008
    Point3d: int  # = 5009
    Int32: int  # = 5010
    Void: int  # = 5014
    ListBegin: int  # = 5016
    ListEnd: int  # = 5017
    DottedPair: int  # = 5018
    Nil: int  # = 5019
    T_atom: int  # = 5021
class LispFunctionAttribute(Attribute):
    """.NET: Autodesk.AutoCAD.Runtime.LispFunctionAttribute"""
    def __init__(self, *args) -> None: ...
    HelpTopic: str
    HelpFileName: str
    LocalizedNameId: str
    GlobalName: str
    TypeId: object

class Marshaler:
    """.NET: Autodesk.AutoCAD.Runtime.Marshaler"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def AcValueToObject(acValueObj: IntPtr) -> object: ...
    @staticmethod
    def BitmapInfoToBitmap(bitmapInfo: IntPtr) -> Bitmap: ...
    @staticmethod
    def BitmapToBitmapInfo(bitmap: Bitmap) -> IntPtr: ...
    @staticmethod
    def CopyToManagedFullSubentityPath(path: IntPtr) -> FullSubentityPath: ...
    @staticmethod
    def CopyToUnmanagedFullSubentityPath(path: FullSubentityPath, newPath: IntPtr) -> None: ...
    @staticmethod
    def GetInternalArray(col: Vector3dCollection) -> list: ...
    @staticmethod
    def ObjectToAcValue(obj: object, acValueObj: IntPtr) -> None: ...
    @staticmethod
    def ObjectToResbuf(o: object, rb: IntPtr) -> None: ...
    @staticmethod
    def ObjectsToResbuf(objects: list) -> IntPtr: ...
    @staticmethod
    def ResbufToObject(rb: IntPtr) -> object: ...
    @staticmethod
    def ResbufToTypedValues(resbuf: IntPtr) -> list: ...
    @staticmethod
    def SetInternalArray(col: Vector3dCollection, newArray: list, count: int) -> None: ...
    @staticmethod
    def TypedValuesToResbuf(values: list) -> IntPtr: ...

class ModuleLoadAbortedEventHandler:
    """.NET: Autodesk.AutoCAD.Runtime.ModuleLoadAbortedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: DynamicLinkerEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: DynamicLinkerEventArgs) -> None: ...

class ModuleLoadedEventHandler:
    """.NET: Autodesk.AutoCAD.Runtime.ModuleLoadedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: DynamicLinkerEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: DynamicLinkerEventArgs) -> None: ...

class ModuleLoadingEventHandler:
    """.NET: Autodesk.AutoCAD.Runtime.ModuleLoadingEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: DynamicLinkerEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: DynamicLinkerEventArgs) -> None: ...

class ModuleUnloadAbortedEventHandler:
    """.NET: Autodesk.AutoCAD.Runtime.ModuleUnloadAbortedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: DynamicLinkerEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: DynamicLinkerEventArgs) -> None: ...

class ModuleUnloadedEventHandler:
    """.NET: Autodesk.AutoCAD.Runtime.ModuleUnloadedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: DynamicLinkerEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: DynamicLinkerEventArgs) -> None: ...

class ModuleUnloadingEventHandler:
    """.NET: Autodesk.AutoCAD.Runtime.ModuleUnloadingEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: DynamicLinkerEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: DynamicLinkerEventArgs) -> None: ...

class Overrule(RXObject):
    """.NET: Autodesk.AutoCAD.Runtime.Overrule"""
    def __init__(self, *args) -> None: ...
    Overruling: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def AddOverrule(targetClass: RXClass, overrule: Overrule, bAtLast: bool) -> None: ...
    @staticmethod
    def HasOverrule(overruledSubject: RXObject, targetClass: RXClass) -> bool: ...
    def IsApplicable(self, overruledSubject: RXObject) -> bool: ...
    @staticmethod
    def RemoveOverrule(targetClass: RXClass, overrule: Overrule) -> None: ...
    def SetCustomFilter(self, ) -> None: ...
    def SetExtensionDictionaryEntryFilter(self, entryName: str) -> None: ...
    def SetIdFilter(self, ids: list) -> None: ...
    def SetNoFilter(self, ) -> None: ...
    def SetXDataFilter(self, registeredApplicationName: str) -> None: ...

class PerDocumentClassAttribute(Attribute):
    """.NET: Autodesk.AutoCAD.Runtime.PerDocumentClassAttribute"""
    def __init__(self, *args) -> None: ...
    Type: Type
    TypeId: object

class PointCloudExtractResult:
    """.NET: Autodesk.AutoCAD.Runtime.PointCloudExtractResult"""
    def __init__(self, *args) -> None: ...
    ...

class PointCloudExtractor(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Runtime.PointCloudExtractor"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def AppendLineProfile(profile: PointCloudExtractResult, spaceId: ObjectId, layer: str, color: Color) -> ObjectIdCollection: ...
    @staticmethod
    def AppendPolylineProfile(profile: PointCloudExtractResult, spaceId: ObjectId, layer: str, color: Color, polylineWidth: float) -> ObjectIdCollection: ...
    @staticmethod
    def Extract(pointCloud: PointCloudEx, planZDirection: Vector3d, planXDirection: Vector3d, pointOnPlan: Point3d, extractOption: ExtractOption, progress: IPointCloudExtractionProgressCallback) -> PointCloudExtractResult: ...

class ProfileCurve2d(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Runtime.ProfileCurve2d"""
    def __init__(self, *args) -> None: ...
    Arc: CircularArc2d
    LineSeg: LineSegment2d
    IsArc: bool
    IsSegment: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ProfileCurveType:
    """.NET enum: Autodesk.AutoCAD.Runtime.ProfileCurveType"""
    def __init__(self, *args) -> None: ...
    LineSeg: int  # = 0
    Arc: int  # = 1
class ProgressMeter(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Runtime.ProgressMeter"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def MeterProgress(self, ) -> None: ...
    def SetLimit(self, max: int) -> None: ...
    def Start(self, displayString: str) -> None: ...
    def Stop(self, ) -> None: ...

class RXClass(RXObject):
    """.NET: Autodesk.AutoCAD.Runtime.RXClass"""
    def __init__(self, *args) -> None: ...
    MyParent: RXClass
    ProxyFlags: int
    ClassVersion: Version
    Name: str
    DxfName: str
    AppName: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AddX(self, runtimeClass: RXClass, protocolExtension: RXObject) -> IntPtr: ...
    def Create(self, ) -> RXObject: ...
    def DelX(self, runtimeClass: RXClass) -> IntPtr: ...
    def GetRuntimeType(self, ) -> Type: ...
    def GetX(self, runtimeClass: RXClass) -> IntPtr: ...
    def IsDerivedFrom(self, runtimeClass: RXClass) -> bool: ...
    def QueryX(self, runtimeClass: RXClass) -> IntPtr: ...

class RXObject(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Runtime.RXObject"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Clone(self, ) -> object: ...
    def CompareTo(self, obj: object) -> int: ...
    def CopyFrom(self, source: RXObject) -> None: ...
    @staticmethod
    def Create(unmanagedPointer: IntPtr, autoDelete: bool) -> RXObject: ...
    @staticmethod
    def GetClass(type: Type) -> RXClass: ...
    def GetRXClass(self, ) -> RXClass: ...
    def QueryX(self, protocolClass: RXClass) -> IntPtr: ...
    def X(self, protocolClass: RXClass) -> IntPtr: ...

class Registry:
    """.NET: Autodesk.AutoCAD.Runtime.Registry"""
    def __init__(self, *args) -> None: ...
    CurrentConfig: RegistryKey
    ClassesRoot: RegistryKey
    CurrentUser: RegistryKey
    LocalMachine: RegistryKey

class RegistryKey:
    """.NET: Autodesk.AutoCAD.Runtime.RegistryKey"""
    def __init__(self, *args) -> None: ...
    ValueCount: int
    SubKeyCount: int
    def Close(self, ) -> None: ...
    def CreateSubKey(self, subkey: str, permissionCheck: RegistryKeyPermissionCheck, registryOptions: RegistryOptions, registrySecurity: RegistrySecurity) -> RegistryKey: ...
    def DeleteSubKey(self, subkey: str) -> None: ...
    def DeleteSubKeyTree(self, subkey: str) -> None: ...
    def DeleteValue(self, name: str) -> None: ...
    def Dispose(self, ) -> None: ...
    @staticmethod
    def GetBaseKey(hKey: RegistryHive) -> RegistryKey: ...
    def GetSubKeyNames(self, ) -> list: ...
    def GetValue(self, name: str, defaultValue: object, options: RegistryValueOptions) -> object: ...
    def GetValueKind(self, name: str) -> RegistryValueKind: ...
    def GetValueNames(self, ) -> list: ...
    @staticmethod
    def OpenBaseKey(hKey: RegistryHive, view: RegistryView) -> RegistryKey: ...
    def OpenSubKey(self, name: str, permissionCheck: RegistryKeyPermissionCheck, rights: RegistryRights) -> RegistryKey: ...
    def SetValue(self, name: str, value: object, kind: RegistryValueKind) -> None: ...

class RuntimeSystem:
    """.NET: Autodesk.AutoCAD.Runtime.RuntimeSystem"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def Initialize(hostServices: HostApplicationServices, localId: int) -> None: ...
    @staticmethod
    def Main(arg: IntPtr, argLength: int) -> int: ...
    @staticmethod
    def Terminate() -> None: ...

class SecuredApplicationAttribute(Attribute):
    """.NET: Autodesk.AutoCAD.Runtime.SecuredApplicationAttribute"""
    def __init__(self, *args) -> None: ...
    ClientPublicKey: str
    ClientSignature: str
    OurSignature: str
    License: str
    TypeId: object

class ShowExceptionDialogHandler:
    """.NET: Autodesk.AutoCAD.Runtime.ShowExceptionDialogHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, e: Exception, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, e: Exception) -> None: ...

class SynchronizationContext(SynchronizationContext):
    """.NET: Autodesk.AutoCAD.Runtime.SynchronizationContext"""
    def __init__(self, *args) -> None: ...
    def CreateCopy(self, ) -> SynchronizationContext: ...
    def OperationCompleted(self, ) -> None: ...
    def OperationStarted(self, ) -> None: ...
    def Post(self, d: SendOrPostCallback, state: object) -> None: ...
    def Send(self, d: SendOrPostCallback, state: object) -> None: ...
    def Wait(self, waitHandles: list, waitAll: bool, millisecondsTimeout: int) -> int: ...

class SystemObjects:
    """.NET: Autodesk.AutoCAD.Runtime.SystemObjects"""
    def __init__(self, *args) -> None: ...
    Variables: Variables
    DynamicLinker: DynamicLinker
    ServiceDictionary: Dictionary
    ClassDictionary: Dictionary

class SystemVariableEnumerator(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Runtime.SystemVariableEnumerator"""
    def __init__(self, *args) -> None: ...
    Current: Variable
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class UnhandledExceptionFilter:
    """.NET: Autodesk.AutoCAD.Runtime.UnhandledExceptionFilter"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def CerOrShowExceptionDialog(e: Exception) -> None: ...

class Utilities:
    """.NET: Autodesk.AutoCAD.Runtime.Utilities"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetErrorStatus(eStatus: ErrorStatus) -> str: ...
    @staticmethod
    def GetRedirectedRegistryValue(subPath: str, propertyName: str) -> str: ...
    @staticmethod
    def GetRedirectedRegistryValueMap(subPath: str) -> IDictionary: ...
    @staticmethod
    def GetReservedString(reservedType: ReservedStringEnumType, bGetLocalized: bool) -> str: ...
    @staticmethod
    def TranslateReservedString(pGlobalName: str) -> str: ...

class Variable(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Runtime.Variable"""
    def __init__(self, *args) -> None: ...
    Range: RangeInfo
    TypeFlags: int
    Storage: StorageType
    SecondaryType: SecondaryTypeInfo
    PrimaryType: int
    Name: str
    IsLocked: bool
    IsReadOnly: bool
    Value: object
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Reset(self, ) -> None: ...

class VariableChangedEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.Runtime.VariableChangedEventArgs"""
    def __init__(self, *args) -> None: ...
    NewValue: object
    OldValue: object
    def Dispose(self, ) -> None: ...

class VariableChangedEventHandler:
    """.NET: Autodesk.AutoCAD.Runtime.VariableChangedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: VariableChangedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: VariableChangedEventArgs) -> None: ...

class VariableChangingEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.Runtime.VariableChangingEventArgs"""
    def __init__(self, *args) -> None: ...
    IsResetting: bool
    NewValue: object
    OldValue: object
    def Dispose(self, ) -> None: ...
    def Veto(self, reason: str) -> None: ...

class VariableChangingEventHandler:
    """.NET: Autodesk.AutoCAD.Runtime.VariableChangingEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: VariableChangingEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: VariableChangingEventArgs) -> None: ...

class Variables(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Runtime.Variables"""
    def __init__(self, *args) -> None: ...
    Item: Variable
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetAllNames(self, ) -> list: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Reset(self, filter: StorageType) -> None: ...

class WrapperAttribute(Attribute):
    """.NET: Autodesk.AutoCAD.Runtime.WrapperAttribute"""
    def __init__(self, *args) -> None: ...
    WrappedClass: str
    TypeId: object
