from typing import Any, ClassVar, overload

class RoundingMode:
    UP: ClassVar["RoundingMode"]
    DOWN: ClassVar["RoundingMode"]
    CEILING: ClassVar["RoundingMode"]
    FLOOR: ClassVar["RoundingMode"]
    HALF_UP: ClassVar["RoundingMode"]
    HALF_DOWN: ClassVar["RoundingMode"]
    HALF_EVEN: ClassVar["RoundingMode"]
    UNNECESSARY: ClassVar["RoundingMode"]
    @staticmethod
    def values() -> list["RoundingMode"]: ...
    @overload
    @staticmethod
    def valueOf(arg0: str) -> "RoundingMode": ...
    @overload
    @staticmethod
    def valueOf(arg0: int) -> "RoundingMode": ...
