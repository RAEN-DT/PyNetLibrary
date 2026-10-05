# Auto-generated — Tekla 2026 — Tekla.Structures.Internal.ConnectUploads

class Connect:
    """.NET: Tekla.Structures.Internal.ConnectUploads.Connect"""
    def __init__(self, *args) -> None: ...
    Id: str
    VersionId: str
    Location: str
    UploadedBy: str

class IUploads:
    """.NET: Tekla.Structures.Internal.ConnectUploads.IUploads"""
    def __init__(self, *args) -> None: ...
    def AddUpload(self, upload: Upload) -> bool: ...
    def GetUploadByNameAndConnectLocation(self, name: str, connectLocation: str) -> Upload: ...
    def GetUploadByNameAndLocalPath(self, name: str, localPath: str) -> Upload: ...
    def GetUploadByNameLocalPathAndModelInstanceId(self, name: str, localPath: str, modelInstanceId: str) -> Upload: ...
    def RemoveUpload(self, upload: Upload) -> bool: ...

class Local:
    """.NET: Tekla.Structures.Internal.ConnectUploads.Local"""
    def __init__(self, *args) -> None: ...
    Path: str
    FileHash: str
    EventName: str
    CreatedTimeGuid: str

class Project:
    """.NET: Tekla.Structures.Internal.ConnectUploads.Project"""
    def __init__(self, *args) -> None: ...
    Id: str
    Uploads: List

class Upload:
    """.NET: Tekla.Structures.Internal.ConnectUploads.Upload"""
    def __init__(self, *args) -> None: ...
    Name: str
    Local: Local
    Connect: Connect
