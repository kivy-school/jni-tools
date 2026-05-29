from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChronoLocalDateTime"]

class ChronoLocalDateTime(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/ChronoLocalDateTime"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Ljava/time/chrono/ChronoLocalDateTime;)I", False, False)])
    format = JavaMethod("(Ljava/time/format/DateTimeFormatter;)Ljava/lang/String;")
    from = JavaStaticMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoLocalDateTime;")
    isSupported = JavaMultipleMethod([("(Ljava/time/temporal/TemporalField;)Z", False, False), ("(Ljava/time/temporal/TemporalUnit;)Z", False, False)])
    with = JavaMultipleMethod([("(Ljava/time/temporal/TemporalField;J)Ljava/time/temporal/Temporal;", False, False), ("(Ljava/time/temporal/TemporalAdjuster;)Ljava/time/chrono/ChronoLocalDateTime;", False, False), ("(Ljava/time/temporal/TemporalAdjuster;)Ljava/time/temporal/Temporal;", False, False), ("(Ljava/time/temporal/TemporalField;J)Ljava/time/chrono/ChronoLocalDateTime;", False, False)])
    query = JavaMethod("(Ljava/time/temporal/TemporalQuery;)Ljava/lang/Object;")
    isEqual = JavaMethod("(Ljava/time/chrono/ChronoLocalDateTime;)Z")
    atZone = JavaMethod("(Ljava/time/ZoneId;)Ljava/time/chrono/ChronoZonedDateTime;")
    toLocalDate = JavaMethod("()Ljava/time/chrono/ChronoLocalDate;")
    plus = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAmount;)Ljava/time/chrono/ChronoLocalDateTime;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/chrono/ChronoLocalDateTime;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/temporal/Temporal;", False, False), ("(Ljava/time/temporal/TemporalAmount;)Ljava/time/temporal/Temporal;", False, False)])
    minus = JavaMultipleMethod([("(JLjava/time/temporal/TemporalUnit;)Ljava/time/chrono/ChronoLocalDateTime;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/temporal/Temporal;", False, False), ("(Ljava/time/temporal/TemporalAmount;)Ljava/time/temporal/Temporal;", False, False), ("(Ljava/time/temporal/TemporalAmount;)Ljava/time/chrono/ChronoLocalDateTime;", False, False)])
    getChronology = JavaMethod("()Ljava/time/chrono/Chronology;")
    adjustInto = JavaMethod("(Ljava/time/temporal/Temporal;)Ljava/time/temporal/Temporal;")
    toLocalTime = JavaMethod("()Ljava/time/LocalTime;")
    isAfter = JavaMethod("(Ljava/time/chrono/ChronoLocalDateTime;)Z")
    isBefore = JavaMethod("(Ljava/time/chrono/ChronoLocalDateTime;)Z")
    timeLineOrder = JavaStaticMethod("()Ljava/util/Comparator;")
    toEpochSecond = JavaMethod("(Ljava/time/ZoneOffset;)J")
    toInstant = JavaMethod("(Ljava/time/ZoneOffset;)Ljava/time/Instant;")