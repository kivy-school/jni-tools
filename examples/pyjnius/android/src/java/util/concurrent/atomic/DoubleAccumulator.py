from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DoubleAccumulator"]

class DoubleAccumulator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/atomic/DoubleAccumulator"
    __javaconstructor__ = [("(Ljava/util/function/DoubleBinaryOperator;D)V", False)]
    reset = JavaMethod("()V")
    toString = JavaMethod("()Ljava/lang/String;")
    intValue = JavaMethod("()I")
    longValue = JavaMethod("()J")
    floatValue = JavaMethod("()F")
    doubleValue = JavaMethod("()D")
    get = JavaMethod("()D")
    accumulate = JavaMethod("(D)V")
    getThenReset = JavaMethod("()D")