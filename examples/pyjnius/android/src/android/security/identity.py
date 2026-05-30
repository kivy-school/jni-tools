from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class CredentialDataResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/CredentialDataResult"
    getDeviceMac = JavaMethod("()[B")
    getDeviceNameSpaces = JavaMethod("()[B")
    getStaticAuthenticationData = JavaMethod("()[B")
    getDeviceSignature = JavaMethod("()[B")
    getDeviceSignedEntries = JavaMethod("()Landroid/security/identity/CredentialDataResult$Entries;")
    getIssuerSignedEntries = JavaMethod("()Landroid/security/identity/CredentialDataResult$Entries;")

    class Entries(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/security/identity/CredentialDataResult$Entries"
        STATUS_NOT_IN_REQUEST_MESSAGE = JavaStaticField("I")
        STATUS_NOT_REQUESTED = JavaStaticField("I")
        STATUS_NO_ACCESS_CONTROL_PROFILES = JavaStaticField("I")
        STATUS_NO_SUCH_ENTRY = JavaStaticField("I")
        STATUS_OK = JavaStaticField("I")
        STATUS_READER_AUTHENTICATION_FAILED = JavaStaticField("I")
        STATUS_USER_AUTHENTICATION_FAILED = JavaStaticField("I")
        getStatus = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)I")
        getNamespaces = JavaMethod("()Ljava/util/Collection;")
        getRetrievedEntryNames = JavaMethod("(Ljava/lang/String;)Ljava/util/Collection;")
        getEntryNames = JavaMethod("(Ljava/lang/String;)Ljava/util/Collection;")
        getEntry = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)[B")

class MessageDecryptionException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/MessageDecryptionException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]

class IdentityCredentialStore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/IdentityCredentialStore"
    CIPHERSUITE_ECDHE_HKDF_ECDSA_WITH_AES_256_GCM_SHA256 = JavaStaticField("I")
    createCredential = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Landroid/security/identity/WritableIdentityCredential;")
    getCredentialByName = JavaMethod("(Ljava/lang/String;I)Landroid/security/identity/IdentityCredential;")
    createPresentationSession = JavaMethod("(I)Landroid/security/identity/PresentationSession;")
    getDirectAccessInstance = JavaStaticMethod("(Landroid/content/Context;)Landroid/security/identity/IdentityCredentialStore;")
    getSupportedDocTypes = JavaMethod("()[Ljava/lang/String;")
    deleteCredentialByName = JavaMethod("(Ljava/lang/String;)[B")
    getInstance = JavaStaticMethod("(Landroid/content/Context;)Landroid/security/identity/IdentityCredentialStore;")

class SessionTranscriptMismatchException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/SessionTranscriptMismatchException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]

class PresentationSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/PresentationSession"
    getCredentialData = JavaMethod("(Ljava/lang/String;Landroid/security/identity/CredentialDataRequest;)Landroid/security/identity/CredentialDataResult;")
    setReaderEphemeralPublicKey = JavaMethod("(Ljava/security/PublicKey;)V")
    getEphemeralKeyPair = JavaMethod("()Ljava/security/KeyPair;")
    setSessionTranscript = JavaMethod("([B)V")

class AccessControlProfile(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/AccessControlProfile"

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/security/identity/AccessControlProfile$Builder"
        __javaconstructor__ = [("(Landroid/security/identity/AccessControlProfileId;)V", False)]
        setReaderCertificate = JavaMethod("(Ljava/security/cert/X509Certificate;)Landroid/security/identity/AccessControlProfile$Builder;")
        setUserAuthenticationTimeout = JavaMethod("(J)Landroid/security/identity/AccessControlProfile$Builder;")
        setUserAuthenticationRequired = JavaMethod("(Z)Landroid/security/identity/AccessControlProfile$Builder;")
        build = JavaMethod("()Landroid/security/identity/AccessControlProfile;")

class AuthenticationKeyMetadata(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/AuthenticationKeyMetadata"
    getExpirationDate = JavaMethod("()Ljava/time/Instant;")
    getUsageCount = JavaMethod("()I")

class AccessControlProfileId(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/AccessControlProfileId"
    __javaconstructor__ = [("(I)V", False)]
    getId = JavaMethod("()I")

class CipherSuiteNotSupportedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/CipherSuiteNotSupportedException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]

class CredentialDataRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/CredentialDataRequest"
    getReaderSignature = JavaMethod("()[B")
    isAllowUsingExhaustedKeys = JavaMethod("()Z")
    getDeviceSignedEntriesToRequest = JavaMethod("()Ljava/util/Map;")
    getIssuerSignedEntriesToRequest = JavaMethod("()Ljava/util/Map;")
    getRequestMessage = JavaMethod("()[B")
    isAllowUsingExpiredKeys = JavaMethod("()Z")
    isIncrementUseCount = JavaMethod("()Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/security/identity/CredentialDataRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        setAllowUsingExhaustedKeys = JavaMethod("(Z)Landroid/security/identity/CredentialDataRequest$Builder;")
        setAllowUsingExpiredKeys = JavaMethod("(Z)Landroid/security/identity/CredentialDataRequest$Builder;")
        setDeviceSignedEntriesToRequest = JavaMethod("(Ljava/util/Map;)Landroid/security/identity/CredentialDataRequest$Builder;")
        setIncrementUseCount = JavaMethod("(Z)Landroid/security/identity/CredentialDataRequest$Builder;")
        setIssuerSignedEntriesToRequest = JavaMethod("(Ljava/util/Map;)Landroid/security/identity/CredentialDataRequest$Builder;")
        setReaderSignature = JavaMethod("([B)Landroid/security/identity/CredentialDataRequest$Builder;")
        setRequestMessage = JavaMethod("([B)Landroid/security/identity/CredentialDataRequest$Builder;")
        build = JavaMethod("()Landroid/security/identity/CredentialDataRequest;")

class UnknownAuthenticationKeyException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/UnknownAuthenticationKeyException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]

class InvalidRequestMessageException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/InvalidRequestMessageException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]

class IdentityCredentialException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/IdentityCredentialException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]

