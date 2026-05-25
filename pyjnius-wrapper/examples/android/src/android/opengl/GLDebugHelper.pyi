from typing import Any, ClassVar, overload
from java.io.Writer import Writer
from javax.microedition.khronos.egl.EGL import EGL
from javax.microedition.khronos.opengles.GL import GL

class GLDebugHelper:
    CONFIG_CHECK_GL_ERROR: ClassVar[int]
    CONFIG_CHECK_THREAD: ClassVar[int]
    CONFIG_LOG_ARGUMENT_NAMES: ClassVar[int]
    ERROR_WRONG_THREAD: ClassVar[int]
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def wrap(arg0: GL, arg1: int, arg2: Writer) -> GL: ...
    @overload
    @staticmethod
    def wrap(arg0: EGL, arg1: int, arg2: Writer) -> EGL: ...
