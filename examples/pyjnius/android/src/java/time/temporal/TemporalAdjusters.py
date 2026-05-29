from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TemporalAdjusters"]

class TemporalAdjusters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/temporal/TemporalAdjusters"
    next = JavaStaticMethod("(Ljava/time/DayOfWeek;)Ljava/time/temporal/TemporalAdjuster;")
    lastDayOfMonth = JavaStaticMethod("()Ljava/time/temporal/TemporalAdjuster;")
    nextOrSame = JavaStaticMethod("(Ljava/time/DayOfWeek;)Ljava/time/temporal/TemporalAdjuster;")
    previous = JavaStaticMethod("(Ljava/time/DayOfWeek;)Ljava/time/temporal/TemporalAdjuster;")
    firstDayOfYear = JavaStaticMethod("()Ljava/time/temporal/TemporalAdjuster;")
    previousOrSame = JavaStaticMethod("(Ljava/time/DayOfWeek;)Ljava/time/temporal/TemporalAdjuster;")
    dayOfWeekInMonth = JavaStaticMethod("(ILjava/time/DayOfWeek;)Ljava/time/temporal/TemporalAdjuster;")
    ofDateAdjuster = JavaStaticMethod("(Ljava/util/function/UnaryOperator;)Ljava/time/temporal/TemporalAdjuster;")
    firstDayOfMonth = JavaStaticMethod("()Ljava/time/temporal/TemporalAdjuster;")
    firstDayOfNextMonth = JavaStaticMethod("()Ljava/time/temporal/TemporalAdjuster;")
    lastDayOfYear = JavaStaticMethod("()Ljava/time/temporal/TemporalAdjuster;")
    firstDayOfNextYear = JavaStaticMethod("()Ljava/time/temporal/TemporalAdjuster;")
    firstInMonth = JavaStaticMethod("(Ljava/time/DayOfWeek;)Ljava/time/temporal/TemporalAdjuster;")
    lastInMonth = JavaStaticMethod("(Ljava/time/DayOfWeek;)Ljava/time/temporal/TemporalAdjuster;")