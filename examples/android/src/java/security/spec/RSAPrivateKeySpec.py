from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RSAPrivateKeySpec"]

class RSAPrivateKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/RSAPrivateKeySpec"
    __javaconstructor__ = [("(Ljava/math/BigInteger;Ljava/math/BigInteger;)V", False), ("(Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/security/spec/AlgorithmParameterSpec;)V", False)]
    getModulus = JavaMethod("()Ljava/math/BigInteger;")
    getPrivateExponent = JavaMethod("()Ljava/math/BigInteger;")
    getParams = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")