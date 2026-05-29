from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntToLongFunction"]

class IntToLongFunction(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/IntToLongFunction"
    applyAsLong = JavaMethod("(I)J")