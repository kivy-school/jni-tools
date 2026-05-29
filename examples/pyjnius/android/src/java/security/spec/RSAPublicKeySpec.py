from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RSAPublicKeySpec"]

class RSAPublicKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/RSAPublicKeySpec"
    __javaconstructor__ = [("(Ljava/math/BigInteger;Ljava/math/BigInteger;)V", False), ("(Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/security/spec/AlgorithmParameterSpec;)V", False)]
    getParams = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")
    getPublicExponent = JavaMethod("()Ljava/math/BigInteger;")
    getModulus = JavaMethod("()Ljava/math/BigInteger;")