from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DHPublicKey"]

class DHPublicKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/interfaces/DHPublicKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getY = JavaMethod("()Ljava/math/BigInteger;")
    getParams = JavaMultipleMethod([("()Ljavax/crypto/spec/DHParameterSpec;", False, False), ("()Ljava/security/spec/AlgorithmParameterSpec;", False, False)])