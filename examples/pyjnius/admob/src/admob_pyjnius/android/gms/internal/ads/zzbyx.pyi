from typing import Any, ClassVar, overload
from android.gms.internal.ads.zzboc import zzboc

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class OnNativeAdLoadedListener:
    """Forward declaration for ``com.google.android.gms.ads.nativead.NativeAd.OnNativeAdLoadedListener``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.google.android.gms.ads.nativead.NativeAd.OnNativeAdLoadedListener')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developers.google.com/android/reference/com/google/android/gms/ads/nativead/NativeAd/OnNativeAdLoadedListener
    """
    ...

class zzbyx:
    def __init__(self, arg0: OnNativeAdLoadedListener) -> None: ...
    def zze(self, arg0: zzboc) -> None: ...
