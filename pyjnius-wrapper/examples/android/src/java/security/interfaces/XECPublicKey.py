from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XECPublicKey"]

class XECPublicKey(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/XECPublicKey"
    getU = JavaMethod("()Ljava/math/BigInteger;")