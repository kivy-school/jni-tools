from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.os.Parcelable.Creator import Creator

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class JSONArray:
    """Forward declaration for ``org.json.JSONArray``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONArray')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class zzcci:
    CREATOR: ClassVar[Creator]
    zza: str
    zzb: int
    def __init__(self, arg0: str, arg1: int) -> None: ...
    @staticmethod
    def zza(arg0: JSONArray) -> "zzcci": ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def equals(self, arg0: Any) -> bool: ...
    def hashCode(self) -> int: ...
