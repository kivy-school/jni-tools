from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DoubleSummaryStatistics"]

class DoubleSummaryStatistics(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/DoubleSummaryStatistics"
    __javaconstructor__ = [("()V", False), ("(JDDD)V", False)]
    accept = JavaMethod("(D)V")
    combine = JavaMethod("(Ljava/util/DoubleSummaryStatistics;)V")
    getCount = JavaMethod("()J")
    getSum = JavaMethod("()D")
    getMin = JavaMethod("()D")
    getMax = JavaMethod("()D")
    getAverage = JavaMethod("()D")
    toString = JavaMethod("()Ljava/lang/String;")