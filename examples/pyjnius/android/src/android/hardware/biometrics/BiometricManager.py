from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BiometricManager"]

class BiometricManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/biometrics/BiometricManager"
    BIOMETRIC_ERROR_HW_UNAVAILABLE = JavaStaticField("I")
    BIOMETRIC_ERROR_IDENTITY_CHECK_NOT_ACTIVE = JavaStaticField("I")
    BIOMETRIC_ERROR_NONE_ENROLLED = JavaStaticField("I")
    BIOMETRIC_ERROR_NOT_ENABLED_FOR_APPS = JavaStaticField("I")
    BIOMETRIC_ERROR_NO_HARDWARE = JavaStaticField("I")
    BIOMETRIC_ERROR_SECURITY_UPDATE_REQUIRED = JavaStaticField("I")
    BIOMETRIC_NO_AUTHENTICATION = JavaStaticField("J")
    BIOMETRIC_SUCCESS = JavaStaticField("I")
    canAuthenticate = JavaMultipleMethod([("(I)I", False, False), ("()I", False, False)])
    getLastAuthenticationTime = JavaMethod("(I)J")
    getStrings = JavaMethod("(I)Landroid/hardware/biometrics/BiometricManager$Strings;")

    class Strings(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/biometrics/BiometricManager$Strings"
        getButtonLabel = JavaMethod("()Ljava/lang/CharSequence;")
        getPromptMessage = JavaMethod("()Ljava/lang/CharSequence;")
        getSettingName = JavaMethod("()Ljava/lang/CharSequence;")

    class Authenticators(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/biometrics/BiometricManager$Authenticators"
        BIOMETRIC_STRONG = JavaStaticField("I")
        BIOMETRIC_WEAK = JavaStaticField("I")
        DEVICE_CREDENTIAL = JavaStaticField("I")
        IDENTITY_CHECK = JavaStaticField("I")