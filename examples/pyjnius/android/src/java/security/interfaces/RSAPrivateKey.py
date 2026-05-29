from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RSAPrivateKey"]

class RSAPrivateKey(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/RSAPrivateKey"
    serialVersionUID = JavaStaticField("J")
    getPrivateExponent = JavaMethod("()Ljava/math/BigInteger;")