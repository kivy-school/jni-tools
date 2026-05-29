from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocalizedNumberFormatter"]

class LocalizedNumberFormatter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/LocalizedNumberFormatter"
    toFormat = JavaMethod("()Ljava/text/Format;")
    withoutLocale = JavaMethod("()Landroid/icu/number/UnlocalizedNumberFormatter;")
    format = JavaMultipleMethod([("(Ljava/lang/Number;)Landroid/icu/number/FormattedNumber;", False, False), ("(Landroid/icu/util/Measure;)Landroid/icu/number/FormattedNumber;", False, False), ("(J)Landroid/icu/number/FormattedNumber;", False, False), ("(D)Landroid/icu/number/FormattedNumber;", False, False)])