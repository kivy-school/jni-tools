from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntToLongFunction"]

class IntToLongFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/IntToLongFunction"
    applyAsLong = JavaMethod("(I)J")