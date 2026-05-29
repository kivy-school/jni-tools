from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyProtection"]

class KeyProtection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/keystore/KeyProtection"
    getDigests = JavaMethod("()[Ljava/lang/String;")
    getEncryptionPaddings = JavaMethod("()[Ljava/lang/String;")
    getBlockModes = JavaMethod("()[Ljava/lang/String;")
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
        setBlockModes = JavaMethod("([Ljava/lang/String;)Landroid/security/keystore/KeyProtection$Builder;", varargs=True)
        setDigests = JavaMethod("([Ljava/lang/String;)Landroid/security/keystore/KeyProtection$Builder;", varargs=True)
        setKeyValidityEnd = JavaMethod("(Ljava/util/Date;)Landroid/security/keystore/KeyProtection$Builder;")
        setEncryptionPaddings = JavaMethod("([Ljava/lang/String;)Landroid/security/keystore/KeyProtection$Builder;", varargs=True)
        setInvalidatedByBiometricEnrollment = JavaMethod("(Z)Landroid/security/keystore/KeyProtection$Builder;")
        setIsStrongBoxBacked = JavaMethod("(Z)Landroid/security/keystore/KeyProtection$Builder;")
        setKeyValidityForConsumptionEnd = JavaMethod("(Ljava/util/Date;)Landroid/security/keystore/KeyProtection$Builder;")
        setKeyValidityForOriginationEnd = JavaMethod("(Ljava/util/Date;)Landroid/security/keystore/KeyProtection$Builder;")
        setKeyValidityStart = JavaMethod("(Ljava/util/Date;)Landroid/security/keystore/KeyProtection$Builder;")
        setRandomizedEncryptionRequired = JavaMethod("(Z)Landroid/security/keystore/KeyProtection$Builder;")
        setSignaturePaddings = JavaMethod("([Ljava/lang/String;)Landroid/security/keystore/KeyProtection$Builder;", varargs=True)
        setUnlockedDeviceRequired = JavaMethod("(Z)Landroid/security/keystore/KeyProtection$Builder;")
        setUserAuthenticationParameters = JavaMethod("(II)Landroid/security/keystore/KeyProtection$Builder;")
        setUserAuthenticationRequired = JavaMethod("(Z)Landroid/security/keystore/KeyProtection$Builder;")
        setUserAuthenticationValidWhileOnBody = JavaMethod("(Z)Landroid/security/keystore/KeyProtection$Builder;")
        setUserAuthenticationValidityDurationSeconds = JavaMethod("(I)Landroid/security/keystore/KeyProtection$Builder;")
        setUserConfirmationRequired = JavaMethod("(Z)Landroid/security/keystore/KeyProtection$Builder;")
        setUserPresenceRequired = JavaMethod("(Z)Landroid/security/keystore/KeyProtection$Builder;")
        setMgf1Digests = JavaMethod("([Ljava/lang/String;)Landroid/security/keystore/KeyProtection$Builder;", varargs=True)
        setMaxUsageCount = JavaMethod("(I)Landroid/security/keystore/KeyProtection$Builder;")
        build = JavaMethod("()Landroid/security/keystore/KeyProtection;")