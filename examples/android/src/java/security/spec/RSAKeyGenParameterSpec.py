from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RSAKeyGenParameterSpec"]

class RSAKeyGenParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/RSAKeyGenParameterSpec"
    __javaconstructor__ = [("(ILjava/math/BigInteger;)V", False), ("(ILjava/math/BigInteger;Ljava/security/spec/AlgorithmParameterSpec;)V", False)]
    F0 = JavaStaticField("Ljava/math/BigInteger;")
    F4 = JavaStaticField("Ljava/math/BigInteger;")
    getKeysize = JavaMethod("()I")
    getPublicExponent = JavaMethod("()Ljava/math/BigInteger;")
    getKeyParams = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")