class InvalidReaderSignatureException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/InvalidReaderSignatureException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]

class ResultData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/ResultData"
    STATUS_NOT_IN_REQUEST_MESSAGE = JavaStaticField("I")
    STATUS_NOT_REQUESTED = JavaStaticField("I")
    STATUS_NO_ACCESS_CONTROL_PROFILES = JavaStaticField("I")
    STATUS_NO_SUCH_ENTRY = JavaStaticField("I")
    STATUS_OK = JavaStaticField("I")
    STATUS_READER_AUTHENTICATION_FAILED = JavaStaticField("I")
    STATUS_USER_AUTHENTICATION_FAILED = JavaStaticField("I")
    getStatus = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)I")
    getNamespaces = JavaMethod("()Ljava/util/Collection;")
    getStaticAuthenticationData = JavaMethod("()[B")
    getRetrievedEntryNames = JavaMethod("(Ljava/lang/String;)Ljava/util/Collection;")
    getEntryNames = JavaMethod("(Ljava/lang/String;)Ljava/util/Collection;")
    getAuthenticatedData = JavaMethod("()[B")
    getMessageAuthenticationCode = JavaMethod("()[B")
    getEntry = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)[B")

class NoAuthenticationKeyAvailableException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/NoAuthenticationKeyAvailableException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]

class WritableIdentityCredential(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/WritableIdentityCredential"
    getCredentialKeyCertificateChain = JavaMethod("([B)Ljava/util/Collection;")
    personalize = JavaMethod("(Landroid/security/identity/PersonalizationData;)[B")

class DocTypeNotSupportedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/DocTypeNotSupportedException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]

class IdentityCredential(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/IdentityCredential"
    encryptMessageToReader = JavaMethod("([B)[B")
    createEphemeralKeyPair = JavaMethod("()Ljava/security/KeyPair;")
    decryptMessageFromReader = JavaMethod("([B)[B")
    getAuthKeysNeedingCertification = JavaMethod("()Ljava/util/Collection;")
    getAuthenticationDataUsageCount = JavaMethod("()[I")
    getAuthenticationKeyMetadata = JavaMethod("()Ljava/util/List;")
    getCredentialKeyCertificateChain = JavaMethod("()Ljava/util/Collection;")
    proveOwnership = JavaMethod("([B)[B")
    setAllowUsingExhaustedKeys = JavaMethod("(Z)V")
    setAllowUsingExpiredKeys = JavaMethod("(Z)V")
    setAvailableAuthenticationKeys = JavaMultipleMethod([("(II)V", False, False), ("(IIJ)V", False, False)])
    setReaderEphemeralPublicKey = JavaMethod("(Ljava/security/PublicKey;)V")
    storeStaticAuthenticationData = JavaMultipleMethod([("(Ljava/security/cert/X509Certificate;Ljava/time/Instant;[B)V", False, False), ("(Ljava/security/cert/X509Certificate;[B)V", False, False)])
    update = JavaMethod("(Landroid/security/identity/PersonalizationData;)[B")
    delete = JavaMethod("([B)[B")
    getEntries = JavaMethod("([BLjava/util/Map;[B[B)Landroid/security/identity/ResultData;")

class EphemeralPublicKeyNotFoundException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/EphemeralPublicKeyNotFoundException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]

class PersonalizationData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/PersonalizationData"

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/security/identity/PersonalizationData$Builder"
        __javaconstructor__ = [("()V", False)]
        putEntry = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/util/Collection;[B)Landroid/security/identity/PersonalizationData$Builder;")
        addAccessControlProfile = JavaMethod("(Landroid/security/identity/AccessControlProfile;)Landroid/security/identity/PersonalizationData$Builder;")
        build = JavaMethod("()Landroid/security/identity/PersonalizationData;")

class AlreadyPersonalizedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/AlreadyPersonalizedException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]