from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CurrencyPluralInfo"]

class CurrencyPluralInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/CurrencyPluralInfo"
    __javaconstructor__ = [("()V", False), ("(Ljava/util/Locale;)V", False), ("(Landroid/icu/util/ULocale;)V", False)]
    getInstance = JavaMultipleMethod([("()Landroid/icu/text/CurrencyPluralInfo;", True, False), ("(Ljava/util/Locale;)Landroid/icu/text/CurrencyPluralInfo;", True, False), ("(Landroid/icu/util/ULocale;)Landroid/icu/text/CurrencyPluralInfo;", True, False)])
    getPluralRules = JavaMethod("()Landroid/icu/text/PluralRules;")
    getCurrencyPluralPattern = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getLocale = JavaMethod("()Landroid/icu/util/ULocale;")
    setPluralRules = JavaMethod("(Ljava/lang/String;)V")
    setCurrencyPluralPattern = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    setLocale = JavaMethod("(Landroid/icu/util/ULocale;)V")
    clone = JavaMethod("()Ljava/lang/Object;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")