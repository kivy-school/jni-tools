from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyInfo"]

class KeyInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/keystore/KeyInfo"
    getKeystoreAlias = JavaMethod("()Ljava/lang/String;")
    isInsideSecureHardware = JavaMethod("()Z")
    getOrigin = JavaMethod("()I")
    getKeySize = JavaMethod("()I")
    getKeyValidityStart = JavaMethod("()Ljava/util/Date;")
    getKeyValidityForConsumptionEnd = JavaMethod("()Ljava/util/Date;")
    getKeyValidityForOriginationEnd = JavaMethod("()Ljava/util/Date;")
    getPurposes = JavaMethod("()I")
    getBlockModes = JavaMethod("()[Ljava/lang/String;")
    getEncryptionPaddings = JavaMethod("()[Ljava/lang/String;")
    getSignaturePaddings = JavaMethod("()[Ljava/lang/String;")
    getDigests = JavaMethod("()[Ljava/lang/String;")
    isUserAuthenticationRequired = JavaMethod("()Z")
    isUserConfirmationRequired = JavaMethod("()Z")
    getUserAuthenticationValidityDurationSeconds = JavaMethod("()I")
    getUserAuthenticationType = JavaMethod("()I")
    isUserAuthenticationRequirementEnforcedBySecureHardware = JavaMethod("()Z")
    isUserAuthenticationValidWhileOnBody = JavaMethod("()Z")
    isInvalidatedByBiometricEnrollment = JavaMethod("()Z")
    isTrustedUserPresenceRequired = JavaMethod("()Z")
    getSecurityLevel = JavaMethod("()I")
    getRemainingUsageCount = JavaMethod("()I")