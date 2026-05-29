from typing import Any, ClassVar, overload
from java.io.PrintWriter import PrintWriter
from javax.sql.PooledConnection import PooledConnection

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class PooledConnectionBuilder:
    """Forward declaration for ``javax.sql.PooledConnectionBuilder``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('javax.sql.PooledConnectionBuilder')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/javax/sql/PooledConnectionBuilder.html
    """
    ...

class ConnectionPoolDataSource:
    def getLogWriter(self) -> PrintWriter: ...
    def setLogWriter(self, p0: PrintWriter) -> None: ...
    def setLoginTimeout(self, p0: int) -> None: ...
    def getLoginTimeout(self) -> int: ...
    @overload
    def getPooledConnection(self) -> PooledConnection: ...
    @overload
    def getPooledConnection(self, p0: str, p1: str) -> PooledConnection: ...
    def createPooledConnectionBuilder(self) -> PooledConnectionBuilder: ...
