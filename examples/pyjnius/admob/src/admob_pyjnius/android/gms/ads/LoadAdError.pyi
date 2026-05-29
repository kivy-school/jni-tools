from typing import Any, ClassVar, overload
from android.gms.ads.AdError import AdError
from android.gms.ads.ResponseInfo import ResponseInfo

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

class LoadAdError:
    def __init__(self, arg0: int, arg1: str, arg2: str, arg3: AdError, arg4: ResponseInfo) -> None: ...
    def getResponseInfo(self) -> ResponseInfo: ...
    def toString(self) -> str: ...
    def zzb(self) -> JSONObject: ...
