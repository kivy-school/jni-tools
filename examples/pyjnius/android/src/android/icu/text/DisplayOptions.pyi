from typing import Any, ClassVar, overload

class DisplayOptions:
    @staticmethod
    def builder() -> "Builder": ...
    def copyToBuilder(self) -> "Builder": ...
    def getGrammaticalCase(self) -> "GrammaticalCase": ...
    def getNounClass(self) -> "NounClass": ...
    def getPluralCategory(self) -> "PluralCategory": ...
    def getCapitalization(self) -> "Capitalization": ...
    def getNameStyle(self) -> "NameStyle": ...
    def getDisplayLength(self) -> "DisplayLength": ...
    def getSubstituteHandling(self) -> "SubstituteHandling": ...

    class Builder:
        def setGrammaticalCase(self, arg0: "GrammaticalCase") -> "Builder": ...
        def setNounClass(self, arg0: "NounClass") -> "Builder": ...
        def setPluralCategory(self, arg0: "PluralCategory") -> "Builder": ...
        def setCapitalization(self, arg0: "Capitalization") -> "Builder": ...
        def setNameStyle(self, arg0: "NameStyle") -> "Builder": ...
        def setDisplayLength(self, arg0: "DisplayLength") -> "Builder": ...
        def setSubstituteHandling(self, arg0: "SubstituteHandling") -> "Builder": ...
        def build(self) -> "DisplayOptions": ...

    class Capitalization:
        UNDEFINED: ClassVar["Capitalization"]
        BEGINNING_OF_SENTENCE: ClassVar["Capitalization"]
        MIDDLE_OF_SENTENCE: ClassVar["Capitalization"]
        STANDALONE: ClassVar["Capitalization"]
        UI_LIST_OR_MENU: ClassVar["Capitalization"]
        VALUES: ClassVar[list]
        @staticmethod
        def values() -> list["Capitalization"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "Capitalization": ...

    class DisplayLength:
        UNDEFINED: ClassVar["DisplayLength"]
        LENGTH_FULL: ClassVar["DisplayLength"]
        LENGTH_SHORT: ClassVar["DisplayLength"]
        VALUES: ClassVar[list]
        @staticmethod
        def values() -> list["DisplayLength"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "DisplayLength": ...

    class GrammaticalCase:
        UNDEFINED: ClassVar["GrammaticalCase"]
        ABLATIVE: ClassVar["GrammaticalCase"]
        ACCUSATIVE: ClassVar["GrammaticalCase"]
        COMITATIVE: ClassVar["GrammaticalCase"]
        DATIVE: ClassVar["GrammaticalCase"]
        ERGATIVE: ClassVar["GrammaticalCase"]
        GENITIVE: ClassVar["GrammaticalCase"]
        INSTRUMENTAL: ClassVar["GrammaticalCase"]
        LOCATIVE: ClassVar["GrammaticalCase"]
        LOCATIVE_COPULATIVE: ClassVar["GrammaticalCase"]
        NOMINATIVE: ClassVar["GrammaticalCase"]
        OBLIQUE: ClassVar["GrammaticalCase"]
        PREPOSITIONAL: ClassVar["GrammaticalCase"]
        SOCIATIVE: ClassVar["GrammaticalCase"]
        VOCATIVE: ClassVar["GrammaticalCase"]
        VALUES: ClassVar[list]
        @staticmethod
        def values() -> list["GrammaticalCase"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "GrammaticalCase": ...
        def getIdentifier(self) -> str: ...
        @staticmethod
        def fromIdentifier(arg0: str) -> "GrammaticalCase": ...

    class NameStyle:
        UNDEFINED: ClassVar["NameStyle"]
        STANDARD_NAMES: ClassVar["NameStyle"]
        DIALECT_NAMES: ClassVar["NameStyle"]
        VALUES: ClassVar[list]
        @staticmethod
        def values() -> list["NameStyle"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "NameStyle": ...

    class NounClass:
        UNDEFINED: ClassVar["NounClass"]
        OTHER: ClassVar["NounClass"]
        NEUTER: ClassVar["NounClass"]
        FEMININE: ClassVar["NounClass"]
        MASCULINE: ClassVar["NounClass"]
        ANIMATE: ClassVar["NounClass"]
        INANIMATE: ClassVar["NounClass"]
        PERSONAL: ClassVar["NounClass"]
        COMMON: ClassVar["NounClass"]
        VALUES: ClassVar[list]
        @staticmethod
        def values() -> list["NounClass"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "NounClass": ...
        def getIdentifier(self) -> str: ...
        @staticmethod
        def fromIdentifier(arg0: str) -> "NounClass": ...

    class PluralCategory:
        UNDEFINED: ClassVar["PluralCategory"]
        ZERO: ClassVar["PluralCategory"]
        ONE: ClassVar["PluralCategory"]
        TWO: ClassVar["PluralCategory"]
        FEW: ClassVar["PluralCategory"]
        MANY: ClassVar["PluralCategory"]
        OTHER: ClassVar["PluralCategory"]
        VALUES: ClassVar[list]
        @staticmethod
        def values() -> list["PluralCategory"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "PluralCategory": ...
        def getIdentifier(self) -> str: ...
        @staticmethod
        def fromIdentifier(arg0: str) -> "PluralCategory": ...

    class SubstituteHandling:
        UNDEFINED: ClassVar["SubstituteHandling"]
        SUBSTITUTE: ClassVar["SubstituteHandling"]
        NO_SUBSTITUTE: ClassVar["SubstituteHandling"]
        VALUES: ClassVar[list]
        @staticmethod
        def values() -> list["SubstituteHandling"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "SubstituteHandling": ...
