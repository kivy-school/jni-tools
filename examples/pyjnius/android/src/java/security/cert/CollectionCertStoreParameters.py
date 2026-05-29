from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CollectionCertStoreParameters"]

class CollectionCertStoreParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CollectionCertStoreParameters"
    __javaconstructor__ = [("(Ljava/util/Collection;)V", False), ("()V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    clone = JavaMethod("()Ljava/lang/Object;")
    getCollection = JavaMethod("()Ljava/util/Collection;")