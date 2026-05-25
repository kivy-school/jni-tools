from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FractionPrecision"]

class FractionPrecision(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/FractionPrecision"
    withSignificantDigits = JavaMethod("(IILandroid/icu/number/NumberFormatter$RoundingPriority;)Landroid/icu/number/Precision;")
    withMinDigits = JavaMethod("(I)Landroid/icu/number/Precision;")
    withMaxDigits = JavaMethod("(I)Landroid/icu/number/Precision;")