from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FormattedNumber"]

class FormattedNumber(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/FormattedNumber"
    toBigDecimal = JavaMethod("()Ljava/math/BigDecimal;")
    getOutputUnit = JavaMethod("()Landroid/icu/util/MeasureUnit;")
    getNounClass = JavaMethod("()Landroid/icu/text/DisplayOptions$NounClass;")
    appendTo = JavaMethod("(Ljava/lang/Appendable;)Ljava/lang/Appendable;")
    nextPosition = JavaMethod("(Landroid/icu/text/ConstrainedFieldPosition;)Z")
    toCharacterIterator = JavaMethod("()Ljava/text/AttributedCharacterIterator;")
    length = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    charAt = JavaMethod("(I)C")
    subSequence = JavaMethod("(II)Ljava/lang/CharSequence;")