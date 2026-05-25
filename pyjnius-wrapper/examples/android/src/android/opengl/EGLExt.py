from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EGLExt"]

class EGLExt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/opengl/EGLExt"
    __javaconstructor__ = [("()V", False)]
    EGL_CONTEXT_FLAGS_KHR = JavaStaticField("I")
    EGL_CONTEXT_MAJOR_VERSION_KHR = JavaStaticField("I")
    EGL_CONTEXT_MINOR_VERSION_KHR = JavaStaticField("I")
    EGL_NO_NATIVE_FENCE_FD_ANDROID = JavaStaticField("I")
    EGL_OPENGL_ES3_BIT_KHR = JavaStaticField("I")
    EGL_RECORDABLE_ANDROID = JavaStaticField("I")
    EGL_SYNC_NATIVE_FENCE_ANDROID = JavaStaticField("I")
    EGL_SYNC_NATIVE_FENCE_FD_ANDROID = JavaStaticField("I")
    EGL_SYNC_NATIVE_FENCE_SIGNALED_ANDROID = JavaStaticField("I")
    eglDupNativeFenceFDANDROID = JavaStaticMethod("(Landroid/opengl/EGLDisplay;Landroid/opengl/EGLSync;)Landroid/hardware/SyncFence;")
    eglPresentationTimeANDROID = JavaStaticMethod("(Landroid/opengl/EGLDisplay;Landroid/opengl/EGLSurface;J)Z")