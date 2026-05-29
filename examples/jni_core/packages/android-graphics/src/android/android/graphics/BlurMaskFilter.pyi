from typing import Any, ClassVar, overload

class BlurMaskFilter:
    def __init__(self, p0: float, p1: Any) -> None: ...

    class Blur:
        NORMAL: ClassVar["Blur"]
        SOLID: ClassVar["Blur"]
        OUTER: ClassVar["Blur"]
        INNER: ClassVar["Blur"]
        NORMAL: ClassVar[Any]
        SOLID: ClassVar[Any]
        OUTER: ClassVar[Any]
        INNER: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
