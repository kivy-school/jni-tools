from typing import Any, ClassVar, overload

class FormatStyle:
    FULL: ClassVar["FormatStyle"]
    LONG: ClassVar["FormatStyle"]
    MEDIUM: ClassVar["FormatStyle"]
    SHORT: ClassVar["FormatStyle"]
    FULL: ClassVar["FormatStyle"]
    LONG: ClassVar["FormatStyle"]
    MEDIUM: ClassVar["FormatStyle"]
    SHORT: ClassVar["FormatStyle"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "FormatStyle": ...
