# Auto-generated — Rhino 8 — Rhino.Render.Fields

class BoolField(Field):
    """.NET: Rhino.Render.Fields.BoolField"""
    def __init__(self, *args) -> None: ...
    Value: bool
    Name: str
    Key: str
    Tag: object
    TextureAmountMax: float
    TextureAmountMin: float
    UseTextureOn: bool
    UseTextureAmount: bool
    IsHiddenInAutoUI: bool
    AutomaticRegisteredProperty: bool
    def ValueAsObject(self, ) -> object: ...

class ByteArrayField(Field):
    """.NET: Rhino.Render.Fields.ByteArrayField"""
    def __init__(self, *args) -> None: ...
    Value: list
    Name: str
    Key: str
    Tag: object
    TextureAmountMax: float
    TextureAmountMin: float
    UseTextureOn: bool
    UseTextureAmount: bool
    IsHiddenInAutoUI: bool
    AutomaticRegisteredProperty: bool
    def ValueAsObject(self, ) -> object: ...

class Color4fField(Field):
    """.NET: Rhino.Render.Fields.Color4fField"""
    def __init__(self, *args) -> None: ...
    Value: Color4f
    SystemColorValue: Color
    Name: str
    Key: str
    Tag: object
    TextureAmountMax: float
    TextureAmountMin: float
    UseTextureOn: bool
    UseTextureAmount: bool
    IsHiddenInAutoUI: bool
    AutomaticRegisteredProperty: bool
    def ValueAsObject(self, ) -> object: ...

class DateTimeField(Field):
    """.NET: Rhino.Render.Fields.DateTimeField"""
    def __init__(self, *args) -> None: ...
    Value: DateTime
    Name: str
    Key: str
    Tag: object
    TextureAmountMax: float
    TextureAmountMin: float
    UseTextureOn: bool
    UseTextureAmount: bool
    IsHiddenInAutoUI: bool
    AutomaticRegisteredProperty: bool
    def ValueAsObject(self, ) -> object: ...

class DoubleField(Field):
    """.NET: Rhino.Render.Fields.DoubleField"""
    def __init__(self, *args) -> None: ...
    Value: float
    Name: str
    Key: str
    Tag: object
    TextureAmountMax: float
    TextureAmountMin: float
    UseTextureOn: bool
    UseTextureAmount: bool
    IsHiddenInAutoUI: bool
    AutomaticRegisteredProperty: bool
    def ValueAsObject(self, ) -> object: ...

class Field:
    """.NET: Rhino.Render.Fields.Field"""
    def __init__(self, *args) -> None: ...
    Name: str
    Key: str
    Tag: object
    TextureAmountMax: float
    TextureAmountMin: float
    UseTextureOn: bool
    UseTextureAmount: bool
    IsHiddenInAutoUI: bool
    AutomaticRegisteredProperty: bool
    def GetValue(self, ) -> T: ...
    def ValueAsObject(self, ) -> object: ...

class FieldDictionary:
    """.NET: Rhino.Render.Fields.FieldDictionary"""
    def __init__(self, *args) -> None: ...
    def Add(self, key: str, value: str, prompt: str, sectionId: int) -> StringField: ...
    def AddFilename(self, key: str, value: str, prompt: str, sectionId: int) -> StringField: ...
    def AddTextured(self, key: str, value: str, prompt: str, treatAsLinear: bool, sectionId: int) -> StringField: ...
    def ContainsField(self, fieldName: str) -> bool: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetField(self, fieldName: str) -> Field: ...
    def RemoveField(self, fieldName: str) -> None: ...
    def Set(self, key: str, value: str, changeContext: ChangeContexts) -> None: ...
    def SetTag(self, key: str, tag: object) -> bool: ...
    def TryGetTag(self, key: str, tag: object) -> bool: ...
    def TryGetValue(self, key: str, value: T) -> bool: ...

class FloatField(Field):
    """.NET: Rhino.Render.Fields.FloatField"""
    def __init__(self, *args) -> None: ...
    Value: float
    Name: str
    Key: str
    Tag: object
    TextureAmountMax: float
    TextureAmountMin: float
    UseTextureOn: bool
    UseTextureAmount: bool
    IsHiddenInAutoUI: bool
    AutomaticRegisteredProperty: bool
    def ValueAsObject(self, ) -> object: ...

