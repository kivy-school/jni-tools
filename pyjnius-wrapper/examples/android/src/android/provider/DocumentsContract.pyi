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

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator:
    """Forward declaration for ``android.os.Parcelable.Creator``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Parcelable.Creator')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Parcelable/Creator
    """
    ...

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
    def buildRootsUri(arg0: str) -> Uri: ...
    @staticmethod
    def buildRootUri(arg0: str, arg1: str) -> Uri: ...
    @staticmethod
    def buildRecentDocumentsUri(arg0: str, arg1: str) -> Uri: ...
    @staticmethod
    def buildTreeDocumentUri(arg0: str, arg1: str) -> Uri: ...
    @staticmethod
    def buildDocumentUri(arg0: str, arg1: str) -> Uri: ...
    @staticmethod
    def buildDocumentUriUsingTree(arg0: Uri, arg1: str) -> Uri: ...
    @staticmethod
    def buildChildDocumentsUri(arg0: str, arg1: str) -> Uri: ...
    @staticmethod
    def buildChildDocumentsUriUsingTree(arg0: Uri, arg1: str) -> Uri: ...
    @staticmethod
    def buildSearchDocumentsUri(arg0: str, arg1: str, arg2: str) -> Uri: ...
    @staticmethod
    def isDocumentUri(arg0: Context, arg1: Uri) -> bool: ...
    @staticmethod
    def isRootsUri(arg0: Context, arg1: Uri) -> bool: ...
    @staticmethod
    def isRootUri(arg0: Context, arg1: Uri) -> bool: ...
    @staticmethod
    def isTreeUri(arg0: Uri) -> bool: ...
    @staticmethod
    def getRootId(arg0: Uri) -> str: ...
    @staticmethod
    def getDocumentId(arg0: Uri) -> str: ...
    @staticmethod
    def getTreeDocumentId(arg0: Uri) -> str: ...
    @staticmethod
    def getSearchDocumentsQuery(arg0: Uri) -> str: ...
    @staticmethod
    def getDocumentThumbnail(arg0: ContentResolver, arg1: Uri, arg2: Point, arg3: CancellationSignal) -> Bitmap: ...
    @staticmethod
    def createDocument(arg0: ContentResolver, arg1: Uri, arg2: str, arg3: str) -> Uri: ...
    @staticmethod
    def isChildDocument(arg0: ContentResolver, arg1: Uri, arg2: Uri) -> bool: ...
    @staticmethod
    def renameDocument(arg0: ContentResolver, arg1: Uri, arg2: str) -> Uri: ...
    @staticmethod
    def deleteDocument(arg0: ContentResolver, arg1: Uri) -> bool: ...
    @staticmethod
    def copyDocument(arg0: ContentResolver, arg1: Uri, arg2: Uri) -> Uri: ...
    @staticmethod
    def moveDocument(arg0: ContentResolver, arg1: Uri, arg2: Uri, arg3: Uri) -> Uri: ...
    @staticmethod
    def removeDocument(arg0: ContentResolver, arg1: Uri, arg2: Uri) -> bool: ...
    @staticmethod
    def ejectRoot(arg0: ContentResolver, arg1: Uri) -> None: ...
    @staticmethod
    def getDocumentMetadata(arg0: ContentResolver, arg1: Uri) -> Bundle: ...
    @staticmethod
    def findDocumentPath(arg0: ContentResolver, arg1: Uri) -> "Path": ...
    @staticmethod
    def createWebLinkIntent(arg0: ContentResolver, arg1: Uri, arg2: Bundle) -> IntentSender: ...

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

    class Path:
        CREATOR: ClassVar[Creator]
        def __init__(self, arg0: str, arg1: list) -> None: ...
        def getRootId(self) -> str: ...
        def getPath(self) -> list: ...
        def equals(self, arg0: Any) -> bool: ...
        def hashCode(self) -> int: ...
        def toString(self) -> str: ...
        def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
        def describeContents(self) -> int: ...

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
