from typing import Any, ClassVar, overload
from java.util.Formatter import Formatter

class Formattable:
    def formatTo(self, p0: Formatter, p1: int, p2: int, p3: int) -> None: ...
