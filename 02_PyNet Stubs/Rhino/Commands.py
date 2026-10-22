# Auto-generated — Rhino 8 — Rhino.Commands

class Command:
    """.NET: Rhino.Commands.Command"""
    def __init__(self, *args) -> None: ...
    LastCommandId: Guid
    LastCommandResult: Result
    PlugIn: PlugIn
    Id: Guid
    EnglishName: str
    LocalName: str
    Settings: PersistentSettings
    HistoryReplayOnObjectAttributeChange: bool
    @staticmethod
    def DisplayHelp(commandId: Guid) -> None: ...
    @staticmethod
    def GetCommandContextHelpUrl(commandId: Guid) -> str: ...
    @staticmethod
    def GetCommandNames(english: bool, loaded: bool) -> list: ...
    @staticmethod
    def GetCommandStack() -> list: ...
    @staticmethod
    def GetMostRecentCommands() -> list: ...
    @staticmethod
    def InCommand() -> bool: ...
    @staticmethod
    def InScriptRunnerCommand() -> bool: ...
    @staticmethod
    def IsCommand(name: str) -> bool: ...
    @staticmethod
    def IsValidCommandName(name: str) -> bool: ...
    @staticmethod
    def LookupCommandId(name: str, searchForEnglishName: bool) -> Guid: ...
    @staticmethod
    def LookupCommandName(commandId: Guid, englishName: bool) -> str: ...
    @staticmethod
    def RunProxyCommand(commandCallback: RunCommandDelegate, doc: RhinoDoc, data: object) -> None: ...

class CommandEventArgs(EventArgs):
    """.NET: Rhino.Commands.CommandEventArgs"""
    def __init__(self, *args) -> None: ...
    CommandId: Guid
    CommandEnglishName: str
    CommandLocalName: str
    CommandHelpURL: str
    CommandPluginName: str
    CommandResult: Result
    DocumentRuntimeSerialNumber: int
    Document: RhinoDoc

class CommandStyleAttribute(Attribute):
    """.NET: Rhino.Commands.CommandStyleAttribute"""
    def __init__(self, *args) -> None: ...
    Styles: Style
    TypeId: object

class CustomUndoEventArgs(EventArgs):
    """.NET: Rhino.Commands.CustomUndoEventArgs"""
    def __init__(self, *args) -> None: ...
    CommandId: Guid
    UndoSerialNumber: int
    ActionDescription: str
    CreatedByRedo: bool
    Tag: object
    Document: RhinoDoc

class MostRecentCommandDescription:
    """.NET: Rhino.Commands.MostRecentCommandDescription"""
    def __init__(self, *args) -> None: ...
    DisplayString: str
    Macro: str

class Result:
    """.NET: Rhino.Commands.Result"""
    def __init__(self, *args) -> None: ...
    ...

class RunMode:
    """.NET: Rhino.Commands.RunMode"""
    def __init__(self, *args) -> None: ...
    ...

class SelCommand(Command):
    """.NET: Rhino.Commands.SelCommand"""
    def __init__(self, *args) -> None: ...
    TestLights: bool
    TestGrips: bool
    BeQuiet: bool
    PlugIn: PlugIn
    Id: Guid
    EnglishName: str
    LocalName: str
    Settings: PersistentSettings
    HistoryReplayOnObjectAttributeChange: bool

class Style:
    """.NET: Rhino.Commands.Style"""
    def __init__(self, *args) -> None: ...
    ...

class TransformCommand(Command):
    """.NET: Rhino.Commands.TransformCommand"""
    def __init__(self, *args) -> None: ...
    PlugIn: PlugIn
    Id: Guid
    EnglishName: str
    LocalName: str
    Settings: PersistentSettings
    HistoryReplayOnObjectAttributeChange: bool

class UndoRedoEventArgs(EventArgs):
    """.NET: Rhino.Commands.UndoRedoEventArgs"""
    def __init__(self, *args) -> None: ...
    CommandId: Guid
    UndoSerialNumber: int
    IsBeforeBeginRecording: bool
    IsBeginRecording: bool
    IsBeforeEndRecording: bool
    IsEndRecording: bool
    IsBeginUndo: bool
    IsEndUndo: bool
    IsBeginRedo: bool
    IsEndRedo: bool
    IsPurgeRecord: bool
