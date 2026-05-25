from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ArcShape"]

class ArcShape(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/shapes/ArcShape"
    __javaconstructor__ = [("(FF)V", False)]
    getStartAngle = JavaMethod("()F")
    getSweepAngle = JavaMethod("()F")
    draw = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;)V")
    getOutline = JavaMethod("(Landroid/graphics/Outline;)V")
    clone = JavaMethod("()Landroid/graphics/drawable/shapes/ArcShape;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")