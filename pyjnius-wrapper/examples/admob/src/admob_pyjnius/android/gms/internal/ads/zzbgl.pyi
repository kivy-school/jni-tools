from typing import Any, ClassVar, overload
from android.gms.ads.internal.client.zze import zze
from android.gms.internal.ads.zzbgq import zzbgq

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class AppOpenAdLoadCallback:
    """Forward declaration for ``com.google.android.gms.ads.appopen.AppOpenAd.AppOpenAdLoadCallback``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.google.android.gms.ads.appopen.AppOpenAd.AppOpenAdLoadCallback')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developers.google.com/android/reference/com/google/android/gms/ads/appopen/AppOpenAd/AppOpenAdLoadCallback
    """
    ...

class zzbgl:
    def __init__(self, arg0: AppOpenAdLoadCallback, arg1: str) -> None: ...
    def zzb(self, arg0: zzbgq) -> None: ...
    def zzc(self, arg0: int) -> None: ...
    def zzd(self, arg0: zze) -> None: ...
