from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyInfo"]

class KeyInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/keystore/KeyInfo"
    getDigests = JavaMethod("()[Ljava/lang/String;")
    getEncryptionPaddings = JavaMethod("()[Ljava/lang/String;")
    getBlockModes = JavaMethod("()[Ljava/lang/String;")
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
    getOrigin = JavaMethod("()I")
    getSecurityLevel = JavaMethod("()I")
    getRemainingUsageCount = JavaMethod("()I")
    isInsideSecureHardware = JavaMethod("()Z")
    isTrustedUserPresenceRequired = JavaMethod("()Z")
    isUserAuthenticationRequirementEnforcedBySecureHardware = JavaMethod("()Z")