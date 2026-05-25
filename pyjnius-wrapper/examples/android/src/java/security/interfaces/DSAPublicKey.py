from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DSAPublicKey"]

class DSAPublicKey(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/DSAPublicKey"
    serialVersionUID = JavaStaticField("J")
    getY = JavaMethod("()Ljava/math/BigInteger;")