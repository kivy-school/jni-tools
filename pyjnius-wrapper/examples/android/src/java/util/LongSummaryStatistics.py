from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LongSummaryStatistics"]

class LongSummaryStatistics(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/LongSummaryStatistics"
    __javaconstructor__ = [("()V", False), ("(JJJJ)V", False)]
    accept = JavaMultipleMethod([("(I)V", False, False), ("(J)V", False, False)])
    combine = JavaMethod("(Ljava/util/LongSummaryStatistics;)V")
    getCount = JavaMethod("()J")
    getSum = JavaMethod("()J")
    getMin = JavaMethod("()J")
    getMax = JavaMethod("()J")
    getAverage = JavaMethod("()D")
    toString = JavaMethod("()Ljava/lang/String;")