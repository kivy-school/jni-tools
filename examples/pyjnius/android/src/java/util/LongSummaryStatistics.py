from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LongSummaryStatistics"]

class LongSummaryStatistics(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/LongSummaryStatistics"
    __javaconstructor__ = [("()V", False), ("(JJJJ)V", False)]
    combine = JavaMethod("(Ljava/util/LongSummaryStatistics;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    accept = JavaMultipleMethod([("(J)V", False, False), ("(I)V", False, False)])
    getCount = JavaMethod("()J")
    getMax = JavaMethod("()J")
    getMin = JavaMethod("()J")
    getSum = JavaMethod("()J")
    getAverage = JavaMethod("()D")