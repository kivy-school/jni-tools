from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChineseCalendar"]

class ChineseCalendar(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/ChineseCalendar"
    __javaconstructor__ = [("()V", False), ("(Ljava/util/Date;)V", False), ("(IIII)V", False), ("(IIIIIII)V", False), ("(IIIII)V", False), ("(IIIIIIII)V", False), ("(Ljava/util/Locale;)V", False), ("(Landroid/icu/util/TimeZone;)V", False), ("(Landroid/icu/util/TimeZone;Ljava/util/Locale;)V", False), ("(Landroid/icu/util/ULocale;)V", False), ("(Landroid/icu/util/TimeZone;Landroid/icu/util/ULocale;)V", False)]
    handleGetLimit = JavaMethod("(II)I")
    handleGetExtendedYear = JavaMethod("()I")
    handleGetMonthLength = JavaMethod("(II)I")
    handleGetDateFormat = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Landroid/icu/util/ULocale;)Landroid/icu/text/DateFormat;")
    getFieldResolutionTable = JavaMethod("()[[[I")
    add = JavaMethod("(II)V")
    roll = JavaMethod("(II)V")
    handleComputeFields = JavaMethod("(I)V")
    handleComputeMonthStart = JavaMethod("(IIZ)I")
    getType = JavaMethod("()Ljava/lang/String;")