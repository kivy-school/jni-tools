from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PresentationSession"]

class PresentationSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/PresentationSession"
    getEphemeralKeyPair = JavaMethod("()Ljava/security/KeyPair;")
    setReaderEphemeralPublicKey = JavaMethod("(Ljava/security/PublicKey;)V")
    setSessionTranscript = JavaMethod("([B)V")
    getCredentialData = JavaMethod("(Ljava/lang/String;Landroid/security/identity/CredentialDataRequest;)Landroid/security/identity/CredentialDataResult;")