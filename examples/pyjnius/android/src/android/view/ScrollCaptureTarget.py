from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScrollCaptureTarget"]

class ScrollCaptureTarget(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ScrollCaptureTarget"
    __javaconstructor__ = [("(Landroid/view/View;Landroid/graphics/Rect;Landroid/graphics/Point;Landroid/view/ScrollCaptureCallback;)V", False)]
    getContainingView = JavaMethod("()Landroid/view/View;")
    getPositionInWindow = JavaMethod("()Landroid/graphics/Point;")
    getScrollBounds = JavaMethod("()Landroid/graphics/Rect;")
    setScrollBounds = JavaMethod("(Landroid/graphics/Rect;)V")
    updatePositionInWindow = JavaMethod("()V")
    toString = JavaMethod("()Ljava/lang/String;")
    getLocalVisibleRect = JavaMethod("()Landroid/graphics/Rect;")
    getHint = JavaMethod("()I")
    getCallback = JavaMethod("()Landroid/view/ScrollCaptureCallback;")