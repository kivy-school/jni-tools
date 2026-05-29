from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EllipticCurve"]

class EllipticCurve(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/EllipticCurve"
    __javaconstructor__ = [("(Ljava/security/spec/ECField;Ljava/math/BigInteger;Ljava/math/BigInteger;)V", False), ("(Ljava/security/spec/ECField;Ljava/math/BigInteger;Ljava/math/BigInteger;[B)V", False)]
    getA = JavaMethod("()Ljava/math/BigInteger;")
    getB = JavaMethod("()Ljava/math/BigInteger;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getField = JavaMethod("()Ljava/security/spec/ECField;")
    getSeed = JavaMethod("()[B")