from typing import Any, ClassVar, overload

class StandardCopyOption:
    REPLACE_EXISTING: ClassVar["StandardCopyOption"]
    COPY_ATTRIBUTES: ClassVar["StandardCopyOption"]
    ATOMIC_MOVE: ClassVar["StandardCopyOption"]
    @staticmethod
    def values() -> list["StandardCopyOption"]: ...
    @staticmethod
    def valueOf(arg0: str) -> "StandardCopyOption": ...
