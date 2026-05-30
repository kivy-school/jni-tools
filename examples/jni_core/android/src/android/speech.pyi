from typing import Any, ClassVar, overload

class ModelDownloadListener:
    def onError(self, p0: int) -> None: ...
    def onProgress(self, p0: int) -> None: ...
    def onScheduled(self) -> None: ...
    def onSuccess(self) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle

class RecognitionListener:
    def onError(self, p0: int) -> None: ...
    def onBeginningOfSpeech(self) -> None: ...
    def onBufferReceived(self, p0: Any) -> None: ...
    def onEndOfSegmentedSession(self) -> None: ...
    def onEndOfSpeech(self) -> None: ...
    def onEvent(self, p0: int, p1: Bundle) -> None: ...
    def onLanguageDetection(self, p0: Bundle) -> None: ...
    def onPartialResults(self, p0: Bundle) -> None: ...
    def onReadyForSpeech(self, p0: Bundle) -> None: ...
    def onResults(self, p0: Bundle) -> None: ...
    def onRmsChanged(self, p0: float) -> None: ...
    def onSegmentResults(self, p0: Bundle) -> None: ...

from typing import Any, ClassVar, overload
from android.speech.RecognitionSupport import RecognitionSupport

class RecognitionSupportCallback:
    def onSupportResult(self, p0: RecognitionSupport) -> None: ...
    def onError(self, p0: int) -> None: ...

from typing import Any, ClassVar, overload
from android.content.ComponentName import ComponentName
from android.content.Context import Context
from android.content.Intent import Intent
from android.speech.ModelDownloadListener import ModelDownloadListener
from android.speech.RecognitionListener import RecognitionListener
from android.speech.RecognitionSupportCallback import RecognitionSupportCallback
from java.util.concurrent.Executor import Executor

