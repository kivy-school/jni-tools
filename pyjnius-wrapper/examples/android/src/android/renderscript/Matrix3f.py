from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Matrix3f"]

class Matrix3f(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Matrix3f"
    __javaconstructor__ = [("()V", False), ("([F)V", False)]
    getArray = JavaMethod("()[F")
    get = JavaMethod("(II)F")
    set = JavaMethod("(IIF)V")
    loadIdentity = JavaMethod("()V")
    load = JavaMethod("(Landroid/renderscript/Matrix3f;)V")
    loadRotate = JavaMultipleMethod([("(FFFF)V", False, False), ("(F)V", False, False)])
    loadScale = JavaMultipleMethod([("(FF)V", False, False), ("(FFF)V", False, False)])
    loadTranslate = JavaMethod("(FF)V")
    loadMultiply = JavaMethod("(Landroid/renderscript/Matrix3f;Landroid/renderscript/Matrix3f;)V")
    multiply = JavaMethod("(Landroid/renderscript/Matrix3f;)V")
    rotate = JavaMultipleMethod([("(FFFF)V", False, False), ("(F)V", False, False)])
    scale = JavaMultipleMethod([("(FF)V", False, False), ("(FFF)V", False, False)])
    translate = JavaMethod("(FF)V")
    transpose = JavaMethod("()V")