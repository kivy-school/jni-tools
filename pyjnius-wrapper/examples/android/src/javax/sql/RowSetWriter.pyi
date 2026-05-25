from typing import Any, ClassVar, overload
from javax.sql.RowSetInternal import RowSetInternal

class RowSetWriter:
    def writeData(self, arg0: RowSetInternal) -> bool: ...
