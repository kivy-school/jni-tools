from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnaryOperator"]

class UnaryOperator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/UnaryOperator"
    identity = JavaStaticMethod("()Ljava/util/function/UnaryOperator;")