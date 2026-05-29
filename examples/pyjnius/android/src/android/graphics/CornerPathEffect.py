from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CornerPathEffect"]

class CornerPathEffect(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/CornerPathEffect"
    __javaconstructor__ = [("(F)V", False)]