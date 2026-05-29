from typing import Any, ClassVar, overload

class DisplayOptions:
    def getNounClass(self) -> Any: ...
    def getNameStyle(self) -> Any: ...
    def getCapitalization(self) -> Any: ...
    def getDisplayLength(self) -> Any: ...
    def getPluralCategory(self) -> Any: ...
    def copyToBuilder(self) -> Any: ...
    def getGrammaticalCase(self) -> Any: ...
    def getSubstituteHandling(self) -> Any: ...
    @staticmethod
    def builder() -> Any: ...

    class SubstituteHandling:
        NO_SUBSTITUTE: ClassVar["SubstituteHandling"]
        SUBSTITUTE: ClassVar["SubstituteHandling"]
        UNDEFINED: ClassVar["SubstituteHandling"]
        NO_SUBSTITUTE: ClassVar[Any]
        SUBSTITUTE: ClassVar[Any]
        UNDEFINED: ClassVar[Any]
        VALUES: ClassVar[list]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class PluralCategory:
        FEW: ClassVar["PluralCategory"]
        MANY: ClassVar["PluralCategory"]
        ONE: ClassVar["PluralCategory"]
        OTHER: ClassVar["PluralCategory"]
        TWO: ClassVar["PluralCategory"]
        UNDEFINED: ClassVar["PluralCategory"]
        ZERO: ClassVar["PluralCategory"]
        FEW: ClassVar[Any]
        MANY: ClassVar[Any]
        ONE: ClassVar[Any]
        OTHER: ClassVar[Any]
        TWO: ClassVar[Any]
        UNDEFINED: ClassVar[Any]
        ZERO: ClassVar[Any]
        VALUES: ClassVar[list]
        @staticmethod
        def fromIdentifier(p0: str) -> Any: ...
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
        def getIdentifier(self) -> str: ...

    class NounClass:
        ANIMATE: ClassVar["NounClass"]
        COMMON: ClassVar["NounClass"]
        FEMININE: ClassVar["NounClass"]
        INANIMATE: ClassVar["NounClass"]
        MASCULINE: ClassVar["NounClass"]
        NEUTER: ClassVar["NounClass"]
        OTHER: ClassVar["NounClass"]
        PERSONAL: ClassVar["NounClass"]
        UNDEFINED: ClassVar["NounClass"]
        ANIMATE: ClassVar[Any]
        COMMON: ClassVar[Any]
        FEMININE: ClassVar[Any]
        INANIMATE: ClassVar[Any]
        MASCULINE: ClassVar[Any]
        NEUTER: ClassVar[Any]
        OTHER: ClassVar[Any]
        PERSONAL: ClassVar[Any]
        UNDEFINED: ClassVar[Any]
        VALUES: ClassVar[list]
        @staticmethod
        def fromIdentifier(p0: str) -> Any: ...
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
        def getIdentifier(self) -> str: ...

    class NameStyle:
        DIALECT_NAMES: ClassVar["NameStyle"]
        STANDARD_NAMES: ClassVar["NameStyle"]
        UNDEFINED: ClassVar["NameStyle"]
        DIALECT_NAMES: ClassVar[Any]
        STANDARD_NAMES: ClassVar[Any]
        UNDEFINED: ClassVar[Any]
        VALUES: ClassVar[list]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class GrammaticalCase:
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
        UNDEFINED: ClassVar["GrammaticalCase"]
        VOCATIVE: ClassVar["GrammaticalCase"]
        ABLATIVE: ClassVar[Any]
        ACCUSATIVE: ClassVar[Any]
        COMITATIVE: ClassVar[Any]
        DATIVE: ClassVar[Any]
        ERGATIVE: ClassVar[Any]
        GENITIVE: ClassVar[Any]
        INSTRUMENTAL: ClassVar[Any]
        LOCATIVE: ClassVar[Any]
        LOCATIVE_COPULATIVE: ClassVar[Any]
        NOMINATIVE: ClassVar[Any]
        OBLIQUE: ClassVar[Any]
        PREPOSITIONAL: ClassVar[Any]
        SOCIATIVE: ClassVar[Any]
        UNDEFINED: ClassVar[Any]
        VOCATIVE: ClassVar[Any]
        VALUES: ClassVar[list]
        @staticmethod
        def fromIdentifier(p0: str) -> Any: ...
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
        def getIdentifier(self) -> str: ...

    class DisplayLength:
        LENGTH_FULL: ClassVar["DisplayLength"]
        LENGTH_SHORT: ClassVar["DisplayLength"]
        UNDEFINED: ClassVar["DisplayLength"]
        LENGTH_FULL: ClassVar[Any]
        LENGTH_SHORT: ClassVar[Any]
        UNDEFINED: ClassVar[Any]
        VALUES: ClassVar[list]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class Capitalization:
        BEGINNING_OF_SENTENCE: ClassVar["Capitalization"]
        MIDDLE_OF_SENTENCE: ClassVar["Capitalization"]
        STANDALONE: ClassVar["Capitalization"]
        UI_LIST_OR_MENU: ClassVar["Capitalization"]
        UNDEFINED: ClassVar["Capitalization"]
        BEGINNING_OF_SENTENCE: ClassVar[Any]
        MIDDLE_OF_SENTENCE: ClassVar[Any]
        STANDALONE: ClassVar[Any]
        UI_LIST_OR_MENU: ClassVar[Any]
        UNDEFINED: ClassVar[Any]
        VALUES: ClassVar[list]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class Builder:
        def setCapitalization(self, p0: Any) -> Any: ...
        def setDisplayLength(self, p0: Any) -> Any: ...
        def setGrammaticalCase(self, p0: Any) -> Any: ...
        def setNameStyle(self, p0: Any) -> Any: ...
        def setNounClass(self, p0: Any) -> Any: ...
        def setPluralCategory(self, p0: Any) -> Any: ...
        def setSubstituteHandling(self, p0: Any) -> Any: ...
        def build(self) -> "DisplayOptions": ...
