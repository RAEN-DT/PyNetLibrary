# Auto-generated — Civil 26 — Autodesk.AutoCAD.EditorInput

class AddedKeywords:
    """.NET enum: Autodesk.AutoCAD.EditorInput.AddedKeywords"""
    def __init__(self, *args) -> None: ...
    LastAllPrevious: int  # = 1
    PickImplied: int  # = 2
    All: int  # = 4
    WindowCrossingBoxWPolygonCPolygon: int  # = 8
    Multiple: int  # = 16
    CrossingCPolygon: int  # = 32
    Fence: int  # = 64
    Last: int  # = 128
    Previous: int  # = 256
    WindowWPolygon: int  # = 512
    Group: int  # = 1024
class Camera(Entity):
    """.NET: Autodesk.AutoCAD.EditorInput.Camera"""
    def __init__(self, *args) -> None: ...
    FrontClipEnabled: bool
    BackClipEnabled: bool
    BackClipDistance: float
    FrontClipDistance: float
    IsCameraPlottable: bool
    ViewTwist: float
    FieldOfView: float
    LensLength: float
    Target: Point3d
    Position: Point3d
    ViewId: ObjectId
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

class ConstraintUtilities:
    """.NET: Autodesk.AutoCAD.EditorInput.ConstraintUtilities"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def ShowConstraintBar(subentityPaths: list, bToShow: bool) -> bool: ...

class CrossingOrWindowSelectedObject(SelectedObject):
    """.NET: Autodesk.AutoCAD.EditorInput.CrossingOrWindowSelectedObject"""
    def __init__(self, *args) -> None: ...
    OptionalDetails: SelectionDetails
    GraphicsSystemMarkerPtr: IntPtr
    GraphicsSystemMarker: int
    SelectionMethod: SelectionMethod
    ObjectId: ObjectId
    def GetPickPoints(self, ) -> list: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class CrossingOrWindowSelectedSubObject(SelectedSubObject):
    """.NET: Autodesk.AutoCAD.EditorInput.CrossingOrWindowSelectedSubObject"""
    def __init__(self, *args) -> None: ...
    GraphicsSystemMarkerPtr: IntPtr
    GraphicsSystemMarker: int
    OptionalDetails: SelectionDetails
    SelectionMethod: SelectionMethod
    FullSubentityPath: FullSubentityPath
    def GetPickPoints(self, ) -> list: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class CursorBadgeUtilities:
    """.NET: Autodesk.AutoCAD.EditorInput.CursorBadgeUtilities"""
    def __init__(self, *args) -> None: ...
    def AddSupplementalCursorImage(self, cursorImage: ImageBGRA32, priority: int) -> bool: ...
    def GetSupplementalCursorOffset(self, x: int, y: int) -> None: ...
    def HasSupplementalCursorImage(self, ) -> bool: ...
    def RemoveSupplementalCursorImage(self, cursorImage: ImageBGRA32) -> bool: ...
    def SetSupplementalCursorOffset(self, x: int, y: int) -> None: ...

class CursorType:
    """.NET enum: Autodesk.AutoCAD.EditorInput.CursorType"""
    def __init__(self, *args) -> None: ...
    Crosshair: int  # = 0
    RectangularCursor: int  # = 1
    RubberBand: int  # = 2
    NotRotated: int  # = 3
    TargetBox: int  # = 4
    RotatedCrosshair: int  # = 5
    CrosshairNoRotate: int  # = 6
    Invisible: int  # = 7
    EntitySelect: int  # = 8
    Parallelogram: int  # = 9
    EntitySelectNoPerspective: int  # = 10
    PickfirstOrGrips: int  # = 11
    NoSpecialCursor: int  # = -1
class DeviceInputEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.DeviceInputEventArgs"""
    def __init__(self, *args) -> None: ...
    Handled: bool
    LParam: IntPtr
    WParam: IntPtr
    Message: int
    GraphicsSystemMarker: IntPtr

class DeviceInputEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.DeviceInputEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: DeviceInputEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: DeviceInputEventArgs) -> None: ...

class DisposableSelectionSet:
    """.NET: Autodesk.AutoCAD.EditorInput.DisposableSelectionSet"""
    def __init__(self, *args) -> None: ...
    def Dispose(self, ) -> None: ...

class DragCallback:
    """.NET: Autodesk.AutoCAD.EditorInput.DragCallback"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, current: Point3d, xform: Matrix3d, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> SamplerStatus: ...
    def Invoke(self, current: Point3d, xform: Matrix3d) -> SamplerStatus: ...

class DragCursor:
    """.NET enum: Autodesk.AutoCAD.EditorInput.DragCursor"""
    def __init__(self, *args) -> None: ...
    Normal: int  # = 0
    None_: int  # = 1
    Selection: int  # = 2
class DraggingEndedEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.DraggingEndedEventArgs"""
    def __init__(self, *args) -> None: ...
    Offset: Vector3d
    PickPoint: Point3d
    Status: PromptStatus

class DraggingEndedEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.DraggingEndedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: DraggingEndedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: DraggingEndedEventArgs) -> None: ...

class DraggingEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.DraggingEventArgs"""
    def __init__(self, *args) -> None: ...
    Prompt: str

class DraggingEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.DraggingEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: DraggingEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: DraggingEventArgs) -> None: ...

class DrawJig(Jig):
    """.NET: Autodesk.AutoCAD.EditorInput.DrawJig"""
    def __init__(self, *args) -> None: ...
    ...

class Editor(MarshalByRefObject):
    """.NET: Autodesk.AutoCAD.EditorInput.Editor"""
    def __init__(self, *args) -> None: ...
    MouseHasMoved: bool
    CurrentUserCoordinateSystem: Matrix3d
    UseCommandLineInterface: bool
    IsDragging: bool
    IsQuiescentForTransparentCommand: bool
    IsQuiescent: bool
    CurrentViewportObjectId: ObjectId
    ActiveViewportId: ObjectId
    Document: Document
    def ApplyCurDwgLayerTableChanges(self, ) -> None: ...
    def Command(self, parameter: list) -> None: ...
    def CommandAsync(self, parameter: list) -> CommandResult: ...
    def DoPrompt(self, opt: PromptOptions) -> PromptResult: ...
    def Drag(self, selection: SelectionSet, message: str, callback: DragCallback) -> PromptPointResult: ...
    def DrawVector(self, from_: Point3d, to: Point3d, color: int, drawHighlighted: bool) -> None: ...
    def DrawVectors(self, rb: ResultBuffer, transform: Matrix3d) -> None: ...
    def GetAngle(self, options: PromptAngleOptions) -> PromptDoubleResult: ...
    def GetCommandVersion(self, ) -> int: ...
    def GetCorner(self, message: str, basePoint: Point3d) -> PromptPointResult: ...
    def GetCurrentView(self, ) -> ViewTableRecord: ...
    def GetDistance(self, options: PromptDistanceOptions) -> PromptDoubleResult: ...
    def GetDouble(self, options: PromptDoubleOptions) -> PromptDoubleResult: ...
    def GetEntity(self, options: PromptEntityOptions) -> PromptEntityResult: ...
    def GetFileNameForOpen(self, options: PromptOpenFileOptions) -> PromptFileNameResult: ...
    def GetFileNameForSave(self, options: PromptSaveFileOptions) -> PromptFileNameResult: ...
    def GetInteger(self, options: PromptIntegerOptions) -> PromptIntegerResult: ...
    def GetKeywords(self, message: str, globalKeywords: list) -> PromptResult: ...
    def GetNestedEntity(self, options: PromptNestedEntityOptions) -> PromptNestedEntityResult: ...
    def GetPoint(self, options: PromptPointOptions) -> PromptPointResult: ...
    def GetSelection(self, options: PromptSelectionOptions, filter: SelectionFilter) -> PromptSelectionResult: ...
    def GetString(self, options: PromptStringOptions) -> PromptResult: ...
    def GetViewportNumber(self, point: Point) -> int: ...
    def InitCommandVersion(self, nVersion: int) -> int: ...
    def PointToScreen(self, pt: Point3d, viewportNumber: int) -> Point: ...
    def PointToWorld(self, pt: Point, viewportNumber: int) -> Point3d: ...
    def PostCommandPrompt(self, ) -> None: ...
    def Regen(self, ) -> None: ...
    def SelectAll(self, filter: SelectionFilter) -> PromptSelectionResult: ...
    def SelectCrossingPolygon(self, polygon: Point3dCollection, filter: SelectionFilter) -> PromptSelectionResult: ...
    def SelectCrossingWindow(self, pt1: Point3d, pt2: Point3d, filter: SelectionFilter, forceSubEntitySelection: bool) -> PromptSelectionResult: ...
    def SelectFence(self, fence: Point3dCollection, filter: SelectionFilter) -> PromptSelectionResult: ...
    def SelectImplied(self, ) -> PromptSelectionResult: ...
    def SelectLast(self, ) -> PromptSelectionResult: ...
    def SelectPrevious(self, ) -> PromptSelectionResult: ...
    def SelectWindow(self, pt1: Point3d, pt2: Point3d, filter: SelectionFilter) -> PromptSelectionResult: ...
    def SelectWindowPolygon(self, polygon: Point3dCollection, filter: SelectionFilter) -> PromptSelectionResult: ...
    def SetCurrentView(self, value: ViewTableRecord) -> None: ...
    def SetImpliedSelection(self, selectionSet: SelectionSet) -> None: ...
    def Snap(self, snapMode: str, input: Point3d) -> Point3d: ...
    def StartUserInteraction(self, hwnd: IntPtr) -> EditorUserInteraction: ...
    def SwitchToModelSpace(self, ) -> None: ...
    def SwitchToPaperSpace(self, ) -> None: ...
    def TraceBoundary(self, seedPoint: Point3d, detectIslands: bool) -> DBObjectCollection: ...
    def TurnForcedPickOff(self, ) -> int: ...
    def TurnForcedPickOn(self, ) -> int: ...
    def TurnSubentityWindowSelectionOff(self, ) -> None: ...
    def TurnSubentityWindowSelectionOn(self, ) -> None: ...
    def UpdateScreen(self, ) -> None: ...
    def UpdateTiledViewportsFromDatabase(self, ) -> None: ...
    def UpdateTiledViewportsInDatabase(self, ) -> None: ...
    def ViewportIdFromNumber(self, viewportNumber: int) -> ObjectId: ...
    def WriteMessage(self, message: str, parameter: list) -> None: ...

class EditorExtension:
    """.NET: Autodesk.AutoCAD.EditorInput.EditorExtension"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def GetViewportNumber(editor: Editor, point: Point) -> int: ...
    @staticmethod
    def PointToScreen(editor: Editor, pt: Point3d, viewportNumber: int) -> Point: ...
    @staticmethod
    def PointToWorld(editor: Editor, pt: Point, viewportNumber: int) -> Point3d: ...
    @staticmethod
    def StartUserInteraction(editor: Editor, modalForm: Control) -> EditorUserInteraction: ...

class EditorUserInteraction:
    """.NET: Autodesk.AutoCAD.EditorInput.EditorUserInteraction"""
    def __init__(self, *args) -> None: ...
    def Dispose(self, ) -> None: ...
    def End(self, ) -> None: ...

class EditorVisualStyle:
    """.NET: Autodesk.AutoCAD.EditorInput.EditorVisualStyle"""
    def __init__(self, *args) -> None: ...
    IsVS3dType: bool
    IsVS2dType: bool
    @staticmethod
    def setCvpVS2d() -> None: ...

class EntityJig(Jig):
    """.NET: Autodesk.AutoCAD.EditorInput.EntityJig"""
    def __init__(self, *args) -> None: ...
    ...

