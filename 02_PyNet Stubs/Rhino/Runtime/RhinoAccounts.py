# Auto-generated — Rhino 8 — Rhino.Runtime.RhinoAccounts

class IOAuth2Token:
    """.NET: Rhino.Runtime.RhinoAccounts.IOAuth2Token"""
    def __init__(self, *args) -> None: ...
    Exp: Nullable
    Scope: IReadOnlyCollection
    RawToken: str
    IsExpired: bool

class IOpenIDConnectToken:
    """.NET: Rhino.Runtime.RhinoAccounts.IOpenIDConnectToken"""
    def __init__(self, *args) -> None: ...
    Sub: str
    MemberGroups: IReadOnlyDictionary
    AdminGroups: IReadOnlyDictionary
    OwnerGroups: IReadOnlyDictionary
    AllGroups: IReadOnlyDictionary
    UpdatedAt: Nullable
    Iat: Nullable
    Exp: Nullable
    Iss: str
    Aud: str
    AuthTime: Nullable
    Nonce: str
    AtHash: str
    Emails: IReadOnlyCollection
    EmailVerified: Nullable
    Name: str
    Phone: str
    Locale: str
    Picture: str
    RawToken: str
    IsExpired: bool
    IsUpdated: bool

class IRhinoAccountsManager:
    """.NET: Rhino.Runtime.RhinoAccounts.IRhinoAccountsManager"""
    def __init__(self, *args) -> None: ...
    def ExecuteProtectedCode(self, protectedCode: Action) -> None: ...
    def ExecuteProtectedCodeAsync(self, protectedCode: Func) -> Task: ...
    def GetAuthTokensAsync(self, clientId: str, clientSecret: str, scope: IEnumerable, prompt: str, maxAge: Nullable, showUI: bool, progress: IProgress, secretKey: SecretKey, cancellationToken: CancellationToken) -> Task: ...
    def RevokeAuthTokenAsync(self, oauth2Token: IOAuth2Token, secretKey: SecretKey, cancellationToken: CancellationToken) -> Task: ...
    def TryGetAuthTokens(self, clientId: str, scope: IEnumerable, secretKey: SecretKey) -> Tuple: ...
    def UpdateOpenIDConnectTokenAsync(self, currentToken: IOpenIDConnectToken, oauth2Token: IOAuth2Token, secretKey: SecretKey, cancellationToken: CancellationToken) -> Task: ...

class ProgressState:
    """.NET: Rhino.Runtime.RhinoAccounts.ProgressState"""
    def __init__(self, *args) -> None: ...
    ...

class RhinoAccoountsProgressInfo:
    """.NET: Rhino.Runtime.RhinoAccounts.RhinoAccoountsProgressInfo"""
    def __init__(self, *args) -> None: ...
    Metadata: Dictionary
    Description: str
    State: ProgressState

class RhinoAccountsAuthTokenMismatchException(RhinoAccountsException):
    """.NET: Rhino.Runtime.RhinoAccounts.RhinoAccountsAuthTokenMismatchException"""
    def __init__(self, *args) -> None: ...
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str

class RhinoAccountsCannotListenException(RhinoAccountsException):
    """.NET: Rhino.Runtime.RhinoAccounts.RhinoAccountsCannotListenException"""
    def __init__(self, *args) -> None: ...
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str

class RhinoAccountsException(Exception):
    """.NET: Rhino.Runtime.RhinoAccounts.RhinoAccountsException"""
    def __init__(self, *args) -> None: ...
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str

class RhinoAccountsGroup:
    """.NET: Rhino.Runtime.RhinoAccounts.RhinoAccountsGroup"""
    def __init__(self, *args) -> None: ...
    Id: str
    Name: str

class RhinoAccountsInvalidResponseException(RhinoAccountsException):
    """.NET: Rhino.Runtime.RhinoAccounts.RhinoAccountsInvalidResponseException"""
    def __init__(self, *args) -> None: ...
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str

class RhinoAccountsInvalidStateException(RhinoAccountsException):
    """.NET: Rhino.Runtime.RhinoAccounts.RhinoAccountsInvalidStateException"""
    def __init__(self, *args) -> None: ...
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str

class RhinoAccountsInvalidTokenException(RhinoAccountsException):
    """.NET: Rhino.Runtime.RhinoAccounts.RhinoAccountsInvalidTokenException"""
    def __init__(self, *args) -> None: ...
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str

class RhinoAccountsManager:
    """.NET: Rhino.Runtime.RhinoAccounts.RhinoAccountsManager"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def ExecuteProtectedCode(protectedCode: Action) -> None: ...
    @staticmethod
    def ExecuteProtectedCodeAsync(protectedCode: Func) -> Task: ...
    @staticmethod
    def GetAuthTokensAsync(clientId: str, clientSecret: str, scope: IEnumerable, prompt: str, maxAge: Nullable, showUI: bool, progress: IProgress, secretKey: SecretKey, cancellationToken: CancellationToken) -> Task: ...
    @staticmethod
    def RevokeAuthTokenAsync(oauth2Token: IOAuth2Token, secretKey: SecretKey, cancellationToken: CancellationToken) -> Task: ...
    @staticmethod
    def TryGetAuthTokens(clientId: str, scope: IEnumerable, secretKey: SecretKey) -> Tuple: ...
    @staticmethod
    def UpdateOpenIDConnectTokenAsync(currentToken: IOpenIDConnectToken, oauth2Token: IOAuth2Token, secretKey: SecretKey, cancellationToken: CancellationToken) -> Task: ...

class RhinoAccountsOperationInProgressException(RhinoAccountsException):
    """.NET: Rhino.Runtime.RhinoAccounts.RhinoAccountsOperationInProgressException"""
    def __init__(self, *args) -> None: ...
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str

class RhinoAccountsProxyException(RhinoAccountsException):
    """.NET: Rhino.Runtime.RhinoAccounts.RhinoAccountsProxyException"""
    def __init__(self, *args) -> None: ...
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str

class RhinoAccountsServerException(RhinoAccountsException):
    """.NET: Rhino.Runtime.RhinoAccounts.RhinoAccountsServerException"""
    def __init__(self, *args) -> None: ...
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str

class RhinoAccountsServerNotReachableException(RhinoAccountsException):
    """.NET: Rhino.Runtime.RhinoAccounts.RhinoAccountsServerNotReachableException"""
    def __init__(self, *args) -> None: ...
    TargetSite: MethodBase
    Message: str
    Data: IDictionary
    InnerException: Exception
    HelpLink: str
    Source: str
    HResult: int
    StackTrace: str

class SecretKey:
    """.NET: Rhino.Runtime.RhinoAccounts.SecretKey"""
    def __init__(self, *args) -> None: ...
    ...
