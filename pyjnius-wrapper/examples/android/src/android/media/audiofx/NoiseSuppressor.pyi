from typing import Any, ClassVar, overload

class NoiseSuppressor:
    @staticmethod
    def isAvailable() -> bool: ...
    @staticmethod
    def create(arg0: int) -> "NoiseSuppressor": ...
