from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScrollCaptureTarget"]

class ScrollCaptureTarget(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ScrollCaptureTarget"
    __javaconstructor__ = [("(Landroid/view/View;Landroid/graphics/Rect;Landroid/graphics/Point;Landroid/view/ScrollCaptureCallback;)V", False)]
    getHint = JavaMethod("()I")
    getCallback = JavaMethod("()Landroid/view/ScrollCaptureCallback;")
    getContainingView = JavaMethod("()Landroid/view/View;")
    getLocalVisibleRect = JavaMethod("()Landroid/graphics/Rect;")
    getPositionInWindow = JavaMethod("()Landroid/graphics/Point;")
    getScrollBounds = JavaMethod("()Landroid/graphics/Rect;")
    setScrollBounds = JavaMethod("(Landroid/graphics/Rect;)V")
    updatePositionInWindow = JavaMethod("()V")
    toString = JavaMethod("()Ljava/lang/String;")