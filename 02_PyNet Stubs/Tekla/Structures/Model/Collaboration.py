# Auto-generated — Tekla 2026 — Tekla.Structures.Model.Collaboration

class IFC2X3_ParametricObject_CShapeProfile(ReferenceModelObjectAttribute):
    """.NET: Tekla.Structures.Model.Collaboration.IFC2X3_ParametricObject_CShapeProfile"""
    def __init__(self, *args) -> None: ...
    Depth: float
    Width: float
    WallThickness: float
    Girth: float
    InternalFilletRadius: float
    Origin: Point
    xDir: Vector
    Extrusion: Vector
    ProfileName: str
    Name: str
    Description: str
    ObjectType: str

class IFC2X3_ParametricObject_CircleHollowProfile(ReferenceModelObjectAttribute):
    """.NET: Tekla.Structures.Model.Collaboration.IFC2X3_ParametricObject_CircleHollowProfile"""
    def __init__(self, *args) -> None: ...
    Radius: float
    WallThickness: float
    Origin: Point
    xDir: Vector
    Extrusion: Vector
    ProfileName: str
    Name: str
    Description: str
    ObjectType: str

class IFC2X3_ParametricObject_CircleProfile(ReferenceModelObjectAttribute):
    """.NET: Tekla.Structures.Model.Collaboration.IFC2X3_ParametricObject_CircleProfile"""
    def __init__(self, *args) -> None: ...
    Radius: float
    Origin: Point
    xDir: Vector
    Extrusion: Vector
    ProfileName: str
    Name: str
    Description: str
    ObjectType: str

class IFC2X3_ParametricObject_EllipseProfile(ReferenceModelObjectAttribute):
    """.NET: Tekla.Structures.Model.Collaboration.IFC2X3_ParametricObject_EllipseProfile"""
    def __init__(self, *args) -> None: ...
    SemiAxis1: float
    SemiAxis2: float
    Origin: Point
    xDir: Vector
    Extrusion: Vector
    ProfileName: str
    Name: str
    Description: str
    ObjectType: str

class IFC2X3_ParametricObject_IShapeProfile(ReferenceModelObjectAttribute):
    """.NET: Tekla.Structures.Model.Collaboration.IFC2X3_ParametricObject_IShapeProfile"""
    def __init__(self, *args) -> None: ...
    OverallWidth: float
    OverallDepth: float
    WebThickness: float
    FlangeThickness: float
    FilletRadius: float
    Origin: Point
    xDir: Vector
    Extrusion: Vector
    ProfileName: str
    Name: str
    Description: str
    ObjectType: str

class IFC2X3_ParametricObject_LShapeProfile(ReferenceModelObjectAttribute):
    """.NET: Tekla.Structures.Model.Collaboration.IFC2X3_ParametricObject_LShapeProfile"""
    def __init__(self, *args) -> None: ...
    Depth: float
    Width: float
    Thickness: float
    FilletRadius: float
    EdgeRadius: float
    LegSlope: float
    Origin: Point
    xDir: Vector
    Extrusion: Vector
    ProfileName: str
    Name: str
    Description: str
    ObjectType: str

class IFC2X3_ParametricObject_RectangleHollowProfile(ReferenceModelObjectAttribute):
    """.NET: Tekla.Structures.Model.Collaboration.IFC2X3_ParametricObject_RectangleHollowProfile"""
    def __init__(self, *args) -> None: ...
    XDim: float
    YDim: float
    WallThickness: float
    InnerFilletRadius: float
    OuterFilletRadius: float
    Origin: Point
    xDir: Vector
    Extrusion: Vector
    ProfileName: str
    Name: str
    Description: str
    ObjectType: str

class IFC2X3_ParametricObject_RectangleProfile(ReferenceModelObjectAttribute):
    """.NET: Tekla.Structures.Model.Collaboration.IFC2X3_ParametricObject_RectangleProfile"""
    def __init__(self, *args) -> None: ...
    XDim: float
    YDim: float
    Origin: Point
    xDir: Vector
    Extrusion: Vector
    ProfileName: str
    Name: str
    Description: str
    ObjectType: str

class IFC2X3_ParametricObject_TShapeProfile(ReferenceModelObjectAttribute):
    """.NET: Tekla.Structures.Model.Collaboration.IFC2X3_ParametricObject_TShapeProfile"""
    def __init__(self, *args) -> None: ...
    Depth: float
    FlangeWidth: float
    WebThickness: float
    FlangeThickness: float
    FilletRadius: float
    FlangeEdgeRadius: float
    WebEdgeRadius: float
    WebSlope: float
    FlangeSlope: float
    Origin: Point
    xDir: Vector
    Extrusion: Vector
    ProfileName: str
    Name: str
    Description: str
    ObjectType: str

class IFC2X3_ParametricObject_UShapeProfile(ReferenceModelObjectAttribute):
    """.NET: Tekla.Structures.Model.Collaboration.IFC2X3_ParametricObject_UShapeProfile"""
    def __init__(self, *args) -> None: ...
    Depth: float
    FlangeWidth: float
    WebThickness: float
    FlangeThickness: float
    FilletRadius: float
    EdgeRadius: float
    FlangeSlope: float
    Origin: Point
    xDir: Vector
    Extrusion: Vector
    ProfileName: str
    Name: str
    Description: str
    ObjectType: str

class IFC2X3_ParametricObject_ZShapeProfile(ReferenceModelObjectAttribute):
    """.NET: Tekla.Structures.Model.Collaboration.IFC2X3_ParametricObject_ZShapeProfile"""
    def __init__(self, *args) -> None: ...
    Depth: float
    FlangeWidth: float
    WebThickness: float
    FlangeThickness: float
    FilletRadius: float
    EdgeRadius: float
    Origin: Point
    xDir: Vector
    Extrusion: Vector
    ProfileName: str
    Name: str
    Description: str
    ObjectType: str

class ParametricObject_CustomProfile(ReferenceModelObjectAttribute):
    """.NET: Tekla.Structures.Model.Collaboration.ParametricObject_CustomProfile"""
    def __init__(self, *args) -> None: ...
    Origin: Point
    xDir: Vector
    Extrusion: Vector
    ProfileName: str
    Name: str
    Description: str
    ObjectType: str

class ParametricObject_ObjectBoundingBox(ReferenceModelObjectAttribute):
    """.NET: Tekla.Structures.Model.Collaboration.ParametricObject_ObjectBoundingBox"""
    def __init__(self, *args) -> None: ...
    yDir: Vector
    Origin: Point
    xDir: Vector
    Extrusion: Vector
    ProfileName: str
    Name: str
    Description: str
    ObjectType: str

class ReferenceModelObjectAttribute:
    """.NET: Tekla.Structures.Model.Collaboration.ReferenceModelObjectAttribute"""
    def __init__(self, *args) -> None: ...
    Origin: Point
    xDir: Vector
    Extrusion: Vector
    ProfileName: str
    Name: str
    Description: str
    ObjectType: str

class ReferenceModelObjectAttributeEnumerator:
    """.NET: Tekla.Structures.Model.Collaboration.ReferenceModelObjectAttributeEnumerator"""
    def __init__(self, *args) -> None: ...
    Current: object
    def MoveNext(self, ) -> bool: ...
    def Reset(self, ) -> None: ...
