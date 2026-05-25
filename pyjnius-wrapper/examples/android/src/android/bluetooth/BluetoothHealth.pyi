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
    def registerSinkAppConfiguration(self, arg0: str, arg1: int, arg2: BluetoothHealthCallback) -> bool: ...
    def unregisterAppConfiguration(self, arg0: BluetoothHealthAppConfiguration) -> bool: ...
    def connectChannelToSource(self, arg0: BluetoothDevice, arg1: BluetoothHealthAppConfiguration) -> bool: ...
    def disconnectChannel(self, arg0: BluetoothDevice, arg1: BluetoothHealthAppConfiguration, arg2: int) -> bool: ...
    def getMainChannelFd(self, arg0: BluetoothDevice, arg1: BluetoothHealthAppConfiguration) -> ParcelFileDescriptor: ...
    def getConnectionState(self, arg0: BluetoothDevice) -> int: ...
    def getConnectedDevices(self) -> list: ...
    def getDevicesMatchingConnectionStates(self, arg0: list[int]) -> list: ...
