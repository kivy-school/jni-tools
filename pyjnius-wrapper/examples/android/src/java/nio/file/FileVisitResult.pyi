from typing import Any, ClassVar, overload

class FileVisitResult:
    CONTINUE: ClassVar["FileVisitResult"]
    TERMINATE: ClassVar["FileVisitResult"]
    SKIP_SUBTREE: ClassVar["FileVisitResult"]
    SKIP_SIBLINGS: ClassVar["FileVisitResult"]
    @staticmethod
    def values() -> list["FileVisitResult"]: ...
    @staticmethod
    def valueOf(arg0: str) -> "FileVisitResult": ...
