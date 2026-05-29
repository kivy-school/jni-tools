from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DHPrivateKey"]

class DHPrivateKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/interfaces/DHPrivateKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getX = JavaMethod("()Ljava/math/BigInteger;")
    getParams = JavaMultipleMethod([("()Ljavax/crypto/spec/DHParameterSpec;", False, False), ("()Ljava/security/spec/AlgorithmParameterSpec;", False, False)])