# Auto-generated — Civil 26 — Autodesk.AutoCAD.Internal

class ADPUtil:
    """.NET: Autodesk.AutoCAD.Internal.ADPUtil"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def logData(waypointName: str, attrs: Dictionary) -> None: ...

class AcAeUtilities:
    """.NET: Autodesk.AutoCAD.Internal.AcAeUtilities"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetBeditConstraintColor(constraintType: ConstraintType) -> Color: ...
    @staticmethod
    def GetBlockName() -> str: ...
    @staticmethod
    def GetCurrentVisibilityStateName() -> str: ...
    @staticmethod
    def GetVisibilitySets(visibilities: List) -> None: ...
    @staticmethod
    def IsAuthorPaletteVisible() -> bool: ...
    @staticmethod
    def IsInBVMode() -> bool: ...
    @staticmethod
    def IsInBlockEditor() -> bool: ...
    @staticmethod
    def IsVisibilityParameterPresent() -> bool: ...
    @staticmethod
    def PickFirstBeforeInvokeBvHide() -> bool: ...
    @staticmethod
    def PickFirstBeforeInvokeBvShow() -> bool: ...
    @staticmethod
    def SetBeditConstraintColor(constraintType: ConstraintType, color: Color) -> None: ...
    @staticmethod
    def ShowAuthorPalette(bShow: bool) -> None: ...

class AcDownloadCallback:
    """.NET: Autodesk.AutoCAD.Internal.AcDownloadCallback"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, ) -> None: ...

class AcNavisworksProtocolAdapter:
    """.NET: Autodesk.AutoCAD.Internal.AcNavisworksProtocolAdapter"""
    def __init__(self, *args) -> None: ...
    ...

class AcNavisworksService:
    """.NET: Autodesk.AutoCAD.Internal.AcNavisworksService"""
    def __init__(self, *args) -> None: ...
    def Dispose(self, ) -> None: ...
    def RegisterFileProtocol(self, scheme: str, fileprotocol: INavisworksFileProtocol) -> None: ...

class AcShareFileData:
    """.NET: Autodesk.AutoCAD.Internal.AcShareFileData"""
    def __init__(self, *args) -> None: ...
    ...

class AcSmUtils:
    """.NET: Autodesk.AutoCAD.Internal.AcSmUtils"""
    def __init__(self, *args) -> None: ...
    SheetSetCmdAllowed: bool
    @staticmethod
    def GetDrawingsFromSheetSet(sheetSetPath: str, dwgList: Hashtable) -> None: ...
    @staticmethod
    def IsSheetSet(path: str) -> bool: ...
    @staticmethod
    def OpenSheetSet(path: str) -> None: ...

class AcWorkItemUtils:
    """.NET: Autodesk.AutoCAD.Internal.AcWorkItemUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def getProductName() -> str: ...
    @staticmethod
    def parseWorkItemMessage(resultJsonStr: str, requestId: str) -> None: ...

class AcadTaskDialogs:
    """.NET: Autodesk.AutoCAD.Internal.AcadTaskDialogs"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def ShowCurrentLayerOff() -> int: ...
    @staticmethod
    def ShowDuplicateNameCopyReplaceTD(objectname: str, duplicatename: str, copyname: str, pParentWnd: IntPtr) -> int: ...
    @staticmethod
    def ShowDuplicateNameErrorTD(objectname: str, duplicatename: str, pParentWnd: IntPtr) -> int: ...
    @staticmethod
    def ShowDuplicateNameReplaceCancelTD(objectname: str, duplicatename: str, pParentWnd: IntPtr) -> int: ...
    @staticmethod
    def ShowFileConfirmationWithNoToAll(featureName: str, featureType: str, fullFileName: str, fileName: str, pParentWnd: IntPtr) -> int: ...
    @staticmethod
    def ShowFileConfirmationWithoutNoToAll(featureName: str, featureType: str, fullFileName: str, fileName: str, pParentWnd: IntPtr) -> int: ...
    @staticmethod
    def ShowInvalidNameEmptyNameTD(objectname: str, fieldname: str, pParentWnd: IntPtr) -> None: ...
    @staticmethod
    def ShowInvalidNameTooLongTD(objectname: str, fieldname: str, pParentWnd: IntPtr) -> None: ...
    @staticmethod
    def ShowInvalidNameUnsupportedCharactersTD(objectname: str, fieldname: str, pParentWnd: IntPtr) -> None: ...
    @staticmethod
    def ShowLayerCannotFreeze() -> None: ...
    @staticmethod
    def Source() -> Uri: ...

class ActiveThemeColor:
    """.NET: Autodesk.AutoCAD.Internal.ActiveThemeColor"""
    def __init__(self, *args) -> None: ...
    CurrentTheme: ColorThemeEnum
    InspectorBGHighlight: Color
    InspectorItem: Color
    PaletteBackground: Color
    @staticmethod
    def Instance() -> ActiveThemeColor: ...

class AppLoaderDownloadUtils:
    """.NET: Autodesk.AutoCAD.Internal.AppLoaderDownloadUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def CancelDownloadJob(nToken: int) -> None: ...

class AppMenuUtil:
    """.NET: Autodesk.AutoCAD.Internal.AppMenuUtil"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def Initialize() -> ValueTuple: ...
    @staticmethod
    def IsApplicationRegistered(appName: str) -> bool: ...
    @staticmethod
    def RibbonDockedTop(top: bool) -> None: ...
    @staticmethod
    def SuspendAlt(suspend: bool) -> None: ...

class AttachUtil:
    """.NET: Autodesk.AutoCAD.Internal.AttachUtil"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def CheckDwgFile(csDwgPath: str) -> bool: ...
    @staticmethod
    def CheckImageFile(csImagePath: str) -> bool: ...
    @staticmethod
    def CmdLineImageAttach(strImageFile: str) -> None: ...
    @staticmethod
    def CmdLineNavisworksAttach(strNavisworksFile: str) -> None: ...
    @staticmethod
    def CmdLinePointCloudAttach(strPointCloudFile: str) -> None: ...
    @staticmethod
    def CmdLineXAttach(strDWGFile: str) -> bool: ...
    def Dispose(self, ) -> None: ...
    @staticmethod
    def GetImageFileExtensions() -> str: ...
    @staticmethod
    def GetImageFilterString() -> str: ...
    @staticmethod
    def GetOpenFilesResult(opt: PromptOpenFileOptions, multiSelArray: list) -> list: ...
    @staticmethod
    def ImageAdjust(objIds: list) -> None: ...
    @staticmethod
    def ImageAttach(strImageFile: str) -> None: ...
    @staticmethod
    def ImageClip(objId: ObjectId) -> None: ...
    @staticmethod
    def IsPCAttachAllowed() -> bool: ...
    @staticmethod
    def LoadBIMUnderlayArx() -> None: ...
    @staticmethod
    def LoadBIMUnderlayCrx() -> None: ...
    @staticmethod
    def LoadISM() -> None: ...
    @staticmethod
    def LoadPointCloudArx() -> None: ...
    @staticmethod
    def LoadPointCloudCrx() -> None: ...
    @staticmethod
    def NavisworksAttach(strNavisworksFile: str) -> None: ...
    @staticmethod
    def PointCloudAttach(strPointCloudFile: str) -> None: ...
    @staticmethod
    def PointCloudClip(objId: ObjectId) -> None: ...
    @staticmethod
    def VPClip() -> None: ...
    @staticmethod
    def XAttach(strDWGFileArray: list) -> None: ...
    @staticmethod
    def XClip() -> None: ...
    @staticmethod
    def isDialogShow() -> bool: ...

class BlockDisplayItem(DependencyObject):
    """.NET: Autodesk.AutoCAD.Internal.BlockDisplayItem"""
    def __init__(self, *args) -> None: ...
    GeneratePreviewInLocalServer: bool
    UseDefaultThumbnail: bool
    IsFromCurrentDrawing: bool
    InsUnit: UnitsValue
    Explodable: bool
    SnapshotInfo: BlockSnapshotInfo
    SerializeState: BlockSnapshotSerializeState
    Id: ObjectId
    IsThumbnailGenerated: bool
    GeoCoordSystemId: str
    HasGeoData: bool
    ScaleUniformly: bool
    AllowExplode: bool
    IsBlockOriented: bool
    IsAnnotative: bool
    IsDynamic: bool
    IsVisible: bool
    IsValid: bool
    ThumbnailSize: int
    ViewMode: BlockViewMode
    ItemType: ItemTypeEnum
    FavoriteTime: int
    ModifyTime: int
    InsertTime: int
    IsPinned: bool
    ToolTipImageState: ThumbnailGenerateState
    ThumbnailState: ThumbnailGenerateState
    ToolTipImageSize: int
    ToolTipImage: ImageSource
    Thumbnail: ImageSource
    PreviewImage: str
    TranslatedURL: str
    URL: str
    ThumbnailLabel: str
    Name: str
    Key: str
    DependencyObjectType: DependencyObjectType
    IsSealed: bool
    Dispatcher: Dispatcher
    def ToBlockSelectedItemData(self, ) -> str: ...
    def ToString(self, ) -> str: ...
    def copyFrom(self, other: BlockDisplayItem) -> None: ...
    @staticmethod
    def createDrawingAsBlockItem(fullPathName: str) -> BlockDisplayItem: ...
    @staticmethod
    def createDrawingDisplayItem(fullPathName: str, viewMode: BlockViewMode) -> BlockDisplayItem: ...
    @staticmethod
    def generateKey(btrId: ValueType, asCurrentDwgBlock: bool) -> str: ...
    def generateThumbnail(self, ) -> None: ...
    def generateToolTipThumbnail(self, size: int) -> None: ...
    def hasThumbnailCreated(self, ) -> bool: ...
    def hasToolTipImageCreated(self, ) -> bool: ...
    def isEqualTo(self, other: BlockDisplayItem) -> bool: ...
    def refreshBlockStandardIcon(self, ) -> None: ...
    def resetThumbnail(self, ) -> None: ...
    def resetToolTipThumbnail(self, ) -> None: ...
    def setThumbnailToDefault(self, ) -> None: ...
    def setTooltipThumbnailToDefault(self, ) -> None: ...

class BlockLibraryPathChangedEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.Internal.BlockLibraryPathChangedEventArgs"""
    def __init__(self, *args) -> None: ...
    BlockLibraryPath: str

class BlockPaletteNeedUpdateEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.Internal.BlockPaletteNeedUpdateEventArgs"""
    def __init__(self, *args) -> None: ...
    PaletteName: str

class BlockPermissionMgr:
    """.NET: Autodesk.AutoCAD.Internal.BlockPermissionMgr"""
    def __init__(self, *args) -> None: ...
    IsAuthorized: bool
    Instance: BlockPermissionMgr
    def Dispose(self, ) -> None: ...

class BlockSnapshotInfo:
    """.NET: Autodesk.AutoCAD.Internal.BlockSnapshotInfo"""
    def __init__(self, *args) -> None: ...
    targetBlockName: str
    snapshotUrl: str

class BlockSnapshotSerializeState:
    """.NET enum: Autodesk.AutoCAD.Internal.BlockSnapshotSerializeState"""
    def __init__(self, *args) -> None: ...
    kInMemory: int  # = 0
    kSerializable: int  # = 1
    kSerializing: int  # = 2
    kSerialized: int  # = 3
    kDeleted: int  # = 4
class BlockSpotTools:
    """.NET: Autodesk.AutoCAD.Internal.BlockSpotTools"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def IsValidForTextToAttribute(document: Document) -> bool: ...

class BlockStreamCIPLog:
    """.NET: Autodesk.AutoCAD.Internal.BlockStreamCIPLog"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def logBlockPaletteClosed() -> None: ...
    @staticmethod
    def logBlockPaletteOpened() -> None: ...
    @staticmethod
    def logBlockrecentfolderSysvarInfo(valueType: str) -> None: ...
    @staticmethod
    def logCountOfAutoPlacementChecked() -> None: ...
    @staticmethod
    def logCountOfCurrentTabSwitchedTo() -> None: ...
    @staticmethod
    def logCountOfCurrentTabUsed() -> None: ...
    @staticmethod
    def logCountOfExplodeChecked() -> None: ...
    @staticmethod
    def logCountOfExternalTabSwitchedTo() -> None: ...
    @staticmethod
    def logCountOfExternalTabUsed() -> None: ...
    @staticmethod
    def logCountOfFavoritesTabSwitchedTo() -> None: ...
    @staticmethod
    def logCountOfFavoritesTabUsed() -> None: ...
    @staticmethod
    def logCountOfInsertPointChecked() -> None: ...
    @staticmethod
    def logCountOfRecentTabSwitchedTo() -> None: ...
    @staticmethod
    def logCountOfRecentTabUsed() -> None: ...
    @staticmethod
    def logCountOfRepeatChecked() -> None: ...
    @staticmethod
    def logCountOfRotationChecked() -> None: ...
    @staticmethod
    def logCountOfScaleChecked() -> None: ...
    @staticmethod
    def logCountOfScaleUniformUsed() -> None: ...
    @staticmethod
    def logCountOfStartOnBoardingProcessFromMessage() -> None: ...
    @staticmethod
    def logCountOfStartOnBoardingProcessFromPage() -> None: ...
    @staticmethod
    def logCountOfStartOnBoardingProcessFromSyncSetting() -> None: ...
    @staticmethod
    def logCurrentTabUsedMetaData(bMetaDataUsedInCurrentDrawingTab: bool) -> None: ...
    @staticmethod
    def logDwgInsertedAsABlock() -> None: ...
    @staticmethod
    def logFavoriteBlockSize(averageSize: float, maxSize: float, minSize: float, snapshotCount: int) -> None: ...
    @staticmethod
    def logFavoriteBlocksData(totalBlockCount: int, uniqueBlockNameCount: int, duplicatingNamedBlockCount: int, duplicatingUniqueBlockNameCount: int) -> None: ...
    @staticmethod
    def logFileSelectedAsLibrary() -> None: ...
    @staticmethod
    def logFolderSelectedAsLibrary(countOfFilesInFolder: int) -> None: ...
    @staticmethod
    def logInsertDwgAsABlockFromFolder() -> None: ...
    @staticmethod
    def logLibraryInfo(libraryOperation: str, libraryType: str) -> None: ...
    @staticmethod
    def logLocalServerActivityInfo(activityType: str, runTime: int, status: str) -> None: ...
    @staticmethod
    def logNonDwgBlockInserted() -> None: ...
    @staticmethod
    def logNumberOfBlocksInCurrentTab(count: int) -> None: ...
    @staticmethod
    def logNumberOfBlocksInExternalTab(count: int) -> None: ...
    @staticmethod
    def logNumberOfBlocksInFavoritesTab(count: int) -> None: ...
    @staticmethod
    def logNumberOfBlocksInRecentTab(count: int) -> None: ...
    @staticmethod
    def logOnboardingCompleted(sSyncFolder: str) -> None: ...
    @staticmethod
    def logSearchUsed() -> None: ...
    @staticmethod
    def logSuppressAllSetMessage(isCloudSyncFolder: bool) -> None: ...
    @staticmethod
    def logSuppressSyncBlockMessage() -> None: ...
    @staticmethod
    def logSyncFolderChangedFromSyncSettingDialog(sSyncFolder: AcString) -> None: ...
    @staticmethod
    def logWayToInsertBlockByContextMenu() -> None: ...
    @staticmethod
    def logWayToInsertBlockByContextMenuInsert() -> None: ...
    @staticmethod
    def logWayToInsertBlockByContextMenuInsertAndExplode() -> None: ...
    @staticmethod
    def logWayToInsertBlockByContextMenuInsertAndRedefine() -> None: ...
    @staticmethod
    def logWayToInsertBlockByContextMenuRedefineOnly() -> None: ...
    @staticmethod
    def logWayToInsertBlockByDoubleClick() -> None: ...
    @staticmethod
    def logWayToInsertBlockByDragDrop() -> None: ...
    @staticmethod
    def logWayToInsertBlockByDrawingAsBlockButton() -> None: ...
    @staticmethod
    def logWayToInsertBlockByDrawingAsBlockButtonSuccess() -> None: ...
    @staticmethod
    def logWayToInsertBlockBySinglelick() -> None: ...

