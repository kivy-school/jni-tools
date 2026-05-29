from typing import Any, ClassVar, overload
from android.app.Fragment import Fragment
from android.content.Intent import Intent
from android.content.res.Resources import Resources
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel
from android.preference.Preference import Preference
from android.preference.PreferenceFragment import PreferenceFragment
from android.preference.PreferenceManager import PreferenceManager
from android.preference.PreferenceScreen import PreferenceScreen
from android.view.MenuItem import MenuItem
from android.view.View import View

class PreferenceActivity:
    EXTRA_NO_HEADERS: ClassVar[str]
    EXTRA_SHOW_FRAGMENT: ClassVar[str]
    EXTRA_SHOW_FRAGMENT_ARGUMENTS: ClassVar[str]
    EXTRA_SHOW_FRAGMENT_SHORT_TITLE: ClassVar[str]
    EXTRA_SHOW_FRAGMENT_TITLE: ClassVar[str]
    HEADER_ID_UNDEFINED: ClassVar[int]
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
    def findPreference(self, p0: str) -> Preference: ...
    def addPreferencesFromResource(self, p0: int) -> None: ...
    def onPreferenceTreeClick(self, p0: PreferenceScreen, p1: Preference) -> bool: ...
    def setPreferenceScreen(self, p0: PreferenceScreen) -> None: ...
    def addPreferencesFromIntent(self, p0: Intent) -> None: ...
    def getPreferenceManager(self) -> PreferenceManager: ...
    def getPreferenceScreen(self) -> PreferenceScreen: ...
    def setParentTitle(self, p0: str, p1: str, p2: Any) -> None: ...
    def onHeaderClick(self, p0: Any, p1: int) -> None: ...
    def isMultiPane(self) -> bool: ...
    def onGetNewHeader(self) -> Any: ...
    def onGetInitialHeader(self) -> Any: ...
    def onBuildHeaders(self, p0: list) -> None: ...
    def invalidateHeaders(self) -> None: ...
    def hasHeaders(self) -> bool: ...
    def loadHeadersFromResource(self, p0: int, p1: list) -> None: ...
    def onBuildStartFragmentIntent(self, p0: str, p1: Bundle, p2: int, p3: int) -> Intent: ...
    def showBreadCrumbs(self, p0: str, p1: str) -> None: ...
    def startPreferenceFragment(self, p0: Fragment, p1: bool) -> None: ...
    def startPreferencePanel(self, p0: str, p1: Bundle, p2: int, p3: str, p4: Fragment, p5: int) -> None: ...
    def onIsHidingHeaders(self) -> bool: ...
    def setListFooter(self, p0: View) -> None: ...
    def finishPreferencePanel(self, p0: Fragment, p1: int, p2: Intent) -> None: ...
    def onIsMultiPane(self) -> bool: ...
    @overload
    def startWithFragment(self, p0: str, p1: Bundle, p2: Fragment, p3: int, p4: int, p5: int) -> None: ...
    @overload
    def startWithFragment(self, p0: str, p1: Bundle, p2: Fragment, p3: int) -> None: ...
    @overload
    def switchToHeader(self, p0: Any) -> None: ...
    @overload
    def switchToHeader(self, p0: str, p1: Bundle) -> None: ...
    def onPreferenceStartFragment(self, p0: PreferenceFragment, p1: Preference) -> bool: ...
    def onBackPressed(self) -> None: ...
    def onOptionsItemSelected(self, p0: MenuItem) -> bool: ...
    def onContentChanged(self) -> None: ...

    class Header:
        CREATOR: ClassVar[Any]
        CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
        PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
        breadCrumbShortTitle: str
        breadCrumbShortTitleRes: int
        breadCrumbTitle: str
        breadCrumbTitleRes: int
        extras: Bundle
        fragment: str
        fragmentArguments: Bundle
        iconRes: int
        id: int
        intent: Intent
        summary: str
        summaryRes: int
        title: str
        titleRes: int
        def __init__(self) -> None: ...
        def getSummary(self, p0: Resources) -> str: ...
        def getBreadCrumbShortTitle(self, p0: Resources) -> str: ...
        def getBreadCrumbTitle(self, p0: Resources) -> str: ...
        def getTitle(self, p0: Resources) -> str: ...
        def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
        def readFromParcel(self, p0: Parcel) -> None: ...
        def describeContents(self) -> int: ...
