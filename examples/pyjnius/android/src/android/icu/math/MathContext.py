from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MathContext"]

class MathContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/math/MathContext"
    __javaconstructor__ = [("(IIZI)V", False), ("(I)V", False), ("(II)V", False), ("(IIZ)V", False)]
    DEFAULT = JavaStaticField("Landroid/icu/math/MathContext;")
    ENGINEERING = JavaStaticField("I")
    PLAIN = JavaStaticField("I")
    ROUND_CEILING = JavaStaticField("I")
    ROUND_DOWN = JavaStaticField("I")
    ROUND_FLOOR = JavaStaticField("I")
    ROUND_HALF_DOWN = JavaStaticField("I")
    ROUND_HALF_EVEN = JavaStaticField("I")
    ROUND_HALF_UP = JavaStaticField("I")
    ROUND_UNNECESSARY = JavaStaticField("I")
    ROUND_UP = JavaStaticField("I")
    SCIENTIFIC = JavaStaticField("I")
    getLostDigits = JavaMethod("()Z")
    getForm = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    getDigits = JavaMethod("()I")
    getRoundingMode = JavaMethod("()I")