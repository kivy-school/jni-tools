from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Rational"]

class Rational(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/Rational"
    __javaconstructor__ = [("(II)V", False)]
    NEGATIVE_INFINITY = JavaStaticField("Landroid/util/Rational;")
    NaN = JavaStaticField("Landroid/util/Rational;")
    POSITIVE_INFINITY = JavaStaticField("Landroid/util/Rational;")
    ZERO = JavaStaticField("Landroid/util/Rational;")
    getNumerator = JavaMethod("()I")
    getDenominator = JavaMethod("()I")
    isNaN = JavaMethod("()Z")
    isInfinite = JavaMethod("()Z")
    isFinite = JavaMethod("()Z")
    isZero = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    doubleValue = JavaMethod("()D")
    floatValue = JavaMethod("()F")
    intValue = JavaMethod("()I")
    longValue = JavaMethod("()J")
    shortValue = JavaMethod("()S")
    compareTo = JavaMethod("(Landroid/util/Rational;)I")
    parseRational = JavaStaticMethod("(Ljava/lang/String;)Landroid/util/Rational;")