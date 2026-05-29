from typing import Any, ClassVar, overload

class LocalSocketAddress:
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self, p0: str, p1: Any) -> None: ...
    def getName(self) -> str: ...
    def getNamespace(self) -> Any: ...

    class Namespace:
        ABSTRACT: ClassVar["Namespace"]
        FILESYSTEM: ClassVar["Namespace"]
        RESERVED: ClassVar["Namespace"]
        ABSTRACT: ClassVar[Any]
        FILESYSTEM: ClassVar[Any]
        RESERVED: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
