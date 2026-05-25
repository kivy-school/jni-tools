from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RSAOtherPrimeInfo"]

class RSAOtherPrimeInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/RSAOtherPrimeInfo"
    __javaconstructor__ = [("(Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;)V", False)]
    getPrime = JavaMethod("()Ljava/math/BigInteger;")
    getExponent = JavaMethod("()Ljava/math/BigInteger;")
    getCrtCoefficient = JavaMethod("()Ljava/math/BigInteger;")