from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["X509Certificate"]

class X509Certificate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/X509Certificate"
    __javaconstructor__ = [("()V", False)]
    checkValidity = JavaMultipleMethod([("()V", False, False), ("(Ljava/util/Date;)V", False, False)])
    getVersion = JavaMethod("()I")
    getSerialNumber = JavaMethod("()Ljava/math/BigInteger;")
    getIssuerDN = JavaMethod("()Ljava/security/Principal;")
    getIssuerX500Principal = JavaMethod("()Ljavax/security/auth/x500/X500Principal;")
    getSubjectDN = JavaMethod("()Ljava/security/Principal;")
    getSubjectX500Principal = JavaMethod("()Ljavax/security/auth/x500/X500Principal;")
    getNotBefore = JavaMethod("()Ljava/util/Date;")
    getNotAfter = JavaMethod("()Ljava/util/Date;")
    getTBSCertificate = JavaMethod("()[B")
    getSignature = JavaMethod("()[B")
    getSigAlgName = JavaMethod("()Ljava/lang/String;")
    getSigAlgOID = JavaMethod("()Ljava/lang/String;")
    getSigAlgParams = JavaMethod("()[B")
    getIssuerUniqueID = JavaMethod("()[Z")
    getSubjectUniqueID = JavaMethod("()[Z")
    getKeyUsage = JavaMethod("()[Z")
    getExtendedKeyUsage = JavaMethod("()Ljava/util/List;")
    getBasicConstraints = JavaMethod("()I")
    getSubjectAlternativeNames = JavaMethod("()Ljava/util/Collection;")
    getIssuerAlternativeNames = JavaMethod("()Ljava/util/Collection;")
    verify = JavaMethod("(Ljava/security/PublicKey;Ljava/security/Provider;)V")