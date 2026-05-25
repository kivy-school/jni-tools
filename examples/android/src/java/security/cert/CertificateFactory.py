from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertificateFactory"]

class CertificateFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertificateFactory"
    __javaconstructor__ = [("(Ljava/security/cert/CertificateFactorySpi;Ljava/security/Provider;Ljava/lang/String;)V", False)]
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/security/cert/CertificateFactory;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/cert/CertificateFactory;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/cert/CertificateFactory;", True, False)])
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getType = JavaMethod("()Ljava/lang/String;")
    generateCertificate = JavaMethod("(Ljava/io/InputStream;)Ljava/security/cert/Certificate;")
    getCertPathEncodings = JavaMethod("()Ljava/util/Iterator;")
    generateCertPath = JavaMultipleMethod([("(Ljava/io/InputStream;)Ljava/security/cert/CertPath;", False, False), ("(Ljava/io/InputStream;Ljava/lang/String;)Ljava/security/cert/CertPath;", False, False), ("(Ljava/util/List;)Ljava/security/cert/CertPath;", False, False)])
    generateCertificates = JavaMethod("(Ljava/io/InputStream;)Ljava/util/Collection;")
    generateCRL = JavaMethod("(Ljava/io/InputStream;)Ljava/security/cert/CRL;")
    generateCRLs = JavaMethod("(Ljava/io/InputStream;)Ljava/util/Collection;")