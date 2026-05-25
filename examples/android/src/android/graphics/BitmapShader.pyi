from typing import Any, ClassVar, overload
from android.graphics.Bitmap import Bitmap
from android.graphics.Gainmap import Gainmap

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class TileMode:
    """Forward declaration for ``android.graphics.Shader.TileMode``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.graphics.Shader.TileMode')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/graphics/Shader/TileMode
    """
    ...

class BitmapShader:
    FILTER_MODE_DEFAULT: ClassVar[int]
    FILTER_MODE_LINEAR: ClassVar[int]
    FILTER_MODE_NEAREST: ClassVar[int]
    def __init__(self, arg0: Bitmap, arg1: TileMode, arg2: TileMode) -> None: ...
    def getFilterMode(self) -> int: ...
    def setFilterMode(self, arg0: int) -> None: ...
    def setMaxAnisotropy(self, arg0: int) -> None: ...
    def setOverrideGainmap(self, arg0: Gainmap) -> None: ...
    def getMaxAnisotropy(self) -> int: ...
