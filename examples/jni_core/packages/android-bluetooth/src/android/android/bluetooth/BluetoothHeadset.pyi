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
    def getConnectedDevices(self) -> list: ...
    def getConnectionState(self, p0: BluetoothDevice) -> int: ...
    def getDevicesMatchingConnectionStates(self, p0: Any) -> list: ...
    def isNoiseReductionSupported(self, p0: BluetoothDevice) -> bool: ...
    def isVoiceRecognitionSupported(self, p0: BluetoothDevice) -> bool: ...
    def startVoiceRecognition(self, p0: BluetoothDevice) -> bool: ...
    def stopVoiceRecognition(self, p0: BluetoothDevice) -> bool: ...
    def isAudioConnected(self, p0: BluetoothDevice) -> bool: ...
    def sendVendorSpecificResultCode(self, p0: BluetoothDevice, p1: str, p2: str) -> bool: ...
