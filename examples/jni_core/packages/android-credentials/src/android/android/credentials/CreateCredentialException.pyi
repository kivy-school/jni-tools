from typing import Any, ClassVar, overload
from java.lang.Throwable import Throwable

class CreateCredentialException:
    TYPE_INTERRUPTED: ClassVar[str]
    TYPE_NO_CREATE_OPTIONS: ClassVar[str]
    TYPE_UNKNOWN: ClassVar[str]
    TYPE_USER_CANCELED: ClassVar[str]
    @overload
    def __init__(self, p0: str, p1: Throwable) -> None: ...
    @overload
    def __init__(self, p0: str, p1: str, p2: Throwable) -> None: ...
    @overload
    def __init__(self, p0: str, p1: str) -> None: ...
    @overload
    def __init__(self, p0: str) -> None: ...
    def getType(self) -> str: ...
