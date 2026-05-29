from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntFunction"]

class IntFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/IntFunction"
    apply = JavaMethod("(I)Ljava/lang/Object;")