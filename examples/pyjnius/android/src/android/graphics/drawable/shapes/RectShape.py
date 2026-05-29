from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RectShape"]

class RectShape(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/shapes/RectShape"
    __javaconstructor__ = [("()V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    clone = JavaMultipleMethod([("()Landroid/graphics/drawable/shapes/RectShape;", False, False), ("()Landroid/graphics/drawable/shapes/Shape;", False, False), ("()Ljava/lang/Object;", False, False)])
    draw = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;)V")
    getOutline = JavaMethod("(Landroid/graphics/Outline;)V")