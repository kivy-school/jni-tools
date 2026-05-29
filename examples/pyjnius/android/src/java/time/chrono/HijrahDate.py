from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HijrahDate"]

class HijrahDate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/HijrahDate"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getLong = JavaMethod("(Ljava/time/temporal/TemporalField;)J")
    of = JavaStaticMethod("(III)Ljava/time/chrono/HijrahDate;")
    from = JavaStaticMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/HijrahDate;")
    with = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAdjuster;)Ljava/time/chrono/HijrahDate;", False, False), ("(Ljava/time/temporal/TemporalField;J)Ljava/time/temporal/Temporal;", False, False), ("(Ljava/time/temporal/TemporalField;J)Ljava/time/chrono/HijrahDate;", False, False), ("(Ljava/time/temporal/TemporalAdjuster;)Ljava/time/temporal/Temporal;", False, False), ("(Ljava/time/temporal/TemporalAdjuster;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/temporal/TemporalField;J)Ljava/time/chrono/ChronoLocalDate;", False, False)])
    now = JavaMultipleMethod([("(Ljava/time/ZoneId;)Ljava/time/chrono/HijrahDate;", True, False), ("()Ljava/time/chrono/HijrahDate;", True, False), ("(Ljava/time/Clock;)Ljava/time/chrono/HijrahDate;", True, False)])
    range = JavaMethod("(Ljava/time/temporal/TemporalField;)Ljava/time/temporal/ValueRange;")
    withVariant = JavaMethod("(Ljava/time/chrono/HijrahChronology;)Ljava/time/chrono/HijrahDate;")
    plus = JavaMultipleMethod([("(JLjava/time/temporal/TemporalUnit;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/temporal/TemporalAmount;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/temporal/TemporalAmount;)Ljava/time/temporal/Temporal;", False, False), ("(Ljava/time/temporal/TemporalAmount;)Ljava/time/chrono/HijrahDate;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/chrono/HijrahDate;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/temporal/Temporal;", False, False)])
    until = JavaMultipleMethod([("(Ljava/time/chrono/ChronoLocalDate;)Ljava/time/chrono/ChronoPeriod;", False, False), ("(Ljava/time/temporal/Temporal;Ljava/time/temporal/TemporalUnit;)J", False, False)])
    minus = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAmount;)Ljava/time/temporal/Temporal;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/temporal/Temporal;", False, False), ("(Ljava/time/temporal/TemporalAmount;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/chrono/HijrahDate;", False, False), ("(Ljava/time/temporal/TemporalAmount;)Ljava/time/chrono/HijrahDate;", False, False)])
    getChronology = JavaMultipleMethod([("()Ljava/time/chrono/HijrahChronology;", False, False), ("()Ljava/time/chrono/Chronology;", False, False)])
    isLeapYear = JavaMethod("()Z")
    lengthOfMonth = JavaMethod("()I")
    lengthOfYear = JavaMethod("()I")
    toEpochDay = JavaMethod("()J")
    atTime = JavaMethod("(Ljava/time/LocalTime;)Ljava/time/chrono/ChronoLocalDateTime;")
    getEra = JavaMultipleMethod([("()Ljava/time/chrono/HijrahEra;", False, False), ("()Ljava/time/chrono/Era;", False, False)])