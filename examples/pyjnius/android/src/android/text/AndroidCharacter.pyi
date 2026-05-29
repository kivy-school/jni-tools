from typing import Any, ClassVar, overload

class AndroidCharacter:
    EAST_ASIAN_WIDTH_AMBIGUOUS: ClassVar[int]
    EAST_ASIAN_WIDTH_FULL_WIDTH: ClassVar[int]
    EAST_ASIAN_WIDTH_HALF_WIDTH: ClassVar[int]
    EAST_ASIAN_WIDTH_NARROW: ClassVar[int]
    EAST_ASIAN_WIDTH_NEUTRAL: ClassVar[int]
    EAST_ASIAN_WIDTH_WIDE: ClassVar[int]
    def __init__(self) -> None: ...
    @staticmethod
    def getEastAsianWidth(p0: str) -> int: ...
    @staticmethod
    def getMirror(p0: str) -> str: ...
    @staticmethod
    def getEastAsianWidths(p0: Any, p1: int, p2: int, p3: Any) -> None: ...
    @staticmethod
    def getDirectionalities(p0: Any, p1: Any, p2: int) -> None: ...
    @staticmethod
    def mirror(p0: Any, p1: int, p2: int) -> bool: ...
