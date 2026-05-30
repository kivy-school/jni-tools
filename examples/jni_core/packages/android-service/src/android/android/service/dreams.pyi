from typing import Any, ClassVar, overload
from android.content.Intent import Intent
from android.os.IBinder import IBinder
from android.view.ActionMode import ActionMode
from android.view.KeyEvent import KeyEvent
from android.view.Menu import Menu
from android.view.MenuItem import MenuItem
from android.view.MotionEvent import MotionEvent
from android.view.SearchEvent import SearchEvent
from android.view.View import View
from android.view.Window import Window
from android.view.WindowManager import WindowManager
from android.view.accessibility.AccessibilityEvent import AccessibilityEvent

class DreamService:
    DREAM_META_DATA: ClassVar[str]
    SERVICE_INTERFACE: ClassVar[str]
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
    def isInteractive(self) -> bool: ...
    def isScreenBright(self) -> bool: ...
    def onDreamingStarted(self) -> None: ...
    def onDreamingStopped(self) -> None: ...
    def onWakeUp(self) -> None: ...
    def setFullscreen(self, p0: bool) -> None: ...
    def isFullscreen(self) -> bool: ...
    def setInteractive(self, p0: bool) -> None: ...
    def setScreenBright(self, p0: bool) -> None: ...
    def wakeUp(self) -> None: ...
    @overload
    def setContentView(self, p0: View, p1: Any) -> None: ...
    @overload
    def setContentView(self, p0: int) -> None: ...
    @overload
    def setContentView(self, p0: View) -> None: ...
    def onBind(self, p0: Intent) -> IBinder: ...
    def onCreate(self) -> None: ...
    def onDestroy(self) -> None: ...
    def getWindow(self) -> Window: ...
    def getWindowManager(self) -> WindowManager: ...
    def onActionModeFinished(self, p0: ActionMode) -> None: ...
    def onActionModeStarted(self, p0: ActionMode) -> None: ...
    def onCreatePanelMenu(self, p0: int, p1: Menu) -> bool: ...
    def onCreatePanelView(self, p0: int) -> View: ...
    def onMenuItemSelected(self, p0: int, p1: MenuItem) -> bool: ...
    def onMenuOpened(self, p0: int, p1: Menu) -> bool: ...
    def onPanelClosed(self, p0: int, p1: Menu) -> None: ...
    def onPreparePanel(self, p0: int, p1: View, p2: Menu) -> bool: ...
    @overload
    def onSearchRequested(self) -> bool: ...
    @overload
    def onSearchRequested(self, p0: SearchEvent) -> bool: ...
    def onWindowAttributesChanged(self, p0: Any) -> None: ...
    @overload
    def onWindowStartingActionMode(self, p0: Any, p1: int) -> ActionMode: ...
    @overload
    def onWindowStartingActionMode(self, p0: Any) -> ActionMode: ...
    def onWindowFocusChanged(self, p0: bool) -> None: ...
    def requireViewById(self, p0: int) -> View: ...
    def onContentChanged(self) -> None: ...
    def onUnbind(self, p0: Intent) -> bool: ...
    def addContentView(self, p0: View, p1: Any) -> None: ...
    def onAttachedToWindow(self) -> None: ...
    def onDetachedFromWindow(self) -> None: ...
    def dispatchGenericMotionEvent(self, p0: MotionEvent) -> bool: ...
    def dispatchKeyEvent(self, p0: KeyEvent) -> bool: ...
    def dispatchKeyShortcutEvent(self, p0: KeyEvent) -> bool: ...
    def dispatchPopulateAccessibilityEvent(self, p0: AccessibilityEvent) -> bool: ...
    def dispatchTouchEvent(self, p0: MotionEvent) -> bool: ...
    def dispatchTrackballEvent(self, p0: MotionEvent) -> bool: ...
    def findViewById(self, p0: int) -> View: ...
    def finish(self) -> None: ...

