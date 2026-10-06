# Auto-generated — Tekla 2026 — Tekla.Structures.Plugins

class AutoDirectionTypeAttribute(Attribute):
    """.NET: Tekla.Structures.Plugins.AutoDirectionTypeAttribute"""
    def __init__(self, *args) -> None: ...
    Type: AutoDirectionTypeEnum
    TypeId: object

class ConnectionBase(MarshalByRefObject):
    """.NET: Tekla.Structures.Plugins.ConnectionBase"""
    def __init__(self, *args) -> None: ...
    Identifier: Identifier
    Code: str
    Primary: Identifier
    Positions: List
    Secondaries: List
    def IsDefaultValue(self, Value: int) -> bool: ...
    def Run(self, ) -> bool: ...

class CustomPartBase(MarshalByRefObject):
    """.NET: Tekla.Structures.Plugins.CustomPartBase"""
    def __init__(self, *args) -> None: ...
    Identifier: Identifier
    Positions: List
    def IsDefaultValue(self, Value: int) -> bool: ...
    def Run(self, ) -> bool: ...

class CustomPartInputTypeAttribute(Attribute):
    """.NET: Tekla.Structures.Plugins.CustomPartInputTypeAttribute"""
    def __init__(self, *args) -> None: ...
    Type: CustomPartInputType
    TypeId: object

class CustomPartPositioningTypeAttribute(Attribute):
    """.NET: Tekla.Structures.Plugins.CustomPartPositioningTypeAttribute"""
    def __init__(self, *args) -> None: ...
    Type: CustomPartPositioningType
    TypeId: object

class DetailTypeAttribute(Attribute):
    """.NET: Tekla.Structures.Plugins.DetailTypeAttribute"""
    def __init__(self, *args) -> None: ...
    Type: DetailTypeEnum
    TypeId: object

class DrawingPluginBase(MarshalByRefObject):
    """.NET: Tekla.Structures.Plugins.DrawingPluginBase"""
    def __init__(self, *args) -> None: ...
    def DefineInput(self, ) -> List: ...
    def IsDefaultValue(self, Value: int) -> bool: ...
    def Run(self, Input: List) -> bool: ...

class InputObjectDependencyAttribute(Attribute):
    """.NET: Tekla.Structures.Plugins.InputObjectDependencyAttribute"""
    def __init__(self, *args) -> None: ...
    Type: InputObjectDependency
    TypeId: object

class InputObjectTypeAttribute(Attribute):
    """.NET: Tekla.Structures.Plugins.InputObjectTypeAttribute"""
    def __init__(self, *args) -> None: ...
    Type: InputObjectType
    TypeId: object

class PluginAttribute(Attribute):
    """.NET: Tekla.Structures.Plugins.PluginAttribute"""
    def __init__(self, *args) -> None: ...
    Name: str
    TypeId: object

class PluginBase(MarshalByRefObject):
    """.NET: Tekla.Structures.Plugins.PluginBase"""
    def __init__(self, *args) -> None: ...
    Identifier: Identifier
    def DefineInput(self, ) -> List: ...
    def IsDefaultValue(self, Value: int) -> bool: ...
    def Run(self, Input: List) -> bool: ...

class PluginCoordinateSystemAttribute(Attribute):
    """.NET: Tekla.Structures.Plugins.PluginCoordinateSystemAttribute"""
    def __init__(self, *args) -> None: ...
    Type: CoordinateSystemType
    TypeId: object

class PluginDescriptionAttribute(Attribute):
    """.NET: Tekla.Structures.Plugins.PluginDescriptionAttribute"""
    def __init__(self, *args) -> None: ...
    Language: str
    Description: str
    TypeId: object

class PluginNameAttribute(Attribute):
    """.NET: Tekla.Structures.Plugins.PluginNameAttribute"""
    def __init__(self, *args) -> None: ...
    Language: str
    Name: str
    TypeId: object

class PluginPropertyFileLocationAttribute(Attribute):
    """.NET: Tekla.Structures.Plugins.PluginPropertyFileLocationAttribute"""
    def __init__(self, *args) -> None: ...
    Suffix: str
    Subdirectory: str
    TypeId: object

class PluginSymbolVisiblityAttribute(Attribute):
    """.NET: Tekla.Structures.Plugins.PluginSymbolVisiblityAttribute"""
    def __init__(self, *args) -> None: ...
    Type: SymbolVisibility
    TypeId: object

class PluginUserInterfaceAttribute(Attribute):
    """.NET: Tekla.Structures.Plugins.PluginUserInterfaceAttribute"""
    def __init__(self, *args) -> None: ...
    Description: str
    TypeId: object

class PositionTypeAttribute(Attribute):
    """.NET: Tekla.Structures.Plugins.PositionTypeAttribute"""
    def __init__(self, *args) -> None: ...
    Type: PositionTypeEnum
    TypeId: object

class SeamInputTypeAttribute(Attribute):
    """.NET: Tekla.Structures.Plugins.SeamInputTypeAttribute"""
    def __init__(self, *args) -> None: ...
    Type: SeamInputType
    TypeId: object

class SecondaryTypeAttribute(Attribute):
    """.NET: Tekla.Structures.Plugins.SecondaryTypeAttribute"""
    def __init__(self, *args) -> None: ...
    Type: SecondaryType
    TypeId: object

class StructuresFieldAttribute(Attribute):
    """.NET: Tekla.Structures.Plugins.StructuresFieldAttribute"""
    def __init__(self, *args) -> None: ...
    AttributeName: str
    TypeId: object

class UpdateModeAttribute(Attribute):
    """.NET: Tekla.Structures.Plugins.UpdateModeAttribute"""
    def __init__(self, *args) -> None: ...
    Type: UpdateMode
    TypeId: object
