from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DoubleAdder"]

class DoubleAdder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/atomic/DoubleAdder"
    __javaconstructor__ = [("()V", False)]
    reset = JavaMethod("()V")
    toString = JavaMethod("()Ljava/lang/String;")
    intValue = JavaMethod("()I")
    longValue = JavaMethod("()J")
    floatValue = JavaMethod("()F")
    doubleValue = JavaMethod("()D")
    add = JavaMethod("(D)V")
    sumThenReset = JavaMethod("()D")
    sum = JavaMethod("()D")