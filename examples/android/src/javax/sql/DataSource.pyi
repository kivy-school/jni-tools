from typing import Any, ClassVar, overload
from java.sql.Connection import Connection

class DataSource:
    @overload
    def getConnection(self) -> Connection: ...
    @overload
    def getConnection(self, arg0: str, arg1: str) -> Connection: ...
