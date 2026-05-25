from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MathContext"]

class MathContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/math/MathContext"
    __javaconstructor__ = [("(I)V", False), ("(ILjava/math/RoundingMode;)V", False), ("(Ljava/lang/String;)V", False)]
    DECIMAL128 = JavaStaticField("Ljava/math/MathContext;")
    DECIMAL32 = JavaStaticField("Ljava/math/MathContext;")
    DECIMAL64 = JavaStaticField("Ljava/math/MathContext;")
    UNLIMITED = JavaStaticField("Ljava/math/MathContext;")
    getPrecision = JavaMethod("()I")
    getRoundingMode = JavaMethod("()Ljava/math/RoundingMode;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")