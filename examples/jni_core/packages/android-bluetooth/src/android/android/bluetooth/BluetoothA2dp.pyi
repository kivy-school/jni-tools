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
    def isA2dpPlaying(self, p0: BluetoothDevice) -> bool: ...
    def getSupportedCodecTypes(self) -> list: ...
    def getConnectedDevices(self) -> list: ...
    def getConnectionState(self, p0: BluetoothDevice) -> int: ...
    def getDevicesMatchingConnectionStates(self, p0: Any) -> list: ...
    def finalize(self) -> None: ...
