from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LongSupplier"]

class LongSupplier(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/LongSupplier"
    getAsLong = JavaMethod("()J")