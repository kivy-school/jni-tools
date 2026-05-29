from typing import Any, ClassVar, overload
from android.hardware.SyncFence import SyncFence
from android.opengl.EGLDisplay import EGLDisplay
from android.opengl.EGLSurface import EGLSurface
from android.opengl.EGLSync import EGLSync

class EGLExt:
    EGL_CONTEXT_FLAGS_KHR: ClassVar[int]
    EGL_CONTEXT_MAJOR_VERSION_KHR: ClassVar[int]
    EGL_CONTEXT_MINOR_VERSION_KHR: ClassVar[int]
    EGL_NO_NATIVE_FENCE_FD_ANDROID: ClassVar[int]
    EGL_OPENGL_ES3_BIT_KHR: ClassVar[int]
    EGL_RECORDABLE_ANDROID: ClassVar[int]
    EGL_SYNC_NATIVE_FENCE_ANDROID: ClassVar[int]
    EGL_SYNC_NATIVE_FENCE_FD_ANDROID: ClassVar[int]
    EGL_SYNC_NATIVE_FENCE_SIGNALED_ANDROID: ClassVar[int]
    def __init__(self) -> None: ...
    @staticmethod
    def eglDupNativeFenceFDANDROID(p0: EGLDisplay, p1: EGLSync) -> SyncFence: ...
    @staticmethod
    def eglPresentationTimeANDROID(p0: EGLDisplay, p1: EGLSurface, p2: int) -> bool: ...
