from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Outline"]

class Outline(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/Outline"
    __javaconstructor__ = [("()V", False), ("(Landroid/graphics/Outline;)V", False)]
    setEmpty = JavaMethod("()V")
    isEmpty = JavaMethod("()Z")
    canClip = JavaMethod("()Z")
    setAlpha = JavaMethod("(F)V")
    getAlpha = JavaMethod("()F")
    set = JavaMethod("(Landroid/graphics/Outline;)V")
    setRect = JavaMultipleMethod([("(IIII)V", False, False), ("(Landroid/graphics/Rect;)V", False, False)])
    setRoundRect = JavaMultipleMethod([("(IIIIF)V", False, False), ("(Landroid/graphics/Rect;F)V", False, False)])
    getRect = JavaMethod("(Landroid/graphics/Rect;)Z")
    getRadius = JavaMethod("()F")
    setOval = JavaMultipleMethod([("(IIII)V", False, False), ("(Landroid/graphics/Rect;)V", False, False)])
    setConvexPath = JavaMethod("(Landroid/graphics/Path;)V")
    setPath = JavaMethod("(Landroid/graphics/Path;)V")
    offset = JavaMethod("(II)V")