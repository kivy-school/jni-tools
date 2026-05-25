from typing import Any, ClassVar, overload
from android.gms.internal.ads.zzgug import zzgug

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

class zzo:
    zzb: ClassVar[zzgug]
    @staticmethod
    def zzd(arg0: str) -> None: ...
    @staticmethod
    def zze(arg0: str, arg1: Throwable) -> None: ...
    @staticmethod
    def zzf(arg0: str) -> None: ...
    @staticmethod
    def zzg(arg0: str, arg1: Throwable) -> None: ...
    @staticmethod
    def zzh(arg0: str) -> None: ...
    @staticmethod
    def zzi(arg0: str) -> None: ...
    @staticmethod
    def zzj(arg0: str, arg1: Throwable) -> None: ...
    @staticmethod
    def zzl(arg0: str, arg1: Throwable) -> None: ...
    @staticmethod
    def zzm(arg0: int) -> bool: ...
