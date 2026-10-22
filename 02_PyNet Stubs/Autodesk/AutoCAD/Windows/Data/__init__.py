# Auto-generated — Civil 26 — Autodesk.AutoCAD.Windows.Data

class AnimationEditor:
    """.NET: Autodesk.AutoCAD.Windows.Data.AnimationEditor"""
    def __init__(self, *args) -> None: ...
    Status: NavStatus
    IsActive: bool

class AttachmentPointCommand(IPECommandBase):
    """.NET: Autodesk.AutoCAD.Windows.Data.AttachmentPointCommand"""
    def __init__(self, *args) -> None: ...
    def Execute(self, parameter: object) -> None: ...

class AutoCompleteList(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Windows.Data.AutoCompleteList"""
    def __init__(self, *args) -> None: ...
    Item: CommandLineItem
    Length: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Sort(self, ) -> None: ...

class AutoCompleteToolTipService:
    """.NET: Autodesk.AutoCAD.Windows.Data.AutoCompleteToolTipService"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def HideToolTip() -> None: ...
    @staticmethod
    def ShowToolTip(pTooltipInfo: ValueType) -> None: ...

class AutoCorrectList(DisposableWrapper):
    """.NET: Autodesk.AutoCAD.Windows.Data.AutoCorrectList"""
    def __init__(self, *args) -> None: ...
    Item: CommandLineItem
    HasClearWinner: bool
    Length: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Sort(self, ) -> None: ...

class AutoCorrectType:
    """.NET enum: Autodesk.AutoCAD.Windows.Data.AutoCorrectType"""
    def __init__(self, *args) -> None: ...
    CommandSysvar: int  # = 0
    InternalCommand: int  # = 1
class AutoCorrectorService:
    """.NET: Autodesk.AutoCAD.Windows.Data.AutoCorrectorService"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def IsAutoCorrectSupported() -> bool: ...
    @staticmethod
    def IsInputCommand(isInput: bool) -> None: ...
    @staticmethod
    def UpdateErrInputCount(errInput: str, cmdGlobalName: str, cmdLocalName: str) -> None: ...

class BackgroundMaskCommand(IPECommandBase):
    """.NET: Autodesk.AutoCAD.Windows.Data.BackgroundMaskCommand"""
    def __init__(self, *args) -> None: ...
    def Execute(self, parameter: object) -> None: ...

class BlockDialogModelBase:
    """.NET: Autodesk.AutoCAD.Windows.Data.BlockDialogModelBase"""
    def __init__(self, *args) -> None: ...
    Name: str

class BlockDialogModelInsert(BlockDialogModelBase):
    """.NET: Autodesk.AutoCAD.Windows.Data.BlockDialogModelInsert"""
    def __init__(self, *args) -> None: ...
    PaletteWindow: Window
    IsDragingInsert: bool
    SelectedBlockData: str
    AutoPlacement: BlockDialogModelValue<bool>
    Repeat: BlockDialogModelValue<bool>
    UseGeoData: BlockDialogModelValue<bool>
    Explode: BlockDialogModelValue<bool>
    Unit: BlockDialogModelUnit
    Rotation: BlockDialogModelRotation
    InsertionPoint: BlockDialogModelInsertionPoint
    Scales: BlockDialogModelScales
    Name: str
    def Dispose(self, ) -> None: ...
    def Insert(self, blockKey: str) -> None: ...
    def InsertAndRedefine(self, blockKey: str) -> None: ...
    def InsertSnapshot(self, snapshotPath: str, targetBlockName: str) -> None: ...
    def InsertSnapshotAndRedefine(self, snapshotPath: str, targetBlockName: str) -> None: ...
    def InsertSnapshotWithoutRedefine(self, snapshotPath: str, targetBlockName: str) -> None: ...
    def InsertWithoutRedefine(self, blockKey: str) -> None: ...
    def IsBlockCanBeRedefined(self, blockKey: str) -> bool: ...
    def RedefineFromSnapshotOnly(self, snapshotPath: str, targetBlockName: str) -> None: ...
    def RedefineOnly(self, blockKey: str) -> None: ...
    def initBlockStreamUIData(self, ) -> None: ...
    def isPaletteVisible(self, ) -> bool: ...
    def saveBlockStreamUIData(self, ) -> None: ...

class BlockDialogModelInsertionPoint:
    """.NET: Autodesk.AutoCAD.Windows.Data.BlockDialogModelInsertionPoint"""
    def __init__(self, *args) -> None: ...
    PickOnScreen: BlockDialogModelValue<bool>
    Z: BlockDialogModelValue<double>
    Y: BlockDialogModelValue<double>
    X: BlockDialogModelValue<double>

class BlockDialogModelRotation:
    """.NET: Autodesk.AutoCAD.Windows.Data.BlockDialogModelRotation"""
    def __init__(self, *args) -> None: ...
    PickOnScreen: BlockDialogModelValue<bool>
    Angle: BlockDialogModelValue<double>

class BlockDialogModelScales:
    """.NET: Autodesk.AutoCAD.Windows.Data.BlockDialogModelScales"""
    def __init__(self, *args) -> None: ...
    ScaleOnScreen: BlockDialogModelValue<bool>
    UniformScale: BlockDialogModelValue<bool>
    Z: BlockDialogModelValue<double>
    Y: BlockDialogModelValue<double>
    XLabelState: BlockDialogModelValue<bool>
    X: BlockDialogModelValue<double>

class BlockDialogModelUnit:
    """.NET: Autodesk.AutoCAD.Windows.Data.BlockDialogModelUnit"""
    def __init__(self, *args) -> None: ...
    ScaleFactor: BlockDialogModelValueString
    UnitValue: BlockDialogModelValueString

class BlockDialogModelValue<bool>:
    """.NET: Autodesk.AutoCAD.Windows.Data.BlockDialogModelValue<bool>"""
    def __init__(self, *args) -> None: ...
    Enabled: bool
    Value: bool

class BlockDialogModelValue<double>:
    """.NET: Autodesk.AutoCAD.Windows.Data.BlockDialogModelValue<double>"""
    def __init__(self, *args) -> None: ...
    Enabled: bool
    Value: float

class BlockDialogModelValueString:
    """.NET: Autodesk.AutoCAD.Windows.Data.BlockDialogModelValueString"""
    def __init__(self, *args) -> None: ...
    Enabled: bool
    Value: str

class BlockEditor:
    """.NET: Autodesk.AutoCAD.Windows.Data.BlockEditor"""
    def __init__(self, *args) -> None: ...
    VisibilitySets: ObservableCollection
    CurrentVisibilityStateName: str
    Tooltip: str
    BlockName: str
    IsAuthorPaletteVisible: bool
    IsVisibilityParameterPresent: bool
    IsInBlockEditor: bool
    def Dispose(self, ) -> None: ...
    def OnDocumentActivated(self, sender: object, e: DocumentCollectionEventArgs) -> None: ...
    def OnSystemVariableChanged(self, sender: object, e: PropertyChangedEventArgs) -> None: ...

class BlockLibraryInterop:
    """.NET: Autodesk.AutoCAD.Windows.Data.BlockLibraryInterop"""
    def __init__(self, *args) -> None: ...
    def Dispose(self, ) -> None: ...
    def setWPFBrowserPalette(self, tabs: Window) -> None: ...

class CMLContentSearchPreviews:
    """.NET: Autodesk.AutoCAD.Windows.Data.CMLContentSearchPreviews"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def ClearDimStySampleObjects() -> None: ...
    @staticmethod
    def ConvertImageToImageSource(pImage: Image) -> ImageSource: ...
    @staticmethod
    def CreateDimStySampleObjects() -> None: ...
    @staticmethod
    def GetBlockTRThumbnail(blockTR: BlockTableRecord) -> ImageSource: ...
    @staticmethod
    def GetColorFromSysvarSettings(sysvarName: str, outColor: Color) -> bool: ...
    @staticmethod
    def GetDimStyleThumbnail(dimStyle: DimStyleTableRecord) -> ImageSource: ...

class CellStyleConverter:
    """.NET: Autodesk.AutoCAD.Windows.Data.CellStyleConverter"""
    def __init__(self, *args) -> None: ...
    ByRowColumn: str
    Varies: str
    def Convert(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...
    def ConvertBack(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...

class CharacterSetCommand(IPECommandBase):
    """.NET: Autodesk.AutoCAD.Windows.Data.CharacterSetCommand"""
    def __init__(self, *args) -> None: ...
    def Execute(self, parameter: object) -> None: ...

class ClearLineSpaceCommand(IPECommandBase):
    """.NET: Autodesk.AutoCAD.Windows.Data.ClearLineSpaceCommand"""
    def __init__(self, *args) -> None: ...
    def Execute(self, parameter: object) -> None: ...

class CloseCommand(IPECommandBase):
    """.NET: Autodesk.AutoCAD.Windows.Data.CloseCommand"""
    def __init__(self, *args) -> None: ...
    def Execute(self, parameter: object) -> None: ...

class ColorCollection(DataItemCollection):
    """.NET: Autodesk.AutoCAD.Windows.Data.ColorCollection"""
    def __init__(self, *args) -> None: ...
    Commands: ILookup
    IsReadOnly: bool
    Item: ICustomTypeDescriptor
    Count: int
    Active: bool
    CurrentItem: ICustomTypeDescriptor
    def AddIfNotContain(self, value: Color) -> AcDiDynamicObject: ...

class ColorCommand:
    """.NET: Autodesk.AutoCAD.Windows.Data.ColorCommand"""
    def __init__(self, *args) -> None: ...
    def CanExecute(self, parameter: object) -> bool: ...
    def Execute(self, parameter: object) -> None: ...

class ColorSetting:
    """.NET: Autodesk.AutoCAD.Windows.Data.ColorSetting"""
    def __init__(self, *args) -> None: ...
    Value: Color
    Name: str

class ColorToNamedValueConverter:
    """.NET: Autodesk.AutoCAD.Windows.Data.ColorToNamedValueConverter"""
    def __init__(self, *args) -> None: ...
    def Convert(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...
    def ConvertBack(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...

class ColumnsSettingsDialogCommand(IPECommandBase):
    """.NET: Autodesk.AutoCAD.Windows.Data.ColumnsSettingsDialogCommand"""
    def __init__(self, *args) -> None: ...
    def Execute(self, parameter: object) -> None: ...

class Command:
    """.NET: Autodesk.AutoCAD.Windows.Data.Command"""
    def __init__(self, *args) -> None: ...
    IsFocusAble: bool
    Hidden: bool
    Synchronous: bool
    def CanExecute(self, parameter: object) -> bool: ...
    def Clone(self, ) -> object: ...
    def Execute(self, parameter: object) -> None: ...

class CommandCompletionType:
    """.NET enum: Autodesk.AutoCAD.Windows.Data.CommandCompletionType"""
    def __init__(self, *args) -> None: ...
    Command: int  # = 1
    Keyword: int  # = 2
    File: int  # = 4
class CommandEditor:
    """.NET: Autodesk.AutoCAD.Windows.Data.CommandEditor"""
    def __init__(self, *args) -> None: ...
    ActualDisplayedLinesCount: int
    NeedShowClickableKeywords: bool
    VisibleHistoryItemsCount: int
    IsBusy: bool
    CurrentCommandIcon: IntPtr
    CurrentCommand: str
    TemporaryHistory: ObservableCollection
    History: ObservableCollection
    RecentCommands: List
    PromptAndInput: PromptAndInput
    def ClearTempHistory(self, ) -> None: ...
    def CopyHistoryToClipBoard(self, ) -> None: ...
    def SyncHistoryViewList(self, ) -> None: ...

class CommandEditorManager:
    """.NET: Autodesk.AutoCAD.Windows.Data.CommandEditorManager"""
    def __init__(self, *args) -> None: ...
    ActiveEditor: CommandEditor
    def Dispose(self, ) -> None: ...

class CommandHistory:
    """.NET: Autodesk.AutoCAD.Windows.Data.CommandHistory"""
    def __init__(self, *args) -> None: ...
    Command: str

class CommandLineItem:
    """.NET: Autodesk.AutoCAD.Windows.Data.CommandLineItem"""
    def __init__(self, *args) -> None: ...
    Tooltip: IntPtr
    ImageKey: str
    Image: IntPtr
    Flags: int
    LocalName: str
    GlobalName: str
    UnderlyingCommand: str
    DisplayText: str
    Value: str
    def AddRef(self, ) -> None: ...
    @staticmethod
    def ImageFromKey(key: str) -> BitmapSource: ...
    def Release(self, ) -> None: ...

class CommandStack:
    """.NET: Autodesk.AutoCAD.Windows.Data.CommandStack"""
    def __init__(self, *args) -> None: ...
    AllCommands: str
    MainCommand: str
    def ContainsAny(self, commands: list) -> bool: ...
    def ContainsOnly(self, commands: list) -> bool: ...
    def Dispose(self, ) -> None: ...

class Commands3DPrint:
    """.NET: Autodesk.AutoCAD.Windows.Data.Commands3DPrint"""
    def __init__(self, *args) -> None: ...
    IsPrintStudioAvailable: bool

class CommonProperties(WrapICustomTypeDescriptor):
    """.NET: Autodesk.AutoCAD.Windows.Data.CommonProperties"""
    def __init__(self, *args) -> None: ...
    Item: CommonProperty
    RequireRegisteredTypes: Nullable
    def ContainsAny(self, properties: list) -> bool: ...
    def Dispose(self, ) -> None: ...
    def GetConverterFromRegisteredType(self, ) -> TypeConverter: ...
    def GetEventsFromRegisteredType(self, ) -> EventDescriptorCollection: ...
    def GetPropertiesFromRegisteredType(self, ) -> PropertyDescriptorCollection: ...
    def PreviewEnded(self, sender: object, e: LivePreviewEventArgs) -> None: ...

class CommonProperty(PropertyDescriptor):
    """.NET: Autodesk.AutoCAD.Windows.Data.CommonProperty"""
    def __init__(self, *args) -> None: ...
    TrueValues: TrueValues
    SupportsChangeEvents: bool
    PropertyType: Type
    ComponentType: Type
    IsReadOnly: bool
    Converter: TypeConverter
    ConverterFromRegisteredType: TypeConverter
    IsLocalizable: bool
    SerializationVisibility: DesignerSerializationVisibility
    Attributes: AttributeCollection
    Category: str
    Description: str
    IsBrowsable: bool
    Name: str
    DesignTimeOnly: bool
    DisplayName: str
    def CanResetValue(self, component: object) -> bool: ...
    def Dispose(self, ) -> None: ...
    def GetValue(self, component: object) -> object: ...
    def ResetValue(self, component: object) -> None: ...
    def SetValue(self, component: object, value: object) -> None: ...
    def ShouldSerializeValue(self, component: object) -> bool: ...

class CompositeConverter:
    """.NET: Autodesk.AutoCAD.Windows.Data.CompositeConverter"""
    def __init__(self, *args) -> None: ...
    Converters: List
    def Convert(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...
    def ConvertBack(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...

class DataBindings:
    """.NET: Autodesk.AutoCAD.Windows.Data.DataBindings"""
    def __init__(self, *args) -> None: ...
    DoNothing: object
    BlockDialogModelInsert: BlockDialogModelInsert
    Commands3DPrint: Commands3DPrint
    ArrayCreation: object
    ColorSettings: ILookup
    CommandEditorManager: CommandEditorManager
    Views2DCommands: Views2DCommands
    Workspaces: WorkspaceCollection
    ThemeEngine: ThemeEngine
    HatchCommands: HatchCommands
    EffectivePropertySource: EffectivePropertySource
    EplotExport: EplotExport
    CurrentViewport: object
    LightEngine: LightEngine
    RenderEngine: RenderEngine
    AnimationEditor: AnimationEditor
    SysvarMonitorState: SysvarMonitorState
    IsoDraft: IsoDraft
    GeoData: GeoData
    BlockEditor: BlockEditor
    ViewportsCommands: ILookup
    TextSize: TextSize
    InplaceTextEditor: InplaceTextEditor
    ActiveCommands: CommandStack
    Commands: ILookup
    NativeFunctions: ILookup
    SystemVariables: ILookup
    Collections: DataItemCollections
    def Dispose(self, ) -> None: ...
    def GetLocalColorName(self, acadColor: Color) -> str: ...
    def Refresh(self, ) -> None: ...

class DataItemCollection:
    """.NET: Autodesk.AutoCAD.Windows.Data.DataItemCollection"""
    def __init__(self, *args) -> None: ...
    IsReadOnly: bool
    Item: ICustomTypeDescriptor
    Count: int
    Active: bool
    CurrentItem: ICustomTypeDescriptor
    def Dispose(self, ) -> None: ...
    def InvalidateProperty(self, propertyName: str) -> None: ...

class DataItemCollections:
    """.NET: Autodesk.AutoCAD.Windows.Data.DataItemCollections"""
    def __init__(self, *args) -> None: ...
    RecentBlocks: DataItemCollection
    Blocks: DataItemCollection
    UcsPlanes: DataItemCollection
    PlotStyles: DataItemCollection
    Colors: ColorCollection
    UIFontInfoCollection: IList
    Lineweights: EnumItemCollection
    Item: DataItemCollection
    RenderPresets: DataItemCollection
    TableCellStyles: DataItemCollection
    Selection: Selection
    NamedViews: DataItemCollection
    NamedModelViews: DataItemCollection
    Linetypes: DataItemCollection
    LayerFilters: DataItemCollection
    LayerStates: DataItemCollection
    Layers: DataItemCollection
    PointCloudClassificationSchemes: DataItemCollection
    PointCloudColorSchemes: DataItemCollection
    PointClouds: DataItemCollection
    VisualStyles: DataItemCollection
    TextStyles: DataItemCollection
    DimensionStyles: DataItemCollection
    DetailViewStyles: DataItemCollection
    SectionViewStyles: DataItemCollection
    MleaderStyles: DataItemCollection
    TableStyles: DataItemCollection
    def Dispose(self, ) -> None: ...

class DataItemFactoryMethod:
    """.NET: Autodesk.AutoCAD.Windows.Data.DataItemFactoryMethod"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, objId: FullSubentityPath, wrapper: object, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> DataItem: ...
    def Invoke(self, objId: FullSubentityPath, wrapper: object) -> DataItem: ...

class DbObjectCollection(DataItemCollection):
    """.NET: Autodesk.AutoCAD.Windows.Data.DbObjectCollection"""
    def __init__(self, *args) -> None: ...
    IsReadOnly: bool
    Item: ICustomTypeDescriptor
    Count: int
    Active: bool
    CurrentItem: ICustomTypeDescriptor

class DefinedSymbolsCommand(IPECommandBase):
    """.NET: Autodesk.AutoCAD.Windows.Data.DefinedSymbolsCommand"""
    def __init__(self, *args) -> None: ...
    def Execute(self, parameter: object) -> None: ...

class DisposingEventHandler:
    """.NET: Autodesk.AutoCAD.Windows.Data.DisposingEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: EventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: EventArgs) -> None: ...

class DoubleToStringConverter:
    """.NET: Autodesk.AutoCAD.Windows.Data.DoubleToStringConverter"""
    def __init__(self, *args) -> None: ...
    DefaultValue: float
    def Convert(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...
    def ConvertBack(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...

class EffectiveProperties(WrapICustomTypeDescriptor):
    """.NET: Autodesk.AutoCAD.Windows.Data.EffectiveProperties"""
    def __init__(self, *args) -> None: ...
    Item: EffectiveProperty
    RequireRegisteredTypes: Nullable
    def GetConverterFromRegisteredType(self, ) -> TypeConverter: ...
    def GetEventsFromRegisteredType(self, ) -> EventDescriptorCollection: ...
    def GetPropertiesFromRegisteredType(self, ) -> PropertyDescriptorCollection: ...
    def Invalidate(self, propertyName: str) -> None: ...
    def InvalidateProperty(self, propertyName: str) -> None: ...

class EffectiveProperty(PropertyDescriptor):
    """.NET: Autodesk.AutoCAD.Windows.Data.EffectiveProperty"""
    def __init__(self, *args) -> None: ...
    TrueValues: TrueValues
    SupportsChangeEvents: bool
    PropertyType: Type
    ComponentType: Type
    IsReadOnly: bool
    Converter: TypeConverter
    ConverterFromRegisteredType: TypeConverter
    IsLocalizable: bool
    SerializationVisibility: DesignerSerializationVisibility
    Attributes: AttributeCollection
    Category: str
    Description: str
    IsBrowsable: bool
    Name: str
    DesignTimeOnly: bool
    DisplayName: str
    def CanResetValue(self, component: object) -> bool: ...
    def GetValue(self, component: object) -> object: ...
    def ResetValue(self, component: object) -> None: ...
    def SetValue(self, component: object, value: object) -> None: ...
    def ShouldSerializeValue(self, component: object) -> bool: ...

class EffectivePropertySource:
    """.NET: Autodesk.AutoCAD.Windows.Data.EffectivePropertySource"""
    def __init__(self, *args) -> None: ...
    EffectiveProperties: EffectiveProperties
    def Dispose(self, ) -> None: ...

class EnumItemCollection:
    """.NET: Autodesk.AutoCAD.Windows.Data.EnumItemCollection"""
    def __init__(self, *args) -> None: ...
    IsReadOnly: bool
    Item: ICustomTypeDescriptor
    Count: int
    CurrentItem: ICustomTypeDescriptor
    def Dispose(self, ) -> None: ...
    def InvalidateProperty(self, propertyName: str) -> None: ...

class EnumSubsetConverter:
    """.NET: Autodesk.AutoCAD.Windows.Data.EnumSubsetConverter"""
    def __init__(self, *args) -> None: ...
    def Convert(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...
    def ConvertBack(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...

class EplotExport:
    """.NET: Autodesk.AutoCAD.Windows.Data.EplotExport"""
    def __init__(self, *args) -> None: ...
    EnableWindowBtn: bool
    EnablePageSetupBtn: bool
    CurrentItemPageSetup: str
    CurrentItemExport: str
    PageSetupSet: ObservableCollection
    ExportSet: ObservableCollection
    def Dispose(self, ) -> None: ...
    def UpdateCurrentItemExport(self, ) -> None: ...

class Expression:
    """.NET: Autodesk.AutoCAD.Windows.Data.Expression"""
    def __init__(self, *args) -> None: ...
    Value: object
    Text: str

class ExtendedPropertyEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.Windows.Data.ExtendedPropertyEventArgs"""
    def __init__(self, *args) -> None: ...
    DataItemType: str
    DataItem: ICustomTypeDescriptor
    PropertyName: str
    PropertyDesc: PropertyDescriptor

class ExtendedPropertyEventHandler:
    """.NET: Autodesk.AutoCAD.Windows.Data.ExtendedPropertyEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: ExtendedPropertyEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: ExtendedPropertyEventArgs) -> None: ...

class ExtendedPropertyManager:
    """.NET: Autodesk.AutoCAD.Windows.Data.ExtendedPropertyManager"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def TryGetExtendedProperty(propertyName: str, dataItem: ICustomTypeDescriptor, dataItemType: str) -> PropertyDescriptor: ...

class FieldDialogCommand(IPECommandBase):
    """.NET: Autodesk.AutoCAD.Windows.Data.FieldDialogCommand"""
    def __init__(self, *args) -> None: ...
    def Execute(self, parameter: object) -> None: ...

class FindReplaceCommand(IPECommandBase):
    """.NET: Autodesk.AutoCAD.Windows.Data.FindReplaceCommand"""
    def __init__(self, *args) -> None: ...
    def Execute(self, parameter: object) -> None: ...

class FindTextCommand(IPECommandBase):
    """.NET: Autodesk.AutoCAD.Windows.Data.FindTextCommand"""
    def __init__(self, *args) -> None: ...
    def Dispose(self, ) -> None: ...
    def Execute(self, parameter: object) -> None: ...

class GeoData:
    """.NET: Autodesk.AutoCAD.Windows.Data.GeoData"""
    def __init__(self, *args) -> None: ...
    IsGeomapImageUpdateAllowed: ValueType
    IsSnapShotAllowed: ValueType
    IsGeoCsSupported: ValueType
    IsMyGeoDataAvailable: ValueType
    IsMyLocationAvaliable: ValueType
    Instance: GeoData
    def Dispose(self, ) -> None: ...

class HatchCommands:
    """.NET: Autodesk.AutoCAD.Windows.Data.HatchCommands"""
    def __init__(self, *args) -> None: ...
    IsHatchCreation: bool
    HasDefinedBoundaries: bool
    LaunchDialog: ICommand
    MatchProperties: ICommand
    SetOrigin: ICommand
    RecreateBoundaries: ICommand
    RemoveBoundaries: ICommand
    SelectObjects: ICommand
    PickPoints: ICommand
    def Dispose(self, ) -> None: ...

class HatchPatterns:
    """.NET: Autodesk.AutoCAD.Windows.Data.HatchPatterns"""
    def __init__(self, *args) -> None: ...
    IsUnknownPatternSelected: bool
    AllPatterns: ObservableCollection
    UserDefinedPattern: str
    UnknownPatterns: ObservableCollection
    CustomPatterns: ObservableCollection
    GradientPatterns: ObservableCollection
    PredefinedOtherPatterns: ObservableCollection
    PredefinedISOPatterns: ObservableCollection
    PredefinedANSIPatterns: ObservableCollection
    PredefinedPatterns: ObservableCollection
    Instance: HatchPatterns
    def AppendUnknownPattern(self, unknownPattern: str) -> bool: ...
    def Dispose(self, ) -> None: ...
    @staticmethod
    def GetCustomSwatchImage(name: str, patternColor: Color, backgroundColor: Color, nWidth: int, nHeight: int) -> IntPtr: ...
    @staticmethod
    def GetGradientSwatchImage(name: str, angle: float, bShifted: bool, startColor: Color, stopColor: Color, nWidth: int, nHeight: int) -> IntPtr: ...
    @staticmethod
    def GetPatternSwatchImage(name: str, patternColor: Color, backgroundColor: Color, nWidth: int, nHeight: int) -> IntPtr: ...
    @staticmethod
    def ValidPatternName(patternName: str) -> PatPatternCategory: ...

class HatchRibbonItem(RibbonItem):
    """.NET: Autodesk.AutoCAD.Windows.Data.HatchRibbonItem"""
    def __init__(self, *args) -> None: ...
    IsEnabled: bool
    Id: str
    AutomationName: str
    Text: str
    TextBinding: BindingBase
    TextOverride: str
    Name: str
    Description: str
    GroupName: str
    Highlight: HighlightMode
    Image: ImageSource
    ImageBinding: BindingBase
    LargeImage: ImageSource
    LargeImageBinding: BindingBase
    Tag: object
    ShowText: bool
    ShowImage: bool
    ToolTip: object
    ToolTipOverride: object
    IsUsingDefaultToolTip: bool
    ToolTipResolver: object
    HelpSource: Uri
    HelpTopic: str
    IsToolTipEnabled: bool
    ShowToolTipOnDisabled: bool
    KeyTip: str
    UID: str
    IsVisible: bool
    IsEnabledBinding: BindingBase
    IsVisibleBinding: BindingBase
    MinWidth: float
    Width: float
    MinHeight: float
    MaxHeight: float
    Height: float
    CanResizeWidth: bool
    CanResizeHeightWithGrip: bool
    SupportedSubPanel: RibbonSupportedSubPanelStyle
    ResizeStyle: RibbonItemResizeStyles
    Size: RibbonItemSize
    AllowInToolBar: bool
    AllowInStatusBar: bool
    IsInitialized: bool
    Cookie: str
    GroupLocation: RibbonItemGroupLocation
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToString(self, ) -> str: ...

class IDataItem:
    """.NET: Autodesk.AutoCAD.Windows.Data.IDataItem"""
    def __init__(self, *args) -> None: ...
    ObjectId: ObjectId
    def StartTransaction(self, mode: OpenMode) -> IDataItemTransaction: ...

class IDataItemTransaction:
    """.NET: Autodesk.AutoCAD.Windows.Data.IDataItemTransaction"""
    def __init__(self, *args) -> None: ...
    Item: object
    def Commit(self, ) -> None: ...

class IInvalidateProperty:
    """.NET: Autodesk.AutoCAD.Windows.Data.IInvalidateProperty"""
    def __init__(self, *args) -> None: ...
    def InvalidateProperty(self, propertyName: str) -> None: ...

class ILookup:
    """.NET: Autodesk.AutoCAD.Windows.Data.ILookup`1"""
    def __init__(self, *args) -> None: ...
    Item: T

class INamedImageProvider:
    """.NET: Autodesk.AutoCAD.Windows.Data.INamedImageProvider"""
    def __init__(self, *args) -> None: ...
    def GetNamedImage(self, objectName: str) -> ImageSource: ...

class INamedValue:
    """.NET: Autodesk.AutoCAD.Windows.Data.INamedValue"""
    def __init__(self, *args) -> None: ...
    Value: object
    Name: str

class INotifyCollectionItemsChanged:
    """.NET: Autodesk.AutoCAD.Windows.Data.INotifyCollectionItemsChanged"""
    def __init__(self, *args) -> None: ...
    ...

class IPEAttachmentPoint:
    """.NET enum: Autodesk.AutoCAD.Windows.Data.IPEAttachmentPoint"""
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
class IPEColumnType:
    """.NET enum: Autodesk.AutoCAD.Windows.Data.IPEColumnType"""
    def __init__(self, *args) -> None: ...
    NoColumns: int  # = 0
    StaticColumns: int  # = 1
    DynamicColumns: int  # = 2
class IPECommandBase:
    """.NET: Autodesk.AutoCAD.Windows.Data.IPECommandBase"""
    def __init__(self, *args) -> None: ...
    def CanExecute(self, parameter: object) -> bool: ...
    def Execute(self, parameter: object) -> None: ...
    def SetCanExecute(self, value: bool) -> None: ...

class IPEDynamicColumnType:
    """.NET enum: Autodesk.AutoCAD.Windows.Data.IPEDynamicColumnType"""
    def __init__(self, *args) -> None: ...
    DynamicAutoHeight: int  # = 0
    DynamicManualHeight: int  # = 1
class IPEEditorSettings:
    """.NET enum: Autodesk.AutoCAD.Windows.Data.IPEEditorSettings"""
    def __init__(self, *args) -> None: ...
    AlwaysDisplayWysiwyg: int  # = 0
    ShowToolbar: int  # = 1
    ShowRuler: int  # = 2
    OpaqueBackground: int  # = 3
    CheckSpelling: int  # = 4
class IPEFlowAlignmentType:
    """.NET enum: Autodesk.AutoCAD.Windows.Data.IPEFlowAlignmentType"""
    def __init__(self, *args) -> None: ...
    FlowBase: int  # = 0
    FlowCenter: int  # = 1
    FlowTop: int  # = 2
class IPENumberingType:
    """.NET enum: Autodesk.AutoCAD.Windows.Data.IPENumberingType"""
    def __init__(self, *args) -> None: ...
    NumberingOff: int  # = 0
    NumberingBullet: int  # = 1
    NumberingNumber: int  # = 2
    NumberingLetterLower: int  # = 3
    NumberingLetterUpper: int  # = 4
    NumberingLettered: int  # = 5
class IPENumberingTypeEnumConverter(EnumConverter):
    """.NET: Autodesk.AutoCAD.Windows.Data.IPENumberingTypeEnumConverter"""
    def __init__(self, *args) -> None: ...
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool: ...
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object: ...
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object: ...

class IPEParagraphAlignmentType:
    """.NET enum: Autodesk.AutoCAD.Windows.Data.IPEParagraphAlignmentType"""
    def __init__(self, *args) -> None: ...
    AlignmentDefault: int  # = 0
    AlignmentLeft: int  # = 1
    AlignmentCenter: int  # = 2
    AlignmentRight: int  # = 3
    AlignmentJustify: int  # = 4
    AlignmentDistribute: int  # = 5
    NumAlignmentTypes: int  # = 6
class IPEStaticColumnType:
    """.NET enum: Autodesk.AutoCAD.Windows.Data.IPEStaticColumnType"""
    def __init__(self, *args) -> None: ...
    OneColumn: int  # = 1
    TwoColumns: int  # = 2
    ThreeColumns: int  # = 3
    FourColumns: int  # = 4
    FiveColumns: int  # = 5
    SixColumns: int  # = 6
class ImportCommand(IPECommandBase):
    """.NET: Autodesk.AutoCAD.Windows.Data.ImportCommand"""
    def __init__(self, *args) -> None: ...
    def Execute(self, parameter: object) -> None: ...

class InplaceTextEditor:
    """.NET: Autodesk.AutoCAD.Windows.Data.InplaceTextEditor"""
    def __init__(self, *args) -> None: ...
    Superscript: bool
    Subscript: bool
    Scriptable: bool
    IsMatchPropertiesState: bool
    IsActive: bool
    StaticColumnsList: Collection
    IsColumnsEnabled: bool
    LineSpacingFactors: Collection
    LineSpacingFactor: float
    IsLineSpacingFactorAvailable: bool
    FontSizes: ObservableCollection
    Color: Color
    TextStyle: object
    TextHeight: object
    WidthScale: float
    ObliqueAngle: float
    TrackingFactor: float
    FlowAlignment: IPEFlowAlignmentType
    LineSpacingType: LineSpacingTypes
    NumberingType: IPENumberingType
    AttachmentPointType: IPEAttachmentPoint
    LanguageIndexType: int
    StaticColumnType: IPEStaticColumnType
    DynamicColumnType: IPEDynamicColumnType
    ColumnType: IPEColumnType
    ParagraphAlignment: IPEParagraphAlignmentType
    IsParagraphAlignmentAvailable: bool
    CurrentLayer: str
    CurrentFont: UIFontInfo
    IsWysiwyg: bool
    HaveSelection: bool
    IsChangeCaseAvailable: bool
    IsTabOnlyDelimiterEnabled: bool
    IsAutoListEnabled: bool
    NumberingAvailable: bool
    Stacked: bool
    IsStackOrUnstackEnabled: bool
    AutoCAPS: bool
    IsRedoEnabled: bool
    IsUndoEnabled: bool
    InsertField: bool
    IsInsertFieldEnabled: bool
    InsertColumnBreak: bool
    IsInsertColumnBreak: bool
    OpaqueBackground: bool
    IsOpaqueBackgroundEnabled: bool
    ShowToolbar: bool
    IsShowToolbarEnabled: bool
    Ruler: bool
    IsRulerChecked: bool
    IsRulerEnabled: bool
    Speller: bool
    IsSpellerEnabled: bool
    Annotative: bool
    IsAnnotativeEnabled: bool
    StrikeThrough: bool
    IsStrikeThroughEnabled: bool
    Overline: bool
    IsOverlineEnabled: bool
    Underline: bool
    IsUnderlineEnabled: bool
    Italic: bool
    IsItalicEnabled: bool
    Bold: bool
    IsBoldEnabled: bool
    QuickFindText: ICommand
    Undo: ICommand
    Redo: ICommand
    ColumnsSettingsDialog: ICommand
    Lowercase: ICommand
    Uppercase: ICommand
    BackgroundMask: ICommand
    Options: ICommand
    CharacterSet: ICommand
    ParagraphAlignmentOpions: ICommand
    StaticColumns: ICommand
    Numbering: ICommand
    AttachmentPoint: ICommand
    DefinedSymbols: ICommand
    MoreLineSpace: ICommand
    ClearLineSpace: ICommand
    LineSpacingMultiples: ICommand
    ParagraphDialog: ICommand
    FieldDialog: ICommand
    Close: ICommand
    Import: ICommand
    FindReplace: ICommand
    def Dispose(self, ) -> None: ...

class InputBuffer:
    """.NET: Autodesk.AutoCAD.Windows.Data.InputBuffer"""
    def __init__(self, *args) -> None: ...
    HasSelection: bool
    SelectPosition: int
    Position: int
    Text: str
    def ExecuteKeyword(self, keyword: str) -> bool: ...
    def IsPromptingForCommandName(self, ) -> bool: ...
    def OnCharQueue(self, inputChar: int, repCnt: int, flags: int) -> bool: ...
    def OnKeyDownQueue(self, inputChar: int, repCnt: int, flags: int) -> bool: ...
    def OnSetSelectedTextQueue(self, start: int, end: int) -> bool: ...
    def OnSysKeyDownQueue(self, inputChar: int, repCnt: int, flags: int) -> bool: ...
    def ParseKeywordForExecute(self, keyword: str) -> str: ...
    def PasteString(self, originalString: str, stringToPaste: str) -> None: ...
    def ReplaceInputQueue(self, newInput: str) -> None: ...

class InputSearchOptions:
    """.NET enum: Autodesk.AutoCAD.Windows.Data.InputSearchOptions"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    AutoComplete: int  # = 1
    AutoCorrect: int  # = 2
    SysvarSearch: int  # = 4
    ContentSearch: int  # = 8
    MidString: int  # = 16
class Int32ToImageConverter:
    """.NET: Autodesk.AutoCAD.Windows.Data.Int32ToImageConverter"""
    def __init__(self, *args) -> None: ...
    Images: List
    def Convert(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...
    def ConvertBack(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...

class IsoDraft:
    """.NET: Autodesk.AutoCAD.Windows.Data.IsoDraft"""
    def __init__(self, *args) -> None: ...
    State: int
    def Dispose(self, ) -> None: ...

class LayerFilterCollection(NamedObjectCollection):
    """.NET: Autodesk.AutoCAD.Windows.Data.LayerFilterCollection"""
    def __init__(self, *args) -> None: ...
    IsReadOnly: bool
    Item: ICustomTypeDescriptor
    Count: int
    Active: bool
    CurrentItem: ICustomTypeDescriptor

class LayerRecordCollection(DbObjectCollection):
    """.NET: Autodesk.AutoCAD.Windows.Data.LayerRecordCollection"""
    def __init__(self, *args) -> None: ...
    IsReadOnly: bool
    Item: ICustomTypeDescriptor
    Count: int
    Active: bool
    CurrentItem: ICustomTypeDescriptor

class LightEngine:
    """.NET: Autodesk.AutoCAD.Windows.Data.LightEngine"""
    def __init__(self, *args) -> None: ...
    IsDateTimeEnabled: bool
    Time: float
    Date: float
    DateTicks: DoubleCollection
    MaxTime: float
    MinTime: float
    MaxDate: float
    MinDate: float
    IsUsingGenericLightingUnits: bool
    def Dispose(self, ) -> None: ...

class LineSpacingMultiplesCommand(IPECommandBase):
    """.NET: Autodesk.AutoCAD.Windows.Data.LineSpacingMultiplesCommand"""
    def __init__(self, *args) -> None: ...
    def Execute(self, parameter: object) -> None: ...

class LineSpacingTypes:
    """.NET enum: Autodesk.AutoCAD.Windows.Data.LineSpacingTypes"""
    def __init__(self, *args) -> None: ...
    LineSpacingExactly: int  # = 1
    LineSpacingAtLeast: int  # = 2
    LineSpacingMultiple: int  # = 3
class LineSpacingTypesEnumConverter(EnumConverter):
    """.NET: Autodesk.AutoCAD.Windows.Data.LineSpacingTypesEnumConverter"""
    def __init__(self, *args) -> None: ...
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool: ...
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object: ...
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object: ...

class LineWeightCollection(EnumItemCollection):
    """.NET: Autodesk.AutoCAD.Windows.Data.LineWeightCollection"""
    def __init__(self, *args) -> None: ...
    IsReadOnly: bool
    Item: ICustomTypeDescriptor
    Count: int
    CurrentItem: ICustomTypeDescriptor

class LowercaseCommand(IPECommandBase):
    """.NET: Autodesk.AutoCAD.Windows.Data.LowercaseCommand"""
    def __init__(self, *args) -> None: ...
    def Execute(self, parameter: object) -> None: ...

class MoreLineSpaceCommand(IPECommandBase):
    """.NET: Autodesk.AutoCAD.Windows.Data.MoreLineSpaceCommand"""
    def __init__(self, *args) -> None: ...
    def Execute(self, parameter: object) -> None: ...

class MultiReplaceConverter:
    """.NET: Autodesk.AutoCAD.Windows.Data.MultiReplaceConverter"""
    def __init__(self, *args) -> None: ...
    DefaultConverter: IValueConverter
    Filters: List
    def Convert(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...
    def ConvertBack(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...

class NamedImageProvider:
    """.NET: Autodesk.AutoCAD.Windows.Data.NamedImageProvider"""
    def __init__(self, *args) -> None: ...
    ImageProvider: INamedImageProvider
    def Convert(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...
    def ConvertBack(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...

class NamedObjectCollection(DataItemCollection):
    """.NET: Autodesk.AutoCAD.Windows.Data.NamedObjectCollection"""
    def __init__(self, *args) -> None: ...
    IsReadOnly: bool
    Item: ICustomTypeDescriptor
    Count: int
    Active: bool
    CurrentItem: ICustomTypeDescriptor

class NativeFunction:
    """.NET: Autodesk.AutoCAD.Windows.Data.NativeFunction"""
    def __init__(self, *args) -> None: ...
    def CanExecute(self, parameter: object) -> bool: ...
    def Dispose(self, ) -> None: ...
    def Execute(self, parameter: object) -> None: ...

class NavStatus:
    """.NET enum: Autodesk.AutoCAD.Windows.Data.NavStatus"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Paused: int  # = 1
    Recording: int  # = 2
    Default: int  # = 4
class NotifyCollectionItemsChangedEventArgs(EventArgs):
    """.NET: Autodesk.AutoCAD.Windows.Data.NotifyCollectionItemsChangedEventArgs"""
    def __init__(self, *args) -> None: ...
    Items: IList

class NotifyCollectionItemsChangedEventHandler:
    """.NET: Autodesk.AutoCAD.Windows.Data.NotifyCollectionItemsChangedEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, sender: object, e: NotifyCollectionItemsChangedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: object, e: NotifyCollectionItemsChangedEventArgs) -> None: ...

class NullToVariesConverter:
    """.NET: Autodesk.AutoCAD.Windows.Data.NullToVariesConverter"""
    def __init__(self, *args) -> None: ...
    def Convert(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...
    def ConvertBack(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...

class NumberingCommand(IPECommandBase):
    """.NET: Autodesk.AutoCAD.Windows.Data.NumberingCommand"""
    def __init__(self, *args) -> None: ...
    def Execute(self, parameter: object) -> None: ...

class OptionsCommand(IPECommandBase):
    """.NET: Autodesk.AutoCAD.Windows.Data.OptionsCommand"""
    def __init__(self, *args) -> None: ...
    def Execute(self, parameter: object) -> None: ...

class ParagraphAlignmentOpionsCommand(IPECommandBase):
    """.NET: Autodesk.AutoCAD.Windows.Data.ParagraphAlignmentOpionsCommand"""
    def __init__(self, *args) -> None: ...
    def Execute(self, parameter: object) -> None: ...

class ParagraphDialogCommand(IPECommandBase):
    """.NET: Autodesk.AutoCAD.Windows.Data.ParagraphDialogCommand"""
    def __init__(self, *args) -> None: ...
    def Execute(self, parameter: object) -> None: ...

class PatPatternCategory:
    """.NET enum: Autodesk.AutoCAD.Windows.Data.PatPatternCategory"""
    def __init__(self, *args) -> None: ...
    kPredef: int  # = 0
    kUserdef: int  # = 1
    kCustomdef: int  # = 2
    kSolid_fill: int  # = 3
    kISOdef: int  # = 4
    kInvalid: int  # = -1
class PlotStyleCollection(DbObjectCollection):
    """.NET: Autodesk.AutoCAD.Windows.Data.PlotStyleCollection"""
    def __init__(self, *args) -> None: ...
    IsReadOnly: bool
    Item: ICustomTypeDescriptor
    Count: int
    Active: bool
    CurrentItem: ICustomTypeDescriptor

class PlotStyleNameToDataItemConverter:
    """.NET: Autodesk.AutoCAD.Windows.Data.PlotStyleNameToDataItemConverter"""
    def __init__(self, *args) -> None: ...
    def Convert(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...
    def ConvertBack(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...

class PromptAndInput:
    """.NET: Autodesk.AutoCAD.Windows.Data.PromptAndInput"""
    def __init__(self, *args) -> None: ...
    SelectPosition: int
    Position: int
    PromptDefault: str
    PromptKeywords: ObservableCollection
    KeywordsStringLength: int
    KeywordsStringStart: int
    Prompt: str
    Text: str
    InputBuffer: InputBuffer

class RedoCommand(IPECommandBase):
    """.NET: Autodesk.AutoCAD.Windows.Data.RedoCommand"""
    def __init__(self, *args) -> None: ...
    def Execute(self, parameter: object) -> None: ...

class ReplaceConverter:
    """.NET: Autodesk.AutoCAD.Windows.Data.ReplaceConverter"""
    def __init__(self, *args) -> None: ...
    Converter: IValueConverter
    TargetValue: object
    SourceValue: object
    def Convert(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...
    def ConvertBack(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...

class Selection(DbObjectCollection):
    """.NET: Autodesk.AutoCAD.Windows.Data.Selection"""
    def __init__(self, *args) -> None: ...
    CommonProperties: CommonProperties
    IsContinuing: bool
    IsReadOnly: bool
    Item: ICustomTypeDescriptor
    Count: int
    Active: bool
    CurrentItem: ICustomTypeDescriptor
    def ContainsAny(self, types: list) -> bool: ...
    def ContainsAnyDrawingView(self, ) -> bool: ...
    def ContainsOnly(self, types: list) -> bool: ...
    def ContainsOnlyCenterTypeEntities(self, ) -> bool: ...
    def ContainsOnlyCoordinationModel(self, ) -> bool: ...
    def ContainsOnlyDrawingView(self, ) -> bool: ...
    def ContainsOnlyGeoMapImage(self, ) -> bool: ...
    def ContainsOnlyRevcloudEntities(self, ) -> bool: ...
    def ContainsOnlyTrace(self, ) -> bool: ...
    def RemoveNonEditableObjects(self, type: NonEditableType) -> int: ...
    def isContainSectionViewHatch(self, ) -> bool: ...
    def isOnlySectionViewHatchs(self, ) -> bool: ...

class SourceToTypeConverter:
    """.NET: Autodesk.AutoCAD.Windows.Data.SourceToTypeConverter"""
    def __init__(self, *args) -> None: ...
    ConverterType: Type
    SourceType: Type
    def Convert(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...
    def ConvertBack(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...

class StandardConverter:
    """.NET: Autodesk.AutoCAD.Windows.Data.StandardConverter"""
    def __init__(self, *args) -> None: ...
    TargetType: Type
    SourceType: Type
    def Convert(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...
    def ConvertBack(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...

class StandardUcsPlane:
    """.NET: Autodesk.AutoCAD.Windows.Data.StandardUcsPlane"""
    def __init__(self, *args) -> None: ...
    Unnamed: object
    World: object
    Back: object
    Front: object
    Right: object
    Left: object
    Bottom: object
    Top: object

class StaticColumnsCommand(IPECommandBase):
    """.NET: Autodesk.AutoCAD.Windows.Data.StaticColumnsCommand"""
    def __init__(self, *args) -> None: ...
    def Execute(self, parameter: object) -> None: ...

class SubEntity:
    """.NET: Autodesk.AutoCAD.Windows.Data.SubEntity"""
    def __init__(self, *args) -> None: ...
    ParentType: Type
    @staticmethod
    def Create(path: FullSubentityPath) -> SubEntity: ...
    def Dispose(self, ) -> None: ...

class SystemVariable:
    """.NET: Autodesk.AutoCAD.Windows.Data.SystemVariable"""
    def __init__(self, *args) -> None: ...
    Name: str
    ValueType: Type
    Maximum: float
    Minimum: float
    IsEnabled: bool
    MutedValue: object
    Value: object
    TrueValues: TrueValues
    def Dispose(self, ) -> None: ...

class SysvarMonitorState:
    """.NET: Autodesk.AutoCAD.Windows.Data.SysvarMonitorState"""
    def __init__(self, *args) -> None: ...
    ShowBalloon: bool
    DifferenceNumber: int
    HasDifference: bool
    def Dispose(self, ) -> None: ...
    def ShowDialog(self, ) -> None: ...
    def SyncState(self, ) -> None: ...

class TextSize:
    """.NET: Autodesk.AutoCAD.Windows.Data.TextSize"""
    def __init__(self, *args) -> None: ...
    FontSizes: ObservableCollection
    TextHeight: object
    def Dispose(self, ) -> None: ...

class ThemeEngine:
    """.NET: Autodesk.AutoCAD.Windows.Data.ThemeEngine"""
    def __init__(self, *args) -> None: ...
    Brightness: float
    Saturation: float
    Hue: float
    def Dispose(self, ) -> None: ...

class TransparencyItem:
    """.NET: Autodesk.AutoCAD.Windows.Data.TransparencyItem"""
    def __init__(self, *args) -> None: ...
    LayerValue: int
    ErrorText: str
    Transparency: Transparency

class TrueValues:
    """.NET: Autodesk.AutoCAD.Windows.Data.TrueValues"""
    def __init__(self, *args) -> None: ...
    HPBACKGROUNDCOLOR: str
    HPCOLOR: str
    StringValue: str
    AcadColor: Color

class UIFontInfo:
    """.NET: Autodesk.AutoCAD.Windows.Data.UIFontInfo"""
    def __init__(self, *args) -> None: ...
    IsTrueType: bool
    Name: str
    @staticmethod
    def GetFontInfo(fontName: str) -> UIFontInfo: ...
    @staticmethod
    def GetFontInfoCollection() -> Collection: ...

class UndoCommand(IPECommandBase):
    """.NET: Autodesk.AutoCAD.Windows.Data.UndoCommand"""
    def __init__(self, *args) -> None: ...
    def Execute(self, parameter: object) -> None: ...

class UppercaseCommand(IPECommandBase):
    """.NET: Autodesk.AutoCAD.Windows.Data.UppercaseCommand"""
    def __init__(self, *args) -> None: ...
    def Execute(self, parameter: object) -> None: ...

class ValueToNamedValueConverter:
    """.NET: Autodesk.AutoCAD.Windows.Data.ValueToNamedValueConverter"""
    def __init__(self, *args) -> None: ...
    def Convert(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...
    def ConvertBack(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...

class View2DRibbonItemData:
    """.NET: Autodesk.AutoCAD.Windows.Data.View2DRibbonItemData"""
    def __init__(self, *args) -> None: ...
    Key: str
    Text: str
    def Dispose(self, ) -> None: ...

class Views2DCommands:
    """.NET: Autodesk.AutoCAD.Windows.Data.Views2DCommands"""
    def __init__(self, *args) -> None: ...
    IsSynergyObjServiceRegistered: bool
    IsEmptyMS: int
    IsEnableReturn: bool
    IsEnableGradientPatern: bool
    JaggedRbt: bool
    SmoothWCRbt: bool
    SmoothWBRbt: bool
    SmoothRbt: bool
    IsEnabledModelEdgeRbt: bool
    RectangularRbt: bool
    CircularRbt: bool
    IsEnabledBoundaryRbt: bool
    AutoUpdate: bool
    IsEnabledAutoUpdate: bool
    ShowHatch: bool
    IsEnabledShowHatch: bool
    SViewLabel: bool
    IsEnabledSViewLabel: bool
    Identifier: str
    IsEnabledIdentifier: bool
    Depth: float
    IsEnabledDepth: bool
    IsEnabledDepthDrag: bool
    DepthTypeList: ObservableCollection
    DepthType: object
    IsEnabledDepthType: bool
    ProjectionViewList: ObservableCollection
    ProjectionView: object
    IsEnabledProjectionView: bool
    StyleObject: RibbonListButton
    IsEnabledSelect: bool
    IsEnabledOption: bool
    IsEnabledMove: bool
    DeferUpdate: bool
    IsEnabledDeferUpdate: bool
    IsEnabledCancel: bool
    IsEnabledAccept: bool
    OrientationList: ObservableCollection
    Orientation: object
    IsEnabledOrientation: bool
    MemberList: ObservableCollection
    Member: object
    IsEnabledMember: bool
    SheetMetalList: ObservableCollection
    SheetMetal: object
    IsEnabledSheetMetal: bool
    WeldmentList: ObservableCollection
    Weldment: object
    IsEnabledWeldment: bool
    PresentationList: ObservableCollection
    Presentation: object
    IsEnabledPresentation: bool
    DetailLevelList: ObservableCollection
    DetailLevel: object
    IsEnabledDetailLevel: bool
    PosRepresentationList: ObservableCollection
    PosRepresentation: object
    IsEnabledPosRepresentation: bool
    DesignViewList: ObservableCollection
    DesignView: object
    IsEnabledDesignView: bool
    IsEnabledViewStyle: bool
    ViewStyle: int
    IsEnabledCutInheritance1: bool
    IsEnabledCutInheritance: bool
    CutInheritance_1: bool
    IsEnabledVisibility6: bool
    IsEnabledVisibility5: bool
    IsEnabledVisibility4: bool
    IsEnabledVisibility3: bool
    IsEnabledVisibility2: bool
    IsEnabledVisibility1: bool
    IsEnabledVisibility: bool
    Visibility_6: bool
    Visibility_5: bool
    Visibility_4: bool
    Visibility_3: bool
    Visibility_2: bool
    Visibility_1: bool
    ScaleList: ObservableCollection
    Scale: object
    IsEnabledScale: bool
    ViewStyleFBImage: object
    ViewStyleFBText: str
    ViewBaseINV: ICommand
    ViewBaseMS: ICommand
    ViewReturn: ICommand
    ViewStyleSH: ICommand
    ViewStyleSV: ICommand
    ViewStyleWH: ICommand
    ViewStyleWV: ICommand
    ViewStyleFB: ICommand
    ViewSelectDepth: ICommand
    ViewSelect: ICommand
    ViewUpdateAll: ICommand
    ViewCancel: ICommand
    ViewAccept: ICommand
    ViewMove: ICommand
    ViewOption: ICommand
    def ConvertDoubleToStr(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...
    def ConvertStrToDouble(self, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object: ...
    def Dispose(self, ) -> None: ...
    def convertItemData2Image(self, item: object) -> str: ...
    def isVetoSetCurrentDetailViewStyle(self, ) -> bool: ...
    def isVetoSetCurrentSectionViewStyle(self, ) -> bool: ...
    def showVetoWarning(self, ) -> None: ...
    def vetoSetCurrentDetailViewStyle(self, value: object) -> bool: ...
    def vetoSetCurrentSectionViewStyle(self, value: object) -> bool: ...

class WorkspaceCollection(ObservableCollection):
    """.NET: Autodesk.AutoCAD.Windows.Data.WorkspaceCollection"""
    def __init__(self, *args) -> None: ...
    IsEnabled: bool
    CurrentWorkspace: RibbonItem
    Count: int
    Item: RibbonItem
    def CUILoaded(self, sender: object, e: CuiLoadEventArgs) -> None: ...
    def OnSysvarCmdNamesChanged(self, sender: object, e: PropertyChangedEventArgs) -> None: ...
    def OnSysvarWSCurrentChanged(self, sender: object, e: PropertyChangedEventArgs) -> None: ...
    def WorkspaceSaved(self, sender: object, e: WorkspaceEventArgs) -> None: ...
    def WorkspaceSettingsSaved(self, sender: object, e: EventArgs) -> None: ...
