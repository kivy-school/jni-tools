from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class SupplicantState:
    DISCONNECTED: ClassVar["SupplicantState"]
    INTERFACE_DISABLED: ClassVar["SupplicantState"]
    INACTIVE: ClassVar["SupplicantState"]
    SCANNING: ClassVar["SupplicantState"]
    AUTHENTICATING: ClassVar["SupplicantState"]
    ASSOCIATING: ClassVar["SupplicantState"]
    ASSOCIATED: ClassVar["SupplicantState"]
    FOUR_WAY_HANDSHAKE: ClassVar["SupplicantState"]
    GROUP_HANDSHAKE: ClassVar["SupplicantState"]
    COMPLETED: ClassVar["SupplicantState"]
    DORMANT: ClassVar["SupplicantState"]
    UNINITIALIZED: ClassVar["SupplicantState"]
    INVALID: ClassVar["SupplicantState"]
    DISCONNECTED: ClassVar["SupplicantState"]
    INTERFACE_DISABLED: ClassVar["SupplicantState"]
    INACTIVE: ClassVar["SupplicantState"]
    SCANNING: ClassVar["SupplicantState"]
    AUTHENTICATING: ClassVar["SupplicantState"]
    ASSOCIATING: ClassVar["SupplicantState"]
    ASSOCIATED: ClassVar["SupplicantState"]
    FOUR_WAY_HANDSHAKE: ClassVar["SupplicantState"]
    GROUP_HANDSHAKE: ClassVar["SupplicantState"]
    COMPLETED: ClassVar["SupplicantState"]
    DORMANT: ClassVar["SupplicantState"]
    UNINITIALIZED: ClassVar["SupplicantState"]
    INVALID: ClassVar["SupplicantState"]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    @staticmethod
    def isValidState(p0: "SupplicantState") -> bool: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "SupplicantState": ...
