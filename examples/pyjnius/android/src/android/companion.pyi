from typing import Any, ClassVar, overload

class DeviceNotAssociatedException:
    ...

from typing import Any, ClassVar, overload
from android.companion.DeviceFilter import DeviceFilter
from android.os.Parcel import Parcel

class AssociationRequest:
    CREATOR: ClassVar[Any]
    DEVICE_PROFILE_APP_STREAMING: ClassVar[str]
    DEVICE_PROFILE_AUTOMOTIVE_PROJECTION: ClassVar[str]
    DEVICE_PROFILE_COMPUTER: ClassVar[str]
    DEVICE_PROFILE_GLASSES: ClassVar[str]
    DEVICE_PROFILE_NEARBY_DEVICE_STREAMING: ClassVar[str]
    DEVICE_PROFILE_WATCH: ClassVar[str]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getDeviceProfile(self) -> str: ...
    def isForceConfirmation(self) -> bool: ...
    def isSelfManaged(self) -> bool: ...
    def isSingleDevice(self) -> bool: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getDisplayName(self) -> str: ...

    class Builder:
        def __init__(self) -> None: ...
        def setDeviceProfile(self, p0: str) -> Any: ...
        def addDeviceFilter(self, p0: DeviceFilter) -> Any: ...
        def setForceConfirmation(self, p0: bool) -> Any: ...
        def setSelfManaged(self, p0: bool) -> Any: ...
        def setSingleDevice(self, p0: bool) -> Any: ...
        def setDisplayName(self, p0: str) -> Any: ...
        def build(self) -> "AssociationRequest": ...

from typing import Any, ClassVar, overload
from android.companion.AssociatedDevice import AssociatedDevice
from android.companion.DeviceId import DeviceId
from android.net.MacAddress import MacAddress
from android.os.Parcel import Parcel

