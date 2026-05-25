from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocalizedNumberRangeFormatter"]

class LocalizedNumberRangeFormatter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/LocalizedNumberRangeFormatter"
    formatRange = JavaMultipleMethod([("(II)Landroid/icu/number/FormattedNumberRange;", False, False), ("(DD)Landroid/icu/number/FormattedNumberRange;", False, False), ("(Ljava/lang/Number;Ljava/lang/Number;)Landroid/icu/number/FormattedNumberRange;", False, False)])