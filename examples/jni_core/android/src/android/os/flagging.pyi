from typing import Any, ClassVar, overload
from java.lang.Throwable import Throwable

class AconfigStorageReadException:
    ERROR_CANNOT_READ_STORAGE_FILE: ClassVar[int]
    ERROR_CONTAINER_NOT_FOUND: ClassVar[int]
    ERROR_GENERIC: ClassVar[int]
    ERROR_PACKAGE_NOT_FOUND: ClassVar[int]
    ERROR_STORAGE_SYSTEM_NOT_FOUND: ClassVar[int]
    @overload
    def __init__(self, p0: int, p1: Throwable) -> None: ...
    @overload
    def __init__(self, p0: int, p1: str, p2: Throwable) -> None: ...
    @overload
    def __init__(self, p0: int, p1: str) -> None: ...
    def getErrorCode(self) -> int: ...
    def getMessage(self) -> str: ...

from typing import Any, ClassVar, overload

class AconfigPackage:
    @staticmethod
    def load(p0: str) -> "AconfigPackage": ...
    def getBooleanFlagValue(self, p0: str, p1: bool) -> bool: ...

