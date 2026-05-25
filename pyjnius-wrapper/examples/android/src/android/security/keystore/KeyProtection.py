from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyProtection"]

class KeyProtection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/keystore/KeyProtection"
    getKeyValidityStart = JavaMethod("()Ljava/util/Date;")
    getKeyValidityForConsumptionEnd = JavaMethod("()Ljava/util/Date;")
    getKeyValidityForOriginationEnd = JavaMethod("()Ljava/util/Date;")
    getPurposes = JavaMethod("()I")
    getEncryptionPaddings = JavaMethod("()[Ljava/lang/String;")
    getSignaturePaddings = JavaMethod("()[Ljava/lang/String;")
    getDigests = JavaMethod("()[Ljava/lang/String;")
    isDigestsSpecified = JavaMethod("()Z")
    getMgf1Digests = JavaMethod("()Ljava/util/Set;")
    isMgf1DigestsSpecified = JavaMethod("()Z")
    getBlockModes = JavaMethod("()[Ljava/lang/String;")
    isRandomizedEncryptionRequired = JavaMethod("()Z")
    isUserAuthenticationRequired = JavaMethod("()Z")
    isUserConfirmationRequired = JavaMethod("()Z")
    getUserAuthenticationType = JavaMethod("()I")
    getUserAuthenticationValidityDurationSeconds = JavaMethod("()I")
    isUserPresenceRequired = JavaMethod("()Z")
    isUserAuthenticationValidWhileOnBody = JavaMethod("()Z")
    isInvalidatedByBiometricEnrollment = JavaMethod("()Z")
    isUnlockedDeviceRequired = JavaMethod("()Z")
    getMaxUsageCount = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/security/keystore/KeyProtection/Builder"
        __javaconstructor__ = [("(I)V", False)]
        setKeyValidityStart = JavaMethod("(Ljava/util/Date;)Landroid/security/keystore/KeyProtection$Builder;")
        setKeyValidityEnd = JavaMethod("(Ljava/util/Date;)Landroid/security/keystore/KeyProtection$Builder;")
        setKeyValidityForOriginationEnd = JavaMethod("(Ljava/util/Date;)Landroid/security/keystore/KeyProtection$Builder;")
        setKeyValidityForConsumptionEnd = JavaMethod("(Ljava/util/Date;)Landroid/security/keystore/KeyProtection$Builder;")
        setEncryptionPaddings = JavaMethod("([Ljava/lang/String;)Landroid/security/keystore/KeyProtection$Builder;", varargs=True)
        setSignaturePaddings = JavaMethod("([Ljava/lang/String;)Landroid/security/keystore/KeyProtection$Builder;", varargs=True)
        setDigests = JavaMethod("([Ljava/lang/String;)Landroid/security/keystore/KeyProtection$Builder;", varargs=True)
        setMgf1Digests = JavaMethod("([Ljava/lang/String;)Landroid/security/keystore/KeyProtection$Builder;", varargs=True)
        setBlockModes = JavaMethod("([Ljava/lang/String;)Landroid/security/keystore/KeyProtection$Builder;", varargs=True)
        setRandomizedEncryptionRequired = JavaMethod("(Z)Landroid/security/keystore/KeyProtection$Builder;")
        setUserAuthenticationRequired = JavaMethod("(Z)Landroid/security/keystore/KeyProtection$Builder;")
        setUserConfirmationRequired = JavaMethod("(Z)Landroid/security/keystore/KeyProtection$Builder;")
        setUserAuthenticationValidityDurationSeconds = JavaMethod("(I)Landroid/security/keystore/KeyProtection$Builder;")
        setUserAuthenticationParameters = JavaMethod("(II)Landroid/security/keystore/KeyProtection$Builder;")
        setUserPresenceRequired = JavaMethod("(Z)Landroid/security/keystore/KeyProtection$Builder;")
        setUserAuthenticationValidWhileOnBody = JavaMethod("(Z)Landroid/security/keystore/KeyProtection$Builder;")
        setInvalidatedByBiometricEnrollment = JavaMethod("(Z)Landroid/security/keystore/KeyProtection$Builder;")
        setUnlockedDeviceRequired = JavaMethod("(Z)Landroid/security/keystore/KeyProtection$Builder;")
        setIsStrongBoxBacked = JavaMethod("(Z)Landroid/security/keystore/KeyProtection$Builder;")
        setMaxUsageCount = JavaMethod("(I)Landroid/security/keystore/KeyProtection$Builder;")
        build = JavaMethod("()Landroid/security/keystore/KeyProtection;")