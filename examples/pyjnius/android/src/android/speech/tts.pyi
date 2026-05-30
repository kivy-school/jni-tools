from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle

class SynthesisRequest:
    @overload
    def __init__(self, p0: str, p1: Bundle) -> None: ...
    @overload
    def __init__(self, p0: str, p1: Bundle) -> None: ...
    def getLanguage(self) -> str: ...
    def getCallerUid(self) -> int: ...
    def getCharSequenceText(self) -> str: ...
    def getParams(self) -> Bundle: ...
    def getPitch(self) -> int: ...
    def getSpeechRate(self) -> int: ...
    def getText(self) -> str: ...
    def getVoiceName(self) -> str: ...
    def getCountry(self) -> str: ...
    def getVariant(self) -> str: ...

from typing import Any, ClassVar, overload
from android.content.Intent import Intent
from android.os.IBinder import IBinder

class TextToSpeechService:
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
    def onBind(self, p0: Intent) -> IBinder: ...
    def onCreate(self) -> None: ...
    def onDestroy(self) -> None: ...
    def onGetDefaultVoiceNameFor(self, p0: str, p1: str, p2: str) -> str: ...
    def onGetVoices(self) -> list: ...
    def onIsValidVoiceName(self, p0: str) -> int: ...
    def onLoadVoice(self, p0: str) -> int: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.media.AudioAttributes import AudioAttributes
from android.net.Uri import Uri
from android.os.Bundle import Bundle
from android.os.ParcelFileDescriptor import ParcelFileDescriptor
from android.speech.tts.UtteranceProgressListener import UtteranceProgressListener
from android.speech.tts.Voice import Voice
from java.io.File import File
from java.util.Locale import Locale

class TextToSpeech:
    ACTION_TTS_QUEUE_PROCESSING_COMPLETED: ClassVar[str]
    ERROR: ClassVar[int]
    ERROR_INVALID_REQUEST: ClassVar[int]
    ERROR_NETWORK: ClassVar[int]
    ERROR_NETWORK_TIMEOUT: ClassVar[int]
    ERROR_NOT_INSTALLED_YET: ClassVar[int]
    ERROR_OUTPUT: ClassVar[int]
    ERROR_SERVICE: ClassVar[int]
    ERROR_SYNTHESIS: ClassVar[int]
    LANG_AVAILABLE: ClassVar[int]
    LANG_COUNTRY_AVAILABLE: ClassVar[int]
    LANG_COUNTRY_VAR_AVAILABLE: ClassVar[int]
    LANG_MISSING_DATA: ClassVar[int]
    LANG_NOT_SUPPORTED: ClassVar[int]
    QUEUE_ADD: ClassVar[int]
    QUEUE_FLUSH: ClassVar[int]
    STOPPED: ClassVar[int]
    SUCCESS: ClassVar[int]
    @overload
    def __init__(self, p0: Context, p1: Any) -> None: ...
    @overload
    def __init__(self, p0: Context, p1: Any, p2: str) -> None: ...
    def getLanguage(self) -> Locale: ...
    def shutdown(self) -> None: ...
    def stop(self) -> int: ...
    @overload
    def speak(self, p0: str, p1: int, p2: Bundle, p3: str) -> int: ...
    @overload
    def speak(self, p0: str, p1: int, p2: dict) -> int: ...
    @overload
    def addEarcon(self, p0: str, p1: File) -> int: ...
    @overload
    def addEarcon(self, p0: str, p1: Uri) -> int: ...
    @overload
    def addEarcon(self, p0: str, p1: str, p2: int) -> int: ...
    @overload
    def addEarcon(self, p0: str, p1: str) -> int: ...
    @overload
    def addSpeech(self, p0: str, p1: Uri) -> int: ...
    @overload
    def addSpeech(self, p0: str, p1: str, p2: int) -> int: ...
    @overload
    def addSpeech(self, p0: str, p1: str) -> int: ...
    @overload
    def addSpeech(self, p0: str, p1: str, p2: int) -> int: ...
    @overload
    def addSpeech(self, p0: str, p1: File) -> int: ...
    def areDefaultsEnforced(self) -> bool: ...
    def getAvailableLanguages(self) -> set: ...
    def getDefaultEngine(self) -> str: ...
    def getDefaultLanguage(self) -> Locale: ...
    def getDefaultVoice(self) -> Voice: ...
    def getEngines(self) -> list: ...
    def getFeatures(self, p0: Locale) -> set: ...
    @staticmethod
    def getMaxSpeechInputLength() -> int: ...
    def getVoice(self) -> Voice: ...
    def getVoices(self) -> set: ...
    def isLanguageAvailable(self, p0: Locale) -> int: ...
    def isSpeaking(self) -> bool: ...
    @overload
    def playEarcon(self, p0: str, p1: int, p2: Bundle, p3: str) -> int: ...
    @overload
    def playEarcon(self, p0: str, p1: int, p2: dict) -> int: ...
    def playSilence(self, p0: int, p1: int, p2: dict) -> int: ...
    def playSilentUtterance(self, p0: int, p1: int, p2: str) -> int: ...
    def setAudioAttributes(self, p0: AudioAttributes) -> int: ...
    def setEngineByPackageName(self, p0: str) -> int: ...
    def setLanguage(self, p0: Locale) -> int: ...
    def setOnUtteranceCompletedListener(self, p0: Any) -> int: ...
    def setOnUtteranceProgressListener(self, p0: UtteranceProgressListener) -> int: ...
    def setPitch(self, p0: float) -> int: ...
    def setSpeechRate(self, p0: float) -> int: ...
    def setVoice(self, p0: Voice) -> int: ...
    @overload
    def synthesizeToFile(self, p0: str, p1: Bundle, p2: File, p3: str) -> int: ...
    @overload
    def synthesizeToFile(self, p0: str, p1: dict, p2: str) -> int: ...
    @overload
    def synthesizeToFile(self, p0: str, p1: Bundle, p2: ParcelFileDescriptor, p3: str) -> int: ...

    class OnUtteranceCompletedListener:
        def onUtteranceCompleted(self, p0: str) -> None: ...

    class OnInitListener:
        def onInit(self, p0: int) -> None: ...

    class EngineInfo:
        icon: int
        label: str
        name: str
        def __init__(self) -> None: ...
        def toString(self) -> str: ...

    class Engine:
        ACTION_CHECK_TTS_DATA: ClassVar[str]
        ACTION_GET_SAMPLE_TEXT: ClassVar[str]
        ACTION_INSTALL_TTS_DATA: ClassVar[str]
        ACTION_TTS_DATA_INSTALLED: ClassVar[str]
        CHECK_VOICE_DATA_BAD_DATA: ClassVar[int]
        CHECK_VOICE_DATA_FAIL: ClassVar[int]
        CHECK_VOICE_DATA_MISSING_DATA: ClassVar[int]
        CHECK_VOICE_DATA_MISSING_VOLUME: ClassVar[int]
        CHECK_VOICE_DATA_PASS: ClassVar[int]
        DEFAULT_STREAM: ClassVar[int]
        EXTRA_AVAILABLE_VOICES: ClassVar[str]
        EXTRA_CHECK_VOICE_DATA_FOR: ClassVar[str]
        EXTRA_SAMPLE_TEXT: ClassVar[str]
        EXTRA_TTS_DATA_INSTALLED: ClassVar[str]
        EXTRA_UNAVAILABLE_VOICES: ClassVar[str]
        EXTRA_VOICE_DATA_FILES: ClassVar[str]
        EXTRA_VOICE_DATA_FILES_INFO: ClassVar[str]
        EXTRA_VOICE_DATA_ROOT_DIRECTORY: ClassVar[str]
        INTENT_ACTION_TTS_SERVICE: ClassVar[str]
        KEY_FEATURE_EMBEDDED_SYNTHESIS: ClassVar[str]
        KEY_FEATURE_NETWORK_RETRIES_COUNT: ClassVar[str]
        KEY_FEATURE_NETWORK_SYNTHESIS: ClassVar[str]
        KEY_FEATURE_NETWORK_TIMEOUT_MS: ClassVar[str]
        KEY_FEATURE_NOT_INSTALLED: ClassVar[str]
        KEY_PARAM_PAN: ClassVar[str]
        KEY_PARAM_SESSION_ID: ClassVar[str]
        KEY_PARAM_STREAM: ClassVar[str]
        KEY_PARAM_UTTERANCE_ID: ClassVar[str]
        KEY_PARAM_VOLUME: ClassVar[str]
        SERVICE_META_DATA: ClassVar[str]
        def __init__(self, p0: "TextToSpeech") -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from java.util.Locale import Locale

