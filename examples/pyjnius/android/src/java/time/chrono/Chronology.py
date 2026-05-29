from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Chronology"]

class Chronology(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/Chronology"
    from = JavaStaticMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/Chronology;")
    ofLocale = JavaStaticMethod("(Ljava/util/Locale;)Ljava/time/chrono/Chronology;")
    of = JavaStaticMethod("(Ljava/lang/String;)Ljava/time/chrono/Chronology;")
    getAvailableChronologies = JavaStaticMethod("()Ljava/util/Set;")
    getId = JavaMethod("()Ljava/lang/String;")
    getCalendarType = JavaMethod("()Ljava/lang/String;")
    date = JavaMultipleMethod([("(Ljava/time/chrono/Era;III)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(III)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoLocalDate;", False, False)])
    dateYearDay = JavaMultipleMethod([("(Ljava/time/chrono/Era;II)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(II)Ljava/time/chrono/ChronoLocalDate;", False, False)])
    dateEpochDay = JavaMethod("(J)Ljava/time/chrono/ChronoLocalDate;")
    dateNow = JavaMultipleMethod([("()Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/ZoneId;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/Clock;)Ljava/time/chrono/ChronoLocalDate;", False, False)])
    localDateTime = JavaMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoLocalDateTime;")
    zonedDateTime = JavaMultipleMethod([("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoZonedDateTime;", False, False), ("(Ljava/time/Instant;Ljava/time/ZoneId;)Ljava/time/chrono/ChronoZonedDateTime;", False, False)])
    isLeapYear = JavaMethod("(J)Z")
    prolepticYear = JavaMethod("(Ljava/time/chrono/Era;I)I")
    eraOf = JavaMethod("(I)Ljava/time/chrono/Era;")
    eras = JavaMethod("()Ljava/util/List;")
    range = JavaMethod("(Ljava/time/temporal/ChronoField;)Ljava/time/temporal/ValueRange;")
    getDisplayName = JavaMethod("(Ljava/time/format/TextStyle;Ljava/util/Locale;)Ljava/lang/String;")
    resolveDate = JavaMethod("(Ljava/util/Map;Ljava/time/format/ResolverStyle;)Ljava/time/chrono/ChronoLocalDate;")
    period = JavaMethod("(III)Ljava/time/chrono/ChronoPeriod;")
    epochSecond = JavaMultipleMethod([("(IIIIIILjava/time/ZoneOffset;)J", False, False), ("(Ljava/time/chrono/Era;IIIIIILjava/time/ZoneOffset;)J", False, False)])
    compareTo = JavaMethod("(Ljava/time/chrono/Chronology;)I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")