from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HijrahChronology"]

class HijrahChronology(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/HijrahChronology"
    INSTANCE = JavaStaticField("Ljava/time/chrono/HijrahChronology;")
    getId = JavaMethod("()Ljava/lang/String;")
    getCalendarType = JavaMethod("()Ljava/lang/String;")
    date = JavaMultipleMethod([("(Ljava/time/chrono/Era;III)Ljava/time/chrono/HijrahDate;", False, False), ("(III)Ljava/time/chrono/HijrahDate;", False, False), ("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/HijrahDate;", False, False)])
    dateYearDay = JavaMultipleMethod([("(Ljava/time/chrono/Era;II)Ljava/time/chrono/HijrahDate;", False, False), ("(II)Ljava/time/chrono/HijrahDate;", False, False)])
    dateEpochDay = JavaMethod("(J)Ljava/time/chrono/HijrahDate;")
    dateNow = JavaMultipleMethod([("()Ljava/time/chrono/HijrahDate;", False, False), ("(Ljava/time/ZoneId;)Ljava/time/chrono/HijrahDate;", False, False), ("(Ljava/time/Clock;)Ljava/time/chrono/HijrahDate;", False, False)])
    localDateTime = JavaMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoLocalDateTime;")
    zonedDateTime = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoZonedDateTime;", False, False), ("(Ljava/time/Instant;Ljava/time/ZoneId;)Ljava/time/chrono/ChronoZonedDateTime;", False, False)])
    isLeapYear = JavaMethod("(J)Z")
    prolepticYear = JavaMethod("(Ljava/time/chrono/Era;I)I")
    eraOf = JavaMethod("(I)Ljava/time/chrono/HijrahEra;")
    eras = JavaMethod("()Ljava/util/List;")
    range = JavaMethod("(Ljava/time/temporal/ChronoField;)Ljava/time/temporal/ValueRange;")
    resolveDate = JavaMethod("(Ljava/util/Map;Ljava/time/format/ResolverStyle;)Ljava/time/chrono/HijrahDate;")