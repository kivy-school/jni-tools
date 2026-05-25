from typing import Any, ClassVar, overload
from java.lang.Throwable import Throwable

class InvalidPropertiesFormatException:
    @overload
    def __init__(self, arg0: Throwable) -> None: ...
    @overload
    def __init__(self, arg0: str) -> None: ...
