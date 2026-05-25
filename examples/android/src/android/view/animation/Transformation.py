from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Transformation"]

class Transformation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/Transformation"
    __javaconstructor__ = [("()V", False)]
    TYPE_ALPHA = JavaStaticField("I")
    TYPE_BOTH = JavaStaticField("I")
    TYPE_IDENTITY = JavaStaticField("I")
    TYPE_MATRIX = JavaStaticField("I")
    mAlpha = JavaField("F")
    mMatrix = JavaField("Landroid/graphics/Matrix;")
    mTransformationType = JavaField("I")
    clear = JavaMethod("()V")
    getTransformationType = JavaMethod("()I")
    setTransformationType = JavaMethod("(I)V")
    set = JavaMethod("(Landroid/view/animation/Transformation;)V")
    compose = JavaMethod("(Landroid/view/animation/Transformation;)V")
    getMatrix = JavaMethod("()Landroid/graphics/Matrix;")
    setAlpha = JavaMethod("(F)V")
    getAlpha = JavaMethod("()F")
    toString = JavaMethod("()Ljava/lang/String;")
    toShortString = JavaMethod("()Ljava/lang/String;")