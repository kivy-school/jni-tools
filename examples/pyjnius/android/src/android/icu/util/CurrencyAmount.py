from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CurrencyAmount"]

class CurrencyAmount(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/CurrencyAmount"
    __javaconstructor__ = [("(Ljava/lang/Number;Ljava/util/Currency;)V", False), ("(Ljava/lang/Number;Landroid/icu/util/Currency;)V", False), ("(DLjava/util/Currency;)V", False), ("(DLandroid/icu/util/Currency;)V", False)]
    getCurrency = JavaMethod("()Landroid/icu/util/Currency;")