from typing import Any, ClassVar, overload

class BlurMaskFilter:
    def __init__(self, p0: float, p1: Any) -> None: ...

    class Blur:
        INNER: ClassVar["Blur"]
        NORMAL: ClassVar["Blur"]
        OUTER: ClassVar["Blur"]
        SOLID: ClassVar["Blur"]
        INNER: ClassVar[Any]
        NORMAL: ClassVar[Any]
        OUTER: ClassVar[Any]
        SOLID: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
