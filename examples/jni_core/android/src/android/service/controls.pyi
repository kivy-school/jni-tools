from typing import Any, ClassVar, overload
from android.app.PendingIntent import PendingIntent
from android.content.res.ColorStateList import ColorStateList
from android.graphics.drawable.Icon import Icon
from android.os.Parcel import Parcel
from android.service.controls.templates.ControlTemplate import ControlTemplate

class Control:
    CREATOR: ClassVar[Any]
    STATUS_DISABLED: ClassVar[int]
    STATUS_ERROR: ClassVar[int]
    STATUS_NOT_FOUND: ClassVar[int]
    STATUS_OK: ClassVar[int]
    STATUS_UNKNOWN: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getStructure(self) -> str: ...
    def getAppIntent(self) -> PendingIntent: ...
    def getControlId(self) -> str: ...
    def getControlTemplate(self) -> ControlTemplate: ...
    def getCustomColor(self) -> ColorStateList: ...
    def getCustomIcon(self) -> Icon: ...
    def getDeviceType(self) -> int: ...
    def getStatusText(self) -> str: ...
    def isAuthRequired(self) -> bool: ...
    def getStatus(self) -> int: ...
    def getZone(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getSubtitle(self) -> str: ...
    def getTitle(self) -> str: ...

    class StatelessBuilder:
        @overload
        def __init__(self, p0: "Control") -> None: ...
        @overload
        def __init__(self, p0: str, p1: PendingIntent) -> None: ...
        def setCustomIcon(self, p0: Icon) -> Any: ...
        def setDeviceType(self, p0: int) -> Any: ...
        def setAppIntent(self, p0: PendingIntent) -> Any: ...
        def setControlId(self, p0: str) -> Any: ...
        def setCustomColor(self, p0: ColorStateList) -> Any: ...
        def setStructure(self, p0: str) -> Any: ...
        def setZone(self, p0: str) -> Any: ...
        def build(self) -> "Control": ...
        def setSubtitle(self, p0: str) -> Any: ...
        def setTitle(self, p0: str) -> Any: ...

    class StatefulBuilder:
        @overload
        def __init__(self, p0: "Control") -> None: ...
        @overload
        def __init__(self, p0: str, p1: PendingIntent) -> None: ...
        def setCustomIcon(self, p0: Icon) -> Any: ...
        def setDeviceType(self, p0: int) -> Any: ...
        def setAppIntent(self, p0: PendingIntent) -> Any: ...
        def setControlId(self, p0: str) -> Any: ...
        def setCustomColor(self, p0: ColorStateList) -> Any: ...
        def setStructure(self, p0: str) -> Any: ...
        def setZone(self, p0: str) -> Any: ...
        def setAuthRequired(self, p0: bool) -> Any: ...
        def setControlTemplate(self, p0: ControlTemplate) -> Any: ...
        def setStatus(self, p0: int) -> Any: ...
        def setStatusText(self, p0: str) -> Any: ...
        def build(self) -> "Control": ...
        def setSubtitle(self, p0: str) -> Any: ...
        def setTitle(self, p0: str) -> Any: ...

from typing import Any, ClassVar, overload

class DeviceTypes:
    TYPE_AC_HEATER: ClassVar[int]
    TYPE_AC_UNIT: ClassVar[int]
    TYPE_AIR_FRESHENER: ClassVar[int]
    TYPE_AIR_PURIFIER: ClassVar[int]
    TYPE_AWNING: ClassVar[int]
    TYPE_BLINDS: ClassVar[int]
    TYPE_CAMERA: ClassVar[int]
    TYPE_CLOSET: ClassVar[int]
    TYPE_COFFEE_MAKER: ClassVar[int]
    TYPE_CURTAIN: ClassVar[int]
    TYPE_DEHUMIDIFIER: ClassVar[int]
    TYPE_DISHWASHER: ClassVar[int]
    TYPE_DISPLAY: ClassVar[int]
    TYPE_DOOR: ClassVar[int]
    TYPE_DOORBELL: ClassVar[int]
    TYPE_DRAWER: ClassVar[int]
    TYPE_DRYER: ClassVar[int]
    TYPE_FAN: ClassVar[int]
    TYPE_GARAGE: ClassVar[int]
    TYPE_GATE: ClassVar[int]
    TYPE_GENERIC_ARM_DISARM: ClassVar[int]
    TYPE_GENERIC_LOCK_UNLOCK: ClassVar[int]
    TYPE_GENERIC_ON_OFF: ClassVar[int]
    TYPE_GENERIC_OPEN_CLOSE: ClassVar[int]
    TYPE_GENERIC_START_STOP: ClassVar[int]
    TYPE_GENERIC_TEMP_SETTING: ClassVar[int]
    TYPE_GENERIC_VIEWSTREAM: ClassVar[int]
    TYPE_HEATER: ClassVar[int]
    TYPE_HOOD: ClassVar[int]
    TYPE_HUMIDIFIER: ClassVar[int]
    TYPE_KETTLE: ClassVar[int]
    TYPE_LIGHT: ClassVar[int]
    TYPE_LOCK: ClassVar[int]
    TYPE_MICROWAVE: ClassVar[int]
    TYPE_MOP: ClassVar[int]
    TYPE_MOWER: ClassVar[int]
    TYPE_MULTICOOKER: ClassVar[int]
    TYPE_OUTLET: ClassVar[int]
    TYPE_PERGOLA: ClassVar[int]
    TYPE_RADIATOR: ClassVar[int]
    TYPE_REFRIGERATOR: ClassVar[int]
    TYPE_REMOTE_CONTROL: ClassVar[int]
    TYPE_ROUTINE: ClassVar[int]
    TYPE_SECURITY_SYSTEM: ClassVar[int]
    TYPE_SET_TOP: ClassVar[int]
    TYPE_SHOWER: ClassVar[int]
    TYPE_SHUTTER: ClassVar[int]
    TYPE_SPRINKLER: ClassVar[int]
    TYPE_STANDMIXER: ClassVar[int]
    TYPE_STYLER: ClassVar[int]
    TYPE_SWITCH: ClassVar[int]
    TYPE_THERMOSTAT: ClassVar[int]
    TYPE_TV: ClassVar[int]
    TYPE_UNKNOWN: ClassVar[int]
    TYPE_VACUUM: ClassVar[int]
    TYPE_VALVE: ClassVar[int]
    TYPE_WASHER: ClassVar[int]
    TYPE_WATER_HEATER: ClassVar[int]
    TYPE_WINDOW: ClassVar[int]
    @staticmethod
    def validDeviceType(p0: int) -> bool: ...

from typing import Any, ClassVar, overload
from android.content.ComponentName import ComponentName
from android.content.Context import Context
from android.content.Intent import Intent
from android.os.IBinder import IBinder
from android.service.controls.Control import Control
from android.service.controls.actions.ControlAction import ControlAction
from java.util.function.Consumer import Consumer

class ControlsProviderService:
    CONTROLS_SURFACE_ACTIVITY_PANEL: ClassVar[int]
    CONTROLS_SURFACE_DREAM: ClassVar[int]
    EXTRA_CONTROLS_SURFACE: ClassVar[str]
    EXTRA_LOCKSCREEN_ALLOW_TRIVIAL_CONTROLS: ClassVar[str]
    META_DATA_PANEL_ACTIVITY: ClassVar[str]
    SERVICE_CONTROLS: ClassVar[str]
    TAG: ClassVar[str]
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
    def createPublisherFor(self, p0: list) -> Any: ...
    def createPublisherForAllAvailable(self) -> Any: ...
    def createPublisherForSuggested(self) -> Any: ...
    def performControlAction(self, p0: str, p1: ControlAction, p2: Consumer) -> None: ...
    @staticmethod
    def requestAddControl(p0: Context, p1: ComponentName, p2: Control) -> None: ...
    def onBind(self, p0: Intent) -> IBinder: ...
    def onUnbind(self, p0: Intent) -> bool: ...

