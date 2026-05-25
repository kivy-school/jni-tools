from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RectShape"]

class RectShape(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/shapes/RectShape"
    __javaconstructor__ = [("()V", False)]
    draw = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;)V")
    getOutline = JavaMethod("(Landroid/graphics/Outline;)V")
    onResize = JavaMethod("(FF)V")
    rect = JavaMethod("()Landroid/graphics/RectF;")
    clone = JavaMethod("()Landroid/graphics/drawable/shapes/RectShape;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")