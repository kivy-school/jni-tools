from typing import Any, ClassVar, overload
from java.lang.Throwable import Throwable

class KeyExpiredException:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: str) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: Throwable) -> None: ...
