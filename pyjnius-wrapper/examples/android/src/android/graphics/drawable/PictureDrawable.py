from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PictureDrawable"]

class PictureDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/PictureDrawable"
    __javaconstructor__ = [("(Landroid/graphics/Picture;)V", False)]
    getPicture = JavaMethod("()Landroid/graphics/Picture;")
    setPicture = JavaMethod("(Landroid/graphics/Picture;)V")
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    getIntrinsicWidth = JavaMethod("()I")
    getIntrinsicHeight = JavaMethod("()I")
    getOpacity = JavaMethod("()I")
    setColorFilter = JavaMethod("(Landroid/graphics/ColorFilter;)V")
    setAlpha = JavaMethod("(I)V")