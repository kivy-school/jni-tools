from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DateTimeFormatterBuilder"]

class DateTimeFormatterBuilder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/format/DateTimeFormatterBuilder"
    __javaconstructor__ = [("()V", False)]
    getLocalizedDateTimePattern = JavaStaticMethod("(Ljava/time/format/FormatStyle;Ljava/time/format/FormatStyle;Ljava/time/chrono/Chronology;Ljava/util/Locale;)Ljava/lang/String;")
    parseCaseSensitive = JavaMethod("()Ljava/time/format/DateTimeFormatterBuilder;")
    parseCaseInsensitive = JavaMethod("()Ljava/time/format/DateTimeFormatterBuilder;")
    parseStrict = JavaMethod("()Ljava/time/format/DateTimeFormatterBuilder;")
    parseLenient = JavaMethod("()Ljava/time/format/DateTimeFormatterBuilder;")
    parseDefaulting = JavaMethod("(Ljava/time/temporal/TemporalField;J)Ljava/time/format/DateTimeFormatterBuilder;")
    appendValue = JavaMultipleMethod([("(Ljava/time/temporal/TemporalField;)Ljava/time/format/DateTimeFormatterBuilder;", False, False), ("(Ljava/time/temporal/TemporalField;I)Ljava/time/format/DateTimeFormatterBuilder;", False, False), ("(Ljava/time/temporal/TemporalField;IILjava/time/format/SignStyle;)Ljava/time/format/DateTimeFormatterBuilder;", False, False)])
    appendValueReduced = JavaMultipleMethod([("(Ljava/time/temporal/TemporalField;III)Ljava/time/format/DateTimeFormatterBuilder;", False, False), ("(Ljava/time/temporal/TemporalField;IILjava/time/chrono/ChronoLocalDate;)Ljava/time/format/DateTimeFormatterBuilder;", False, False)])
    appendFraction = JavaMethod("(Ljava/time/temporal/TemporalField;IIZ)Ljava/time/format/DateTimeFormatterBuilder;")
    appendText = JavaMultipleMethod([("(Ljava/time/temporal/TemporalField;)Ljava/time/format/DateTimeFormatterBuilder;", False, False), ("(Ljava/time/temporal/TemporalField;Ljava/time/format/TextStyle;)Ljava/time/format/DateTimeFormatterBuilder;", False, False), ("(Ljava/time/temporal/TemporalField;Ljava/util/Map;)Ljava/time/format/DateTimeFormatterBuilder;", False, False)])
    appendInstant = JavaMultipleMethod([("()Ljava/time/format/DateTimeFormatterBuilder;", False, False), ("(I)Ljava/time/format/DateTimeFormatterBuilder;", False, False)])
    appendOffsetId = JavaMethod("()Ljava/time/format/DateTimeFormatterBuilder;")
    appendOffset = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Ljava/time/format/DateTimeFormatterBuilder;")
    appendLocalizedOffset = JavaMethod("(Ljava/time/format/TextStyle;)Ljava/time/format/DateTimeFormatterBuilder;")
    appendZoneId = JavaMethod("()Ljava/time/format/DateTimeFormatterBuilder;")
    appendZoneRegionId = JavaMethod("()Ljava/time/format/DateTimeFormatterBuilder;")
    appendZoneOrOffsetId = JavaMethod("()Ljava/time/format/DateTimeFormatterBuilder;")
    appendZoneText = JavaMultipleMethod([("(Ljava/time/format/TextStyle;)Ljava/time/format/DateTimeFormatterBuilder;", False, False), ("(Ljava/time/format/TextStyle;Ljava/util/Set;)Ljava/time/format/DateTimeFormatterBuilder;", False, False)])
    appendGenericZoneText = JavaMultipleMethod([("(Ljava/time/format/TextStyle;)Ljava/time/format/DateTimeFormatterBuilder;", False, False), ("(Ljava/time/format/TextStyle;Ljava/util/Set;)Ljava/time/format/DateTimeFormatterBuilder;", False, False)])
    appendChronologyId = JavaMethod("()Ljava/time/format/DateTimeFormatterBuilder;")
    appendChronologyText = JavaMethod("(Ljava/time/format/TextStyle;)Ljava/time/format/DateTimeFormatterBuilder;")
    appendLocalized = JavaMethod("(Ljava/time/format/FormatStyle;Ljava/time/format/FormatStyle;)Ljava/time/format/DateTimeFormatterBuilder;")
    appendLiteral = JavaMultipleMethod([("(C)Ljava/time/format/DateTimeFormatterBuilder;", False, False), ("(Ljava/lang/String;)Ljava/time/format/DateTimeFormatterBuilder;", False, False)])
    append = JavaMethod("(Ljava/time/format/DateTimeFormatter;)Ljava/time/format/DateTimeFormatterBuilder;")
    appendOptional = JavaMethod("(Ljava/time/format/DateTimeFormatter;)Ljava/time/format/DateTimeFormatterBuilder;")
    appendPattern = JavaMethod("(Ljava/lang/String;)Ljava/time/format/DateTimeFormatterBuilder;")
    padNext = JavaMultipleMethod([("(I)Ljava/time/format/DateTimeFormatterBuilder;", False, False), ("(IC)Ljava/time/format/DateTimeFormatterBuilder;", False, False)])
    optionalStart = JavaMethod("()Ljava/time/format/DateTimeFormatterBuilder;")
    optionalEnd = JavaMethod("()Ljava/time/format/DateTimeFormatterBuilder;")
    toFormatter = JavaMultipleMethod([("()Ljava/time/format/DateTimeFormatter;", False, False), ("(Ljava/util/Locale;)Ljava/time/format/DateTimeFormatter;", False, False)])