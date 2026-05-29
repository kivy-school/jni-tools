from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DomainLoadStoreParameter"]

class DomainLoadStoreParameter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/DomainLoadStoreParameter"
    __javaconstructor__ = [("(Ljava/net/URI;Ljava/util/Map;)V", False)]
    getProtectionParameter = JavaMethod("()Ljava/security/KeyStore$ProtectionParameter;")
    getConfiguration = JavaMethod("()Ljava/net/URI;")
    getProtectionParams = JavaMethod("()Ljava/util/Map;")