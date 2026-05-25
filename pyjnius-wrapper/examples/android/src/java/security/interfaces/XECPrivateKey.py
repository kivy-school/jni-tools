from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XECPrivateKey"]

class XECPrivateKey(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/XECPrivateKey"
    getScalar = JavaMethod("()Ljava/util/Optional;")