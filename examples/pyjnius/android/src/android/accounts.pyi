from typing import Any, ClassVar, overload
from java.lang.Throwable import Throwable

class OperationCanceledException:
    @overload
    def __init__(self, p0: Throwable) -> None: ...
    @overload
    def __init__(self, p0: str, p1: Throwable) -> None: ...
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self) -> None: ...

from typing import Any, ClassVar, overload
from android.accounts.Account import Account
from android.accounts.AccountManagerCallback import AccountManagerCallback
from android.accounts.AccountManagerFuture import AccountManagerFuture
from android.accounts.OnAccountsUpdateListener import OnAccountsUpdateListener
from android.app.Activity import Activity
from android.content.Context import Context
from android.content.Intent import Intent
from android.os.Bundle import Bundle
from android.os.Handler import Handler

class AccountManager:
    ACTION_ACCOUNT_REMOVED: ClassVar[str]
    ACTION_AUTHENTICATOR_INTENT: ClassVar[str]
    AUTHENTICATOR_ATTRIBUTES_NAME: ClassVar[str]
    AUTHENTICATOR_META_DATA_NAME: ClassVar[str]
    ERROR_CODE_BAD_ARGUMENTS: ClassVar[int]
    ERROR_CODE_BAD_AUTHENTICATION: ClassVar[int]
    ERROR_CODE_BAD_REQUEST: ClassVar[int]
    ERROR_CODE_CANCELED: ClassVar[int]
    ERROR_CODE_INVALID_RESPONSE: ClassVar[int]
    ERROR_CODE_NETWORK_ERROR: ClassVar[int]
    ERROR_CODE_REMOTE_EXCEPTION: ClassVar[int]
    ERROR_CODE_UNSUPPORTED_OPERATION: ClassVar[int]
    KEY_ACCOUNTS: ClassVar[str]
    KEY_ACCOUNT_AUTHENTICATOR_RESPONSE: ClassVar[str]
    KEY_ACCOUNT_MANAGER_RESPONSE: ClassVar[str]
    KEY_ACCOUNT_NAME: ClassVar[str]
    KEY_ACCOUNT_SESSION_BUNDLE: ClassVar[str]
    KEY_ACCOUNT_STATUS_TOKEN: ClassVar[str]
    KEY_ACCOUNT_TYPE: ClassVar[str]
    KEY_ANDROID_PACKAGE_NAME: ClassVar[str]
    KEY_AUTHENTICATOR_TYPES: ClassVar[str]
    KEY_AUTHTOKEN: ClassVar[str]
    KEY_AUTH_FAILED_MESSAGE: ClassVar[str]
    KEY_AUTH_TOKEN_LABEL: ClassVar[str]
    KEY_BOOLEAN_RESULT: ClassVar[str]
    KEY_CALLER_PID: ClassVar[str]
    KEY_CALLER_UID: ClassVar[str]
    KEY_ERROR_CODE: ClassVar[str]
    KEY_ERROR_MESSAGE: ClassVar[str]
    KEY_INTENT: ClassVar[str]
    KEY_LAST_AUTHENTICATED_TIME: ClassVar[str]
    KEY_PASSWORD: ClassVar[str]
    KEY_USERDATA: ClassVar[str]
    LOGIN_ACCOUNTS_CHANGED_ACTION: ClassVar[str]
    PACKAGE_NAME_KEY_LEGACY_NOT_VISIBLE: ClassVar[str]
    PACKAGE_NAME_KEY_LEGACY_VISIBLE: ClassVar[str]
    VISIBILITY_NOT_VISIBLE: ClassVar[int]
    VISIBILITY_UNDEFINED: ClassVar[int]
    VISIBILITY_USER_MANAGED_NOT_VISIBLE: ClassVar[int]
    VISIBILITY_USER_MANAGED_VISIBLE: ClassVar[int]
    VISIBILITY_VISIBLE: ClassVar[int]
    def getUserData(self, p0: Account, p1: str) -> str: ...
    def setUserData(self, p0: Account, p1: str, p2: str) -> None: ...
    def getPassword(self, p0: Account) -> str: ...
    def addAccount(self, p0: str, p1: str, p2: Any, p3: Bundle, p4: Activity, p5: AccountManagerCallback, p6: Handler) -> AccountManagerFuture: ...
    @overload
    def addAccountExplicitly(self, p0: Account, p1: str, p2: Bundle) -> bool: ...
    @overload
    def addAccountExplicitly(self, p0: Account, p1: str, p2: Bundle, p3: dict) -> bool: ...
    @overload
    def addOnAccountsUpdatedListener(self, p0: OnAccountsUpdateListener, p1: Handler, p2: bool) -> None: ...
    @overload
    def addOnAccountsUpdatedListener(self, p0: OnAccountsUpdateListener, p1: Handler, p2: bool, p3: Any) -> None: ...
    def blockingGetAuthToken(self, p0: Account, p1: str, p2: bool) -> str: ...
    def clearPassword(self, p0: Account) -> None: ...
    def confirmCredentials(self, p0: Account, p1: Bundle, p2: Activity, p3: AccountManagerCallback, p4: Handler) -> AccountManagerFuture: ...
    def editProperties(self, p0: str, p1: Activity, p2: AccountManagerCallback, p3: Handler) -> AccountManagerFuture: ...
    def finishSession(self, p0: Bundle, p1: Activity, p2: AccountManagerCallback, p3: Handler) -> AccountManagerFuture: ...
    def getAccountVisibility(self, p0: Account, p1: str) -> int: ...
    def getAccounts(self) -> Any: ...
    def getAccountsAndVisibilityForPackage(self, p0: str, p1: str) -> dict: ...
    def getAccountsByType(self, p0: str) -> Any: ...
    def getAccountsByTypeAndFeatures(self, p0: str, p1: Any, p2: AccountManagerCallback, p3: Handler) -> AccountManagerFuture: ...
    def getAccountsByTypeForPackage(self, p0: str, p1: str) -> Any: ...
    @overload
    def getAuthToken(self, p0: Account, p1: str, p2: Bundle, p3: Activity, p4: AccountManagerCallback, p5: Handler) -> AccountManagerFuture: ...
    @overload
    def getAuthToken(self, p0: Account, p1: str, p2: bool, p3: AccountManagerCallback, p4: Handler) -> AccountManagerFuture: ...
    @overload
    def getAuthToken(self, p0: Account, p1: str, p2: Bundle, p3: bool, p4: AccountManagerCallback, p5: Handler) -> AccountManagerFuture: ...
    def getAuthTokenByFeatures(self, p0: str, p1: str, p2: Any, p3: Activity, p4: Bundle, p5: Bundle, p6: AccountManagerCallback, p7: Handler) -> AccountManagerFuture: ...
    def getAuthenticatorTypes(self) -> Any: ...
    def getPackagesAndVisibilityForAccount(self, p0: Account) -> dict: ...
    def getPreviousName(self, p0: Account) -> str: ...
    def hasFeatures(self, p0: Account, p1: Any, p2: AccountManagerCallback, p3: Handler) -> AccountManagerFuture: ...
    def invalidateAuthToken(self, p0: str, p1: str) -> None: ...
    def isCredentialsUpdateSuggested(self, p0: Account, p1: str, p2: AccountManagerCallback, p3: Handler) -> AccountManagerFuture: ...
    @overload
    @staticmethod
    def newChooseAccountIntent(p0: Account, p1: list, p2: Any, p3: str, p4: str, p5: Any, p6: Bundle) -> Intent: ...
    @overload
    @staticmethod
    def newChooseAccountIntent(p0: Account, p1: list, p2: Any, p3: bool, p4: str, p5: str, p6: Any, p7: Bundle) -> Intent: ...
    def notifyAccountAuthenticated(self, p0: Account) -> bool: ...
    def peekAuthToken(self, p0: Account, p1: str) -> str: ...
    @overload
    def removeAccount(self, p0: Account, p1: Activity, p2: AccountManagerCallback, p3: Handler) -> AccountManagerFuture: ...
    @overload
    def removeAccount(self, p0: Account, p1: AccountManagerCallback, p2: Handler) -> AccountManagerFuture: ...
    def removeAccountExplicitly(self, p0: Account) -> bool: ...
    def removeOnAccountsUpdatedListener(self, p0: OnAccountsUpdateListener) -> None: ...
    def renameAccount(self, p0: Account, p1: str, p2: AccountManagerCallback, p3: Handler) -> AccountManagerFuture: ...
    def setAccountVisibility(self, p0: Account, p1: str, p2: int) -> bool: ...
    def setAuthToken(self, p0: Account, p1: str, p2: str) -> None: ...
    def startAddAccountSession(self, p0: str, p1: str, p2: Any, p3: Bundle, p4: Activity, p5: AccountManagerCallback, p6: Handler) -> AccountManagerFuture: ...
    def startUpdateCredentialsSession(self, p0: Account, p1: str, p2: Bundle, p3: Activity, p4: AccountManagerCallback, p5: Handler) -> AccountManagerFuture: ...
    def updateCredentials(self, p0: Account, p1: str, p2: Bundle, p3: Activity, p4: AccountManagerCallback, p5: Handler) -> AccountManagerFuture: ...
    @staticmethod
    def get(p0: Context) -> "AccountManager": ...
    def setPassword(self, p0: Account, p1: str) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class Account:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    name: str
    type: str
    @overload
    def __init__(self, p0: Parcel) -> None: ...
    @overload
    def __init__(self, p0: str, p1: str) -> None: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from java.lang.Throwable import Throwable

