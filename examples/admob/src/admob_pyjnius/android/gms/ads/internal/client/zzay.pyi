from typing import Any, ClassVar, overload
from android.gms.ads.internal.client.zzaw import zzaw
from android.gms.ads.internal.util.client.VersionInfoParcel import VersionInfoParcel
from android.gms.ads.internal.util.client.zzf import zzf

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Random:
    """Forward declaration for ``java.util.Random``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.util.Random')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/util/Random.html
    """
    ...

class zzay:
    def __init__(self) -> None: ...
    @staticmethod
    def zza() -> zzf: ...
    @staticmethod
    def zzb() -> zzaw: ...
    @staticmethod
    def zzc() -> None: ...
    @staticmethod
    def zzd() -> None: ...
    @staticmethod
    def zze() -> bool: ...
    @staticmethod
    def zzf() -> str: ...
    @staticmethod
    def zzg() -> VersionInfoParcel: ...
    @staticmethod
    def zzh() -> Random: ...
