from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class SignalingDataRequest:
    CREATOR: ClassVar[Any]
    SIGNALING_DATA_NO_GROUP_ID: ClassVar[int]
    SIGNALING_METADATA_AEAT: ClassVar[str]
    SIGNALING_METADATA_AEI: ClassVar[str]
    SIGNALING_METADATA_APD: ClassVar[str]
    SIGNALING_METADATA_ASD: ClassVar[str]
    SIGNALING_METADATA_ASPD: ClassVar[str]
    SIGNALING_METADATA_CAD: ClassVar[str]
    SIGNALING_METADATA_CDT: ClassVar[str]
    SIGNALING_METADATA_CRIT: ClassVar[str]
    SIGNALING_METADATA_DCIT: ClassVar[str]
    SIGNALING_METADATA_DWD: ClassVar[str]
    SIGNALING_METADATA_EMSG: ClassVar[str]
    SIGNALING_METADATA_EVTI: ClassVar[str]
    SIGNALING_METADATA_HELD: ClassVar[str]
    SIGNALING_METADATA_IED: ClassVar[str]
    SIGNALING_METADATA_MPD: ClassVar[str]
    SIGNALING_METADATA_MPIT: ClassVar[str]
    SIGNALING_METADATA_MPT: ClassVar[str]
    SIGNALING_METADATA_OSN: ClassVar[str]
    SIGNALING_METADATA_PAT: ClassVar[str]
    SIGNALING_METADATA_RDT: ClassVar[str]
    SIGNALING_METADATA_RRT: ClassVar[str]
    SIGNALING_METADATA_RSAT: ClassVar[str]
    SIGNALING_METADATA_SLT: ClassVar[str]
    SIGNALING_METADATA_SMT: ClassVar[str]
    SIGNALING_METADATA_SSD: ClassVar[str]
    SIGNALING_METADATA_STSID: ClassVar[str]
    SIGNALING_METADATA_STT: ClassVar[str]
    SIGNALING_METADATA_USBD: ClassVar[str]
    SIGNALING_METADATA_USD: ClassVar[str]
    SIGNALING_METADATA_VSPD: ClassVar[str]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CREATOR: ClassVar[Any]
    REQUEST_OPTION_AUTO_UPDATE: ClassVar[int]
    REQUEST_OPTION_ONESHOT: ClassVar[int]
    REQUEST_OPTION_ONEWAY: ClassVar[int]
    REQUEST_OPTION_REPEAT: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: int, p3: list) -> None: ...
    def getSignalingDataTypes(self) -> list: ...
    def getGroup(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
