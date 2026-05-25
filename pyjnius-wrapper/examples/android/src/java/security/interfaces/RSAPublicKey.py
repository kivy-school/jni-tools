from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RSAPublicKey"]

class RSAPublicKey(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/RSAPublicKey"
    serialVersionUID = JavaStaticField("J")
    getPublicExponent = JavaMethod("()Ljava/math/BigInteger;")