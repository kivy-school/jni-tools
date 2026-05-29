from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScrollCaptureSession"]

class ScrollCaptureSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ScrollCaptureSession"
    __javaconstructor__ = [("(Landroid/view/Surface;Landroid/graphics/Rect;Landroid/graphics/Point;)V", False)]
    getPositionInWindow = JavaMethod("()Landroid/graphics/Point;")
    getScrollBounds = JavaMethod("()Landroid/graphics/Rect;")
    getSurface = JavaMethod("()Landroid/view/Surface;")