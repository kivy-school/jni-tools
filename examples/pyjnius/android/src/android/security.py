from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class AppUriAuthenticationPolicy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/AppUriAuthenticationPolicy"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getAppAndUriMappings = JavaMethod("()Ljava/util/Map;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/security/AppUriAuthenticationPolicy$Builder"
        __javaconstructor__ = [("()V", False)]
        addAppAndUriMapping = JavaMethod("(Ljava/lang/String;Landroid/net/Uri;Ljava/lang/String;)Landroid/security/AppUriAuthenticationPolicy$Builder;")
        build = JavaMethod("()Landroid/security/AppUriAuthenticationPolicy;")

class ConfirmationCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/ConfirmationCallback"
    __javaconstructor__ = [("()V", False)]
    onCanceled = JavaMethod("()V")
    onDismissed = JavaMethod("()V")
    onConfirmed = JavaMethod("([B)V")
    onError = JavaMethod("(Ljava/lang/Throwable;)V")

class ConfirmationPrompt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/ConfirmationPrompt"
    presentPrompt = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/security/ConfirmationCallback;)V")
    cancelPrompt = JavaMethod("()V")
    isSupported = JavaStaticMethod("(Landroid/content/Context;)Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/security/ConfirmationPrompt$Builder"
        __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
        setPromptText = JavaMethod("(Ljava/lang/CharSequence;)Landroid/security/ConfirmationPrompt$Builder;")
        setExtraData = JavaMethod("([B)Landroid/security/ConfirmationPrompt$Builder;")
        build = JavaMethod("()Landroid/security/ConfirmationPrompt;")

class KeyChainAliasCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/KeyChainAliasCallback"
    alias = JavaMethod("(Ljava/lang/String;)V")

class ConfirmationAlreadyPresentingException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/ConfirmationAlreadyPresentingException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]

class KeyPairGeneratorSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/KeyPairGeneratorSpec"
    getKeySize = JavaMethod("()I")
    getKeystoreAlias = JavaMethod("()Ljava/lang/String;")
    getEndDate = JavaMethod("()Ljava/util/Date;")
    isEncryptionRequired = JavaMethod("()Z")
    getKeyType = JavaMethod("()Ljava/lang/String;")
    getAlgorithmParameterSpec = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")
    getContext = JavaMethod("()Landroid/content/Context;")
    getStartDate = JavaMethod("()Ljava/util/Date;")
    getSerialNumber = JavaMethod("()Ljava/math/BigInteger;")
    getSubjectDN = JavaMethod("()Ljavax/security/auth/x500/X500Principal;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/security/KeyPairGeneratorSpec$Builder"
        __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
        setAlias = JavaMethod("(Ljava/lang/String;)Landroid/security/KeyPairGeneratorSpec$Builder;")
        setEndDate = JavaMethod("(Ljava/util/Date;)Landroid/security/KeyPairGeneratorSpec$Builder;")
        setEncryptionRequired = JavaMethod("()Landroid/security/KeyPairGeneratorSpec$Builder;")
        setAlgorithmParameterSpec = JavaMethod("(Ljava/security/spec/AlgorithmParameterSpec;)Landroid/security/KeyPairGeneratorSpec$Builder;")
        setKeySize = JavaMethod("(I)Landroid/security/KeyPairGeneratorSpec$Builder;")
        setKeyType = JavaMethod("(Ljava/lang/String;)Landroid/security/KeyPairGeneratorSpec$Builder;")
        setSerialNumber = JavaMethod("(Ljava/math/BigInteger;)Landroid/security/KeyPairGeneratorSpec$Builder;")
        setStartDate = JavaMethod("(Ljava/util/Date;)Landroid/security/KeyPairGeneratorSpec$Builder;")
        setSubject = JavaMethod("(Ljavax/security/auth/x500/X500Principal;)Landroid/security/KeyPairGeneratorSpec$Builder;")
        build = JavaMethod("()Landroid/security/KeyPairGeneratorSpec;")

class KeyChain(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/KeyChain"
    __javaconstructor__ = [("()V", False)]
    ACTION_KEYCHAIN_CHANGED = JavaStaticField("Ljava/lang/String;")
    ACTION_KEY_ACCESS_CHANGED = JavaStaticField("Ljava/lang/String;")
    ACTION_STORAGE_CHANGED = JavaStaticField("Ljava/lang/String;")
    ACTION_TRUST_STORE_CHANGED = JavaStaticField("Ljava/lang/String;")
    EXTRA_CERTIFICATE = JavaStaticField("Ljava/lang/String;")
    EXTRA_KEY_ACCESSIBLE = JavaStaticField("Ljava/lang/String;")
    EXTRA_KEY_ALIAS = JavaStaticField("Ljava/lang/String;")
    EXTRA_NAME = JavaStaticField("Ljava/lang/String;")
    EXTRA_PKCS12 = JavaStaticField("Ljava/lang/String;")
    KEY_ALIAS_SELECTION_DENIED = JavaStaticField("Ljava/lang/String;")
    choosePrivateKeyAlias = JavaMultipleMethod([("(Landroid/app/Activity;Landroid/security/KeyChainAliasCallback;[Ljava/lang/String;[Ljava/security/Principal;Ljava/lang/String;ILjava/lang/String;)V", True, False), ("(Landroid/app/Activity;Landroid/security/KeyChainAliasCallback;[Ljava/lang/String;[Ljava/security/Principal;Landroid/net/Uri;Ljava/lang/String;)V", True, False)])
    createInstallIntent = JavaStaticMethod("()Landroid/content/Intent;")
    createManageCredentialsIntent = JavaStaticMethod("(Landroid/security/AppUriAuthenticationPolicy;)Landroid/content/Intent;")
    getCredentialManagementAppPolicy = JavaStaticMethod("(Landroid/content/Context;)Landroid/security/AppUriAuthenticationPolicy;")
    getPrivateKey = JavaStaticMethod("(Landroid/content/Context;Ljava/lang/String;)Ljava/security/PrivateKey;")
    isBoundKeyAlgorithm = JavaStaticMethod("(Ljava/lang/String;)Z")
    isCredentialManagementApp = JavaStaticMethod("(Landroid/content/Context;)Z")
    isKeyAlgorithmSupported = JavaStaticMethod("(Ljava/lang/String;)Z")
    removeCredentialManagementApp = JavaStaticMethod("(Landroid/content/Context;)Z")
    getCertificateChain = JavaStaticMethod("(Landroid/content/Context;Ljava/lang/String;)[Ljava/security/cert/X509Certificate;")

class KeyStoreException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/KeyStoreException"
    ERROR_ATTESTATION_CHALLENGE_TOO_LARGE = JavaStaticField("I")
    ERROR_ATTESTATION_KEYS_UNAVAILABLE = JavaStaticField("I")
    ERROR_ID_ATTESTATION_FAILURE = JavaStaticField("I")
    ERROR_INCORRECT_USAGE = JavaStaticField("I")
    ERROR_INTERNAL_SYSTEM_ERROR = JavaStaticField("I")
    ERROR_KEYMINT_FAILURE = JavaStaticField("I")
    ERROR_KEYSTORE_FAILURE = JavaStaticField("I")
    ERROR_KEYSTORE_UNINITIALIZED = JavaStaticField("I")
    ERROR_KEY_CORRUPTED = JavaStaticField("I")
    ERROR_KEY_DOES_NOT_EXIST = JavaStaticField("I")
    ERROR_KEY_NOT_TEMPORALLY_VALID = JavaStaticField("I")
    ERROR_KEY_OPERATION_EXPIRED = JavaStaticField("I")
    ERROR_OTHER = JavaStaticField("I")
    ERROR_PERMISSION_DENIED = JavaStaticField("I")
    ERROR_UNIMPLEMENTED = JavaStaticField("I")
    ERROR_USER_AUTHENTICATION_REQUIRED = JavaStaticField("I")
    RETRY_AFTER_NEXT_REBOOT = JavaStaticField("I")
    RETRY_NEVER = JavaStaticField("I")
    RETRY_WHEN_CONNECTIVITY_AVAILABLE = JavaStaticField("I")
    RETRY_WITH_EXPONENTIAL_BACKOFF = JavaStaticField("I")
    getNumericErrorCode = JavaMethod("()I")
    getRetryPolicy = JavaMethod("()I")
    isSystemError = JavaMethod("()Z")
    isTransientFailure = JavaMethod("()Z")
    requiresUserAuthentication = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")

class FileIntegrityManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/FileIntegrityManager"
    isApkVeritySupported = JavaMethod("()Z")
    isAppSourceCertificateTrusted = JavaMethod("(Ljava/security/cert/X509Certificate;)Z")

class KeyStoreParameter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/KeyStoreParameter"
    isEncryptionRequired = JavaMethod("()Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/security/KeyStoreParameter$Builder"
        __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
        setEncryptionRequired = JavaMethod("(Z)Landroid/security/KeyStoreParameter$Builder;")
        build = JavaMethod("()Landroid/security/KeyStoreParameter;")

class AttestedKeyPair(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/AttestedKeyPair"
    __javaconstructor__ = [("(Ljava/security/KeyPair;Ljava/util/List;)V", False)]
    getAttestationRecord = JavaMethod("()Ljava/util/List;")
    getKeyPair = JavaMethod("()Ljava/security/KeyPair;")

class KeyChainException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/KeyChainException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]

class ConfirmationNotAvailableException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/ConfirmationNotAvailableException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]

class NetworkSecurityPolicy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/NetworkSecurityPolicy"
    isCleartextTrafficPermitted = JavaMultipleMethod([("(Ljava/lang/String;)Z", False, False), ("()Z", False, False)])
    isCertificateTransparencyVerificationRequired = JavaMethod("(Ljava/lang/String;)Z")
    getInstance = JavaStaticMethod("()Landroid/security/NetworkSecurityPolicy;")