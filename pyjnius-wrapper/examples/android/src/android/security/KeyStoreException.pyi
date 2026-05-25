from typing import Any, ClassVar, overload

class KeyStoreException:
    ERROR_ATTESTATION_CHALLENGE_TOO_LARGE: ClassVar[int]
    ERROR_ATTESTATION_KEYS_UNAVAILABLE: ClassVar[int]
    ERROR_ID_ATTESTATION_FAILURE: ClassVar[int]
    ERROR_INCORRECT_USAGE: ClassVar[int]
    ERROR_INTERNAL_SYSTEM_ERROR: ClassVar[int]
    ERROR_KEYMINT_FAILURE: ClassVar[int]
    ERROR_KEYSTORE_FAILURE: ClassVar[int]
    ERROR_KEYSTORE_UNINITIALIZED: ClassVar[int]
    ERROR_KEY_CORRUPTED: ClassVar[int]
    ERROR_KEY_DOES_NOT_EXIST: ClassVar[int]
    ERROR_KEY_NOT_TEMPORALLY_VALID: ClassVar[int]
    ERROR_KEY_OPERATION_EXPIRED: ClassVar[int]
    ERROR_OTHER: ClassVar[int]
    ERROR_PERMISSION_DENIED: ClassVar[int]
    ERROR_UNIMPLEMENTED: ClassVar[int]
    ERROR_USER_AUTHENTICATION_REQUIRED: ClassVar[int]
    RETRY_AFTER_NEXT_REBOOT: ClassVar[int]
    RETRY_NEVER: ClassVar[int]
    RETRY_WHEN_CONNECTIVITY_AVAILABLE: ClassVar[int]
    RETRY_WITH_EXPONENTIAL_BACKOFF: ClassVar[int]
    def getNumericErrorCode(self) -> int: ...
    def isTransientFailure(self) -> bool: ...
    def requiresUserAuthentication(self) -> bool: ...
    def isSystemError(self) -> bool: ...
    def getRetryPolicy(self) -> int: ...
    def toString(self) -> str: ...
