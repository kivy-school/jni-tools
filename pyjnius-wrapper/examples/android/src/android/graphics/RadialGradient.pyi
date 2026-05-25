from typing import Any, ClassVar, overload

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

class RadialGradient:
    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: list[int], arg4: list[float], arg5: TileMode) -> None: ...
    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: list[int], arg4: list[float], arg5: TileMode) -> None: ...
    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: list[int], arg7: list[float], arg8: TileMode) -> None: ...
    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: TileMode) -> None: ...
    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: TileMode) -> None: ...
