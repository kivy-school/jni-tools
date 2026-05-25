from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnaryOperator"]

class UnaryOperator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/UnaryOperator"
    identity = JavaStaticMethod("()Ljava/util/function/UnaryOperator;")