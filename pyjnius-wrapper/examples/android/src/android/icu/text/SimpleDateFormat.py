from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SimpleDateFormat"]

class SimpleDateFormat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/SimpleDateFormat"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/util/Locale;)V", False), ("(Ljava/lang/String;Landroid/icu/util/ULocale;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Landroid/icu/util/ULocale;)V", False), ("(Ljava/lang/String;Landroid/icu/text/DateFormatSymbols;)V", False)]
    set2DigitYearStart = JavaMethod("(Ljava/util/Date;)V")
    get2DigitYearStart = JavaMethod("()Ljava/util/Date;")
    setContext = JavaMethod("(Landroid/icu/text/DisplayContext;)V")
    format = JavaMethod("(Landroid/icu/util/Calendar;Ljava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;")
    patternCharToDateFormatField = JavaMethod("(C)Landroid/icu/text/DateFormat$Field;")
    subFormat = JavaMethod("(CIILjava/text/FieldPosition;Landroid/icu/text/DateFormatSymbols;Landroid/icu/util/Calendar;)Ljava/lang/String;")
    setNumberFormat = JavaMultipleMethod([("(Landroid/icu/text/NumberFormat;)V", False, False), ("(Ljava/lang/String;Landroid/icu/text/NumberFormat;)V", False, False)])
    zeroPaddingNumber = JavaMethod("(JII)Ljava/lang/String;")
    parse = JavaMethod("(Ljava/lang/String;Landroid/icu/util/Calendar;Ljava/text/ParsePosition;)V")
    matchString = JavaMethod("(Ljava/lang/String;II[Ljava/lang/String;Landroid/icu/util/Calendar;)I")
    matchQuarterString = JavaMethod("(Ljava/lang/String;II[Ljava/lang/String;Landroid/icu/util/Calendar;)I")
    subParse = JavaMethod("(Ljava/lang/String;ICIZZ[ZLandroid/icu/util/Calendar;)I")
    toPattern = JavaMethod("()Ljava/lang/String;")
    toLocalizedPattern = JavaMethod("()Ljava/lang/String;")
    applyPattern = JavaMethod("(Ljava/lang/String;)V")
    applyLocalizedPattern = JavaMethod("(Ljava/lang/String;)V")
    getDateFormatSymbols = JavaMethod("()Landroid/icu/text/DateFormatSymbols;")
    setDateFormatSymbols = JavaMethod("(Landroid/icu/text/DateFormatSymbols;)V")
    getSymbols = JavaMethod("()Landroid/icu/text/DateFormatSymbols;")
    getTimeZoneFormat = JavaMethod("()Landroid/icu/text/TimeZoneFormat;")
    setTimeZoneFormat = JavaMethod("(Landroid/icu/text/TimeZoneFormat;)V")
    clone = JavaMethod("()Ljava/lang/Object;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    formatToCharacterIterator = JavaMethod("(Ljava/lang/Object;)Ljava/text/AttributedCharacterIterator;")
    getNumberFormat = JavaMethod("(C)Landroid/icu/text/NumberFormat;")