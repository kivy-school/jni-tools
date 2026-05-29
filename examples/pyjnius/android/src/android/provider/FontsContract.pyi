from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.graphics.Typeface import Typeface
from android.graphics.fonts.FontVariationAxis import FontVariationAxis
from android.net.Uri import Uri
from android.os.CancellationSignal import CancellationSignal
from android.os.Handler import Handler
from android.provider.FontRequest import FontRequest

class FontsContract:
    @staticmethod
    def requestFonts(arg0: Context, arg1: FontRequest, arg2: Handler, arg3: CancellationSignal, arg4: "FontRequestCallback") -> None: ...
    @staticmethod
    def fetchFonts(arg0: Context, arg1: CancellationSignal, arg2: FontRequest) -> "FontFamilyResult": ...
    @staticmethod
    def buildTypeface(arg0: Context, arg1: CancellationSignal, arg2: list["FontInfo"]) -> Typeface: ...

    class Columns:
        FILE_ID: ClassVar[str]
        ITALIC: ClassVar[str]
        RESULT_CODE: ClassVar[str]
        RESULT_CODE_FONT_NOT_FOUND: ClassVar[int]
        RESULT_CODE_FONT_UNAVAILABLE: ClassVar[int]
        RESULT_CODE_MALFORMED_QUERY: ClassVar[int]
        RESULT_CODE_OK: ClassVar[int]
        TTC_INDEX: ClassVar[str]
        VARIATION_SETTINGS: ClassVar[str]
        WEIGHT: ClassVar[str]

    class FontFamilyResult:
        STATUS_OK: ClassVar[int]
        STATUS_REJECTED: ClassVar[int]
        STATUS_UNEXPECTED_DATA_PROVIDED: ClassVar[int]
        STATUS_WRONG_CERTIFICATES: ClassVar[int]
        def getStatusCode(self) -> int: ...
        def getFonts(self) -> list["FontInfo"]: ...

    class FontInfo:
        def getUri(self) -> Uri: ...
        def getTtcIndex(self) -> int: ...
        def getAxes(self) -> list[FontVariationAxis]: ...
        def getWeight(self) -> int: ...
        def isItalic(self) -> bool: ...
        def getResultCode(self) -> int: ...

    class FontRequestCallback:
        FAIL_REASON_FONT_LOAD_ERROR: ClassVar[int]
        FAIL_REASON_FONT_NOT_FOUND: ClassVar[int]
        FAIL_REASON_FONT_UNAVAILABLE: ClassVar[int]
        FAIL_REASON_MALFORMED_QUERY: ClassVar[int]
        FAIL_REASON_PROVIDER_NOT_FOUND: ClassVar[int]
        FAIL_REASON_WRONG_CERTIFICATES: ClassVar[int]
        def __init__(self) -> None: ...
        def onTypefaceRetrieved(self, arg0: Typeface) -> None: ...
        def onTypefaceRequestFailed(self, arg0: int) -> None: ...
