from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MaskFilter"]

class MaskFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/MaskFilter"
    __javaconstructor__ = [("()V", False)]