from typing import Any, ClassVar, overload

class AutomaticGainControl:
    @staticmethod
    def isAvailable() -> bool: ...
    @staticmethod
    def create(arg0: int) -> "AutomaticGainControl": ...
