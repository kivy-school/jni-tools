from typing import Any, ClassVar, overload
from java.sql.SQLException import SQLException
from javax.sql.PooledConnection import PooledConnection

class ConnectionEvent:
    @overload
    def __init__(self, arg0: PooledConnection) -> None: ...
    @overload
    def __init__(self, arg0: PooledConnection, arg1: SQLException) -> None: ...
    def getSQLException(self) -> SQLException: ...