class Voice:
    CREATOR: ClassVar[Any]
    LATENCY_HIGH: ClassVar[int]
    LATENCY_LOW: ClassVar[int]
    LATENCY_NORMAL: ClassVar[int]
    LATENCY_VERY_HIGH: ClassVar[int]
    LATENCY_VERY_LOW: ClassVar[int]
    QUALITY_HIGH: ClassVar[int]
    QUALITY_LOW: ClassVar[int]
    QUALITY_NORMAL: ClassVar[int]
    QUALITY_VERY_HIGH: ClassVar[int]
    QUALITY_VERY_LOW: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: str, p1: Locale, p2: int, p3: int, p4: bool, p5: set) -> None: ...
    def getName(self) -> str: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def getFeatures(self) -> set: ...
    def getLatency(self) -> int: ...
    def getLocale(self) -> Locale: ...
    def getQuality(self) -> int: ...
    def isNetworkConnectionRequired(self) -> bool: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload

class UtteranceProgressListener:
    def __init__(self) -> None: ...
    def onStart(self, p0: str) -> None: ...
    def onDone(self, p0: str) -> None: ...
    def onAudioAvailable(self, p0: str, p1: Any) -> None: ...
    def onBeginSynthesis(self, p0: str, p1: int, p2: int, p3: int) -> None: ...
    @overload
    def onError(self, p0: str, p1: int) -> None: ...
    @overload
    def onError(self, p0: str) -> None: ...
    def onRangeStart(self, p0: str, p1: int, p2: int, p3: int) -> None: ...
    def onStop(self, p0: str, p1: bool) -> None: ...

from typing import Any, ClassVar, overload

class SynthesisCallback:
    def done(self) -> int: ...
    def start(self, p0: int, p1: int, p2: int) -> int: ...
    def audioAvailable(self, p0: Any, p1: int, p2: int) -> int: ...
    def getMaxBufferSize(self) -> int: ...
    def hasFinished(self) -> bool: ...
    def hasStarted(self) -> bool: ...
    def rangeStart(self, p0: int, p1: int, p2: int) -> None: ...
    @overload
    def error(self) -> None: ...
    @overload
    def error(self, p0: int) -> None: ...

