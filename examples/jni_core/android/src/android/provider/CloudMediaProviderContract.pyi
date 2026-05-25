from typing import Any, ClassVar, overload

class CloudMediaProviderContract:
    EXTRA_ALBUM_ID: ClassVar[str]
    EXTRA_LOOPING_PLAYBACK_ENABLED: ClassVar[str]
    EXTRA_MEDIA_COLLECTION_ID: ClassVar[str]
    EXTRA_PAGE_SIZE: ClassVar[str]
    EXTRA_PAGE_TOKEN: ClassVar[str]
    EXTRA_PREVIEW_THUMBNAIL: ClassVar[str]
    EXTRA_SURFACE_CONTROLLER_AUDIO_MUTE_ENABLED: ClassVar[str]
    EXTRA_SYNC_GENERATION: ClassVar[str]
    MANAGE_CLOUD_MEDIA_PROVIDERS_PERMISSION: ClassVar[str]
    PROVIDER_INTERFACE: ClassVar[str]

    class MediaColumns:
        DATE_TAKEN_MILLIS: ClassVar[str]
        DURATION_MILLIS: ClassVar[str]
        HEIGHT: ClassVar[str]
        ID: ClassVar[str]
        IS_FAVORITE: ClassVar[str]
        MEDIA_STORE_URI: ClassVar[str]
        MIME_TYPE: ClassVar[str]
        ORIENTATION: ClassVar[str]
        SIZE_BYTES: ClassVar[str]
        STANDARD_MIME_TYPE_EXTENSION: ClassVar[str]
        STANDARD_MIME_TYPE_EXTENSION_ANIMATED_WEBP: ClassVar[int]
        STANDARD_MIME_TYPE_EXTENSION_GIF: ClassVar[int]
        STANDARD_MIME_TYPE_EXTENSION_MOTION_PHOTO: ClassVar[int]
        STANDARD_MIME_TYPE_EXTENSION_NONE: ClassVar[int]
        SYNC_GENERATION: ClassVar[str]
        WIDTH: ClassVar[str]

    class MediaCollectionInfo:
        ACCOUNT_CONFIGURATION_INTENT: ClassVar[str]
        ACCOUNT_NAME: ClassVar[str]
        LAST_MEDIA_SYNC_GENERATION: ClassVar[str]
        MEDIA_COLLECTION_ID: ClassVar[str]

    class AlbumColumns:
        DATE_TAKEN_MILLIS: ClassVar[str]
        DISPLAY_NAME: ClassVar[str]
        ID: ClassVar[str]
        MEDIA_COUNT: ClassVar[str]
        MEDIA_COVER_ID: ClassVar[str]
