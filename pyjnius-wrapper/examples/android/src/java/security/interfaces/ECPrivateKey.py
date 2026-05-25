from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ECPrivateKey"]

class ECPrivateKey(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/ECPrivateKey"
    serialVersionUID = JavaStaticField("J")
    getS = JavaMethod("()Ljava/math/BigInteger;")