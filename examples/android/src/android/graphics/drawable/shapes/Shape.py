from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Shape"]

class Shape(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/shapes/Shape"
    __javaconstructor__ = [("()V", False)]
    getWidth = JavaMethod("()F")
    getHeight = JavaMethod("()F")
    draw = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;)V")
    resize = JavaMethod("(FF)V")
    hasAlpha = JavaMethod("()Z")
    onResize = JavaMethod("(FF)V")
    getOutline = JavaMethod("(Landroid/graphics/Outline;)V")
    clone = JavaMethod("()Landroid/graphics/drawable/shapes/Shape;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")