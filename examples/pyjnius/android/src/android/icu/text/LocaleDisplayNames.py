from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocaleDisplayNames"]

class LocaleDisplayNames(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/LocaleDisplayNames"
    getInstance = JavaMultipleMethod([("(Landroid/icu/util/ULocale;[Landroid/icu/text/DisplayContext;)Landroid/icu/text/LocaleDisplayNames;", True, True), ("(Landroid/icu/util/ULocale;Landroid/icu/text/LocaleDisplayNames$DialectHandling;)Landroid/icu/text/LocaleDisplayNames;", True, False), ("(Ljava/util/Locale;)Landroid/icu/text/LocaleDisplayNames;", True, False), ("(Ljava/util/Locale;[Landroid/icu/text/DisplayContext;)Landroid/icu/text/LocaleDisplayNames;", True, True), ("(Landroid/icu/util/ULocale;)Landroid/icu/text/LocaleDisplayNames;", True, False)])
    getContext = JavaMethod("(Landroid/icu/text/DisplayContext$Type;)Landroid/icu/text/DisplayContext;")
    getDialectHandling = JavaMethod("()Landroid/icu/text/LocaleDisplayNames$DialectHandling;")
    getUiList = JavaMethod("(Ljava/util/Set;ZLjava/util/Comparator;)Ljava/util/List;")
    getUiListCompareWholeItems = JavaMethod("(Ljava/util/Set;Ljava/util/Comparator;)Ljava/util/List;")
    keyDisplayName = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    keyValueDisplayName = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")
    languageDisplayName = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    localeDisplayName = JavaMultipleMethod([("(Landroid/icu/util/ULocale;)Ljava/lang/String;", False, False), ("(Ljava/util/Locale;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False)])
    regionDisplayName = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    scriptDisplayName = JavaMultipleMethod([("(I)Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False)])
    variantDisplayName = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getLocale = JavaMethod("()Landroid/icu/util/ULocale;")

    class UiListItem(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/LocaleDisplayNames$UiListItem"
        __javaconstructor__ = [("(Landroid/icu/util/ULocale;Landroid/icu/util/ULocale;Ljava/lang/String;Ljava/lang/String;)V", False)]
        minimized = JavaField("Landroid/icu/util/ULocale;")
        modified = JavaField("Landroid/icu/util/ULocale;")
        nameInDisplayLocale = JavaField("Ljava/lang/String;")
        nameInSelf = JavaField("Ljava/lang/String;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")
        hashCode = JavaMethod("()I")
        getComparator = JavaStaticMethod("(Ljava/util/Comparator;Z)Ljava/util/Comparator;")

    class DialectHandling(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/LocaleDisplayNames$DialectHandling"
        DIALECT_NAMES = JavaStaticField("Landroid/icu/text/LocaleDisplayNames$DialectHandling;")
        STANDARD_NAMES = JavaStaticField("Landroid/icu/text/LocaleDisplayNames$DialectHandling;")
        values = JavaStaticMethod("()[Landroid/icu/text/LocaleDisplayNames$DialectHandling;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/text/LocaleDisplayNames$DialectHandling;")
        DIALECT_NAMES = JavaStaticField("Landroid/icu/text/LocaleDisplayNames$DialectHandling;")
        STANDARD_NAMES = JavaStaticField("Landroid/icu/text/LocaleDisplayNames$DialectHandling;")