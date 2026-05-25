from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EdECPrivateKey"]

class EdECPrivateKey(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/EdECPrivateKey"
    getBytes = JavaMethod("()Ljava/util/Optional;")