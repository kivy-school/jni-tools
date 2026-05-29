from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LightingColorFilter"]

class LightingColorFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/LightingColorFilter"
    __javaconstructor__ = [("(II)V", False)]
    getColorAdd = JavaMethod("()I")
    getColorMultiply = JavaMethod("()I")