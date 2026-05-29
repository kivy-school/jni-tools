from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IdentityCredential"]

class IdentityCredential(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/IdentityCredential"
    update = JavaMethod("(Landroid/security/identity/PersonalizationData;)[B")
    delete = JavaMethod("([B)[B")
    getEntries = JavaMethod("([BLjava/util/Map;[B[B)Landroid/security/identity/ResultData;")
    createEphemeralKeyPair = JavaMethod("()Ljava/security/KeyPair;")
    decryptMessageFromReader = JavaMethod("([B)[B")
    encryptMessageToReader = JavaMethod("([B)[B")
    getAuthKeysNeedingCertification = JavaMethod("()Ljava/util/Collection;")
    getAuthenticationDataUsageCount = JavaMethod("()[I")
    getAuthenticationKeyMetadata = JavaMethod("()Ljava/util/List;")
    getCredentialKeyCertificateChain = JavaMethod("()Ljava/util/Collection;")
    proveOwnership = JavaMethod("([B)[B")
    setAllowUsingExhaustedKeys = JavaMethod("(Z)V")
    setAllowUsingExpiredKeys = JavaMethod("(Z)V")
    setAvailableAuthenticationKeys = JavaMultipleMethod([("(IIJ)V", False, False), ("(II)V", False, False)])
    setReaderEphemeralPublicKey = JavaMethod("(Ljava/security/PublicKey;)V")
    storeStaticAuthenticationData = JavaMultipleMethod([("(Ljava/security/cert/X509Certificate;Ljava/time/Instant;[B)V", False, False), ("(Ljava/security/cert/X509Certificate;[B)V", False, False)])