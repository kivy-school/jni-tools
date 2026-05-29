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
    def wrap(p0: EGL, p1: int, p2: Writer) -> EGL: ...
    @overload
    @staticmethod
    def wrap(p0: GL, p1: int, p2: Writer) -> GL: ...
