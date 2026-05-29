from typing import Any, ClassVar, overload
from android.gms.ads.MediaContent import MediaContent
from android.gms.internal.ads.zzbnc import zzbnc

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Image:
    """Forward declaration for ``com.google.android.gms.ads.nativead.NativeAd.Image``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.google.android.gms.ads.nativead.NativeAd.Image')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developers.google.com/android/reference/com/google/android/gms/ads/nativead/NativeAd/Image
    """
    ...
class DisplayOpenMeasurement:
    """Forward declaration for ``com.google.android.gms.ads.nativead.NativeCustomFormatAd.DisplayOpenMeasurement``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.google.android.gms.ads.nativead.NativeCustomFormatAd.DisplayOpenMeasurement')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developers.google.com/android/reference/com/google/android/gms/ads/nativead/NativeCustomFormatAd/DisplayOpenMeasurement
    """
    ...

class zzbyw:
    def __init__(self, arg0: zzbnc) -> None: ...
    def getText(self, arg0: str) -> str: ...
    def getImage(self, arg0: str) -> Image: ...
    def getMediaContent(self) -> MediaContent: ...
    def getAvailableAssetNames(self) -> list: ...
    def getCustomFormatId(self) -> str: ...
    def performClick(self, arg0: str) -> None: ...
    def recordImpression(self) -> None: ...
    def getDisplayOpenMeasurement(self) -> DisplayOpenMeasurement: ...
    def destroy(self) -> None: ...
