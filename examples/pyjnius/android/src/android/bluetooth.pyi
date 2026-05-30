from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class BluetoothHidDeviceAppSdpSettings:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: str, p1: str, p2: str, p3: int, p4: Any) -> None: ...
    def getDescriptors(self) -> Any: ...
    def getSubclass(self) -> int: ...
    def getProvider(self) -> str: ...
    def getName(self) -> str: ...
    def getDescription(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class BluetoothClass:
    CREATOR: ClassVar[Any]
    PROFILE_A2DP: ClassVar[int]
    PROFILE_HEADSET: ClassVar[int]
    PROFILE_HID: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getDeviceClass(self) -> int: ...
    def doesClassMatch(self, p0: int) -> bool: ...
    def getMajorDeviceClass(self) -> int: ...
    def hasService(self, p0: int) -> bool: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class Service:
        AUDIO: ClassVar[int]
        CAPTURE: ClassVar[int]
        INFORMATION: ClassVar[int]
        LE_AUDIO: ClassVar[int]
        LIMITED_DISCOVERABILITY: ClassVar[int]
        NETWORKING: ClassVar[int]
        OBJECT_TRANSFER: ClassVar[int]
        POSITIONING: ClassVar[int]
        RENDER: ClassVar[int]
        TELEPHONY: ClassVar[int]
        def __init__(self) -> None: ...

    class Device:
        AUDIO_VIDEO_CAMCORDER: ClassVar[int]
        AUDIO_VIDEO_CAR_AUDIO: ClassVar[int]
        AUDIO_VIDEO_HANDSFREE: ClassVar[int]
        AUDIO_VIDEO_HEADPHONES: ClassVar[int]
        AUDIO_VIDEO_HIFI_AUDIO: ClassVar[int]
        AUDIO_VIDEO_LOUDSPEAKER: ClassVar[int]
        AUDIO_VIDEO_MICROPHONE: ClassVar[int]
        AUDIO_VIDEO_PORTABLE_AUDIO: ClassVar[int]
        AUDIO_VIDEO_SET_TOP_BOX: ClassVar[int]
        AUDIO_VIDEO_UNCATEGORIZED: ClassVar[int]
        AUDIO_VIDEO_VCR: ClassVar[int]
        AUDIO_VIDEO_VIDEO_CAMERA: ClassVar[int]
        AUDIO_VIDEO_VIDEO_CONFERENCING: ClassVar[int]
        AUDIO_VIDEO_VIDEO_DISPLAY_AND_LOUDSPEAKER: ClassVar[int]
        AUDIO_VIDEO_VIDEO_GAMING_TOY: ClassVar[int]
        AUDIO_VIDEO_VIDEO_MONITOR: ClassVar[int]
        AUDIO_VIDEO_WEARABLE_HEADSET: ClassVar[int]
        COMPUTER_DESKTOP: ClassVar[int]
        COMPUTER_HANDHELD_PC_PDA: ClassVar[int]
        COMPUTER_LAPTOP: ClassVar[int]
        COMPUTER_PALM_SIZE_PC_PDA: ClassVar[int]
        COMPUTER_SERVER: ClassVar[int]
        COMPUTER_UNCATEGORIZED: ClassVar[int]
        COMPUTER_WEARABLE: ClassVar[int]
        HEALTH_BLOOD_PRESSURE: ClassVar[int]
        HEALTH_DATA_DISPLAY: ClassVar[int]
        HEALTH_GLUCOSE: ClassVar[int]
        HEALTH_PULSE_OXIMETER: ClassVar[int]
        HEALTH_PULSE_RATE: ClassVar[int]
        HEALTH_THERMOMETER: ClassVar[int]
        HEALTH_UNCATEGORIZED: ClassVar[int]
        HEALTH_WEIGHING: ClassVar[int]
        PERIPHERAL_KEYBOARD: ClassVar[int]
        PERIPHERAL_KEYBOARD_POINTING: ClassVar[int]
        PERIPHERAL_NON_KEYBOARD_NON_POINTING: ClassVar[int]
        PERIPHERAL_POINTING: ClassVar[int]
        PHONE_CELLULAR: ClassVar[int]
        PHONE_CORDLESS: ClassVar[int]
        PHONE_ISDN: ClassVar[int]
        PHONE_MODEM_OR_GATEWAY: ClassVar[int]
        PHONE_SMART: ClassVar[int]
        PHONE_UNCATEGORIZED: ClassVar[int]
        TOY_CONTROLLER: ClassVar[int]
        TOY_DOLL_ACTION_FIGURE: ClassVar[int]
        TOY_GAME: ClassVar[int]
        TOY_ROBOT: ClassVar[int]
        TOY_UNCATEGORIZED: ClassVar[int]
        TOY_VEHICLE: ClassVar[int]
        WEARABLE_GLASSES: ClassVar[int]
        WEARABLE_HELMET: ClassVar[int]
        WEARABLE_JACKET: ClassVar[int]
        WEARABLE_PAGER: ClassVar[int]
        WEARABLE_UNCATEGORIZED: ClassVar[int]
        WEARABLE_WRIST_WATCH: ClassVar[int]
        def __init__(self) -> None: ...

        class Major:
            AUDIO_VIDEO: ClassVar[int]
            COMPUTER: ClassVar[int]
            HEALTH: ClassVar[int]
            IMAGING: ClassVar[int]
            MISC: ClassVar[int]
            NETWORKING: ClassVar[int]
            PERIPHERAL: ClassVar[int]
            PHONE: ClassVar[int]
            TOY: ClassVar[int]
            UNCATEGORIZED: ClassVar[int]
            WEARABLE: ClassVar[int]
            def __init__(self) -> None: ...

from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothAdapter import BluetoothAdapter
from android.bluetooth.BluetoothDevice import BluetoothDevice
from android.bluetooth.BluetoothGattServer import BluetoothGattServer
from android.bluetooth.BluetoothGattServerCallback import BluetoothGattServerCallback
from android.content.Context import Context

class BluetoothManager:
    def openGattServer(self, p0: Context, p1: BluetoothGattServerCallback) -> BluetoothGattServer: ...
    def getConnectedDevices(self, p0: int) -> list: ...
    def getConnectionState(self, p0: BluetoothDevice, p1: int) -> int: ...
    def getDevicesMatchingConnectionStates(self, p0: int, p1: Any) -> list: ...
    def getAdapter(self) -> BluetoothAdapter: ...

from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothDevice import BluetoothDevice
from android.bluetooth.BluetoothGattCharacteristic import BluetoothGattCharacteristic
from android.bluetooth.BluetoothGattDescriptor import BluetoothGattDescriptor
from android.bluetooth.BluetoothGattService import BluetoothGattService
from java.util.UUID import UUID

class BluetoothGatt:
    CONNECTION_PRIORITY_BALANCED: ClassVar[int]
    CONNECTION_PRIORITY_DCK: ClassVar[int]
    CONNECTION_PRIORITY_HIGH: ClassVar[int]
    CONNECTION_PRIORITY_LOW_POWER: ClassVar[int]
    GATT_CONNECTION_CONGESTED: ClassVar[int]
    GATT_CONNECTION_TIMEOUT: ClassVar[int]
    GATT_FAILURE: ClassVar[int]
    GATT_INSUFFICIENT_AUTHENTICATION: ClassVar[int]
    GATT_INSUFFICIENT_AUTHORIZATION: ClassVar[int]
    GATT_INSUFFICIENT_ENCRYPTION: ClassVar[int]
    GATT_INVALID_ATTRIBUTE_LENGTH: ClassVar[int]
    GATT_INVALID_OFFSET: ClassVar[int]
    GATT_READ_NOT_PERMITTED: ClassVar[int]
    GATT_REQUEST_NOT_SUPPORTED: ClassVar[int]
    GATT_SUCCESS: ClassVar[int]
    GATT_WRITE_NOT_PERMITTED: ClassVar[int]
    A2DP: ClassVar[int]
    CSIP_SET_COORDINATOR: ClassVar[int]
    EXTRA_PREVIOUS_STATE: ClassVar[str]
    EXTRA_STATE: ClassVar[str]
    GATT: ClassVar[int]
    GATT_SERVER: ClassVar[int]
    HAP_CLIENT: ClassVar[int]
    HEADSET: ClassVar[int]
    HEALTH: ClassVar[int]
    HEARING_AID: ClassVar[int]
    HID_DEVICE: ClassVar[int]
    LE_AUDIO: ClassVar[int]
    SAP: ClassVar[int]
    STATE_CONNECTED: ClassVar[int]
    STATE_CONNECTING: ClassVar[int]
    STATE_DISCONNECTED: ClassVar[int]
    STATE_DISCONNECTING: ClassVar[int]
    @overload
    def abortReliableWrite(self, p0: BluetoothDevice) -> None: ...
    @overload
    def abortReliableWrite(self) -> None: ...
    def beginReliableWrite(self) -> bool: ...
    def disconnect(self) -> None: ...
    def discoverServices(self) -> bool: ...
    def executeReliableWrite(self) -> bool: ...
    def readCharacteristic(self, p0: BluetoothGattCharacteristic) -> bool: ...
    def readDescriptor(self, p0: BluetoothGattDescriptor) -> bool: ...
    def readRemoteRssi(self) -> bool: ...
    def requestConnectionPriority(self, p0: int) -> bool: ...
    def requestMtu(self, p0: int) -> bool: ...
    def setCharacteristicNotification(self, p0: BluetoothGattCharacteristic, p1: bool) -> bool: ...
    @overload
    def writeCharacteristic(self, p0: BluetoothGattCharacteristic, p1: Any, p2: int) -> int: ...
    @overload
    def writeCharacteristic(self, p0: BluetoothGattCharacteristic) -> bool: ...
    @overload
    def writeDescriptor(self, p0: BluetoothGattDescriptor, p1: Any) -> int: ...
    @overload
    def writeDescriptor(self, p0: BluetoothGattDescriptor) -> bool: ...
    def readPhy(self) -> None: ...
    def setPreferredPhy(self, p0: int, p1: int, p2: int) -> None: ...
    def getServices(self) -> list: ...
    def connect(self) -> bool: ...
    def close(self) -> None: ...
    def getConnectedDevices(self) -> list: ...
    def getConnectionState(self, p0: BluetoothDevice) -> int: ...
    def getDevicesMatchingConnectionStates(self, p0: Any) -> list: ...
    def getDevice(self) -> BluetoothDevice: ...
    def getService(self, p0: UUID) -> BluetoothGattService: ...

from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothDevice import BluetoothDevice
from android.bluetooth.BluetoothHealthAppConfiguration import BluetoothHealthAppConfiguration
from android.bluetooth.BluetoothHealthCallback import BluetoothHealthCallback
from android.os.ParcelFileDescriptor import ParcelFileDescriptor

class BluetoothHealth:
    APP_CONFIG_REGISTRATION_FAILURE: ClassVar[int]
    APP_CONFIG_REGISTRATION_SUCCESS: ClassVar[int]
    APP_CONFIG_UNREGISTRATION_FAILURE: ClassVar[int]
    APP_CONFIG_UNREGISTRATION_SUCCESS: ClassVar[int]
    CHANNEL_TYPE_RELIABLE: ClassVar[int]
    CHANNEL_TYPE_STREAMING: ClassVar[int]
    SINK_ROLE: ClassVar[int]
    SOURCE_ROLE: ClassVar[int]
    STATE_CHANNEL_CONNECTED: ClassVar[int]
    STATE_CHANNEL_CONNECTING: ClassVar[int]
    STATE_CHANNEL_DISCONNECTED: ClassVar[int]
    STATE_CHANNEL_DISCONNECTING: ClassVar[int]
    A2DP: ClassVar[int]
    CSIP_SET_COORDINATOR: ClassVar[int]
    EXTRA_PREVIOUS_STATE: ClassVar[str]
    EXTRA_STATE: ClassVar[str]
    GATT: ClassVar[int]
    GATT_SERVER: ClassVar[int]
    HAP_CLIENT: ClassVar[int]
    HEADSET: ClassVar[int]
    HEALTH: ClassVar[int]
    HEARING_AID: ClassVar[int]
    HID_DEVICE: ClassVar[int]
    LE_AUDIO: ClassVar[int]
    SAP: ClassVar[int]
    STATE_CONNECTED: ClassVar[int]
    STATE_CONNECTING: ClassVar[int]
    STATE_DISCONNECTED: ClassVar[int]
    STATE_DISCONNECTING: ClassVar[int]
    def connectChannelToSource(self, p0: BluetoothDevice, p1: BluetoothHealthAppConfiguration) -> bool: ...
    def disconnectChannel(self, p0: BluetoothDevice, p1: BluetoothHealthAppConfiguration, p2: int) -> bool: ...
    def getMainChannelFd(self, p0: BluetoothDevice, p1: BluetoothHealthAppConfiguration) -> ParcelFileDescriptor: ...
    def registerSinkAppConfiguration(self, p0: str, p1: int, p2: BluetoothHealthCallback) -> bool: ...
    def unregisterAppConfiguration(self, p0: BluetoothHealthAppConfiguration) -> bool: ...
    def getConnectedDevices(self) -> list: ...
    def getConnectionState(self, p0: BluetoothDevice) -> int: ...
    def getDevicesMatchingConnectionStates(self, p0: Any) -> list: ...

from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothGattCharacteristic import BluetoothGattCharacteristic
from android.os.Parcel import Parcel
from java.util.UUID import UUID

class BluetoothGattDescriptor:
    CREATOR: ClassVar[Any]
    DISABLE_NOTIFICATION_VALUE: ClassVar[Any]
    ENABLE_INDICATION_VALUE: ClassVar[Any]
    ENABLE_NOTIFICATION_VALUE: ClassVar[Any]
    PERMISSION_READ: ClassVar[int]
    PERMISSION_READ_ENCRYPTED: ClassVar[int]
    PERMISSION_READ_ENCRYPTED_MITM: ClassVar[int]
    PERMISSION_WRITE: ClassVar[int]
    PERMISSION_WRITE_ENCRYPTED: ClassVar[int]
    PERMISSION_WRITE_ENCRYPTED_MITM: ClassVar[int]
    PERMISSION_WRITE_SIGNED: ClassVar[int]
    PERMISSION_WRITE_SIGNED_MITM: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: UUID, p1: int) -> None: ...
    def getUuid(self) -> UUID: ...
    def getCharacteristic(self) -> BluetoothGattCharacteristic: ...
    def getValue(self) -> Any: ...
    def getPermissions(self) -> int: ...
    def setValue(self, p0: Any) -> bool: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothCodecType import BluetoothCodecType
