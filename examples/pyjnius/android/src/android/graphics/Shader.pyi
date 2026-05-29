from typing import Any, ClassVar, overload
from android.graphics.Matrix import Matrix

class Shader:
    def __init__(self) -> None: ...
    def getLocalMatrix(self, arg0: Matrix) -> bool: ...
    def setLocalMatrix(self, arg0: Matrix) -> None: ...

    class TileMode:
        CLAMP: ClassVar["TileMode"]
        REPEAT: ClassVar["TileMode"]
        MIRROR: ClassVar["TileMode"]
        DECAL: ClassVar["TileMode"]
        @staticmethod
        def values() -> list["TileMode"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "TileMode": ...
