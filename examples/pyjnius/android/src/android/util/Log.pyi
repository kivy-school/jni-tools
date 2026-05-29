from typing import Any, ClassVar, overload
from java.lang.Throwable import Throwable

class Log:
    ASSERT: ClassVar[int]
    DEBUG: ClassVar[int]
    ERROR: ClassVar[int]
    INFO: ClassVar[int]
    VERBOSE: ClassVar[int]
    WARN: ClassVar[int]
    @overload
    @staticmethod
    def v(arg0: str, arg1: str) -> int: ...
    @overload
    @staticmethod
    def v(arg0: str, arg1: str, arg2: Throwable) -> int: ...
    @overload
    @staticmethod
    def d(arg0: str, arg1: str) -> int: ...
    @overload
    @staticmethod
    def d(arg0: str, arg1: str, arg2: Throwable) -> int: ...
    @overload
    @staticmethod
    def i(arg0: str, arg1: str) -> int: ...
    @overload
    @staticmethod
    def i(arg0: str, arg1: str, arg2: Throwable) -> int: ...
    @overload
    @staticmethod
    def w(arg0: str, arg1: str) -> int: ...
    @overload
    @staticmethod
    def w(arg0: str, arg1: str, arg2: Throwable) -> int: ...
    @overload
    @staticmethod
    def w(arg0: str, arg1: Throwable) -> int: ...
    @staticmethod
    def isLoggable(arg0: str, arg1: int) -> bool: ...
    @overload
    @staticmethod
    def e(arg0: str, arg1: str) -> int: ...
    @overload
    @staticmethod
    def e(arg0: str, arg1: str, arg2: Throwable) -> int: ...
    @overload
    @staticmethod
    def wtf(arg0: str, arg1: str) -> int: ...
    @overload
    @staticmethod
    def wtf(arg0: str, arg1: Throwable) -> int: ...
    @overload
    @staticmethod
    def wtf(arg0: str, arg1: str, arg2: Throwable) -> int: ...
    @staticmethod
    def getStackTraceString(arg0: Throwable) -> str: ...
    @staticmethod
    def println(arg0: int, arg1: str, arg2: str) -> int: ...