class AssociationInfo:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getDeviceProfile(self) -> str: ...
    def isSelfManaged(self) -> bool: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def getId(self) -> int: ...
    def getDeviceId(self) -> DeviceId: ...
    def getAssociatedDevice(self) -> AssociatedDevice: ...
    def getDeviceMacAddress(self) -> MacAddress: ...
    def getSystemDataSyncFlags(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getDisplayName(self) -> str: ...

from typing import Any, ClassVar, overload
from android.net.MacAddress import MacAddress
from android.os.Parcel import Parcel
from java.util.regex.Pattern import Pattern

class WifiDeviceFilter:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def equals(self, p0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class Builder:
        def __init__(self) -> None: ...
        def setBssid(self, p0: MacAddress) -> Any: ...
        def setBssidMask(self, p0: MacAddress) -> Any: ...
        def setNamePattern(self, p0: Pattern) -> Any: ...
        def build(self) -> "WifiDeviceFilter": ...

from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothDevice import BluetoothDevice
from android.bluetooth.le.ScanResult import ScanResult
from android.net.wifi.ScanResult import ScanResult
from android.os.Parcel import Parcel

class AssociatedDevice:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getBleDevice(self) -> ScanResult: ...
    def getBluetoothDevice(self) -> BluetoothDevice: ...
    def getWifiDevice(self) -> ScanResult: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.os.ParcelUuid import ParcelUuid
from java.util.regex.Pattern import Pattern

class BluetoothDeviceFilter:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class Builder:
        def __init__(self) -> None: ...
        def setAddress(self, p0: str) -> Any: ...
        def addServiceUuid(self, p0: ParcelUuid, p1: ParcelUuid) -> Any: ...
        def setNamePattern(self, p0: Pattern) -> Any: ...
        def build(self) -> "BluetoothDeviceFilter": ...

from typing import Any, ClassVar, overload
from android.companion.AssociationInfo import AssociationInfo
from android.companion.AssociationRequest import AssociationRequest
from android.companion.DeviceId import DeviceId
from android.companion.ObservingDevicePresenceRequest import ObservingDevicePresenceRequest
from android.content.ComponentName import ComponentName
from android.content.IntentSender import IntentSender
from android.os.Handler import Handler
from android.os.OutcomeReceiver import OutcomeReceiver
from java.io.InputStream import InputStream
from java.io.OutputStream import OutputStream
from java.util.concurrent.Executor import Executor

class CompanionDeviceManager:
    EXTRA_ASSOCIATION: ClassVar[str]
    EXTRA_DEVICE: ClassVar[str]
    FLAG_CALL_METADATA: ClassVar[int]
    RESULT_CANCELED: ClassVar[int]
    RESULT_DISCOVERY_TIMEOUT: ClassVar[int]
    RESULT_INTERNAL_ERROR: ClassVar[int]
    RESULT_OK: ClassVar[int]
    RESULT_SECURITY_ERROR: ClassVar[int]
    RESULT_USER_REJECTED: ClassVar[int]
    @overload
    def associate(self, p0: AssociationRequest, p1: Executor, p2: Any) -> None: ...
    @overload
    def associate(self, p0: AssociationRequest, p1: Any, p2: Handler) -> None: ...
    def attachSystemDataTransport(self, p0: int, p1: InputStream, p2: OutputStream) -> None: ...
    def buildAssociationCancellationIntent(self) -> IntentSender: ...
    def buildPermissionTransferUserConsentIntent(self, p0: int) -> IntentSender: ...
    def detachSystemDataTransport(self, p0: int) -> None: ...
    def disableSystemDataSyncForTypes(self, p0: int, p1: int) -> None: ...
    @overload
    def disassociate(self, p0: int) -> None: ...
    @overload
    def disassociate(self, p0: str) -> None: ...
    def enableSystemDataSyncForTypes(self, p0: int, p1: int) -> None: ...
    def getAssociations(self) -> list: ...
    def getMyAssociations(self) -> list: ...
    def hasNotificationAccess(self, p0: ComponentName) -> bool: ...
    def isPermissionTransferUserConsented(self, p0: int) -> bool: ...
    def removeBond(self, p0: int) -> bool: ...
    def requestNotificationAccess(self, p0: ComponentName) -> None: ...
    @overload
    def startObservingDevicePresence(self, p0: ObservingDevicePresenceRequest) -> None: ...
    @overload
    def startObservingDevicePresence(self, p0: str) -> None: ...
    def startSystemDataTransfer(self, p0: int, p1: Executor, p2: OutcomeReceiver) -> None: ...
    @overload
    def stopObservingDevicePresence(self, p0: ObservingDevicePresenceRequest) -> None: ...
    @overload
    def stopObservingDevicePresence(self, p0: str) -> None: ...
    def setDeviceId(self, p0: int, p1: DeviceId) -> None: ...

    class Callback:
        def __init__(self) -> None: ...
        @overload
        def onFailure(self, p0: int, p1: str) -> None: ...
        @overload
        def onFailure(self, p0: str) -> None: ...
        def onAssociationCreated(self, p0: AssociationInfo) -> None: ...
        def onAssociationPending(self, p0: IntentSender) -> None: ...
        def onDeviceFound(self, p0: IntentSender) -> None: ...

from typing import Any, ClassVar, overload
from android.bluetooth.le.ScanFilter import ScanFilter
from android.os.Parcel import Parcel
from java.nio.ByteOrder import ByteOrder
from java.util.regex.Pattern import Pattern

class BluetoothLeDeviceFilter:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    @staticmethod
    def getRenamePrefixLengthLimit() -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class Builder:
        def __init__(self) -> None: ...
        def setNamePattern(self, p0: Pattern) -> Any: ...
        def setRawDataFilter(self, p0: Any, p1: Any) -> Any: ...
        def setRenameFromBytes(self, p0: str, p1: str, p2: int, p3: int, p4: ByteOrder) -> Any: ...
        def setRenameFromName(self, p0: str, p1: str, p2: int, p3: int) -> Any: ...
        def setScanFilter(self, p0: ScanFilter) -> Any: ...
        def build(self) -> "BluetoothLeDeviceFilter": ...

from typing import Any, ClassVar, overload

class DeviceFilter:
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]

from typing import Any, ClassVar, overload
from android.companion.AssociationInfo import AssociationInfo
from android.companion.DevicePresenceEvent import DevicePresenceEvent
from android.content.Intent import Intent
from android.os.IBinder import IBinder
from java.io.InputStream import InputStream
from java.io.OutputStream import OutputStream

class CompanionDeviceService:
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
    @overload
    def onDeviceAppeared(self, p0: AssociationInfo) -> None: ...
    @overload
    def onDeviceAppeared(self, p0: str) -> None: ...
    @overload
    def onDeviceDisappeared(self, p0: AssociationInfo) -> None: ...
    @overload
    def onDeviceDisappeared(self, p0: str) -> None: ...
    def onDevicePresenceEvent(self, p0: DevicePresenceEvent) -> None: ...
    def attachSystemDataTransport(self, p0: int, p1: InputStream, p2: OutputStream) -> None: ...
    def detachSystemDataTransport(self, p0: int) -> None: ...
    def onBind(self, p0: Intent) -> IBinder: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.os.ParcelUuid import ParcelUuid

class DevicePresenceEvent:
    CREATOR: ClassVar[Any]
    EVENT_BLE_APPEARED: ClassVar[int]
    EVENT_BLE_DISAPPEARED: ClassVar[int]
    EVENT_BT_CONNECTED: ClassVar[int]
    EVENT_BT_DISCONNECTED: ClassVar[int]
    EVENT_SELF_MANAGED_APPEARED: ClassVar[int]
    EVENT_SELF_MANAGED_DISAPPEARED: ClassVar[int]
    NO_ASSOCIATION: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: ParcelUuid) -> None: ...
    def getUuid(self) -> ParcelUuid: ...
    def getAssociationId(self) -> int: ...
    def getEvent(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.net.MacAddress import MacAddress
from android.os.Parcel import Parcel

class DeviceId:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getCustomId(self) -> str: ...
    def getMacAddress(self) -> MacAddress: ...

    class Builder:
        def __init__(self) -> None: ...
        def setCustomId(self, p0: str) -> Any: ...
        def setMacAddress(self, p0: MacAddress) -> Any: ...
        def build(self) -> "DeviceId": ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.os.ParcelUuid import ParcelUuid

class ObservingDevicePresenceRequest:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getUuid(self) -> ParcelUuid: ...
    def getAssociationId(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class Builder:
        def __init__(self) -> None: ...
        def setUuid(self, p0: ParcelUuid) -> Any: ...
        def setAssociationId(self, p0: int) -> Any: ...
        def build(self) -> "ObservingDevicePresenceRequest": ...

from typing import Any, ClassVar, overload

class CompanionException:
    ...

