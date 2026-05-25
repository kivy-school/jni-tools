from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SurfaceView"]

class SurfaceView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/SurfaceView"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    SURFACE_LIFECYCLE_DEFAULT = JavaStaticField("I")
    SURFACE_LIFECYCLE_FOLLOWS_ATTACHMENT = JavaStaticField("I")
    SURFACE_LIFECYCLE_FOLLOWS_VISIBILITY = JavaStaticField("I")
    getHolder = JavaMethod("()Landroid/view/SurfaceHolder;")
    onAttachedToWindow = JavaMethod("()V")
    onWindowVisibilityChanged = JavaMethod("(I)V")
    setVisibility = JavaMethod("(I)V")
    setAlpha = JavaMethod("(F)V")
    onSetAlpha = JavaMethod("(I)Z")
    onDetachedFromWindow = JavaMethod("()V")
    onMeasure = JavaMethod("(II)V")
    gatherTransparentRegion = JavaMethod("(Landroid/graphics/Region;)Z")
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    dispatchDraw = JavaMethod("(Landroid/graphics/Canvas;)V")
    setClipBounds = JavaMethod("(Landroid/graphics/Rect;)V")
    hasOverlappingRendering = JavaMethod("()Z")
    setZOrderMediaOverlay = JavaMethod("(Z)V")
    setZOrderOnTop = JavaMethod("(Z)V")
    setSecure = JavaMethod("(Z)V")
    setSurfaceLifecycle = JavaMethod("(I)V")
    setDesiredHdrHeadroom = JavaMethod("(F)V")
    getSurfaceControl = JavaMethod("()Landroid/view/SurfaceControl;")
    getHostToken = JavaMethod("()Landroid/os/IBinder;")
    setChildSurfacePackage = JavaMethod("(Landroid/view/SurfaceControlViewHost$SurfacePackage;)V")
    getImportantForAccessibility = JavaMethod("()I")
    onFocusChanged = JavaMethod("(ZILandroid/graphics/Rect;)V")
    applyTransactionToFrame = JavaMethod("(Landroid/view/SurfaceControl$Transaction;)V")