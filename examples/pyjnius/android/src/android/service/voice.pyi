from typing import Any, ClassVar, overload
from android.content.Intent import Intent
from android.content.res.Configuration import Configuration
from android.os.Bundle import Bundle
from android.os.IBinder import IBinder
from android.service.voice.VoiceInteractionSession import VoiceInteractionSession

class VoiceInteractionSessionService:
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
    def onNewSession(self, p0: Bundle) -> VoiceInteractionSession: ...
    def onBind(self, p0: Intent) -> IBinder: ...
    def onCreate(self) -> None: ...
    def onConfigurationChanged(self, p0: Configuration) -> None: ...
    def onLowMemory(self) -> None: ...
    def onTrimMemory(self, p0: int) -> None: ...

from typing import Any, ClassVar, overload
from android.content.ComponentName import ComponentName
from android.content.Context import Context
from android.content.Intent import Intent
from android.os.Bundle import Bundle
from android.os.IBinder import IBinder

class VoiceInteractionService:
    SERVICE_INTERFACE: ClassVar[str]
    SERVICE_META_DATA: ClassVar[str]
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
    def getDisabledShowContext(self) -> int: ...
    def setDisabledShowContext(self, p0: int) -> None: ...
    @staticmethod
    def isActiveService(p0: Context, p1: ComponentName) -> bool: ...
    def onGetSupportedVoiceActions(self, p0: set) -> set: ...
    def onLaunchVoiceAssistFromKeyguard(self) -> None: ...
    def onPrepareToShowSession(self, p0: Bundle, p1: int) -> None: ...
    def onShowSessionFailed(self, p0: Bundle) -> None: ...
    def onShutdown(self) -> None: ...
    def setUiHints(self, p0: Bundle) -> None: ...
    def showSession(self, p0: Bundle, p1: int) -> None: ...
    def onBind(self, p0: Intent) -> IBinder: ...
    def onReady(self) -> None: ...

from typing import Any, ClassVar, overload
from android.app.Dialog import Dialog
from android.app.DirectAction import DirectAction
from android.app.assist.AssistContent import AssistContent
from android.app.assist.AssistStructure import AssistStructure
from android.content.Context import Context
from android.content.Intent import Intent
from android.content.res.Configuration import Configuration
from android.graphics.Bitmap import Bitmap
from android.graphics.Rect import Rect
from android.graphics.Region import Region
from android.os.Bundle import Bundle
from android.os.CancellationSignal import CancellationSignal
from android.os.Handler import Handler
from android.service.voice.VisibleActivityInfo import VisibleActivityInfo
from android.view.KeyEvent import KeyEvent
from android.view.LayoutInflater import LayoutInflater
from android.view.View import View
from java.io.FileDescriptor import FileDescriptor
from java.io.PrintWriter import PrintWriter
from java.lang.Throwable import Throwable
from java.util.concurrent.Executor import Executor
from java.util.function.Consumer import Consumer

