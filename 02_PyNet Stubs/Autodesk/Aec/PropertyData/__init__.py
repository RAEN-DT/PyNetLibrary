# Auto-generated — Civil 26 — Autodesk.Aec.PropertyData

class DataType:
    """.NET: Autodesk.Aec.PropertyData.DataType"""
    def __init__(self, *args) -> None: ...
    ...

class IteratorType:
    """.NET: Autodesk.Aec.PropertyData.IteratorType"""
    def __init__(self, *args) -> None: ...
    ...

class ScheduleHeaderPositionNode(DisposableWrapper):
    """.NET: Autodesk.Aec.PropertyData.ScheduleHeaderPositionNode"""
    def __init__(self, *args) -> None: ...
    HeaderNode: ScheduleTableStyleHeaderNode
    Position: ScheduleTableHeaderPosition
    Heading: str
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ScheduleTableColumnOrder(DisposableWrapper):
    """.NET: Autodesk.Aec.PropertyData.ScheduleTableColumnOrder"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def CompareRows(self, row1: int, row2: int, raw: bool) -> int: ...

class ScheduleTableColumnOrderAllColumns(ScheduleTableColumnOrder):
    """.NET: Autodesk.Aec.PropertyData.ScheduleTableColumnOrderAllColumns"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ScheduleTableColumnOrderSingleColumn(ScheduleTableColumnOrder):
    """.NET: Autodesk.Aec.PropertyData.ScheduleTableColumnOrderSingleColumn"""
    def __init__(self, *args) -> None: ...
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ScheduleTableHeaderPosition(DisposableWrapper):
    """.NET: Autodesk.Aec.PropertyData.ScheduleTableHeaderPosition"""
    def __init__(self, *args) -> None: ...
    Top: float
    Bottom: float
    Right: float
    Left: float
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr

class ScheduleTableHeaderPositionIterator(DisposableWrapper):
    """.NET: Autodesk.Aec.PropertyData.ScheduleTableHeaderPositionIterator"""
    def __init__(self, *args) -> None: ...
    Next: ScheduleHeaderPositionNode
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    @staticmethod
    def Create(unmanagedPointer: IntPtr, autoDelete: bool) -> ScheduleTableHeaderPositionIterator: ...
    def Reset(self, ) -> None: ...

class ScheduleTableStyleHeaderTreeParameter:
    """.NET: Autodesk.Aec.PropertyData.ScheduleTableStyleHeaderTreeParameter"""
    def __init__(self, *args) -> None: ...
    ...

class ScheduleTableUniqueVariantCollection(DisposableWrapper):
    """.NET: Autodesk.Aec.PropertyData.ScheduleTableUniqueVariantCollection"""
    def __init__(self, *args) -> None: ...
    SplitDelimitedValues: bool
    IsReadOnly: bool
    IsSynchronized: bool
    IsFixedSize: bool
    Item: object
    Count: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def Add(self, value: object) -> int: ...
    def Contains(self, value: object) -> bool: ...
    def CopyTo(self, array: Array, start: int) -> None: ...
    def Dump(self, ) -> None: ...
    def GetEnumerator(self, ) -> IEnumerator: ...
    def IndexOf(self, value: object) -> int: ...

class ScheduleTableVariantMatrix(DisposableWrapper):
    """.NET: Autodesk.Aec.PropertyData.ScheduleTableVariantMatrix"""
    def __init__(self, *args) -> None: ...
    StyleId: ObjectId
    NumberOfColumns: int
    NumberOfRows: int
    AutoDelete: bool
    IsDisposed: bool
    UnmanagedObject: IntPtr
    def AppendRowDataAt(self, row: int, entityId: ObjectId, blockReferencePathIdArray: ObjectIdCollection, sorted: bool) -> None: ...
    def CreateQuantity(self, desiredQuantityColumn: int, dataColumn: int, desiredProductColumn: int, repeatFirstColumn: bool) -> ScheduleTableVariantMatrix: ...
    def GetRowDataAt(self, row: int, sorted: bool) -> ObjectIdAndBlockReferencePathCollection: ...
    def GetValue(self, row: int, column: int, raw: bool) -> object: ...
    def SetValue(self, row: int, column: int, variant: object, raw: bool) -> None: ...
    def SortRows(self, order: ScheduleTableColumnOrder) -> None: ...
    def SortedRowIndex(self, row: int) -> int: ...
    def SwapColumns(self, column1: int, column2: int) -> None: ...
