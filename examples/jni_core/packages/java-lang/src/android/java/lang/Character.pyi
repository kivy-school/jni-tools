from typing import Any, ClassVar, overload
from java.util.Optional import Optional

class Character:
    MIN_RADIX: ClassVar[int]
    MAX_RADIX: ClassVar[int]
    MIN_VALUE: ClassVar[str]
    MAX_VALUE: ClassVar[str]
    TYPE: ClassVar[type]
    UNASSIGNED: ClassVar[int]
    UPPERCASE_LETTER: ClassVar[int]
    LOWERCASE_LETTER: ClassVar[int]
    TITLECASE_LETTER: ClassVar[int]
    MODIFIER_LETTER: ClassVar[int]
    OTHER_LETTER: ClassVar[int]
    NON_SPACING_MARK: ClassVar[int]
    ENCLOSING_MARK: ClassVar[int]
    COMBINING_SPACING_MARK: ClassVar[int]
    DECIMAL_DIGIT_NUMBER: ClassVar[int]
    LETTER_NUMBER: ClassVar[int]
    OTHER_NUMBER: ClassVar[int]
    SPACE_SEPARATOR: ClassVar[int]
    LINE_SEPARATOR: ClassVar[int]
    PARAGRAPH_SEPARATOR: ClassVar[int]
    CONTROL: ClassVar[int]
    FORMAT: ClassVar[int]
    PRIVATE_USE: ClassVar[int]
    SURROGATE: ClassVar[int]
    DASH_PUNCTUATION: ClassVar[int]
    START_PUNCTUATION: ClassVar[int]
    END_PUNCTUATION: ClassVar[int]
    CONNECTOR_PUNCTUATION: ClassVar[int]
    OTHER_PUNCTUATION: ClassVar[int]
    MATH_SYMBOL: ClassVar[int]
    CURRENCY_SYMBOL: ClassVar[int]
    MODIFIER_SYMBOL: ClassVar[int]
    OTHER_SYMBOL: ClassVar[int]
    INITIAL_QUOTE_PUNCTUATION: ClassVar[int]
    FINAL_QUOTE_PUNCTUATION: ClassVar[int]
    DIRECTIONALITY_UNDEFINED: ClassVar[int]
    DIRECTIONALITY_LEFT_TO_RIGHT: ClassVar[int]
    DIRECTIONALITY_RIGHT_TO_LEFT: ClassVar[int]
    DIRECTIONALITY_RIGHT_TO_LEFT_ARABIC: ClassVar[int]
    DIRECTIONALITY_EUROPEAN_NUMBER: ClassVar[int]
    DIRECTIONALITY_EUROPEAN_NUMBER_SEPARATOR: ClassVar[int]
    DIRECTIONALITY_EUROPEAN_NUMBER_TERMINATOR: ClassVar[int]
    DIRECTIONALITY_ARABIC_NUMBER: ClassVar[int]
    DIRECTIONALITY_COMMON_NUMBER_SEPARATOR: ClassVar[int]
    DIRECTIONALITY_NONSPACING_MARK: ClassVar[int]
    DIRECTIONALITY_BOUNDARY_NEUTRAL: ClassVar[int]
    DIRECTIONALITY_PARAGRAPH_SEPARATOR: ClassVar[int]
    DIRECTIONALITY_SEGMENT_SEPARATOR: ClassVar[int]
    DIRECTIONALITY_WHITESPACE: ClassVar[int]
    DIRECTIONALITY_OTHER_NEUTRALS: ClassVar[int]
    DIRECTIONALITY_LEFT_TO_RIGHT_EMBEDDING: ClassVar[int]
    DIRECTIONALITY_LEFT_TO_RIGHT_OVERRIDE: ClassVar[int]
    DIRECTIONALITY_RIGHT_TO_LEFT_EMBEDDING: ClassVar[int]
    DIRECTIONALITY_RIGHT_TO_LEFT_OVERRIDE: ClassVar[int]
    DIRECTIONALITY_POP_DIRECTIONAL_FORMAT: ClassVar[int]
    DIRECTIONALITY_LEFT_TO_RIGHT_ISOLATE: ClassVar[int]
    DIRECTIONALITY_RIGHT_TO_LEFT_ISOLATE: ClassVar[int]
    DIRECTIONALITY_FIRST_STRONG_ISOLATE: ClassVar[int]
    DIRECTIONALITY_POP_DIRECTIONAL_ISOLATE: ClassVar[int]
    MIN_HIGH_SURROGATE: ClassVar[str]
    MAX_HIGH_SURROGATE: ClassVar[str]
    MIN_LOW_SURROGATE: ClassVar[str]
    MAX_LOW_SURROGATE: ClassVar[str]
    MIN_SURROGATE: ClassVar[str]
    MAX_SURROGATE: ClassVar[str]
    MIN_SUPPLEMENTARY_CODE_POINT: ClassVar[int]
    MIN_CODE_POINT: ClassVar[int]
    MAX_CODE_POINT: ClassVar[int]
    SIZE: ClassVar[int]
    BYTES: ClassVar[int]
    def __init__(self, p0: str) -> None: ...
    @staticmethod
    def getName(p0: int) -> str: ...
    @overload
    @staticmethod
    def isJavaIdentifierStart(p0: str) -> bool: ...
    @overload
    @staticmethod
    def isJavaIdentifierStart(p0: int) -> bool: ...
    @overload
    @staticmethod
    def isJavaIdentifierPart(p0: str) -> bool: ...
    @overload
    @staticmethod
    def isJavaIdentifierPart(p0: int) -> bool: ...
    def equals(self, p0: Any) -> bool: ...
    @overload
    def toString(self) -> str: ...
    @overload
    @staticmethod
    def toString(p0: int) -> str: ...
    @overload
    @staticmethod
    def toString(p0: str) -> str: ...
    @overload
    def hashCode(self) -> int: ...
    @overload
    @staticmethod
    def hashCode(p0: str) -> int: ...
    @staticmethod
    def reverseBytes(p0: str) -> str: ...
    @overload
    def compareTo(self, p0: str) -> int: ...
    @overload
    def compareTo(self, p0: Any) -> int: ...
    @overload
    @staticmethod
    def isDigit(p0: str) -> bool: ...
    @overload
    @staticmethod
    def isDigit(p0: int) -> bool: ...
    @overload
    @staticmethod
    def isLowerCase(p0: str) -> bool: ...
    @overload
    @staticmethod
    def isLowerCase(p0: int) -> bool: ...
    @overload
    @staticmethod
    def isUpperCase(p0: int) -> bool: ...
    @overload
    @staticmethod
    def isUpperCase(p0: str) -> bool: ...
    @overload
    @staticmethod
    def isWhitespace(p0: str) -> bool: ...
    @overload
    @staticmethod
    def isWhitespace(p0: int) -> bool: ...
    @staticmethod
    def compare(p0: str, p1: str) -> int: ...
    def charValue(self) -> str: ...
    @staticmethod
    def valueOf(p0: str) -> str: ...
    @overload
    @staticmethod
    def toChars(p0: int) -> Any: ...
    @overload
    @staticmethod
    def toChars(p0: int, p1: Any, p2: int) -> int: ...
    @staticmethod
    def isHighSurrogate(p0: str) -> bool: ...
    @staticmethod
    def isLowSurrogate(p0: str) -> bool: ...
    @staticmethod
    def isSurrogate(p0: str) -> bool: ...
    @staticmethod
    def isSupplementaryCodePoint(p0: int) -> bool: ...
    @staticmethod
    def highSurrogate(p0: int) -> str: ...
    @staticmethod
    def lowSurrogate(p0: int) -> str: ...
    @staticmethod
    def toCodePoint(p0: str, p1: str) -> int: ...
    @overload
    @staticmethod
    def codePointAt(p0: str, p1: int) -> int: ...
    @overload
    @staticmethod
    def codePointAt(p0: Any, p1: int, p2: int) -> int: ...
    @overload
    @staticmethod
    def codePointAt(p0: Any, p1: int) -> int: ...
    @overload
    @staticmethod
    def codePointBefore(p0: str, p1: int) -> int: ...
    @overload
    @staticmethod
    def codePointBefore(p0: Any, p1: int) -> int: ...
    @overload
    @staticmethod
    def codePointBefore(p0: Any, p1: int, p2: int) -> int: ...
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
    def toLowerCase(p0: str) -> str: ...
    @overload
    @staticmethod
    def toLowerCase(p0: int) -> int: ...
    @overload
    @staticmethod
    def toUpperCase(p0: int) -> int: ...
    @overload
    @staticmethod
    def toUpperCase(p0: str) -> str: ...
    @staticmethod
    def isBmpCodePoint(p0: int) -> bool: ...
    def describeConstable(self) -> Optional: ...
    @overload
    @staticmethod
    def getType(p0: str) -> int: ...
    @overload
    @staticmethod
    def getType(p0: int) -> int: ...
    @overload
    @staticmethod
    def isLetter(p0: str) -> bool: ...
    @overload
    @staticmethod
    def isLetter(p0: int) -> bool: ...
    @overload
    @staticmethod
    def isLetterOrDigit(p0: int) -> bool: ...
    @overload
    @staticmethod
    def isLetterOrDigit(p0: str) -> bool: ...
    @staticmethod
    def isValidCodePoint(p0: int) -> bool: ...
    @overload
    @staticmethod
    def isTitleCase(p0: int) -> bool: ...
    @overload
    @staticmethod
    def isTitleCase(p0: str) -> bool: ...
    @overload
    @staticmethod
    def isDefined(p0: str) -> bool: ...
    @overload
    @staticmethod
    def isDefined(p0: int) -> bool: ...
    @staticmethod
    def isIdeographic(p0: int) -> bool: ...
    @overload
    @staticmethod
    def isUnicodeIdentifierStart(p0: int) -> bool: ...
    @overload
    @staticmethod
    def isUnicodeIdentifierStart(p0: str) -> bool: ...
    @overload
    @staticmethod
    def isUnicodeIdentifierPart(p0: int) -> bool: ...
    @overload
    @staticmethod
    def isUnicodeIdentifierPart(p0: str) -> bool: ...
    @overload
    @staticmethod
    def isIdentifierIgnorable(p0: int) -> bool: ...
    @overload
    @staticmethod
    def isIdentifierIgnorable(p0: str) -> bool: ...
    @staticmethod
    def isEmoji(p0: int) -> bool: ...
    @staticmethod
    def isEmojiPresentation(p0: int) -> bool: ...
    @staticmethod
    def isEmojiModifier(p0: int) -> bool: ...
    @staticmethod
    def isEmojiModifierBase(p0: int) -> bool: ...
    @staticmethod
    def isEmojiComponent(p0: int) -> bool: ...
    @staticmethod
    def isExtendedPictographic(p0: int) -> bool: ...
    @overload
    @staticmethod
    def toTitleCase(p0: str) -> str: ...
    @overload
    @staticmethod
    def toTitleCase(p0: int) -> int: ...
    @overload
    @staticmethod
    def digit(p0: str, p1: int) -> int: ...
    @overload
    @staticmethod
    def digit(p0: int, p1: int) -> int: ...
    @overload
    @staticmethod
    def getNumericValue(p0: int) -> int: ...
    @overload
    @staticmethod
    def getNumericValue(p0: str) -> int: ...
    @overload
    @staticmethod
    def isSpaceChar(p0: str) -> bool: ...
    @overload
    @staticmethod
    def isSpaceChar(p0: int) -> bool: ...
    @overload
    @staticmethod
    def isISOControl(p0: int) -> bool: ...
    @overload
    @staticmethod
    def isISOControl(p0: str) -> bool: ...
    @overload
    @staticmethod
    def getDirectionality(p0: str) -> int: ...
    @overload
    @staticmethod
    def getDirectionality(p0: int) -> int: ...
    @overload
    @staticmethod
    def isMirrored(p0: str) -> bool: ...
    @overload
    @staticmethod
    def isMirrored(p0: int) -> bool: ...
    @staticmethod
    def isSurrogatePair(p0: str, p1: str) -> bool: ...
    @staticmethod
    def charCount(p0: int) -> int: ...
    @staticmethod
    def isJavaLetter(p0: str) -> bool: ...
    @staticmethod
    def isJavaLetterOrDigit(p0: str) -> bool: ...
    @staticmethod
    def isAlphabetic(p0: int) -> bool: ...
    @staticmethod
    def isSpace(p0: str) -> bool: ...
    @staticmethod
    def forDigit(p0: int, p1: int) -> str: ...
    @staticmethod
    def codePointOf(p0: str) -> int: ...

    class UnicodeBlock:
        BASIC_LATIN: ClassVar[Any]
        LATIN_1_SUPPLEMENT: ClassVar[Any]
        LATIN_EXTENDED_A: ClassVar[Any]
        LATIN_EXTENDED_B: ClassVar[Any]
        IPA_EXTENSIONS: ClassVar[Any]
        SPACING_MODIFIER_LETTERS: ClassVar[Any]
        COMBINING_DIACRITICAL_MARKS: ClassVar[Any]
        GREEK: ClassVar[Any]
        CYRILLIC: ClassVar[Any]
        ARMENIAN: ClassVar[Any]
        HEBREW: ClassVar[Any]
        ARABIC: ClassVar[Any]
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
        GEORGIAN: ClassVar[Any]
        HANGUL_JAMO: ClassVar[Any]
        LATIN_EXTENDED_ADDITIONAL: ClassVar[Any]
        GREEK_EXTENDED: ClassVar[Any]
        GENERAL_PUNCTUATION: ClassVar[Any]
        SUPERSCRIPTS_AND_SUBSCRIPTS: ClassVar[Any]
        CURRENCY_SYMBOLS: ClassVar[Any]
        COMBINING_MARKS_FOR_SYMBOLS: ClassVar[Any]
        LETTERLIKE_SYMBOLS: ClassVar[Any]
        NUMBER_FORMS: ClassVar[Any]
        ARROWS: ClassVar[Any]
        MATHEMATICAL_OPERATORS: ClassVar[Any]
        MISCELLANEOUS_TECHNICAL: ClassVar[Any]
        CONTROL_PICTURES: ClassVar[Any]
        OPTICAL_CHARACTER_RECOGNITION: ClassVar[Any]
        ENCLOSED_ALPHANUMERICS: ClassVar[Any]
        BOX_DRAWING: ClassVar[Any]
        BLOCK_ELEMENTS: ClassVar[Any]
        GEOMETRIC_SHAPES: ClassVar[Any]
        MISCELLANEOUS_SYMBOLS: ClassVar[Any]
        DINGBATS: ClassVar[Any]
        CJK_SYMBOLS_AND_PUNCTUATION: ClassVar[Any]
        HIRAGANA: ClassVar[Any]
        KATAKANA: ClassVar[Any]
        BOPOMOFO: ClassVar[Any]
        HANGUL_COMPATIBILITY_JAMO: ClassVar[Any]
        KANBUN: ClassVar[Any]
        ENCLOSED_CJK_LETTERS_AND_MONTHS: ClassVar[Any]
        CJK_COMPATIBILITY: ClassVar[Any]
        CJK_UNIFIED_IDEOGRAPHS: ClassVar[Any]
        HANGUL_SYLLABLES: ClassVar[Any]
        PRIVATE_USE_AREA: ClassVar[Any]
        CJK_COMPATIBILITY_IDEOGRAPHS: ClassVar[Any]
        ALPHABETIC_PRESENTATION_FORMS: ClassVar[Any]
        ARABIC_PRESENTATION_FORMS_A: ClassVar[Any]
        COMBINING_HALF_MARKS: ClassVar[Any]
        CJK_COMPATIBILITY_FORMS: ClassVar[Any]
        SMALL_FORM_VARIANTS: ClassVar[Any]
        ARABIC_PRESENTATION_FORMS_B: ClassVar[Any]
        HALFWIDTH_AND_FULLWIDTH_FORMS: ClassVar[Any]
        SPECIALS: ClassVar[Any]
        SURROGATES_AREA: ClassVar[Any]
        SYRIAC: ClassVar[Any]
        THAANA: ClassVar[Any]
        SINHALA: ClassVar[Any]
        MYANMAR: ClassVar[Any]
        ETHIOPIC: ClassVar[Any]
        CHEROKEE: ClassVar[Any]
        UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS: ClassVar[Any]
        OGHAM: ClassVar[Any]
        RUNIC: ClassVar[Any]
        KHMER: ClassVar[Any]
        MONGOLIAN: ClassVar[Any]
        BRAILLE_PATTERNS: ClassVar[Any]
        CJK_RADICALS_SUPPLEMENT: ClassVar[Any]
        KANGXI_RADICALS: ClassVar[Any]
        IDEOGRAPHIC_DESCRIPTION_CHARACTERS: ClassVar[Any]
        BOPOMOFO_EXTENDED: ClassVar[Any]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_A: ClassVar[Any]
        YI_SYLLABLES: ClassVar[Any]
        YI_RADICALS: ClassVar[Any]
        CYRILLIC_SUPPLEMENTARY: ClassVar[Any]
        TAGALOG: ClassVar[Any]
        HANUNOO: ClassVar[Any]
        BUHID: ClassVar[Any]
        TAGBANWA: ClassVar[Any]
        LIMBU: ClassVar[Any]
        TAI_LE: ClassVar[Any]
        KHMER_SYMBOLS: ClassVar[Any]
        PHONETIC_EXTENSIONS: ClassVar[Any]
        MISCELLANEOUS_MATHEMATICAL_SYMBOLS_A: ClassVar[Any]
        SUPPLEMENTAL_ARROWS_A: ClassVar[Any]
        SUPPLEMENTAL_ARROWS_B: ClassVar[Any]
        MISCELLANEOUS_MATHEMATICAL_SYMBOLS_B: ClassVar[Any]
        SUPPLEMENTAL_MATHEMATICAL_OPERATORS: ClassVar[Any]
        MISCELLANEOUS_SYMBOLS_AND_ARROWS: ClassVar[Any]
        KATAKANA_PHONETIC_EXTENSIONS: ClassVar[Any]
        YIJING_HEXAGRAM_SYMBOLS: ClassVar[Any]
        VARIATION_SELECTORS: ClassVar[Any]
        LINEAR_B_SYLLABARY: ClassVar[Any]
        LINEAR_B_IDEOGRAMS: ClassVar[Any]
        AEGEAN_NUMBERS: ClassVar[Any]
        OLD_ITALIC: ClassVar[Any]
        GOTHIC: ClassVar[Any]
        UGARITIC: ClassVar[Any]
        DESERET: ClassVar[Any]
        SHAVIAN: ClassVar[Any]
        OSMANYA: ClassVar[Any]
        CYPRIOT_SYLLABARY: ClassVar[Any]
        BYZANTINE_MUSICAL_SYMBOLS: ClassVar[Any]
        MUSICAL_SYMBOLS: ClassVar[Any]
        TAI_XUAN_JING_SYMBOLS: ClassVar[Any]
        MATHEMATICAL_ALPHANUMERIC_SYMBOLS: ClassVar[Any]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_B: ClassVar[Any]
        CJK_COMPATIBILITY_IDEOGRAPHS_SUPPLEMENT: ClassVar[Any]
        TAGS: ClassVar[Any]
        VARIATION_SELECTORS_SUPPLEMENT: ClassVar[Any]
        SUPPLEMENTARY_PRIVATE_USE_AREA_A: ClassVar[Any]
        SUPPLEMENTARY_PRIVATE_USE_AREA_B: ClassVar[Any]
        HIGH_SURROGATES: ClassVar[Any]
        HIGH_PRIVATE_USE_SURROGATES: ClassVar[Any]
        LOW_SURROGATES: ClassVar[Any]
        ARABIC_SUPPLEMENT: ClassVar[Any]
        NKO: ClassVar[Any]
        SAMARITAN: ClassVar[Any]
        MANDAIC: ClassVar[Any]
        ETHIOPIC_SUPPLEMENT: ClassVar[Any]
        UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_EXTENDED: ClassVar[Any]
        NEW_TAI_LUE: ClassVar[Any]
        BUGINESE: ClassVar[Any]
        TAI_THAM: ClassVar[Any]
        BALINESE: ClassVar[Any]
        SUNDANESE: ClassVar[Any]
        BATAK: ClassVar[Any]
        LEPCHA: ClassVar[Any]
        OL_CHIKI: ClassVar[Any]
        VEDIC_EXTENSIONS: ClassVar[Any]
        PHONETIC_EXTENSIONS_SUPPLEMENT: ClassVar[Any]
        COMBINING_DIACRITICAL_MARKS_SUPPLEMENT: ClassVar[Any]
        GLAGOLITIC: ClassVar[Any]
        LATIN_EXTENDED_C: ClassVar[Any]
        COPTIC: ClassVar[Any]
        GEORGIAN_SUPPLEMENT: ClassVar[Any]
        TIFINAGH: ClassVar[Any]
        ETHIOPIC_EXTENDED: ClassVar[Any]
        CYRILLIC_EXTENDED_A: ClassVar[Any]
        SUPPLEMENTAL_PUNCTUATION: ClassVar[Any]
        CJK_STROKES: ClassVar[Any]
        LISU: ClassVar[Any]
        VAI: ClassVar[Any]
        CYRILLIC_EXTENDED_B: ClassVar[Any]
        BAMUM: ClassVar[Any]
        MODIFIER_TONE_LETTERS: ClassVar[Any]
        LATIN_EXTENDED_D: ClassVar[Any]
        SYLOTI_NAGRI: ClassVar[Any]
        COMMON_INDIC_NUMBER_FORMS: ClassVar[Any]
        PHAGS_PA: ClassVar[Any]
        SAURASHTRA: ClassVar[Any]
        DEVANAGARI_EXTENDED: ClassVar[Any]
        KAYAH_LI: ClassVar[Any]
        REJANG: ClassVar[Any]
        HANGUL_JAMO_EXTENDED_A: ClassVar[Any]
        JAVANESE: ClassVar[Any]
        CHAM: ClassVar[Any]
        MYANMAR_EXTENDED_A: ClassVar[Any]
        TAI_VIET: ClassVar[Any]
        ETHIOPIC_EXTENDED_A: ClassVar[Any]
        MEETEI_MAYEK: ClassVar[Any]
        HANGUL_JAMO_EXTENDED_B: ClassVar[Any]
        VERTICAL_FORMS: ClassVar[Any]
        ANCIENT_GREEK_NUMBERS: ClassVar[Any]
        ANCIENT_SYMBOLS: ClassVar[Any]
        PHAISTOS_DISC: ClassVar[Any]
        LYCIAN: ClassVar[Any]
        CARIAN: ClassVar[Any]
        OLD_PERSIAN: ClassVar[Any]
        IMPERIAL_ARAMAIC: ClassVar[Any]
        PHOENICIAN: ClassVar[Any]
        LYDIAN: ClassVar[Any]
        KHAROSHTHI: ClassVar[Any]
        OLD_SOUTH_ARABIAN: ClassVar[Any]
        AVESTAN: ClassVar[Any]
        INSCRIPTIONAL_PARTHIAN: ClassVar[Any]
        INSCRIPTIONAL_PAHLAVI: ClassVar[Any]
        OLD_TURKIC: ClassVar[Any]
        RUMI_NUMERAL_SYMBOLS: ClassVar[Any]
        BRAHMI: ClassVar[Any]
        KAITHI: ClassVar[Any]
        CUNEIFORM: ClassVar[Any]
        CUNEIFORM_NUMBERS_AND_PUNCTUATION: ClassVar[Any]
        EGYPTIAN_HIEROGLYPHS: ClassVar[Any]
        BAMUM_SUPPLEMENT: ClassVar[Any]
        KANA_SUPPLEMENT: ClassVar[Any]
        ANCIENT_GREEK_MUSICAL_NOTATION: ClassVar[Any]
        COUNTING_ROD_NUMERALS: ClassVar[Any]
        MAHJONG_TILES: ClassVar[Any]
        DOMINO_TILES: ClassVar[Any]
        PLAYING_CARDS: ClassVar[Any]
        ENCLOSED_ALPHANUMERIC_SUPPLEMENT: ClassVar[Any]
        ENCLOSED_IDEOGRAPHIC_SUPPLEMENT: ClassVar[Any]
        MISCELLANEOUS_SYMBOLS_AND_PICTOGRAPHS: ClassVar[Any]
        EMOTICONS: ClassVar[Any]
        TRANSPORT_AND_MAP_SYMBOLS: ClassVar[Any]
        ALCHEMICAL_SYMBOLS: ClassVar[Any]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_C: ClassVar[Any]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_D: ClassVar[Any]
        ARABIC_EXTENDED_A: ClassVar[Any]
        SUNDANESE_SUPPLEMENT: ClassVar[Any]
        MEETEI_MAYEK_EXTENSIONS: ClassVar[Any]
        MEROITIC_HIEROGLYPHS: ClassVar[Any]
        MEROITIC_CURSIVE: ClassVar[Any]
        SORA_SOMPENG: ClassVar[Any]
        CHAKMA: ClassVar[Any]
        SHARADA: ClassVar[Any]
        TAKRI: ClassVar[Any]
        MIAO: ClassVar[Any]
        ARABIC_MATHEMATICAL_ALPHABETIC_SYMBOLS: ClassVar[Any]
        COMBINING_DIACRITICAL_MARKS_EXTENDED: ClassVar[Any]
        MYANMAR_EXTENDED_B: ClassVar[Any]
        LATIN_EXTENDED_E: ClassVar[Any]
        COPTIC_EPACT_NUMBERS: ClassVar[Any]
        OLD_PERMIC: ClassVar[Any]
        ELBASAN: ClassVar[Any]
        CAUCASIAN_ALBANIAN: ClassVar[Any]
        LINEAR_A: ClassVar[Any]
        PALMYRENE: ClassVar[Any]
        NABATAEAN: ClassVar[Any]
        OLD_NORTH_ARABIAN: ClassVar[Any]
        MANICHAEAN: ClassVar[Any]
        PSALTER_PAHLAVI: ClassVar[Any]
        MAHAJANI: ClassVar[Any]
        SINHALA_ARCHAIC_NUMBERS: ClassVar[Any]
        KHOJKI: ClassVar[Any]
        KHUDAWADI: ClassVar[Any]
        GRANTHA: ClassVar[Any]
        TIRHUTA: ClassVar[Any]
        SIDDHAM: ClassVar[Any]
        MODI: ClassVar[Any]
        WARANG_CITI: ClassVar[Any]
        PAU_CIN_HAU: ClassVar[Any]
        MRO: ClassVar[Any]
        BASSA_VAH: ClassVar[Any]
        PAHAWH_HMONG: ClassVar[Any]
        DUPLOYAN: ClassVar[Any]
        SHORTHAND_FORMAT_CONTROLS: ClassVar[Any]
        MENDE_KIKAKUI: ClassVar[Any]
        ORNAMENTAL_DINGBATS: ClassVar[Any]
        GEOMETRIC_SHAPES_EXTENDED: ClassVar[Any]
        SUPPLEMENTAL_ARROWS_C: ClassVar[Any]
        CHEROKEE_SUPPLEMENT: ClassVar[Any]
        HATRAN: ClassVar[Any]
        OLD_HUNGARIAN: ClassVar[Any]
        MULTANI: ClassVar[Any]
        AHOM: ClassVar[Any]
        EARLY_DYNASTIC_CUNEIFORM: ClassVar[Any]
        ANATOLIAN_HIEROGLYPHS: ClassVar[Any]
        SUTTON_SIGNWRITING: ClassVar[Any]
        SUPPLEMENTAL_SYMBOLS_AND_PICTOGRAPHS: ClassVar[Any]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_E: ClassVar[Any]
        SYRIAC_SUPPLEMENT: ClassVar[Any]
        CYRILLIC_EXTENDED_C: ClassVar[Any]
        OSAGE: ClassVar[Any]
        NEWA: ClassVar[Any]
        MONGOLIAN_SUPPLEMENT: ClassVar[Any]
        MARCHEN: ClassVar[Any]
        IDEOGRAPHIC_SYMBOLS_AND_PUNCTUATION: ClassVar[Any]
        TANGUT: ClassVar[Any]
        TANGUT_COMPONENTS: ClassVar[Any]
        KANA_EXTENDED_A: ClassVar[Any]
        GLAGOLITIC_SUPPLEMENT: ClassVar[Any]
        ADLAM: ClassVar[Any]
        MASARAM_GONDI: ClassVar[Any]
        ZANABAZAR_SQUARE: ClassVar[Any]
        NUSHU: ClassVar[Any]
        SOYOMBO: ClassVar[Any]
        BHAIKSUKI: ClassVar[Any]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_F: ClassVar[Any]
        GEORGIAN_EXTENDED: ClassVar[Any]
        HANIFI_ROHINGYA: ClassVar[Any]
        OLD_SOGDIAN: ClassVar[Any]
        SOGDIAN: ClassVar[Any]
        DOGRA: ClassVar[Any]
        GUNJALA_GONDI: ClassVar[Any]
        MAKASAR: ClassVar[Any]
        MEDEFAIDRIN: ClassVar[Any]
        MAYAN_NUMERALS: ClassVar[Any]
        INDIC_SIYAQ_NUMBERS: ClassVar[Any]
        CHESS_SYMBOLS: ClassVar[Any]
        ELYMAIC: ClassVar[Any]
        NANDINAGARI: ClassVar[Any]
        TAMIL_SUPPLEMENT: ClassVar[Any]
        EGYPTIAN_HIEROGLYPH_FORMAT_CONTROLS: ClassVar[Any]
        SMALL_KANA_EXTENSION: ClassVar[Any]
        NYIAKENG_PUACHUE_HMONG: ClassVar[Any]
        WANCHO: ClassVar[Any]
        OTTOMAN_SIYAQ_NUMBERS: ClassVar[Any]
        SYMBOLS_AND_PICTOGRAPHS_EXTENDED_A: ClassVar[Any]
        YEZIDI: ClassVar[Any]
        CHORASMIAN: ClassVar[Any]
        DIVES_AKURU: ClassVar[Any]
        LISU_SUPPLEMENT: ClassVar[Any]
        KHITAN_SMALL_SCRIPT: ClassVar[Any]
        TANGUT_SUPPLEMENT: ClassVar[Any]
        SYMBOLS_FOR_LEGACY_COMPUTING: ClassVar[Any]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_G: ClassVar[Any]
        ARABIC_EXTENDED_B: ClassVar[Any]
        VITHKUQI: ClassVar[Any]
        LATIN_EXTENDED_F: ClassVar[Any]
        OLD_UYGHUR: ClassVar[Any]
        UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_EXTENDED_A: ClassVar[Any]
        CYPRO_MINOAN: ClassVar[Any]
        TANGSA: ClassVar[Any]
        KANA_EXTENDED_B: ClassVar[Any]
        ZNAMENNY_MUSICAL_NOTATION: ClassVar[Any]
        LATIN_EXTENDED_G: ClassVar[Any]
        TOTO: ClassVar[Any]
        ETHIOPIC_EXTENDED_B: ClassVar[Any]
        ARABIC_EXTENDED_C: ClassVar[Any]
        DEVANAGARI_EXTENDED_A: ClassVar[Any]
        KAWI: ClassVar[Any]
        KAKTOVIK_NUMERALS: ClassVar[Any]
        CYRILLIC_EXTENDED_D: ClassVar[Any]
        NAG_MUNDARI: ClassVar[Any]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_H: ClassVar[Any]
        @staticmethod
        def forName(p0: str) -> Any: ...
        @overload
        @staticmethod
        def of(p0: int) -> Any: ...
        @overload
        @staticmethod
        def of(p0: str) -> Any: ...

    class UnicodeScript:
        COMMON: ClassVar["UnicodeScript"]
        LATIN: ClassVar["UnicodeScript"]
        GREEK: ClassVar["UnicodeScript"]
        CYRILLIC: ClassVar["UnicodeScript"]
        ARMENIAN: ClassVar["UnicodeScript"]
        HEBREW: ClassVar["UnicodeScript"]
        ARABIC: ClassVar["UnicodeScript"]
        SYRIAC: ClassVar["UnicodeScript"]
        THAANA: ClassVar["UnicodeScript"]
        DEVANAGARI: ClassVar["UnicodeScript"]
        BENGALI: ClassVar["UnicodeScript"]
        GURMUKHI: ClassVar["UnicodeScript"]
        GUJARATI: ClassVar["UnicodeScript"]
        ORIYA: ClassVar["UnicodeScript"]
        TAMIL: ClassVar["UnicodeScript"]
        TELUGU: ClassVar["UnicodeScript"]
        KANNADA: ClassVar["UnicodeScript"]
        MALAYALAM: ClassVar["UnicodeScript"]
        SINHALA: ClassVar["UnicodeScript"]
        THAI: ClassVar["UnicodeScript"]
        LAO: ClassVar["UnicodeScript"]
        TIBETAN: ClassVar["UnicodeScript"]
        MYANMAR: ClassVar["UnicodeScript"]
        GEORGIAN: ClassVar["UnicodeScript"]
        HANGUL: ClassVar["UnicodeScript"]
        ETHIOPIC: ClassVar["UnicodeScript"]
        CHEROKEE: ClassVar["UnicodeScript"]
        CANADIAN_ABORIGINAL: ClassVar["UnicodeScript"]
        OGHAM: ClassVar["UnicodeScript"]
        RUNIC: ClassVar["UnicodeScript"]
        KHMER: ClassVar["UnicodeScript"]
        MONGOLIAN: ClassVar["UnicodeScript"]
        HIRAGANA: ClassVar["UnicodeScript"]
        KATAKANA: ClassVar["UnicodeScript"]
        BOPOMOFO: ClassVar["UnicodeScript"]
        HAN: ClassVar["UnicodeScript"]
        YI: ClassVar["UnicodeScript"]
        OLD_ITALIC: ClassVar["UnicodeScript"]
        GOTHIC: ClassVar["UnicodeScript"]
        DESERET: ClassVar["UnicodeScript"]
        INHERITED: ClassVar["UnicodeScript"]
        TAGALOG: ClassVar["UnicodeScript"]
        HANUNOO: ClassVar["UnicodeScript"]
        BUHID: ClassVar["UnicodeScript"]
        TAGBANWA: ClassVar["UnicodeScript"]
        LIMBU: ClassVar["UnicodeScript"]
        TAI_LE: ClassVar["UnicodeScript"]
        LINEAR_B: ClassVar["UnicodeScript"]
        UGARITIC: ClassVar["UnicodeScript"]
        SHAVIAN: ClassVar["UnicodeScript"]
        OSMANYA: ClassVar["UnicodeScript"]
        CYPRIOT: ClassVar["UnicodeScript"]
        BRAILLE: ClassVar["UnicodeScript"]
        BUGINESE: ClassVar["UnicodeScript"]
        COPTIC: ClassVar["UnicodeScript"]
        NEW_TAI_LUE: ClassVar["UnicodeScript"]
        GLAGOLITIC: ClassVar["UnicodeScript"]
        TIFINAGH: ClassVar["UnicodeScript"]
        SYLOTI_NAGRI: ClassVar["UnicodeScript"]
        OLD_PERSIAN: ClassVar["UnicodeScript"]
        KHAROSHTHI: ClassVar["UnicodeScript"]
        BALINESE: ClassVar["UnicodeScript"]
        CUNEIFORM: ClassVar["UnicodeScript"]
        PHOENICIAN: ClassVar["UnicodeScript"]
        PHAGS_PA: ClassVar["UnicodeScript"]
        NKO: ClassVar["UnicodeScript"]
        SUNDANESE: ClassVar["UnicodeScript"]
        BATAK: ClassVar["UnicodeScript"]
        LEPCHA: ClassVar["UnicodeScript"]
        OL_CHIKI: ClassVar["UnicodeScript"]
        VAI: ClassVar["UnicodeScript"]
        SAURASHTRA: ClassVar["UnicodeScript"]
        KAYAH_LI: ClassVar["UnicodeScript"]
        REJANG: ClassVar["UnicodeScript"]
        LYCIAN: ClassVar["UnicodeScript"]
        CARIAN: ClassVar["UnicodeScript"]
        LYDIAN: ClassVar["UnicodeScript"]
        CHAM: ClassVar["UnicodeScript"]
        TAI_THAM: ClassVar["UnicodeScript"]
        TAI_VIET: ClassVar["UnicodeScript"]
        AVESTAN: ClassVar["UnicodeScript"]
        EGYPTIAN_HIEROGLYPHS: ClassVar["UnicodeScript"]
        SAMARITAN: ClassVar["UnicodeScript"]
        MANDAIC: ClassVar["UnicodeScript"]
        LISU: ClassVar["UnicodeScript"]
        BAMUM: ClassVar["UnicodeScript"]
        JAVANESE: ClassVar["UnicodeScript"]
        MEETEI_MAYEK: ClassVar["UnicodeScript"]
        IMPERIAL_ARAMAIC: ClassVar["UnicodeScript"]
        OLD_SOUTH_ARABIAN: ClassVar["UnicodeScript"]
        INSCRIPTIONAL_PARTHIAN: ClassVar["UnicodeScript"]
        INSCRIPTIONAL_PAHLAVI: ClassVar["UnicodeScript"]
        OLD_TURKIC: ClassVar["UnicodeScript"]
        BRAHMI: ClassVar["UnicodeScript"]
        KAITHI: ClassVar["UnicodeScript"]
        MEROITIC_HIEROGLYPHS: ClassVar["UnicodeScript"]
        MEROITIC_CURSIVE: ClassVar["UnicodeScript"]
        SORA_SOMPENG: ClassVar["UnicodeScript"]
        CHAKMA: ClassVar["UnicodeScript"]
        SHARADA: ClassVar["UnicodeScript"]
        TAKRI: ClassVar["UnicodeScript"]
        MIAO: ClassVar["UnicodeScript"]
        CAUCASIAN_ALBANIAN: ClassVar["UnicodeScript"]
        BASSA_VAH: ClassVar["UnicodeScript"]
        DUPLOYAN: ClassVar["UnicodeScript"]
        ELBASAN: ClassVar["UnicodeScript"]
        GRANTHA: ClassVar["UnicodeScript"]
        PAHAWH_HMONG: ClassVar["UnicodeScript"]
        KHOJKI: ClassVar["UnicodeScript"]
        LINEAR_A: ClassVar["UnicodeScript"]
        MAHAJANI: ClassVar["UnicodeScript"]
        MANICHAEAN: ClassVar["UnicodeScript"]
        MENDE_KIKAKUI: ClassVar["UnicodeScript"]
        MODI: ClassVar["UnicodeScript"]
        MRO: ClassVar["UnicodeScript"]
        OLD_NORTH_ARABIAN: ClassVar["UnicodeScript"]
        NABATAEAN: ClassVar["UnicodeScript"]
        PALMYRENE: ClassVar["UnicodeScript"]
        PAU_CIN_HAU: ClassVar["UnicodeScript"]
        OLD_PERMIC: ClassVar["UnicodeScript"]
        PSALTER_PAHLAVI: ClassVar["UnicodeScript"]
        SIDDHAM: ClassVar["UnicodeScript"]
        KHUDAWADI: ClassVar["UnicodeScript"]
        TIRHUTA: ClassVar["UnicodeScript"]
        WARANG_CITI: ClassVar["UnicodeScript"]
        AHOM: ClassVar["UnicodeScript"]
        ANATOLIAN_HIEROGLYPHS: ClassVar["UnicodeScript"]
        HATRAN: ClassVar["UnicodeScript"]
        MULTANI: ClassVar["UnicodeScript"]
        OLD_HUNGARIAN: ClassVar["UnicodeScript"]
        SIGNWRITING: ClassVar["UnicodeScript"]
        ADLAM: ClassVar["UnicodeScript"]
        BHAIKSUKI: ClassVar["UnicodeScript"]
        MARCHEN: ClassVar["UnicodeScript"]
        NEWA: ClassVar["UnicodeScript"]
        OSAGE: ClassVar["UnicodeScript"]
        TANGUT: ClassVar["UnicodeScript"]
        MASARAM_GONDI: ClassVar["UnicodeScript"]
        NUSHU: ClassVar["UnicodeScript"]
        SOYOMBO: ClassVar["UnicodeScript"]
        ZANABAZAR_SQUARE: ClassVar["UnicodeScript"]
        HANIFI_ROHINGYA: ClassVar["UnicodeScript"]
        OLD_SOGDIAN: ClassVar["UnicodeScript"]
        SOGDIAN: ClassVar["UnicodeScript"]
        DOGRA: ClassVar["UnicodeScript"]
        GUNJALA_GONDI: ClassVar["UnicodeScript"]
        MAKASAR: ClassVar["UnicodeScript"]
        MEDEFAIDRIN: ClassVar["UnicodeScript"]
        ELYMAIC: ClassVar["UnicodeScript"]
        NANDINAGARI: ClassVar["UnicodeScript"]
        NYIAKENG_PUACHUE_HMONG: ClassVar["UnicodeScript"]
        WANCHO: ClassVar["UnicodeScript"]
        YEZIDI: ClassVar["UnicodeScript"]
        CHORASMIAN: ClassVar["UnicodeScript"]
        DIVES_AKURU: ClassVar["UnicodeScript"]
        KHITAN_SMALL_SCRIPT: ClassVar["UnicodeScript"]
        VITHKUQI: ClassVar["UnicodeScript"]
        OLD_UYGHUR: ClassVar["UnicodeScript"]
        CYPRO_MINOAN: ClassVar["UnicodeScript"]
        TANGSA: ClassVar["UnicodeScript"]
        TOTO: ClassVar["UnicodeScript"]
        KAWI: ClassVar["UnicodeScript"]
        NAG_MUNDARI: ClassVar["UnicodeScript"]
        UNKNOWN: ClassVar["UnicodeScript"]
        COMMON: ClassVar[Any]
        LATIN: ClassVar[Any]
        GREEK: ClassVar[Any]
        CYRILLIC: ClassVar[Any]
        ARMENIAN: ClassVar[Any]
        HEBREW: ClassVar[Any]
        ARABIC: ClassVar[Any]
        SYRIAC: ClassVar[Any]
        THAANA: ClassVar[Any]
        DEVANAGARI: ClassVar[Any]
        BENGALI: ClassVar[Any]
        GURMUKHI: ClassVar[Any]
        GUJARATI: ClassVar[Any]
        ORIYA: ClassVar[Any]
        TAMIL: ClassVar[Any]
        TELUGU: ClassVar[Any]
        KANNADA: ClassVar[Any]
        MALAYALAM: ClassVar[Any]
        SINHALA: ClassVar[Any]
        THAI: ClassVar[Any]
        LAO: ClassVar[Any]
        TIBETAN: ClassVar[Any]
        MYANMAR: ClassVar[Any]
        GEORGIAN: ClassVar[Any]
        HANGUL: ClassVar[Any]
        ETHIOPIC: ClassVar[Any]
        CHEROKEE: ClassVar[Any]
        CANADIAN_ABORIGINAL: ClassVar[Any]
        OGHAM: ClassVar[Any]
        RUNIC: ClassVar[Any]
        KHMER: ClassVar[Any]
        MONGOLIAN: ClassVar[Any]
        HIRAGANA: ClassVar[Any]
        KATAKANA: ClassVar[Any]
        BOPOMOFO: ClassVar[Any]
        HAN: ClassVar[Any]
        YI: ClassVar[Any]
        OLD_ITALIC: ClassVar[Any]
        GOTHIC: ClassVar[Any]
        DESERET: ClassVar[Any]
        INHERITED: ClassVar[Any]
        TAGALOG: ClassVar[Any]
        HANUNOO: ClassVar[Any]
        BUHID: ClassVar[Any]
        TAGBANWA: ClassVar[Any]
        LIMBU: ClassVar[Any]
        TAI_LE: ClassVar[Any]
        LINEAR_B: ClassVar[Any]
        UGARITIC: ClassVar[Any]
        SHAVIAN: ClassVar[Any]
        OSMANYA: ClassVar[Any]
        CYPRIOT: ClassVar[Any]
        BRAILLE: ClassVar[Any]
        BUGINESE: ClassVar[Any]
        COPTIC: ClassVar[Any]
        NEW_TAI_LUE: ClassVar[Any]
        GLAGOLITIC: ClassVar[Any]
        TIFINAGH: ClassVar[Any]
        SYLOTI_NAGRI: ClassVar[Any]
        OLD_PERSIAN: ClassVar[Any]
        KHAROSHTHI: ClassVar[Any]
        BALINESE: ClassVar[Any]
        CUNEIFORM: ClassVar[Any]
        PHOENICIAN: ClassVar[Any]
        PHAGS_PA: ClassVar[Any]
        NKO: ClassVar[Any]
        SUNDANESE: ClassVar[Any]
        BATAK: ClassVar[Any]
        LEPCHA: ClassVar[Any]
        OL_CHIKI: ClassVar[Any]
        VAI: ClassVar[Any]
        SAURASHTRA: ClassVar[Any]
        KAYAH_LI: ClassVar[Any]
        REJANG: ClassVar[Any]
        LYCIAN: ClassVar[Any]
        CARIAN: ClassVar[Any]
        LYDIAN: ClassVar[Any]
        CHAM: ClassVar[Any]
        TAI_THAM: ClassVar[Any]
        TAI_VIET: ClassVar[Any]
        AVESTAN: ClassVar[Any]
        EGYPTIAN_HIEROGLYPHS: ClassVar[Any]
        SAMARITAN: ClassVar[Any]
        MANDAIC: ClassVar[Any]
        LISU: ClassVar[Any]
        BAMUM: ClassVar[Any]
        JAVANESE: ClassVar[Any]
        MEETEI_MAYEK: ClassVar[Any]
        IMPERIAL_ARAMAIC: ClassVar[Any]
        OLD_SOUTH_ARABIAN: ClassVar[Any]
        INSCRIPTIONAL_PARTHIAN: ClassVar[Any]
        INSCRIPTIONAL_PAHLAVI: ClassVar[Any]
        OLD_TURKIC: ClassVar[Any]
        BRAHMI: ClassVar[Any]
        KAITHI: ClassVar[Any]
        MEROITIC_HIEROGLYPHS: ClassVar[Any]
        MEROITIC_CURSIVE: ClassVar[Any]
        SORA_SOMPENG: ClassVar[Any]
        CHAKMA: ClassVar[Any]
        SHARADA: ClassVar[Any]
        TAKRI: ClassVar[Any]
        MIAO: ClassVar[Any]
        CAUCASIAN_ALBANIAN: ClassVar[Any]
        BASSA_VAH: ClassVar[Any]
        DUPLOYAN: ClassVar[Any]
        ELBASAN: ClassVar[Any]
        GRANTHA: ClassVar[Any]
        PAHAWH_HMONG: ClassVar[Any]
        KHOJKI: ClassVar[Any]
        LINEAR_A: ClassVar[Any]
        MAHAJANI: ClassVar[Any]
        MANICHAEAN: ClassVar[Any]
        MENDE_KIKAKUI: ClassVar[Any]
        MODI: ClassVar[Any]
        MRO: ClassVar[Any]
        OLD_NORTH_ARABIAN: ClassVar[Any]
        NABATAEAN: ClassVar[Any]
        PALMYRENE: ClassVar[Any]
        PAU_CIN_HAU: ClassVar[Any]
        OLD_PERMIC: ClassVar[Any]
        PSALTER_PAHLAVI: ClassVar[Any]
        SIDDHAM: ClassVar[Any]
        KHUDAWADI: ClassVar[Any]
        TIRHUTA: ClassVar[Any]
        WARANG_CITI: ClassVar[Any]
        AHOM: ClassVar[Any]
        ANATOLIAN_HIEROGLYPHS: ClassVar[Any]
        HATRAN: ClassVar[Any]
        MULTANI: ClassVar[Any]
        OLD_HUNGARIAN: ClassVar[Any]
        SIGNWRITING: ClassVar[Any]
        ADLAM: ClassVar[Any]
        BHAIKSUKI: ClassVar[Any]
        MARCHEN: ClassVar[Any]
        NEWA: ClassVar[Any]
        OSAGE: ClassVar[Any]
        TANGUT: ClassVar[Any]
        MASARAM_GONDI: ClassVar[Any]
        NUSHU: ClassVar[Any]
        SOYOMBO: ClassVar[Any]
        ZANABAZAR_SQUARE: ClassVar[Any]
        HANIFI_ROHINGYA: ClassVar[Any]
        OLD_SOGDIAN: ClassVar[Any]
        SOGDIAN: ClassVar[Any]
        DOGRA: ClassVar[Any]
        GUNJALA_GONDI: ClassVar[Any]
        MAKASAR: ClassVar[Any]
        MEDEFAIDRIN: ClassVar[Any]
        ELYMAIC: ClassVar[Any]
        NANDINAGARI: ClassVar[Any]
        NYIAKENG_PUACHUE_HMONG: ClassVar[Any]
        WANCHO: ClassVar[Any]
        YEZIDI: ClassVar[Any]
        CHORASMIAN: ClassVar[Any]
        DIVES_AKURU: ClassVar[Any]
        KHITAN_SMALL_SCRIPT: ClassVar[Any]
        VITHKUQI: ClassVar[Any]
        OLD_UYGHUR: ClassVar[Any]
        CYPRO_MINOAN: ClassVar[Any]
        TANGSA: ClassVar[Any]
        TOTO: ClassVar[Any]
        KAWI: ClassVar[Any]
        NAG_MUNDARI: ClassVar[Any]
        UNKNOWN: ClassVar[Any]
        @staticmethod
        def forName(p0: str) -> Any: ...
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
        @staticmethod
        def of(p0: int) -> Any: ...

    class Subset:
        def equals(self, p0: Any) -> bool: ...
        def toString(self) -> str: ...
        def hashCode(self) -> int: ...
