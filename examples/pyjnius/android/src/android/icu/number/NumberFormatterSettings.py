from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NumberFormatterSettings"]

class NumberFormatterSettings(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/NumberFormatterSettings"
    decimal = JavaMethod("(Landroid/icu/number/NumberFormatter$DecimalSeparatorDisplay;)Landroid/icu/number/NumberFormatterSettings;")
    displayOptions = JavaMethod("(Landroid/icu/text/DisplayOptions;)Landroid/icu/number/NumberFormatterSettings;")
    grouping = JavaMethod("(Landroid/icu/number/NumberFormatter$GroupingStrategy;)Landroid/icu/number/NumberFormatterSettings;")
    integerWidth = JavaMethod("(Landroid/icu/number/IntegerWidth;)Landroid/icu/number/NumberFormatterSettings;")
    notation = JavaMethod("(Landroid/icu/number/Notation;)Landroid/icu/number/NumberFormatterSettings;")
    perUnit = JavaMethod("(Landroid/icu/util/MeasureUnit;)Landroid/icu/number/NumberFormatterSettings;")
    unitWidth = JavaMethod("(Landroid/icu/number/NumberFormatter$UnitWidth;)Landroid/icu/number/NumberFormatterSettings;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    scale = JavaMethod("(Landroid/icu/number/Scale;)Landroid/icu/number/NumberFormatterSettings;")
    unit = JavaMethod("(Landroid/icu/util/MeasureUnit;)Landroid/icu/number/NumberFormatterSettings;")
    usage = JavaMethod("(Ljava/lang/String;)Landroid/icu/number/NumberFormatterSettings;")
    symbols = JavaMultipleMethod([("(Landroid/icu/text/NumberingSystem;)Landroid/icu/number/NumberFormatterSettings;", False, False), ("(Landroid/icu/text/DecimalFormatSymbols;)Landroid/icu/number/NumberFormatterSettings;", False, False)])
    roundingMode = JavaMethod("(Ljava/math/RoundingMode;)Landroid/icu/number/NumberFormatterSettings;")
    sign = JavaMethod("(Landroid/icu/number/NumberFormatter$SignDisplay;)Landroid/icu/number/NumberFormatterSettings;")
    precision = JavaMethod("(Landroid/icu/number/Precision;)Landroid/icu/number/NumberFormatterSettings;")