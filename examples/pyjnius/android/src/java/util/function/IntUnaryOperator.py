from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntUnaryOperator"]

class IntUnaryOperator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/IntUnaryOperator"
    applyAsInt = JavaMethod("(I)I")
    compose = JavaMethod("(Ljava/util/function/IntUnaryOperator;)Ljava/util/function/IntUnaryOperator;")
    andThen = JavaMethod("(Ljava/util/function/IntUnaryOperator;)Ljava/util/function/IntUnaryOperator;")
    identity = JavaStaticMethod("()Ljava/util/function/IntUnaryOperator;")