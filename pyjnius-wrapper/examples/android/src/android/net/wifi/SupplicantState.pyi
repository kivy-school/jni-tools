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
    @staticmethod
    def values() -> list["SupplicantState"]: ...
    @staticmethod
    def valueOf(arg0: str) -> "SupplicantState": ...
    @staticmethod
    def isValidState(arg0: "SupplicantState") -> bool: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
