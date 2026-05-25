from typing import Any, ClassVar, overload

class FileVisitOption:
    FOLLOW_LINKS: ClassVar["FileVisitOption"]
    @staticmethod
    def values() -> list["FileVisitOption"]: ...
    @staticmethod
    def valueOf(arg0: str) -> "FileVisitOption": ...
