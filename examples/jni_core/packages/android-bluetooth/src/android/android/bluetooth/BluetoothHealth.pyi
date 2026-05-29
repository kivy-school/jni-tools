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
    def registerSinkAppConfiguration(self, p0: str, p1: int, p2: BluetoothHealthCallback) -> bool: ...
    def unregisterAppConfiguration(self, p0: BluetoothHealthAppConfiguration) -> bool: ...
    def connectChannelToSource(self, p0: BluetoothDevice, p1: BluetoothHealthAppConfiguration) -> bool: ...
    def disconnectChannel(self, p0: BluetoothDevice, p1: BluetoothHealthAppConfiguration, p2: int) -> bool: ...
    def getMainChannelFd(self, p0: BluetoothDevice, p1: BluetoothHealthAppConfiguration) -> ParcelFileDescriptor: ...
    def getConnectedDevices(self) -> list: ...
    def getConnectionState(self, p0: BluetoothDevice) -> int: ...
    def getDevicesMatchingConnectionStates(self, p0: Any) -> list: ...
