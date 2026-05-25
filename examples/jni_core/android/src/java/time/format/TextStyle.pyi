from typing import Any, ClassVar, overload

class TextStyle:
    FULL: ClassVar["TextStyle"]
    FULL_STANDALONE: ClassVar["TextStyle"]
    SHORT: ClassVar["TextStyle"]
    SHORT_STANDALONE: ClassVar["TextStyle"]
    NARROW: ClassVar["TextStyle"]
    NARROW_STANDALONE: ClassVar["TextStyle"]
    FULL: ClassVar["TextStyle"]
    FULL_STANDALONE: ClassVar["TextStyle"]
    SHORT: ClassVar["TextStyle"]
    SHORT_STANDALONE: ClassVar["TextStyle"]
    NARROW: ClassVar["TextStyle"]
    NARROW_STANDALONE: ClassVar["TextStyle"]
    def isStandalone(self) -> bool: ...
    def asStandalone(self) -> "TextStyle": ...
    def asNormal(self) -> "TextStyle": ...
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "TextStyle": ...
