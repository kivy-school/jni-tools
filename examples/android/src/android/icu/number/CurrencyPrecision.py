from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CurrencyPrecision"]

class CurrencyPrecision(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/CurrencyPrecision"
    withCurrency = JavaMethod("(Landroid/icu/util/Currency;)Landroid/icu/number/Precision;")