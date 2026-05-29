from typing import Any, ClassVar, overload
from java.util.Observable import Observable

class Observer:
    def update(self, arg0: Observable, arg1: Any) -> None: ...
