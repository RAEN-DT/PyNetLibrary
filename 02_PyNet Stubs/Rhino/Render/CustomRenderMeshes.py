# Auto-generated — Rhino 8 — Rhino.Render.CustomRenderMeshes

class CustomRenderMeshProviderAttribute(Attribute):
    """.NET: Rhino.Render.CustomRenderMeshes.CustomRenderMeshProviderAttribute"""
    def __init__(self, *args) -> None: ...
    NonObjectIdsOnly: bool
    TypeId: object

class Instance:
    """.NET: Rhino.Render.CustomRenderMeshes.Instance"""
    def __init__(self, *args) -> None: ...
    Mesh: Mesh
    Material: RenderMaterial
    Transform: Transform
    IsViewDependent: bool
    IsRequestingPlugInDependent: bool
    IsForcedMaterial: bool
    def Dispose(self, ) -> None: ...

class MeshProviderIds:
    """.NET: Rhino.Render.CustomRenderMeshes.MeshProviderIds"""
    def __init__(self, *args) -> None: ...
    EdgeSoftening: Guid
    Displacement: Guid
    CurvePiping: Guid
    Shutlining: Guid
    Thickening: Guid

class RenderMeshProvider:
    """.NET: Rhino.Render.CustomRenderMeshes.RenderMeshProvider"""
    def __init__(self, *args) -> None: ...
    Name: str
    ProviderId: Guid
    NonObjectIds: List
    def Dispose(self, ) -> None: ...
    def GetParameter(self, doc: RhinoDoc, objectId: Guid, parameterName: str) -> object: ...
    def HasCustomRenderMeshes(self, mt: MeshType, vp: ViewportInfo, doc: RhinoDoc, objectId: Guid, flags: Flags, plugin: PlugIn, attrs: DisplayPipelineAttributes) -> bool: ...
    def Progress(self, doc: RhinoDoc, optional_objectIds: list) -> RenderMeshProviderProgress: ...
    @staticmethod
    def ProgressForAll(doc: RhinoDoc, optional_objectIds: list) -> list: ...
    @staticmethod
    def RegisterProvider(provider: RenderMeshProvider, plugin: PlugIn) -> bool: ...
    @staticmethod
    def RegisterProviders(assembly: Assembly, plugin: PlugIn) -> None: ...
    def RenderMeshes(self, mt: MeshType, vp: ViewportInfo, doc: RhinoDoc, objectId: Guid, ancestry: List, flags: Flags, previousPrimitives: RenderMeshes, plugin: PlugIn, attrs: DisplayPipelineAttributes) -> RenderMeshes: ...
    def SetParameter(self, doc: RhinoDoc, objectId: Guid, parameterName: str, value: object) -> None: ...

class RenderMeshProviderProgress:
    """.NET: Rhino.Render.CustomRenderMeshes.RenderMeshProviderProgress"""
    def __init__(self, *args) -> None: ...
    Text: str
    Amount: float
    Target: float
    IsComplete: bool
    ProviderId: Guid

class RenderMeshes:
    """.NET: Rhino.Render.CustomRenderMeshes.RenderMeshes"""
    def __init__(self, *args) -> None: ...
    InstanceCount: int
    ObjectId: Guid
    Document: RhinoDoc
    Hash: int
    def AddInstance(self, instance: Instance) -> None: ...
    def Dispose(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetHashCode(self, ) -> int: ...
