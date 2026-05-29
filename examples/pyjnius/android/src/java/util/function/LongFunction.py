from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LongFunction"]

class LongFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/LongFunction"
    apply = JavaMethod("(J)Ljava/lang/Object;")