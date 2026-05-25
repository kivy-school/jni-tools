from typing import Any, ClassVar, overload
from java.io.PrintWriter import PrintWriter
from java.util.logging.Logger import Logger

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class ShardingKeyBuilder:
    """Forward declaration for ``java.sql.ShardingKeyBuilder``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.sql.ShardingKeyBuilder')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/sql/ShardingKeyBuilder.html
    """
    ...

class CommonDataSource:
    def createShardingKeyBuilder(self) -> ShardingKeyBuilder: ...
    def getLogWriter(self) -> PrintWriter: ...
    def setLogWriter(self, p0: PrintWriter) -> None: ...
    def setLoginTimeout(self, p0: int) -> None: ...
    def getLoginTimeout(self) -> int: ...
    def getParentLogger(self) -> Logger: ...
