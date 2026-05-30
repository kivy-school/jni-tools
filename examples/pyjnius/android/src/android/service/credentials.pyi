from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel
from android.service.credentials.CallingAppInfo import CallingAppInfo

class ClearCredentialStateRequest:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: CallingAppInfo, p1: Bundle) -> None: ...
    def getCallingAppInfo(self) -> CallingAppInfo: ...
    def getData(self) -> Bundle: ...
    def toString(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.service.credentials.CallingAppInfo import CallingAppInfo

class GetCredentialRequest:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: CallingAppInfo, p1: list) -> None: ...
    def getCredentialOptions(self) -> list: ...
    def getCallingAppInfo(self) -> CallingAppInfo: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel
from android.service.credentials.CallingAppInfo import CallingAppInfo

class CreateCredentialRequest:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: CallingAppInfo, p1: str, p2: Bundle) -> None: ...
    def getCallingAppInfo(self) -> CallingAppInfo: ...
    def getData(self) -> Bundle: ...
    def getType(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.app.slice.Slice import Slice
from android.os.Parcel import Parcel

class Action:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: Slice) -> None: ...
    def getSlice(self) -> Slice: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.app.slice.Slice import Slice
from android.os.Parcel import Parcel
from android.service.credentials.BeginGetCredentialOption import BeginGetCredentialOption

class CredentialEntry:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    @overload
    def __init__(self, p0: BeginGetCredentialOption, p1: Slice) -> None: ...
    @overload
    def __init__(self, p0: str, p1: Slice) -> None: ...
    @overload
    def __init__(self, p0: str, p1: str, p2: Slice) -> None: ...
    def getSlice(self) -> Slice: ...
    def getBeginGetCredentialOptionId(self) -> str: ...
    def getType(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.service.credentials.CreateEntry import CreateEntry
from android.service.credentials.RemoteEntry import RemoteEntry

class BeginCreateCredentialResponse:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self) -> None: ...
    def getRemoteCreateEntry(self) -> RemoteEntry: ...
    def getCreateEntries(self) -> list: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class Builder:
        def __init__(self) -> None: ...
        def addCreateEntry(self, p0: CreateEntry) -> Any: ...
        def setCreateEntries(self, p0: list) -> Any: ...
        def setRemoteCreateEntry(self, p0: RemoteEntry) -> Any: ...
        def build(self) -> "BeginCreateCredentialResponse": ...

from typing import Any, ClassVar, overload
from android.app.slice.Slice import Slice
from android.os.Parcel import Parcel

class CreateEntry:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: Slice) -> None: ...
    def getSlice(self) -> Slice: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.content.Intent import Intent
from android.os.CancellationSignal import CancellationSignal
from android.os.IBinder import IBinder
from android.os.OutcomeReceiver import OutcomeReceiver
from android.service.credentials.BeginCreateCredentialRequest import BeginCreateCredentialRequest
from android.service.credentials.BeginGetCredentialRequest import BeginGetCredentialRequest
from android.service.credentials.ClearCredentialStateRequest import ClearCredentialStateRequest

class CredentialProviderService:
    EXTRA_BEGIN_GET_CREDENTIAL_REQUEST: ClassVar[str]
    EXTRA_BEGIN_GET_CREDENTIAL_RESPONSE: ClassVar[str]
    EXTRA_CREATE_CREDENTIAL_EXCEPTION: ClassVar[str]
    EXTRA_CREATE_CREDENTIAL_REQUEST: ClassVar[str]
    EXTRA_CREATE_CREDENTIAL_RESPONSE: ClassVar[str]
    EXTRA_GET_CREDENTIAL_EXCEPTION: ClassVar[str]
    EXTRA_GET_CREDENTIAL_REQUEST: ClassVar[str]
    EXTRA_GET_CREDENTIAL_RESPONSE: ClassVar[str]
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
    def onBeginCreateCredential(self, p0: BeginCreateCredentialRequest, p1: CancellationSignal, p2: OutcomeReceiver) -> None: ...
    def onBeginGetCredential(self, p0: BeginGetCredentialRequest, p1: CancellationSignal, p2: OutcomeReceiver) -> None: ...
    def onClearCredentialState(self, p0: ClearCredentialStateRequest, p1: CancellationSignal, p2: OutcomeReceiver) -> None: ...
    def onBind(self, p0: Intent) -> IBinder: ...
    def onCreate(self) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel
from android.service.credentials.CallingAppInfo import CallingAppInfo

class BeginCreateCredentialRequest:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    @overload
    def __init__(self, p0: str, p1: Bundle) -> None: ...
    @overload
    def __init__(self, p0: str, p1: Bundle, p2: CallingAppInfo) -> None: ...
    def getCallingAppInfo(self) -> CallingAppInfo: ...
    def getData(self) -> Bundle: ...
    def getType(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.content.pm.SigningInfo import SigningInfo
from android.os.Parcel import Parcel

class CallingAppInfo:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    @overload
    def __init__(self, p0: str, p1: SigningInfo) -> None: ...
    @overload
    def __init__(self, p0: str, p1: SigningInfo, p2: str) -> None: ...
    def getOrigin(self) -> str: ...
    def toString(self) -> str: ...
    def getPackageName(self) -> str: ...
    def getSigningInfo(self) -> SigningInfo: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.service.credentials.BeginGetCredentialOption import BeginGetCredentialOption
from android.service.credentials.CallingAppInfo import CallingAppInfo

class BeginGetCredentialRequest:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getCallingAppInfo(self) -> CallingAppInfo: ...
    def getBeginGetCredentialOptions(self) -> list: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class Builder:
        def __init__(self) -> None: ...
        def setCallingAppInfo(self, p0: CallingAppInfo) -> Any: ...
        def addBeginGetCredentialOption(self, p0: BeginGetCredentialOption) -> Any: ...
        def setBeginGetCredentialOptions(self, p0: list) -> Any: ...
        def build(self) -> "BeginGetCredentialRequest": ...

from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel

class BeginGetCredentialOption:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: str, p1: str, p2: Bundle) -> None: ...
    def toString(self) -> str: ...
    def getId(self) -> str: ...
    def getType(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getCandidateQueryData(self) -> Bundle: ...

from typing import Any, ClassVar, overload
from android.app.slice.Slice import Slice
from android.os.Parcel import Parcel

class RemoteEntry:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: Slice) -> None: ...
    def getSlice(self) -> Slice: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.service.credentials.Action import Action
from android.service.credentials.CredentialEntry import CredentialEntry
from android.service.credentials.RemoteEntry import RemoteEntry

class BeginGetCredentialResponse:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self) -> None: ...
    def getCredentialEntries(self) -> list: ...
    def getRemoteCredentialEntry(self) -> RemoteEntry: ...
    def getAuthenticationActions(self) -> list: ...
    def getActions(self) -> list: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class Builder:
        def __init__(self) -> None: ...
        def addAuthenticationAction(self, p0: Action) -> Any: ...
        def addCredentialEntry(self, p0: CredentialEntry) -> Any: ...
        def setActions(self, p0: list) -> Any: ...
        def setAuthenticationActions(self, p0: list) -> Any: ...
        def setCredentialEntries(self, p0: list) -> Any: ...
        def setRemoteCredentialEntry(self, p0: RemoteEntry) -> Any: ...
        def build(self) -> "BeginGetCredentialResponse": ...
        def addAction(self, p0: Action) -> Any: ...

