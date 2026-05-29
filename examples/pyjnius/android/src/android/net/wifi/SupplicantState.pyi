from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class SupplicantState:
    ASSOCIATED: ClassVar["SupplicantState"]
    ASSOCIATING: ClassVar["SupplicantState"]
    AUTHENTICATING: ClassVar["SupplicantState"]
    COMPLETED: ClassVar["SupplicantState"]
    DISCONNECTED: ClassVar["SupplicantState"]
    DORMANT: ClassVar["SupplicantState"]
    FOUR_WAY_HANDSHAKE: ClassVar["SupplicantState"]
    GROUP_HANDSHAKE: ClassVar["SupplicantState"]
    INACTIVE: ClassVar["SupplicantState"]
    INTERFACE_DISABLED: ClassVar["SupplicantState"]
    INVALID: ClassVar["SupplicantState"]
    SCANNING: ClassVar["SupplicantState"]
    UNINITIALIZED: ClassVar["SupplicantState"]
    ASSOCIATED: ClassVar["SupplicantState"]
    ASSOCIATING: ClassVar["SupplicantState"]
    AUTHENTICATING: ClassVar["SupplicantState"]
    COMPLETED: ClassVar["SupplicantState"]
    DISCONNECTED: ClassVar["SupplicantState"]
    DORMANT: ClassVar["SupplicantState"]
    FOUR_WAY_HANDSHAKE: ClassVar["SupplicantState"]
    GROUP_HANDSHAKE: ClassVar["SupplicantState"]
    INACTIVE: ClassVar["SupplicantState"]
    INTERFACE_DISABLED: ClassVar["SupplicantState"]
    INVALID: ClassVar["SupplicantState"]
    SCANNING: ClassVar["SupplicantState"]
    UNINITIALIZED: ClassVar["SupplicantState"]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    @staticmethod
    def isValidState(p0: "SupplicantState") -> bool: ...
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "SupplicantState": ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
