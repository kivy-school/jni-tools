from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NumberFormatter"]

class NumberFormatter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/NumberFormatter"
    with = JavaStaticMethod("()Landroid/icu/number/UnlocalizedNumberFormatter;")
    withLocale = JavaMultipleMethod([("(Ljava/util/Locale;)Landroid/icu/number/LocalizedNumberFormatter;", True, False), ("(Landroid/icu/util/ULocale;)Landroid/icu/number/LocalizedNumberFormatter;", True, False)])

    class DecimalSeparatorDisplay(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/number/NumberFormatter/DecimalSeparatorDisplay"
        values = JavaStaticMethod("()[Landroid/icu/number/NumberFormatter$DecimalSeparatorDisplay;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/number/NumberFormatter$DecimalSeparatorDisplay;")
        AUTO = JavaStaticField("Landroid/icu/number/NumberFormatter/DecimalSeparatorDisplay;")
        ALWAYS = JavaStaticField("Landroid/icu/number/NumberFormatter/DecimalSeparatorDisplay;")

    class GroupingStrategy(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/number/NumberFormatter/GroupingStrategy"
        values = JavaStaticMethod("()[Landroid/icu/number/NumberFormatter$GroupingStrategy;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/number/NumberFormatter$GroupingStrategy;")
        OFF = JavaStaticField("Landroid/icu/number/NumberFormatter/GroupingStrategy;")
        MIN2 = JavaStaticField("Landroid/icu/number/NumberFormatter/GroupingStrategy;")
        AUTO = JavaStaticField("Landroid/icu/number/NumberFormatter/GroupingStrategy;")
        ON_ALIGNED = JavaStaticField("Landroid/icu/number/NumberFormatter/GroupingStrategy;")
        THOUSANDS = JavaStaticField("Landroid/icu/number/NumberFormatter/GroupingStrategy;")

    class RoundingPriority(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/number/NumberFormatter/RoundingPriority"
        values = JavaStaticMethod("()[Landroid/icu/number/NumberFormatter$RoundingPriority;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/number/NumberFormatter$RoundingPriority;")
        RELAXED = JavaStaticField("Landroid/icu/number/NumberFormatter/RoundingPriority;")
        STRICT = JavaStaticField("Landroid/icu/number/NumberFormatter/RoundingPriority;")

    class SignDisplay(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/number/NumberFormatter/SignDisplay"
        values = JavaStaticMethod("()[Landroid/icu/number/NumberFormatter$SignDisplay;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/number/NumberFormatter$SignDisplay;")
        AUTO = JavaStaticField("Landroid/icu/number/NumberFormatter/SignDisplay;")
        ALWAYS = JavaStaticField("Landroid/icu/number/NumberFormatter/SignDisplay;")
        NEVER = JavaStaticField("Landroid/icu/number/NumberFormatter/SignDisplay;")
        ACCOUNTING = JavaStaticField("Landroid/icu/number/NumberFormatter/SignDisplay;")
        ACCOUNTING_ALWAYS = JavaStaticField("Landroid/icu/number/NumberFormatter/SignDisplay;")
        EXCEPT_ZERO = JavaStaticField("Landroid/icu/number/NumberFormatter/SignDisplay;")
        ACCOUNTING_EXCEPT_ZERO = JavaStaticField("Landroid/icu/number/NumberFormatter/SignDisplay;")
        NEGATIVE = JavaStaticField("Landroid/icu/number/NumberFormatter/SignDisplay;")
        ACCOUNTING_NEGATIVE = JavaStaticField("Landroid/icu/number/NumberFormatter/SignDisplay;")

    class TrailingZeroDisplay(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/number/NumberFormatter/TrailingZeroDisplay"
        values = JavaStaticMethod("()[Landroid/icu/number/NumberFormatter$TrailingZeroDisplay;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/number/NumberFormatter$TrailingZeroDisplay;")
        AUTO = JavaStaticField("Landroid/icu/number/NumberFormatter/TrailingZeroDisplay;")
        HIDE_IF_WHOLE = JavaStaticField("Landroid/icu/number/NumberFormatter/TrailingZeroDisplay;")

    class UnitWidth(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/number/NumberFormatter/UnitWidth"
        values = JavaStaticMethod("()[Landroid/icu/number/NumberFormatter$UnitWidth;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/number/NumberFormatter$UnitWidth;")
        NARROW = JavaStaticField("Landroid/icu/number/NumberFormatter/UnitWidth;")
        SHORT = JavaStaticField("Landroid/icu/number/NumberFormatter/UnitWidth;")
        FULL_NAME = JavaStaticField("Landroid/icu/number/NumberFormatter/UnitWidth;")
        ISO_CODE = JavaStaticField("Landroid/icu/number/NumberFormatter/UnitWidth;")
        FORMAL = JavaStaticField("Landroid/icu/number/NumberFormatter/UnitWidth;")
        VARIANT = JavaStaticField("Landroid/icu/number/NumberFormatter/UnitWidth;")
        HIDDEN = JavaStaticField("Landroid/icu/number/NumberFormatter/UnitWidth;")