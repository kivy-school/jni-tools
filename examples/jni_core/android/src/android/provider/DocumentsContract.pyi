from typing import Any, ClassVar, overload
from android.content.ContentResolver import ContentResolver
from android.content.Context import Context
from android.content.IntentSender import IntentSender
from android.graphics.Bitmap import Bitmap
from android.graphics.Point import Point
from android.net.Uri import Uri
from android.os.Bundle import Bundle
from android.os.CancellationSignal import CancellationSignal
from android.os.Parcel import Parcel

class DocumentsContract:
    ACTION_DOCUMENT_SETTINGS: ClassVar[str]
    EXTRA_ERROR: ClassVar[str]
    EXTRA_EXCLUDE_SELF: ClassVar[str]
    EXTRA_INFO: ClassVar[str]
    EXTRA_INITIAL_URI: ClassVar[str]
    EXTRA_LOADING: ClassVar[str]
    EXTRA_ORIENTATION: ClassVar[str]
    EXTRA_PROMPT: ClassVar[str]
    METADATA_EXIF: ClassVar[str]
    METADATA_TREE_COUNT: ClassVar[str]
    METADATA_TREE_SIZE: ClassVar[str]
    METADATA_TYPES: ClassVar[str]
    PROVIDER_INTERFACE: ClassVar[str]
    QUERY_ARG_DISPLAY_NAME: ClassVar[str]
    QUERY_ARG_EXCLUDE_MEDIA: ClassVar[str]
    QUERY_ARG_FILE_SIZE_OVER: ClassVar[str]
    QUERY_ARG_LAST_MODIFIED_AFTER: ClassVar[str]
    QUERY_ARG_MIME_TYPES: ClassVar[str]
    @staticmethod
    def buildRootsUri(p0: str) -> Uri: ...
    @staticmethod
    def buildRootUri(p0: str, p1: str) -> Uri: ...
    @staticmethod
    def buildRecentDocumentsUri(p0: str, p1: str) -> Uri: ...
    @staticmethod
    def buildTreeDocumentUri(p0: str, p1: str) -> Uri: ...
    @staticmethod
    def buildDocumentUri(p0: str, p1: str) -> Uri: ...
    @staticmethod
    def buildDocumentUriUsingTree(p0: Uri, p1: str) -> Uri: ...
    @staticmethod
    def buildChildDocumentsUri(p0: str, p1: str) -> Uri: ...
    @staticmethod
    def buildChildDocumentsUriUsingTree(p0: Uri, p1: str) -> Uri: ...
    @staticmethod
    def buildSearchDocumentsUri(p0: str, p1: str, p2: str) -> Uri: ...
    @staticmethod
    def isDocumentUri(p0: Context, p1: Uri) -> bool: ...
    @staticmethod
    def isRootsUri(p0: Context, p1: Uri) -> bool: ...
    @staticmethod
    def isRootUri(p0: Context, p1: Uri) -> bool: ...
    @staticmethod
    def isTreeUri(p0: Uri) -> bool: ...
    @staticmethod
    def getRootId(p0: Uri) -> str: ...
    @staticmethod
    def getDocumentId(p0: Uri) -> str: ...
    @staticmethod
    def getTreeDocumentId(p0: Uri) -> str: ...
    @staticmethod
    def getSearchDocumentsQuery(p0: Uri) -> str: ...
    @staticmethod
    def getDocumentThumbnail(p0: ContentResolver, p1: Uri, p2: Point, p3: CancellationSignal) -> Bitmap: ...
    @staticmethod
    def createDocument(p0: ContentResolver, p1: Uri, p2: str, p3: str) -> Uri: ...
    @staticmethod
    def isChildDocument(p0: ContentResolver, p1: Uri, p2: Uri) -> bool: ...
    @staticmethod
    def renameDocument(p0: ContentResolver, p1: Uri, p2: str) -> Uri: ...
    @staticmethod
    def deleteDocument(p0: ContentResolver, p1: Uri) -> bool: ...
    @staticmethod
    def copyDocument(p0: ContentResolver, p1: Uri, p2: Uri) -> Uri: ...
    @staticmethod
    def moveDocument(p0: ContentResolver, p1: Uri, p2: Uri, p3: Uri) -> Uri: ...
    @staticmethod
    def removeDocument(p0: ContentResolver, p1: Uri, p2: Uri) -> bool: ...
    @staticmethod
    def ejectRoot(p0: ContentResolver, p1: Uri) -> None: ...
    @staticmethod
    def getDocumentMetadata(p0: ContentResolver, p1: Uri) -> Bundle: ...
    @staticmethod
    def findDocumentPath(p0: ContentResolver, p1: Uri) -> Any: ...
    @staticmethod
    def createWebLinkIntent(p0: ContentResolver, p1: Uri, p2: Bundle) -> IntentSender: ...

    class Root:
        COLUMN_AVAILABLE_BYTES: ClassVar[str]
        COLUMN_CAPACITY_BYTES: ClassVar[str]
        COLUMN_DOCUMENT_ID: ClassVar[str]
        COLUMN_FLAGS: ClassVar[str]
        COLUMN_ICON: ClassVar[str]
        COLUMN_MIME_TYPES: ClassVar[str]
        COLUMN_QUERY_ARGS: ClassVar[str]
        COLUMN_ROOT_ID: ClassVar[str]
        COLUMN_SUMMARY: ClassVar[str]
        COLUMN_TITLE: ClassVar[str]
        FLAG_EMPTY: ClassVar[int]
        FLAG_LOCAL_ONLY: ClassVar[int]
        FLAG_SUPPORTS_CREATE: ClassVar[int]
        FLAG_SUPPORTS_EJECT: ClassVar[int]
        FLAG_SUPPORTS_IS_CHILD: ClassVar[int]
        FLAG_SUPPORTS_RECENTS: ClassVar[int]
        FLAG_SUPPORTS_SEARCH: ClassVar[int]
        MIME_TYPE_ITEM: ClassVar[str]

    class Path:
        CREATOR: ClassVar[Any]
        CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
        PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
        def __init__(self, p0: str, p1: list) -> None: ...
        def getRootId(self) -> str: ...
        def describeContents(self) -> int: ...
        def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
        def getPath(self) -> list: ...
        def equals(self, p0: Any) -> bool: ...
        def toString(self) -> str: ...
        def hashCode(self) -> int: ...

    class Document:
        COLUMN_DISPLAY_NAME: ClassVar[str]
        COLUMN_DOCUMENT_ID: ClassVar[str]
        COLUMN_FLAGS: ClassVar[str]
        COLUMN_ICON: ClassVar[str]
        COLUMN_LAST_MODIFIED: ClassVar[str]
        COLUMN_MIME_TYPE: ClassVar[str]
        COLUMN_SIZE: ClassVar[str]
        COLUMN_SUMMARY: ClassVar[str]
        FLAG_DIR_BLOCKS_OPEN_DOCUMENT_TREE: ClassVar[int]
        FLAG_DIR_PREFERS_GRID: ClassVar[int]
        FLAG_DIR_PREFERS_LAST_MODIFIED: ClassVar[int]
        FLAG_DIR_SUPPORTS_CREATE: ClassVar[int]
        FLAG_PARTIAL: ClassVar[int]
        FLAG_SUPPORTS_COPY: ClassVar[int]
        FLAG_SUPPORTS_DELETE: ClassVar[int]
        FLAG_SUPPORTS_METADATA: ClassVar[int]
        FLAG_SUPPORTS_MOVE: ClassVar[int]
        FLAG_SUPPORTS_REMOVE: ClassVar[int]
        FLAG_SUPPORTS_RENAME: ClassVar[int]
        FLAG_SUPPORTS_SETTINGS: ClassVar[int]
        FLAG_SUPPORTS_THUMBNAIL: ClassVar[int]
        FLAG_SUPPORTS_WRITE: ClassVar[int]
        FLAG_VIRTUAL_DOCUMENT: ClassVar[int]
        FLAG_WEB_LINKABLE: ClassVar[int]
        MIME_TYPE_DIR: ClassVar[str]
