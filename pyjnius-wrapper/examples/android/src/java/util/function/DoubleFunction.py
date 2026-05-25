from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DoubleFunction"]

class DoubleFunction(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/DoubleFunction"
    apply = JavaMethod("(D)Ljava/lang/Object;")