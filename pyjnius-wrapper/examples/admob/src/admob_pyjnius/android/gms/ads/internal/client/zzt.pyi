from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.os.Parcelable.Creator import Creator

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class JSONObject:
    """Forward declaration for ``org.json.JSONObject``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONObject')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class zzt:
    CREATOR: ClassVar[Creator]
    zza: int
    zzb: int
    zzc: str
    zzd: int
    def __init__(self, arg0: int, arg1: int, arg2: str, arg3: int) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    @staticmethod
    def zza(arg0: JSONObject) -> "zzt": ...
