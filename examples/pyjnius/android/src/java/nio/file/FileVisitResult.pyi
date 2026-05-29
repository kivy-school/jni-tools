from typing import Any, ClassVar, overload

class FileVisitResult:
    CONTINUE: ClassVar["FileVisitResult"]
    TERMINATE: ClassVar["FileVisitResult"]
    SKIP_SUBTREE: ClassVar["FileVisitResult"]
    SKIP_SIBLINGS: ClassVar["FileVisitResult"]
    CONTINUE: ClassVar["FileVisitResult"]
    TERMINATE: ClassVar["FileVisitResult"]
    SKIP_SUBTREE: ClassVar["FileVisitResult"]
    SKIP_SIBLINGS: ClassVar["FileVisitResult"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "FileVisitResult": ...
