from typing import Any, ClassVar, overload
from java.util.Formatter import Formatter

class Formattable:
    def formatTo(self, arg0: Formatter, arg1: int, arg2: int, arg3: int) -> None: ...
