from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DSAPrivateKey"]

class DSAPrivateKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/DSAPrivateKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getX = JavaMethod("()Ljava/math/BigInteger;")
    getParams = JavaMultipleMethod([("()Ljava/security/interfaces/DSAParams;", False, False), ("()Ljava/security/spec/AlgorithmParameterSpec;", False, False)])