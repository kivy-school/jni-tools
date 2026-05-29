from typing import Any, ClassVar, overload
from java.lang.Exception import Exception

class BadParcelableException:
    @overload
    def __init__(self, p0: Exception) -> None: ...
    @overload
    def __init__(self, p0: str) -> None: ...
