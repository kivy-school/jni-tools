from typing import Any, ClassVar, overload
from java.util.Observable import Observable

class Observer:
    def update(self, p0: Observable, p1: Any) -> None: ...
