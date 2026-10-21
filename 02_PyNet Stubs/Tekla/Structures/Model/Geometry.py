# Auto-generated — Tekla 2026 — Tekla.Structures.Model.Geometry

class Rotation3D:
    """.NET: Tekla.Structures.Model.Geometry.Rotation3D"""
    def __init__(self, *args) -> None: ...
    AxisX: Vector
    AxisY: Vector
    AxisZ: Vector
    def Equals(self, other: Rotation3D, tolerance: float) -> bool: ...
    @staticmethod
    def FromZRotation(angle: Angle) -> Rotation3D: ...
