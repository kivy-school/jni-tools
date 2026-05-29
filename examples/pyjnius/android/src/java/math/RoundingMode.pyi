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
    UP: ClassVar["RoundingMode"]
    DOWN: ClassVar["RoundingMode"]
    CEILING: ClassVar["RoundingMode"]
    FLOOR: ClassVar["RoundingMode"]
    HALF_UP: ClassVar["RoundingMode"]
    HALF_DOWN: ClassVar["RoundingMode"]
    HALF_EVEN: ClassVar["RoundingMode"]
    UNNECESSARY: ClassVar["RoundingMode"]
    @staticmethod
    def values() -> Any: ...
    @overload
    @staticmethod
    def valueOf(p0: str) -> "RoundingMode": ...
    @overload
    @staticmethod
    def valueOf(p0: int) -> "RoundingMode": ...
