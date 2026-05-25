from typing import Any, ClassVar, overload
from android.gms.internal.ads.zzbqx import zzbqx
from android.gms.internal.ads.zzbra import zzbra
from android.gms.internal.ads.zzbvj import zzbvj

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class IObjectWrapper:
    """Forward declaration for ``com.google.android.gms.dynamic.IObjectWrapper``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.google.android.gms.dynamic.IObjectWrapper')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developers.google.com/android/reference/com/google/android/gms/dynamic/IObjectWrapper
    """
    ...

class zzbrd:
    def zze(self, arg0: IObjectWrapper, arg1: zzbvj, arg2: int, arg3: zzbqx) -> zzbra: ...
