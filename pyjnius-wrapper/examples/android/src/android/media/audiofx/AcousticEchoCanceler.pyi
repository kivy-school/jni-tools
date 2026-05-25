from typing import Any, ClassVar, overload

class AcousticEchoCanceler:
    @staticmethod
    def isAvailable() -> bool: ...
    @staticmethod
    def create(arg0: int) -> "AcousticEchoCanceler": ...
