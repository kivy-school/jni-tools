from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RSAOtherPrimeInfo"]

class RSAOtherPrimeInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/RSAOtherPrimeInfo"
    __javaconstructor__ = [("(Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;)V", False)]
    getCrtCoefficient = JavaMethod("()Ljava/math/BigInteger;")
    getPrime = JavaMethod("()Ljava/math/BigInteger;")
    getExponent = JavaMethod("()Ljava/math/BigInteger;")