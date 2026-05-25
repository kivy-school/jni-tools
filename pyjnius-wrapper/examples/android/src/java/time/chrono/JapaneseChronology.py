from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JapaneseChronology"]

class JapaneseChronology(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/JapaneseChronology"
    INSTANCE = JavaStaticField("Ljava/time/chrono/JapaneseChronology;")
    getId = JavaMethod("()Ljava/lang/String;")
    getCalendarType = JavaMethod("()Ljava/lang/String;")
    date = JavaMultipleMethod([("(Ljava/time/chrono/Era;III)Ljava/time/chrono/JapaneseDate;", False, False), ("(III)Ljava/time/chrono/JapaneseDate;", False, False), ("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/JapaneseDate;", False, False)])
    dateYearDay = JavaMultipleMethod([("(Ljava/time/chrono/Era;II)Ljava/time/chrono/JapaneseDate;", False, False), ("(II)Ljava/time/chrono/JapaneseDate;", False, False)])
    dateEpochDay = JavaMethod("(J)Ljava/time/chrono/JapaneseDate;")
    dateNow = JavaMultipleMethod([("()Ljava/time/chrono/JapaneseDate;", False, False), ("(Ljava/time/ZoneId;)Ljava/time/chrono/JapaneseDate;", False, False), ("(Ljava/time/Clock;)Ljava/time/chrono/JapaneseDate;", False, False)])
    localDateTime = JavaMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoLocalDateTime;")
    zonedDateTime = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoZonedDateTime;", False, False), ("(Ljava/time/Instant;Ljava/time/ZoneId;)Ljava/time/chrono/ChronoZonedDateTime;", False, False)])
    isLeapYear = JavaMethod("(J)Z")
    prolepticYear = JavaMethod("(Ljava/time/chrono/Era;I)I")
    eraOf = JavaMethod("(I)Ljava/time/chrono/JapaneseEra;")
    eras = JavaMethod("()Ljava/util/List;")
    range = JavaMethod("(Ljava/time/temporal/ChronoField;)Ljava/time/temporal/ValueRange;")
    resolveDate = JavaMethod("(Ljava/util/Map;Ljava/time/format/ResolverStyle;)Ljava/time/chrono/JapaneseDate;")