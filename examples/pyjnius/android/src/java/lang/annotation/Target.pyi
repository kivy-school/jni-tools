from typing import Any, ClassVar, overload
from java.lang.annotation.ElementType import ElementType

class Target:
    def value(self) -> list[ElementType]: ...
