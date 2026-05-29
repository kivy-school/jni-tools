from typing import Any, ClassVar, overload
from android.opengl.EGLConfig import EGLConfig
from android.opengl.EGLContext import EGLContext
from android.opengl.EGLDisplay import EGLDisplay
from android.opengl.EGLSurface import EGLSurface

class EGL14:
    EGL_ALPHA_MASK_SIZE: ClassVar[int]
    EGL_ALPHA_SIZE: ClassVar[int]
    EGL_BACK_BUFFER: ClassVar[int]
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
    EGL_BIND_TO_TEXTURE_RGB: ClassVar[int]
    EGL_BIND_TO_TEXTURE_RGBA: ClassVar[int]
    EGL_BLUE_SIZE: ClassVar[int]
    EGL_BUFFER_DESTROYED: ClassVar[int]
    EGL_BUFFER_PRESERVED: ClassVar[int]
    EGL_BUFFER_SIZE: ClassVar[int]
    EGL_CLIENT_APIS: ClassVar[int]
    EGL_COLOR_BUFFER_TYPE: ClassVar[int]
    EGL_CONFIG_CAVEAT: ClassVar[int]
    EGL_CONFIG_ID: ClassVar[int]
    EGL_CONFORMANT: ClassVar[int]
    EGL_CONTEXT_CLIENT_TYPE: ClassVar[int]
    EGL_CONTEXT_CLIENT_VERSION: ClassVar[int]
    EGL_CONTEXT_LOST: ClassVar[int]
    EGL_CORE_NATIVE_ENGINE: ClassVar[int]
    EGL_DEFAULT_DISPLAY: ClassVar[int]
    EGL_DEPTH_SIZE: ClassVar[int]
    EGL_DISPLAY_SCALING: ClassVar[int]
    EGL_DRAW: ClassVar[int]
    EGL_EXTENSIONS: ClassVar[int]
    EGL_FALSE: ClassVar[int]
    EGL_GREEN_SIZE: ClassVar[int]
    EGL_HEIGHT: ClassVar[int]
    EGL_HORIZONTAL_RESOLUTION: ClassVar[int]
    EGL_LARGEST_PBUFFER: ClassVar[int]
    EGL_LEVEL: ClassVar[int]
    EGL_LUMINANCE_BUFFER: ClassVar[int]
    EGL_LUMINANCE_SIZE: ClassVar[int]
    EGL_MATCH_NATIVE_PIXMAP: ClassVar[int]
    EGL_MAX_PBUFFER_HEIGHT: ClassVar[int]
    EGL_MAX_PBUFFER_PIXELS: ClassVar[int]
    EGL_MAX_PBUFFER_WIDTH: ClassVar[int]
    EGL_MAX_SWAP_INTERVAL: ClassVar[int]
    EGL_MIN_SWAP_INTERVAL: ClassVar[int]
    EGL_MIPMAP_LEVEL: ClassVar[int]
    EGL_MIPMAP_TEXTURE: ClassVar[int]
    EGL_MULTISAMPLE_RESOLVE: ClassVar[int]
    EGL_MULTISAMPLE_RESOLVE_BOX: ClassVar[int]
    EGL_MULTISAMPLE_RESOLVE_BOX_BIT: ClassVar[int]
    EGL_MULTISAMPLE_RESOLVE_DEFAULT: ClassVar[int]
    EGL_NATIVE_RENDERABLE: ClassVar[int]
    EGL_NATIVE_VISUAL_ID: ClassVar[int]
    EGL_NATIVE_VISUAL_TYPE: ClassVar[int]
    EGL_NONE: ClassVar[int]
    EGL_NON_CONFORMANT_CONFIG: ClassVar[int]
    EGL_NOT_INITIALIZED: ClassVar[int]
    EGL_NO_CONTEXT: ClassVar[EGLContext]
    EGL_NO_DISPLAY: ClassVar[EGLDisplay]
    EGL_NO_SURFACE: ClassVar[EGLSurface]
    EGL_NO_TEXTURE: ClassVar[int]
    EGL_OPENGL_API: ClassVar[int]
    EGL_OPENGL_BIT: ClassVar[int]
    EGL_OPENGL_ES2_BIT: ClassVar[int]
    EGL_OPENGL_ES_API: ClassVar[int]
    EGL_OPENGL_ES_BIT: ClassVar[int]
    EGL_OPENVG_API: ClassVar[int]
    EGL_OPENVG_BIT: ClassVar[int]
    EGL_OPENVG_IMAGE: ClassVar[int]
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
    EGL_SWAP_BEHAVIOR: ClassVar[int]
    EGL_SWAP_BEHAVIOR_PRESERVED_BIT: ClassVar[int]
    EGL_TEXTURE_2D: ClassVar[int]
    EGL_TEXTURE_FORMAT: ClassVar[int]
    EGL_TEXTURE_RGB: ClassVar[int]
    EGL_TEXTURE_RGBA: ClassVar[int]
    EGL_TEXTURE_TARGET: ClassVar[int]
    EGL_TRANSPARENT_BLUE_VALUE: ClassVar[int]
    EGL_TRANSPARENT_GREEN_VALUE: ClassVar[int]
    EGL_TRANSPARENT_RED_VALUE: ClassVar[int]
    EGL_TRANSPARENT_RGB: ClassVar[int]
    EGL_TRANSPARENT_TYPE: ClassVar[int]
    EGL_TRUE: ClassVar[int]
    EGL_VENDOR: ClassVar[int]
    EGL_VERSION: ClassVar[int]
    EGL_VERTICAL_RESOLUTION: ClassVar[int]
    EGL_VG_ALPHA_FORMAT: ClassVar[int]
    EGL_VG_ALPHA_FORMAT_NONPRE: ClassVar[int]
    EGL_VG_ALPHA_FORMAT_PRE: ClassVar[int]
    EGL_VG_ALPHA_FORMAT_PRE_BIT: ClassVar[int]
    EGL_VG_COLORSPACE: ClassVar[int]
    EGL_VG_COLORSPACE_LINEAR: ClassVar[int]
    EGL_VG_COLORSPACE_LINEAR_BIT: ClassVar[int]
    EGL_VG_COLORSPACE_sRGB: ClassVar[int]
    EGL_WIDTH: ClassVar[int]
    EGL_WINDOW_BIT: ClassVar[int]
    def __init__(self) -> None: ...
    @staticmethod
    def eglChooseConfig(p0: EGLDisplay, p1: Any, p2: int, p3: Any, p4: int, p5: int, p6: Any, p7: int) -> bool: ...
    @staticmethod
    def eglCopyBuffers(p0: EGLDisplay, p1: EGLSurface, p2: int) -> bool: ...
    @staticmethod
    def eglCreateContext(p0: EGLDisplay, p1: EGLConfig, p2: EGLContext, p3: Any, p4: int) -> EGLContext: ...
    @staticmethod
    def eglCreatePbufferSurface(p0: EGLDisplay, p1: EGLConfig, p2: Any, p3: int) -> EGLSurface: ...
    @staticmethod
    def eglCreatePixmapSurface(p0: EGLDisplay, p1: EGLConfig, p2: int, p3: Any, p4: int) -> EGLSurface: ...
    @staticmethod
    def eglCreateWindowSurface(p0: EGLDisplay, p1: EGLConfig, p2: Any, p3: Any, p4: int) -> EGLSurface: ...
    @staticmethod
    def eglDestroyContext(p0: EGLDisplay, p1: EGLContext) -> bool: ...
    @staticmethod
    def eglDestroySurface(p0: EGLDisplay, p1: EGLSurface) -> bool: ...
    @staticmethod
    def eglGetConfigAttrib(p0: EGLDisplay, p1: EGLConfig, p2: int, p3: Any, p4: int) -> bool: ...
    @staticmethod
    def eglGetConfigs(p0: EGLDisplay, p1: Any, p2: int, p3: int, p4: Any, p5: int) -> bool: ...
    @staticmethod
    def eglGetCurrentContext() -> EGLContext: ...
    @staticmethod
    def eglGetCurrentDisplay() -> EGLDisplay: ...
    @staticmethod
    def eglGetCurrentSurface(p0: int) -> EGLSurface: ...
    @staticmethod
    def eglGetDisplay(p0: int) -> EGLDisplay: ...
    @staticmethod
    def eglGetError() -> int: ...
    @staticmethod
    def eglInitialize(p0: EGLDisplay, p1: Any, p2: int, p3: Any, p4: int) -> bool: ...
    @staticmethod
    def eglMakeCurrent(p0: EGLDisplay, p1: EGLSurface, p2: EGLSurface, p3: EGLContext) -> bool: ...
    @staticmethod
    def eglQueryContext(p0: EGLDisplay, p1: EGLContext, p2: int, p3: Any, p4: int) -> bool: ...
    @staticmethod
    def eglQueryString(p0: EGLDisplay, p1: int) -> str: ...
    @staticmethod
    def eglQuerySurface(p0: EGLDisplay, p1: EGLSurface, p2: int, p3: Any, p4: int) -> bool: ...
    @staticmethod
    def eglSwapBuffers(p0: EGLDisplay, p1: EGLSurface) -> bool: ...
    @staticmethod
    def eglTerminate(p0: EGLDisplay) -> bool: ...
    @staticmethod
    def eglWaitGL() -> bool: ...
    @staticmethod
    def eglWaitNative(p0: int) -> bool: ...
    @staticmethod
    def eglBindAPI(p0: int) -> bool: ...
    @staticmethod
    def eglBindTexImage(p0: EGLDisplay, p1: EGLSurface, p2: int) -> bool: ...
    @staticmethod
    def eglCreatePbufferFromClientBuffer(p0: EGLDisplay, p1: int, p2: int, p3: EGLConfig, p4: Any, p5: int) -> EGLSurface: ...
    @staticmethod
    def eglQueryAPI() -> int: ...
    @staticmethod
    def eglReleaseTexImage(p0: EGLDisplay, p1: EGLSurface, p2: int) -> bool: ...
    @staticmethod
    def eglReleaseThread() -> bool: ...
    @staticmethod
    def eglSurfaceAttrib(p0: EGLDisplay, p1: EGLSurface, p2: int, p3: int) -> bool: ...
    @staticmethod
    def eglSwapInterval(p0: EGLDisplay, p1: int) -> bool: ...
    @staticmethod
    def eglWaitClient() -> bool: ...
