from typing import Any, ClassVar, overload
from android.graphics.Matrix import Matrix

class Shader:
    def __init__(self) -> None: ...
    def getLocalMatrix(self, p0: Matrix) -> bool: ...
    def setLocalMatrix(self, p0: Matrix) -> None: ...

    class TileMode:
        CLAMP: ClassVar["TileMode"]
        DECAL: ClassVar["TileMode"]
        MIRROR: ClassVar["TileMode"]
        REPEAT: ClassVar["TileMode"]
        CLAMP: ClassVar[Any]
        DECAL: ClassVar[Any]
        MIRROR: ClassVar[Any]
        REPEAT: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
