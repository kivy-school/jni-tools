from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MeasureFormat"]

class MeasureFormat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/MeasureFormat"
    getNumberFormat = JavaMethod("()Landroid/icu/text/NumberFormat;")
    parseObject = JavaMultipleMethod([("(Ljava/lang/String;Ljava/text/ParsePosition;)Ljava/lang/Object;", False, False), ("(Ljava/lang/String;Ljava/text/ParsePosition;)Landroid/icu/util/Measure;", False, False)])
    getCurrencyFormat = JavaMultipleMethod([("(Landroid/icu/util/ULocale;)Landroid/icu/text/MeasureFormat;", True, False), ("()Landroid/icu/text/MeasureFormat;", True, False), ("(Ljava/util/Locale;)Landroid/icu/text/MeasureFormat;", True, False)])
    getUnitDisplayName = JavaMethod("(Landroid/icu/util/MeasureUnit;)Ljava/lang/String;")
    formatMeasures = JavaMultipleMethod([("(Ljava/lang/StringBuilder;Ljava/text/FieldPosition;[Landroid/icu/util/Measure;)Ljava/lang/StringBuilder;", False, True), ("([Landroid/icu/util/Measure;)Ljava/lang/String;", False, True)])
    formatMeasurePerUnit = JavaMethod("(Landroid/icu/util/Measure;Landroid/icu/util/MeasureUnit;Ljava/lang/StringBuilder;Ljava/text/FieldPosition;)Ljava/lang/StringBuilder;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    format = JavaMethod("(Ljava/lang/Object;Ljava/lang/StringBuffer;Ljava/text/FieldPosition;)Ljava/lang/StringBuffer;")
    getInstance = JavaMultipleMethod([("(Landroid/icu/util/ULocale;Landroid/icu/text/MeasureFormat$FormatWidth;Landroid/icu/text/NumberFormat;)Landroid/icu/text/MeasureFormat;", True, False), ("(Ljava/util/Locale;Landroid/icu/text/MeasureFormat$FormatWidth;)Landroid/icu/text/MeasureFormat;", True, False), ("(Ljava/util/Locale;Landroid/icu/text/MeasureFormat$FormatWidth;Landroid/icu/text/NumberFormat;)Landroid/icu/text/MeasureFormat;", True, False), ("(Landroid/icu/util/ULocale;Landroid/icu/text/MeasureFormat$FormatWidth;)Landroid/icu/text/MeasureFormat;", True, False)])
    getWidth = JavaMethod("()Landroid/icu/text/MeasureFormat$FormatWidth;")
    getLocale = JavaMethod("()Landroid/icu/util/ULocale;")

    class FormatWidth(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/MeasureFormat$FormatWidth"
        NARROW = JavaStaticField("Landroid/icu/text/MeasureFormat$FormatWidth;")
        NUMERIC = JavaStaticField("Landroid/icu/text/MeasureFormat$FormatWidth;")
        SHORT = JavaStaticField("Landroid/icu/text/MeasureFormat$FormatWidth;")
        WIDE = JavaStaticField("Landroid/icu/text/MeasureFormat$FormatWidth;")
        values = JavaStaticMethod("()[Landroid/icu/text/MeasureFormat$FormatWidth;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/MeasureFormat$FormatWidth;")
        NARROW = JavaStaticField("Landroid/icu/text/MeasureFormat$FormatWidth;")
        NUMERIC = JavaStaticField("Landroid/icu/text/MeasureFormat$FormatWidth;")
        SHORT = JavaStaticField("Landroid/icu/text/MeasureFormat$FormatWidth;")
        WIDE = JavaStaticField("Landroid/icu/text/MeasureFormat$FormatWidth;")