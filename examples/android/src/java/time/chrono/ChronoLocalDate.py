from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChronoLocalDate"]

class ChronoLocalDate(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/ChronoLocalDate"
    timeLineOrder = JavaStaticMethod("()Ljava/util/Comparator;")
    from = JavaStaticMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoLocalDate;")
    getChronology = JavaMethod("()Ljava/time/chrono/Chronology;")
    getEra = JavaMethod("()Ljava/time/chrono/Era;")
    isLeapYear = JavaMethod("()Z")
    lengthOfMonth = JavaMethod("()I")
    lengthOfYear = JavaMethod("()I")
    isSupported = JavaMultipleMethod([("(Ljava/time/temporal/TemporalField;)Z", False, False), ("(Ljava/time/temporal/TemporalUnit;)Z", False, False)])
    with = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAdjuster;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/temporal/TemporalField;J)Ljava/time/chrono/ChronoLocalDate;", False, False)])
    plus = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAmount;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/chrono/ChronoLocalDate;", False, False)])
    minus = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAmount;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/chrono/ChronoLocalDate;", False, False)])
    query = JavaMethod("(Ljava/time/temporal/TemporalQuery;)Ljava/lang/Object;")
    adjustInto = JavaMethod("(Ljava/time/temporal/Temporal;)Ljava/time/temporal/Temporal;")
    until = JavaMultipleMethod([("(Ljava/time/temporal/Temporal;Ljava/time/temporal/TemporalUnit;)J", False, False), ("(Ljava/time/chrono/ChronoLocalDate;)Ljava/time/chrono/ChronoPeriod;", False, False)])
    format = JavaMethod("(Ljava/time/format/DateTimeFormatter;)Ljava/lang/String;")
    atTime = JavaMethod("(Ljava/time/LocalTime;)Ljava/time/chrono/ChronoLocalDateTime;")
    toEpochDay = JavaMethod("()J")
    compareTo = JavaMethod("(Ljava/time/chrono/ChronoLocalDate;)I")
    isAfter = JavaMethod("(Ljava/time/chrono/ChronoLocalDate;)Z")
    isBefore = JavaMethod("(Ljava/time/chrono/ChronoLocalDate;)Z")
    isEqual = JavaMethod("(Ljava/time/chrono/ChronoLocalDate;)Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")