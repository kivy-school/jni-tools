from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnlocalizedNumberFormatter"]

class UnlocalizedNumberFormatter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/UnlocalizedNumberFormatter"
    locale = JavaMultipleMethod([("(Landroid/icu/util/ULocale;)Landroid/icu/number/LocalizedNumberFormatter;", False, False), ("(Ljava/util/Locale;)Landroid/icu/number/LocalizedNumberFormatter;", False, False)])