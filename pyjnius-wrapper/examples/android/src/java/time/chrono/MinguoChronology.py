from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MinguoChronology"]

class MinguoChronology(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/MinguoChronology"
    INSTANCE = JavaStaticField("Ljava/time/chrono/MinguoChronology;")
    getId = JavaMethod("()Ljava/lang/String;")
    getCalendarType = JavaMethod("()Ljava/lang/String;")
    date = JavaMultipleMethod([("(Ljava/time/chrono/Era;III)Ljava/time/chrono/MinguoDate;", False, False), ("(III)Ljava/time/chrono/MinguoDate;", False, False), ("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/MinguoDate;", False, False)])
    dateYearDay = JavaMultipleMethod([("(Ljava/time/chrono/Era;II)Ljava/time/chrono/MinguoDate;", False, False), ("(II)Ljava/time/chrono/MinguoDate;", False, False)])
    dateEpochDay = JavaMethod("(J)Ljava/time/chrono/MinguoDate;")
    dateNow = JavaMultipleMethod([("()Ljava/time/chrono/MinguoDate;", False, False), ("(Ljava/time/ZoneId;)Ljava/time/chrono/MinguoDate;", False, False), ("(Ljava/time/Clock;)Ljava/time/chrono/MinguoDate;", False, False)])
    localDateTime = JavaMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoLocalDateTime;")
    zonedDateTime = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoZonedDateTime;", False, False), ("(Ljava/time/Instant;Ljava/time/ZoneId;)Ljava/time/chrono/ChronoZonedDateTime;", False, False)])
    isLeapYear = JavaMethod("(J)Z")
    prolepticYear = JavaMethod("(Ljava/time/chrono/Era;I)I")
    eraOf = JavaMethod("(I)Ljava/time/chrono/MinguoEra;")
    eras = JavaMethod("()Ljava/util/List;")
    range = JavaMethod("(Ljava/time/temporal/ChronoField;)Ljava/time/temporal/ValueRange;")
    resolveDate = JavaMethod("(Ljava/util/Map;Ljava/time/format/ResolverStyle;)Ljava/time/chrono/MinguoDate;")