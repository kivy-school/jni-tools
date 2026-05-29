from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertificateFactorySpi"]

class CertificateFactorySpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertificateFactorySpi"
    __javaconstructor__ = [("()V", False)]
    engineGenerateCertificate = JavaMethod("(Ljava/io/InputStream;)Ljava/security/cert/Certificate;")
    engineGetCertPathEncodings = JavaMethod("()Ljava/util/Iterator;")
    engineGenerateCertPath = JavaMultipleMethod([("(Ljava/util/List;)Ljava/security/cert/CertPath;", False, False), ("(Ljava/io/InputStream;Ljava/lang/String;)Ljava/security/cert/CertPath;", False, False), ("(Ljava/io/InputStream;)Ljava/security/cert/CertPath;", False, False)])
    engineGenerateCertificates = JavaMethod("(Ljava/io/InputStream;)Ljava/util/Collection;")
    engineGenerateCRL = JavaMethod("(Ljava/io/InputStream;)Ljava/security/cert/CRL;")
    engineGenerateCRLs = JavaMethod("(Ljava/io/InputStream;)Ljava/util/Collection;")