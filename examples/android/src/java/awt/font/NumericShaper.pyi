from typing import Any, ClassVar, overload

class NumericShaper:
    ALL_RANGES: ClassVar[int]
    ARABIC: ClassVar[int]
    BENGALI: ClassVar[int]
    DEVANAGARI: ClassVar[int]
    EASTERN_ARABIC: ClassVar[int]
    ETHIOPIC: ClassVar[int]
    EUROPEAN: ClassVar[int]
    GUJARATI: ClassVar[int]
    GURMUKHI: ClassVar[int]
    KANNADA: ClassVar[int]
    KHMER: ClassVar[int]
    LAO: ClassVar[int]
    MALAYALAM: ClassVar[int]
    MONGOLIAN: ClassVar[int]
    MYANMAR: ClassVar[int]
    ORIYA: ClassVar[int]
    TAMIL: ClassVar[int]
    TELUGU: ClassVar[int]
    THAI: ClassVar[int]
    TIBETAN: ClassVar[int]
    @overload
    @staticmethod
    def getShaper(arg0: int) -> "NumericShaper": ...
    @overload
    @staticmethod
    def getShaper(arg0: "Range") -> "NumericShaper": ...
    @overload
    @staticmethod
    def getContextualShaper(arg0: int) -> "NumericShaper": ...
    @overload
    @staticmethod
    def getContextualShaper(arg0: set) -> "NumericShaper": ...
    @overload
    @staticmethod
    def getContextualShaper(arg0: int, arg1: int) -> "NumericShaper": ...
    @overload
    @staticmethod
    def getContextualShaper(arg0: set, arg1: "Range") -> "NumericShaper": ...
    @overload
    def shape(self, arg0: list[str], arg1: int, arg2: int) -> None: ...
    @overload
    def shape(self, arg0: list[str], arg1: int, arg2: int, arg3: int) -> None: ...
    @overload
    def shape(self, arg0: list[str], arg1: int, arg2: int, arg3: "Range") -> None: ...
    def isContextual(self) -> bool: ...
    def getRanges(self) -> int: ...
    def getRangeSet(self) -> set: ...
    def hashCode(self) -> int: ...
    def equals(self, arg0: Any) -> bool: ...
    def toString(self) -> str: ...

    class Range:
        EUROPEAN: ClassVar["Range"]
        ARABIC: ClassVar["Range"]
        EASTERN_ARABIC: ClassVar["Range"]
        DEVANAGARI: ClassVar["Range"]
        BENGALI: ClassVar["Range"]
        GURMUKHI: ClassVar["Range"]
        GUJARATI: ClassVar["Range"]
        ORIYA: ClassVar["Range"]
        TAMIL: ClassVar["Range"]
        TELUGU: ClassVar["Range"]
        KANNADA: ClassVar["Range"]
        MALAYALAM: ClassVar["Range"]
        THAI: ClassVar["Range"]
        LAO: ClassVar["Range"]
        TIBETAN: ClassVar["Range"]
        MYANMAR: ClassVar["Range"]
        ETHIOPIC: ClassVar["Range"]
        KHMER: ClassVar["Range"]
        MONGOLIAN: ClassVar["Range"]
        NKO: ClassVar["Range"]
        MYANMAR_SHAN: ClassVar["Range"]
        LIMBU: ClassVar["Range"]
        NEW_TAI_LUE: ClassVar["Range"]
        BALINESE: ClassVar["Range"]
        SUNDANESE: ClassVar["Range"]
        LEPCHA: ClassVar["Range"]
        OL_CHIKI: ClassVar["Range"]
        VAI: ClassVar["Range"]
        SAURASHTRA: ClassVar["Range"]
        KAYAH_LI: ClassVar["Range"]
        CHAM: ClassVar["Range"]
        TAI_THAM_HORA: ClassVar["Range"]
        TAI_THAM_THAM: ClassVar["Range"]
        JAVANESE: ClassVar["Range"]
        MEETEI_MAYEK: ClassVar["Range"]
        @staticmethod
        def values() -> list["Range"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "Range": ...
