from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Matrix44"]

class Matrix44(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/Matrix44"
    __javaconstructor__ = [("()V", False), ("(Landroid/graphics/Matrix;)V", False)]
    getValues = JavaMethod("([F)V")
    setValues = JavaMethod("([F)V")
    get = JavaMethod("(II)F")
    set = JavaMethod("(IIF)V")
    reset = JavaMethod("()V")
    invert = JavaMethod("()Z")
    isIdentity = JavaMethod("()Z")
    map = JavaMultipleMethod([("(FFFF)[F", False, False), ("(FFFF[F)V", False, False)])
    concat = JavaMethod("(Landroid/graphics/Matrix44;)Landroid/graphics/Matrix44;")
    rotate = JavaMethod("(FFFF)Landroid/graphics/Matrix44;")
    scale = JavaMethod("(FFF)Landroid/graphics/Matrix44;")
    translate = JavaMethod("(FFF)Landroid/graphics/Matrix44;")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")