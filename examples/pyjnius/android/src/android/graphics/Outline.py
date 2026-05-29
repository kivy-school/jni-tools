from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Outline"]

class Outline(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/Outline"
    __javaconstructor__ = [("()V", False), ("(Landroid/graphics/Outline;)V", False)]
    isEmpty = JavaMethod("()Z")
    offset = JavaMethod("(II)V")
    set = JavaMethod("(Landroid/graphics/Outline;)V")
    setAlpha = JavaMethod("(F)V")
    getAlpha = JavaMethod("()F")
    getRadius = JavaMethod("()F")
    setEmpty = JavaMethod("()V")
    getRect = JavaMethod("(Landroid/graphics/Rect;)Z")
    setConvexPath = JavaMethod("(Landroid/graphics/Path;)V")
    canClip = JavaMethod("()Z")
    setOval = JavaMultipleMethod([("(IIII)V", False, False), ("(Landroid/graphics/Rect;)V", False, False)])
    setPath = JavaMethod("(Landroid/graphics/Path;)V")
    setRect = JavaMultipleMethod([("(IIII)V", False, False), ("(Landroid/graphics/Rect;)V", False, False)])
    setRoundRect = JavaMultipleMethod([("(Landroid/graphics/Rect;F)V", False, False), ("(IIIIF)V", False, False)])