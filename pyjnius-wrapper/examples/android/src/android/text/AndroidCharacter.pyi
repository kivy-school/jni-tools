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
    def getDirectionalities(arg0: list[str], arg1: list[int], arg2: int) -> None: ...
    @staticmethod
    def getEastAsianWidth(arg0: str) -> int: ...
    @staticmethod
    def getEastAsianWidths(arg0: list[str], arg1: int, arg2: int, arg3: list[int]) -> None: ...
    @staticmethod
    def mirror(arg0: list[str], arg1: int, arg2: int) -> bool: ...
    @staticmethod
    def getMirror(arg0: str) -> str: ...
