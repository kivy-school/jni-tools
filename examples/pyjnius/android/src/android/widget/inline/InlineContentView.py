from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InlineContentView"]

class InlineContentView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/inline/InlineContentView"
    getSurfaceControl = JavaMethod("()Landroid/view/SurfaceControl;")
    setClipBounds = JavaMethod("(Landroid/graphics/Rect;)V")
    onAttachedToWindow = JavaMethod("()V")
    onDetachedFromWindow = JavaMethod("()V")
    onLayout = JavaMethod("(ZIIII)V")
    setSurfaceControlCallback = JavaMethod("(Landroid/widget/inline/InlineContentView$SurfaceControlCallback;)V")
    isZOrderedOnTop = JavaMethod("()Z")
    setZOrderedOnTop = JavaMethod("(Z)Z")

    class SurfaceControlCallback(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/inline/InlineContentView/SurfaceControlCallback"
        onCreated = JavaMethod("(Landroid/view/SurfaceControl;)V")
        onDestroyed = JavaMethod("(Landroid/view/SurfaceControl;)V")