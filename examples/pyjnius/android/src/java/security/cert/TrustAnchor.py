from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TrustAnchor"]

class TrustAnchor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/TrustAnchor"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/security/PublicKey;[B)V", False), ("(Ljavax/security/auth/x500/X500Principal;Ljava/security/PublicKey;[B)V", False), ("(Ljava/security/cert/X509Certificate;[B)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    getTrustedCert = JavaMethod("()Ljava/security/cert/X509Certificate;")
    getCA = JavaMethod("()Ljavax/security/auth/x500/X500Principal;")
    getCAName = JavaMethod("()Ljava/lang/String;")
    getCAPublicKey = JavaMethod("()Ljava/security/PublicKey;")
    getNameConstraints = JavaMethod("()[B")