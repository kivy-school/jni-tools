from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ECPublicKey"]

class ECPublicKey(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/ECPublicKey"
    serialVersionUID = JavaStaticField("J")
    getW = JavaMethod("()Ljava/security/spec/ECPoint;")