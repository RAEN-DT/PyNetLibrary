# Auto-generated — Civil 26 — Autodesk.AutoCAD.PlottingServices

class AppPlotStatus:
    """.NET enum: Autodesk.AutoCAD.PlottingServices.AppPlotStatus"""
    def __init__(self, *args) -> None: ...
    PlotStart: int  # = 0
    ViewPlotLog: int  # = 1
    PlotSuccessful: int  # = 2
    PlotHadErrors: int  # = 3
    PlotHadSystemError: int  # = 4
    DwfFilePlotted: int  # = -3
    PlottingMessage: int  # = -2
    NoPlotYet: int  # = -1
class BeginDocumentEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.PlottingServices.BeginDocumentEventArgs"""
    def __init__(self, *args) -> None: ...
    FileName: str
    PlotToFile: bool
    Copies: int
    DocumentName: str
    PlotInfo: PlotInfo

class BeginDocumentEventHandler:
    """.NET: Autodesk.AutoCAD.PlottingServices.BeginDocumentEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: BeginDocumentEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: BeginDocumentEventArgs) -> None: ...

class BeginPageEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.PlottingServices.BeginPageEventArgs"""
    def __init__(self, *args) -> None: ...
    LastPage: bool
    PlotPageInfo: PlotPageInfo
    PlotInfo: PlotInfo

class BeginPageEventHandler:
    """.NET: Autodesk.AutoCAD.PlottingServices.BeginPageEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: BeginPageEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: BeginPageEventArgs) -> None: ...

class BeginPlotEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.PlottingServices.BeginPlotEventArgs"""
    def __init__(self, *args) -> None: ...
    PlotType: PlotType
    PlotProgress: PlotProgress

class BeginPlotEventHandler:
    """.NET: Autodesk.AutoCAD.PlottingServices.BeginPlotEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: BeginPlotEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: BeginPlotEventArgs) -> None: ...

class CustomSizeResults:
    """.NET enum: Autodesk.AutoCAD.PlottingServices.CustomSizeResults"""
    def __init__(self, *args) -> None: ...
    Possible: int  # = 0
    MustCreatePC3: int  # = 1
    RotationRequired: int  # = 2
    PC3DirReadOnly: int  # = 4
    PmpDirReadOnly: int  # = 8
    PmpDirMissing: int  # = 16
    UnknownErrPmpDir: int  # = 32
    PC3FileReadOnly: int  # = 64
    SizeTooBig: int  # = 128
    Exception: int  # = 256
    UnknownErrPC3File: int  # = 512
    UnknownErrPmpFile: int  # = 1024
    PmpFileReadOnly: int  # = 2048
    WidthAndHeightMustBePositive: int  # = 4096
    DeviceLoadFailed: int  # = 8192
class DeviceType:
    """.NET enum: Autodesk.AutoCAD.PlottingServices.DeviceType"""
    def __init__(self, *args) -> None: ...
    SystemPrinter: int  # = 0
    PC3File: int  # = 1
    OneOffConfig: int  # = 2
    Uninitialized: int  # = -1
class DsdData(RXObject):
    """.NET: Autodesk.AutoCAD.PlottingServices.DsdData"""
    def __init__(self, *args) -> None: ...
    InitializeLayouts: bool
    Dwf3dOptions: Dwf3dOptions
    LogFilePath: str
    CategoryName: str
    SelectionSetName: str
    PromptForDwfName: bool
    PlotStampOn: bool
    IsHomogeneous: bool
    IsSheetSet: bool
    NoOfCopies: int
    SheetSetName: str
    MinorVersion: int
    MajorVersion: int
    UnrecognizedDataSections: StringCollection
    UnrecognizedDataSectionNames: StringCollection
    Password: str
    SheetType: SheetType
    DestinationName: str
    ProjectPath: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Copy(self, ) -> DsdData: ...
    def GetDsdEntryCollection(self, ) -> DsdEntryCollection: ...
    def ReadDsd(self, fileName: str) -> None: ...
    def SetDsdEntryCollection(self, entries: DsdEntryCollection) -> None: ...
    def SetUnrecognizedData(self, sectionNames: StringCollection, sectionData: StringCollection) -> None: ...
    def WriteDsd(self, fileName: str) -> None: ...

