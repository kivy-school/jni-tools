from typing import Any, ClassVar, overload
from android.graphics.Path import Path

class PathDashPathEffect:
    def __init__(self, p0: Path, p1: float, p2: float, p3: Any) -> None: ...

    class Style:
        TRANSLATE: ClassVar["Style"]
        ROTATE: ClassVar["Style"]
        MORPH: ClassVar["Style"]
        TRANSLATE: ClassVar[Any]
        ROTATE: ClassVar[Any]
        MORPH: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