class FenceSelectedObject(SelectedObject):
    """.NET: Autodesk.AutoCAD.EditorInput.FenceSelectedObject"""
    def __init__(self, *args) -> None: ...
    OptionalDetails: SelectionDetails
    GraphicsSystemMarkerPtr: IntPtr
    GraphicsSystemMarker: int
    SelectionMethod: SelectionMethod
    ObjectId: ObjectId
    def GetIntersectionPoints(self, ) -> list: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class FenceSelectedSubObject(SelectedSubObject):
    """.NET: Autodesk.AutoCAD.EditorInput.FenceSelectedSubObject"""
    def __init__(self, *args) -> None: ...
    GraphicsSystemMarkerPtr: IntPtr
    GraphicsSystemMarker: int
    OptionalDetails: SelectionDetails
    SelectionMethod: SelectionMethod
    FullSubentityPath: FullSubentityPath
    def GetIntersectionPoints(self, ) -> list: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class InputPointContext:
    """.NET: Autodesk.AutoCAD.EditorInput.InputPointContext"""
    def __init__(self, *args) -> None: ...
    ToolTipText: str
    ComputedPoint: Point3d
    ObjectSnapOverrides: ObjectSnapMasks
    ObjectSnapMask: ObjectSnapMasks
    ObjectSnappedPoint: Point3d
    CartesianSnappedPoint: Point3d
    GrippedPoint: Point3d
    RawPoint: Point3d
    LastPoint: Point3d
    History: PointHistoryBits
    PointComputed: bool
    DrawContext: ViewportDraw
    Document: Document
    def Dispose(self, ) -> None: ...
    def GetAlignmentPaths(self, ) -> list: ...
    def GetCustomObjectSnapModes(self, ) -> list: ...
    def GetCustomObjectSnapOverrides(self, ) -> list: ...
    def GetKeyPointEntities(self, ) -> list: ...
    def GetPickedEntities(self, ) -> list: ...

class Jig:
    """.NET: Autodesk.AutoCAD.EditorInput.Jig"""
    def __init__(self, *args) -> None: ...
    ...

class JigPromptAngleOptions(JigPromptGeometryOptions):
    """.NET: Autodesk.AutoCAD.EditorInput.JigPromptAngleOptions"""
    def __init__(self, *args) -> None: ...
    DefaultValue: float
    UseBasePoint: bool
    BasePoint: Point3d
    UserInputControls: UserInputControls
    Cursor: CursorType
    Keywords: KeywordCollection
    AppendKeywordsToMessage: bool
    Message: str
    IsReadOnly: bool

class JigPromptDistanceOptions(JigPromptGeometryOptions):
    """.NET: Autodesk.AutoCAD.EditorInput.JigPromptDistanceOptions"""
    def __init__(self, *args) -> None: ...
    DefaultValue: float
    UseBasePoint: bool
    BasePoint: Point3d
    UserInputControls: UserInputControls
    Cursor: CursorType
    Keywords: KeywordCollection
    AppendKeywordsToMessage: bool
    Message: str
    IsReadOnly: bool

class JigPromptGeometryOptions(JigPromptOptions):
    """.NET: Autodesk.AutoCAD.EditorInput.JigPromptGeometryOptions"""
    def __init__(self, *args) -> None: ...
    UseBasePoint: bool
    BasePoint: Point3d
    UserInputControls: UserInputControls
    Cursor: CursorType
    Keywords: KeywordCollection
    AppendKeywordsToMessage: bool
    Message: str
    IsReadOnly: bool

class JigPromptOptions(PromptOptions):
    """.NET: Autodesk.AutoCAD.EditorInput.JigPromptOptions"""
    def __init__(self, *args) -> None: ...
    UserInputControls: UserInputControls
    Cursor: CursorType
    Keywords: KeywordCollection
    AppendKeywordsToMessage: bool
    Message: str
    IsReadOnly: bool

class JigPromptPointOptions(JigPromptGeometryOptions):
    """.NET: Autodesk.AutoCAD.EditorInput.JigPromptPointOptions"""
    def __init__(self, *args) -> None: ...
    DefaultValue: Point3d
    UseBasePoint: bool
    BasePoint: Point3d
    UserInputControls: UserInputControls
    Cursor: CursorType
    Keywords: KeywordCollection
    AppendKeywordsToMessage: bool
    Message: str
    IsReadOnly: bool

class JigPromptStringOptions(JigPromptOptions):
    """.NET: Autodesk.AutoCAD.EditorInput.JigPromptStringOptions"""
    def __init__(self, *args) -> None: ...
    DefaultValue: str
    UserInputControls: UserInputControls
    Cursor: CursorType
    Keywords: KeywordCollection
    AppendKeywordsToMessage: bool
    Message: str
    IsReadOnly: bool

class JigPrompts:
    """.NET: Autodesk.AutoCAD.EditorInput.JigPrompts"""
    def __init__(self, *args) -> None: ...
    def AcquireAngle(self, messageAndKeywords: str, globalKeywords: str) -> PromptDoubleResult: ...
    def AcquireDistance(self, messageAndKeywords: str, globalKeywords: str) -> PromptDoubleResult: ...
    def AcquirePoint(self, messageAndKeywords: str, globalKeywords: str) -> PromptPointResult: ...
    def AcquireString(self, messageAndKeywords: str, globalKeywords: str) -> PromptResult: ...

class Keyword:
    """.NET: Autodesk.AutoCAD.EditorInput.Keyword"""
    def __init__(self, *args) -> None: ...
    Enabled: bool
    Visible: bool
    DisplayName: str
    GlobalName: str
    LocalName: str
    IsReadOnly: bool

class KeywordCollection:
    """.NET: Autodesk.AutoCAD.EditorInput.KeywordCollection"""
    def __init__(self, *args) -> None: ...
    Item: Keyword
    Default: str
    IsReadOnly: bool
    Count: int
    def Add(self, globalName: str, localName: str, displayName: str, visible: bool, enabled: bool) -> None: ...
    def Clear(self, ) -> None: ...
    def CopyTo(self, array: list, index: int) -> None: ...
    def GetDisplayString(self, showNoDefault: bool) -> str: ...
    def GetEnumerator(self, ) -> IEnumerator: ...