class VoiceInteractionSession:
    KEY_FOREGROUND_ACTIVITIES: ClassVar[str]
    KEY_SHOW_SESSION_ID: ClassVar[str]
    SHOW_SOURCE_ACTIVITY: ClassVar[int]
    SHOW_SOURCE_APPLICATION: ClassVar[int]
    SHOW_SOURCE_ASSIST_GESTURE: ClassVar[int]
    SHOW_SOURCE_AUTOMOTIVE_SYSTEM_UI: ClassVar[int]
    SHOW_SOURCE_NOTIFICATION: ClassVar[int]
    SHOW_SOURCE_PUSH_TO_TALK: ClassVar[int]
    SHOW_WITH_ASSIST: ClassVar[int]
    SHOW_WITH_SCREENSHOT: ClassVar[int]
    TRIM_MEMORY_BACKGROUND: ClassVar[int]
    TRIM_MEMORY_COMPLETE: ClassVar[int]
    TRIM_MEMORY_MODERATE: ClassVar[int]
    TRIM_MEMORY_RUNNING_CRITICAL: ClassVar[int]
    TRIM_MEMORY_RUNNING_LOW: ClassVar[int]
    TRIM_MEMORY_RUNNING_MODERATE: ClassVar[int]
    TRIM_MEMORY_UI_HIDDEN: ClassVar[int]
    @overload
    def __init__(self, p0: Context, p1: Handler) -> None: ...
    @overload
    def __init__(self, p0: Context) -> None: ...
    def onShow(self, p0: Bundle, p1: int) -> None: ...
    def getLayoutInflater(self) -> LayoutInflater: ...
    def onBackPressed(self) -> None: ...
    def closeSystemDialogs(self) -> None: ...
    def getDisabledShowContext(self) -> int: ...
    def getUserDisabledShowContext(self) -> int: ...
    def onAssistStructureFailure(self, p0: Throwable) -> None: ...
    def onCancelRequest(self, p0: Any) -> None: ...
    def onCloseSystemDialogs(self) -> None: ...
    def onComputeInsets(self, p0: Any) -> None: ...
    def onCreateContentView(self) -> View: ...
    def onDirectActionsInvalidated(self, p0: Any) -> None: ...
    def onGetSupportedCommands(self, p0: Any) -> Any: ...
    @overload
    def onHandleAssist(self, p0: Any) -> None: ...
    @overload
    def onHandleAssist(self, p0: Bundle, p1: AssistStructure, p2: AssistContent) -> None: ...
    def onHandleAssistSecondary(self, p0: Bundle, p1: AssistStructure, p2: AssistContent, p3: int, p4: int) -> None: ...
    def onHandleScreenshot(self, p0: Bitmap) -> None: ...
    def onHide(self) -> None: ...
    def onLockscreenShown(self) -> None: ...
    def onPrepareShow(self, p0: Bundle, p1: int) -> None: ...
    def onRequestAbortVoice(self, p0: Any) -> None: ...
    def onRequestCommand(self, p0: Any) -> None: ...
    def onRequestCompleteVoice(self, p0: Any) -> None: ...
    def onRequestConfirmation(self, p0: Any) -> None: ...
    def onRequestPickOption(self, p0: Any) -> None: ...
    def onTaskFinished(self, p0: Intent, p1: int) -> None: ...
    def onTaskStarted(self, p0: Intent, p1: int) -> None: ...
    def performDirectAction(self, p0: DirectAction, p1: Bundle, p2: CancellationSignal, p3: Executor, p4: Consumer) -> None: ...
    def registerVisibleActivityCallback(self, p0: Executor, p1: Any) -> None: ...
    def requestDirectActions(self, p0: Any, p1: CancellationSignal, p2: Executor, p3: Consumer) -> None: ...
    def setDisabledShowContext(self, p0: int) -> None: ...
    def setKeepAwake(self, p0: bool) -> None: ...
    def setUiEnabled(self, p0: bool) -> None: ...
    @overload
    def startAssistantActivity(self, p0: Intent, p1: Bundle) -> None: ...
    @overload
    def startAssistantActivity(self, p0: Intent) -> None: ...
    def startVoiceActivity(self, p0: Intent) -> None: ...
    def unregisterVisibleActivityCallback(self, p0: Any) -> None: ...
    def getContext(self) -> Context: ...
    def setTheme(self, p0: int) -> None: ...
    def onKeyDown(self, p0: int, p1: KeyEvent) -> bool: ...
    def onKeyLongPress(self, p0: int, p1: KeyEvent) -> bool: ...
    def onKeyMultiple(self, p0: int, p1: int, p2: KeyEvent) -> bool: ...
    def setContentView(self, p0: View) -> None: ...
    def onCreate(self) -> None: ...
    def onDestroy(self) -> None: ...
    def onConfigurationChanged(self, p0: Configuration) -> None: ...
    def onLowMemory(self) -> None: ...
    def onTrimMemory(self, p0: int) -> None: ...
    def onKeyUp(self, p0: int, p1: KeyEvent) -> bool: ...
    def finish(self) -> None: ...
    def dump(self, p0: str, p1: FileDescriptor, p2: PrintWriter, p3: Any) -> None: ...
    def hide(self) -> None: ...
    def show(self, p0: Bundle, p1: int) -> None: ...
    def getWindow(self) -> Dialog: ...

    class VisibleActivityCallback:
        def onInvisible(self, p0: Any) -> None: ...
        def onVisible(self, p0: VisibleActivityInfo) -> None: ...

    class Request:
        def toString(self) -> str: ...
        def cancel(self) -> None: ...
        def isActive(self) -> bool: ...
        def getCallingPackage(self) -> str: ...
        def getExtras(self) -> Bundle: ...
        def getCallingUid(self) -> int: ...

    class PickOptionRequest:
        def getPrompt(self) -> str: ...
        def getVoicePrompt(self) -> Any: ...
        def getOptions(self) -> Any: ...
        def sendIntermediatePickOptionResult(self, p0: Any, p1: Bundle) -> None: ...
        def sendPickOptionResult(self, p0: Any, p1: Bundle) -> None: ...

    class Insets:
        TOUCHABLE_INSETS_CONTENT: ClassVar[int]
        TOUCHABLE_INSETS_FRAME: ClassVar[int]
        TOUCHABLE_INSETS_REGION: ClassVar[int]
        contentInsets: Rect
        touchableInsets: int
        touchableRegion: Region
        def __init__(self) -> None: ...

    class ConfirmationRequest:
        def getPrompt(self) -> str: ...
        def getVoicePrompt(self) -> Any: ...
        def sendConfirmationResult(self, p0: bool, p1: Bundle) -> None: ...

    class CompleteVoiceRequest:
        def getMessage(self) -> str: ...
        def getVoicePrompt(self) -> Any: ...
        def sendCompleteResult(self, p0: Bundle) -> None: ...

    class CommandRequest:
        def getCommand(self) -> str: ...
        def sendIntermediateResult(self, p0: Bundle) -> None: ...
        def sendResult(self, p0: Bundle) -> None: ...

    class AssistState:
        def getActivityId(self) -> Any: ...
        def getAssistContent(self) -> AssistContent: ...
        def getAssistData(self) -> Bundle: ...
        def getAssistStructure(self) -> AssistStructure: ...
        def getCount(self) -> int: ...
        def getIndex(self) -> int: ...
        def isFocused(self) -> bool: ...

    class ActivityId:
        def equals(self, p0: Any) -> bool: ...
        def hashCode(self) -> int: ...

    class AbortVoiceRequest:
        def getMessage(self) -> str: ...
        def sendAbortResult(self, p0: Bundle) -> None: ...
        def getVoicePrompt(self) -> Any: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class VisibleActivityInfo:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getActivityId(self) -> Any: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

