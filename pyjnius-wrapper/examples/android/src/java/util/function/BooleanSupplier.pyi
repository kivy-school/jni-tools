from typing import Any, ClassVar, overload

class BooleanSupplier:
    def getAsBoolean(self) -> bool: ...
