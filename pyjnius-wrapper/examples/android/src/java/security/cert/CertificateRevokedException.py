from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertificateRevokedException"]

class CertificateRevokedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertificateRevokedException"
    __javaconstructor__ = [("(Ljava/util/Date;Ljava/security/cert/CRLReason;Ljavax/security/auth/x500/X500Principal;Ljava/util/Map;)V", False)]
    getRevocationDate = JavaMethod("()Ljava/util/Date;")
    getRevocationReason = JavaMethod("()Ljava/security/cert/CRLReason;")
    getAuthorityName = JavaMethod("()Ljavax/security/auth/x500/X500Principal;")
    getInvalidityDate = JavaMethod("()Ljava/util/Date;")
    getExtensions = JavaMethod("()Ljava/util/Map;")
    getMessage = JavaMethod("()Ljava/lang/String;")