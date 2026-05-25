from typing import Any, ClassVar, overload
from android.graphics.BlendMode import BlendMode
from android.graphics.Shader import Shader
from android.graphics.Xfermode import Xfermode

class ComposeShader:
    @overload
    def __init__(self, p0: Shader, p1: Shader, p2: Xfermode) -> None: ...
    @overload
    def __init__(self, p0: Shader, p1: Shader, p2: Any) -> None: ...
    @overload
    def __init__(self, p0: Shader, p1: Shader, p2: BlendMode) -> None: ...
