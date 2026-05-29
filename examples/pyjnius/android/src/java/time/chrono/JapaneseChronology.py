from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JapaneseChronology"]

class JapaneseChronology(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/JapaneseChronology"
    INSTANCE = JavaStaticField("Ljava/time/chrono/JapaneseChronology;")
    getId = JavaMethod("()Ljava/lang/String;")
    range = JavaMethod("(Ljava/time/temporal/ChronoField;)Ljava/time/temporal/ValueRange;")
    prolepticYear = JavaMethod("(Ljava/time/chrono/Era;I)I")
    dateYearDay = JavaMultipleMethod([("(II)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/chrono/Era;II)Ljava/time/chrono/JapaneseDate;", False, False), ("(Ljava/time/chrono/Era;II)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(II)Ljava/time/chrono/JapaneseDate;", False, False)])
    dateNow = JavaMultipleMethod([("()Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/ZoneId;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/Clock;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("()Ljava/time/chrono/JapaneseDate;", False, False), ("(Ljava/time/ZoneId;)Ljava/time/chrono/JapaneseDate;", False, False), ("(Ljava/time/Clock;)Ljava/time/chrono/JapaneseDate;", False, False)])
    dateEpochDay = JavaMultipleMethod([("(J)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(J)Ljava/time/chrono/JapaneseDate;", False, False)])
    resolveDate = JavaMultipleMethod([("(Ljava/util/Map;Ljava/time/format/ResolverStyle;)Ljava/time/chrono/JapaneseDate;", False, False), ("(Ljava/util/Map;Ljava/time/format/ResolverStyle;)Ljava/time/chrono/ChronoLocalDate;", False, False)])
    eras = JavaMethod("()Ljava/util/List;")
    isIsoBased = JavaMethod("()Z")
    date = JavaMultipleMethod([("(Ljava/time/chrono/Era;III)Ljava/time/chrono/JapaneseDate;", False, False), ("(III)Ljava/time/chrono/JapaneseDate;", False, False), ("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/JapaneseDate;", False, False), ("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(III)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/chrono/Era;III)Ljava/time/chrono/ChronoLocalDate;", False, False)])
    localDateTime = JavaMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoLocalDateTime;")
    zonedDateTime = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoZonedDateTime;", False, False), ("(Ljava/time/Instant;Ljava/time/ZoneId;)Ljava/time/chrono/ChronoZonedDateTime;", False, False)])
    getCalendarType = JavaMethod("()Ljava/lang/String;")
    isLeapYear = JavaMethod("(J)Z")
    eraOf = JavaMultipleMethod([("(I)Ljava/time/chrono/Era;", False, False), ("(I)Ljava/time/chrono/JapaneseEra;", False, False)])