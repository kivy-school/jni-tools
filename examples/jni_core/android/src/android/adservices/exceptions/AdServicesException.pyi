from typing import Any, ClassVar, overload
from java.lang.Throwable import Throwable

class AdServicesException:
    @overload
    def __init__(self, p0: str, p1: Throwable) -> None: ...
    @overload
    def __init__(self, p0: str) -> None: ...
