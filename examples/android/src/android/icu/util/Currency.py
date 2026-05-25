from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Currency"]

class Currency(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/Currency"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    FORMAL_SYMBOL_NAME = JavaStaticField("I")
    LONG_NAME = JavaStaticField("I")
    NARROW_SYMBOL_NAME = JavaStaticField("I")
    PLURAL_LONG_NAME = JavaStaticField("I")
    SYMBOL_NAME = JavaStaticField("I")
    VARIANT_SYMBOL_NAME = JavaStaticField("I")
    getInstance = JavaMultipleMethod([("(Ljava/util/Locale;)Landroid/icu/util/Currency;", True, False), ("(Landroid/icu/util/ULocale;)Landroid/icu/util/Currency;", True, False), ("(Ljava/lang/String;)Landroid/icu/util/Currency;", True, False)])
    getAvailableCurrencyCodes = JavaMultipleMethod([("(Landroid/icu/util/ULocale;Ljava/util/Date;)[Ljava/lang/String;", True, False), ("(Ljava/util/Locale;Ljava/util/Date;)[Ljava/lang/String;", True, False)])
    getAvailableCurrencies = JavaStaticMethod("()Ljava/util/Set;")
    fromJavaCurrency = JavaStaticMethod("(Ljava/util/Currency;)Landroid/icu/util/Currency;")
    toJavaCurrency = JavaMethod("()Ljava/util/Currency;")
    getAvailableLocales = JavaStaticMethod("()[Ljava/util/Locale;")
    getAvailableULocales = JavaStaticMethod("()[Landroid/icu/util/ULocale;")
    getKeywordValuesForLocale = JavaStaticMethod("(Ljava/lang/String;Landroid/icu/util/ULocale;Z)[Ljava/lang/String;")
    getCurrencyCode = JavaMethod("()Ljava/lang/String;")
    getNumericCode = JavaMethod("()I")
    getSymbol = JavaMultipleMethod([("()Ljava/lang/String;", False, False), ("(Ljava/util/Locale;)Ljava/lang/String;", False, False), ("(Landroid/icu/util/ULocale;)Ljava/lang/String;", False, False)])
    getName = JavaMultipleMethod([("(Ljava/util/Locale;I[Z)Ljava/lang/String;", False, False), ("(Landroid/icu/util/ULocale;I[Z)Ljava/lang/String;", False, False), ("(Ljava/util/Locale;ILjava/lang/String;[Z)Ljava/lang/String;", False, False), ("(Landroid/icu/util/ULocale;ILjava/lang/String;[Z)Ljava/lang/String;", False, False)])
    getDisplayName = JavaMultipleMethod([("()Ljava/lang/String;", False, False), ("(Ljava/util/Locale;)Ljava/lang/String;", False, False)])
    getDefaultFractionDigits = JavaMultipleMethod([("()I", False, False), ("(Landroid/icu/util/Currency$CurrencyUsage;)I", False, False)])
    getRoundingIncrement = JavaMultipleMethod([("()D", False, False), ("(Landroid/icu/util/Currency$CurrencyUsage;)D", False, False)])
    toString = JavaMethod("()Ljava/lang/String;")
    isAvailable = JavaStaticMethod("(Ljava/lang/String;Ljava/util/Date;Ljava/util/Date;)Z")

    class CurrencyUsage(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/util/Currency/CurrencyUsage"
        values = JavaStaticMethod("()[Landroid/icu/util/Currency$CurrencyUsage;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/util/Currency$CurrencyUsage;")
        STANDARD = JavaStaticField("Landroid/icu/util/Currency/CurrencyUsage;")
        CASH = JavaStaticField("Landroid/icu/util/Currency/CurrencyUsage;")