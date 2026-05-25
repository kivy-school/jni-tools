from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GregorianCalendar"]

class GregorianCalendar(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/GregorianCalendar"
    __javaconstructor__ = [("()V", False), ("(Landroid/icu/util/TimeZone;)V", False), ("(Ljava/util/Locale;)V", False), ("(Landroid/icu/util/ULocale;)V", False), ("(Landroid/icu/util/TimeZone;Ljava/util/Locale;)V", False), ("(Landroid/icu/util/TimeZone;Landroid/icu/util/ULocale;)V", False), ("(III)V", False), ("(IIIII)V", False), ("(IIIIII)V", False)]
    AD = JavaStaticField("I")
    BC = JavaStaticField("I")
    invertGregorian = JavaField("Z")
    isGregorian = JavaField("Z")
    handleGetLimit = JavaMethod("(II)I")
    setGregorianChange = JavaMethod("(Ljava/util/Date;)V")
    getGregorianChange = JavaMethod("()Ljava/util/Date;")
    isLeapYear = JavaMethod("(I)Z")
    isEquivalentTo = JavaMethod("(Landroid/icu/util/Calendar;)Z")
    hashCode = JavaMethod("()I")
    roll = JavaMethod("(II)V")
    getActualMinimum = JavaMethod("(I)I")
    getActualMaximum = JavaMethod("(I)I")
    handleGetMonthLength = JavaMethod("(II)I")
    handleGetYearLength = JavaMethod("(I)I")
    handleComputeFields = JavaMethod("(I)V")
    handleGetExtendedYear = JavaMethod("()I")
    handleComputeJulianDay = JavaMethod("(I)I")
    handleComputeMonthStart = JavaMethod("(IIZ)I")
    getType = JavaMethod("()Ljava/lang/String;")