from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DateIntervalFormat"]

class DateIntervalFormat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/DateIntervalFormat"
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/icu/text/DateIntervalFormat;", True, False), ("(Ljava/lang/String;Ljava/util/Locale;)Landroid/icu/text/DateIntervalFormat;", True, False), ("(Ljava/lang/String;Landroid/icu/util/ULocale;)Landroid/icu/text/DateIntervalFormat;", True, False), ("(Ljava/lang/String;Landroid/icu/text/DateIntervalInfo;)Landroid/icu/text/DateIntervalFormat;", True, False), ("(Ljava/lang/String;Ljava/util/Locale;Landroid/icu/text/DateIntervalInfo;)Landroid/icu/text/DateIntervalFormat;", True, False), ("(Ljava/lang/String;Landroid/icu/util/ULocale;Landroid/icu/text/DateIntervalInfo;)Landroid/icu/text/DateIntervalFormat;", True, False)])
    clone = JavaMethod("()Ljava/lang/Object;")
    format = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;", False, False), ("(Landroid/icu/util/DateInterval;Ljava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;", False, False), ("(Landroid/icu/util/Calendar;Landroid/icu/util/Calendar;Ljava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;", False, False)])
    formatToValue = JavaMultipleMethod([("(Landroid/icu/util/DateInterval;)Landroid/icu/text/DateIntervalFormat$FormattedDateInterval;", False, False), ("(Landroid/icu/util/Calendar;Landroid/icu/util/Calendar;)Landroid/icu/text/DateIntervalFormat$FormattedDateInterval;", False, False)])
    parseObject = JavaMethod("(Ljava/lang/String;Ljava/text/ParsePosition;)Ljava/lang/Object;")
    getDateIntervalInfo = JavaMethod("()Landroid/icu/text/DateIntervalInfo;")
    setDateIntervalInfo = JavaMethod("(Landroid/icu/text/DateIntervalInfo;)V")
    getTimeZone = JavaMethod("()Landroid/icu/util/TimeZone;")
    setTimeZone = JavaMethod("(Landroid/icu/util/TimeZone;)V")
    setContext = JavaMethod("(Landroid/icu/text/DisplayContext;)V")
    getContext = JavaMethod("(Landroid/icu/text/DisplayContext$Type;)Landroid/icu/text/DisplayContext;")
    getDateFormat = JavaMethod("()Landroid/icu/text/DateFormat;")

    class FormattedDateInterval(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/DateIntervalFormat/FormattedDateInterval"
        toString = JavaMethod("()Ljava/lang/String;")
        length = JavaMethod("()I")
        charAt = JavaMethod("(I)C")
        subSequence = JavaMethod("(II)Ljava/lang/CharSequence;")
        appendTo = JavaMethod("(Ljava/lang/Appendable;)Ljava/lang/Appendable;")
        nextPosition = JavaMethod("(Landroid/icu/text/ConstrainedFieldPosition;)Z")
        toCharacterIterator = JavaMethod("()Ljava/text/AttributedCharacterIterator;")