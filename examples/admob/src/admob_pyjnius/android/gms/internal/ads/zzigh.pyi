from typing import Any, ClassVar, overload
from android.gms.internal.ads.zzidl import zzidl
from android.gms.internal.ads.zzidp import zzidp
from android.gms.internal.ads.zzidz import zzidz

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class InputStream:
    """Forward declaration for ``java.io.InputStream``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.io.InputStream')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html
    """
    ...

class zzigh:
    def zzc(self, arg0: zzidp, arg1: zzidz) -> Any: ...
    def zzb(self, arg0: zzidl, arg1: zzidz) -> Any: ...
    def zza(self, arg0: InputStream, arg1: zzidz) -> Any: ...
