from typing import Any, ClassVar, overload
from android.content.Intent import Intent
from android.os.Bundle import Bundle
from android.os.PersistableBundle import PersistableBundle
from android.os.UserHandle import UserHandle

class UserManager:
    ALLOW_PARENT_PROFILE_APP_LINKING: ClassVar[str]
    DISALLOW_ADD_MANAGED_PROFILE: ClassVar[str]
    DISALLOW_ADD_PRIVATE_PROFILE: ClassVar[str]
    DISALLOW_ADD_USER: ClassVar[str]
    DISALLOW_ADD_WIFI_CONFIG: ClassVar[str]
    DISALLOW_ADJUST_VOLUME: ClassVar[str]
    DISALLOW_AIRPLANE_MODE: ClassVar[str]
    DISALLOW_AMBIENT_DISPLAY: ClassVar[str]
    DISALLOW_APPS_CONTROL: ClassVar[str]
    DISALLOW_ASSIST_CONTENT: ClassVar[str]
    DISALLOW_AUTOFILL: ClassVar[str]
    DISALLOW_BLUETOOTH: ClassVar[str]
    DISALLOW_BLUETOOTH_SHARING: ClassVar[str]
    DISALLOW_CAMERA_TOGGLE: ClassVar[str]
    DISALLOW_CELLULAR_2G: ClassVar[str]
    DISALLOW_CHANGE_WIFI_STATE: ClassVar[str]
    DISALLOW_CONFIG_BLUETOOTH: ClassVar[str]
    DISALLOW_CONFIG_BRIGHTNESS: ClassVar[str]
    DISALLOW_CONFIG_CELL_BROADCASTS: ClassVar[str]
    DISALLOW_CONFIG_CREDENTIALS: ClassVar[str]
    DISALLOW_CONFIG_DATE_TIME: ClassVar[str]
    DISALLOW_CONFIG_DEFAULT_APPS: ClassVar[str]
    DISALLOW_CONFIG_LOCALE: ClassVar[str]
    DISALLOW_CONFIG_LOCATION: ClassVar[str]
    DISALLOW_CONFIG_MOBILE_NETWORKS: ClassVar[str]
    DISALLOW_CONFIG_PRIVATE_DNS: ClassVar[str]
    DISALLOW_CONFIG_SCREEN_TIMEOUT: ClassVar[str]
    DISALLOW_CONFIG_TETHERING: ClassVar[str]
    DISALLOW_CONFIG_VPN: ClassVar[str]
    DISALLOW_CONFIG_WIFI: ClassVar[str]
    DISALLOW_CONTENT_CAPTURE: ClassVar[str]
    DISALLOW_CONTENT_SUGGESTIONS: ClassVar[str]
    DISALLOW_CREATE_WINDOWS: ClassVar[str]
    DISALLOW_CROSS_PROFILE_COPY_PASTE: ClassVar[str]
    DISALLOW_DATA_ROAMING: ClassVar[str]
    DISALLOW_DEBUGGING_FEATURES: ClassVar[str]
    DISALLOW_FACTORY_RESET: ClassVar[str]
    DISALLOW_FUN: ClassVar[str]
    DISALLOW_GRANT_ADMIN: ClassVar[str]
    DISALLOW_INSTALL_APPS: ClassVar[str]
    DISALLOW_INSTALL_UNKNOWN_SOURCES: ClassVar[str]
    DISALLOW_INSTALL_UNKNOWN_SOURCES_GLOBALLY: ClassVar[str]
    DISALLOW_MICROPHONE_TOGGLE: ClassVar[str]
    DISALLOW_MODIFY_ACCOUNTS: ClassVar[str]
    DISALLOW_MOUNT_PHYSICAL_MEDIA: ClassVar[str]
    DISALLOW_NEAR_FIELD_COMMUNICATION_RADIO: ClassVar[str]
    DISALLOW_NETWORK_RESET: ClassVar[str]
    DISALLOW_OUTGOING_BEAM: ClassVar[str]
    DISALLOW_OUTGOING_CALLS: ClassVar[str]
    DISALLOW_PRINTING: ClassVar[str]
    DISALLOW_REMOVE_MANAGED_PROFILE: ClassVar[str]
    DISALLOW_REMOVE_USER: ClassVar[str]
    DISALLOW_SAFE_BOOT: ClassVar[str]
    DISALLOW_SET_USER_ICON: ClassVar[str]
    DISALLOW_SET_WALLPAPER: ClassVar[str]
    DISALLOW_SHARE_INTO_MANAGED_PROFILE: ClassVar[str]
    DISALLOW_SHARE_LOCATION: ClassVar[str]
    DISALLOW_SHARING_ADMIN_CONFIGURED_WIFI: ClassVar[str]
    DISALLOW_SIM_GLOBALLY: ClassVar[str]
    DISALLOW_SMS: ClassVar[str]
    DISALLOW_SYSTEM_ERROR_DIALOGS: ClassVar[str]
    DISALLOW_ULTRA_WIDEBAND_RADIO: ClassVar[str]
    DISALLOW_UNIFIED_PASSWORD: ClassVar[str]
    DISALLOW_UNINSTALL_APPS: ClassVar[str]
    DISALLOW_UNMUTE_MICROPHONE: ClassVar[str]
    DISALLOW_USB_FILE_TRANSFER: ClassVar[str]
    DISALLOW_USER_SWITCH: ClassVar[str]
    DISALLOW_WIFI_DIRECT: ClassVar[str]
    DISALLOW_WIFI_TETHERING: ClassVar[str]
    ENSURE_VERIFY_APPS: ClassVar[str]
    KEY_RESTRICTIONS_PENDING: ClassVar[str]
    QUIET_MODE_DISABLE_ONLY_IF_CREDENTIAL_NOT_REQUIRED: ClassVar[int]
    USER_CREATION_FAILED_NOT_PERMITTED: ClassVar[int]
    USER_CREATION_FAILED_NO_MORE_USERS: ClassVar[int]
    USER_OPERATION_ERROR_CURRENT_USER: ClassVar[int]
    USER_OPERATION_ERROR_LOW_STORAGE: ClassVar[int]
    USER_OPERATION_ERROR_MANAGED_PROFILE: ClassVar[int]
    USER_OPERATION_ERROR_MAX_RUNNING_USERS: ClassVar[int]
    USER_OPERATION_ERROR_MAX_USERS: ClassVar[int]
    USER_OPERATION_ERROR_UNKNOWN: ClassVar[int]
    USER_OPERATION_SUCCESS: ClassVar[int]
    USER_TYPE_PROFILE_CLONE: ClassVar[str]
    USER_TYPE_PROFILE_MANAGED: ClassVar[str]
    USER_TYPE_PROFILE_PRIVATE: ClassVar[str]
    @staticmethod
    def supportsMultipleUsers() -> bool: ...
    @staticmethod
    def isHeadlessSystemUserMode() -> bool: ...
    def getUserName(self) -> str: ...
    def isUserAGoat(self) -> bool: ...
    def isSystemUser(self) -> bool: ...
    def isAdminUser(self) -> bool: ...
    def isDemoUser(self) -> bool: ...
    def isProfile(self) -> bool: ...
    def isManagedProfile(self) -> bool: ...
    def isUserRunning(self, arg0: UserHandle) -> bool: ...
    def isUserRunningOrStopping(self, arg0: UserHandle) -> bool: ...
    def isUserForeground(self) -> bool: ...
    @overload
    def isUserUnlocked(self) -> bool: ...
    @overload
    def isUserUnlocked(self, arg0: UserHandle) -> bool: ...
    @overload
    def getUserRestrictions(self) -> Bundle: ...
    @overload
    def getUserRestrictions(self, arg0: UserHandle) -> Bundle: ...
    @overload
    def setUserRestrictions(self, arg0: Bundle) -> None: ...
    @overload
    def setUserRestrictions(self, arg0: Bundle, arg1: UserHandle) -> None: ...
    def setUserRestriction(self, arg0: str, arg1: bool) -> None: ...
    def hasUserRestriction(self, arg0: str) -> bool: ...
    def getSerialNumberForUser(self, arg0: UserHandle) -> int: ...
    def getUserForSerialNumber(self, arg0: int) -> UserHandle: ...
    @staticmethod
    def createUserCreationIntent(arg0: str, arg1: str, arg2: str, arg3: PersistableBundle) -> Intent: ...
    def getUserCount(self) -> int: ...
    def getUserProfiles(self) -> list: ...
    @overload
    def requestQuietModeEnabled(self, arg0: bool, arg1: UserHandle) -> bool: ...
    @overload
    def requestQuietModeEnabled(self, arg0: bool, arg1: UserHandle, arg2: int) -> bool: ...
    def isQuietModeEnabled(self, arg0: UserHandle) -> bool: ...
    def getApplicationRestrictions(self, arg0: str) -> Bundle: ...
    def setRestrictionsChallenge(self, arg0: str) -> bool: ...
    def getUserCreationTime(self, arg0: UserHandle) -> int: ...

    class UserOperationException:
        def getUserOperationResult(self) -> int: ...
