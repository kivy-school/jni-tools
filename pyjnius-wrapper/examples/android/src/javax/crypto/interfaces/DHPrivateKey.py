from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DHPrivateKey"]

class DHPrivateKey(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/interfaces/DHPrivateKey"
    serialVersionUID = JavaStaticField("J")
    getX = JavaMethod("()Ljava/math/BigInteger;")