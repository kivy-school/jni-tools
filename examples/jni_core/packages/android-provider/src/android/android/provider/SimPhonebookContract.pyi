from typing import Any, ClassVar, overload
from android.content.ContentResolver import ContentResolver
from android.net.Uri import Uri

class SimPhonebookContract:
    AUTHORITY: ClassVar[str]
    AUTHORITY_URI: ClassVar[Uri]

    class SimRecords:
        CONTENT_ITEM_TYPE: ClassVar[str]
        CONTENT_TYPE: ClassVar[str]
        ELEMENTARY_FILE_TYPE: ClassVar[str]
        ERROR_NAME_UNSUPPORTED: ClassVar[int]
        NAME: ClassVar[str]
        PHONE_NUMBER: ClassVar[str]
        RECORD_NUMBER: ClassVar[str]
        SUBSCRIPTION_ID: ClassVar[str]
        @staticmethod
        def getEncodedNameLength(p0: ContentResolver, p1: str) -> int: ...
        @staticmethod
        def getItemUri(p0: int, p1: int, p2: int) -> Uri: ...
        @staticmethod
        def getContentUri(p0: int, p1: int) -> Uri: ...

    class ElementaryFiles:
        CONTENT_ITEM_TYPE: ClassVar[str]
        CONTENT_TYPE: ClassVar[str]
        CONTENT_URI: ClassVar[Uri]
        EF_ADN: ClassVar[int]
        EF_FDN: ClassVar[int]
        EF_SDN: ClassVar[int]
        EF_TYPE: ClassVar[str]
        EF_UNKNOWN: ClassVar[int]
        MAX_RECORDS: ClassVar[str]
        NAME_MAX_LENGTH: ClassVar[str]
        PHONE_NUMBER_MAX_LENGTH: ClassVar[str]
        RECORD_COUNT: ClassVar[str]
        SLOT_INDEX: ClassVar[str]
        SUBSCRIPTION_ID: ClassVar[str]
        @staticmethod
        def getItemUri(p0: int, p1: int) -> Uri: ...
