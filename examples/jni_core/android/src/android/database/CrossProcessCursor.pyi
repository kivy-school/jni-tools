from typing import Any, ClassVar, overload
from android.database.CursorWindow import CursorWindow

class CrossProcessCursor:
    FIELD_TYPE_BLOB: ClassVar[int]
    FIELD_TYPE_FLOAT: ClassVar[int]
    FIELD_TYPE_INTEGER: ClassVar[int]
    FIELD_TYPE_NULL: ClassVar[int]
    FIELD_TYPE_STRING: ClassVar[int]
    def onMove(self, p0: int, p1: int) -> bool: ...
    def fillWindow(self, p0: int, p1: CursorWindow) -> None: ...
    def getWindow(self) -> CursorWindow: ...
