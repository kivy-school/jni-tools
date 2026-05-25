from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CopticCalendar"]

class CopticCalendar(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/CopticCalendar"
    __javaconstructor__ = [("()V", False), ("(Landroid/icu/util/TimeZone;)V", False), ("(Ljava/util/Locale;)V", False), ("(Landroid/icu/util/ULocale;)V", False), ("(Landroid/icu/util/TimeZone;Ljava/util/Locale;)V", False), ("(Landroid/icu/util/TimeZone;Landroid/icu/util/ULocale;)V", False), ("(III)V", False), ("(Ljava/util/Date;)V", False), ("(IIIIII)V", False)]
    AMSHIR = JavaStaticField("I")
    BABA = JavaStaticField("I")
    BARAMHAT = JavaStaticField("I")
    BARAMOUDA = JavaStaticField("I")
    BASHANS = JavaStaticField("I")
    EPEP = JavaStaticField("I")
    HATOR = JavaStaticField("I")
    KIAHK = JavaStaticField("I")
    MESRA = JavaStaticField("I")
    NASIE = JavaStaticField("I")
    PAONA = JavaStaticField("I")
    TOBA = JavaStaticField("I")
    TOUT = JavaStaticField("I")
    getType = JavaMethod("()Ljava/lang/String;")
    handleGetExtendedYear = JavaMethod("()I")
    handleComputeFields = JavaMethod("(I)V")
    handleComputeMonthStart = JavaMethod("(IIZ)I")
    handleGetLimit = JavaMethod("(II)I")