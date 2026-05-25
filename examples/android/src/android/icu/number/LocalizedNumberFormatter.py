from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocalizedNumberFormatter"]

class LocalizedNumberFormatter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/LocalizedNumberFormatter"
    format = JavaMultipleMethod([("(J)Landroid/icu/number/FormattedNumber;", False, False), ("(D)Landroid/icu/number/FormattedNumber;", False, False), ("(Ljava/lang/Number;)Landroid/icu/number/FormattedNumber;", False, False), ("(Landroid/icu/util/Measure;)Landroid/icu/number/FormattedNumber;", False, False)])
    toFormat = JavaMethod("()Ljava/text/Format;")