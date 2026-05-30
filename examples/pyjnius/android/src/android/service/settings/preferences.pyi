from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.service.settings.preferences.SettingsPreferenceMetadata import SettingsPreferenceMetadata
from android.service.settings.preferences.SettingsPreferenceValue import SettingsPreferenceValue

class GetValueResult:
    CREATOR: ClassVar[Any]
    RESULT_DISALLOW: ClassVar[int]
    RESULT_INTERNAL_ERROR: ClassVar[int]
    RESULT_INVALID_REQUEST: ClassVar[int]
    RESULT_OK: ClassVar[int]
    RESULT_REQUIRE_APP_PERMISSION: ClassVar[int]
    RESULT_UNAVAILABLE: ClassVar[int]
    RESULT_UNSUPPORTED: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getResultCode(self) -> int: ...
    def getValue(self) -> SettingsPreferenceValue: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getMetadata(self) -> SettingsPreferenceMetadata: ...

    class Builder:
        def __init__(self, p0: int) -> None: ...
        def setValue(self, p0: SettingsPreferenceValue) -> Any: ...
        def setMetadata(self, p0: SettingsPreferenceMetadata) -> Any: ...
        def build(self) -> "GetValueResult": ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.service.settings.preferences.SettingsPreferenceValue import SettingsPreferenceValue

class SetValueRequest:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getScreenKey(self) -> str: ...
    def getPreferenceKey(self) -> str: ...
    def getPreferenceValue(self) -> SettingsPreferenceValue: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class Builder:
        def __init__(self, p0: str, p1: str, p2: SettingsPreferenceValue) -> None: ...
        def build(self) -> "SetValueRequest": ...

from typing import Any, ClassVar, overload
from android.content.Intent import Intent
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel

