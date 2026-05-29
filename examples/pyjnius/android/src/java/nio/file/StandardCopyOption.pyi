from typing import Any, ClassVar, overload

class StandardCopyOption:
    REPLACE_EXISTING: ClassVar["StandardCopyOption"]
    COPY_ATTRIBUTES: ClassVar["StandardCopyOption"]
    ATOMIC_MOVE: ClassVar["StandardCopyOption"]
    REPLACE_EXISTING: ClassVar["StandardCopyOption"]
    COPY_ATTRIBUTES: ClassVar["StandardCopyOption"]
    ATOMIC_MOVE: ClassVar["StandardCopyOption"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "StandardCopyOption": ...
