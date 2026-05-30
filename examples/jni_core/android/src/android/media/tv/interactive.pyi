from typing import Any, ClassVar, overload
from android.content.ComponentName import ComponentName
from android.net.Uri import Uri
from android.os.Parcel import Parcel

class AppLinkInfo:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: str, p1: str, p2: str) -> None: ...
    def toString(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getUri(self) -> Uri: ...
    def getComponentName(self) -> ComponentName: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.graphics.Rect import Rect
from android.media.PlaybackParams import PlaybackParams
from android.media.tv.TvRecordingInfo import TvRecordingInfo
from android.media.tv.TvView import TvView
from android.net.Uri import Uri
from android.net.http.SslCertificate import SslCertificate
from android.os.Bundle import Bundle
from android.util.AttributeSet import AttributeSet
from android.util.Property import Property
from android.view.InputEvent import InputEvent
from android.view.KeyEvent import KeyEvent
from android.view.View import View
from java.util.concurrent.Executor import Executor

class TvInteractiveAppView:
    BI_INTERACTIVE_APP_KEY_ALIAS: ClassVar[str]
    BI_INTERACTIVE_APP_KEY_CERTIFICATE: ClassVar[str]
    BI_INTERACTIVE_APP_KEY_HTTP_ADDITIONAL_HEADERS: ClassVar[str]
    BI_INTERACTIVE_APP_KEY_HTTP_USER_AGENT: ClassVar[str]
    BI_INTERACTIVE_APP_KEY_PRIVATE_KEY: ClassVar[str]
    ERROR_KEY_METHOD_NAME: ClassVar[str]
    FOCUS_AFTER_DESCENDANTS: ClassVar[int]
    FOCUS_BEFORE_DESCENDANTS: ClassVar[int]
    FOCUS_BLOCK_DESCENDANTS: ClassVar[int]
    LAYOUT_MODE_CLIP_BOUNDS: ClassVar[int]
    LAYOUT_MODE_OPTICAL_BOUNDS: ClassVar[int]
    PERSISTENT_ALL_CACHES: ClassVar[int]
    PERSISTENT_ANIMATION_CACHE: ClassVar[int]
    PERSISTENT_NO_CACHE: ClassVar[int]
    PERSISTENT_SCROLLING_CACHE: ClassVar[int]
    ACCESSIBILITY_DATA_SENSITIVE_AUTO: ClassVar[int]
    ACCESSIBILITY_DATA_SENSITIVE_NO: ClassVar[int]
    ACCESSIBILITY_DATA_SENSITIVE_YES: ClassVar[int]
    ACCESSIBILITY_LIVE_REGION_ASSERTIVE: ClassVar[int]
    ACCESSIBILITY_LIVE_REGION_NONE: ClassVar[int]
    ACCESSIBILITY_LIVE_REGION_POLITE: ClassVar[int]
    ALPHA: ClassVar[Property]
    AUTOFILL_FLAG_INCLUDE_NOT_IMPORTANT_VIEWS: ClassVar[int]
    AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_DATE: ClassVar[str]
    AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_DAY: ClassVar[str]
    AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_MONTH: ClassVar[str]
    AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_YEAR: ClassVar[str]
    AUTOFILL_HINT_CREDIT_CARD_NUMBER: ClassVar[str]
    AUTOFILL_HINT_CREDIT_CARD_SECURITY_CODE: ClassVar[str]
    AUTOFILL_HINT_EMAIL_ADDRESS: ClassVar[str]
    AUTOFILL_HINT_NAME: ClassVar[str]
    AUTOFILL_HINT_PASSWORD: ClassVar[str]
    AUTOFILL_HINT_PHONE: ClassVar[str]
    AUTOFILL_HINT_POSTAL_ADDRESS: ClassVar[str]
    AUTOFILL_HINT_POSTAL_CODE: ClassVar[str]
    AUTOFILL_HINT_USERNAME: ClassVar[str]
    AUTOFILL_TYPE_DATE: ClassVar[int]
    AUTOFILL_TYPE_LIST: ClassVar[int]
    AUTOFILL_TYPE_NONE: ClassVar[int]
    AUTOFILL_TYPE_TEXT: ClassVar[int]
    AUTOFILL_TYPE_TOGGLE: ClassVar[int]
    CONTENT_SENSITIVITY_AUTO: ClassVar[int]
    CONTENT_SENSITIVITY_NOT_SENSITIVE: ClassVar[int]
    CONTENT_SENSITIVITY_SENSITIVE: ClassVar[int]
    DRAG_FLAG_ACCESSIBILITY_ACTION: ClassVar[int]
    DRAG_FLAG_GLOBAL: ClassVar[int]
    DRAG_FLAG_GLOBAL_PERSISTABLE_URI_PERMISSION: ClassVar[int]
    DRAG_FLAG_GLOBAL_PREFIX_URI_PERMISSION: ClassVar[int]
    DRAG_FLAG_GLOBAL_SAME_APPLICATION: ClassVar[int]
    DRAG_FLAG_GLOBAL_URI_READ: ClassVar[int]
    DRAG_FLAG_GLOBAL_URI_WRITE: ClassVar[int]
    DRAG_FLAG_HIDE_CALLING_TASK_ON_DRAG_START: ClassVar[int]
    DRAG_FLAG_OPAQUE: ClassVar[int]
    DRAG_FLAG_START_INTENT_SENDER_ON_UNHANDLED_DRAG: ClassVar[int]
    DRAWING_CACHE_QUALITY_AUTO: ClassVar[int]
    DRAWING_CACHE_QUALITY_HIGH: ClassVar[int]
    DRAWING_CACHE_QUALITY_LOW: ClassVar[int]
    FIND_VIEWS_WITH_CONTENT_DESCRIPTION: ClassVar[int]
    FIND_VIEWS_WITH_TEXT: ClassVar[int]
    FOCUSABLE: ClassVar[int]
    FOCUSABLES_ALL: ClassVar[int]
    FOCUSABLES_TOUCH_MODE: ClassVar[int]
    FOCUSABLE_AUTO: ClassVar[int]
    FOCUS_BACKWARD: ClassVar[int]
    FOCUS_DOWN: ClassVar[int]
    FOCUS_FORWARD: ClassVar[int]
    FOCUS_LEFT: ClassVar[int]
    FOCUS_RIGHT: ClassVar[int]
    FOCUS_UP: ClassVar[int]
    GONE: ClassVar[int]
    HAPTIC_FEEDBACK_ENABLED: ClassVar[int]
    IMPORTANT_FOR_ACCESSIBILITY_AUTO: ClassVar[int]
    IMPORTANT_FOR_ACCESSIBILITY_NO: ClassVar[int]
    IMPORTANT_FOR_ACCESSIBILITY_NO_HIDE_DESCENDANTS: ClassVar[int]
    IMPORTANT_FOR_ACCESSIBILITY_YES: ClassVar[int]
    IMPORTANT_FOR_AUTOFILL_AUTO: ClassVar[int]
    IMPORTANT_FOR_AUTOFILL_NO: ClassVar[int]
    IMPORTANT_FOR_AUTOFILL_NO_EXCLUDE_DESCENDANTS: ClassVar[int]
    IMPORTANT_FOR_AUTOFILL_YES: ClassVar[int]
    IMPORTANT_FOR_AUTOFILL_YES_EXCLUDE_DESCENDANTS: ClassVar[int]
    IMPORTANT_FOR_CONTENT_CAPTURE_AUTO: ClassVar[int]
    IMPORTANT_FOR_CONTENT_CAPTURE_NO: ClassVar[int]
    IMPORTANT_FOR_CONTENT_CAPTURE_NO_EXCLUDE_DESCENDANTS: ClassVar[int]
    IMPORTANT_FOR_CONTENT_CAPTURE_YES: ClassVar[int]
    IMPORTANT_FOR_CONTENT_CAPTURE_YES_EXCLUDE_DESCENDANTS: ClassVar[int]
    INVISIBLE: ClassVar[int]
    KEEP_SCREEN_ON: ClassVar[int]
    LAYER_TYPE_HARDWARE: ClassVar[int]
    LAYER_TYPE_NONE: ClassVar[int]
    LAYER_TYPE_SOFTWARE: ClassVar[int]
    LAYOUT_DIRECTION_INHERIT: ClassVar[int]
    LAYOUT_DIRECTION_LOCALE: ClassVar[int]
    LAYOUT_DIRECTION_LTR: ClassVar[int]
    LAYOUT_DIRECTION_RTL: ClassVar[int]
    MEASURED_HEIGHT_STATE_SHIFT: ClassVar[int]
    MEASURED_SIZE_MASK: ClassVar[int]
    MEASURED_STATE_MASK: ClassVar[int]
    MEASURED_STATE_TOO_SMALL: ClassVar[int]
    NOT_FOCUSABLE: ClassVar[int]
    NO_ID: ClassVar[int]
    OVER_SCROLL_ALWAYS: ClassVar[int]
    OVER_SCROLL_IF_CONTENT_SCROLLS: ClassVar[int]
    OVER_SCROLL_NEVER: ClassVar[int]
    REQUESTED_FRAME_RATE_CATEGORY_DEFAULT: ClassVar[float]
    REQUESTED_FRAME_RATE_CATEGORY_HIGH: ClassVar[float]
    REQUESTED_FRAME_RATE_CATEGORY_LOW: ClassVar[float]
    REQUESTED_FRAME_RATE_CATEGORY_NORMAL: ClassVar[float]
    REQUESTED_FRAME_RATE_CATEGORY_NO_PREFERENCE: ClassVar[float]
    ROTATION: ClassVar[Property]
    ROTATION_X: ClassVar[Property]
    ROTATION_Y: ClassVar[Property]
    SCALE_X: ClassVar[Property]
    SCALE_Y: ClassVar[Property]
    SCREEN_STATE_OFF: ClassVar[int]
    SCREEN_STATE_ON: ClassVar[int]
    SCROLLBARS_INSIDE_INSET: ClassVar[int]
    SCROLLBARS_INSIDE_OVERLAY: ClassVar[int]
    SCROLLBARS_OUTSIDE_INSET: ClassVar[int]
    SCROLLBARS_OUTSIDE_OVERLAY: ClassVar[int]
    SCROLLBAR_POSITION_DEFAULT: ClassVar[int]
    SCROLLBAR_POSITION_LEFT: ClassVar[int]
    SCROLLBAR_POSITION_RIGHT: ClassVar[int]
    SCROLL_AXIS_HORIZONTAL: ClassVar[int]
    SCROLL_AXIS_NONE: ClassVar[int]
    SCROLL_AXIS_VERTICAL: ClassVar[int]
    SCROLL_CAPTURE_HINT_AUTO: ClassVar[int]
    SCROLL_CAPTURE_HINT_EXCLUDE: ClassVar[int]
    SCROLL_CAPTURE_HINT_EXCLUDE_DESCENDANTS: ClassVar[int]
    SCROLL_CAPTURE_HINT_INCLUDE: ClassVar[int]
    SCROLL_INDICATOR_BOTTOM: ClassVar[int]
    SCROLL_INDICATOR_END: ClassVar[int]
    SCROLL_INDICATOR_LEFT: ClassVar[int]
    SCROLL_INDICATOR_RIGHT: ClassVar[int]
    SCROLL_INDICATOR_START: ClassVar[int]
    SCROLL_INDICATOR_TOP: ClassVar[int]
    SOUND_EFFECTS_ENABLED: ClassVar[int]
    STATUS_BAR_HIDDEN: ClassVar[int]
    STATUS_BAR_VISIBLE: ClassVar[int]
    SYSTEM_UI_FLAG_FULLSCREEN: ClassVar[int]
    SYSTEM_UI_FLAG_HIDE_NAVIGATION: ClassVar[int]
    SYSTEM_UI_FLAG_IMMERSIVE: ClassVar[int]
    SYSTEM_UI_FLAG_IMMERSIVE_STICKY: ClassVar[int]
    SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN: ClassVar[int]
    SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION: ClassVar[int]
    SYSTEM_UI_FLAG_LAYOUT_STABLE: ClassVar[int]
    SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR: ClassVar[int]
    SYSTEM_UI_FLAG_LIGHT_STATUS_BAR: ClassVar[int]
    SYSTEM_UI_FLAG_LOW_PROFILE: ClassVar[int]
    SYSTEM_UI_FLAG_VISIBLE: ClassVar[int]
    SYSTEM_UI_LAYOUT_FLAGS: ClassVar[int]
    TEXT_ALIGNMENT_CENTER: ClassVar[int]
    TEXT_ALIGNMENT_GRAVITY: ClassVar[int]
    TEXT_ALIGNMENT_INHERIT: ClassVar[int]
    TEXT_ALIGNMENT_TEXT_END: ClassVar[int]
    TEXT_ALIGNMENT_TEXT_START: ClassVar[int]
    TEXT_ALIGNMENT_VIEW_END: ClassVar[int]
    TEXT_ALIGNMENT_VIEW_START: ClassVar[int]
    TEXT_DIRECTION_ANY_RTL: ClassVar[int]
    TEXT_DIRECTION_FIRST_STRONG: ClassVar[int]
    TEXT_DIRECTION_FIRST_STRONG_LTR: ClassVar[int]
    TEXT_DIRECTION_FIRST_STRONG_RTL: ClassVar[int]
    TEXT_DIRECTION_INHERIT: ClassVar[int]
    TEXT_DIRECTION_LOCALE: ClassVar[int]
    TEXT_DIRECTION_LTR: ClassVar[int]
    TEXT_DIRECTION_RTL: ClassVar[int]
    TRANSLATION_X: ClassVar[Property]
    TRANSLATION_Y: ClassVar[Property]
    TRANSLATION_Z: ClassVar[Property]
    VISIBLE: ClassVar[int]
    X: ClassVar[Property]
    Y: ClassVar[Property]
    Z: ClassVar[Property]
    @overload
    def __init__(self, p0: Context, p1: AttributeSet) -> None: ...
    @overload
    def __init__(self, p0: Context) -> None: ...
    @overload
    def __init__(self, p0: Context, p1: AttributeSet, p2: int) -> None: ...
    def clearCallback(self) -> None: ...
    def clearOnUnhandledInputEventListener(self) -> None: ...
    def dispatchUnhandledInputEvent(self, p0: InputEvent) -> bool: ...
    def getOnUnhandledInputEventListener(self) -> Any: ...
    def notifyError(self, p0: str, p1: Bundle) -> None: ...
    def notifyTvMessage(self, p0: int, p1: Bundle) -> None: ...
    def onUnhandledInputEvent(self, p0: InputEvent) -> bool: ...
    def sendCurrentChannelUri(self, p0: Uri) -> None: ...
    def sendCurrentTvInputId(self, p0: str) -> None: ...
    def sendCurrentVideoBounds(self, p0: Rect) -> None: ...
    def sendSigningResult(self, p0: str, p1: Any) -> None: ...
    def sendTrackInfoList(self, p0: list) -> None: ...
    def setOnUnhandledInputEventListener(self, p0: Executor, p1: Any) -> None: ...
    def setTvView(self, p0: TvView) -> int: ...
    def createBiInteractiveApp(self, p0: Uri, p1: Bundle) -> None: ...
    def destroyBiInteractiveApp(self, p0: str) -> None: ...
    def notifyRecordingScheduled(self, p0: str, p1: str) -> None: ...
    def notifyRecordingStarted(self, p0: str, p1: str) -> None: ...
    def notifyRecordingStopped(self, p0: str) -> None: ...
    def notifyTimeShiftCurrentPositionChanged(self, p0: str, p1: int) -> None: ...
    def notifyTimeShiftPlaybackParams(self, p0: PlaybackParams) -> None: ...
    def notifyTimeShiftStartPositionChanged(self, p0: str, p1: int) -> None: ...
    def notifyTimeShiftStatusChanged(self, p0: str, p1: int) -> None: ...
    def notifyVideoFreezeUpdated(self, p0: bool) -> None: ...
    def prepareInteractiveApp(self, p0: str, p1: int) -> None: ...
    def resetInteractiveApp(self) -> None: ...
    def sendAvailableSpeeds(self, p0: Any) -> None: ...
    def sendCertificate(self, p0: str, p1: int, p2: SslCertificate) -> None: ...
    def sendCurrentChannelLcn(self, p0: int) -> None: ...
    def sendSelectedTrackInfo(self, p0: list) -> None: ...
    def sendStreamVolume(self, p0: float) -> None: ...
    def sendTimeShiftMode(self, p0: int) -> None: ...
    def sendTvRecordingInfo(self, p0: TvRecordingInfo) -> None: ...
    def sendTvRecordingInfoList(self, p0: list) -> None: ...
    def setTeletextAppEnabled(self, p0: bool) -> None: ...
    def startInteractiveApp(self) -> None: ...
    def stopInteractiveApp(self) -> None: ...
    def reset(self) -> None: ...
    def setZOrderMediaOverlay(self, p0: bool) -> None: ...
    def setZOrderOnTop(self, p0: bool) -> None: ...
    def onLayout(self, p0: bool, p1: int, p2: int, p3: int, p4: int) -> None: ...
    def onVisibilityChanged(self, p0: View, p1: int) -> None: ...
    def setCallback(self, p0: Executor, p1: Any) -> None: ...
    def onAttachedToWindow(self) -> None: ...
    def onDetachedFromWindow(self) -> None: ...
    def onMeasure(self, p0: int, p1: int) -> None: ...
    def dispatchKeyEvent(self, p0: KeyEvent) -> bool: ...

    class TvInteractiveAppCallback:
        def __init__(self) -> None: ...
        def onStateChanged(self, p0: str, p1: int, p2: int) -> None: ...
        def onBiInteractiveAppCreated(self, p0: str, p1: Uri, p2: str) -> None: ...
        def onPlaybackCommandRequest(self, p0: str, p1: str, p2: Bundle) -> None: ...
        def onRequestAvailableSpeeds(self, p0: str) -> None: ...
        def onRequestCertificate(self, p0: str, p1: str, p2: int) -> None: ...
        def onRequestCurrentChannelLcn(self, p0: str) -> None: ...
        @overload
        def onRequestScheduleRecording(self, p0: str, p1: str, p2: str, p3: Uri, p4: int, p5: int, p6: int, p7: Bundle) -> None: ...
        @overload
        def onRequestScheduleRecording(self, p0: str, p1: str, p2: str, p3: Uri, p4: Uri, p5: Bundle) -> None: ...
        def onRequestSelectedTrackInfo(self, p0: str) -> None: ...
        def onRequestStartRecording(self, p0: str, p1: str, p2: Uri) -> None: ...
        def onRequestStopRecording(self, p0: str, p1: str) -> None: ...
        def onRequestStreamVolume(self, p0: str) -> None: ...
        def onRequestTimeShiftMode(self, p0: str) -> None: ...
        def onRequestTvRecordingInfo(self, p0: str, p1: str) -> None: ...
        def onRequestTvRecordingInfoList(self, p0: str, p1: int) -> None: ...
        def onSetTvRecordingInfo(self, p0: str, p1: str, p2: TvRecordingInfo) -> None: ...
        def onSetVideoBounds(self, p0: str, p1: Rect) -> None: ...
        def onTeletextAppStateChanged(self, p0: str, p1: int) -> None: ...
        def onTimeShiftCommandRequest(self, p0: str, p1: str, p2: Bundle) -> None: ...
        def onRequestCurrentChannelUri(self, p0: str) -> None: ...
        def onRequestCurrentTvInputId(self, p0: str) -> None: ...
        def onRequestCurrentVideoBounds(self, p0: str) -> None: ...
        @overload
        def onRequestSigning(self, p0: str, p1: str, p2: str, p3: str, p4: Any) -> None: ...
        @overload
        def onRequestSigning(self, p0: str, p1: str, p2: str, p3: str, p4: int, p5: Any) -> None: ...
        def onRequestTrackInfoList(self, p0: str) -> None: ...

    class OnUnhandledInputEventListener:
        def onUnhandledInputEvent(self, p0: InputEvent) -> bool: ...

from typing import Any, ClassVar, overload
from android.media.tv.interactive.AppLinkInfo import AppLinkInfo
from android.os.Bundle import Bundle
from java.util.concurrent.Executor import Executor

class TvInteractiveAppManager:
    ACTION_APP_LINK_COMMAND: ClassVar[str]
    APP_LINK_KEY_BACK_URI: ClassVar[str]
    APP_LINK_KEY_CLASS_NAME: ClassVar[str]
    APP_LINK_KEY_COMMAND_TYPE: ClassVar[str]
    APP_LINK_KEY_PACKAGE_NAME: ClassVar[str]
    APP_LINK_KEY_SERVICE_ID: ClassVar[str]
    ERROR_BLOCKED: ClassVar[int]
    ERROR_ENCRYPTED: ClassVar[int]
    ERROR_NONE: ClassVar[int]
    ERROR_NOT_SUPPORTED: ClassVar[int]
    ERROR_RESOURCE_UNAVAILABLE: ClassVar[int]
    ERROR_UNKNOWN: ClassVar[int]
    ERROR_UNKNOWN_CHANNEL: ClassVar[int]
    ERROR_WEAK_SIGNAL: ClassVar[int]
    INTENT_KEY_BI_INTERACTIVE_APP_TYPE: ClassVar[str]
    INTENT_KEY_BI_INTERACTIVE_APP_URI: ClassVar[str]
    INTENT_KEY_CHANNEL_URI: ClassVar[str]
    INTENT_KEY_COMMAND_TYPE: ClassVar[str]
    INTENT_KEY_INTERACTIVE_APP_SERVICE_ID: ClassVar[str]
    INTENT_KEY_TV_INPUT_ID: ClassVar[str]
    INTERACTIVE_APP_STATE_ERROR: ClassVar[int]
    INTERACTIVE_APP_STATE_RUNNING: ClassVar[int]
    INTERACTIVE_APP_STATE_STOPPED: ClassVar[int]
    SERVICE_STATE_ERROR: ClassVar[int]
    SERVICE_STATE_PREPARING: ClassVar[int]
    SERVICE_STATE_READY: ClassVar[int]
    SERVICE_STATE_UNREALIZED: ClassVar[int]
    TELETEXT_APP_STATE_ERROR: ClassVar[int]
    TELETEXT_APP_STATE_HIDE: ClassVar[int]
    TELETEXT_APP_STATE_SHOW: ClassVar[int]
    def getAppLinkInfoList(self) -> list: ...
    def getTvInteractiveAppServiceList(self) -> list: ...
    def registerAppLinkInfo(self, p0: str, p1: AppLinkInfo) -> None: ...
    def unregisterAppLinkInfo(self, p0: str, p1: AppLinkInfo) -> None: ...
    def sendAppLinkCommand(self, p0: str, p1: Bundle) -> None: ...
    def registerCallback(self, p0: Executor, p1: Any) -> None: ...
    def unregisterCallback(self, p0: Any) -> None: ...

    class TvInteractiveAppCallback:
        def __init__(self) -> None: ...
        def onInteractiveAppServiceAdded(self, p0: str) -> None: ...
        def onInteractiveAppServiceRemoved(self, p0: str) -> None: ...
        def onInteractiveAppServiceUpdated(self, p0: str) -> None: ...
        def onTvInteractiveAppServiceStateChanged(self, p0: str, p1: int, p2: int, p3: int) -> None: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.content.Intent import Intent
from android.graphics.Rect import Rect
from android.media.PlaybackParams import PlaybackParams
from android.media.tv.AdBuffer import AdBuffer
from android.media.tv.AdRequest import AdRequest
from android.media.tv.AdResponse import AdResponse
from android.media.tv.BroadcastInfoRequest import BroadcastInfoRequest
from android.media.tv.BroadcastInfoResponse import BroadcastInfoResponse
from android.media.tv.TvContentRating import TvContentRating
from android.media.tv.TvRecordingInfo import TvRecordingInfo
from android.media.tv.interactive.AppLinkInfo import AppLinkInfo
from android.net.Uri import Uri
from android.net.http.SslCertificate import SslCertificate
from android.os.Bundle import Bundle
from android.os.IBinder import IBinder
from android.view.KeyEvent import KeyEvent
from android.view.MotionEvent import MotionEvent
from android.view.Surface import Surface
from android.view.View import View

class TvInteractiveAppService:
    COMMAND_PARAMETER_KEY_CHANGE_CHANNEL_QUIETLY: ClassVar[str]
    COMMAND_PARAMETER_KEY_CHANNEL_URI: ClassVar[str]
    COMMAND_PARAMETER_KEY_INPUT_ID: ClassVar[str]
    COMMAND_PARAMETER_KEY_PLAYBACK_PARAMS: ClassVar[str]
    COMMAND_PARAMETER_KEY_PROGRAM_URI: ClassVar[str]
    COMMAND_PARAMETER_KEY_STOP_MODE: ClassVar[str]
    COMMAND_PARAMETER_KEY_TIME_POSITION: ClassVar[str]
    COMMAND_PARAMETER_KEY_TIME_SHIFT_MODE: ClassVar[str]
    COMMAND_PARAMETER_KEY_TRACK_ID: ClassVar[str]
    COMMAND_PARAMETER_KEY_TRACK_TYPE: ClassVar[str]
    COMMAND_PARAMETER_KEY_VOLUME: ClassVar[str]
    COMMAND_PARAMETER_VALUE_STOP_MODE_BLANK: ClassVar[int]
    COMMAND_PARAMETER_VALUE_STOP_MODE_FREEZE: ClassVar[int]
    PLAYBACK_COMMAND_TYPE_SELECT_TRACK: ClassVar[str]
    PLAYBACK_COMMAND_TYPE_SET_STREAM_VOLUME: ClassVar[str]
    PLAYBACK_COMMAND_TYPE_STOP: ClassVar[str]
    PLAYBACK_COMMAND_TYPE_TUNE: ClassVar[str]
    PLAYBACK_COMMAND_TYPE_TUNE_NEXT: ClassVar[str]
    PLAYBACK_COMMAND_TYPE_TUNE_PREV: ClassVar[str]
    SERVICE_INTERFACE: ClassVar[str]
    SERVICE_META_DATA: ClassVar[str]
    TIME_SHIFT_COMMAND_TYPE_PAUSE: ClassVar[str]
    TIME_SHIFT_COMMAND_TYPE_PLAY: ClassVar[str]
    TIME_SHIFT_COMMAND_TYPE_RESUME: ClassVar[str]
    TIME_SHIFT_COMMAND_TYPE_SEEK_TO: ClassVar[str]
    TIME_SHIFT_COMMAND_TYPE_SET_MODE: ClassVar[str]
    TIME_SHIFT_COMMAND_TYPE_SET_PLAYBACK_PARAMS: ClassVar[str]
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
    def onCreateSession(self, p0: str, p1: int) -> Any: ...
    def notifyStateChanged(self, p0: int, p1: int, p2: int) -> None: ...
    def onRegisterAppLinkInfo(self, p0: AppLinkInfo) -> None: ...
    def onUnregisterAppLinkInfo(self, p0: AppLinkInfo) -> None: ...
    def onAppLinkCommand(self, p0: Bundle) -> None: ...
    def onBind(self, p0: Intent) -> IBinder: ...

    class Session:
        def __init__(self, p0: Context) -> None: ...
        def notifyBiInteractiveAppCreated(self, p0: Uri, p1: str) -> None: ...
        def notifyTeletextAppStateChanged(self, p0: int) -> None: ...
        def onAdBufferConsumed(self, p0: AdBuffer) -> None: ...
        def onAdResponse(self, p0: AdResponse) -> None: ...
        def onAvailableSpeeds(self, p0: Any) -> None: ...
        def onBroadcastInfoResponse(self, p0: BroadcastInfoResponse) -> None: ...
        def onCertificate(self, p0: str, p1: int, p2: SslCertificate) -> None: ...
        def onContentAllowed(self) -> None: ...
        def onContentBlocked(self, p0: TvContentRating) -> None: ...
        def onCreateBiInteractiveAppRequest(self, p0: Uri, p1: Bundle) -> None: ...
        def onCurrentChannelLcn(self, p0: int) -> None: ...
        def onDestroyBiInteractiveAppRequest(self, p0: str) -> None: ...
        def onRecordingConnectionFailed(self, p0: str, p1: str) -> None: ...
        def onRecordingDisconnected(self, p0: str, p1: str) -> None: ...
        def onRecordingError(self, p0: str, p1: int) -> None: ...
        def onRecordingScheduled(self, p0: str, p1: str) -> None: ...
        def onRecordingStarted(self, p0: str, p1: str) -> None: ...
        def onRecordingStopped(self, p0: str) -> None: ...
        def onRecordingTuned(self, p0: str, p1: Uri) -> None: ...
        def onResetInteractiveApp(self) -> None: ...
        def onSelectedTrackInfo(self, p0: list) -> None: ...
        def onSetTeletextAppEnabled(self, p0: bool) -> None: ...
        def onSignalStrength(self, p0: int) -> None: ...
        def onStartInteractiveApp(self) -> None: ...
        def onStopInteractiveApp(self) -> None: ...
        def onStreamVolume(self, p0: float) -> None: ...
        def onTimeShiftCurrentPositionChanged(self, p0: str, p1: int) -> None: ...
        def onTimeShiftMode(self, p0: int) -> None: ...
        def onTimeShiftPlaybackParams(self, p0: PlaybackParams) -> None: ...
        def onTimeShiftStartPositionChanged(self, p0: str, p1: int) -> None: ...
        def onTimeShiftStatusChanged(self, p0: str, p1: int) -> None: ...
        def onTrackSelected(self, p0: int, p1: str) -> None: ...
        def onTracksChanged(self, p0: list) -> None: ...
        def onTuned(self, p0: Uri) -> None: ...
        def onTvRecordingInfo(self, p0: TvRecordingInfo) -> None: ...
        def onTvRecordingInfoList(self, p0: list) -> None: ...
        def onVideoAvailable(self) -> None: ...
        def onVideoFreezeUpdated(self, p0: bool) -> None: ...
        def onVideoUnavailable(self, p0: int) -> None: ...
        def removeBroadcastInfo(self, p0: int) -> None: ...
        def requestAd(self, p0: AdRequest) -> None: ...
        def requestAvailableSpeeds(self) -> None: ...
        def requestBroadcastInfo(self, p0: BroadcastInfoRequest) -> None: ...
        def requestCertificate(self, p0: str, p1: int) -> None: ...
        def requestCurrentChannelLcn(self) -> None: ...
        @overload
        def requestScheduleRecording(self, p0: str, p1: str, p2: Uri, p3: int, p4: int, p5: int, p6: Bundle) -> None: ...
        @overload
        def requestScheduleRecording(self, p0: str, p1: str, p2: Uri, p3: Uri, p4: Bundle) -> None: ...
        def requestSelectedTrackInfo(self) -> None: ...
        def requestStartRecording(self, p0: str, p1: Uri) -> None: ...
        def requestStopRecording(self, p0: str) -> None: ...
        def requestStreamVolume(self) -> None: ...
        def requestTimeShiftMode(self) -> None: ...
        def requestTvRecordingInfo(self, p0: str) -> None: ...
        def requestTvRecordingInfoList(self, p0: int) -> None: ...
        def sendPlaybackCommandRequest(self, p0: str, p1: Bundle) -> None: ...
        def sendTimeShiftCommandRequest(self, p0: str, p1: Bundle) -> None: ...
        def setTvRecordingInfo(self, p0: str, p1: TvRecordingInfo) -> None: ...
        def setVideoBounds(self, p0: Rect) -> None: ...
        def notifyAdBufferReady(self, p0: AdBuffer) -> None: ...
        def notifySessionStateChanged(self, p0: int, p1: int) -> None: ...
        def isMediaViewEnabled(self) -> bool: ...
        def layoutSurface(self, p0: int, p1: int, p2: int, p3: int) -> None: ...
        def onCreateMediaView(self) -> View: ...
        def onCurrentChannelUri(self, p0: Uri) -> None: ...
        def onCurrentTvInputId(self, p0: str) -> None: ...
        def onCurrentVideoBounds(self, p0: Rect) -> None: ...
        def onMediaViewSizeChanged(self, p0: int, p1: int) -> None: ...
        def onSetSurface(self, p0: Surface) -> bool: ...
        def onSigningResult(self, p0: str, p1: Any) -> None: ...
        def onTrackInfoList(self, p0: list) -> None: ...
        def onTvMessage(self, p0: int, p1: Bundle) -> None: ...
        def requestCurrentChannelUri(self) -> None: ...
        def requestCurrentTvInputId(self) -> None: ...
        def requestCurrentVideoBounds(self) -> None: ...
        @overload
        def requestSigning(self, p0: str, p1: str, p2: str, p3: int, p4: Any) -> None: ...
        @overload
        def requestSigning(self, p0: str, p1: str, p2: str, p3: Any) -> None: ...
        def requestTrackInfoList(self) -> None: ...
        def setMediaViewEnabled(self, p0: bool) -> None: ...
        def onSurfaceChanged(self, p0: int, p1: int, p2: int) -> None: ...
        def onError(self, p0: str, p1: Bundle) -> None: ...
        def onKeyUp(self, p0: int, p1: KeyEvent) -> bool: ...
        def onTouchEvent(self, p0: MotionEvent) -> bool: ...
        def onGenericMotionEvent(self, p0: MotionEvent) -> bool: ...
        def onKeyDown(self, p0: int, p1: KeyEvent) -> bool: ...
        def onKeyLongPress(self, p0: int, p1: KeyEvent) -> bool: ...
        def onKeyMultiple(self, p0: int, p1: int, p2: KeyEvent) -> bool: ...
        def onTrackballEvent(self, p0: MotionEvent) -> bool: ...
        def onRelease(self) -> None: ...

from typing import Any, ClassVar, overload
from android.content.ComponentName import ComponentName
from android.content.Context import Context
from android.content.pm.ServiceInfo import ServiceInfo
from android.os.Parcel import Parcel

class TvInteractiveAppServiceInfo:
    CREATOR: ClassVar[Any]
    INTERACTIVE_APP_TYPE_ATSC: ClassVar[int]
    INTERACTIVE_APP_TYPE_GINGA: ClassVar[int]
    INTERACTIVE_APP_TYPE_HBBTV: ClassVar[int]
    INTERACTIVE_APP_TYPE_OTHER: ClassVar[int]
    INTERACTIVE_APP_TYPE_TARGETED_AD: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: Context, p1: ComponentName) -> None: ...
    def getSupportedTypes(self) -> int: ...
    def getCustomSupportedTypes(self) -> list: ...
    def getServiceInfo(self) -> ServiceInfo: ...
    def getId(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

