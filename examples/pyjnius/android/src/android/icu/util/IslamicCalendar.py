from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IslamicCalendar"]

class IslamicCalendar(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/IslamicCalendar"
    __javaconstructor__ = [("()V", False), ("(Landroid/icu/util/TimeZone;)V", False), ("(Ljava/util/Locale;)V", False), ("(Landroid/icu/util/ULocale;)V", False), ("(Landroid/icu/util/TimeZone;Ljava/util/Locale;)V", False), ("(Landroid/icu/util/TimeZone;Landroid/icu/util/ULocale;)V", False), ("(Ljava/util/Date;)V", False), ("(III)V", False), ("(IIIIII)V", False)]
    DHU_AL_HIJJAH = JavaStaticField("I")
    DHU_AL_QIDAH = JavaStaticField("I")
    JUMADA_1 = JavaStaticField("I")
    JUMADA_2 = JavaStaticField("I")
    MUHARRAM = JavaStaticField("I")
    RABI_1 = JavaStaticField("I")
    RABI_2 = JavaStaticField("I")
    RAJAB = JavaStaticField("I")
    RAMADAN = JavaStaticField("I")
    SAFAR = JavaStaticField("I")
    SHABAN = JavaStaticField("I")
    SHAWWAL = JavaStaticField("I")
    handleGetLimit = JavaMethod("(II)I")
    handleGetMonthLength = JavaMethod("(II)I")
    handleGetYearLength = JavaMethod("(I)I")
    handleComputeMonthStart = JavaMethod("(IIZ)I")
    handleGetExtendedYear = JavaMethod("()I")
    handleComputeFields = JavaMethod("(I)V")
    setCalculationType = JavaMethod("(Landroid/icu/util/IslamicCalendar$CalculationType;)V")
    getCalculationType = JavaMethod("()Landroid/icu/util/IslamicCalendar$CalculationType;")
    getType = JavaMethod("()Ljava/lang/String;")

    class CalculationType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/util/IslamicCalendar/CalculationType"
        values = JavaStaticMethod("()[Landroid/icu/util/IslamicCalendar$CalculationType;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/util/IslamicCalendar$CalculationType;")
        ISLAMIC = JavaStaticField("Landroid/icu/util/IslamicCalendar/CalculationType;")
        ISLAMIC_CIVIL = JavaStaticField("Landroid/icu/util/IslamicCalendar/CalculationType;")
        ISLAMIC_UMALQURA = JavaStaticField("Landroid/icu/util/IslamicCalendar/CalculationType;")
        ISLAMIC_TBLA = JavaStaticField("Landroid/icu/util/IslamicCalendar/CalculationType;")