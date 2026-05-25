from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GLSurfaceView"]

class GLSurfaceView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/opengl/GLSurfaceView"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    DEBUG_CHECK_GL_ERROR = JavaStaticField("I")
    DEBUG_LOG_GL_CALLS = JavaStaticField("I")
    RENDERMODE_CONTINUOUSLY = JavaStaticField("I")
    RENDERMODE_WHEN_DIRTY = JavaStaticField("I")
    finalize = JavaMethod("()V")
    setGLWrapper = JavaMethod("(Landroid/opengl/GLSurfaceView$GLWrapper;)V")
    setDebugFlags = JavaMethod("(I)V")
    getDebugFlags = JavaMethod("()I")
    setPreserveEGLContextOnPause = JavaMethod("(Z)V")
    getPreserveEGLContextOnPause = JavaMethod("()Z")
    setRenderer = JavaMethod("(Landroid/opengl/GLSurfaceView$Renderer;)V")
    setEGLContextFactory = JavaMethod("(Landroid/opengl/GLSurfaceView$EGLContextFactory;)V")
    setEGLWindowSurfaceFactory = JavaMethod("(Landroid/opengl/GLSurfaceView$EGLWindowSurfaceFactory;)V")
    setEGLConfigChooser = JavaMultipleMethod([("(Landroid/opengl/GLSurfaceView$EGLConfigChooser;)V", False, False), ("(Z)V", False, False), ("(IIIIII)V", False, False)])
    setEGLContextClientVersion = JavaMethod("(I)V")
    setRenderMode = JavaMethod("(I)V")
    getRenderMode = JavaMethod("()I")
    requestRender = JavaMethod("()V")
    surfaceCreated = JavaMethod("(Landroid/view/SurfaceHolder;)V")
    surfaceDestroyed = JavaMethod("(Landroid/view/SurfaceHolder;)V")
    surfaceChanged = JavaMethod("(Landroid/view/SurfaceHolder;III)V")
    surfaceRedrawNeededAsync = JavaMethod("(Landroid/view/SurfaceHolder;Ljava/lang/Runnable;)V")
    surfaceRedrawNeeded = JavaMethod("(Landroid/view/SurfaceHolder;)V")
    onPause = JavaMethod("()V")
    onResume = JavaMethod("()V")
    queueEvent = JavaMethod("(Ljava/lang/Runnable;)V")
    onAttachedToWindow = JavaMethod("()V")
    onDetachedFromWindow = JavaMethod("()V")

    class EGLConfigChooser(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/opengl/GLSurfaceView/EGLConfigChooser"
        chooseConfig = JavaMethod("(Ljavax/microedition/khronos/egl/EGL10;Ljavax/microedition/khronos/egl/EGLDisplay;)Ljavax/microedition/khronos/egl/EGLConfig;")

    class EGLContextFactory(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/opengl/GLSurfaceView/EGLContextFactory"
        createContext = JavaMethod("(Ljavax/microedition/khronos/egl/EGL10;Ljavax/microedition/khronos/egl/EGLDisplay;Ljavax/microedition/khronos/egl/EGLConfig;)Ljavax/microedition/khronos/egl/EGLContext;")
        destroyContext = JavaMethod("(Ljavax/microedition/khronos/egl/EGL10;Ljavax/microedition/khronos/egl/EGLDisplay;Ljavax/microedition/khronos/egl/EGLContext;)V")

    class EGLWindowSurfaceFactory(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/opengl/GLSurfaceView/EGLWindowSurfaceFactory"
        createWindowSurface = JavaMethod("(Ljavax/microedition/khronos/egl/EGL10;Ljavax/microedition/khronos/egl/EGLDisplay;Ljavax/microedition/khronos/egl/EGLConfig;Ljava/lang/Object;)Ljavax/microedition/khronos/egl/EGLSurface;")
        destroySurface = JavaMethod("(Ljavax/microedition/khronos/egl/EGL10;Ljavax/microedition/khronos/egl/EGLDisplay;Ljavax/microedition/khronos/egl/EGLSurface;)V")

    class GLWrapper(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/opengl/GLSurfaceView/GLWrapper"
        wrap = JavaMethod("(Ljavax/microedition/khronos/opengles/GL;)Ljavax/microedition/khronos/opengles/GL;")

    class Renderer(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/opengl/GLSurfaceView/Renderer"
        onSurfaceCreated = JavaMethod("(Ljavax/microedition/khronos/opengles/GL10;Ljavax/microedition/khronos/egl/EGLConfig;)V")
        onSurfaceChanged = JavaMethod("(Ljavax/microedition/khronos/opengles/GL10;II)V")
        onDrawFrame = JavaMethod("(Ljavax/microedition/khronos/opengles/GL10;)V")