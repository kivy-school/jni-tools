from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.net.Uri import Uri

class BlockedNumberContract:
    AUTHORITY: ClassVar[str]
    AUTHORITY_URI: ClassVar[Uri]
    @staticmethod
    def isBlocked(p0: Context, p1: str) -> bool: ...
    @staticmethod
    def unblock(p0: Context, p1: str) -> int: ...
    @staticmethod
    def canCurrentUserBlockNumbers(p0: Context) -> bool: ...

    class BlockedNumbers:
        COLUMN_E164_NUMBER: ClassVar[str]
        COLUMN_ID: ClassVar[str]
        COLUMN_ORIGINAL_NUMBER: ClassVar[str]
        CONTENT_ITEM_TYPE: ClassVar[str]
        CONTENT_TYPE: ClassVar[str]
        CONTENT_URI: ClassVar[Uri]
