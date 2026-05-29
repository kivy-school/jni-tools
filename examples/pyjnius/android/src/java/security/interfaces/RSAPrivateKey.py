from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RSAPrivateKey"]

class RSAPrivateKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/RSAPrivateKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getParams = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")
    getPrivateExponent = JavaMethod("()Ljava/math/BigInteger;")