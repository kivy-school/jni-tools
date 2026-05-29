from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WeekFields"]

class WeekFields(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/temporal/WeekFields"
    ISO = JavaStaticField("Ljava/time/temporal/WeekFields;")
    SUNDAY_START = JavaStaticField("Ljava/time/temporal/WeekFields;")
    WEEK_BASED_YEARS = JavaStaticField("Ljava/time/temporal/TemporalUnit;")
    of = JavaMultipleMethod([("(Ljava/util/Locale;)Ljava/time/temporal/WeekFields;", True, False), ("(Ljava/time/DayOfWeek;I)Ljava/time/temporal/WeekFields;", True, False)])
    getFirstDayOfWeek = JavaMethod("()Ljava/time/DayOfWeek;")
    getMinimalDaysInFirstWeek = JavaMethod("()I")
    dayOfWeek = JavaMethod("()Ljava/time/temporal/TemporalField;")
    weekOfMonth = JavaMethod("()Ljava/time/temporal/TemporalField;")
    weekOfYear = JavaMethod("()Ljava/time/temporal/TemporalField;")
    weekOfWeekBasedYear = JavaMethod("()Ljava/time/temporal/TemporalField;")
    weekBasedYear = JavaMethod("()Ljava/time/temporal/TemporalField;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")