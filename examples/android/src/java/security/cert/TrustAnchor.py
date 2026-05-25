from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TrustAnchor"]

class TrustAnchor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/TrustAnchor"
    __javaconstructor__ = [("(Ljava/security/cert/X509Certificate;[B)V", False), ("(Ljavax/security/auth/x500/X500Principal;Ljava/security/PublicKey;[B)V", False), ("(Ljava/lang/String;Ljava/security/PublicKey;[B)V", False)]
    getTrustedCert = JavaMethod("()Ljava/security/cert/X509Certificate;")
    getCA = JavaMethod("()Ljavax/security/auth/x500/X500Principal;")
    getCAName = JavaMethod("()Ljava/lang/String;")
    getCAPublicKey = JavaMethod("()Ljava/security/PublicKey;")
    getNameConstraints = JavaMethod("()[B")
    toString = JavaMethod("()Ljava/lang/String;")