from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChronoLocalDateTime"]

class ChronoLocalDateTime(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/ChronoLocalDateTime"
    timeLineOrder = JavaStaticMethod("()Ljava/util/Comparator;")
    from = JavaStaticMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoLocalDateTime;")
    getChronology = JavaMethod("()Ljava/time/chrono/Chronology;")
    toLocalDate = JavaMethod("()Ljava/time/chrono/ChronoLocalDate;")
    toLocalTime = JavaMethod("()Ljava/time/LocalTime;")
    isSupported = JavaMultipleMethod([("(Ljava/time/temporal/TemporalField;)Z", False, False), ("(Ljava/time/temporal/TemporalUnit;)Z", False, False)])
    with = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAdjuster;)Ljava/time/chrono/ChronoLocalDateTime;", False, False), ("(Ljava/time/temporal/TemporalField;J)Ljava/time/chrono/ChronoLocalDateTime;", False, False)])
    plus = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAmount;)Ljava/time/chrono/ChronoLocalDateTime;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/chrono/ChronoLocalDateTime;", False, False)])
    minus = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAmount;)Ljava/time/chrono/ChronoLocalDateTime;", False, False), ("(JLjava/time/temporal/TemporalUnit;)Ljava/time/chrono/ChronoLocalDateTime;", False, False)])
    query = JavaMethod("(Ljava/time/temporal/TemporalQuery;)Ljava/lang/Object;")
    adjustInto = JavaMethod("(Ljava/time/temporal/Temporal;)Ljava/time/temporal/Temporal;")
    format = JavaMethod("(Ljava/time/format/DateTimeFormatter;)Ljava/lang/String;")
    atZone = JavaMethod("(Ljava/time/ZoneId;)Ljava/time/chrono/ChronoZonedDateTime;")
    toInstant = JavaMethod("(Ljava/time/ZoneOffset;)Ljava/time/Instant;")
    toEpochSecond = JavaMethod("(Ljava/time/ZoneOffset;)J")
    compareTo = JavaMethod("(Ljava/time/chrono/ChronoLocalDateTime;)I")
    isAfter = JavaMethod("(Ljava/time/chrono/ChronoLocalDateTime;)Z")
    isBefore = JavaMethod("(Ljava/time/chrono/ChronoLocalDateTime;)Z")
    isEqual = JavaMethod("(Ljava/time/chrono/ChronoLocalDateTime;)Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")