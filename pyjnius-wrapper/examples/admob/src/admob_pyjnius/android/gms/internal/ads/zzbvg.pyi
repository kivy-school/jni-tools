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
class Throwable:
    """Forward declaration for ``java.lang.Throwable``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.lang.Throwable')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html
    """
    ...

class zzbvg:
    @staticmethod
    def zza(arg0: IObjectWrapper, arg1: Throwable, arg2: str) -> None: ...
