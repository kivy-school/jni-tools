from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EthiopicCalendar"]

class EthiopicCalendar(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/EthiopicCalendar"
    __javaconstructor__ = [("()V", False), ("(Landroid/icu/util/TimeZone;)V", False), ("(Ljava/util/Locale;)V", False), ("(Landroid/icu/util/ULocale;)V", False), ("(Landroid/icu/util/TimeZone;Ljava/util/Locale;)V", False), ("(Landroid/icu/util/TimeZone;Landroid/icu/util/ULocale;)V", False), ("(III)V", False), ("(Ljava/util/Date;)V", False), ("(IIIIII)V", False)]
    GENBOT = JavaStaticField("I")
    HAMLE = JavaStaticField("I")
    HEDAR = JavaStaticField("I")
    MEGABIT = JavaStaticField("I")
    MESKEREM = JavaStaticField("I")
    MIAZIA = JavaStaticField("I")
    NEHASSE = JavaStaticField("I")
    PAGUMEN = JavaStaticField("I")
    SENE = JavaStaticField("I")
    TAHSAS = JavaStaticField("I")
    TEKEMT = JavaStaticField("I")
    TER = JavaStaticField("I")
    YEKATIT = JavaStaticField("I")
    getType = JavaMethod("()Ljava/lang/String;")
    setAmeteAlemEra = JavaMethod("(Z)V")
    isAmeteAlemEra = JavaMethod("()Z")
    handleGetExtendedYear = JavaMethod("()I")
    handleComputeFields = JavaMethod("(I)V")
    handleGetLimit = JavaMethod("(II)I")
    handleComputeMonthStart = JavaMethod("(IIZ)I")