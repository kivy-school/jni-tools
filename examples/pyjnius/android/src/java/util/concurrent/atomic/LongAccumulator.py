from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LongAccumulator"]

class LongAccumulator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/atomic/LongAccumulator"
    __javaconstructor__ = [("(Ljava/util/function/LongBinaryOperator;J)V", False)]
    reset = JavaMethod("()V")
    toString = JavaMethod("()Ljava/lang/String;")
    intValue = JavaMethod("()I")
    longValue = JavaMethod("()J")
    floatValue = JavaMethod("()F")
    doubleValue = JavaMethod("()D")
    get = JavaMethod("()J")
    accumulate = JavaMethod("(J)V")
    getThenReset = JavaMethod("()J")