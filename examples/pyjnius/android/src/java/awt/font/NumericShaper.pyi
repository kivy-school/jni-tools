from typing import Any, ClassVar, overload

class NumericShaper:
    EUROPEAN: ClassVar[int]
    ARABIC: ClassVar[int]
    EASTERN_ARABIC: ClassVar[int]
    DEVANAGARI: ClassVar[int]
    BENGALI: ClassVar[int]
    GURMUKHI: ClassVar[int]
    GUJARATI: ClassVar[int]
    ORIYA: ClassVar[int]
    TAMIL: ClassVar[int]
    TELUGU: ClassVar[int]
    KANNADA: ClassVar[int]
    MALAYALAM: ClassVar[int]
    THAI: ClassVar[int]
    LAO: ClassVar[int]
    TIBETAN: ClassVar[int]
    MYANMAR: ClassVar[int]
    ETHIOPIC: ClassVar[int]
    KHMER: ClassVar[int]
    MONGOLIAN: ClassVar[int]
    ALL_RANGES: ClassVar[int]
    @overload
    def shape(self, p0: Any, p1: int, p2: int) -> None: ...
    @overload
    def shape(self, p0: Any, p1: int, p2: int, p3: Any) -> None: ...
    @overload
    def shape(self, p0: Any, p1: int, p2: int, p3: int) -> None: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def getRanges(self) -> int: ...
    def isContextual(self) -> bool: ...
    @overload
    @staticmethod
    def getShaper(p0: Any) -> "NumericShaper": ...
    @overload
    @staticmethod
    def getShaper(p0: int) -> "NumericShaper": ...
    @overload
    @staticmethod
    def getContextualShaper(p0: set, p1: Any) -> "NumericShaper": ...
    @overload
    @staticmethod
    def getContextualShaper(p0: int, p1: int) -> "NumericShaper": ...
    @overload
    @staticmethod
    def getContextualShaper(p0: set) -> "NumericShaper": ...
    @overload
    @staticmethod
    def getContextualShaper(p0: int) -> "NumericShaper": ...
    def getRangeSet(self) -> set: ...

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
        SINHALA: ClassVar["Range"]
        MYANMAR_TAI_LAING: ClassVar["Range"]
        EUROPEAN: ClassVar[Any]
        ARABIC: ClassVar[Any]
        EASTERN_ARABIC: ClassVar[Any]
        DEVANAGARI: ClassVar[Any]
        BENGALI: ClassVar[Any]
        GURMUKHI: ClassVar[Any]
        GUJARATI: ClassVar[Any]
        ORIYA: ClassVar[Any]
        TAMIL: ClassVar[Any]
        TELUGU: ClassVar[Any]
        KANNADA: ClassVar[Any]
        MALAYALAM: ClassVar[Any]
        THAI: ClassVar[Any]
        LAO: ClassVar[Any]
        TIBETAN: ClassVar[Any]
        MYANMAR: ClassVar[Any]
        ETHIOPIC: ClassVar[Any]
        KHMER: ClassVar[Any]
        MONGOLIAN: ClassVar[Any]
        NKO: ClassVar[Any]
        MYANMAR_SHAN: ClassVar[Any]
        LIMBU: ClassVar[Any]
        NEW_TAI_LUE: ClassVar[Any]
        BALINESE: ClassVar[Any]
        SUNDANESE: ClassVar[Any]
        LEPCHA: ClassVar[Any]
        OL_CHIKI: ClassVar[Any]
        VAI: ClassVar[Any]
        SAURASHTRA: ClassVar[Any]
        KAYAH_LI: ClassVar[Any]
        CHAM: ClassVar[Any]
        TAI_THAM_HORA: ClassVar[Any]
        TAI_THAM_THAM: ClassVar[Any]
        JAVANESE: ClassVar[Any]
        MEETEI_MAYEK: ClassVar[Any]
        SINHALA: ClassVar[Any]
        MYANMAR_TAI_LAING: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
