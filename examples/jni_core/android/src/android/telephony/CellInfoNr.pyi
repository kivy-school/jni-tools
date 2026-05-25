from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.telephony.CellIdentity import CellIdentity
from android.telephony.CellSignalStrength import CellSignalStrength

class CellInfoNr:
    CREATOR: ClassVar[Any]
    CONNECTION_NONE: ClassVar[int]
    CONNECTION_PRIMARY_SERVING: ClassVar[int]
    CONNECTION_SECONDARY_SERVING: ClassVar[int]
    CONNECTION_UNKNOWN: ClassVar[int]
    CREATOR: ClassVar[Any]
    UNAVAILABLE: ClassVar[int]
    UNAVAILABLE_LONG: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getCellSignalStrength(self) -> CellSignalStrength: ...
    def getCellIdentity(self) -> CellIdentity: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
