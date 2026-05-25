from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HebrewCalendar"]

class HebrewCalendar(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/HebrewCalendar"
    __javaconstructor__ = [("()V", False), ("(Landroid/icu/util/TimeZone;)V", False), ("(Ljava/util/Locale;)V", False), ("(Landroid/icu/util/ULocale;)V", False), ("(Landroid/icu/util/TimeZone;Ljava/util/Locale;)V", False), ("(Landroid/icu/util/TimeZone;Landroid/icu/util/ULocale;)V", False), ("(III)V", False), ("(Ljava/util/Date;)V", False), ("(IIIIII)V", False)]
    ADAR = JavaStaticField("I")
    ADAR_1 = JavaStaticField("I")
    AV = JavaStaticField("I")
    ELUL = JavaStaticField("I")
    HESHVAN = JavaStaticField("I")
    IYAR = JavaStaticField("I")
    KISLEV = JavaStaticField("I")
    NISAN = JavaStaticField("I")
    SHEVAT = JavaStaticField("I")
    SIVAN = JavaStaticField("I")
    TAMUZ = JavaStaticField("I")
    TEVET = JavaStaticField("I")
    TISHRI = JavaStaticField("I")
    add = JavaMethod("(II)V")
    roll = JavaMethod("(II)V")
    handleGetLimit = JavaMethod("(II)I")
    handleGetMonthLength = JavaMethod("(II)I")
    handleGetYearLength = JavaMethod("(I)I")
    validateField = JavaMethod("(I)V")
    handleComputeFields = JavaMethod("(I)V")
    handleGetExtendedYear = JavaMethod("()I")
    handleComputeMonthStart = JavaMethod("(IIZ)I")
    getType = JavaMethod("()Ljava/lang/String;")