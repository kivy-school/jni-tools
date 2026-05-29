from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ColorMatrix"]

class ColorMatrix(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/ColorMatrix"
    __javaconstructor__ = [("()V", False), ("([F)V", False), ("(Landroid/graphics/ColorMatrix;)V", False)]
    setRGB2YUV = JavaMethod("()V")
    setYUV2RGB = JavaMethod("()V")
    setSaturation = JavaMethod("(F)V")
    reset = JavaMethod("()V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    set = JavaMultipleMethod([("(Landroid/graphics/ColorMatrix;)V", False, False), ("([F)V", False, False)])
    postConcat = JavaMethod("(Landroid/graphics/ColorMatrix;)V")
    preConcat = JavaMethod("(Landroid/graphics/ColorMatrix;)V")
    setConcat = JavaMethod("(Landroid/graphics/ColorMatrix;Landroid/graphics/ColorMatrix;)V")
    setRotate = JavaMethod("(IF)V")
    setScale = JavaMethod("(FFFF)V")
    getArray = JavaMethod("()[F")