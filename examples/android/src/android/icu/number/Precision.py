from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Precision"]

class Precision(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/Precision"
    unlimited = JavaStaticMethod("()Landroid/icu/number/Precision;")
    integer = JavaStaticMethod("()Landroid/icu/number/FractionPrecision;")
    fixedFraction = JavaStaticMethod("(I)Landroid/icu/number/FractionPrecision;")
    minFraction = JavaStaticMethod("(I)Landroid/icu/number/FractionPrecision;")
    maxFraction = JavaStaticMethod("(I)Landroid/icu/number/FractionPrecision;")
    minMaxFraction = JavaStaticMethod("(II)Landroid/icu/number/FractionPrecision;")
    fixedSignificantDigits = JavaStaticMethod("(I)Landroid/icu/number/Precision;")
    minSignificantDigits = JavaStaticMethod("(I)Landroid/icu/number/Precision;")
    maxSignificantDigits = JavaStaticMethod("(I)Landroid/icu/number/Precision;")
    minMaxSignificantDigits = JavaStaticMethod("(II)Landroid/icu/number/Precision;")
    increment = JavaStaticMethod("(Ljava/math/BigDecimal;)Landroid/icu/number/Precision;")
    currency = JavaStaticMethod("(Landroid/icu/util/Currency$CurrencyUsage;)Landroid/icu/number/CurrencyPrecision;")
    trailingZeroDisplay = JavaMethod("(Landroid/icu/number/NumberFormatter$TrailingZeroDisplay;)Landroid/icu/number/Precision;")