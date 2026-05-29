from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnlocalizedNumberRangeFormatter"]

class UnlocalizedNumberRangeFormatter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/UnlocalizedNumberRangeFormatter"
    locale = JavaMultipleMethod([("(Landroid/icu/util/ULocale;)Landroid/icu/number/LocalizedNumberRangeFormatter;", False, False), ("(Ljava/util/Locale;)Landroid/icu/number/LocalizedNumberRangeFormatter;", False, False)])