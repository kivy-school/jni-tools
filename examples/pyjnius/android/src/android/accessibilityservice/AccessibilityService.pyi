from typing import Any, ClassVar, overload
from android.accessibilityservice.AccessibilityButtonController import AccessibilityButtonController
from android.accessibilityservice.AccessibilityGestureEvent import AccessibilityGestureEvent
from android.accessibilityservice.AccessibilityServiceInfo import AccessibilityServiceInfo
from android.accessibilityservice.BrailleDisplayController import BrailleDisplayController
from android.accessibilityservice.FingerprintGestureController import FingerprintGestureController
from android.accessibilityservice.GestureDescription import GestureDescription
from android.accessibilityservice.InputMethod import InputMethod
from android.accessibilityservice.MagnificationConfig import MagnificationConfig
from android.accessibilityservice.TouchInteractionController import TouchInteractionController
from android.content.Context import Context
from android.content.Intent import Intent
from android.graphics.ColorSpace import ColorSpace
from android.graphics.Region import Region
from android.hardware.HardwareBuffer import HardwareBuffer
from android.os.Bundle import Bundle
from android.os.Handler import Handler
from android.os.IBinder import IBinder
from android.util.SparseArray import SparseArray
from android.view.Display import Display
from android.view.MotionEvent import MotionEvent
from android.view.SurfaceControl import SurfaceControl
from android.view.accessibility.AccessibilityEvent import AccessibilityEvent
from android.view.accessibility.AccessibilityNodeInfo import AccessibilityNodeInfo
from java.util.concurrent.Executor import Executor

