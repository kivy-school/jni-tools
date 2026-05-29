from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CurrencyPluralInfo"]

class CurrencyPluralInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/CurrencyPluralInfo"
    __javaconstructor__ = [("()V", False), ("(Ljava/util/Locale;)V", False), ("(Landroid/icu/util/ULocale;)V", False)]
    getCurrencyPluralPattern = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getPluralRules = JavaMethod("()Landroid/icu/text/PluralRules;")
    setPluralRules = JavaMethod("(Ljava/lang/String;)V")
    setCurrencyPluralPattern = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")
    getInstance = JavaMultipleMethod([("(Landroid/icu/util/ULocale;)Landroid/icu/text/CurrencyPluralInfo;", True, False), ("()Landroid/icu/text/CurrencyPluralInfo;", True, False), ("(Ljava/util/Locale;)Landroid/icu/text/CurrencyPluralInfo;", True, False)])
    getLocale = JavaMethod("()Landroid/icu/util/ULocale;")
    setLocale = JavaMethod("(Landroid/icu/util/ULocale;)V")