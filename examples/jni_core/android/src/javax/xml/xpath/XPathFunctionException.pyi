from typing import Any, ClassVar, overload
from java.lang.Throwable import Throwable

class XPathFunctionException:
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self, p0: Throwable) -> None: ...