class AccessibilityService:
    ERROR_TAKE_SCREENSHOT_INTERNAL_ERROR: ClassVar[int]
    ERROR_TAKE_SCREENSHOT_INTERVAL_TIME_SHORT: ClassVar[int]
    ERROR_TAKE_SCREENSHOT_INVALID_DISPLAY: ClassVar[int]
    ERROR_TAKE_SCREENSHOT_INVALID_WINDOW: ClassVar[int]
    ERROR_TAKE_SCREENSHOT_NO_ACCESSIBILITY_ACCESS: ClassVar[int]
    ERROR_TAKE_SCREENSHOT_SECURE_WINDOW: ClassVar[int]
    GESTURE_2_FINGER_DOUBLE_TAP: ClassVar[int]
    GESTURE_2_FINGER_DOUBLE_TAP_AND_HOLD: ClassVar[int]
    GESTURE_2_FINGER_SINGLE_TAP: ClassVar[int]
    GESTURE_2_FINGER_SWIPE_DOWN: ClassVar[int]
    GESTURE_2_FINGER_SWIPE_LEFT: ClassVar[int]
    GESTURE_2_FINGER_SWIPE_RIGHT: ClassVar[int]
    GESTURE_2_FINGER_SWIPE_UP: ClassVar[int]
    GESTURE_2_FINGER_TRIPLE_TAP: ClassVar[int]
    GESTURE_2_FINGER_TRIPLE_TAP_AND_HOLD: ClassVar[int]
    GESTURE_3_FINGER_DOUBLE_TAP: ClassVar[int]
    GESTURE_3_FINGER_DOUBLE_TAP_AND_HOLD: ClassVar[int]
    GESTURE_3_FINGER_SINGLE_TAP: ClassVar[int]
    GESTURE_3_FINGER_SINGLE_TAP_AND_HOLD: ClassVar[int]
    GESTURE_3_FINGER_SWIPE_DOWN: ClassVar[int]
    GESTURE_3_FINGER_SWIPE_LEFT: ClassVar[int]
    GESTURE_3_FINGER_SWIPE_RIGHT: ClassVar[int]
    GESTURE_3_FINGER_SWIPE_UP: ClassVar[int]
    GESTURE_3_FINGER_TRIPLE_TAP: ClassVar[int]
    GESTURE_3_FINGER_TRIPLE_TAP_AND_HOLD: ClassVar[int]
    GESTURE_4_FINGER_DOUBLE_TAP: ClassVar[int]
    GESTURE_4_FINGER_DOUBLE_TAP_AND_HOLD: ClassVar[int]
    GESTURE_4_FINGER_SINGLE_TAP: ClassVar[int]
    GESTURE_4_FINGER_SWIPE_DOWN: ClassVar[int]
    GESTURE_4_FINGER_SWIPE_LEFT: ClassVar[int]
    GESTURE_4_FINGER_SWIPE_RIGHT: ClassVar[int]
    GESTURE_4_FINGER_SWIPE_UP: ClassVar[int]
    GESTURE_4_FINGER_TRIPLE_TAP: ClassVar[int]
    GESTURE_DOUBLE_TAP: ClassVar[int]
    GESTURE_DOUBLE_TAP_AND_HOLD: ClassVar[int]
    GESTURE_SWIPE_DOWN: ClassVar[int]
    GESTURE_SWIPE_DOWN_AND_LEFT: ClassVar[int]
    GESTURE_SWIPE_DOWN_AND_RIGHT: ClassVar[int]
    GESTURE_SWIPE_DOWN_AND_UP: ClassVar[int]
    GESTURE_SWIPE_LEFT: ClassVar[int]
    GESTURE_SWIPE_LEFT_AND_DOWN: ClassVar[int]
    GESTURE_SWIPE_LEFT_AND_RIGHT: ClassVar[int]
    GESTURE_SWIPE_LEFT_AND_UP: ClassVar[int]
    GESTURE_SWIPE_RIGHT: ClassVar[int]
    GESTURE_SWIPE_RIGHT_AND_DOWN: ClassVar[int]
    GESTURE_SWIPE_RIGHT_AND_LEFT: ClassVar[int]
    GESTURE_SWIPE_RIGHT_AND_UP: ClassVar[int]
    GESTURE_SWIPE_UP: ClassVar[int]
    GESTURE_SWIPE_UP_AND_DOWN: ClassVar[int]
    GESTURE_SWIPE_UP_AND_LEFT: ClassVar[int]
    GESTURE_SWIPE_UP_AND_RIGHT: ClassVar[int]
    GESTURE_UNKNOWN: ClassVar[int]
    GLOBAL_ACTION_ACCESSIBILITY_ALL_APPS: ClassVar[int]
    GLOBAL_ACTION_ACCESSIBILITY_BUTTON: ClassVar[int]
    GLOBAL_ACTION_ACCESSIBILITY_BUTTON_CHOOSER: ClassVar[int]
    GLOBAL_ACTION_ACCESSIBILITY_SHORTCUT: ClassVar[int]
    GLOBAL_ACTION_BACK: ClassVar[int]
    GLOBAL_ACTION_DISMISS_NOTIFICATION_SHADE: ClassVar[int]
    GLOBAL_ACTION_DPAD_CENTER: ClassVar[int]
    GLOBAL_ACTION_DPAD_DOWN: ClassVar[int]
    GLOBAL_ACTION_DPAD_LEFT: ClassVar[int]
    GLOBAL_ACTION_DPAD_RIGHT: ClassVar[int]
    GLOBAL_ACTION_DPAD_UP: ClassVar[int]
    GLOBAL_ACTION_HOME: ClassVar[int]
    GLOBAL_ACTION_KEYCODE_HEADSETHOOK: ClassVar[int]
    GLOBAL_ACTION_LOCK_SCREEN: ClassVar[int]
    GLOBAL_ACTION_MEDIA_PLAY_PAUSE: ClassVar[int]
    GLOBAL_ACTION_MENU: ClassVar[int]
    GLOBAL_ACTION_NOTIFICATIONS: ClassVar[int]
    GLOBAL_ACTION_POWER_DIALOG: ClassVar[int]
    GLOBAL_ACTION_QUICK_SETTINGS: ClassVar[int]
    GLOBAL_ACTION_RECENTS: ClassVar[int]
    GLOBAL_ACTION_TAKE_SCREENSHOT: ClassVar[int]
    GLOBAL_ACTION_TOGGLE_SPLIT_SCREEN: ClassVar[int]
    SERVICE_INTERFACE: ClassVar[str]
    SERVICE_META_DATA: ClassVar[str]
    SHOW_MODE_AUTO: ClassVar[int]
    SHOW_MODE_HIDDEN: ClassVar[int]
    SHOW_MODE_IGNORE_HARD_KEYBOARD: ClassVar[int]
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
    def onAccessibilityEvent(self, p0: AccessibilityEvent) -> None: ...
    def onMotionEvent(self, p0: MotionEvent) -> None: ...
    def attachAccessibilityOverlayToDisplay(self, p0: int, p1: SurfaceControl) -> None: ...
    def attachAccessibilityOverlayToWindow(self, p0: int, p1: SurfaceControl) -> None: ...
    def clearCachedSubtree(self, p0: AccessibilityNodeInfo) -> bool: ...
    def disableSelf(self) -> None: ...
    def dispatchGesture(self, p0: GestureDescription, p1: Any, p2: Handler) -> bool: ...
    @overload
    def getAccessibilityButtonController(self) -> AccessibilityButtonController: ...
    @overload
    def getAccessibilityButtonController(self, p0: int) -> AccessibilityButtonController: ...
    def getBrailleDisplayController(self) -> BrailleDisplayController: ...
    def getFingerprintGestureController(self) -> FingerprintGestureController: ...
    def getInputMethod(self) -> InputMethod: ...
    def getMagnificationController(self) -> Any: ...
    def getSoftKeyboardController(self) -> Any: ...
    def getSystemActions(self) -> list: ...
    def getTouchInteractionController(self, p0: int) -> TouchInteractionController: ...
    def isCacheEnabled(self) -> bool: ...
    def isNodeInCache(self, p0: AccessibilityNodeInfo) -> bool: ...
    def onCreateInputMethod(self) -> InputMethod: ...
    def onInterrupt(self) -> None: ...
    def onSystemActionsChanged(self) -> None: ...
    def setAccessibilityFocusAppearance(self, p0: int, p1: int) -> None: ...
    def setCacheEnabled(self, p0: bool) -> bool: ...
    def setGestureDetectionPassthroughRegion(self, p0: int, p1: Region) -> None: ...
    def setTouchExplorationPassthroughRegion(self, p0: int, p1: Region) -> None: ...
    def takeScreenshotOfWindow(self, p0: int, p1: Executor, p2: Any) -> None: ...
    def findFocus(self, p0: int) -> AccessibilityNodeInfo: ...
    def getServiceInfo(self) -> AccessibilityServiceInfo: ...
    def clearCache(self) -> bool: ...
    def onBind(self, p0: Intent) -> IBinder: ...
    def createDisplayContext(self, p0: Display) -> Context: ...
    @overload
    def createWindowContext(self, p0: Display, p1: int, p2: Bundle) -> Context: ...
    @overload
    def createWindowContext(self, p0: int, p1: Bundle) -> Context: ...
    def getSystemService(self, p0: str) -> Any: ...
    def performGlobalAction(self, p0: int) -> bool: ...
    def takeScreenshot(self, p0: int, p1: Executor, p2: Any) -> None: ...
    def getWindows(self) -> list: ...
    def setServiceInfo(self, p0: AccessibilityServiceInfo) -> None: ...
    def getWindowsOnAllDisplays(self) -> SparseArray: ...
    def setAnimationScale(self, p0: float) -> None: ...
    @overload
    def getRootInActiveWindow(self, p0: int) -> AccessibilityNodeInfo: ...
    @overload
    def getRootInActiveWindow(self) -> AccessibilityNodeInfo: ...
    def onGesture(self, p0: AccessibilityGestureEvent) -> bool: ...

    class TakeScreenshotCallback:
        def onFailure(self, p0: int) -> None: ...
        def onSuccess(self, p0: Any) -> None: ...

    class SoftKeyboardController:
        ENABLE_IME_FAIL_BY_ADMIN: ClassVar[int]
        ENABLE_IME_FAIL_UNKNOWN: ClassVar[int]
        ENABLE_IME_SUCCESS: ClassVar[int]
        @overload
        def addOnShowModeChangedListener(self, p0: Any, p1: Handler) -> None: ...
        @overload
        def addOnShowModeChangedListener(self, p0: Any) -> None: ...
        def getShowMode(self) -> int: ...
        def removeOnShowModeChangedListener(self, p0: Any) -> bool: ...
        def setInputMethodEnabled(self, p0: str, p1: bool) -> int: ...
        def setShowMode(self, p0: int) -> bool: ...
        def switchToInputMethod(self, p0: str) -> bool: ...

        class OnShowModeChangedListener:
            def onShowModeChanged(self, p0: Any, p1: int) -> None: ...

    class ScreenshotResult:
        def getHardwareBuffer(self) -> HardwareBuffer: ...
        def getColorSpace(self) -> ColorSpace: ...
        def getTimestamp(self) -> int: ...

    class MagnificationController:
        def getCurrentMagnificationRegion(self) -> Region: ...
        def getMagnificationConfig(self) -> MagnificationConfig: ...
        def getMagnificationRegion(self) -> Region: ...
        def resetCurrentMagnification(self, p0: bool) -> bool: ...
        def setMagnificationConfig(self, p0: MagnificationConfig, p1: bool) -> bool: ...
        def setCenter(self, p0: float, p1: float, p2: bool) -> bool: ...
        def getCenterY(self) -> float: ...
        def getCenterX(self) -> float: ...
        def reset(self, p0: bool) -> bool: ...
        def setScale(self, p0: float, p1: bool) -> bool: ...
        def getScale(self) -> float: ...
        @overload
        def addListener(self, p0: Any) -> None: ...
        @overload
        def addListener(self, p0: Any, p1: Handler) -> None: ...
        def removeListener(self, p0: Any) -> bool: ...

        class OnMagnificationChangedListener:
            @overload
            def onMagnificationChanged(self, p0: Any, p1: Region, p2: MagnificationConfig) -> None: ...
            @overload
            def onMagnificationChanged(self, p0: Any, p1: Region, p2: float, p3: float, p4: float) -> None: ...

    class GestureResultCallback:
        def __init__(self) -> None: ...
        def onCompleted(self, p0: GestureDescription) -> None: ...
        def onCancelled(self, p0: GestureDescription) -> None: ...
