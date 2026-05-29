from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OvalShape"]

class OvalShape(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/shapes/OvalShape"
    __javaconstructor__ = [("()V", False)]
    clone = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Landroid/graphics/drawable/shapes/RectShape;", False, False), ("()Landroid/graphics/drawable/shapes/Shape;", False, False), ("()Landroid/graphics/drawable/shapes/OvalShape;", False, False)])
    draw = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;)V")
    getOutline = JavaMethod("(Landroid/graphics/Outline;)V")