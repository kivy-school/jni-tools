from typing import Any, ClassVar, overload
from java.lang.Throwable import Throwable

class GetCredentialException:
    TYPE_INTERRUPTED: ClassVar[str]
    TYPE_NO_CREDENTIAL: ClassVar[str]
    TYPE_UNKNOWN: ClassVar[str]
    TYPE_USER_CANCELED: ClassVar[str]
    @overload
    def __init__(self, arg0: str, arg1: str) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: str, arg2: Throwable) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: Throwable) -> None: ...
    @overload
    def __init__(self, arg0: str) -> None: ...
    def getType(self) -> str: ...
