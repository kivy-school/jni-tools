from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertificateFactory"]

class CertificateFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertificateFactory"
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/cert/CertificateFactory;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/cert/CertificateFactory;", True, False), ("(Ljava/lang/String;)Ljava/security/cert/CertificateFactory;", True, False)])
    getType = JavaMethod("()Ljava/lang/String;")
    generateCertificate = JavaMethod("(Ljava/io/InputStream;)Ljava/security/cert/Certificate;")
    generateCertPath = JavaMultipleMethod([("(Ljava/io/InputStream;Ljava/lang/String;)Ljava/security/cert/CertPath;", False, False), ("(Ljava/io/InputStream;)Ljava/security/cert/CertPath;", False, False), ("(Ljava/util/List;)Ljava/security/cert/CertPath;", False, False)])
    getCertPathEncodings = JavaMethod("()Ljava/util/Iterator;")
    generateCertificates = JavaMethod("(Ljava/io/InputStream;)Ljava/util/Collection;")
    generateCRL = JavaMethod("(Ljava/io/InputStream;)Ljava/security/cert/CRL;")
    generateCRLs = JavaMethod("(Ljava/io/InputStream;)Ljava/util/Collection;")