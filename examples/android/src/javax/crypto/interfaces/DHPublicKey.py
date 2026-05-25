from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DHPublicKey"]

class DHPublicKey(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/interfaces/DHPublicKey"
    serialVersionUID = JavaStaticField("J")
    getY = JavaMethod("()Ljava/math/BigInteger;")