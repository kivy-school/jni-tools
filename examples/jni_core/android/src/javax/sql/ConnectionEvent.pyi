from typing import Any, ClassVar, overload
from java.sql.SQLException import SQLException
from javax.sql.PooledConnection import PooledConnection

class ConnectionEvent:
    @overload
    def __init__(self, p0: PooledConnection, p1: SQLException) -> None: ...
    @overload
    def __init__(self, p0: PooledConnection) -> None: ...
    def getSQLException(self) -> SQLException: ...
