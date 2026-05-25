from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ThaiBuddhistDate"]

class ThaiBuddhistDate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/ThaiBuddhistDate"
    now = JavaMultipleMethod([("()Ljava/time/chrono/ThaiBuddhistDate;", True, False), ("(Ljava/time/ZoneId;)Ljava/time/chrono/ThaiBuddhistDate;", True, False), ("(Ljava/time/Clock;)Ljava/time/chrono/ThaiBuddhistDate;", True, False)])
    of = JavaStaticMethod("(III)Ljava/time/chrono/ThaiBuddhistDate;")
    from = JavaStaticMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ThaiBuddhistDate;")
    getChronology = JavaMethod("()Ljava/time/chrono/ThaiBuddhistChronology;")
    getEra = JavaMethod("()Ljava/time/chrono/ThaiBuddhistEra;")
    lengthOfMonth = JavaMethod("()I")
    range = JavaMethod("(Ljava/time/temporal/TemporalField;)Ljava/time/temporal/ValueRange;")
    getLong = JavaMethod("(Ljava/time/temporal/TemporalField;)J")
    with = JavaMultipleMethod([("(Ljava/time/temporal/TemporalField;J)Ljava/time/chrono/ThaiBuddhistDate;", False, False), ("(Ljava/time/temporal/TemporalAdjuster;)Ljava/time/chrono/ThaiBuddhistDate;", False, False)])
    plus = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAmount;)Ljava/time/chrono/ThaiBuddhistDate;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/chrono/ThaiBuddhistDate;", False, False)])
    minus = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAmount;)Ljava/time/chrono/ThaiBuddhistDate;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/chrono/ThaiBuddhistDate;", False, False)])
    atTime = JavaMethod("(Ljava/time/LocalTime;)Ljava/time/chrono/ChronoLocalDateTime;")
    until = JavaMultipleMethod([("(Ljava/time/chrono/ChronoLocalDate;)Ljava/time/chrono/ChronoPeriod;", False, False), ("(Ljava/time/temporal/Temporal;Ljava/time/temporal/TemporalUnit;)J", False, False)])
    toEpochDay = JavaMethod("()J")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")