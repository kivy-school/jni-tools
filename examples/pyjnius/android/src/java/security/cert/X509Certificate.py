from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["X509Certificate"]

class X509Certificate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/X509Certificate"
    getSignature = JavaMethod("()[B")
    getBasicConstraints = JavaMethod("()I")
    getIssuerX500Principal = JavaMethod("()Ljavax/security/auth/x500/X500Principal;")
    getSubjectX500Principal = JavaMethod("()Ljavax/security/auth/x500/X500Principal;")
    getExtendedKeyUsage = JavaMethod("()Ljava/util/List;")
    getSubjectAlternativeNames = JavaMethod("()Ljava/util/Collection;")
    getIssuerAlternativeNames = JavaMethod("()Ljava/util/Collection;")
    getSigAlgName = JavaMethod("()Ljava/lang/String;")
    getSigAlgParams = JavaMethod("()[B")
    getTBSCertificate = JavaMethod("()[B")
    checkValidity = JavaMultipleMethod([("()V", False, False), ("(Ljava/util/Date;)V", False, False)])
    getSerialNumber = JavaMethod("()Ljava/math/BigInteger;")
    getIssuerDN = JavaMethod("()Ljava/security/Principal;")
    getSubjectDN = JavaMethod("()Ljava/security/Principal;")
    getNotBefore = JavaMethod("()Ljava/util/Date;")
    getNotAfter = JavaMethod("()Ljava/util/Date;")
    getSigAlgOID = JavaMethod("()Ljava/lang/String;")
    getIssuerUniqueID = JavaMethod("()[Z")
    getSubjectUniqueID = JavaMethod("()[Z")
    getKeyUsage = JavaMethod("()[Z")
    getVersion = JavaMethod("()I")
    verify = JavaMethod("(Ljava/security/PublicKey;Ljava/security/Provider;)V")