from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Shape"]

class Shape(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/shapes/Shape"
    __javaconstructor__ = [("()V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    clone = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Landroid/graphics/drawable/shapes/Shape;", False, False)])
    hasAlpha = JavaMethod("()Z")
    draw = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;)V")
    getHeight = JavaMethod("()F")
    getWidth = JavaMethod("()F")
    getOutline = JavaMethod("(Landroid/graphics/Outline;)V")
    resize = JavaMethod("(FF)V")