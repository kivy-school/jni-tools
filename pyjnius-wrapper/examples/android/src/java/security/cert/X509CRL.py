from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["X509CRL"]

class X509CRL(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/X509CRL"
    __javaconstructor__ = [("()V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getEncoded = JavaMethod("()[B")
    verify = JavaMultipleMethod([("(Ljava/security/PublicKey;)V", False, False), ("(Ljava/security/PublicKey;Ljava/lang/String;)V", False, False), ("(Ljava/security/PublicKey;Ljava/security/Provider;)V", False, False)])
    getVersion = JavaMethod("()I")
    getIssuerDN = JavaMethod("()Ljava/security/Principal;")
    getIssuerX500Principal = JavaMethod("()Ljavax/security/auth/x500/X500Principal;")
    getThisUpdate = JavaMethod("()Ljava/util/Date;")
    getNextUpdate = JavaMethod("()Ljava/util/Date;")
    getRevokedCertificate = JavaMultipleMethod([("(Ljava/math/BigInteger;)Ljava/security/cert/X509CRLEntry;", False, False), ("(Ljava/security/cert/X509Certificate;)Ljava/security/cert/X509CRLEntry;", False, False)])
    getRevokedCertificates = JavaMethod("()Ljava/util/Set;")
    getTBSCertList = JavaMethod("()[B")
    getSignature = JavaMethod("()[B")
    getSigAlgName = JavaMethod("()Ljava/lang/String;")
    getSigAlgOID = JavaMethod("()Ljava/lang/String;")
    getSigAlgParams = JavaMethod("()[B")