from android.os.Parcel import Parcel

class BluetoothCodecConfig:
    BITS_PER_SAMPLE_16: ClassVar[int]
    BITS_PER_SAMPLE_24: ClassVar[int]
    BITS_PER_SAMPLE_32: ClassVar[int]
    BITS_PER_SAMPLE_NONE: ClassVar[int]
    CHANNEL_MODE_MONO: ClassVar[int]
    CHANNEL_MODE_NONE: ClassVar[int]
    CHANNEL_MODE_STEREO: ClassVar[int]
    CODEC_PRIORITY_DEFAULT: ClassVar[int]
    CODEC_PRIORITY_DISABLED: ClassVar[int]
    CODEC_PRIORITY_HIGHEST: ClassVar[int]
    CREATOR: ClassVar[Any]
    SAMPLE_RATE_176400: ClassVar[int]
    SAMPLE_RATE_192000: ClassVar[int]
    SAMPLE_RATE_44100: ClassVar[int]
    SAMPLE_RATE_48000: ClassVar[int]
    SAMPLE_RATE_88200: ClassVar[int]
    SAMPLE_RATE_96000: ClassVar[int]
    SAMPLE_RATE_NONE: ClassVar[int]
    SOURCE_CODEC_TYPE_AAC: ClassVar[int]
    SOURCE_CODEC_TYPE_APTX: ClassVar[int]
    SOURCE_CODEC_TYPE_APTX_HD: ClassVar[int]
    SOURCE_CODEC_TYPE_INVALID: ClassVar[int]
    SOURCE_CODEC_TYPE_LC3: ClassVar[int]
    SOURCE_CODEC_TYPE_LDAC: ClassVar[int]
    SOURCE_CODEC_TYPE_OPUS: ClassVar[int]
    SOURCE_CODEC_TYPE_SBC: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getBitsPerSample(self) -> int: ...
    def getChannelMode(self) -> int: ...
    def getCodecPriority(self) -> int: ...
    def getCodecSpecific1(self) -> int: ...
    def getCodecSpecific2(self) -> int: ...
    def getCodecSpecific3(self) -> int: ...
    def getCodecSpecific4(self) -> int: ...
    def getCodecType(self) -> int: ...
    def getExtendedCodecType(self) -> BluetoothCodecType: ...
    def getSampleRate(self) -> int: ...
    def isMandatoryCodec(self) -> bool: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class Builder:
        def __init__(self) -> None: ...
        def setBitsPerSample(self, p0: int) -> Any: ...
        def setCodecPriority(self, p0: int) -> Any: ...
        def setCodecSpecific1(self, p0: int) -> Any: ...
        def setChannelMode(self, p0: int) -> Any: ...
        def setCodecSpecific2(self, p0: int) -> Any: ...
        def setCodecSpecific3(self, p0: int) -> Any: ...
        def setCodecSpecific4(self, p0: int) -> Any: ...
        def setCodecType(self, p0: int) -> Any: ...
        def setExtendedCodecType(self, p0: BluetoothCodecType) -> Any: ...
        def setSampleRate(self, p0: int) -> Any: ...
        def build(self) -> "BluetoothCodecConfig": ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class BluetoothCodecType:
    CODEC_ID_AAC: ClassVar[int]
    CODEC_ID_APTX: ClassVar[int]
    CODEC_ID_APTX_HD: ClassVar[int]
    CODEC_ID_LDAC: ClassVar[int]
    CODEC_ID_OPUS: ClassVar[int]
    CODEC_ID_SBC: ClassVar[int]
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def isMandatoryCodec(self) -> bool: ...
    def getCodecId(self) -> int: ...
    def getCodecName(self) -> str: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothCodecConfig import BluetoothCodecConfig
from android.os.Parcel import Parcel

class BluetoothCodecStatus:
    CREATOR: ClassVar[Any]
    EXTRA_CODEC_STATUS: ClassVar[str]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getCodecsLocalCapabilities(self) -> list: ...
    def getCodecConfig(self) -> BluetoothCodecConfig: ...
    def getCodecsSelectableCapabilities(self) -> list: ...
    def isCodecConfigSelectable(self, p0: BluetoothCodecConfig) -> bool: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class Builder:
        def __init__(self) -> None: ...
        def setCodecConfig(self, p0: BluetoothCodecConfig) -> Any: ...
        def setCodecsLocalCapabilities(self, p0: list) -> Any: ...
        def setCodecsSelectableCapabilities(self, p0: list) -> Any: ...
        def build(self) -> "BluetoothCodecStatus": ...

from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothGatt import BluetoothGatt
from android.bluetooth.BluetoothGattCharacteristic import BluetoothGattCharacteristic
from android.bluetooth.BluetoothGattDescriptor import BluetoothGattDescriptor

