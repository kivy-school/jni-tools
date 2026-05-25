from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DateFormatSymbols"]

class DateFormatSymbols(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/DateFormatSymbols"
    __javaconstructor__ = [("()V", False), ("(Ljava/util/Locale;)V", False)]
    getAvailableLocales = JavaStaticMethod("()[Ljava/util/Locale;")
    getInstance = JavaMultipleMethod([("()Ljava/text/DateFormatSymbols;", True, False), ("(Ljava/util/Locale;)Ljava/text/DateFormatSymbols;", True, False)])
    getEras = JavaMethod("()[Ljava/lang/String;")
    setEras = JavaMethod("([Ljava/lang/String;)V")
    getMonths = JavaMethod("()[Ljava/lang/String;")
    setMonths = JavaMethod("([Ljava/lang/String;)V")
    getShortMonths = JavaMethod("()[Ljava/lang/String;")
    setShortMonths = JavaMethod("([Ljava/lang/String;)V")
    getWeekdays = JavaMethod("()[Ljava/lang/String;")
    setWeekdays = JavaMethod("([Ljava/lang/String;)V")
    getShortWeekdays = JavaMethod("()[Ljava/lang/String;")
    setShortWeekdays = JavaMethod("([Ljava/lang/String;)V")
    getAmPmStrings = JavaMethod("()[Ljava/lang/String;")
    setAmPmStrings = JavaMethod("([Ljava/lang/String;)V")
    getZoneStrings = JavaMethod("()[[Ljava/lang/String;")
    setZoneStrings = JavaMethod("([[Ljava/lang/String;)V")
    getLocalPatternChars = JavaMethod("()Ljava/lang/String;")
    setLocalPatternChars = JavaMethod("(Ljava/lang/String;)V")
    clone = JavaMethod("()Ljava/lang/Object;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")