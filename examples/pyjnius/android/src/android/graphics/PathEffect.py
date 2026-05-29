from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PathEffect"]

class PathEffect(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/PathEffect"
    __javaconstructor__ = [("()V", False)]