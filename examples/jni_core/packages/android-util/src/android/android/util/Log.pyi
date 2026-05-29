from typing import Any, ClassVar, overload
from java.lang.Throwable import Throwable

class Log:
    ASSERT: ClassVar[int]
    DEBUG: ClassVar[int]
    ERROR: ClassVar[int]
    INFO: ClassVar[int]
    VERBOSE: ClassVar[int]
    WARN: ClassVar[int]
    @staticmethod
    def isLoggable(p0: str, p1: int) -> bool: ...
    @overload
    @staticmethod
    def wtf(p0: str, p1: str) -> int: ...
    @overload
    @staticmethod
    def wtf(p0: str, p1: Throwable) -> int: ...
    @overload
    @staticmethod
    def wtf(p0: str, p1: str, p2: Throwable) -> int: ...
    @staticmethod
    def getStackTraceString(p0: Throwable) -> str: ...
    @staticmethod
    def println(p0: int, p1: str, p2: str) -> int: ...
    @overload
    @staticmethod
    def e(p0: str, p1: str, p2: Throwable) -> int: ...
    @overload
    @staticmethod
    def e(p0: str, p1: str) -> int: ...
    @overload
    @staticmethod
    def i(p0: str, p1: str, p2: Throwable) -> int: ...
    @overload
    @staticmethod
    def i(p0: str, p1: str) -> int: ...
    @overload
    @staticmethod
    def d(p0: str, p1: str, p2: Throwable) -> int: ...
    @overload
    @staticmethod
    def d(p0: str, p1: str) -> int: ...
    @overload
    @staticmethod
    def v(p0: str, p1: str) -> int: ...
    @overload
    @staticmethod
    def v(p0: str, p1: str, p2: Throwable) -> int: ...
    @overload
    @staticmethod
    def w(p0: str, p1: Throwable) -> int: ...
    @overload
    @staticmethod
    def w(p0: str, p1: str) -> int: ...
    @overload
    @staticmethod
    def w(p0: str, p1: str, p2: Throwable) -> int: ...
