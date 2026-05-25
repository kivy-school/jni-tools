from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PathShape"]

class PathShape(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/shapes/PathShape"
    __javaconstructor__ = [("(Landroid/graphics/Path;FF)V", False)]
    draw = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;)V")
    onResize = JavaMethod("(FF)V")
    clone = JavaMethod("()Landroid/graphics/drawable/shapes/PathShape;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")