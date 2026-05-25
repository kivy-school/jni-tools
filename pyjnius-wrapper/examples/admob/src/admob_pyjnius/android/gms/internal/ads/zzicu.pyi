from typing import Any, ClassVar, overload
from android.gms.internal.ads.zzidl import zzidl
from android.gms.internal.ads.zzige import zzige

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
class Iterable:
    """Forward declaration for ``java.lang.Iterable``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.lang.Iterable')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html
    """
    ...

class zzicu:
    zzq: int
    def __init__(self) -> None: ...
    def zzaM(self) -> zzidl: ...
    def zzaN(self) -> list[int]: ...
    def zzaO(self, arg0: OutputStream) -> None: ...
    def zzaP(self, arg0: OutputStream) -> None: ...
    def zzaS(self) -> zzige: ...
    @staticmethod
    def zzaV(arg0: zzidl) -> None: ...
    @staticmethod
    def zzaW(arg0: Iterable, arg1: list) -> None: ...
