# Auto-generated — Tekla 2026 — Tekla.Structures.ModelInternal.BimModelDataProduct

class AccessControlDto:
    """.NET: Tekla.Structures.ModelInternal.BimModelDataProduct.AccessControlDto"""
    def __init__(self, *args) -> None: ...
    PrincipalId: str
    AccessLevel: str

class AccessControlListEntry:
    """.NET: Tekla.Structures.ModelInternal.BimModelDataProduct.AccessControlListEntry"""
    def __init__(self, *args) -> None: ...
    AccessLevel: str
    ModelId: str
    PrincipalId: str

class BimModelDataProductClient:
    """.NET: Tekla.Structures.ModelInternal.BimModelDataProduct.BimModelDataProductClient"""
    def __init__(self, *args) -> None: ...
    def AddOrUpdateModelAccessAsync(self, accessToken: str, cloudModelInfo: ICloudModelInfo, accessControlListEntries: list, cancellationToken: CancellationToken) -> Task: ...
    def CheckApiCompatibilityAsync(self, TsProductVersion: str, cancellationToken: CancellationToken) -> Task: ...
    def CreateModelAsync(self, accessToken: str, region: BimModelDataApiRegion, createModelRequest: CreateModelRequest, stream: Stream, cancellationToken: CancellationToken, progress: IProgress) -> Task: ...
    def CreateModelVersionAsync(self, accessToken: str, cloudModelInfo: ICloudModelInfo, modelVersionInit: ModelVersionInit, stream: Stream, cancellationToken: CancellationToken, progress: IProgress) -> Task: ...
    def DeleteModelAsync(self, accessToken: str, cloudModelInfo: ICloudModelInfo, immediate: bool, cancellationToken: CancellationToken) -> Task: ...
    def GetModelAccessAsync(self, accessToken: str, cloudModelInfo: ICloudModelInfo, cancellationToken: CancellationToken) -> IAsyncEnumerable: ...
    def GetModelVersionAsync(self, accessToken: str, cloudModelVersionInfo: ICloudModelVersionInfo, cancellationToken: CancellationToken) -> Task: ...
    def GetModelVersionsAsync(self, accessToken: str, cloudModelInfo: ICloudModelInfo, cancellationToken: CancellationToken) -> Task: ...
    def GetModelsAsync(self, accessToken: str, region: BimModelDataApiRegion, options: ListModelOptions, cancellationToken: CancellationToken) -> IAsyncEnumerable: ...
    def RemoveModelAccessAsync(self, accessToken: str, cloudModelInfo: ICloudModelInfo, principalIds: list, cancellationToken: CancellationToken) -> Task: ...
    def UpdateModelAsync(self, accessToken: str, cloudModelInfo: ICloudModelInfo, modelUpdate: ModelUpdate, cancellationToken: CancellationToken) -> Task: ...
    def UploadModelVersionFormat(self, accessToken: str, cloudModelVersionInfo: ICloudModelVersionInfo, uploadFormat: str, stream: Stream, cancellationToken: CancellationToken, progress: IProgress) -> Task: ...

class BimModelDataProductMetadata:
    """.NET: Tekla.Structures.ModelInternal.BimModelDataProduct.BimModelDataProductMetadata"""
    def __init__(self, *args) -> None: ...
    Lifecycle: str
    MinimumVersion: Version
    RecommendedVersion: Version
    EndOfLife: Nullable

class CompatibilityCheckResult:
    """.NET: Tekla.Structures.ModelInternal.BimModelDataProduct.CompatibilityCheckResult"""
    def __init__(self, *args) -> None: ...
    Status: CompatibilityStatus
    Metadata: BimModelDataProductMetadata

class CompatibilityStatus:
    """.NET: Tekla.Structures.ModelInternal.BimModelDataProduct.CompatibilityStatus"""
    def __init__(self, *args) -> None: ...
    ...

class CurieParser:
    """.NET: Tekla.Structures.ModelInternal.BimModelDataProduct.CurieParser"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def ParseCurie(curie: str) -> CurieResult: ...

class CurieResult:
    """.NET: Tekla.Structures.ModelInternal.BimModelDataProduct.CurieResult"""
    def __init__(self, *args) -> None: ...
    Type: str
    Identifier: str

class ICloudModelInfo:
    """.NET: Tekla.Structures.ModelInternal.BimModelDataProduct.ICloudModelInfo"""
    def __init__(self, *args) -> None: ...
    Name: str
    ModelSchemaVersion: str
    ModelType: str
    ModelOwnerId: str
    ModelTags: IReadOnlyList
    ModelMetadata: IReadOnlyDictionary
    ModelCreatedAt: DateTimeOffset
    ModelCreatedBy: str
    ModelUpdatedAt: DateTimeOffset
    ModelUpdatedBy: str
    Region: BimModelDataApiRegion

class ICloudModelVersionInfo:
    """.NET: Tekla.Structures.ModelInternal.BimModelDataProduct.ICloudModelVersionInfo"""
    def __init__(self, *args) -> None: ...
    ModelInfo: ICloudModelInfo
    VersionSchemaVersion: str
    VersionCreatedAt: DateTimeOffset
    VersionUpdatedAt: DateTimeOffset
    VersionCreatedBy: str
    VersionDescription: str
    VersionUpdatedBy: str
    FriendlyVersion: str
    VersionAuthor: IReadOnlyDictionary

class ListModelOptions:
    """.NET: Tekla.Structures.ModelInternal.BimModelDataProduct.ListModelOptions"""
    def __init__(self, *args) -> None: ...
    AccessLevel: str
    Name: str
    SchemaVersion: str
    State: str
    Tags: str
    Type: str
    View: str
    OrganizationId: str

class ModelUpdate:
    """.NET: Tekla.Structures.ModelInternal.BimModelDataProduct.ModelUpdate"""
    def __init__(self, *args) -> None: ...
    ModelName: str
    VersionId: str
    Tags: List
    Metadata: Dictionary

class ModelVersionInit:
    """.NET: Tekla.Structures.ModelInternal.BimModelDataProduct.ModelVersionInit"""
    def __init__(self, *args) -> None: ...
    SchemaVersion: str
    VersionName: str
    Format: str
    Author: Dictionary
    Comment: str

class UnsupportedTsVersionException(Exception):
    """.NET: Tekla.Structures.ModelInternal.BimModelDataProduct.UnsupportedTsVersionException"""
    def __init__(self, *args) -> None: ...
    MinimumVersion: str
    RecommendedVersion: str
    CurrentTsVersion: str
    Message: str
    Data: IDictionary
    InnerException: Exception
    TargetSite: MethodBase
    StackTrace: str
    HelpLink: str
    Source: str
    HResult: int