class LivePreview(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.EditorInput.LivePreview"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AbortAll(self, ) -> None: ...
    def EndPreview(self, delayTime: int, bRegen: bool) -> None: ...
    def EndRecording(self, ) -> None: ...
    @staticmethod
    def IsPreviewRecording(doc: Document) -> bool: ...
    @staticmethod
    def IsPreviewStarted(doc: Document) -> bool: ...
    def QueueAction(self, action: LivePreviewActionBase, delayTime: int) -> None: ...
    def StartRecording(self, ) -> None: ...

class LivePreviewAction(LivePreviewActionBase):
    """.NET: Autodesk.AutoCAD.EditorInput.LivePreviewAction"""
    def __init__(self, *args) -> None: ...
    def Execute(self, ) -> None: ...

class LivePreviewActionBase:
    """.NET: Autodesk.AutoCAD.EditorInput.LivePreviewActionBase"""
    def __init__(self, *args) -> None: ...
    def Execute(self, ) -> None: ...
    def OnAborted(self, ) -> None: ...

class LivePreviewCallback:
    """.NET: Autodesk.AutoCAD.EditorInput.LivePreviewCallback"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, ) -> None: ...

class LivePreviewCommand(LivePreviewActionBase):
    """.NET: Autodesk.AutoCAD.EditorInput.LivePreviewCommand"""
    def __init__(self, *args) -> None: ...
    def Execute(self, ) -> None: ...

class LivePreviewContextCallback:
    """.NET: Autodesk.AutoCAD.EditorInput.LivePreviewContextCallback"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, contextName: str, contextVal: object, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, contextName: str, contextVal: object) -> None: ...

class LivePreviewContextParameter:
    """.NET: Autodesk.AutoCAD.EditorInput.LivePreviewContextParameter"""
    def __init__(self, *args) -> None: ...
    LivePreview: LivePreview
    Value: object
    Type: LivePreviewContextType

class LivePreviewContextProxy:
    """.NET: Autodesk.AutoCAD.EditorInput.LivePreviewContextProxy"""
    def __init__(self, *args) -> None: ...
    def Dispose(self, ) -> None: ...

class LivePreviewContextType:
    """.NET enum: Autodesk.AutoCAD.EditorInput.LivePreviewContextType"""
    def __init__(self, *args) -> None: ...
    EndPreview: int  # = 0
    UpdatePreview: int  # = 1
class LivePreviewDelegate(LivePreviewActionBase):
    """.NET: Autodesk.AutoCAD.EditorInput.LivePreviewDelegate"""
    def __init__(self, *args) -> None: ...
    def Execute(self, ) -> None: ...
    def OnAborted(self, ) -> None: ...

class LivePreviewEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.LivePreviewEventArgs"""
    def __init__(self, *args) -> None: ...
    CommandParameter: object
    Parameters: list
    Document: Document
    AbortPreview: bool
    def LockDocument(self, ) -> IDisposable: ...

class LivePreviewPropertySetting(LivePreviewActionBase):
    """.NET: Autodesk.AutoCAD.EditorInput.LivePreviewPropertySetting"""
    def __init__(self, *args) -> None: ...
    def Execute(self, ) -> None: ...

class ObjectSnapMasks:
    """.NET enum: Autodesk.AutoCAD.EditorInput.ObjectSnapMasks"""
    def __init__(self, *args) -> None: ...
    End: int  # = 1
    Middle: int  # = 2
    Center: int  # = 4
    Node: int  # = 8
    Quadrant: int  # = 16
    Intersection: int  # = 32
    Insertion: int  # = 64
    Perpendicular: int  # = 128
    Tangent: int  # = 256
    Near: int  # = 512
    Quick: int  # = 1024
    ApparentIntersection: int  # = 2048
    Immediate: int  # = 65536
    AllowTangent: int  # = 131072
    DisablePerpendicular: int  # = 262144
    RelativeCartesian: int  # = 524288
    RelativePolar: int  # = 1048576
    NoneOverride: int  # = 2097152
class PickPointDescriptor:
    """.NET: Autodesk.AutoCAD.EditorInput.PickPointDescriptor"""
    def __init__(self, *args) -> None: ...
    Direction: Vector3d
    PointOnLine: Point3d
    Kind: PickPointKind
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def IsEqualTo(self, a: PickPointDescriptor, tolerance: Tolerance) -> bool: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class PickPointKind:
    """.NET enum: Autodesk.AutoCAD.EditorInput.PickPointKind"""
    def __init__(self, *args) -> None: ...
    InfiniteLine: int  # = 0
    Ray: int  # = 1
    LineSegment: int  # = 2
class PickPointSelectedObject(SelectedObject):
    """.NET: Autodesk.AutoCAD.EditorInput.PickPointSelectedObject"""
    def __init__(self, *args) -> None: ...
    PickPoint: PickPointDescriptor
    OptionalDetails: SelectionDetails
    GraphicsSystemMarkerPtr: IntPtr
    GraphicsSystemMarker: int
    SelectionMethod: SelectionMethod
    ObjectId: ObjectId
    def ToString(self, provider: IFormatProvider) -> str: ...

class PickPointSelectedSubObject(SelectedSubObject):
    """.NET: Autodesk.AutoCAD.EditorInput.PickPointSelectedSubObject"""
    def __init__(self, *args) -> None: ...
    PickPoint: PickPointDescriptor
    GraphicsSystemMarkerPtr: IntPtr
    GraphicsSystemMarker: int
    OptionalDetails: SelectionDetails
    SelectionMethod: SelectionMethod
    FullSubentityPath: FullSubentityPath
    def ToString(self, provider: IFormatProvider) -> str: ...

class PointFilterEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.PointFilterEventArgs"""
    def __init__(self, *args) -> None: ...
    CallNext: bool
    Result: PointFilterResult
    Context: InputPointContext
    def Dispose(self, ) -> None: ...

class PointFilterEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.PointFilterEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: PointFilterEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: PointFilterEventArgs) -> None: ...

class PointFilterResult:
    """.NET: Autodesk.AutoCAD.EditorInput.PointFilterResult"""
    def __init__(self, *args) -> None: ...
    ToolTipText: str
    DisplayObjectSnapGlyph: bool
    NewPoint: Point3d
    Retry: bool
    def Dispose(self, ) -> None: ...

class PointHistoryBits:
    """.NET enum: Autodesk.AutoCAD.EditorInput.PointHistoryBits"""
    def __init__(self, *args) -> None: ...
    DidNotPick: int  # = 0
    Tablet: int  # = 1
    NotDigitizer: int  # = 2
    LastPoint: int  # = 4
    Gripped: int  # = 8
    CartSnapped: int  # = 16
    Ortho: int  # = 32
    CyclingPoint: int  # = 64
    ObjectSnapped: int  # = 128
    PolarAngle: int  # = 256
    Aligned: int  # = 1024
    AppFiltered: int  # = 2048
    ForcedPick: int  # = 4096
    UsedPickBox: int  # = 8192
    UsedObjectSnapBox: int  # = 16384
    PickAborted: int  # = 32768
    PickMask: int  # = 57344
    XPending: int  # = 65536
    YPending: int  # = 131072
    ZPending: int  # = 262144
    CoordinatePending: int  # = 458752
    FromKeyboard: int  # = 524288
    NotInteractive: int  # = 1048576
class PointInputEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.PointInputEventArgs"""
    def __init__(self, *args) -> None: ...
    Handled: bool
    Result: PointFilterResult
    Context: InputPointContext
    GraphicsSystemMarker: IntPtr

class PointInputEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.PointInputEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: PointInputEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: PointInputEventArgs) -> None: ...

class PointMonitorEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.PointMonitorEventArgs"""
    def __init__(self, *args) -> None: ...
    Context: InputPointContext
    def AppendToolTipText(self, value: str) -> None: ...
    def Dispose(self, ) -> None: ...

class PointMonitorEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.PointMonitorEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: PointMonitorEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: PointMonitorEventArgs) -> None: ...

class PromptAngleOptions(PromptEditorOptions):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptAngleOptions"""
    def __init__(self, *args) -> None: ...
    UseAngleBase: bool
    UseDefaultValue: bool
    DefaultValue: float
    UseDashedLine: bool
    UseBasePoint: bool
    BasePoint: Point3d
    AllowZero: bool
    AllowArbitraryInput: bool
    AllowNone: bool
    Keywords: KeywordCollection
    AppendKeywordsToMessage: bool
    Message: str
    IsReadOnly: bool

class PromptAngleOptionsEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptAngleOptionsEventArgs"""
    def __init__(self, *args) -> None: ...
    Options: PromptAngleOptions

class PromptAngleOptionsEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.PromptAngleOptionsEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: PromptAngleOptionsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: PromptAngleOptionsEventArgs) -> None: ...

class PromptCornerOptions(PromptEditorOptions):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptCornerOptions"""
    def __init__(self, *args) -> None: ...
    LimitsChecked: bool
    UseDashedLine: bool
    BasePoint: Point3d
    AllowArbitraryInput: bool
    AllowNone: bool
    Keywords: KeywordCollection
    AppendKeywordsToMessage: bool
    Message: str
    IsReadOnly: bool

class PromptDistanceOptions(PromptNumericalOptions):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptDistanceOptions"""
    def __init__(self, *args) -> None: ...
    DefaultValue: float
    Only2d: bool
    UseDashedLine: bool
    UseBasePoint: bool
    BasePoint: Point3d
    UseDefaultValue: bool
    AllowZero: bool
    AllowNegative: bool
    AllowArbitraryInput: bool
    AllowNone: bool
    Keywords: KeywordCollection
    AppendKeywordsToMessage: bool
    Message: str
    IsReadOnly: bool

class PromptDistanceOptionsEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptDistanceOptionsEventArgs"""
    def __init__(self, *args) -> None: ...
    Options: PromptDistanceOptions

class PromptDistanceOptionsEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.PromptDistanceOptionsEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: PromptDistanceOptionsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: PromptDistanceOptionsEventArgs) -> None: ...

class PromptDoubleOptions(PromptNumericalOptions):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptDoubleOptions"""
    def __init__(self, *args) -> None: ...
    DefaultValue: float
    UseDefaultValue: bool
    AllowZero: bool
    AllowNegative: bool
    AllowArbitraryInput: bool
    AllowNone: bool
    Keywords: KeywordCollection
    AppendKeywordsToMessage: bool
    Message: str
    IsReadOnly: bool

class PromptDoubleOptionsEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptDoubleOptionsEventArgs"""
    def __init__(self, *args) -> None: ...
    Options: PromptDoubleOptions

class PromptDoubleOptionsEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.PromptDoubleOptionsEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: PromptDoubleOptionsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: PromptDoubleOptionsEventArgs) -> None: ...

class PromptDoubleResult(PromptResult):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptDoubleResult"""
    def __init__(self, *args) -> None: ...
    Value: float
    StringResult: str
    Status: PromptStatus
    def ToString(self, provider: IFormatProvider) -> str: ...

class PromptDoubleResultEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptDoubleResultEventArgs"""
    def __init__(self, *args) -> None: ...
    Result: PromptDoubleResult

class PromptDoubleResultEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.PromptDoubleResultEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: PromptDoubleResultEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: PromptDoubleResultEventArgs) -> None: ...

class PromptDragOptions(PromptEditorOptions):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptDragOptions"""
    def __init__(self, *args) -> None: ...
    Cursor: DragCursor
    Callback: DragCallback
    Selection: SelectionSet
    AllowArbitraryInput: bool
    AllowNone: bool
    Keywords: KeywordCollection
    AppendKeywordsToMessage: bool
    Message: str
    IsReadOnly: bool

class PromptEditorOptions(PromptOptions):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptEditorOptions"""
    def __init__(self, *args) -> None: ...
    Keywords: KeywordCollection
    AppendKeywordsToMessage: bool
    Message: str
    IsReadOnly: bool

class PromptEntityOptions(PromptEditorOptions):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptEntityOptions"""
    def __init__(self, *args) -> None: ...
    AllowObjectOnLockedLayer: bool
    AllowNone: bool
    Keywords: KeywordCollection
    AppendKeywordsToMessage: bool
    Message: str
    IsReadOnly: bool
    def AddAllowedClass(self, type: Type, exactMatch: bool) -> None: ...
    def RemoveAllowedClass(self, type: Type) -> None: ...
    def SetRejectMessage(self, message: str) -> None: ...

class PromptEntityOptionsEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptEntityOptionsEventArgs"""
    def __init__(self, *args) -> None: ...
    Options: PromptEntityOptions

class PromptEntityOptionsEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.PromptEntityOptionsEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: PromptEntityOptionsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: PromptEntityOptionsEventArgs) -> None: ...

class PromptEntityResult(PromptResult):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptEntityResult"""
    def __init__(self, *args) -> None: ...
    PickedPoint: Point3d
    ObjectId: ObjectId
    StringResult: str
    Status: PromptStatus
    def ToString(self, provider: IFormatProvider) -> str: ...

class PromptEntityResultEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptEntityResultEventArgs"""
    def __init__(self, *args) -> None: ...
    Result: PromptEntityResult

class PromptEntityResultEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.PromptEntityResultEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: PromptEntityResultEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: PromptEntityResultEventArgs) -> None: ...

class PromptFileNameResult(PromptResult):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptFileNameResult"""
    def __init__(self, *args) -> None: ...
    ReadOnly: bool
    StringResult: str
    Status: PromptStatus
    def ToString(self, provider: IFormatProvider) -> str: ...

