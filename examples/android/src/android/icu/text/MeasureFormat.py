from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MeasureFormat"]

class MeasureFormat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/MeasureFormat"
    getInstance = JavaMultipleMethod([("(Landroid/icu/util/ULocale;Landroid/icu/text/MeasureFormat$FormatWidth;)Landroid/icu/text/MeasureFormat;", True, False), ("(Ljava/util/Locale;Landroid/icu/text/MeasureFormat$FormatWidth;)Landroid/icu/text/MeasureFormat;", True, False), ("(Landroid/icu/util/ULocale;Landroid/icu/text/MeasureFormat$FormatWidth;Landroid/icu/text/NumberFormat;)Landroid/icu/text/MeasureFormat;", True, False), ("(Ljava/util/Locale;Landroid/icu/text/MeasureFormat$FormatWidth;Landroid/icu/text/NumberFormat;)Landroid/icu/text/MeasureFormat;", True, False)])
    format = JavaMethod("(Ljava/lang/Object;Ljava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;")
    parseObject = JavaMethod("(Ljava/lang/String;Ljava/text/ParsePosition;)Landroid/icu/util/Measure;")
    formatMeasures = JavaMultipleMethod([("([Landroid/icu/util/Measure;)Ljava/lang/String;", False, True), ("(Ljava/lang/StringBuilder;Ljava/text/FieldPosition;[Landroid/icu/util/Measure;)Ljava/lang/StringBuilder;", False, True)])
    formatMeasurePerUnit = JavaMethod("(Landroid/icu/util/Measure;Landroid/icu/util/MeasureUnit;Ljava/lang/StringBuilder;Ljava/text/FieldPosition;)Ljava/lang/StringBuilder;")
    getUnitDisplayName = JavaMethod("(Landroid/icu/util/MeasureUnit;)Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getWidth = JavaMethod("()Landroid/icu/text/MeasureFormat$FormatWidth;")
    getLocale = JavaMethod("()Landroid/icu/util/ULocale;")
    getNumberFormat = JavaMethod("()Landroid/icu/text/NumberFormat;")
    getCurrencyFormat = JavaMultipleMethod([("(Landroid/icu/util/ULocale;)Landroid/icu/text/MeasureFormat;", True, False), ("(Ljava/util/Locale;)Landroid/icu/text/MeasureFormat;", True, False), ("()Landroid/icu/text/MeasureFormat;", True, False)])

    class FormatWidth(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/MeasureFormat/FormatWidth"
        values = JavaStaticMethod("()[Landroid/icu/text/MeasureFormat$FormatWidth;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/MeasureFormat$FormatWidth;")
        WIDE = JavaStaticField("Landroid/icu/text/MeasureFormat/FormatWidth;")
        SHORT = JavaStaticField("Landroid/icu/text/MeasureFormat/FormatWidth;")
        NARROW = JavaStaticField("Landroid/icu/text/MeasureFormat/FormatWidth;")
        NUMERIC = JavaStaticField("Landroid/icu/text/MeasureFormat/FormatWidth;")