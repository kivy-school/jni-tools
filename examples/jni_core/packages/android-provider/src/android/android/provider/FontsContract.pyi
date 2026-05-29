from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.graphics.Typeface import Typeface
from android.net.Uri import Uri
from android.os.CancellationSignal import CancellationSignal
from android.os.Handler import Handler
from android.provider.FontRequest import FontRequest

class FontsContract:
    @staticmethod
    def buildTypeface(p0: Context, p1: CancellationSignal, p2: Any) -> Typeface: ...
    @staticmethod
    def fetchFonts(p0: Context, p1: CancellationSignal, p2: FontRequest) -> Any: ...
    @staticmethod
    def requestFonts(p0: Context, p1: FontRequest, p2: Handler, p3: CancellationSignal, p4: Any) -> None: ...

    class FontRequestCallback:
        FAIL_REASON_FONT_LOAD_ERROR: ClassVar[int]
        FAIL_REASON_FONT_NOT_FOUND: ClassVar[int]
        FAIL_REASON_FONT_UNAVAILABLE: ClassVar[int]
        FAIL_REASON_MALFORMED_QUERY: ClassVar[int]
        FAIL_REASON_PROVIDER_NOT_FOUND: ClassVar[int]
        FAIL_REASON_WRONG_CERTIFICATES: ClassVar[int]
        def __init__(self) -> None: ...
        def onTypefaceRequestFailed(self, p0: int) -> None: ...
        def onTypefaceRetrieved(self, p0: Typeface) -> None: ...

    class FontInfo:
        def getUri(self) -> Uri: ...
        def isItalic(self) -> bool: ...
        def getWeight(self) -> int: ...
        def getResultCode(self) -> int: ...
        def getAxes(self) -> Any: ...
        def getTtcIndex(self) -> int: ...

    class FontFamilyResult:
        STATUS_OK: ClassVar[int]
        STATUS_REJECTED: ClassVar[int]
        STATUS_UNEXPECTED_DATA_PROVIDED: ClassVar[int]
        STATUS_WRONG_CERTIFICATES: ClassVar[int]
        def getStatusCode(self) -> int: ...
        def getFonts(self) -> Any: ...

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
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]
