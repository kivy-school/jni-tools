from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MaskFilter"]

class MaskFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/MaskFilter"
    __javaconstructor__ = [("()V", False)]
    finalize = JavaMethod("()V")