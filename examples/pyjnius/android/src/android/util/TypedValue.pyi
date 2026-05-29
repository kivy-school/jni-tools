from typing import Any, ClassVar, overload
from android.util.DisplayMetrics import DisplayMetrics

class TypedValue:
    COMPLEX_MANTISSA_MASK: ClassVar[int]
    COMPLEX_MANTISSA_SHIFT: ClassVar[int]
    COMPLEX_RADIX_0p23: ClassVar[int]
    COMPLEX_RADIX_16p7: ClassVar[int]
    COMPLEX_RADIX_23p0: ClassVar[int]
    COMPLEX_RADIX_8p15: ClassVar[int]
    COMPLEX_RADIX_MASK: ClassVar[int]
    COMPLEX_RADIX_SHIFT: ClassVar[int]
    COMPLEX_UNIT_DIP: ClassVar[int]
    COMPLEX_UNIT_FRACTION: ClassVar[int]
    COMPLEX_UNIT_FRACTION_PARENT: ClassVar[int]
    COMPLEX_UNIT_IN: ClassVar[int]
    COMPLEX_UNIT_MASK: ClassVar[int]
    COMPLEX_UNIT_MM: ClassVar[int]
    COMPLEX_UNIT_PT: ClassVar[int]
    COMPLEX_UNIT_PX: ClassVar[int]
    COMPLEX_UNIT_SHIFT: ClassVar[int]
    COMPLEX_UNIT_SP: ClassVar[int]
    DATA_NULL_EMPTY: ClassVar[int]
    DATA_NULL_UNDEFINED: ClassVar[int]
    DENSITY_DEFAULT: ClassVar[int]
    DENSITY_NONE: ClassVar[int]
    TYPE_ATTRIBUTE: ClassVar[int]
    TYPE_DIMENSION: ClassVar[int]
    TYPE_FIRST_COLOR_INT: ClassVar[int]
    TYPE_FIRST_INT: ClassVar[int]
    TYPE_FLOAT: ClassVar[int]
    TYPE_FRACTION: ClassVar[int]
    TYPE_INT_BOOLEAN: ClassVar[int]
    TYPE_INT_COLOR_ARGB4: ClassVar[int]
    TYPE_INT_COLOR_ARGB8: ClassVar[int]
    TYPE_INT_COLOR_RGB4: ClassVar[int]
    TYPE_INT_COLOR_RGB8: ClassVar[int]
    TYPE_INT_DEC: ClassVar[int]
    TYPE_INT_HEX: ClassVar[int]
    TYPE_LAST_COLOR_INT: ClassVar[int]
    TYPE_LAST_INT: ClassVar[int]
    TYPE_NULL: ClassVar[int]
    TYPE_REFERENCE: ClassVar[int]
    TYPE_STRING: ClassVar[int]
    assetCookie: int
    changingConfigurations: int
    data: int
    density: int
    resourceId: int
    sourceResourceId: int
    string: str
    type: int
    def __init__(self) -> None: ...
    def toString(self) -> str: ...
    def getFloat(self) -> float: ...
    @staticmethod
    def applyDimension(p0: int, p1: float, p2: DisplayMetrics) -> float: ...
    @overload
    def coerceToString(self) -> str: ...
    @overload
    @staticmethod
    def coerceToString(p0: int, p1: int) -> str: ...
    @staticmethod
    def complexToDimension(p0: int, p1: DisplayMetrics) -> float: ...
    @staticmethod
    def complexToDimensionPixelOffset(p0: int, p1: DisplayMetrics) -> int: ...
    @staticmethod
    def complexToDimensionPixelSize(p0: int, p1: DisplayMetrics) -> int: ...
    @staticmethod
    def complexToFloat(p0: int) -> float: ...
    @staticmethod
    def complexToFraction(p0: int, p1: float, p2: float) -> float: ...
    @staticmethod
    def convertDimensionToPixels(p0: int, p1: float, p2: DisplayMetrics) -> float: ...
    @staticmethod
    def convertPixelsToDimension(p0: int, p1: float, p2: DisplayMetrics) -> float: ...
    @staticmethod
    def deriveDimension(p0: int, p1: float, p2: DisplayMetrics) -> float: ...
    def getComplexUnit(self) -> int: ...
    def isColorType(self) -> bool: ...
    def getDimension(self, p0: DisplayMetrics) -> float: ...
    def getFraction(self, p0: float, p1: float) -> float: ...
    def setTo(self, p0: "TypedValue") -> None: ...
