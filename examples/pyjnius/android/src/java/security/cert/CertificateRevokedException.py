from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertificateRevokedException"]

class CertificateRevokedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertificateRevokedException"
    __javaconstructor__ = [("(Ljava/util/Date;Ljava/security/cert/CRLReason;Ljavax/security/auth/x500/X500Principal;Ljava/util/Map;)V", False)]
    getMessage = JavaMethod("()Ljava/lang/String;")
    getRevocationReason = JavaMethod("()Ljava/security/cert/CRLReason;")
    getRevocationDate = JavaMethod("()Ljava/util/Date;")
    getExtensions = JavaMethod("()Ljava/util/Map;")
    getAuthorityName = JavaMethod("()Ljavax/security/auth/x500/X500Principal;")
    getInvalidityDate = JavaMethod("()Ljava/util/Date;")