class DsdEntry(RXObject):
    """.NET: Autodesk.AutoCAD.PlottingServices.DsdEntry"""
    def __init__(self, *args) -> None: ...
    TraceSession: str
    OriginalSheetPath: str
    NpsSourceDwg: str
    Nps: str
    Title: str
    Layout: str
    DwgName: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Copy(self, ) -> DsdEntry: ...

class DsdEntryCollection(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.PlottingServices.DsdEntryCollection"""
    def __init__(self, *args) -> None: ...
    Item: DsdEntry
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, value: DsdEntry) -> int: ...
    def Clear(self, ) -> None: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Insert(self, index: int, value: DsdEntry) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class Dwf3dOptions:
    """.NET: Autodesk.AutoCAD.PlottingServices.Dwf3dOptions"""
    def __init__(self, *args) -> None: ...
    PublishWithMaterials: bool
    GroupByXrefHierarchy: bool

class EndDocumentEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.PlottingServices.EndDocumentEventArgs"""
    def __init__(self, *args) -> None: ...
    Status: PlotCancelStatus

class EndDocumentEventHandler:
    """.NET: Autodesk.AutoCAD.PlottingServices.EndDocumentEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: EndDocumentEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: EndDocumentEventArgs) -> None: ...

class EndPageEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.PlottingServices.EndPageEventArgs"""
    def __init__(self, *args) -> None: ...
    Status: SheetCancelStatus

class EndPageEventHandler:
    """.NET: Autodesk.AutoCAD.PlottingServices.EndPageEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: EndPageEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: EndPageEventArgs) -> None: ...

class EndPlotEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.PlottingServices.EndPlotEventArgs"""
    def __init__(self, *args) -> None: ...
    Status: PlotCancelStatus

class EndPlotEventHandler:
    """.NET: Autodesk.AutoCAD.PlottingServices.EndPlotEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: EndPlotEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: EndPlotEventArgs) -> None: ...

class HostAppServices:
    """.NET: Autodesk.AutoCAD.PlottingServices.HostAppServices"""
    def __init__(self, *args) -> None: ...
    PlotLogger: PlotLogger
    @staticmethod
    def UpdatePlotJobStatus(status: AppPlotStatus, message: str) -> None: ...

class MatchingPolicy:
    """.NET enum: Autodesk.AutoCAD.PlottingServices.MatchingPolicy"""
    def __init__(self, *args) -> None: ...
    MatchDisabled: int  # = 1
    MatchEnabled: int  # = 2
    MatchEnabledCustom: int  # = 3
    MatchEnabledTemporaryCustom: int  # = 4
class MediaBounds:
    """.NET: Autodesk.AutoCAD.PlottingServices.MediaBounds"""
    def __init__(self, *args) -> None: ...
    UpperRightPrintableArea: Point2d
    LowerLeftPrintableArea: Point2d
    PageSize: Point2d
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def IsEqualTo(self, a: MediaBounds, tolerance: Tolerance) -> bool: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class MergeStatus:
    """.NET enum: Autodesk.AutoCAD.PlottingServices.MergeStatus"""
    def __init__(self, *args) -> None: ...
    NoChanges: int  # = 0
    PlotConfigurationName: int  # = 1
    PlotPaperMargins: int  # = 2
    PlotPaperSize: int  # = 4
    CanonicalMediaName: int  # = 8
    PlotOrigin: int  # = 16
    PlotPaperUnits: int  # = 32
    PlotViewportBorders: int  # = 64
    PlotPlotStyles: int  # = 128
    ShowPlotStyles: int  # = 256
    PlotRotation: int  # = 512
    PlotCentered: int  # = 1024
    PlotHidden: int  # = 2048
    ShadePlot: int  # = 4096
    ShadePlotResLevel: int  # = 8192
    ShadePlotCustomDpi: int  # = 16384
    PlotType: int  # = 32768
    PlotWindowArea: int  # = 65536
    PlotViewName: int  # = 131072
    Scale: int  # = 262144
    CurrentStyleSheet: int  # = 524288
    ScaleLineWeights: int  # = 1048576
    PrintLineWeights: int  # = 2097152
    DrawViewportsFirst: int  # = 4194304
    PlotTransparency: int  # = 8388608
class PageCancelledEventHandler:
    """.NET: Autodesk.AutoCAD.PlottingServices.PageCancelledEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: EventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: EventArgs) -> None: ...

