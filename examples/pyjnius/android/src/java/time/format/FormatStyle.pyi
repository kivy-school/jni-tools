from typing import Any, ClassVar, overload

class FormatStyle:
    FULL: ClassVar["FormatStyle"]
    LONG: ClassVar["FormatStyle"]
    MEDIUM: ClassVar["FormatStyle"]
    SHORT: ClassVar["FormatStyle"]
    @staticmethod
    def values() -> list["FormatStyle"]: ...
    @staticmethod
    def valueOf(arg0: str) -> "FormatStyle": ...
