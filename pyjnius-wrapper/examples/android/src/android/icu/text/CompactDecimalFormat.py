from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CompactDecimalFormat"]

class CompactDecimalFormat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/CompactDecimalFormat"
    getInstance = JavaMultipleMethod([("(Landroid/icu/util/ULocale;Landroid/icu/text/CompactDecimalFormat$CompactStyle;)Landroid/icu/text/CompactDecimalFormat;", True, False), ("(Ljava/util/Locale;Landroid/icu/text/CompactDecimalFormat$CompactStyle;)Landroid/icu/text/CompactDecimalFormat;", True, False)])
    parse = JavaMethod("(Ljava/lang/String;Ljava/text/ParsePosition;)Ljava/lang/Number;")
    parseCurrency = JavaMethod("(Ljava/lang/CharSequence;Ljava/text/ParsePosition;)Landroid/icu/util/CurrencyAmount;")

    class CompactStyle(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/CompactDecimalFormat/CompactStyle"
        values = JavaStaticMethod("()[Landroid/icu/text/CompactDecimalFormat$CompactStyle;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/CompactDecimalFormat$CompactStyle;")
        SHORT = JavaStaticField("Landroid/icu/text/CompactDecimalFormat/CompactStyle;")
        LONG = JavaStaticField("Landroid/icu/text/CompactDecimalFormat/CompactStyle;")