from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GregorianCalendar"]

class GregorianCalendar(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/GregorianCalendar"
    __javaconstructor__ = [("()V", False), ("(Ljava/util/TimeZone;)V", False), ("(Ljava/util/Locale;)V", False), ("(Ljava/util/TimeZone;Ljava/util/Locale;)V", False), ("(III)V", False), ("(IIIII)V", False), ("(IIIIII)V", False)]
    AD = JavaStaticField("I")
    BC = JavaStaticField("I")
    setGregorianChange = JavaMethod("(Ljava/util/Date;)V")
    getGregorianChange = JavaMethod("()Ljava/util/Date;")
    isLeapYear = JavaMethod("(I)Z")
    getCalendarType = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    add = JavaMethod("(II)V")
    roll = JavaMultipleMethod([("(IZ)V", False, False), ("(II)V", False, False)])
    getMinimum = JavaMethod("(I)I")
    getMaximum = JavaMethod("(I)I")
    getGreatestMinimum = JavaMethod("(I)I")
    getLeastMaximum = JavaMethod("(I)I")
    getActualMinimum = JavaMethod("(I)I")
    getActualMaximum = JavaMethod("(I)I")
    clone = JavaMethod("()Ljava/lang/Object;")
    getTimeZone = JavaMethod("()Ljava/util/TimeZone;")
    setTimeZone = JavaMethod("(Ljava/util/TimeZone;)V")
    isWeekDateSupported = JavaMethod("()Z")
    getWeekYear = JavaMethod("()I")
    setWeekDate = JavaMethod("(III)V")
    getWeeksInWeekYear = JavaMethod("()I")
    computeFields = JavaMethod("()V")
    computeTime = JavaMethod("()V")
    toZonedDateTime = JavaMethod("()Ljava/time/ZonedDateTime;")
    from = JavaStaticMethod("(Ljava/time/ZonedDateTime;)Ljava/util/GregorianCalendar;")