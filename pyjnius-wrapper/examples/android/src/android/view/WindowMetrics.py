from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WindowMetrics"]

class WindowMetrics(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/WindowMetrics"
    __javaconstructor__ = [("(Landroid/graphics/Rect;Landroid/view/WindowInsets;)V", False), ("(Landroid/graphics/Rect;Landroid/view/WindowInsets;F)V", False)]
    getBounds = JavaMethod("()Landroid/graphics/Rect;")
    getWindowInsets = JavaMethod("()Landroid/view/WindowInsets;")
    getDensity = JavaMethod("()F")
    toString = JavaMethod("()Ljava/lang/String;")