from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FormattedNumberRange"]

class FormattedNumberRange(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/FormattedNumberRange"
    getFirstBigDecimal = JavaMethod("()Ljava/math/BigDecimal;")
    getIdentityResult = JavaMethod("()Landroid/icu/number/NumberRangeFormatter$RangeIdentityResult;")
    getSecondBigDecimal = JavaMethod("()Ljava/math/BigDecimal;")
    appendTo = JavaMethod("(Ljava/lang/Appendable;)Ljava/lang/Appendable;")
    nextPosition = JavaMethod("(Landroid/icu/text/ConstrainedFieldPosition;)Z")
    toCharacterIterator = JavaMethod("()Ljava/text/AttributedCharacterIterator;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    length = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    charAt = JavaMethod("(I)C")
    subSequence = JavaMethod("(II)Ljava/lang/CharSequence;")