class PlotCancelStatus:
    """.NET enum: Autodesk.AutoCAD.PlottingServices.PlotCancelStatus"""
    def __init__(self, *args) -> None: ...
    Continue: int  # = 0
    CanceledByCaller: int  # = 1
    CanceledByCancelAllButton: int  # = 2
class PlotCancelledEventHandler:
    """.NET: Autodesk.AutoCAD.PlottingServices.PlotCancelledEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: EventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: EventArgs) -> None: ...

class PlotConfig(RXObject):
    """.NET: Autodesk.AutoCAD.PlottingServices.PlotConfig"""
    def __init__(self, *args) -> None: ...
    PlotToFileCapability: PlotToFileCapability
    DefaultFileExtension: str
    IsPlotToFile: bool
    CanonicalMediaNames: StringCollection
    MaximumDeviceDotsPerInch: int
    DeviceType: int
    FullPath: str
    DeviceName: str
    TagLine: str
    ServerName: str
    PortName: str
    Comment: str
    LocationName: str
    DriverName: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def GetLocalMediaName(self, canonicalMediaName: str) -> str: ...
    def GetMediaBounds(self, canonicalMediaName: str) -> MediaBounds: ...
    def RefreshMediaNameList(self, ) -> None: ...
    def SaveToPC3(self, name: str) -> None: ...

class PlotConfigInfo(RXObject):
    """.NET: Autodesk.AutoCAD.PlottingServices.PlotConfigInfo"""
    def __init__(self, *args) -> None: ...
    DeviceType: DeviceType
    DeviceName: str
    FullPath: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Clone(self, ) -> object: ...

class PlotConfigInfoCollection(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.PlottingServices.PlotConfigInfoCollection"""
    def __init__(self, *args) -> None: ...
    Item: PlotConfigInfo
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...

class PlotConfigManager:
    """.NET: Autodesk.AutoCAD.PlottingServices.PlotConfigManager"""
    def __init__(self, *args) -> None: ...
    CurrentConfig: PlotConfig
    StdConfigNames: str
    ColorDependentPlotStyles: StringCollection
    NamedPlotStyles: StringCollection
    Devices: PlotConfigInfoCollection
    @staticmethod
    def RefreshList(refreshCode: RefreshCode) -> None: ...
    @staticmethod
    def SetCurrentConfig(deviceName: str) -> PlotConfig: ...

