from typing import Any, ClassVar, overload

class TextAttribute:
    FAMILY: ClassVar["TextAttribute"]
    WEIGHT: ClassVar["TextAttribute"]
    WEIGHT_EXTRA_LIGHT: ClassVar[float]
    WEIGHT_LIGHT: ClassVar[float]
    WEIGHT_DEMILIGHT: ClassVar[float]
    WEIGHT_REGULAR: ClassVar[float]
    WEIGHT_SEMIBOLD: ClassVar[float]
    WEIGHT_MEDIUM: ClassVar[float]
    WEIGHT_DEMIBOLD: ClassVar[float]
    WEIGHT_BOLD: ClassVar[float]
    WEIGHT_HEAVY: ClassVar[float]
    WEIGHT_EXTRABOLD: ClassVar[float]
    WEIGHT_ULTRABOLD: ClassVar[float]
    WIDTH: ClassVar["TextAttribute"]
    WIDTH_CONDENSED: ClassVar[float]
    WIDTH_SEMI_CONDENSED: ClassVar[float]
    WIDTH_REGULAR: ClassVar[float]
    WIDTH_SEMI_EXTENDED: ClassVar[float]
    WIDTH_EXTENDED: ClassVar[float]
    POSTURE: ClassVar["TextAttribute"]
    POSTURE_REGULAR: ClassVar[float]
    POSTURE_OBLIQUE: ClassVar[float]
    SIZE: ClassVar["TextAttribute"]
    TRANSFORM: ClassVar["TextAttribute"]
    SUPERSCRIPT: ClassVar["TextAttribute"]
    SUPERSCRIPT_SUPER: ClassVar[int]
    SUPERSCRIPT_SUB: ClassVar[int]
    FONT: ClassVar["TextAttribute"]
    CHAR_REPLACEMENT: ClassVar["TextAttribute"]
    FOREGROUND: ClassVar["TextAttribute"]
    BACKGROUND: ClassVar["TextAttribute"]
    UNDERLINE: ClassVar["TextAttribute"]
    UNDERLINE_ON: ClassVar[int]
    STRIKETHROUGH: ClassVar["TextAttribute"]
    STRIKETHROUGH_ON: ClassVar[bool]
    RUN_DIRECTION: ClassVar["TextAttribute"]
    RUN_DIRECTION_LTR: ClassVar[bool]
    RUN_DIRECTION_RTL: ClassVar[bool]
    BIDI_EMBEDDING: ClassVar["TextAttribute"]
    JUSTIFICATION: ClassVar["TextAttribute"]
    JUSTIFICATION_FULL: ClassVar[float]
    JUSTIFICATION_NONE: ClassVar[float]
    INPUT_METHOD_HIGHLIGHT: ClassVar["TextAttribute"]
    INPUT_METHOD_UNDERLINE: ClassVar["TextAttribute"]
    UNDERLINE_LOW_ONE_PIXEL: ClassVar[int]
    UNDERLINE_LOW_TWO_PIXEL: ClassVar[int]
    UNDERLINE_LOW_DOTTED: ClassVar[int]
    UNDERLINE_LOW_GRAY: ClassVar[int]
    UNDERLINE_LOW_DASHED: ClassVar[int]
    SWAP_COLORS: ClassVar["TextAttribute"]
    SWAP_COLORS_ON: ClassVar[bool]
    NUMERIC_SHAPING: ClassVar["TextAttribute"]
    KERNING: ClassVar["TextAttribute"]
    KERNING_ON: ClassVar[int]
    LIGATURES: ClassVar["TextAttribute"]
    LIGATURES_ON: ClassVar[int]
    TRACKING: ClassVar["TextAttribute"]
    TRACKING_TIGHT: ClassVar[float]
    TRACKING_LOOSE: ClassVar[float]
    LANGUAGE: ClassVar[Any]
    READING: ClassVar[Any]
    INPUT_METHOD_SEGMENT: ClassVar[Any]

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
    def shape(self, p0: Any, p1: int, p2: int, p3: Any) -> None: ...
    @overload
    def shape(self, p0: Any, p1: int, p2: int, p3: int) -> None: ...
    @overload
    def shape(self, p0: Any, p1: int, p2: int) -> None: ...
    def isContextual(self) -> bool: ...
    def getRanges(self) -> int: ...
    @overload
    @staticmethod
    def getShaper(p0: Any) -> "NumericShaper": ...
    @overload
    @staticmethod
    def getShaper(p0: int) -> "NumericShaper": ...
    @overload
    @staticmethod
    def getContextualShaper(p0: int) -> "NumericShaper": ...
    @overload
    @staticmethod
    def getContextualShaper(p0: set, p1: Any) -> "NumericShaper": ...
    @overload
    @staticmethod
    def getContextualShaper(p0: int, p1: int) -> "NumericShaper": ...
    @overload
    @staticmethod
    def getContextualShaper(p0: set) -> "NumericShaper": ...
    def getRangeSet(self) -> set: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...

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

