from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RelativeDateTimeFormatter"]

class RelativeDateTimeFormatter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/RelativeDateTimeFormatter"
    getInstance = JavaMultipleMethod([("()Landroid/icu/text/RelativeDateTimeFormatter;", True, False), ("(Landroid/icu/util/ULocale;)Landroid/icu/text/RelativeDateTimeFormatter;", True, False), ("(Ljava/util/Locale;)Landroid/icu/text/RelativeDateTimeFormatter;", True, False), ("(Landroid/icu/util/ULocale;Landroid/icu/text/NumberFormat;)Landroid/icu/text/RelativeDateTimeFormatter;", True, False), ("(Landroid/icu/util/ULocale;Landroid/icu/text/NumberFormat;Landroid/icu/text/RelativeDateTimeFormatter$Style;Landroid/icu/text/DisplayContext;)Landroid/icu/text/RelativeDateTimeFormatter;", True, False), ("(Ljava/util/Locale;Landroid/icu/text/NumberFormat;)Landroid/icu/text/RelativeDateTimeFormatter;", True, False)])
    format = JavaMultipleMethod([("(DLandroid/icu/text/RelativeDateTimeFormatter$Direction;Landroid/icu/text/RelativeDateTimeFormatter$RelativeUnit;)Ljava/lang/String;", False, False), ("(Landroid/icu/text/RelativeDateTimeFormatter$Direction;Landroid/icu/text/RelativeDateTimeFormatter$AbsoluteUnit;)Ljava/lang/String;", False, False), ("(DLandroid/icu/text/RelativeDateTimeFormatter$RelativeDateTimeUnit;)Ljava/lang/String;", False, False)])
    formatToValue = JavaMultipleMethod([("(DLandroid/icu/text/RelativeDateTimeFormatter$Direction;Landroid/icu/text/RelativeDateTimeFormatter$RelativeUnit;)Landroid/icu/text/RelativeDateTimeFormatter$FormattedRelativeDateTime;", False, False), ("(Landroid/icu/text/RelativeDateTimeFormatter$Direction;Landroid/icu/text/RelativeDateTimeFormatter$AbsoluteUnit;)Landroid/icu/text/RelativeDateTimeFormatter$FormattedRelativeDateTime;", False, False), ("(DLandroid/icu/text/RelativeDateTimeFormatter$RelativeDateTimeUnit;)Landroid/icu/text/RelativeDateTimeFormatter$FormattedRelativeDateTime;", False, False)])
    formatNumeric = JavaMethod("(DLandroid/icu/text/RelativeDateTimeFormatter$RelativeDateTimeUnit;)Ljava/lang/String;")
    formatNumericToValue = JavaMethod("(DLandroid/icu/text/RelativeDateTimeFormatter$RelativeDateTimeUnit;)Landroid/icu/text/RelativeDateTimeFormatter$FormattedRelativeDateTime;")
    combineDateAndTime = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")
    getNumberFormat = JavaMethod("()Landroid/icu/text/NumberFormat;")
    getCapitalizationContext = JavaMethod("()Landroid/icu/text/DisplayContext;")
    getFormatStyle = JavaMethod("()Landroid/icu/text/RelativeDateTimeFormatter$Style;")

    class AbsoluteUnit(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/RelativeDateTimeFormatter/AbsoluteUnit"
        values = JavaStaticMethod("()[Landroid/icu/text/RelativeDateTimeFormatter$AbsoluteUnit;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/RelativeDateTimeFormatter$AbsoluteUnit;")
        SUNDAY = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/AbsoluteUnit;")
        MONDAY = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/AbsoluteUnit;")
        TUESDAY = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/AbsoluteUnit;")
        WEDNESDAY = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/AbsoluteUnit;")
        THURSDAY = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/AbsoluteUnit;")
        FRIDAY = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/AbsoluteUnit;")
        SATURDAY = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/AbsoluteUnit;")
        DAY = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/AbsoluteUnit;")
        WEEK = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/AbsoluteUnit;")
        MONTH = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/AbsoluteUnit;")
        YEAR = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/AbsoluteUnit;")
        NOW = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/AbsoluteUnit;")
        QUARTER = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/AbsoluteUnit;")
        HOUR = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/AbsoluteUnit;")
        MINUTE = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/AbsoluteUnit;")

    class Direction(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/RelativeDateTimeFormatter/Direction"
        values = JavaStaticMethod("()[Landroid/icu/text/RelativeDateTimeFormatter$Direction;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/RelativeDateTimeFormatter$Direction;")
        LAST_2 = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/Direction;")
        LAST = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/Direction;")
        THIS = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/Direction;")
        NEXT = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/Direction;")
        NEXT_2 = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/Direction;")
        PLAIN = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/Direction;")

    class FormattedRelativeDateTime(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/RelativeDateTimeFormatter/FormattedRelativeDateTime"
        toString = JavaMethod("()Ljava/lang/String;")
        length = JavaMethod("()I")
        charAt = JavaMethod("(I)C")
        subSequence = JavaMethod("(II)Ljava/lang/CharSequence;")
        appendTo = JavaMethod("(Ljava/lang/Appendable;)Ljava/lang/Appendable;")
        nextPosition = JavaMethod("(Landroid/icu/text/ConstrainedFieldPosition;)Z")
        toCharacterIterator = JavaMethod("()Ljava/text/AttributedCharacterIterator;")

    class RelativeDateTimeUnit(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/RelativeDateTimeFormatter/RelativeDateTimeUnit"
        values = JavaStaticMethod("()[Landroid/icu/text/RelativeDateTimeFormatter$RelativeDateTimeUnit;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/RelativeDateTimeFormatter$RelativeDateTimeUnit;")
        YEAR = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/RelativeDateTimeUnit;")
        QUARTER = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/RelativeDateTimeUnit;")
        MONTH = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/RelativeDateTimeUnit;")
        WEEK = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/RelativeDateTimeUnit;")
        DAY = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/RelativeDateTimeUnit;")
        HOUR = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/RelativeDateTimeUnit;")
        MINUTE = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/RelativeDateTimeUnit;")
        SECOND = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/RelativeDateTimeUnit;")
        SUNDAY = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/RelativeDateTimeUnit;")
        MONDAY = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/RelativeDateTimeUnit;")
        TUESDAY = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/RelativeDateTimeUnit;")
        WEDNESDAY = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/RelativeDateTimeUnit;")
        THURSDAY = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/RelativeDateTimeUnit;")
        FRIDAY = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/RelativeDateTimeUnit;")
        SATURDAY = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/RelativeDateTimeUnit;")

    class RelativeUnit(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/RelativeDateTimeFormatter/RelativeUnit"
        values = JavaStaticMethod("()[Landroid/icu/text/RelativeDateTimeFormatter$RelativeUnit;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/RelativeDateTimeFormatter$RelativeUnit;")
        SECONDS = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/RelativeUnit;")
        MINUTES = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/RelativeUnit;")
        HOURS = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/RelativeUnit;")
        DAYS = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/RelativeUnit;")
        WEEKS = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/RelativeUnit;")
        MONTHS = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/RelativeUnit;")
        YEARS = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/RelativeUnit;")

    class Style(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/RelativeDateTimeFormatter/Style"
        values = JavaStaticMethod("()[Landroid/icu/text/RelativeDateTimeFormatter$Style;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/RelativeDateTimeFormatter$Style;")
        LONG = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/Style;")
        SHORT = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/Style;")
        NARROW = JavaStaticField("Landroid/icu/text/RelativeDateTimeFormatter/Style;")