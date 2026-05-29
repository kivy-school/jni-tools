from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DoubleSummaryStatistics"]

class DoubleSummaryStatistics(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/DoubleSummaryStatistics"
    __javaconstructor__ = [("()V", False), ("(JDDD)V", False)]
    combine = JavaMethod("(Ljava/util/DoubleSummaryStatistics;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    accept = JavaMethod("(D)V")
    getCount = JavaMethod("()J")
    getMax = JavaMethod("()D")
    getMin = JavaMethod("()D")
    getSum = JavaMethod("()D")
    getAverage = JavaMethod("()D")