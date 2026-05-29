from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DoubleAccumulator"]

class DoubleAccumulator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/atomic/DoubleAccumulator"
    __javaconstructor__ = [("(Ljava/util/function/DoubleBinaryOperator;D)V", False)]
    accumulate = JavaMethod("(D)V")
    get = JavaMethod("()D")
    reset = JavaMethod("()V")
    getThenReset = JavaMethod("()D")
    toString = JavaMethod("()Ljava/lang/String;")
    doubleValue = JavaMethod("()D")
    longValue = JavaMethod("()J")
    intValue = JavaMethod("()I")
    floatValue = JavaMethod("()F")