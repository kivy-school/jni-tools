from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class WifiP2pPairingBootstrappingConfig:
    CREATOR: ClassVar[Any]
    PAIRING_BOOTSTRAPPING_METHOD_DISPLAY_PASSPHRASE: ClassVar[int]
    PAIRING_BOOTSTRAPPING_METHOD_DISPLAY_PINCODE: ClassVar[int]
    PAIRING_BOOTSTRAPPING_METHOD_KEYPAD_PASSPHRASE: ClassVar[int]
    PAIRING_BOOTSTRAPPING_METHOD_KEYPAD_PINCODE: ClassVar[int]
    PAIRING_BOOTSTRAPPING_METHOD_OPPORTUNISTIC: ClassVar[int]
    PAIRING_BOOTSTRAPPING_METHOD_OUT_OF_BAND: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: int, p1: str) -> None: ...
    def toString(self) -> str: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
