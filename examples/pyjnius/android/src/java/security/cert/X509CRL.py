from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["X509CRL"]

class X509CRL(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/X509CRL"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getSignature = JavaMethod("()[B")
    getEncoded = JavaMethod("()[B")
    getIssuerX500Principal = JavaMethod("()Ljavax/security/auth/x500/X500Principal;")
    getSigAlgName = JavaMethod("()Ljava/lang/String;")
    getSigAlgParams = JavaMethod("()[B")
    getIssuerDN = JavaMethod("()Ljava/security/Principal;")
    getSigAlgOID = JavaMethod("()Ljava/lang/String;")
    getVersion = JavaMethod("()I")
    getThisUpdate = JavaMethod("()Ljava/util/Date;")
    getNextUpdate = JavaMethod("()Ljava/util/Date;")
    getTBSCertList = JavaMethod("()[B")
    getRevokedCertificate = JavaMultipleMethod([("(Ljava/math/BigInteger;)Ljava/security/cert/X509CRLEntry;", False, False), ("(Ljava/security/cert/X509Certificate;)Ljava/security/cert/X509CRLEntry;", False, False)])
    getRevokedCertificates = JavaMethod("()Ljava/util/Set;")
    verify = JavaMultipleMethod([("(Ljava/security/PublicKey;)V", False, False), ("(Ljava/security/PublicKey;Ljava/security/Provider;)V", False, False), ("(Ljava/security/PublicKey;Ljava/lang/String;)V", False, False)])