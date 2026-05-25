from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class BluetoothClass:
    CREATOR: ClassVar[Any]
    PROFILE_A2DP: ClassVar[int]
    PROFILE_HEADSET: ClassVar[int]
    PROFILE_HID: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def hasService(self, p0: int) -> bool: ...
    def getMajorDeviceClass(self) -> int: ...
    def doesClassMatch(self, p0: int) -> bool: ...
    def getDeviceClass(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...

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
