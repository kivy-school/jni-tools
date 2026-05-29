from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CredentialDataRequest"]

class CredentialDataRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/CredentialDataRequest"
    getReaderSignature = JavaMethod("()[B")
    getRequestMessage = JavaMethod("()[B")
    getDeviceSignedEntriesToRequest = JavaMethod("()Ljava/util/Map;")
    getIssuerSignedEntriesToRequest = JavaMethod("()Ljava/util/Map;")
    isAllowUsingExhaustedKeys = JavaMethod("()Z")
    isAllowUsingExpiredKeys = JavaMethod("()Z")
    isIncrementUseCount = JavaMethod("()Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/security/identity/CredentialDataRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        setRequestMessage = JavaMethod("([B)Landroid/security/identity/CredentialDataRequest$Builder;")
        setReaderSignature = JavaMethod("([B)Landroid/security/identity/CredentialDataRequest$Builder;")
        setDeviceSignedEntriesToRequest = JavaMethod("(Ljava/util/Map;)Landroid/security/identity/CredentialDataRequest$Builder;")
        setIncrementUseCount = JavaMethod("(Z)Landroid/security/identity/CredentialDataRequest$Builder;")
        setIssuerSignedEntriesToRequest = JavaMethod("(Ljava/util/Map;)Landroid/security/identity/CredentialDataRequest$Builder;")
        build = JavaMethod("()Landroid/security/identity/CredentialDataRequest;")
        setAllowUsingExhaustedKeys = JavaMethod("(Z)Landroid/security/identity/CredentialDataRequest$Builder;")
        setAllowUsingExpiredKeys = JavaMethod("(Z)Landroid/security/identity/CredentialDataRequest$Builder;")