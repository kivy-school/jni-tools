from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["X500PrivateCredential"]

class X500PrivateCredential(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/x500/X500PrivateCredential"
    __javaconstructor__ = [("(Ljava/security/cert/X509Certificate;Ljava/security/PrivateKey;)V", False), ("(Ljava/security/cert/X509Certificate;Ljava/security/PrivateKey;Ljava/lang/String;)V", False)]
    getCertificate = JavaMethod("()Ljava/security/cert/X509Certificate;")
    getPrivateKey = JavaMethod("()Ljava/security/PrivateKey;")
    getAlias = JavaMethod("()Ljava/lang/String;")
    destroy = JavaMethod("()V")
    isDestroyed = JavaMethod("()Z")