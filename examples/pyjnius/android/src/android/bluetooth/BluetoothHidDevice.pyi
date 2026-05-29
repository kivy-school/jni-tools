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
    def connect(self, p0: BluetoothDevice) -> bool: ...
    def getConnectionState(self, p0: BluetoothDevice) -> int: ...
    def getConnectedDevices(self) -> list: ...
    def getDevicesMatchingConnectionStates(self, p0: Any) -> list: ...
    def disconnect(self, p0: BluetoothDevice) -> bool: ...
    def registerApp(self, p0: BluetoothHidDeviceAppSdpSettings, p1: BluetoothHidDeviceAppQosSettings, p2: BluetoothHidDeviceAppQosSettings, p3: Executor, p4: Any) -> bool: ...
    def replyReport(self, p0: BluetoothDevice, p1: int, p2: int, p3: Any) -> bool: ...
    def reportError(self, p0: BluetoothDevice, p1: int) -> bool: ...
    def sendReport(self, p0: BluetoothDevice, p1: int, p2: Any) -> bool: ...
    def unregisterApp(self) -> bool: ...

    class Callback:
        def __init__(self) -> None: ...
        def onAppStatusChanged(self, p0: BluetoothDevice, p1: bool) -> None: ...
        def onVirtualCableUnplug(self, p0: BluetoothDevice) -> None: ...
        def onInterruptData(self, p0: BluetoothDevice, p1: int, p2: Any) -> None: ...
        def onGetReport(self, p0: BluetoothDevice, p1: int, p2: int, p3: int) -> None: ...
        def onSetProtocol(self, p0: BluetoothDevice, p1: int) -> None: ...
        def onSetReport(self, p0: BluetoothDevice, p1: int, p2: int, p3: Any) -> None: ...
        def onConnectionStateChanged(self, p0: BluetoothDevice, p1: int) -> None: ...
