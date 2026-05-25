from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Matrix4f"]

class Matrix4f(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Matrix4f"
    __javaconstructor__ = [("()V", False), ("([F)V", False)]
    getArray = JavaMethod("()[F")
    get = JavaMethod("(II)F")
    set = JavaMethod("(IIF)V")
    loadIdentity = JavaMethod("()V")
    load = JavaMethod("(Landroid/renderscript/Matrix4f;)V")
    loadRotate = JavaMethod("(FFFF)V")
    loadScale = JavaMethod("(FFF)V")
    loadTranslate = JavaMethod("(FFF)V")
    loadMultiply = JavaMethod("(Landroid/renderscript/Matrix4f;Landroid/renderscript/Matrix4f;)V")
    loadOrtho = JavaMethod("(FFFFFF)V")
    loadOrthoWindow = JavaMethod("(II)V")
    loadFrustum = JavaMethod("(FFFFFF)V")
    loadPerspective = JavaMethod("(FFFF)V")
    loadProjectionNormalized = JavaMethod("(II)V")
    multiply = JavaMethod("(Landroid/renderscript/Matrix4f;)V")
    rotate = JavaMethod("(FFFF)V")
    scale = JavaMethod("(FFF)V")
    translate = JavaMethod("(FFF)V")
    inverse = JavaMethod("()Z")
    inverseTranspose = JavaMethod("()Z")
    transpose = JavaMethod("()V")