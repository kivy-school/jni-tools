from typing import Any, ClassVar, overload
from android.database.Cursor import Cursor

class FilterQueryProvider:
    def runQuery(self, arg0: str) -> Cursor: ...
