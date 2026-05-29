from typing import Any, ClassVar, overload

class DisplayOptions:
    def copyToBuilder(self) -> Any: ...
    def getGrammaticalCase(self) -> Any: ...
    def getPluralCategory(self) -> Any: ...
    def getCapitalization(self) -> Any: ...
    def getNameStyle(self) -> Any: ...
    def getDisplayLength(self) -> Any: ...
    def getSubstituteHandling(self) -> Any: ...
    def getNounClass(self) -> Any: ...
    @staticmethod
    def builder() -> Any: ...

    class SubstituteHandling:
        UNDEFINED: ClassVar["SubstituteHandling"]
        SUBSTITUTE: ClassVar["SubstituteHandling"]
        NO_SUBSTITUTE: ClassVar["SubstituteHandling"]
        UNDEFINED: ClassVar[Any]
        SUBSTITUTE: ClassVar[Any]
        NO_SUBSTITUTE: ClassVar[Any]
        VALUES: ClassVar[list]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class PluralCategory:
        UNDEFINED: ClassVar["PluralCategory"]
        ZERO: ClassVar["PluralCategory"]
        ONE: ClassVar["PluralCategory"]
        TWO: ClassVar["PluralCategory"]
        FEW: ClassVar["PluralCategory"]
        MANY: ClassVar["PluralCategory"]
        OTHER: ClassVar["PluralCategory"]
        UNDEFINED: ClassVar[Any]
        ZERO: ClassVar[Any]
        ONE: ClassVar[Any]
        TWO: ClassVar[Any]
        FEW: ClassVar[Any]
        MANY: ClassVar[Any]
        OTHER: ClassVar[Any]
        VALUES: ClassVar[list]
        @staticmethod
        def fromIdentifier(p0: str) -> Any: ...
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
        def getIdentifier(self) -> str: ...

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
        UNDEFINED: ClassVar[Any]
        OTHER: ClassVar[Any]
        NEUTER: ClassVar[Any]
        FEMININE: ClassVar[Any]
        MASCULINE: ClassVar[Any]
        ANIMATE: ClassVar[Any]
        INANIMATE: ClassVar[Any]
        PERSONAL: ClassVar[Any]
        COMMON: ClassVar[Any]
        VALUES: ClassVar[list]
        @staticmethod
        def fromIdentifier(p0: str) -> Any: ...
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
        def getIdentifier(self) -> str: ...

    class NameStyle:
        UNDEFINED: ClassVar["NameStyle"]
        STANDARD_NAMES: ClassVar["NameStyle"]
        DIALECT_NAMES: ClassVar["NameStyle"]
        UNDEFINED: ClassVar[Any]
        STANDARD_NAMES: ClassVar[Any]
        DIALECT_NAMES: ClassVar[Any]
        VALUES: ClassVar[list]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

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
        UNDEFINED: ClassVar[Any]
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
        UNDEFINED: ClassVar["DisplayLength"]
        LENGTH_FULL: ClassVar["DisplayLength"]
        LENGTH_SHORT: ClassVar["DisplayLength"]
        UNDEFINED: ClassVar[Any]
        LENGTH_FULL: ClassVar[Any]
        LENGTH_SHORT: ClassVar[Any]
        VALUES: ClassVar[list]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class Capitalization:
        UNDEFINED: ClassVar["Capitalization"]
        BEGINNING_OF_SENTENCE: ClassVar["Capitalization"]
        MIDDLE_OF_SENTENCE: ClassVar["Capitalization"]
        STANDALONE: ClassVar["Capitalization"]
        UI_LIST_OR_MENU: ClassVar["Capitalization"]
        UNDEFINED: ClassVar[Any]
        BEGINNING_OF_SENTENCE: ClassVar[Any]
        MIDDLE_OF_SENTENCE: ClassVar[Any]
        STANDALONE: ClassVar[Any]
        UI_LIST_OR_MENU: ClassVar[Any]
        VALUES: ClassVar[list]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class Builder:
        def setGrammaticalCase(self, p0: Any) -> Any: ...
        def setNounClass(self, p0: Any) -> Any: ...
        def setPluralCategory(self, p0: Any) -> Any: ...
        def setCapitalization(self, p0: Any) -> Any: ...
        def setNameStyle(self, p0: Any) -> Any: ...
        def setDisplayLength(self, p0: Any) -> Any: ...
        def setSubstituteHandling(self, p0: Any) -> Any: ...
        def build(self) -> "DisplayOptions": ...
