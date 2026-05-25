from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FingerprintManager"]

class FingerprintManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/fingerprint/FingerprintManager"
    FINGERPRINT_ACQUIRED_GOOD = JavaStaticField("I")
    FINGERPRINT_ACQUIRED_IMAGER_DIRTY = JavaStaticField("I")
    FINGERPRINT_ACQUIRED_INSUFFICIENT = JavaStaticField("I")
    FINGERPRINT_ACQUIRED_PARTIAL = JavaStaticField("I")
    FINGERPRINT_ACQUIRED_TOO_FAST = JavaStaticField("I")
    FINGERPRINT_ACQUIRED_TOO_SLOW = JavaStaticField("I")
    FINGERPRINT_ERROR_CANCELED = JavaStaticField("I")
    FINGERPRINT_ERROR_HW_NOT_PRESENT = JavaStaticField("I")
    FINGERPRINT_ERROR_HW_UNAVAILABLE = JavaStaticField("I")
    FINGERPRINT_ERROR_LOCKOUT = JavaStaticField("I")
    FINGERPRINT_ERROR_LOCKOUT_PERMANENT = JavaStaticField("I")
    FINGERPRINT_ERROR_NO_FINGERPRINTS = JavaStaticField("I")
    FINGERPRINT_ERROR_NO_SPACE = JavaStaticField("I")
    FINGERPRINT_ERROR_TIMEOUT = JavaStaticField("I")
    FINGERPRINT_ERROR_UNABLE_TO_PROCESS = JavaStaticField("I")
    FINGERPRINT_ERROR_USER_CANCELED = JavaStaticField("I")
    FINGERPRINT_ERROR_VENDOR = JavaStaticField("I")
    authenticate = JavaMethod("(Landroid/hardware/fingerprint/FingerprintManager$CryptoObject;Landroid/os/CancellationSignal;ILandroid/hardware/fingerprint/FingerprintManager$AuthenticationCallback;Landroid/os/Handler;)V")
    hasEnrolledFingerprints = JavaMethod("()Z")
    isHardwareDetected = JavaMethod("()Z")

    class AuthenticationCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/fingerprint/FingerprintManager/AuthenticationCallback"
        __javaconstructor__ = [("()V", False)]
        onAuthenticationError = JavaMethod("(ILjava/lang/CharSequence;)V")
        onAuthenticationHelp = JavaMethod("(ILjava/lang/CharSequence;)V")
        onAuthenticationSucceeded = JavaMethod("(Landroid/hardware/fingerprint/FingerprintManager$AuthenticationResult;)V")
        onAuthenticationFailed = JavaMethod("()V")

    class AuthenticationResult(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/fingerprint/FingerprintManager/AuthenticationResult"
        getCryptoObject = JavaMethod("()Landroid/hardware/fingerprint/FingerprintManager$CryptoObject;")

    class CryptoObject(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/fingerprint/FingerprintManager/CryptoObject"
        __javaconstructor__ = [("(Ljava/security/Signature;)V", False), ("(Ljavax/crypto/Cipher;)V", False), ("(Ljavax/crypto/Mac;)V", False)]
        getSignature = JavaMethod("()Ljava/security/Signature;")
        getCipher = JavaMethod("()Ljavax/crypto/Cipher;")
        getMac = JavaMethod("()Ljavax/crypto/Mac;")