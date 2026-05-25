from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LongAccumulator"]

class LongAccumulator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/atomic/LongAccumulator"
    __javaconstructor__ = [("(Ljava/util/function/LongBinaryOperator;J)V", False)]
    accumulate = JavaMethod("(J)V")
    get = JavaMethod("()J")
    reset = JavaMethod("()V")
    getThenReset = JavaMethod("()J")
    toString = JavaMethod("()Ljava/lang/String;")
    longValue = JavaMethod("()J")
    intValue = JavaMethod("()I")
    floatValue = JavaMethod("()F")
    doubleValue = JavaMethod("()D")