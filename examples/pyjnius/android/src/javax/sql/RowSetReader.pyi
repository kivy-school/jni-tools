from typing import Any, ClassVar, overload
from javax.sql.RowSetInternal import RowSetInternal

class RowSetReader:
    def readData(self, p0: RowSetInternal) -> None: ...
