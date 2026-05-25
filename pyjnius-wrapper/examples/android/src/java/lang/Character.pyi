from typing import Any, ClassVar, overload

class Character:
    BYTES: ClassVar[int]
    COMBINING_SPACING_MARK: ClassVar[int]
    CONNECTOR_PUNCTUATION: ClassVar[int]
    CONTROL: ClassVar[int]
    CURRENCY_SYMBOL: ClassVar[int]
    DASH_PUNCTUATION: ClassVar[int]
    DECIMAL_DIGIT_NUMBER: ClassVar[int]
    DIRECTIONALITY_ARABIC_NUMBER: ClassVar[int]
    DIRECTIONALITY_BOUNDARY_NEUTRAL: ClassVar[int]
    DIRECTIONALITY_COMMON_NUMBER_SEPARATOR: ClassVar[int]
    DIRECTIONALITY_EUROPEAN_NUMBER: ClassVar[int]
    DIRECTIONALITY_EUROPEAN_NUMBER_SEPARATOR: ClassVar[int]
    DIRECTIONALITY_EUROPEAN_NUMBER_TERMINATOR: ClassVar[int]
    DIRECTIONALITY_FIRST_STRONG_ISOLATE: ClassVar[int]
    DIRECTIONALITY_LEFT_TO_RIGHT: ClassVar[int]
    DIRECTIONALITY_LEFT_TO_RIGHT_EMBEDDING: ClassVar[int]
    DIRECTIONALITY_LEFT_TO_RIGHT_ISOLATE: ClassVar[int]
    DIRECTIONALITY_LEFT_TO_RIGHT_OVERRIDE: ClassVar[int]
    DIRECTIONALITY_NONSPACING_MARK: ClassVar[int]
    DIRECTIONALITY_OTHER_NEUTRALS: ClassVar[int]
    DIRECTIONALITY_PARAGRAPH_SEPARATOR: ClassVar[int]
    DIRECTIONALITY_POP_DIRECTIONAL_FORMAT: ClassVar[int]
    DIRECTIONALITY_POP_DIRECTIONAL_ISOLATE: ClassVar[int]
    DIRECTIONALITY_RIGHT_TO_LEFT: ClassVar[int]
    DIRECTIONALITY_RIGHT_TO_LEFT_ARABIC: ClassVar[int]
    DIRECTIONALITY_RIGHT_TO_LEFT_EMBEDDING: ClassVar[int]
    DIRECTIONALITY_RIGHT_TO_LEFT_ISOLATE: ClassVar[int]
    DIRECTIONALITY_RIGHT_TO_LEFT_OVERRIDE: ClassVar[int]
    DIRECTIONALITY_SEGMENT_SEPARATOR: ClassVar[int]
    DIRECTIONALITY_UNDEFINED: ClassVar[int]
    DIRECTIONALITY_WHITESPACE: ClassVar[int]
    ENCLOSING_MARK: ClassVar[int]
    END_PUNCTUATION: ClassVar[int]
    FINAL_QUOTE_PUNCTUATION: ClassVar[int]
    FORMAT: ClassVar[int]
    INITIAL_QUOTE_PUNCTUATION: ClassVar[int]
    LETTER_NUMBER: ClassVar[int]
    LINE_SEPARATOR: ClassVar[int]
    LOWERCASE_LETTER: ClassVar[int]
    MATH_SYMBOL: ClassVar[int]
    MAX_CODE_POINT: ClassVar[int]
    MAX_HIGH_SURROGATE: ClassVar[str]
    MAX_LOW_SURROGATE: ClassVar[str]
    MAX_RADIX: ClassVar[int]
    MAX_SURROGATE: ClassVar[str]
    MAX_VALUE: ClassVar[str]
    MIN_CODE_POINT: ClassVar[int]
    MIN_HIGH_SURROGATE: ClassVar[str]
    MIN_LOW_SURROGATE: ClassVar[str]
    MIN_RADIX: ClassVar[int]
    MIN_SUPPLEMENTARY_CODE_POINT: ClassVar[int]
    MIN_SURROGATE: ClassVar[str]
    MIN_VALUE: ClassVar[str]
    MODIFIER_LETTER: ClassVar[int]
    MODIFIER_SYMBOL: ClassVar[int]
    NON_SPACING_MARK: ClassVar[int]
    OTHER_LETTER: ClassVar[int]
    OTHER_NUMBER: ClassVar[int]
    OTHER_PUNCTUATION: ClassVar[int]
    OTHER_SYMBOL: ClassVar[int]
    PARAGRAPH_SEPARATOR: ClassVar[int]
    PRIVATE_USE: ClassVar[int]
    SIZE: ClassVar[int]
    SPACE_SEPARATOR: ClassVar[int]
    START_PUNCTUATION: ClassVar[int]
    SURROGATE: ClassVar[int]
    TITLECASE_LETTER: ClassVar[int]
    TYPE: ClassVar[type]
    UNASSIGNED: ClassVar[int]
    UPPERCASE_LETTER: ClassVar[int]
    def __init__(self, arg0: str) -> None: ...
    @staticmethod
    def valueOf(arg0: str) -> str: ...
    def charValue(self) -> str: ...
    @overload
    def hashCode(self) -> int: ...
    @overload
    @staticmethod
    def hashCode(arg0: str) -> int: ...
    def equals(self, arg0: Any) -> bool: ...
    @overload
    def toString(self) -> str: ...
    @overload
    @staticmethod
    def toString(arg0: str) -> str: ...
    @overload
    @staticmethod
    def toString(arg0: int) -> str: ...
    @staticmethod
    def isValidCodePoint(arg0: int) -> bool: ...
    @staticmethod
    def isBmpCodePoint(arg0: int) -> bool: ...
    @staticmethod
    def isSupplementaryCodePoint(arg0: int) -> bool: ...
    @staticmethod
    def isHighSurrogate(arg0: str) -> bool: ...
    @staticmethod
    def isLowSurrogate(arg0: str) -> bool: ...
    @staticmethod
    def isSurrogate(arg0: str) -> bool: ...
    @staticmethod
    def isSurrogatePair(arg0: str, arg1: str) -> bool: ...
    @staticmethod
    def charCount(arg0: int) -> int: ...
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
    @staticmethod
    def highSurrogate(arg0: int) -> str: ...
    @staticmethod
    def lowSurrogate(arg0: int) -> str: ...
    @overload
    @staticmethod
    def toChars(arg0: int, arg1: list[str], arg2: int) -> int: ...
    @overload
    @staticmethod
    def toChars(arg0: int) -> list[str]: ...
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
    @overload
    @staticmethod
    def isLowerCase(arg0: str) -> bool: ...
    @overload
    @staticmethod
    def isLowerCase(arg0: int) -> bool: ...
    @overload
    @staticmethod
    def isUpperCase(arg0: str) -> bool: ...
    @overload
    @staticmethod
    def isUpperCase(arg0: int) -> bool: ...
    @overload
    @staticmethod
    def isTitleCase(arg0: str) -> bool: ...
    @overload
    @staticmethod
    def isTitleCase(arg0: int) -> bool: ...
    @overload
    @staticmethod
    def isDigit(arg0: str) -> bool: ...
    @overload
    @staticmethod
    def isDigit(arg0: int) -> bool: ...
    @overload
    @staticmethod
    def isDefined(arg0: str) -> bool: ...
    @overload
    @staticmethod
    def isDefined(arg0: int) -> bool: ...
    @overload
    @staticmethod
    def isLetter(arg0: str) -> bool: ...
    @overload
    @staticmethod
    def isLetter(arg0: int) -> bool: ...
    @overload
    @staticmethod
    def isLetterOrDigit(arg0: str) -> bool: ...
    @overload
    @staticmethod
    def isLetterOrDigit(arg0: int) -> bool: ...
    @staticmethod
    def isJavaLetter(arg0: str) -> bool: ...
    @staticmethod
    def isJavaLetterOrDigit(arg0: str) -> bool: ...
    @staticmethod
    def isAlphabetic(arg0: int) -> bool: ...
    @staticmethod
    def isIdeographic(arg0: int) -> bool: ...
    @overload
    @staticmethod
    def isJavaIdentifierStart(arg0: str) -> bool: ...
    @overload
    @staticmethod
    def isJavaIdentifierStart(arg0: int) -> bool: ...
    @overload
    @staticmethod
    def isJavaIdentifierPart(arg0: str) -> bool: ...
    @overload
    @staticmethod
    def isJavaIdentifierPart(arg0: int) -> bool: ...
    @overload
    @staticmethod
    def isUnicodeIdentifierStart(arg0: str) -> bool: ...
    @overload
    @staticmethod
    def isUnicodeIdentifierStart(arg0: int) -> bool: ...
    @overload
    @staticmethod
    def isUnicodeIdentifierPart(arg0: str) -> bool: ...
    @overload
    @staticmethod
    def isUnicodeIdentifierPart(arg0: int) -> bool: ...
    @overload
    @staticmethod
    def isIdentifierIgnorable(arg0: str) -> bool: ...
    @overload
    @staticmethod
    def isIdentifierIgnorable(arg0: int) -> bool: ...
    @overload
    @staticmethod
    def toLowerCase(arg0: str) -> str: ...
    @overload
    @staticmethod
    def toLowerCase(arg0: int) -> int: ...
    @overload
    @staticmethod
    def toUpperCase(arg0: str) -> str: ...
    @overload
    @staticmethod
    def toUpperCase(arg0: int) -> int: ...
    @overload
    @staticmethod
    def toTitleCase(arg0: str) -> str: ...
    @overload
    @staticmethod
    def toTitleCase(arg0: int) -> int: ...
    @overload
    @staticmethod
    def digit(arg0: str, arg1: int) -> int: ...
    @overload
    @staticmethod
    def digit(arg0: int, arg1: int) -> int: ...
    @overload
    @staticmethod
    def getNumericValue(arg0: str) -> int: ...
    @overload
    @staticmethod
    def getNumericValue(arg0: int) -> int: ...
    @staticmethod
    def isSpace(arg0: str) -> bool: ...
    @overload
    @staticmethod
    def isSpaceChar(arg0: str) -> bool: ...
    @overload
    @staticmethod
    def isSpaceChar(arg0: int) -> bool: ...
    @overload
    @staticmethod
    def isWhitespace(arg0: str) -> bool: ...
    @overload
    @staticmethod
    def isWhitespace(arg0: int) -> bool: ...
    @overload
    @staticmethod
    def isISOControl(arg0: str) -> bool: ...
    @overload
    @staticmethod
    def isISOControl(arg0: int) -> bool: ...
    @overload
    @staticmethod
    def getType(arg0: str) -> int: ...
    @overload
    @staticmethod
    def getType(arg0: int) -> int: ...
    @staticmethod
    def forDigit(arg0: int, arg1: int) -> str: ...
    @overload
    @staticmethod
    def getDirectionality(arg0: str) -> int: ...
    @overload
    @staticmethod
    def getDirectionality(arg0: int) -> int: ...
    @overload
    @staticmethod
    def isMirrored(arg0: str) -> bool: ...
    @overload
    @staticmethod
    def isMirrored(arg0: int) -> bool: ...
    def compareTo(self, arg0: str) -> int: ...
    @staticmethod
    def compare(arg0: str, arg1: str) -> int: ...
    @staticmethod
    def reverseBytes(arg0: str) -> str: ...
    @staticmethod
    def getName(arg0: int) -> str: ...
    @staticmethod
    def codePointOf(arg0: str) -> int: ...

    class Subset:
        def __init__(self, arg0: str) -> None: ...
        def equals(self, arg0: Any) -> bool: ...
        def hashCode(self) -> int: ...
        def toString(self) -> str: ...

    class UnicodeBlock:
        ADLAM: ClassVar["UnicodeBlock"]
        AEGEAN_NUMBERS: ClassVar["UnicodeBlock"]
        AHOM: ClassVar["UnicodeBlock"]
        ALCHEMICAL_SYMBOLS: ClassVar["UnicodeBlock"]
        ALPHABETIC_PRESENTATION_FORMS: ClassVar["UnicodeBlock"]
        ANATOLIAN_HIEROGLYPHS: ClassVar["UnicodeBlock"]
        ANCIENT_GREEK_MUSICAL_NOTATION: ClassVar["UnicodeBlock"]
        ANCIENT_GREEK_NUMBERS: ClassVar["UnicodeBlock"]
        ANCIENT_SYMBOLS: ClassVar["UnicodeBlock"]
        ARABIC: ClassVar["UnicodeBlock"]
        ARABIC_EXTENDED_A: ClassVar["UnicodeBlock"]
        ARABIC_MATHEMATICAL_ALPHABETIC_SYMBOLS: ClassVar["UnicodeBlock"]
        ARABIC_PRESENTATION_FORMS_A: ClassVar["UnicodeBlock"]
        ARABIC_PRESENTATION_FORMS_B: ClassVar["UnicodeBlock"]
        ARABIC_SUPPLEMENT: ClassVar["UnicodeBlock"]
        ARMENIAN: ClassVar["UnicodeBlock"]
        ARROWS: ClassVar["UnicodeBlock"]
        AVESTAN: ClassVar["UnicodeBlock"]
        BALINESE: ClassVar["UnicodeBlock"]
        BAMUM: ClassVar["UnicodeBlock"]
        BAMUM_SUPPLEMENT: ClassVar["UnicodeBlock"]
        BASIC_LATIN: ClassVar["UnicodeBlock"]
        BASSA_VAH: ClassVar["UnicodeBlock"]
        BATAK: ClassVar["UnicodeBlock"]
        BENGALI: ClassVar["UnicodeBlock"]
        BHAIKSUKI: ClassVar["UnicodeBlock"]
        BLOCK_ELEMENTS: ClassVar["UnicodeBlock"]
        BOPOMOFO: ClassVar["UnicodeBlock"]
        BOPOMOFO_EXTENDED: ClassVar["UnicodeBlock"]
        BOX_DRAWING: ClassVar["UnicodeBlock"]
        BRAHMI: ClassVar["UnicodeBlock"]
        BRAILLE_PATTERNS: ClassVar["UnicodeBlock"]
        BUGINESE: ClassVar["UnicodeBlock"]
        BUHID: ClassVar["UnicodeBlock"]
        BYZANTINE_MUSICAL_SYMBOLS: ClassVar["UnicodeBlock"]
        CARIAN: ClassVar["UnicodeBlock"]
        CAUCASIAN_ALBANIAN: ClassVar["UnicodeBlock"]
        CHAKMA: ClassVar["UnicodeBlock"]
        CHAM: ClassVar["UnicodeBlock"]
        CHEROKEE: ClassVar["UnicodeBlock"]
        CHEROKEE_SUPPLEMENT: ClassVar["UnicodeBlock"]
        CHESS_SYMBOLS: ClassVar["UnicodeBlock"]
        CHORASMIAN: ClassVar["UnicodeBlock"]
        CJK_COMPATIBILITY: ClassVar["UnicodeBlock"]
        CJK_COMPATIBILITY_FORMS: ClassVar["UnicodeBlock"]
        CJK_COMPATIBILITY_IDEOGRAPHS: ClassVar["UnicodeBlock"]
        CJK_COMPATIBILITY_IDEOGRAPHS_SUPPLEMENT: ClassVar["UnicodeBlock"]
        CJK_RADICALS_SUPPLEMENT: ClassVar["UnicodeBlock"]
        CJK_STROKES: ClassVar["UnicodeBlock"]
        CJK_SYMBOLS_AND_PUNCTUATION: ClassVar["UnicodeBlock"]
        CJK_UNIFIED_IDEOGRAPHS: ClassVar["UnicodeBlock"]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_A: ClassVar["UnicodeBlock"]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_B: ClassVar["UnicodeBlock"]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_C: ClassVar["UnicodeBlock"]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_D: ClassVar["UnicodeBlock"]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_E: ClassVar["UnicodeBlock"]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_F: ClassVar["UnicodeBlock"]
        CJK_UNIFIED_IDEOGRAPHS_EXTENSION_G: ClassVar["UnicodeBlock"]
        COMBINING_DIACRITICAL_MARKS: ClassVar["UnicodeBlock"]
        COMBINING_DIACRITICAL_MARKS_EXTENDED: ClassVar["UnicodeBlock"]
        COMBINING_DIACRITICAL_MARKS_SUPPLEMENT: ClassVar["UnicodeBlock"]
        COMBINING_HALF_MARKS: ClassVar["UnicodeBlock"]
        COMBINING_MARKS_FOR_SYMBOLS: ClassVar["UnicodeBlock"]
        COMMON_INDIC_NUMBER_FORMS: ClassVar["UnicodeBlock"]
        CONTROL_PICTURES: ClassVar["UnicodeBlock"]
        COPTIC: ClassVar["UnicodeBlock"]
        COPTIC_EPACT_NUMBERS: ClassVar["UnicodeBlock"]
        COUNTING_ROD_NUMERALS: ClassVar["UnicodeBlock"]
        CUNEIFORM: ClassVar["UnicodeBlock"]
        CUNEIFORM_NUMBERS_AND_PUNCTUATION: ClassVar["UnicodeBlock"]
        CURRENCY_SYMBOLS: ClassVar["UnicodeBlock"]
        CYPRIOT_SYLLABARY: ClassVar["UnicodeBlock"]
        CYRILLIC: ClassVar["UnicodeBlock"]
        CYRILLIC_EXTENDED_A: ClassVar["UnicodeBlock"]
        CYRILLIC_EXTENDED_B: ClassVar["UnicodeBlock"]
        CYRILLIC_EXTENDED_C: ClassVar["UnicodeBlock"]
        CYRILLIC_SUPPLEMENTARY: ClassVar["UnicodeBlock"]
        DESERET: ClassVar["UnicodeBlock"]
        DEVANAGARI: ClassVar["UnicodeBlock"]
        DEVANAGARI_EXTENDED: ClassVar["UnicodeBlock"]
        DINGBATS: ClassVar["UnicodeBlock"]
        DIVES_AKURU: ClassVar["UnicodeBlock"]
        DOGRA: ClassVar["UnicodeBlock"]
        DOMINO_TILES: ClassVar["UnicodeBlock"]
        DUPLOYAN: ClassVar["UnicodeBlock"]
        EARLY_DYNASTIC_CUNEIFORM: ClassVar["UnicodeBlock"]
        EGYPTIAN_HIEROGLYPHS: ClassVar["UnicodeBlock"]
        EGYPTIAN_HIEROGLYPH_FORMAT_CONTROLS: ClassVar["UnicodeBlock"]
        ELBASAN: ClassVar["UnicodeBlock"]
        ELYMAIC: ClassVar["UnicodeBlock"]
        EMOTICONS: ClassVar["UnicodeBlock"]
        ENCLOSED_ALPHANUMERICS: ClassVar["UnicodeBlock"]
        ENCLOSED_ALPHANUMERIC_SUPPLEMENT: ClassVar["UnicodeBlock"]
        ENCLOSED_CJK_LETTERS_AND_MONTHS: ClassVar["UnicodeBlock"]
        ENCLOSED_IDEOGRAPHIC_SUPPLEMENT: ClassVar["UnicodeBlock"]
        ETHIOPIC: ClassVar["UnicodeBlock"]
        ETHIOPIC_EXTENDED: ClassVar["UnicodeBlock"]
        ETHIOPIC_EXTENDED_A: ClassVar["UnicodeBlock"]
        ETHIOPIC_SUPPLEMENT: ClassVar["UnicodeBlock"]
        GENERAL_PUNCTUATION: ClassVar["UnicodeBlock"]
        GEOMETRIC_SHAPES: ClassVar["UnicodeBlock"]
        GEOMETRIC_SHAPES_EXTENDED: ClassVar["UnicodeBlock"]
        GEORGIAN: ClassVar["UnicodeBlock"]
        GEORGIAN_EXTENDED: ClassVar["UnicodeBlock"]
        GEORGIAN_SUPPLEMENT: ClassVar["UnicodeBlock"]
        GLAGOLITIC: ClassVar["UnicodeBlock"]
        GLAGOLITIC_SUPPLEMENT: ClassVar["UnicodeBlock"]
        GOTHIC: ClassVar["UnicodeBlock"]
        GRANTHA: ClassVar["UnicodeBlock"]
        GREEK: ClassVar["UnicodeBlock"]
        GREEK_EXTENDED: ClassVar["UnicodeBlock"]
        GUJARATI: ClassVar["UnicodeBlock"]
        GUNJALA_GONDI: ClassVar["UnicodeBlock"]
        GURMUKHI: ClassVar["UnicodeBlock"]
        HALFWIDTH_AND_FULLWIDTH_FORMS: ClassVar["UnicodeBlock"]
        HANGUL_COMPATIBILITY_JAMO: ClassVar["UnicodeBlock"]
        HANGUL_JAMO: ClassVar["UnicodeBlock"]
        HANGUL_JAMO_EXTENDED_A: ClassVar["UnicodeBlock"]
        HANGUL_JAMO_EXTENDED_B: ClassVar["UnicodeBlock"]
        HANGUL_SYLLABLES: ClassVar["UnicodeBlock"]
        HANIFI_ROHINGYA: ClassVar["UnicodeBlock"]
        HANUNOO: ClassVar["UnicodeBlock"]
        HATRAN: ClassVar["UnicodeBlock"]
        HEBREW: ClassVar["UnicodeBlock"]
        HIGH_PRIVATE_USE_SURROGATES: ClassVar["UnicodeBlock"]
        HIGH_SURROGATES: ClassVar["UnicodeBlock"]
        HIRAGANA: ClassVar["UnicodeBlock"]
        IDEOGRAPHIC_DESCRIPTION_CHARACTERS: ClassVar["UnicodeBlock"]
        IDEOGRAPHIC_SYMBOLS_AND_PUNCTUATION: ClassVar["UnicodeBlock"]
        IMPERIAL_ARAMAIC: ClassVar["UnicodeBlock"]
        INDIC_SIYAQ_NUMBERS: ClassVar["UnicodeBlock"]
        INSCRIPTIONAL_PAHLAVI: ClassVar["UnicodeBlock"]
        INSCRIPTIONAL_PARTHIAN: ClassVar["UnicodeBlock"]
        IPA_EXTENSIONS: ClassVar["UnicodeBlock"]
        JAVANESE: ClassVar["UnicodeBlock"]
        KAITHI: ClassVar["UnicodeBlock"]
        KANA_EXTENDED_A: ClassVar["UnicodeBlock"]
        KANA_SUPPLEMENT: ClassVar["UnicodeBlock"]
        KANBUN: ClassVar["UnicodeBlock"]
        KANGXI_RADICALS: ClassVar["UnicodeBlock"]
        KANNADA: ClassVar["UnicodeBlock"]
        KATAKANA: ClassVar["UnicodeBlock"]
        KATAKANA_PHONETIC_EXTENSIONS: ClassVar["UnicodeBlock"]
        KAYAH_LI: ClassVar["UnicodeBlock"]
        KHAROSHTHI: ClassVar["UnicodeBlock"]
        KHITAN_SMALL_SCRIPT: ClassVar["UnicodeBlock"]
        KHMER: ClassVar["UnicodeBlock"]
        KHMER_SYMBOLS: ClassVar["UnicodeBlock"]
        KHOJKI: ClassVar["UnicodeBlock"]
        KHUDAWADI: ClassVar["UnicodeBlock"]
        LAO: ClassVar["UnicodeBlock"]
        LATIN_1_SUPPLEMENT: ClassVar["UnicodeBlock"]
        LATIN_EXTENDED_A: ClassVar["UnicodeBlock"]
        LATIN_EXTENDED_ADDITIONAL: ClassVar["UnicodeBlock"]
        LATIN_EXTENDED_B: ClassVar["UnicodeBlock"]
        LATIN_EXTENDED_C: ClassVar["UnicodeBlock"]
        LATIN_EXTENDED_D: ClassVar["UnicodeBlock"]
        LATIN_EXTENDED_E: ClassVar["UnicodeBlock"]
        LEPCHA: ClassVar["UnicodeBlock"]
        LETTERLIKE_SYMBOLS: ClassVar["UnicodeBlock"]
        LIMBU: ClassVar["UnicodeBlock"]
        LINEAR_A: ClassVar["UnicodeBlock"]
        LINEAR_B_IDEOGRAMS: ClassVar["UnicodeBlock"]
        LINEAR_B_SYLLABARY: ClassVar["UnicodeBlock"]
        LISU: ClassVar["UnicodeBlock"]
        LISU_SUPPLEMENT: ClassVar["UnicodeBlock"]
        LOW_SURROGATES: ClassVar["UnicodeBlock"]
        LYCIAN: ClassVar["UnicodeBlock"]
        LYDIAN: ClassVar["UnicodeBlock"]
        MAHAJANI: ClassVar["UnicodeBlock"]
        MAHJONG_TILES: ClassVar["UnicodeBlock"]
        MAKASAR: ClassVar["UnicodeBlock"]
        MALAYALAM: ClassVar["UnicodeBlock"]
        MANDAIC: ClassVar["UnicodeBlock"]
        MANICHAEAN: ClassVar["UnicodeBlock"]
        MARCHEN: ClassVar["UnicodeBlock"]
        MASARAM_GONDI: ClassVar["UnicodeBlock"]
        MATHEMATICAL_ALPHANUMERIC_SYMBOLS: ClassVar["UnicodeBlock"]
        MATHEMATICAL_OPERATORS: ClassVar["UnicodeBlock"]
        MAYAN_NUMERALS: ClassVar["UnicodeBlock"]
        MEDEFAIDRIN: ClassVar["UnicodeBlock"]
        MEETEI_MAYEK: ClassVar["UnicodeBlock"]
        MEETEI_MAYEK_EXTENSIONS: ClassVar["UnicodeBlock"]
        MENDE_KIKAKUI: ClassVar["UnicodeBlock"]
        MEROITIC_CURSIVE: ClassVar["UnicodeBlock"]
        MEROITIC_HIEROGLYPHS: ClassVar["UnicodeBlock"]
        MIAO: ClassVar["UnicodeBlock"]
        MISCELLANEOUS_MATHEMATICAL_SYMBOLS_A: ClassVar["UnicodeBlock"]
        MISCELLANEOUS_MATHEMATICAL_SYMBOLS_B: ClassVar["UnicodeBlock"]
        MISCELLANEOUS_SYMBOLS: ClassVar["UnicodeBlock"]
        MISCELLANEOUS_SYMBOLS_AND_ARROWS: ClassVar["UnicodeBlock"]
        MISCELLANEOUS_SYMBOLS_AND_PICTOGRAPHS: ClassVar["UnicodeBlock"]
        MISCELLANEOUS_TECHNICAL: ClassVar["UnicodeBlock"]
        MODI: ClassVar["UnicodeBlock"]
        MODIFIER_TONE_LETTERS: ClassVar["UnicodeBlock"]
        MONGOLIAN: ClassVar["UnicodeBlock"]
        MONGOLIAN_SUPPLEMENT: ClassVar["UnicodeBlock"]
        MRO: ClassVar["UnicodeBlock"]
        MULTANI: ClassVar["UnicodeBlock"]
        MUSICAL_SYMBOLS: ClassVar["UnicodeBlock"]
        MYANMAR: ClassVar["UnicodeBlock"]
        MYANMAR_EXTENDED_A: ClassVar["UnicodeBlock"]
        MYANMAR_EXTENDED_B: ClassVar["UnicodeBlock"]
        NABATAEAN: ClassVar["UnicodeBlock"]
        NANDINAGARI: ClassVar["UnicodeBlock"]
        NEWA: ClassVar["UnicodeBlock"]
        NEW_TAI_LUE: ClassVar["UnicodeBlock"]
        NKO: ClassVar["UnicodeBlock"]
        NUMBER_FORMS: ClassVar["UnicodeBlock"]
        NUSHU: ClassVar["UnicodeBlock"]
        NYIAKENG_PUACHUE_HMONG: ClassVar["UnicodeBlock"]
        OGHAM: ClassVar["UnicodeBlock"]
        OLD_HUNGARIAN: ClassVar["UnicodeBlock"]
        OLD_ITALIC: ClassVar["UnicodeBlock"]
        OLD_NORTH_ARABIAN: ClassVar["UnicodeBlock"]
        OLD_PERMIC: ClassVar["UnicodeBlock"]
        OLD_PERSIAN: ClassVar["UnicodeBlock"]
        OLD_SOGDIAN: ClassVar["UnicodeBlock"]
        OLD_SOUTH_ARABIAN: ClassVar["UnicodeBlock"]
        OLD_TURKIC: ClassVar["UnicodeBlock"]
        OL_CHIKI: ClassVar["UnicodeBlock"]
        OPTICAL_CHARACTER_RECOGNITION: ClassVar["UnicodeBlock"]
        ORIYA: ClassVar["UnicodeBlock"]
        ORNAMENTAL_DINGBATS: ClassVar["UnicodeBlock"]
        OSAGE: ClassVar["UnicodeBlock"]
        OSMANYA: ClassVar["UnicodeBlock"]
        OTTOMAN_SIYAQ_NUMBERS: ClassVar["UnicodeBlock"]
        PAHAWH_HMONG: ClassVar["UnicodeBlock"]
        PALMYRENE: ClassVar["UnicodeBlock"]
        PAU_CIN_HAU: ClassVar["UnicodeBlock"]
        PHAGS_PA: ClassVar["UnicodeBlock"]
        PHAISTOS_DISC: ClassVar["UnicodeBlock"]
        PHOENICIAN: ClassVar["UnicodeBlock"]
        PHONETIC_EXTENSIONS: ClassVar["UnicodeBlock"]
        PHONETIC_EXTENSIONS_SUPPLEMENT: ClassVar["UnicodeBlock"]
        PLAYING_CARDS: ClassVar["UnicodeBlock"]
        PRIVATE_USE_AREA: ClassVar["UnicodeBlock"]
        PSALTER_PAHLAVI: ClassVar["UnicodeBlock"]
        REJANG: ClassVar["UnicodeBlock"]
        RUMI_NUMERAL_SYMBOLS: ClassVar["UnicodeBlock"]
        RUNIC: ClassVar["UnicodeBlock"]
        SAMARITAN: ClassVar["UnicodeBlock"]
        SAURASHTRA: ClassVar["UnicodeBlock"]
        SHARADA: ClassVar["UnicodeBlock"]
        SHAVIAN: ClassVar["UnicodeBlock"]
        SHORTHAND_FORMAT_CONTROLS: ClassVar["UnicodeBlock"]
        SIDDHAM: ClassVar["UnicodeBlock"]
        SINHALA: ClassVar["UnicodeBlock"]
        SINHALA_ARCHAIC_NUMBERS: ClassVar["UnicodeBlock"]
        SMALL_FORM_VARIANTS: ClassVar["UnicodeBlock"]
        SMALL_KANA_EXTENSION: ClassVar["UnicodeBlock"]
        SOGDIAN: ClassVar["UnicodeBlock"]
        SORA_SOMPENG: ClassVar["UnicodeBlock"]
        SOYOMBO: ClassVar["UnicodeBlock"]
        SPACING_MODIFIER_LETTERS: ClassVar["UnicodeBlock"]
        SPECIALS: ClassVar["UnicodeBlock"]
        SUNDANESE: ClassVar["UnicodeBlock"]
        SUNDANESE_SUPPLEMENT: ClassVar["UnicodeBlock"]
        SUPERSCRIPTS_AND_SUBSCRIPTS: ClassVar["UnicodeBlock"]
        SUPPLEMENTAL_ARROWS_A: ClassVar["UnicodeBlock"]
        SUPPLEMENTAL_ARROWS_B: ClassVar["UnicodeBlock"]
        SUPPLEMENTAL_ARROWS_C: ClassVar["UnicodeBlock"]
        SUPPLEMENTAL_MATHEMATICAL_OPERATORS: ClassVar["UnicodeBlock"]
        SUPPLEMENTAL_PUNCTUATION: ClassVar["UnicodeBlock"]
        SUPPLEMENTAL_SYMBOLS_AND_PICTOGRAPHS: ClassVar["UnicodeBlock"]
        SUPPLEMENTARY_PRIVATE_USE_AREA_A: ClassVar["UnicodeBlock"]
        SUPPLEMENTARY_PRIVATE_USE_AREA_B: ClassVar["UnicodeBlock"]
        SURROGATES_AREA: ClassVar["UnicodeBlock"]
        SUTTON_SIGNWRITING: ClassVar["UnicodeBlock"]
        SYLOTI_NAGRI: ClassVar["UnicodeBlock"]
        SYMBOLS_AND_PICTOGRAPHS_EXTENDED_A: ClassVar["UnicodeBlock"]
        SYMBOLS_FOR_LEGACY_COMPUTING: ClassVar["UnicodeBlock"]
        SYRIAC: ClassVar["UnicodeBlock"]
        SYRIAC_SUPPLEMENT: ClassVar["UnicodeBlock"]
        TAGALOG: ClassVar["UnicodeBlock"]
        TAGBANWA: ClassVar["UnicodeBlock"]
        TAGS: ClassVar["UnicodeBlock"]
        TAI_LE: ClassVar["UnicodeBlock"]
        TAI_THAM: ClassVar["UnicodeBlock"]
        TAI_VIET: ClassVar["UnicodeBlock"]
        TAI_XUAN_JING_SYMBOLS: ClassVar["UnicodeBlock"]
        TAKRI: ClassVar["UnicodeBlock"]
        TAMIL: ClassVar["UnicodeBlock"]
        TAMIL_SUPPLEMENT: ClassVar["UnicodeBlock"]
        TANGUT: ClassVar["UnicodeBlock"]
        TANGUT_COMPONENTS: ClassVar["UnicodeBlock"]
        TANGUT_SUPPLEMENT: ClassVar["UnicodeBlock"]
        TELUGU: ClassVar["UnicodeBlock"]
        THAANA: ClassVar["UnicodeBlock"]
        THAI: ClassVar["UnicodeBlock"]
        TIBETAN: ClassVar["UnicodeBlock"]
        TIFINAGH: ClassVar["UnicodeBlock"]
        TIRHUTA: ClassVar["UnicodeBlock"]
        TRANSPORT_AND_MAP_SYMBOLS: ClassVar["UnicodeBlock"]
        UGARITIC: ClassVar["UnicodeBlock"]
        UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS: ClassVar["UnicodeBlock"]
        UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_EXTENDED: ClassVar["UnicodeBlock"]
        VAI: ClassVar["UnicodeBlock"]
        VARIATION_SELECTORS: ClassVar["UnicodeBlock"]
        VARIATION_SELECTORS_SUPPLEMENT: ClassVar["UnicodeBlock"]
        VEDIC_EXTENSIONS: ClassVar["UnicodeBlock"]
        VERTICAL_FORMS: ClassVar["UnicodeBlock"]
        WANCHO: ClassVar["UnicodeBlock"]
        WARANG_CITI: ClassVar["UnicodeBlock"]
        YEZIDI: ClassVar["UnicodeBlock"]
        YIJING_HEXAGRAM_SYMBOLS: ClassVar["UnicodeBlock"]
        YI_RADICALS: ClassVar["UnicodeBlock"]
        YI_SYLLABLES: ClassVar["UnicodeBlock"]
        ZANABAZAR_SQUARE: ClassVar["UnicodeBlock"]
        @overload
        @staticmethod
        def of(arg0: str) -> "UnicodeBlock": ...
        @overload
        @staticmethod
        def of(arg0: int) -> "UnicodeBlock": ...
        @staticmethod
        def forName(arg0: str) -> "UnicodeBlock": ...

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
        UNKNOWN: ClassVar["UnicodeScript"]
        @staticmethod
        def values() -> list["UnicodeScript"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "UnicodeScript": ...
        @staticmethod
        def of(arg0: int) -> "UnicodeScript": ...
        @staticmethod
        def forName(arg0: str) -> "UnicodeScript": ...
