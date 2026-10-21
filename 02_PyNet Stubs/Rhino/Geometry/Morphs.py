# Auto-generated — Rhino 8 — Rhino.Geometry.Morphs

class BendSpaceMorph(SpaceMorph):
    """.NET: Rhino.Geometry.Morphs.BendSpaceMorph"""
    def __init__(self, *args) -> None: ...
    IsValid: bool
    Tolerance: float
    QuickPreview: bool
    PreserveStructure: bool
    def Dispose(self, ) -> None: ...
    def MorphPoint(self, point: Point3d) -> Point3d: ...

class FlowSpaceMorph(SpaceMorph):
    """.NET: Rhino.Geometry.Morphs.FlowSpaceMorph"""
    def __init__(self, *args) -> None: ...
    IsValid: bool
    Tolerance: float
    QuickPreview: bool
    PreserveStructure: bool
    def Dispose(self, ) -> None: ...
    def MorphPoint(self, point: Point3d) -> Point3d: ...

class MaelstromSpaceMorph(SpaceMorph):
    """.NET: Rhino.Geometry.Morphs.MaelstromSpaceMorph"""
    def __init__(self, *args) -> None: ...
    IsValid: bool
    Tolerance: float
    QuickPreview: bool
    PreserveStructure: bool
    def Dispose(self, ) -> None: ...
    def MorphPoint(self, point: Point3d) -> Point3d: ...

class SplopSpaceMorph(SpaceMorph):
    """.NET: Rhino.Geometry.Morphs.SplopSpaceMorph"""
    def __init__(self, *args) -> None: ...
    IsValid: bool
    Tolerance: float
    QuickPreview: bool
    PreserveStructure: bool
    def Dispose(self, ) -> None: ...
    def MorphPoint(self, point: Point3d) -> Point3d: ...

class SporphSpaceMorph(SpaceMorph):
    """.NET: Rhino.Geometry.Morphs.SporphSpaceMorph"""
    def __init__(self, *args) -> None: ...
    IsValid: bool
    ConstrainNormal: Vector3d
    Tolerance: float
    QuickPreview: bool
    PreserveStructure: bool
    def Dispose(self, ) -> None: ...
    def MorphPoint(self, point: Point3d) -> Point3d: ...

class StretchSpaceMorph(SpaceMorph):
    """.NET: Rhino.Geometry.Morphs.StretchSpaceMorph"""
    def __init__(self, *args) -> None: ...
    IsValid: bool
    Tolerance: float
    QuickPreview: bool
    PreserveStructure: bool
    def Dispose(self, ) -> None: ...
    def MorphPoint(self, point: Point3d) -> Point3d: ...

class TaperSpaceMorph(SpaceMorph):
    """.NET: Rhino.Geometry.Morphs.TaperSpaceMorph"""
    def __init__(self, *args) -> None: ...
    IsValid: bool
    Tolerance: float
    QuickPreview: bool
    PreserveStructure: bool
    def Dispose(self, ) -> None: ...
    def MorphPoint(self, point: Point3d) -> Point3d: ...

class TwistSpaceMorph(SpaceMorph):
    """.NET: Rhino.Geometry.Morphs.TwistSpaceMorph"""
    def __init__(self, *args) -> None: ...
    TwistAxis: Line
    TwistAngleRadians: float
    InfiniteTwist: bool
    Tolerance: float
    QuickPreview: bool
    PreserveStructure: bool
    def Dispose(self, ) -> None: ...
    def MorphPoint(self, point: Point3d) -> Point3d: ...