class AccountsException:
    @overload
    def __init__(self, p0: Throwable) -> None: ...
    @overload
    def __init__(self, p0: str, p1: Throwable) -> None: ...
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self) -> None: ...

from typing import Any, ClassVar, overload
from android.accounts.AccountManagerFuture import AccountManagerFuture

class AccountManagerCallback:
    def run(self, p0: AccountManagerFuture) -> None: ...

from typing import Any, ClassVar, overload
from android.accounts.Account import Account
from android.accounts.AccountAuthenticatorResponse import AccountAuthenticatorResponse
from android.content.Context import Context
from android.os.Bundle import Bundle
from android.os.IBinder import IBinder

class AbstractAccountAuthenticator:
    KEY_CUSTOM_TOKEN_EXPIRY: ClassVar[str]
    def __init__(self, p0: Context) -> None: ...
    def addAccount(self, p0: AccountAuthenticatorResponse, p1: str, p2: str, p3: Any, p4: Bundle) -> Bundle: ...
    def confirmCredentials(self, p0: AccountAuthenticatorResponse, p1: Account, p2: Bundle) -> Bundle: ...
    def editProperties(self, p0: AccountAuthenticatorResponse, p1: str) -> Bundle: ...
    def finishSession(self, p0: AccountAuthenticatorResponse, p1: str, p2: Bundle) -> Bundle: ...
    def getAuthToken(self, p0: AccountAuthenticatorResponse, p1: Account, p2: str, p3: Bundle) -> Bundle: ...
    def hasFeatures(self, p0: AccountAuthenticatorResponse, p1: Account, p2: Any) -> Bundle: ...
    def isCredentialsUpdateSuggested(self, p0: AccountAuthenticatorResponse, p1: Account, p2: str) -> Bundle: ...
    def startAddAccountSession(self, p0: AccountAuthenticatorResponse, p1: str, p2: str, p3: Any, p4: Bundle) -> Bundle: ...
    def startUpdateCredentialsSession(self, p0: AccountAuthenticatorResponse, p1: Account, p2: str, p3: Bundle) -> Bundle: ...
    def updateCredentials(self, p0: AccountAuthenticatorResponse, p1: Account, p2: str, p3: Bundle) -> Bundle: ...
    def addAccountFromCredentials(self, p0: AccountAuthenticatorResponse, p1: Account, p2: Bundle) -> Bundle: ...
    def getIBinder(self) -> IBinder: ...
    def getAccountCredentialsForCloning(self, p0: AccountAuthenticatorResponse, p1: Account) -> Bundle: ...
    def getAccountRemovalAllowed(self, p0: AccountAuthenticatorResponse, p1: Account) -> Bundle: ...
    def getAuthTokenLabel(self, p0: str) -> str: ...

