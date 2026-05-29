from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NumberRangeFormatterSettings"]

class NumberRangeFormatterSettings(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/NumberRangeFormatterSettings"
    collapse = JavaMethod("(Landroid/icu/number/NumberRangeFormatter$RangeCollapse;)Landroid/icu/number/NumberRangeFormatterSettings;")
    identityFallback = JavaMethod("(Landroid/icu/number/NumberRangeFormatter$RangeIdentityFallback;)Landroid/icu/number/NumberRangeFormatterSettings;")
    numberFormatterBoth = JavaMethod("(Landroid/icu/number/UnlocalizedNumberFormatter;)Landroid/icu/number/NumberRangeFormatterSettings;")
    numberFormatterFirst = JavaMethod("(Landroid/icu/number/UnlocalizedNumberFormatter;)Landroid/icu/number/NumberRangeFormatterSettings;")
    numberFormatterSecond = JavaMethod("(Landroid/icu/number/UnlocalizedNumberFormatter;)Landroid/icu/number/NumberRangeFormatterSettings;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")