from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RoundRectShape"]

class RoundRectShape(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/shapes/RoundRectShape"
    __javaconstructor__ = [("([FLandroid/graphics/RectF;[F)V", False)]
    draw = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;)V")
    getOutline = JavaMethod("(Landroid/graphics/Outline;)V")
    onResize = JavaMethod("(FF)V")
    clone = JavaMethod("()Landroid/graphics/drawable/shapes/RoundRectShape;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")