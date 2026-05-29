from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntFunction"]

class IntFunction(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/IntFunction"
    apply = JavaMethod("(I)Ljava/lang/Object;")