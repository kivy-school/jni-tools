from typing import Any, ClassVar, overload
from java.io.PrintStream import PrintStream
from java.io.PrintWriter import PrintWriter
from java.sql.Connection import Connection
from java.sql.Driver import Driver
from java.util.Enumeration import Enumeration
from java.util.Properties import Properties
from java.util.stream.Stream import Stream

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class DriverAction:
    """Forward declaration for ``java.sql.DriverAction``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.sql.DriverAction')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/sql/DriverAction.html
    """
    ...

class DriverManager:
    @overload
    @staticmethod
    def getConnection(p0: str, p1: str, p2: str) -> Connection: ...
    @overload
    @staticmethod
    def getConnection(p0: str) -> Connection: ...
    @overload
    @staticmethod
    def getConnection(p0: str, p1: Properties) -> Connection: ...
    @staticmethod
    def setLoginTimeout(p0: int) -> None: ...
    @staticmethod
    def getLoginTimeout() -> int: ...
    @staticmethod
    def deregisterDriver(p0: Driver) -> None: ...
    @staticmethod
    def drivers() -> Stream: ...
    @staticmethod
    def setLogStream(p0: PrintStream) -> None: ...
    @staticmethod
    def getLogStream() -> PrintStream: ...
    @staticmethod
    def getDriver(p0: str) -> Driver: ...
    @staticmethod
    def setLogWriter(p0: PrintWriter) -> None: ...
    @staticmethod
    def println(p0: str) -> None: ...
    @overload
    @staticmethod
    def registerDriver(p0: Driver, p1: DriverAction) -> None: ...
    @overload
    @staticmethod
    def registerDriver(p0: Driver) -> None: ...
    @staticmethod
    def getDrivers() -> Enumeration: ...
    @staticmethod
    def getLogWriter() -> PrintWriter: ...
