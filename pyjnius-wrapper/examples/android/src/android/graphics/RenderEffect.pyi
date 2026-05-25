from typing import Any, ClassVar, overload
from android.graphics.Bitmap import Bitmap
from android.graphics.BlendMode import BlendMode
from android.graphics.ColorFilter import ColorFilter
from android.graphics.Rect import Rect
from android.graphics.RuntimeShader import RuntimeShader
from android.graphics.Shader import Shader

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

class RenderEffect:
    @overload
    @staticmethod
    def createOffsetEffect(arg0: float, arg1: float) -> "RenderEffect": ...
    @overload
    @staticmethod
    def createOffsetEffect(arg0: float, arg1: float, arg2: "RenderEffect") -> "RenderEffect": ...
    @overload
    @staticmethod
    def createBlurEffect(arg0: float, arg1: float, arg2: "RenderEffect", arg3: TileMode) -> "RenderEffect": ...
    @overload
    @staticmethod
    def createBlurEffect(arg0: float, arg1: float, arg2: TileMode) -> "RenderEffect": ...
    @overload
    @staticmethod
    def createBitmapEffect(arg0: Bitmap) -> "RenderEffect": ...
    @overload
    @staticmethod
    def createBitmapEffect(arg0: Bitmap, arg1: Rect, arg2: Rect) -> "RenderEffect": ...
    @overload
    @staticmethod
    def createColorFilterEffect(arg0: ColorFilter, arg1: "RenderEffect") -> "RenderEffect": ...
    @overload
    @staticmethod
    def createColorFilterEffect(arg0: ColorFilter) -> "RenderEffect": ...
    @staticmethod
    def createBlendModeEffect(arg0: "RenderEffect", arg1: "RenderEffect", arg2: BlendMode) -> "RenderEffect": ...
    @staticmethod
    def createChainEffect(arg0: "RenderEffect", arg1: "RenderEffect") -> "RenderEffect": ...
    @staticmethod
    def createShaderEffect(arg0: Shader) -> "RenderEffect": ...
    @staticmethod
    def createRuntimeShaderEffect(arg0: RuntimeShader, arg1: str) -> "RenderEffect": ...
