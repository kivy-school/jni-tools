from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CompactDecimalFormat"]

class CompactDecimalFormat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/CompactDecimalFormat"
    MINIMUM_GROUPING_DIGITS_AUTO = JavaStaticField("I")
    MINIMUM_GROUPING_DIGITS_MIN2 = JavaStaticField("I")
    PAD_AFTER_PREFIX = JavaStaticField("I")
    PAD_AFTER_SUFFIX = JavaStaticField("I")
    PAD_BEFORE_PREFIX = JavaStaticField("I")
    PAD_BEFORE_SUFFIX = JavaStaticField("I")
    ACCOUNTINGCURRENCYSTYLE = JavaStaticField("I")
    CASHCURRENCYSTYLE = JavaStaticField("I")
    CURRENCYSTYLE = JavaStaticField("I")
    FRACTION_FIELD = JavaStaticField("I")
    INTEGERSTYLE = JavaStaticField("I")
    INTEGER_FIELD = JavaStaticField("I")
    ISOCURRENCYSTYLE = JavaStaticField("I")
    NUMBERSTYLE = JavaStaticField("I")
    PERCENTSTYLE = JavaStaticField("I")
    PLURALCURRENCYSTYLE = JavaStaticField("I")
    SCIENTIFICSTYLE = JavaStaticField("I")
    STANDARDCURRENCYSTYLE = JavaStaticField("I")
    parseCurrency = JavaMethod("(Ljava/lang/CharSequence;Ljava/text/ParsePosition;)Landroid/icu/util/CurrencyAmount;")
    getInstance = JavaMultipleMethod([("(Landroid/icu/util/ULocale;Landroid/icu/text/CompactDecimalFormat$CompactStyle;)Landroid/icu/text/CompactDecimalFormat;", True, False), ("(Ljava/util/Locale;Landroid/icu/text/CompactDecimalFormat$CompactStyle;)Landroid/icu/text/CompactDecimalFormat;", True, False)])
    parse = JavaMethod("(Ljava/lang/String;Ljava/text/ParsePosition;)Ljava/lang/Number;")

    class CompactStyle(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/CompactDecimalFormat$CompactStyle"
        LONG = JavaStaticField("Landroid/icu/text/CompactDecimalFormat$CompactStyle;")
        SHORT = JavaStaticField("Landroid/icu/text/CompactDecimalFormat$CompactStyle;")
        values = JavaStaticMethod("()[Landroid/icu/text/CompactDecimalFormat$CompactStyle;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/CompactDecimalFormat$CompactStyle;")
        LONG = JavaStaticField("Landroid/icu/text/CompactDecimalFormat$CompactStyle;")
        SHORT = JavaStaticField("Landroid/icu/text/CompactDecimalFormat$CompactStyle;")