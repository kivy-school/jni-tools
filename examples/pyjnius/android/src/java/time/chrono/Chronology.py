from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Chronology"]

class Chronology(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/Chronology"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/time/chrono/Chronology;)I", False, False), ("(Ljava/lang/Object;)I", False, False)])
    of = JavaStaticMethod("(Ljava/lang/String;)Ljava/time/chrono/Chronology;")
    from = JavaStaticMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/Chronology;")
    getId = JavaMethod("()Ljava/lang/String;")
    period = JavaMethod("(III)Ljava/time/chrono/ChronoPeriod;")
    getDisplayName = JavaMethod("(Ljava/time/format/TextStyle;Ljava/util/Locale;)Ljava/lang/String;")
    range = JavaMethod("(Ljava/time/temporal/ChronoField;)Ljava/time/temporal/ValueRange;")
    ofLocale = JavaStaticMethod("(Ljava/util/Locale;)Ljava/time/chrono/Chronology;")
    getAvailableChronologies = JavaStaticMethod("()Ljava/util/Set;")
    prolepticYear = JavaMethod("(Ljava/time/chrono/Era;I)I")
    dateYearDay = JavaMultipleMethod([("(II)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/chrono/Era;II)Ljava/time/chrono/ChronoLocalDate;", False, False)])
    dateNow = JavaMultipleMethod([("(Ljava/time/Clock;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("()Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/ZoneId;)Ljava/time/chrono/ChronoLocalDate;", False, False)])
    dateEpochDay = JavaMethod("(J)Ljava/time/chrono/ChronoLocalDate;")
    resolveDate = JavaMethod("(Ljava/util/Map;Ljava/time/format/ResolverStyle;)Ljava/time/chrono/ChronoLocalDate;")
    eras = JavaMethod("()Ljava/util/List;")
    isIsoBased = JavaMethod("()Z")
    date = JavaMultipleMethod([("(III)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoLocalDate;", False, False), ("(Ljava/time/chrono/Era;III)Ljava/time/chrono/ChronoLocalDate;", False, False)])
    epochSecond = JavaMultipleMethod([("(Ljava/time/chrono/Era;IIIIIILjava/time/ZoneOffset;)J", False, False), ("(IIIIIILjava/time/ZoneOffset;)J", False, False)])
    localDateTime = JavaMethod("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoLocalDateTime;")
    zonedDateTime = JavaMultipleMethod([("(Ljava/time/Instant;Ljava/time/ZoneId;)Ljava/time/chrono/ChronoZonedDateTime;", False, False), ("(Ljava/time/temporal/TemporalAccessor;)Ljava/time/chrono/ChronoZonedDateTime;", False, False)])
    getCalendarType = JavaMethod("()Ljava/lang/String;")
    isLeapYear = JavaMethod("(J)Z")
    eraOf = JavaMethod("(I)Ljava/time/chrono/Era;")