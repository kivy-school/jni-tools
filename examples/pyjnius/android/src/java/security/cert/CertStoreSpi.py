from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertStoreSpi"]

class CertStoreSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertStoreSpi"
    __javaconstructor__ = [("(Ljava/security/cert/CertStoreParameters;)V", False)]
    engineGetCertificates = JavaMethod("(Ljava/security/cert/CertSelector;)Ljava/util/Collection;")
    engineGetCRLs = JavaMethod("(Ljava/security/cert/CRLSelector;)Ljava/util/Collection;")