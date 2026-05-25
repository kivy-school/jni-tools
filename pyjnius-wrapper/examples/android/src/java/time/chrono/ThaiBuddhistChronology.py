from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ThaiBuddhistChronology"]

class ThaiBuddhistChronology(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/ThaiBuddhistChronology"
    INSTANCE = JavaStaticField("Ljava/time/chrono/ThaiBuddhistChronology;")
    getId = JavaMethod("()Ljava/lang/String;")
    getCalendarType = JavaMethod("()Ljava/lang/String;")
    date = JavaMultipleMethod([("(Ljava/time/chrono/Era;III)Ljava/time/chrono/ThaiBuddhistDate;", False, False), ("(III)Ljava/time/chrono/ThaiBuddhistDate;", False, False), ("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ThaiBuddhistDate;", False, False)])
    dateYearDay = JavaMultipleMethod([("(Ljava/time/chrono/Era;II)Ljava/time/chrono/ThaiBuddhistDate;", False, False), ("(II)Ljava/time/chrono/ThaiBuddhistDate;", False, False)])
    dateEpochDay = JavaMethod("(J)Ljava/time/chrono/ThaiBuddhistDate;")
    dateNow = JavaMultipleMethod([("()Ljava/time/chrono/ThaiBuddhistDate;", False, False), ("(Ljava/time/ZoneId;)Ljava/time/chrono/ThaiBuddhistDate;", False, False), ("(Ljava/time/Clock;)Ljava/time/chrono/ThaiBuddhistDate;", False, False)])
    localDateTime = JavaMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoLocalDateTime;")
    zonedDateTime = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoZonedDateTime;", False, False), ("(Ljava/time/Instant;Ljava/time/ZoneId;)Ljava/time/chrono/ChronoZonedDateTime;", False, False)])
    isLeapYear = JavaMethod("(J)Z")
    prolepticYear = JavaMethod("(Ljava/time/chrono/Era;I)I")
    eraOf = JavaMethod("(I)Ljava/time/chrono/ThaiBuddhistEra;")
    eras = JavaMethod("()Ljava/util/List;")
    range = JavaMethod("(Ljava/time/temporal/ChronoField;)Ljava/time/temporal/ValueRange;")
    resolveDate = JavaMethod("(Ljava/util/Map;Ljava/time/format/ResolverStyle;)Ljava/time/chrono/ThaiBuddhistDate;")