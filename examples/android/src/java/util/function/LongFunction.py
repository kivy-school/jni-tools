from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LongFunction"]

class LongFunction(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/LongFunction"
    apply = JavaMethod("(J)Ljava/lang/Object;")