from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DoubleSupplier"]

class DoubleSupplier(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/DoubleSupplier"
    getAsDouble = JavaMethod("()D")