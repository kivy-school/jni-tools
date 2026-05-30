from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class FractionPrecision(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/FractionPrecision"
    withMaxDigits = JavaMethod("(I)Landroid/icu/number/Precision;")
    withMinDigits = JavaMethod("(I)Landroid/icu/number/Precision;")
    withSignificantDigits = JavaMethod("(IILandroid/icu/number/NumberFormatter$RoundingPriority;)Landroid/icu/number/Precision;")

class Scale(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/Scale"
    none = JavaStaticMethod("()Landroid/icu/number/Scale;")
    byBigDecimal = JavaStaticMethod("(Ljava/math/BigDecimal;)Landroid/icu/number/Scale;")
    byDouble = JavaStaticMethod("(D)Landroid/icu/number/Scale;")
    byDoubleAndPowerOfTen = JavaStaticMethod("(DI)Landroid/icu/number/Scale;")
    powerOfTen = JavaStaticMethod("(I)Landroid/icu/number/Scale;")

class Precision(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/Precision"
    currency = JavaStaticMethod("(Landroid/icu/util/Currency$CurrencyUsage;)Landroid/icu/number/CurrencyPrecision;")
    integer = JavaStaticMethod("()Landroid/icu/number/FractionPrecision;")
    maxSignificantDigits = JavaStaticMethod("(I)Landroid/icu/number/Precision;")
    minSignificantDigits = JavaStaticMethod("(I)Landroid/icu/number/Precision;")
    fixedFraction = JavaStaticMethod("(I)Landroid/icu/number/FractionPrecision;")
    fixedSignificantDigits = JavaStaticMethod("(I)Landroid/icu/number/Precision;")
    minMaxSignificantDigits = JavaStaticMethod("(II)Landroid/icu/number/Precision;")
    maxFraction = JavaStaticMethod("(I)Landroid/icu/number/FractionPrecision;")
    minFraction = JavaStaticMethod("(I)Landroid/icu/number/FractionPrecision;")
    minMaxFraction = JavaStaticMethod("(II)Landroid/icu/number/FractionPrecision;")
    trailingZeroDisplay = JavaMethod("(Landroid/icu/number/NumberFormatter$TrailingZeroDisplay;)Landroid/icu/number/Precision;")
    unlimited = JavaStaticMethod("()Landroid/icu/number/Precision;")
    increment = JavaStaticMethod("(Ljava/math/BigDecimal;)Landroid/icu/number/Precision;")

class FormattedNumber(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/FormattedNumber"
    getNounClass = JavaMethod("()Landroid/icu/text/DisplayOptions$NounClass;")
    getOutputUnit = JavaMethod("()Landroid/icu/util/MeasureUnit;")
    nextPosition = JavaMethod("(Landroid/icu/text/ConstrainedFieldPosition;)Z")
    toCharacterIterator = JavaMethod("()Ljava/text/AttributedCharacterIterator;")
    toBigDecimal = JavaMethod("()Ljava/math/BigDecimal;")
    length = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    charAt = JavaMethod("(I)C")
    subSequence = JavaMethod("(II)Ljava/lang/CharSequence;")
    appendTo = JavaMethod("(Ljava/lang/Appendable;)Ljava/lang/Appendable;")

class IntegerWidth(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/IntegerWidth"
    zeroFillTo = JavaStaticMethod("(I)Landroid/icu/number/IntegerWidth;")
    truncateAt = JavaMethod("(I)Landroid/icu/number/IntegerWidth;")

class NumberRangeFormatterSettings(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/NumberRangeFormatterSettings"
    identityFallback = JavaMethod("(Landroid/icu/number/NumberRangeFormatter$RangeIdentityFallback;)Landroid/icu/number/NumberRangeFormatterSettings;")
    collapse = JavaMethod("(Landroid/icu/number/NumberRangeFormatter$RangeCollapse;)Landroid/icu/number/NumberRangeFormatterSettings;")
    numberFormatterBoth = JavaMethod("(Landroid/icu/number/UnlocalizedNumberFormatter;)Landroid/icu/number/NumberRangeFormatterSettings;")
    numberFormatterFirst = JavaMethod("(Landroid/icu/number/UnlocalizedNumberFormatter;)Landroid/icu/number/NumberRangeFormatterSettings;")
    numberFormatterSecond = JavaMethod("(Landroid/icu/number/UnlocalizedNumberFormatter;)Landroid/icu/number/NumberRangeFormatterSettings;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

class UnlocalizedNumberRangeFormatter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/UnlocalizedNumberRangeFormatter"
    locale = JavaMultipleMethod([("(Landroid/icu/util/ULocale;)Landroid/icu/number/LocalizedNumberRangeFormatter;", False, False), ("(Ljava/util/Locale;)Landroid/icu/number/LocalizedNumberRangeFormatter;", False, False)])

class CurrencyPrecision(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/CurrencyPrecision"
    withCurrency = JavaMethod("(Landroid/icu/util/Currency;)Landroid/icu/number/Precision;")

class NumberFormatter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/NumberFormatter"
    with = JavaStaticMethod("()Landroid/icu/number/UnlocalizedNumberFormatter;")
    withLocale = JavaMultipleMethod([("(Ljava/util/Locale;)Landroid/icu/number/LocalizedNumberFormatter;", True, False), ("(Landroid/icu/util/ULocale;)Landroid/icu/number/LocalizedNumberFormatter;", True, False)])

    class UnitWidth(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/number/NumberFormatter$UnitWidth"
        FORMAL = JavaStaticField("Landroid/icu/number/NumberFormatter$UnitWidth;")
        FULL_NAME = JavaStaticField("Landroid/icu/number/NumberFormatter$UnitWidth;")
        HIDDEN = JavaStaticField("Landroid/icu/number/NumberFormatter$UnitWidth;")
        ISO_CODE = JavaStaticField("Landroid/icu/number/NumberFormatter$UnitWidth;")
        NARROW = JavaStaticField("Landroid/icu/number/NumberFormatter$UnitWidth;")
        SHORT = JavaStaticField("Landroid/icu/number/NumberFormatter$UnitWidth;")
        VARIANT = JavaStaticField("Landroid/icu/number/NumberFormatter$UnitWidth;")
        values = JavaStaticMethod("()[Landroid/icu/number/NumberFormatter$UnitWidth;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/number/NumberFormatter$UnitWidth;")
        FORMAL = JavaStaticField("Landroid/icu/number/NumberFormatter$UnitWidth;")
        FULL_NAME = JavaStaticField("Landroid/icu/number/NumberFormatter$UnitWidth;")
        HIDDEN = JavaStaticField("Landroid/icu/number/NumberFormatter$UnitWidth;")
        ISO_CODE = JavaStaticField("Landroid/icu/number/NumberFormatter$UnitWidth;")
        NARROW = JavaStaticField("Landroid/icu/number/NumberFormatter$UnitWidth;")
        SHORT = JavaStaticField("Landroid/icu/number/NumberFormatter$UnitWidth;")
        VARIANT = JavaStaticField("Landroid/icu/number/NumberFormatter$UnitWidth;")

    class TrailingZeroDisplay(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/number/NumberFormatter$TrailingZeroDisplay"
        AUTO = JavaStaticField("Landroid/icu/number/NumberFormatter$TrailingZeroDisplay;")
        HIDE_IF_WHOLE = JavaStaticField("Landroid/icu/number/NumberFormatter$TrailingZeroDisplay;")
        values = JavaStaticMethod("()[Landroid/icu/number/NumberFormatter$TrailingZeroDisplay;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/number/NumberFormatter$TrailingZeroDisplay;")
        AUTO = JavaStaticField("Landroid/icu/number/NumberFormatter$TrailingZeroDisplay;")
        HIDE_IF_WHOLE = JavaStaticField("Landroid/icu/number/NumberFormatter$TrailingZeroDisplay;")

    class SignDisplay(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/number/NumberFormatter$SignDisplay"
        ACCOUNTING = JavaStaticField("Landroid/icu/number/NumberFormatter$SignDisplay;")
        ACCOUNTING_ALWAYS = JavaStaticField("Landroid/icu/number/NumberFormatter$SignDisplay;")
        ACCOUNTING_EXCEPT_ZERO = JavaStaticField("Landroid/icu/number/NumberFormatter$SignDisplay;")
        ACCOUNTING_NEGATIVE = JavaStaticField("Landroid/icu/number/NumberFormatter$SignDisplay;")
        ALWAYS = JavaStaticField("Landroid/icu/number/NumberFormatter$SignDisplay;")
        AUTO = JavaStaticField("Landroid/icu/number/NumberFormatter$SignDisplay;")
        EXCEPT_ZERO = JavaStaticField("Landroid/icu/number/NumberFormatter$SignDisplay;")
        NEGATIVE = JavaStaticField("Landroid/icu/number/NumberFormatter$SignDisplay;")
        NEVER = JavaStaticField("Landroid/icu/number/NumberFormatter$SignDisplay;")
        values = JavaStaticMethod("()[Landroid/icu/number/NumberFormatter$SignDisplay;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/number/NumberFormatter$SignDisplay;")
        ACCOUNTING = JavaStaticField("Landroid/icu/number/NumberFormatter$SignDisplay;")
        ACCOUNTING_ALWAYS = JavaStaticField("Landroid/icu/number/NumberFormatter$SignDisplay;")
        ACCOUNTING_EXCEPT_ZERO = JavaStaticField("Landroid/icu/number/NumberFormatter$SignDisplay;")
        ACCOUNTING_NEGATIVE = JavaStaticField("Landroid/icu/number/NumberFormatter$SignDisplay;")
        ALWAYS = JavaStaticField("Landroid/icu/number/NumberFormatter$SignDisplay;")
        AUTO = JavaStaticField("Landroid/icu/number/NumberFormatter$SignDisplay;")
        EXCEPT_ZERO = JavaStaticField("Landroid/icu/number/NumberFormatter$SignDisplay;")
        NEGATIVE = JavaStaticField("Landroid/icu/number/NumberFormatter$SignDisplay;")
        NEVER = JavaStaticField("Landroid/icu/number/NumberFormatter$SignDisplay;")

    class RoundingPriority(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/number/NumberFormatter$RoundingPriority"
        RELAXED = JavaStaticField("Landroid/icu/number/NumberFormatter$RoundingPriority;")
        STRICT = JavaStaticField("Landroid/icu/number/NumberFormatter$RoundingPriority;")
        values = JavaStaticMethod("()[Landroid/icu/number/NumberFormatter$RoundingPriority;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/number/NumberFormatter$RoundingPriority;")
        RELAXED = JavaStaticField("Landroid/icu/number/NumberFormatter$RoundingPriority;")
        STRICT = JavaStaticField("Landroid/icu/number/NumberFormatter$RoundingPriority;")

    class GroupingStrategy(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/number/NumberFormatter$GroupingStrategy"
        AUTO = JavaStaticField("Landroid/icu/number/NumberFormatter$GroupingStrategy;")
        MIN2 = JavaStaticField("Landroid/icu/number/NumberFormatter$GroupingStrategy;")
        OFF = JavaStaticField("Landroid/icu/number/NumberFormatter$GroupingStrategy;")
        ON_ALIGNED = JavaStaticField("Landroid/icu/number/NumberFormatter$GroupingStrategy;")
        THOUSANDS = JavaStaticField("Landroid/icu/number/NumberFormatter$GroupingStrategy;")
        values = JavaStaticMethod("()[Landroid/icu/number/NumberFormatter$GroupingStrategy;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/number/NumberFormatter$GroupingStrategy;")
        AUTO = JavaStaticField("Landroid/icu/number/NumberFormatter$GroupingStrategy;")
        MIN2 = JavaStaticField("Landroid/icu/number/NumberFormatter$GroupingStrategy;")
        OFF = JavaStaticField("Landroid/icu/number/NumberFormatter$GroupingStrategy;")
        ON_ALIGNED = JavaStaticField("Landroid/icu/number/NumberFormatter$GroupingStrategy;")
        THOUSANDS = JavaStaticField("Landroid/icu/number/NumberFormatter$GroupingStrategy;")

    class DecimalSeparatorDisplay(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/number/NumberFormatter$DecimalSeparatorDisplay"
        ALWAYS = JavaStaticField("Landroid/icu/number/NumberFormatter$DecimalSeparatorDisplay;")
        AUTO = JavaStaticField("Landroid/icu/number/NumberFormatter$DecimalSeparatorDisplay;")
        values = JavaStaticMethod("()[Landroid/icu/number/NumberFormatter$DecimalSeparatorDisplay;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/icu/number/NumberFormatter$DecimalSeparatorDisplay;")
        ALWAYS = JavaStaticField("Landroid/icu/number/NumberFormatter$DecimalSeparatorDisplay;")
        AUTO = JavaStaticField("Landroid/icu/number/NumberFormatter$DecimalSeparatorDisplay;")

class FormattedNumberRange(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/FormattedNumberRange"
    getFirstBigDecimal = JavaMethod("()Ljava/math/BigDecimal;")
    getIdentityResult = JavaMethod("()Landroid/icu/number/NumberRangeFormatter$RangeIdentityResult;")
    getSecondBigDecimal = JavaMethod("()Ljava/math/BigDecimal;")
    nextPosition = JavaMethod("(Landroid/icu/text/ConstrainedFieldPosition;)Z")
    toCharacterIterator = JavaMethod("()Ljava/text/AttributedCharacterIterator;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    length = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    charAt = JavaMethod("(I)C")
    subSequence = JavaMethod("(II)Ljava/lang/CharSequence;")
    appendTo = JavaMethod("(Ljava/lang/Appendable;)Ljava/lang/Appendable;")

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

class Notation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/Notation"
    simple = JavaStaticMethod("()Landroid/icu/number/SimpleNotation;")
    compactShort = JavaStaticMethod("()Landroid/icu/number/CompactNotation;")
    engineering = JavaStaticMethod("()Landroid/icu/number/ScientificNotation;")
    scientific = JavaStaticMethod("()Landroid/icu/number/ScientificNotation;")
    compactLong = JavaStaticMethod("()Landroid/icu/number/CompactNotation;")

class LocalizedNumberFormatter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/LocalizedNumberFormatter"
    withoutLocale = JavaMethod("()Landroid/icu/number/UnlocalizedNumberFormatter;")
    format = JavaMultipleMethod([("(Ljava/lang/Number;)Landroid/icu/number/FormattedNumber;", False, False), ("(J)Landroid/icu/number/FormattedNumber;", False, False), ("(Landroid/icu/util/Measure;)Landroid/icu/number/FormattedNumber;", False, False), ("(D)Landroid/icu/number/FormattedNumber;", False, False)])
    toFormat = JavaMethod("()Ljava/text/Format;")

class LocalizedNumberRangeFormatter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/LocalizedNumberRangeFormatter"
    formatRange = JavaMultipleMethod([("(II)Landroid/icu/number/FormattedNumberRange;", False, False), ("(DD)Landroid/icu/number/FormattedNumberRange;", False, False), ("(Ljava/lang/Number;Ljava/lang/Number;)Landroid/icu/number/FormattedNumberRange;", False, False)])
    withoutLocale = JavaMethod("()Landroid/icu/number/UnlocalizedNumberRangeFormatter;")

class ScientificNotation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/ScientificNotation"
    withExponentSignDisplay = JavaMethod("(Landroid/icu/number/NumberFormatter$SignDisplay;)Landroid/icu/number/ScientificNotation;")
    withMinExponentDigits = JavaMethod("(I)Landroid/icu/number/ScientificNotation;")

class CompactNotation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/CompactNotation"

class NumberFormatterSettings(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/NumberFormatterSettings"
    usage = JavaMethod("(Ljava/lang/String;)Landroid/icu/number/NumberFormatterSettings;")
    displayOptions = JavaMethod("(Landroid/icu/text/DisplayOptions;)Landroid/icu/number/NumberFormatterSettings;")
    decimal = JavaMethod("(Landroid/icu/number/NumberFormatter$DecimalSeparatorDisplay;)Landroid/icu/number/NumberFormatterSettings;")
    grouping = JavaMethod("(Landroid/icu/number/NumberFormatter$GroupingStrategy;)Landroid/icu/number/NumberFormatterSettings;")
    integerWidth = JavaMethod("(Landroid/icu/number/IntegerWidth;)Landroid/icu/number/NumberFormatterSettings;")
    notation = JavaMethod("(Landroid/icu/number/Notation;)Landroid/icu/number/NumberFormatterSettings;")
    perUnit = JavaMethod("(Landroid/icu/util/MeasureUnit;)Landroid/icu/number/NumberFormatterSettings;")
    unitWidth = JavaMethod("(Landroid/icu/number/NumberFormatter$UnitWidth;)Landroid/icu/number/NumberFormatterSettings;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    scale = JavaMethod("(Landroid/icu/number/Scale;)Landroid/icu/number/NumberFormatterSettings;")
    precision = JavaMethod("(Landroid/icu/number/Precision;)Landroid/icu/number/NumberFormatterSettings;")
    sign = JavaMethod("(Landroid/icu/number/NumberFormatter$SignDisplay;)Landroid/icu/number/NumberFormatterSettings;")
    unit = JavaMethod("(Landroid/icu/util/MeasureUnit;)Landroid/icu/number/NumberFormatterSettings;")
    symbols = JavaMultipleMethod([("(Landroid/icu/text/NumberingSystem;)Landroid/icu/number/NumberFormatterSettings;", False, False), ("(Landroid/icu/text/DecimalFormatSymbols;)Landroid/icu/number/NumberFormatterSettings;", False, False)])
    roundingMode = JavaMethod("(Ljava/math/RoundingMode;)Landroid/icu/number/NumberFormatterSettings;")

class UnlocalizedNumberFormatter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/UnlocalizedNumberFormatter"
    locale = JavaMultipleMethod([("(Landroid/icu/util/ULocale;)Landroid/icu/number/LocalizedNumberFormatter;", False, False), ("(Ljava/util/Locale;)Landroid/icu/number/LocalizedNumberFormatter;", False, False)])

class SimpleNotation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/SimpleNotation"