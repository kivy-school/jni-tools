from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LightingColorFilter"]

class LightingColorFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/LightingColorFilter"
    __javaconstructor__ = [("(II)V", False)]
    getColorMultiply = JavaMethod("()I")
    getColorAdd = JavaMethod("()I")