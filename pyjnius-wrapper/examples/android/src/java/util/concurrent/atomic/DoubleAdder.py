from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DoubleAdder"]

class DoubleAdder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/atomic/DoubleAdder"
    __javaconstructor__ = [("()V", False)]
    add = JavaMethod("(D)V")
    sum = JavaMethod("()D")
    reset = JavaMethod("()V")
    sumThenReset = JavaMethod("()D")
    toString = JavaMethod("()Ljava/lang/String;")
    doubleValue = JavaMethod("()D")
    longValue = JavaMethod("()J")
    intValue = JavaMethod("()I")
    floatValue = JavaMethod("()F")