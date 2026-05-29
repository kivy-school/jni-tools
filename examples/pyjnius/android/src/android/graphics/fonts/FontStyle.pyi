from typing import Any, ClassVar, overload

class FontStyle:
    FONT_SLANT_ITALIC: ClassVar[int]
    FONT_SLANT_UPRIGHT: ClassVar[int]
    FONT_WEIGHT_BLACK: ClassVar[int]
    FONT_WEIGHT_BOLD: ClassVar[int]
    FONT_WEIGHT_EXTRA_BOLD: ClassVar[int]
    FONT_WEIGHT_EXTRA_LIGHT: ClassVar[int]
    FONT_WEIGHT_LIGHT: ClassVar[int]
    FONT_WEIGHT_MAX: ClassVar[int]
    FONT_WEIGHT_MEDIUM: ClassVar[int]
    FONT_WEIGHT_MIN: ClassVar[int]
    FONT_WEIGHT_NORMAL: ClassVar[int]
    FONT_WEIGHT_SEMI_BOLD: ClassVar[int]
    FONT_WEIGHT_THIN: ClassVar[int]
    FONT_WEIGHT_UNSPECIFIED: ClassVar[int]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int) -> None: ...
    def getSlant(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def getWeight(self) -> int: ...
