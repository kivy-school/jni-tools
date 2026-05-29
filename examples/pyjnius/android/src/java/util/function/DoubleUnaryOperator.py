from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DoubleUnaryOperator"]

class DoubleUnaryOperator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/DoubleUnaryOperator"
    identity = JavaStaticMethod("()Ljava/util/function/DoubleUnaryOperator;")
    applyAsDouble = JavaMethod("(D)D")
    compose = JavaMethod("(Ljava/util/function/DoubleUnaryOperator;)Ljava/util/function/DoubleUnaryOperator;")
    andThen = JavaMethod("(Ljava/util/function/DoubleUnaryOperator;)Ljava/util/function/DoubleUnaryOperator;")