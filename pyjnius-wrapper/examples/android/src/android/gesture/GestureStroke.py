from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GestureStroke"]

class GestureStroke(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/gesture/GestureStroke"
    __javaconstructor__ = [("(Ljava/util/ArrayList;)V", False)]
    boundingBox = JavaField("Landroid/graphics/RectF;")
    length = JavaField("F")
    points = JavaField("[F")
    clone = JavaMethod("()Ljava/lang/Object;")
    getPath = JavaMethod("()Landroid/graphics/Path;")
    toPath = JavaMethod("(FFI)Landroid/graphics/Path;")
    clearPath = JavaMethod("()V")
    computeOrientedBoundingBox = JavaMethod("()Landroid/gesture/OrientedBoundingBox;")