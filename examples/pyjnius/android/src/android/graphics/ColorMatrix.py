from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ColorMatrix"]

class ColorMatrix(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/ColorMatrix"
    __javaconstructor__ = [("()V", False), ("([F)V", False), ("(Landroid/graphics/ColorMatrix;)V", False)]
    getArray = JavaMethod("()[F")
    reset = JavaMethod("()V")
    set = JavaMultipleMethod([("(Landroid/graphics/ColorMatrix;)V", False, False), ("([F)V", False, False)])
    setScale = JavaMethod("(FFFF)V")
    setRotate = JavaMethod("(IF)V")
    setConcat = JavaMethod("(Landroid/graphics/ColorMatrix;Landroid/graphics/ColorMatrix;)V")
    preConcat = JavaMethod("(Landroid/graphics/ColorMatrix;)V")
    postConcat = JavaMethod("(Landroid/graphics/ColorMatrix;)V")
    setSaturation = JavaMethod("(F)V")
    setRGB2YUV = JavaMethod("()V")
    setYUV2RGB = JavaMethod("()V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")