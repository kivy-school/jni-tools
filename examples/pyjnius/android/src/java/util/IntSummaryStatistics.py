from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntSummaryStatistics"]

class IntSummaryStatistics(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/IntSummaryStatistics"
    __javaconstructor__ = [("()V", False), ("(JIIJ)V", False)]
    combine = JavaMethod("(Ljava/util/IntSummaryStatistics;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    accept = JavaMethod("(I)V")
    getCount = JavaMethod("()J")
    getMax = JavaMethod("()I")
    getMin = JavaMethod("()I")
    getSum = JavaMethod("()J")
    getAverage = JavaMethod("()D")