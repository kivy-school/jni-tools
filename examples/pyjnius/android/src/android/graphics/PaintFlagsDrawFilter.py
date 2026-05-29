from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PaintFlagsDrawFilter"]

class PaintFlagsDrawFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/PaintFlagsDrawFilter"
    __javaconstructor__ = [("(II)V", False)]