from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IsoChronology"]

class IsoChronology(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/IsoChronology"
    INSTANCE = JavaStaticField("Ljava/time/chrono/IsoChronology;")
    getId = JavaMethod("()Ljava/lang/String;")
    period = JavaMultipleMethod([("(III)Ljava/time/chrono/ChronoPeriod;", False, False), ("(III)Ljava/time/Period;", False, False)])
    range = JavaMethod("(Ljava/time/temporal/ChronoField;)Ljava/time/temporal/ValueRange;")
    prolepticYear = JavaMethod("(Ljava/time/chrono/Era;I)I")
    dateYearDay = JavaMultipleMethod([("(II)Ljava/time/LocalDate;", False, False), ("(Ljava/time/chrono/Era;II)Ljava/time/LocalDate;", False, False), ("(Ljava/time/chrono/Era;II)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(II)Ljava/time/chrono/ChronoLocalDate;", False, False)])
    dateNow = JavaMultipleMethod([("(Ljava/time/ZoneId;)Ljava/time/LocalDate;", False, False), ("()Ljava/time/LocalDate;", False, False), ("()Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/Clock;)Ljava/time/LocalDate;", False, False), ("(Ljava/time/ZoneId;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/Clock;)Ljava/time/chrono/ChronoLocalDate;", False, False)])
    dateEpochDay = JavaMultipleMethod([("(J)Ljava/time/LocalDate;", False, False), ("(J)Ljava/time/chrono/ChronoLocalDate;", False, False)])
    resolveDate = JavaMultipleMethod([("(Ljava/util/Map;Ljava/time/format/ResolverStyle;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/util/Map;Ljava/time/format/ResolverStyle;)Ljava/time/LocalDate;", False, False)])
    eras = JavaMethod("()Ljava/util/List;")
    isIsoBased = JavaMethod("()Z")
    date = JavaMultipleMethod([("(Ljava/time/chrono/Era;III)Ljava/time/LocalDate;", False, False), ("(III)Ljava/time/LocalDate;", False, False), ("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/LocalDate;", False, False), ("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(III)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/chrono/Era;III)Ljava/time/chrono/ChronoLocalDate;", False, False)])
    epochSecond = JavaMethod("(IIIIIILjava/time/ZoneOffset;)J")
    localDateTime = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/LocalDateTime;", False, False), ("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoLocalDateTime;", False, False)])
    zonedDateTime = JavaMultipleMethod([("(Ljava/time/Instant;Ljava/time/ZoneId;)Ljava/time/ZonedDateTime;", False, False), ("(Ljava/time/Instant;Ljava/time/ZoneId;)Ljava/time/chrono/ChronoZonedDateTime;", False, False), ("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoZonedDateTime;", False, False), ("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/ZonedDateTime;", False, False)])
    getCalendarType = JavaMethod("()Ljava/lang/String;")
    isLeapYear = JavaMethod("(J)Z")
    eraOf = JavaMultipleMethod([("(I)Ljava/time/chrono/Era;", False, False), ("(I)Ljava/time/chrono/IsoEra;", False, False)])