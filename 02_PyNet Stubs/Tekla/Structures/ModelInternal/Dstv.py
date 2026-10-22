# Auto-generated — Tekla 2026 — Tekla.Structures.ModelInternal.Dstv

class DstvBendInfo:
    """.NET: Tekla.Structures.ModelInternal.Dstv.DstvBendInfo"""
    def __init__(self, *args) -> None: ...
    FirstPoint: Point
    SecondPoint: Point
    Angle: float
    Radius: float

class DstvContour:
    """.NET: Tekla.Structures.ModelInternal.Dstv.DstvContour"""
    def __init__(self, *args) -> None: ...
    ContourType: DstvContourType
    ContourRows: List

class DstvContourRow:
    """.NET: Tekla.Structures.ModelInternal.Dstv.DstvContourRow"""
    def __init__(self, *args) -> None: ...
    DstvView: DstvViewType
    Position: DstvPoint
    NotchType: DstvNotchType
    Radius: float
    WeldPrepTop: DstvWeldingPreparation
    WeldPrepBottom: DstvWeldingPreparation

class DstvContourType:
    """.NET: Tekla.Structures.ModelInternal.Dstv.DstvContourType"""
    def __init__(self, *args) -> None: ...
    ...

class DstvHeader:
    """.NET: Tekla.Structures.ModelInternal.Dstv.DstvHeader"""
    def __init__(self, *args) -> None: ...
    Filename: str
    ProjectNumber: str
    PhaseNumber: str
    PartMark: str
    DrawingMark: str
    Material: str
    Quantity: int
    Profile: str
    ProfileType: str
    NetLength: float
    GrossLength: float
    ProfileHeight: float
    FlangeHeight: float
    FlangeThickness: float
    WebThickness: float
    Radius: float
    MeterWeight: float
    FinishArea: float
    WebAngleFront: float
    WebAngleBack: float
    FlangeAngleFront: float
    FlangeAngleBack: float
    InfoText1: str
    InfoText2: str
    InfoText3: str
    InfoText4: str
    Comments: List

class DstvHole:
    """.NET: Tekla.Structures.ModelInternal.Dstv.DstvHole"""
    def __init__(self, *args) -> None: ...
    HoleRows: List

class DstvHoleRow:
    """.NET: Tekla.Structures.ModelInternal.Dstv.DstvHoleRow"""
    def __init__(self, *args) -> None: ...
    DstvView: DstvViewType
    Position: DstvPoint
    HoleType: DstvHoleType
    Diameter: float
    Thickness: float
    Slotted: bool
    Width: float
    Height: float
    Angle: float

class DstvHoleType:
    """.NET: Tekla.Structures.ModelInternal.Dstv.DstvHoleType"""
    def __init__(self, *args) -> None: ...
    ...

class DstvMark:
    """.NET: Tekla.Structures.ModelInternal.Dstv.DstvMark"""
    def __init__(self, *args) -> None: ...
    MarkType: DstvMarkType
    MarkRows: List
    HardStamp: DstvNumeration

class DstvMarkRow:
    """.NET: Tekla.Structures.ModelInternal.Dstv.DstvMarkRow"""
    def __init__(self, *args) -> None: ...
    DstvView: DstvViewType
    Position: DstvPoint
    Radius: float

class DstvMarkType:
    """.NET: Tekla.Structures.ModelInternal.Dstv.DstvMarkType"""
    def __init__(self, *args) -> None: ...
    ...

class DstvNotchType:
    """.NET: Tekla.Structures.ModelInternal.Dstv.DstvNotchType"""
    def __init__(self, *args) -> None: ...
    ...

class DstvNumeration:
    """.NET: Tekla.Structures.ModelInternal.Dstv.DstvNumeration"""
    def __init__(self, *args) -> None: ...
    DstvView: DstvViewType
    Position: DstvPoint
    Angle: float
    TextHeight: float
    Text: str

class DstvPoint:
    """.NET: Tekla.Structures.ModelInternal.Dstv.DstvPoint"""
    def __init__(self, *args) -> None: ...
    X: float
    Y: float
    Reference: DstvReferenceType

class DstvReferenceType:
    """.NET: Tekla.Structures.ModelInternal.Dstv.DstvReferenceType"""
    def __init__(self, *args) -> None: ...
    ...

class DstvStructure:
    """.NET: Tekla.Structures.ModelInternal.Dstv.DstvStructure"""
    def __init__(self, *args) -> None: ...
    Header: DstvHeader
    HeaderOrder: HeaderOrder
    Holes: List
    Contours: List
    ContourMarks: List
    HardStamp: DstvNumeration
    BentLines: List
    Filename: str
    FilePath: str
    FileExtension: str
    Precision: int
    def WriteOutput(self, ) -> bool: ...

class DstvViewType:
    """.NET: Tekla.Structures.ModelInternal.Dstv.DstvViewType"""
    def __init__(self, *args) -> None: ...
    ...

class DstvWeldingPreparation:
    """.NET: Tekla.Structures.ModelInternal.Dstv.DstvWeldingPreparation"""
    def __init__(self, *args) -> None: ...
    Angle: float
    Offset: float

class HeaderFields:
    """.NET: Tekla.Structures.ModelInternal.Dstv.HeaderFields"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def ApplyPrecision(value: str) -> bool: ...
    @staticmethod
    def IsValid(value: str) -> bool: ...

class HeaderOrder:
    """.NET: Tekla.Structures.ModelInternal.Dstv.HeaderOrder"""
    def __init__(self, *args) -> None: ...
    def AddRow(self, Row: HeaderRow) -> None: ...
    def DeleteAt(self, Index: int) -> None: ...
    def DeleteRow(self, Row: HeaderRow) -> bool: ...
    def GetRows(self, ) -> List: ...

class HeaderRow:
    """.NET: Tekla.Structures.ModelInternal.Dstv.HeaderRow"""
    def __init__(self, *args) -> None: ...
    def Add(self, Items: List) -> None: ...
    def AddItem(self, Item: str) -> None: ...
    def GetRowItems(self, ) -> List: ...
