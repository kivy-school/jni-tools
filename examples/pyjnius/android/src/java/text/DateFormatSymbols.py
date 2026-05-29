from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DateFormatSymbols"]

class DateFormatSymbols(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/DateFormatSymbols"
    __javaconstructor__ = [("(Ljava/util/Locale;)V", False), ("()V", False)]
    getLocalPatternChars = JavaMethod("()Ljava/lang/String;")
    getZoneStrings = JavaMethod("()[[Ljava/lang/String;")
    setAmPmStrings = JavaMethod("([Ljava/lang/String;)V")
    setEras = JavaMethod("([Ljava/lang/String;)V")
    setLocalPatternChars = JavaMethod("(Ljava/lang/String;)V")
    setMonths = JavaMethod("([Ljava/lang/String;)V")
    setShortMonths = JavaMethod("([Ljava/lang/String;)V")
    setShortWeekdays = JavaMethod("([Ljava/lang/String;)V")
    setWeekdays = JavaMethod("([Ljava/lang/String;)V")
    setZoneStrings = JavaMethod("([[Ljava/lang/String;)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")
    getInstance = JavaMultipleMethod([("()Ljava/text/DateFormatSymbols;", True, False), ("(Ljava/util/Locale;)Ljava/text/DateFormatSymbols;", True, False)])
    getAvailableLocales = JavaStaticMethod("()[Ljava/util/Locale;")
    getEras = JavaMethod("()[Ljava/lang/String;")
    getShortMonths = JavaMethod("()[Ljava/lang/String;")
    getWeekdays = JavaMethod("()[Ljava/lang/String;")
    getShortWeekdays = JavaMethod("()[Ljava/lang/String;")
    getAmPmStrings = JavaMethod("()[Ljava/lang/String;")
    getMonths = JavaMethod("()[Ljava/lang/String;")