class PlotEngine(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.PlottingServices.PlotEngine"""
    def __init__(self, *args) -> None: ...
    IsBackgroundPackaging: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def BeginDocument(self, plotInfo: PlotInfo, documentName: str, parameters: object, copies: int, plotToFile: bool, fileName: str) -> None: ...
    def BeginGenerateGraphics(self, parameters: object) -> None: ...
    def BeginPage(self, pageInfo: PlotPageInfo, plotInfo: PlotInfo, lastPage: bool, parameters: object) -> None: ...
    def BeginPlot(self, plotProgress: PlotProgress, parameters: object) -> None: ...
    def Destroy(self, ) -> None: ...
    def EndDocument(self, parameters: object) -> None: ...
    def EndGenerateGraphics(self, parameters: object) -> None: ...
    def EndPage(self, parameters: object) -> None: ...
    def EndPlot(self, parameters: object) -> None: ...

class PlotFactory:
    """.NET: Autodesk.AutoCAD.PlottingServices.PlotFactory"""
    def __init__(self, *args) -> None: ...
    ProcessPlotState: ProcessPlotState
    @staticmethod
    def CreatePreviewEngine(previewFlags: int) -> PlotEngine: ...
    @staticmethod
    def CreatePublishEngine() -> PlotEngine: ...

class PlotInfo(RXObject):
    """.NET: Autodesk.AutoCAD.PlottingServices.PlotInfo"""
    def __init__(self, *args) -> None: ...
    MergeStatus: int
    IsValidated: bool
    ValidatedConfig: PlotConfig
    ValidatedSettings: PlotSettings
    DeviceOverride: PlotConfig
    OverrideSettings: PlotSettings
    Layout: ObjectId
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def IsCompatibleDocument(self, info: PlotInfo) -> bool: ...

class PlotInfoValidator(RXObject):
    """.NET: Autodesk.AutoCAD.PlottingServices.PlotInfoValidator"""
    def __init__(self, *args) -> None: ...
    MediaMatchingThreshold: int
    SheetDimensionalWeight: int
    DimensionalWeight: int
    PrintableBoundsWeight: int
    MediaBoundsWeight: int
    SheetMediaGroupWeight: int
    MediaGroupWeight: int
    MediaMatchingPolicy: MatchingPolicy
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def IsCustomPossible(self, info: PlotInfo) -> int: ...
    def Validate(self, info: PlotInfo) -> None: ...

class PlotLogger(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.PlottingServices.PlotLogger"""
    def __init__(self, *args) -> None: ...
    WarningHasHappenedInJob: bool
    ErrorHasHappenedInJob: bool
    WarningHasHappenedInSheet: bool
    ErrorHasHappenedInSheet: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def EndJob(self, ) -> None: ...
    def EndSheet(self, ) -> None: ...
    def LogAbortRetryIgnoreError(self, message: str) -> None: ...
    def LogError(self, message: str) -> None: ...
    def LogInformation(self, message: str) -> None: ...
    def LogMessage(self, message: str) -> None: ...
    def LogSevereError(self, message: str) -> None: ...
    def LogTerminalError(self, message: str) -> None: ...
    def LogWarning(self, message: str) -> None: ...
    def StartJob(self, ) -> None: ...
    def StartSheet(self, ) -> None: ...

class PlotMessageIndex:
    """.NET enum: Autodesk.AutoCAD.PlottingServices.PlotMessageIndex"""
    def __init__(self, *args) -> None: ...
    DialogTitle: int  # = 0
    SheetName: int  # = 1
    SheetNameToolTip: int  # = 2
    Status: int  # = 3
    SheetProgressCaption: int  # = 4
    SheetSetProgressCaption: int  # = 5
    MessageCanceling: int  # = 6
    MessageCancelingCurrent: int  # = 7
    CancelSheetButtonMessage: int  # = 8
    CancelJobButtonMessage: int  # = 9
    MessageCount: int  # = 10
class PlotPageInfo(RXObject):
    """.NET: Autodesk.AutoCAD.PlottingServices.PlotPageInfo"""
    def __init__(self, *args) -> None: ...
    ShadedViewportType: int
    GradientCount: int
    OleObjectCount: int
    RasterCount: int
    EntityCount: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PlotProgress(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.PlottingServices.PlotProgress"""
    def __init__(self, *args) -> None: ...
    StatusMsgString: str
    IsVisible: bool
    SheetProgressPos: int
    UpperSheetProgressRange: int
    LowerSheetProgressRange: int
    SheetCancelStatus: SheetCancelStatus
    IsSheetCancelled: bool
    PlotProgressPos: int
    UpperPlotProgressRange: int
    LowerPlotProgressRange: int
    PlotCancelStatus: PlotCancelStatus
    IsPlotCancelled: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Heartbeat(self, ) -> None: ...

class PlotProgressDialog(PlotProgress):
    """.NET: Autodesk.AutoCAD.PlottingServices.PlotProgressDialog"""
    def __init__(self, *args) -> None: ...
    IsSingleSheetPlot: bool
    PlotMsgString: str
    StatusMsgString: str
    IsVisible: bool
    SheetProgressPos: int
    UpperSheetProgressRange: int
    LowerSheetProgressRange: int
    SheetCancelStatus: SheetCancelStatus
    IsSheetCancelled: bool
    PlotProgressPos: int
    UpperPlotProgressRange: int
    LowerPlotProgressRange: int
    PlotCancelStatus: PlotCancelStatus
    IsPlotCancelled: bool
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Destroy(self, ) -> None: ...
    def OnBeginPlot(self, ) -> None: ...
    def OnBeginSheet(self, ) -> None: ...
    def OnEndPlot(self, ) -> None: ...
    def OnEndSheet(self, ) -> None: ...

class PlotReactorManager:
    """.NET: Autodesk.AutoCAD.PlottingServices.PlotReactorManager"""
    def __init__(self, *args) -> None: ...
    ...

class PlotToFileCapability:
    """.NET enum: Autodesk.AutoCAD.PlottingServices.PlotToFileCapability"""
    def __init__(self, *args) -> None: ...
    NoPlotToFile: int  # = 0
    PlotToFileAllowed: int  # = 1
    MustPlotToFile: int  # = 2
class PlotType:
    """.NET enum: Autodesk.AutoCAD.PlottingServices.PlotType"""
    def __init__(self, *args) -> None: ...
    Plot: int  # = 0
    Preview: int  # = 1
    BackgroundPackaging: int  # = 2
    BackgroundPlot: int  # = 3
class PreviewEndPlotInfo(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.PlottingServices.PreviewEndPlotInfo"""
    def __init__(self, *args) -> None: ...
    Status: PreviewEndPlotStatus
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class PreviewEndPlotStatus:
    """.NET enum: Autodesk.AutoCAD.PlottingServices.PreviewEndPlotStatus"""
    def __init__(self, *args) -> None: ...
    Normal: int  # = 0
    Plot: int  # = 1
    Cancel: int  # = 2
    Next: int  # = 3
    Previous: int  # = 4
class PreviewEngineFlags:
    """.NET enum: Autodesk.AutoCAD.PlottingServices.PreviewEngineFlags"""
    def __init__(self, *args) -> None: ...
    Plot: int  # = 1
    NextSheet: int  # = 2
    PreviousSheet: int  # = 4
class ProcessPlotState:
    """.NET enum: Autodesk.AutoCAD.PlottingServices.ProcessPlotState"""
    def __init__(self, *args) -> None: ...
    NotPlotting: int  # = 0
    ForegroundPlotting: int  # = 1
    BackgroundPlotting: int  # = 2
class RefreshCode:
    """.NET enum: Autodesk.AutoCAD.PlottingServices.RefreshCode"""
    def __init__(self, *args) -> None: ...
    All: int  # = 0
    RefreshDevicesList: int  # = 1
    RefreshStyleList: int  # = 2
    RefreshSystemDevicesList: int  # = 3
    RefreshPC3DevicesList: int  # = 4
class SheetCancelStatus:
    """.NET enum: Autodesk.AutoCAD.PlottingServices.SheetCancelStatus"""
    def __init__(self, *args) -> None: ...
    Continue: int  # = 0
    CanceledByCancelButton: int  # = 1
    CanceledByCancelAllButton: int  # = 2
    CanceledByCaller: int  # = 3
class SheetType:
    """.NET enum: Autodesk.AutoCAD.PlottingServices.SheetType"""
    def __init__(self, *args) -> None: ...
    SingleDwf: int  # = 0
    MultiDwf: int  # = 1
    OriginalDevice: int  # = 2
    SingleDwfx: int  # = 3
    MultiDwfx: int  # = 4
    SinglePdf: int  # = 5
    MultiPdf: int  # = 6
class StdConfiguration:
    """.NET enum: Autodesk.AutoCAD.PlottingServices.StdConfiguration"""
    def __init__(self, *args) -> None: ...
    NoneDevice: int  # = 0
    DefaultWindowsSysPrinter: int  # = 1
    Dwf6ePlot: int  # = 2
    DwfEplotOptForPlotting: int  # = 3
    DwfEplotOptForViewing: int  # = 4
    PublishToWebDwf: int  # = 5
    PublishToWebJpg: int  # = 6
    PublishToWebPng: int  # = 7
    DWFxePlot: int  # = 8
    PublishToWebDWFx: int  # = 9
