from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WritableIdentityCredential"]

class WritableIdentityCredential(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/WritableIdentityCredential"
    getCredentialKeyCertificateChain = JavaMethod("([B)Ljava/util/Collection;")
    personalize = JavaMethod("(Landroid/security/identity/PersonalizationData;)[B")