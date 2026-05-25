from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ToLongFunction"]

class ToLongFunction(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/ToLongFunction"
    applyAsLong = JavaMethod("(Ljava/lang/Object;)J")