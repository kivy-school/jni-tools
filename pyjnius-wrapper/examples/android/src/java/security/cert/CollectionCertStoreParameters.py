from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CollectionCertStoreParameters"]

class CollectionCertStoreParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CollectionCertStoreParameters"
    __javaconstructor__ = [("(Ljava/util/Collection;)V", False), ("()V", False)]
    getCollection = JavaMethod("()Ljava/util/Collection;")
    clone = JavaMethod("()Ljava/lang/Object;")
    toString = JavaMethod("()Ljava/lang/String;")