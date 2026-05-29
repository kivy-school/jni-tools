from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WindowMetrics"]

class WindowMetrics(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/WindowMetrics"
    __javaconstructor__ = [("(Landroid/graphics/Rect;Landroid/view/WindowInsets;)V", False), ("(Landroid/graphics/Rect;Landroid/view/WindowInsets;F)V", False)]
    getWindowInsets = JavaMethod("()Landroid/view/WindowInsets;")
    toString = JavaMethod("()Ljava/lang/String;")
    getBounds = JavaMethod("()Landroid/graphics/Rect;")
    getDensity = JavaMethod("()F")