class SpeechRecognizer:
    CONFIDENCE_SCORES: ClassVar[str]
    DETECTED_LANGUAGE: ClassVar[str]
    ERROR_AUDIO: ClassVar[int]
    ERROR_CANNOT_CHECK_SUPPORT: ClassVar[int]
    ERROR_CANNOT_LISTEN_TO_DOWNLOAD_EVENTS: ClassVar[int]
    ERROR_CLIENT: ClassVar[int]
    ERROR_INSUFFICIENT_PERMISSIONS: ClassVar[int]
    ERROR_LANGUAGE_NOT_SUPPORTED: ClassVar[int]
    ERROR_LANGUAGE_UNAVAILABLE: ClassVar[int]
    ERROR_NETWORK: ClassVar[int]
    ERROR_NETWORK_TIMEOUT: ClassVar[int]
    ERROR_NO_MATCH: ClassVar[int]
    ERROR_RECOGNIZER_BUSY: ClassVar[int]
    ERROR_SERVER: ClassVar[int]
    ERROR_SERVER_DISCONNECTED: ClassVar[int]
    ERROR_SPEECH_TIMEOUT: ClassVar[int]
    ERROR_TOO_MANY_REQUESTS: ClassVar[int]
    LANGUAGE_DETECTION_CONFIDENCE_LEVEL: ClassVar[str]
    LANGUAGE_DETECTION_CONFIDENCE_LEVEL_CONFIDENT: ClassVar[int]
    LANGUAGE_DETECTION_CONFIDENCE_LEVEL_HIGHLY_CONFIDENT: ClassVar[int]
    LANGUAGE_DETECTION_CONFIDENCE_LEVEL_NOT_CONFIDENT: ClassVar[int]
    LANGUAGE_DETECTION_CONFIDENCE_LEVEL_UNKNOWN: ClassVar[int]
    LANGUAGE_SWITCH_RESULT: ClassVar[str]
    LANGUAGE_SWITCH_RESULT_FAILED: ClassVar[int]
    LANGUAGE_SWITCH_RESULT_NOT_ATTEMPTED: ClassVar[int]
    LANGUAGE_SWITCH_RESULT_SKIPPED_NO_MODEL: ClassVar[int]
    LANGUAGE_SWITCH_RESULT_SUCCEEDED: ClassVar[int]
    RECOGNITION_PARTS: ClassVar[str]
    RESULTS_ALTERNATIVES: ClassVar[str]
    RESULTS_RECOGNITION: ClassVar[str]
    TOP_LOCALE_ALTERNATIVES: ClassVar[str]
    def destroy(self) -> None: ...
    def cancel(self) -> None: ...
    def startListening(self, p0: Intent) -> None: ...
    def checkRecognitionSupport(self, p0: Intent, p1: Executor, p2: RecognitionSupportCallback) -> None: ...
    @staticmethod
    def createOnDeviceSpeechRecognizer(p0: Context) -> "SpeechRecognizer": ...
    @overload
    @staticmethod
    def createSpeechRecognizer(p0: Context, p1: ComponentName) -> "SpeechRecognizer": ...
    @overload
    @staticmethod
    def createSpeechRecognizer(p0: Context) -> "SpeechRecognizer": ...
    @staticmethod
    def isOnDeviceRecognitionAvailable(p0: Context) -> bool: ...
    @staticmethod
    def isRecognitionAvailable(p0: Context) -> bool: ...
    def setRecognitionListener(self, p0: RecognitionListener) -> None: ...
    def stopListening(self) -> None: ...
    @overload
    def triggerModelDownload(self, p0: Intent) -> None: ...
    @overload
    def triggerModelDownload(self, p0: Intent, p1: Executor, p2: ModelDownloadListener) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class RecognitionSupport:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getOnlineLanguages(self) -> list: ...
    def getInstalledOnDeviceLanguages(self) -> list: ...
    def getPendingOnDeviceLanguages(self) -> list: ...
    def getSupportedOnDeviceLanguages(self) -> list: ...

    class Builder:
        def __init__(self) -> None: ...
        def build(self) -> "RecognitionSupport": ...
        def addInstalledOnDeviceLanguage(self, p0: str) -> Any: ...
        def addOnlineLanguage(self, p0: str) -> Any: ...
        def addPendingOnDeviceLanguage(self, p0: str) -> Any: ...
        def addSupportedOnDeviceLanguage(self, p0: str) -> Any: ...
        def setInstalledOnDeviceLanguages(self, p0: list) -> Any: ...
        def setOnlineLanguages(self, p0: list) -> Any: ...
        def setPendingOnDeviceLanguages(self, p0: list) -> Any: ...
        def setSupportedOnDeviceLanguages(self, p0: list) -> Any: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class RecognitionPart:
    CONFIDENCE_LEVEL_HIGH: ClassVar[int]
    CONFIDENCE_LEVEL_LOW: ClassVar[int]
    CONFIDENCE_LEVEL_MEDIUM: ClassVar[int]
    CONFIDENCE_LEVEL_MEDIUM_HIGH: ClassVar[int]
    CONFIDENCE_LEVEL_MEDIUM_LOW: ClassVar[int]
    CONFIDENCE_LEVEL_UNKNOWN: ClassVar[int]
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def getConfidenceLevel(self) -> int: ...
    def getFormattedText(self) -> str: ...
    def getRawText(self) -> str: ...
    def getTimestampMillis(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class Builder:
        def __init__(self, p0: str) -> None: ...
        def build(self) -> "RecognitionPart": ...
        def setConfidenceLevel(self, p0: int) -> Any: ...
        def setRawText(self, p0: str) -> Any: ...
        def setTimestampMillis(self, p0: int) -> Any: ...
        def setFormattedText(self, p0: str) -> Any: ...

from typing import Any, ClassVar, overload

class RecognizerResultsIntent:
    ACTION_VOICE_SEARCH_RESULTS: ClassVar[str]
    EXTRA_VOICE_SEARCH_RESULT_HTML: ClassVar[str]
    EXTRA_VOICE_SEARCH_RESULT_HTML_BASE_URLS: ClassVar[str]
    EXTRA_VOICE_SEARCH_RESULT_HTTP_HEADERS: ClassVar[str]
    EXTRA_VOICE_SEARCH_RESULT_STRINGS: ClassVar[str]
    EXTRA_VOICE_SEARCH_RESULT_URLS: ClassVar[str]
    URI_SCHEME_INLINE: ClassVar[str]

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class AlternativeSpan:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: list) -> None: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def getAlternatives(self) -> list: ...
    def getEndPosition(self) -> int: ...
    def getStartPosition(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.content.Intent import Intent

class RecognizerIntent:
    ACTION_GET_LANGUAGE_DETAILS: ClassVar[str]
    ACTION_RECOGNIZE_SPEECH: ClassVar[str]
    ACTION_VOICE_SEARCH_HANDS_FREE: ClassVar[str]
    ACTION_WEB_SEARCH: ClassVar[str]
    DETAILS_META_DATA: ClassVar[str]
    EXTRA_AUDIO_INJECT_SOURCE: ClassVar[str]
    EXTRA_AUDIO_SOURCE: ClassVar[str]
    EXTRA_AUDIO_SOURCE_CHANNEL_COUNT: ClassVar[str]
    EXTRA_AUDIO_SOURCE_ENCODING: ClassVar[str]
    EXTRA_AUDIO_SOURCE_SAMPLING_RATE: ClassVar[str]
    EXTRA_BIASING_STRINGS: ClassVar[str]
    EXTRA_CALLING_PACKAGE: ClassVar[str]
    EXTRA_CONFIDENCE_SCORES: ClassVar[str]
    EXTRA_ENABLE_BIASING_DEVICE_CONTEXT: ClassVar[str]
    EXTRA_ENABLE_FORMATTING: ClassVar[str]
    EXTRA_ENABLE_LANGUAGE_DETECTION: ClassVar[str]
    EXTRA_ENABLE_LANGUAGE_SWITCH: ClassVar[str]
    EXTRA_HIDE_PARTIAL_TRAILING_PUNCTUATION: ClassVar[str]
    EXTRA_LANGUAGE: ClassVar[str]
    EXTRA_LANGUAGE_DETECTION_ALLOWED_LANGUAGES: ClassVar[str]
    EXTRA_LANGUAGE_MODEL: ClassVar[str]
    EXTRA_LANGUAGE_PREFERENCE: ClassVar[str]
    EXTRA_LANGUAGE_SWITCH_ALLOWED_LANGUAGES: ClassVar[str]
    EXTRA_LANGUAGE_SWITCH_INITIAL_ACTIVE_DURATION_TIME_MILLIS: ClassVar[str]
    EXTRA_LANGUAGE_SWITCH_MAX_SWITCHES: ClassVar[str]
    EXTRA_MASK_OFFENSIVE_WORDS: ClassVar[str]
    EXTRA_MAX_RESULTS: ClassVar[str]
    EXTRA_ONLY_RETURN_LANGUAGE_PREFERENCE: ClassVar[str]
    EXTRA_ORIGIN: ClassVar[str]
    EXTRA_PARTIAL_RESULTS: ClassVar[str]
    EXTRA_PREFER_OFFLINE: ClassVar[str]
    EXTRA_PROMPT: ClassVar[str]
    EXTRA_REQUEST_WORD_CONFIDENCE: ClassVar[str]
    EXTRA_REQUEST_WORD_TIMING: ClassVar[str]
    EXTRA_RESULTS: ClassVar[str]
    EXTRA_RESULTS_PENDINGINTENT: ClassVar[str]
    EXTRA_RESULTS_PENDINGINTENT_BUNDLE: ClassVar[str]
    EXTRA_SECURE: ClassVar[str]
    EXTRA_SEGMENTED_SESSION: ClassVar[str]
    EXTRA_SPEECH_INPUT_COMPLETE_SILENCE_LENGTH_MILLIS: ClassVar[str]
    EXTRA_SPEECH_INPUT_MINIMUM_LENGTH_MILLIS: ClassVar[str]
    EXTRA_SPEECH_INPUT_POSSIBLY_COMPLETE_SILENCE_LENGTH_MILLIS: ClassVar[str]
    EXTRA_SUPPORTED_LANGUAGES: ClassVar[str]
    EXTRA_WEB_SEARCH_ONLY: ClassVar[str]
    FORMATTING_OPTIMIZE_LATENCY: ClassVar[str]
    FORMATTING_OPTIMIZE_QUALITY: ClassVar[str]
    LANGUAGE_MODEL_FREE_FORM: ClassVar[str]
    LANGUAGE_MODEL_WEB_SEARCH: ClassVar[str]
    LANGUAGE_SWITCH_BALANCED: ClassVar[str]
    LANGUAGE_SWITCH_HIGH_PRECISION: ClassVar[str]
    LANGUAGE_SWITCH_QUICK_RESPONSE: ClassVar[str]
    RESULT_AUDIO_ERROR: ClassVar[int]
    RESULT_CLIENT_ERROR: ClassVar[int]
    RESULT_NETWORK_ERROR: ClassVar[int]
    RESULT_NO_MATCH: ClassVar[int]
    RESULT_SERVER_ERROR: ClassVar[int]
    @staticmethod
    def getVoiceDetailsIntent(p0: Context) -> Intent: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class AlternativeSpans:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: list) -> None: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getSpans(self) -> list: ...

