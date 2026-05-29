from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Matrix2f"]

class Matrix2f(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Matrix2f"
    __javaconstructor__ = [("()V", False), ("([F)V", False)]
    loadMultiply = JavaMethod("(Landroid/renderscript/Matrix2f;Landroid/renderscript/Matrix2f;)V")
    loadRotate = JavaMethod("(F)V")
    loadScale = JavaMethod("(FF)V")
    loadIdentity = JavaMethod("()V")
    transpose = JavaMethod("()V")
    load = JavaMethod("(Landroid/renderscript/Matrix2f;)V")
    scale = JavaMethod("(FF)V")
    get = JavaMethod("(II)F")
    set = JavaMethod("(IIF)V")
    getArray = JavaMethod("()[F")
    multiply = JavaMethod("(Landroid/renderscript/Matrix2f;)V")
    rotate = JavaMethod("(F)V")