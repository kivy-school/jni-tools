from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DoubleSupplier"]

class DoubleSupplier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/DoubleSupplier"
    getAsDouble = JavaMethod("()D")