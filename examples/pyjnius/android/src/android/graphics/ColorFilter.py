from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ColorFilter"]

class ColorFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/ColorFilter"
    __javaconstructor__ = [("()V", False)]