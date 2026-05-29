from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SurfaceHolder"]

class SurfaceHolder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/SurfaceHolder"
    SURFACE_TYPE_GPU = JavaStaticField("I")
    SURFACE_TYPE_HARDWARE = JavaStaticField("I")
    SURFACE_TYPE_NORMAL = JavaStaticField("I")
    SURFACE_TYPE_PUSH_BUFFERS = JavaStaticField("I")
    setKeepScreenOn = JavaMethod("(Z)V")
    getSurface = JavaMethod("()Landroid/view/Surface;")
    lockCanvas = JavaMultipleMethod([("()Landroid/graphics/Canvas;", False, False), ("(Landroid/graphics/Rect;)Landroid/graphics/Canvas;", False, False)])
    lockHardwareCanvas = JavaMethod("()Landroid/graphics/Canvas;")
    unlockCanvasAndPost = JavaMethod("(Landroid/graphics/Canvas;)V")
    setType = JavaMethod("(I)V")
    setFixedSize = JavaMethod("(II)V")
    isCreating = JavaMethod("()Z")
    getSurfaceFrame = JavaMethod("()Landroid/graphics/Rect;")
    setSizeFromLayout = JavaMethod("()V")
    setFormat = JavaMethod("(I)V")
    removeCallback = JavaMethod("(Landroid/view/SurfaceHolder$Callback;)V")
    addCallback = JavaMethod("(Landroid/view/SurfaceHolder$Callback;)V")

    class Callback2(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/SurfaceHolder$Callback2"
        surfaceRedrawNeeded = JavaMethod("(Landroid/view/SurfaceHolder;)V")
        surfaceRedrawNeededAsync = JavaMethod("(Landroid/view/SurfaceHolder;Ljava/lang/Runnable;)V")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/SurfaceHolder$Callback"
        surfaceChanged = JavaMethod("(Landroid/view/SurfaceHolder;III)V")
        surfaceCreated = JavaMethod("(Landroid/view/SurfaceHolder;)V")
        surfaceDestroyed = JavaMethod("(Landroid/view/SurfaceHolder;)V")

    class BadSurfaceTypeException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/SurfaceHolder$BadSurfaceTypeException"
        __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]