class GuidField(Field):
    """.NET: Rhino.Render.Fields.GuidField"""
    def __init__(self, *args) -> None: ...
    Value: Guid
    Name: str
    Key: str
    Tag: object
    TextureAmountMax: float
    TextureAmountMin: float
    UseTextureOn: bool
    UseTextureAmount: bool
    IsHiddenInAutoUI: bool
    AutomaticRegisteredProperty: bool
    def ValueAsObject(self, ) -> object: ...

class IntField(Field):
    """.NET: Rhino.Render.Fields.IntField"""
    def __init__(self, *args) -> None: ...
    Value: int
    Name: str
    Key: str
    Tag: object
    TextureAmountMax: float
    TextureAmountMin: float
    UseTextureOn: bool
    UseTextureAmount: bool
    IsHiddenInAutoUI: bool
    AutomaticRegisteredProperty: bool
    def ValueAsObject(self, ) -> object: ...

class NullField(Field):
    """.NET: Rhino.Render.Fields.NullField"""
    def __init__(self, *args) -> None: ...
    Value: bool
    Name: str
    Key: str
    Tag: object
    TextureAmountMax: float
    TextureAmountMin: float
    UseTextureOn: bool
    UseTextureAmount: bool
    IsHiddenInAutoUI: bool
    AutomaticRegisteredProperty: bool
    def ValueAsObject(self, ) -> object: ...

class Point2dField(Field):
    """.NET: Rhino.Render.Fields.Point2dField"""
    def __init__(self, *args) -> None: ...
    Value: Point2d
    Name: str
    Key: str
    Tag: object
    TextureAmountMax: float
    TextureAmountMin: float
    UseTextureOn: bool
    UseTextureAmount: bool
    IsHiddenInAutoUI: bool
    AutomaticRegisteredProperty: bool
    def ValueAsObject(self, ) -> object: ...

class Point3dField(Field):
    """.NET: Rhino.Render.Fields.Point3dField"""
    def __init__(self, *args) -> None: ...
    Value: Point3d
    Name: str
    Key: str
    Tag: object
    TextureAmountMax: float
    TextureAmountMin: float
    UseTextureOn: bool
    UseTextureAmount: bool
    IsHiddenInAutoUI: bool
    AutomaticRegisteredProperty: bool
    def ValueAsObject(self, ) -> object: ...

class Point4dField(Field):
    """.NET: Rhino.Render.Fields.Point4dField"""
    def __init__(self, *args) -> None: ...
    Value: Point4d
    Name: str
    Key: str
    Tag: object
    TextureAmountMax: float
    TextureAmountMin: float
    UseTextureOn: bool
    UseTextureAmount: bool
    IsHiddenInAutoUI: bool
    AutomaticRegisteredProperty: bool
    def ValueAsObject(self, ) -> object: ...

class StringField(Field):
    """.NET: Rhino.Render.Fields.StringField"""
    def __init__(self, *args) -> None: ...
    Value: str
    Name: str
    Key: str
    Tag: object
    TextureAmountMax: float
    TextureAmountMin: float
    UseTextureOn: bool
    UseTextureAmount: bool
    IsHiddenInAutoUI: bool
    AutomaticRegisteredProperty: bool
    def ValueAsObject(self, ) -> object: ...

class TransformField(Field):
    """.NET: Rhino.Render.Fields.TransformField"""
    def __init__(self, *args) -> None: ...
    Value: Transform
    Name: str
    Key: str
    Tag: object
    TextureAmountMax: float
    TextureAmountMin: float
    UseTextureOn: bool
    UseTextureAmount: bool
    IsHiddenInAutoUI: bool
    AutomaticRegisteredProperty: bool
    def ValueAsObject(self, ) -> object: ...

class Vector2dField(Field):
    """.NET: Rhino.Render.Fields.Vector2dField"""
    def __init__(self, *args) -> None: ...
    Value: Vector2d
    Name: str
    Key: str
    Tag: object
    TextureAmountMax: float
    TextureAmountMin: float
    UseTextureOn: bool
    UseTextureAmount: bool
    IsHiddenInAutoUI: bool
    AutomaticRegisteredProperty: bool
    def ValueAsObject(self, ) -> object: ...

class Vector3dField(Field):
    """.NET: Rhino.Render.Fields.Vector3dField"""
    def __init__(self, *args) -> None: ...
    Value: Vector3d
    Name: str
    Key: str
    Tag: object
    TextureAmountMax: float
    TextureAmountMin: float
    UseTextureOn: bool
    UseTextureAmount: bool
    IsHiddenInAutoUI: bool
    AutomaticRegisteredProperty: bool
    def ValueAsObject(self, ) -> object: ...
