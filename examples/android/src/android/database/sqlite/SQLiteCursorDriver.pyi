from typing import Any, ClassVar, overload
from android.database.Cursor import Cursor

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class CursorFactory:
    """Forward declaration for ``android.database.sqlite.SQLiteDatabase.CursorFactory``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.database.sqlite.SQLiteDatabase.CursorFactory')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase/CursorFactory
    """
    ...

class SQLiteCursorDriver:
    def query(self, arg0: CursorFactory, arg1: list[str]) -> Cursor: ...
    def cursorDeactivated(self) -> None: ...
    def cursorRequeried(self, arg0: Cursor) -> None: ...
    def cursorClosed(self) -> None: ...
    def setBindArguments(self, arg0: list[str]) -> None: ...