class BlockStreamLocalServer:
    """.NET: Autodesk.AutoCAD.Internal.BlockStreamLocalServer"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def displayItemToBlockPreviewInfo(displayItem: BlockDisplayItem, bForToolTip: bool) -> mgBlockPreviewInfo: ...
    @staticmethod
    def getBlockNameListResultJsonUrlName() -> str: ...
    @staticmethod
    def getBlockNameListResultReadyStr() -> str: ...
    @staticmethod
    def getBlockPreviewpartialResultName() -> str: ...
    @staticmethod
    def getFileModifyTime(filePath: str) -> int: ...
    @staticmethod
    def getRequestDict() -> Dictionary: ...
    @staticmethod
    def getRequstBlocksStr(displayList: List) -> str: ...
    @staticmethod
    def pushBlockPreviewGenerationRequest(displayItem: BlockDisplayItem, bForToolTip: bool) -> bool: ...
    @staticmethod
    def useLocalServerForBlock(blockDisplayItem: BlockDisplayItem) -> bool: ...

class BlockStreamLog:
    """.NET: Autodesk.AutoCAD.Internal.BlockStreamLog"""
    def __init__(self, *args) -> None: ...
    def Dispose(self, ) -> None: ...
    @staticmethod
    def debug(message: AcString) -> None: ...
    @staticmethod
    def error(message: AcString) -> None: ...
    @staticmethod
    def inform(message: AcString) -> None: ...
    @staticmethod
    def init() -> None: ...
    @staticmethod
    def isInitialized() -> bool: ...
    @staticmethod
    def isLogEnabled() -> bool: ...
    @staticmethod
    def setLogEnableState(val: bool) -> None: ...
    @staticmethod
    def uninit() -> None: ...
    @staticmethod
    def warning(message: AcString) -> None: ...

class BlockStreamUtils:
    """.NET: Autodesk.AutoCAD.Internal.BlockStreamUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def FindFile(FullPathName: str) -> bool: ...
    @staticmethod
    def GetClientId() -> str: ...
    @staticmethod
    def GetLocalServerUage() -> int: ...
    @staticmethod
    def GetPreviewGenerateMethod() -> int: ...
    @staticmethod
    def GetPreviewParameter(viewMode: BlockViewMode) -> str: ...
    @staticmethod
    def GetPreviewParameterAsJsonString(viewMode: BlockViewMode, bForFileSnapshot: bool) -> str: ...
    @staticmethod
    def IsCloudDriveSyncFolder(dir: str) -> bool: ...
    @staticmethod
    def IsMetadataValid(dwgFileUrl: str, metadataRootDir: str, viewMode: BlockViewMode, bDarakTheme: bool, bForFileSnapShot: bool, bMiniValidation: bool) -> bool: ...
    @staticmethod
    def Log(msg: str) -> None: ...
    @staticmethod
    def OnBlockThumbnailGenerated(fileName: str, blockName: str, width: int, height: int, bkColorRed: int, bkColorGreen: int, bkColorBlue: int, bUseBlackForWhite: bool, bForTooltip: bool, pngFilePath: str, itemToUpdate: BlockDisplayItem) -> None: ...
    @staticmethod
    def UpdateDisplayItemFromPartialResults(resultsFile: str, dataSources: ObservableCollection) -> bool: ...
    @staticmethod
    def UseLocalServerForActivities() -> bool: ...
    @staticmethod
    def UseLocalServerForMetadata() -> bool: ...
    @staticmethod
    def UseWhipToGeneratePreview() -> bool: ...
    @staticmethod
    def blockIndexCachePath() -> str: ...
    @staticmethod
    def cleanupSnapshotFromRecentBlockList(snapshotInfo: BlockSnapshotInfo) -> None: ...
    @staticmethod
    def closeInSideDbPool(key: str) -> None: ...
    @staticmethod
    def combineRecentBlocksPath(recent_item: Dictionary) -> str: ...
    @staticmethod
    def convertProviderToProviderDetail(inputProvider: str, outputTechnology: str, outputSubscription: str) -> bool: ...
    @staticmethod
    def convertToSecureTranslatedPath(translatedPath: str) -> str: ...
    @staticmethod
    def doDragDrop(item: BlockDisplayItem) -> int: ...
    @staticmethod
    def getAbsolutePath(provider: str, accountEmail: str, relativePath: str) -> str: ...
    @staticmethod
    def getBlockNavigateFile() -> str: ...
    @staticmethod
    def getBlockOnBoardingFolder() -> str: ...
    @staticmethod
    def getBlockPreviewImageType(previewImage: Image) -> ImageCacheType: ...
    @staticmethod
    def getBlockRecentOnBoardingFolder() -> str: ...
    @staticmethod
    def getBlocksFromExternalFile(FullPathName: str, metadataRoot: str, bNeedEntireDrawing: bool, viewMode: BlockViewMode, bDarkTheme: bool) -> ObservableCollection: ...
    @staticmethod
    def getBlocksFromPartialResults(FullPathName: str, partialResultsJsonFilePath: str, bNeedEntireDrawing: bool, viewMode: BlockViewMode) -> ObservableCollection: ...
    @staticmethod
    def getCurrentDrawingBlocks(viewMode: BlockViewMode) -> ObservableCollection: ...
    @staticmethod
    def getDwgDisplayItem(FullPathName: str, viewMode: BlockViewMode) -> BlockDisplayItem: ...
    @staticmethod
    def getFilePathType(path: str) -> str: ...
    @staticmethod
    def getLastAccessedLibrary() -> str: ...
    @staticmethod
    def getLastAccessedLibraryNode() -> str: ...
    @staticmethod
    def getLibraryList() -> List: ...
    @staticmethod
    def getRealPath(path: str) -> str: ...
    @staticmethod
    def getRecentBlocks(viewMode: BlockViewMode) -> ObservableCollection: ...
    @staticmethod
    def getSerializedBlocks(viewMode: BlockViewMode) -> List: ...
    @staticmethod
    def getThumbnailSize(viewMode: BlockViewMode) -> int: ...
    @staticmethod
    def isBlockSyncFolderCustomizedToLocal() -> bool: ...
    @staticmethod
    def isBlockSyncFolderSetToCloudStorage() -> bool: ...
    @staticmethod
    def isDragDropTempBlock(blockId: ValueType) -> bool: ...
    @staticmethod
    def isLocalPath(filePath: str) -> bool: ...
    @staticmethod
    def isPaletteVisible() -> bool: ...
    @staticmethod
    def isProductEnableDataSyncing() -> bool: ...
    @staticmethod
    def isReadyToLoadSideDb() -> bool: ...
    @staticmethod
    def isSystemBlock(blockId: ValueType) -> bool: ...
    @staticmethod
    def isSystemBlockInCurDb(blockName: str) -> bool: ...
    @staticmethod
    def isUnsavedBlock(block: BlockDisplayItem) -> bool: ...
    @staticmethod
    def isValidBlockName(blockName: str, allowExtendedNames: bool) -> bool: ...
    @staticmethod
    def makeTransparentImage(srcPngPath: str, targetTransparentPngPath: str) -> None: ...
    @staticmethod
    def notifyBlockLibraryPathChanged(strPath: str) -> None: ...
    @staticmethod
    def notifyBlockPaletteNeedUpdate(strPath: str) -> None: ...
    @staticmethod
    def onBlockSuggestionResultReceived(resultJsonStr: str, requestId: str) -> None: ...
    @staticmethod
    def openInSideDbPool(key: str) -> None: ...
    @staticmethod
    def parseConentKey(contentKey: str) -> Tuple: ...
    @staticmethod
    def parseJsonBlockPreview(resultJsonStr: str, itemsToUpdate: List) -> None: ...
    @staticmethod
    def parseRecentBlocksPath(path: str) -> Dictionary: ...
    @staticmethod
    def readRegistryInt(keyName: str, defValue: int) -> int: ...
    @staticmethod
    def readRegistryString(keyName: str, defValue: str) -> str: ...
    @staticmethod
    def refreshCurrentDwgBlocks(oldCurrentDwgBlocks: ObservableCollection, viewMode: BlockViewMode) -> None: ...
    @staticmethod
    def refreshRecentBlocks(oldRecentBlocks: ObservableCollection, viewMode: BlockViewMode) -> None: ...
    @staticmethod
    def removeFromRecentBlocks(itemToBeRemoved: BlockDisplayItem) -> None: ...
    @staticmethod
    def safePathCombine(folderPath: str, fileName: str) -> str: ...
    @staticmethod
    def saveSerializedBlocks(blocksToSerialize: List) -> None: ...
    @staticmethod
    def setLastAccessedLibrary(value: str) -> None: ...
    @staticmethod
    def setLastAccessedLibraryNode(value: str) -> None: ...
    @staticmethod
    def setRecentBlockPinned(key: str, val: bool) -> None: ...
    @staticmethod
    def showBlockOnBoardingGuideDialog() -> bool: ...
    @staticmethod
    def writeRegistryInt(keyName: str, value: int) -> None: ...
    @staticmethod
    def writeRegistryString(keyName: str, value: str) -> None: ...

class BlockViewMode:
    """.NET enum: Autodesk.AutoCAD.Internal.BlockViewMode"""
    def __init__(self, *args) -> None: ...
    kExtraLargeIcon: int  # = 0
    kLargeIcon: int  # = 1
    kMediumIcon: int  # = 2
    kSmallIcon: int  # = 3
    kDetails: int  # = 4
    kList: int  # = 5
class BlockViewModeEnum:
    """.NET: Autodesk.AutoCAD.Internal.BlockViewModeEnum"""
    def __init__(self, *args) -> None: ...
    ...

class COwnerDrawComboBoxWrapper(ComboBox):
    """.NET: Autodesk.AutoCAD.Internal.COwnerDrawComboBoxWrapper"""
    def __init__(self, *args) -> None: ...
    AutoCompleteMode: AutoCompleteMode
    AutoCompleteSource: AutoCompleteSource
    AutoCompleteCustomSource: AutoCompleteStringCollection
    BackColor: Color
    BackgroundImage: Image
    BackgroundImageLayout: ImageLayout
    DataSource: object
    DrawMode: DrawMode
    DropDownWidth: int
    DropDownHeight: int
    DroppedDown: bool
    FlatStyle: FlatStyle
    Focused: bool
    ForeColor: Color
    IntegralHeight: bool
    ItemHeight: int
    Items: ObjectCollection
    MaxDropDownItems: int
    MaximumSize: Size
    MinimumSize: Size
    MaxLength: int
    Padding: Padding
    PreferredHeight: int
    SelectedIndex: int
    SelectedItem: object
    SelectedText: str
    SelectionLength: int
    SelectionStart: int
    Sorted: bool
    DropDownStyle: ComboBoxStyle
    Text: str
    DisplayMember: str
    FormatInfo: IFormatProvider
    FormatString: str
    FormattingEnabled: bool
    ValueMember: str
    SelectedValue: object
    AccessibilityObject: AccessibleObject
    AccessibleDefaultActionDescription: str
    AccessibleDescription: str
    AccessibleName: str
    AccessibleRole: AccessibleRole
    AllowDrop: bool
    Anchor: AnchorStyles
    AutoSize: bool
    AutoScrollOffset: Point
    LayoutEngine: LayoutEngine
    DataContext: object
    BindingContext: BindingContext
    Bottom: int
    Bounds: Rectangle
    CanFocus: bool
    CanSelect: bool
    Capture: bool
    CausesValidation: bool
    ClientRectangle: Rectangle
    ClientSize: Size
    CompanyName: str
    ContainsFocus: bool
    ContextMenuStrip: ContextMenuStrip
    Controls: ControlCollection
    Created: bool
    Cursor: Cursor
    DataBindings: ControlBindingsCollection
    DeviceDpi: int
    DisplayRectangle: Rectangle
    IsDisposed: bool
    Disposing: bool
    Dock: DockStyle
    Enabled: bool
    Font: Font
    Handle: IntPtr
    HasChildren: bool
    Height: int
    IsHandleCreated: bool
    InvokeRequired: bool
    IsAccessible: bool
    IsAncestorSiteInDesignMode: bool
    IsMirrored: bool
    Left: int
    Location: Point
    Margin: Padding
    Name: str
    Parent: Control
    ProductName: str
    ProductVersion: str
    RecreatingHandle: bool
    Region: Region
    Right: int
    RightToLeft: RightToLeft
    Site: ISite
    Size: Size
    TabIndex: int
    TabStop: bool
    Tag: object
    Top: int
    TopLevelControl: Control
    UseWaitCursor: bool
    Visible: bool
    Width: int
    WindowTarget: IWindowTarget
    PreferredSize: Size
    ContextMenu: ContextMenu
    ImeMode: ImeMode
    Container: IContainer

class CertificationUtil:
    """.NET: Autodesk.AutoCAD.Internal.CertificationUtil"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetDiagnosisStatus() -> int: ...
    @staticmethod
    def GetGraphicsAdapters() -> List: ...

class CipUtils:
    """.NET: Autodesk.AutoCAD.Internal.CipUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def Instance() -> CipUtils: ...
    def IsOperational(self, ) -> bool: ...
    def LogApplicationMenuCommandExecute(self, id: str, sCmd: str, insightsMacroId: str) -> None: ...
    def LogGPUTextOnOff(self, value: int) -> None: ...
    def LogIcLaunch(self, icType: int, group: str, category: str, title: str, url: str) -> None: ...
    def LogIcQuery(self, queryString: str, buttonIndex: int) -> None: ...
    def LogInfoCenterCommandExecute(self, id: str, sCmd: str, type: int) -> None: ...
    def LogModelessLayerItem(self, cmdStr: str, bInRibbon: bool) -> None: ...
    def LogQuickAccessToolbarCommandExecute(self, id: str, sCmd: str, insightsMacroId: str) -> None: ...
    def LogRibbonItemCommandExecute(self, sCmd: str, sTabName: str, sPanelName: str, bMenuMacro: bool, dockSide: int, insightsMacroId: str) -> None: ...
    def LogStatusBarElementVisibility(self, elementName: str, isVisible: bool) -> None: ...
    def SetUaLaunchType(self, uaLaunchType: str) -> None: ...
    def WaypointReachedWithAttributes(self, waypoint: str, state: str, attrs: Dictionary) -> None: ...
    def WaypointReachedWithNoState(self, waypoint: str) -> None: ...
    def WaypointReachedWithStringAtt(self, waypoint: str, state: str, att: str, strAttValue: str) -> None: ...
    def getMacroString(self, macro: str) -> str: ...
    def getSessionId(self, ) -> str: ...

class CloudPrintingServiceManager:
    """.NET: Autodesk.AutoCAD.Internal.CloudPrintingServiceManager"""
    def __init__(self, *args) -> None: ...
    Host: ICloudPrintingService

class ColorThemeChangedEventHandler:
    """.NET: Autodesk.AutoCAD.Internal.ColorThemeChangedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: EventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: EventArgs) -> None: ...

class ColorThemeEnum:
    """.NET enum: Autodesk.AutoCAD.Internal.ColorThemeEnum"""
    def __init__(self, *args) -> None: ...
    Dark: int  # = 0
    Light: int  # = 1
    User: int  # = 2
class ComboBoxWrapper(ControlWrapper):
    """.NET: Autodesk.AutoCAD.Internal.ComboBoxWrapper"""
    def __init__(self, *args) -> None: ...
    AccessibilityObject: AccessibleObject
    AccessibleDefaultActionDescription: str
    AccessibleDescription: str
    AccessibleName: str
    AccessibleRole: AccessibleRole
    AllowDrop: bool
    Anchor: AnchorStyles
    AutoSize: bool
    AutoScrollOffset: Point
    LayoutEngine: LayoutEngine
    DataContext: object
    BackColor: Color
    BackgroundImage: Image
    BackgroundImageLayout: ImageLayout
    BindingContext: BindingContext
    Bottom: int
    Bounds: Rectangle
    CanFocus: bool
    CanSelect: bool
    Capture: bool
    CausesValidation: bool
    ClientRectangle: Rectangle
    ClientSize: Size
    CompanyName: str
    ContainsFocus: bool
    ContextMenuStrip: ContextMenuStrip
    Controls: ControlCollection
    Created: bool
    Cursor: Cursor
    DataBindings: ControlBindingsCollection
    DeviceDpi: int
    DisplayRectangle: Rectangle
    IsDisposed: bool
    Disposing: bool
    Dock: DockStyle
    Enabled: bool
    Focused: bool
    Font: Font
    ForeColor: Color
    Handle: IntPtr
    HasChildren: bool
    Height: int
    IsHandleCreated: bool
    InvokeRequired: bool
    IsAccessible: bool
    IsAncestorSiteInDesignMode: bool
    IsMirrored: bool
    Left: int
    Location: Point
    Margin: Padding
    MaximumSize: Size
    MinimumSize: Size
    Name: str
    Parent: Control
    ProductName: str
    ProductVersion: str
    RecreatingHandle: bool
    Region: Region
    Right: int
    RightToLeft: RightToLeft
    Site: ISite
    Size: Size
    TabIndex: int
    TabStop: bool
    Tag: object
    Text: str
    Top: int
    TopLevelControl: Control
    UseWaitCursor: bool
    Visible: bool
    Width: int
    WindowTarget: IWindowTarget
    PreferredSize: Size
    Padding: Padding
    ContextMenu: ContextMenu
    ImeMode: ImeMode
    Container: IContainer

class CommandCallback:
    """.NET: Autodesk.AutoCAD.Internal.CommandCallback"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, ) -> None: ...

class CommandPiper:
    """.NET: Autodesk.AutoCAD.Internal.CommandPiper"""
    def __init__(self, *args) -> None: ...
    BlockingCommands: int
    QueueCount: int
    LayerCount: int
    @staticmethod
    def CommandWillStart(layerMgrCtrlId: int) -> bool: ...
    @staticmethod
    def CommandsSentButNotStartedClear() -> None: ...
    def Dispose(self, ) -> None: ...
    @staticmethod
    def GetRegenLayers(layerIds: ObjectIdCollection) -> int: ...
    @staticmethod
    def IsBlockingCommand(cmdName: str) -> bool: ...
    def LayerClose(self, ) -> None: ...
    def LayerColor(self, value: Color, layerName: str) -> bool: ...
    def LayerCurrent(self, layerName: str) -> None: ...
    def LayerDelete(self, layerName: str) -> None: ...
    def LayerDescription(self, value: str, existingValueEmpty: bool, layerName: str) -> None: ...
    def LayerFilterDelete(self, filtersNames: ArrayList) -> None: ...
    def LayerFilterEditGroup(self, add: bool, filterName: str, layerName: str) -> None: ...
    def LayerFilterEditGroupReplace(self, filterName: str, parentName: str, layerNames: ArrayList) -> None: ...
    def LayerFilterEditPropertyConvert(self, filterName: str) -> None: ...
    def LayerFilterEditPropertyDef(self, filterName: str, filterExpression: str) -> None: ...
    def LayerFilterNewGroup(self, filterName: str, parentName: str) -> None: ...
    def LayerFilterNewProperty(self, filterName: str, filterExpression: str, parentName: str) -> None: ...
    def LayerFilterRename(self, value: str, filterName: str) -> None: ...
    def LayerFilterSet(self, filterName: str) -> None: ...
    def LayerFrozen(self, value: bool, layerName: str, layerId: ObjectId) -> None: ...
    def LayerLineWeight(self, value: LineWeight, layerName: str) -> None: ...
    def LayerLinetype(self, value: str, layerName: str) -> None: ...
    def LayerLocked(self, value: bool, layerName: str) -> None: ...
    def LayerNew(self, layerName: str) -> None: ...
    def LayerOffCurrent(self, layerName: str) -> None: ...
    def LayerOn(self, value: bool, layerName: str) -> None: ...
    def LayerPlot(self, value: bool, layerName: str) -> None: ...
    def LayerPlotStyle(self, value: str, layerName: str) -> None: ...
    def LayerReconcile(self, layerName: str) -> None: ...
    def LayerRename(self, value: str, layerName: str) -> None: ...
    def LayerTemplate(self, protoName: str, layerName: str, showUsed: bool, freezeInAllVPs: bool) -> None: ...
    def LayerTransparency(self, value: str, layerName: str) -> None: ...
    @staticmethod
    def OnCommandEnded() -> bool: ...
    @staticmethod
    def QueueClear() -> None: ...
    @staticmethod
    def QueueSend() -> None: ...
    def Send(self, ) -> None: ...
    @staticmethod
    def SkipUpdate() -> bool: ...
    def VplayerColor(self, value: Color, all: bool, layerName: str) -> bool: ...
    def VplayerFrozen(self, value: bool, flag: VPType, layerName: str, layerId: ObjectId) -> None: ...
    def VplayerLineWeight(self, value: LineWeight, all: bool, layerName: str) -> None: ...
    def VplayerLinetype(self, value: str, all: bool, layerName: str) -> None: ...
    def VplayerPlotStyle(self, value: str, all: bool, layerName: str) -> None: ...
    def VplayerRemoveOverrides(self, theProperty: str, all: bool, layerName: str) -> None: ...
    def VplayerReset(self, all: bool, layerName: str) -> None: ...
    def VplayerTransparency(self, value: str, all: bool, layerName: str) -> None: ...
    def VplayerViewportVisibilityDefault(self, bFrozen: bool, all: bool, layerName: str) -> None: ...

