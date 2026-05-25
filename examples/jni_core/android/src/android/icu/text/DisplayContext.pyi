from typing import Any, ClassVar, overload

class DisplayContext:
    STANDARD_NAMES: ClassVar["DisplayContext"]
    DIALECT_NAMES: ClassVar["DisplayContext"]
    CAPITALIZATION_NONE: ClassVar["DisplayContext"]
    CAPITALIZATION_FOR_MIDDLE_OF_SENTENCE: ClassVar["DisplayContext"]
    CAPITALIZATION_FOR_BEGINNING_OF_SENTENCE: ClassVar["DisplayContext"]
    CAPITALIZATION_FOR_UI_LIST_OR_MENU: ClassVar["DisplayContext"]
    CAPITALIZATION_FOR_STANDALONE: ClassVar["DisplayContext"]
    LENGTH_FULL: ClassVar["DisplayContext"]
    LENGTH_SHORT: ClassVar["DisplayContext"]
    SUBSTITUTE: ClassVar["DisplayContext"]
    NO_SUBSTITUTE: ClassVar["DisplayContext"]
    STANDARD_NAMES: ClassVar["DisplayContext"]
    DIALECT_NAMES: ClassVar["DisplayContext"]
    CAPITALIZATION_NONE: ClassVar["DisplayContext"]
    CAPITALIZATION_FOR_MIDDLE_OF_SENTENCE: ClassVar["DisplayContext"]
    CAPITALIZATION_FOR_BEGINNING_OF_SENTENCE: ClassVar["DisplayContext"]
    CAPITALIZATION_FOR_UI_LIST_OR_MENU: ClassVar["DisplayContext"]
    CAPITALIZATION_FOR_STANDALONE: ClassVar["DisplayContext"]
    LENGTH_FULL: ClassVar["DisplayContext"]
    LENGTH_SHORT: ClassVar["DisplayContext"]
    SUBSTITUTE: ClassVar["DisplayContext"]
    NO_SUBSTITUTE: ClassVar["DisplayContext"]
    def type(self) -> Any: ...
    def value(self) -> int: ...
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "DisplayContext": ...

    class Type:
        DIALECT_HANDLING: ClassVar["Type"]
        CAPITALIZATION: ClassVar["Type"]
        DISPLAY_LENGTH: ClassVar["Type"]
        SUBSTITUTE_HANDLING: ClassVar["Type"]
        DIALECT_HANDLING: ClassVar[Any]
        CAPITALIZATION: ClassVar[Any]
        DISPLAY_LENGTH: ClassVar[Any]
        SUBSTITUTE_HANDLING: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
