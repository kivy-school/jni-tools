from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DoubleFunction"]

class DoubleFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/DoubleFunction"
    apply = JavaMethod("(D)Ljava/lang/Object;")