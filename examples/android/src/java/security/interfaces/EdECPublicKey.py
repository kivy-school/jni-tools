from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EdECPublicKey"]

class EdECPublicKey(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/EdECPublicKey"
    getPoint = JavaMethod("()Ljava/security/spec/EdECPoint;")