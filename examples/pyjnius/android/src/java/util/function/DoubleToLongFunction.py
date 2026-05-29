from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DoubleToLongFunction"]

class DoubleToLongFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/DoubleToLongFunction"
    applyAsLong = JavaMethod("(D)J")