from typing import Any, ClassVar, overload
from java.lang.Exception import Exception

class ErrorManager:
    GENERIC_FAILURE: ClassVar[int]
    WRITE_FAILURE: ClassVar[int]
    FLUSH_FAILURE: ClassVar[int]
    CLOSE_FAILURE: ClassVar[int]
    OPEN_FAILURE: ClassVar[int]
    FORMAT_FAILURE: ClassVar[int]
    def __init__(self) -> None: ...
    def error(self, p0: str, p1: Exception, p2: int) -> None: ...
