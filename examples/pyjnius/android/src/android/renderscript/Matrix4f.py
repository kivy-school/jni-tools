from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Matrix4f"]

class Matrix4f(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Matrix4f"
    __javaconstructor__ = [("([F)V", False), ("()V", False)]
    loadMultiply = JavaMethod("(Landroid/renderscript/Matrix4f;Landroid/renderscript/Matrix4f;)V")
    loadRotate = JavaMethod("(FFFF)V")
    loadScale = JavaMethod("(FFF)V")
    loadIdentity = JavaMethod("()V")
    loadTranslate = JavaMethod("(FFF)V")
    transpose = JavaMethod("()V")
    loadOrthoWindow = JavaMethod("(II)V")
    loadPerspective = JavaMethod("(FFFF)V")
    loadFrustum = JavaMethod("(FFFFFF)V")
    inverseTranspose = JavaMethod("()Z")
    loadProjectionNormalized = JavaMethod("(II)V")
    loadOrtho = JavaMethod("(FFFFFF)V")
    load = JavaMethod("(Landroid/renderscript/Matrix4f;)V")
    scale = JavaMethod("(FFF)V")
    get = JavaMethod("(II)F")
    set = JavaMethod("(IIF)V")
    translate = JavaMethod("(FFF)V")
    inverse = JavaMethod("()Z")
    getArray = JavaMethod("()[F")
    multiply = JavaMethod("(Landroid/renderscript/Matrix4f;)V")
    rotate = JavaMethod("(FFFF)V")