class CommandTypeFlags:
    """.NET enum: Autodesk.AutoCAD.Internal.CommandTypeFlags"""
    def __init__(self, *args) -> None: ...
    NoneCmd: int  # = 0
    CoreCmd: int  # = 1
    ARXCmd: int  # = 2
    LispCmd: int  # = 3
    ActionMacroCmd: int  # = 4
    SetvarCmd: int  # = 5
class ConsentStateEnum:
    """.NET enum: Autodesk.AutoCAD.Internal.ConsentStateEnum"""
    def __init__(self, *args) -> None: ...
    kUnspecified: int  # = 0
    kGranted: int  # = 1
    kRevoked: int  # = 2
    kRevokePending: int  # = 3
class CoreLayerUtilities:
    """.NET: Autodesk.AutoCAD.Internal.CoreLayerUtilities"""
    def __init__(self, *args) -> None: ...
    RegenPending: int
    @staticmethod
    def LayerNameCompareNatural(str1: str, str2: str) -> int: ...
    @staticmethod
    def RegenLayers(layers: list, regenPending: int, regenRequired: int) -> None: ...

class CoreUtils:
    """.NET: Autodesk.AutoCAD.Internal.CoreUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def AreFilesSame(file1: str, file2: str) -> bool: ...
    @staticmethod
    def GraphScr() -> None: ...
    @staticmethod
    def SetUndoRequiresRegen(db: Database) -> bool: ...
    @staticmethod
    def TextScr() -> None: ...
    @staticmethod
    def WcMatch(str: str, pattern: str) -> bool: ...
    @staticmethod
    def WriteDebugConsole(msg: str) -> None: ...

class CoreXRefUtils:
    """.NET: Autodesk.AutoCAD.Internal.CoreXRefUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def getDelayResolveXRefRelativePaths() -> list: ...
    @staticmethod
    def isMarkedForDelayXRefRelativePathResolve(defId: ObjectId) -> bool: ...
    @staticmethod
    def markForDelayXRefRelativePathResolve(defId: ObjectId) -> None: ...
    @staticmethod
    def unmarkForDelayXRefRelativePathResolve(defId: ObjectId) -> None: ...

class CustomizationUtilities:
    """.NET: Autodesk.AutoCAD.Internal.CustomizationUtilities"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def SetCustomizationInterface(customization: object) -> None: ...

class DMFileData:
    """.NET: Autodesk.AutoCAD.Internal.DMFileData"""
    def __init__(self, *args) -> None: ...
    ...

class DMFileUtil:
    """.NET: Autodesk.AutoCAD.Internal.DMFileUtil"""
    def __init__(self, *args) -> None: ...
    GetDMFileCallback: GetDMFileItemCallback

class DbBlockImageCache:
    """.NET: Autodesk.AutoCAD.Internal.DbBlockImageCache"""
    def __init__(self, *args) -> None: ...
    def OnDatabaseToBeDestroyed(self, sender: object, e: EventArgs) -> None: ...
    def OnDocumentCreated(self, sender: object, e: DocumentCollectionEventArgs) -> None: ...
    def OnObjectErased(self, sender: object, e: ObjectErasedEventArgs) -> None: ...
    def OnObjectModified(self, sender: object, e: ObjectEventArgs) -> None: ...
    def OnObjectUnAppended(self, sender: object, e: ObjectEventArgs) -> None: ...
    def addDbReactors(self, ) -> None: ...
    def addToCache(self, key: BlockImageCacheKey, cache: BlockImageCacheStruct) -> None: ...
    def getCachedBlockBitmap(self, queryKey: BlockImageCacheKey, result: BlockImageCacheStruct) -> bool: ...

class DebugUtil:
    """.NET: Autodesk.AutoCAD.Internal.DebugUtil"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def Assert(condition: bool, message: str, detailMessage: str) -> None: ...
    @staticmethod
    def Verify(b: bool, t: str) -> bool: ...

class DocumentWindowUtil:
    """.NET: Autodesk.AutoCAD.Internal.DocumentWindowUtil"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def CanClose(docWindow: DocumentWindow) -> bool: ...
    @staticmethod
    def SetNextActiveWindow(docWindow: DocumentWindow) -> None: ...

class DxLegacyBinaryTemplate:
    """.NET: Autodesk.AutoCAD.Internal.DxLegacyBinaryTemplate"""
    def __init__(self, *args) -> None: ...
    AttributeList: ArrayList
    BlockList: ArrayList
    def LoadFromFile(self, filename: str) -> None: ...

class ExtensionApplication:
    """.NET: Autodesk.AutoCAD.Internal.ExtensionApplication"""
    def __init__(self, *args) -> None: ...
    def Initialize(self, ) -> None: ...
    def Terminate(self, ) -> None: ...

class ExtensionApplication_App:
    """.NET: Autodesk.AutoCAD.Internal.ExtensionApplication_App"""
    def __init__(self, *args) -> None: ...
    def Initialize(self, ) -> None: ...
    def Terminate(self, ) -> None: ...

class ExternalBlockListResultHost:
    """.NET: Autodesk.AutoCAD.Internal.ExternalBlockListResultHost"""
    def __init__(self, *args) -> None: ...
    def getBlockDataSource(self, ) -> ObservableCollection: ...
    def getBlockListRequestFileInfo(self, ) -> str: ...
    def getBlocksFromExternalFile(self, fullPathName: str) -> ObservableCollection: ...
    def parseJsonBlockList(self, resultJsonStr: str, viewMode: BlockViewMode) -> bool: ...
    def setBlockDataSource(self, dataSource: ObservableCollection) -> None: ...

class FocusChangedEventHandler:
    """.NET: Autodesk.AutoCAD.Internal.FocusChangedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: GroupControl, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: GroupControl) -> None: ...

class GetDMFileItemCallback:
    """.NET: Autodesk.AutoCAD.Internal.GetDMFileItemCallback"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, filePath: str, fileData: DMFileData, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> bool: ...
    def Invoke(self, filePath: str, fileData: DMFileData) -> bool: ...

class GetSharedRecentFilesCallback:
    """.NET: Autodesk.AutoCAD.Internal.GetSharedRecentFilesCallback"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, data: List, nItems: int, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, data: List, nItems: int) -> None: ...

class GetTheAnswerDelegate:
    """.NET: Autodesk.AutoCAD.Internal.GetTheAnswerDelegate"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, pngFilePath: AcString, previewTaskInfo: AcBlockPreviewInfo, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, pngFilePath: AcString, previewTaskInfo: AcBlockPreviewInfo) -> None: ...

class GroupControl(Control):
    """.NET: Autodesk.AutoCAD.Internal.GroupControl"""
    def __init__(self, *args) -> None: ...
    UseDialogTheme: bool
    Title: str
    RestoredHeight: int
    Minimized: bool
    Hidden: bool
    HeaderHeight: int
    AccessibilityObject: AccessibleObject
    AccessibleDefaultActionDescription: str
    AccessibleDescription: str
    AccessibleName: str
    AccessibleRole: AccessibleRole
    AllowDrop: bool
    Anchor: AnchorStyles
    AutoSize: bool
    AutoScrollOffset: Point
    LayoutEngine: LayoutEngine
    DataContext: object
    BackColor: Color
    BackgroundImage: Image
    BackgroundImageLayout: ImageLayout
    BindingContext: BindingContext
    Bottom: int
    Bounds: Rectangle
    CanFocus: bool
    CanSelect: bool
    Capture: bool
    CausesValidation: bool
    ClientRectangle: Rectangle
    ClientSize: Size
    CompanyName: str
    ContainsFocus: bool
    ContextMenuStrip: ContextMenuStrip
    Controls: ControlCollection
    Created: bool
    Cursor: Cursor
    DataBindings: ControlBindingsCollection
    DeviceDpi: int
    DisplayRectangle: Rectangle
    IsDisposed: bool
    Disposing: bool
    Dock: DockStyle
    Enabled: bool
    Focused: bool
    Font: Font
    ForeColor: Color
    Handle: IntPtr
    HasChildren: bool
    Height: int
    IsHandleCreated: bool
    InvokeRequired: bool
    IsAccessible: bool
    IsAncestorSiteInDesignMode: bool
    IsMirrored: bool
    Left: int
    Location: Point
    Margin: Padding
    MaximumSize: Size
    MinimumSize: Size
    Name: str
    Parent: Control
    ProductName: str
    ProductVersion: str
    RecreatingHandle: bool
    Region: Region
    Right: int
    RightToLeft: RightToLeft
    Site: ISite
    Size: Size
    TabIndex: int
    TabStop: bool
    Tag: object
    Text: str
    Top: int
    TopLevelControl: Control
    UseWaitCursor: bool
    Visible: bool
    Width: int
    WindowTarget: IWindowTarget
    PreferredSize: Size
    Padding: Padding
    ContextMenu: ContextMenu
    ImeMode: ImeMode
    Container: IContainer
    def AddStyle(self, styleAdd: GroupControlStyles) -> None: ...
    def AddTitleButton(self, button: GroupControlHeaderButton) -> bool: ...
    def RemoveBitmap(self, button: GroupControlHeaderButton) -> bool: ...
    def RemoveStyle(self, styleRemove: GroupControlStyles) -> None: ...
    def SetActive(self, bActive: bool) -> None: ...
    def SetHeight(self, ) -> None: ...

class GroupControlEventHandler:
    """.NET: Autodesk.AutoCAD.Internal.GroupControlEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: EventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: EventArgs) -> None: ...

class GroupControlEventIndex:
    """.NET enum: Autodesk.AutoCAD.Internal.GroupControlEventIndex"""
    def __init__(self, *args) -> None: ...
    Show: int  # = 0
    Hide: int  # = 1
    ChevronClick: int  # = 2
    TitleButtonClick: int  # = 3
    FocusChange: int  # = 4
    Resize: int  # = 5
class GroupControlHeaderButton:
    """.NET: Autodesk.AutoCAD.Internal.GroupControlHeaderButton"""
    def __init__(self, *args) -> None: ...
    Parent: GroupControl
    Enabled: bool
    ToolTip: str
    Bitmap: Bitmap
    def Dispose(self, ) -> None: ...

class GroupControlStyles:
    """.NET enum: Autodesk.AutoCAD.Internal.GroupControlStyles"""
    def __init__(self, *args) -> None: ...
    ShowChevron: int  # = 1
    ShowButtonForce: int  # = 2
    ShowNonActive: int  # = 4
    ShowNoBorder: int  # = 8
    ShowTransparentButton: int  # = 16
    ShowButtonBorder: int  # = 32
    ShowOpaqueImage: int  # = 128
class GroupResizedEventHandler:
    """.NET: Autodesk.AutoCAD.Internal.GroupResizedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: GroupControl, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: GroupControl) -> None: ...

class GsfUtil:
    """.NET: Autodesk.AutoCAD.Internal.GsfUtil"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GsfLevel() -> int: ...

class HPPrinter:
    """.NET: Autodesk.AutoCAD.Internal.HPPrinter"""
    def __init__(self, *args) -> None: ...
    WSUserId: str
    HPUserId: str
    PrinterName: str
    PrinterId: str

class HPPrinterPlotOption:
    """.NET: Autodesk.AutoCAD.Internal.HPPrinterPlotOption"""
    def __init__(self, *args) -> None: ...
    Quality: HPPrinterPlotQuality
    Copies: int

class HPPrinterPlotQuality:
    """.NET enum: Autodesk.AutoCAD.Internal.HPPrinterPlotQuality"""
    def __init__(self, *args) -> None: ...
    Normal: int  # = 0
    Fast: int  # = 1
    Best: int  # = 2
class HPPrinterPlotResult:
    """.NET: Autodesk.AutoCAD.Internal.HPPrinterPlotResult"""
    def __init__(self, *args) -> None: ...
    Message: str
    Code: str
    Status: int

class HiddenChangedEventHandler:
    """.NET: Autodesk.AutoCAD.Internal.HiddenChangedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: GroupControl, bHidden: bool, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: GroupControl, bHidden: bool) -> None: ...

class HttpMethod:
    """.NET enum: Autodesk.AutoCAD.Internal.HttpMethod"""
    def __init__(self, *args) -> None: ...
    Get: int  # = 0
    Post: int  # = 1
    Head: int  # = 2
    Put: int  # = 3
    Delete: int  # = 4
class ICloudPrintingService:
    """.NET: Autodesk.AutoCAD.Internal.ICloudPrintingService"""
    def __init__(self, *args) -> None: ...
    def ListHPPrinters(self, ) -> list: ...
    def PlotHPPrinter(self, pdfFilePath: str, printer: HPPrinter, option: HPPrinterPlotOption) -> HPPrinterPlotResult: ...
    def ShowHPUserLoginDialog(self, ) -> bool: ...

class ILivePreviewControl:
    """.NET: Autodesk.AutoCAD.Internal.ILivePreviewControl"""
    def __init__(self, *args) -> None: ...
    PreviewDelay: int
    Rule: str
    ControlType: PreviewControlType

class ILivePreviewRule:
    """.NET: Autodesk.AutoCAD.Internal.ILivePreviewRule"""
    def __init__(self, *args) -> None: ...
    IsPreviewAble: bool

class INavisworksFileProtocol:
    """.NET: Autodesk.AutoCAD.Internal.INavisworksFileProtocol"""
    def __init__(self, *args) -> None: ...
    def CloseFile(self, filehandle: IntPtr) -> None: ...
    def GetAggregateInfo(self, filename: str, aggregateJson: str) -> NavisworksFileType: ...
    def GetFileInfo(self, filename: str) -> NavisworksFileInfo: ...
    def OpenFile(self, filename: str) -> IntPtr: ...
    def ReadFile(self, filehandle: IntPtr, offset: int, numbytes: int, bytes: list) -> bool: ...

class INavisworksService:
    """.NET: Autodesk.AutoCAD.Internal.INavisworksService"""
    def __init__(self, *args) -> None: ...
    def RegisterFileProtocol(self, scheme: str, fileprotocol: INavisworksFileProtocol) -> None: ...

class IPECallbackType:
    """.NET enum: Autodesk.AutoCAD.Internal.IPECallbackType"""
    def __init__(self, *args) -> None: ...
    IPECallbackUpdateUI: int  # = 0
    IPECallbackEnableUI: int  # = 1
    IPECallbackCreateUI: int  # = 2
    IPECallbackRemoveUI: int  # = 3
    IPECallbackCreateToolbar: int  # = 4
    IPECallbackRemoveToolbar: int  # = 5
class IPECharFlags:
    """.NET enum: Autodesk.AutoCAD.Internal.IPECharFlags"""
    def __init__(self, *args) -> None: ...
    BoldFlag: int  # = 1
    ItalicFlag: int  # = 2
    UnderlineFlag: int  # = 4
    OverlineFlag: int  # = 8
    FontFlag: int  # = 16
    HeightFlag: int  # = 32
    ColorFlag: int  # = 64
    LanguageFlag: int  # = 128
    ObliqueAngleFlag: int  # = 256
    WidthScaleFlag: int  # = 512
    TrackingFactorFlag: int  # = 1024
    FlowAlignFlag: int  # = 2048
class IPECharFlowType:
    """.NET enum: Autodesk.AutoCAD.Internal.IPECharFlowType"""
    def __init__(self, *args) -> None: ...
    FlowBase: int  # = 0
    FlowCenter: int  # = 1
    FlowTop: int  # = 2
class IPECharStateWrapper(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Internal.IPECharStateWrapper"""
    def __init__(self, *args) -> None: ...
    Color: Color
    FontName: str
    Language: int
    TrackingFactor: float
    WidthScale: float
    ObliqueAngle: float
    Height: float
    TrueType: bool
    Overline: bool
    Underline: bool
    Italic: bool
    Bold: bool
    FlowAlign: IPECharFlowType
    Flags: IPECharFlags
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Clone(self, ) -> object: ...

class IPEColumnCommandType:
    """.NET enum: Autodesk.AutoCAD.Internal.IPEColumnCommandType"""
    def __init__(self, *args) -> None: ...
    IPENoColumnsCommand: int  # = 0
    IPEStaticColumnsCommand: int  # = 1
    IPEDynamicColumnsCommand: int  # = 2
    IPEMoreStaticColumnsCommand: int  # = 3
    IPEInsertColumnBreakCommand: int  # = 4
    IPEColumnSettingsCommand: int  # = 5
