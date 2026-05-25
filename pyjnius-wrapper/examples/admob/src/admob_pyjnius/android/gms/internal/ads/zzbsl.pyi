from typing import Any, ClassVar, overload
from android.gms.ads.internal.client.zzea import zzea
from android.gms.internal.ads.zzbmi import zzbmi
from android.gms.internal.ads.zzbso import zzbso

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

class zzbsl:
    def zzb(self) -> zzea: ...
    def zzc(self) -> None: ...
    def zzd(self, arg0: IObjectWrapper, arg1: zzbso) -> None: ...
    def zze(self, arg0: IObjectWrapper) -> None: ...
    def zzf(self) -> zzbmi: ...
