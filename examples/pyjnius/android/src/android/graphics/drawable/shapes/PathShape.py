from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PathShape"]

class PathShape(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/shapes/PathShape"
    __javaconstructor__ = [("(Landroid/graphics/Path;FF)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    clone = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Landroid/graphics/drawable/shapes/PathShape;", False, False), ("()Landroid/graphics/drawable/shapes/Shape;", False, False)])
    draw = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;)V")