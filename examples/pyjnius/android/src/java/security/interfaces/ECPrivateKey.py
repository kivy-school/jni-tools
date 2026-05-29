from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ECPrivateKey"]

class ECPrivateKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/ECPrivateKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getS = JavaMethod("()Ljava/math/BigInteger;")
    getParams = JavaMultipleMethod([("()Ljava/security/spec/ECParameterSpec;", False, False), ("()Ljava/security/spec/AlgorithmParameterSpec;", False, False)])