class SettingsPreferenceMetadata:
    CREATOR: ClassVar[Any]
    DEEPLINK_ONLY: ClassVar[int]
    EXPECT_POST_CONFIRMATION: ClassVar[int]
    NO_DIRECT_ACCESS: ClassVar[int]
    NO_SENSITIVITY: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getScreenKey(self) -> str: ...
    def getLaunchIntent(self) -> Intent: ...
    def getReadPermissions(self) -> list: ...
    def getSummary(self) -> str: ...
    def getWritePermissions(self) -> list: ...
    def getWriteSensitivity(self) -> int: ...
    def isAvailable(self) -> bool: ...
    def isWritable(self) -> bool: ...
    def isEnabled(self) -> bool: ...
    def getKey(self) -> str: ...
    def isRestricted(self) -> bool: ...
    def getExtras(self) -> Bundle: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getTitle(self) -> str: ...

    class Builder:
        def __init__(self, p0: str, p1: str) -> None: ...
        def setLaunchIntent(self, p0: Intent) -> Any: ...
        def setAvailable(self, p0: bool) -> Any: ...
        def setReadPermissions(self, p0: list) -> Any: ...
        def setRestricted(self, p0: bool) -> Any: ...
        def setSummary(self, p0: str) -> Any: ...
        def setWritePermissions(self, p0: list) -> Any: ...
        def setWriteSensitivity(self, p0: int) -> Any: ...
        def setExtras(self, p0: Bundle) -> Any: ...
        def setEnabled(self, p0: bool) -> Any: ...
        def build(self) -> "SettingsPreferenceMetadata": ...
        def setWritable(self, p0: bool) -> Any: ...
        def setTitle(self, p0: str) -> Any: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class MetadataRequest:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class Builder:
        def __init__(self) -> None: ...
        def build(self) -> "MetadataRequest": ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class GetValueRequest:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getScreenKey(self) -> str: ...
    def getPreferenceKey(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class Builder:
        def __init__(self, p0: str, p1: str) -> None: ...
        def build(self) -> "GetValueRequest": ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class MetadataResult:
    CREATOR: ClassVar[Any]
    RESULT_INTERNAL_ERROR: ClassVar[int]
    RESULT_OK: ClassVar[int]
    RESULT_UNSUPPORTED: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getResultCode(self) -> int: ...
    def getMetadataList(self) -> list: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class Builder:
        def __init__(self, p0: int) -> None: ...
        def setMetadataList(self, p0: list) -> Any: ...
        def build(self) -> "MetadataResult": ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.os.OutcomeReceiver import OutcomeReceiver
from android.service.settings.preferences.GetValueRequest import GetValueRequest
from android.service.settings.preferences.MetadataRequest import MetadataRequest
from android.service.settings.preferences.SetValueRequest import SetValueRequest
from java.util.concurrent.Executor import Executor

class SettingsPreferenceServiceClient:
    def __init__(self, p0: Context, p1: str, p2: Executor, p3: OutcomeReceiver) -> None: ...
    def getAllPreferenceMetadata(self, p0: MetadataRequest, p1: Executor, p2: OutcomeReceiver) -> None: ...
    def setPreferenceValue(self, p0: SetValueRequest, p1: Executor, p2: OutcomeReceiver) -> None: ...
    def getPreferenceValue(self, p0: GetValueRequest, p1: Executor, p2: OutcomeReceiver) -> None: ...
    def close(self) -> None: ...

from typing import Any, ClassVar, overload
from android.content.Intent import Intent
from android.os.IBinder import IBinder
from android.os.OutcomeReceiver import OutcomeReceiver
from android.service.settings.preferences.GetValueRequest import GetValueRequest
from android.service.settings.preferences.MetadataRequest import MetadataRequest
from android.service.settings.preferences.SetValueRequest import SetValueRequest

class SettingsPreferenceService:
    ACTION_PREFERENCE_SERVICE: ClassVar[str]
    START_CONTINUATION_MASK: ClassVar[int]
    START_FLAG_REDELIVERY: ClassVar[int]
    START_FLAG_RETRY: ClassVar[int]
    START_NOT_STICKY: ClassVar[int]
    START_REDELIVER_INTENT: ClassVar[int]
    START_STICKY: ClassVar[int]
    START_STICKY_COMPATIBILITY: ClassVar[int]
    STOP_FOREGROUND_DETACH: ClassVar[int]
    STOP_FOREGROUND_LEGACY: ClassVar[int]
    STOP_FOREGROUND_REMOVE: ClassVar[int]
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
    def onGetAllPreferenceMetadata(self, p0: MetadataRequest, p1: OutcomeReceiver) -> None: ...
    def onGetPreferenceValue(self, p0: GetValueRequest, p1: OutcomeReceiver) -> None: ...
    def onSetPreferenceValue(self, p0: SetValueRequest, p1: OutcomeReceiver) -> None: ...
    def onBind(self, p0: Intent) -> IBinder: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class SetValueResult:
    CREATOR: ClassVar[Any]
    RESULT_DISABLED: ClassVar[int]
    RESULT_DISALLOW: ClassVar[int]
    RESULT_INTERNAL_ERROR: ClassVar[int]
    RESULT_INVALID_REQUEST: ClassVar[int]
    RESULT_OK: ClassVar[int]
    RESULT_REQUIRE_APP_PERMISSION: ClassVar[int]
    RESULT_REQUIRE_USER_CONSENT: ClassVar[int]
    RESULT_RESTRICTED: ClassVar[int]
    RESULT_UNAVAILABLE: ClassVar[int]
    RESULT_UNSUPPORTED: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getResultCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class Builder:
        def __init__(self, p0: int) -> None: ...
        def build(self) -> "SetValueResult": ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class SettingsPreferenceValue:
    CREATOR: ClassVar[Any]
    TYPE_BOOLEAN: ClassVar[int]
    TYPE_DOUBLE: ClassVar[int]
    TYPE_INT: ClassVar[int]
    TYPE_LONG: ClassVar[int]
    TYPE_STRING: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getBooleanValue(self) -> bool: ...
    def getDoubleValue(self) -> float: ...
    def getLongValue(self) -> int: ...
    def getStringValue(self) -> str: ...
    def getType(self) -> int: ...
    def getIntValue(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class Builder:
        def __init__(self, p0: int) -> None: ...
        def setBooleanValue(self, p0: bool) -> Any: ...
        def setDoubleValue(self, p0: float) -> Any: ...
        def setLongValue(self, p0: int) -> Any: ...
        def setStringValue(self, p0: str) -> Any: ...
        def setIntValue(self, p0: int) -> Any: ...
        def build(self) -> "SettingsPreferenceValue": ...