class PromptFileOptions:
    """.NET: Autodesk.AutoCAD.EditorInput.PromptFileOptions"""
    def __init__(self, *args) -> None: ...
    AllowUrls: bool
    PreferCommandLine: bool
    InitialDirectory: str
    InitialFileName: str
    FilterIndex: int
    Filter: str
    DialogName: str
    DialogCaption: str
    Message: str

class PromptForEntityEndingEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptForEntityEndingEventArgs"""
    def __init__(self, *args) -> None: ...
    Result: PromptEntityResult
    def Dispose(self, ) -> None: ...
    def RemoveSelectedObject(self, ) -> None: ...
    def ReplaceSelectedObject(self, newValue: SelectedObject) -> None: ...

class PromptForEntityEndingEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.PromptForEntityEndingEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: PromptForEntityEndingEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: PromptForEntityEndingEventArgs) -> None: ...

class PromptForSelectionEndingEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptForSelectionEndingEventArgs"""
    def __init__(self, *args) -> None: ...
    Selection: SelectionSet
    Flags: SelectionFlags
    def Add(self, value: SelectedObject) -> None: ...
    def AddSubEntity(self, value: SelectedSubObject) -> None: ...
    def Dispose(self, ) -> None: ...
    def Remove(self, index: int) -> None: ...
    def RemoveSubEntity(self, entityIndex: int, subEntityIndex: int) -> None: ...

class PromptForSelectionEndingEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.PromptForSelectionEndingEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: PromptForSelectionEndingEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: PromptForSelectionEndingEventArgs) -> None: ...

class PromptIntegerOptions(PromptNumericalOptions):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptIntegerOptions"""
    def __init__(self, *args) -> None: ...
    UpperLimit: int
    LowerLimit: int
    DefaultValue: int
    UseDefaultValue: bool
    AllowZero: bool
    AllowNegative: bool
    AllowArbitraryInput: bool
    AllowNone: bool
    Keywords: KeywordCollection
    AppendKeywordsToMessage: bool
    Message: str
    IsReadOnly: bool

class PromptIntegerOptionsEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptIntegerOptionsEventArgs"""
    def __init__(self, *args) -> None: ...
    Options: PromptIntegerOptions

class PromptIntegerOptionsEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.PromptIntegerOptionsEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: PromptIntegerOptionsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: PromptIntegerOptionsEventArgs) -> None: ...

class PromptIntegerResult(PromptResult):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptIntegerResult"""
    def __init__(self, *args) -> None: ...
    Value: int
    StringResult: str
    Status: PromptStatus
    def ToString(self, provider: IFormatProvider) -> str: ...

class PromptIntegerResultEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptIntegerResultEventArgs"""
    def __init__(self, *args) -> None: ...
    Result: PromptIntegerResult

class PromptIntegerResultEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.PromptIntegerResultEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: PromptIntegerResultEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: PromptIntegerResultEventArgs) -> None: ...

class PromptKeywordOptions(PromptEditorOptions):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptKeywordOptions"""
    def __init__(self, *args) -> None: ...
    AllowArbitraryInput: bool
    AllowNone: bool
    Keywords: KeywordCollection
    AppendKeywordsToMessage: bool
    Message: str
    IsReadOnly: bool

class PromptKeywordOptionsEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptKeywordOptionsEventArgs"""
    def __init__(self, *args) -> None: ...
    Options: PromptKeywordOptions

class PromptKeywordOptionsEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.PromptKeywordOptionsEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: PromptKeywordOptionsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: PromptKeywordOptionsEventArgs) -> None: ...

class PromptNestedEntityOptions(PromptEditorOptions):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptNestedEntityOptions"""
    def __init__(self, *args) -> None: ...
    UseNonInteractivePickPoint: bool
    NonInteractivePickPoint: Point3d
    AllowNone: bool
    Keywords: KeywordCollection
    AppendKeywordsToMessage: bool
    Message: str
    IsReadOnly: bool

class PromptNestedEntityOptionsEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptNestedEntityOptionsEventArgs"""
    def __init__(self, *args) -> None: ...
    Options: PromptNestedEntityOptions

class PromptNestedEntityOptionsEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.PromptNestedEntityOptionsEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: PromptNestedEntityOptionsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: PromptNestedEntityOptionsEventArgs) -> None: ...

class PromptNestedEntityResult(PromptEntityResult):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptNestedEntityResult"""
    def __init__(self, *args) -> None: ...
    Transform: Matrix3d
    PickedPoint: Point3d
    ObjectId: ObjectId
    StringResult: str
    Status: PromptStatus
    def GetContainers(self, ) -> list: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class PromptNestedEntityResultEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptNestedEntityResultEventArgs"""
    def __init__(self, *args) -> None: ...
    Result: PromptNestedEntityResult

class PromptNestedEntityResultEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.PromptNestedEntityResultEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: PromptNestedEntityResultEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: PromptNestedEntityResultEventArgs) -> None: ...

class PromptNumericalOptions(PromptEditorOptions):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptNumericalOptions"""
    def __init__(self, *args) -> None: ...
    UseDefaultValue: bool
    AllowZero: bool
    AllowNegative: bool
    AllowArbitraryInput: bool
    AllowNone: bool
    Keywords: KeywordCollection
    AppendKeywordsToMessage: bool
    Message: str
    IsReadOnly: bool

class PromptOpenFileOptions(PromptFileOptions):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptOpenFileOptions"""
    def __init__(self, *args) -> None: ...
    TransferRemoteFiles: bool
    SearchPath: bool
    AllowUrls: bool
    PreferCommandLine: bool
    InitialDirectory: str
    InitialFileName: str
    FilterIndex: int
    Filter: str
    DialogName: str
    DialogCaption: str
    Message: str

class PromptOptions:
    """.NET: Autodesk.AutoCAD.EditorInput.PromptOptions"""
    def __init__(self, *args) -> None: ...
    Keywords: KeywordCollection
    AppendKeywordsToMessage: bool
    Message: str
    IsReadOnly: bool
    def SetMessageAndKeywords(self, messageAndKeywords: str, globalKeywords: str) -> None: ...

class PromptPointOptions(PromptCornerOptions):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptPointOptions"""
    def __init__(self, *args) -> None: ...
    UseBasePoint: bool
    LimitsChecked: bool
    UseDashedLine: bool
    BasePoint: Point3d
    AllowArbitraryInput: bool
    AllowNone: bool
    Keywords: KeywordCollection
    AppendKeywordsToMessage: bool
    Message: str
    IsReadOnly: bool

class PromptPointOptionsEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptPointOptionsEventArgs"""
    def __init__(self, *args) -> None: ...
    Options: PromptPointOptions

class PromptPointOptionsEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.PromptPointOptionsEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: PromptPointOptionsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: PromptPointOptionsEventArgs) -> None: ...

class PromptPointResult(PromptResult):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptPointResult"""
    def __init__(self, *args) -> None: ...
    Value: Point3d
    StringResult: str
    Status: PromptStatus
    def ToString(self, provider: IFormatProvider) -> str: ...

class PromptPointResultEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptPointResultEventArgs"""
    def __init__(self, *args) -> None: ...
    Result: PromptPointResult

class PromptPointResultEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.PromptPointResultEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: PromptPointResultEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: PromptPointResultEventArgs) -> None: ...

class PromptResult:
    """.NET: Autodesk.AutoCAD.EditorInput.PromptResult"""
    def __init__(self, *args) -> None: ...
    StringResult: str
    Status: PromptStatus
    def ToString(self, provider: IFormatProvider) -> str: ...

class PromptSaveFileOptions(PromptFileOptions):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptSaveFileOptions"""
    def __init__(self, *args) -> None: ...
    DisplaySaveOptionsMenuItem: bool
    ForceOverwriteWarningForScriptsAndLisp: bool
    DeriveInitialFilenameFromDrawingName: bool
    AllowUrls: bool
    PreferCommandLine: bool
    InitialDirectory: str
    InitialFileName: str
    FilterIndex: int
    Filter: str
    DialogName: str
    DialogCaption: str
    Message: str

class PromptSelectionOptions:
    """.NET: Autodesk.AutoCAD.EditorInput.PromptSelectionOptions"""
    def __init__(self, *args) -> None: ...
    RejectPaperspaceViewport: bool
    RejectObjectsFromNonCurrentSpace: bool
    RejectObjectsOnLockedLayers: bool
    ForceSubSelections: bool
    AllowSubSelections: bool
    SingleOnly: bool
    PrepareOptionalDetails: bool
    Keywords: KeywordCollection
    SelectEverythingInAperture: bool
    AllowDuplicates: bool
    SinglePickInSpace: bool
    MessageForRemoval: str
    MessageForAdding: str
    def AddKeywordsToMinimalList(self, kwds: AddedKeywords) -> None: ...
    def RemoveKeywordsFromFullList(self, kwds: SubtractedKeywords) -> None: ...
    def SetKeywords(self, keywords: str, globalKeywords: str) -> None: ...

class PromptSelectionOptionsEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptSelectionOptionsEventArgs"""
    def __init__(self, *args) -> None: ...
    Filter: SelectionFilter
    Options: PromptSelectionOptions
    def GetPoints(self, ) -> list: ...

class PromptSelectionOptionsEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.PromptSelectionOptionsEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: PromptSelectionOptionsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: PromptSelectionOptionsEventArgs) -> None: ...

class PromptSelectionResult:
    """.NET: Autodesk.AutoCAD.EditorInput.PromptSelectionResult"""
    def __init__(self, *args) -> None: ...
    Value: SelectionSet
    Status: PromptStatus
    def ToString(self, provider: IFormatProvider) -> str: ...

class PromptSelectionResultEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptSelectionResultEventArgs"""
    def __init__(self, *args) -> None: ...
    Result: PromptSelectionResult

class PromptSelectionResultEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.PromptSelectionResultEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: PromptSelectionResultEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: PromptSelectionResultEventArgs) -> None: ...

class PromptStatus:
    """.NET enum: Autodesk.AutoCAD.EditorInput.PromptStatus"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 5000
    Modeless: int  # = 5027
    Other: int  # = 5028
    OK: int  # = 5100
    Keyword: int  # = -5005
    Cancel: int  # = -5002
    Error: int  # = -5001
class PromptStringOptions(PromptEditorOptions):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptStringOptions"""
    def __init__(self, *args) -> None: ...
    UseDefaultValue: bool
    DefaultValue: str
    AllowSpaces: bool
    Keywords: KeywordCollection
    AppendKeywordsToMessage: bool
    Message: str
    IsReadOnly: bool

class PromptStringOptionsEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptStringOptionsEventArgs"""
    def __init__(self, *args) -> None: ...
    Options: PromptStringOptions

class PromptStringOptionsEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.PromptStringOptionsEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: PromptStringOptionsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: PromptStringOptionsEventArgs) -> None: ...

class PromptStringResultEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.PromptStringResultEventArgs"""
    def __init__(self, *args) -> None: ...
    Result: PromptResult

class PromptStringResultEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.PromptStringResultEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: PromptStringResultEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: PromptStringResultEventArgs) -> None: ...

class RolloverEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.RolloverEventArgs"""
    def __init__(self, *args) -> None: ...
    Highlighted: FullSubentityPath
    Picked: FullSubentityPath

class RolloverEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.RolloverEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: RolloverEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: RolloverEventArgs) -> None: ...

class SamplerStatus:
    """.NET enum: Autodesk.AutoCAD.EditorInput.SamplerStatus"""
    def __init__(self, *args) -> None: ...
    OK: int  # = 0
    NoChange: int  # = 1
    Cancel: int  # = 2
class SelectedObject:
    """.NET: Autodesk.AutoCAD.EditorInput.SelectedObject"""
    def __init__(self, *args) -> None: ...
    OptionalDetails: SelectionDetails
    GraphicsSystemMarkerPtr: IntPtr
    GraphicsSystemMarker: int
    SelectionMethod: SelectionMethod
    ObjectId: ObjectId
    def GetSubentities(self, ) -> list: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class SelectedSubObject:
    """.NET: Autodesk.AutoCAD.EditorInput.SelectedSubObject"""
    def __init__(self, *args) -> None: ...
    GraphicsSystemMarkerPtr: IntPtr
    GraphicsSystemMarker: int
    OptionalDetails: SelectionDetails
    SelectionMethod: SelectionMethod
    FullSubentityPath: FullSubentityPath
    def ToString(self, provider: IFormatProvider) -> str: ...

class SelectionAddedEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.SelectionAddedEventArgs"""
    def __init__(self, *args) -> None: ...
    AddedObjects: SelectionSet
    Selection: SelectionSet
    Flags: SelectionFlags
    def Add(self, value: SelectedObject) -> None: ...
    def AddSubEntity(self, value: SelectedSubObject) -> None: ...
    def Dispose(self, ) -> None: ...
    def Highlight(self, subSelectionIndex: int, path: FullSubentityPath) -> None: ...
    def Remove(self, index: int) -> None: ...
    def RemoveSubEntity(self, entityIndex: int, subEntityIndex: int) -> None: ...

class SelectionAddedEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.SelectionAddedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: SelectionAddedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: SelectionAddedEventArgs) -> None: ...

class SelectionDetails:
    """.NET: Autodesk.AutoCAD.EditorInput.SelectionDetails"""
    def __init__(self, *args) -> None: ...
    Transform: Matrix3d
    def GetContainers(self, ) -> list: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class SelectionFilter:
    """.NET: Autodesk.AutoCAD.EditorInput.SelectionFilter"""
    def __init__(self, *args) -> None: ...
    def GetFilter(self, ) -> list: ...

class SelectionFlags:
    """.NET enum: Autodesk.AutoCAD.EditorInput.SelectionFlags"""
    def __init__(self, *args) -> None: ...
    Normal: int  # = 0
    PickPoints: int  # = 1
    Duplicates: int  # = 2
    NestedEntities: int  # = 4
    SubEntities: int  # = 8
    SinglePick: int  # = 16
    PickfirstSet: int  # = 32
    PreviousSet: int  # = 64
    SubSelection: int  # = 128
    Undo: int  # = 256
    FailedPickAuto: int  # = 512
class SelectionMethod:
    """.NET enum: Autodesk.AutoCAD.EditorInput.SelectionMethod"""
    def __init__(self, *args) -> None: ...
    NonGraphical: int  # = 0
    PickPoint: int  # = 1
    Window: int  # = 2
    Crossing: int  # = 3
    Fence: int  # = 4
    SubEntity: int  # = 5
    Unavailable: int  # = -1
class SelectionMode:
    """.NET enum: Autodesk.AutoCAD.EditorInput.SelectionMode"""
    def __init__(self, *args) -> None: ...
    Window: int  # = 1
    Crossing: int  # = 2
    Box: int  # = 3
    Last: int  # = 4
    Entity: int  # = 5
    All: int  # = 6
    FencePolyline: int  # = 7
    CrossingPolygon: int  # = 8
    WindowPolygon: int  # = 9
    Pick: int  # = 10
    Every: int  # = 11
    Extents: int  # = 12
    Group: int  # = 13
    Previous: int  # = 14
    Multiple: int  # = 15
class SelectionRemovedEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.SelectionRemovedEventArgs"""
    def __init__(self, *args) -> None: ...
    RemovedObjects: SelectionSet
    Selection: SelectionSet
    Flags: SelectionFlags
    def Dispose(self, ) -> None: ...
    def Remove(self, index: int) -> None: ...
    def RemoveSubentity(self, index: int, subentityIndex: int) -> None: ...

class SelectionRemovedEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.SelectionRemovedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: SelectionRemovedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: SelectionRemovedEventArgs) -> None: ...

class SelectionSet:
    """.NET: Autodesk.AutoCAD.EditorInput.SelectionSet"""
    def __init__(self, *args) -> None: ...
    IsSynchronized: bool
    SyncRoot: object
    Item: SelectedObject
    Count: int
    def CopyTo(self, array: list, index: int) -> None: ...
    def Dispose(self, ) -> None: ...
    @staticmethod
    def FromObjectIds(ids: list) -> SelectionSet: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectIds(self, ) -> list: ...
    def ToString(self, provider: IFormatProvider) -> str: ...

class SelectionSetDelayMarshalled(SelectionSet):
    """.NET: Autodesk.AutoCAD.EditorInput.SelectionSetDelayMarshalled"""
    def __init__(self, *args) -> None: ...
    Item: SelectedObject
    Count: int
    IsSynchronized: bool
    SyncRoot: object
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectIds(self, ) -> list: ...

class SelectionTextInputEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.EditorInput.SelectionTextInputEventArgs"""
    def __init__(self, *args) -> None: ...
    Input: str
    def AddObjects(self, ids: list) -> None: ...
    def SetErrorMessage(self, errorMessage: str) -> None: ...

class SelectionTextInputEventHandler:
    """.NET: Autodesk.AutoCAD.EditorInput.SelectionTextInputEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: SelectionTextInputEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: SelectionTextInputEventArgs) -> None: ...

class SubtractedKeywords:
    """.NET enum: Autodesk.AutoCAD.EditorInput.SubtractedKeywords"""
    def __init__(self, *args) -> None: ...
    LastAllGroupPrevious: int  # = 1
    PickImplied: int  # = 2
    All: int  # = 4
    BoxAuto: int  # = 8
    Multiple: int  # = 16
    CrossingCPolygon: int  # = 32
    Fence: int  # = 64
    Last: int  # = 128
    Previous: int  # = 256
    WindowWPolygon: int  # = 512
    Group: int  # = 1024
    AddRemove: int  # = 2048
class Transient(Drawable):
    """.NET: Autodesk.AutoCAD.EditorInput.Transient"""
    def __init__(self, *args) -> None: ...
    Id: ObjectId
    IsPersistent: bool
    CapturedDrawable: Drawable
    DrawStream: DrawStream
    Bounds: Nullable
    DrawableType: DrawableType
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class UserInputControls:
    """.NET enum: Autodesk.AutoCAD.EditorInput.UserInputControls"""
    def __init__(self, *args) -> None: ...
    GovernedByOrthoMode: int  # = 1
    NullResponseAccepted: int  # = 2
    DoNotEchoCancelForCtrlC: int  # = 4
    DoNotUpdateLastPoint: int  # = 8
    NoDwgLimitsChecking: int  # = 16
    NoZeroResponseAccepted: int  # = 32
    NoNegativeResponseAccepted: int  # = 64
    Accept3dCoordinates: int  # = 128
    AcceptMouseUpAsPoint: int  # = 256
    AnyBlankTerminatesInput: int  # = 512
    InitialBlankTerminatesInput: int  # = 1024
    AcceptOtherInputString: int  # = 2048
    GovernedByUCSDetect: int  # = 4096
    NoZDirectionOrtho: int  # = 8192
    UseBasePointElevation: int  # = 32768
