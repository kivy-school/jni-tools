from typing import Any, ClassVar, overload
from java.io.PrintWriter import PrintWriter
from java.sql.Connection import Connection

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class ConnectionBuilder:
    """Forward declaration for ``java.sql.ConnectionBuilder``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.sql.ConnectionBuilder')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/sql/ConnectionBuilder.html
    """
    ...

class DataSource:
    def getLogWriter(self) -> PrintWriter: ...
    def setLogWriter(self, p0: PrintWriter) -> None: ...
    def setLoginTimeout(self, p0: int) -> None: ...
    def getLoginTimeout(self) -> int: ...
    @overload
    def getConnection(self) -> Connection: ...
    @overload
    def getConnection(self, p0: str, p1: str) -> Connection: ...
    def createConnectionBuilder(self) -> ConnectionBuilder: ...
