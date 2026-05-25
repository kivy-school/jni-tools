from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DSAPrivateKey"]

class DSAPrivateKey(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/DSAPrivateKey"
    serialVersionUID = JavaStaticField("J")
    getX = JavaMethod("()Ljava/math/BigInteger;")