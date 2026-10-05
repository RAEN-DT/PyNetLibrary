# Auto-generated — Rhino 8 — Rhino.Render.ChangeQueue

class ChangeQueue:
    """.NET: Rhino.Render.ChangeQueue.ChangeQueue"""
    def __init__(self, *args) -> None: ...
    IsPreview: bool
    ViewId: Guid
    DisplayPipelineAttributes: DisplayPipelineAttributes
    def AreViewsEqual(self, aView: ViewInfo, bView: ViewInfo) -> bool: ...
    @staticmethod
    def ConvertCameraBasedLightToWorld(changequeue: ChangeQueue, light: Light, vp: ViewInfo) -> None: ...
    @staticmethod
    def CrcFromGuid(guid: Guid) -> int: ...
    def CreateWorld(self, bFlushWhenReady: bool) -> None: ...
    def Dispose(self, ) -> None: ...
    def EnvironmentForid(self, crc: int) -> RenderEnvironment: ...
    def EnvironmentFromOriginalInstanceId(self, id: Guid) -> RenderEnvironment: ...
    def EnvironmentIdForUsage(self, usage: Usage) -> int: ...
    def Flush(self, ) -> None: ...
    def GetQueueGroundPlane(self, ) -> GroundPlane: ...
    def GetQueueRenderSettings(self, ) -> RenderSettings: ...
    def GetQueueSceneBoundingBox(self, ) -> BoundingBox: ...
    def GetQueueSkylight(self, ) -> Skylight: ...
    def GetQueueSun(self, ) -> Light: ...
    def GetQueueView(self, ) -> ViewInfo: ...
    def MaterialFromId(self, crc: int) -> RenderMaterial: ...
    def MaterialFromOriginalInstanceId(self, id: Guid) -> RenderMaterial: ...
    def OneShot(self, ) -> None: ...
    def OriginalInstanceIdsFromEnvironmentId(self, crc: int) -> list: ...
    def OriginalInstanceIdsFromMaterialId(self, crc: int) -> list: ...
    def OriginalInstanceIdsFromTextureId(self, crc: int) -> list: ...
    def TextureForId(self, crc: int) -> RenderTexture: ...
    def TextureFromOriginalInstanceId(self, id: Guid) -> RenderTexture: ...

class ClippingPlane:
    """.NET: Rhino.Render.ChangeQueue.ClippingPlane"""
    def __init__(self, *args) -> None: ...
    IsEnabled: bool
    Plane: Plane
    Attributes: ObjectAttributes
    Id: Guid
    ViewIds: List
    ClipViewports: list

class DisplayRenderSettings:
    """.NET: Rhino.Render.ChangeQueue.DisplayRenderSettings"""
    def __init__(self, *args) -> None: ...
    CullBackFaces: bool
    ForceFlatShading: bool
    SceneLightingOn: bool

class DynamicObjectTransform:
    """.NET: Rhino.Render.ChangeQueue.DynamicObjectTransform"""
    def __init__(self, *args) -> None: ...
    MeshInstanceId: int
    Transform: Transform
    def ToString(self, ) -> str: ...

class Environment:
    """.NET: Rhino.Render.ChangeQueue.Environment"""
    def __init__(self, *args) -> None: ...
    ...

class GroundPlane:
    """.NET: Rhino.Render.ChangeQueue.GroundPlane"""
    def __init__(self, *args) -> None: ...
    IsShadowOnly: bool
    ShowUnderside: bool
    Altitude: float
    MaterialId: int
    TextureScale: Vector2d
    TextureOffset: Vector2d
    TextureRotation: float
    Enabled: bool
    Crc: int

class Light:
    """.NET: Rhino.Render.ChangeQueue.Light"""
    def __init__(self, *args) -> None: ...
    Id: Guid
    IdCrc: int
    Data: Light
    MaterialId: int
    ChangeType: Event

class MappingChannel:
    """.NET: Rhino.Render.ChangeQueue.MappingChannel"""
    def __init__(self, *args) -> None: ...
    Local: Transform
    Channel: int
    Mapping: TextureMapping

class MappingChannelCollection:
    """.NET: Rhino.Render.ChangeQueue.MappingChannelCollection"""
    def __init__(self, *args) -> None: ...
    SingleMapping: MappingChannel
    Count: int
    Item: MappingChannel
    Channels: IEnumerable

class Material:
    """.NET: Rhino.Render.ChangeQueue.Material"""
    def __init__(self, *args) -> None: ...
    MeshInstanceId: int
    Id: int
    MeshIndex: int

class Mesh:
    """.NET: Rhino.Render.ChangeQueue.Mesh"""
    def __init__(self, *args) -> None: ...
    SingleMesh: Mesh
    SingleMapping: MappingChannel
    Mapping: MappingChannelCollection
    Mappings: list
    OcsTransform: Transform
    Attributes: ObjectAttributes
    Object: RhinoObject
    def GetMeshes(self, ) -> list: ...
    def Id(self, ) -> Guid: ...

class MeshInstance:
    """.NET: Rhino.Render.ChangeQueue.MeshInstance"""
    def __init__(self, *args) -> None: ...
    ReceiveShadows: bool
    CastShadows: bool
    InstanceId: int
    RootId: Guid
    ParentId: Guid
    MeshId: Guid
    GroupId: int
    MeshIndex: int
    MaterialId: int
    RenderMaterial: RenderMaterial
    Transform: Transform
    Decals: Decals
    ObjectAttributes: ObjectAttributes
    OcsTransform: Transform
    Ancestry: list

class Skylight:
    """.NET: Rhino.Render.ChangeQueue.Skylight"""
    def __init__(self, *args) -> None: ...
    Enabled: bool
    UsesCustomEnvironment: bool
    ShadowIntensity: float
    def ToString(self, ) -> str: ...
