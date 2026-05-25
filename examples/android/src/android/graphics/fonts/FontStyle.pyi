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
    def __init__(self, arg0: int, arg1: int) -> None: ...
    def getWeight(self) -> int: ...
    def getSlant(self) -> int: ...
    def equals(self, arg0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
