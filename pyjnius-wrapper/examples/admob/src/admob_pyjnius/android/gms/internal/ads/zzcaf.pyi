from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.gms.ads.internal.util.client.VersionInfoParcel import VersionInfoParcel
from android.gms.internal.ads.zzcah import zzcah

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Throwable:
    """Forward declaration for ``java.lang.Throwable``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.lang.Throwable')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html
    """
    ...
class Thread:
    """Forward declaration for ``java.lang.Thread``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.lang.Thread')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/lang/Thread.html
    """
    ...

class zzcaf:
    zza: ClassVar[zzcah]
    @overload
    def __init__(self, arg0: Context, arg1: VersionInfoParcel) -> None: ...
    @overload
    def __init__(self, arg0: Context, arg1: VersionInfoParcel, arg2: bool) -> None: ...
    @staticmethod
    def zza(arg0: Context) -> zzcah: ...
    @staticmethod
    def zzb(arg0: Context, arg1: VersionInfoParcel) -> zzcah: ...
    @staticmethod
    def zzc(arg0: Context) -> zzcah: ...
    @staticmethod
    def zzd(arg0: Context, arg1: VersionInfoParcel) -> zzcah: ...
    @staticmethod
    def zze(arg0: Throwable) -> str: ...
    @staticmethod
    def zzf(arg0: Throwable) -> str: ...
    def zzg(self, arg0: Thread, arg1: Throwable) -> None: ...
    def zzh(self, arg0: Throwable, arg1: str) -> None: ...
    def zzi(self, arg0: Throwable, arg1: str, arg2: float) -> None: ...
