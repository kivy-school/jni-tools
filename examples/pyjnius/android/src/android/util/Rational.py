from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Rational"]

class Rational(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/Rational"
    __javaconstructor__ = [("(II)V", False)]
    NEGATIVE_INFINITY = JavaStaticField("Landroid/util/Rational;")
    NaN = JavaStaticField("Landroid/util/Rational;")
    POSITIVE_INFINITY = JavaStaticField("Landroid/util/Rational;")
    ZERO = JavaStaticField("Landroid/util/Rational;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    isInfinite = JavaMethod("()Z")
    isFinite = JavaMethod("()Z")
    compareTo = JavaMultipleMethod([("(Landroid/util/Rational;)I", False, False), ("(Ljava/lang/Object;)I", False, False)])
    shortValue = JavaMethod("()S")
    intValue = JavaMethod("()I")
    longValue = JavaMethod("()J")
    floatValue = JavaMethod("()F")
    doubleValue = JavaMethod("()D")
    isNaN = JavaMethod("()Z")
    getDenominator = JavaMethod("()I")
    getNumerator = JavaMethod("()I")
    parseRational = JavaStaticMethod("(Ljava/lang/String;)Landroid/util/Rational;")
    isZero = JavaMethod("()Z")