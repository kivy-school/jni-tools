from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NumberRangeFormatter"]

class NumberRangeFormatter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/NumberRangeFormatter"
    with = JavaStaticMethod("()Landroid/icu/number/UnlocalizedNumberRangeFormatter;")
    withLocale = JavaMultipleMethod([("(Ljava/util/Locale;)Landroid/icu/number/LocalizedNumberRangeFormatter;", True, False), ("(Landroid/icu/util/ULocale;)Landroid/icu/number/LocalizedNumberRangeFormatter;", True, False)])

    class RangeIdentityResult(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/number/NumberRangeFormatter$RangeIdentityResult"
        EQUAL_AFTER_ROUNDING = JavaStaticField("Landroid/icu/number/NumberRangeFormatter$RangeIdentityResult;")
        EQUAL_BEFORE_ROUNDING = JavaStaticField("Landroid/icu/number/NumberRangeFormatter$RangeIdentityResult;")
        NOT_EQUAL = JavaStaticField("Landroid/icu/number/NumberRangeFormatter$RangeIdentityResult;")
        values = JavaStaticMethod("()[Landroid/icu/number/NumberRangeFormatter$RangeIdentityResult;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/number/NumberRangeFormatter$RangeIdentityResult;")
        EQUAL_AFTER_ROUNDING = JavaStaticField("Landroid/icu/number/NumberRangeFormatter$RangeIdentityResult;")
        EQUAL_BEFORE_ROUNDING = JavaStaticField("Landroid/icu/number/NumberRangeFormatter$RangeIdentityResult;")
        NOT_EQUAL = JavaStaticField("Landroid/icu/number/NumberRangeFormatter$RangeIdentityResult;")

    class RangeIdentityFallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/number/NumberRangeFormatter$RangeIdentityFallback"
        APPROXIMATELY = JavaStaticField("Landroid/icu/number/NumberRangeFormatter$RangeIdentityFallback;")
        APPROXIMATELY_OR_SINGLE_VALUE = JavaStaticField("Landroid/icu/number/NumberRangeFormatter$RangeIdentityFallback;")
        RANGE = JavaStaticField("Landroid/icu/number/NumberRangeFormatter$RangeIdentityFallback;")
        SINGLE_VALUE = JavaStaticField("Landroid/icu/number/NumberRangeFormatter$RangeIdentityFallback;")
        values = JavaStaticMethod("()[Landroid/icu/number/NumberRangeFormatter$RangeIdentityFallback;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/number/NumberRangeFormatter$RangeIdentityFallback;")
        APPROXIMATELY = JavaStaticField("Landroid/icu/number/NumberRangeFormatter$RangeIdentityFallback;")
        APPROXIMATELY_OR_SINGLE_VALUE = JavaStaticField("Landroid/icu/number/NumberRangeFormatter$RangeIdentityFallback;")
        RANGE = JavaStaticField("Landroid/icu/number/NumberRangeFormatter$RangeIdentityFallback;")
        SINGLE_VALUE = JavaStaticField("Landroid/icu/number/NumberRangeFormatter$RangeIdentityFallback;")

    class RangeCollapse(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/number/NumberRangeFormatter$RangeCollapse"
        ALL = JavaStaticField("Landroid/icu/number/NumberRangeFormatter$RangeCollapse;")
        AUTO = JavaStaticField("Landroid/icu/number/NumberRangeFormatter$RangeCollapse;")
        NONE = JavaStaticField("Landroid/icu/number/NumberRangeFormatter$RangeCollapse;")
        UNIT = JavaStaticField("Landroid/icu/number/NumberRangeFormatter$RangeCollapse;")
        values = JavaStaticMethod("()[Landroid/icu/number/NumberRangeFormatter$RangeCollapse;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/number/NumberRangeFormatter$RangeCollapse;")
        ALL = JavaStaticField("Landroid/icu/number/NumberRangeFormatter$RangeCollapse;")
        AUTO = JavaStaticField("Landroid/icu/number/NumberRangeFormatter$RangeCollapse;")
        NONE = JavaStaticField("Landroid/icu/number/NumberRangeFormatter$RangeCollapse;")
        UNIT = JavaStaticField("Landroid/icu/number/NumberRangeFormatter$RangeCollapse;")