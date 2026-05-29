from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnlocalizedNumberFormatter"]

class UnlocalizedNumberFormatter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/UnlocalizedNumberFormatter"
    locale = JavaMultipleMethod([("(Ljava/util/Locale;)Landroid/icu/number/LocalizedNumberFormatter;", False, False), ("(Landroid/icu/util/ULocale;)Landroid/icu/number/LocalizedNumberFormatter;", False, False)])