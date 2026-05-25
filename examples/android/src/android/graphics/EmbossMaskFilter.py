from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EmbossMaskFilter"]

class EmbossMaskFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/EmbossMaskFilter"
    __javaconstructor__ = [("([FFFF)V", False)]