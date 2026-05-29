from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MinguoDate"]

class MinguoDate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/MinguoDate"
    now = JavaMultipleMethod([("()Ljava/time/chrono/MinguoDate;", True, False), ("(Ljava/time/ZoneId;)Ljava/time/chrono/MinguoDate;", True, False), ("(Ljava/time/Clock;)Ljava/time/chrono/MinguoDate;", True, False)])
    of = JavaStaticMethod("(III)Ljava/time/chrono/MinguoDate;")
    from = JavaStaticMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/MinguoDate;")
    getChronology = JavaMethod("()Ljava/time/chrono/MinguoChronology;")
    getEra = JavaMethod("()Ljava/time/chrono/MinguoEra;")
    lengthOfMonth = JavaMethod("()I")
    range = JavaMethod("(Ljava/time/temporal/TemporalField;)Ljava/time/temporal/ValueRange;")
    getLong = JavaMethod("(Ljava/time/temporal/TemporalField;)J")
    with = JavaMultipleMethod([("(Ljava/time/temporal/TemporalField;J)Ljava/time/chrono/MinguoDate;", False, False), ("(Ljava/time/temporal/TemporalAdjuster;)Ljava/time/chrono/MinguoDate;", False, False)])
    plus = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAmount;)Ljava/time/chrono/MinguoDate;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/chrono/MinguoDate;", False, False)])
    minus = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAmount;)Ljava/time/chrono/MinguoDate;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/chrono/MinguoDate;", False, False)])
    atTime = JavaMethod("(Ljava/time/LocalTime;)Ljava/time/chrono/ChronoLocalDateTime;")
    until = JavaMultipleMethod([("(Ljava/time/chrono/ChronoLocalDate;)Ljava/time/chrono/ChronoPeriod;", False, False), ("(Ljava/time/temporal/Temporal;Ljava/time/temporal/TemporalUnit;)J", False, False)])
    toEpochDay = JavaMethod("()J")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")