class BluetoothGattCallback:
    def __init__(self) -> None: ...
    def onConnectionStateChange(self, p0: BluetoothGatt, p1: int, p2: int) -> None: ...
    def onMtuChanged(self, p0: BluetoothGatt, p1: int, p2: int) -> None: ...
    def onPhyRead(self, p0: BluetoothGatt, p1: int, p2: int, p3: int) -> None: ...
    def onPhyUpdate(self, p0: BluetoothGatt, p1: int, p2: int, p3: int) -> None: ...
    @overload
    def onCharacteristicRead(self, p0: BluetoothGatt, p1: BluetoothGattCharacteristic, p2: int) -> None: ...
    @overload
    def onCharacteristicRead(self, p0: BluetoothGatt, p1: BluetoothGattCharacteristic, p2: Any, p3: int) -> None: ...
    @overload
    def onCharacteristicChanged(self, p0: BluetoothGatt, p1: BluetoothGattCharacteristic, p2: Any) -> None: ...
    @overload
    def onCharacteristicChanged(self, p0: BluetoothGatt, p1: BluetoothGattCharacteristic) -> None: ...
    def onCharacteristicWrite(self, p0: BluetoothGatt, p1: BluetoothGattCharacteristic, p2: int) -> None: ...
    @overload
    def onDescriptorRead(self, p0: BluetoothGatt, p1: BluetoothGattDescriptor, p2: int, p3: Any) -> None: ...
    @overload
    def onDescriptorRead(self, p0: BluetoothGatt, p1: BluetoothGattDescriptor, p2: int) -> None: ...
    def onDescriptorWrite(self, p0: BluetoothGatt, p1: BluetoothGattDescriptor, p2: int) -> None: ...
    def onReadRemoteRssi(self, p0: BluetoothGatt, p1: int, p2: int) -> None: ...
    def onReliableWriteCompleted(self, p0: BluetoothGatt, p1: int) -> None: ...
    def onServiceChanged(self, p0: BluetoothGatt) -> None: ...
    def onServicesDiscovered(self, p0: BluetoothGatt, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothDevice import BluetoothDevice
from android.bluetooth.BluetoothProfile import BluetoothProfile
from android.bluetooth.BluetoothServerSocket import BluetoothServerSocket
from android.bluetooth.BluetoothSocketSettings import BluetoothSocketSettings
from android.bluetooth.le.BluetoothLeAdvertiser import BluetoothLeAdvertiser
from android.bluetooth.le.BluetoothLeScanner import BluetoothLeScanner
from android.content.Context import Context
from java.time.Duration import Duration
from java.util.UUID import UUID

class BluetoothAdapter:
    ACTION_CONNECTION_STATE_CHANGED: ClassVar[str]
    ACTION_DISCOVERY_FINISHED: ClassVar[str]
    ACTION_DISCOVERY_STARTED: ClassVar[str]
    ACTION_LOCAL_NAME_CHANGED: ClassVar[str]
    ACTION_REQUEST_DISCOVERABLE: ClassVar[str]
    ACTION_REQUEST_ENABLE: ClassVar[str]
    ACTION_SCAN_MODE_CHANGED: ClassVar[str]
    ACTION_STATE_CHANGED: ClassVar[str]
    ERROR: ClassVar[int]
    EXTRA_CONNECTION_STATE: ClassVar[str]
    EXTRA_DISCOVERABLE_DURATION: ClassVar[str]
    EXTRA_LOCAL_NAME: ClassVar[str]
    EXTRA_PREVIOUS_CONNECTION_STATE: ClassVar[str]
    EXTRA_PREVIOUS_SCAN_MODE: ClassVar[str]
    EXTRA_PREVIOUS_STATE: ClassVar[str]
    EXTRA_SCAN_MODE: ClassVar[str]
    EXTRA_STATE: ClassVar[str]
    SCAN_MODE_CONNECTABLE: ClassVar[int]
    SCAN_MODE_CONNECTABLE_DISCOVERABLE: ClassVar[int]
    SCAN_MODE_NONE: ClassVar[int]
    STATE_CONNECTED: ClassVar[int]
    STATE_CONNECTING: ClassVar[int]
    STATE_DISCONNECTED: ClassVar[int]
    STATE_DISCONNECTING: ClassVar[int]
    STATE_OFF: ClassVar[int]
    STATE_ON: ClassVar[int]
    STATE_TURNING_OFF: ClassVar[int]
    STATE_TURNING_ON: ClassVar[int]
    def disable(self) -> bool: ...
    @staticmethod
    def getDefaultAdapter() -> "BluetoothAdapter": ...
    def cancelDiscovery(self) -> bool: ...
    @staticmethod
    def checkBluetoothAddress(p0: str) -> bool: ...
    def closeProfileProxy(self, p0: int, p1: BluetoothProfile) -> None: ...
    def getBluetoothLeAdvertiser(self) -> BluetoothLeAdvertiser: ...
    def getBluetoothLeScanner(self) -> BluetoothLeScanner: ...
    def getBondedDevices(self) -> set: ...
    def getDiscoverableTimeout(self) -> Duration: ...
    def getLeMaximumAdvertisingDataLength(self) -> int: ...
    def getMaxConnectedAudioDevices(self) -> int: ...
    def getProfileConnectionState(self, p0: int) -> int: ...
    def getProfileProxy(self, p0: Context, p1: Any, p2: int) -> bool: ...
    @overload
    def getRemoteDevice(self, p0: Any) -> BluetoothDevice: ...
    @overload
    def getRemoteDevice(self, p0: str) -> BluetoothDevice: ...
    def getRemoteLeDevice(self, p0: str, p1: int) -> BluetoothDevice: ...
    def getScanMode(self) -> int: ...
    def isDiscovering(self) -> bool: ...
    def isLe2MPhySupported(self) -> bool: ...
    def isLeAudioBroadcastAssistantSupported(self) -> int: ...
    def isLeAudioBroadcastSourceSupported(self) -> int: ...
    def isLeAudioSupported(self) -> int: ...
    def isLeCodedPhySupported(self) -> bool: ...
    def isLeExtendedAdvertisingSupported(self) -> bool: ...
    def isLePeriodicAdvertisingSupported(self) -> bool: ...
    def isMultipleAdvertisementSupported(self) -> bool: ...
    def isOffloadedFilteringSupported(self) -> bool: ...
    def isOffloadedScanBatchingSupported(self) -> bool: ...
    def listenUsingInsecureL2capChannel(self) -> BluetoothServerSocket: ...
    def listenUsingInsecureRfcommWithServiceRecord(self, p0: str, p1: UUID) -> BluetoothServerSocket: ...
    def listenUsingL2capChannel(self) -> BluetoothServerSocket: ...
    def listenUsingRfcommWithServiceRecord(self, p0: str, p1: UUID) -> BluetoothServerSocket: ...
    def listenUsingSocketSettings(self, p0: BluetoothSocketSettings) -> BluetoothServerSocket: ...
    def startDiscovery(self) -> bool: ...
    @overload
    def startLeScan(self, p0: Any, p1: Any) -> bool: ...
    @overload
    def startLeScan(self, p0: Any) -> bool: ...
    def stopLeScan(self, p0: Any) -> None: ...
    def getName(self) -> str: ...
    def isEnabled(self) -> bool: ...
    def setName(self, p0: str) -> bool: ...
    def getState(self) -> int: ...
    def enable(self) -> bool: ...
    def getAddress(self) -> str: ...

    class LeScanCallback:
        def onLeScan(self, p0: BluetoothDevice, p1: int, p2: Any) -> None: ...

from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothDevice import BluetoothDevice
from android.bluetooth.BluetoothGattCharacteristic import BluetoothGattCharacteristic
from android.bluetooth.BluetoothGattDescriptor import BluetoothGattDescriptor
from android.bluetooth.BluetoothGattService import BluetoothGattService

class BluetoothGattServerCallback:
    def __init__(self) -> None: ...
    def onCharacteristicWriteRequest(self, p0: BluetoothDevice, p1: int, p2: BluetoothGattCharacteristic, p3: bool, p4: bool, p5: int, p6: Any) -> None: ...
    def onCharacteristicReadRequest(self, p0: BluetoothDevice, p1: int, p2: int, p3: BluetoothGattCharacteristic) -> None: ...
    def onConnectionStateChange(self, p0: BluetoothDevice, p1: int, p2: int) -> None: ...
    def onDescriptorReadRequest(self, p0: BluetoothDevice, p1: int, p2: int, p3: BluetoothGattDescriptor) -> None: ...
    def onExecuteWrite(self, p0: BluetoothDevice, p1: int, p2: bool) -> None: ...
    def onDescriptorWriteRequest(self, p0: BluetoothDevice, p1: int, p2: BluetoothGattDescriptor, p3: bool, p4: bool, p5: int, p6: Any) -> None: ...
    def onMtuChanged(self, p0: BluetoothDevice, p1: int) -> None: ...
    def onNotificationSent(self, p0: BluetoothDevice, p1: int) -> None: ...
    def onPhyRead(self, p0: BluetoothDevice, p1: int, p2: int, p3: int) -> None: ...
    def onPhyUpdate(self, p0: BluetoothDevice, p1: int, p2: int, p3: int) -> None: ...
    def onServiceAdded(self, p0: int, p1: BluetoothGattService) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class BluetoothHealthAppConfiguration:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getRole(self) -> int: ...
    def getName(self) -> str: ...
    def getDataType(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothDevice import BluetoothDevice
from android.bluetooth.BluetoothHidDeviceAppQosSettings import BluetoothHidDeviceAppQosSettings
from android.bluetooth.BluetoothHidDeviceAppSdpSettings import BluetoothHidDeviceAppSdpSettings
from java.util.concurrent.Executor import Executor

class BluetoothHidDevice:
    ACTION_CONNECTION_STATE_CHANGED: ClassVar[str]
    ERROR_RSP_INVALID_PARAM: ClassVar[int]
    ERROR_RSP_INVALID_RPT_ID: ClassVar[int]
    ERROR_RSP_NOT_READY: ClassVar[int]
    ERROR_RSP_SUCCESS: ClassVar[int]
    ERROR_RSP_UNKNOWN: ClassVar[int]
    ERROR_RSP_UNSUPPORTED_REQ: ClassVar[int]
    PROTOCOL_BOOT_MODE: ClassVar[int]
    PROTOCOL_REPORT_MODE: ClassVar[int]
    REPORT_TYPE_FEATURE: ClassVar[int]
    REPORT_TYPE_INPUT: ClassVar[int]
    REPORT_TYPE_OUTPUT: ClassVar[int]
    SUBCLASS1_COMBO: ClassVar[int]
    SUBCLASS1_KEYBOARD: ClassVar[int]
    SUBCLASS1_MOUSE: ClassVar[int]
    SUBCLASS1_NONE: ClassVar[int]
    SUBCLASS2_CARD_READER: ClassVar[int]
    SUBCLASS2_DIGITIZER_TABLET: ClassVar[int]
    SUBCLASS2_GAMEPAD: ClassVar[int]
    SUBCLASS2_JOYSTICK: ClassVar[int]
    SUBCLASS2_REMOTE_CONTROL: ClassVar[int]
    SUBCLASS2_SENSING_DEVICE: ClassVar[int]
    SUBCLASS2_UNCATEGORIZED: ClassVar[int]
    A2DP: ClassVar[int]
    CSIP_SET_COORDINATOR: ClassVar[int]
    EXTRA_PREVIOUS_STATE: ClassVar[str]
    EXTRA_STATE: ClassVar[str]
    GATT: ClassVar[int]
    GATT_SERVER: ClassVar[int]
    HAP_CLIENT: ClassVar[int]
    HEADSET: ClassVar[int]
    HEALTH: ClassVar[int]
    HEARING_AID: ClassVar[int]
    HID_DEVICE: ClassVar[int]
    LE_AUDIO: ClassVar[int]
    SAP: ClassVar[int]
    STATE_CONNECTED: ClassVar[int]
    STATE_CONNECTING: ClassVar[int]
    STATE_DISCONNECTED: ClassVar[int]
    STATE_DISCONNECTING: ClassVar[int]
    def disconnect(self, p0: BluetoothDevice) -> bool: ...
    def registerApp(self, p0: BluetoothHidDeviceAppSdpSettings, p1: BluetoothHidDeviceAppQosSettings, p2: BluetoothHidDeviceAppQosSettings, p3: Executor, p4: Any) -> bool: ...
    def replyReport(self, p0: BluetoothDevice, p1: int, p2: int, p3: Any) -> bool: ...
    def reportError(self, p0: BluetoothDevice, p1: int) -> bool: ...
    def sendReport(self, p0: BluetoothDevice, p1: int, p2: Any) -> bool: ...
    def unregisterApp(self) -> bool: ...
    def connect(self, p0: BluetoothDevice) -> bool: ...
    def getConnectedDevices(self) -> list: ...
    def getConnectionState(self, p0: BluetoothDevice) -> int: ...
    def getDevicesMatchingConnectionStates(self, p0: Any) -> list: ...

    class Callback:
        def __init__(self) -> None: ...
        def onAppStatusChanged(self, p0: BluetoothDevice, p1: bool) -> None: ...
        def onGetReport(self, p0: BluetoothDevice, p1: int, p2: int, p3: int) -> None: ...
        def onInterruptData(self, p0: BluetoothDevice, p1: int, p2: Any) -> None: ...
        def onSetProtocol(self, p0: BluetoothDevice, p1: int) -> None: ...
        def onSetReport(self, p0: BluetoothDevice, p1: int, p2: int, p3: Any) -> None: ...
        def onVirtualCableUnplug(self, p0: BluetoothDevice) -> None: ...
        def onConnectionStateChanged(self, p0: BluetoothDevice, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothDevice import BluetoothDevice
from android.bluetooth.BluetoothGattCharacteristic import BluetoothGattCharacteristic
from android.bluetooth.BluetoothGattService import BluetoothGattService
from java.util.UUID import UUID

class BluetoothGattServer:
    A2DP: ClassVar[int]
    CSIP_SET_COORDINATOR: ClassVar[int]
    EXTRA_PREVIOUS_STATE: ClassVar[str]
    EXTRA_STATE: ClassVar[str]
    GATT: ClassVar[int]
    GATT_SERVER: ClassVar[int]
    HAP_CLIENT: ClassVar[int]
    HEADSET: ClassVar[int]
    HEALTH: ClassVar[int]
    HEARING_AID: ClassVar[int]
    HID_DEVICE: ClassVar[int]
    LE_AUDIO: ClassVar[int]
    SAP: ClassVar[int]
    STATE_CONNECTED: ClassVar[int]
    STATE_CONNECTING: ClassVar[int]
    STATE_DISCONNECTED: ClassVar[int]
    STATE_DISCONNECTING: ClassVar[int]
    @overload
    def notifyCharacteristicChanged(self, p0: BluetoothDevice, p1: BluetoothGattCharacteristic, p2: bool) -> bool: ...
    @overload
    def notifyCharacteristicChanged(self, p0: BluetoothDevice, p1: BluetoothGattCharacteristic, p2: bool, p3: Any) -> int: ...
    def addService(self, p0: BluetoothGattService) -> bool: ...
    def cancelConnection(self, p0: BluetoothDevice) -> None: ...
    def clearServices(self) -> None: ...
    def readPhy(self, p0: BluetoothDevice) -> None: ...
    def removeService(self, p0: BluetoothGattService) -> bool: ...
    def sendResponse(self, p0: BluetoothDevice, p1: int, p2: int, p3: int, p4: Any) -> bool: ...
    def setPreferredPhy(self, p0: BluetoothDevice, p1: int, p2: int, p3: int) -> None: ...
    def getServices(self) -> list: ...
    def connect(self, p0: BluetoothDevice, p1: bool) -> bool: ...
    def close(self) -> None: ...
    def getConnectedDevices(self) -> list: ...
    def getConnectionState(self, p0: BluetoothDevice) -> int: ...
    def getDevicesMatchingConnectionStates(self, p0: Any) -> list: ...
    def getService(self, p0: UUID) -> BluetoothGattService: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class BluetoothLeAudioCodecConfig:
    BITS_PER_SAMPLE_16: ClassVar[int]
    BITS_PER_SAMPLE_24: ClassVar[int]
    BITS_PER_SAMPLE_32: ClassVar[int]
    BITS_PER_SAMPLE_NONE: ClassVar[int]
    CHANNEL_COUNT_1: ClassVar[int]
    CHANNEL_COUNT_2: ClassVar[int]
    CHANNEL_COUNT_NONE: ClassVar[int]
    CODEC_PRIORITY_DEFAULT: ClassVar[int]
    CODEC_PRIORITY_DISABLED: ClassVar[int]
    CODEC_PRIORITY_HIGHEST: ClassVar[int]
    CREATOR: ClassVar[Any]
    FRAME_DURATION_10000: ClassVar[int]
    FRAME_DURATION_7500: ClassVar[int]
    FRAME_DURATION_NONE: ClassVar[int]
    SAMPLE_RATE_11025: ClassVar[int]
    SAMPLE_RATE_16000: ClassVar[int]
    SAMPLE_RATE_176400: ClassVar[int]
    SAMPLE_RATE_192000: ClassVar[int]
    SAMPLE_RATE_22050: ClassVar[int]
    SAMPLE_RATE_24000: ClassVar[int]
    SAMPLE_RATE_32000: ClassVar[int]
    SAMPLE_RATE_384000: ClassVar[int]
    SAMPLE_RATE_44100: ClassVar[int]
    SAMPLE_RATE_48000: ClassVar[int]
    SAMPLE_RATE_8000: ClassVar[int]
    SAMPLE_RATE_88200: ClassVar[int]
    SAMPLE_RATE_96000: ClassVar[int]
    SAMPLE_RATE_NONE: ClassVar[int]
    SOURCE_CODEC_TYPE_INVALID: ClassVar[int]
    SOURCE_CODEC_TYPE_LC3: ClassVar[int]
    SOURCE_CODEC_TYPE_OPUS: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getBitsPerSample(self) -> int: ...
    def getCodecPriority(self) -> int: ...
    def getCodecType(self) -> int: ...
    def getSampleRate(self) -> int: ...
    def getCodecName(self) -> str: ...
    def getChannelCount(self) -> int: ...
    def getFrameDuration(self) -> int: ...
    def getMaxOctetsPerFrame(self) -> int: ...
    def getMinOctetsPerFrame(self) -> int: ...
    def getOctetsPerFrame(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class Builder:
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, p0: "BluetoothLeAudioCodecConfig") -> None: ...
        def setMinOctetsPerFrame(self, p0: int) -> Any: ...
        def setChannelCount(self, p0: int) -> Any: ...
        def setMaxOctetsPerFrame(self, p0: int) -> Any: ...
        def setFrameDuration(self, p0: int) -> Any: ...
        def setOctetsPerFrame(self, p0: int) -> Any: ...
        def setBitsPerSample(self, p0: int) -> Any: ...
        def setCodecPriority(self, p0: int) -> Any: ...
        def setCodecType(self, p0: int) -> Any: ...
        def setSampleRate(self, p0: int) -> Any: ...
        def build(self) -> "BluetoothLeAudioCodecConfig": ...

from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothDevice import BluetoothDevice
from java.io.InputStream import InputStream
from java.io.OutputStream import OutputStream

class BluetoothSocket:
    TYPE_L2CAP: ClassVar[int]
    TYPE_LE: ClassVar[int]
    TYPE_RFCOMM: ClassVar[int]
    TYPE_SCO: ClassVar[int]
    def getOutputStream(self) -> OutputStream: ...
    def isConnected(self) -> bool: ...
    def getMaxReceivePacketSize(self) -> int: ...
    def getConnectionType(self) -> int: ...
    def getMaxTransmitPacketSize(self) -> int: ...
    def getRemoteDevice(self) -> BluetoothDevice: ...
    def toString(self) -> str: ...
    def connect(self) -> None: ...
    def close(self) -> None: ...
    def getInputStream(self) -> InputStream: ...

from typing import Any, ClassVar, overload

class BluetoothStatusCodes:
    ERROR_BLUETOOTH_NOT_ALLOWED: ClassVar[int]
    ERROR_BLUETOOTH_NOT_ENABLED: ClassVar[int]
    ERROR_DEVICE_NOT_BONDED: ClassVar[int]
    ERROR_GATT_WRITE_NOT_ALLOWED: ClassVar[int]
    ERROR_GATT_WRITE_REQUEST_BUSY: ClassVar[int]
    ERROR_MISSING_BLUETOOTH_CONNECT_PERMISSION: ClassVar[int]
    ERROR_PROFILE_SERVICE_NOT_BOUND: ClassVar[int]
    ERROR_UNKNOWN: ClassVar[int]
    FEATURE_NOT_CONFIGURED: ClassVar[int]
    FEATURE_NOT_SUPPORTED: ClassVar[int]
    FEATURE_SUPPORTED: ClassVar[int]
    SUCCESS: ClassVar[int]

from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothDevice import BluetoothDevice

class BluetoothHeadset:
    ACTION_AUDIO_STATE_CHANGED: ClassVar[str]
    ACTION_CONNECTION_STATE_CHANGED: ClassVar[str]
    ACTION_VENDOR_SPECIFIC_HEADSET_EVENT: ClassVar[str]
    AT_CMD_TYPE_ACTION: ClassVar[int]
    AT_CMD_TYPE_BASIC: ClassVar[int]
    AT_CMD_TYPE_READ: ClassVar[int]
    AT_CMD_TYPE_SET: ClassVar[int]
    AT_CMD_TYPE_TEST: ClassVar[int]
    EXTRA_VENDOR_SPECIFIC_HEADSET_EVENT_ARGS: ClassVar[str]
    EXTRA_VENDOR_SPECIFIC_HEADSET_EVENT_CMD: ClassVar[str]
    EXTRA_VENDOR_SPECIFIC_HEADSET_EVENT_CMD_TYPE: ClassVar[str]
    STATE_AUDIO_CONNECTED: ClassVar[int]
    STATE_AUDIO_CONNECTING: ClassVar[int]
    STATE_AUDIO_DISCONNECTED: ClassVar[int]
    VENDOR_RESULT_CODE_COMMAND_ANDROID: ClassVar[str]
    VENDOR_SPECIFIC_HEADSET_EVENT_COMPANY_ID_CATEGORY: ClassVar[str]
    A2DP: ClassVar[int]
    CSIP_SET_COORDINATOR: ClassVar[int]
    EXTRA_PREVIOUS_STATE: ClassVar[str]
    EXTRA_STATE: ClassVar[str]
    GATT: ClassVar[int]
    GATT_SERVER: ClassVar[int]
    HAP_CLIENT: ClassVar[int]
    HEADSET: ClassVar[int]
    HEALTH: ClassVar[int]
    HEARING_AID: ClassVar[int]
    HID_DEVICE: ClassVar[int]
    LE_AUDIO: ClassVar[int]
    SAP: ClassVar[int]
    STATE_CONNECTED: ClassVar[int]
    STATE_CONNECTING: ClassVar[int]
    STATE_DISCONNECTED: ClassVar[int]
    STATE_DISCONNECTING: ClassVar[int]
    def isAudioConnected(self, p0: BluetoothDevice) -> bool: ...
    def isNoiseReductionSupported(self, p0: BluetoothDevice) -> bool: ...
    def isVoiceRecognitionSupported(self, p0: BluetoothDevice) -> bool: ...
    def sendVendorSpecificResultCode(self, p0: BluetoothDevice, p1: str, p2: str) -> bool: ...
    def startVoiceRecognition(self, p0: BluetoothDevice) -> bool: ...
    def stopVoiceRecognition(self, p0: BluetoothDevice) -> bool: ...
    def getConnectedDevices(self) -> list: ...
    def getConnectionState(self, p0: BluetoothDevice) -> int: ...
    def getDevicesMatchingConnectionStates(self, p0: Any) -> list: ...

from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothDevice import BluetoothDevice

class BluetoothHearingAid:
    ACTION_CONNECTION_STATE_CHANGED: ClassVar[str]
    A2DP: ClassVar[int]
    CSIP_SET_COORDINATOR: ClassVar[int]
    EXTRA_PREVIOUS_STATE: ClassVar[str]
    EXTRA_STATE: ClassVar[str]
    GATT: ClassVar[int]
    GATT_SERVER: ClassVar[int]
    HAP_CLIENT: ClassVar[int]
    HEADSET: ClassVar[int]
    HEALTH: ClassVar[int]
    HEARING_AID: ClassVar[int]
    HID_DEVICE: ClassVar[int]
    LE_AUDIO: ClassVar[int]
    SAP: ClassVar[int]
    STATE_CONNECTED: ClassVar[int]
    STATE_CONNECTING: ClassVar[int]
    STATE_DISCONNECTED: ClassVar[int]
    STATE_DISCONNECTING: ClassVar[int]
    def getConnectedDevices(self) -> list: ...
    def getConnectionState(self, p0: BluetoothDevice) -> int: ...
    def getDevicesMatchingConnectionStates(self, p0: Any) -> list: ...

from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothDevice import BluetoothDevice

class BluetoothProfile:
    A2DP: ClassVar[int]
    CSIP_SET_COORDINATOR: ClassVar[int]
    EXTRA_PREVIOUS_STATE: ClassVar[str]
    EXTRA_STATE: ClassVar[str]
    GATT: ClassVar[int]
    GATT_SERVER: ClassVar[int]
    HAP_CLIENT: ClassVar[int]
    HEADSET: ClassVar[int]
    HEALTH: ClassVar[int]
    HEARING_AID: ClassVar[int]
    HID_DEVICE: ClassVar[int]
    LE_AUDIO: ClassVar[int]
    SAP: ClassVar[int]
    STATE_CONNECTED: ClassVar[int]
    STATE_CONNECTING: ClassVar[int]
    STATE_DISCONNECTED: ClassVar[int]
    STATE_DISCONNECTING: ClassVar[int]
    def getConnectedDevices(self) -> list: ...
    def getConnectionState(self, p0: BluetoothDevice) -> int: ...
    def getDevicesMatchingConnectionStates(self, p0: Any) -> list: ...

    class ServiceListener:
        def onServiceConnected(self, p0: int, p1: "BluetoothProfile") -> None: ...
        def onServiceDisconnected(self, p0: int) -> None: ...

from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothDevice import BluetoothDevice
from android.bluetooth.BluetoothHealthAppConfiguration import BluetoothHealthAppConfiguration
from android.os.ParcelFileDescriptor import ParcelFileDescriptor

class BluetoothHealthCallback:
    def __init__(self) -> None: ...
    def onHealthAppConfigurationStatusChange(self, p0: BluetoothHealthAppConfiguration, p1: int) -> None: ...
    def onHealthChannelStateChange(self, p0: BluetoothHealthAppConfiguration, p1: BluetoothDevice, p2: int, p3: int, p4: ParcelFileDescriptor, p5: int) -> None: ...

from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothGattCharacteristic import BluetoothGattCharacteristic
from android.os.Parcel import Parcel
from java.util.UUID import UUID

class BluetoothGattService:
    CREATOR: ClassVar[Any]
    SERVICE_TYPE_PRIMARY: ClassVar[int]
    SERVICE_TYPE_SECONDARY: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: UUID, p1: int) -> None: ...
    def getUuid(self) -> UUID: ...
    def addService(self, p0: "BluetoothGattService") -> bool: ...
    def getInstanceId(self) -> int: ...
    def getCharacteristic(self, p0: UUID) -> BluetoothGattCharacteristic: ...
    def addCharacteristic(self, p0: BluetoothGattCharacteristic) -> bool: ...
    def getCharacteristics(self) -> list: ...
    def getIncludedServices(self) -> list: ...
    def getType(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothSocket import BluetoothSocket

class BluetoothServerSocket:
    def getPsm(self) -> int: ...
    def toString(self) -> str: ...
    @overload
    def accept(self, p0: int) -> BluetoothSocket: ...
    @overload
    def accept(self) -> BluetoothSocket: ...
    def close(self) -> None: ...

from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothDevice import BluetoothDevice

class BluetoothA2dp:
    ACTION_CONNECTION_STATE_CHANGED: ClassVar[str]
    ACTION_PLAYING_STATE_CHANGED: ClassVar[str]
    STATE_NOT_PLAYING: ClassVar[int]
    STATE_PLAYING: ClassVar[int]
    A2DP: ClassVar[int]
    CSIP_SET_COORDINATOR: ClassVar[int]
    EXTRA_PREVIOUS_STATE: ClassVar[str]
    EXTRA_STATE: ClassVar[str]
    GATT: ClassVar[int]
    GATT_SERVER: ClassVar[int]
    HAP_CLIENT: ClassVar[int]
    HEADSET: ClassVar[int]
    HEALTH: ClassVar[int]
    HEARING_AID: ClassVar[int]
    HID_DEVICE: ClassVar[int]
    LE_AUDIO: ClassVar[int]
    SAP: ClassVar[int]
    STATE_CONNECTED: ClassVar[int]
    STATE_CONNECTING: ClassVar[int]
    STATE_DISCONNECTED: ClassVar[int]
    STATE_DISCONNECTING: ClassVar[int]
    def getSupportedCodecTypes(self) -> list: ...
    def isA2dpPlaying(self, p0: BluetoothDevice) -> bool: ...
    def finalize(self) -> None: ...
    def getConnectedDevices(self) -> list: ...
    def getConnectionState(self, p0: BluetoothDevice) -> int: ...
    def getDevicesMatchingConnectionStates(self, p0: Any) -> list: ...

from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothClass import BluetoothClass
from android.bluetooth.BluetoothGatt import BluetoothGatt
from android.bluetooth.BluetoothGattCallback import BluetoothGattCallback
from android.bluetooth.BluetoothSocket import BluetoothSocket
from android.bluetooth.BluetoothSocketSettings import BluetoothSocketSettings
from android.content.Context import Context
from android.os.Handler import Handler
from android.os.Parcel import Parcel
from java.util.UUID import UUID

class BluetoothDevice:
    ACTION_ACL_CONNECTED: ClassVar[str]
    ACTION_ACL_DISCONNECTED: ClassVar[str]
    ACTION_ACL_DISCONNECT_REQUESTED: ClassVar[str]
    ACTION_ALIAS_CHANGED: ClassVar[str]
    ACTION_BOND_STATE_CHANGED: ClassVar[str]
    ACTION_CLASS_CHANGED: ClassVar[str]
    ACTION_ENCRYPTION_CHANGE: ClassVar[str]
    ACTION_FOUND: ClassVar[str]
    ACTION_KEY_MISSING: ClassVar[str]
    ACTION_NAME_CHANGED: ClassVar[str]
    ACTION_PAIRING_REQUEST: ClassVar[str]
    ACTION_UUID: ClassVar[str]
    ADDRESS_TYPE_ANONYMOUS: ClassVar[int]
    ADDRESS_TYPE_PUBLIC: ClassVar[int]
    ADDRESS_TYPE_RANDOM: ClassVar[int]
    ADDRESS_TYPE_UNKNOWN: ClassVar[int]
    BOND_BONDED: ClassVar[int]
    BOND_BONDING: ClassVar[int]
    BOND_NONE: ClassVar[int]
    CREATOR: ClassVar[Any]
    DEVICE_TYPE_CLASSIC: ClassVar[int]
    DEVICE_TYPE_DUAL: ClassVar[int]
    DEVICE_TYPE_LE: ClassVar[int]
    DEVICE_TYPE_UNKNOWN: ClassVar[int]
    ENCRYPTION_ALGORITHM_AES: ClassVar[int]
    ENCRYPTION_ALGORITHM_E0: ClassVar[int]
    ENCRYPTION_ALGORITHM_NONE: ClassVar[int]
    ERROR: ClassVar[int]
    EXTRA_BOND_STATE: ClassVar[str]
    EXTRA_CLASS: ClassVar[str]
    EXTRA_DEVICE: ClassVar[str]
    EXTRA_ENCRYPTION_ALGORITHM: ClassVar[str]
    EXTRA_ENCRYPTION_ENABLED: ClassVar[str]
    EXTRA_ENCRYPTION_STATUS: ClassVar[str]
    EXTRA_IS_COORDINATED_SET_MEMBER: ClassVar[str]
    EXTRA_KEY_SIZE: ClassVar[str]
    EXTRA_NAME: ClassVar[str]
    EXTRA_PAIRING_KEY: ClassVar[str]
    EXTRA_PAIRING_VARIANT: ClassVar[str]
    EXTRA_PREVIOUS_BOND_STATE: ClassVar[str]
    EXTRA_RSSI: ClassVar[str]
    EXTRA_TRANSPORT: ClassVar[str]
    EXTRA_UUID: ClassVar[str]
    PAIRING_VARIANT_PASSKEY_CONFIRMATION: ClassVar[int]
    PAIRING_VARIANT_PIN: ClassVar[int]
    PHY_LE_1M: ClassVar[int]
    PHY_LE_1M_MASK: ClassVar[int]
    PHY_LE_2M: ClassVar[int]
    PHY_LE_2M_MASK: ClassVar[int]
    PHY_LE_CODED: ClassVar[int]
    PHY_LE_CODED_MASK: ClassVar[int]
    PHY_OPTION_NO_PREFERRED: ClassVar[int]
    PHY_OPTION_S2: ClassVar[int]
    PHY_OPTION_S8: ClassVar[int]
    TRANSPORT_AUTO: ClassVar[int]
    TRANSPORT_BREDR: ClassVar[int]
    TRANSPORT_LE: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getBondState(self) -> int: ...
    def getIdentityAddressWithType(self) -> Any: ...
    def getUuids(self) -> Any: ...
    def setAlias(self, p0: str) -> int: ...
    def setPairingConfirmation(self, p0: bool) -> bool: ...
    @overload
    def connectGatt(self, p0: Context, p1: bool, p2: BluetoothGattCallback, p3: int) -> BluetoothGatt: ...
    @overload
    def connectGatt(self, p0: Context, p1: bool, p2: BluetoothGattCallback) -> BluetoothGatt: ...
    @overload
    def connectGatt(self, p0: Context, p1: bool, p2: BluetoothGattCallback, p3: int, p4: int) -> BluetoothGatt: ...
    @overload
    def connectGatt(self, p0: Context, p1: bool, p2: BluetoothGattCallback, p3: int, p4: int, p5: Handler) -> BluetoothGatt: ...
    def createBond(self) -> bool: ...
    def createInsecureL2capChannel(self, p0: int) -> BluetoothSocket: ...
    def createInsecureRfcommSocketToServiceRecord(self, p0: UUID) -> BluetoothSocket: ...
    def createL2capChannel(self, p0: int) -> BluetoothSocket: ...
    def createRfcommSocketToServiceRecord(self, p0: UUID) -> BluetoothSocket: ...
    def createUsingSocketSettings(self, p0: BluetoothSocketSettings) -> BluetoothSocket: ...
    def fetchUuidsWithSdp(self) -> bool: ...
    def getAlias(self) -> str: ...
    def getBluetoothClass(self) -> BluetoothClass: ...
    def getName(self) -> str: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def getType(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def setPin(self, p0: Any) -> bool: ...
    def getAddressType(self) -> int: ...
    def getAddress(self) -> str: ...

    class BluetoothAddress:
        CREATOR: ClassVar[Any]
        CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
        PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
        def __init__(self, p0: str, p1: int) -> None: ...
        def describeContents(self) -> int: ...
        def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
        def getAddressType(self) -> int: ...
        def getAddress(self) -> str: ...

from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothLeAudioCodecConfig import BluetoothLeAudioCodecConfig
from android.os.Parcel import Parcel

class BluetoothLeAudioCodecStatus:
    CREATOR: ClassVar[Any]
    EXTRA_LE_AUDIO_CODEC_STATUS: ClassVar[str]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: BluetoothLeAudioCodecConfig, p1: BluetoothLeAudioCodecConfig, p2: list, p3: list, p4: list, p5: list) -> None: ...
    def getInputCodecConfig(self) -> BluetoothLeAudioCodecConfig: ...
    def getInputCodecLocalCapabilities(self) -> list: ...
    def getInputCodecSelectableCapabilities(self) -> list: ...
    def getOutputCodecConfig(self) -> BluetoothLeAudioCodecConfig: ...
    def getOutputCodecLocalCapabilities(self) -> list: ...
    def getOutputCodecSelectableCapabilities(self) -> list: ...
    def isInputCodecConfigSelectable(self, p0: BluetoothLeAudioCodecConfig) -> bool: ...
    def isOutputCodecConfigSelectable(self, p0: BluetoothLeAudioCodecConfig) -> bool: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothGattDescriptor import BluetoothGattDescriptor
from android.bluetooth.BluetoothGattService import BluetoothGattService
from android.os.Parcel import Parcel
from java.util.UUID import UUID

class BluetoothGattCharacteristic:
    CREATOR: ClassVar[Any]
    FORMAT_FLOAT: ClassVar[int]
    FORMAT_SFLOAT: ClassVar[int]
    FORMAT_SINT16: ClassVar[int]
    FORMAT_SINT32: ClassVar[int]
    FORMAT_SINT8: ClassVar[int]
    FORMAT_UINT16: ClassVar[int]
    FORMAT_UINT32: ClassVar[int]
    FORMAT_UINT8: ClassVar[int]
    PERMISSION_READ: ClassVar[int]
    PERMISSION_READ_ENCRYPTED: ClassVar[int]
    PERMISSION_READ_ENCRYPTED_MITM: ClassVar[int]
    PERMISSION_WRITE: ClassVar[int]
    PERMISSION_WRITE_ENCRYPTED: ClassVar[int]
    PERMISSION_WRITE_ENCRYPTED_MITM: ClassVar[int]
    PERMISSION_WRITE_SIGNED: ClassVar[int]
    PERMISSION_WRITE_SIGNED_MITM: ClassVar[int]
    PROPERTY_BROADCAST: ClassVar[int]
    PROPERTY_EXTENDED_PROPS: ClassVar[int]
    PROPERTY_INDICATE: ClassVar[int]
    PROPERTY_NOTIFY: ClassVar[int]
    PROPERTY_READ: ClassVar[int]
    PROPERTY_SIGNED_WRITE: ClassVar[int]
    PROPERTY_WRITE: ClassVar[int]
    PROPERTY_WRITE_NO_RESPONSE: ClassVar[int]
    WRITE_TYPE_DEFAULT: ClassVar[int]
    WRITE_TYPE_NO_RESPONSE: ClassVar[int]
    WRITE_TYPE_SIGNED: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: UUID, p1: int, p2: int) -> None: ...
    def getUuid(self) -> UUID: ...
    def getStringValue(self, p0: int) -> str: ...
    def getDescriptors(self) -> list: ...
    def addDescriptor(self, p0: BluetoothGattDescriptor) -> bool: ...
    def getFloatValue(self, p0: int, p1: int) -> float: ...
    def getInstanceId(self) -> int: ...
    def getWriteType(self) -> int: ...
    def setWriteType(self, p0: int) -> None: ...
    def getValue(self) -> Any: ...
    def getDescriptor(self, p0: UUID) -> BluetoothGattDescriptor: ...
    def getProperties(self) -> int: ...
    def getPermissions(self) -> int: ...
    @overload
    def setValue(self, p0: int, p1: int, p2: int) -> bool: ...
    @overload
    def setValue(self, p0: Any) -> bool: ...
    @overload
    def setValue(self, p0: str) -> bool: ...
    @overload
    def setValue(self, p0: int, p1: int, p2: int, p3: int) -> bool: ...
    def getIntValue(self, p0: int, p1: int) -> int: ...
    def getService(self) -> BluetoothGattService: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class BluetoothHidDeviceAppQosSettings:
    CREATOR: ClassVar[Any]
    MAX: ClassVar[int]
    SERVICE_BEST_EFFORT: ClassVar[int]
    SERVICE_GUARANTEED: ClassVar[int]
    SERVICE_NO_TRAFFIC: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    def getDelayVariation(self) -> int: ...
    def getPeakBandwidth(self) -> int: ...
    def getServiceType(self) -> int: ...
    def getTokenBucketSize(self) -> int: ...
    def getTokenRate(self) -> int: ...
    def getLatency(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload

class BluetoothSocketException:
    BLUETOOTH_OFF_FAILURE: ClassVar[int]
    L2CAP_ACL_FAILURE: ClassVar[int]
    L2CAP_CLIENT_SECURITY_FAILURE: ClassVar[int]
    L2CAP_INSUFFICIENT_AUTHENTICATION: ClassVar[int]
    L2CAP_INSUFFICIENT_AUTHORIZATION: ClassVar[int]
    L2CAP_INSUFFICIENT_ENCRYPTION: ClassVar[int]
    L2CAP_INSUFFICIENT_ENCRYPT_KEY_SIZE: ClassVar[int]
    L2CAP_INVALID_PARAMETERS: ClassVar[int]
    L2CAP_INVALID_SOURCE_CID: ClassVar[int]
    L2CAP_NO_PSM_AVAILABLE: ClassVar[int]
    L2CAP_NO_RESOURCES: ClassVar[int]
    L2CAP_SOURCE_CID_ALREADY_ALLOCATED: ClassVar[int]
    L2CAP_TIMEOUT: ClassVar[int]
    L2CAP_UNACCEPTABLE_PARAMETERS: ClassVar[int]
    L2CAP_UNKNOWN: ClassVar[int]
    NULL_DEVICE: ClassVar[int]
    RPC_FAILURE: ClassVar[int]
    SOCKET_CLOSED: ClassVar[int]
    SOCKET_CONNECTION_FAILURE: ClassVar[int]
    SOCKET_MANAGER_FAILURE: ClassVar[int]
    UNIX_FILE_SOCKET_CREATION_FAILURE: ClassVar[int]
    UNSPECIFIED: ClassVar[int]
    @overload
    def __init__(self, p0: int) -> None: ...
    @overload
    def __init__(self, p0: int, p1: str) -> None: ...
    def getErrorCode(self) -> int: ...

from typing import Any, ClassVar, overload
from java.util.UUID import UUID

class BluetoothSocketSettings:
    def isAuthenticationRequired(self) -> bool: ...
    def isEncryptionRequired(self) -> bool: ...
    def getL2capPsm(self) -> int: ...
    def getRfcommServiceName(self) -> str: ...
    def getRfcommUuid(self) -> UUID: ...
    def getSocketType(self) -> int: ...
    def toString(self) -> str: ...

    class Builder:
        def __init__(self) -> None: ...
        def setAuthenticationRequired(self, p0: bool) -> Any: ...
        def setL2capPsm(self, p0: int) -> Any: ...
        def setRfcommServiceName(self, p0: str) -> Any: ...
        def setRfcommUuid(self, p0: UUID) -> Any: ...
        def setSocketType(self, p0: int) -> Any: ...
        def setEncryptionRequired(self, p0: bool) -> Any: ...
        def build(self) -> "BluetoothSocketSettings": ...

from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothDevice import BluetoothDevice

class BluetoothCsipSetCoordinator:
    ACTION_CSIS_CONNECTION_STATE_CHANGED: ClassVar[str]
    A2DP: ClassVar[int]
    CSIP_SET_COORDINATOR: ClassVar[int]
    EXTRA_PREVIOUS_STATE: ClassVar[str]
    EXTRA_STATE: ClassVar[str]
    GATT: ClassVar[int]
    GATT_SERVER: ClassVar[int]
    HAP_CLIENT: ClassVar[int]
    HEADSET: ClassVar[int]
    HEALTH: ClassVar[int]
    HEARING_AID: ClassVar[int]
    HID_DEVICE: ClassVar[int]
    LE_AUDIO: ClassVar[int]
    SAP: ClassVar[int]
    STATE_CONNECTED: ClassVar[int]
    STATE_CONNECTING: ClassVar[int]
    STATE_DISCONNECTED: ClassVar[int]
    STATE_DISCONNECTING: ClassVar[int]
    def close(self) -> None: ...
    def getConnectedDevices(self) -> list: ...
    def getConnectionState(self, p0: BluetoothDevice) -> int: ...
    def getDevicesMatchingConnectionStates(self, p0: Any) -> list: ...

from typing import Any, ClassVar, overload

class BluetoothAssignedNumbers:
    AAMP_OF_AMERICA: ClassVar[int]
    ACCEL_SEMICONDUCTOR: ClassVar[int]
    ACE_SENSOR: ClassVar[int]
    ADIDAS: ClassVar[int]
    ADVANCED_PANMOBIL_SYSTEMS: ClassVar[int]
    AIROHA_TECHNOLOGY: ClassVar[int]
    ALCATEL: ClassVar[int]
    ALPWISE: ClassVar[int]
    AMICCOM_ELECTRONICS: ClassVar[int]
    APLIX: ClassVar[int]
    APPLE: ClassVar[int]
    APT_LICENSING: ClassVar[int]
    ARCHOS: ClassVar[int]
    ARP_DEVICES: ClassVar[int]
    ATHEROS_COMMUNICATIONS: ClassVar[int]
    ATMEL: ClassVar[int]
    AUSTCO_COMMUNICATION_SYSTEMS: ClassVar[int]
    AUTONET_MOBILE: ClassVar[int]
    AVAGO: ClassVar[int]
    AVM_BERLIN: ClassVar[int]
    A_AND_D_ENGINEERING: ClassVar[int]
    A_AND_R_CAMBRIDGE: ClassVar[int]
    BANDSPEED: ClassVar[int]
    BAND_XI_INTERNATIONAL: ClassVar[int]
    BDE_TECHNOLOGY: ClassVar[int]
    BEATS_ELECTRONICS: ClassVar[int]
    BEAUTIFUL_ENTERPRISE: ClassVar[int]
    BEKEY: ClassVar[int]
    BELKIN_INTERNATIONAL: ClassVar[int]
    BINAURIC: ClassVar[int]
    BIOSENTRONICS: ClassVar[int]
    BLUEGIGA: ClassVar[int]
    BLUERADIOS: ClassVar[int]
    BLUETOOTH_SIG: ClassVar[int]
    BLUETREK_TECHNOLOGIES: ClassVar[int]
    BOSE: ClassVar[int]
    BRIARTEK: ClassVar[int]
    BROADCOM: ClassVar[int]
    CAEN_RFID: ClassVar[int]
    CAMBRIDGE_SILICON_RADIO: ClassVar[int]
    CATC: ClassVar[int]
    CINETIX: ClassVar[int]
    CLARINOX_TECHNOLOGIES: ClassVar[int]
    COLORFY: ClassVar[int]
    COMMIL: ClassVar[int]
    CONEXANT_SYSTEMS: ClassVar[int]
    CONNECTBLUE: ClassVar[int]
    CONTINENTAL_AUTOMOTIVE: ClassVar[int]
    CONWISE_TECHNOLOGY: ClassVar[int]
    CREATIVE_TECHNOLOGY: ClassVar[int]
    C_TECHNOLOGIES: ClassVar[int]
    DANLERS: ClassVar[int]
    DELORME_PUBLISHING_COMPANY: ClassVar[int]
    DEXCOM: ClassVar[int]
    DIALOG_SEMICONDUCTOR: ClassVar[int]
    DIGIANSWER: ClassVar[int]
    ECLIPSE: ClassVar[int]
    ECOTEST: ClassVar[int]
    ELGATO_SYSTEMS: ClassVar[int]
    EM_MICROELECTRONIC_MARIN: ClassVar[int]
    EQUINOX_AG: ClassVar[int]
    ERICSSON_TECHNOLOGY: ClassVar[int]
    EVLUMA: ClassVar[int]
    FREE2MOVE: ClassVar[int]
    FUNAI_ELECTRIC: ClassVar[int]
    GARMIN_INTERNATIONAL: ClassVar[int]
    GCT_SEMICONDUCTOR: ClassVar[int]
    GELO: ClassVar[int]
    GENEQ: ClassVar[int]
    GENERAL_MOTORS: ClassVar[int]
    GENNUM: ClassVar[int]
    GEOFORCE: ClassVar[int]
    GIBSON_GUITARS: ClassVar[int]
    GN_NETCOM: ClassVar[int]
    GN_RESOUND: ClassVar[int]
    GOOGLE: ClassVar[int]
    GREEN_THROTTLE_GAMES: ClassVar[int]
    GROUP_SENSE: ClassVar[int]
    HANLYNN_TECHNOLOGIES: ClassVar[int]
    HARMAN_INTERNATIONAL: ClassVar[int]
    HEWLETT_PACKARD: ClassVar[int]
    HITACHI: ClassVar[int]
    HOSIDEN: ClassVar[int]
    IBM: ClassVar[int]
    INFINEON_TECHNOLOGIES: ClassVar[int]
    INGENIEUR_SYSTEMGRUPPE_ZAHN: ClassVar[int]
    INTEGRATED_SILICON_SOLUTION: ClassVar[int]
    INTEGRATED_SYSTEM_SOLUTION: ClassVar[int]
    INTEL: ClassVar[int]
    INVENTEL: ClassVar[int]
    IPEXTREME: ClassVar[int]
    I_TECH_DYNAMIC_GLOBAL_DISTRIBUTION: ClassVar[int]
    JAWBONE: ClassVar[int]
    JIANGSU_TOPPOWER_AUTOMOTIVE_ELECTRONICS: ClassVar[int]
    JOHNSON_CONTROLS: ClassVar[int]
    J_AND_M: ClassVar[int]
    KAWANTECH: ClassVar[int]
    KC_TECHNOLOGY: ClassVar[int]
    KENSINGTON_COMPUTER_PRODUCTS_GROUP: ClassVar[int]
    LAIRD_TECHNOLOGIES: ClassVar[int]
    LESSWIRE: ClassVar[int]
    LG_ELECTRONICS: ClassVar[int]
    LINAK: ClassVar[int]
    LUCENT: ClassVar[int]
    LUDUS_HELSINKI: ClassVar[int]
    MACRONIX: ClassVar[int]
    MAGNETI_MARELLI: ClassVar[int]
    MANSELLA: ClassVar[int]
    MARVELL: ClassVar[int]
    MATSUSHITA_ELECTRIC: ClassVar[int]
    MC10: ClassVar[int]
    MEDIATEK: ClassVar[int]
    MESO_INTERNATIONAL: ClassVar[int]
    META_WATCH: ClassVar[int]
    MEWTEL_TECHNOLOGY: ClassVar[int]
    MICOMMAND: ClassVar[int]
    MICROCHIP_TECHNOLOGY: ClassVar[int]
    MICROSOFT: ClassVar[int]
    MINDTREE: ClassVar[int]
    MISFIT_WEARABLES: ClassVar[int]
    MITEL_SEMICONDUCTOR: ClassVar[int]
    MITSUBISHI_ELECTRIC: ClassVar[int]
    MOBILIAN_CORPORATION: ClassVar[int]
    MONSTER: ClassVar[int]
    MOTOROLA: ClassVar[int]
    MSTAR_SEMICONDUCTOR: ClassVar[int]
    MUZIK: ClassVar[int]
    NEC: ClassVar[int]
    NEC_LIGHTING: ClassVar[int]
    NEWLOGIC: ClassVar[int]
    NIKE: ClassVar[int]
    NINE_SOLUTIONS: ClassVar[int]
    NOKIA_MOBILE_PHONES: ClassVar[int]
    NORDIC_SEMICONDUCTOR: ClassVar[int]
    NORWOOD_SYSTEMS: ClassVar[int]
    ODM_TECHNOLOGY: ClassVar[int]
    OMEGAWAVE: ClassVar[int]
    ONSET_COMPUTER: ClassVar[int]
    OPEN_INTERFACE: ClassVar[int]
    OTL_DYNAMICS: ClassVar[int]
    PANDA_OCEAN: ClassVar[int]
    PARROT: ClassVar[int]
    PARTHUS_TECHNOLOGIES: ClassVar[int]
    PASSIF_SEMICONDUCTOR: ClassVar[int]
    PETER_SYSTEMTECHNIK: ClassVar[int]
    PHILIPS_SEMICONDUCTORS: ClassVar[int]
    PLANTRONICS: ClassVar[int]
    POLAR_ELECTRO: ClassVar[int]
    POLAR_ELECTRO_EUROPE: ClassVar[int]
    PROCTER_AND_GAMBLE: ClassVar[int]
    QUALCOMM: ClassVar[int]
    QUALCOMM_CONNECTED_EXPERIENCES: ClassVar[int]
    QUALCOMM_INNOVATION_CENTER: ClassVar[int]
    QUALCOMM_LABS: ClassVar[int]
    QUALCOMM_TECHNOLOGIES: ClassVar[int]
    QUINTIC: ClassVar[int]
    QUUPPA: ClassVar[int]
    RALINK_TECHNOLOGY: ClassVar[int]
    RDA_MICROELECTRONICS: ClassVar[int]
    REALTEK_SEMICONDUCTOR: ClassVar[int]
    RED_M: ClassVar[int]
    RENESAS_TECHNOLOGY: ClassVar[int]
    RESEARCH_IN_MOTION: ClassVar[int]
    RF_MICRO_DEVICES: ClassVar[int]
    RIVIERAWAVES: ClassVar[int]
    ROHDE_AND_SCHWARZ: ClassVar[int]
    RTX_TELECOM: ClassVar[int]
    SAMSUNG_ELECTRONICS: ClassVar[int]
    SARIS_CYCLING_GROUP: ClassVar[int]
    SEERS_TECHNOLOGY: ClassVar[int]
    SEIKO_EPSON: ClassVar[int]
    SELFLY: ClassVar[int]
    SEMILINK: ClassVar[int]
    SENNHEISER_COMMUNICATIONS: ClassVar[int]
    SHANGHAI_SUPER_SMART_ELECTRONICS: ClassVar[int]
    SHENZHEN_EXCELSECU_DATA_TECHNOLOGY: ClassVar[int]
    SIGNIA_TECHNOLOGIES: ClassVar[int]
    SILICON_WAVE: ClassVar[int]
    SIRF_TECHNOLOGY: ClassVar[int]
    SOCKET_MOBILE: ClassVar[int]
    SONY_ERICSSON: ClassVar[int]
    SOUND_ID: ClassVar[int]
    SPORTS_TRACKING_TECHNOLOGIES: ClassVar[int]
    SR_MEDIZINELEKTRONIK: ClassVar[int]
    STACCATO_COMMUNICATIONS: ClassVar[int]
    STALMART_TECHNOLOGY: ClassVar[int]
    STARKEY_LABORATORIES: ClassVar[int]
    STOLLMAN_E_PLUS_V: ClassVar[int]
    STONESTREET_ONE: ClassVar[int]
    ST_MICROELECTRONICS: ClassVar[int]
    SUMMIT_DATA_COMMUNICATIONS: ClassVar[int]
    SUUNTO: ClassVar[int]
    SWIRL_NETWORKS: ClassVar[int]
    SYMBOL_TECHNOLOGIES: ClassVar[int]
    SYNOPSYS: ClassVar[int]
    SYSTEMS_AND_CHIPS: ClassVar[int]
    S_POWER_ELECTRONICS: ClassVar[int]
    TAIXINGBANG_TECHNOLOGY: ClassVar[int]
    TENOVIS: ClassVar[int]
    TERAX: ClassVar[int]
    TEXAS_INSTRUMENTS: ClassVar[int]
    THINKOPTICS: ClassVar[int]
    THREECOM: ClassVar[int]
    THREE_DIJOY: ClassVar[int]
    THREE_DSP: ClassVar[int]
    TIMEKEEPING_SYSTEMS: ClassVar[int]
    TIMEX_GROUP_USA: ClassVar[int]
    TOPCORN_POSITIONING_SYSTEMS: ClassVar[int]
    TOSHIBA: ClassVar[int]
    TRANSILICA: ClassVar[int]
    TRELAB: ClassVar[int]
    TTPCOM: ClassVar[int]
    TXTR: ClassVar[int]
    TZERO_TECHNOLOGIES: ClassVar[int]
    UNIVERSAL_ELECTRONICS: ClassVar[int]
    VERTU: ClassVar[int]
    VISTEON: ClassVar[int]
    VIZIO: ClassVar[int]
    VOYETRA_TURTLE_BEACH: ClassVar[int]
    WAVEPLUS_TECHNOLOGY: ClassVar[int]
    WICENTRIC: ClassVar[int]
    WIDCOMM: ClassVar[int]
    WUXI_VIMICRO: ClassVar[int]
    ZEEVO: ClassVar[int]
    ZER01_TV: ClassVar[int]
    ZOMM: ClassVar[int]
    ZSCAN_SOFTWARE: ClassVar[int]

from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothDevice import BluetoothDevice

class BluetoothLeAudio:
    ACTION_LE_AUDIO_CONNECTION_STATE_CHANGED: ClassVar[str]
    GROUP_ID_INVALID: ClassVar[int]
    A2DP: ClassVar[int]
    CSIP_SET_COORDINATOR: ClassVar[int]
    EXTRA_PREVIOUS_STATE: ClassVar[str]
    EXTRA_STATE: ClassVar[str]
    GATT: ClassVar[int]
    GATT_SERVER: ClassVar[int]
    HAP_CLIENT: ClassVar[int]
    HEADSET: ClassVar[int]
    HEALTH: ClassVar[int]
    HEARING_AID: ClassVar[int]
    HID_DEVICE: ClassVar[int]
    LE_AUDIO: ClassVar[int]
    SAP: ClassVar[int]
    STATE_CONNECTED: ClassVar[int]
    STATE_CONNECTING: ClassVar[int]
    STATE_DISCONNECTED: ClassVar[int]
    STATE_DISCONNECTING: ClassVar[int]
    def getConnectedGroupLeadDevice(self, p0: int) -> BluetoothDevice: ...
    def close(self) -> None: ...
    def getGroupId(self, p0: BluetoothDevice) -> int: ...
    def getConnectedDevices(self) -> list: ...
    def getConnectionState(self, p0: BluetoothDevice) -> int: ...
    def getDevicesMatchingConnectionStates(self, p0: Any) -> list: ...

