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
    def eglDestroyImage(p0: EGLDisplay, p1: EGLImage) -> bool: ...
    @staticmethod
    def eglWaitSync(p0: EGLDisplay, p1: EGLSync, p2: int) -> bool: ...
    @staticmethod
    def eglGetSyncAttrib(p0: EGLDisplay, p1: EGLSync, p2: int, p3: Any, p4: int) -> bool: ...
    @staticmethod
    def eglCreateImage(p0: EGLDisplay, p1: EGLContext, p2: int, p3: int, p4: Any, p5: int) -> EGLImage: ...
    @staticmethod
    def eglCreateSync(p0: EGLDisplay, p1: int, p2: Any, p3: int) -> EGLSync: ...
    @staticmethod
    def eglClientWaitSync(p0: EGLDisplay, p1: EGLSync, p2: int, p3: int) -> int: ...
    @staticmethod
    def eglDestroySync(p0: EGLDisplay, p1: EGLSync) -> bool: ...
    @staticmethod
    def eglCreatePlatformPixmapSurface(p0: EGLDisplay, p1: EGLConfig, p2: Buffer, p3: Any, p4: int) -> EGLSurface: ...
    @staticmethod
    def eglCreatePlatformWindowSurface(p0: EGLDisplay, p1: EGLConfig, p2: Buffer, p3: Any, p4: int) -> EGLSurface: ...
    @staticmethod
    def eglGetPlatformDisplay(p0: int, p1: int, p2: Any, p3: int) -> EGLDisplay: ...
