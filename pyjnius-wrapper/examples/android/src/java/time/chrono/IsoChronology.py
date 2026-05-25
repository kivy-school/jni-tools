from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IsoChronology"]

class IsoChronology(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/IsoChronology"
    INSTANCE = JavaStaticField("Ljava/time/chrono/IsoChronology;")
    getId = JavaMethod("()Ljava/lang/String;")
    getCalendarType = JavaMethod("()Ljava/lang/String;")
    date = JavaMultipleMethod([("(Ljava/time/chrono/Era;III)Ljava/time/LocalDate;", False, False), ("(III)Ljava/time/LocalDate;", False, False), ("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/LocalDate;", False, False)])
    dateYearDay = JavaMultipleMethod([("(Ljava/time/chrono/Era;II)Ljava/time/LocalDate;", False, False), ("(II)Ljava/time/LocalDate;", False, False)])
    dateEpochDay = JavaMethod("(J)Ljava/time/LocalDate;")
    epochSecond = JavaMethod("(IIIIIILjava/time/ZoneOffset;)J")
    localDateTime = JavaMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/LocalDateTime;")
    zonedDateTime = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/ZonedDateTime;", False, False), ("(Ljava/time/Instant;Ljava/time/ZoneId;)Ljava/time/ZonedDateTime;", False, False)])
    dateNow = JavaMultipleMethod([("()Ljava/time/LocalDate;", False, False), ("(Ljava/time/ZoneId;)Ljava/time/LocalDate;", False, False), ("(Ljava/time/Clock;)Ljava/time/LocalDate;", False, False)])
    isLeapYear = JavaMethod("(J)Z")
    prolepticYear = JavaMethod("(Ljava/time/chrono/Era;I)I")
    eraOf = JavaMethod("(I)Ljava/time/chrono/IsoEra;")
    eras = JavaMethod("()Ljava/util/List;")
    resolveDate = JavaMethod("(Ljava/util/Map;Ljava/time/format/ResolverStyle;)Ljava/time/LocalDate;")
    range = JavaMethod("(Ljava/time/temporal/ChronoField;)Ljava/time/temporal/ValueRange;")
    period = JavaMethod("(III)Ljava/time/Period;")