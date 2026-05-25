from typing import Any, ClassVar, overload
from java.lang.Exception import Exception

class ErrorManager:
    CLOSE_FAILURE: ClassVar[int]
    FLUSH_FAILURE: ClassVar[int]
    FORMAT_FAILURE: ClassVar[int]
    GENERIC_FAILURE: ClassVar[int]
    OPEN_FAILURE: ClassVar[int]
    WRITE_FAILURE: ClassVar[int]
    def __init__(self) -> None: ...
    def error(self, arg0: str, arg1: Exception, arg2: int) -> None: ...
