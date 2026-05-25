from typing import Any, ClassVar, overload

class BlurMaskFilter:
    def __init__(self, arg0: float, arg1: "Blur") -> None: ...

    class Blur:
        NORMAL: ClassVar["Blur"]
        SOLID: ClassVar["Blur"]
        OUTER: ClassVar["Blur"]
        INNER: ClassVar["Blur"]
        @staticmethod
        def values() -> list["Blur"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "Blur": ...
