from typing import Any, ClassVar, overload
from android.graphics.BlendMode import BlendMode
from android.graphics.Shader import Shader
from android.graphics.Xfermode import Xfermode

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Mode:
    """Forward declaration for ``android.graphics.PorterDuff.Mode``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.graphics.PorterDuff.Mode')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/graphics/PorterDuff/Mode
    """
    ...

class ComposeShader:
    @overload
    def __init__(self, arg0: Shader, arg1: Shader, arg2: Xfermode) -> None: ...
    @overload
    def __init__(self, arg0: Shader, arg1: Shader, arg2: Mode) -> None: ...
    @overload
    def __init__(self, arg0: Shader, arg1: Shader, arg2: BlendMode) -> None: ...
