from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Matrix44"]

class Matrix44(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/Matrix44"
    __javaconstructor__ = [("()V", False), ("(Landroid/graphics/Matrix;)V", False)]
    reset = JavaMethod("()V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    scale = JavaMethod("(FFF)Landroid/graphics/Matrix44;")
    get = JavaMethod("(II)F")
    map = JavaMultipleMethod([("(FFFF)[F", False, False), ("(FFFF[F)V", False, False)])
    concat = JavaMethod("(Landroid/graphics/Matrix44;)Landroid/graphics/Matrix44;")
    set = JavaMethod("(IIF)V")
    isIdentity = JavaMethod("()Z")
    translate = JavaMethod("(FFF)Landroid/graphics/Matrix44;")
    getValues = JavaMethod("([F)V")
    invert = JavaMethod("()Z")
    setValues = JavaMethod("([F)V")
    rotate = JavaMethod("(FFFF)Landroid/graphics/Matrix44;")