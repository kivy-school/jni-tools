from typing import Any, ClassVar, overload
from android.opengl.EGLConfig import EGLConfig
from android.opengl.EGLContext import EGLContext
from android.opengl.EGLDisplay import EGLDisplay
from android.opengl.EGLImage import EGLImage
from android.opengl.EGLSurface import EGLSurface
from android.opengl.EGLSync import EGLSync
from java.nio.Buffer import Buffer

class EGL15:
    EGL_CL_EVENT_HANDLE: ClassVar[int]
    EGL_CONDITION_SATISFIED: ClassVar[int]
    EGL_CONTEXT_MAJOR_VERSION: ClassVar[int]
    EGL_CONTEXT_MINOR_VERSION: ClassVar[int]
    EGL_CONTEXT_OPENGL_COMPATIBILITY_PROFILE_BIT: ClassVar[int]
    EGL_CONTEXT_OPENGL_CORE_PROFILE_BIT: ClassVar[int]
    EGL_CONTEXT_OPENGL_DEBUG: ClassVar[int]
    EGL_CONTEXT_OPENGL_FORWARD_COMPATIBLE: ClassVar[int]
    EGL_CONTEXT_OPENGL_PROFILE_MASK: ClassVar[int]
    EGL_CONTEXT_OPENGL_RESET_NOTIFICATION_STRATEGY: ClassVar[int]
    EGL_CONTEXT_OPENGL_ROBUST_ACCESS: ClassVar[int]
    EGL_FOREVER: ClassVar[int]
    EGL_GL_COLORSPACE: ClassVar[int]
    EGL_GL_COLORSPACE_LINEAR: ClassVar[int]
    EGL_GL_COLORSPACE_SRGB: ClassVar[int]
    EGL_GL_RENDERBUFFER: ClassVar[int]
    EGL_GL_TEXTURE_2D: ClassVar[int]
    EGL_GL_TEXTURE_3D: ClassVar[int]
    EGL_GL_TEXTURE_CUBE_MAP_NEGATIVE_X: ClassVar[int]
    EGL_GL_TEXTURE_CUBE_MAP_NEGATIVE_Y: ClassVar[int]
    EGL_GL_TEXTURE_CUBE_MAP_NEGATIVE_Z: ClassVar[int]
    EGL_GL_TEXTURE_CUBE_MAP_POSITIVE_X: ClassVar[int]
    EGL_GL_TEXTURE_CUBE_MAP_POSITIVE_Y: ClassVar[int]
    EGL_GL_TEXTURE_CUBE_MAP_POSITIVE_Z: ClassVar[int]
    EGL_GL_TEXTURE_LEVEL: ClassVar[int]
    EGL_GL_TEXTURE_ZOFFSET: ClassVar[int]
    EGL_IMAGE_PRESERVED: ClassVar[int]
    EGL_LOSE_CONTEXT_ON_RESET: ClassVar[int]
    EGL_NO_CONTEXT: ClassVar[EGLContext]
    EGL_NO_DISPLAY: ClassVar[EGLDisplay]
    EGL_NO_IMAGE: ClassVar[EGLImage]
    EGL_NO_RESET_NOTIFICATION: ClassVar[int]
    EGL_NO_SURFACE: ClassVar[EGLSurface]
    EGL_NO_SYNC: ClassVar[EGLSync]
    EGL_OPENGL_ES3_BIT: ClassVar[int]
    EGL_PLATFORM_ANDROID_KHR: ClassVar[int]
    EGL_SIGNALED: ClassVar[int]
    EGL_SYNC_CL_EVENT: ClassVar[int]
    EGL_SYNC_CL_EVENT_COMPLETE: ClassVar[int]
    EGL_SYNC_CONDITION: ClassVar[int]
    EGL_SYNC_FENCE: ClassVar[int]
    EGL_SYNC_FLUSH_COMMANDS_BIT: ClassVar[int]
    EGL_SYNC_PRIOR_COMMANDS_COMPLETE: ClassVar[int]
    EGL_SYNC_STATUS: ClassVar[int]
    EGL_SYNC_TYPE: ClassVar[int]
    EGL_TIMEOUT_EXPIRED: ClassVar[int]
    EGL_UNSIGNALED: ClassVar[int]
    @staticmethod
    def eglCreateSync(arg0: EGLDisplay, arg1: int, arg2: list[int], arg3: int) -> EGLSync: ...
    @staticmethod
    def eglGetSyncAttrib(arg0: EGLDisplay, arg1: EGLSync, arg2: int, arg3: list[int], arg4: int) -> bool: ...
    @staticmethod
    def eglDestroySync(arg0: EGLDisplay, arg1: EGLSync) -> bool: ...
    @staticmethod
    def eglClientWaitSync(arg0: EGLDisplay, arg1: EGLSync, arg2: int, arg3: int) -> int: ...
    @staticmethod
    def eglGetPlatformDisplay(arg0: int, arg1: int, arg2: list[int], arg3: int) -> EGLDisplay: ...
    @staticmethod
    def eglCreatePlatformWindowSurface(arg0: EGLDisplay, arg1: EGLConfig, arg2: Buffer, arg3: list[int], arg4: int) -> EGLSurface: ...
    @staticmethod
    def eglCreatePlatformPixmapSurface(arg0: EGLDisplay, arg1: EGLConfig, arg2: Buffer, arg3: list[int], arg4: int) -> EGLSurface: ...
    @staticmethod
    def eglWaitSync(arg0: EGLDisplay, arg1: EGLSync, arg2: int) -> bool: ...
    @staticmethod
    def eglCreateImage(arg0: EGLDisplay, arg1: EGLContext, arg2: int, arg3: int, arg4: list[int], arg5: int) -> EGLImage: ...
    @staticmethod
    def eglDestroyImage(arg0: EGLDisplay, arg1: EGLImage) -> bool: ...
