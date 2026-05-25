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
    @staticmethod
    def values() -> list["DisplayContext"]: ...
    @staticmethod
    def valueOf(arg0: str) -> "DisplayContext": ...
    def type(self) -> "Type": ...
    def value(self) -> int: ...

    class Type:
        DIALECT_HANDLING: ClassVar["Type"]
        CAPITALIZATION: ClassVar["Type"]
        DISPLAY_LENGTH: ClassVar["Type"]
        SUBSTITUTE_HANDLING: ClassVar["Type"]
        @staticmethod
        def values() -> list["Type"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "Type": ...
