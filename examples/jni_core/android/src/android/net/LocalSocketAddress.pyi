from typing import Any, ClassVar, overload

class LocalSocketAddress:
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self, p0: str, p1: Any) -> None: ...
    def getNamespace(self) -> Any: ...
    def getName(self) -> str: ...

    class Namespace:
        ABSTRACT: ClassVar["Namespace"]
        RESERVED: ClassVar["Namespace"]
        FILESYSTEM: ClassVar["Namespace"]
        ABSTRACT: ClassVar[Any]
        RESERVED: ClassVar[Any]
        FILESYSTEM: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
