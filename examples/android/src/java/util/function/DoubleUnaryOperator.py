from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DoubleUnaryOperator"]

class DoubleUnaryOperator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/DoubleUnaryOperator"
    applyAsDouble = JavaMethod("(D)D")
    compose = JavaMethod("(Ljava/util/function/DoubleUnaryOperator;)Ljava/util/function/DoubleUnaryOperator;")
    andThen = JavaMethod("(Ljava/util/function/DoubleUnaryOperator;)Ljava/util/function/DoubleUnaryOperator;")
    identity = JavaStaticMethod("()Ljava/util/function/DoubleUnaryOperator;")