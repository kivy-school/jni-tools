from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChronoLocalDate"]

class ChronoLocalDate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/ChronoLocalDate"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/time/chrono/ChronoLocalDate;)I", False, False), ("(Ljava/lang/Object;)I", False, False)])
    format = JavaMethod("(Ljava/time/format/DateTimeFormatter;)Ljava/lang/String;")
    from = JavaStaticMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoLocalDate;")
    isSupported = JavaMultipleMethod([("(Ljava/time/temporal/TemporalUnit;)Z", False, False), ("(Ljava/time/temporal/TemporalField;)Z", False, False)])
    with = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAdjuster;)Ljava/time/temporal/Temporal;", False, False), ("(Ljava/time/temporal/TemporalField;J)Ljava/time/temporal/Temporal;", False, False), ("(Ljava/time/temporal/TemporalField;J)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/temporal/TemporalAdjuster;)Ljava/time/chrono/ChronoLocalDate;", False, False)])
    query = JavaMethod("(Ljava/time/temporal/TemporalQuery;)Ljava/lang/Object;")
    isEqual = JavaMethod("(Ljava/time/chrono/ChronoLocalDate;)Z")
    plus = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAmount;)Ljava/time/temporal/Temporal;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/temporal/Temporal;", False, False), ("(Ljava/time/temporal/TemporalAmount;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/chrono/ChronoLocalDate;", False, False)])
    until = JavaMultipleMethod([("(Ljava/time/chrono/ChronoLocalDate;)Ljava/time/chrono/ChronoPeriod;", False, False), ("(Ljava/time/temporal/Temporal;Ljava/time/temporal/TemporalUnit;)J", False, False)])
    minus = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAmount;)Ljava/time/temporal/Temporal;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/temporal/Temporal;", False, False), ("(Ljava/time/temporal/TemporalAmount;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/chrono/ChronoLocalDate;", False, False)])
    getChronology = JavaMethod("()Ljava/time/chrono/Chronology;")
    isLeapYear = JavaMethod("()Z")
    lengthOfMonth = JavaMethod("()I")
    lengthOfYear = JavaMethod("()I")
    toEpochDay = JavaMethod("()J")
    adjustInto = JavaMethod("(Ljava/time/temporal/Temporal;)Ljava/time/temporal/Temporal;")
    atTime = JavaMethod("(Ljava/time/LocalTime;)Ljava/time/chrono/ChronoLocalDateTime;")
    isAfter = JavaMethod("(Ljava/time/chrono/ChronoLocalDate;)Z")
    isBefore = JavaMethod("(Ljava/time/chrono/ChronoLocalDate;)Z")
    getEra = JavaMethod("()Ljava/time/chrono/Era;")
    timeLineOrder = JavaStaticMethod("()Ljava/util/Comparator;")