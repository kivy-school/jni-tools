from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ColorMatrixColorFilter"]

class ColorMatrixColorFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/ColorMatrixColorFilter"
    __javaconstructor__ = [("(Landroid/graphics/ColorMatrix;)V", False), ("([F)V", False)]
    getColorMatrix = JavaMethod("(Landroid/graphics/ColorMatrix;)V")