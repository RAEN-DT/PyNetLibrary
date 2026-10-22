# Auto-generated — Rhino 8 — Rhino.DocObjects.Custom

class ClassIdAttribute(Attribute):
    """.NET: Rhino.DocObjects.Custom.ClassIdAttribute"""
    def __init__(self, *args) -> None: ...
    Id: Guid
    TypeId: object

class CustomBrepObject(BrepObject):
    """.NET: Rhino.DocObjects.Custom.CustomBrepObject"""
    def __init__(self, *args) -> None: ...
    BrepGeometry: Brep
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary

class CustomCurveObject(CurveObject):
    """.NET: Rhino.DocObjects.Custom.CustomCurveObject"""
    def __init__(self, *args) -> None: ...
    CurveGeometry: Curve
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def Dispose(self, ) -> None: ...

class CustomGripObject(GripObject):
    """.NET: Rhino.DocObjects.Custom.CustomGripObject"""
    def __init__(self, *args) -> None: ...
    Index: int
    OriginalLocation: Point3d
    Weight: float
    CurrentLocation: Point3d
    Moved: bool
    OwnerId: Guid
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def Dispose(self, ) -> None: ...
    def NewLocation(self, ) -> None: ...

class CustomMeshObject(MeshObject):
    """.NET: Rhino.DocObjects.Custom.CustomMeshObject"""
    def __init__(self, *args) -> None: ...
    IsCustomObject: bool
    MeshGeometry: Mesh
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def Dispose(self, ) -> None: ...

class CustomObjectGrips:
    """.NET: Rhino.DocObjects.Custom.CustomObjectGrips"""
    def __init__(self, *args) -> None: ...
    GripCount: int
    NewLocation: bool
    GripsMoved: bool
    OwnerObject: RhinoObject
    def Dispose(self, ) -> None: ...
    @staticmethod
    def Dragging() -> bool: ...
    def Grip(self, index: int) -> CustomGripObject: ...
    @staticmethod
    def RegisterGripsEnabler(enabler: TurnOnGripsEventHandler, customGripsType: Type) -> None: ...

class CustomPointObject(PointObject):
    """.NET: Rhino.DocObjects.Custom.CustomPointObject"""
    def __init__(self, *args) -> None: ...
    PointGeometry: Point
    ComponentType: ModelComponentType
    IsDeleted: bool
    IsReference: bool
    ObjectType: ObjectType
    Document: RhinoDoc
    Geometry: GeometryBase
    Attributes: ObjectAttributes
    RuntimeSerialNumber: int
    IsSolid: bool
    IsDeletable: bool
    IsInstanceDefinitionGeometry: bool
    IsNormal: bool
    IsLocked: bool
    IsHidden: bool
    WorksessionReferenceSerialNumber: int
    ReferenceModelSerialNumber: int
    InstanceDefinitionModelSerialNumber: int
    Visible: bool
    Id: Guid
    Name: str
    GroupCount: int
    GripsOn: bool
    GripsSelected: bool
    IsPictureFrame: bool
    HasDynamicTransform: bool
    RenderMaterial: RenderMaterial
    HasSubobjectMaterials: bool
    SubobjectMaterialComponents: list
    IsSystemComponent: bool
    HasId: bool
    IdIsLocked: bool
    Index: int
    HasIndex: bool
    IndexIsLocked: bool
    ComponentStatus: ComponentStatus
    IsComponentStatusLocked: bool
    HasName: bool
    NameIsLocked: bool
    DeletedName: str
    ModelSerialNumber: int
    IsDocumentControlled: bool
    IsValid: bool
    Disposed: bool
    HasUserData: bool
    UserData: UserDataList
    UserDictionary: ArchivableDictionary
    def Dispose(self, ) -> None: ...

class GripStatus:
    """.NET: Rhino.DocObjects.Custom.GripStatus"""
    def __init__(self, *args) -> None: ...
    Culled: bool
    Visible: bool

class GripsDrawEventArgs(DrawEventArgs):
    """.NET: Rhino.DocObjects.Custom.GripsDrawEventArgs"""
    def __init__(self, *args) -> None: ...
    DrawStaticStuff: bool
    DrawDynamicStuff: bool
    ControlPolygonStyle: int
    GripColor: Color
    LockedGripColor: Color
    SelectedGripColor: Color
    GripStatusCount: int
    Viewport: RhinoViewport
    Display: DisplayPipeline
    RhinoDoc: RhinoDoc
    def DrawControlPolygonLine(self, start: Point3d, end: Point3d, startStatus: int, endStatus: int) -> None: ...
    def GripStatus(self, index: int) -> GripStatus: ...
    def RestoreViewportSettings(self, ) -> None: ...

class TurnOnGripsEventHandler:
    """.NET: Rhino.DocObjects.Custom.TurnOnGripsEventHandler"""
    def __init__(self, *args) -> None: ...
    Target: object
    Method: MethodInfo
    def BeginInvoke(self, rhObj: RhinoObject, callback: AsyncCallback, object: object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, rhObj: RhinoObject) -> None: ...

class UnknownUserData(UserData):
    """.NET: Rhino.DocObjects.Custom.UnknownUserData"""
    def __init__(self, *args) -> None: ...
    Description: str
    ShouldWrite: bool
    Transform: Transform

class UserData:
    """.NET: Rhino.DocObjects.Custom.UserData"""
    def __init__(self, *args) -> None: ...
    Description: str
    ShouldWrite: bool
    Transform: Transform
    @staticmethod
    def Copy(source: CommonObject, destination: CommonObject) -> None: ...
    def Dispose(self, ) -> None: ...
    @staticmethod
    def MoveUserDataFrom(objectWithUserData: CommonObject) -> Guid: ...
    @staticmethod
    def MoveUserDataTo(objectToGetUserData: CommonObject, id: Guid, append: bool) -> None: ...

class UserDataList:
    """.NET: Rhino.DocObjects.Custom.UserDataList"""
    def __init__(self, *args) -> None: ...
    Count: int
    Item: UserData
    def Add(self, userdata: UserData) -> bool: ...
    def Contains(self, userdataId: Guid) -> bool: ...
    def Find(self, userdataType: Type) -> UserData: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def Purge(self, ) -> None: ...
    def Remove(self, userdata: UserData) -> bool: ...

class UserDataListEnumerator:
    """.NET: Rhino.DocObjects.Custom.UserDataListEnumerator"""
    def __init__(self, *args) -> None: ...
    Current: UserData
    def Dispose(self, ) -> None: ...
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...

class UserDictionary(UserData):
    """.NET: Rhino.DocObjects.Custom.UserDictionary"""
    def __init__(self, *args) -> None: ...
    Dictionary: ArchivableDictionary
    Description: str
    ShouldWrite: bool
    Transform: Transform
