from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PathEffect"]

class PathEffect(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/PathEffect"
    __javaconstructor__ = [("()V", False)]
    finalize = JavaMethod("()V")