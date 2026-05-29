from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertStore"]

class CertStore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertStore"
    getDefaultType = JavaStaticMethod("()Ljava/lang/String;")
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/security/cert/CertStoreParameters;Ljava/lang/String;)Ljava/security/cert/CertStore;", True, False), ("(Ljava/lang/String;Ljava/security/cert/CertStoreParameters;Ljava/security/Provider;)Ljava/security/cert/CertStore;", True, False), ("(Ljava/lang/String;Ljava/security/cert/CertStoreParameters;)Ljava/security/cert/CertStore;", True, False)])
    getCertificates = JavaMethod("(Ljava/security/cert/CertSelector;)Ljava/util/Collection;")
    getType = JavaMethod("()Ljava/lang/String;")
    getCRLs = JavaMethod("(Ljava/security/cert/CRLSelector;)Ljava/util/Collection;")
    getCertStoreParameters = JavaMethod("()Ljava/security/cert/CertStoreParameters;")