from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Currency"]

class Currency(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Currency"
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/util/Currency;", True, False), ("(Ljava/util/Locale;)Ljava/util/Currency;", True, False)])
    getAvailableCurrencies = JavaStaticMethod("()Ljava/util/Set;")
    getCurrencyCode = JavaMethod("()Ljava/lang/String;")
    getSymbol = JavaMultipleMethod([("()Ljava/lang/String;", False, False), ("(Ljava/util/Locale;)Ljava/lang/String;", False, False)])
    getDefaultFractionDigits = JavaMethod("()I")
    getNumericCode = JavaMethod("()I")
    getNumericCodeAsString = JavaMethod("()Ljava/lang/String;")
    getDisplayName = JavaMultipleMethod([("()Ljava/lang/String;", False, False), ("(Ljava/util/Locale;)Ljava/lang/String;", False, False)])
    toString = JavaMethod("()Ljava/lang/String;")