from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EllipticCurve"]

class EllipticCurve(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/EllipticCurve"
    __javaconstructor__ = [("(Ljava/security/spec/ECField;Ljava/math/BigInteger;Ljava/math/BigInteger;)V", False), ("(Ljava/security/spec/ECField;Ljava/math/BigInteger;Ljava/math/BigInteger;[B)V", False)]
    getField = JavaMethod("()Ljava/security/spec/ECField;")
    getA = JavaMethod("()Ljava/math/BigInteger;")
    getB = JavaMethod("()Ljava/math/BigInteger;")
    getSeed = JavaMethod("()[B")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")