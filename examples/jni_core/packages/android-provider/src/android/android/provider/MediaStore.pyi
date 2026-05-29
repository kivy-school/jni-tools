from typing import Any, ClassVar, overload
from android.app.PendingIntent import PendingIntent
from android.content.ContentResolver import ContentResolver
from android.content.Context import Context
from android.content.res.AssetFileDescriptor import AssetFileDescriptor
from android.database.Cursor import Cursor
from android.graphics.Bitmap import Bitmap
from android.net.Uri import Uri
from android.os.Bundle import Bundle
from android.os.CancellationSignal import CancellationSignal
from android.os.ParcelFileDescriptor import ParcelFileDescriptor
from android.util.Size import Size

class MediaStore:
    ACCESS_MEDIA_OWNER_PACKAGE_NAME_PERMISSION: ClassVar[str]
    ACCESS_OEM_METADATA_PERMISSION: ClassVar[str]
    ACTION_IMAGE_CAPTURE: ClassVar[str]
    ACTION_IMAGE_CAPTURE_SECURE: ClassVar[str]
    ACTION_MOTION_PHOTO_CAPTURE: ClassVar[str]
    ACTION_MOTION_PHOTO_CAPTURE_SECURE: ClassVar[str]
    ACTION_PICK_IMAGES: ClassVar[str]
    ACTION_PICK_IMAGES_SETTINGS: ClassVar[str]
    ACTION_REVIEW: ClassVar[str]
    ACTION_REVIEW_SECURE: ClassVar[str]
    ACTION_VIDEO_CAPTURE: ClassVar[str]
    AUTHORITY: ClassVar[str]
    AUTHORITY_URI: ClassVar[Uri]
    EXTRA_ACCEPT_ORIGINAL_MEDIA_FORMAT: ClassVar[str]
    EXTRA_BRIGHTNESS: ClassVar[str]
    EXTRA_DURATION_LIMIT: ClassVar[str]
    EXTRA_FINISH_ON_COMPLETION: ClassVar[str]
    EXTRA_FULL_SCREEN: ClassVar[str]
    EXTRA_MEDIA_ALBUM: ClassVar[str]
    EXTRA_MEDIA_ARTIST: ClassVar[str]
    EXTRA_MEDIA_CAPABILITIES: ClassVar[str]
    EXTRA_MEDIA_CAPABILITIES_UID: ClassVar[str]
    EXTRA_MEDIA_FOCUS: ClassVar[str]
    EXTRA_MEDIA_GENRE: ClassVar[str]
    EXTRA_MEDIA_PLAYLIST: ClassVar[str]
    EXTRA_MEDIA_RADIO_CHANNEL: ClassVar[str]
    EXTRA_MEDIA_TITLE: ClassVar[str]
    EXTRA_OUTPUT: ClassVar[str]
    EXTRA_PICKER_PRE_SELECTION_URIS: ClassVar[str]
    EXTRA_PICK_IMAGES_ACCENT_COLOR: ClassVar[str]
    EXTRA_PICK_IMAGES_IN_ORDER: ClassVar[str]
    EXTRA_PICK_IMAGES_LAUNCH_TAB: ClassVar[str]
    EXTRA_PICK_IMAGES_MAX: ClassVar[str]
    EXTRA_SCREEN_ORIENTATION: ClassVar[str]
    EXTRA_SHOW_ACTION_ICONS: ClassVar[str]
    EXTRA_SIZE_LIMIT: ClassVar[str]
    EXTRA_VIDEO_QUALITY: ClassVar[str]
    INTENT_ACTION_MEDIA_PLAY_FROM_SEARCH: ClassVar[str]
    INTENT_ACTION_MEDIA_SEARCH: ClassVar[str]
    INTENT_ACTION_MUSIC_PLAYER: ClassVar[str]
    INTENT_ACTION_STILL_IMAGE_CAMERA: ClassVar[str]
    INTENT_ACTION_STILL_IMAGE_CAMERA_SECURE: ClassVar[str]
    INTENT_ACTION_TEXT_OPEN_FROM_SEARCH: ClassVar[str]
    INTENT_ACTION_VIDEO_CAMERA: ClassVar[str]
    INTENT_ACTION_VIDEO_PLAY_FROM_SEARCH: ClassVar[str]
    MATCH_DEFAULT: ClassVar[int]
    MATCH_EXCLUDE: ClassVar[int]
    MATCH_INCLUDE: ClassVar[int]
    MATCH_ONLY: ClassVar[int]
    MEDIA_IGNORE_FILENAME: ClassVar[str]
    MEDIA_SCANNER_VOLUME: ClassVar[str]
    META_DATA_REVIEW_GALLERY_PREWARM_SERVICE: ClassVar[str]
    META_DATA_STILL_IMAGE_CAMERA_PREWARM_SERVICE: ClassVar[str]
    PICK_IMAGES_TAB_ALBUMS: ClassVar[int]
    PICK_IMAGES_TAB_IMAGES: ClassVar[int]
    QUERY_ARG_INCLUDE_RECENTLY_UNMOUNTED_VOLUMES: ClassVar[str]
    QUERY_ARG_LATEST_SELECTION_ONLY: ClassVar[str]
    QUERY_ARG_MATCH_FAVORITE: ClassVar[str]
    QUERY_ARG_MATCH_PENDING: ClassVar[str]
    QUERY_ARG_MATCH_TRASHED: ClassVar[str]
    QUERY_ARG_MEDIA_STANDARD_SORT_ORDER: ClassVar[str]
    QUERY_ARG_RELATED_URI: ClassVar[str]
    UNKNOWN_STRING: ClassVar[str]
    VOLUME_EXTERNAL: ClassVar[str]
    VOLUME_EXTERNAL_PRIMARY: ClassVar[str]
    VOLUME_INTERNAL: ClassVar[str]
    def __init__(self) -> None: ...
    @staticmethod
    def canManageMedia(p0: Context) -> bool: ...
    @staticmethod
    def createDeleteRequest(p0: ContentResolver, p1: list) -> PendingIntent: ...
    @staticmethod
    def createFavoriteRequest(p0: ContentResolver, p1: list, p2: bool) -> PendingIntent: ...
    @staticmethod
    def createTrashRequest(p0: ContentResolver, p1: list, p2: bool) -> PendingIntent: ...
    @staticmethod
    def createWriteRequest(p0: ContentResolver, p1: list) -> PendingIntent: ...
    @staticmethod
    def getDocumentUri(p0: Context, p1: Uri) -> Uri: ...
    @staticmethod
    def getExternalVolumeNames(p0: Context) -> set: ...
    @staticmethod
    def getGeneration(p0: Context, p1: str) -> int: ...
    @staticmethod
    def getMediaScannerUri() -> Uri: ...
    @staticmethod
    def getMediaUri(p0: Context, p1: Uri) -> Uri: ...
    @staticmethod
    def getOriginalMediaFormatFileDescriptor(p0: Context, p1: ParcelFileDescriptor) -> ParcelFileDescriptor: ...
    @staticmethod
    def getPickImagesMaxLimit() -> int: ...
    @staticmethod
    def getRecentExternalVolumeNames(p0: Context) -> set: ...
    @overload
    @staticmethod
    def getRedactedUri(p0: ContentResolver, p1: Uri) -> Uri: ...
    @overload
    @staticmethod
    def getRedactedUri(p0: ContentResolver, p1: list) -> list: ...
    @staticmethod
    def getRequireOriginal(p0: Uri) -> bool: ...
    @staticmethod
    def getVolumeName(p0: Uri) -> str: ...
    @staticmethod
    def isCurrentCloudMediaProviderAuthority(p0: ContentResolver, p1: str) -> bool: ...
    @staticmethod
    def isCurrentSystemGallery(p0: ContentResolver, p1: int, p2: str) -> bool: ...
    @staticmethod
    def isSupportedCloudMediaProviderAuthority(p0: ContentResolver, p1: str) -> bool: ...
    @staticmethod
    def markIsFavoriteStatus(p0: ContentResolver, p1: list, p2: bool) -> None: ...
    @staticmethod
    def notifyCloudMediaChangedEvent(p0: ContentResolver, p1: str, p2: str) -> None: ...
    @staticmethod
    def setIncludePending(p0: Uri) -> Uri: ...
    @staticmethod
    def setRequireOriginal(p0: Uri) -> Uri: ...
    @overload
    @staticmethod
    def getVersion(p0: Context) -> str: ...
    @overload
    @staticmethod
    def getVersion(p0: Context, p1: str) -> str: ...
    @staticmethod
    def openAssetFileDescriptor(p0: ContentResolver, p1: Uri, p2: str, p3: CancellationSignal) -> AssetFileDescriptor: ...
    @staticmethod
    def openFileDescriptor(p0: ContentResolver, p1: Uri, p2: str, p3: CancellationSignal) -> ParcelFileDescriptor: ...
    @staticmethod
    def openTypedAssetFileDescriptor(p0: ContentResolver, p1: Uri, p2: str, p3: Bundle, p4: CancellationSignal) -> AssetFileDescriptor: ...

    class Video:
        DEFAULT_SORT_ORDER: ClassVar[str]
        def __init__(self) -> None: ...
        @staticmethod
        def query(p0: ContentResolver, p1: Uri, p2: Any) -> Cursor: ...

        class VideoColumns:
            BOOKMARK: ClassVar[str]
            CATEGORY: ClassVar[str]
            COLOR_RANGE: ClassVar[str]
            COLOR_STANDARD: ClassVar[str]
            COLOR_TRANSFER: ClassVar[str]
            DESCRIPTION: ClassVar[str]
            IS_PRIVATE: ClassVar[str]
            LANGUAGE: ClassVar[str]
            LATITUDE: ClassVar[str]
            LONGITUDE: ClassVar[str]
            MINI_THUMB_MAGIC: ClassVar[str]
            TAGS: ClassVar[str]
            ALBUM: ClassVar[str]
            ALBUM_ARTIST: ClassVar[str]
            ARTIST: ClassVar[str]
            AUTHOR: ClassVar[str]
            BITRATE: ClassVar[str]
            BUCKET_DISPLAY_NAME: ClassVar[str]
            BUCKET_ID: ClassVar[str]
            CAPTURE_FRAMERATE: ClassVar[str]
            CD_TRACK_NUMBER: ClassVar[str]
            COMPILATION: ClassVar[str]
            COMPOSER: ClassVar[str]
            DATA: ClassVar[str]
            DATE_ADDED: ClassVar[str]
            DATE_EXPIRES: ClassVar[str]
            DATE_MODIFIED: ClassVar[str]
            DATE_TAKEN: ClassVar[str]
            DISC_NUMBER: ClassVar[str]
            DISPLAY_NAME: ClassVar[str]
            DOCUMENT_ID: ClassVar[str]
            DURATION: ClassVar[str]
            GENERATION_ADDED: ClassVar[str]
            GENERATION_MODIFIED: ClassVar[str]
            GENRE: ClassVar[str]
            HEIGHT: ClassVar[str]
            INFERRED_DATE: ClassVar[str]
            INSTANCE_ID: ClassVar[str]
            IS_DOWNLOAD: ClassVar[str]
            IS_DRM: ClassVar[str]
            IS_FAVORITE: ClassVar[str]
            IS_PENDING: ClassVar[str]
            IS_TRASHED: ClassVar[str]
            MIME_TYPE: ClassVar[str]
            NUM_TRACKS: ClassVar[str]
            OEM_METADATA: ClassVar[str]
            ORIENTATION: ClassVar[str]
            ORIGINAL_DOCUMENT_ID: ClassVar[str]
            OWNER_PACKAGE_NAME: ClassVar[str]
            RELATIVE_PATH: ClassVar[str]
            RESOLUTION: ClassVar[str]
            SIZE: ClassVar[str]
            TITLE: ClassVar[str]
            VOLUME_NAME: ClassVar[str]
            WIDTH: ClassVar[str]
            WRITER: ClassVar[str]
            XMP: ClassVar[str]
            YEAR: ClassVar[str]
            _COUNT: ClassVar[str]
            _ID: ClassVar[str]

        class Thumbnails:
            DATA: ClassVar[str]
            DEFAULT_SORT_ORDER: ClassVar[str]
            EXTERNAL_CONTENT_URI: ClassVar[Uri]
            FULL_SCREEN_KIND: ClassVar[int]
            HEIGHT: ClassVar[str]
            INTERNAL_CONTENT_URI: ClassVar[Uri]
            KIND: ClassVar[str]
            MICRO_KIND: ClassVar[int]
            MINI_KIND: ClassVar[int]
            VIDEO_ID: ClassVar[str]
            WIDTH: ClassVar[str]
            _COUNT: ClassVar[str]
            _ID: ClassVar[str]
            def __init__(self) -> None: ...
            @staticmethod
            def getContentUri(p0: str) -> Uri: ...
            @overload
            @staticmethod
            def cancelThumbnailRequest(p0: ContentResolver, p1: int, p2: int) -> None: ...
            @overload
            @staticmethod
            def cancelThumbnailRequest(p0: ContentResolver, p1: int) -> None: ...
            @staticmethod
            def getKindSize(p0: int) -> Size: ...
            @overload
            @staticmethod
            def getThumbnail(p0: ContentResolver, p1: int, p2: int, p3: int, p4: Any) -> Bitmap: ...
            @overload
            @staticmethod
            def getThumbnail(p0: ContentResolver, p1: int, p2: int, p3: Any) -> Bitmap: ...

        class Media:
            CONTENT_TYPE: ClassVar[str]
            DEFAULT_SORT_ORDER: ClassVar[str]
            EXTERNAL_CONTENT_URI: ClassVar[Uri]
            INTERNAL_CONTENT_URI: ClassVar[Uri]
            BOOKMARK: ClassVar[str]
            CATEGORY: ClassVar[str]
            COLOR_RANGE: ClassVar[str]
            COLOR_STANDARD: ClassVar[str]
            COLOR_TRANSFER: ClassVar[str]
            DESCRIPTION: ClassVar[str]
            IS_PRIVATE: ClassVar[str]
            LANGUAGE: ClassVar[str]
            LATITUDE: ClassVar[str]
            LONGITUDE: ClassVar[str]
            MINI_THUMB_MAGIC: ClassVar[str]
            TAGS: ClassVar[str]
            ALBUM: ClassVar[str]
            ALBUM_ARTIST: ClassVar[str]
            ARTIST: ClassVar[str]
            AUTHOR: ClassVar[str]
            BITRATE: ClassVar[str]
            BUCKET_DISPLAY_NAME: ClassVar[str]
            BUCKET_ID: ClassVar[str]
            CAPTURE_FRAMERATE: ClassVar[str]
            CD_TRACK_NUMBER: ClassVar[str]
            COMPILATION: ClassVar[str]
            COMPOSER: ClassVar[str]
            DATA: ClassVar[str]
            DATE_ADDED: ClassVar[str]
            DATE_EXPIRES: ClassVar[str]
            DATE_MODIFIED: ClassVar[str]
            DATE_TAKEN: ClassVar[str]
            DISC_NUMBER: ClassVar[str]
            DISPLAY_NAME: ClassVar[str]
            DOCUMENT_ID: ClassVar[str]
            DURATION: ClassVar[str]
            GENERATION_ADDED: ClassVar[str]
            GENERATION_MODIFIED: ClassVar[str]
            GENRE: ClassVar[str]
            HEIGHT: ClassVar[str]
            INFERRED_DATE: ClassVar[str]
            INSTANCE_ID: ClassVar[str]
            IS_DOWNLOAD: ClassVar[str]
            IS_DRM: ClassVar[str]
            IS_FAVORITE: ClassVar[str]
            IS_PENDING: ClassVar[str]
            IS_TRASHED: ClassVar[str]
            MIME_TYPE: ClassVar[str]
            NUM_TRACKS: ClassVar[str]
            OEM_METADATA: ClassVar[str]
            ORIENTATION: ClassVar[str]
            ORIGINAL_DOCUMENT_ID: ClassVar[str]
            OWNER_PACKAGE_NAME: ClassVar[str]
            RELATIVE_PATH: ClassVar[str]
            RESOLUTION: ClassVar[str]
            SIZE: ClassVar[str]
            TITLE: ClassVar[str]
            VOLUME_NAME: ClassVar[str]
            WIDTH: ClassVar[str]
            WRITER: ClassVar[str]
            XMP: ClassVar[str]
            YEAR: ClassVar[str]
            _COUNT: ClassVar[str]
            _ID: ClassVar[str]
            def __init__(self) -> None: ...
            @overload
            @staticmethod
            def getContentUri(p0: str, p1: int) -> Uri: ...
            @overload
            @staticmethod
            def getContentUri(p0: str) -> Uri: ...

    class PickerMediaColumns:
        DATA: ClassVar[str]
        DATE_TAKEN: ClassVar[str]
        DISPLAY_NAME: ClassVar[str]
        DURATION_MILLIS: ClassVar[str]
        HEIGHT: ClassVar[str]
        MIME_TYPE: ClassVar[str]
        ORIENTATION: ClassVar[str]
        SIZE: ClassVar[str]
        WIDTH: ClassVar[str]

    class MediaColumns:
        ALBUM: ClassVar[str]
        ALBUM_ARTIST: ClassVar[str]
        ARTIST: ClassVar[str]
        AUTHOR: ClassVar[str]
        BITRATE: ClassVar[str]
        BUCKET_DISPLAY_NAME: ClassVar[str]
        BUCKET_ID: ClassVar[str]
        CAPTURE_FRAMERATE: ClassVar[str]
        CD_TRACK_NUMBER: ClassVar[str]
        COMPILATION: ClassVar[str]
        COMPOSER: ClassVar[str]
        DATA: ClassVar[str]
        DATE_ADDED: ClassVar[str]
        DATE_EXPIRES: ClassVar[str]
        DATE_MODIFIED: ClassVar[str]
        DATE_TAKEN: ClassVar[str]
        DISC_NUMBER: ClassVar[str]
        DISPLAY_NAME: ClassVar[str]
        DOCUMENT_ID: ClassVar[str]
        DURATION: ClassVar[str]
        GENERATION_ADDED: ClassVar[str]
        GENERATION_MODIFIED: ClassVar[str]
        GENRE: ClassVar[str]
        HEIGHT: ClassVar[str]
        INFERRED_DATE: ClassVar[str]
        INSTANCE_ID: ClassVar[str]
        IS_DOWNLOAD: ClassVar[str]
        IS_DRM: ClassVar[str]
        IS_FAVORITE: ClassVar[str]
        IS_PENDING: ClassVar[str]
        IS_TRASHED: ClassVar[str]
        MIME_TYPE: ClassVar[str]
        NUM_TRACKS: ClassVar[str]
        OEM_METADATA: ClassVar[str]
        ORIENTATION: ClassVar[str]
        ORIGINAL_DOCUMENT_ID: ClassVar[str]
        OWNER_PACKAGE_NAME: ClassVar[str]
        RELATIVE_PATH: ClassVar[str]
        RESOLUTION: ClassVar[str]
        SIZE: ClassVar[str]
        TITLE: ClassVar[str]
        VOLUME_NAME: ClassVar[str]
        WIDTH: ClassVar[str]
        WRITER: ClassVar[str]
        XMP: ClassVar[str]
        YEAR: ClassVar[str]
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]

    class Images:
        def __init__(self) -> None: ...

        class Thumbnails:
            DATA: ClassVar[str]
            DEFAULT_SORT_ORDER: ClassVar[str]
            EXTERNAL_CONTENT_URI: ClassVar[Uri]
            FULL_SCREEN_KIND: ClassVar[int]
            HEIGHT: ClassVar[str]
            IMAGE_ID: ClassVar[str]
            INTERNAL_CONTENT_URI: ClassVar[Uri]
            KIND: ClassVar[str]
            MICRO_KIND: ClassVar[int]
            MINI_KIND: ClassVar[int]
            THUMB_DATA: ClassVar[str]
            WIDTH: ClassVar[str]
            _COUNT: ClassVar[str]
            _ID: ClassVar[str]
            def __init__(self) -> None: ...
            @staticmethod
            def getContentUri(p0: str) -> Uri: ...
            @staticmethod
            def queryMiniThumbnail(p0: ContentResolver, p1: int, p2: int, p3: Any) -> Cursor: ...
            @staticmethod
            def queryMiniThumbnails(p0: ContentResolver, p1: Uri, p2: int, p3: Any) -> Cursor: ...
            @overload
            @staticmethod
            def cancelThumbnailRequest(p0: ContentResolver, p1: int) -> None: ...
            @overload
            @staticmethod
            def cancelThumbnailRequest(p0: ContentResolver, p1: int, p2: int) -> None: ...
            @staticmethod
            def getKindSize(p0: int) -> Size: ...
            @overload
            @staticmethod
            def getThumbnail(p0: ContentResolver, p1: int, p2: int, p3: int, p4: Any) -> Bitmap: ...
            @overload
            @staticmethod
            def getThumbnail(p0: ContentResolver, p1: int, p2: int, p3: Any) -> Bitmap: ...
            @staticmethod
            def query(p0: ContentResolver, p1: Uri, p2: Any) -> Cursor: ...

        class Media:
            CONTENT_TYPE: ClassVar[str]
            DEFAULT_SORT_ORDER: ClassVar[str]
            EXTERNAL_CONTENT_URI: ClassVar[Uri]
            INTERNAL_CONTENT_URI: ClassVar[Uri]
            DESCRIPTION: ClassVar[str]
            EXPOSURE_TIME: ClassVar[str]
            F_NUMBER: ClassVar[str]
            ISO: ClassVar[str]
            IS_PRIVATE: ClassVar[str]
            LATITUDE: ClassVar[str]
            LONGITUDE: ClassVar[str]
            MINI_THUMB_MAGIC: ClassVar[str]
            PICASA_ID: ClassVar[str]
            SCENE_CAPTURE_TYPE: ClassVar[str]
            ALBUM: ClassVar[str]
            ALBUM_ARTIST: ClassVar[str]
            ARTIST: ClassVar[str]
            AUTHOR: ClassVar[str]
            BITRATE: ClassVar[str]
            BUCKET_DISPLAY_NAME: ClassVar[str]
            BUCKET_ID: ClassVar[str]
            CAPTURE_FRAMERATE: ClassVar[str]
            CD_TRACK_NUMBER: ClassVar[str]
            COMPILATION: ClassVar[str]
            COMPOSER: ClassVar[str]
            DATA: ClassVar[str]
            DATE_ADDED: ClassVar[str]
            DATE_EXPIRES: ClassVar[str]
            DATE_MODIFIED: ClassVar[str]
            DATE_TAKEN: ClassVar[str]
            DISC_NUMBER: ClassVar[str]
            DISPLAY_NAME: ClassVar[str]
            DOCUMENT_ID: ClassVar[str]
            DURATION: ClassVar[str]
            GENERATION_ADDED: ClassVar[str]
            GENERATION_MODIFIED: ClassVar[str]
            GENRE: ClassVar[str]
            HEIGHT: ClassVar[str]
            INFERRED_DATE: ClassVar[str]
            INSTANCE_ID: ClassVar[str]
            IS_DOWNLOAD: ClassVar[str]
            IS_DRM: ClassVar[str]
            IS_FAVORITE: ClassVar[str]
            IS_PENDING: ClassVar[str]
            IS_TRASHED: ClassVar[str]
            MIME_TYPE: ClassVar[str]
            NUM_TRACKS: ClassVar[str]
            OEM_METADATA: ClassVar[str]
            ORIENTATION: ClassVar[str]
            ORIGINAL_DOCUMENT_ID: ClassVar[str]
            OWNER_PACKAGE_NAME: ClassVar[str]
            RELATIVE_PATH: ClassVar[str]
            RESOLUTION: ClassVar[str]
            SIZE: ClassVar[str]
            TITLE: ClassVar[str]
            VOLUME_NAME: ClassVar[str]
            WIDTH: ClassVar[str]
            WRITER: ClassVar[str]
            XMP: ClassVar[str]
            YEAR: ClassVar[str]
            _COUNT: ClassVar[str]
            _ID: ClassVar[str]
            def __init__(self) -> None: ...
            @overload
            @staticmethod
            def getContentUri(p0: str) -> Uri: ...
            @overload
            @staticmethod
            def getContentUri(p0: str, p1: int) -> Uri: ...
            @staticmethod
            def getBitmap(p0: ContentResolver, p1: Uri) -> Bitmap: ...
            @overload
            @staticmethod
            def insertImage(p0: ContentResolver, p1: Bitmap, p2: str, p3: str) -> str: ...
            @overload
            @staticmethod
            def insertImage(p0: ContentResolver, p1: str, p2: str, p3: str) -> str: ...
            @overload
            @staticmethod
            def query(p0: ContentResolver, p1: Uri, p2: Any) -> Cursor: ...
            @overload
            @staticmethod
            def query(p0: ContentResolver, p1: Uri, p2: Any, p3: str, p4: Any, p5: str) -> Cursor: ...
            @overload
            @staticmethod
            def query(p0: ContentResolver, p1: Uri, p2: Any, p3: str, p4: str) -> Cursor: ...

        class ImageColumns:
            DESCRIPTION: ClassVar[str]
            EXPOSURE_TIME: ClassVar[str]
            F_NUMBER: ClassVar[str]
            ISO: ClassVar[str]
            IS_PRIVATE: ClassVar[str]
            LATITUDE: ClassVar[str]
            LONGITUDE: ClassVar[str]
            MINI_THUMB_MAGIC: ClassVar[str]
            PICASA_ID: ClassVar[str]
            SCENE_CAPTURE_TYPE: ClassVar[str]
            ALBUM: ClassVar[str]
            ALBUM_ARTIST: ClassVar[str]
            ARTIST: ClassVar[str]
            AUTHOR: ClassVar[str]
            BITRATE: ClassVar[str]
            BUCKET_DISPLAY_NAME: ClassVar[str]
            BUCKET_ID: ClassVar[str]
            CAPTURE_FRAMERATE: ClassVar[str]
            CD_TRACK_NUMBER: ClassVar[str]
            COMPILATION: ClassVar[str]
            COMPOSER: ClassVar[str]
            DATA: ClassVar[str]
            DATE_ADDED: ClassVar[str]
            DATE_EXPIRES: ClassVar[str]
            DATE_MODIFIED: ClassVar[str]
            DATE_TAKEN: ClassVar[str]
            DISC_NUMBER: ClassVar[str]
            DISPLAY_NAME: ClassVar[str]
            DOCUMENT_ID: ClassVar[str]
            DURATION: ClassVar[str]
            GENERATION_ADDED: ClassVar[str]
            GENERATION_MODIFIED: ClassVar[str]
            GENRE: ClassVar[str]
            HEIGHT: ClassVar[str]
            INFERRED_DATE: ClassVar[str]
            INSTANCE_ID: ClassVar[str]
            IS_DOWNLOAD: ClassVar[str]
            IS_DRM: ClassVar[str]
            IS_FAVORITE: ClassVar[str]
            IS_PENDING: ClassVar[str]
            IS_TRASHED: ClassVar[str]
            MIME_TYPE: ClassVar[str]
            NUM_TRACKS: ClassVar[str]
            OEM_METADATA: ClassVar[str]
            ORIENTATION: ClassVar[str]
            ORIGINAL_DOCUMENT_ID: ClassVar[str]
            OWNER_PACKAGE_NAME: ClassVar[str]
            RELATIVE_PATH: ClassVar[str]
            RESOLUTION: ClassVar[str]
            SIZE: ClassVar[str]
            TITLE: ClassVar[str]
            VOLUME_NAME: ClassVar[str]
            WIDTH: ClassVar[str]
            WRITER: ClassVar[str]
            XMP: ClassVar[str]
            YEAR: ClassVar[str]
            _COUNT: ClassVar[str]
            _ID: ClassVar[str]

    class Files:
        def __init__(self) -> None: ...
        @overload
        @staticmethod
        def getContentUri(p0: str) -> Uri: ...
        @overload
        @staticmethod
        def getContentUri(p0: str, p1: int) -> Uri: ...

        class FileColumns:
            MEDIA_TYPE: ClassVar[str]
            MEDIA_TYPE_AUDIO: ClassVar[int]
            MEDIA_TYPE_DOCUMENT: ClassVar[int]
            MEDIA_TYPE_IMAGE: ClassVar[int]
            MEDIA_TYPE_NONE: ClassVar[int]
            MEDIA_TYPE_PLAYLIST: ClassVar[int]
            MEDIA_TYPE_SUBTITLE: ClassVar[int]
            MEDIA_TYPE_VIDEO: ClassVar[int]
            MIME_TYPE: ClassVar[str]
            PARENT: ClassVar[str]
            ALBUM: ClassVar[str]
            ALBUM_ARTIST: ClassVar[str]
            ARTIST: ClassVar[str]
            AUTHOR: ClassVar[str]
            BITRATE: ClassVar[str]
            BUCKET_DISPLAY_NAME: ClassVar[str]
            BUCKET_ID: ClassVar[str]
            CAPTURE_FRAMERATE: ClassVar[str]
            CD_TRACK_NUMBER: ClassVar[str]
            COMPILATION: ClassVar[str]
            COMPOSER: ClassVar[str]
            DATA: ClassVar[str]
            DATE_ADDED: ClassVar[str]
            DATE_EXPIRES: ClassVar[str]
            DATE_MODIFIED: ClassVar[str]
            DATE_TAKEN: ClassVar[str]
            DISC_NUMBER: ClassVar[str]
            DISPLAY_NAME: ClassVar[str]
            DOCUMENT_ID: ClassVar[str]
            DURATION: ClassVar[str]
            GENERATION_ADDED: ClassVar[str]
            GENERATION_MODIFIED: ClassVar[str]
            GENRE: ClassVar[str]
            HEIGHT: ClassVar[str]
            INFERRED_DATE: ClassVar[str]
            INSTANCE_ID: ClassVar[str]
            IS_DOWNLOAD: ClassVar[str]
            IS_DRM: ClassVar[str]
            IS_FAVORITE: ClassVar[str]
            IS_PENDING: ClassVar[str]
            IS_TRASHED: ClassVar[str]
            MIME_TYPE: ClassVar[str]
            NUM_TRACKS: ClassVar[str]
            OEM_METADATA: ClassVar[str]
            ORIENTATION: ClassVar[str]
            ORIGINAL_DOCUMENT_ID: ClassVar[str]
            OWNER_PACKAGE_NAME: ClassVar[str]
            RELATIVE_PATH: ClassVar[str]
            RESOLUTION: ClassVar[str]
            SIZE: ClassVar[str]
            TITLE: ClassVar[str]
            VOLUME_NAME: ClassVar[str]
            WIDTH: ClassVar[str]
            WRITER: ClassVar[str]
            XMP: ClassVar[str]
            YEAR: ClassVar[str]
            _COUNT: ClassVar[str]
            _ID: ClassVar[str]

    class Downloads:
        CONTENT_TYPE: ClassVar[str]
        EXTERNAL_CONTENT_URI: ClassVar[Uri]
        INTERNAL_CONTENT_URI: ClassVar[Uri]
        DOWNLOAD_URI: ClassVar[str]
        REFERER_URI: ClassVar[str]
        ALBUM: ClassVar[str]
        ALBUM_ARTIST: ClassVar[str]
        ARTIST: ClassVar[str]
        AUTHOR: ClassVar[str]
        BITRATE: ClassVar[str]
        BUCKET_DISPLAY_NAME: ClassVar[str]
        BUCKET_ID: ClassVar[str]
        CAPTURE_FRAMERATE: ClassVar[str]
        CD_TRACK_NUMBER: ClassVar[str]
        COMPILATION: ClassVar[str]
        COMPOSER: ClassVar[str]
        DATA: ClassVar[str]
        DATE_ADDED: ClassVar[str]
        DATE_EXPIRES: ClassVar[str]
        DATE_MODIFIED: ClassVar[str]
        DATE_TAKEN: ClassVar[str]
        DISC_NUMBER: ClassVar[str]
        DISPLAY_NAME: ClassVar[str]
        DOCUMENT_ID: ClassVar[str]
        DURATION: ClassVar[str]
        GENERATION_ADDED: ClassVar[str]
        GENERATION_MODIFIED: ClassVar[str]
        GENRE: ClassVar[str]
        HEIGHT: ClassVar[str]
        INFERRED_DATE: ClassVar[str]
        INSTANCE_ID: ClassVar[str]
        IS_DOWNLOAD: ClassVar[str]
        IS_DRM: ClassVar[str]
        IS_FAVORITE: ClassVar[str]
        IS_PENDING: ClassVar[str]
        IS_TRASHED: ClassVar[str]
        MIME_TYPE: ClassVar[str]
        NUM_TRACKS: ClassVar[str]
        OEM_METADATA: ClassVar[str]
        ORIENTATION: ClassVar[str]
        ORIGINAL_DOCUMENT_ID: ClassVar[str]
        OWNER_PACKAGE_NAME: ClassVar[str]
        RELATIVE_PATH: ClassVar[str]
        RESOLUTION: ClassVar[str]
        SIZE: ClassVar[str]
        TITLE: ClassVar[str]
        VOLUME_NAME: ClassVar[str]
        WIDTH: ClassVar[str]
        WRITER: ClassVar[str]
        XMP: ClassVar[str]
        YEAR: ClassVar[str]
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]
        @overload
        @staticmethod
        def getContentUri(p0: str, p1: int) -> Uri: ...
        @overload
        @staticmethod
        def getContentUri(p0: str) -> Uri: ...

    class DownloadColumns:
        DOWNLOAD_URI: ClassVar[str]
        REFERER_URI: ClassVar[str]
        ALBUM: ClassVar[str]
        ALBUM_ARTIST: ClassVar[str]
        ARTIST: ClassVar[str]
        AUTHOR: ClassVar[str]
        BITRATE: ClassVar[str]
        BUCKET_DISPLAY_NAME: ClassVar[str]
        BUCKET_ID: ClassVar[str]
        CAPTURE_FRAMERATE: ClassVar[str]
        CD_TRACK_NUMBER: ClassVar[str]
        COMPILATION: ClassVar[str]
        COMPOSER: ClassVar[str]
        DATA: ClassVar[str]
        DATE_ADDED: ClassVar[str]
        DATE_EXPIRES: ClassVar[str]
        DATE_MODIFIED: ClassVar[str]
        DATE_TAKEN: ClassVar[str]
        DISC_NUMBER: ClassVar[str]
        DISPLAY_NAME: ClassVar[str]
        DOCUMENT_ID: ClassVar[str]
        DURATION: ClassVar[str]
        GENERATION_ADDED: ClassVar[str]
        GENERATION_MODIFIED: ClassVar[str]
        GENRE: ClassVar[str]
        HEIGHT: ClassVar[str]
        INFERRED_DATE: ClassVar[str]
        INSTANCE_ID: ClassVar[str]
        IS_DOWNLOAD: ClassVar[str]
        IS_DRM: ClassVar[str]
        IS_FAVORITE: ClassVar[str]
        IS_PENDING: ClassVar[str]
        IS_TRASHED: ClassVar[str]
        MIME_TYPE: ClassVar[str]
        NUM_TRACKS: ClassVar[str]
        OEM_METADATA: ClassVar[str]
        ORIENTATION: ClassVar[str]
        ORIGINAL_DOCUMENT_ID: ClassVar[str]
        OWNER_PACKAGE_NAME: ClassVar[str]
        RELATIVE_PATH: ClassVar[str]
        RESOLUTION: ClassVar[str]
        SIZE: ClassVar[str]
        TITLE: ClassVar[str]
        VOLUME_NAME: ClassVar[str]
        WIDTH: ClassVar[str]
        WRITER: ClassVar[str]
        XMP: ClassVar[str]
        YEAR: ClassVar[str]
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]

    class Audio:
        def __init__(self) -> None: ...
        @staticmethod
        def keyFor(p0: str) -> str: ...

        class Radio:
            ENTRY_CONTENT_TYPE: ClassVar[str]

        class PlaylistsColumns:
            DATA: ClassVar[str]
            DATE_ADDED: ClassVar[str]
            DATE_MODIFIED: ClassVar[str]
            NAME: ClassVar[str]
            ALBUM: ClassVar[str]
            ALBUM_ARTIST: ClassVar[str]
            ARTIST: ClassVar[str]
            AUTHOR: ClassVar[str]
            BITRATE: ClassVar[str]
            BUCKET_DISPLAY_NAME: ClassVar[str]
            BUCKET_ID: ClassVar[str]
            CAPTURE_FRAMERATE: ClassVar[str]
            CD_TRACK_NUMBER: ClassVar[str]
            COMPILATION: ClassVar[str]
            COMPOSER: ClassVar[str]
            DATA: ClassVar[str]
            DATE_ADDED: ClassVar[str]
            DATE_EXPIRES: ClassVar[str]
            DATE_MODIFIED: ClassVar[str]
            DATE_TAKEN: ClassVar[str]
            DISC_NUMBER: ClassVar[str]
            DISPLAY_NAME: ClassVar[str]
            DOCUMENT_ID: ClassVar[str]
            DURATION: ClassVar[str]
            GENERATION_ADDED: ClassVar[str]
            GENERATION_MODIFIED: ClassVar[str]
            GENRE: ClassVar[str]
            HEIGHT: ClassVar[str]
            INFERRED_DATE: ClassVar[str]
            INSTANCE_ID: ClassVar[str]
            IS_DOWNLOAD: ClassVar[str]
            IS_DRM: ClassVar[str]
            IS_FAVORITE: ClassVar[str]
            IS_PENDING: ClassVar[str]
            IS_TRASHED: ClassVar[str]
            MIME_TYPE: ClassVar[str]
            NUM_TRACKS: ClassVar[str]
            OEM_METADATA: ClassVar[str]
            ORIENTATION: ClassVar[str]
            ORIGINAL_DOCUMENT_ID: ClassVar[str]
            OWNER_PACKAGE_NAME: ClassVar[str]
            RELATIVE_PATH: ClassVar[str]
            RESOLUTION: ClassVar[str]
            SIZE: ClassVar[str]
            TITLE: ClassVar[str]
            VOLUME_NAME: ClassVar[str]
            WIDTH: ClassVar[str]
            WRITER: ClassVar[str]
            XMP: ClassVar[str]
            YEAR: ClassVar[str]
            _COUNT: ClassVar[str]
            _ID: ClassVar[str]

        class Playlists:
            CONTENT_TYPE: ClassVar[str]
            DEFAULT_SORT_ORDER: ClassVar[str]
            ENTRY_CONTENT_TYPE: ClassVar[str]
            EXTERNAL_CONTENT_URI: ClassVar[Uri]
            INTERNAL_CONTENT_URI: ClassVar[Uri]
            _COUNT: ClassVar[str]
            _ID: ClassVar[str]
            DATA: ClassVar[str]
            DATE_ADDED: ClassVar[str]
            DATE_MODIFIED: ClassVar[str]
            NAME: ClassVar[str]
            ALBUM: ClassVar[str]
            ALBUM_ARTIST: ClassVar[str]
            ARTIST: ClassVar[str]
            AUTHOR: ClassVar[str]
            BITRATE: ClassVar[str]
            BUCKET_DISPLAY_NAME: ClassVar[str]
            BUCKET_ID: ClassVar[str]
            CAPTURE_FRAMERATE: ClassVar[str]
            CD_TRACK_NUMBER: ClassVar[str]
            COMPILATION: ClassVar[str]
            COMPOSER: ClassVar[str]
            DATA: ClassVar[str]
            DATE_ADDED: ClassVar[str]
            DATE_EXPIRES: ClassVar[str]
            DATE_MODIFIED: ClassVar[str]
            DATE_TAKEN: ClassVar[str]
            DISC_NUMBER: ClassVar[str]
            DISPLAY_NAME: ClassVar[str]
            DOCUMENT_ID: ClassVar[str]
            DURATION: ClassVar[str]
            GENERATION_ADDED: ClassVar[str]
            GENERATION_MODIFIED: ClassVar[str]
            GENRE: ClassVar[str]
            HEIGHT: ClassVar[str]
            INFERRED_DATE: ClassVar[str]
            INSTANCE_ID: ClassVar[str]
            IS_DOWNLOAD: ClassVar[str]
            IS_DRM: ClassVar[str]
            IS_FAVORITE: ClassVar[str]
            IS_PENDING: ClassVar[str]
            IS_TRASHED: ClassVar[str]
            MIME_TYPE: ClassVar[str]
            NUM_TRACKS: ClassVar[str]
            OEM_METADATA: ClassVar[str]
            ORIENTATION: ClassVar[str]
            ORIGINAL_DOCUMENT_ID: ClassVar[str]
            OWNER_PACKAGE_NAME: ClassVar[str]
            RELATIVE_PATH: ClassVar[str]
            RESOLUTION: ClassVar[str]
            SIZE: ClassVar[str]
            TITLE: ClassVar[str]
            VOLUME_NAME: ClassVar[str]
            WIDTH: ClassVar[str]
            WRITER: ClassVar[str]
            XMP: ClassVar[str]
            YEAR: ClassVar[str]
            def __init__(self) -> None: ...
            @staticmethod
            def getContentUri(p0: str) -> Uri: ...

            class Members:
                AUDIO_ID: ClassVar[str]
                CONTENT_DIRECTORY: ClassVar[str]
                DEFAULT_SORT_ORDER: ClassVar[str]
                PLAYLIST_ID: ClassVar[str]
                PLAY_ORDER: ClassVar[str]
                _ID: ClassVar[str]
                ALBUM_ID: ClassVar[str]
                ALBUM_KEY: ClassVar[str]
                ARTIST_ID: ClassVar[str]
                ARTIST_KEY: ClassVar[str]
                BITS_PER_SAMPLE: ClassVar[str]
                BOOKMARK: ClassVar[str]
                GENRE: ClassVar[str]
                GENRE_ID: ClassVar[str]
                GENRE_KEY: ClassVar[str]
                IS_ALARM: ClassVar[str]
                IS_AUDIOBOOK: ClassVar[str]
                IS_MUSIC: ClassVar[str]
                IS_NOTIFICATION: ClassVar[str]
                IS_PODCAST: ClassVar[str]
                IS_RECORDING: ClassVar[str]
                IS_RINGTONE: ClassVar[str]
                SAMPLERATE: ClassVar[str]
                TITLE_KEY: ClassVar[str]
                TITLE_RESOURCE_URI: ClassVar[str]
                TRACK: ClassVar[str]
                YEAR: ClassVar[str]
                ALBUM: ClassVar[str]
                ALBUM_ARTIST: ClassVar[str]
                ARTIST: ClassVar[str]
                AUTHOR: ClassVar[str]
                BITRATE: ClassVar[str]
                BUCKET_DISPLAY_NAME: ClassVar[str]
                BUCKET_ID: ClassVar[str]
                CAPTURE_FRAMERATE: ClassVar[str]
                CD_TRACK_NUMBER: ClassVar[str]
                COMPILATION: ClassVar[str]
                COMPOSER: ClassVar[str]
                DATA: ClassVar[str]
                DATE_ADDED: ClassVar[str]
                DATE_EXPIRES: ClassVar[str]
                DATE_MODIFIED: ClassVar[str]
                DATE_TAKEN: ClassVar[str]
                DISC_NUMBER: ClassVar[str]
                DISPLAY_NAME: ClassVar[str]
                DOCUMENT_ID: ClassVar[str]
                DURATION: ClassVar[str]
                GENERATION_ADDED: ClassVar[str]
                GENERATION_MODIFIED: ClassVar[str]
                GENRE: ClassVar[str]
                HEIGHT: ClassVar[str]
                INFERRED_DATE: ClassVar[str]
                INSTANCE_ID: ClassVar[str]
                IS_DOWNLOAD: ClassVar[str]
                IS_DRM: ClassVar[str]
                IS_FAVORITE: ClassVar[str]
                IS_PENDING: ClassVar[str]
                IS_TRASHED: ClassVar[str]
                MIME_TYPE: ClassVar[str]
                NUM_TRACKS: ClassVar[str]
                OEM_METADATA: ClassVar[str]
                ORIENTATION: ClassVar[str]
                ORIGINAL_DOCUMENT_ID: ClassVar[str]
                OWNER_PACKAGE_NAME: ClassVar[str]
                RELATIVE_PATH: ClassVar[str]
                RESOLUTION: ClassVar[str]
                SIZE: ClassVar[str]
                TITLE: ClassVar[str]
                VOLUME_NAME: ClassVar[str]
                WIDTH: ClassVar[str]
                WRITER: ClassVar[str]
                XMP: ClassVar[str]
                YEAR: ClassVar[str]
                _COUNT: ClassVar[str]
                _ID: ClassVar[str]
                def __init__(self) -> None: ...
                @staticmethod
                def getContentUri(p0: str, p1: int) -> Uri: ...
                @staticmethod
                def moveItem(p0: ContentResolver, p1: int, p2: int, p3: int) -> bool: ...

        class Media:
            CONTENT_TYPE: ClassVar[str]
            DEFAULT_SORT_ORDER: ClassVar[str]
            ENTRY_CONTENT_TYPE: ClassVar[str]
            EXTERNAL_CONTENT_URI: ClassVar[Uri]
            EXTRA_MAX_BYTES: ClassVar[str]
            INTERNAL_CONTENT_URI: ClassVar[Uri]
            RECORD_SOUND_ACTION: ClassVar[str]
            ALBUM_ID: ClassVar[str]
            ALBUM_KEY: ClassVar[str]
            ARTIST_ID: ClassVar[str]
            ARTIST_KEY: ClassVar[str]
            BITS_PER_SAMPLE: ClassVar[str]
            BOOKMARK: ClassVar[str]
            GENRE: ClassVar[str]
            GENRE_ID: ClassVar[str]
            GENRE_KEY: ClassVar[str]
            IS_ALARM: ClassVar[str]
            IS_AUDIOBOOK: ClassVar[str]
            IS_MUSIC: ClassVar[str]
            IS_NOTIFICATION: ClassVar[str]
            IS_PODCAST: ClassVar[str]
            IS_RECORDING: ClassVar[str]
            IS_RINGTONE: ClassVar[str]
            SAMPLERATE: ClassVar[str]
            TITLE_KEY: ClassVar[str]
            TITLE_RESOURCE_URI: ClassVar[str]
            TRACK: ClassVar[str]
            YEAR: ClassVar[str]
            ALBUM: ClassVar[str]
            ALBUM_ARTIST: ClassVar[str]
            ARTIST: ClassVar[str]
            AUTHOR: ClassVar[str]
            BITRATE: ClassVar[str]
            BUCKET_DISPLAY_NAME: ClassVar[str]
            BUCKET_ID: ClassVar[str]
            CAPTURE_FRAMERATE: ClassVar[str]
            CD_TRACK_NUMBER: ClassVar[str]
            COMPILATION: ClassVar[str]
            COMPOSER: ClassVar[str]
            DATA: ClassVar[str]
            DATE_ADDED: ClassVar[str]
            DATE_EXPIRES: ClassVar[str]
            DATE_MODIFIED: ClassVar[str]
            DATE_TAKEN: ClassVar[str]
            DISC_NUMBER: ClassVar[str]
            DISPLAY_NAME: ClassVar[str]
            DOCUMENT_ID: ClassVar[str]
            DURATION: ClassVar[str]
            GENERATION_ADDED: ClassVar[str]
            GENERATION_MODIFIED: ClassVar[str]
            GENRE: ClassVar[str]
            HEIGHT: ClassVar[str]
            INFERRED_DATE: ClassVar[str]
            INSTANCE_ID: ClassVar[str]
            IS_DOWNLOAD: ClassVar[str]
            IS_DRM: ClassVar[str]
            IS_FAVORITE: ClassVar[str]
            IS_PENDING: ClassVar[str]
            IS_TRASHED: ClassVar[str]
            MIME_TYPE: ClassVar[str]
            NUM_TRACKS: ClassVar[str]
            OEM_METADATA: ClassVar[str]
            ORIENTATION: ClassVar[str]
            ORIGINAL_DOCUMENT_ID: ClassVar[str]
            OWNER_PACKAGE_NAME: ClassVar[str]
            RELATIVE_PATH: ClassVar[str]
            RESOLUTION: ClassVar[str]
            SIZE: ClassVar[str]
            TITLE: ClassVar[str]
            VOLUME_NAME: ClassVar[str]
            WIDTH: ClassVar[str]
            WRITER: ClassVar[str]
            XMP: ClassVar[str]
            YEAR: ClassVar[str]
            _COUNT: ClassVar[str]
            _ID: ClassVar[str]
            def __init__(self) -> None: ...
            @overload
            @staticmethod
            def getContentUri(p0: str, p1: int) -> Uri: ...
            @overload
            @staticmethod
            def getContentUri(p0: str) -> Uri: ...
            @staticmethod
            def getContentUriForPath(p0: str) -> Uri: ...

        class GenresColumns:
            NAME: ClassVar[str]

        class Genres:
            CONTENT_TYPE: ClassVar[str]
            DEFAULT_SORT_ORDER: ClassVar[str]
            ENTRY_CONTENT_TYPE: ClassVar[str]
            EXTERNAL_CONTENT_URI: ClassVar[Uri]
            INTERNAL_CONTENT_URI: ClassVar[Uri]
            _COUNT: ClassVar[str]
            _ID: ClassVar[str]
            NAME: ClassVar[str]
            def __init__(self) -> None: ...
            @staticmethod
            def getContentUri(p0: str) -> Uri: ...
            @staticmethod
            def getContentUriForAudioId(p0: str, p1: int) -> Uri: ...

            class Members:
                AUDIO_ID: ClassVar[str]
                CONTENT_DIRECTORY: ClassVar[str]
                DEFAULT_SORT_ORDER: ClassVar[str]
                GENRE_ID: ClassVar[str]
                ALBUM_ID: ClassVar[str]
                ALBUM_KEY: ClassVar[str]
                ARTIST_ID: ClassVar[str]
                ARTIST_KEY: ClassVar[str]
                BITS_PER_SAMPLE: ClassVar[str]
                BOOKMARK: ClassVar[str]
                GENRE: ClassVar[str]
                GENRE_ID: ClassVar[str]
                GENRE_KEY: ClassVar[str]
                IS_ALARM: ClassVar[str]
                IS_AUDIOBOOK: ClassVar[str]
                IS_MUSIC: ClassVar[str]
                IS_NOTIFICATION: ClassVar[str]
                IS_PODCAST: ClassVar[str]
                IS_RECORDING: ClassVar[str]
                IS_RINGTONE: ClassVar[str]
                SAMPLERATE: ClassVar[str]
                TITLE_KEY: ClassVar[str]
                TITLE_RESOURCE_URI: ClassVar[str]
                TRACK: ClassVar[str]
                YEAR: ClassVar[str]
                ALBUM: ClassVar[str]
                ALBUM_ARTIST: ClassVar[str]
                ARTIST: ClassVar[str]
                AUTHOR: ClassVar[str]
                BITRATE: ClassVar[str]
                BUCKET_DISPLAY_NAME: ClassVar[str]
                BUCKET_ID: ClassVar[str]
                CAPTURE_FRAMERATE: ClassVar[str]
                CD_TRACK_NUMBER: ClassVar[str]
                COMPILATION: ClassVar[str]
                COMPOSER: ClassVar[str]
                DATA: ClassVar[str]
                DATE_ADDED: ClassVar[str]
                DATE_EXPIRES: ClassVar[str]
                DATE_MODIFIED: ClassVar[str]
                DATE_TAKEN: ClassVar[str]
                DISC_NUMBER: ClassVar[str]
                DISPLAY_NAME: ClassVar[str]
                DOCUMENT_ID: ClassVar[str]
                DURATION: ClassVar[str]
                GENERATION_ADDED: ClassVar[str]
                GENERATION_MODIFIED: ClassVar[str]
                GENRE: ClassVar[str]
                HEIGHT: ClassVar[str]
                INFERRED_DATE: ClassVar[str]
                INSTANCE_ID: ClassVar[str]
                IS_DOWNLOAD: ClassVar[str]
                IS_DRM: ClassVar[str]
                IS_FAVORITE: ClassVar[str]
                IS_PENDING: ClassVar[str]
                IS_TRASHED: ClassVar[str]
                MIME_TYPE: ClassVar[str]
                NUM_TRACKS: ClassVar[str]
                OEM_METADATA: ClassVar[str]
                ORIENTATION: ClassVar[str]
                ORIGINAL_DOCUMENT_ID: ClassVar[str]
                OWNER_PACKAGE_NAME: ClassVar[str]
                RELATIVE_PATH: ClassVar[str]
                RESOLUTION: ClassVar[str]
                SIZE: ClassVar[str]
                TITLE: ClassVar[str]
                VOLUME_NAME: ClassVar[str]
                WIDTH: ClassVar[str]
                WRITER: ClassVar[str]
                XMP: ClassVar[str]
                YEAR: ClassVar[str]
                _COUNT: ClassVar[str]
                _ID: ClassVar[str]
                def __init__(self) -> None: ...
                @staticmethod
                def getContentUri(p0: str, p1: int) -> Uri: ...

        class AudioColumns:
            ALBUM_ID: ClassVar[str]
            ALBUM_KEY: ClassVar[str]
            ARTIST_ID: ClassVar[str]
            ARTIST_KEY: ClassVar[str]
            BITS_PER_SAMPLE: ClassVar[str]
            BOOKMARK: ClassVar[str]
            GENRE: ClassVar[str]
            GENRE_ID: ClassVar[str]
            GENRE_KEY: ClassVar[str]
            IS_ALARM: ClassVar[str]
            IS_AUDIOBOOK: ClassVar[str]
            IS_MUSIC: ClassVar[str]
            IS_NOTIFICATION: ClassVar[str]
            IS_PODCAST: ClassVar[str]
            IS_RECORDING: ClassVar[str]
            IS_RINGTONE: ClassVar[str]
            SAMPLERATE: ClassVar[str]
            TITLE_KEY: ClassVar[str]
            TITLE_RESOURCE_URI: ClassVar[str]
            TRACK: ClassVar[str]
            YEAR: ClassVar[str]
            ALBUM: ClassVar[str]
            ALBUM_ARTIST: ClassVar[str]
            ARTIST: ClassVar[str]
            AUTHOR: ClassVar[str]
            BITRATE: ClassVar[str]
            BUCKET_DISPLAY_NAME: ClassVar[str]
            BUCKET_ID: ClassVar[str]
            CAPTURE_FRAMERATE: ClassVar[str]
            CD_TRACK_NUMBER: ClassVar[str]
            COMPILATION: ClassVar[str]
            COMPOSER: ClassVar[str]
            DATA: ClassVar[str]
            DATE_ADDED: ClassVar[str]
            DATE_EXPIRES: ClassVar[str]
            DATE_MODIFIED: ClassVar[str]
            DATE_TAKEN: ClassVar[str]
            DISC_NUMBER: ClassVar[str]
            DISPLAY_NAME: ClassVar[str]
            DOCUMENT_ID: ClassVar[str]
            DURATION: ClassVar[str]
            GENERATION_ADDED: ClassVar[str]
            GENERATION_MODIFIED: ClassVar[str]
            GENRE: ClassVar[str]
            HEIGHT: ClassVar[str]
            INFERRED_DATE: ClassVar[str]
            INSTANCE_ID: ClassVar[str]
            IS_DOWNLOAD: ClassVar[str]
            IS_DRM: ClassVar[str]
            IS_FAVORITE: ClassVar[str]
            IS_PENDING: ClassVar[str]
            IS_TRASHED: ClassVar[str]
            MIME_TYPE: ClassVar[str]
            NUM_TRACKS: ClassVar[str]
            OEM_METADATA: ClassVar[str]
            ORIENTATION: ClassVar[str]
            ORIGINAL_DOCUMENT_ID: ClassVar[str]
            OWNER_PACKAGE_NAME: ClassVar[str]
            RELATIVE_PATH: ClassVar[str]
            RESOLUTION: ClassVar[str]
            SIZE: ClassVar[str]
            TITLE: ClassVar[str]
            VOLUME_NAME: ClassVar[str]
            WIDTH: ClassVar[str]
            WRITER: ClassVar[str]
            XMP: ClassVar[str]
            YEAR: ClassVar[str]
            _COUNT: ClassVar[str]
            _ID: ClassVar[str]

        class Artists:
            CONTENT_TYPE: ClassVar[str]
            DEFAULT_SORT_ORDER: ClassVar[str]
            ENTRY_CONTENT_TYPE: ClassVar[str]
            EXTERNAL_CONTENT_URI: ClassVar[Uri]
            INTERNAL_CONTENT_URI: ClassVar[Uri]
            _COUNT: ClassVar[str]
            _ID: ClassVar[str]
            ARTIST: ClassVar[str]
            ARTIST_KEY: ClassVar[str]
            NUMBER_OF_ALBUMS: ClassVar[str]
            NUMBER_OF_TRACKS: ClassVar[str]
            def __init__(self) -> None: ...
            @staticmethod
            def getContentUri(p0: str) -> Uri: ...

            class Albums:
                _COUNT: ClassVar[str]
                _ID: ClassVar[str]
                ALBUM: ClassVar[str]
                ALBUM_ART: ClassVar[str]
                ALBUM_ID: ClassVar[str]
                ALBUM_KEY: ClassVar[str]
                ARTIST: ClassVar[str]
                ARTIST_ID: ClassVar[str]
                ARTIST_KEY: ClassVar[str]
                FIRST_YEAR: ClassVar[str]
                LAST_YEAR: ClassVar[str]
                NUMBER_OF_SONGS: ClassVar[str]
                NUMBER_OF_SONGS_FOR_ARTIST: ClassVar[str]
                def __init__(self) -> None: ...
                @staticmethod
                def getContentUri(p0: str, p1: int) -> Uri: ...

        class ArtistColumns:
            ARTIST: ClassVar[str]
            ARTIST_KEY: ClassVar[str]
            NUMBER_OF_ALBUMS: ClassVar[str]
            NUMBER_OF_TRACKS: ClassVar[str]

        class Albums:
            CONTENT_TYPE: ClassVar[str]
            DEFAULT_SORT_ORDER: ClassVar[str]
            ENTRY_CONTENT_TYPE: ClassVar[str]
            EXTERNAL_CONTENT_URI: ClassVar[Uri]
            INTERNAL_CONTENT_URI: ClassVar[Uri]
            _COUNT: ClassVar[str]
            _ID: ClassVar[str]
            ALBUM: ClassVar[str]
            ALBUM_ART: ClassVar[str]
            ALBUM_ID: ClassVar[str]
            ALBUM_KEY: ClassVar[str]
            ARTIST: ClassVar[str]
            ARTIST_ID: ClassVar[str]
            ARTIST_KEY: ClassVar[str]
            FIRST_YEAR: ClassVar[str]
            LAST_YEAR: ClassVar[str]
            NUMBER_OF_SONGS: ClassVar[str]
            NUMBER_OF_SONGS_FOR_ARTIST: ClassVar[str]
            def __init__(self) -> None: ...
            @staticmethod
            def getContentUri(p0: str) -> Uri: ...

        class AlbumColumns:
            ALBUM: ClassVar[str]
            ALBUM_ART: ClassVar[str]
            ALBUM_ID: ClassVar[str]
            ALBUM_KEY: ClassVar[str]
            ARTIST: ClassVar[str]
            ARTIST_ID: ClassVar[str]
            ARTIST_KEY: ClassVar[str]
            FIRST_YEAR: ClassVar[str]
            LAST_YEAR: ClassVar[str]
            NUMBER_OF_SONGS: ClassVar[str]
            NUMBER_OF_SONGS_FOR_ARTIST: ClassVar[str]
