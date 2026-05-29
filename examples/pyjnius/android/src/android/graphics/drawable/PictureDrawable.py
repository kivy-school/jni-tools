from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PictureDrawable"]

class PictureDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/PictureDrawable"
    __javaconstructor__ = [("(Landroid/graphics/Picture;)V", False)]
    setAlpha = JavaMethod("(I)V")
    setColorFilter = JavaMethod("(Landroid/graphics/ColorFilter;)V")
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    setPicture = JavaMethod("(Landroid/graphics/Picture;)V")
    getPicture = JavaMethod("()Landroid/graphics/Picture;")
    getIntrinsicHeight = JavaMethod("()I")
    getIntrinsicWidth = JavaMethod("()I")
    getOpacity = JavaMethod("()I")