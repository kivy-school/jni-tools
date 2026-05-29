from typing import Any, ClassVar, overload
from android.graphics.Bitmap import Bitmap
from android.graphics.BlendMode import BlendMode
from android.graphics.ColorFilter import ColorFilter
from android.graphics.Rect import Rect
from android.graphics.RuntimeShader import RuntimeShader
from android.graphics.Shader import Shader

class RenderEffect:
    @overload
    @staticmethod
    def createBitmapEffect(p0: Bitmap, p1: Rect, p2: Rect) -> "RenderEffect": ...
    @overload
    @staticmethod
    def createBitmapEffect(p0: Bitmap) -> "RenderEffect": ...
    @staticmethod
    def createBlendModeEffect(p0: "RenderEffect", p1: "RenderEffect", p2: BlendMode) -> "RenderEffect": ...
    @overload
    @staticmethod
    def createBlurEffect(p0: float, p1: float, p2: "RenderEffect", p3: Any) -> "RenderEffect": ...
    @overload
    @staticmethod
    def createBlurEffect(p0: float, p1: float, p2: Any) -> "RenderEffect": ...
    @staticmethod
    def createChainEffect(p0: "RenderEffect", p1: "RenderEffect") -> "RenderEffect": ...
    @overload
    @staticmethod
    def createColorFilterEffect(p0: ColorFilter, p1: "RenderEffect") -> "RenderEffect": ...
    @overload
    @staticmethod
    def createColorFilterEffect(p0: ColorFilter) -> "RenderEffect": ...
    @overload
    @staticmethod
    def createOffsetEffect(p0: float, p1: float) -> "RenderEffect": ...
    @overload
    @staticmethod
    def createOffsetEffect(p0: float, p1: float, p2: "RenderEffect") -> "RenderEffect": ...
    @staticmethod
    def createRuntimeShaderEffect(p0: RuntimeShader, p1: str) -> "RenderEffect": ...
    @staticmethod
    def createShaderEffect(p0: Shader) -> "RenderEffect": ...
