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
    def eglGetError() -> int: ...
    @staticmethod
    def eglGetDisplay(arg0: int) -> EGLDisplay: ...
    @staticmethod
    def eglInitialize(arg0: EGLDisplay, arg1: list[int], arg2: int, arg3: list[int], arg4: int) -> bool: ...
    @staticmethod
    def eglTerminate(arg0: EGLDisplay) -> bool: ...
    @staticmethod
    def eglQueryString(arg0: EGLDisplay, arg1: int) -> str: ...
    @staticmethod
    def eglGetConfigs(arg0: EGLDisplay, arg1: list[EGLConfig], arg2: int, arg3: int, arg4: list[int], arg5: int) -> bool: ...
    @staticmethod
    def eglChooseConfig(arg0: EGLDisplay, arg1: list[int], arg2: int, arg3: list[EGLConfig], arg4: int, arg5: int, arg6: list[int], arg7: int) -> bool: ...
    @staticmethod
    def eglGetConfigAttrib(arg0: EGLDisplay, arg1: EGLConfig, arg2: int, arg3: list[int], arg4: int) -> bool: ...
    @staticmethod
    def eglCreateWindowSurface(arg0: EGLDisplay, arg1: EGLConfig, arg2: Any, arg3: list[int], arg4: int) -> EGLSurface: ...
    @staticmethod
    def eglCreatePbufferSurface(arg0: EGLDisplay, arg1: EGLConfig, arg2: list[int], arg3: int) -> EGLSurface: ...
    @staticmethod
    def eglCreatePixmapSurface(arg0: EGLDisplay, arg1: EGLConfig, arg2: int, arg3: list[int], arg4: int) -> EGLSurface: ...
    @staticmethod
    def eglDestroySurface(arg0: EGLDisplay, arg1: EGLSurface) -> bool: ...
    @staticmethod
    def eglQuerySurface(arg0: EGLDisplay, arg1: EGLSurface, arg2: int, arg3: list[int], arg4: int) -> bool: ...
    @staticmethod
    def eglBindAPI(arg0: int) -> bool: ...
    @staticmethod
    def eglQueryAPI() -> int: ...
    @staticmethod
    def eglWaitClient() -> bool: ...
    @staticmethod
    def eglReleaseThread() -> bool: ...
    @staticmethod
    def eglCreatePbufferFromClientBuffer(arg0: EGLDisplay, arg1: int, arg2: int, arg3: EGLConfig, arg4: list[int], arg5: int) -> EGLSurface: ...
    @staticmethod
    def eglSurfaceAttrib(arg0: EGLDisplay, arg1: EGLSurface, arg2: int, arg3: int) -> bool: ...
    @staticmethod
    def eglBindTexImage(arg0: EGLDisplay, arg1: EGLSurface, arg2: int) -> bool: ...
    @staticmethod
    def eglReleaseTexImage(arg0: EGLDisplay, arg1: EGLSurface, arg2: int) -> bool: ...
    @staticmethod
    def eglSwapInterval(arg0: EGLDisplay, arg1: int) -> bool: ...
    @staticmethod
    def eglCreateContext(arg0: EGLDisplay, arg1: EGLConfig, arg2: EGLContext, arg3: list[int], arg4: int) -> EGLContext: ...
    @staticmethod
    def eglDestroyContext(arg0: EGLDisplay, arg1: EGLContext) -> bool: ...
    @staticmethod
    def eglMakeCurrent(arg0: EGLDisplay, arg1: EGLSurface, arg2: EGLSurface, arg3: EGLContext) -> bool: ...
    @staticmethod
    def eglGetCurrentContext() -> EGLContext: ...
    @staticmethod
    def eglGetCurrentSurface(arg0: int) -> EGLSurface: ...
    @staticmethod
    def eglGetCurrentDisplay() -> EGLDisplay: ...
    @staticmethod
    def eglQueryContext(arg0: EGLDisplay, arg1: EGLContext, arg2: int, arg3: list[int], arg4: int) -> bool: ...
    @staticmethod
    def eglWaitGL() -> bool: ...
    @staticmethod
    def eglWaitNative(arg0: int) -> bool: ...
    @staticmethod
    def eglSwapBuffers(arg0: EGLDisplay, arg1: EGLSurface) -> bool: ...
    @staticmethod
    def eglCopyBuffers(arg0: EGLDisplay, arg1: EGLSurface, arg2: int) -> bool: ...
