from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IdentityCredential"]

class IdentityCredential(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/IdentityCredential"
    createEphemeralKeyPair = JavaMethod("()Ljava/security/KeyPair;")
    setReaderEphemeralPublicKey = JavaMethod("(Ljava/security/PublicKey;)V")
    encryptMessageToReader = JavaMethod("([B)[B")
    decryptMessageFromReader = JavaMethod("([B)[B")
    getCredentialKeyCertificateChain = JavaMethod("()Ljava/util/Collection;")
    setAllowUsingExhaustedKeys = JavaMethod("(Z)V")
    setAllowUsingExpiredKeys = JavaMethod("(Z)V")
    getEntries = JavaMethod("([BLjava/util/Map;[B[B)Landroid/security/identity/ResultData;")
    setAvailableAuthenticationKeys = JavaMultipleMethod([("(II)V", False, False), ("(IIJ)V", False, False)])
    getAuthKeysNeedingCertification = JavaMethod("()Ljava/util/Collection;")
    storeStaticAuthenticationData = JavaMultipleMethod([("(Ljava/security/cert/X509Certificate;[B)V", False, False), ("(Ljava/security/cert/X509Certificate;Ljava/time/Instant;[B)V", False, False)])
    getAuthenticationDataUsageCount = JavaMethod("()[I")
    proveOwnership = JavaMethod("([B)[B")
    delete = JavaMethod("([B)[B")
    update = JavaMethod("(Landroid/security/identity/PersonalizationData;)[B")
    getAuthenticationKeyMetadata = JavaMethod("()Ljava/util/List;")