from typing import Any, ClassVar, overload
from java.util.concurrent.TimeUnit import TimeUnit

class AccountManagerFuture:
    def isCancelled(self) -> bool: ...
    def isDone(self) -> bool: ...
    def cancel(self, p0: bool) -> bool: ...
    @overload
    def getResult(self) -> Any: ...
    @overload
    def getResult(self, p0: int, p1: TimeUnit) -> Any: ...

from typing import Any, ClassVar, overload
from java.lang.Throwable import Throwable

class NetworkErrorException:
    @overload
    def __init__(self, p0: Throwable) -> None: ...
    @overload
    def __init__(self, p0: str, p1: Throwable) -> None: ...
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle

class AccountAuthenticatorActivity:
    DEFAULT_KEYS_DIALER: ClassVar[int]
    DEFAULT_KEYS_DISABLE: ClassVar[int]
    DEFAULT_KEYS_SEARCH_GLOBAL: ClassVar[int]
    DEFAULT_KEYS_SEARCH_LOCAL: ClassVar[int]
    DEFAULT_KEYS_SHORTCUT: ClassVar[int]
    FULLSCREEN_MODE_REQUEST_ENTER: ClassVar[int]
    FULLSCREEN_MODE_REQUEST_EXIT: ClassVar[int]
    OVERRIDE_TRANSITION_CLOSE: ClassVar[int]
    OVERRIDE_TRANSITION_OPEN: ClassVar[int]
    RESULT_CANCELED: ClassVar[int]
    RESULT_FIRST_USER: ClassVar[int]
    RESULT_OK: ClassVar[int]
    TRIM_MEMORY_BACKGROUND: ClassVar[int]
    TRIM_MEMORY_COMPLETE: ClassVar[int]
    TRIM_MEMORY_MODERATE: ClassVar[int]
    TRIM_MEMORY_RUNNING_CRITICAL: ClassVar[int]
    TRIM_MEMORY_RUNNING_LOW: ClassVar[int]
    TRIM_MEMORY_RUNNING_MODERATE: ClassVar[int]
    TRIM_MEMORY_UI_HIDDEN: ClassVar[int]
    ACCESSIBILITY_SERVICE: ClassVar[str]
    ACCOUNT_SERVICE: ClassVar[str]
    ACTIVITY_SERVICE: ClassVar[str]
    ADVANCED_PROTECTION_SERVICE: ClassVar[str]
    ALARM_SERVICE: ClassVar[str]
    APPWIDGET_SERVICE: ClassVar[str]
    APP_FUNCTION_SERVICE: ClassVar[str]
    APP_OPS_SERVICE: ClassVar[str]
    APP_SEARCH_SERVICE: ClassVar[str]
    AUDIO_SERVICE: ClassVar[str]
    BATTERY_SERVICE: ClassVar[str]
    BIND_ABOVE_CLIENT: ClassVar[int]
    BIND_ADJUST_WITH_ACTIVITY: ClassVar[int]
    BIND_ALLOW_ACTIVITY_STARTS: ClassVar[int]
    BIND_ALLOW_OOM_MANAGEMENT: ClassVar[int]
    BIND_AUTO_CREATE: ClassVar[int]
    BIND_DEBUG_UNBIND: ClassVar[int]
    BIND_EXTERNAL_SERVICE: ClassVar[int]
    BIND_EXTERNAL_SERVICE_LONG: ClassVar[int]
    BIND_IMPORTANT: ClassVar[int]
    BIND_INCLUDE_CAPABILITIES: ClassVar[int]
    BIND_NOT_FOREGROUND: ClassVar[int]
    BIND_NOT_PERCEPTIBLE: ClassVar[int]
    BIND_PACKAGE_ISOLATED_PROCESS: ClassVar[int]
    BIND_SHARED_ISOLATED_PROCESS: ClassVar[int]
    BIND_WAIVE_PRIORITY: ClassVar[int]
    BIOMETRIC_SERVICE: ClassVar[str]
    BLOB_STORE_SERVICE: ClassVar[str]
    BLUETOOTH_SERVICE: ClassVar[str]
    BUGREPORT_SERVICE: ClassVar[str]
    CAMERA_SERVICE: ClassVar[str]
    CAPTIONING_SERVICE: ClassVar[str]
    CARRIER_CONFIG_SERVICE: ClassVar[str]
    CLIPBOARD_SERVICE: ClassVar[str]
    COMPANION_DEVICE_SERVICE: ClassVar[str]
    CONNECTIVITY_DIAGNOSTICS_SERVICE: ClassVar[str]
    CONNECTIVITY_SERVICE: ClassVar[str]
    CONSUMER_IR_SERVICE: ClassVar[str]
    CONTACT_KEYS_SERVICE: ClassVar[str]
    CONTEXT_IGNORE_SECURITY: ClassVar[int]
    CONTEXT_INCLUDE_CODE: ClassVar[int]
    CONTEXT_RESTRICTED: ClassVar[int]
    CREDENTIAL_SERVICE: ClassVar[str]
    CROSS_PROFILE_APPS_SERVICE: ClassVar[str]
    DEVICE_ID_DEFAULT: ClassVar[int]
    DEVICE_ID_INVALID: ClassVar[int]
    DEVICE_LOCK_SERVICE: ClassVar[str]
    DEVICE_POLICY_SERVICE: ClassVar[str]
    DISPLAY_HASH_SERVICE: ClassVar[str]
    DISPLAY_SERVICE: ClassVar[str]
    DOMAIN_VERIFICATION_SERVICE: ClassVar[str]
    DOWNLOAD_SERVICE: ClassVar[str]
    DROPBOX_SERVICE: ClassVar[str]
    EUICC_SERVICE: ClassVar[str]
    FILE_INTEGRITY_SERVICE: ClassVar[str]
    FINGERPRINT_SERVICE: ClassVar[str]
    GAME_SERVICE: ClassVar[str]
    GRAMMATICAL_INFLECTION_SERVICE: ClassVar[str]
    HARDWARE_PROPERTIES_SERVICE: ClassVar[str]
    HEALTHCONNECT_SERVICE: ClassVar[str]
    INPUT_METHOD_SERVICE: ClassVar[str]
    INPUT_SERVICE: ClassVar[str]
    IPSEC_SERVICE: ClassVar[str]
    JOB_SCHEDULER_SERVICE: ClassVar[str]
    KEYGUARD_SERVICE: ClassVar[str]
    KEYSTORE_SERVICE: ClassVar[str]
    LAUNCHER_APPS_SERVICE: ClassVar[str]
    LAYOUT_INFLATER_SERVICE: ClassVar[str]
    LOCALE_SERVICE: ClassVar[str]
    LOCATION_SERVICE: ClassVar[str]
    MEDIA_COMMUNICATION_SERVICE: ClassVar[str]
    MEDIA_METRICS_SERVICE: ClassVar[str]
    MEDIA_PROJECTION_SERVICE: ClassVar[str]
    MEDIA_QUALITY_SERVICE: ClassVar[str]
    MEDIA_ROUTER_SERVICE: ClassVar[str]
    MEDIA_SESSION_SERVICE: ClassVar[str]
    MIDI_SERVICE: ClassVar[str]
    MODE_APPEND: ClassVar[int]
    MODE_ENABLE_WRITE_AHEAD_LOGGING: ClassVar[int]
    MODE_MULTI_PROCESS: ClassVar[int]
    MODE_NO_LOCALIZED_COLLATORS: ClassVar[int]
    MODE_PRIVATE: ClassVar[int]
    MODE_WORLD_READABLE: ClassVar[int]
    MODE_WORLD_WRITEABLE: ClassVar[int]
    NETWORK_STATS_SERVICE: ClassVar[str]
    NFC_SERVICE: ClassVar[str]
    NOTIFICATION_SERVICE: ClassVar[str]
    NSD_SERVICE: ClassVar[str]
    OVERLAY_SERVICE: ClassVar[str]
    PEOPLE_SERVICE: ClassVar[str]
    PERFORMANCE_HINT_SERVICE: ClassVar[str]
    PERSISTENT_DATA_BLOCK_SERVICE: ClassVar[str]
    POWER_SERVICE: ClassVar[str]
    PRINT_SERVICE: ClassVar[str]
    PROFILING_SERVICE: ClassVar[str]
    RECEIVER_EXPORTED: ClassVar[int]
    RECEIVER_NOT_EXPORTED: ClassVar[int]
    RECEIVER_VISIBLE_TO_INSTANT_APPS: ClassVar[int]
    RESTRICTIONS_SERVICE: ClassVar[str]
    ROLE_SERVICE: ClassVar[str]
    SATELLITE_SERVICE: ClassVar[str]
    SEARCH_SERVICE: ClassVar[str]
    SECURITY_STATE_SERVICE: ClassVar[str]
    SENSOR_SERVICE: ClassVar[str]
    SHORTCUT_SERVICE: ClassVar[str]
    STATUS_BAR_SERVICE: ClassVar[str]
    STORAGE_SERVICE: ClassVar[str]
    STORAGE_STATS_SERVICE: ClassVar[str]
    SYSTEM_HEALTH_SERVICE: ClassVar[str]
    TELECOM_SERVICE: ClassVar[str]
    TELEPHONY_IMS_SERVICE: ClassVar[str]
    TELEPHONY_SERVICE: ClassVar[str]
    TELEPHONY_SUBSCRIPTION_SERVICE: ClassVar[str]
    TETHERING_SERVICE: ClassVar[str]
    TEXT_CLASSIFICATION_SERVICE: ClassVar[str]
    TEXT_SERVICES_MANAGER_SERVICE: ClassVar[str]
    TV_AD_SERVICE: ClassVar[str]
    TV_INPUT_SERVICE: ClassVar[str]
    TV_INTERACTIVE_APP_SERVICE: ClassVar[str]
    UI_MODE_SERVICE: ClassVar[str]
    USAGE_STATS_SERVICE: ClassVar[str]
    USB_SERVICE: ClassVar[str]
    USER_SERVICE: ClassVar[str]
    VIBRATOR_MANAGER_SERVICE: ClassVar[str]
    VIBRATOR_SERVICE: ClassVar[str]
    VIRTUAL_DEVICE_SERVICE: ClassVar[str]
    VPN_MANAGEMENT_SERVICE: ClassVar[str]
    WALLPAPER_SERVICE: ClassVar[str]
    WIFI_AWARE_SERVICE: ClassVar[str]
    WIFI_P2P_SERVICE: ClassVar[str]
    WIFI_RTT_RANGING_SERVICE: ClassVar[str]
    WIFI_SERVICE: ClassVar[str]
    WINDOW_SERVICE: ClassVar[str]
    def __init__(self) -> None: ...
    def setAccountAuthenticatorResult(self, p0: Bundle) -> None: ...
    def finish(self) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class AuthenticatorDescription:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    accountPreferencesId: int
    customTokens: bool
    iconId: int
    labelId: int
    packageName: str
    smallIconId: int
    type: str
    @overload
    def __init__(self, p0: str, p1: str, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @overload
    def __init__(self, p0: str, p1: str, p2: int, p3: int, p4: int, p5: int, p6: bool) -> None: ...
    @staticmethod
    def newKey(p0: str) -> "AuthenticatorDescription": ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload

class OnAccountsUpdateListener:
    def onAccountsUpdated(self, p0: Any) -> None: ...

from typing import Any, ClassVar, overload
from java.lang.Throwable import Throwable

class AuthenticatorException:
    @overload
    def __init__(self, p0: Throwable) -> None: ...
    @overload
    def __init__(self, p0: str, p1: Throwable) -> None: ...
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel

class AccountAuthenticatorResponse:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: Parcel) -> None: ...
    def onRequestContinued(self) -> None: ...
    def onError(self, p0: int, p1: str) -> None: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def onResult(self, p0: Bundle) -> None: ...

