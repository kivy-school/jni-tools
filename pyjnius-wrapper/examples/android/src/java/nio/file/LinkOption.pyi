from typing import Any, ClassVar, overload

class LinkOption:
    NOFOLLOW_LINKS: ClassVar["LinkOption"]
    @staticmethod
    def values() -> list["LinkOption"]: ...
    @staticmethod
    def valueOf(arg0: str) -> "LinkOption": ...
