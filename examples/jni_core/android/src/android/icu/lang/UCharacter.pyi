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
    COMBINING_SPACING_MARK: ClassVar[int]
    CONNECTOR_PUNCTUATION: ClassVar[int]
    CONTROL: ClassVar[int]
    CURRENCY_SYMBOL: ClassVar[int]
    DASH_PUNCTUATION: ClassVar[int]
    DECIMAL_DIGIT_NUMBER: ClassVar[int]
    ENCLOSING_MARK: ClassVar[int]
    END_PUNCTUATION: ClassVar[int]
    FINAL_PUNCTUATION: ClassVar[int]
    FINAL_QUOTE_PUNCTUATION: ClassVar[int]
    FORMAT: ClassVar[int]
    GENERAL_OTHER_TYPES: ClassVar[int]
    INITIAL_PUNCTUATION: ClassVar[int]
    INITIAL_QUOTE_PUNCTUATION: ClassVar[int]
    LETTER_NUMBER: ClassVar[int]
    LINE_SEPARATOR: ClassVar[int]
    LOWERCASE_LETTER: ClassVar[int]
    MATH_SYMBOL: ClassVar[int]
    MODIFIER_LETTER: ClassVar[int]
    MODIFIER_SYMBOL: ClassVar[int]
    NON_SPACING_MARK: ClassVar[int]
    OTHER_LETTER: ClassVar[int]
    OTHER_NUMBER: ClassVar[int]
    OTHER_PUNCTUATION: ClassVar[int]
    OTHER_SYMBOL: ClassVar[int]
    PARAGRAPH_SEPARATOR: ClassVar[int]
    PRIVATE_USE: ClassVar[int]
    SPACE_SEPARATOR: ClassVar[int]
    START_PUNCTUATION: ClassVar[int]
    SURROGATE: ClassVar[int]
    TITLECASE_LETTER: ClassVar[int]
    UNASSIGNED: ClassVar[int]
    UPPERCASE_LETTER: ClassVar[int]
    ARABIC_NUMBER: ClassVar[int]
    BLOCK_SEPARATOR: ClassVar[int]
    BOUNDARY_NEUTRAL: ClassVar[int]
    COMMON_NUMBER_SEPARATOR: ClassVar[int]
    DIRECTIONALITY_ARABIC_NUMBER: ClassVar[int]
    DIRECTIONALITY_BOUNDARY_NEUTRAL: ClassVar[int]
    DIRECTIONALITY_COMMON_NUMBER_SEPARATOR: ClassVar[int]
    DIRECTIONALITY_EUROPEAN_NUMBER: ClassVar[int]
    DIRECTIONALITY_EUROPEAN_NUMBER_SEPARATOR: ClassVar[int]
    DIRECTIONALITY_EUROPEAN_NUMBER_TERMINATOR: ClassVar[int]
    DIRECTIONALITY_LEFT_TO_RIGHT: ClassVar[int]
    DIRECTIONALITY_LEFT_TO_RIGHT_EMBEDDING: ClassVar[int]
    DIRECTIONALITY_LEFT_TO_RIGHT_OVERRIDE: ClassVar[int]
    DIRECTIONALITY_NONSPACING_MARK: ClassVar[int]
    DIRECTIONALITY_OTHER_NEUTRALS: ClassVar[int]
    DIRECTIONALITY_PARAGRAPH_SEPARATOR: ClassVar[int]
    DIRECTIONALITY_POP_DIRECTIONAL_FORMAT: ClassVar[int]
    DIRECTIONALITY_RIGHT_TO_LEFT: ClassVar[int]
    DIRECTIONALITY_RIGHT_TO_LEFT_ARABIC: ClassVar[int]
    DIRECTIONALITY_RIGHT_TO_LEFT_EMBEDDING: ClassVar[int]
    DIRECTIONALITY_RIGHT_TO_LEFT_OVERRIDE: ClassVar[int]
    DIRECTIONALITY_SEGMENT_SEPARATOR: ClassVar[int]
    DIRECTIONALITY_UNDEFINED: ClassVar[int]
    DIRECTIONALITY_WHITESPACE: ClassVar[int]
    DIR_NON_SPACING_MARK: ClassVar[int]
    EUROPEAN_NUMBER: ClassVar[int]
    EUROPEAN_NUMBER_SEPARATOR: ClassVar[int]
    EUROPEAN_NUMBER_TERMINATOR: ClassVar[int]
    FIRST_STRONG_ISOLATE: ClassVar[int]
    LEFT_TO_RIGHT: ClassVar[int]
    LEFT_TO_RIGHT_EMBEDDING: ClassVar[int]
    LEFT_TO_RIGHT_ISOLATE: ClassVar[int]
    LEFT_TO_RIGHT_OVERRIDE: ClassVar[int]
    OTHER_NEUTRAL: ClassVar[int]
    POP_DIRECTIONAL_FORMAT: ClassVar[int]
    POP_DIRECTIONAL_ISOLATE: ClassVar[int]
    RIGHT_TO_LEFT: ClassVar[int]
    RIGHT_TO_LEFT_ARABIC: ClassVar[int]
    RIGHT_TO_LEFT_EMBEDDING: ClassVar[int]
    RIGHT_TO_LEFT_ISOLATE: ClassVar[int]
    RIGHT_TO_LEFT_OVERRIDE: ClassVar[int]
    SEGMENT_SEPARATOR: ClassVar[int]
    WHITE_SPACE_NEUTRAL: ClassVar[int]
    @staticmethod
    def getDirection(p0: int) -> int: ...
    @staticmethod
    def getMirror(p0: int) -> int: ...
    @staticmethod
    def getAge(p0: int) -> VersionInfo: ...
    @staticmethod
    def getCharFromName(p0: str) -> int: ...
    @overload
    @staticmethod
    def foldCase(p0: int, p1: bool) -> int: ...
    @overload
    @staticmethod
    def foldCase(p0: int, p1: int) -> int: ...
    @overload
    @staticmethod
    def foldCase(p0: str, p1: bool) -> str: ...
    @overload
    @staticmethod
    def foldCase(p0: str, p1: int) -> str: ...
    @staticmethod
    def getBidiPairedBracket(p0: int) -> int: ...
    @staticmethod
    def getCharFromExtendedName(p0: str) -> int: ...
    @staticmethod
    def getCharFromNameAlias(p0: str) -> int: ...
    @staticmethod
    def getExtendedName(p0: int) -> str: ...
    @staticmethod
    def getExtendedNameIterator() -> ValueIterator: ...
    @staticmethod
    def getHanNumericValue(p0: int) -> int: ...
    @staticmethod
    def getIntPropertyMaxValue(p0: int) -> int: ...
    @staticmethod
    def getIntPropertyMinValue(p0: int) -> int: ...
    @staticmethod
    def getIntPropertyValue(p0: int, p1: int) -> int: ...
    @staticmethod
    def getNameAlias(p0: int) -> str: ...
    @staticmethod
    def getNameIterator() -> ValueIterator: ...
    @staticmethod
    def getPropertyEnum(p0: str) -> int: ...
    @staticmethod
    def getPropertyValueEnum(p0: int, p1: str) -> int: ...
    @staticmethod
    def getPropertyValueName(p0: int, p1: int, p2: int) -> str: ...
    @staticmethod
    def getTypeIterator() -> RangeValueIterator: ...
    @staticmethod
    def getUnicodeNumericValue(p0: int) -> float: ...
    @staticmethod
    def getUnicodeVersion() -> VersionInfo: ...
    @overload
    @staticmethod
    def hasBinaryProperty(p0: str, p1: int) -> bool: ...
    @overload
    @staticmethod
    def hasBinaryProperty(p0: int, p1: int) -> bool: ...
    @staticmethod
    def isBMP(p0: int) -> bool: ...
    @staticmethod
    def isBaseForm(p0: int) -> bool: ...
    @overload
    @staticmethod
    def isLegal(p0: str) -> bool: ...
    @overload
    @staticmethod
    def isLegal(p0: int) -> bool: ...
    @staticmethod
    def isPrintable(p0: int) -> bool: ...
    @staticmethod
    def isUAlphabetic(p0: int) -> bool: ...
    @staticmethod
    def isULowercase(p0: int) -> bool: ...
    @staticmethod
    def isUUppercase(p0: int) -> bool: ...
    @staticmethod
    def isUWhiteSpace(p0: int) -> bool: ...
    @overload
    @staticmethod
    def getName(p0: int) -> str: ...
    @overload
    @staticmethod
    def getName(p0: str, p1: str) -> str: ...
    @staticmethod
    def isJavaIdentifierStart(p0: int) -> bool: ...
    @staticmethod
    def isJavaIdentifierPart(p0: int) -> bool: ...
    @staticmethod
    def toString(p0: int) -> str: ...
    @staticmethod
    def isDigit(p0: int) -> bool: ...
    @staticmethod
    def isLowerCase(p0: int) -> bool: ...
    @staticmethod
    def isUpperCase(p0: int) -> bool: ...
    @staticmethod
    def isWhitespace(p0: int) -> bool: ...
    @overload
    @staticmethod
    def toChars(p0: int) -> Any: ...
    @overload
    @staticmethod
    def toChars(p0: int, p1: Any, p2: int) -> int: ...
    @overload
    @staticmethod
    def isHighSurrogate(p0: str) -> bool: ...
    @overload
    @staticmethod
    def isHighSurrogate(p0: int) -> bool: ...
    @overload
    @staticmethod
    def isLowSurrogate(p0: int) -> bool: ...
    @overload
    @staticmethod
    def isLowSurrogate(p0: str) -> bool: ...
    @staticmethod
    def isSupplementaryCodePoint(p0: int) -> bool: ...
    @overload
    @staticmethod
    def toCodePoint(p0: int, p1: int) -> int: ...
    @overload
    @staticmethod
    def toCodePoint(p0: str, p1: str) -> int: ...
    @overload
    @staticmethod
    def codePointAt(p0: Any, p1: int) -> int: ...
    @overload
    @staticmethod
    def codePointAt(p0: str, p1: int) -> int: ...
    @overload
    @staticmethod
    def codePointAt(p0: Any, p1: int, p2: int) -> int: ...
    @overload
    @staticmethod
    def codePointBefore(p0: str, p1: int) -> int: ...
    @overload
    @staticmethod
    def codePointBefore(p0: Any, p1: int, p2: int) -> int: ...
    @overload
    @staticmethod
    def codePointBefore(p0: Any, p1: int) -> int: ...
    @overload
    @staticmethod
    def codePointCount(p0: str, p1: int, p2: int) -> int: ...
    @overload
    @staticmethod
    def codePointCount(p0: Any, p1: int, p2: int) -> int: ...
    @overload
    @staticmethod
    def offsetByCodePoints(p0: Any, p1: int, p2: int, p3: int, p4: int) -> int: ...
    @overload
    @staticmethod
    def offsetByCodePoints(p0: str, p1: int, p2: int) -> int: ...
    @overload
    @staticmethod
    def toLowerCase(p0: ULocale, p1: str) -> str: ...
    @overload
    @staticmethod
    def toLowerCase(p0: int) -> int: ...
    @overload
    @staticmethod
    def toLowerCase(p0: str) -> str: ...
    @overload
    @staticmethod
    def toLowerCase(p0: Locale, p1: str) -> str: ...
    @overload
    @staticmethod
    def toUpperCase(p0: ULocale, p1: str) -> str: ...
    @overload
    @staticmethod
    def toUpperCase(p0: str) -> str: ...
    @overload
    @staticmethod
    def toUpperCase(p0: int) -> int: ...
    @overload
    @staticmethod
    def toUpperCase(p0: Locale, p1: str) -> str: ...
    @staticmethod
    def getType(p0: int) -> int: ...
    @staticmethod
    def isLetter(p0: int) -> bool: ...
    @staticmethod
    def isLetterOrDigit(p0: int) -> bool: ...
    @staticmethod
    def getPropertyName(p0: int, p1: int) -> str: ...
    @staticmethod
    def getCombiningClass(p0: int) -> int: ...
    @staticmethod
    def isSupplementary(p0: int) -> bool: ...
    @staticmethod
    def isValidCodePoint(p0: int) -> bool: ...
    @staticmethod
    def isTitleCase(p0: int) -> bool: ...
    @staticmethod
    def isDefined(p0: int) -> bool: ...
    @staticmethod
    def isUnicodeIdentifierStart(p0: int) -> bool: ...
    @staticmethod
    def isUnicodeIdentifierPart(p0: int) -> bool: ...
    @staticmethod
    def isIdentifierIgnorable(p0: int) -> bool: ...
    @overload
    @staticmethod
    def toTitleCase(p0: str, p1: BreakIterator) -> str: ...
    @overload
    @staticmethod
    def toTitleCase(p0: int) -> int: ...
    @overload
    @staticmethod
    def toTitleCase(p0: ULocale, p1: str, p2: BreakIterator, p3: int) -> str: ...
    @overload
    @staticmethod
    def toTitleCase(p0: Locale, p1: str, p2: BreakIterator) -> str: ...
    @overload
    @staticmethod
    def toTitleCase(p0: Locale, p1: str, p2: BreakIterator, p3: int) -> str: ...
    @overload
    @staticmethod
    def toTitleCase(p0: ULocale, p1: str, p2: BreakIterator) -> str: ...
    @overload
    @staticmethod
    def digit(p0: int, p1: int) -> int: ...
    @overload
    @staticmethod
    def digit(p0: int) -> int: ...
    @staticmethod
    def getNumericValue(p0: int) -> int: ...
    @staticmethod
    def isSpaceChar(p0: int) -> bool: ...
    @staticmethod
    def isISOControl(p0: int) -> bool: ...
    @staticmethod
    def getDirectionality(p0: int) -> int: ...
    @staticmethod
    def isMirrored(p0: int) -> bool: ...
    @overload
    @staticmethod
    def getCodePoint(p0: str) -> int: ...
    @overload
    @staticmethod
    def getCodePoint(p0: int, p1: int) -> int: ...
    @overload
    @staticmethod
    def getCodePoint(p0: str, p1: str) -> int: ...
    @overload
    @staticmethod
    def isSurrogatePair(p0: int, p1: int) -> bool: ...
    @overload
    @staticmethod
    def isSurrogatePair(p0: str, p1: str) -> bool: ...
    @staticmethod
    def charCount(p0: int) -> int: ...
    @staticmethod
    def forDigit(p0: int, p1: int) -> str: ...

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

    class VerticalOrientation:
        ROTATED: ClassVar[int]
        TRANSFORMED_ROTATED: ClassVar[int]
        TRANSFORMED_UPRIGHT: ClassVar[int]
        UPRIGHT: ClassVar[int]

    class UnicodeBlock:
        ADLAM: ClassVar[Any]
        ADLAM_ID: ClassVar[int]
        AEGEAN_NUMBERS: ClassVar[Any]
        AEGEAN_NUMBERS_ID: ClassVar[int]
        AHOM: ClassVar[Any]
        AHOM_ID: ClassVar[int]
        ALCHEMICAL_SYMBOLS: ClassVar[Any]
        ALCHEMICAL_SYMBOLS_ID: ClassVar[int]
        ALPHABETIC_PRESENTATION_FORMS: ClassVar[Any]
        ALPHABETIC_PRESENTATION_FORMS_ID: ClassVar[int]
        ANATOLIAN_HIEROGLYPHS: ClassVar[Any]
        ANATOLIAN_HIEROGLYPHS_ID: ClassVar[int]
        ANCIENT_GREEK_MUSICAL_NOTATION: ClassVar[Any]
        ANCIENT_GREEK_MUSICAL_NOTATION_ID: ClassVar[int]
        ANCIENT_GREEK_NUMBERS: ClassVar[Any]
        ANCIENT_GREEK_NUMBERS_ID: ClassVar[int]
        ANCIENT_SYMBOLS: ClassVar[Any]
        ANCIENT_SYMBOLS_ID: ClassVar[int]
        ARABIC: ClassVar[Any]
        ARABIC_EXTENDED_A: ClassVar[Any]
        ARABIC_EXTENDED_A_ID: ClassVar[int]
        ARABIC_EXTENDED_B: ClassVar[Any]
        ARABIC_EXTENDED_B_ID: ClassVar[int]
        ARABIC_EXTENDED_C: ClassVar[Any]
        ARABIC_EXTENDED_C_ID: ClassVar[int]
        ARABIC_ID: ClassVar[int]
        ARABIC_MATHEMATICAL_ALPHABETIC_SYMBOLS: ClassVar[Any]
        ARABIC_MATHEMATICAL_ALPHABETIC_SYMBOLS_ID: ClassVar[int]
        ARABIC_PRESENTATION_FORMS_A: ClassVar[Any]
        ARABIC_PRESENTATION_FORMS_A_ID: ClassVar[int]
        ARABIC_PRESENTATION_FORMS_B: ClassVar[Any]
        ARABIC_PRESENTATION_FORMS_B_ID: ClassVar[int]
        ARABIC_SUPPLEMENT: ClassVar[Any]
        ARABIC_SUPPLEMENT_ID: ClassVar[int]
        ARMENIAN: ClassVar[Any]
        ARMENIAN_ID: ClassVar[int]
        ARROWS: ClassVar[Any]
        ARROWS_ID: ClassVar[int]
        AVESTAN: ClassVar[Any]
        AVESTAN_ID: ClassVar[int]
        BALINESE: ClassVar[Any]
        BALINESE_ID: ClassVar[int]
        BAMUM: ClassVar[Any]
        BAMUM_ID: ClassVar[int]
        BAMUM_SUPPLEMENT: ClassVar[Any]
        BAMUM_SUPPLEMENT_ID: ClassVar[int]
        BASIC_LATIN: ClassVar[Any]
        BASIC_LATIN_ID: ClassVar[int]
        BASSA_VAH: ClassVar[Any]
        BASSA_VAH_ID: ClassVar[int]
        BATAK: ClassVar[Any]
        BATAK_ID: ClassVar[int]
        BENGALI: ClassVar[Any]
        BENGALI_ID: ClassVar[int]
        BHAIKSUKI: ClassVar[Any]
        BHAIKSUKI_ID: ClassVar[int]
        BLOCK_ELEMENTS: ClassVar[Any]
        BLOCK_ELEMENTS_ID: ClassVar[int]
        BOPOMOFO: ClassVar[Any]
        BOPOMOFO_EXTENDED: ClassVar[Any]
        BOPOMOFO_EXTENDED_ID: ClassVar[int]
        BOPOMOFO_ID: ClassVar[int]
        BOX_DRAWING: ClassVar[Any]
        BOX_DRAWING_ID: ClassVar[int]
        BRAHMI: ClassVar[Any]
        BRAHMI_ID: ClassVar[int]
        BRAILLE_PATTERNS: ClassVar[Any]
        BRAILLE_PATTERNS_ID: ClassVar[int]
        BUGINESE: ClassVar[Any]
        BUGINESE_ID: ClassVar[int]
        BUHID: ClassVar[Any]
        BUHID_ID: ClassVar[int]
        BYZANTINE_MUSICAL_SYMBOLS: ClassVar[Any]
        BYZANTINE_MUSICAL_SYMBOLS_ID: ClassVar[int]
        CARIAN: ClassVar[Any]
        CARIAN_ID: ClassVar[int]
        CAUCASIAN_ALBANIAN: ClassVar[Any]
        CAUCASIAN_ALBANIAN_ID: ClassVar[int]
        CHAKMA: ClassVar[Any]
        CHAKMA_ID: ClassVar[int]
        CHAM: ClassVar[Any]
        CHAM_ID: ClassVar[int]
        CHEROKEE: ClassVar[Any]
        CHEROKEE_ID: ClassVar[int]
        CHEROKEE_SUPPLEMENT: ClassVar[Any]
        CHEROKEE_SUPPLEMENT_ID: ClassVar[int]
        CHESS_SYMBOLS: ClassVar[Any]
        CHESS_SYMBOLS_ID: ClassVar[int]
        CHORASMIAN: ClassVar[Any]
        CHORASMIAN_ID: ClassVar[int]
        CJK_COMPATIBILITY: ClassVar[Any]
        CJK_COMPATIBILITY_FORMS: ClassVar[Any]
        CJK_COMPATIBILITY_FORMS_ID: ClassVar[int]
        CJK_COMPATIBILITY_ID: ClassVar[int]
        CJK_COMPATIBILITY_IDEOGRAPHS: ClassVar[Any]
        CJK_COMPATIBILITY_IDEOGRAPHS_ID: ClassVar[int]
        CJK_COMPATIBILITY_IDEOGRAPHS_SUPPLEMENT: ClassVar[Any]
        CJK_COMPATIBILITY_IDEOGRAPHS_SUPPLEMENT_ID: ClassVar[int]
        CJK_RADICALS_SUPPLEMENT: ClassVar[Any]
        CJK_RADICALS_SUPPLEMENT_ID: ClassVar[int]
        CJK_STROKES: ClassVar[Any]
        CJK_STROKES_ID: ClassVar[int]
        CJK_SYMBOLS_AND_PUNCTUATION: ClassVar[Any]
        CJK_SYMBOLS_AND_PUNCTUATION_ID: ClassVar[int]
        CJK_UNIFIED_IDEOGRAPHS: ClassVar[Any]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_A: ClassVar[Any]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_A_ID: ClassVar[int]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_B: ClassVar[Any]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_B_ID: ClassVar[int]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_C: ClassVar[Any]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_C_ID: ClassVar[int]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_D: ClassVar[Any]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_D_ID: ClassVar[int]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_E: ClassVar[Any]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_E_ID: ClassVar[int]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_F: ClassVar[Any]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_F_ID: ClassVar[int]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_G: ClassVar[Any]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_G_ID: ClassVar[int]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_H: ClassVar[Any]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_H_ID: ClassVar[int]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_I: ClassVar[Any]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_I_ID: ClassVar[int]
        CJK_UNIFIED_IDEOGRAPHS_ID: ClassVar[int]
        COMBINING_DIACRITICAL_MARKS: ClassVar[Any]
        COMBINING_DIACRITICAL_MARKS_EXTENDED: ClassVar[Any]
        COMBINING_DIACRITICAL_MARKS_EXTENDED_ID: ClassVar[int]
        COMBINING_DIACRITICAL_MARKS_ID: ClassVar[int]
        COMBINING_DIACRITICAL_MARKS_SUPPLEMENT: ClassVar[Any]
        COMBINING_DIACRITICAL_MARKS_SUPPLEMENT_ID: ClassVar[int]
        COMBINING_HALF_MARKS: ClassVar[Any]
        COMBINING_HALF_MARKS_ID: ClassVar[int]
        COMBINING_MARKS_FOR_SYMBOLS: ClassVar[Any]
        COMBINING_MARKS_FOR_SYMBOLS_ID: ClassVar[int]
        COMMON_INDIC_NUMBER_FORMS: ClassVar[Any]
        COMMON_INDIC_NUMBER_FORMS_ID: ClassVar[int]
        CONTROL_PICTURES: ClassVar[Any]
        CONTROL_PICTURES_ID: ClassVar[int]
        COPTIC: ClassVar[Any]
        COPTIC_EPACT_NUMBERS: ClassVar[Any]
        COPTIC_EPACT_NUMBERS_ID: ClassVar[int]
        COPTIC_ID: ClassVar[int]
        COUNTING_ROD_NUMERALS: ClassVar[Any]
        COUNTING_ROD_NUMERALS_ID: ClassVar[int]
        CUNEIFORM: ClassVar[Any]
        CUNEIFORM_ID: ClassVar[int]
        CUNEIFORM_NUMBERS_AND_PUNCTUATION: ClassVar[Any]
        CUNEIFORM_NUMBERS_AND_PUNCTUATION_ID: ClassVar[int]
        CURRENCY_SYMBOLS: ClassVar[Any]
        CURRENCY_SYMBOLS_ID: ClassVar[int]
        CYPRIOT_SYLLABARY: ClassVar[Any]
        CYPRIOT_SYLLABARY_ID: ClassVar[int]
        CYPRO_MINOAN: ClassVar[Any]
        CYPRO_MINOAN_ID: ClassVar[int]
        CYRILLIC: ClassVar[Any]
        CYRILLIC_EXTENDED_A: ClassVar[Any]
        CYRILLIC_EXTENDED_A_ID: ClassVar[int]
        CYRILLIC_EXTENDED_B: ClassVar[Any]
        CYRILLIC_EXTENDED_B_ID: ClassVar[int]
        CYRILLIC_EXTENDED_C: ClassVar[Any]
        CYRILLIC_EXTENDED_C_ID: ClassVar[int]
        CYRILLIC_EXTENDED_D: ClassVar[Any]
        CYRILLIC_EXTENDED_D_ID: ClassVar[int]
        CYRILLIC_ID: ClassVar[int]
        CYRILLIC_SUPPLEMENT: ClassVar[Any]
        CYRILLIC_SUPPLEMENTARY: ClassVar[Any]
        CYRILLIC_SUPPLEMENTARY_ID: ClassVar[int]
        CYRILLIC_SUPPLEMENT_ID: ClassVar[int]
        DESERET: ClassVar[Any]
        DESERET_ID: ClassVar[int]
        DEVANAGARI: ClassVar[Any]
        DEVANAGARI_EXTENDED: ClassVar[Any]
        DEVANAGARI_EXTENDED_A: ClassVar[Any]
        DEVANAGARI_EXTENDED_A_ID: ClassVar[int]
        DEVANAGARI_EXTENDED_ID: ClassVar[int]
        DEVANAGARI_ID: ClassVar[int]
        DINGBATS: ClassVar[Any]
        DINGBATS_ID: ClassVar[int]
        DIVES_AKURU: ClassVar[Any]
        DIVES_AKURU_ID: ClassVar[int]
        DOGRA: ClassVar[Any]
        DOGRA_ID: ClassVar[int]
        DOMINO_TILES: ClassVar[Any]
        DOMINO_TILES_ID: ClassVar[int]
        DUPLOYAN: ClassVar[Any]
        DUPLOYAN_ID: ClassVar[int]
        EARLY_DYNASTIC_CUNEIFORM: ClassVar[Any]
        EARLY_DYNASTIC_CUNEIFORM_ID: ClassVar[int]
        EGYPTIAN_HIEROGLYPHS: ClassVar[Any]
        EGYPTIAN_HIEROGLYPHS_EXTENDED_A: ClassVar[Any]
        EGYPTIAN_HIEROGLYPHS_EXTENDED_A_ID: ClassVar[int]
        EGYPTIAN_HIEROGLYPHS_ID: ClassVar[int]
        EGYPTIAN_HIEROGLYPH_FORMAT_CONTROLS: ClassVar[Any]
        EGYPTIAN_HIEROGLYPH_FORMAT_CONTROLS_ID: ClassVar[int]
        ELBASAN: ClassVar[Any]
        ELBASAN_ID: ClassVar[int]
        ELYMAIC: ClassVar[Any]
        ELYMAIC_ID: ClassVar[int]
        EMOTICONS: ClassVar[Any]
        EMOTICONS_ID: ClassVar[int]
        ENCLOSED_ALPHANUMERICS: ClassVar[Any]
        ENCLOSED_ALPHANUMERICS_ID: ClassVar[int]
        ENCLOSED_ALPHANUMERIC_SUPPLEMENT: ClassVar[Any]
        ENCLOSED_ALPHANUMERIC_SUPPLEMENT_ID: ClassVar[int]
        ENCLOSED_CJK_LETTERS_AND_MONTHS: ClassVar[Any]
        ENCLOSED_CJK_LETTERS_AND_MONTHS_ID: ClassVar[int]
        ENCLOSED_IDEOGRAPHIC_SUPPLEMENT: ClassVar[Any]
        ENCLOSED_IDEOGRAPHIC_SUPPLEMENT_ID: ClassVar[int]
        ETHIOPIC: ClassVar[Any]
        ETHIOPIC_EXTENDED: ClassVar[Any]
        ETHIOPIC_EXTENDED_A: ClassVar[Any]
        ETHIOPIC_EXTENDED_A_ID: ClassVar[int]
        ETHIOPIC_EXTENDED_B: ClassVar[Any]
        ETHIOPIC_EXTENDED_B_ID: ClassVar[int]
        ETHIOPIC_EXTENDED_ID: ClassVar[int]
        ETHIOPIC_ID: ClassVar[int]
        ETHIOPIC_SUPPLEMENT: ClassVar[Any]
        ETHIOPIC_SUPPLEMENT_ID: ClassVar[int]
        GARAY: ClassVar[Any]
        GARAY_ID: ClassVar[int]
        GENERAL_PUNCTUATION: ClassVar[Any]
        GENERAL_PUNCTUATION_ID: ClassVar[int]
        GEOMETRIC_SHAPES: ClassVar[Any]
        GEOMETRIC_SHAPES_EXTENDED: ClassVar[Any]
        GEOMETRIC_SHAPES_EXTENDED_ID: ClassVar[int]
        GEOMETRIC_SHAPES_ID: ClassVar[int]
        GEORGIAN: ClassVar[Any]
        GEORGIAN_EXTENDED: ClassVar[Any]
        GEORGIAN_EXTENDED_ID: ClassVar[int]
        GEORGIAN_ID: ClassVar[int]
        GEORGIAN_SUPPLEMENT: ClassVar[Any]
        GEORGIAN_SUPPLEMENT_ID: ClassVar[int]
        GLAGOLITIC: ClassVar[Any]
        GLAGOLITIC_ID: ClassVar[int]
        GLAGOLITIC_SUPPLEMENT: ClassVar[Any]
        GLAGOLITIC_SUPPLEMENT_ID: ClassVar[int]
        GOTHIC: ClassVar[Any]
        GOTHIC_ID: ClassVar[int]
        GRANTHA: ClassVar[Any]
        GRANTHA_ID: ClassVar[int]
        GREEK: ClassVar[Any]
        GREEK_EXTENDED: ClassVar[Any]
        GREEK_EXTENDED_ID: ClassVar[int]
        GREEK_ID: ClassVar[int]
        GUJARATI: ClassVar[Any]
        GUJARATI_ID: ClassVar[int]
        GUNJALA_GONDI: ClassVar[Any]
        GUNJALA_GONDI_ID: ClassVar[int]
        GURMUKHI: ClassVar[Any]
        GURMUKHI_ID: ClassVar[int]
        GURUNG_KHEMA: ClassVar[Any]
        GURUNG_KHEMA_ID: ClassVar[int]
        HALFWIDTH_AND_FULLWIDTH_FORMS: ClassVar[Any]
        HALFWIDTH_AND_FULLWIDTH_FORMS_ID: ClassVar[int]
        HANGUL_COMPATIBILITY_JAMO: ClassVar[Any]
        HANGUL_COMPATIBILITY_JAMO_ID: ClassVar[int]
        HANGUL_JAMO: ClassVar[Any]
        HANGUL_JAMO_EXTENDED_A: ClassVar[Any]
        HANGUL_JAMO_EXTENDED_A_ID: ClassVar[int]
        HANGUL_JAMO_EXTENDED_B: ClassVar[Any]
        HANGUL_JAMO_EXTENDED_B_ID: ClassVar[int]
        HANGUL_JAMO_ID: ClassVar[int]
        HANGUL_SYLLABLES: ClassVar[Any]
        HANGUL_SYLLABLES_ID: ClassVar[int]
        HANIFI_ROHINGYA: ClassVar[Any]
        HANIFI_ROHINGYA_ID: ClassVar[int]
        HANUNOO: ClassVar[Any]
        HANUNOO_ID: ClassVar[int]
        HATRAN: ClassVar[Any]
        HATRAN_ID: ClassVar[int]
        HEBREW: ClassVar[Any]
        HEBREW_ID: ClassVar[int]
        HIGH_PRIVATE_USE_SURROGATES: ClassVar[Any]
        HIGH_PRIVATE_USE_SURROGATES_ID: ClassVar[int]
        HIGH_SURROGATES: ClassVar[Any]
        HIGH_SURROGATES_ID: ClassVar[int]
        HIRAGANA: ClassVar[Any]
        HIRAGANA_ID: ClassVar[int]
        IDEOGRAPHIC_DESCRIPTION_CHARACTERS: ClassVar[Any]
        IDEOGRAPHIC_DESCRIPTION_CHARACTERS_ID: ClassVar[int]
        IDEOGRAPHIC_SYMBOLS_AND_PUNCTUATION: ClassVar[Any]
        IDEOGRAPHIC_SYMBOLS_AND_PUNCTUATION_ID: ClassVar[int]
        IMPERIAL_ARAMAIC: ClassVar[Any]
        IMPERIAL_ARAMAIC_ID: ClassVar[int]
        INDIC_SIYAQ_NUMBERS: ClassVar[Any]
        INDIC_SIYAQ_NUMBERS_ID: ClassVar[int]
        INSCRIPTIONAL_PAHLAVI: ClassVar[Any]
        INSCRIPTIONAL_PAHLAVI_ID: ClassVar[int]
        INSCRIPTIONAL_PARTHIAN: ClassVar[Any]
        INSCRIPTIONAL_PARTHIAN_ID: ClassVar[int]
        INVALID_CODE: ClassVar[Any]
        INVALID_CODE_ID: ClassVar[int]
        IPA_EXTENSIONS: ClassVar[Any]
        IPA_EXTENSIONS_ID: ClassVar[int]
        JAVANESE: ClassVar[Any]
        JAVANESE_ID: ClassVar[int]
        KAITHI: ClassVar[Any]
        KAITHI_ID: ClassVar[int]
        KAKTOVIK_NUMERALS: ClassVar[Any]
        KAKTOVIK_NUMERALS_ID: ClassVar[int]
        KANA_EXTENDED_A: ClassVar[Any]
        KANA_EXTENDED_A_ID: ClassVar[int]
        KANA_EXTENDED_B: ClassVar[Any]
        KANA_EXTENDED_B_ID: ClassVar[int]
        KANA_SUPPLEMENT: ClassVar[Any]
        KANA_SUPPLEMENT_ID: ClassVar[int]
        KANBUN: ClassVar[Any]
        KANBUN_ID: ClassVar[int]
        KANGXI_RADICALS: ClassVar[Any]
        KANGXI_RADICALS_ID: ClassVar[int]
        KANNADA: ClassVar[Any]
        KANNADA_ID: ClassVar[int]
        KATAKANA: ClassVar[Any]
        KATAKANA_ID: ClassVar[int]
        KATAKANA_PHONETIC_EXTENSIONS: ClassVar[Any]
        KATAKANA_PHONETIC_EXTENSIONS_ID: ClassVar[int]
        KAWI: ClassVar[Any]
        KAWI_ID: ClassVar[int]
        KAYAH_LI: ClassVar[Any]
        KAYAH_LI_ID: ClassVar[int]
        KHAROSHTHI: ClassVar[Any]
        KHAROSHTHI_ID: ClassVar[int]
        KHITAN_SMALL_SCRIPT: ClassVar[Any]
        KHITAN_SMALL_SCRIPT_ID: ClassVar[int]
        KHMER: ClassVar[Any]
        KHMER_ID: ClassVar[int]
        KHMER_SYMBOLS: ClassVar[Any]
        KHMER_SYMBOLS_ID: ClassVar[int]
        KHOJKI: ClassVar[Any]
        KHOJKI_ID: ClassVar[int]
        KHUDAWADI: ClassVar[Any]
        KHUDAWADI_ID: ClassVar[int]
        KIRAT_RAI: ClassVar[Any]
        KIRAT_RAI_ID: ClassVar[int]
        LAO: ClassVar[Any]
        LAO_ID: ClassVar[int]
        LATIN_1_SUPPLEMENT: ClassVar[Any]
        LATIN_1_SUPPLEMENT_ID: ClassVar[int]
        LATIN_EXTENDED_A: ClassVar[Any]
        LATIN_EXTENDED_ADDITIONAL: ClassVar[Any]
        LATIN_EXTENDED_ADDITIONAL_ID: ClassVar[int]
        LATIN_EXTENDED_A_ID: ClassVar[int]
        LATIN_EXTENDED_B: ClassVar[Any]
        LATIN_EXTENDED_B_ID: ClassVar[int]
        LATIN_EXTENDED_C: ClassVar[Any]
        LATIN_EXTENDED_C_ID: ClassVar[int]
        LATIN_EXTENDED_D: ClassVar[Any]
        LATIN_EXTENDED_D_ID: ClassVar[int]
        LATIN_EXTENDED_E: ClassVar[Any]
        LATIN_EXTENDED_E_ID: ClassVar[int]
        LATIN_EXTENDED_F: ClassVar[Any]
        LATIN_EXTENDED_F_ID: ClassVar[int]
        LATIN_EXTENDED_G: ClassVar[Any]
        LATIN_EXTENDED_G_ID: ClassVar[int]
        LEPCHA: ClassVar[Any]
        LEPCHA_ID: ClassVar[int]
        LETTERLIKE_SYMBOLS: ClassVar[Any]
        LETTERLIKE_SYMBOLS_ID: ClassVar[int]
        LIMBU: ClassVar[Any]
        LIMBU_ID: ClassVar[int]
        LINEAR_A: ClassVar[Any]
        LINEAR_A_ID: ClassVar[int]
        LINEAR_B_IDEOGRAMS: ClassVar[Any]
        LINEAR_B_IDEOGRAMS_ID: ClassVar[int]
        LINEAR_B_SYLLABARY: ClassVar[Any]
        LINEAR_B_SYLLABARY_ID: ClassVar[int]
        LISU: ClassVar[Any]
        LISU_ID: ClassVar[int]
        LISU_SUPPLEMENT: ClassVar[Any]
        LISU_SUPPLEMENT_ID: ClassVar[int]
        LOW_SURROGATES: ClassVar[Any]
        LOW_SURROGATES_ID: ClassVar[int]
        LYCIAN: ClassVar[Any]
        LYCIAN_ID: ClassVar[int]
        LYDIAN: ClassVar[Any]
        LYDIAN_ID: ClassVar[int]
        MAHAJANI: ClassVar[Any]
        MAHAJANI_ID: ClassVar[int]
        MAHJONG_TILES: ClassVar[Any]
        MAHJONG_TILES_ID: ClassVar[int]
        MAKASAR: ClassVar[Any]
        MAKASAR_ID: ClassVar[int]
        MALAYALAM: ClassVar[Any]
        MALAYALAM_ID: ClassVar[int]
        MANDAIC: ClassVar[Any]
        MANDAIC_ID: ClassVar[int]
        MANICHAEAN: ClassVar[Any]
        MANICHAEAN_ID: ClassVar[int]
        MARCHEN: ClassVar[Any]
        MARCHEN_ID: ClassVar[int]
        MASARAM_GONDI: ClassVar[Any]
        MASARAM_GONDI_ID: ClassVar[int]
        MATHEMATICAL_ALPHANUMERIC_SYMBOLS: ClassVar[Any]
        MATHEMATICAL_ALPHANUMERIC_SYMBOLS_ID: ClassVar[int]
        MATHEMATICAL_OPERATORS: ClassVar[Any]
        MATHEMATICAL_OPERATORS_ID: ClassVar[int]
        MAYAN_NUMERALS: ClassVar[Any]
        MAYAN_NUMERALS_ID: ClassVar[int]
        MEDEFAIDRIN: ClassVar[Any]
        MEDEFAIDRIN_ID: ClassVar[int]
        MEETEI_MAYEK: ClassVar[Any]
        MEETEI_MAYEK_EXTENSIONS: ClassVar[Any]
        MEETEI_MAYEK_EXTENSIONS_ID: ClassVar[int]
        MEETEI_MAYEK_ID: ClassVar[int]
        MENDE_KIKAKUI: ClassVar[Any]
        MENDE_KIKAKUI_ID: ClassVar[int]
        MEROITIC_CURSIVE: ClassVar[Any]
        MEROITIC_CURSIVE_ID: ClassVar[int]
        MEROITIC_HIEROGLYPHS: ClassVar[Any]
        MEROITIC_HIEROGLYPHS_ID: ClassVar[int]
        MIAO: ClassVar[Any]
        MIAO_ID: ClassVar[int]
        MISCELLANEOUS_MATHEMATICAL_SYMBOLS_A: ClassVar[Any]
        MISCELLANEOUS_MATHEMATICAL_SYMBOLS_A_ID: ClassVar[int]
        MISCELLANEOUS_MATHEMATICAL_SYMBOLS_B: ClassVar[Any]
        MISCELLANEOUS_MATHEMATICAL_SYMBOLS_B_ID: ClassVar[int]
        MISCELLANEOUS_SYMBOLS: ClassVar[Any]
        MISCELLANEOUS_SYMBOLS_AND_ARROWS: ClassVar[Any]
        MISCELLANEOUS_SYMBOLS_AND_ARROWS_ID: ClassVar[int]
        MISCELLANEOUS_SYMBOLS_AND_PICTOGRAPHS: ClassVar[Any]
        MISCELLANEOUS_SYMBOLS_AND_PICTOGRAPHS_ID: ClassVar[int]
        MISCELLANEOUS_SYMBOLS_ID: ClassVar[int]
        MISCELLANEOUS_TECHNICAL: ClassVar[Any]
        MISCELLANEOUS_TECHNICAL_ID: ClassVar[int]
        MODI: ClassVar[Any]
        MODIFIER_TONE_LETTERS: ClassVar[Any]
        MODIFIER_TONE_LETTERS_ID: ClassVar[int]
        MODI_ID: ClassVar[int]
        MONGOLIAN: ClassVar[Any]
        MONGOLIAN_ID: ClassVar[int]
        MONGOLIAN_SUPPLEMENT: ClassVar[Any]
        MONGOLIAN_SUPPLEMENT_ID: ClassVar[int]
        MRO: ClassVar[Any]
        MRO_ID: ClassVar[int]
        MULTANI: ClassVar[Any]
        MULTANI_ID: ClassVar[int]
        MUSICAL_SYMBOLS: ClassVar[Any]
        MUSICAL_SYMBOLS_ID: ClassVar[int]
        MYANMAR: ClassVar[Any]
        MYANMAR_EXTENDED_A: ClassVar[Any]
        MYANMAR_EXTENDED_A_ID: ClassVar[int]
        MYANMAR_EXTENDED_B: ClassVar[Any]
        MYANMAR_EXTENDED_B_ID: ClassVar[int]
        MYANMAR_EXTENDED_C: ClassVar[Any]
        MYANMAR_EXTENDED_C_ID: ClassVar[int]
        MYANMAR_ID: ClassVar[int]
        NABATAEAN: ClassVar[Any]
        NABATAEAN_ID: ClassVar[int]
        NAG_MUNDARI: ClassVar[Any]
        NAG_MUNDARI_ID: ClassVar[int]
        NANDINAGARI: ClassVar[Any]
        NANDINAGARI_ID: ClassVar[int]
        NEWA: ClassVar[Any]
        NEWA_ID: ClassVar[int]
        NEW_TAI_LUE: ClassVar[Any]
        NEW_TAI_LUE_ID: ClassVar[int]
        NKO: ClassVar[Any]
        NKO_ID: ClassVar[int]
        NO_BLOCK: ClassVar[Any]
        NUMBER_FORMS: ClassVar[Any]
        NUMBER_FORMS_ID: ClassVar[int]
        NUSHU: ClassVar[Any]
        NUSHU_ID: ClassVar[int]
        NYIAKENG_PUACHUE_HMONG: ClassVar[Any]
        NYIAKENG_PUACHUE_HMONG_ID: ClassVar[int]
        OGHAM: ClassVar[Any]
        OGHAM_ID: ClassVar[int]
        OLD_HUNGARIAN: ClassVar[Any]
        OLD_HUNGARIAN_ID: ClassVar[int]
        OLD_ITALIC: ClassVar[Any]
        OLD_ITALIC_ID: ClassVar[int]
        OLD_NORTH_ARABIAN: ClassVar[Any]
        OLD_NORTH_ARABIAN_ID: ClassVar[int]
        OLD_PERMIC: ClassVar[Any]
        OLD_PERMIC_ID: ClassVar[int]
        OLD_PERSIAN: ClassVar[Any]
        OLD_PERSIAN_ID: ClassVar[int]
        OLD_SOGDIAN: ClassVar[Any]
        OLD_SOGDIAN_ID: ClassVar[int]
        OLD_SOUTH_ARABIAN: ClassVar[Any]
        OLD_SOUTH_ARABIAN_ID: ClassVar[int]
        OLD_TURKIC: ClassVar[Any]
        OLD_TURKIC_ID: ClassVar[int]
        OLD_UYGHUR: ClassVar[Any]
        OLD_UYGHUR_ID: ClassVar[int]
        OL_CHIKI: ClassVar[Any]
        OL_CHIKI_ID: ClassVar[int]
        OL_ONAL: ClassVar[Any]
        OL_ONAL_ID: ClassVar[int]
        OPTICAL_CHARACTER_RECOGNITION: ClassVar[Any]
        OPTICAL_CHARACTER_RECOGNITION_ID: ClassVar[int]
        ORIYA: ClassVar[Any]
        ORIYA_ID: ClassVar[int]
        ORNAMENTAL_DINGBATS: ClassVar[Any]
        ORNAMENTAL_DINGBATS_ID: ClassVar[int]
        OSAGE: ClassVar[Any]
        OSAGE_ID: ClassVar[int]
        OSMANYA: ClassVar[Any]
        OSMANYA_ID: ClassVar[int]
        OTTOMAN_SIYAQ_NUMBERS: ClassVar[Any]
        OTTOMAN_SIYAQ_NUMBERS_ID: ClassVar[int]
        PAHAWH_HMONG: ClassVar[Any]
        PAHAWH_HMONG_ID: ClassVar[int]
        PALMYRENE: ClassVar[Any]
        PALMYRENE_ID: ClassVar[int]
        PAU_CIN_HAU: ClassVar[Any]
        PAU_CIN_HAU_ID: ClassVar[int]
        PHAGS_PA: ClassVar[Any]
        PHAGS_PA_ID: ClassVar[int]
        PHAISTOS_DISC: ClassVar[Any]
        PHAISTOS_DISC_ID: ClassVar[int]
        PHOENICIAN: ClassVar[Any]
        PHOENICIAN_ID: ClassVar[int]
        PHONETIC_EXTENSIONS: ClassVar[Any]
        PHONETIC_EXTENSIONS_ID: ClassVar[int]
        PHONETIC_EXTENSIONS_SUPPLEMENT: ClassVar[Any]
        PHONETIC_EXTENSIONS_SUPPLEMENT_ID: ClassVar[int]
        PLAYING_CARDS: ClassVar[Any]
        PLAYING_CARDS_ID: ClassVar[int]
        PRIVATE_USE: ClassVar[Any]
        PRIVATE_USE_AREA: ClassVar[Any]
        PRIVATE_USE_AREA_ID: ClassVar[int]
        PRIVATE_USE_ID: ClassVar[int]
        PSALTER_PAHLAVI: ClassVar[Any]
        PSALTER_PAHLAVI_ID: ClassVar[int]
        REJANG: ClassVar[Any]
        REJANG_ID: ClassVar[int]
        RUMI_NUMERAL_SYMBOLS: ClassVar[Any]
        RUMI_NUMERAL_SYMBOLS_ID: ClassVar[int]
        RUNIC: ClassVar[Any]
        RUNIC_ID: ClassVar[int]
        SAMARITAN: ClassVar[Any]
        SAMARITAN_ID: ClassVar[int]
        SAURASHTRA: ClassVar[Any]
        SAURASHTRA_ID: ClassVar[int]
        SHARADA: ClassVar[Any]
        SHARADA_ID: ClassVar[int]
        SHAVIAN: ClassVar[Any]
        SHAVIAN_ID: ClassVar[int]
        SHORTHAND_FORMAT_CONTROLS: ClassVar[Any]
        SHORTHAND_FORMAT_CONTROLS_ID: ClassVar[int]
        SIDDHAM: ClassVar[Any]
        SIDDHAM_ID: ClassVar[int]
        SINHALA: ClassVar[Any]
        SINHALA_ARCHAIC_NUMBERS: ClassVar[Any]
        SINHALA_ARCHAIC_NUMBERS_ID: ClassVar[int]
        SINHALA_ID: ClassVar[int]
        SMALL_FORM_VARIANTS: ClassVar[Any]
        SMALL_FORM_VARIANTS_ID: ClassVar[int]
        SMALL_KANA_EXTENSION: ClassVar[Any]
        SMALL_KANA_EXTENSION_ID: ClassVar[int]
        SOGDIAN: ClassVar[Any]
        SOGDIAN_ID: ClassVar[int]
        SORA_SOMPENG: ClassVar[Any]
        SORA_SOMPENG_ID: ClassVar[int]
        SOYOMBO: ClassVar[Any]
        SOYOMBO_ID: ClassVar[int]
        SPACING_MODIFIER_LETTERS: ClassVar[Any]
        SPACING_MODIFIER_LETTERS_ID: ClassVar[int]
        SPECIALS: ClassVar[Any]
        SPECIALS_ID: ClassVar[int]
        SUNDANESE: ClassVar[Any]
        SUNDANESE_ID: ClassVar[int]
        SUNDANESE_SUPPLEMENT: ClassVar[Any]
        SUNDANESE_SUPPLEMENT_ID: ClassVar[int]
        SUNUWAR: ClassVar[Any]
        SUNUWAR_ID: ClassVar[int]
        SUPERSCRIPTS_AND_SUBSCRIPTS: ClassVar[Any]
        SUPERSCRIPTS_AND_SUBSCRIPTS_ID: ClassVar[int]
        SUPPLEMENTAL_ARROWS_A: ClassVar[Any]
        SUPPLEMENTAL_ARROWS_A_ID: ClassVar[int]
        SUPPLEMENTAL_ARROWS_B: ClassVar[Any]
        SUPPLEMENTAL_ARROWS_B_ID: ClassVar[int]
        SUPPLEMENTAL_ARROWS_C: ClassVar[Any]
        SUPPLEMENTAL_ARROWS_C_ID: ClassVar[int]
        SUPPLEMENTAL_MATHEMATICAL_OPERATORS: ClassVar[Any]
        SUPPLEMENTAL_MATHEMATICAL_OPERATORS_ID: ClassVar[int]
        SUPPLEMENTAL_PUNCTUATION: ClassVar[Any]
        SUPPLEMENTAL_PUNCTUATION_ID: ClassVar[int]
        SUPPLEMENTAL_SYMBOLS_AND_PICTOGRAPHS: ClassVar[Any]
        SUPPLEMENTAL_SYMBOLS_AND_PICTOGRAPHS_ID: ClassVar[int]
        SUPPLEMENTARY_PRIVATE_USE_AREA_A: ClassVar[Any]
        SUPPLEMENTARY_PRIVATE_USE_AREA_A_ID: ClassVar[int]
        SUPPLEMENTARY_PRIVATE_USE_AREA_B: ClassVar[Any]
        SUPPLEMENTARY_PRIVATE_USE_AREA_B_ID: ClassVar[int]
        SUTTON_SIGNWRITING: ClassVar[Any]
        SUTTON_SIGNWRITING_ID: ClassVar[int]
        SYLOTI_NAGRI: ClassVar[Any]
        SYLOTI_NAGRI_ID: ClassVar[int]
        SYMBOLS_AND_PICTOGRAPHS_EXTENDED_A: ClassVar[Any]
        SYMBOLS_AND_PICTOGRAPHS_EXTENDED_A_ID: ClassVar[int]
        SYMBOLS_FOR_LEGACY_COMPUTING: ClassVar[Any]
        SYMBOLS_FOR_LEGACY_COMPUTING_ID: ClassVar[int]
        SYMBOLS_FOR_LEGACY_COMPUTING_SUPPLEMENT: ClassVar[Any]
        SYMBOLS_FOR_LEGACY_COMPUTING_SUPPLEMENT_ID: ClassVar[int]
        SYRIAC: ClassVar[Any]
        SYRIAC_ID: ClassVar[int]
        SYRIAC_SUPPLEMENT: ClassVar[Any]
        SYRIAC_SUPPLEMENT_ID: ClassVar[int]
        TAGALOG: ClassVar[Any]
        TAGALOG_ID: ClassVar[int]
        TAGBANWA: ClassVar[Any]
        TAGBANWA_ID: ClassVar[int]
        TAGS: ClassVar[Any]
        TAGS_ID: ClassVar[int]
        TAI_LE: ClassVar[Any]
        TAI_LE_ID: ClassVar[int]
        TAI_THAM: ClassVar[Any]
        TAI_THAM_ID: ClassVar[int]
        TAI_VIET: ClassVar[Any]
        TAI_VIET_ID: ClassVar[int]
        TAI_XUAN_JING_SYMBOLS: ClassVar[Any]
        TAI_XUAN_JING_SYMBOLS_ID: ClassVar[int]
        TAKRI: ClassVar[Any]
        TAKRI_ID: ClassVar[int]
        TAMIL: ClassVar[Any]
        TAMIL_ID: ClassVar[int]
        TAMIL_SUPPLEMENT: ClassVar[Any]
        TAMIL_SUPPLEMENT_ID: ClassVar[int]
        TANGSA: ClassVar[Any]
        TANGSA_ID: ClassVar[int]
        TANGUT: ClassVar[Any]
        TANGUT_COMPONENTS: ClassVar[Any]
        TANGUT_COMPONENTS_ID: ClassVar[int]
        TANGUT_ID: ClassVar[int]
        TANGUT_SUPPLEMENT: ClassVar[Any]
        TANGUT_SUPPLEMENT_ID: ClassVar[int]
        TELUGU: ClassVar[Any]
        TELUGU_ID: ClassVar[int]
        THAANA: ClassVar[Any]
        THAANA_ID: ClassVar[int]
        THAI: ClassVar[Any]
        THAI_ID: ClassVar[int]
        TIBETAN: ClassVar[Any]
        TIBETAN_ID: ClassVar[int]
        TIFINAGH: ClassVar[Any]
        TIFINAGH_ID: ClassVar[int]
        TIRHUTA: ClassVar[Any]
        TIRHUTA_ID: ClassVar[int]
        TODHRI: ClassVar[Any]
        TODHRI_ID: ClassVar[int]
        TOTO: ClassVar[Any]
        TOTO_ID: ClassVar[int]
        TRANSPORT_AND_MAP_SYMBOLS: ClassVar[Any]
        TRANSPORT_AND_MAP_SYMBOLS_ID: ClassVar[int]
        TULU_TIGALARI: ClassVar[Any]
        TULU_TIGALARI_ID: ClassVar[int]
        UGARITIC: ClassVar[Any]
        UGARITIC_ID: ClassVar[int]
        UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS: ClassVar[Any]
        UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_EXTENDED: ClassVar[Any]
        UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_EXTENDED_A: ClassVar[Any]
        UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_EXTENDED_A_ID: ClassVar[int]
        UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_EXTENDED_ID: ClassVar[int]
        UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_ID: ClassVar[int]
        VAI: ClassVar[Any]
        VAI_ID: ClassVar[int]
        VARIATION_SELECTORS: ClassVar[Any]
        VARIATION_SELECTORS_ID: ClassVar[int]
        VARIATION_SELECTORS_SUPPLEMENT: ClassVar[Any]
        VARIATION_SELECTORS_SUPPLEMENT_ID: ClassVar[int]
        VEDIC_EXTENSIONS: ClassVar[Any]
        VEDIC_EXTENSIONS_ID: ClassVar[int]
        VERTICAL_FORMS: ClassVar[Any]
        VERTICAL_FORMS_ID: ClassVar[int]
        VITHKUQI: ClassVar[Any]
        VITHKUQI_ID: ClassVar[int]
        WANCHO: ClassVar[Any]
        WANCHO_ID: ClassVar[int]
        WARANG_CITI: ClassVar[Any]
        WARANG_CITI_ID: ClassVar[int]
        YEZIDI: ClassVar[Any]
        YEZIDI_ID: ClassVar[int]
        YIJING_HEXAGRAM_SYMBOLS: ClassVar[Any]
        YIJING_HEXAGRAM_SYMBOLS_ID: ClassVar[int]
        YI_RADICALS: ClassVar[Any]
        YI_RADICALS_ID: ClassVar[int]
        YI_SYLLABLES: ClassVar[Any]
        YI_SYLLABLES_ID: ClassVar[int]
        ZANABAZAR_SQUARE: ClassVar[Any]
        ZANABAZAR_SQUARE_ID: ClassVar[int]
        ZNAMENNY_MUSICAL_NOTATION: ClassVar[Any]
        ZNAMENNY_MUSICAL_NOTATION_ID: ClassVar[int]
        @staticmethod
        def forName(p0: str) -> Any: ...
        @staticmethod
        def of(p0: int) -> Any: ...
        @staticmethod
        def getInstance(p0: int) -> Any: ...
        def getID(self) -> int: ...

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

    class NumericType:
        DECIMAL: ClassVar[int]
        DIGIT: ClassVar[int]
        NONE: ClassVar[int]
        NUMERIC: ClassVar[int]

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

    class JoiningType:
        DUAL_JOINING: ClassVar[int]
        JOIN_CAUSING: ClassVar[int]
        LEFT_JOINING: ClassVar[int]
        NON_JOINING: ClassVar[int]
        RIGHT_JOINING: ClassVar[int]
        TRANSPARENT: ClassVar[int]

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
        KASHMIRI_YEH: ClassVar[int]
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
        REORDERING_KILLER: ClassVar[int]
        SYLLABLE_MODIFIER: ClassVar[int]
        TONE_LETTER: ClassVar[int]
        TONE_MARK: ClassVar[int]
        VIRAMA: ClassVar[int]
        VISARGA: ClassVar[int]
        VOWEL: ClassVar[int]
        VOWEL_DEPENDENT: ClassVar[int]
        VOWEL_INDEPENDENT: ClassVar[int]

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

    class HangulSyllableType:
        LEADING_JAMO: ClassVar[int]
        LVT_SYLLABLE: ClassVar[int]
        LV_SYLLABLE: ClassVar[int]
        NOT_APPLICABLE: ClassVar[int]
        TRAILING_JAMO: ClassVar[int]
        VOWEL_JAMO: ClassVar[int]

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

    class EastAsianWidth:
        AMBIGUOUS: ClassVar[int]
        FULLWIDTH: ClassVar[int]
        HALFWIDTH: ClassVar[int]
        NARROW: ClassVar[int]
        NEUTRAL: ClassVar[int]
        WIDE: ClassVar[int]

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

    class BidiPairedBracketType:
        CLOSE: ClassVar[int]
        NONE: ClassVar[int]
        OPEN: ClassVar[int]
