from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class SecurityLog:
    LEVEL_ERROR: ClassVar[int]
    LEVEL_INFO: ClassVar[int]
    LEVEL_WARNING: ClassVar[int]
    TAG_ADB_SHELL_CMD: ClassVar[int]
    TAG_ADB_SHELL_INTERACTIVE: ClassVar[int]
    TAG_APP_PROCESS_START: ClassVar[int]
    TAG_BACKUP_SERVICE_TOGGLED: ClassVar[int]
    TAG_BLUETOOTH_CONNECTION: ClassVar[int]
    TAG_BLUETOOTH_DISCONNECTION: ClassVar[int]
    TAG_CAMERA_POLICY_SET: ClassVar[int]
    TAG_CERT_AUTHORITY_INSTALLED: ClassVar[int]
    TAG_CERT_AUTHORITY_REMOVED: ClassVar[int]
    TAG_CERT_VALIDATION_FAILURE: ClassVar[int]
    TAG_CRYPTO_SELF_TEST_COMPLETED: ClassVar[int]
    TAG_KEYGUARD_DISABLED_FEATURES_SET: ClassVar[int]
    TAG_KEYGUARD_DISMISSED: ClassVar[int]
    TAG_KEYGUARD_DISMISS_AUTH_ATTEMPT: ClassVar[int]
    TAG_KEYGUARD_SECURED: ClassVar[int]
    TAG_KEY_DESTRUCTION: ClassVar[int]
    TAG_KEY_GENERATED: ClassVar[int]
    TAG_KEY_IMPORT: ClassVar[int]
    TAG_KEY_INTEGRITY_VIOLATION: ClassVar[int]
    TAG_LOGGING_STARTED: ClassVar[int]
    TAG_LOGGING_STOPPED: ClassVar[int]
    TAG_LOG_BUFFER_SIZE_CRITICAL: ClassVar[int]
    TAG_MAX_PASSWORD_ATTEMPTS_SET: ClassVar[int]
    TAG_MAX_SCREEN_LOCK_TIMEOUT_SET: ClassVar[int]
    TAG_MEDIA_MOUNT: ClassVar[int]
    TAG_MEDIA_UNMOUNT: ClassVar[int]
    TAG_OS_SHUTDOWN: ClassVar[int]
    TAG_OS_STARTUP: ClassVar[int]
    TAG_PACKAGE_INSTALLED: ClassVar[int]
    TAG_PACKAGE_UNINSTALLED: ClassVar[int]
    TAG_PACKAGE_UPDATED: ClassVar[int]
    TAG_PASSWORD_CHANGED: ClassVar[int]
    TAG_PASSWORD_COMPLEXITY_REQUIRED: ClassVar[int]
    TAG_PASSWORD_COMPLEXITY_SET: ClassVar[int]
    TAG_PASSWORD_EXPIRATION_SET: ClassVar[int]
    TAG_PASSWORD_HISTORY_LENGTH_SET: ClassVar[int]
    TAG_REMOTE_LOCK: ClassVar[int]
    TAG_SYNC_RECV_FILE: ClassVar[int]
    TAG_SYNC_SEND_FILE: ClassVar[int]
    TAG_USER_RESTRICTION_ADDED: ClassVar[int]
    TAG_USER_RESTRICTION_REMOVED: ClassVar[int]
    TAG_WIFI_CONNECTION: ClassVar[int]
    TAG_WIFI_DISCONNECTION: ClassVar[int]
    TAG_WIPE_FAILURE: ClassVar[int]
    def __init__(self) -> None: ...

    class SecurityEvent:
        CREATOR: ClassVar[Any]
        CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
        PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
        def getLogLevel(self) -> int: ...
        def getTimeNanos(self) -> int: ...
        def describeContents(self) -> int: ...
        def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
        def getTag(self) -> int: ...
        def getData(self) -> Any: ...
        def equals(self, p0: Any) -> bool: ...
        def hashCode(self) -> int: ...
        def getId(self) -> int: ...
