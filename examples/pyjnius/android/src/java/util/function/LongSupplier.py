from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LongSupplier"]

class LongSupplier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/LongSupplier"
    getAsLong = JavaMethod("()J")