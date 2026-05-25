from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LongAdder"]

class LongAdder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/atomic/LongAdder"
    __javaconstructor__ = [("()V", False)]
    add = JavaMethod("(J)V")
    increment = JavaMethod("()V")
    decrement = JavaMethod("()V")
    sum = JavaMethod("()J")
    reset = JavaMethod("()V")
    sumThenReset = JavaMethod("()J")
    toString = JavaMethod("()Ljava/lang/String;")
    longValue = JavaMethod("()J")
    intValue = JavaMethod("()I")
    floatValue = JavaMethod("()F")
    doubleValue = JavaMethod("()D")