from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LongUnaryOperator"]

class LongUnaryOperator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/LongUnaryOperator"
    identity = JavaStaticMethod("()Ljava/util/function/LongUnaryOperator;")
    applyAsLong = JavaMethod("(J)J")
    compose = JavaMethod("(Ljava/util/function/LongUnaryOperator;)Ljava/util/function/LongUnaryOperator;")
    andThen = JavaMethod("(Ljava/util/function/LongUnaryOperator;)Ljava/util/function/LongUnaryOperator;")