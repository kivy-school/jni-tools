from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Currency"]

class Currency(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Currency"
    toString = JavaMethod("()Ljava/lang/String;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/util/Currency;", True, False), ("(Ljava/util/Locale;)Ljava/util/Currency;", True, False)])
    getDisplayName = JavaMultipleMethod([("(Ljava/util/Locale;)Ljava/lang/String;", False, False), ("()Ljava/lang/String;", False, False)])
    getSymbol = JavaMultipleMethod([("(Ljava/util/Locale;)Ljava/lang/String;", False, False), ("()Ljava/lang/String;", False, False)])
    getAvailableCurrencies = JavaStaticMethod("()Ljava/util/Set;")
    availableCurrencies = JavaStaticMethod("()Ljava/util/stream/Stream;")
    getCurrencyCode = JavaMethod("()Ljava/lang/String;")
    getDefaultFractionDigits = JavaMethod("()I")
    getNumericCode = JavaMethod("()I")
    getNumericCodeAsString = JavaMethod("()Ljava/lang/String;")