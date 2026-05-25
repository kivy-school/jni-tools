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
    def getDevicesMatchingConnectionStates(self, arg0: list[int]) -> list: ...
    def getConnectionState(self, arg0: BluetoothDevice) -> int: ...

    class ServiceListener:
        def onServiceConnected(self, arg0: int, arg1: "BluetoothProfile") -> None: ...
        def onServiceDisconnected(self, arg0: int) -> None: ...
