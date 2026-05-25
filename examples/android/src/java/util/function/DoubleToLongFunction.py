from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DoubleToLongFunction"]

class DoubleToLongFunction(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/DoubleToLongFunction"
    applyAsLong = JavaMethod("(D)J")