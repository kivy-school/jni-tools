from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DSAPublicKey"]

class DSAPublicKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/DSAPublicKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getY = JavaMethod("()Ljava/math/BigInteger;")
    getParams = JavaMultipleMethod([("()Ljava/security/interfaces/DSAParams;", False, False), ("()Ljava/security/spec/AlgorithmParameterSpec;", False, False)])