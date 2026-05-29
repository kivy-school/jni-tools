from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertStore"]

class CertStore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertStore"
    __javaconstructor__ = [("(Ljava/security/cert/CertStoreSpi;Ljava/security/Provider;Ljava/lang/String;Ljava/security/cert/CertStoreParameters;)V", False)]
    getCertificates = JavaMethod("(Ljava/security/cert/CertSelector;)Ljava/util/Collection;")
    getCRLs = JavaMethod("(Ljava/security/cert/CRLSelector;)Ljava/util/Collection;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/security/cert/CertStoreParameters;)Ljava/security/cert/CertStore;", True, False), ("(Ljava/lang/String;Ljava/security/cert/CertStoreParameters;Ljava/lang/String;)Ljava/security/cert/CertStore;", True, False), ("(Ljava/lang/String;Ljava/security/cert/CertStoreParameters;Ljava/security/Provider;)Ljava/security/cert/CertStore;", True, False)])
    getCertStoreParameters = JavaMethod("()Ljava/security/cert/CertStoreParameters;")
    getType = JavaMethod("()Ljava/lang/String;")
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getDefaultType = JavaStaticMethod("()Ljava/lang/String;")