from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntSummaryStatistics"]

class IntSummaryStatistics(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/IntSummaryStatistics"
    __javaconstructor__ = [("()V", False), ("(JIIJ)V", False)]
    accept = JavaMethod("(I)V")
    combine = JavaMethod("(Ljava/util/IntSummaryStatistics;)V")
    getCount = JavaMethod("()J")
    getSum = JavaMethod("()J")
    getMin = JavaMethod("()I")
    getMax = JavaMethod("()I")
    getAverage = JavaMethod("()D")
    toString = JavaMethod("()Ljava/lang/String;")