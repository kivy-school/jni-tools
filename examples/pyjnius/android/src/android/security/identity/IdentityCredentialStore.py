from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IdentityCredentialStore"]

class IdentityCredentialStore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/IdentityCredentialStore"
    CIPHERSUITE_ECDHE_HKDF_ECDSA_WITH_AES_256_GCM_SHA256 = JavaStaticField("I")
    createCredential = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Landroid/security/identity/WritableIdentityCredential;")
    getInstance = JavaStaticMethod("(Landroid/content/Context;)Landroid/security/identity/IdentityCredentialStore;")
    createPresentationSession = JavaMethod("(I)Landroid/security/identity/PresentationSession;")
    deleteCredentialByName = JavaMethod("(Ljava/lang/String;)[B")
    getCredentialByName = JavaMethod("(Ljava/lang/String;I)Landroid/security/identity/IdentityCredential;")
    getDirectAccessInstance = JavaStaticMethod("(Landroid/content/Context;)Landroid/security/identity/IdentityCredentialStore;")
    getSupportedDocTypes = JavaMethod("()[Ljava/lang/String;")