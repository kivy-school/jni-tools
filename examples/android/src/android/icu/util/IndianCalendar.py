from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IndianCalendar"]

class IndianCalendar(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/IndianCalendar"
    __javaconstructor__ = [("()V", False), ("(Landroid/icu/util/TimeZone;)V", False), ("(Ljava/util/Locale;)V", False), ("(Landroid/icu/util/ULocale;)V", False), ("(Landroid/icu/util/TimeZone;Ljava/util/Locale;)V", False), ("(Landroid/icu/util/TimeZone;Landroid/icu/util/ULocale;)V", False), ("(Ljava/util/Date;)V", False), ("(III)V", False), ("(IIIIII)V", False)]
    AGRAHAYANA = JavaStaticField("I")
    ASADHA = JavaStaticField("I")
    ASVINA = JavaStaticField("I")
    BHADRA = JavaStaticField("I")
    CHAITRA = JavaStaticField("I")
    IE = JavaStaticField("I")
    JYAISTHA = JavaStaticField("I")
    KARTIKA = JavaStaticField("I")
    MAGHA = JavaStaticField("I")
    PAUSA = JavaStaticField("I")
    PHALGUNA = JavaStaticField("I")
    SRAVANA = JavaStaticField("I")
    VAISAKHA = JavaStaticField("I")
    handleGetExtendedYear = JavaMethod("()I")
    handleGetYearLength = JavaMethod("(I)I")
    handleGetMonthLength = JavaMethod("(II)I")
    handleComputeFields = JavaMethod("(I)V")
    handleGetLimit = JavaMethod("(II)I")
    handleComputeMonthStart = JavaMethod("(IIZ)I")
    getType = JavaMethod("()Ljava/lang/String;")