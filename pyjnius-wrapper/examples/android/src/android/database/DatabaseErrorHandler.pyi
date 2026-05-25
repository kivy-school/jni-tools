from typing import Any, ClassVar, overload
from android.database.sqlite.SQLiteDatabase import SQLiteDatabase

class DatabaseErrorHandler:
    def onCorruption(self, arg0: SQLiteDatabase) -> None: ...
