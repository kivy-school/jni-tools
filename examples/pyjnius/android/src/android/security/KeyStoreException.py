from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyStoreException"]

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
    getRetryPolicy = JavaMethod("()I")
    isSystemError = JavaMethod("()Z")
    getNumericErrorCode = JavaMethod("()I")
    isTransientFailure = JavaMethod("()Z")
    requiresUserAuthentication = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")