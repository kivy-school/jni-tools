from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LongAdder"]

class LongAdder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/atomic/LongAdder"
    __javaconstructor__ = [("()V", False)]
    reset = JavaMethod("()V")
    toString = JavaMethod("()Ljava/lang/String;")
    intValue = JavaMethod("()I")
    longValue = JavaMethod("()J")
    floatValue = JavaMethod("()F")
    doubleValue = JavaMethod("()D")
    add = JavaMethod("(J)V")
    increment = JavaMethod("()V")
    sumThenReset = JavaMethod("()J")
    sum = JavaMethod("()J")
    decrement = JavaMethod("()V")