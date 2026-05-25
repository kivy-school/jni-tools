from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DSAPublicKeySpec"]

class DSAPublicKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/DSAPublicKeySpec"
    __javaconstructor__ = [("(Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;)V", False)]
    getY = JavaMethod("()Ljava/math/BigInteger;")
    getP = JavaMethod("()Ljava/math/BigInteger;")
    getQ = JavaMethod("()Ljava/math/BigInteger;")
    getG = JavaMethod("()Ljava/math/BigInteger;")