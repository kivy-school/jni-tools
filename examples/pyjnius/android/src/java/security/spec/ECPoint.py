from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ECPoint"]

class ECPoint(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/ECPoint"
    __javaconstructor__ = [("(Ljava/math/BigInteger;Ljava/math/BigInteger;)V", False)]
    POINT_INFINITY = JavaStaticField("Ljava/security/spec/ECPoint;")
    getAffineX = JavaMethod("()Ljava/math/BigInteger;")
    getAffineY = JavaMethod("()Ljava/math/BigInteger;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")