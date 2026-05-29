from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ThaiBuddhistChronology"]

class ThaiBuddhistChronology(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/ThaiBuddhistChronology"
    INSTANCE = JavaStaticField("Ljava/time/chrono/ThaiBuddhistChronology;")
    getId = JavaMethod("()Ljava/lang/String;")
    range = JavaMethod("(Ljava/time/temporal/ChronoField;)Ljava/time/temporal/ValueRange;")
    prolepticYear = JavaMethod("(Ljava/time/chrono/Era;I)I")
    dateYearDay = JavaMultipleMethod([("(Ljava/time/chrono/Era;II)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(II)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/chrono/Era;II)Ljava/time/chrono/ThaiBuddhistDate;", False, False), ("(II)Ljava/time/chrono/ThaiBuddhistDate;", False, False)])
    dateNow = JavaMultipleMethod([("(Ljava/time/ZoneId;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/Clock;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/ZoneId;)Ljava/time/chrono/ThaiBuddhistDate;", False, False), ("()Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/Clock;)Ljava/time/chrono/ThaiBuddhistDate;", False, False), ("()Ljava/time/chrono/ThaiBuddhistDate;", False, False)])
    dateEpochDay = JavaMultipleMethod([("(J)Ljava/time/chrono/ThaiBuddhistDate;", False, False), ("(J)Ljava/time/chrono/ChronoLocalDate;", False, False)])
    resolveDate = JavaMultipleMethod([("(Ljava/util/Map;Ljava/time/format/ResolverStyle;)Ljava/time/chrono/ThaiBuddhistDate;", False, False), ("(Ljava/util/Map;Ljava/time/format/ResolverStyle;)Ljava/time/chrono/ChronoLocalDate;", False, False)])
    eras = JavaMethod("()Ljava/util/List;")
    isIsoBased = JavaMethod("()Z")
    date = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/chrono/Era;III)Ljava/time/chrono/ThaiBuddhistDate;", False, False), ("(III)Ljava/time/chrono/ThaiBuddhistDate;", False, False), ("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ThaiBuddhistDate;", False, False), ("(III)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/chrono/Era;III)Ljava/time/chrono/ChronoLocalDate;", False, False)])
    localDateTime = JavaMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoLocalDateTime;")
    zonedDateTime = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoZonedDateTime;", False, False), ("(Ljava/time/Instant;Ljava/time/ZoneId;)Ljava/time/chrono/ChronoZonedDateTime;", False, False)])
    getCalendarType = JavaMethod("()Ljava/lang/String;")
    isLeapYear = JavaMethod("(J)Z")
    eraOf = JavaMultipleMethod([("(I)Ljava/time/chrono/ThaiBuddhistEra;", False, False), ("(I)Ljava/time/chrono/Era;", False, False)])