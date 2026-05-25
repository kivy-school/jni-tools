from typing import Any, ClassVar, overload
from android.gms.internal.ads.zzbnm import zzbnm
from android.gms.internal.ads.zzbnp import zzbnp

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class OnCustomFormatAdLoadedListener:
    """Forward declaration for ``com.google.android.gms.ads.nativead.NativeCustomFormatAd.OnCustomFormatAdLoadedListener``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.google.android.gms.ads.nativead.NativeCustomFormatAd.OnCustomFormatAdLoadedListener')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developers.google.com/android/reference/com/google/android/gms/ads/nativead/NativeCustomFormatAd/OnCustomFormatAdLoadedListener
    """
    ...
class OnCustomClickListener:
    """Forward declaration for ``com.google.android.gms.ads.nativead.NativeCustomFormatAd.OnCustomClickListener``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.google.android.gms.ads.nativead.NativeCustomFormatAd.OnCustomClickListener')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developers.google.com/android/reference/com/google/android/gms/ads/nativead/NativeCustomFormatAd/OnCustomClickListener
    """
    ...

class zzbyv:
    def __init__(self, arg0: OnCustomFormatAdLoadedListener, arg1: OnCustomClickListener) -> None: ...
    def zza(self) -> zzbnp: ...
    def zzb(self) -> zzbnm: ...
