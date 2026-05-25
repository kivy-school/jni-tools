from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RSAPrivateCrtKey"]

class RSAPrivateCrtKey(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/RSAPrivateCrtKey"
    serialVersionUID = JavaStaticField("J")
    getPublicExponent = JavaMethod("()Ljava/math/BigInteger;")
    getPrimeP = JavaMethod("()Ljava/math/BigInteger;")
    getPrimeQ = JavaMethod("()Ljava/math/BigInteger;")
    getPrimeExponentP = JavaMethod("()Ljava/math/BigInteger;")
    getPrimeExponentQ = JavaMethod("()Ljava/math/BigInteger;")
    getCrtCoefficient = JavaMethod("()Ljava/math/BigInteger;")