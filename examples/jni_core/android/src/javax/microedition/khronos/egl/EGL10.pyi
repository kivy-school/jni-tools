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
    def eglChooseConfig(self, p0: EGLDisplay, p1: Any, p2: Any, p3: int, p4: Any) -> bool: ...
    def eglCopyBuffers(self, p0: EGLDisplay, p1: EGLSurface, p2: Any) -> bool: ...
    def eglCreateContext(self, p0: EGLDisplay, p1: EGLConfig, p2: EGLContext, p3: Any) -> EGLContext: ...
    def eglCreatePbufferSurface(self, p0: EGLDisplay, p1: EGLConfig, p2: Any) -> EGLSurface: ...
    def eglCreatePixmapSurface(self, p0: EGLDisplay, p1: EGLConfig, p2: Any, p3: Any) -> EGLSurface: ...
    def eglCreateWindowSurface(self, p0: EGLDisplay, p1: EGLConfig, p2: Any, p3: Any) -> EGLSurface: ...
    def eglDestroyContext(self, p0: EGLDisplay, p1: EGLContext) -> bool: ...
    def eglDestroySurface(self, p0: EGLDisplay, p1: EGLSurface) -> bool: ...
    def eglGetConfigAttrib(self, p0: EGLDisplay, p1: EGLConfig, p2: int, p3: Any) -> bool: ...
    def eglGetConfigs(self, p0: EGLDisplay, p1: Any, p2: int, p3: Any) -> bool: ...
    def eglGetCurrentContext(self) -> EGLContext: ...
    def eglGetCurrentDisplay(self) -> EGLDisplay: ...
    def eglGetCurrentSurface(self, p0: int) -> EGLSurface: ...
    def eglGetDisplay(self, p0: Any) -> EGLDisplay: ...
    def eglGetError(self) -> int: ...
    def eglInitialize(self, p0: EGLDisplay, p1: Any) -> bool: ...
    def eglMakeCurrent(self, p0: EGLDisplay, p1: EGLSurface, p2: EGLSurface, p3: EGLContext) -> bool: ...
    def eglQueryContext(self, p0: EGLDisplay, p1: EGLContext, p2: int, p3: Any) -> bool: ...
    def eglQueryString(self, p0: EGLDisplay, p1: int) -> str: ...
    def eglQuerySurface(self, p0: EGLDisplay, p1: EGLSurface, p2: int, p3: Any) -> bool: ...
    def eglSwapBuffers(self, p0: EGLDisplay, p1: EGLSurface) -> bool: ...
    def eglTerminate(self, p0: EGLDisplay) -> bool: ...
    def eglWaitGL(self) -> bool: ...
    def eglWaitNative(self, p0: int, p1: Any) -> bool: ...