class IPECommands:
    """.NET enum: Autodesk.AutoCAD.Internal.IPECommands"""
    def __init__(self, *args) -> None: ...
    IPEUnknownCmd: int  # = 0
    IPESuspendEditorCmd: int  # = 1
    IPEReinstateEditorCmd: int  # = 2
    IPEUndoCmd: int  # = 3
    IPERedoCmd: int  # = 4
    IPEStackCmd: int  # = 5
    IPECloseCmd: int  # = 6
    IPEToggleRulerCmd: int  # = 7
    IPEContextMenuCmd: int  # = 8
    IPESetStyleCmd: int  # = 9
    IPESetFontCmd: int  # = 10
    IPEToggleAnnotativeCmd: int  # = 11
    IPESetTextHeightCmd: int  # = 12
    IPESetColorCmd: int  # = 13
    IPEToggleBoldCmd: int  # = 14
    IPEToggleItalicCmd: int  # = 15
    IPEToggleUnderlineCmd: int  # = 16
    IPEToggleOverlineCmd: int  # = 17
    IPESetObliqueAngleCmd: int  # = 18
    IPESetTrackingFactorCmd: int  # = 19
    IPESetWidthScaleCmd: int  # = 20
    IPEColumnsMenuCmd: int  # = 21
    IPEAttachmentMenuCmd: int  # = 22
    IPELineSpacingMenuCmd: int  # = 23
    IPENumberingMenuCmd: int  # = 24
    IPESymbolMenuCmd: int  # = 25
    IPEParagraphDialogCmd: int  # = 26
    IPEFieldDialogCmd: int  # = 27
    IPESetParagraphAlignmentCmd: int  # = 28
    IPEChangeCaseCmd: int  # = 29
    IPEReplaceContentsCmd: int  # = 30
    IPEInsertMTextCmd: int  # = 31
    IPEToggleDimPrimaryCmd: int  # = 32
    IPEToggleDimAlternateCmd: int  # = 33
    IPEToggleDimUnderlineCmd: int  # = 34
    IPEToggleDimParenthesesCmd: int  # = 35
    IPETweakDimensionCmd: int  # = 36
    IPESetCustomStringCmd: int  # = 37
    IPEInsertCustomStringCmd: int  # = 38
    IPERemoveCustomStringCmd: int  # = 39
    IPEHandleColumnsCmd: int  # = 40
    IPEHandleJustificationCmd: int  # = 41
    IPEHandleLineSpacingCmd: int  # = 42
    IPEHandleSymbolCmd: int  # = 43
    IPEHandleNumberingCmd: int  # = 44
    IPEHandleOptionsCmd: int  # = 45
    IPESetLayerCmd: int  # = 46
class IPEControlIconType:
    """.NET enum: Autodesk.AutoCAD.Internal.IPEControlIconType"""
    def __init__(self, *args) -> None: ...
    IPEBoldButtonIcon: int  # = 0
    IPEItalicButtonIcon: int  # = 1
    IPEOverlineButtonIcon: int  # = 2
    IPEUnderlineButtonIcon: int  # = 3
    IPEObliqueAngleSpinnerIcon: int  # = 4
