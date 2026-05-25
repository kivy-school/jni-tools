from typing import Any, ClassVar, overload

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

class zzbmu:
    def zzb(self, arg0: IObjectWrapper) -> None: ...
    def zzc(self) -> None: ...
    def zzd(self, arg0: IObjectWrapper) -> None: ...
