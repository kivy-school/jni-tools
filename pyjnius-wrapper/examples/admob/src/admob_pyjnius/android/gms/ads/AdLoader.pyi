from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.gms.ads.AdListener import AdListener
from android.gms.ads.AdRequest import AdRequest
from android.gms.ads.AdSize import AdSize
from android.gms.ads.admanager.AdManagerAdRequest import AdManagerAdRequest
from android.gms.ads.formats.AdManagerAdViewOptions import AdManagerAdViewOptions
from android.gms.ads.formats.NativeAdOptions import NativeAdOptions
from android.gms.ads.formats.OnAdManagerAdViewLoadedListener import OnAdManagerAdViewLoadedListener
from android.gms.ads.formats.zzd import zzd
from android.gms.ads.formats.zze import zze
from android.gms.ads.formats.zzg import zzg
from android.gms.ads.nativead.NativeAdOptions import NativeAdOptions

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

class AdLoader:
    @overload
    def loadAd(self, arg0: AdRequest) -> None: ...
    @overload
    def loadAd(self, arg0: AdManagerAdRequest) -> None: ...
    def loadAds(self, arg0: AdRequest, arg1: int) -> None: ...
    def isLoading(self) -> bool: ...

    class Builder:
        def __init__(self, arg0: Context, arg1: str) -> None: ...
        def forNativeAd(self, arg0: OnNativeAdLoadedListener) -> "Builder": ...
        def forCustomFormatAd(self, arg0: str, arg1: OnCustomFormatAdLoadedListener, arg2: OnCustomClickListener) -> "Builder": ...
        def forAdManagerAdView(self, arg0: OnAdManagerAdViewLoadedListener, *arg1: AdSize) -> "Builder": ...
        def withAdListener(self, arg0: AdListener) -> "Builder": ...
        def withNativeAdOptions(self, arg0: NativeAdOptions) -> "Builder": ...
        def withAdManagerAdViewOptions(self, arg0: AdManagerAdViewOptions) -> "Builder": ...
        def build(self) -> "AdLoader": ...
        def zza(self, arg0: zzg) -> "Builder": ...
        def zzb(self, arg0: str, arg1: zze, arg2: zzd) -> "Builder": ...
        def zzc(self, arg0: NativeAdOptions) -> "Builder": ...
