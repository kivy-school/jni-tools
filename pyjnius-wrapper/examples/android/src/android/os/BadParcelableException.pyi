from typing import Any, ClassVar, overload
from java.lang.Exception import Exception

class BadParcelableException:
    @overload
    def __init__(self, arg0: str) -> None: ...
    @overload
    def __init__(self, arg0: Exception) -> None: ...
