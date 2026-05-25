from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator:
    """Forward declaration for ``android.os.Parcelable.Creator``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Parcelable.Creator')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Parcelable/Creator
    """
    ...

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
        CREATOR: ClassVar[Creator]
        def getTimeNanos(self) -> int: ...
        def getTag(self) -> int: ...
        def getData(self) -> Any: ...
        def getId(self) -> int: ...
        def getLogLevel(self) -> int: ...
        def describeContents(self) -> int: ...
        def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
        def equals(self, arg0: Any) -> bool: ...
        def hashCode(self) -> int: ...
