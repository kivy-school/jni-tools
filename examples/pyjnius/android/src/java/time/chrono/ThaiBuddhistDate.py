from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ThaiBuddhistDate"]

class ThaiBuddhistDate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/ThaiBuddhistDate"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getLong = JavaMethod("(Ljava/time/temporal/TemporalField;)J")
    of = JavaStaticMethod("(III)Ljava/time/chrono/ThaiBuddhistDate;")
    from = JavaStaticMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ThaiBuddhistDate;")
    with = JavaMultipleMethod([("(Ljava/time/temporal/TemporalField;J)Ljava/time/chrono/ThaiBuddhistDate;", False, False), ("(Ljava/time/temporal/TemporalAdjuster;)Ljava/time/chrono/ThaiBuddhistDate;", False, False), ("(Ljava/time/temporal/TemporalField;J)Ljava/time/temporal/Temporal;", False, False), ("(Ljava/time/temporal/TemporalAdjuster;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/temporal/TemporalField;J)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/temporal/TemporalAdjuster;)Ljava/time/temporal/Temporal;", False, False)])
    now = JavaMultipleMethod([("()Ljava/time/chrono/ThaiBuddhistDate;", True, False), ("(Ljava/time/Clock;)Ljava/time/chrono/ThaiBuddhistDate;", True, False), ("(Ljava/time/ZoneId;)Ljava/time/chrono/ThaiBuddhistDate;", True, False)])
    range = JavaMethod("(Ljava/time/temporal/TemporalField;)Ljava/time/temporal/ValueRange;")
    plus = JavaMultipleMethod([("(JLjava/time/temporal/TemporalUnit;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/temporal/TemporalAmount;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/temporal/TemporalAmount;)Ljava/time/chrono/ThaiBuddhistDate;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/temporal/Temporal;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/chrono/ThaiBuddhistDate;", False, False), ("(Ljava/time/temporal/TemporalAmount;)Ljava/time/temporal/Temporal;", False, False)])
    until = JavaMultipleMethod([("(Ljava/time/temporal/Temporal;Ljava/time/temporal/TemporalUnit;)J", False, False), ("(Ljava/time/chrono/ChronoLocalDate;)Ljava/time/chrono/ChronoPeriod;", False, False)])
    minus = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAmount;)Ljava/time/temporal/Temporal;", False, False), ("(Ljava/time/temporal/TemporalAmount;)Ljava/time/chrono/ThaiBuddhistDate;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/temporal/Temporal;", False, False), ("(Ljava/time/temporal/TemporalAmount;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/chrono/ThaiBuddhistDate;", False, False)])
    getChronology = JavaMultipleMethod([("()Ljava/time/chrono/Chronology;", False, False), ("()Ljava/time/chrono/ThaiBuddhistChronology;", False, False)])
    lengthOfMonth = JavaMethod("()I")
    toEpochDay = JavaMethod("()J")
    atTime = JavaMethod("(Ljava/time/LocalTime;)Ljava/time/chrono/ChronoLocalDateTime;")
    getEra = JavaMultipleMethod([("()Ljava/time/chrono/ThaiBuddhistEra;", False, False), ("()Ljava/time/chrono/Era;", False, False)])