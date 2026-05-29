from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DateIntervalFormat"]

class DateIntervalFormat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/DateIntervalFormat"
    parseObject = JavaMethod("(Ljava/lang/String;Ljava/text/ParsePosition;)Ljava/lang/Object;")
    setContext = JavaMethod("(Landroid/icu/text/DisplayContext;)V")
    getDateFormat = JavaMethod("()Landroid/icu/text/DateFormat;")
    formatToValue = JavaMultipleMethod([("(Landroid/icu/util/DateInterval;)Landroid/icu/text/DateIntervalFormat$FormattedDateInterval;", False, False), ("(Landroid/icu/util/Calendar;Landroid/icu/util/Calendar;)Landroid/icu/text/DateIntervalFormat$FormattedDateInterval;", False, False)])
    getDateIntervalInfo = JavaMethod("()Landroid/icu/text/DateIntervalInfo;")
    setDateIntervalInfo = JavaMethod("(Landroid/icu/text/DateIntervalInfo;)V")
    clone = JavaMethod("()Ljava/lang/Object;")
    format = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;", False, False), ("(Landroid/icu/util/Calendar;Landroid/icu/util/Calendar;Ljava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;", False, False), ("(Landroid/icu/util/DateInterval;Ljava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;", False, False)])
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/util/Locale;Landroid/icu/text/DateIntervalInfo;)Landroid/icu/text/DateIntervalFormat;", True, False), ("(Ljava/lang/String;Ljava/util/Locale;)Landroid/icu/text/DateIntervalFormat;", True, False), ("(Ljava/lang/String;)Landroid/icu/text/DateIntervalFormat;", True, False), ("(Ljava/lang/String;Landroid/icu/text/DateIntervalInfo;)Landroid/icu/text/DateIntervalFormat;", True, False), ("(Ljava/lang/String;Landroid/icu/util/ULocale;Landroid/icu/text/DateIntervalInfo;)Landroid/icu/text/DateIntervalFormat;", True, False), ("(Ljava/lang/String;Landroid/icu/util/ULocale;)Landroid/icu/text/DateIntervalFormat;", True, False)])
    getContext = JavaMethod("(Landroid/icu/text/DisplayContext$Type;)Landroid/icu/text/DisplayContext;")
    getTimeZone = JavaMethod("()Landroid/icu/util/TimeZone;")
    setTimeZone = JavaMethod("(Landroid/icu/util/TimeZone;)V")

    class FormattedDateInterval(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/DateIntervalFormat$FormattedDateInterval"
        appendTo = JavaMethod("(Ljava/lang/Appendable;)Ljava/lang/Appendable;")
        nextPosition = JavaMethod("(Landroid/icu/text/ConstrainedFieldPosition;)Z")
        toCharacterIterator = JavaMethod("()Ljava/text/AttributedCharacterIterator;")
        length = JavaMethod("()I")
        toString = JavaMethod("()Ljava/lang/String;")
        charAt = JavaMethod("(I)C")
        subSequence = JavaMethod("(II)Ljava/lang/CharSequence;")