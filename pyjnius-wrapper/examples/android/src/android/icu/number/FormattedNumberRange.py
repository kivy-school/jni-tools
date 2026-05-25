from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FormattedNumberRange"]

class FormattedNumberRange(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/number/FormattedNumberRange"
    toString = JavaMethod("()Ljava/lang/String;")
    appendTo = JavaMethod("(Ljava/lang/Appendable;)Ljava/lang/Appendable;")
    charAt = JavaMethod("(I)C")
    length = JavaMethod("()I")
    subSequence = JavaMethod("(II)Ljava/lang/CharSequence;")
    nextPosition = JavaMethod("(Landroid/icu/text/ConstrainedFieldPosition;)Z")
    toCharacterIterator = JavaMethod("()Ljava/text/AttributedCharacterIterator;")
    getFirstBigDecimal = JavaMethod("()Ljava/math/BigDecimal;")
    getSecondBigDecimal = JavaMethod("()Ljava/math/BigDecimal;")
    getIdentityResult = JavaMethod("()Landroid/icu/number/NumberRangeFormatter$RangeIdentityResult;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")