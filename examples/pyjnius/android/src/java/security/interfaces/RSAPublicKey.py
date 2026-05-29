from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RSAPublicKey"]

class RSAPublicKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/RSAPublicKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getParams = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")
    getPublicExponent = JavaMethod("()Ljava/math/BigInteger;")