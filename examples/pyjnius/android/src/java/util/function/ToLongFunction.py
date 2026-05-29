from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ToLongFunction"]

class ToLongFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/ToLongFunction"
    applyAsLong = JavaMethod("(Ljava/lang/Object;)J")