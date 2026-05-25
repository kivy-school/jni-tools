from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JapaneseCalendar"]

class JapaneseCalendar(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/JapaneseCalendar"
    __javaconstructor__ = [("()V", False), ("(Landroid/icu/util/TimeZone;)V", False), ("(Ljava/util/Locale;)V", False), ("(Landroid/icu/util/ULocale;)V", False), ("(Landroid/icu/util/TimeZone;Ljava/util/Locale;)V", False), ("(Landroid/icu/util/TimeZone;Landroid/icu/util/ULocale;)V", False), ("(Ljava/util/Date;)V", False), ("(IIII)V", False), ("(III)V", False), ("(IIIIII)V", False)]
    HEISEI = JavaStaticField("I")
    MEIJI = JavaStaticField("I")
    REIWA = JavaStaticField("I")
    SHOWA = JavaStaticField("I")
    TAISHO = JavaStaticField("I")
    handleGetExtendedYear = JavaMethod("()I")
    handleComputeFields = JavaMethod("(I)V")
    handleGetLimit = JavaMethod("(II)I")
    getType = JavaMethod("()Ljava/lang/String;")
    getActualMaximum = JavaMethod("(I)I")