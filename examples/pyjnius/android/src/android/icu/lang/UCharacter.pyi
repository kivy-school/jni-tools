from typing import Any, ClassVar, overload
from android.icu.text.BreakIterator import BreakIterator
from android.icu.util.RangeValueIterator import RangeValueIterator
from android.icu.util.ULocale import ULocale
from android.icu.util.ValueIterator import ValueIterator
from android.icu.util.VersionInfo import VersionInfo
from java.util.Locale import Locale

class UCharacter:
    FOLD_CASE_DEFAULT: ClassVar[int]
    FOLD_CASE_EXCLUDE_SPECIAL_I: ClassVar[int]
    MAX_CODE_POINT: ClassVar[int]
    MAX_HIGH_SURROGATE: ClassVar[str]
    MAX_LOW_SURROGATE: ClassVar[str]
    MAX_RADIX: ClassVar[int]
    MAX_SURROGATE: ClassVar[str]
    MAX_VALUE: ClassVar[int]
    MIN_CODE_POINT: ClassVar[int]
    MIN_HIGH_SURROGATE: ClassVar[str]
    MIN_LOW_SURROGATE: ClassVar[str]
    MIN_RADIX: ClassVar[int]
    MIN_SUPPLEMENTARY_CODE_POINT: ClassVar[int]
    MIN_SURROGATE: ClassVar[str]
    MIN_VALUE: ClassVar[int]
    NO_NUMERIC_VALUE: ClassVar[float]
    REPLACEMENT_CHAR: ClassVar[int]
    SUPPLEMENTARY_MIN_VALUE: ClassVar[int]
    TITLECASE_NO_BREAK_ADJUSTMENT: ClassVar[int]
    TITLECASE_NO_LOWERCASE: ClassVar[int]
    @overload
    @staticmethod
    def digit(arg0: int, arg1: int) -> int: ...
    @overload
    @staticmethod
    def digit(arg0: int) -> int: ...
    @staticmethod
    def getNumericValue(arg0: int) -> int: ...
    @staticmethod
    def getUnicodeNumericValue(arg0: int) -> float: ...
    @staticmethod
    def getType(arg0: int) -> int: ...
    @staticmethod
    def isDefined(arg0: int) -> bool: ...
    @staticmethod
    def isDigit(arg0: int) -> bool: ...
    @staticmethod
    def isISOControl(arg0: int) -> bool: ...
    @staticmethod
    def isLetter(arg0: int) -> bool: ...
    @staticmethod
    def isLetterOrDigit(arg0: int) -> bool: ...
    @staticmethod
    def isJavaIdentifierStart(arg0: int) -> bool: ...
    @staticmethod
    def isJavaIdentifierPart(arg0: int) -> bool: ...
    @staticmethod
    def isLowerCase(arg0: int) -> bool: ...
    @staticmethod
    def isWhitespace(arg0: int) -> bool: ...
    @staticmethod
    def isSpaceChar(arg0: int) -> bool: ...
    @staticmethod
    def isTitleCase(arg0: int) -> bool: ...
    @staticmethod
    def isUnicodeIdentifierPart(arg0: int) -> bool: ...
    @staticmethod
    def isUnicodeIdentifierStart(arg0: int) -> bool: ...
    @staticmethod
    def isIdentifierIgnorable(arg0: int) -> bool: ...
    @staticmethod
    def isUpperCase(arg0: int) -> bool: ...
    @overload
    @staticmethod
    def toLowerCase(arg0: int) -> int: ...
    @overload
    @staticmethod
    def toLowerCase(arg0: str) -> str: ...
    @overload
    @staticmethod
    def toLowerCase(arg0: Locale, arg1: str) -> str: ...
    @overload
    @staticmethod
    def toLowerCase(arg0: ULocale, arg1: str) -> str: ...
    @staticmethod
    def toString(arg0: int) -> str: ...
    @overload
    @staticmethod
    def toTitleCase(arg0: int) -> int: ...
    @overload
    @staticmethod
    def toTitleCase(arg0: str, arg1: BreakIterator) -> str: ...
    @overload
    @staticmethod
    def toTitleCase(arg0: Locale, arg1: str, arg2: BreakIterator) -> str: ...
    @overload
    @staticmethod
    def toTitleCase(arg0: ULocale, arg1: str, arg2: BreakIterator) -> str: ...
    @overload
    @staticmethod
    def toTitleCase(arg0: ULocale, arg1: str, arg2: BreakIterator, arg3: int) -> str: ...
    @overload
    @staticmethod
    def toTitleCase(arg0: Locale, arg1: str, arg2: BreakIterator, arg3: int) -> str: ...
    @overload
    @staticmethod
    def toUpperCase(arg0: int) -> int: ...
    @overload
    @staticmethod
    def toUpperCase(arg0: str) -> str: ...
    @overload
    @staticmethod
    def toUpperCase(arg0: Locale, arg1: str) -> str: ...
    @overload
    @staticmethod
    def toUpperCase(arg0: ULocale, arg1: str) -> str: ...
    @staticmethod
    def isSupplementary(arg0: int) -> bool: ...
    @staticmethod
    def isBMP(arg0: int) -> bool: ...
    @staticmethod
    def isPrintable(arg0: int) -> bool: ...
    @staticmethod
    def isBaseForm(arg0: int) -> bool: ...
    @staticmethod
    def getDirection(arg0: int) -> int: ...
    @staticmethod
    def isMirrored(arg0: int) -> bool: ...
    @staticmethod
    def getMirror(arg0: int) -> int: ...
    @staticmethod
    def getBidiPairedBracket(arg0: int) -> int: ...
    @staticmethod
    def getCombiningClass(arg0: int) -> int: ...
    @overload
    @staticmethod
    def isLegal(arg0: int) -> bool: ...
    @overload
    @staticmethod
    def isLegal(arg0: str) -> bool: ...
    @staticmethod
    def getUnicodeVersion() -> VersionInfo: ...
    @overload
    @staticmethod
    def getName(arg0: int) -> str: ...
    @overload
    @staticmethod
    def getName(arg0: str, arg1: str) -> str: ...
    @staticmethod
    def getExtendedName(arg0: int) -> str: ...
    @staticmethod
    def getNameAlias(arg0: int) -> str: ...
    @staticmethod
    def getCharFromName(arg0: str) -> int: ...
    @staticmethod
    def getCharFromExtendedName(arg0: str) -> int: ...
    @staticmethod
    def getCharFromNameAlias(arg0: str) -> int: ...
    @staticmethod
    def getPropertyName(arg0: int, arg1: int) -> str: ...
    @staticmethod
    def getPropertyEnum(arg0: str) -> int: ...
    @staticmethod
    def getPropertyValueName(arg0: int, arg1: int, arg2: int) -> str: ...
    @staticmethod
    def getPropertyValueEnum(arg0: int, arg1: str) -> int: ...
    @overload
    @staticmethod
    def getCodePoint(arg0: int, arg1: int) -> int: ...
    @overload
    @staticmethod
    def getCodePoint(arg0: str, arg1: str) -> int: ...
    @overload
    @staticmethod
    def getCodePoint(arg0: str) -> int: ...
    @overload
    @staticmethod
    def foldCase(arg0: int, arg1: bool) -> int: ...
    @overload
    @staticmethod
    def foldCase(arg0: str, arg1: bool) -> str: ...
    @overload
    @staticmethod
    def foldCase(arg0: int, arg1: int) -> int: ...
    @overload
    @staticmethod
    def foldCase(arg0: str, arg1: int) -> str: ...
    @staticmethod
    def getHanNumericValue(arg0: int) -> int: ...
    @staticmethod
    def getTypeIterator() -> RangeValueIterator: ...
    @staticmethod
    def getNameIterator() -> ValueIterator: ...
    @staticmethod
    def getExtendedNameIterator() -> ValueIterator: ...
    @staticmethod
    def getAge(arg0: int) -> VersionInfo: ...
    @overload
    @staticmethod
    def hasBinaryProperty(arg0: int, arg1: int) -> bool: ...
    @overload
    @staticmethod
    def hasBinaryProperty(arg0: str, arg1: int) -> bool: ...
    @staticmethod
    def isUAlphabetic(arg0: int) -> bool: ...
    @staticmethod
    def isULowercase(arg0: int) -> bool: ...
    @staticmethod
    def isUUppercase(arg0: int) -> bool: ...
    @staticmethod
    def isUWhiteSpace(arg0: int) -> bool: ...
    @staticmethod
    def getIntPropertyValue(arg0: int, arg1: int) -> int: ...
    @staticmethod
    def getIntPropertyMinValue(arg0: int) -> int: ...
    @staticmethod
    def getIntPropertyMaxValue(arg0: int) -> int: ...
    @staticmethod
    def forDigit(arg0: int, arg1: int) -> str: ...
    @staticmethod
    def isValidCodePoint(arg0: int) -> bool: ...
    @staticmethod
    def isSupplementaryCodePoint(arg0: int) -> bool: ...
    @overload
    @staticmethod
    def isHighSurrogate(arg0: int) -> bool: ...
    @overload
    @staticmethod
    def isHighSurrogate(arg0: str) -> bool: ...
    @overload
    @staticmethod
    def isLowSurrogate(arg0: int) -> bool: ...
    @overload
    @staticmethod
    def isLowSurrogate(arg0: str) -> bool: ...
    @overload
    @staticmethod
    def isSurrogatePair(arg0: int, arg1: int) -> bool: ...
    @overload
    @staticmethod
    def isSurrogatePair(arg0: str, arg1: str) -> bool: ...
    @staticmethod
    def charCount(arg0: int) -> int: ...
    @overload
    @staticmethod
    def toCodePoint(arg0: int, arg1: int) -> int: ...
    @overload
    @staticmethod
    def toCodePoint(arg0: str, arg1: str) -> int: ...
    @overload
    @staticmethod
    def codePointAt(arg0: str, arg1: int) -> int: ...
    @overload
    @staticmethod
    def codePointAt(arg0: list[str], arg1: int) -> int: ...
    @overload
    @staticmethod
    def codePointAt(arg0: list[str], arg1: int, arg2: int) -> int: ...
    @overload
    @staticmethod
    def codePointBefore(arg0: str, arg1: int) -> int: ...
    @overload
    @staticmethod
    def codePointBefore(arg0: list[str], arg1: int) -> int: ...
    @overload
    @staticmethod
    def codePointBefore(arg0: list[str], arg1: int, arg2: int) -> int: ...
    @overload
    @staticmethod
    def toChars(arg0: int, arg1: list[str], arg2: int) -> int: ...
    @overload
    @staticmethod
    def toChars(arg0: int) -> list[str]: ...
    @staticmethod
    def getDirectionality(arg0: int) -> int: ...
    @overload
    @staticmethod
    def codePointCount(arg0: str, arg1: int, arg2: int) -> int: ...
    @overload
    @staticmethod
    def codePointCount(arg0: list[str], arg1: int, arg2: int) -> int: ...
    @overload
    @staticmethod
    def offsetByCodePoints(arg0: str, arg1: int, arg2: int) -> int: ...
    @overload
    @staticmethod
    def offsetByCodePoints(arg0: list[str], arg1: int, arg2: int, arg3: int, arg4: int) -> int: ...

    class BidiPairedBracketType:
        CLOSE: ClassVar[int]
        NONE: ClassVar[int]
        OPEN: ClassVar[int]

    class DecompositionType:
        CANONICAL: ClassVar[int]
        CIRCLE: ClassVar[int]
        COMPAT: ClassVar[int]
        FINAL: ClassVar[int]
        FONT: ClassVar[int]
        FRACTION: ClassVar[int]
        INITIAL: ClassVar[int]
        ISOLATED: ClassVar[int]
        MEDIAL: ClassVar[int]
        NARROW: ClassVar[int]
        NOBREAK: ClassVar[int]
        NONE: ClassVar[int]
        SMALL: ClassVar[int]
        SQUARE: ClassVar[int]
        SUB: ClassVar[int]
        SUPER: ClassVar[int]
        VERTICAL: ClassVar[int]
        WIDE: ClassVar[int]

    class EastAsianWidth:
        AMBIGUOUS: ClassVar[int]
        FULLWIDTH: ClassVar[int]
        HALFWIDTH: ClassVar[int]
        NARROW: ClassVar[int]
        NEUTRAL: ClassVar[int]
        WIDE: ClassVar[int]

    class GraphemeClusterBreak:
        CONTROL: ClassVar[int]
        CR: ClassVar[int]
        EXTEND: ClassVar[int]
        E_BASE: ClassVar[int]
        E_BASE_GAZ: ClassVar[int]
        E_MODIFIER: ClassVar[int]
        GLUE_AFTER_ZWJ: ClassVar[int]
        L: ClassVar[int]
        LF: ClassVar[int]
        LV: ClassVar[int]
        LVT: ClassVar[int]
        OTHER: ClassVar[int]
        PREPEND: ClassVar[int]
        REGIONAL_INDICATOR: ClassVar[int]
        SPACING_MARK: ClassVar[int]
        T: ClassVar[int]
        V: ClassVar[int]
        ZWJ: ClassVar[int]

    class HangulSyllableType:
        LEADING_JAMO: ClassVar[int]
        LVT_SYLLABLE: ClassVar[int]
        LV_SYLLABLE: ClassVar[int]
        NOT_APPLICABLE: ClassVar[int]
        TRAILING_JAMO: ClassVar[int]
        VOWEL_JAMO: ClassVar[int]

    class IndicPositionalCategory:
        BOTTOM: ClassVar[int]
        BOTTOM_AND_LEFT: ClassVar[int]
        BOTTOM_AND_RIGHT: ClassVar[int]
        LEFT: ClassVar[int]
        LEFT_AND_RIGHT: ClassVar[int]
        NA: ClassVar[int]
        OVERSTRUCK: ClassVar[int]
        RIGHT: ClassVar[int]
        TOP: ClassVar[int]
        TOP_AND_BOTTOM: ClassVar[int]
        TOP_AND_BOTTOM_AND_LEFT: ClassVar[int]
        TOP_AND_BOTTOM_AND_RIGHT: ClassVar[int]
        TOP_AND_LEFT: ClassVar[int]
        TOP_AND_LEFT_AND_RIGHT: ClassVar[int]
        TOP_AND_RIGHT: ClassVar[int]
        VISUAL_ORDER_LEFT: ClassVar[int]

    class IndicSyllabicCategory:
        AVAGRAHA: ClassVar[int]
        BINDU: ClassVar[int]
        BRAHMI_JOINING_NUMBER: ClassVar[int]
        CANTILLATION_MARK: ClassVar[int]
        CONSONANT: ClassVar[int]
        CONSONANT_DEAD: ClassVar[int]
        CONSONANT_FINAL: ClassVar[int]
        CONSONANT_HEAD_LETTER: ClassVar[int]
        CONSONANT_INITIAL_POSTFIXED: ClassVar[int]
        CONSONANT_KILLER: ClassVar[int]
        CONSONANT_MEDIAL: ClassVar[int]
        CONSONANT_PLACEHOLDER: ClassVar[int]
        CONSONANT_PRECEDING_REPHA: ClassVar[int]
        CONSONANT_PREFIXED: ClassVar[int]
        CONSONANT_SUBJOINED: ClassVar[int]
        CONSONANT_SUCCEEDING_REPHA: ClassVar[int]
        CONSONANT_WITH_STACKER: ClassVar[int]
        GEMINATION_MARK: ClassVar[int]
        INVISIBLE_STACKER: ClassVar[int]
        JOINER: ClassVar[int]
        MODIFYING_LETTER: ClassVar[int]
        NON_JOINER: ClassVar[int]
        NUKTA: ClassVar[int]
        NUMBER: ClassVar[int]
        NUMBER_JOINER: ClassVar[int]
        OTHER: ClassVar[int]
        PURE_KILLER: ClassVar[int]
        REGISTER_SHIFTER: ClassVar[int]
        SYLLABLE_MODIFIER: ClassVar[int]
        TONE_LETTER: ClassVar[int]
        TONE_MARK: ClassVar[int]
        VIRAMA: ClassVar[int]
        VISARGA: ClassVar[int]
        VOWEL: ClassVar[int]
        VOWEL_DEPENDENT: ClassVar[int]
        VOWEL_INDEPENDENT: ClassVar[int]

    class JoiningGroup:
        AFRICAN_FEH: ClassVar[int]
        AFRICAN_NOON: ClassVar[int]
        AFRICAN_QAF: ClassVar[int]
        AIN: ClassVar[int]
        ALAPH: ClassVar[int]
        ALEF: ClassVar[int]
        BEH: ClassVar[int]
        BETH: ClassVar[int]
        BURUSHASKI_YEH_BARREE: ClassVar[int]
        DAL: ClassVar[int]
        DALATH_RISH: ClassVar[int]
        E: ClassVar[int]
        FARSI_YEH: ClassVar[int]
        FE: ClassVar[int]
        FEH: ClassVar[int]
        FINAL_SEMKATH: ClassVar[int]
        GAF: ClassVar[int]
        GAMAL: ClassVar[int]
        HAH: ClassVar[int]
        HAMZA_ON_HEH_GOAL: ClassVar[int]
        HANIFI_ROHINGYA_KINNA_YA: ClassVar[int]
        HANIFI_ROHINGYA_PA: ClassVar[int]
        HE: ClassVar[int]
        HEH: ClassVar[int]
        HEH_GOAL: ClassVar[int]
        HETH: ClassVar[int]
        KAF: ClassVar[int]
        KAPH: ClassVar[int]
        KHAPH: ClassVar[int]
        KNOTTED_HEH: ClassVar[int]
        LAM: ClassVar[int]
        LAMADH: ClassVar[int]
        MALAYALAM_BHA: ClassVar[int]
        MALAYALAM_JA: ClassVar[int]
        MALAYALAM_LLA: ClassVar[int]
        MALAYALAM_LLLA: ClassVar[int]
        MALAYALAM_NGA: ClassVar[int]
        MALAYALAM_NNA: ClassVar[int]
        MALAYALAM_NNNA: ClassVar[int]
        MALAYALAM_NYA: ClassVar[int]
        MALAYALAM_RA: ClassVar[int]
        MALAYALAM_SSA: ClassVar[int]
        MALAYALAM_TTA: ClassVar[int]
        MANICHAEAN_ALEPH: ClassVar[int]
        MANICHAEAN_AYIN: ClassVar[int]
        MANICHAEAN_BETH: ClassVar[int]
        MANICHAEAN_DALETH: ClassVar[int]
        MANICHAEAN_DHAMEDH: ClassVar[int]
        MANICHAEAN_FIVE: ClassVar[int]
        MANICHAEAN_GIMEL: ClassVar[int]
        MANICHAEAN_HETH: ClassVar[int]
        MANICHAEAN_HUNDRED: ClassVar[int]
        MANICHAEAN_KAPH: ClassVar[int]
        MANICHAEAN_LAMEDH: ClassVar[int]
        MANICHAEAN_MEM: ClassVar[int]
        MANICHAEAN_NUN: ClassVar[int]
        MANICHAEAN_ONE: ClassVar[int]
        MANICHAEAN_PE: ClassVar[int]
        MANICHAEAN_QOPH: ClassVar[int]
        MANICHAEAN_RESH: ClassVar[int]
        MANICHAEAN_SADHE: ClassVar[int]
        MANICHAEAN_SAMEKH: ClassVar[int]
        MANICHAEAN_TAW: ClassVar[int]
        MANICHAEAN_TEN: ClassVar[int]
        MANICHAEAN_TETH: ClassVar[int]
        MANICHAEAN_THAMEDH: ClassVar[int]
        MANICHAEAN_TWENTY: ClassVar[int]
        MANICHAEAN_WAW: ClassVar[int]
        MANICHAEAN_YODH: ClassVar[int]
        MANICHAEAN_ZAYIN: ClassVar[int]
        MEEM: ClassVar[int]
        MIM: ClassVar[int]
        NOON: ClassVar[int]
        NO_JOINING_GROUP: ClassVar[int]
        NUN: ClassVar[int]
        NYA: ClassVar[int]
        PE: ClassVar[int]
        QAF: ClassVar[int]
        QAPH: ClassVar[int]
        REH: ClassVar[int]
        REVERSED_PE: ClassVar[int]
        ROHINGYA_YEH: ClassVar[int]
        SAD: ClassVar[int]
        SADHE: ClassVar[int]
        SEEN: ClassVar[int]
        SEMKATH: ClassVar[int]
        SHIN: ClassVar[int]
        STRAIGHT_WAW: ClassVar[int]
        SWASH_KAF: ClassVar[int]
        SYRIAC_WAW: ClassVar[int]
        TAH: ClassVar[int]
        TAW: ClassVar[int]
        TEH_MARBUTA: ClassVar[int]
        TEH_MARBUTA_GOAL: ClassVar[int]
        TETH: ClassVar[int]
        THIN_YEH: ClassVar[int]
        VERTICAL_TAIL: ClassVar[int]
        WAW: ClassVar[int]
        YEH: ClassVar[int]
        YEH_BARREE: ClassVar[int]
        YEH_WITH_TAIL: ClassVar[int]
        YUDH: ClassVar[int]
        YUDH_HE: ClassVar[int]
        ZAIN: ClassVar[int]
        ZHAIN: ClassVar[int]

    class JoiningType:
        DUAL_JOINING: ClassVar[int]
        JOIN_CAUSING: ClassVar[int]
        LEFT_JOINING: ClassVar[int]
        NON_JOINING: ClassVar[int]
        RIGHT_JOINING: ClassVar[int]
        TRANSPARENT: ClassVar[int]

    class LineBreak:
        AKSARA: ClassVar[int]
        AKSARA_PREBASE: ClassVar[int]
        AKSARA_START: ClassVar[int]
        ALPHABETIC: ClassVar[int]
        AMBIGUOUS: ClassVar[int]
        BREAK_AFTER: ClassVar[int]
        BREAK_BEFORE: ClassVar[int]
        BREAK_BOTH: ClassVar[int]
        BREAK_SYMBOLS: ClassVar[int]
        CARRIAGE_RETURN: ClassVar[int]
        CLOSE_PARENTHESIS: ClassVar[int]
        CLOSE_PUNCTUATION: ClassVar[int]
        COMBINING_MARK: ClassVar[int]
        COMPLEX_CONTEXT: ClassVar[int]
        CONDITIONAL_JAPANESE_STARTER: ClassVar[int]
        CONTINGENT_BREAK: ClassVar[int]
        EXCLAMATION: ClassVar[int]
        E_BASE: ClassVar[int]
        E_MODIFIER: ClassVar[int]
        GLUE: ClassVar[int]
        H2: ClassVar[int]
        H3: ClassVar[int]
        HEBREW_LETTER: ClassVar[int]
        HYPHEN: ClassVar[int]
        IDEOGRAPHIC: ClassVar[int]
        INFIX_NUMERIC: ClassVar[int]
        INSEPARABLE: ClassVar[int]
        INSEPERABLE: ClassVar[int]
        JL: ClassVar[int]
        JT: ClassVar[int]
        JV: ClassVar[int]
        LINE_FEED: ClassVar[int]
        MANDATORY_BREAK: ClassVar[int]
        NEXT_LINE: ClassVar[int]
        NONSTARTER: ClassVar[int]
        NUMERIC: ClassVar[int]
        OPEN_PUNCTUATION: ClassVar[int]
        POSTFIX_NUMERIC: ClassVar[int]
        PREFIX_NUMERIC: ClassVar[int]
        QUOTATION: ClassVar[int]
        REGIONAL_INDICATOR: ClassVar[int]
        SPACE: ClassVar[int]
        SURROGATE: ClassVar[int]
        UNKNOWN: ClassVar[int]
        VIRAMA: ClassVar[int]
        VIRAMA_FINAL: ClassVar[int]
        WORD_JOINER: ClassVar[int]
        ZWJ: ClassVar[int]
        ZWSPACE: ClassVar[int]

    class NumericType:
        DECIMAL: ClassVar[int]
        DIGIT: ClassVar[int]
        NONE: ClassVar[int]
        NUMERIC: ClassVar[int]

    class SentenceBreak:
        ATERM: ClassVar[int]
        CLOSE: ClassVar[int]
        CR: ClassVar[int]
        EXTEND: ClassVar[int]
        FORMAT: ClassVar[int]
        LF: ClassVar[int]
        LOWER: ClassVar[int]
        NUMERIC: ClassVar[int]
        OLETTER: ClassVar[int]
        OTHER: ClassVar[int]
        SCONTINUE: ClassVar[int]
        SEP: ClassVar[int]
        SP: ClassVar[int]
        STERM: ClassVar[int]
        UPPER: ClassVar[int]

    class UnicodeBlock:
        ADLAM: ClassVar["UnicodeBlock"]
        ADLAM_ID: ClassVar[int]
        AEGEAN_NUMBERS: ClassVar["UnicodeBlock"]
        AEGEAN_NUMBERS_ID: ClassVar[int]
        AHOM: ClassVar["UnicodeBlock"]
        AHOM_ID: ClassVar[int]
        ALCHEMICAL_SYMBOLS: ClassVar["UnicodeBlock"]
        ALCHEMICAL_SYMBOLS_ID: ClassVar[int]
        ALPHABETIC_PRESENTATION_FORMS: ClassVar["UnicodeBlock"]
        ALPHABETIC_PRESENTATION_FORMS_ID: ClassVar[int]
        ANATOLIAN_HIEROGLYPHS: ClassVar["UnicodeBlock"]
        ANATOLIAN_HIEROGLYPHS_ID: ClassVar[int]
        ANCIENT_GREEK_MUSICAL_NOTATION: ClassVar["UnicodeBlock"]
        ANCIENT_GREEK_MUSICAL_NOTATION_ID: ClassVar[int]
        ANCIENT_GREEK_NUMBERS: ClassVar["UnicodeBlock"]
        ANCIENT_GREEK_NUMBERS_ID: ClassVar[int]
        ANCIENT_SYMBOLS: ClassVar["UnicodeBlock"]
        ANCIENT_SYMBOLS_ID: ClassVar[int]
        ARABIC: ClassVar["UnicodeBlock"]
        ARABIC_EXTENDED_A: ClassVar["UnicodeBlock"]
        ARABIC_EXTENDED_A_ID: ClassVar[int]
        ARABIC_EXTENDED_B: ClassVar["UnicodeBlock"]
        ARABIC_EXTENDED_B_ID: ClassVar[int]
        ARABIC_EXTENDED_C: ClassVar["UnicodeBlock"]
        ARABIC_EXTENDED_C_ID: ClassVar[int]
        ARABIC_ID: ClassVar[int]
        ARABIC_MATHEMATICAL_ALPHABETIC_SYMBOLS: ClassVar["UnicodeBlock"]
        ARABIC_MATHEMATICAL_ALPHABETIC_SYMBOLS_ID: ClassVar[int]
        ARABIC_PRESENTATION_FORMS_A: ClassVar["UnicodeBlock"]
        ARABIC_PRESENTATION_FORMS_A_ID: ClassVar[int]
        ARABIC_PRESENTATION_FORMS_B: ClassVar["UnicodeBlock"]
        ARABIC_PRESENTATION_FORMS_B_ID: ClassVar[int]
        ARABIC_SUPPLEMENT: ClassVar["UnicodeBlock"]
        ARABIC_SUPPLEMENT_ID: ClassVar[int]
        ARMENIAN: ClassVar["UnicodeBlock"]
        ARMENIAN_ID: ClassVar[int]
        ARROWS: ClassVar["UnicodeBlock"]
        ARROWS_ID: ClassVar[int]
        AVESTAN: ClassVar["UnicodeBlock"]
        AVESTAN_ID: ClassVar[int]
        BALINESE: ClassVar["UnicodeBlock"]
        BALINESE_ID: ClassVar[int]
        BAMUM: ClassVar["UnicodeBlock"]
        BAMUM_ID: ClassVar[int]
        BAMUM_SUPPLEMENT: ClassVar["UnicodeBlock"]
        BAMUM_SUPPLEMENT_ID: ClassVar[int]
        BASIC_LATIN: ClassVar["UnicodeBlock"]
        BASIC_LATIN_ID: ClassVar[int]
        BASSA_VAH: ClassVar["UnicodeBlock"]
        BASSA_VAH_ID: ClassVar[int]
        BATAK: ClassVar["UnicodeBlock"]
        BATAK_ID: ClassVar[int]
        BENGALI: ClassVar["UnicodeBlock"]
        BENGALI_ID: ClassVar[int]
        BHAIKSUKI: ClassVar["UnicodeBlock"]
        BHAIKSUKI_ID: ClassVar[int]
        BLOCK_ELEMENTS: ClassVar["UnicodeBlock"]
        BLOCK_ELEMENTS_ID: ClassVar[int]
        BOPOMOFO: ClassVar["UnicodeBlock"]
        BOPOMOFO_EXTENDED: ClassVar["UnicodeBlock"]
        BOPOMOFO_EXTENDED_ID: ClassVar[int]
        BOPOMOFO_ID: ClassVar[int]
        BOX_DRAWING: ClassVar["UnicodeBlock"]
        BOX_DRAWING_ID: ClassVar[int]
        BRAHMI: ClassVar["UnicodeBlock"]
        BRAHMI_ID: ClassVar[int]
        BRAILLE_PATTERNS: ClassVar["UnicodeBlock"]
        BRAILLE_PATTERNS_ID: ClassVar[int]
        BUGINESE: ClassVar["UnicodeBlock"]
        BUGINESE_ID: ClassVar[int]
        BUHID: ClassVar["UnicodeBlock"]
        BUHID_ID: ClassVar[int]
        BYZANTINE_MUSICAL_SYMBOLS: ClassVar["UnicodeBlock"]
        BYZANTINE_MUSICAL_SYMBOLS_ID: ClassVar[int]
        CARIAN: ClassVar["UnicodeBlock"]
        CARIAN_ID: ClassVar[int]
        CAUCASIAN_ALBANIAN: ClassVar["UnicodeBlock"]
        CAUCASIAN_ALBANIAN_ID: ClassVar[int]
        CHAKMA: ClassVar["UnicodeBlock"]
        CHAKMA_ID: ClassVar[int]
        CHAM: ClassVar["UnicodeBlock"]
        CHAM_ID: ClassVar[int]
        CHEROKEE: ClassVar["UnicodeBlock"]
        CHEROKEE_ID: ClassVar[int]
        CHEROKEE_SUPPLEMENT: ClassVar["UnicodeBlock"]
        CHEROKEE_SUPPLEMENT_ID: ClassVar[int]
        CHESS_SYMBOLS: ClassVar["UnicodeBlock"]
        CHESS_SYMBOLS_ID: ClassVar[int]
        CHORASMIAN: ClassVar["UnicodeBlock"]
        CHORASMIAN_ID: ClassVar[int]
        CJK_COMPATIBILITY: ClassVar["UnicodeBlock"]
        CJK_COMPATIBILITY_FORMS: ClassVar["UnicodeBlock"]
        CJK_COMPATIBILITY_FORMS_ID: ClassVar[int]
        CJK_COMPATIBILITY_ID: ClassVar[int]
        CJK_COMPATIBILITY_IDEOGRAPHS: ClassVar["UnicodeBlock"]
        CJK_COMPATIBILITY_IDEOGRAPHS_ID: ClassVar[int]
        CJK_COMPATIBILITY_IDEOGRAPHS_SUPPLEMENT: ClassVar["UnicodeBlock"]
        CJK_COMPATIBILITY_IDEOGRAPHS_SUPPLEMENT_ID: ClassVar[int]
        CJK_RADICALS_SUPPLEMENT: ClassVar["UnicodeBlock"]
        CJK_RADICALS_SUPPLEMENT_ID: ClassVar[int]
        CJK_STROKES: ClassVar["UnicodeBlock"]
        CJK_STROKES_ID: ClassVar[int]
        CJK_SYMBOLS_AND_PUNCTUATION: ClassVar["UnicodeBlock"]
        CJK_SYMBOLS_AND_PUNCTUATION_ID: ClassVar[int]
        CJK_UNIFIED_IDEOGRAPHS: ClassVar["UnicodeBlock"]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_A: ClassVar["UnicodeBlock"]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_A_ID: ClassVar[int]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_B: ClassVar["UnicodeBlock"]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_B_ID: ClassVar[int]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_C: ClassVar["UnicodeBlock"]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_C_ID: ClassVar[int]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_D: ClassVar["UnicodeBlock"]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_D_ID: ClassVar[int]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_E: ClassVar["UnicodeBlock"]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_E_ID: ClassVar[int]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_F: ClassVar["UnicodeBlock"]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_F_ID: ClassVar[int]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_G: ClassVar["UnicodeBlock"]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_G_ID: ClassVar[int]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_H: ClassVar["UnicodeBlock"]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_H_ID: ClassVar[int]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_I: ClassVar["UnicodeBlock"]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_I_ID: ClassVar[int]
        CJK_UNIFIED_IDEOGRAPHS_ID: ClassVar[int]
        COMBINING_DIACRITICAL_MARKS: ClassVar["UnicodeBlock"]
        COMBINING_DIACRITICAL_MARKS_EXTENDED: ClassVar["UnicodeBlock"]
        COMBINING_DIACRITICAL_MARKS_EXTENDED_ID: ClassVar[int]
        COMBINING_DIACRITICAL_MARKS_ID: ClassVar[int]
        COMBINING_DIACRITICAL_MARKS_SUPPLEMENT: ClassVar["UnicodeBlock"]
        COMBINING_DIACRITICAL_MARKS_SUPPLEMENT_ID: ClassVar[int]
        COMBINING_HALF_MARKS: ClassVar["UnicodeBlock"]
        COMBINING_HALF_MARKS_ID: ClassVar[int]
        COMBINING_MARKS_FOR_SYMBOLS: ClassVar["UnicodeBlock"]
        COMBINING_MARKS_FOR_SYMBOLS_ID: ClassVar[int]
        COMMON_INDIC_NUMBER_FORMS: ClassVar["UnicodeBlock"]
        COMMON_INDIC_NUMBER_FORMS_ID: ClassVar[int]
        CONTROL_PICTURES: ClassVar["UnicodeBlock"]
        CONTROL_PICTURES_ID: ClassVar[int]
        COPTIC: ClassVar["UnicodeBlock"]
        COPTIC_EPACT_NUMBERS: ClassVar["UnicodeBlock"]
        COPTIC_EPACT_NUMBERS_ID: ClassVar[int]
        COPTIC_ID: ClassVar[int]
        COUNTING_ROD_NUMERALS: ClassVar["UnicodeBlock"]
        COUNTING_ROD_NUMERALS_ID: ClassVar[int]
        CUNEIFORM: ClassVar["UnicodeBlock"]
        CUNEIFORM_ID: ClassVar[int]
        CUNEIFORM_NUMBERS_AND_PUNCTUATION: ClassVar["UnicodeBlock"]
        CUNEIFORM_NUMBERS_AND_PUNCTUATION_ID: ClassVar[int]
        CURRENCY_SYMBOLS: ClassVar["UnicodeBlock"]
        CURRENCY_SYMBOLS_ID: ClassVar[int]
        CYPRIOT_SYLLABARY: ClassVar["UnicodeBlock"]
        CYPRIOT_SYLLABARY_ID: ClassVar[int]
        CYPRO_MINOAN: ClassVar["UnicodeBlock"]
        CYPRO_MINOAN_ID: ClassVar[int]
        CYRILLIC: ClassVar["UnicodeBlock"]
        CYRILLIC_EXTENDED_A: ClassVar["UnicodeBlock"]
        CYRILLIC_EXTENDED_A_ID: ClassVar[int]
        CYRILLIC_EXTENDED_B: ClassVar["UnicodeBlock"]
        CYRILLIC_EXTENDED_B_ID: ClassVar[int]
        CYRILLIC_EXTENDED_C: ClassVar["UnicodeBlock"]
        CYRILLIC_EXTENDED_C_ID: ClassVar[int]
        CYRILLIC_EXTENDED_D: ClassVar["UnicodeBlock"]
        CYRILLIC_EXTENDED_D_ID: ClassVar[int]
        CYRILLIC_ID: ClassVar[int]
        CYRILLIC_SUPPLEMENT: ClassVar["UnicodeBlock"]
        CYRILLIC_SUPPLEMENTARY: ClassVar["UnicodeBlock"]
        CYRILLIC_SUPPLEMENTARY_ID: ClassVar[int]
        CYRILLIC_SUPPLEMENT_ID: ClassVar[int]
        DESERET: ClassVar["UnicodeBlock"]
        DESERET_ID: ClassVar[int]
        DEVANAGARI: ClassVar["UnicodeBlock"]
        DEVANAGARI_EXTENDED: ClassVar["UnicodeBlock"]
        DEVANAGARI_EXTENDED_A: ClassVar["UnicodeBlock"]
        DEVANAGARI_EXTENDED_A_ID: ClassVar[int]
        DEVANAGARI_EXTENDED_ID: ClassVar[int]
        DEVANAGARI_ID: ClassVar[int]
        DINGBATS: ClassVar["UnicodeBlock"]
        DINGBATS_ID: ClassVar[int]
        DIVES_AKURU: ClassVar["UnicodeBlock"]
        DIVES_AKURU_ID: ClassVar[int]
        DOGRA: ClassVar["UnicodeBlock"]
        DOGRA_ID: ClassVar[int]
        DOMINO_TILES: ClassVar["UnicodeBlock"]
        DOMINO_TILES_ID: ClassVar[int]
        DUPLOYAN: ClassVar["UnicodeBlock"]
        DUPLOYAN_ID: ClassVar[int]
        EARLY_DYNASTIC_CUNEIFORM: ClassVar["UnicodeBlock"]
        EARLY_DYNASTIC_CUNEIFORM_ID: ClassVar[int]
        EGYPTIAN_HIEROGLYPHS: ClassVar["UnicodeBlock"]
        EGYPTIAN_HIEROGLYPHS_ID: ClassVar[int]
        EGYPTIAN_HIEROGLYPH_FORMAT_CONTROLS: ClassVar["UnicodeBlock"]
        EGYPTIAN_HIEROGLYPH_FORMAT_CONTROLS_ID: ClassVar[int]
        ELBASAN: ClassVar["UnicodeBlock"]
        ELBASAN_ID: ClassVar[int]
        ELYMAIC: ClassVar["UnicodeBlock"]
        ELYMAIC_ID: ClassVar[int]
        EMOTICONS: ClassVar["UnicodeBlock"]
        EMOTICONS_ID: ClassVar[int]
        ENCLOSED_ALPHANUMERICS: ClassVar["UnicodeBlock"]
        ENCLOSED_ALPHANUMERICS_ID: ClassVar[int]
        ENCLOSED_ALPHANUMERIC_SUPPLEMENT: ClassVar["UnicodeBlock"]
        ENCLOSED_ALPHANUMERIC_SUPPLEMENT_ID: ClassVar[int]
        ENCLOSED_CJK_LETTERS_AND_MONTHS: ClassVar["UnicodeBlock"]
        ENCLOSED_CJK_LETTERS_AND_MONTHS_ID: ClassVar[int]
        ENCLOSED_IDEOGRAPHIC_SUPPLEMENT: ClassVar["UnicodeBlock"]
        ENCLOSED_IDEOGRAPHIC_SUPPLEMENT_ID: ClassVar[int]
        ETHIOPIC: ClassVar["UnicodeBlock"]
        ETHIOPIC_EXTENDED: ClassVar["UnicodeBlock"]
        ETHIOPIC_EXTENDED_A: ClassVar["UnicodeBlock"]
        ETHIOPIC_EXTENDED_A_ID: ClassVar[int]
        ETHIOPIC_EXTENDED_B: ClassVar["UnicodeBlock"]
        ETHIOPIC_EXTENDED_B_ID: ClassVar[int]
        ETHIOPIC_EXTENDED_ID: ClassVar[int]
        ETHIOPIC_ID: ClassVar[int]
        ETHIOPIC_SUPPLEMENT: ClassVar["UnicodeBlock"]
        ETHIOPIC_SUPPLEMENT_ID: ClassVar[int]
        GENERAL_PUNCTUATION: ClassVar["UnicodeBlock"]
        GENERAL_PUNCTUATION_ID: ClassVar[int]
        GEOMETRIC_SHAPES: ClassVar["UnicodeBlock"]
        GEOMETRIC_SHAPES_EXTENDED: ClassVar["UnicodeBlock"]
        GEOMETRIC_SHAPES_EXTENDED_ID: ClassVar[int]
        GEOMETRIC_SHAPES_ID: ClassVar[int]
        GEORGIAN: ClassVar["UnicodeBlock"]
        GEORGIAN_EXTENDED: ClassVar["UnicodeBlock"]
        GEORGIAN_EXTENDED_ID: ClassVar[int]
        GEORGIAN_ID: ClassVar[int]
        GEORGIAN_SUPPLEMENT: ClassVar["UnicodeBlock"]
        GEORGIAN_SUPPLEMENT_ID: ClassVar[int]
        GLAGOLITIC: ClassVar["UnicodeBlock"]
        GLAGOLITIC_ID: ClassVar[int]
        GLAGOLITIC_SUPPLEMENT: ClassVar["UnicodeBlock"]
        GLAGOLITIC_SUPPLEMENT_ID: ClassVar[int]
        GOTHIC: ClassVar["UnicodeBlock"]
        GOTHIC_ID: ClassVar[int]
        GRANTHA: ClassVar["UnicodeBlock"]
        GRANTHA_ID: ClassVar[int]
        GREEK: ClassVar["UnicodeBlock"]
        GREEK_EXTENDED: ClassVar["UnicodeBlock"]
        GREEK_EXTENDED_ID: ClassVar[int]
        GREEK_ID: ClassVar[int]
        GUJARATI: ClassVar["UnicodeBlock"]
        GUJARATI_ID: ClassVar[int]
        GUNJALA_GONDI: ClassVar["UnicodeBlock"]
        GUNJALA_GONDI_ID: ClassVar[int]
        GURMUKHI: ClassVar["UnicodeBlock"]
        GURMUKHI_ID: ClassVar[int]
        HALFWIDTH_AND_FULLWIDTH_FORMS: ClassVar["UnicodeBlock"]
        HALFWIDTH_AND_FULLWIDTH_FORMS_ID: ClassVar[int]
        HANGUL_COMPATIBILITY_JAMO: ClassVar["UnicodeBlock"]
        HANGUL_COMPATIBILITY_JAMO_ID: ClassVar[int]
        HANGUL_JAMO: ClassVar["UnicodeBlock"]
        HANGUL_JAMO_EXTENDED_A: ClassVar["UnicodeBlock"]
        HANGUL_JAMO_EXTENDED_A_ID: ClassVar[int]
        HANGUL_JAMO_EXTENDED_B: ClassVar["UnicodeBlock"]
        HANGUL_JAMO_EXTENDED_B_ID: ClassVar[int]
        HANGUL_JAMO_ID: ClassVar[int]
        HANGUL_SYLLABLES: ClassVar["UnicodeBlock"]
        HANGUL_SYLLABLES_ID: ClassVar[int]
        HANIFI_ROHINGYA: ClassVar["UnicodeBlock"]
        HANIFI_ROHINGYA_ID: ClassVar[int]
        HANUNOO: ClassVar["UnicodeBlock"]
        HANUNOO_ID: ClassVar[int]
        HATRAN: ClassVar["UnicodeBlock"]
        HATRAN_ID: ClassVar[int]
        HEBREW: ClassVar["UnicodeBlock"]
        HEBREW_ID: ClassVar[int]
        HIGH_PRIVATE_USE_SURROGATES: ClassVar["UnicodeBlock"]
        HIGH_PRIVATE_USE_SURROGATES_ID: ClassVar[int]
        HIGH_SURROGATES: ClassVar["UnicodeBlock"]
        HIGH_SURROGATES_ID: ClassVar[int]
        HIRAGANA: ClassVar["UnicodeBlock"]
        HIRAGANA_ID: ClassVar[int]
        IDEOGRAPHIC_DESCRIPTION_CHARACTERS: ClassVar["UnicodeBlock"]
        IDEOGRAPHIC_DESCRIPTION_CHARACTERS_ID: ClassVar[int]
        IDEOGRAPHIC_SYMBOLS_AND_PUNCTUATION: ClassVar["UnicodeBlock"]
        IDEOGRAPHIC_SYMBOLS_AND_PUNCTUATION_ID: ClassVar[int]
        IMPERIAL_ARAMAIC: ClassVar["UnicodeBlock"]
        IMPERIAL_ARAMAIC_ID: ClassVar[int]
        INDIC_SIYAQ_NUMBERS: ClassVar["UnicodeBlock"]
        INDIC_SIYAQ_NUMBERS_ID: ClassVar[int]
        INSCRIPTIONAL_PAHLAVI: ClassVar["UnicodeBlock"]
        INSCRIPTIONAL_PAHLAVI_ID: ClassVar[int]
        INSCRIPTIONAL_PARTHIAN: ClassVar["UnicodeBlock"]
        INSCRIPTIONAL_PARTHIAN_ID: ClassVar[int]
        INVALID_CODE: ClassVar["UnicodeBlock"]
        INVALID_CODE_ID: ClassVar[int]
        IPA_EXTENSIONS: ClassVar["UnicodeBlock"]
        IPA_EXTENSIONS_ID: ClassVar[int]
        JAVANESE: ClassVar["UnicodeBlock"]
        JAVANESE_ID: ClassVar[int]
        KAITHI: ClassVar["UnicodeBlock"]
        KAITHI_ID: ClassVar[int]
        KAKTOVIK_NUMERALS: ClassVar["UnicodeBlock"]
        KAKTOVIK_NUMERALS_ID: ClassVar[int]
        KANA_EXTENDED_A: ClassVar["UnicodeBlock"]
        KANA_EXTENDED_A_ID: ClassVar[int]
        KANA_EXTENDED_B: ClassVar["UnicodeBlock"]
        KANA_EXTENDED_B_ID: ClassVar[int]
        KANA_SUPPLEMENT: ClassVar["UnicodeBlock"]
        KANA_SUPPLEMENT_ID: ClassVar[int]
        KANBUN: ClassVar["UnicodeBlock"]
        KANBUN_ID: ClassVar[int]
        KANGXI_RADICALS: ClassVar["UnicodeBlock"]
        KANGXI_RADICALS_ID: ClassVar[int]
        KANNADA: ClassVar["UnicodeBlock"]
        KANNADA_ID: ClassVar[int]
        KATAKANA: ClassVar["UnicodeBlock"]
        KATAKANA_ID: ClassVar[int]
        KATAKANA_PHONETIC_EXTENSIONS: ClassVar["UnicodeBlock"]
        KATAKANA_PHONETIC_EXTENSIONS_ID: ClassVar[int]
        KAWI: ClassVar["UnicodeBlock"]
        KAWI_ID: ClassVar[int]
        KAYAH_LI: ClassVar["UnicodeBlock"]
        KAYAH_LI_ID: ClassVar[int]
        KHAROSHTHI: ClassVar["UnicodeBlock"]
        KHAROSHTHI_ID: ClassVar[int]
        KHITAN_SMALL_SCRIPT: ClassVar["UnicodeBlock"]
        KHITAN_SMALL_SCRIPT_ID: ClassVar[int]
        KHMER: ClassVar["UnicodeBlock"]
        KHMER_ID: ClassVar[int]
        KHMER_SYMBOLS: ClassVar["UnicodeBlock"]
        KHMER_SYMBOLS_ID: ClassVar[int]
        KHOJKI: ClassVar["UnicodeBlock"]
        KHOJKI_ID: ClassVar[int]
        KHUDAWADI: ClassVar["UnicodeBlock"]
        KHUDAWADI_ID: ClassVar[int]
        LAO: ClassVar["UnicodeBlock"]
        LAO_ID: ClassVar[int]
        LATIN_1_SUPPLEMENT: ClassVar["UnicodeBlock"]
        LATIN_1_SUPPLEMENT_ID: ClassVar[int]
        LATIN_EXTENDED_A: ClassVar["UnicodeBlock"]
        LATIN_EXTENDED_ADDITIONAL: ClassVar["UnicodeBlock"]
        LATIN_EXTENDED_ADDITIONAL_ID: ClassVar[int]
        LATIN_EXTENDED_A_ID: ClassVar[int]
        LATIN_EXTENDED_B: ClassVar["UnicodeBlock"]
        LATIN_EXTENDED_B_ID: ClassVar[int]
        LATIN_EXTENDED_C: ClassVar["UnicodeBlock"]
        LATIN_EXTENDED_C_ID: ClassVar[int]
        LATIN_EXTENDED_D: ClassVar["UnicodeBlock"]
        LATIN_EXTENDED_D_ID: ClassVar[int]
        LATIN_EXTENDED_E: ClassVar["UnicodeBlock"]
        LATIN_EXTENDED_E_ID: ClassVar[int]
        LATIN_EXTENDED_F: ClassVar["UnicodeBlock"]
        LATIN_EXTENDED_F_ID: ClassVar[int]
        LATIN_EXTENDED_G: ClassVar["UnicodeBlock"]
        LATIN_EXTENDED_G_ID: ClassVar[int]
        LEPCHA: ClassVar["UnicodeBlock"]
        LEPCHA_ID: ClassVar[int]
        LETTERLIKE_SYMBOLS: ClassVar["UnicodeBlock"]
        LETTERLIKE_SYMBOLS_ID: ClassVar[int]
        LIMBU: ClassVar["UnicodeBlock"]
        LIMBU_ID: ClassVar[int]
        LINEAR_A: ClassVar["UnicodeBlock"]
        LINEAR_A_ID: ClassVar[int]
        LINEAR_B_IDEOGRAMS: ClassVar["UnicodeBlock"]
        LINEAR_B_IDEOGRAMS_ID: ClassVar[int]
        LINEAR_B_SYLLABARY: ClassVar["UnicodeBlock"]
        LINEAR_B_SYLLABARY_ID: ClassVar[int]
        LISU: ClassVar["UnicodeBlock"]
        LISU_ID: ClassVar[int]
        LISU_SUPPLEMENT: ClassVar["UnicodeBlock"]
        LISU_SUPPLEMENT_ID: ClassVar[int]
        LOW_SURROGATES: ClassVar["UnicodeBlock"]
        LOW_SURROGATES_ID: ClassVar[int]
        LYCIAN: ClassVar["UnicodeBlock"]
        LYCIAN_ID: ClassVar[int]
        LYDIAN: ClassVar["UnicodeBlock"]
        LYDIAN_ID: ClassVar[int]
        MAHAJANI: ClassVar["UnicodeBlock"]
        MAHAJANI_ID: ClassVar[int]
        MAHJONG_TILES: ClassVar["UnicodeBlock"]
        MAHJONG_TILES_ID: ClassVar[int]
        MAKASAR: ClassVar["UnicodeBlock"]
        MAKASAR_ID: ClassVar[int]
        MALAYALAM: ClassVar["UnicodeBlock"]
        MALAYALAM_ID: ClassVar[int]
        MANDAIC: ClassVar["UnicodeBlock"]
        MANDAIC_ID: ClassVar[int]
        MANICHAEAN: ClassVar["UnicodeBlock"]
        MANICHAEAN_ID: ClassVar[int]
        MARCHEN: ClassVar["UnicodeBlock"]
        MARCHEN_ID: ClassVar[int]
        MASARAM_GONDI: ClassVar["UnicodeBlock"]
        MASARAM_GONDI_ID: ClassVar[int]
        MATHEMATICAL_ALPHANUMERIC_SYMBOLS: ClassVar["UnicodeBlock"]
        MATHEMATICAL_ALPHANUMERIC_SYMBOLS_ID: ClassVar[int]
        MATHEMATICAL_OPERATORS: ClassVar["UnicodeBlock"]
        MATHEMATICAL_OPERATORS_ID: ClassVar[int]
        MAYAN_NUMERALS: ClassVar["UnicodeBlock"]
        MAYAN_NUMERALS_ID: ClassVar[int]
        MEDEFAIDRIN: ClassVar["UnicodeBlock"]
        MEDEFAIDRIN_ID: ClassVar[int]
        MEETEI_MAYEK: ClassVar["UnicodeBlock"]
        MEETEI_MAYEK_EXTENSIONS: ClassVar["UnicodeBlock"]
        MEETEI_MAYEK_EXTENSIONS_ID: ClassVar[int]
        MEETEI_MAYEK_ID: ClassVar[int]
        MENDE_KIKAKUI: ClassVar["UnicodeBlock"]
        MENDE_KIKAKUI_ID: ClassVar[int]
        MEROITIC_CURSIVE: ClassVar["UnicodeBlock"]
        MEROITIC_CURSIVE_ID: ClassVar[int]
        MEROITIC_HIEROGLYPHS: ClassVar["UnicodeBlock"]
        MEROITIC_HIEROGLYPHS_ID: ClassVar[int]
        MIAO: ClassVar["UnicodeBlock"]
        MIAO_ID: ClassVar[int]
        MISCELLANEOUS_MATHEMATICAL_SYMBOLS_A: ClassVar["UnicodeBlock"]
        MISCELLANEOUS_MATHEMATICAL_SYMBOLS_A_ID: ClassVar[int]
        MISCELLANEOUS_MATHEMATICAL_SYMBOLS_B: ClassVar["UnicodeBlock"]
        MISCELLANEOUS_MATHEMATICAL_SYMBOLS_B_ID: ClassVar[int]
        MISCELLANEOUS_SYMBOLS: ClassVar["UnicodeBlock"]
        MISCELLANEOUS_SYMBOLS_AND_ARROWS: ClassVar["UnicodeBlock"]
        MISCELLANEOUS_SYMBOLS_AND_ARROWS_ID: ClassVar[int]
        MISCELLANEOUS_SYMBOLS_AND_PICTOGRAPHS: ClassVar["UnicodeBlock"]
        MISCELLANEOUS_SYMBOLS_AND_PICTOGRAPHS_ID: ClassVar[int]
        MISCELLANEOUS_SYMBOLS_ID: ClassVar[int]
        MISCELLANEOUS_TECHNICAL: ClassVar["UnicodeBlock"]
        MISCELLANEOUS_TECHNICAL_ID: ClassVar[int]
        MODI: ClassVar["UnicodeBlock"]
        MODIFIER_TONE_LETTERS: ClassVar["UnicodeBlock"]
        MODIFIER_TONE_LETTERS_ID: ClassVar[int]
        MODI_ID: ClassVar[int]
        MONGOLIAN: ClassVar["UnicodeBlock"]
        MONGOLIAN_ID: ClassVar[int]
        MONGOLIAN_SUPPLEMENT: ClassVar["UnicodeBlock"]
        MONGOLIAN_SUPPLEMENT_ID: ClassVar[int]
        MRO: ClassVar["UnicodeBlock"]
        MRO_ID: ClassVar[int]
        MULTANI: ClassVar["UnicodeBlock"]
        MULTANI_ID: ClassVar[int]
        MUSICAL_SYMBOLS: ClassVar["UnicodeBlock"]
        MUSICAL_SYMBOLS_ID: ClassVar[int]
        MYANMAR: ClassVar["UnicodeBlock"]
        MYANMAR_EXTENDED_A: ClassVar["UnicodeBlock"]
        MYANMAR_EXTENDED_A_ID: ClassVar[int]
        MYANMAR_EXTENDED_B: ClassVar["UnicodeBlock"]
        MYANMAR_EXTENDED_B_ID: ClassVar[int]
        MYANMAR_ID: ClassVar[int]
        NABATAEAN: ClassVar["UnicodeBlock"]
        NABATAEAN_ID: ClassVar[int]
        NAG_MUNDARI: ClassVar["UnicodeBlock"]
        NAG_MUNDARI_ID: ClassVar[int]
        NANDINAGARI: ClassVar["UnicodeBlock"]
        NANDINAGARI_ID: ClassVar[int]
        NEWA: ClassVar["UnicodeBlock"]
        NEWA_ID: ClassVar[int]
        NEW_TAI_LUE: ClassVar["UnicodeBlock"]
        NEW_TAI_LUE_ID: ClassVar[int]
        NKO: ClassVar["UnicodeBlock"]
        NKO_ID: ClassVar[int]
        NO_BLOCK: ClassVar["UnicodeBlock"]
        NUMBER_FORMS: ClassVar["UnicodeBlock"]
        NUMBER_FORMS_ID: ClassVar[int]
        NUSHU: ClassVar["UnicodeBlock"]
        NUSHU_ID: ClassVar[int]
        NYIAKENG_PUACHUE_HMONG: ClassVar["UnicodeBlock"]
        NYIAKENG_PUACHUE_HMONG_ID: ClassVar[int]
        OGHAM: ClassVar["UnicodeBlock"]
        OGHAM_ID: ClassVar[int]
        OLD_HUNGARIAN: ClassVar["UnicodeBlock"]
        OLD_HUNGARIAN_ID: ClassVar[int]
        OLD_ITALIC: ClassVar["UnicodeBlock"]
        OLD_ITALIC_ID: ClassVar[int]
        OLD_NORTH_ARABIAN: ClassVar["UnicodeBlock"]
        OLD_NORTH_ARABIAN_ID: ClassVar[int]
        OLD_PERMIC: ClassVar["UnicodeBlock"]
        OLD_PERMIC_ID: ClassVar[int]
        OLD_PERSIAN: ClassVar["UnicodeBlock"]
        OLD_PERSIAN_ID: ClassVar[int]
        OLD_SOGDIAN: ClassVar["UnicodeBlock"]
        OLD_SOGDIAN_ID: ClassVar[int]
        OLD_SOUTH_ARABIAN: ClassVar["UnicodeBlock"]
        OLD_SOUTH_ARABIAN_ID: ClassVar[int]
        OLD_TURKIC: ClassVar["UnicodeBlock"]
        OLD_TURKIC_ID: ClassVar[int]
        OLD_UYGHUR: ClassVar["UnicodeBlock"]
        OLD_UYGHUR_ID: ClassVar[int]
        OL_CHIKI: ClassVar["UnicodeBlock"]
        OL_CHIKI_ID: ClassVar[int]
        OPTICAL_CHARACTER_RECOGNITION: ClassVar["UnicodeBlock"]
        OPTICAL_CHARACTER_RECOGNITION_ID: ClassVar[int]
        ORIYA: ClassVar["UnicodeBlock"]
        ORIYA_ID: ClassVar[int]
        ORNAMENTAL_DINGBATS: ClassVar["UnicodeBlock"]
        ORNAMENTAL_DINGBATS_ID: ClassVar[int]
        OSAGE: ClassVar["UnicodeBlock"]
        OSAGE_ID: ClassVar[int]
        OSMANYA: ClassVar["UnicodeBlock"]
        OSMANYA_ID: ClassVar[int]
        OTTOMAN_SIYAQ_NUMBERS: ClassVar["UnicodeBlock"]
        OTTOMAN_SIYAQ_NUMBERS_ID: ClassVar[int]
        PAHAWH_HMONG: ClassVar["UnicodeBlock"]
        PAHAWH_HMONG_ID: ClassVar[int]
        PALMYRENE: ClassVar["UnicodeBlock"]
        PALMYRENE_ID: ClassVar[int]
        PAU_CIN_HAU: ClassVar["UnicodeBlock"]
        PAU_CIN_HAU_ID: ClassVar[int]
        PHAGS_PA: ClassVar["UnicodeBlock"]
        PHAGS_PA_ID: ClassVar[int]
        PHAISTOS_DISC: ClassVar["UnicodeBlock"]
        PHAISTOS_DISC_ID: ClassVar[int]
        PHOENICIAN: ClassVar["UnicodeBlock"]
        PHOENICIAN_ID: ClassVar[int]
        PHONETIC_EXTENSIONS: ClassVar["UnicodeBlock"]
        PHONETIC_EXTENSIONS_ID: ClassVar[int]
        PHONETIC_EXTENSIONS_SUPPLEMENT: ClassVar["UnicodeBlock"]
        PHONETIC_EXTENSIONS_SUPPLEMENT_ID: ClassVar[int]
        PLAYING_CARDS: ClassVar["UnicodeBlock"]
        PLAYING_CARDS_ID: ClassVar[int]
        PRIVATE_USE: ClassVar["UnicodeBlock"]
        PRIVATE_USE_AREA: ClassVar["UnicodeBlock"]
        PRIVATE_USE_AREA_ID: ClassVar[int]
        PRIVATE_USE_ID: ClassVar[int]
        PSALTER_PAHLAVI: ClassVar["UnicodeBlock"]
        PSALTER_PAHLAVI_ID: ClassVar[int]
        REJANG: ClassVar["UnicodeBlock"]
        REJANG_ID: ClassVar[int]
        RUMI_NUMERAL_SYMBOLS: ClassVar["UnicodeBlock"]
        RUMI_NUMERAL_SYMBOLS_ID: ClassVar[int]
        RUNIC: ClassVar["UnicodeBlock"]
        RUNIC_ID: ClassVar[int]
        SAMARITAN: ClassVar["UnicodeBlock"]
        SAMARITAN_ID: ClassVar[int]
        SAURASHTRA: ClassVar["UnicodeBlock"]
        SAURASHTRA_ID: ClassVar[int]
        SHARADA: ClassVar["UnicodeBlock"]
        SHARADA_ID: ClassVar[int]
        SHAVIAN: ClassVar["UnicodeBlock"]
        SHAVIAN_ID: ClassVar[int]
        SHORTHAND_FORMAT_CONTROLS: ClassVar["UnicodeBlock"]
        SHORTHAND_FORMAT_CONTROLS_ID: ClassVar[int]
        SIDDHAM: ClassVar["UnicodeBlock"]
        SIDDHAM_ID: ClassVar[int]
        SINHALA: ClassVar["UnicodeBlock"]
        SINHALA_ARCHAIC_NUMBERS: ClassVar["UnicodeBlock"]
        SINHALA_ARCHAIC_NUMBERS_ID: ClassVar[int]
        SINHALA_ID: ClassVar[int]
        SMALL_FORM_VARIANTS: ClassVar["UnicodeBlock"]
        SMALL_FORM_VARIANTS_ID: ClassVar[int]
        SMALL_KANA_EXTENSION: ClassVar["UnicodeBlock"]
        SMALL_KANA_EXTENSION_ID: ClassVar[int]
        SOGDIAN: ClassVar["UnicodeBlock"]
        SOGDIAN_ID: ClassVar[int]
        SORA_SOMPENG: ClassVar["UnicodeBlock"]
        SORA_SOMPENG_ID: ClassVar[int]
        SOYOMBO: ClassVar["UnicodeBlock"]
        SOYOMBO_ID: ClassVar[int]
        SPACING_MODIFIER_LETTERS: ClassVar["UnicodeBlock"]
        SPACING_MODIFIER_LETTERS_ID: ClassVar[int]
        SPECIALS: ClassVar["UnicodeBlock"]
        SPECIALS_ID: ClassVar[int]
        SUNDANESE: ClassVar["UnicodeBlock"]
        SUNDANESE_ID: ClassVar[int]
        SUNDANESE_SUPPLEMENT: ClassVar["UnicodeBlock"]
        SUNDANESE_SUPPLEMENT_ID: ClassVar[int]
        SUPERSCRIPTS_AND_SUBSCRIPTS: ClassVar["UnicodeBlock"]
        SUPERSCRIPTS_AND_SUBSCRIPTS_ID: ClassVar[int]
        SUPPLEMENTAL_ARROWS_A: ClassVar["UnicodeBlock"]
        SUPPLEMENTAL_ARROWS_A_ID: ClassVar[int]
        SUPPLEMENTAL_ARROWS_B: ClassVar["UnicodeBlock"]
        SUPPLEMENTAL_ARROWS_B_ID: ClassVar[int]
        SUPPLEMENTAL_ARROWS_C: ClassVar["UnicodeBlock"]
        SUPPLEMENTAL_ARROWS_C_ID: ClassVar[int]
        SUPPLEMENTAL_MATHEMATICAL_OPERATORS: ClassVar["UnicodeBlock"]
        SUPPLEMENTAL_MATHEMATICAL_OPERATORS_ID: ClassVar[int]
        SUPPLEMENTAL_PUNCTUATION: ClassVar["UnicodeBlock"]
        SUPPLEMENTAL_PUNCTUATION_ID: ClassVar[int]
        SUPPLEMENTAL_SYMBOLS_AND_PICTOGRAPHS: ClassVar["UnicodeBlock"]
        SUPPLEMENTAL_SYMBOLS_AND_PICTOGRAPHS_ID: ClassVar[int]
        SUPPLEMENTARY_PRIVATE_USE_AREA_A: ClassVar["UnicodeBlock"]
        SUPPLEMENTARY_PRIVATE_USE_AREA_A_ID: ClassVar[int]
        SUPPLEMENTARY_PRIVATE_USE_AREA_B: ClassVar["UnicodeBlock"]
        SUPPLEMENTARY_PRIVATE_USE_AREA_B_ID: ClassVar[int]
        SUTTON_SIGNWRITING: ClassVar["UnicodeBlock"]
        SUTTON_SIGNWRITING_ID: ClassVar[int]
        SYLOTI_NAGRI: ClassVar["UnicodeBlock"]
        SYLOTI_NAGRI_ID: ClassVar[int]
        SYMBOLS_AND_PICTOGRAPHS_EXTENDED_A: ClassVar["UnicodeBlock"]
        SYMBOLS_AND_PICTOGRAPHS_EXTENDED_A_ID: ClassVar[int]
        SYMBOLS_FOR_LEGACY_COMPUTING: ClassVar["UnicodeBlock"]
        SYMBOLS_FOR_LEGACY_COMPUTING_ID: ClassVar[int]
        SYRIAC: ClassVar["UnicodeBlock"]
        SYRIAC_ID: ClassVar[int]
        SYRIAC_SUPPLEMENT: ClassVar["UnicodeBlock"]
        SYRIAC_SUPPLEMENT_ID: ClassVar[int]
        TAGALOG: ClassVar["UnicodeBlock"]
        TAGALOG_ID: ClassVar[int]
        TAGBANWA: ClassVar["UnicodeBlock"]
        TAGBANWA_ID: ClassVar[int]
        TAGS: ClassVar["UnicodeBlock"]
        TAGS_ID: ClassVar[int]
        TAI_LE: ClassVar["UnicodeBlock"]
        TAI_LE_ID: ClassVar[int]
        TAI_THAM: ClassVar["UnicodeBlock"]
        TAI_THAM_ID: ClassVar[int]
        TAI_VIET: ClassVar["UnicodeBlock"]
        TAI_VIET_ID: ClassVar[int]
        TAI_XUAN_JING_SYMBOLS: ClassVar["UnicodeBlock"]
        TAI_XUAN_JING_SYMBOLS_ID: ClassVar[int]
        TAKRI: ClassVar["UnicodeBlock"]
        TAKRI_ID: ClassVar[int]
        TAMIL: ClassVar["UnicodeBlock"]
        TAMIL_ID: ClassVar[int]
        TAMIL_SUPPLEMENT: ClassVar["UnicodeBlock"]
        TAMIL_SUPPLEMENT_ID: ClassVar[int]
        TANGSA: ClassVar["UnicodeBlock"]
        TANGSA_ID: ClassVar[int]
        TANGUT: ClassVar["UnicodeBlock"]
        TANGUT_COMPONENTS: ClassVar["UnicodeBlock"]
        TANGUT_COMPONENTS_ID: ClassVar[int]
        TANGUT_ID: ClassVar[int]
        TANGUT_SUPPLEMENT: ClassVar["UnicodeBlock"]
        TANGUT_SUPPLEMENT_ID: ClassVar[int]
        TELUGU: ClassVar["UnicodeBlock"]
        TELUGU_ID: ClassVar[int]
        THAANA: ClassVar["UnicodeBlock"]
        THAANA_ID: ClassVar[int]
        THAI: ClassVar["UnicodeBlock"]
        THAI_ID: ClassVar[int]
        TIBETAN: ClassVar["UnicodeBlock"]
        TIBETAN_ID: ClassVar[int]
        TIFINAGH: ClassVar["UnicodeBlock"]
        TIFINAGH_ID: ClassVar[int]
        TIRHUTA: ClassVar["UnicodeBlock"]
        TIRHUTA_ID: ClassVar[int]
        TOTO: ClassVar["UnicodeBlock"]
        TOTO_ID: ClassVar[int]
        TRANSPORT_AND_MAP_SYMBOLS: ClassVar["UnicodeBlock"]
        TRANSPORT_AND_MAP_SYMBOLS_ID: ClassVar[int]
        UGARITIC: ClassVar["UnicodeBlock"]
        UGARITIC_ID: ClassVar[int]
        UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS: ClassVar["UnicodeBlock"]
        UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_EXTENDED: ClassVar["UnicodeBlock"]
        UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_EXTENDED_A: ClassVar["UnicodeBlock"]
        UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_EXTENDED_A_ID: ClassVar[int]
        UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_EXTENDED_ID: ClassVar[int]
        UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_ID: ClassVar[int]
        VAI: ClassVar["UnicodeBlock"]
        VAI_ID: ClassVar[int]
        VARIATION_SELECTORS: ClassVar["UnicodeBlock"]
        VARIATION_SELECTORS_ID: ClassVar[int]
        VARIATION_SELECTORS_SUPPLEMENT: ClassVar["UnicodeBlock"]
        VARIATION_SELECTORS_SUPPLEMENT_ID: ClassVar[int]
        VEDIC_EXTENSIONS: ClassVar["UnicodeBlock"]
        VEDIC_EXTENSIONS_ID: ClassVar[int]
        VERTICAL_FORMS: ClassVar["UnicodeBlock"]
        VERTICAL_FORMS_ID: ClassVar[int]
        VITHKUQI: ClassVar["UnicodeBlock"]
        VITHKUQI_ID: ClassVar[int]
        WANCHO: ClassVar["UnicodeBlock"]
        WANCHO_ID: ClassVar[int]
        WARANG_CITI: ClassVar["UnicodeBlock"]
        WARANG_CITI_ID: ClassVar[int]
        YEZIDI: ClassVar["UnicodeBlock"]
        YEZIDI_ID: ClassVar[int]
        YIJING_HEXAGRAM_SYMBOLS: ClassVar["UnicodeBlock"]
        YIJING_HEXAGRAM_SYMBOLS_ID: ClassVar[int]
        YI_RADICALS: ClassVar["UnicodeBlock"]
        YI_RADICALS_ID: ClassVar[int]
        YI_SYLLABLES: ClassVar["UnicodeBlock"]
        YI_SYLLABLES_ID: ClassVar[int]
        ZANABAZAR_SQUARE: ClassVar["UnicodeBlock"]
        ZANABAZAR_SQUARE_ID: ClassVar[int]
        ZNAMENNY_MUSICAL_NOTATION: ClassVar["UnicodeBlock"]
        ZNAMENNY_MUSICAL_NOTATION_ID: ClassVar[int]
        @staticmethod
        def getInstance(arg0: int) -> "UnicodeBlock": ...
        @staticmethod
        def of(arg0: int) -> "UnicodeBlock": ...
        @staticmethod
        def forName(arg0: str) -> "UnicodeBlock": ...
        def getID(self) -> int: ...

    class VerticalOrientation:
        ROTATED: ClassVar[int]
        TRANSFORMED_ROTATED: ClassVar[int]
        TRANSFORMED_UPRIGHT: ClassVar[int]
        UPRIGHT: ClassVar[int]

    class WordBreak:
        ALETTER: ClassVar[int]
        CR: ClassVar[int]
        DOUBLE_QUOTE: ClassVar[int]
        EXTEND: ClassVar[int]
        EXTENDNUMLET: ClassVar[int]
        E_BASE: ClassVar[int]
        E_BASE_GAZ: ClassVar[int]
        E_MODIFIER: ClassVar[int]
        FORMAT: ClassVar[int]
        GLUE_AFTER_ZWJ: ClassVar[int]
        HEBREW_LETTER: ClassVar[int]
        KATAKANA: ClassVar[int]
        LF: ClassVar[int]
        MIDLETTER: ClassVar[int]
        MIDNUM: ClassVar[int]
        MIDNUMLET: ClassVar[int]
        NEWLINE: ClassVar[int]
        NUMERIC: ClassVar[int]
        OTHER: ClassVar[int]
        REGIONAL_INDICATOR: ClassVar[int]
        SINGLE_QUOTE: ClassVar[int]
        WSEGSPACE: ClassVar[int]
        ZWJ: ClassVar[int]
