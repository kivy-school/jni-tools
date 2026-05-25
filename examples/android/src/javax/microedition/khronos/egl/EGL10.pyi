from typing import Any, ClassVar, overload
from javax.microedition.khronos.egl.EGLConfig import EGLConfig
from javax.microedition.khronos.egl.EGLContext import EGLContext
from javax.microedition.khronos.egl.EGLDisplay import EGLDisplay
from javax.microedition.khronos.egl.EGLSurface import EGLSurface

class EGL10:
    EGL_ALPHA_FORMAT: ClassVar[int]
    EGL_ALPHA_MASK_SIZE: ClassVar[int]
    EGL_ALPHA_SIZE: ClassVar[int]
    EGL_BAD_ACCESS: ClassVar[int]
    EGL_BAD_ALLOC: ClassVar[int]
    EGL_BAD_ATTRIBUTE: ClassVar[int]
    EGL_BAD_CONFIG: ClassVar[int]
    EGL_BAD_CONTEXT: ClassVar[int]
    EGL_BAD_CURRENT_SURFACE: ClassVar[int]
    EGL_BAD_DISPLAY: ClassVar[int]
    EGL_BAD_MATCH: ClassVar[int]
    EGL_BAD_NATIVE_PIXMAP: ClassVar[int]
    EGL_BAD_NATIVE_WINDOW: ClassVar[int]
    EGL_BAD_PARAMETER: ClassVar[int]
    EGL_BAD_SURFACE: ClassVar[int]
    EGL_BLUE_SIZE: ClassVar[int]
    EGL_BUFFER_SIZE: ClassVar[int]
    EGL_COLORSPACE: ClassVar[int]
    EGL_COLOR_BUFFER_TYPE: ClassVar[int]
    EGL_CONFIG_CAVEAT: ClassVar[int]
    EGL_CONFIG_ID: ClassVar[int]
    EGL_CORE_NATIVE_ENGINE: ClassVar[int]
    EGL_DEFAULT_DISPLAY: ClassVar[Any]
    EGL_DEPTH_SIZE: ClassVar[int]
    EGL_DONT_CARE: ClassVar[int]
    EGL_DRAW: ClassVar[int]
    EGL_EXTENSIONS: ClassVar[int]
    EGL_GREEN_SIZE: ClassVar[int]
    EGL_HEIGHT: ClassVar[int]
    EGL_HORIZONTAL_RESOLUTION: ClassVar[int]
    EGL_LARGEST_PBUFFER: ClassVar[int]
    EGL_LEVEL: ClassVar[int]
    EGL_LUMINANCE_BUFFER: ClassVar[int]
    EGL_LUMINANCE_SIZE: ClassVar[int]
    EGL_MAX_PBUFFER_HEIGHT: ClassVar[int]
    EGL_MAX_PBUFFER_PIXELS: ClassVar[int]
    EGL_MAX_PBUFFER_WIDTH: ClassVar[int]
    EGL_NATIVE_RENDERABLE: ClassVar[int]
    EGL_NATIVE_VISUAL_ID: ClassVar[int]
    EGL_NATIVE_VISUAL_TYPE: ClassVar[int]
    EGL_NONE: ClassVar[int]
    EGL_NON_CONFORMANT_CONFIG: ClassVar[int]
    EGL_NOT_INITIALIZED: ClassVar[int]
    EGL_NO_CONTEXT: ClassVar[EGLContext]
    EGL_NO_DISPLAY: ClassVar[EGLDisplay]
    EGL_NO_SURFACE: ClassVar[EGLSurface]
    EGL_PBUFFER_BIT: ClassVar[int]
    EGL_PIXEL_ASPECT_RATIO: ClassVar[int]
    EGL_PIXMAP_BIT: ClassVar[int]
    EGL_READ: ClassVar[int]
    EGL_RED_SIZE: ClassVar[int]
    EGL_RENDERABLE_TYPE: ClassVar[int]
    EGL_RENDER_BUFFER: ClassVar[int]
    EGL_RGB_BUFFER: ClassVar[int]
    EGL_SAMPLES: ClassVar[int]
    EGL_SAMPLE_BUFFERS: ClassVar[int]
    EGL_SINGLE_BUFFER: ClassVar[int]
    EGL_SLOW_CONFIG: ClassVar[int]
    EGL_STENCIL_SIZE: ClassVar[int]
    EGL_SUCCESS: ClassVar[int]
    EGL_SURFACE_TYPE: ClassVar[int]
    EGL_TRANSPARENT_BLUE_VALUE: ClassVar[int]
    EGL_TRANSPARENT_GREEN_VALUE: ClassVar[int]
    EGL_TRANSPARENT_RED_VALUE: ClassVar[int]
    EGL_TRANSPARENT_RGB: ClassVar[int]
    EGL_TRANSPARENT_TYPE: ClassVar[int]
    EGL_VENDOR: ClassVar[int]
    EGL_VERSION: ClassVar[int]
    EGL_VERTICAL_RESOLUTION: ClassVar[int]
    EGL_WIDTH: ClassVar[int]
    EGL_WINDOW_BIT: ClassVar[int]
    def eglChooseConfig(self, arg0: EGLDisplay, arg1: list[int], arg2: list[EGLConfig], arg3: int, arg4: list[int]) -> bool: ...
    def eglCopyBuffers(self, arg0: EGLDisplay, arg1: EGLSurface, arg2: Any) -> bool: ...
    def eglCreateContext(self, arg0: EGLDisplay, arg1: EGLConfig, arg2: EGLContext, arg3: list[int]) -> EGLContext: ...
    def eglCreatePbufferSurface(self, arg0: EGLDisplay, arg1: EGLConfig, arg2: list[int]) -> EGLSurface: ...
    def eglCreatePixmapSurface(self, arg0: EGLDisplay, arg1: EGLConfig, arg2: Any, arg3: list[int]) -> EGLSurface: ...
    def eglCreateWindowSurface(self, arg0: EGLDisplay, arg1: EGLConfig, arg2: Any, arg3: list[int]) -> EGLSurface: ...
    def eglDestroyContext(self, arg0: EGLDisplay, arg1: EGLContext) -> bool: ...
    def eglDestroySurface(self, arg0: EGLDisplay, arg1: EGLSurface) -> bool: ...
    def eglGetConfigAttrib(self, arg0: EGLDisplay, arg1: EGLConfig, arg2: int, arg3: list[int]) -> bool: ...
    def eglGetConfigs(self, arg0: EGLDisplay, arg1: list[EGLConfig], arg2: int, arg3: list[int]) -> bool: ...
    def eglGetCurrentContext(self) -> EGLContext: ...
    def eglGetCurrentDisplay(self) -> EGLDisplay: ...
    def eglGetCurrentSurface(self, arg0: int) -> EGLSurface: ...
    def eglGetDisplay(self, arg0: Any) -> EGLDisplay: ...
    def eglGetError(self) -> int: ...
    def eglInitialize(self, arg0: EGLDisplay, arg1: list[int]) -> bool: ...
    def eglMakeCurrent(self, arg0: EGLDisplay, arg1: EGLSurface, arg2: EGLSurface, arg3: EGLContext) -> bool: ...
    def eglQueryContext(self, arg0: EGLDisplay, arg1: EGLContext, arg2: int, arg3: list[int]) -> bool: ...
    def eglQueryString(self, arg0: EGLDisplay, arg1: int) -> str: ...
    def eglQuerySurface(self, arg0: EGLDisplay, arg1: EGLSurface, arg2: int, arg3: list[int]) -> bool: ...
    def eglSwapBuffers(self, arg0: EGLDisplay, arg1: EGLSurface) -> bool: ...
    def eglTerminate(self, arg0: EGLDisplay) -> bool: ...
    def eglWaitGL(self) -> bool: ...
    def eglWaitNative(self, arg0: int, arg1: Any) -> bool: ...
