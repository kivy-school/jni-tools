from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Transformation"]

class Transformation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/Transformation"
    __javaconstructor__ = [("()V", False)]
    TYPE_ALPHA = JavaStaticField("I")
    TYPE_BOTH = JavaStaticField("I")
    TYPE_IDENTITY = JavaStaticField("I")
    TYPE_MATRIX = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    clear = JavaMethod("()V")
    set = JavaMethod("(Landroid/view/animation/Transformation;)V")
    toShortString = JavaMethod("()Ljava/lang/String;")
    setAlpha = JavaMethod("(F)V")
    getAlpha = JavaMethod("()F")
    getMatrix = JavaMethod("()Landroid/graphics/Matrix;")
    getTransformationType = JavaMethod("()I")
    setTransformationType = JavaMethod("(I)V")
    compose = JavaMethod("(Landroid/view/animation/Transformation;)V")