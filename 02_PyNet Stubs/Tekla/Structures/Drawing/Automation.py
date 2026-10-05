# Auto-generated — Tekla 2026 — Tekla.Structures.Drawing.Automation

class AutoDrawingRule:
    """.NET: Tekla.Structures.Drawing.Automation.AutoDrawingRule"""
    def __init__(self, *args) -> None: ...
    Filename: str

class AutoDrawingsStatusEnum:
    """.NET: Tekla.Structures.Drawing.Automation.AutoDrawingsStatusEnum"""
    def __init__(self, *args) -> None: ...
    ...

class DrawingCreator:
    """.NET: Tekla.Structures.Drawing.Automation.DrawingCreator"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def CreateDrawings(Rule: AutoDrawingRule, aModelObjectIdentifier: List, OperationStatus: AutoDrawingsStatusEnum) -> bool: ...
