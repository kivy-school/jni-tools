from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnlocalizedNumberRangeFormatter"]

class UnlocalizedNumberRangeFormatter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/UnlocalizedNumberRangeFormatter"
    locale = JavaMultipleMethod([("(Ljava/util/Locale;)Landroid/icu/number/LocalizedNumberRangeFormatter;", False, False), ("(Landroid/icu/util/ULocale;)Landroid/icu/number/LocalizedNumberRangeFormatter;", False, False)])