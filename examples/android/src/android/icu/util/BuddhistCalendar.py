from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BuddhistCalendar"]

class BuddhistCalendar(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/BuddhistCalendar"
    __javaconstructor__ = [("()V", False), ("(Landroid/icu/util/TimeZone;)V", False), ("(Ljava/util/Locale;)V", False), ("(Landroid/icu/util/ULocale;)V", False), ("(Landroid/icu/util/TimeZone;Ljava/util/Locale;)V", False), ("(Landroid/icu/util/TimeZone;Landroid/icu/util/ULocale;)V", False), ("(Ljava/util/Date;)V", False), ("(III)V", False), ("(IIIIII)V", False)]
    BE = JavaStaticField("I")
    handleGetExtendedYear = JavaMethod("()I")
    handleComputeMonthStart = JavaMethod("(IIZ)I")
    handleComputeFields = JavaMethod("(I)V")
    handleGetLimit = JavaMethod("(II)I")
    getType = JavaMethod("()Ljava/lang/String;")