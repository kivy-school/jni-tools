from typing import Any, ClassVar, overload
from android.gms.internal.ads.zzidl import zzidl
from android.gms.internal.ads.zzidu import zzidu
from android.gms.internal.ads.zzify import zzify

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class OutputStream:
    """Forward declaration for ``java.io.OutputStream``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.io.OutputStream')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/io/OutputStream.html
    """
    ...

class zzicv:
    def __init__(self) -> None: ...
    def zzcY(self) -> zzify: ...
    def zzaM(self) -> zzidl: ...
    def zzaO(self, arg0: OutputStream) -> None: ...
    def zzcX(self, arg0: zzidu) -> None: ...
