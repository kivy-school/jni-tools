from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SimpleDateFormat"]

class SimpleDateFormat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/SimpleDateFormat"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/util/Locale;)V", False), ("(Ljava/lang/String;Ljava/text/DateFormatSymbols;)V", False)]
    set2DigitYearStart = JavaMethod("(Ljava/util/Date;)V")
    get2DigitYearStart = JavaMethod("()Ljava/util/Date;")
    format = JavaMethod("(Ljava/util/Date;Ljava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;")
    formatToCharacterIterator = JavaMethod("(Ljava/lang/Object;)Ljava/text/AttributedCharacterIterator;")
    parse = JavaMethod("(Ljava/lang/String;Ljava/text/ParsePosition;)Ljava/util/Date;")
    toPattern = JavaMethod("()Ljava/lang/String;")
    toLocalizedPattern = JavaMethod("()Ljava/lang/String;")
    applyPattern = JavaMethod("(Ljava/lang/String;)V")
    applyLocalizedPattern = JavaMethod("(Ljava/lang/String;)V")
    getDateFormatSymbols = JavaMethod("()Ljava/text/DateFormatSymbols;")
    setDateFormatSymbols = JavaMethod("(Ljava/text/DateFormatSymbols;)V")
    clone = JavaMethod("()Ljava/lang/Object;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")