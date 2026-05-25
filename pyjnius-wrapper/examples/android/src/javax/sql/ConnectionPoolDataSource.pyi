from typing import Any, ClassVar, overload
from javax.sql.PooledConnection import PooledConnection

class ConnectionPoolDataSource:
    @overload
    def getPooledConnection(self) -> PooledConnection: ...
    @overload
    def getPooledConnection(self, arg0: str, arg1: str) -> PooledConnection: ...
