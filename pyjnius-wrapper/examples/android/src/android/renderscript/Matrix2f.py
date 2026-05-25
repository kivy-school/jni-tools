from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Matrix2f"]

class Matrix2f(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Matrix2f"
    __javaconstructor__ = [("()V", False), ("([F)V", False)]
    getArray = JavaMethod("()[F")
    get = JavaMethod("(II)F")
    set = JavaMethod("(IIF)V")
    loadIdentity = JavaMethod("()V")
    load = JavaMethod("(Landroid/renderscript/Matrix2f;)V")
    loadRotate = JavaMethod("(F)V")
    loadScale = JavaMethod("(FF)V")
    loadMultiply = JavaMethod("(Landroid/renderscript/Matrix2f;Landroid/renderscript/Matrix2f;)V")
    multiply = JavaMethod("(Landroid/renderscript/Matrix2f;)V")
    rotate = JavaMethod("(F)V")
    scale = JavaMethod("(FF)V")
    transpose = JavaMethod("()V")