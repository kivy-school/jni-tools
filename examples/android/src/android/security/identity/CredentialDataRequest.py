from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CredentialDataRequest"]

class CredentialDataRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/CredentialDataRequest"
    getDeviceSignedEntriesToRequest = JavaMethod("()Ljava/util/Map;")
    getIssuerSignedEntriesToRequest = JavaMethod("()Ljava/util/Map;")
    isAllowUsingExhaustedKeys = JavaMethod("()Z")
    isAllowUsingExpiredKeys = JavaMethod("()Z")
    isIncrementUseCount = JavaMethod("()Z")
    getRequestMessage = JavaMethod("()[B")
    getReaderSignature = JavaMethod("()[B")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/security/identity/CredentialDataRequest/Builder"
        __javaconstructor__ = [("()V", False)]
        setDeviceSignedEntriesToRequest = JavaMethod("(Ljava/util/Map;)Landroid/security/identity/CredentialDataRequest$Builder;")
        setIssuerSignedEntriesToRequest = JavaMethod("(Ljava/util/Map;)Landroid/security/identity/CredentialDataRequest$Builder;")
        setAllowUsingExhaustedKeys = JavaMethod("(Z)Landroid/security/identity/CredentialDataRequest$Builder;")
        setAllowUsingExpiredKeys = JavaMethod("(Z)Landroid/security/identity/CredentialDataRequest$Builder;")
        setIncrementUseCount = JavaMethod("(Z)Landroid/security/identity/CredentialDataRequest$Builder;")
        setRequestMessage = JavaMethod("([B)Landroid/security/identity/CredentialDataRequest$Builder;")
        setReaderSignature = JavaMethod("([B)Landroid/security/identity/CredentialDataRequest$Builder;")
        build = JavaMethod("()Landroid/security/identity/CredentialDataRequest;")