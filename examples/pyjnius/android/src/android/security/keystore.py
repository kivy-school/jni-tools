from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class SecureKeyImportUnavailableException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/keystore/SecureKeyImportUnavailableException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]

class UserPresenceUnavailableException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/keystore/UserPresenceUnavailableException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]

class KeyPermanentlyInvalidatedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/keystore/KeyPermanentlyInvalidatedException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]

class BackendBusyException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/keystore/BackendBusyException"
    __javaconstructor__ = [("(J)V", False), ("(JLjava/lang/String;Ljava/lang/Throwable;)V", False), ("(JLjava/lang/String;)V", False)]
    getBackOffHintMillis = JavaMethod("()J")

class KeyExpiredException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/keystore/KeyExpiredException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]

class KeyNotYetValidException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/keystore/KeyNotYetValidException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]

class KeyProtection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/keystore/KeyProtection"
    getBlockModes = JavaMethod("()[Ljava/lang/String;")
    getDigests = JavaMethod("()[Ljava/lang/String;")
    getEncryptionPaddings = JavaMethod("()[Ljava/lang/String;")
    getKeyValidityForConsumptionEnd = JavaMethod("()Ljava/util/Date;")
    getKeyValidityForOriginationEnd = JavaMethod("()Ljava/util/Date;")
    getKeyValidityStart = JavaMethod("()Ljava/util/Date;")
    getMaxUsageCount = JavaMethod("()I")
    getMgf1Digests = JavaMethod("()Ljava/util/Set;")
    getPurposes = JavaMethod("()I")
    getSignaturePaddings = JavaMethod("()[Ljava/lang/String;")
    getUserAuthenticationType = JavaMethod("()I")
    getUserAuthenticationValidityDurationSeconds = JavaMethod("()I")
    isDigestsSpecified = JavaMethod("()Z")
    isInvalidatedByBiometricEnrollment = JavaMethod("()Z")
    isMgf1DigestsSpecified = JavaMethod("()Z")
    isRandomizedEncryptionRequired = JavaMethod("()Z")
    isUnlockedDeviceRequired = JavaMethod("()Z")
    isUserAuthenticationRequired = JavaMethod("()Z")
    isUserAuthenticationValidWhileOnBody = JavaMethod("()Z")
    isUserConfirmationRequired = JavaMethod("()Z")
    isUserPresenceRequired = JavaMethod("()Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/security/keystore/KeyProtection$Builder"
        __javaconstructor__ = [("(I)V", False)]
        setDigests = JavaMethod("([Ljava/lang/String;)Landroid/security/keystore/KeyProtection$Builder;", varargs=True)
        setEncryptionPaddings = JavaMethod("([Ljava/lang/String;)Landroid/security/keystore/KeyProtection$Builder;", varargs=True)
        setInvalidatedByBiometricEnrollment = JavaMethod("(Z)Landroid/security/keystore/KeyProtection$Builder;")
        setIsStrongBoxBacked = JavaMethod("(Z)Landroid/security/keystore/KeyProtection$Builder;")
        setKeyValidityEnd = JavaMethod("(Ljava/util/Date;)Landroid/security/keystore/KeyProtection$Builder;")
        setKeyValidityForConsumptionEnd = JavaMethod("(Ljava/util/Date;)Landroid/security/keystore/KeyProtection$Builder;")
        setKeyValidityForOriginationEnd = JavaMethod("(Ljava/util/Date;)Landroid/security/keystore/KeyProtection$Builder;")
        setKeyValidityStart = JavaMethod("(Ljava/util/Date;)Landroid/security/keystore/KeyProtection$Builder;")
        setMaxUsageCount = JavaMethod("(I)Landroid/security/keystore/KeyProtection$Builder;")
        setMgf1Digests = JavaMethod("([Ljava/lang/String;)Landroid/security/keystore/KeyProtection$Builder;", varargs=True)
        setRandomizedEncryptionRequired = JavaMethod("(Z)Landroid/security/keystore/KeyProtection$Builder;")
        setBlockModes = JavaMethod("([Ljava/lang/String;)Landroid/security/keystore/KeyProtection$Builder;", varargs=True)
        setUnlockedDeviceRequired = JavaMethod("(Z)Landroid/security/keystore/KeyProtection$Builder;")
        setSignaturePaddings = JavaMethod("([Ljava/lang/String;)Landroid/security/keystore/KeyProtection$Builder;", varargs=True)
        setUserAuthenticationParameters = JavaMethod("(II)Landroid/security/keystore/KeyProtection$Builder;")
        setUserAuthenticationRequired = JavaMethod("(Z)Landroid/security/keystore/KeyProtection$Builder;")
        setUserAuthenticationValidWhileOnBody = JavaMethod("(Z)Landroid/security/keystore/KeyProtection$Builder;")
        setUserAuthenticationValidityDurationSeconds = JavaMethod("(I)Landroid/security/keystore/KeyProtection$Builder;")
        setUserConfirmationRequired = JavaMethod("(Z)Landroid/security/keystore/KeyProtection$Builder;")
        setUserPresenceRequired = JavaMethod("(Z)Landroid/security/keystore/KeyProtection$Builder;")
        build = JavaMethod("()Landroid/security/keystore/KeyProtection;")

class StrongBoxUnavailableException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/keystore/StrongBoxUnavailableException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]

class KeyStoreManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/keystore/KeyStoreManager"
    MODULE_HASH = JavaStaticField("I")
    getGrantedKeyPairFromId = JavaMethod("(J)Ljava/security/KeyPair;")
    getGrantedCertificateChainFromId = JavaMethod("(J)Ljava/util/List;")
    getGrantedKeyFromId = JavaMethod("(J)Ljava/security/Key;")
    grantKeyAccess = JavaMethod("(Ljava/lang/String;I)J")
    getSupplementaryAttestationInfo = JavaMethod("(I)[B")
    revokeKeyAccess = JavaMethod("(Ljava/lang/String;I)V")

class KeyInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/keystore/KeyInfo"
    getSecurityLevel = JavaMethod("()I")
    getOrigin = JavaMethod("()I")
    getBlockModes = JavaMethod("()[Ljava/lang/String;")
    getDigests = JavaMethod("()[Ljava/lang/String;")
    getEncryptionPaddings = JavaMethod("()[Ljava/lang/String;")
    getKeySize = JavaMethod("()I")
    getKeyValidityForConsumptionEnd = JavaMethod("()Ljava/util/Date;")
    getKeyValidityForOriginationEnd = JavaMethod("()Ljava/util/Date;")
    getKeyValidityStart = JavaMethod("()Ljava/util/Date;")
    getKeystoreAlias = JavaMethod("()Ljava/lang/String;")
    getPurposes = JavaMethod("()I")
    getSignaturePaddings = JavaMethod("()[Ljava/lang/String;")
    getUserAuthenticationType = JavaMethod("()I")
    getUserAuthenticationValidityDurationSeconds = JavaMethod("()I")
    isInvalidatedByBiometricEnrollment = JavaMethod("()Z")
    isUserAuthenticationRequired = JavaMethod("()Z")
    isUserAuthenticationValidWhileOnBody = JavaMethod("()Z")
    isUserConfirmationRequired = JavaMethod("()Z")
    isInsideSecureHardware = JavaMethod("()Z")
    getRemainingUsageCount = JavaMethod("()I")
    isUserAuthenticationRequirementEnforcedBySecureHardware = JavaMethod("()Z")
    isTrustedUserPresenceRequired = JavaMethod("()Z")

class KeyGenParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/keystore/KeyGenParameterSpec"
    getAttestationChallenge = JavaMethod("()[B")
    getAttestKeyAlias = JavaMethod("()Ljava/lang/String;")
    getBlockModes = JavaMethod("()[Ljava/lang/String;")
    getCertificateNotAfter = JavaMethod("()Ljava/util/Date;")
    getCertificateNotBefore = JavaMethod("()Ljava/util/Date;")
    getCertificateSerialNumber = JavaMethod("()Ljava/math/BigInteger;")
    getCertificateSubject = JavaMethod("()Ljavax/security/auth/x500/X500Principal;")
    getDigests = JavaMethod("()[Ljava/lang/String;")
    getEncryptionPaddings = JavaMethod("()[Ljava/lang/String;")
    getKeySize = JavaMethod("()I")
    getKeyValidityForConsumptionEnd = JavaMethod("()Ljava/util/Date;")
    getKeyValidityForOriginationEnd = JavaMethod("()Ljava/util/Date;")
    getKeyValidityStart = JavaMethod("()Ljava/util/Date;")
    getKeystoreAlias = JavaMethod("()Ljava/lang/String;")
    getMaxUsageCount = JavaMethod("()I")
    getMgf1Digests = JavaMethod("()Ljava/util/Set;")
    getPurposes = JavaMethod("()I")
    getSignaturePaddings = JavaMethod("()[Ljava/lang/String;")
    getUserAuthenticationType = JavaMethod("()I")
    getUserAuthenticationValidityDurationSeconds = JavaMethod("()I")
    isDevicePropertiesAttestationIncluded = JavaMethod("()Z")
    isDigestsSpecified = JavaMethod("()Z")
    isInvalidatedByBiometricEnrollment = JavaMethod("()Z")
    isMgf1DigestsSpecified = JavaMethod("()Z")
    isRandomizedEncryptionRequired = JavaMethod("()Z")
    isStrongBoxBacked = JavaMethod("()Z")
    isUnlockedDeviceRequired = JavaMethod("()Z")
    isUserAuthenticationRequired = JavaMethod("()Z")
    isUserAuthenticationValidWhileOnBody = JavaMethod("()Z")
    isUserConfirmationRequired = JavaMethod("()Z")
    isUserPresenceRequired = JavaMethod("()Z")
    getAlgorithmParameterSpec = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/security/keystore/KeyGenParameterSpec$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;I)V", False)]
        setCertificateSubject = JavaMethod("(Ljavax/security/auth/x500/X500Principal;)Landroid/security/keystore/KeyGenParameterSpec$Builder;")
        setDevicePropertiesAttestationIncluded = JavaMethod("(Z)Landroid/security/keystore/KeyGenParameterSpec$Builder;")
        setAttestKeyAlias = JavaMethod("(Ljava/lang/String;)Landroid/security/keystore/KeyGenParameterSpec$Builder;")
        setCertificateNotAfter = JavaMethod("(Ljava/util/Date;)Landroid/security/keystore/KeyGenParameterSpec$Builder;")
        setCertificateNotBefore = JavaMethod("(Ljava/util/Date;)Landroid/security/keystore/KeyGenParameterSpec$Builder;")
        setCertificateSerialNumber = JavaMethod("(Ljava/math/BigInteger;)Landroid/security/keystore/KeyGenParameterSpec$Builder;")
        setAttestationChallenge = JavaMethod("([B)Landroid/security/keystore/KeyGenParameterSpec$Builder;")
        setAlgorithmParameterSpec = JavaMethod("(Ljava/security/spec/AlgorithmParameterSpec;)Landroid/security/keystore/KeyGenParameterSpec$Builder;")
        setKeySize = JavaMethod("(I)Landroid/security/keystore/KeyGenParameterSpec$Builder;")
        setDigests = JavaMethod("([Ljava/lang/String;)Landroid/security/keystore/KeyGenParameterSpec$Builder;", varargs=True)
        setEncryptionPaddings = JavaMethod("([Ljava/lang/String;)Landroid/security/keystore/KeyGenParameterSpec$Builder;", varargs=True)
        setInvalidatedByBiometricEnrollment = JavaMethod("(Z)Landroid/security/keystore/KeyGenParameterSpec$Builder;")
        setIsStrongBoxBacked = JavaMethod("(Z)Landroid/security/keystore/KeyGenParameterSpec$Builder;")
        setKeyValidityEnd = JavaMethod("(Ljava/util/Date;)Landroid/security/keystore/KeyGenParameterSpec$Builder;")
        setKeyValidityForConsumptionEnd = JavaMethod("(Ljava/util/Date;)Landroid/security/keystore/KeyGenParameterSpec$Builder;")
        setKeyValidityForOriginationEnd = JavaMethod("(Ljava/util/Date;)Landroid/security/keystore/KeyGenParameterSpec$Builder;")
        setKeyValidityStart = JavaMethod("(Ljava/util/Date;)Landroid/security/keystore/KeyGenParameterSpec$Builder;")
        setMaxUsageCount = JavaMethod("(I)Landroid/security/keystore/KeyGenParameterSpec$Builder;")
        setMgf1Digests = JavaMethod("([Ljava/lang/String;)Landroid/security/keystore/KeyGenParameterSpec$Builder;", varargs=True)
        setRandomizedEncryptionRequired = JavaMethod("(Z)Landroid/security/keystore/KeyGenParameterSpec$Builder;")
        setBlockModes = JavaMethod("([Ljava/lang/String;)Landroid/security/keystore/KeyGenParameterSpec$Builder;", varargs=True)
        setUnlockedDeviceRequired = JavaMethod("(Z)Landroid/security/keystore/KeyGenParameterSpec$Builder;")
        setSignaturePaddings = JavaMethod("([Ljava/lang/String;)Landroid/security/keystore/KeyGenParameterSpec$Builder;", varargs=True)
        setUserAuthenticationParameters = JavaMethod("(II)Landroid/security/keystore/KeyGenParameterSpec$Builder;")
        setUserAuthenticationRequired = JavaMethod("(Z)Landroid/security/keystore/KeyGenParameterSpec$Builder;")
        setUserAuthenticationValidWhileOnBody = JavaMethod("(Z)Landroid/security/keystore/KeyGenParameterSpec$Builder;")
        setUserAuthenticationValidityDurationSeconds = JavaMethod("(I)Landroid/security/keystore/KeyGenParameterSpec$Builder;")
        setUserConfirmationRequired = JavaMethod("(Z)Landroid/security/keystore/KeyGenParameterSpec$Builder;")
        setUserPresenceRequired = JavaMethod("(Z)Landroid/security/keystore/KeyGenParameterSpec$Builder;")
        build = JavaMethod("()Landroid/security/keystore/KeyGenParameterSpec;")

class UserNotAuthenticatedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/keystore/UserNotAuthenticatedException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]

class KeyProperties(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/keystore/KeyProperties"
    AUTH_BIOMETRIC_STRONG = JavaStaticField("I")
    AUTH_DEVICE_CREDENTIAL = JavaStaticField("I")
    BLOCK_MODE_CBC = JavaStaticField("Ljava/lang/String;")
    BLOCK_MODE_CTR = JavaStaticField("Ljava/lang/String;")
    BLOCK_MODE_ECB = JavaStaticField("Ljava/lang/String;")
    BLOCK_MODE_GCM = JavaStaticField("Ljava/lang/String;")
    DIGEST_MD5 = JavaStaticField("Ljava/lang/String;")
    DIGEST_NONE = JavaStaticField("Ljava/lang/String;")
    DIGEST_SHA1 = JavaStaticField("Ljava/lang/String;")
    DIGEST_SHA224 = JavaStaticField("Ljava/lang/String;")
    DIGEST_SHA256 = JavaStaticField("Ljava/lang/String;")
    DIGEST_SHA384 = JavaStaticField("Ljava/lang/String;")
    DIGEST_SHA512 = JavaStaticField("Ljava/lang/String;")
    ENCRYPTION_PADDING_NONE = JavaStaticField("Ljava/lang/String;")
    ENCRYPTION_PADDING_PKCS7 = JavaStaticField("Ljava/lang/String;")
    ENCRYPTION_PADDING_RSA_OAEP = JavaStaticField("Ljava/lang/String;")
    ENCRYPTION_PADDING_RSA_PKCS1 = JavaStaticField("Ljava/lang/String;")
    KEY_ALGORITHM_3DES = JavaStaticField("Ljava/lang/String;")
    KEY_ALGORITHM_AES = JavaStaticField("Ljava/lang/String;")
    KEY_ALGORITHM_EC = JavaStaticField("Ljava/lang/String;")
    KEY_ALGORITHM_HMAC_SHA1 = JavaStaticField("Ljava/lang/String;")
    KEY_ALGORITHM_HMAC_SHA224 = JavaStaticField("Ljava/lang/String;")
    KEY_ALGORITHM_HMAC_SHA256 = JavaStaticField("Ljava/lang/String;")
    KEY_ALGORITHM_HMAC_SHA384 = JavaStaticField("Ljava/lang/String;")
    KEY_ALGORITHM_HMAC_SHA512 = JavaStaticField("Ljava/lang/String;")
    KEY_ALGORITHM_RSA = JavaStaticField("Ljava/lang/String;")
    ORIGIN_GENERATED = JavaStaticField("I")
    ORIGIN_IMPORTED = JavaStaticField("I")
    ORIGIN_SECURELY_IMPORTED = JavaStaticField("I")
    ORIGIN_UNKNOWN = JavaStaticField("I")
    PURPOSE_AGREE_KEY = JavaStaticField("I")
    PURPOSE_ATTEST_KEY = JavaStaticField("I")
    PURPOSE_DECRYPT = JavaStaticField("I")
    PURPOSE_ENCRYPT = JavaStaticField("I")
    PURPOSE_SIGN = JavaStaticField("I")
    PURPOSE_VERIFY = JavaStaticField("I")
    PURPOSE_WRAP_KEY = JavaStaticField("I")
    SECURITY_LEVEL_SOFTWARE = JavaStaticField("I")
    SECURITY_LEVEL_STRONGBOX = JavaStaticField("I")
    SECURITY_LEVEL_TRUSTED_ENVIRONMENT = JavaStaticField("I")
    SECURITY_LEVEL_UNKNOWN = JavaStaticField("I")
    SECURITY_LEVEL_UNKNOWN_SECURE = JavaStaticField("I")
    SIGNATURE_PADDING_RSA_PKCS1 = JavaStaticField("Ljava/lang/String;")
    SIGNATURE_PADDING_RSA_PSS = JavaStaticField("Ljava/lang/String;")
    UNRESTRICTED_USAGE_COUNT = JavaStaticField("I")

class WrappedKeyEntry(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/keystore/WrappedKeyEntry"
    __javaconstructor__ = [("([BLjava/lang/String;Ljava/lang/String;Ljava/security/spec/AlgorithmParameterSpec;)V", False)]
    getWrappedKeyBytes = JavaMethod("()[B")
    getWrappingKeyAlias = JavaMethod("()Ljava/lang/String;")
    getAlgorithmParameterSpec = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")
    getTransformation = JavaMethod("()Ljava/lang/String;")