from typing import Any, ClassVar, overload
from android.content.AttributionSource import AttributionSource
from android.content.Context import Context
from android.content.ContextParams import ContextParams
from android.content.Intent import Intent
from android.os.Bundle import Bundle
from android.os.IBinder import IBinder
from android.speech.ModelDownloadListener import ModelDownloadListener
from android.speech.RecognitionSupport import RecognitionSupport

class RecognitionService:
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
    def getMaxConcurrentSessionsCount(self) -> int: ...
    @overload
    def onCheckRecognitionSupport(self, p0: Intent, p1: AttributionSource, p2: Any) -> None: ...
    @overload
    def onCheckRecognitionSupport(self, p0: Intent, p1: Any) -> None: ...
    @overload
    def onTriggerModelDownload(self, p0: Intent, p1: AttributionSource, p2: ModelDownloadListener) -> None: ...
    @overload
    def onTriggerModelDownload(self, p0: Intent) -> None: ...
    @overload
    def onTriggerModelDownload(self, p0: Intent, p1: AttributionSource) -> None: ...
    def onBind(self, p0: Intent) -> IBinder: ...
    def onDestroy(self) -> None: ...
    def createContext(self, p0: ContextParams) -> Context: ...

    class SupportCallback:
        def onSupportResult(self, p0: RecognitionSupport) -> None: ...
        def onError(self, p0: int) -> None: ...

    class Callback:
        def error(self, p0: int) -> None: ...
        def bufferReceived(self, p0: Any) -> None: ...
        def endOfSpeech(self) -> None: ...
        def getCallingUid(self) -> int: ...
        def endOfSegmentedSession(self) -> None: ...
        def beginningOfSpeech(self) -> None: ...
        def getCallingAttributionSource(self) -> AttributionSource: ...
        def languageDetection(self, p0: Bundle) -> None: ...
        def partialResults(self, p0: Bundle) -> None: ...
        def readyForSpeech(self, p0: Bundle) -> None: ...
        def rmsChanged(self, p0: float) -> None: ...
        def results(self, p0: Bundle) -> None: ...
        def segmentResults(self, p0: Bundle) -> None: ...

