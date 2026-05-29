from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MathContext"]

class MathContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/math/MathContext"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(ILjava/math/RoundingMode;)V", False), ("(I)V", False)]
    UNLIMITED = JavaStaticField("Ljava/math/MathContext;")
    DECIMAL32 = JavaStaticField("Ljava/math/MathContext;")
    DECIMAL64 = JavaStaticField("Ljava/math/MathContext;")
    DECIMAL128 = JavaStaticField("Ljava/math/MathContext;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getRoundingMode = JavaMethod("()Ljava/math/RoundingMode;")
    getPrecision = JavaMethod("()I")