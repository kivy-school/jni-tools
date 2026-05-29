from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TaiwanCalendar"]

class TaiwanCalendar(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/TaiwanCalendar"
    __javaconstructor__ = [("()V", False), ("(Landroid/icu/util/TimeZone;)V", False), ("(Ljava/util/Locale;)V", False), ("(Landroid/icu/util/ULocale;)V", False), ("(Landroid/icu/util/TimeZone;Ljava/util/Locale;)V", False), ("(Landroid/icu/util/TimeZone;Landroid/icu/util/ULocale;)V", False), ("(Ljava/util/Date;)V", False), ("(III)V", False), ("(IIIIII)V", False)]
    BEFORE_MINGUO = JavaStaticField("I")
    MINGUO = JavaStaticField("I")
    handleGetExtendedYear = JavaMethod("()I")
    handleComputeFields = JavaMethod("(I)V")
    handleGetLimit = JavaMethod("(II)I")
    getType = JavaMethod("()Ljava/lang/String;")