from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class UnconfirmedClickListener:
    """Forward declaration for ``com.google.android.gms.ads.nativead.NativeAd.UnconfirmedClickListener``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.google.android.gms.ads.nativead.NativeAd.UnconfirmedClickListener')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developers.google.com/android/reference/com/google/android/gms/ads/nativead/NativeAd/UnconfirmedClickListener
    """
    ...

class zzbyy:
    def __init__(self, arg0: UnconfirmedClickListener) -> None: ...
    def zze(self, arg0: str) -> None: ...
    def zzf(self) -> None: ...
