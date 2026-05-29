from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntUnaryOperator"]

class IntUnaryOperator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/IntUnaryOperator"
    identity = JavaStaticMethod("()Ljava/util/function/IntUnaryOperator;")
    applyAsInt = JavaMethod("(I)I")
    compose = JavaMethod("(Ljava/util/function/IntUnaryOperator;)Ljava/util/function/IntUnaryOperator;")
    andThen = JavaMethod("(Ljava/util/function/IntUnaryOperator;)Ljava/util/function/IntUnaryOperator;")