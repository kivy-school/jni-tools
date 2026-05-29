from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Matrix3f"]

class Matrix3f(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Matrix3f"
    __javaconstructor__ = [("()V", False), ("([F)V", False)]
    loadMultiply = JavaMethod("(Landroid/renderscript/Matrix3f;Landroid/renderscript/Matrix3f;)V")
    loadRotate = JavaMultipleMethod([("(F)V", False, False), ("(FFFF)V", False, False)])
    loadScale = JavaMultipleMethod([("(FFF)V", False, False), ("(FF)V", False, False)])
    loadIdentity = JavaMethod("()V")
    loadTranslate = JavaMethod("(FF)V")
    transpose = JavaMethod("()V")
    load = JavaMethod("(Landroid/renderscript/Matrix3f;)V")
    scale = JavaMultipleMethod([("(FF)V", False, False), ("(FFF)V", False, False)])
    get = JavaMethod("(II)F")
    set = JavaMethod("(IIF)V")
    translate = JavaMethod("(FF)V")
    getArray = JavaMethod("()[F")
    multiply = JavaMethod("(Landroid/renderscript/Matrix3f;)V")
    rotate = JavaMultipleMethod([("(F)V", False, False), ("(FFFF)V", False, False)])