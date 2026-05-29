from typing import Any, ClassVar, overload
from android.graphics.Path import Path

class PathDashPathEffect:
    def __init__(self, arg0: Path, arg1: float, arg2: float, arg3: "Style") -> None: ...

    class Style:
        TRANSLATE: ClassVar["Style"]
        ROTATE: ClassVar["Style"]
        MORPH: ClassVar["Style"]
        @staticmethod
        def values() -> list["Style"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "Style": ...
