from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HijrahDate"]

class HijrahDate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/HijrahDate"
    now = JavaMultipleMethod([("()Ljava/time/chrono/HijrahDate;", True, False), ("(Ljava/time/ZoneId;)Ljava/time/chrono/HijrahDate;", True, False), ("(Ljava/time/Clock;)Ljava/time/chrono/HijrahDate;", True, False)])
    of = JavaStaticMethod("(III)Ljava/time/chrono/HijrahDate;")
    from = JavaStaticMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/HijrahDate;")
    getChronology = JavaMethod("()Ljava/time/chrono/HijrahChronology;")
    getEra = JavaMethod("()Ljava/time/chrono/HijrahEra;")
    lengthOfMonth = JavaMethod("()I")
    lengthOfYear = JavaMethod("()I")
    range = JavaMethod("(Ljava/time/temporal/TemporalField;)Ljava/time/temporal/ValueRange;")
    getLong = JavaMethod("(Ljava/time/temporal/TemporalField;)J")
    with = JavaMultipleMethod([("(Ljava/time/temporal/TemporalField;J)Ljava/time/chrono/HijrahDate;", False, False), ("(Ljava/time/temporal/TemporalAdjuster;)Ljava/time/chrono/HijrahDate;", False, False)])
    withVariant = JavaMethod("(Ljava/time/chrono/HijrahChronology;)Ljava/time/chrono/HijrahDate;")
    plus = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAmount;)Ljava/time/chrono/HijrahDate;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/chrono/HijrahDate;", False, False)])
    minus = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAmount;)Ljava/time/chrono/HijrahDate;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/chrono/HijrahDate;", False, False)])
    toEpochDay = JavaMethod("()J")
    isLeapYear = JavaMethod("()Z")
    atTime = JavaMethod("(Ljava/time/LocalTime;)Ljava/time/chrono/ChronoLocalDateTime;")
    until = JavaMultipleMethod([("(Ljava/time/chrono/ChronoLocalDate;)Ljava/time/chrono/ChronoPeriod;", False, False), ("(Ljava/time/temporal/Temporal;Ljava/time/temporal/TemporalUnit;)J", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")