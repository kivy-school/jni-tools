from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ArcShape"]

class ArcShape(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/shapes/ArcShape"
    __javaconstructor__ = [("(FF)V", False)]
    getSweepAngle = JavaMethod("()F")
    getStartAngle = JavaMethod("()F")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    clone = JavaMultipleMethod([("()Landroid/graphics/drawable/shapes/Shape;", False, False), ("()Ljava/lang/Object;", False, False), ("()Landroid/graphics/drawable/shapes/RectShape;", False, False), ("()Landroid/graphics/drawable/shapes/ArcShape;", False, False)])
    draw = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;)V")
    getOutline = JavaMethod("(Landroid/graphics/Outline;)V")