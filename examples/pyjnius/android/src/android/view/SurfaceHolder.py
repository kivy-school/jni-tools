from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SurfaceHolder"]

class SurfaceHolder(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/SurfaceHolder"
    SURFACE_TYPE_GPU = JavaStaticField("I")
    SURFACE_TYPE_HARDWARE = JavaStaticField("I")
    SURFACE_TYPE_NORMAL = JavaStaticField("I")
    SURFACE_TYPE_PUSH_BUFFERS = JavaStaticField("I")
    addCallback = JavaMethod("(Landroid/view/SurfaceHolder$Callback;)V")
    removeCallback = JavaMethod("(Landroid/view/SurfaceHolder$Callback;)V")
    isCreating = JavaMethod("()Z")
    setType = JavaMethod("(I)V")
    setFixedSize = JavaMethod("(II)V")
    setSizeFromLayout = JavaMethod("()V")
    setFormat = JavaMethod("(I)V")
    setKeepScreenOn = JavaMethod("(Z)V")
    lockCanvas = JavaMultipleMethod([("()Landroid/graphics/Canvas;", False, False), ("(Landroid/graphics/Rect;)Landroid/graphics/Canvas;", False, False)])
    lockHardwareCanvas = JavaMethod("()Landroid/graphics/Canvas;")
    unlockCanvasAndPost = JavaMethod("(Landroid/graphics/Canvas;)V")
    getSurfaceFrame = JavaMethod("()Landroid/graphics/Rect;")
    getSurface = JavaMethod("()Landroid/view/Surface;")

    class BadSurfaceTypeException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/SurfaceHolder/BadSurfaceTypeException"
        __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]

    class Callback(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/SurfaceHolder/Callback"
        surfaceCreated = JavaMethod("(Landroid/view/SurfaceHolder;)V")
        surfaceChanged = JavaMethod("(Landroid/view/SurfaceHolder;III)V")
        surfaceDestroyed = JavaMethod("(Landroid/view/SurfaceHolder;)V")

    class Callback2(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/SurfaceHolder/Callback2"
        surfaceRedrawNeeded = JavaMethod("(Landroid/view/SurfaceHolder;)V")
        surfaceRedrawNeededAsync = JavaMethod("(Landroid/view/SurfaceHolder;Ljava/lang/Runnable;)V")