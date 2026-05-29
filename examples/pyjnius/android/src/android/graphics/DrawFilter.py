from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DrawFilter"]

class DrawFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/DrawFilter"
    __javaconstructor__ = [("()V", False)]
    finalize = JavaMethod("()V")