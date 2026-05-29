from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class CloudMediaProviderContract:
    EXTRA_ALBUM_ID: ClassVar[str]
    EXTRA_LOOPING_PLAYBACK_ENABLED: ClassVar[str]
    EXTRA_MEDIA_COLLECTION_ID: ClassVar[str]
    EXTRA_PAGE_SIZE: ClassVar[str]
    EXTRA_PAGE_TOKEN: ClassVar[str]
    EXTRA_PREVIEW_THUMBNAIL: ClassVar[str]
    EXTRA_SORT_ORDER: ClassVar[str]
    EXTRA_SURFACE_CONTROLLER_AUDIO_MUTE_ENABLED: ClassVar[str]
    EXTRA_SYNC_GENERATION: ClassVar[str]
    MANAGE_CLOUD_MEDIA_PROVIDERS_PERMISSION: ClassVar[str]
    MEDIA_CATEGORY_TYPE_PEOPLE_AND_PETS: ClassVar[str]
    PROVIDER_INTERFACE: ClassVar[str]
    SEARCH_SUGGESTION_ALBUM: ClassVar[str]
    SEARCH_SUGGESTION_DATE: ClassVar[str]
    SEARCH_SUGGESTION_FACE: ClassVar[str]
    SEARCH_SUGGESTION_LOCATION: ClassVar[str]
    SEARCH_SUGGESTION_TEXT: ClassVar[str]
    SORT_ORDER_DESC_DATE_TAKEN: ClassVar[int]

    class SearchSuggestionColumns:
        DISPLAY_TEXT: ClassVar[str]
        MEDIA_COVER_ID: ClassVar[str]
        MEDIA_SET_ID: ClassVar[str]
        TYPE: ClassVar[str]

    class MediaSetColumns:
        DISPLAY_NAME: ClassVar[str]
        ID: ClassVar[str]
        MEDIA_COUNT: ClassVar[str]
        MEDIA_COVER_ID: ClassVar[str]

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

    class MediaCategoryColumns:
        DISPLAY_NAME: ClassVar[str]
        ID: ClassVar[str]
        MEDIA_CATEGORY_TYPE: ClassVar[str]
        MEDIA_COVER_ID1: ClassVar[str]
        MEDIA_COVER_ID2: ClassVar[str]
        MEDIA_COVER_ID3: ClassVar[str]
        MEDIA_COVER_ID4: ClassVar[str]

    class Capabilities:
        CREATOR: ClassVar[Any]
        CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
        PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
        def isMediaCategoriesEnabled(self) -> bool: ...
        def isSearchEnabled(self) -> bool: ...
        def toString(self) -> str: ...
        def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
        def describeContents(self) -> int: ...

        class Builder:
            def __init__(self) -> None: ...
            def setMediaCategoriesEnabled(self, p0: bool) -> Any: ...
            def setSearchEnabled(self, p0: bool) -> Any: ...
            def build(self) -> Any: ...

    class AlbumColumns:
        DATE_TAKEN_MILLIS: ClassVar[str]
        DISPLAY_NAME: ClassVar[str]
        ID: ClassVar[str]
        MEDIA_COUNT: ClassVar[str]
        MEDIA_COVER_ID: ClassVar[str]