class IPEDimensionStateWrapper(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Internal.IPEDimensionStateWrapper"""
    def __init__(self, *args) -> None: ...
    Dimension: Dimension
    EnclosedWithParentheses: bool
    EverythingUnderlined: bool
    AlternateFound: bool
    PrimaryFound: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Clone(self, ) -> object: ...

class IPEExitType:
    """.NET enum: Autodesk.AutoCAD.Internal.IPEExitType"""
    def __init__(self, *args) -> None: ...
    ExitQuit: int  # = 0
    ExitSave: int  # = 1
    ExitSaveAndGoRight: int  # = 2
    ExitSaveAndGoLeft: int  # = 3
    ExitSaveAndGoBelow: int  # = 4
    ExitSaveAndGoAbove: int  # = 5
class IPELineSpacingCommandType:
    """.NET enum: Autodesk.AutoCAD.Internal.IPELineSpacingCommandType"""
    def __init__(self, *args) -> None: ...
    IPEMultiLineSpaceCommand: int  # = 0
    IPEMoreLineSpaceCommand: int  # = 1
    IPEClearLineSpaceCommand: int  # = 2
class IPELineSpacingStyle:
    """.NET enum: Autodesk.AutoCAD.Internal.IPELineSpacingStyle"""
    def __init__(self, *args) -> None: ...
    LineSpacingDefault: int  # = 0
    LineSpacingExactly: int  # = 1
    LineSpacingAtLeast: int  # = 2
    LineSpacingMultiple: int  # = 3
    NumLineSpacingStyles: int  # = 4
class IPENumberingCommandType:
    """.NET enum: Autodesk.AutoCAD.Internal.IPENumberingCommandType"""
    def __init__(self, *args) -> None: ...
    IPENumberingOffCommand: int  # = 0
    IPENumberingBulletCommand: int  # = 1
    IPENumberingLetterLowCaseCommand: int  # = 2
    IPENumberingLetterUpperCaseCommand: int  # = 3
    IPENumberingNumberedCommand: int  # = 4
    IPENumberingRestartCommand: int  # = 5
    IPENumberingContinueCommand: int  # = 6
    IPENumberingAutoListCommand: int  # = 7
    IPENumberingTabOnlyDelimiterCommand: int  # = 8
    IPENumberingEnabledCommand: int  # = 9
class IPENumberingType:
    """.NET enum: Autodesk.AutoCAD.Internal.IPENumberingType"""
    def __init__(self, *args) -> None: ...
    NumberingOff: int  # = 0
    NumberingBullet: int  # = 1
    NumberingNumber: int  # = 2
    NumberingLetterLower: int  # = 3
    NumberingLetterUpper: int  # = 4
    NumberingNumTypes: int  # = 5
class IPEOptionsCommandType:
    """.NET enum: Autodesk.AutoCAD.Internal.IPEOptionsCommandType"""
    def __init__(self, *args) -> None: ...
    IPEInsertFieldCommand: int  # = 0
    IPEEditFieldCommand: int  # = 1
    IPEUpdateFieldCommand: int  # = 2
    IPEConvertFieldCommand: int  # = 3
    IPEImportTextCommand: int  # = 4
    IPEConvertCustomCommand: int  # = 5
    IPEStackCommand: int  # = 6
    IPEUnstackCommand: int  # = 7
    IPEStackPropertyCommand: int  # = 8
    IPEOpaqueBackgroundCommand: int  # = 9
    IPEParagraphCommand: int  # = 10
    IPEFindReplaceCommand: int  # = 11
    IPEUpperCaseCommand: int  # = 12
    IPELowerCaseCommand: int  # = 13
    IPEAutoCAPSCommand: int  # = 14
    IPECombineParagraphsCommand: int  # = 15
    IPERemoveCharaterFormattingCommand: int  # = 16
    IPERemoveParagraphFormattingCommand: int  # = 17
    IPERemoveAllFormattingCommand: int  # = 18
    IPEBackgroundMaskCommand: int  # = 19
    IPEWYSIWYGCommand: int  # = 20
    IPEShowToolbarCommand: int  # = 21
    IPEShowOptionsCommand: int  # = 22
    IPEShowRulerCommand: int  # = 23
    IPEShowRibbonCommand: int  # = 24
    IPECheckSpellingCommand: int  # = 25
    IPECheckSpellingSettingsCommand: int  # = 26
    IPEDictionariesCommand: int  # = 27
    IPETextHeightlightColorCommand: int  # = 28
    IPENewFeaturesCommand: int  # = 29
    IPEHelpCommand: int  # = 30
    IPEParagraphAlignCommand: int  # = 31
    IPECharaterSetCommand: int  # = 32
class IPEParagraphAlignmentType:
    """.NET enum: Autodesk.AutoCAD.Internal.IPEParagraphAlignmentType"""
    def __init__(self, *args) -> None: ...
    AlignmentDefault: int  # = 0
    AlignmentLeft: int  # = 1
    AlignmentCenter: int  # = 2
    AlignmentRight: int  # = 3
    AlignmentJustify: int  # = 4
    AlignmentDistribute: int  # = 5
    NumAlignmentTypes: int  # = 6
class IPEParagraphFlags:
    """.NET enum: Autodesk.AutoCAD.Internal.IPEParagraphFlags"""
    def __init__(self, *args) -> None: ...
    FirstIndentFlag: int  # = 1
    LeftIndentFlag: int  # = 2
    RightIndentFlag: int  # = 4
    SpaceBeforeFlag: int  # = 8
    SpaceAfterFlag: int  # = 16
    LineSpacingFlag: int  # = 32
    AlignmentFlag: int  # = 64
    NumberingFlag: int  # = 128
class IPEParagraphStateWrapper(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Internal.IPEParagraphStateWrapper"""
    def __init__(self, *args) -> None: ...
    FirstIndent: float
    LeftIndent: float
    RightIndent: float
    SpaceBefore: float
    SpaceAfter: float
    LineSpacingFactor: float
    TabOnlyDelimitedEnabled: bool
    AutoListEnabled: bool
    NumberingType: IPENumberingType
    Alignment: IPEParagraphAlignmentType
    LineSpacingStyle: IPELineSpacingStyle
    Flags: IPEParagraphFlags
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Clone(self, ) -> object: ...

class IPESettingsWrapper(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Internal.IPESettingsWrapper"""
    def __init__(self, *args) -> None: ...
    DimensionObject: Dimension
    ToolbarRectangle: ValueType
    InputString: str
    TableId: ObjectId
    DimensionScale: float
    VerticalMargin: float
    HorizontalMargin: float
    DefinedHeight: float
    EditFlags: int
    SimpleMText: bool
    RotateForFont: bool
    MultilineAttribute: bool
    AuthoringEntity: bool
    TableCell: bool
    Dimension: bool
    AllowTabs: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Clone(self, ) -> object: ...

class IPEStateWrapper(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Internal.IPEStateWrapper"""
    def __init__(self, *args) -> None: ...
    MLeader: bool
    LayerColor: Color
    LanguageIndex: int
    QuickStartLinkAvailable: bool
    Dimension: bool
    TableCell: bool
    SpellingEnabled: bool
    IsAuthoringEntity: bool
    IsDText: bool
    IsSimpleMText: bool
    HideOptions: bool
    RibbonOn: bool
    HideToolbar: bool
    OpaqueBackground: bool
    ForceOpaqueBackground: bool
    MTextFixed: int
    AutoCapsEnabled: bool
    DefinedWidth: float
    SingleCustom: bool
    EmptySelection: bool
    SingleField: bool
    AutoHeightColumns: bool
    StaticColumnsCount: int
    Justification: AttachmentPoint
    StyleId: ObjectId
    StyleName: str
    DimensionState: IPEDimensionStateWrapper
    ParagraphState: IPEParagraphStateWrapper
    CharState: IPECharStateWrapper
    UndoAvailable: bool
    RedoAvailable: bool
    CopyAvailable: bool
    PasteAvailable: bool
    StackAvailable: bool
    UnstackAvailable: bool
    ChangeCaseAvailable: bool
    AnnotativeAvailable: bool
    ParaAttsAvailable: bool
    NumberingAvailable: bool
    ColumnsAvailable: bool
    RulerAvailable: bool
    FieldsAvailable: bool
    Annotative: bool
    VerticalSHX: bool
    RulerVisible: bool
    IPEColumnType: ColumnType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Clone(self, ) -> object: ...

class IPESymbolCommandType:
    """.NET enum: Autodesk.AutoCAD.Internal.IPESymbolCommandType"""
    def __init__(self, *args) -> None: ...
    IPEStandardSymbolCommand: int  # = 0
    IPECustomSymbolCommand: int  # = 1
class IPETableFlags:
    """.NET enum: Autodesk.AutoCAD.Internal.IPETableFlags"""
    def __init__(self, *args) -> None: ...
    TableSubsequentCellFlag: int  # = 1
    StartInOpaqueBackground: int  # = 2
    TableGoRightFlag: int  # = 4
    TableGoLeftFlag: int  # = 8
    TableGoBelowFlag: int  # = 16
    TableGoAboveFlag: int  # = 32
    TableFlipFlag: int  # = 256
    DisableAutoStackFlag: int  # = 512
    SelectAllFlag: int  # = 1024
    CursorAtEndFlag: int  # = 2048
    kForceNoUIWhenScript: int  # = 4096
class IPETestingEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.Internal.IPETestingEventArgs"""
    def __init__(self, *args) -> None: ...
    Data: object

class IPETestingHandler:
    """.NET: Autodesk.AutoCAD.Internal.IPETestingHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: IPETestingEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: IPETestingEventArgs) -> None: ...

class IPETestingWrapper:
    """.NET: Autodesk.AutoCAD.Internal.IPETestingWrapper"""
    def __init__(self, *args) -> None: ...
    Data: object
    IPETestingManager: IPETestingWrapper
    def FireIPETestingHandler(self, ) -> None: ...

class IPEUpdateUIEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.Internal.IPEUpdateUIEventArgs"""
    def __init__(self, *args) -> None: ...
    ForceUpdate: bool

class IPEWrapper:
    """.NET: Autodesk.AutoCAD.Internal.IPEWrapper"""
    def __init__(self, *args) -> None: ...
    IPEEventManager: IPEWrapper
    def FireUpdateUIEvent(self, forceUpdate: bool) -> None: ...

class IPreviewContext:
    """.NET: Autodesk.AutoCAD.Internal.IPreviewContext"""
    def __init__(self, *args) -> None: ...
    Description: str
    Name: str

class IPreviewContextProvider:
    """.NET: Autodesk.AutoCAD.Internal.IPreviewContextProvider"""
    def __init__(self, *args) -> None: ...
    def GetPreviewControl(self, name: str) -> ILivePreviewControl: ...
    def GetPreviewRule(self, name: str) -> ILivePreviewRule: ...

class ItemTypeEnum:
    """.NET enum: Autodesk.AutoCAD.Internal.ItemTypeEnum"""
    def __init__(self, *args) -> None: ...
    kBlock: int  # = 0
    kDrawingAsBlock: int  # = 1
    kDrawing: int  # = 2
    kFolder: int  # = 3
class LayerUtilities:
    """.NET: Autodesk.AutoCAD.Internal.LayerUtilities"""
    def __init__(self, *args) -> None: ...
    IsMultiDocumentActivationEnabled: bool
    XrefOverrideBackgroundColor: Color
    VpOverrideBackgroundColor: Color
    WillHighlightLayerPropOverrides: bool
    UseCurrentLayerFilter: bool
    ApplyLayerFilterToToolbar: bool
    InvertLayerFilter: bool
    @staticmethod
    def CompareName(string1: str, string2: str) -> int: ...
    @staticmethod
    def FocusMainFrameIfPossible() -> None: ...
    @staticmethod
    def GetCurViewportObjectId() -> ObjectId: ...
    @staticmethod
    def GetRestoreFlags() -> int: ...
    @staticmethod
    def IsPredefined(filter: LayerFilter) -> Predefined: ...
    @staticmethod
    def IsXrefLayerPropertyOverridden(layerId: ValueType, prop: int) -> bool: ...
    @staticmethod
    def LineWeightToPixel(lineWeight: LineWeight) -> int: ...
    @staticmethod
    def SetAllLayersUsed(layerTable: LayerTable) -> None: ...
    @staticmethod
    def SetLayerUsed(layerTableRecord: LayerTableRecord) -> None: ...
    @staticmethod
    def SetNotDefaultCommand(bNotDefaultCommand: bool) -> None: ...
    @staticmethod
    def ShowLayerMergeDialog(layers: list) -> None: ...
    @staticmethod
    def ShowLayerStateManagerDialog() -> None: ...
    @staticmethod
    def ShowLayerStateSaveDialog() -> None: ...
    @staticmethod
    def UnreconciledFilterVisible(database: Database) -> bool: ...
    @staticmethod
    def VPOverridesFilterVisible(database: Database, viewport: ObjectId) -> bool: ...
    @staticmethod
    def XrefOverridesFilterVisible(dbHost: Database) -> bool: ...
    @staticmethod
    def addXRefLayerOverride(layerId: ValueType, prop: int) -> bool: ...
    @staticmethod
    def disableXRefLayerPropertyOverrideRecording() -> None: ...
    @staticmethod
    def enableXRefLayerPropertyOverrideRecording() -> None: ...
    @staticmethod
    def getAllLayersWithXRefOveride(value_: AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >, pDb: AcDbDatabase) -> AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >: ...
    @staticmethod
    def hasAnyXRefLayerOverrides(layerId: ValueType) -> bool: ...
    @staticmethod
    def isXRefLayerPropertyOverrideRecordingEnabled() -> bool: ...
    @staticmethod
    def removeXRefLayerOverride(layerId: ValueType, prop: int) -> bool: ...
    @staticmethod
    def removeXRefLayerOverrides(dbHost: Database) -> bool: ...

class LayoutTabCtrl:
    """.NET: Autodesk.AutoCAD.Internal.LayoutTabCtrl"""
    def __init__(self, *args) -> None: ...
    Invoking: Method
    @staticmethod
    def ActiveLayoutName(database: Database) -> str: ...
    def Dispose(self, ) -> None: ...
    def Dragging(self, dragging: int) -> None: ...
    def ExecuteMenu(self, menu: Menu) -> None: ...
    def Invoke(self, method: Method, ids: IEnumerable, current: int, selected: int) -> None: ...
    def UpdateMenu(self, menu: Dictionary, selected: int) -> None: ...

class LayoutThumbnailEnumerator(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Internal.LayoutThumbnailEnumerator"""
    def __init__(self, *args) -> None: ...
    Count: int
    IsLayoutEmpty: bool
    Index: int
    LayoutName: str
    Thumbnail: Bitmap
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def EnumerateLayoutThumbnails(doc: Document, nFlag: ThumbnailCaptureFlags) -> LayoutThumbnailEnumerator: ...
    def Locate(self, layoutName: str) -> bool: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> bool: ...

class LightUtil:
    """.NET: Autodesk.AutoCAD.Internal.LightUtil"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetBackgroundType(type: DrawableType) -> bool: ...
    @staticmethod
    def GetSkyStatus() -> bool: ...
    @staticmethod
    def RegSceneUI() -> bool: ...
    @staticmethod
    def SetSunAngle(db: Database, sunId: ValueType, dateTime: DateTime) -> None: ...

class LineWeightPicker(ComboBoxWrapper):
    """.NET: Autodesk.AutoCAD.Internal.LineWeightPicker"""
    def __init__(self, *args) -> None: ...
    AccessibilityObject: AccessibleObject
    AccessibleDefaultActionDescription: str
    AccessibleDescription: str
    AccessibleName: str
    AccessibleRole: AccessibleRole
    AllowDrop: bool
    Anchor: AnchorStyles
    AutoSize: bool
    AutoScrollOffset: Point
    LayoutEngine: LayoutEngine
    DataContext: object
    BackColor: Color
    BackgroundImage: Image
    BackgroundImageLayout: ImageLayout
    BindingContext: BindingContext
    Bottom: int
    Bounds: Rectangle
    CanFocus: bool
    CanSelect: bool
    Capture: bool
    CausesValidation: bool
    ClientRectangle: Rectangle
    ClientSize: Size
    CompanyName: str
    ContainsFocus: bool
    ContextMenuStrip: ContextMenuStrip
    Controls: ControlCollection
    Created: bool
    Cursor: Cursor
    DataBindings: ControlBindingsCollection
    DeviceDpi: int
    DisplayRectangle: Rectangle
    IsDisposed: bool
    Disposing: bool
    Dock: DockStyle
    Enabled: bool
    Focused: bool
    Font: Font
    ForeColor: Color
    Handle: IntPtr
    HasChildren: bool
    Height: int
    IsHandleCreated: bool
    InvokeRequired: bool
    IsAccessible: bool
    IsAncestorSiteInDesignMode: bool
    IsMirrored: bool
    Left: int
    Location: Point
    Margin: Padding
    MaximumSize: Size
    MinimumSize: Size
    Name: str
    Parent: Control
    ProductName: str
    ProductVersion: str
    RecreatingHandle: bool
    Region: Region
    Right: int
    RightToLeft: RightToLeft
    Site: ISite
    Size: Size
    TabIndex: int
    TabStop: bool
    Tag: object
    Text: str
    Top: int
    TopLevelControl: Control
    UseWaitCursor: bool
    Visible: bool
    Width: int
    WindowTarget: IWindowTarget
    PreferredSize: Size
    Padding: Padding
    ContextMenu: ContextMenu
    ImeMode: ImeMode
    Container: IContainer

class LivePreviewUtil:
    """.NET: Autodesk.AutoCAD.Internal.LivePreviewUtil"""
    def __init__(self, *args) -> None: ...
    PreviewContextProvider: IPreviewContextProvider
    @staticmethod
    def IsControlLivePreviewAble(element: FrameworkElement) -> bool: ...
    @staticmethod
    def SetPreviewContextProvider(provider: IPreviewContextProvider) -> IPreviewContextProvider: ...

class LocalServerUsage:
    """.NET enum: Autodesk.AutoCAD.Internal.LocalServerUsage"""
    def __init__(self, *args) -> None: ...
    kDisabled: int  # = 0
    kForActivity: int  # = 1
    kForMetaData: int  # = 2
    kForBothActivityAndMetadata: int  # = 3
class MLibDownloadUtils:
    """.NET: Autodesk.AutoCAD.Internal.MLibDownloadUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def BeginToExtract() -> None: ...
    @staticmethod
    def CancelDownloadJob() -> None: ...
    @staticmethod
    def DownloadCurrentSize() -> int: ...
    @staticmethod
    def DownloadServicEndUp() -> None: ...
    @staticmethod
    def DownloadServiceStartUp() -> None: ...
    @staticmethod
    def DownloadTotalSize() -> int: ...
    @staticmethod
    def IsMLibCancelled() -> bool: ...
    @staticmethod
    def IsMLibDownloadComplete() -> bool: ...
    @staticmethod
    def IsMLibDownloading() -> bool: ...
    @staticmethod
    def IsMLibError() -> bool: ...
    @staticmethod
    def IsMLibExtracting() -> bool: ...
    @staticmethod
    def IsMLibReadyToInstall() -> bool: ...
    @staticmethod
    def RegisterTimerCallback(fp: AcDownloadCallback) -> None: ...
    @staticmethod
    def ShowErrorTaskDialog() -> None: ...

class MessageButtonEnum:
    """.NET enum: Autodesk.AutoCAD.Internal.MessageButtonEnum"""
    def __init__(self, *args) -> None: ...
    kOK: int  # = 0
    kOKCancel: int  # = 1
    kYesNoCancel: int  # = 3
    kYesNo: int  # = 4
class MessageIconEnum:
    """.NET enum: Autodesk.AutoCAD.Internal.MessageIconEnum"""
    def __init__(self, *args) -> None: ...
    kNone: int  # = 0
    kError: int  # = 16
    kWarning: int  # = 48
    kInformation: int  # = 64
class MessageResultEnum:
    """.NET enum: Autodesk.AutoCAD.Internal.MessageResultEnum"""
    def __init__(self, *args) -> None: ...
    kNone: int  # = 0
    kOK: int  # = 1
    kCancel: int  # = 2
    kYes: int  # = 6
    kNo: int  # = 7
class MgdAcViewTransitions:
    """.NET: Autodesk.AutoCAD.Internal.MgdAcViewTransitions"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetSettings(enable2d: bool, enable3d: bool, enableDuringScripts: bool, timeMs: int, fps: float) -> None: ...
    @staticmethod
    def SetSettings(enable2d: bool, enable3d: bool, enableDuringScripts: bool, timeMs: int, fps: float) -> None: ...

class MlinesMgdServices:
    """.NET: Autodesk.AutoCAD.Internal.MlinesMgdServices"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def AdjustColorToBackground(mgForeground: Color, mgBackground: Color) -> None: ...
    @staticmethod
    def CloseCachedMLStyle() -> None: ...
    @staticmethod
    def GetDefaultMlnFilename() -> str: ...
    @staticmethod
    def GetDisplayBGColor(mgColor: Color) -> None: ...
    @staticmethod
    def GetLinetypeNameForDisplay(linetypeId: ObjectId) -> str: ...
    @staticmethod
    def IsStyleAlterable(mgName: str) -> bool: ...
    @staticmethod
    def IsValidStyleName(mgName: str) -> bool: ...
    @staticmethod
    def LoadAndUpdateMlnStyle(mlnFile: str, fileOffset: int) -> MLError: ...
    @staticmethod
    def MlnFileReadStyles(filename: str, nameList: ArrayList, positionList: ArrayList) -> MLError: ...
    @staticmethod
    def ProcessMlEditCommand(commandCode: CommandCode) -> None: ...
    @staticmethod
    def ShowOpenMlnFileDialog(currentMlnFile: str) -> str: ...
    @staticmethod
    def ShowSaveDialog(styleId: ObjectId, mlnFilename: str) -> MLError: ...

class MonitoredSysvarValueWrapper(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Internal.MonitoredSysvarValueWrapper"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def clone(self, ) -> MonitoredSysvarValueWrapper: ...
    def isEqualTo(self, sysvar_value: MonitoredSysvarValueWrapper) -> bool: ...
    def setFromString(self, value: str) -> bool: ...
    def toString(self, unit: int, prec: int) -> str: ...
    def type(self, ) -> str: ...

class MonitoredSysvarWrapper(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Internal.MonitoredSysvarWrapper"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def currentValue(self, ) -> MonitoredSysvarValueWrapper: ...
    def isValidValue(self, value: MonitoredSysvarValueWrapper) -> bool: ...
    def name(self, ) -> str: ...
    def perferedValue(self, ) -> MonitoredSysvarValueWrapper: ...
    def resetToPreferedValue(self, ) -> None: ...
    def setPreferedValue(self, value: str) -> int: ...
    def syncCurrentValue(self, ) -> None: ...

class NamedViewUtilities:
    """.NET: Autodesk.AutoCAD.Internal.NamedViewUtilities"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetNamedViewImage(objectId: ObjectId, imageWidth: int, imageHeight: int, backgroundColor: Color) -> IntPtr: ...

class NavigationUtils:
    """.NET: Autodesk.AutoCAD.Internal.NavigationUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetNavStatus() -> int: ...
    @staticmethod
    def IsNavActive() -> bool: ...
    @staticmethod
    def NavPauseRecording() -> None: ...
    @staticmethod
    def NavPlayAnimation() -> None: ...
    @staticmethod
    def NavRecordAnimation() -> None: ...
    @staticmethod
    def NavSaveAnimation() -> None: ...
    @staticmethod
    def NavShowAnimationSetting() -> None: ...

class NavisworksFileInfo:
    """.NET: Autodesk.AutoCAD.Internal.NavisworksFileInfo"""
    def __init__(self, *args) -> None: ...
    ...

class NavisworksFileType:
    """.NET enum: Autodesk.AutoCAD.Internal.NavisworksFileType"""
    def __init__(self, *args) -> None: ...
    Aggregate: int  # = 0
    Model: int  # = 1
    Error: int  # = 2
class NavisworksServiceManager:
    """.NET: Autodesk.AutoCAD.Internal.NavisworksServiceManager"""
    def __init__(self, *args) -> None: ...
    Host: INavisworksService

class NewTabPageUtil:
    """.NET: Autodesk.AutoCAD.Internal.NewTabPageUtil"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def SwitchToStartPage() -> bool: ...

class NonMonitoredSysvarEnumerator(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Internal.NonMonitoredSysvarEnumerator"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Current(self, ) -> MonitoredSysvarWrapper: ...
    def Done(self, ) -> bool: ...
    def MoveNext(self, ) -> None: ...
    def Reset(self, ) -> None: ...

class OPMModeFlags:
    """.NET enum: Autodesk.AutoCAD.Internal.OPMModeFlags"""
    def __init__(self, *args) -> None: ...
    Selection: int  # = 1
    ZeroSelection: int  # = 2
    FromCommand: int  # = 4
    InvokeDialog: int  # = 8
    HatchPattern: int  # = 16
    InvokeHatchDialog: int  # = 24
class OPMStatus:
    """.NET enum: Autodesk.AutoCAD.Internal.OPMStatus"""
    def __init__(self, *args) -> None: ...
    OK: int  # = 0
    InvalidProperty: int  # = 1
    InvalidPropertyValue: int  # = 2
    InvalidPropertyType: int  # = 3
    InvalidPropertyCategory: int  # = 4
    Failed: int  # = 5
class ObjectContexts:
    """.NET: Autodesk.AutoCAD.Internal.ObjectContexts"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def AddContext(obj: DBObject, ctxt: ObjectContext) -> None: ...
    @staticmethod
    def GetContexts(obj: DBObject, collectionName: str) -> List: ...
    @staticmethod
    def HasContext(obj: DBObject, ctxt: ObjectContext) -> bool: ...
    @staticmethod
    def RemoveContext(obj: DBObject, ctxt: ObjectContext) -> None: ...

class OnBoardingStateContextBase:
    """.NET: Autodesk.AutoCAD.Internal.OnBoardingStateContextBase"""
    def __init__(self, *args) -> None: ...
    def Dispose(self, ) -> None: ...
    @staticmethod
    def getBlockSyncFolder() -> str: ...
    @staticmethod
    def getBlockSyncFolderFromServer(timeout: int) -> str: ...
    @staticmethod
    def getConsentStatus(timeout: int) -> int: ...
    @staticmethod
    def getOnBoardingCompleted() -> bool: ...
    def isStateTransitionLocked(self, ) -> bool: ...
    def lockStateTransition(self, ) -> None: ...
    @staticmethod
    def outputMessage(title: str, mgs: str, icon: MessageIconEnum, btn: MessageButtonEnum) -> MessageResultEnum: ...
    @staticmethod
    def setBlockSyncFolder(val: str) -> None: ...
    @staticmethod
    def setConsentStatus(status: int) -> None: ...
    @staticmethod
    def setOnBoardingCompleted() -> None: ...
    def unlockStateTransition(self, ) -> None: ...

class OnBoardingStateContextEnum:
    """.NET enum: Autodesk.AutoCAD.Internal.OnBoardingStateContextEnum"""
    def __init__(self, *args) -> None: ...
    kRecent: int  # = 0
    kFavorites: int  # = 1
class OwnerDrawComboBox(COwnerDrawComboBoxWrapper):
    """.NET: Autodesk.AutoCAD.Internal.OwnerDrawComboBox"""
    def __init__(self, *args) -> None: ...
    VistaTheme: bool
    AutoCompleteMode: AutoCompleteMode
    AutoCompleteSource: AutoCompleteSource
    AutoCompleteCustomSource: AutoCompleteStringCollection
    BackColor: Color
    BackgroundImage: Image
    BackgroundImageLayout: ImageLayout
    DataSource: object
    DrawMode: DrawMode
    DropDownWidth: int
    DropDownHeight: int
    DroppedDown: bool
    FlatStyle: FlatStyle
    Focused: bool
    ForeColor: Color
    IntegralHeight: bool
    ItemHeight: int
    Items: ObjectCollection
    MaxDropDownItems: int
    MaximumSize: Size
    MinimumSize: Size
    MaxLength: int
    Padding: Padding
    PreferredHeight: int
    SelectedIndex: int
    SelectedItem: object
    SelectedText: str
    SelectionLength: int
    SelectionStart: int
    Sorted: bool
    DropDownStyle: ComboBoxStyle
    Text: str
    DisplayMember: str
    FormatInfo: IFormatProvider
    FormatString: str
    FormattingEnabled: bool
    ValueMember: str
    SelectedValue: object
    AccessibilityObject: AccessibleObject
    AccessibleDefaultActionDescription: str
    AccessibleDescription: str
    AccessibleName: str
    AccessibleRole: AccessibleRole
    AllowDrop: bool
    Anchor: AnchorStyles
    AutoSize: bool
    AutoScrollOffset: Point
    LayoutEngine: LayoutEngine
    DataContext: object
    BindingContext: BindingContext
    Bottom: int
    Bounds: Rectangle
    CanFocus: bool
    CanSelect: bool
    Capture: bool
    CausesValidation: bool
    ClientRectangle: Rectangle
    ClientSize: Size
    CompanyName: str
    ContainsFocus: bool
    ContextMenuStrip: ContextMenuStrip
    Controls: ControlCollection
    Created: bool
    Cursor: Cursor
    DataBindings: ControlBindingsCollection
    DeviceDpi: int
    DisplayRectangle: Rectangle
    IsDisposed: bool
    Disposing: bool
    Dock: DockStyle
    Enabled: bool
    Font: Font
    Handle: IntPtr
    HasChildren: bool
    Height: int
    IsHandleCreated: bool
    InvokeRequired: bool
    IsAccessible: bool
    IsAncestorSiteInDesignMode: bool
    IsMirrored: bool
    Left: int
    Location: Point
    Margin: Padding
    Name: str
    Parent: Control
    ProductName: str
    ProductVersion: str
    RecreatingHandle: bool
    Region: Region
    Right: int
    RightToLeft: RightToLeft
    Site: ISite
    Size: Size
    TabIndex: int
    TabStop: bool
    Tag: object
    Top: int
    TopLevelControl: Control
    UseWaitCursor: bool
    Visible: bool
    Width: int
    WindowTarget: IWindowTarget
    PreferredSize: Size
    ContextMenu: ContextMenu
    ImeMode: ImeMode
    Container: IContainer
    def IsInEdit(self, state: DrawItemState) -> bool: ...

class PerfLog:
    """.NET: Autodesk.AutoCAD.Internal.PerfLog"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def IsEventEnabled(eventId: int) -> bool: ...
    @staticmethod
    def WriteEvent(eventId: int, param1: str, param2: str) -> bool: ...

class PreviewControl(ControlWrapper):
    """.NET: Autodesk.AutoCAD.Internal.PreviewControl"""
    def __init__(self, *args) -> None: ...
    AccessibilityObject: AccessibleObject
    AccessibleDefaultActionDescription: str
    AccessibleDescription: str
    AccessibleName: str
    AccessibleRole: AccessibleRole
    AllowDrop: bool
    Anchor: AnchorStyles
    AutoSize: bool
    AutoScrollOffset: Point
    LayoutEngine: LayoutEngine
    DataContext: object
    BackColor: Color
    BackgroundImage: Image
    BackgroundImageLayout: ImageLayout
    BindingContext: BindingContext
    Bottom: int
    Bounds: Rectangle
    CanFocus: bool
    CanSelect: bool
    Capture: bool
    CausesValidation: bool
    ClientRectangle: Rectangle
    ClientSize: Size
    CompanyName: str
    ContainsFocus: bool
    ContextMenuStrip: ContextMenuStrip
    Controls: ControlCollection
    Created: bool
    Cursor: Cursor
    DataBindings: ControlBindingsCollection
    DeviceDpi: int
    DisplayRectangle: Rectangle
    IsDisposed: bool
    Disposing: bool
    Dock: DockStyle
    Enabled: bool
    Focused: bool
    Font: Font
    ForeColor: Color
    Handle: IntPtr
    HasChildren: bool
    Height: int
    IsHandleCreated: bool
    InvokeRequired: bool
    IsAccessible: bool
    IsAncestorSiteInDesignMode: bool
    IsMirrored: bool
    Left: int
    Location: Point
    Margin: Padding
    MaximumSize: Size
    MinimumSize: Size
    Name: str
    Parent: Control
    ProductName: str
    ProductVersion: str
    RecreatingHandle: bool
    Region: Region
    Right: int
    RightToLeft: RightToLeft
    Site: ISite
    Size: Size
    TabIndex: int
    TabStop: bool
    Tag: object
    Text: str
    Top: int
    TopLevelControl: Control
    UseWaitCursor: bool
    Visible: bool
    Width: int
    WindowTarget: IWindowTarget
    PreferredSize: Size
    Padding: Padding
    ContextMenu: ContextMenu
    ImeMode: ImeMode
    Container: IContainer
    def ClearAll(self, ) -> None: ...
    def CreateModel(self, ) -> ErrorStatus: ...
    def ErasePreview(self, ) -> None: ...
    def Init(self, ) -> None: ...
    def RefreshPreview(self, ) -> ErrorStatus: ...
    def ShowEntity(self, fieldWidth: float, fieldHeight: float, entity: Entity, added: bool) -> None: ...

class PreviewControlType:
    """.NET enum: Autodesk.AutoCAD.Internal.PreviewControlType"""
    def __init__(self, *args) -> None: ...
    RibbonItemControl: int  # = 1
    PropertyPaletteControl: int  # = 2
class ProductInfo:
    """.NET: Autodesk.AutoCAD.Internal.ProductInfo"""
    def __init__(self, *args) -> None: ...
    highlightsFile: str
    productRootKey: str
    info: str
    update: ValueType
    version: str
    name: str

class QuickStartLink(ControlWrapper):
    """.NET: Autodesk.AutoCAD.Internal.QuickStartLink"""
    def __init__(self, *args) -> None: ...
    AccessibilityObject: AccessibleObject
    AccessibleDefaultActionDescription: str
    AccessibleDescription: str
    AccessibleName: str
    AccessibleRole: AccessibleRole
    AllowDrop: bool
    Anchor: AnchorStyles
    AutoSize: bool
    AutoScrollOffset: Point
    LayoutEngine: LayoutEngine
    DataContext: object
    BackColor: Color
    BackgroundImage: Image
    BackgroundImageLayout: ImageLayout
    BindingContext: BindingContext
    Bottom: int
    Bounds: Rectangle
    CanFocus: bool
    CanSelect: bool
    Capture: bool
    CausesValidation: bool
    ClientRectangle: Rectangle
    ClientSize: Size
    CompanyName: str
    ContainsFocus: bool
    ContextMenuStrip: ContextMenuStrip
    Controls: ControlCollection
    Created: bool
    Cursor: Cursor
    DataBindings: ControlBindingsCollection
    DeviceDpi: int
    DisplayRectangle: Rectangle
    IsDisposed: bool
    Disposing: bool
    Dock: DockStyle
    Enabled: bool
    Focused: bool
    Font: Font
    ForeColor: Color
    Handle: IntPtr
    HasChildren: bool
    Height: int
    IsHandleCreated: bool
    InvokeRequired: bool
    IsAccessible: bool
    IsAncestorSiteInDesignMode: bool
    IsMirrored: bool
    Left: int
    Location: Point
    Margin: Padding
    MaximumSize: Size
    MinimumSize: Size
    Name: str
    Parent: Control
    ProductName: str
    ProductVersion: str
    RecreatingHandle: bool
    Region: Region
    Right: int
    RightToLeft: RightToLeft
    Site: ISite
    Size: Size
    TabIndex: int
    TabStop: bool
    Tag: object
    Text: str
    Top: int
    TopLevelControl: Control
    UseWaitCursor: bool
    Visible: bool
    Width: int
    WindowTarget: IWindowTarget
    PreferredSize: Size
    Padding: Padding
    ContextMenu: ContextMenu
    ImeMode: ImeMode
    Container: IContainer
    def SetHelpTopic(self, helpTopic: str) -> None: ...

class RecentBlockSerializeState:
    """.NET enum: Autodesk.AutoCAD.Internal.RecentBlockSerializeState"""
    def __init__(self, *args) -> None: ...
    kInMemory: int  # = 0
    kSerializable: int  # = 1
    kSerializing: int  # = 2
    kSerialized: int  # = 3
    kDeleted: int  # = 4
class RecentDocumentAction:
    """.NET: Autodesk.AutoCAD.Internal.RecentDocumentAction"""
    def __init__(self, *args) -> None: ...
    Text: str
    Id: str
    Collection: RecentDocumentActionCollection
    def CanExecute(self, document: str) -> bool: ...
    def Execute(self, document: str) -> bool: ...

class RecentDocumentActionCollection(ReadOnlyCollection):
    """.NET: Autodesk.AutoCAD.Internal.RecentDocumentActionCollection`1"""
    def __init__(self, *args) -> None: ...
    Remove: T
    OpenReadOnly: T
    Open: T
    Item: T
    Count: int
    Item: T

class SMManager:
    """.NET: Autodesk.AutoCAD.Internal.SMManager"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def CIP_LogTargetShot(strShotName: str) -> bool: ...
    @staticmethod
    def DeleteSequenceShot(bSequence: bool, strName: str) -> None: ...
    @staticmethod
    def EndPlay() -> None: ...
    @staticmethod
    def GetPlayStatus(activeShotName: str, activeSeqName: str, playMode: PlayMode, playAction: PlayAction, bPause: bool) -> bool: ...
    @staticmethod
    def GetSequenceIds() -> list: ...
    @staticmethod
    def GetShotIds(strName: str) -> list: ...
    @staticmethod
    def IsShotPlaying() -> bool: ...
    @staticmethod
    def LoopStatusChanged(bLoop: bool) -> None: ...
    @staticmethod
    def MoveSequenceShot(bSequence: bool, strName: str, bLeft: bool) -> None: ...
    @staticmethod
    def PauseOrResumePlayBack(bPause: bool) -> None: ...
    @staticmethod
    def RenameSequenceShot(bSequence: bool, oldName: str, newName: str) -> bool: ...
    @staticmethod
    def UIToBeHidden() -> None: ...
    @staticmethod
    def UIToBeShown() -> None: ...
    @staticmethod
    def UpdateCachedData() -> None: ...
    @staticmethod
    def UpdateThumbnailAll() -> bool: ...
    @staticmethod
    def UpdateThumbnailSequenceShot(bSequence: bool, strName: str) -> bool: ...

class ScaleListHelpers:
    """.NET: Autodesk.AutoCAD.Internal.ScaleListHelpers"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetReferencedScaleNames(db: Database, scaleIds: ObjectIdCollection, scaleStr: List, scaleCount: list) -> None: ...
    @staticmethod
    def GetUnitScaleName(db: Database) -> str: ...
    @staticmethod
    def getDefaultScaleList(returnPredefinedScales: bool, measurement: int, scaleStr: List, scaleNum: List, scaleDenom: List, scaleCount: list) -> str: ...
    @staticmethod
    def loadScaleList(referencedScaleIds: ObjectIdCollection, referencedScaleCount: list, scaleStr: List, scaleNum: List, scaleDenom: List, scaleCount: list) -> None: ...
    @staticmethod
    def loadScaleUnitStrings(unitStrings: list) -> None: ...
    @staticmethod
    def resetScaleList(measurement: int, scaleStr: List, scaleNum: List, scaleDenom: List, scaleCount: list) -> None: ...
    @staticmethod
    def saveScaleList(scaleStr: List, scaleNum: List, scaleDenom: List, scaleCount: int) -> None: ...
    @staticmethod
    def setDefaultScaleList(newScaleStr: List, scaleNum: List, scaleDenom: List, scaleType: List, scaleCount: int) -> None: ...
    @staticmethod
    def updateScaleList(oldScaleStr: List, newScaleStr: List, scaleNum: List, scaleDenom: List, scaleCount: int) -> None: ...

class SearchBox(TextBox):
    """.NET: Autodesk.AutoCAD.Internal.SearchBox"""
    def __init__(self, *args) -> None: ...
    IsEditEmpty: bool
    Notification: str
    DefaultText: str
    AcceptsReturn: bool
    AutoCompleteMode: AutoCompleteMode
    AutoCompleteSource: AutoCompleteSource
    AutoCompleteCustomSource: AutoCompleteStringCollection
    CharacterCasing: CharacterCasing
    Multiline: bool
    PasswordChar: str
    ScrollBars: ScrollBars
    Text: str
    TextAlign: HorizontalAlignment
    UseSystemPasswordChar: bool
    PlaceholderText: str
    AcceptsTab: bool
    ShortcutsEnabled: bool
    AutoSize: bool
    BackColor: Color
    BackgroundImage: Image
    BackgroundImageLayout: ImageLayout
    BorderStyle: BorderStyle
    CanUndo: bool
    ForeColor: Color
    HideSelection: bool
    Lines: list
    MaxLength: int
    Modified: bool
    Padding: Padding
    PreferredHeight: int
    ReadOnly: bool
    SelectedText: str
    SelectionLength: int
    SelectionStart: int
    TextLength: int
    WordWrap: bool
    AccessibilityObject: AccessibleObject
    AccessibleDefaultActionDescription: str
    AccessibleDescription: str
    AccessibleName: str
    AccessibleRole: AccessibleRole
    AllowDrop: bool
    Anchor: AnchorStyles
    AutoScrollOffset: Point
    LayoutEngine: LayoutEngine
    DataContext: object
    BindingContext: BindingContext
    Bottom: int
    Bounds: Rectangle
    CanFocus: bool
    CanSelect: bool
    Capture: bool
    CausesValidation: bool
    ClientRectangle: Rectangle
    ClientSize: Size
    CompanyName: str
    ContainsFocus: bool
    ContextMenuStrip: ContextMenuStrip
    Controls: ControlCollection
    Created: bool
    Cursor: Cursor
    DataBindings: ControlBindingsCollection
    DeviceDpi: int
    DisplayRectangle: Rectangle
    IsDisposed: bool
    Disposing: bool
    Dock: DockStyle
    Enabled: bool
    Focused: bool
    Font: Font
    Handle: IntPtr
    HasChildren: bool
    Height: int
    IsHandleCreated: bool
    InvokeRequired: bool
    IsAccessible: bool
    IsAncestorSiteInDesignMode: bool
    IsMirrored: bool
    Left: int
    Location: Point
    Margin: Padding
    MaximumSize: Size
    MinimumSize: Size
    Name: str
    Parent: Control
    ProductName: str
    ProductVersion: str
    RecreatingHandle: bool
    Region: Region
    Right: int
    RightToLeft: RightToLeft
    Site: ISite
    Size: Size
    TabIndex: int
    TabStop: bool
    Tag: object
    Top: int
    TopLevelControl: Control
    UseWaitCursor: bool
    Visible: bool
    Width: int
    WindowTarget: IWindowTarget
    PreferredSize: Size
    ContextMenu: ContextMenu
    ImeMode: ImeMode
    Container: IContainer
    def ClearEditor(self, ) -> None: ...
    def SetButtonBackgroundColorForThemeChange(self, color: Color, bThemeIsDark: bool) -> None: ...

class SecUtil:
    """.NET: Autodesk.AutoCAD.Internal.SecUtil"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetCertificateSubjectName(filePath: str) -> str: ...
    @staticmethod
    def GetSecureSettingsValue() -> int: ...
    @staticmethod
    def HasCADManagerSubsetCmds() -> bool: ...
    @staticmethod
    def IsCADManagerAllowed(cmd: str) -> bool: ...
    @staticmethod
    def IsDownloadOnlyEnabled() -> bool: ...
    @staticmethod
    def IsInternetConnectionAllowed() -> bool: ...
    @staticmethod
    def IsSignatureValid(filePath: str) -> int: ...

class ServicePackInfo:
    """.NET: Autodesk.AutoCAD.Internal.ServicePackInfo"""
    def __init__(self, *args) -> None: ...
    def getProductInfo(self, ) -> List: ...

class SetReadOnlySysvar:
    """.NET: Autodesk.AutoCAD.Internal.SetReadOnlySysvar"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def SetLayerManagerState(eState: int) -> None: ...

class ShareRecentFileCallback:
    """.NET: Autodesk.AutoCAD.Internal.ShareRecentFileCallback"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, path: str, nAccessTime: int, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, path: str, nAccessTime: int) -> None: ...

class ShareRecentListHandler:
    """.NET: Autodesk.AutoCAD.Internal.ShareRecentListHandler"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def prepareShareData(filePath: str, fileData: AcShareFileData) -> bool: ...

class SharedRecentFileData:
    """.NET: Autodesk.AutoCAD.Internal.SharedRecentFileData"""
    def __init__(self, *args) -> None: ...
    ...

class SharedRecentFiles:
    """.NET: Autodesk.AutoCAD.Internal.SharedRecentFiles"""
    def __init__(self, *args) -> None: ...
    GetRecentFilesCallback: GetSharedRecentFilesCallback
    RecentFileCallback: ShareRecentFileCallback

class SmManagerUtilities:
    """.NET: Autodesk.AutoCAD.Internal.SmManagerUtilities"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def SetSmManagerInterface(mgr: object) -> None: ...

class StartupToolsEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.Internal.StartupToolsEventArgs"""
    def __init__(self, *args) -> None: ...
    def Add(self, toolName: str, commandName: str) -> None: ...

class SubSetting:
    """.NET: Autodesk.AutoCAD.Internal.SubSetting"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def IsCommandEnabled(command: str) -> bool: ...
    @staticmethod
    def IsSysVarEnabled(sysvar: str) -> bool: ...

class SupportProject:
    """.NET: Autodesk.AutoCAD.Internal.SupportProject"""
    def __init__(self, *args) -> None: ...
    LoadedProjectPartialCUIs: List
    def UnloadSharedPartialCUI(self, partialCUI: str) -> None: ...

class SupportProjectManager:
    """.NET: Autodesk.AutoCAD.Internal.SupportProjectManager"""
    def __init__(self, *args) -> None: ...
    ProjectName: str
    LoadedLocalPartialCUIs: List
    @staticmethod
    def GetActiveProject() -> SupportProject: ...
    @staticmethod
    def UnloadLocalPartialCUI(partialCUI: str) -> None: ...

class SyncYourBlockHelper:
    """.NET: Autodesk.AutoCAD.Internal.SyncYourBlockHelper"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def getColorTheme() -> str: ...
    @staticmethod
    def getStateContext(name: OnBoardingStateContextEnum) -> OnBoardingStateContextBase: ...
    @staticmethod
    def setStateContext(name: OnBoardingStateContextEnum, ctx: OnBoardingStateContextBase) -> None: ...
    @staticmethod
    def showConsent() -> bool: ...
    @staticmethod
    def showGuide() -> bool: ...
    @staticmethod
    def showStorageDialog(title: str, defaultStr: str) -> str: ...
    @staticmethod
    def showSyncFolderChooser() -> bool: ...
    @staticmethod
    def showSyncSettingsDialog(title: str) -> bool: ...
    @staticmethod
    def signIn() -> bool: ...
    @staticmethod
    def walkOnBoarding() -> bool: ...

class SysvarMonitorIteratorWrapper(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Internal.SysvarMonitorIteratorWrapper"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def isEqual(self, sysvarMonitorIter: SysvarMonitorIteratorWrapper) -> bool: ...
    def isnotEqual(self, sysvarMonitorIter: SysvarMonitorIteratorWrapper) -> bool: ...
    def next(self, ) -> SysvarMonitorIteratorWrapper: ...
    def sysvar(self, ) -> MonitoredSysvarWrapper: ...

class SysvarMonitorWrapper(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Internal.SysvarMonitorWrapper"""
    def __init__(self, *args) -> None: ...
    BalloonAlertEnabled: bool
    Enabled: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def addMonitoredSysvar(self, sysvar: MonitoredSysvarWrapper) -> MonitoredSysvarWrapper: ...
    def begin(self, ) -> SysvarMonitorIteratorWrapper: ...
    @staticmethod
    def createSysvarMonitorWrapper(p: IntPtr) -> SysvarMonitorWrapper: ...
    def end(self, ) -> SysvarMonitorIteratorWrapper: ...
    def getNonMonitoredSysvarEnumerator(self, ) -> NonMonitoredSysvarEnumerator: ...
    def isDifferenceDetected(self, ) -> bool: ...
    def isSysvarMonitored(self, sysvar_name: str) -> bool: ...
    def removeMonitoredSysvar(self, sysvar: MonitoredSysvarWrapper) -> None: ...
    def resetMonitoredSysvar(self, sysvar: MonitoredSysvarWrapper) -> None: ...

class TableItem:
    """.NET enum: Autodesk.AutoCAD.Internal.TableItem"""
    def __init__(self, *args) -> None: ...
    TableItemInvalid: int  # = 0
    TableItemCell: int  # = 1
    TableItemRow: int  # = 2
    TableItemColumn: int  # = 3
class TableStylePreview(ControlWrapper):
    """.NET: Autodesk.AutoCAD.Internal.TableStylePreview"""
    def __init__(self, *args) -> None: ...
    Table: Table
    Database: Database
    TableStyle: ObjectId
    NumColumns: int
    NumRows: int
    DataText: str
    HeaderText: str
    TitleText: str
    AccessibilityObject: AccessibleObject
    AccessibleDefaultActionDescription: str
    AccessibleDescription: str
    AccessibleName: str
    AccessibleRole: AccessibleRole
    AllowDrop: bool
    Anchor: AnchorStyles
    AutoSize: bool
    AutoScrollOffset: Point
    LayoutEngine: LayoutEngine
    DataContext: object
    BackColor: Color
    BackgroundImage: Image
    BackgroundImageLayout: ImageLayout
    BindingContext: BindingContext
    Bottom: int
    Bounds: Rectangle
    CanFocus: bool
    CanSelect: bool
    Capture: bool
    CausesValidation: bool
    ClientRectangle: Rectangle
    ClientSize: Size
    CompanyName: str
    ContainsFocus: bool
    ContextMenuStrip: ContextMenuStrip
    Controls: ControlCollection
    Created: bool
    Cursor: Cursor
    DataBindings: ControlBindingsCollection
    DeviceDpi: int
    DisplayRectangle: Rectangle
    IsDisposed: bool
    Disposing: bool
    Dock: DockStyle
    Enabled: bool
    Focused: bool
    Font: Font
    ForeColor: Color
    Handle: IntPtr
    HasChildren: bool
    Height: int
    IsHandleCreated: bool
    InvokeRequired: bool
    IsAccessible: bool
    IsAncestorSiteInDesignMode: bool
    IsMirrored: bool
    Left: int
    Location: Point
    Margin: Padding
    MaximumSize: Size
    MinimumSize: Size
    Name: str
    Parent: Control
    ProductName: str
    ProductVersion: str
    RecreatingHandle: bool
    Region: Region
    Right: int
    RightToLeft: RightToLeft
    Site: ISite
    Size: Size
    TabIndex: int
    TabStop: bool
    Tag: object
    Text: str
    Top: int
    TopLevelControl: Control
    UseWaitCursor: bool
    Visible: bool
    Width: int
    WindowTarget: IWindowTarget
    PreferredSize: Size
    Padding: Padding
    ContextMenu: ContextMenu
    ImeMode: ImeMode
    Container: IContainer
    def EnablePreview(self, bEnable: bool) -> bool: ...
    def InitializeTable(self, ) -> bool: ...
    def ShowTablePreview(self, bUpdateTable: bool) -> bool: ...

class TableUtilities:
    """.NET: Autodesk.AutoCAD.Internal.TableUtilities"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def CanDelete(table: Table, selRange: CellRange, row: bool) -> bool: ...
    @staticmethod
    def CanInsert(table: Table, selRange: CellRange, row: bool, rightOrBottom: bool) -> bool: ...
    @staticmethod
    def CanMergeCells(table: Table, selRange: CellRange) -> bool: ...
    @staticmethod
    def CanUnMergeCells(table: Table, selRange: CellRange) -> bool: ...
    @staticmethod
    def GetBackgroundColor(table: Table) -> Color: ...
    @staticmethod
    def GetCellStyle(table: Table, selRange: CellRange, item: TableItem, localized: bool, varies: bool) -> str: ...
    @staticmethod
    def GetCellStyles(tableStyle: TableStyle, count: int, localized: bool, sort: bool) -> list: ...
    @staticmethod
    def GetDataType(table: Table, dateType: DataType, unitType: UnitType) -> None: ...
    @staticmethod
    def GetPickFirstTable(tableId: ObjectId, selRange: CellRange, tableIndex: int) -> bool: ...
    @staticmethod
    def GetReadOnlyState(table: Table, selRange: CellRange, readOnlyContent: bool, readOnlyFormat: bool) -> None: ...
    @staticmethod
    def GetSelectionAlignment(tableId: ValueType, alignment: CellAlignment) -> bool: ...
    @staticmethod
    def GetSelectionLock(table: Table, cellState: CellStates) -> bool: ...
    @staticmethod
    def IsDataLinkCommandAllowed() -> bool: ...
    @staticmethod
    def IsFieldCommandAllowed() -> bool: ...
    @staticmethod
    def IsSingleCell(table: Table, selRange: CellRange) -> bool: ...
    @staticmethod
    def SetBackgroundColor(table: Table, color: Color) -> None: ...

class TaskDescriber:
    """.NET: Autodesk.AutoCAD.Internal.TaskDescriber"""
    def __init__(self, *args) -> None: ...
    UseLocalServer: bool
    ThumbnailSize: int
    ThumbnailState: ThumbnailGenerateState
    DisplayItem: BlockDisplayItem
    def onTaskCompleted(self, imageSource: ImageSource) -> None: ...

class TextIPEUtils:
    """.NET: Autodesk.AutoCAD.Internal.TextIPEUtils"""
    def __init__(self, *args) -> None: ...
    MaxmumWidthScale: float
    MinimumWidthScale: float
    MaxmumTrackingFactor: float
    MinimumTrackingFactor: float
    MaxmumObliqueAngle: float
    MinimumObliqueAngle: float
    @staticmethod
    def ContinueAutoNumbering() -> bool: ...
    @staticmethod
    def Diagonal() -> bool: ...
    @staticmethod
    def GetIPEState() -> IPEStateWrapper: ...
    @staticmethod
    def Horizontal() -> bool: ...
    @staticmethod
    def MgdIPESendCommand(command: IPECommands, param1: object, param2: object) -> bool: ...
    @staticmethod
    def NoUnitsNumberToString(dValue: float) -> str: ...
    @staticmethod
    def NumberToString(dValue: float) -> str: ...
    @staticmethod
    def RedoAutoNumbering() -> bool: ...
    @staticmethod
    def RestartAutoNumbering() -> bool: ...
    @staticmethod
    def StackProperties() -> bool: ...
    @staticmethod
    def StringToNoUnitsNumber(sText: str, dValue: float) -> bool: ...
    @staticmethod
    def StringToNumber(sText: str, dValue: float) -> bool: ...
    @staticmethod
    def UndoAutoNumbering() -> bool: ...
    @staticmethod
    def Unstack() -> bool: ...

class ThemeChangedEventHandler:
    """.NET: Autodesk.AutoCAD.Internal.ThemeChangedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, ) -> None: ...

class ThumbnailGenerateState:
    """.NET enum: Autodesk.AutoCAD.Internal.ThumbnailGenerateState"""
    def __init__(self, *args) -> None: ...
    kRaw: int  # = 0
    kRequired: int  # = 1
    kGenerating: int  # = 2
    kGenerated: int  # = 3
class ThumbnailGenerateTask:
    """.NET: Autodesk.AutoCAD.Internal.ThumbnailGenerateTask"""
    def __init__(self, *args) -> None: ...
    DataHost: BlockDisplayItem
    WaitTime: int
    Executed: bool
    Valid: bool
    TaskDesc: TaskDescriber
    def Dispose(self, ) -> None: ...
    def onTaskDiscarded(self, ) -> None: ...
    def run(self, ) -> None: ...

class ThumbnailGenerateTaskQueue:
    """.NET: Autodesk.AutoCAD.Internal.ThumbnailGenerateTaskQueue"""
    def __init__(self, *args) -> None: ...
    def Dispose(self, ) -> None: ...
    def clear(self, ) -> None: ...
    def discard(self, data: HashSet) -> None: ...
    def isEmpty(self, ) -> bool: ...
    def pop(self, ) -> ThumbnailGenerateTask: ...
    def push(self, A_0: ThumbnailGenerateTask) -> None: ...
    @staticmethod
    def queue() -> ThumbnailGenerateTaskQueue: ...
    def queueData(self, ) -> Queue: ...
    def remove(self, task: ThumbnailGenerateTask) -> None: ...
    def top(self, ) -> ThumbnailGenerateTask: ...

class ThumbnailTaskDescriber(TaskDescriber):
    """.NET: Autodesk.AutoCAD.Internal.ThumbnailTaskDescriber"""
    def __init__(self, *args) -> None: ...
    UseLocalServer: bool
    ThumbnailSize: int
    ThumbnailState: ThumbnailGenerateState
    DisplayItem: BlockDisplayItem
    def onTaskCompleted(self, imageSource: ImageSource) -> None: ...

class TooltipTaskDescriber(TaskDescriber):
    """.NET: Autodesk.AutoCAD.Internal.TooltipTaskDescriber"""
    def __init__(self, *args) -> None: ...
    UseLocalServer: bool
    ThumbnailSize: int
    ThumbnailState: ThumbnailGenerateState
    DisplayItem: BlockDisplayItem
    def onTaskCompleted(self, imageSource: ImageSource) -> None: ...

class TraceSheet:
    """.NET: Autodesk.AutoCAD.Internal.TraceSheet"""
    def __init__(self, *args) -> None: ...
    ModifiedAt: str
    IsActive: bool
    IsPrimary: bool
    IsOn: bool
    AvatarUrl: str
    UserName: str
    LastName: str
    FirstName: str
    UserId: str

class TraceUtils:
    """.NET: Autodesk.AutoCAD.Internal.TraceUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def HighlightSheet(userId: str, highLight: bool) -> None: ...
    @staticmethod
    def ToggleSheetVisibility(userId: str) -> bool: ...
    @staticmethod
    def TraceSheets() -> list: ...
    @staticmethod
    def currentTraceIsCheckout() -> bool: ...
    @staticmethod
    def isAccDwgSheetMarkup() -> bool: ...
    @staticmethod
    def isImportedMarkupPresent() -> bool: ...

class TrueColorPicker(ComboBoxWrapper):
    """.NET: Autodesk.AutoCAD.Internal.TrueColorPicker"""
    def __init__(self, *args) -> None: ...
    CurrentSelectionIndex: int
    AccessibilityObject: AccessibleObject
    AccessibleDefaultActionDescription: str
    AccessibleDescription: str
    AccessibleName: str
    AccessibleRole: AccessibleRole
    AllowDrop: bool
    Anchor: AnchorStyles
    AutoSize: bool
    AutoScrollOffset: Point
    LayoutEngine: LayoutEngine
    DataContext: object
    BackColor: Color
    BackgroundImage: Image
    BackgroundImageLayout: ImageLayout
    BindingContext: BindingContext
    Bottom: int
    Bounds: Rectangle
    CanFocus: bool
    CanSelect: bool
    Capture: bool
    CausesValidation: bool
    ClientRectangle: Rectangle
    ClientSize: Size
    CompanyName: str
    ContainsFocus: bool
    ContextMenuStrip: ContextMenuStrip
    Controls: ControlCollection
    Created: bool
    Cursor: Cursor
    DataBindings: ControlBindingsCollection
    DeviceDpi: int
    DisplayRectangle: Rectangle
    IsDisposed: bool
    Disposing: bool
    Dock: DockStyle
    Enabled: bool
    Focused: bool
    Font: Font
    ForeColor: Color
    Handle: IntPtr
    HasChildren: bool
    Height: int
    IsHandleCreated: bool
    InvokeRequired: bool
    IsAccessible: bool
    IsAncestorSiteInDesignMode: bool
    IsMirrored: bool
    Left: int
    Location: Point
    Margin: Padding
    MaximumSize: Size
    MinimumSize: Size
    Name: str
    Parent: Control
    ProductName: str
    ProductVersion: str
    RecreatingHandle: bool
    Region: Region
    Right: int
    RightToLeft: RightToLeft
    Site: ISite
    Size: Size
    TabIndex: int
    TabStop: bool
    Tag: object
    Text: str
    Top: int
    TopLevelControl: Control
    UseWaitCursor: bool
    Visible: bool
    Width: int
    WindowTarget: IWindowTarget
    PreferredSize: Size
    Padding: Padding
    ContextMenu: ContextMenu
    ImeMode: ImeMode
    Container: IContainer
    def AddOtherItemToList(self, name: str, cargo: int) -> int: ...
    def GetCurrentItemColor(self, ) -> Color: ...
    def SetCurrentByColor(self, mgColor: Color) -> None: ...

class UiCallback:
    """.NET: Autodesk.AutoCAD.Internal.UiCallback"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, ) -> None: ...

class UndoBoundaryEnum:
    """.NET enum: Autodesk.AutoCAD.Internal.UndoBoundaryEnum"""
    def __init__(self, *args) -> None: ...
    SubCommandBoundary: int  # = 4
    CommandBoundaryStart: int  # = 8
    CommandBoundaryEnd: int  # = 16
    SubCommandWall: int  # = 2048
class UnmanagedResource:
    """.NET: Autodesk.AutoCAD.Internal.UnmanagedResource"""
    def __init__(self, *args) -> None: ...
    AcadResourceHandle: IntPtr
    @staticmethod
    def GetResourceHandle(moduleName: str) -> IntPtr: ...
    @staticmethod
    def LoadString(resourceHandle: IntPtr, resourceId: int) -> str: ...

class UpdateTitleBarEventHandler:
    """.NET: Autodesk.AutoCAD.Internal.UpdateTitleBarEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, ) -> None: ...

class UpdateUIEventHandler:
    """.NET: Autodesk.AutoCAD.Internal.UpdateUIEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: IPEUpdateUIEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: IPEUpdateUIEventArgs) -> None: ...

class Utils:
    """.NET: Autodesk.AutoCAD.Internal.Utils"""
    def __init__(self, *args) -> None: ...
    IsTrialUser: bool
    IsDocumentOpening: bool
    IsScriptActive: bool
    CaptureOnLayoutSwitch: bool
    IsCuiCommandEnabled: bool
    SysVarInProgress: str
    IsOsThemed: bool
    ApplicationToolbarsMenu: MenuItem
    ApplicationStatusBarMenu: MenuItem
    IsEditorReady: bool
    ImpliedSelectionIsActive: bool
    @staticmethod
    def ActivateDocument(hWndDoc: IntPtr) -> None: ...
    @staticmethod
    def AddCommand(cmdGroupName: str, cmdGlobalName: str, cmdLocalName: str, cmdFlags: CommandFlags, func: CommandCallback) -> None: ...
    @staticmethod
    def AngleToString(dValue: float) -> str: ...
    @staticmethod
    def ApplyAcValueFormat(objValue: object, formatString: str) -> str: ...
    @staticmethod
    def CUIBeginBatch() -> IDisposable: ...
    @staticmethod
    def CUIBitmapAdd(group: str) -> None: ...
    @staticmethod
    def CUIBitmapGet(group: str, id: str, smallIcon: bool) -> Bitmap: ...
    @staticmethod
    def CUIBitmapRemove(group: str) -> None: ...
    @staticmethod
    def CUIIsUsingSmallIcon() -> bool: ...
    @staticmethod
    def CUISaveMenuAndToolbarState() -> None: ...
    @staticmethod
    def CallButtonEditor(resId: str, packageName: str) -> str: ...
    @staticmethod
    def CallButtonEditorWithBitmap(bitmap: Bitmap, resId: str, packageName: str) -> str: ...
    @staticmethod
    def CancelAndRunCmds(pStrCmd: str) -> bool: ...
    @staticmethod
    def CloseCommandLine() -> None: ...
    @staticmethod
    def ConvertBitmapToAcGiImageBGRA32(bmp: Bitmap) -> ImageBGRA32: ...
    @staticmethod
    def ConvertBitmapToAcGiImageBGRA32Ex(bmp: Bitmap) -> ImageBGRA32: ...
    @staticmethod
    def ConvertCMenuToMenuItem(pMenu: CMenu, menuItem: MenuItem) -> None: ...
    @staticmethod
    def ConvertOSnapCMenuToMenuItem(pMenu: CMenu, menuItem: MenuItem, b3DOsnap: bool) -> None: ...
    @staticmethod
    def CreateCommandToolTip(pTooltipInfo: ValueType) -> object: ...
    @staticmethod
    def CreateNativeTrayItemInstance() -> IntPtr: ...
    @staticmethod
    def DeleteDimConstraints(db: Database, bKeepAnnotativeDimensions: bool) -> bool: ...
    @staticmethod
    def DisableUndoRecording(db: Database, bDisable: bool) -> bool: ...
    @staticmethod
    def DoHelpForCommand(cmdName: str) -> None: ...
    @staticmethod
    def Do_Cmd(menuString: str, IsSSetNeedRestore: bool, bMenuMacro: bool, IsHiddenCmd: bool, bSynchronous: bool) -> None: ...
    @staticmethod
    def DragBackAsMDIChildFrame(handle: IntPtr) -> None: ...
    @staticmethod
    def DragOutDwgFrameWindow(handle: IntPtr) -> None: ...
    @staticmethod
    def DrawLineType(type: ObjectId, width: int, height: int) -> IntPtr: ...
    @staticmethod
    def DrawLineWeight(weight: LineWeight, width: int, height: int) -> IntPtr: ...
    @staticmethod
    def DrawLineWeightLine(lineWeight: LineWeight, left: int, top: int, right: int, bottom: int) -> IntPtr: ...
    @staticmethod
    def DropOpenFile(file: str) -> None: ...
    @staticmethod
    def EnableDWGResize(flag: bool) -> None: ...
    @staticmethod
    def EnableDockControlBars(bEnable: bool) -> None: ...
    @staticmethod
    def EnableFloatingWindows(bEnable: bool) -> None: ...
    @staticmethod
    def EnableSysButtons(bEnable: bool) -> None: ...
    @staticmethod
    def EnsureVisible(rect: Int32Rect, flags: EnsureVisibleFlags) -> bool: ...
    @staticmethod
    def EntFirst() -> ObjectId: ...
    @staticmethod
    def EntLast() -> ObjectId: ...
    @staticmethod
    def EntNext(entId: ObjectId, skipSubEnt: bool) -> ObjectId: ...
    @staticmethod
    def EvaluateTopLevelNetwork(db: Database, bRelaxEvaluate: bool) -> bool: ...
    @staticmethod
    def ExecuteApplicationStatusBarMenu(nId: int) -> None: ...
    @staticmethod
    def FlushGraphics() -> None: ...
    @staticmethod
    def GetAcadFrameHandle() -> IntPtr: ...
    @staticmethod
    def GetActualIndex(index: int) -> int: ...
    @staticmethod
    def GetApplicationFrameHWnd() -> IntPtr: ...
    @staticmethod
    def GetBlockImage(objectId: ObjectId, nImgWidth: int, nImgHeight: int, backgroundColor: Color) -> IntPtr: ...
    @staticmethod
    def GetClientId() -> str: ...
    @staticmethod
    def GetCommandAtLevelForDocument(level: int) -> str: ...
    @staticmethod
    def GetCommandPromptString() -> str: ...
    @staticmethod
    def GetCommandVersion() -> int: ...
    @staticmethod
    def GetCurrentEditBlock() -> ObjectId: ...
    @staticmethod
    def GetCurrentFindingContent() -> str: ...
    @staticmethod
    def GetCurrentObjectColor() -> Color: ...
    @staticmethod
    def GetCurrentViewportVisualStyleId() -> ObjectId: ...
    @staticmethod
    def GetDbmodFromDocument(doc: Document) -> int: ...
    @staticmethod
    def GetDieselEvalString(text: str, bGrayed: bool, bChecked: bool) -> str: ...
    @staticmethod
    def GetDimStyleImage(objectId: ObjectId, nImgWidth: int, nImgHeight: int, backgroundColor: Color) -> IntPtr: ...
    @staticmethod
    def GetDocWinClientRect(docWin: DocumentWindow) -> Rect: ...
    @staticmethod
    def GetDockClientRect() -> Rect: ...
    @staticmethod
    def GetDwgFrameIcon(doc: Document) -> Icon: ...
    @staticmethod
    def GetFontImage(fontID: ObjectId) -> IntPtr: ...
    @staticmethod
    def GetGradientDisplayText(nHatchGradientNameEnum: int) -> str: ...
    @staticmethod
    def GetGradientName(displayText: str) -> str: ...
    @staticmethod
    def GetGradientValue(displayText: str) -> int: ...
    @staticmethod
    def GetHideWarningDialogs(nType: int) -> bool: ...
    @staticmethod
    def GetLastCommandLines(lastLines: int, ignoreNull: bool) -> List: ...
    @staticmethod
    def GetLastInsertBlockData(specifyScaleOnScreen: bool, specifyRotationOnScreen: bool) -> None: ...
    @staticmethod
    def GetLayoutThumbnail(doc: Document, layoutName: str) -> Bitmap: ...
    @staticmethod
    def GetMLeaderStyleImage(objectId: ObjectId, nImgWidth: int, nImgHeight: int, backgroundColor: Color) -> IntPtr: ...
    @staticmethod
    def GetMoreHideWarningDialogs(nType: int) -> bool: ...
    @staticmethod
    def GetOpmWindow() -> IntPtr: ...
    @staticmethod
    def GetPredefinedVisualStyleGlobalName(localName: str) -> str: ...
    @staticmethod
    def GetProductbrandingName() -> str: ...
    @staticmethod
    def GetQpWindow() -> IntPtr: ...
    @staticmethod
    def GetRealHatchPreviewImage(nWidth: int, nHeight: int) -> IntPtr: ...
    @staticmethod
    def GetRedoHistory() -> ObservableCollection: ...
    @staticmethod
    def GetRefEditName() -> str: ...
    @staticmethod
    def GetStatusBarOsnapMenu(b3DOsnap: bool, isDarkTheme: bool) -> MenuItem: ...
    @staticmethod
    def GetTableCellStyleImage(cellStyleName: str, nImgWidth: int, nImgHeight: int, backgroundColor: Color) -> IntPtr: ...
    @staticmethod
    def GetTableStyleImage(objectId: ObjectId, nImgWidth: int, nImgHeight: int, backgroundColor: Color) -> IntPtr: ...
    @staticmethod
    def GetTextExtents(styleId: ObjectId, text: str, dHeight: float) -> Point2d: ...
    @staticmethod
    def GetToolPaletteGroups(schemeName: str, pGroups: StringCollection) -> bool: ...
    @staticmethod
    def GetUndoHistory() -> ObservableCollection: ...
    @staticmethod
    def GetUnitsConversion(fromUnits: UnitsValue, toUnits: UnitsValue) -> float: ...
    @staticmethod
    def GetUnknownPatternSwatchImage(nWidth: int, nHeight: int) -> IntPtr: ...
    @staticmethod
    def GetUserDefinedSwatchImage(bDouble: bool, patternColor: Color, backgroundColor: Color, nWidth: int, nHeight: int) -> IntPtr: ...
    @staticmethod
    def GetVisibleAndInActiveTopFrame() -> DocumentWindow: ...
    @staticmethod
    def GetVisualStyleEdgeColor(visualStyleId: ValueType) -> Color: ...
    @staticmethod
    def GetVisualStyleImage(objectId: ObjectId, size: Size) -> IntPtr: ...
    @staticmethod
    def GetVisualStyleIntersectionEdgeColor(visualStyleId: ValueType) -> Color: ...
    @staticmethod
    def GetVisualStyleObscuredEdgeColor(visualStyleId: ValueType) -> Color: ...
    @staticmethod
    def GetVisualStyles(objectIds: ObjectIdCollection, imageList: List) -> None: ...
    @staticmethod
    def GetWSUID(sWSName: str) -> str: ...
    @staticmethod
    def HistoryStatus() -> bool: ...
    @staticmethod
    def IconFilePath() -> str: ...
    @staticmethod
    def InitDialog(bUseDialog: bool) -> bool: ...
    @staticmethod
    def InitializeCommandLineFont() -> None: ...
    @staticmethod
    def InvokeDataLinkManagerDialog(database: Database, dialogMode: int, parentForm: Form, objectId: ObjectId) -> DialogResult: ...
    @staticmethod
    def InvokeDataTypeDialog(inDataType: DataType, inUnitType: UnitType, sFormatIn: str, objValue: object, dialogOptions: int, parentForm: Form, sTitle: str, sHelp: str, outDataType: DataType, outUnitType: UnitType, sFormatOut: str) -> DialogResult: ...
    @staticmethod
    def InvokeOpmSetPropertyValue(prop: object, val: object, objIds: ObjectIdCollection, guid: Guid, mode: OPMModeFlags) -> OPMStatus: ...
    @staticmethod
    def InvokeOptionsDialog(strPos: str, bInvokedAsChildDlg: bool, defaultLabelIdInFileTab: int, bExpanded: bool) -> None: ...
    @staticmethod
    def InvokeStatusBarItemDeleted(ptr: IntPtr) -> None: ...
    @staticmethod
    def InvokeStatusBarItemMouseDown(ptr: IntPtr, type: int, flag: int, point: Point) -> None: ...
    @staticmethod
    def InvokeTableStyleDialog() -> None: ...
    @staticmethod
    def InvokeTrayItemCloseBubbleWindow(trayItemPtr: IntPtr) -> None: ...
    @staticmethod
    def InvokeTrayItemShowBubbleWindow(title: str, description: str, iconType: BubbleWindowIconType, hyperlink: str, hypertext: str, text: str, trayItemPtr: IntPtr) -> None: ...
    @staticmethod
    def Is3dVisualStyle(styleName: str) -> bool: ...
    @staticmethod
    def IsAllowedToFloatDwgFrames() -> bool: ...
    @staticmethod
    def IsAssociativeArrayRibbonContextApplicable(type: str, dataItem: object) -> bool: ...
    @staticmethod
    def IsCommandActive(name: str) -> bool: ...
    @staticmethod
    def IsCommandDefined(cmdName: str) -> bool: ...
    @staticmethod
    def IsCommandNameInUse(name: str) -> CommandTypeFlags: ...
    @staticmethod
    def IsCommandReEntered(name: str) -> bool: ...
    @staticmethod
    def IsCoreCommand(name: str) -> bool: ...
    @staticmethod
    def IsDiesel(text: str) -> bool: ...
    @staticmethod
    def IsDocumentInBlockEditor(doc: Document) -> bool: ...
    @staticmethod
    def IsDroppableExtension(extension: str) -> bool: ...
    @staticmethod
    def IsFirstRun() -> bool: ...
    @staticmethod
    def IsFlagOn(id: int, bDefault: bool) -> bool: ...
    @staticmethod
    def IsInBlockEditor() -> bool: ...
    @staticmethod
    def IsInCommandStack(flags: CommandFlags) -> bool: ...
    @staticmethod
    def IsInCustomizeMode() -> bool: ...
    @staticmethod
    def IsInDragging() -> bool: ...
    @staticmethod
    def IsInPaperSpace() -> bool: ...
    @staticmethod
    def IsInQuiescentState() -> bool: ...
    @staticmethod
    def IsInStartup() -> bool: ...
    @staticmethod
    def IsInTilemode() -> bool: ...
    @staticmethod
    def IsInputPending() -> bool: ...
    @staticmethod
    def IsLinkedObjectExist(doc: Document) -> bool: ...
    @staticmethod
    def IsLispCommandDefined(name: str) -> bool: ...
    @staticmethod
    def IsMultiRedoAvaliable() -> bool: ...
    @staticmethod
    def IsNewTabCommandAllowed() -> bool: ...
    @staticmethod
    def IsNonDrawingDocumentDisabled() -> bool: ...
    @staticmethod
    def IsOEM() -> bool: ...
    @staticmethod
    def IsOverrideActive() -> bool: ...
    @staticmethod
    def IsPasteClipCommandAllowed() -> bool: ...
    @staticmethod
    def IsPointOverToolbar(x: int, y: int) -> bool: ...
    @staticmethod
    def IsTextEditorActive() -> bool: ...
    @staticmethod
    def IsUndoAvailable() -> bool: ...
    @staticmethod
    def IsVisualStyleDefault(visualStyleId: ValueType) -> bool: ...
    @staticmethod
    def NewDocument() -> None: ...
    @staticmethod
    def NotifyStatusBarServiceReady() -> bool: ...
    @staticmethod
    def NumberToUnitsString(dValue: float) -> str: ...
    @staticmethod
    def OpenDocument() -> None: ...
    @staticmethod
    def Orbit() -> None: ...
    @staticmethod
    def Pan() -> None: ...
    @staticmethod
    def PointOnScreen(pt: Point3d) -> bool: ...
    @staticmethod
    def PostCommandPrompt() -> None: ...
    @staticmethod
    def PostRouteMessageToDwgView(handle: IntPtr, message: int, wParam: IntPtr, lParam: IntPtr) -> bool: ...
    @staticmethod
    def PreRouteMessageToDwgView(handle: IntPtr, message: int, wParam: IntPtr, lParam: IntPtr) -> bool: ...
    @staticmethod
    def RawAngleToString(dValue: float) -> str: ...
    @staticmethod
    def RedrawGrips() -> None: ...
    @staticmethod
    def RegenEntity(entId: ObjectId) -> None: ...
    @staticmethod
    def RegisterCommandLineWindow(window: IntPtr) -> None: ...
    @staticmethod
    def RegisterLeaveStartupUiCallback(func: UiCallback) -> bool: ...
    @staticmethod
    def RegisterLispCommand(cmdName: str, lispName: str) -> None: ...
    @staticmethod
    def RegisterStartupUiCallback(ordering: float, func: UiCallback, delayInMs: int) -> bool: ...
    @staticmethod
    def ReloadMenus(wsCurrentStr: str, bResetWorkspace: bool, bIncrementalReloading: bool) -> None: ...
    @staticmethod
    def RemoveCommand(cmdGroupName: str, cmdGlobalName: str) -> None: ...
    @staticmethod
    def RestoreApplicationStatusBar() -> None: ...
    @staticmethod
    def RunFindText(pStrCmd: str) -> None: ...
    @staticmethod
    def SelectObjects(ids: list) -> bool: ...
    @staticmethod
    def SendMenuStringToExecute(doc: Document, menuString: str, bEchoString: bool) -> None: ...
    @staticmethod
    def SetApplicationStatusBarProgressMeter(str: str, minimum: int, maximum: int) -> None: ...
    @staticmethod
    def SetCurrentViewportVisualStyle(visualStyleId: ObjectId) -> None: ...
    @staticmethod
    def SetCurrentWorkspace(wsCurrent: str, bRestoreUI: bool, bAutoSaveWS: bool) -> bool: ...
    @staticmethod
    def SetCursor(cursor: Cursor) -> None: ...
    @staticmethod
    def SetDbmod(nDbmod: int, db: Database) -> bool: ...
    @staticmethod
    def SetFocusToDwgView() -> None: ...
    @staticmethod
    def SetHelpContext(context: str, metadata: str) -> None: ...
    @staticmethod
    def SetHideWarningDialogs(nType: int, bValue: bool) -> None: ...
    @staticmethod
    def SetMoreHideWarningDialogs(nType: int, bValue: bool) -> None: ...
    @staticmethod
    def SetPropertiesInDatabaseForTPPlayback(itemId: Guid, bSet: bool) -> None: ...
    @staticmethod
    def SetQnewTemplateAfterInitialSetup() -> None: ...
    @staticmethod
    def SetQuickViewWindowHandle(hWnd: IntPtr) -> None: ...
    @staticmethod
    def SetRecoverAllMode(bOn: bool) -> None: ...
    @staticmethod
    def SetRecoverRequestedMode(bOn: bool) -> None: ...
    @staticmethod
    def SetStatusBarContainerHeight(height: int) -> None: ...
    @staticmethod
    def SetStatusBarContent(rootVisual: UIElement) -> bool: ...
    @staticmethod
    def SetUndoMark(begin: bool) -> bool: ...
    @staticmethod
    def ShowHideTextWindow(bShow: bool) -> None: ...
    @staticmethod
    def ShowLineTypeDialog() -> None: ...
    @staticmethod
    def ShowMeshConversionTaskDialog() -> MeshConversionType: ...
    @staticmethod
    def StartToolbarDragDrop(menuGroups: StringCollection, names: StringCollection, tags: StringCollection, commands: StringCollection, helpStrs: StringCollection, smallImages: StringCollection, largeImages: StringCollection, resourceFiles: StringCollection) -> bool: ...
    @staticmethod
    def StrCompareNatural(str1: str, str2: str) -> int: ...
    @staticmethod
    def StringToAngle(sText: str, dValue: float) -> bool: ...
    @staticmethod
    def StringToRawAngle(sText: str, dValue: float) -> bool: ...
    @staticmethod
    def TransferToolbarBitmaps() -> None: ...
    @staticmethod
    def UcsToDisplay(ucsPoint: Point3d, bPaperSpace: bool) -> Point3d: ...
    @staticmethod
    def UnitsStringToNumber(sText: str, dValue: float) -> bool: ...
    @staticmethod
    def UnregisterCommandLineWindow(window: IntPtr) -> None: ...
    @staticmethod
    def UpdateDockingTool(paletteSet: PaletteSet, updateStartupTable: bool, forceUpdateStartupTable: bool) -> bool: ...
    @staticmethod
    def ViewHasChanged() -> bool: ...
    @staticmethod
    def ViewportChange(x: int, y: int) -> None: ...
    @staticmethod
    def ViewportCycle() -> None: ...
    @staticmethod
    def ViewportResize(sx: float, sy: float, ex: float, ey: float, split: bool) -> None: ...
    @staticmethod
    def ViewportTypeChange(id: int) -> None: ...
    @staticmethod
    def VpMaxCommand() -> None: ...
    @staticmethod
    def VpMinCommand() -> None: ...
    @staticmethod
    def WcMatchEx(str: str, pattern: str, ignoreCase: bool) -> bool: ...
    @staticmethod
    def WorkspaceVisible(strWS: str) -> bool: ...
    @staticmethod
    def WriteToCommandLine(message: str) -> None: ...
    @staticmethod
    def WriteUndoBoundary(db: Database, boundary: UndoBoundaryEnum, name: str) -> bool: ...
    @staticmethod
    def Zoom() -> None: ...
    @staticmethod
    def ZoomAuto(type: int, a1: float, a2: float, a3: float, a4: float) -> None: ...
    @staticmethod
    def ZoomObjects(use3d: bool) -> None: ...
    @staticmethod
    def visualStyleId(visualStyleName: str) -> ObjectId: ...
    @staticmethod
    def visualStyleName(id: ObjectId) -> str: ...

class ViewUtil:
    """.NET: Autodesk.AutoCAD.Internal.ViewUtil"""
    def __init__(self, *args) -> None: ...
    GsLensLength: float
    @staticmethod
    def GetCurrentViewportNumber() -> int: ...
    @staticmethod
    def acquireView(nVPNum: int, pView: AcGsView, pGraphicsKernel: AcGsGraphicsKernel) -> None: ...
    @staticmethod
    def releaseView(pView: AcGsView, pGraphicsKernel: AcGsGraphicsKernel) -> None: ...

class VisualStyleSet(RXObject):
    """.NET: Autodesk.AutoCAD.Internal.VisualStyleSet"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Intialize(self, objIds: ObjectIdCollection, pRemoveFromSet: VisualStyleSet, pOverrideColor: Color) -> None: ...
    def RemoveAll(self, ) -> None: ...
    def Replace(self, objIds: ObjectIdCollection, pRemoveFromSet: VisualStyleSet) -> None: ...

class WSUtils:
    """.NET: Autodesk.AutoCAD.Internal.WSUtils"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def CreateHttpClientProxyHandler(uri: str) -> HttpClientHandler: ...
    @staticmethod
    def GetLoginUserName() -> str: ...
    @staticmethod
    def GetO2tk(scopes: str) -> str: ...
    @staticmethod
    def GetProxyAuthentication(url: str, userName: str, password: str, server: str, port: str) -> bool: ...
    @staticmethod
    def GetServer() -> Server: ...
    @staticmethod
    def IsLoggedIn() -> bool: ...
    @staticmethod
    def IsLoginValid() -> bool: ...
    @staticmethod
    def Login() -> bool: ...

class WebServiceMultipartRequest:
    """.NET: Autodesk.AutoCAD.Internal.WebServiceMultipartRequest"""
    def __init__(self, *args) -> None: ...
    Parameters: Dictionary
    Request: HttpWebRequest
    def AddFileContentPart(self, fileStream: Stream, paramName: str, fileName: str, contentType: str) -> None: ...
    def BeginMultipartContent(self, ) -> None: ...
    def EndMultipartContent(self, ) -> None: ...

class WebServicePostRequest:
    """.NET: Autodesk.AutoCAD.Internal.WebServicePostRequest"""
    def __init__(self, *args) -> None: ...
    Parameters: Dictionary
    Request: HttpWebRequest
    def UpdateRequestContent(self, ) -> None: ...

class ZipExtractor:
    """.NET: Autodesk.AutoCAD.Internal.ZipExtractor"""
    def __init__(self, *args) -> None: ...
    Files: IEnumerable
    def Dispose(self, ) -> None: ...
    def Extract(self, file: ZipFileInfo, destination: str) -> None: ...
    def ExtractAll(self, destination: str) -> None: ...

class getBlockSyncFolderFromServerHandler:
    """.NET: Autodesk.AutoCAD.Internal.getBlockSyncFolderFromServerHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, __unnamed000: int, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> str: ...
    def Invoke(self, A_0: int) -> str: ...

class getConsentStatusHandler:
    """.NET: Autodesk.AutoCAD.Internal.getConsentStatusHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, __unnamed000: int, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> int: ...
    def Invoke(self, A_0: int) -> int: ...

class getOnBoardingCompletedHandler:
    """.NET: Autodesk.AutoCAD.Internal.getOnBoardingCompletedHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> bool: ...
    def Invoke(self, ) -> bool: ...

class getValueAsStringHandler:
    """.NET: Autodesk.AutoCAD.Internal.getValueAsStringHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> str: ...
    def Invoke(self, ) -> str: ...

class mgBlockPreviewInfo:
    """.NET: Autodesk.AutoCAD.Internal.mgBlockPreviewInfo"""
    def __init__(self, *args) -> None: ...
    def getBlockPreviewInfoJsonStr(self, ) -> str: ...
    def isOutDated(self, ) -> bool: ...

class outputMessageHandler:
    """.NET: Autodesk.AutoCAD.Internal.outputMessageHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, __unnamed000: str, __unnamed001: str, __unnamed002: MessageIconEnum, __unnamed003: MessageButtonEnum, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> MessageResultEnum: ...
    def Invoke(self, A_0: str, A_1: str, A_2: MessageIconEnum, A_3: MessageButtonEnum) -> MessageResultEnum: ...

class setConsentStatusHandler:
    """.NET: Autodesk.AutoCAD.Internal.setConsentStatusHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, __unnamed000: int, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, A_0: int) -> None: ...

class setOnBoardingCompletedHandler:
    """.NET: Autodesk.AutoCAD.Internal.setOnBoardingCompletedHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, ) -> None: ...

class setValueAsStringHandler:
    """.NET: Autodesk.AutoCAD.Internal.setValueAsStringHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, val: str, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, val: str) -> None: ...
