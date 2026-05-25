from typing import Any, ClassVar, overload
from android.content.ContentResolver import ContentResolver
from android.content.Context import Context
from android.content.res.Configuration import Configuration
from android.net.Uri import Uri

class Settings:
    ACTION_ACCESSIBILITY_SETTINGS: ClassVar[str]
    ACTION_ADD_ACCOUNT: ClassVar[str]
    ACTION_ADVANCED_MEMORY_PROTECTION_SETTINGS: ClassVar[str]
    ACTION_AIRPLANE_MODE_SETTINGS: ClassVar[str]
    ACTION_ALL_APPS_NOTIFICATION_SETTINGS: ClassVar[str]
    ACTION_APN_SETTINGS: ClassVar[str]
    ACTION_APPLICATION_DETAILS_SETTINGS: ClassVar[str]
    ACTION_APPLICATION_DEVELOPMENT_SETTINGS: ClassVar[str]
    ACTION_APPLICATION_SETTINGS: ClassVar[str]
    ACTION_APP_LOCALE_SETTINGS: ClassVar[str]
    ACTION_APP_NOTIFICATION_BUBBLE_SETTINGS: ClassVar[str]
    ACTION_APP_NOTIFICATION_SETTINGS: ClassVar[str]
    ACTION_APP_OPEN_BY_DEFAULT_SETTINGS: ClassVar[str]
    ACTION_APP_SEARCH_SETTINGS: ClassVar[str]
    ACTION_APP_USAGE_SETTINGS: ClassVar[str]
    ACTION_AUTOMATIC_ZEN_RULE_SETTINGS: ClassVar[str]
    ACTION_AUTO_ROTATE_SETTINGS: ClassVar[str]
    ACTION_BATTERY_SAVER_SETTINGS: ClassVar[str]
    ACTION_BIOMETRIC_ENROLL: ClassVar[str]
    ACTION_BLUETOOTH_SETTINGS: ClassVar[str]
    ACTION_CAPTIONING_SETTINGS: ClassVar[str]
    ACTION_CAST_SETTINGS: ClassVar[str]
    ACTION_CHANNEL_NOTIFICATION_SETTINGS: ClassVar[str]
    ACTION_CONDITION_PROVIDER_SETTINGS: ClassVar[str]
    ACTION_CREDENTIAL_PROVIDER: ClassVar[str]
    ACTION_DATA_ROAMING_SETTINGS: ClassVar[str]
    ACTION_DATA_USAGE_SETTINGS: ClassVar[str]
    ACTION_DATE_SETTINGS: ClassVar[str]
    ACTION_DEVICE_INFO_SETTINGS: ClassVar[str]
    ACTION_DISPLAY_SETTINGS: ClassVar[str]
    ACTION_DREAM_SETTINGS: ClassVar[str]
    ACTION_FINGERPRINT_ENROLL: ClassVar[str]
    ACTION_HARD_KEYBOARD_SETTINGS: ClassVar[str]
    ACTION_HOME_SETTINGS: ClassVar[str]
    ACTION_IGNORE_BACKGROUND_DATA_RESTRICTIONS_SETTINGS: ClassVar[str]
    ACTION_IGNORE_BATTERY_OPTIMIZATION_SETTINGS: ClassVar[str]
    ACTION_INPUT_METHOD_SETTINGS: ClassVar[str]
    ACTION_INPUT_METHOD_SUBTYPE_SETTINGS: ClassVar[str]
    ACTION_INTERNAL_STORAGE_SETTINGS: ClassVar[str]
    ACTION_LOCALE_SETTINGS: ClassVar[str]
    ACTION_LOCATION_SOURCE_SETTINGS: ClassVar[str]
    ACTION_MANAGE_ALL_APPLICATIONS_SETTINGS: ClassVar[str]
    ACTION_MANAGE_ALL_FILES_ACCESS_PERMISSION: ClassVar[str]
    ACTION_MANAGE_ALL_SIM_PROFILES_SETTINGS: ClassVar[str]
    ACTION_MANAGE_APPLICATIONS_SETTINGS: ClassVar[str]
    ACTION_MANAGE_APP_ALL_FILES_ACCESS_PERMISSION: ClassVar[str]
    ACTION_MANAGE_APP_USE_FULL_SCREEN_INTENT: ClassVar[str]
    ACTION_MANAGE_DEFAULT_APPS_SETTINGS: ClassVar[str]
    ACTION_MANAGE_OVERLAY_PERMISSION: ClassVar[str]
    ACTION_MANAGE_SUPERVISOR_RESTRICTED_SETTING: ClassVar[str]
    ACTION_MANAGE_UNKNOWN_APP_SOURCES: ClassVar[str]
    ACTION_MANAGE_WRITE_SETTINGS: ClassVar[str]
    ACTION_MEMORY_CARD_SETTINGS: ClassVar[str]
    ACTION_NETWORK_OPERATOR_SETTINGS: ClassVar[str]
    ACTION_NFCSHARING_SETTINGS: ClassVar[str]
    ACTION_NFC_PAYMENT_SETTINGS: ClassVar[str]
    ACTION_NFC_SETTINGS: ClassVar[str]
    ACTION_NIGHT_DISPLAY_SETTINGS: ClassVar[str]
    ACTION_NOTIFICATION_ASSISTANT_SETTINGS: ClassVar[str]
    ACTION_NOTIFICATION_LISTENER_DETAIL_SETTINGS: ClassVar[str]
    ACTION_NOTIFICATION_LISTENER_SETTINGS: ClassVar[str]
    ACTION_NOTIFICATION_POLICY_ACCESS_SETTINGS: ClassVar[str]
    ACTION_PRINT_SETTINGS: ClassVar[str]
    ACTION_PRIVACY_SETTINGS: ClassVar[str]
    ACTION_PROCESS_WIFI_EASY_CONNECT_URI: ClassVar[str]
    ACTION_QUICK_ACCESS_WALLET_SETTINGS: ClassVar[str]
    ACTION_QUICK_LAUNCH_SETTINGS: ClassVar[str]
    ACTION_REGIONAL_PREFERENCES_SETTINGS: ClassVar[str]
    ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS: ClassVar[str]
    ACTION_REQUEST_MANAGE_MEDIA: ClassVar[str]
    ACTION_REQUEST_MEDIA_ROUTING_CONTROL: ClassVar[str]
    ACTION_REQUEST_SCHEDULE_EXACT_ALARM: ClassVar[str]
    ACTION_REQUEST_SET_AUTOFILL_SERVICE: ClassVar[str]
    ACTION_SATELLITE_SETTING: ClassVar[str]
    ACTION_SEARCH_SETTINGS: ClassVar[str]
    ACTION_SECURITY_SETTINGS: ClassVar[str]
    ACTION_SETTINGS: ClassVar[str]
    ACTION_SETTINGS_EMBED_DEEP_LINK_ACTIVITY: ClassVar[str]
    ACTION_SHOW_REGULATORY_INFO: ClassVar[str]
    ACTION_SHOW_WORK_POLICY_INFO: ClassVar[str]
    ACTION_SOUND_SETTINGS: ClassVar[str]
    ACTION_STORAGE_VOLUME_ACCESS_SETTINGS: ClassVar[str]
    ACTION_SYNC_SETTINGS: ClassVar[str]
    ACTION_USAGE_ACCESS_SETTINGS: ClassVar[str]
    ACTION_USER_DICTIONARY_SETTINGS: ClassVar[str]
    ACTION_VOICE_CONTROL_AIRPLANE_MODE: ClassVar[str]
    ACTION_VOICE_CONTROL_BATTERY_SAVER_MODE: ClassVar[str]
    ACTION_VOICE_CONTROL_DO_NOT_DISTURB_MODE: ClassVar[str]
    ACTION_VOICE_INPUT_SETTINGS: ClassVar[str]
    ACTION_VPN_SETTINGS: ClassVar[str]
    ACTION_VR_LISTENER_SETTINGS: ClassVar[str]
    ACTION_WEBVIEW_SETTINGS: ClassVar[str]
    ACTION_WIFI_ADD_NETWORKS: ClassVar[str]
    ACTION_WIFI_IP_SETTINGS: ClassVar[str]
    ACTION_WIFI_SETTINGS: ClassVar[str]
    ACTION_WIRELESS_SETTINGS: ClassVar[str]
    ACTION_ZEN_MODE_PRIORITY_SETTINGS: ClassVar[str]
    ADD_WIFI_RESULT_ADD_OR_UPDATE_FAILED: ClassVar[int]
    ADD_WIFI_RESULT_ALREADY_EXISTS: ClassVar[int]
    ADD_WIFI_RESULT_SUCCESS: ClassVar[int]
    AUTHORITY: ClassVar[str]
    EXTRA_ACCOUNT_TYPES: ClassVar[str]
    EXTRA_AIRPLANE_MODE_ENABLED: ClassVar[str]
    EXTRA_APP_PACKAGE: ClassVar[str]
    EXTRA_AUTHORITIES: ClassVar[str]
    EXTRA_AUTOMATIC_ZEN_RULE_ID: ClassVar[str]
    EXTRA_BATTERY_SAVER_MODE_ENABLED: ClassVar[str]
    EXTRA_BIOMETRIC_AUTHENTICATORS_ALLOWED: ClassVar[str]
    EXTRA_CHANNEL_FILTER_LIST: ClassVar[str]
    EXTRA_CHANNEL_ID: ClassVar[str]
    EXTRA_CONVERSATION_ID: ClassVar[str]
    EXTRA_DO_NOT_DISTURB_MODE_ENABLED: ClassVar[str]
    EXTRA_DO_NOT_DISTURB_MODE_MINUTES: ClassVar[str]
    EXTRA_EASY_CONNECT_ATTEMPTED_SSID: ClassVar[str]
    EXTRA_EASY_CONNECT_BAND_LIST: ClassVar[str]
    EXTRA_EASY_CONNECT_CHANNEL_LIST: ClassVar[str]
    EXTRA_EASY_CONNECT_ERROR_CODE: ClassVar[str]
    EXTRA_INPUT_METHOD_ID: ClassVar[str]
    EXTRA_NOTIFICATION_LISTENER_COMPONENT_NAME: ClassVar[str]
    EXTRA_SETTINGS_EMBEDDED_DEEP_LINK_HIGHLIGHT_MENU_KEY: ClassVar[str]
    EXTRA_SETTINGS_EMBEDDED_DEEP_LINK_INTENT_URI: ClassVar[str]
    EXTRA_SUB_ID: ClassVar[str]
    EXTRA_SUPERVISOR_RESTRICTED_SETTING_KEY: ClassVar[str]
    EXTRA_WIFI_NETWORK_LIST: ClassVar[str]
    EXTRA_WIFI_NETWORK_RESULT_LIST: ClassVar[str]
    INTENT_CATEGORY_USAGE_ACCESS_CONFIG: ClassVar[str]
    METADATA_USAGE_ACCESS_REASON: ClassVar[str]
    SUPERVISOR_VERIFICATION_SETTING_BIOMETRICS: ClassVar[int]
    SUPERVISOR_VERIFICATION_SETTING_UNKNOWN: ClassVar[int]
    def __init__(self) -> None: ...
    @staticmethod
    def canDrawOverlays(p0: Context) -> bool: ...

    class System:
        ACCELEROMETER_ROTATION: ClassVar[str]
        ADB_ENABLED: ClassVar[str]
        AIRPLANE_MODE_ON: ClassVar[str]
        AIRPLANE_MODE_RADIOS: ClassVar[str]
        ALARM_ALERT: ClassVar[str]
        ALWAYS_FINISH_ACTIVITIES: ClassVar[str]
        ANDROID_ID: ClassVar[str]
        ANIMATOR_DURATION_SCALE: ClassVar[str]
        AUTO_TIME: ClassVar[str]
        AUTO_TIME_ZONE: ClassVar[str]
        BLUETOOTH_DISCOVERABILITY: ClassVar[str]
        BLUETOOTH_DISCOVERABILITY_TIMEOUT: ClassVar[str]
        BLUETOOTH_ON: ClassVar[str]
        CONTENT_URI: ClassVar[Uri]
        DATA_ROAMING: ClassVar[str]
        DATE_FORMAT: ClassVar[str]
        DEBUG_APP: ClassVar[str]
        DEFAULT_ALARM_ALERT_URI: ClassVar[Uri]
        DEFAULT_NOTIFICATION_URI: ClassVar[Uri]
        DEFAULT_RINGTONE_URI: ClassVar[Uri]
        DEVICE_PROVISIONED: ClassVar[str]
        DIM_SCREEN: ClassVar[str]
        DTMF_TONE_TYPE_WHEN_DIALING: ClassVar[str]
        DTMF_TONE_WHEN_DIALING: ClassVar[str]
        END_BUTTON_BEHAVIOR: ClassVar[str]
        FONT_SCALE: ClassVar[str]
        HAPTIC_FEEDBACK_ENABLED: ClassVar[str]
        HTTP_PROXY: ClassVar[str]
        INSTALL_NON_MARKET_APPS: ClassVar[str]
        LOCATION_PROVIDERS_ALLOWED: ClassVar[str]
        LOCK_PATTERN_ENABLED: ClassVar[str]
        LOCK_PATTERN_TACTILE_FEEDBACK_ENABLED: ClassVar[str]
        LOCK_PATTERN_VISIBLE: ClassVar[str]
        LOGGING_ID: ClassVar[str]
        MODE_RINGER: ClassVar[str]
        MODE_RINGER_STREAMS_AFFECTED: ClassVar[str]
        MUTE_STREAMS_AFFECTED: ClassVar[str]
        NETWORK_PREFERENCE: ClassVar[str]
        NEXT_ALARM_FORMATTED: ClassVar[str]
        NOTIFICATION_SOUND: ClassVar[str]
        PARENTAL_CONTROL_ENABLED: ClassVar[str]
        PARENTAL_CONTROL_LAST_UPDATE: ClassVar[str]
        PARENTAL_CONTROL_REDIRECT_URL: ClassVar[str]
        RADIO_BLUETOOTH: ClassVar[str]
        RADIO_CELL: ClassVar[str]
        RADIO_NFC: ClassVar[str]
        RADIO_WIFI: ClassVar[str]
        RINGTONE: ClassVar[str]
        SCREEN_BRIGHTNESS: ClassVar[str]
        SCREEN_BRIGHTNESS_MODE: ClassVar[str]
        SCREEN_BRIGHTNESS_MODE_AUTOMATIC: ClassVar[int]
        SCREEN_BRIGHTNESS_MODE_MANUAL: ClassVar[int]
        SCREEN_OFF_TIMEOUT: ClassVar[str]
        SETTINGS_CLASSNAME: ClassVar[str]
        SETUP_WIZARD_HAS_RUN: ClassVar[str]
        SHOW_GTALK_SERVICE_STATUS: ClassVar[str]
        SHOW_PROCESSES: ClassVar[str]
        SHOW_WEB_SUGGESTIONS: ClassVar[str]
        SOUND_EFFECTS_ENABLED: ClassVar[str]
        STAY_ON_WHILE_PLUGGED_IN: ClassVar[str]
        TEXT_AUTO_CAPS: ClassVar[str]
        TEXT_AUTO_PUNCTUATE: ClassVar[str]
        TEXT_AUTO_REPLACE: ClassVar[str]
        TEXT_SHOW_PASSWORD: ClassVar[str]
        TIME_12_24: ClassVar[str]
        TRANSITION_ANIMATION_SCALE: ClassVar[str]
        USB_MASS_STORAGE_ENABLED: ClassVar[str]
        USER_ROTATION: ClassVar[str]
        USE_GOOGLE_MAIL: ClassVar[str]
        VIBRATE_ON: ClassVar[str]
        VIBRATE_WHEN_RINGING: ClassVar[str]
        WAIT_FOR_DEBUGGER: ClassVar[str]
        WALLPAPER_ACTIVITY: ClassVar[str]
        WIFI_MAX_DHCP_RETRY_COUNT: ClassVar[str]
        WIFI_MOBILE_DATA_TRANSITION_WAKELOCK_TIMEOUT_MS: ClassVar[str]
        WIFI_NETWORKS_AVAILABLE_NOTIFICATION_ON: ClassVar[str]
        WIFI_NETWORKS_AVAILABLE_REPEAT_DELAY: ClassVar[str]
        WIFI_NUM_OPEN_NETWORKS_KEPT: ClassVar[str]
        WIFI_ON: ClassVar[str]
        WIFI_SLEEP_POLICY: ClassVar[str]
        WIFI_SLEEP_POLICY_DEFAULT: ClassVar[int]
        WIFI_SLEEP_POLICY_NEVER: ClassVar[int]
        WIFI_SLEEP_POLICY_NEVER_WHILE_PLUGGED: ClassVar[int]
        WIFI_STATIC_DNS1: ClassVar[str]
        WIFI_STATIC_DNS2: ClassVar[str]
        WIFI_STATIC_GATEWAY: ClassVar[str]
        WIFI_STATIC_IP: ClassVar[str]
        WIFI_STATIC_NETMASK: ClassVar[str]
        WIFI_USE_STATIC_IP: ClassVar[str]
        WIFI_WATCHDOG_ACCEPTABLE_PACKET_LOSS_PERCENTAGE: ClassVar[str]
        WIFI_WATCHDOG_AP_COUNT: ClassVar[str]
        WIFI_WATCHDOG_BACKGROUND_CHECK_DELAY_MS: ClassVar[str]
        WIFI_WATCHDOG_BACKGROUND_CHECK_ENABLED: ClassVar[str]
        WIFI_WATCHDOG_BACKGROUND_CHECK_TIMEOUT_MS: ClassVar[str]
        WIFI_WATCHDOG_INITIAL_IGNORED_PING_COUNT: ClassVar[str]
        WIFI_WATCHDOG_MAX_AP_CHECKS: ClassVar[str]
        WIFI_WATCHDOG_ON: ClassVar[str]
        WIFI_WATCHDOG_PING_COUNT: ClassVar[str]
        WIFI_WATCHDOG_PING_DELAY_MS: ClassVar[str]
        WIFI_WATCHDOG_PING_TIMEOUT_MS: ClassVar[str]
        WINDOW_ANIMATION_SCALE: ClassVar[str]
        NAME: ClassVar[str]
        VALUE: ClassVar[str]
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]
        def __init__(self) -> None: ...
        @staticmethod
        def getUriFor(p0: str) -> Uri: ...
        @staticmethod
        def putConfiguration(p0: ContentResolver, p1: Configuration) -> bool: ...
        @staticmethod
        def getShowGTalkServiceStatus(p0: ContentResolver) -> bool: ...
        @staticmethod
        def setShowGTalkServiceStatus(p0: ContentResolver, p1: bool) -> None: ...
        @staticmethod
        def getConfiguration(p0: ContentResolver, p1: Configuration) -> None: ...
        @staticmethod
        def putString(p0: ContentResolver, p1: str, p2: str) -> bool: ...
        @staticmethod
        def getString(p0: ContentResolver, p1: str) -> str: ...
        @staticmethod
        def canWrite(p0: Context) -> bool: ...
        @overload
        @staticmethod
        def getInt(p0: ContentResolver, p1: str) -> int: ...
        @overload
        @staticmethod
        def getInt(p0: ContentResolver, p1: str, p2: int) -> int: ...
        @staticmethod
        def putInt(p0: ContentResolver, p1: str, p2: int) -> bool: ...
        @overload
        @staticmethod
        def getLong(p0: ContentResolver, p1: str) -> int: ...
        @overload
        @staticmethod
        def getLong(p0: ContentResolver, p1: str, p2: int) -> int: ...
        @staticmethod
        def putLong(p0: ContentResolver, p1: str, p2: int) -> bool: ...
        @overload
        @staticmethod
        def getFloat(p0: ContentResolver, p1: str, p2: float) -> float: ...
        @overload
        @staticmethod
        def getFloat(p0: ContentResolver, p1: str) -> float: ...
        @staticmethod
        def putFloat(p0: ContentResolver, p1: str, p2: float) -> bool: ...

    class SettingNotFoundException:
        def __init__(self, p0: str) -> None: ...

    class Secure:
        ACCESSIBILITY_DISPLAY_INVERSION_ENABLED: ClassVar[str]
        ACCESSIBILITY_ENABLED: ClassVar[str]
        ACCESSIBILITY_SPEAK_PASSWORD: ClassVar[str]
        ADB_ENABLED: ClassVar[str]
        ALLOWED_GEOLOCATION_ORIGINS: ClassVar[str]
        ALLOW_MOCK_LOCATION: ClassVar[str]
        ANDROID_ID: ClassVar[str]
        BACKGROUND_DATA: ClassVar[str]
        BLUETOOTH_ON: ClassVar[str]
        CONTENT_URI: ClassVar[Uri]
        DATA_ROAMING: ClassVar[str]
        DEFAULT_INPUT_METHOD: ClassVar[str]
        DEVELOPMENT_SETTINGS_ENABLED: ClassVar[str]
        DEVICE_PROVISIONED: ClassVar[str]
        ENABLED_ACCESSIBILITY_SERVICES: ClassVar[str]
        ENABLED_INPUT_METHODS: ClassVar[str]
        HTTP_PROXY: ClassVar[str]
        INPUT_METHOD_SELECTOR_VISIBILITY: ClassVar[str]
        INSTALL_NON_MARKET_APPS: ClassVar[str]
        LOCATION_MODE: ClassVar[str]
        LOCATION_MODE_BATTERY_SAVING: ClassVar[int]
        LOCATION_MODE_HIGH_ACCURACY: ClassVar[int]
        LOCATION_MODE_OFF: ClassVar[int]
        LOCATION_MODE_SENSORS_ONLY: ClassVar[int]
        LOCATION_PROVIDERS_ALLOWED: ClassVar[str]
        LOCK_PATTERN_ENABLED: ClassVar[str]
        LOCK_PATTERN_TACTILE_FEEDBACK_ENABLED: ClassVar[str]
        LOCK_PATTERN_VISIBLE: ClassVar[str]
        LOGGING_ID: ClassVar[str]
        NETWORK_PREFERENCE: ClassVar[str]
        PARENTAL_CONTROL_ENABLED: ClassVar[str]
        PARENTAL_CONTROL_LAST_UPDATE: ClassVar[str]
        PARENTAL_CONTROL_REDIRECT_URL: ClassVar[str]
        RTT_CALLING_MODE: ClassVar[str]
        SECURE_FRP_MODE: ClassVar[str]
        SELECTED_INPUT_METHOD_SUBTYPE: ClassVar[str]
        SETTINGS_CLASSNAME: ClassVar[str]
        SKIP_FIRST_USE_HINTS: ClassVar[str]
        TOUCH_EXPLORATION_ENABLED: ClassVar[str]
        TTS_DEFAULT_COUNTRY: ClassVar[str]
        TTS_DEFAULT_LANG: ClassVar[str]
        TTS_DEFAULT_PITCH: ClassVar[str]
        TTS_DEFAULT_RATE: ClassVar[str]
        TTS_DEFAULT_SYNTH: ClassVar[str]
        TTS_DEFAULT_VARIANT: ClassVar[str]
        TTS_ENABLED_PLUGINS: ClassVar[str]
        TTS_USE_DEFAULTS: ClassVar[str]
        USB_MASS_STORAGE_ENABLED: ClassVar[str]
        USE_GOOGLE_MAIL: ClassVar[str]
        WIFI_MAX_DHCP_RETRY_COUNT: ClassVar[str]
        WIFI_MOBILE_DATA_TRANSITION_WAKELOCK_TIMEOUT_MS: ClassVar[str]
        WIFI_NETWORKS_AVAILABLE_NOTIFICATION_ON: ClassVar[str]
        WIFI_NETWORKS_AVAILABLE_REPEAT_DELAY: ClassVar[str]
        WIFI_NUM_OPEN_NETWORKS_KEPT: ClassVar[str]
        WIFI_ON: ClassVar[str]
        WIFI_WATCHDOG_ACCEPTABLE_PACKET_LOSS_PERCENTAGE: ClassVar[str]
        WIFI_WATCHDOG_AP_COUNT: ClassVar[str]
        WIFI_WATCHDOG_BACKGROUND_CHECK_DELAY_MS: ClassVar[str]
        WIFI_WATCHDOG_BACKGROUND_CHECK_ENABLED: ClassVar[str]
        WIFI_WATCHDOG_BACKGROUND_CHECK_TIMEOUT_MS: ClassVar[str]
        WIFI_WATCHDOG_INITIAL_IGNORED_PING_COUNT: ClassVar[str]
        WIFI_WATCHDOG_MAX_AP_CHECKS: ClassVar[str]
        WIFI_WATCHDOG_ON: ClassVar[str]
        WIFI_WATCHDOG_PING_COUNT: ClassVar[str]
        WIFI_WATCHDOG_PING_DELAY_MS: ClassVar[str]
        WIFI_WATCHDOG_PING_TIMEOUT_MS: ClassVar[str]
        WIFI_WATCHDOG_WATCH_LIST: ClassVar[str]
        NAME: ClassVar[str]
        VALUE: ClassVar[str]
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]
        def __init__(self) -> None: ...
        @staticmethod
        def getUriFor(p0: str) -> Uri: ...
        @staticmethod
        def isLocationProviderEnabled(p0: ContentResolver, p1: str) -> bool: ...
        @staticmethod
        def setLocationProviderEnabled(p0: ContentResolver, p1: str, p2: bool) -> None: ...
        @staticmethod
        def putString(p0: ContentResolver, p1: str, p2: str) -> bool: ...
        @staticmethod
        def getString(p0: ContentResolver, p1: str) -> str: ...
        @overload
        @staticmethod
        def getInt(p0: ContentResolver, p1: str) -> int: ...
        @overload
        @staticmethod
        def getInt(p0: ContentResolver, p1: str, p2: int) -> int: ...
        @staticmethod
        def putInt(p0: ContentResolver, p1: str, p2: int) -> bool: ...
        @overload
        @staticmethod
        def getLong(p0: ContentResolver, p1: str) -> int: ...
        @overload
        @staticmethod
        def getLong(p0: ContentResolver, p1: str, p2: int) -> int: ...
        @staticmethod
        def putLong(p0: ContentResolver, p1: str, p2: int) -> bool: ...
        @overload
        @staticmethod
        def getFloat(p0: ContentResolver, p1: str) -> float: ...
        @overload
        @staticmethod
        def getFloat(p0: ContentResolver, p1: str, p2: float) -> float: ...
        @staticmethod
        def putFloat(p0: ContentResolver, p1: str, p2: float) -> bool: ...

    class Panel:
        ACTION_INTERNET_CONNECTIVITY: ClassVar[str]
        ACTION_NFC: ClassVar[str]
        ACTION_VOLUME: ClassVar[str]
        ACTION_WIFI: ClassVar[str]

    class NameValueTable:
        NAME: ClassVar[str]
        VALUE: ClassVar[str]
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]
        def __init__(self) -> None: ...
        @staticmethod
        def getUriFor(p0: Uri, p1: str) -> Uri: ...

    class Global:
        ADB_ENABLED: ClassVar[str]
        AIRPLANE_MODE_ON: ClassVar[str]
        AIRPLANE_MODE_RADIOS: ClassVar[str]
        ALWAYS_FINISH_ACTIVITIES: ClassVar[str]
        ANIMATOR_DURATION_SCALE: ClassVar[str]
        APPLY_RAMPING_RINGER: ClassVar[str]
        AUTO_TIME: ClassVar[str]
        AUTO_TIME_ZONE: ClassVar[str]
        BLUETOOTH_ON: ClassVar[str]
        BOOT_COUNT: ClassVar[str]
        CONTACT_METADATA_SYNC_ENABLED: ClassVar[str]
        CONTENT_URI: ClassVar[Uri]
        DATA_ROAMING: ClassVar[str]
        DEBUG_APP: ClassVar[str]
        DEVELOPMENT_SETTINGS_ENABLED: ClassVar[str]
        DEVICE_NAME: ClassVar[str]
        DEVICE_PROVISIONED: ClassVar[str]
        HTTP_PROXY: ClassVar[str]
        INSTALL_NON_MARKET_APPS: ClassVar[str]
        MODE_RINGER: ClassVar[str]
        NETWORK_PREFERENCE: ClassVar[str]
        RADIO_BLUETOOTH: ClassVar[str]
        RADIO_CELL: ClassVar[str]
        RADIO_NFC: ClassVar[str]
        RADIO_WIFI: ClassVar[str]
        SECURE_FRP_MODE: ClassVar[str]
        SHOW_PROCESSES: ClassVar[str]
        STAY_ON_WHILE_PLUGGED_IN: ClassVar[str]
        TRANSITION_ANIMATION_SCALE: ClassVar[str]
        USB_MASS_STORAGE_ENABLED: ClassVar[str]
        USE_GOOGLE_MAIL: ClassVar[str]
        WAIT_FOR_DEBUGGER: ClassVar[str]
        WIFI_DEVICE_OWNER_CONFIGS_LOCKDOWN: ClassVar[str]
        WIFI_MAX_DHCP_RETRY_COUNT: ClassVar[str]
        WIFI_MOBILE_DATA_TRANSITION_WAKELOCK_TIMEOUT_MS: ClassVar[str]
        WIFI_NETWORKS_AVAILABLE_NOTIFICATION_ON: ClassVar[str]
        WIFI_NETWORKS_AVAILABLE_REPEAT_DELAY: ClassVar[str]
        WIFI_NUM_OPEN_NETWORKS_KEPT: ClassVar[str]
        WIFI_ON: ClassVar[str]
        WIFI_SLEEP_POLICY: ClassVar[str]
        WIFI_SLEEP_POLICY_DEFAULT: ClassVar[int]
        WIFI_SLEEP_POLICY_NEVER: ClassVar[int]
        WIFI_SLEEP_POLICY_NEVER_WHILE_PLUGGED: ClassVar[int]
        WIFI_WATCHDOG_ON: ClassVar[str]
        WINDOW_ANIMATION_SCALE: ClassVar[str]
        NAME: ClassVar[str]
        VALUE: ClassVar[str]
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]
        def __init__(self) -> None: ...
        @staticmethod
        def getUriFor(p0: str) -> Uri: ...
        @staticmethod
        def putString(p0: ContentResolver, p1: str, p2: str) -> bool: ...
        @staticmethod
        def getString(p0: ContentResolver, p1: str) -> str: ...
        @overload
        @staticmethod
        def getInt(p0: ContentResolver, p1: str, p2: int) -> int: ...
        @overload
        @staticmethod
        def getInt(p0: ContentResolver, p1: str) -> int: ...
        @staticmethod
        def putInt(p0: ContentResolver, p1: str, p2: int) -> bool: ...
        @overload
        @staticmethod
        def getLong(p0: ContentResolver, p1: str, p2: int) -> int: ...
        @overload
        @staticmethod
        def getLong(p0: ContentResolver, p1: str) -> int: ...
        @staticmethod
        def putLong(p0: ContentResolver, p1: str, p2: int) -> bool: ...
        @overload
        @staticmethod
        def getFloat(p0: ContentResolver, p1: str, p2: float) -> float: ...
        @overload
        @staticmethod
        def getFloat(p0: ContentResolver, p1: str) -> float: ...
        @staticmethod
        def putFloat(p0: ContentResolver, p1: str, p2: float) -> bool: ...
