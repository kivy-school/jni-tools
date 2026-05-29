from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.telephony.CellIdentity import CellIdentity
from android.telephony.CellIdentityLte import CellIdentityLte
from android.telephony.CellSignalStrength import CellSignalStrength
from android.telephony.CellSignalStrengthLte import CellSignalStrengthLte

class CellInfoLte:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CONNECTION_NONE: ClassVar[int]
    CONNECTION_PRIMARY_SERVING: ClassVar[int]
    CONNECTION_SECONDARY_SERVING: ClassVar[int]
    CONNECTION_UNKNOWN: ClassVar[int]
    CREATOR: ClassVar[Any]
    UNAVAILABLE: ClassVar[int]
    UNAVAILABLE_LONG: ClassVar[int]
    @overload
    def getCellIdentity(self) -> CellIdentityLte: ...
    @overload
    def getCellIdentity(self) -> CellIdentity: ...
    @overload
    def getCellSignalStrength(self) -> CellSignalStrengthLte: ...
    @overload
    def getCellSignalStrength(self) -> CellSignalStrength: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
