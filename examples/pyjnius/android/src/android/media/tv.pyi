from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class CommandRequest:
    ARGUMENT_TYPE_JSON: ClassVar[str]
    ARGUMENT_TYPE_XML: ClassVar[str]
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CREATOR: ClassVar[Any]
    REQUEST_OPTION_AUTO_UPDATE: ClassVar[int]
    REQUEST_OPTION_ONESHOT: ClassVar[int]
    REQUEST_OPTION_ONEWAY: ClassVar[int]
    REQUEST_OPTION_REPEAT: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: str, p3: str, p4: str, p5: str) -> None: ...
    def getArguments(self) -> str: ...
    def getArgumentType(self) -> str: ...
    def getName(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getNamespace(self) -> str: ...

from typing import Any, ClassVar, overload
from android.net.Uri import Uri
from android.os.Parcel import Parcel

class DsmccRequest:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CREATOR: ClassVar[Any]
    REQUEST_OPTION_AUTO_UPDATE: ClassVar[int]
    REQUEST_OPTION_ONESHOT: ClassVar[int]
    REQUEST_OPTION_ONEWAY: ClassVar[int]
    REQUEST_OPTION_REPEAT: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: Uri) -> None: ...
    def getUri(self) -> Uri: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.os.ParcelFileDescriptor import ParcelFileDescriptor

class DsmccResponse:
    BIOP_MESSAGE_TYPE_DIRECTORY: ClassVar[str]
    BIOP_MESSAGE_TYPE_FILE: ClassVar[str]
    BIOP_MESSAGE_TYPE_SERVICE_GATEWAY: ClassVar[str]
    BIOP_MESSAGE_TYPE_STREAM: ClassVar[str]
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CREATOR: ClassVar[Any]
    RESPONSE_RESULT_CANCEL: ClassVar[int]
    RESPONSE_RESULT_ERROR: ClassVar[int]
    RESPONSE_RESULT_OK: ClassVar[int]
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: ParcelFileDescriptor) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: bool, p4: list) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: Any, p4: Any) -> None: ...
    def getBiopMessageType(self) -> str: ...
    def getChildList(self) -> list: ...
    def getStreamEventIds(self) -> Any: ...
    def getStreamEventNames(self) -> Any: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getFile(self) -> ParcelFileDescriptor: ...

from typing import Any, ClassVar, overload

class TvContentRating:
    UNRATED: ClassVar["TvContentRating"]
    def getDomain(self) -> str: ...
    def equals(self, p0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def contains(self, p0: "TvContentRating") -> bool: ...
    @staticmethod
    def createRating(p0: str, p1: str, p2: str, p3: Any) -> "TvContentRating": ...
    def getMainRating(self) -> str: ...
    def getRatingSystem(self) -> str: ...
    def getSubRatings(self) -> list: ...
    def flattenToString(self) -> str: ...
    @staticmethod
    def unflattenFromString(p0: str) -> "TvContentRating": ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class PesResponse:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CREATOR: ClassVar[Any]
    RESPONSE_RESULT_CANCEL: ClassVar[int]
    RESPONSE_RESULT_ERROR: ClassVar[int]
    RESPONSE_RESULT_OK: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: int, p3: str) -> None: ...
    def getSharedFilterToken(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class TableRequest:
    CREATOR: ClassVar[Any]
    TABLE_NAME_BAT: ClassVar[int]
    TABLE_NAME_CAT: ClassVar[int]
    TABLE_NAME_EIT: ClassVar[int]
    TABLE_NAME_NIT: ClassVar[int]
    TABLE_NAME_PAT: ClassVar[int]
    TABLE_NAME_PMT: ClassVar[int]
    TABLE_NAME_SDT: ClassVar[int]
    TABLE_NAME_SIT: ClassVar[int]
    TABLE_NAME_TDT: ClassVar[int]
    TABLE_NAME_TOT: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CREATOR: ClassVar[Any]
    REQUEST_OPTION_AUTO_UPDATE: ClassVar[int]
    REQUEST_OPTION_ONESHOT: ClassVar[int]
    REQUEST_OPTION_ONEWAY: ClassVar[int]
    REQUEST_OPTION_REPEAT: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    def getTableId(self) -> int: ...
    def getTableName(self) -> int: ...
    def getVersion(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class SectionRequest:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CREATOR: ClassVar[Any]
    REQUEST_OPTION_AUTO_UPDATE: ClassVar[int]
    REQUEST_OPTION_ONESHOT: ClassVar[int]
    REQUEST_OPTION_ONEWAY: ClassVar[int]
    REQUEST_OPTION_REPEAT: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    def getTableId(self) -> int: ...
    def getTsPid(self) -> int: ...
    def getVersion(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.content.ComponentName import ComponentName
from android.content.Context import Context
from android.net.Uri import Uri

class TvContract:
    ACTION_INITIALIZE_PROGRAMS: ClassVar[str]
    ACTION_PREVIEW_PROGRAM_ADDED_TO_WATCH_NEXT: ClassVar[str]
    ACTION_PREVIEW_PROGRAM_BROWSABLE_DISABLED: ClassVar[str]
    ACTION_REQUEST_CHANNEL_BROWSABLE: ClassVar[str]
    ACTION_WATCH_NEXT_PROGRAM_BROWSABLE_DISABLED: ClassVar[str]
    AUTHORITY: ClassVar[str]
    EXTRA_CHANNEL_ID: ClassVar[str]
    EXTRA_PREVIEW_PROGRAM_ID: ClassVar[str]
    EXTRA_WATCH_NEXT_PROGRAM_ID: ClassVar[str]
    @staticmethod
    def buildInputId(p0: ComponentName) -> str: ...
    @overload
    @staticmethod
    def buildChannelLogoUri(p0: int) -> Uri: ...
    @overload
    @staticmethod
    def buildChannelLogoUri(p0: Uri) -> Uri: ...
    @staticmethod
    def buildChannelUri(p0: int) -> Uri: ...
    @staticmethod
    def buildChannelUriForPassthroughInput(p0: str) -> Uri: ...
    @staticmethod
    def buildChannelsUriForInput(p0: str) -> Uri: ...
    @staticmethod
    def buildPreviewProgramUri(p0: int) -> Uri: ...
    @overload
    @staticmethod
    def buildPreviewProgramsUriForChannel(p0: int) -> Uri: ...
    @overload
    @staticmethod
    def buildPreviewProgramsUriForChannel(p0: Uri) -> Uri: ...
    @staticmethod
    def buildProgramUri(p0: int) -> Uri: ...
    @overload
    @staticmethod
    def buildProgramsUriForChannel(p0: Uri, p1: int, p2: int) -> Uri: ...
    @overload
    @staticmethod
    def buildProgramsUriForChannel(p0: int) -> Uri: ...
    @overload
    @staticmethod
    def buildProgramsUriForChannel(p0: int, p1: int, p2: int) -> Uri: ...
    @overload
    @staticmethod
    def buildProgramsUriForChannel(p0: Uri) -> Uri: ...
    @staticmethod
    def buildRecordedProgramUri(p0: int) -> Uri: ...
    @staticmethod
    def buildWatchNextProgramUri(p0: int) -> Uri: ...
    @staticmethod
    def isChannelUri(p0: Uri) -> bool: ...
    @staticmethod
    def isChannelUriForPassthroughInput(p0: Uri) -> bool: ...
    @staticmethod
    def isChannelUriForTunerInput(p0: Uri) -> bool: ...
    @staticmethod
    def isProgramUri(p0: Uri) -> bool: ...
    @staticmethod
    def isRecordedProgramUri(p0: Uri) -> bool: ...
    @staticmethod
    def requestChannelBrowsable(p0: Context, p1: int) -> None: ...

    class WatchNextPrograms:
        ASPECT_RATIO_16_9: ClassVar[int]
        ASPECT_RATIO_1_1: ClassVar[int]
        ASPECT_RATIO_2_3: ClassVar[int]
        ASPECT_RATIO_3_2: ClassVar[int]
        ASPECT_RATIO_4_3: ClassVar[int]
        AVAILABILITY_AVAILABLE: ClassVar[int]
        AVAILABILITY_FREE_WITH_SUBSCRIPTION: ClassVar[int]
        AVAILABILITY_PAID_CONTENT: ClassVar[int]
        COLUMN_AUDIO_LANGUAGE: ClassVar[str]
        COLUMN_AUTHOR: ClassVar[str]
        COLUMN_AVAILABILITY: ClassVar[str]
        COLUMN_BROWSABLE: ClassVar[str]
        COLUMN_CANONICAL_GENRE: ClassVar[str]
        COLUMN_CONTENT_ID: ClassVar[str]
        COLUMN_CONTENT_RATING: ClassVar[str]
        COLUMN_DURATION_MILLIS: ClassVar[str]
        COLUMN_END_TIME_UTC_MILLIS: ClassVar[str]
        COLUMN_EPISODE_DISPLAY_NUMBER: ClassVar[str]
        COLUMN_EPISODE_TITLE: ClassVar[str]
        COLUMN_INTENT_URI: ClassVar[str]
        COLUMN_INTERACTION_COUNT: ClassVar[str]
        COLUMN_INTERACTION_TYPE: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_DATA: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_FLAG1: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_FLAG2: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_FLAG3: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_FLAG4: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_ID: ClassVar[str]
        COLUMN_ITEM_COUNT: ClassVar[str]
        COLUMN_LAST_ENGAGEMENT_TIME_UTC_MILLIS: ClassVar[str]
        COLUMN_LAST_PLAYBACK_POSITION_MILLIS: ClassVar[str]
        COLUMN_LIVE: ClassVar[str]
        COLUMN_LOGO_URI: ClassVar[str]
        COLUMN_LONG_DESCRIPTION: ClassVar[str]
        COLUMN_OFFER_PRICE: ClassVar[str]
        COLUMN_POSTER_ART_ASPECT_RATIO: ClassVar[str]
        COLUMN_POSTER_ART_URI: ClassVar[str]
        COLUMN_PREVIEW_VIDEO_URI: ClassVar[str]
        COLUMN_RELEASE_DATE: ClassVar[str]
        COLUMN_REVIEW_RATING: ClassVar[str]
        COLUMN_REVIEW_RATING_STYLE: ClassVar[str]
        COLUMN_SEARCHABLE: ClassVar[str]
        COLUMN_SEASON_DISPLAY_NUMBER: ClassVar[str]
        COLUMN_SEASON_TITLE: ClassVar[str]
        COLUMN_SERIES_ID: ClassVar[str]
        COLUMN_SHORT_DESCRIPTION: ClassVar[str]
        COLUMN_SPLIT_ID: ClassVar[str]
        COLUMN_STARTING_PRICE: ClassVar[str]
        COLUMN_START_TIME_UTC_MILLIS: ClassVar[str]
        COLUMN_THUMBNAIL_ASPECT_RATIO: ClassVar[str]
        COLUMN_THUMBNAIL_URI: ClassVar[str]
        COLUMN_TITLE: ClassVar[str]
        COLUMN_TRANSIENT: ClassVar[str]
        COLUMN_TYPE: ClassVar[str]
        COLUMN_VERSION_NUMBER: ClassVar[str]
        COLUMN_VIDEO_HEIGHT: ClassVar[str]
        COLUMN_VIDEO_WIDTH: ClassVar[str]
        COLUMN_WATCH_NEXT_TYPE: ClassVar[str]
        CONTENT_ITEM_TYPE: ClassVar[str]
        CONTENT_TYPE: ClassVar[str]
        CONTENT_URI: ClassVar[Uri]
        INTERACTION_TYPE_FANS: ClassVar[int]
        INTERACTION_TYPE_FOLLOWERS: ClassVar[int]
        INTERACTION_TYPE_LIKES: ClassVar[int]
        INTERACTION_TYPE_LISTENS: ClassVar[int]
        INTERACTION_TYPE_THUMBS: ClassVar[int]
        INTERACTION_TYPE_VIEWERS: ClassVar[int]
        INTERACTION_TYPE_VIEWS: ClassVar[int]
        REVIEW_RATING_STYLE_PERCENTAGE: ClassVar[int]
        REVIEW_RATING_STYLE_STARS: ClassVar[int]
        REVIEW_RATING_STYLE_THUMBS_UP_DOWN: ClassVar[int]
        TYPE_ALBUM: ClassVar[int]
        TYPE_ARTIST: ClassVar[int]
        TYPE_CHANNEL: ClassVar[int]
        TYPE_CLIP: ClassVar[int]
        TYPE_EVENT: ClassVar[int]
        TYPE_MOVIE: ClassVar[int]
        TYPE_PLAYLIST: ClassVar[int]
        TYPE_STATION: ClassVar[int]
        TYPE_TRACK: ClassVar[int]
        TYPE_TV_EPISODE: ClassVar[int]
        TYPE_TV_SEASON: ClassVar[int]
        TYPE_TV_SERIES: ClassVar[int]
        WATCH_NEXT_TYPE_CONTINUE: ClassVar[int]
        WATCH_NEXT_TYPE_NEW: ClassVar[int]
        WATCH_NEXT_TYPE_NEXT: ClassVar[int]
        WATCH_NEXT_TYPE_WATCHLIST: ClassVar[int]
        COLUMN_PACKAGE_NAME: ClassVar[str]
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]

    class RecordedPrograms:
        COLUMN_AUDIO_LANGUAGE: ClassVar[str]
        COLUMN_BROADCAST_GENRE: ClassVar[str]
        COLUMN_CANONICAL_GENRE: ClassVar[str]
        COLUMN_CHANNEL_ID: ClassVar[str]
        COLUMN_CONTENT_RATING: ClassVar[str]
        COLUMN_END_TIME_UTC_MILLIS: ClassVar[str]
        COLUMN_EPISODE_DISPLAY_NUMBER: ClassVar[str]
        COLUMN_EPISODE_TITLE: ClassVar[str]
        COLUMN_INPUT_ID: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_DATA: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_FLAG1: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_FLAG2: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_FLAG3: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_FLAG4: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_ID: ClassVar[str]
        COLUMN_LONG_DESCRIPTION: ClassVar[str]
        COLUMN_MULTI_SERIES_ID: ClassVar[str]
        COLUMN_POSTER_ART_URI: ClassVar[str]
        COLUMN_RECORDING_DATA_BYTES: ClassVar[str]
        COLUMN_RECORDING_DATA_URI: ClassVar[str]
        COLUMN_RECORDING_DURATION_MILLIS: ClassVar[str]
        COLUMN_RECORDING_EXPIRE_TIME_UTC_MILLIS: ClassVar[str]
        COLUMN_REVIEW_RATING: ClassVar[str]
        COLUMN_REVIEW_RATING_STYLE: ClassVar[str]
        COLUMN_SEARCHABLE: ClassVar[str]
        COLUMN_SEASON_DISPLAY_NUMBER: ClassVar[str]
        COLUMN_SEASON_TITLE: ClassVar[str]
        COLUMN_SERIES_ID: ClassVar[str]
        COLUMN_SHORT_DESCRIPTION: ClassVar[str]
        COLUMN_SPLIT_ID: ClassVar[str]
        COLUMN_START_TIME_UTC_MILLIS: ClassVar[str]
        COLUMN_THUMBNAIL_URI: ClassVar[str]
        COLUMN_TITLE: ClassVar[str]
        COLUMN_VERSION_NUMBER: ClassVar[str]
        COLUMN_VIDEO_HEIGHT: ClassVar[str]
        COLUMN_VIDEO_WIDTH: ClassVar[str]
        CONTENT_ITEM_TYPE: ClassVar[str]
        CONTENT_TYPE: ClassVar[str]
        CONTENT_URI: ClassVar[Uri]
        REVIEW_RATING_STYLE_PERCENTAGE: ClassVar[int]
        REVIEW_RATING_STYLE_STARS: ClassVar[int]
        REVIEW_RATING_STYLE_THUMBS_UP_DOWN: ClassVar[int]
        COLUMN_PACKAGE_NAME: ClassVar[str]
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]

    class Programs:
        COLUMN_AUDIO_LANGUAGE: ClassVar[str]
        COLUMN_BROADCAST_GENRE: ClassVar[str]
        COLUMN_CANONICAL_GENRE: ClassVar[str]
        COLUMN_CHANNEL_ID: ClassVar[str]
        COLUMN_CONTENT_RATING: ClassVar[str]
        COLUMN_END_TIME_UTC_MILLIS: ClassVar[str]
        COLUMN_EPISODE_DISPLAY_NUMBER: ClassVar[str]
        COLUMN_EPISODE_NUMBER: ClassVar[str]
        COLUMN_EPISODE_TITLE: ClassVar[str]
        COLUMN_EVENT_ID: ClassVar[str]
        COLUMN_GLOBAL_CONTENT_ID: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_DATA: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_FLAG1: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_FLAG2: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_FLAG3: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_FLAG4: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_ID: ClassVar[str]
        COLUMN_LONG_DESCRIPTION: ClassVar[str]
        COLUMN_MULTI_SERIES_ID: ClassVar[str]
        COLUMN_POSTER_ART_URI: ClassVar[str]
        COLUMN_RECORDING_PROHIBITED: ClassVar[str]
        COLUMN_REVIEW_RATING: ClassVar[str]
        COLUMN_REVIEW_RATING_STYLE: ClassVar[str]
        COLUMN_SCRAMBLED: ClassVar[str]
        COLUMN_SEARCHABLE: ClassVar[str]
        COLUMN_SEASON_DISPLAY_NUMBER: ClassVar[str]
        COLUMN_SEASON_NUMBER: ClassVar[str]
        COLUMN_SEASON_TITLE: ClassVar[str]
        COLUMN_SERIES_ID: ClassVar[str]
        COLUMN_SHORT_DESCRIPTION: ClassVar[str]
        COLUMN_SPLIT_ID: ClassVar[str]
        COLUMN_START_TIME_UTC_MILLIS: ClassVar[str]
        COLUMN_THUMBNAIL_URI: ClassVar[str]
        COLUMN_TITLE: ClassVar[str]
        COLUMN_VERSION_NUMBER: ClassVar[str]
        COLUMN_VIDEO_HEIGHT: ClassVar[str]
        COLUMN_VIDEO_WIDTH: ClassVar[str]
        CONTENT_ITEM_TYPE: ClassVar[str]
        CONTENT_TYPE: ClassVar[str]
        CONTENT_URI: ClassVar[Uri]
        REVIEW_RATING_STYLE_PERCENTAGE: ClassVar[int]
        REVIEW_RATING_STYLE_STARS: ClassVar[int]
        REVIEW_RATING_STYLE_THUMBS_UP_DOWN: ClassVar[int]
        COLUMN_PACKAGE_NAME: ClassVar[str]
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]

        class Genres:
            ANIMAL_WILDLIFE: ClassVar[str]
            ARTS: ClassVar[str]
            COMEDY: ClassVar[str]
            DRAMA: ClassVar[str]
            EDUCATION: ClassVar[str]
            ENTERTAINMENT: ClassVar[str]
            FAMILY_KIDS: ClassVar[str]
            GAMING: ClassVar[str]
            LIFE_STYLE: ClassVar[str]
            MOVIES: ClassVar[str]
            MUSIC: ClassVar[str]
            NEWS: ClassVar[str]
            PREMIER: ClassVar[str]
            SHOPPING: ClassVar[str]
            SPORTS: ClassVar[str]
            TECH_SCIENCE: ClassVar[str]
            TRAVEL: ClassVar[str]
            @staticmethod
            def isCanonical(p0: str) -> bool: ...
            @staticmethod
            def decode(p0: str) -> Any: ...
            @staticmethod
            def encode(p0: Any) -> str: ...

    class PreviewPrograms:
        ASPECT_RATIO_16_9: ClassVar[int]
        ASPECT_RATIO_1_1: ClassVar[int]
        ASPECT_RATIO_2_3: ClassVar[int]
        ASPECT_RATIO_3_2: ClassVar[int]
        ASPECT_RATIO_4_3: ClassVar[int]
        AVAILABILITY_AVAILABLE: ClassVar[int]
        AVAILABILITY_FREE_WITH_SUBSCRIPTION: ClassVar[int]
        AVAILABILITY_PAID_CONTENT: ClassVar[int]
        COLUMN_AUDIO_LANGUAGE: ClassVar[str]
        COLUMN_AUTHOR: ClassVar[str]
        COLUMN_AVAILABILITY: ClassVar[str]
        COLUMN_BROWSABLE: ClassVar[str]
        COLUMN_CANONICAL_GENRE: ClassVar[str]
        COLUMN_CHANNEL_ID: ClassVar[str]
        COLUMN_CONTENT_ID: ClassVar[str]
        COLUMN_CONTENT_RATING: ClassVar[str]
        COLUMN_DURATION_MILLIS: ClassVar[str]
        COLUMN_END_TIME_UTC_MILLIS: ClassVar[str]
        COLUMN_EPISODE_DISPLAY_NUMBER: ClassVar[str]
        COLUMN_EPISODE_TITLE: ClassVar[str]
        COLUMN_INTENT_URI: ClassVar[str]
        COLUMN_INTERACTION_COUNT: ClassVar[str]
        COLUMN_INTERACTION_TYPE: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_DATA: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_FLAG1: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_FLAG2: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_FLAG3: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_FLAG4: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_ID: ClassVar[str]
        COLUMN_ITEM_COUNT: ClassVar[str]
        COLUMN_LAST_PLAYBACK_POSITION_MILLIS: ClassVar[str]
        COLUMN_LIVE: ClassVar[str]
        COLUMN_LOGO_URI: ClassVar[str]
        COLUMN_LONG_DESCRIPTION: ClassVar[str]
        COLUMN_OFFER_PRICE: ClassVar[str]
        COLUMN_POSTER_ART_ASPECT_RATIO: ClassVar[str]
        COLUMN_POSTER_ART_URI: ClassVar[str]
        COLUMN_PREVIEW_VIDEO_URI: ClassVar[str]
        COLUMN_RELEASE_DATE: ClassVar[str]
        COLUMN_REVIEW_RATING: ClassVar[str]
        COLUMN_REVIEW_RATING_STYLE: ClassVar[str]
        COLUMN_SEARCHABLE: ClassVar[str]
        COLUMN_SEASON_DISPLAY_NUMBER: ClassVar[str]
        COLUMN_SEASON_TITLE: ClassVar[str]
        COLUMN_SERIES_ID: ClassVar[str]
        COLUMN_SHORT_DESCRIPTION: ClassVar[str]
        COLUMN_SPLIT_ID: ClassVar[str]
        COLUMN_STARTING_PRICE: ClassVar[str]
        COLUMN_START_TIME_UTC_MILLIS: ClassVar[str]
        COLUMN_THUMBNAIL_ASPECT_RATIO: ClassVar[str]
        COLUMN_THUMBNAIL_URI: ClassVar[str]
        COLUMN_TITLE: ClassVar[str]
        COLUMN_TRANSIENT: ClassVar[str]
        COLUMN_TYPE: ClassVar[str]
        COLUMN_VERSION_NUMBER: ClassVar[str]
        COLUMN_VIDEO_HEIGHT: ClassVar[str]
        COLUMN_VIDEO_WIDTH: ClassVar[str]
        COLUMN_WEIGHT: ClassVar[str]
        CONTENT_ITEM_TYPE: ClassVar[str]
        CONTENT_TYPE: ClassVar[str]
        CONTENT_URI: ClassVar[Uri]
        INTERACTION_TYPE_FANS: ClassVar[int]
        INTERACTION_TYPE_FOLLOWERS: ClassVar[int]
        INTERACTION_TYPE_LIKES: ClassVar[int]
        INTERACTION_TYPE_LISTENS: ClassVar[int]
        INTERACTION_TYPE_THUMBS: ClassVar[int]
        INTERACTION_TYPE_VIEWERS: ClassVar[int]
        INTERACTION_TYPE_VIEWS: ClassVar[int]
        REVIEW_RATING_STYLE_PERCENTAGE: ClassVar[int]
        REVIEW_RATING_STYLE_STARS: ClassVar[int]
        REVIEW_RATING_STYLE_THUMBS_UP_DOWN: ClassVar[int]
        TYPE_ALBUM: ClassVar[int]
        TYPE_ARTIST: ClassVar[int]
        TYPE_CHANNEL: ClassVar[int]
        TYPE_CLIP: ClassVar[int]
        TYPE_EVENT: ClassVar[int]
        TYPE_MOVIE: ClassVar[int]
        TYPE_PLAYLIST: ClassVar[int]
        TYPE_STATION: ClassVar[int]
        TYPE_TRACK: ClassVar[int]
        TYPE_TV_EPISODE: ClassVar[int]
        TYPE_TV_SEASON: ClassVar[int]
        TYPE_TV_SERIES: ClassVar[int]
        COLUMN_PACKAGE_NAME: ClassVar[str]
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]

    class Channels:
        BROADCAST_VISIBILITY_TYPE_INVISIBLE: ClassVar[int]
        BROADCAST_VISIBILITY_TYPE_NUMERIC_SELECTABLE_ONLY: ClassVar[int]
        BROADCAST_VISIBILITY_TYPE_VISIBLE: ClassVar[int]
        COLUMN_APP_LINK_COLOR: ClassVar[str]
        COLUMN_APP_LINK_ICON_URI: ClassVar[str]
        COLUMN_APP_LINK_INTENT_URI: ClassVar[str]
        COLUMN_APP_LINK_POSTER_ART_URI: ClassVar[str]
        COLUMN_APP_LINK_TEXT: ClassVar[str]
        COLUMN_BROADCAST_GENRE: ClassVar[str]
        COLUMN_BROADCAST_VISIBILITY_TYPE: ClassVar[str]
        COLUMN_BROWSABLE: ClassVar[str]
        COLUMN_CHANNEL_LIST_ID: ClassVar[str]
        COLUMN_DESCRIPTION: ClassVar[str]
        COLUMN_DISPLAY_NAME: ClassVar[str]
        COLUMN_DISPLAY_NUMBER: ClassVar[str]
        COLUMN_GLOBAL_CONTENT_ID: ClassVar[str]
        COLUMN_INPUT_ID: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_DATA: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_FLAG1: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_FLAG2: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_FLAG3: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_FLAG4: ClassVar[str]
        COLUMN_INTERNAL_PROVIDER_ID: ClassVar[str]
        COLUMN_LOCKED: ClassVar[str]
        COLUMN_NETWORK_AFFILIATION: ClassVar[str]
        COLUMN_ORIGINAL_NETWORK_ID: ClassVar[str]
        COLUMN_REMOTE_CONTROL_KEY_PRESET_NUMBER: ClassVar[str]
        COLUMN_SCRAMBLED: ClassVar[str]
        COLUMN_SEARCHABLE: ClassVar[str]
        COLUMN_SERVICE_ID: ClassVar[str]
        COLUMN_SERVICE_TYPE: ClassVar[str]
        COLUMN_TRANSIENT: ClassVar[str]
        COLUMN_TRANSPORT_STREAM_ID: ClassVar[str]
        COLUMN_TYPE: ClassVar[str]
        COLUMN_VERSION_NUMBER: ClassVar[str]
        COLUMN_VIDEO_FORMAT: ClassVar[str]
        COLUMN_VIDEO_RESOLUTION: ClassVar[str]
        CONTENT_ITEM_TYPE: ClassVar[str]
        CONTENT_TYPE: ClassVar[str]
        CONTENT_URI: ClassVar[Uri]
        SERVICE_TYPE_AUDIO: ClassVar[str]
        SERVICE_TYPE_AUDIO_VIDEO: ClassVar[str]
        SERVICE_TYPE_OTHER: ClassVar[str]
        TYPE_1SEG: ClassVar[str]
        TYPE_ATSC3_T: ClassVar[str]
        TYPE_ATSC_C: ClassVar[str]
        TYPE_ATSC_M_H: ClassVar[str]
        TYPE_ATSC_T: ClassVar[str]
        TYPE_CMMB: ClassVar[str]
        TYPE_DTMB: ClassVar[str]
        TYPE_DVB_C: ClassVar[str]
        TYPE_DVB_C2: ClassVar[str]
        TYPE_DVB_H: ClassVar[str]
        TYPE_DVB_S: ClassVar[str]
        TYPE_DVB_S2: ClassVar[str]
        TYPE_DVB_SH: ClassVar[str]
        TYPE_DVB_T: ClassVar[str]
        TYPE_DVB_T2: ClassVar[str]
        TYPE_ISDB_C: ClassVar[str]
        TYPE_ISDB_S: ClassVar[str]
        TYPE_ISDB_S3: ClassVar[str]
        TYPE_ISDB_T: ClassVar[str]
        TYPE_ISDB_TB: ClassVar[str]
        TYPE_NTSC: ClassVar[str]
        TYPE_OTHER: ClassVar[str]
        TYPE_PAL: ClassVar[str]
        TYPE_PREVIEW: ClassVar[str]
        TYPE_SECAM: ClassVar[str]
        TYPE_S_DMB: ClassVar[str]
        TYPE_T_DMB: ClassVar[str]
        VIDEO_FORMAT_1080I: ClassVar[str]
        VIDEO_FORMAT_1080P: ClassVar[str]
        VIDEO_FORMAT_2160P: ClassVar[str]
        VIDEO_FORMAT_240P: ClassVar[str]
        VIDEO_FORMAT_360P: ClassVar[str]
        VIDEO_FORMAT_4320P: ClassVar[str]
        VIDEO_FORMAT_480I: ClassVar[str]
        VIDEO_FORMAT_480P: ClassVar[str]
        VIDEO_FORMAT_576I: ClassVar[str]
        VIDEO_FORMAT_576P: ClassVar[str]
        VIDEO_FORMAT_720P: ClassVar[str]
        VIDEO_RESOLUTION_ED: ClassVar[str]
        VIDEO_RESOLUTION_FHD: ClassVar[str]
        VIDEO_RESOLUTION_HD: ClassVar[str]
        VIDEO_RESOLUTION_SD: ClassVar[str]
        VIDEO_RESOLUTION_UHD: ClassVar[str]
        COLUMN_PACKAGE_NAME: ClassVar[str]
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]
        @staticmethod
        def getVideoResolution(p0: str) -> str: ...

        class Logo:
            CONTENT_DIRECTORY: ClassVar[str]

    class BaseTvColumns:
        COLUMN_PACKAGE_NAME: ClassVar[str]
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class CommandResponse:
    CREATOR: ClassVar[Any]
    RESPONSE_TYPE_JSON: ClassVar[str]
    RESPONSE_TYPE_XML: ClassVar[str]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CREATOR: ClassVar[Any]
    RESPONSE_RESULT_CANCEL: ClassVar[int]
    RESPONSE_RESULT_ERROR: ClassVar[int]
    RESPONSE_RESULT_OK: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: int, p3: str, p4: str) -> None: ...
    def getResponse(self) -> str: ...
    def getResponseType(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.media.tv.TvContentRating import TvContentRating
from android.media.tv.TvInputInfo import TvInputInfo
from android.os.Handler import Handler

class TvInputManager:
    ACTION_BLOCKED_RATINGS_CHANGED: ClassVar[str]
    ACTION_PARENTAL_CONTROLS_ENABLED_CHANGED: ClassVar[str]
    ACTION_QUERY_CONTENT_RATING_SYSTEMS: ClassVar[str]
    ACTION_SETUP_INPUTS: ClassVar[str]
    ACTION_VIEW_RECORDING_SCHEDULES: ClassVar[str]
    BROADCAST_INFO_STREAM_EVENT: ClassVar[int]
    BROADCAST_INFO_TYPE_COMMAND: ClassVar[int]
    BROADCAST_INFO_TYPE_DSMCC: ClassVar[int]
    BROADCAST_INFO_TYPE_PES: ClassVar[int]
    BROADCAST_INFO_TYPE_SECTION: ClassVar[int]
    BROADCAST_INFO_TYPE_TABLE: ClassVar[int]
    BROADCAST_INFO_TYPE_TIMELINE: ClassVar[int]
    BROADCAST_INFO_TYPE_TS: ClassVar[int]
    INPUT_STATE_CONNECTED: ClassVar[int]
    INPUT_STATE_CONNECTED_STANDBY: ClassVar[int]
    INPUT_STATE_DISCONNECTED: ClassVar[int]
    META_DATA_CONTENT_RATING_SYSTEMS: ClassVar[str]
    RECORDING_ERROR_INSUFFICIENT_SPACE: ClassVar[int]
    RECORDING_ERROR_RESOURCE_BUSY: ClassVar[int]
    RECORDING_ERROR_UNKNOWN: ClassVar[int]
    SESSION_DATA_KEY_AD_BUFFER: ClassVar[str]
    SESSION_DATA_KEY_AD_RESPONSE: ClassVar[str]
    SESSION_DATA_KEY_BROADCAST_INFO_RESPONSE: ClassVar[str]
    SESSION_DATA_KEY_CHANNEL_URI: ClassVar[str]
    SESSION_DATA_KEY_TRACKS: ClassVar[str]
    SESSION_DATA_KEY_TRACK_ID: ClassVar[str]
    SESSION_DATA_KEY_TRACK_TYPE: ClassVar[str]
    SESSION_DATA_KEY_TV_MESSAGE_TYPE: ClassVar[str]
    SESSION_DATA_KEY_VIDEO_UNAVAILABLE_REASON: ClassVar[str]
    SESSION_DATA_TYPE_AD_BUFFER_CONSUMED: ClassVar[str]
    SESSION_DATA_TYPE_AD_RESPONSE: ClassVar[str]
    SESSION_DATA_TYPE_BROADCAST_INFO_RESPONSE: ClassVar[str]
    SESSION_DATA_TYPE_TRACKS_CHANGED: ClassVar[str]
    SESSION_DATA_TYPE_TRACK_SELECTED: ClassVar[str]
    SESSION_DATA_TYPE_TUNED: ClassVar[str]
    SESSION_DATA_TYPE_TV_MESSAGE: ClassVar[str]
    SESSION_DATA_TYPE_VIDEO_AVAILABLE: ClassVar[str]
    SESSION_DATA_TYPE_VIDEO_UNAVAILABLE: ClassVar[str]
    SIGNAL_STRENGTH_LOST: ClassVar[int]
    SIGNAL_STRENGTH_STRONG: ClassVar[int]
    SIGNAL_STRENGTH_WEAK: ClassVar[int]
    TIME_SHIFT_INVALID_TIME: ClassVar[int]
    TIME_SHIFT_MODE_AUTO: ClassVar[int]
    TIME_SHIFT_MODE_LOCAL: ClassVar[int]
    TIME_SHIFT_MODE_NETWORK: ClassVar[int]
    TIME_SHIFT_MODE_OFF: ClassVar[int]
    TIME_SHIFT_STATUS_AVAILABLE: ClassVar[int]
    TIME_SHIFT_STATUS_UNAVAILABLE: ClassVar[int]
    TIME_SHIFT_STATUS_UNKNOWN: ClassVar[int]
    TIME_SHIFT_STATUS_UNSUPPORTED: ClassVar[int]
    TV_MESSAGE_GROUP_ID_NONE: ClassVar[int]
    TV_MESSAGE_KEY_GROUP_ID: ClassVar[str]
    TV_MESSAGE_KEY_RAW_DATA: ClassVar[str]
    TV_MESSAGE_KEY_STREAM_ID: ClassVar[str]
    TV_MESSAGE_KEY_SUBTYPE: ClassVar[str]
    TV_MESSAGE_SUBTYPE_CC_608E: ClassVar[str]
    TV_MESSAGE_SUBTYPE_WATERMARKING_A335: ClassVar[str]
    TV_MESSAGE_TYPE_CLOSED_CAPTION: ClassVar[int]
    TV_MESSAGE_TYPE_OTHER: ClassVar[int]
    TV_MESSAGE_TYPE_WATERMARK: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_AUDIO_ONLY: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_BUFFERING: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_CAS_BLACKOUT: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_CAS_CARD_INVALID: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_CAS_CARD_MUTE: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_CAS_INSUFFICIENT_OUTPUT_PROTECTION: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_CAS_LICENSE_EXPIRED: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_CAS_NEED_ACTIVATION: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_CAS_NEED_PAIRING: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_CAS_NO_CARD: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_CAS_PVR_RECORDING_NOT_ALLOWED: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_CAS_REBOOTING: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_CAS_UNKNOWN: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_INSUFFICIENT_RESOURCE: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_NOT_CONNECTED: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_STOPPED: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_TUNING: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_UNKNOWN: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_WEAK_SIGNAL: ClassVar[int]
    def registerCallback(self, p0: Any, p1: Handler) -> None: ...
    def unregisterCallback(self, p0: Any) -> None: ...
    def getBlockedRatings(self) -> list: ...
    def getInputState(self, p0: str) -> int: ...
    def getTvInputInfo(self, p0: str) -> TvInputInfo: ...
    def getTvInputList(self) -> list: ...
    def isParentalControlsEnabled(self) -> bool: ...
    def isRatingBlocked(self, p0: TvContentRating) -> bool: ...
    def updateTvInputInfo(self, p0: TvInputInfo) -> None: ...

    class TvInputCallback:
        def __init__(self) -> None: ...
        def onInputAdded(self, p0: str) -> None: ...
        def onInputRemoved(self, p0: str) -> None: ...
        def onInputStateChanged(self, p0: str, p1: int) -> None: ...
        def onInputUpdated(self, p0: str) -> None: ...
        def onTvInputInfoUpdated(self, p0: TvInputInfo) -> None: ...

from typing import Any, ClassVar, overload
from android.net.Uri import Uri
from android.os.Parcel import Parcel

class TimelineResponse:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CREATOR: ClassVar[Any]
    RESPONSE_RESULT_CANCEL: ClassVar[int]
    RESPONSE_RESULT_ERROR: ClassVar[int]
    RESPONSE_RESULT_OK: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: int, p3: str, p4: int, p5: int, p6: int, p7: int) -> None: ...
    def getTicks(self) -> int: ...
    def getUnitsPerSecond(self) -> int: ...
    def getUnitsPerTick(self) -> int: ...
    def getWallClock(self) -> int: ...
    def getSelector(self) -> Uri: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.content.AttributionSource import AttributionSource
from android.content.Context import Context
from android.content.Intent import Intent
from android.media.PlaybackParams import PlaybackParams
from android.media.tv.AdBuffer import AdBuffer
from android.media.tv.AdRequest import AdRequest
from android.media.tv.AdResponse import AdResponse
from android.media.tv.AitInfo import AitInfo
from android.media.tv.BroadcastInfoRequest import BroadcastInfoRequest
from android.media.tv.BroadcastInfoResponse import BroadcastInfoResponse
from android.media.tv.TvContentRating import TvContentRating
from android.net.Uri import Uri
from android.os.Bundle import Bundle
from android.os.IBinder import IBinder
from android.view.KeyEvent import KeyEvent
from android.view.MotionEvent import MotionEvent
from android.view.Surface import Surface
from android.view.View import View

class TvInputService:
    PRIORITY_HINT_USE_CASE_TYPE_BACKGROUND: ClassVar[int]
    PRIORITY_HINT_USE_CASE_TYPE_LIVE: ClassVar[int]
    PRIORITY_HINT_USE_CASE_TYPE_PLAYBACK: ClassVar[int]
    PRIORITY_HINT_USE_CASE_TYPE_RECORD: ClassVar[int]
    PRIORITY_HINT_USE_CASE_TYPE_SCAN: ClassVar[int]
    SERVICE_INTERFACE: ClassVar[str]
    SERVICE_META_DATA: ClassVar[str]
    START_CONTINUATION_MASK: ClassVar[int]
    START_FLAG_REDELIVERY: ClassVar[int]
    START_FLAG_RETRY: ClassVar[int]
    START_NOT_STICKY: ClassVar[int]
    START_REDELIVER_INTENT: ClassVar[int]
    START_STICKY: ClassVar[int]
    START_STICKY_COMPATIBILITY: ClassVar[int]
    STOP_FOREGROUND_DETACH: ClassVar[int]
    STOP_FOREGROUND_LEGACY: ClassVar[int]
    STOP_FOREGROUND_REMOVE: ClassVar[int]
    TRIM_MEMORY_BACKGROUND: ClassVar[int]
    TRIM_MEMORY_COMPLETE: ClassVar[int]
    TRIM_MEMORY_MODERATE: ClassVar[int]
    TRIM_MEMORY_RUNNING_CRITICAL: ClassVar[int]
    TRIM_MEMORY_RUNNING_LOW: ClassVar[int]
    TRIM_MEMORY_RUNNING_MODERATE: ClassVar[int]
    TRIM_MEMORY_UI_HIDDEN: ClassVar[int]
    ACCESSIBILITY_SERVICE: ClassVar[str]
    ACCOUNT_SERVICE: ClassVar[str]
    ACTIVITY_SERVICE: ClassVar[str]
    ADVANCED_PROTECTION_SERVICE: ClassVar[str]
    ALARM_SERVICE: ClassVar[str]
    APPWIDGET_SERVICE: ClassVar[str]
    APP_FUNCTION_SERVICE: ClassVar[str]
    APP_OPS_SERVICE: ClassVar[str]
    APP_SEARCH_SERVICE: ClassVar[str]
    AUDIO_SERVICE: ClassVar[str]
    BATTERY_SERVICE: ClassVar[str]
    BIND_ABOVE_CLIENT: ClassVar[int]
    BIND_ADJUST_WITH_ACTIVITY: ClassVar[int]
    BIND_ALLOW_ACTIVITY_STARTS: ClassVar[int]
    BIND_ALLOW_OOM_MANAGEMENT: ClassVar[int]
    BIND_AUTO_CREATE: ClassVar[int]
    BIND_DEBUG_UNBIND: ClassVar[int]
    BIND_EXTERNAL_SERVICE: ClassVar[int]
    BIND_EXTERNAL_SERVICE_LONG: ClassVar[int]
    BIND_IMPORTANT: ClassVar[int]
    BIND_INCLUDE_CAPABILITIES: ClassVar[int]
    BIND_NOT_FOREGROUND: ClassVar[int]
    BIND_NOT_PERCEPTIBLE: ClassVar[int]
    BIND_PACKAGE_ISOLATED_PROCESS: ClassVar[int]
    BIND_SHARED_ISOLATED_PROCESS: ClassVar[int]
    BIND_WAIVE_PRIORITY: ClassVar[int]
    BIOMETRIC_SERVICE: ClassVar[str]
    BLOB_STORE_SERVICE: ClassVar[str]
    BLUETOOTH_SERVICE: ClassVar[str]
    BUGREPORT_SERVICE: ClassVar[str]
    CAMERA_SERVICE: ClassVar[str]
    CAPTIONING_SERVICE: ClassVar[str]
    CARRIER_CONFIG_SERVICE: ClassVar[str]
    CLIPBOARD_SERVICE: ClassVar[str]
    COMPANION_DEVICE_SERVICE: ClassVar[str]
    CONNECTIVITY_DIAGNOSTICS_SERVICE: ClassVar[str]
    CONNECTIVITY_SERVICE: ClassVar[str]
    CONSUMER_IR_SERVICE: ClassVar[str]
    CONTACT_KEYS_SERVICE: ClassVar[str]
    CONTEXT_IGNORE_SECURITY: ClassVar[int]
    CONTEXT_INCLUDE_CODE: ClassVar[int]
    CONTEXT_RESTRICTED: ClassVar[int]
    CREDENTIAL_SERVICE: ClassVar[str]
    CROSS_PROFILE_APPS_SERVICE: ClassVar[str]
    DEVICE_ID_DEFAULT: ClassVar[int]
    DEVICE_ID_INVALID: ClassVar[int]
    DEVICE_LOCK_SERVICE: ClassVar[str]
    DEVICE_POLICY_SERVICE: ClassVar[str]
    DISPLAY_HASH_SERVICE: ClassVar[str]
    DISPLAY_SERVICE: ClassVar[str]
    DOMAIN_VERIFICATION_SERVICE: ClassVar[str]
    DOWNLOAD_SERVICE: ClassVar[str]
    DROPBOX_SERVICE: ClassVar[str]
    EUICC_SERVICE: ClassVar[str]
    FILE_INTEGRITY_SERVICE: ClassVar[str]
    FINGERPRINT_SERVICE: ClassVar[str]
    GAME_SERVICE: ClassVar[str]
    GRAMMATICAL_INFLECTION_SERVICE: ClassVar[str]
    HARDWARE_PROPERTIES_SERVICE: ClassVar[str]
    HEALTHCONNECT_SERVICE: ClassVar[str]
    INPUT_METHOD_SERVICE: ClassVar[str]
    INPUT_SERVICE: ClassVar[str]
    IPSEC_SERVICE: ClassVar[str]
    JOB_SCHEDULER_SERVICE: ClassVar[str]
    KEYGUARD_SERVICE: ClassVar[str]
    KEYSTORE_SERVICE: ClassVar[str]
    LAUNCHER_APPS_SERVICE: ClassVar[str]
    LAYOUT_INFLATER_SERVICE: ClassVar[str]
    LOCALE_SERVICE: ClassVar[str]
    LOCATION_SERVICE: ClassVar[str]
    MEDIA_COMMUNICATION_SERVICE: ClassVar[str]
    MEDIA_METRICS_SERVICE: ClassVar[str]
    MEDIA_PROJECTION_SERVICE: ClassVar[str]
    MEDIA_QUALITY_SERVICE: ClassVar[str]
    MEDIA_ROUTER_SERVICE: ClassVar[str]
    MEDIA_SESSION_SERVICE: ClassVar[str]
    MIDI_SERVICE: ClassVar[str]
    MODE_APPEND: ClassVar[int]
    MODE_ENABLE_WRITE_AHEAD_LOGGING: ClassVar[int]
    MODE_MULTI_PROCESS: ClassVar[int]
    MODE_NO_LOCALIZED_COLLATORS: ClassVar[int]
    MODE_PRIVATE: ClassVar[int]
    MODE_WORLD_READABLE: ClassVar[int]
    MODE_WORLD_WRITEABLE: ClassVar[int]
    NETWORK_STATS_SERVICE: ClassVar[str]
    NFC_SERVICE: ClassVar[str]
    NOTIFICATION_SERVICE: ClassVar[str]
    NSD_SERVICE: ClassVar[str]
    OVERLAY_SERVICE: ClassVar[str]
    PEOPLE_SERVICE: ClassVar[str]
    PERFORMANCE_HINT_SERVICE: ClassVar[str]
    PERSISTENT_DATA_BLOCK_SERVICE: ClassVar[str]
    POWER_SERVICE: ClassVar[str]
    PRINT_SERVICE: ClassVar[str]
    PROFILING_SERVICE: ClassVar[str]
    RECEIVER_EXPORTED: ClassVar[int]
    RECEIVER_NOT_EXPORTED: ClassVar[int]
    RECEIVER_VISIBLE_TO_INSTANT_APPS: ClassVar[int]
    RESTRICTIONS_SERVICE: ClassVar[str]
    ROLE_SERVICE: ClassVar[str]
    SATELLITE_SERVICE: ClassVar[str]
    SEARCH_SERVICE: ClassVar[str]
    SECURITY_STATE_SERVICE: ClassVar[str]
    SENSOR_SERVICE: ClassVar[str]
    SHORTCUT_SERVICE: ClassVar[str]
    STATUS_BAR_SERVICE: ClassVar[str]
    STORAGE_SERVICE: ClassVar[str]
    STORAGE_STATS_SERVICE: ClassVar[str]
    SYSTEM_HEALTH_SERVICE: ClassVar[str]
    TELECOM_SERVICE: ClassVar[str]
    TELEPHONY_IMS_SERVICE: ClassVar[str]
    TELEPHONY_SERVICE: ClassVar[str]
    TELEPHONY_SUBSCRIPTION_SERVICE: ClassVar[str]
    TETHERING_SERVICE: ClassVar[str]
    TEXT_CLASSIFICATION_SERVICE: ClassVar[str]
    TEXT_SERVICES_MANAGER_SERVICE: ClassVar[str]
    TV_AD_SERVICE: ClassVar[str]
    TV_INPUT_SERVICE: ClassVar[str]
    TV_INTERACTIVE_APP_SERVICE: ClassVar[str]
    UI_MODE_SERVICE: ClassVar[str]
    USAGE_STATS_SERVICE: ClassVar[str]
    USB_SERVICE: ClassVar[str]
    USER_SERVICE: ClassVar[str]
    VIBRATOR_MANAGER_SERVICE: ClassVar[str]
    VIBRATOR_SERVICE: ClassVar[str]
    VIRTUAL_DEVICE_SERVICE: ClassVar[str]
    VPN_MANAGEMENT_SERVICE: ClassVar[str]
    WALLPAPER_SERVICE: ClassVar[str]
    WIFI_AWARE_SERVICE: ClassVar[str]
    WIFI_P2P_SERVICE: ClassVar[str]
    WIFI_RTT_RANGING_SERVICE: ClassVar[str]
    WIFI_SERVICE: ClassVar[str]
    WINDOW_SERVICE: ClassVar[str]
    def __init__(self) -> None: ...
    @overload
    def onCreateSession(self, p0: str) -> Any: ...
    @overload
    def onCreateSession(self, p0: str, p1: str) -> Any: ...
    @overload
    def onCreateSession(self, p0: str, p1: str, p2: AttributionSource) -> Any: ...
    @overload
    def onCreateRecordingSession(self, p0: str, p1: str) -> Any: ...
    @overload
    def onCreateRecordingSession(self, p0: str) -> Any: ...
    def onBind(self, p0: Intent) -> IBinder: ...

    class Session:
        def __init__(self, p0: Context) -> None: ...
        def onSurfaceChanged(self, p0: int, p1: int, p2: int) -> None: ...
        def layoutSurface(self, p0: int, p1: int, p2: int, p3: int) -> None: ...
        def onSetSurface(self, p0: Surface) -> bool: ...
        def onTvMessage(self, p0: int, p1: Bundle) -> None: ...
        def onAppPrivateCommand(self, p0: str, p1: Bundle) -> None: ...
        def notifyAdBufferConsumed(self, p0: AdBuffer) -> None: ...
        def notifyAdResponse(self, p0: AdResponse) -> None: ...
        def notifyAitInfoUpdated(self, p0: AitInfo) -> None: ...
        def notifyAudioPresentationChanged(self, p0: list) -> None: ...
        def notifyAudioPresentationSelected(self, p0: int, p1: int) -> None: ...
        def notifyAvailableSpeeds(self, p0: Any) -> None: ...
        def notifyBroadcastInfoResponse(self, p0: BroadcastInfoResponse) -> None: ...
        def notifyChannelRetuned(self, p0: Uri) -> None: ...
        def notifyContentAllowed(self) -> None: ...
        def notifyContentBlocked(self, p0: TvContentRating) -> None: ...
        def notifyCueingMessageAvailability(self, p0: bool) -> None: ...
        def notifySignalStrength(self, p0: int) -> None: ...
        def notifyTimeShiftMode(self, p0: int) -> None: ...
        def notifyTrackSelected(self, p0: int, p1: str) -> None: ...
        def notifyTracksChanged(self, p0: list) -> None: ...
        def notifyTuned(self, p0: Uri) -> None: ...
        def notifyVideoAvailable(self) -> None: ...
        def notifyVideoUnavailable(self, p0: int) -> None: ...
        def onAdBufferReady(self, p0: AdBuffer) -> None: ...
        def onCreateOverlayView(self) -> View: ...
        def onOverlayViewSizeChanged(self, p0: int, p1: int) -> None: ...
        def onRemoveBroadcastInfo(self, p0: int) -> None: ...
        def onRequestAd(self, p0: AdRequest) -> None: ...
        def onRequestBroadcastInfo(self, p0: BroadcastInfoRequest) -> None: ...
        def onResumePlayback(self) -> None: ...
        def onSelectAudioPresentation(self, p0: int, p1: int) -> bool: ...
        def onSelectTrack(self, p0: int, p1: str) -> bool: ...
        def onSetCaptionEnabled(self, p0: bool) -> None: ...
        def onSetInteractiveAppNotificationEnabled(self, p0: bool) -> None: ...
        def onSetStreamVolume(self, p0: float) -> None: ...
        def onSetTvMessageEnabled(self, p0: int, p1: bool) -> None: ...
        def onStopPlayback(self, p0: int) -> None: ...
        def onTimeShiftGetCurrentPosition(self) -> int: ...
        def onTimeShiftGetStartPosition(self) -> int: ...
        def onTimeShiftPause(self) -> None: ...
        def onTimeShiftPlay(self, p0: Uri) -> None: ...
        def onTimeShiftResume(self) -> None: ...
        def onTimeShiftSeekTo(self, p0: int) -> None: ...
        def onTimeShiftSetMode(self, p0: int) -> None: ...
        def onTimeShiftSetPlaybackParams(self, p0: PlaybackParams) -> None: ...
        @overload
        def onTune(self, p0: Uri, p1: Bundle) -> bool: ...
        @overload
        def onTune(self, p0: Uri) -> bool: ...
        def onTvAdSessionData(self, p0: str, p1: Bundle) -> None: ...
        def onUnblockContent(self, p0: TvContentRating) -> None: ...
        def sendTvInputSessionData(self, p0: str, p1: Bundle) -> None: ...
        def setOverlayViewEnabled(self, p0: bool) -> None: ...
        def notifyTimeShiftStatusChanged(self, p0: int) -> None: ...
        def notifyVideoFreezeUpdated(self, p0: bool) -> None: ...
        def notifyTvMessage(self, p0: int, p1: Bundle) -> None: ...
        def onGenericMotionEvent(self, p0: MotionEvent) -> bool: ...
        def onKeyDown(self, p0: int, p1: KeyEvent) -> bool: ...
        def onKeyLongPress(self, p0: int, p1: KeyEvent) -> bool: ...
        def onKeyMultiple(self, p0: int, p1: int, p2: KeyEvent) -> bool: ...
        def onTrackballEvent(self, p0: MotionEvent) -> bool: ...
        def onKeyUp(self, p0: int, p1: KeyEvent) -> bool: ...
        def onTouchEvent(self, p0: MotionEvent) -> bool: ...
        def onRelease(self) -> None: ...

    class RecordingSession:
        def __init__(self, p0: Context) -> None: ...
        def onAppPrivateCommand(self, p0: str, p1: Bundle) -> None: ...
        def notifyTuned(self, p0: Uri) -> None: ...
        @overload
        def onTune(self, p0: Uri, p1: Bundle) -> None: ...
        @overload
        def onTune(self, p0: Uri) -> None: ...
        def onPauseRecording(self, p0: Bundle) -> None: ...
        def onResumeRecording(self, p0: Bundle) -> None: ...
        @overload
        def onStartRecording(self, p0: Uri) -> None: ...
        @overload
        def onStartRecording(self, p0: Uri, p1: Bundle) -> None: ...
        def onStopRecording(self) -> None: ...
        def notifyRecordingStopped(self, p0: Uri) -> None: ...
        def notifyError(self, p0: int) -> None: ...
        def onRelease(self) -> None: ...

    class HardwareSession:
        def __init__(self, p0: Context) -> None: ...
        def onSetSurface(self, p0: Surface) -> bool: ...
        def getHardwareInputId(self) -> str: ...
        def onHardwareVideoAvailable(self) -> None: ...
        def onHardwareVideoUnavailable(self, p0: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class SignalingDataRequest:
    CREATOR: ClassVar[Any]
    SIGNALING_DATA_NO_GROUP_ID: ClassVar[int]
    SIGNALING_METADATA_AEAT: ClassVar[str]
    SIGNALING_METADATA_AEI: ClassVar[str]
    SIGNALING_METADATA_APD: ClassVar[str]
    SIGNALING_METADATA_ASD: ClassVar[str]
    SIGNALING_METADATA_ASPD: ClassVar[str]
    SIGNALING_METADATA_CAD: ClassVar[str]
    SIGNALING_METADATA_CDT: ClassVar[str]
    SIGNALING_METADATA_CRIT: ClassVar[str]
    SIGNALING_METADATA_DCIT: ClassVar[str]
    SIGNALING_METADATA_DWD: ClassVar[str]
    SIGNALING_METADATA_EMSG: ClassVar[str]
    SIGNALING_METADATA_EVTI: ClassVar[str]
    SIGNALING_METADATA_HELD: ClassVar[str]
    SIGNALING_METADATA_IED: ClassVar[str]
    SIGNALING_METADATA_MPD: ClassVar[str]
    SIGNALING_METADATA_MPIT: ClassVar[str]
    SIGNALING_METADATA_MPT: ClassVar[str]
    SIGNALING_METADATA_OSN: ClassVar[str]
    SIGNALING_METADATA_PAT: ClassVar[str]
    SIGNALING_METADATA_RDT: ClassVar[str]
    SIGNALING_METADATA_RRT: ClassVar[str]
    SIGNALING_METADATA_RSAT: ClassVar[str]
    SIGNALING_METADATA_SLT: ClassVar[str]
    SIGNALING_METADATA_SMT: ClassVar[str]
    SIGNALING_METADATA_SSD: ClassVar[str]
    SIGNALING_METADATA_STSID: ClassVar[str]
    SIGNALING_METADATA_STT: ClassVar[str]
    SIGNALING_METADATA_USBD: ClassVar[str]
    SIGNALING_METADATA_USD: ClassVar[str]
    SIGNALING_METADATA_VSPD: ClassVar[str]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CREATOR: ClassVar[Any]
    REQUEST_OPTION_AUTO_UPDATE: ClassVar[int]
    REQUEST_OPTION_ONESHOT: ClassVar[int]
    REQUEST_OPTION_ONEWAY: ClassVar[int]
    REQUEST_OPTION_REPEAT: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: int, p3: list) -> None: ...
    def getSignalingDataTypes(self) -> list: ...
    def getGroup(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class AdResponse:
    CREATOR: ClassVar[Any]
    RESPONSE_TYPE_BUFFERING: ClassVar[int]
    RESPONSE_TYPE_ERROR: ClassVar[int]
    RESPONSE_TYPE_FINISHED: ClassVar[int]
    RESPONSE_TYPE_PLAYING: ClassVar[int]
    RESPONSE_TYPE_STOPPED: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: int) -> None: ...
    def getResponseType(self) -> int: ...
    def getElapsedTimeMillis(self) -> int: ...
    def getId(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class StreamEventResponse:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CREATOR: ClassVar[Any]
    RESPONSE_RESULT_CANCEL: ClassVar[int]
    RESPONSE_RESULT_ERROR: ClassVar[int]
    RESPONSE_RESULT_OK: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: Any) -> None: ...
    def getEventId(self) -> int: ...
    def getNptMillis(self) -> int: ...
    def getData(self) -> Any: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class BroadcastInfoResponse:
    CREATOR: ClassVar[Any]
    RESPONSE_RESULT_CANCEL: ClassVar[int]
    RESPONSE_RESULT_ERROR: ClassVar[int]
    RESPONSE_RESULT_OK: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getRequestId(self) -> int: ...
    def getSequence(self) -> int: ...
    def getResponseResult(self) -> int: ...
    def getType(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.net.Uri import Uri
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel
from android.os.ParcelFileDescriptor import ParcelFileDescriptor

class AdRequest:
    CREATOR: ClassVar[Any]
    REQUEST_TYPE_START: ClassVar[int]
    REQUEST_TYPE_STOP: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    @overload
    def __init__(self, p0: int, p1: int, p2: Uri, p3: int, p4: int, p5: int, p6: Bundle) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: ParcelFileDescriptor, p3: int, p4: int, p5: int, p6: str, p7: Bundle) -> None: ...
    def getRequestType(self) -> int: ...
    def getStartTimeMillis(self) -> int: ...
    def getEchoIntervalMillis(self) -> int: ...
    def getMediaFileType(self) -> str: ...
    def getStopTimeMillis(self) -> int: ...
    def getId(self) -> int: ...
    def getUri(self) -> Uri: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getMetadata(self) -> Bundle: ...
    def getFileDescriptor(self) -> ParcelFileDescriptor: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class TsRequest:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CREATOR: ClassVar[Any]
    REQUEST_OPTION_AUTO_UPDATE: ClassVar[int]
    REQUEST_OPTION_ONESHOT: ClassVar[int]
    REQUEST_OPTION_ONEWAY: ClassVar[int]
    REQUEST_OPTION_REPEAT: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: int) -> None: ...
    def getTsPid(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.os.SharedMemory import SharedMemory

class AdBuffer:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: int, p1: str, p2: SharedMemory, p3: int, p4: int, p5: int, p6: int) -> None: ...
    def getMimeType(self) -> str: ...
    def getPresentationTimeUs(self) -> int: ...
    def getSharedMemory(self) -> SharedMemory: ...
    def getLength(self) -> int: ...
    def getId(self) -> int: ...
    def getOffset(self) -> int: ...
    def getFlags(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel

class SectionResponse:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CREATOR: ClassVar[Any]
    RESPONSE_RESULT_CANCEL: ClassVar[int]
    RESPONSE_RESULT_ERROR: ClassVar[int]
    RESPONSE_RESULT_OK: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: Bundle) -> None: ...
    def getSessionId(self) -> int: ...
    def getSessionData(self) -> Bundle: ...
    def getVersion(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class PesRequest:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CREATOR: ClassVar[Any]
    REQUEST_OPTION_AUTO_UPDATE: ClassVar[int]
    REQUEST_OPTION_ONESHOT: ClassVar[int]
    REQUEST_OPTION_ONEWAY: ClassVar[int]
    REQUEST_OPTION_REPEAT: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: int, p3: int) -> None: ...
    def getTsPid(self) -> int: ...
    def getStreamId(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class BroadcastInfoRequest:
    CREATOR: ClassVar[Any]
    REQUEST_OPTION_AUTO_UPDATE: ClassVar[int]
    REQUEST_OPTION_ONESHOT: ClassVar[int]
    REQUEST_OPTION_ONEWAY: ClassVar[int]
    REQUEST_OPTION_REPEAT: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getRequestId(self) -> int: ...
    def getType(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getOption(self) -> int: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class SignalingDataResponse:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CREATOR: ClassVar[Any]
    RESPONSE_RESULT_CANCEL: ClassVar[int]
    RESPONSE_RESULT_ERROR: ClassVar[int]
    RESPONSE_RESULT_OK: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: int, p3: list, p4: list) -> None: ...
    def getSignalingDataInfoList(self) -> list: ...
    def getSignalingDataTypes(self) -> list: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.net.Uri import Uri
from android.os.Parcel import Parcel

class TvRecordingInfo:
    CREATOR: ClassVar[Any]
    FRIDAY: ClassVar[int]
    MONDAY: ClassVar[int]
    RECORDING_ALL: ClassVar[int]
    RECORDING_IN_PROGRESS: ClassVar[int]
    RECORDING_SCHEDULED: ClassVar[int]
    SATURDAY: ClassVar[int]
    SUNDAY: ClassVar[int]
    THURSDAY: ClassVar[int]
    TUESDAY: ClassVar[int]
    WEDNESDAY: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: str, p1: int, p2: int, p3: int, p4: str, p5: str, p6: int, p7: int, p8: Uri, p9: Uri, p10: list, p11: Uri, p12: int, p13: int) -> None: ...
    def getRecordingDurationMillis(self) -> int: ...
    def getChannelUri(self) -> Uri: ...
    def getContentRatings(self) -> list: ...
    def getEndPaddingMillis(self) -> int: ...
    def getProgramUri(self) -> Uri: ...
    def getRecordingId(self) -> str: ...
    def getRecordingStartTimeMillis(self) -> int: ...
    def getRecordingUri(self) -> Uri: ...
    def getRepeatDays(self) -> int: ...
    def getScheduledDurationMillis(self) -> int: ...
    def getScheduledStartTimeMillis(self) -> int: ...
    def getStartPaddingMillis(self) -> int: ...
    def getName(self) -> str: ...
    def setName(self, p0: str) -> None: ...
    def setDescription(self, p0: str) -> None: ...
    def getDescription(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class AitInfo:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: int, p1: int) -> None: ...
    def getVersion(self) -> int: ...
    def toString(self) -> str: ...
    def getType(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.content.ComponentName import ComponentName
from android.content.Context import Context
from android.content.Intent import Intent
from android.content.pm.ServiceInfo import ServiceInfo
from android.graphics.drawable.Drawable import Drawable
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel

class TvInputInfo:
    CREATOR: ClassVar[Any]
    EXTRA_INPUT_ID: ClassVar[str]
    TYPE_COMPONENT: ClassVar[int]
    TYPE_COMPOSITE: ClassVar[int]
    TYPE_DISPLAY_PORT: ClassVar[int]
    TYPE_DVI: ClassVar[int]
    TYPE_HDMI: ClassVar[int]
    TYPE_OTHER: ClassVar[int]
    TYPE_SCART: ClassVar[int]
    TYPE_SVIDEO: ClassVar[int]
    TYPE_TUNER: ClassVar[int]
    TYPE_VGA: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def loadIcon(self, p0: Context) -> Drawable: ...
    def loadLabel(self, p0: Context) -> str: ...
    def getServiceInfo(self) -> ServiceInfo: ...
    def canPauseRecording(self) -> bool: ...
    def canRecord(self) -> bool: ...
    def createSettingsIntent(self) -> Intent: ...
    def createSetupIntent(self) -> Intent: ...
    def getParentId(self) -> str: ...
    def getTunerCount(self) -> int: ...
    def isPassthroughInput(self) -> bool: ...
    def loadCustomLabel(self, p0: Context) -> str: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def isHidden(self, p0: Context) -> bool: ...
    def getId(self) -> str: ...
    def getType(self) -> int: ...
    def getExtras(self) -> Bundle: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class Builder:
        def __init__(self, p0: Context, p1: ComponentName) -> None: ...
        def setCanPauseRecording(self, p0: bool) -> Any: ...
        def setCanRecord(self, p0: bool) -> Any: ...
        def setTunerCount(self, p0: int) -> Any: ...
        def setExtras(self, p0: Bundle) -> Any: ...
        def build(self) -> "TvInputInfo": ...

from typing import Any, ClassVar, overload
from android.net.Uri import Uri
from android.os.Parcel import Parcel

class StreamEventRequest:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CREATOR: ClassVar[Any]
    REQUEST_OPTION_AUTO_UPDATE: ClassVar[int]
    REQUEST_OPTION_ONESHOT: ClassVar[int]
    REQUEST_OPTION_ONEWAY: ClassVar[int]
    REQUEST_OPTION_REPEAT: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: Uri, p3: str) -> None: ...
    def getEventName(self) -> str: ...
    def getTargetUri(self) -> Uri: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.media.tv.interactive.TvInteractiveAppView import TvInteractiveAppView
from android.net.Uri import Uri
from android.os.Bundle import Bundle
from android.os.Handler import Handler

class TvRecordingClient:
    def __init__(self, p0: Context, p1: str, p2: Any, p3: Handler) -> None: ...
    def sendAppPrivateCommand(self, p0: str, p1: Bundle) -> None: ...
    def setTvInteractiveAppView(self, p0: TvInteractiveAppView, p1: str) -> None: ...
    @overload
    def resumeRecording(self) -> None: ...
    @overload
    def resumeRecording(self, p0: Bundle) -> None: ...
    @overload
    def pauseRecording(self) -> None: ...
    @overload
    def pauseRecording(self, p0: Bundle) -> None: ...
    @overload
    def startRecording(self, p0: Uri, p1: Bundle) -> None: ...
    @overload
    def startRecording(self, p0: Uri) -> None: ...
    def stopRecording(self) -> None: ...
    @overload
    def tune(self, p0: str, p1: Uri) -> None: ...
    @overload
    def tune(self, p0: str, p1: Uri, p2: Bundle) -> None: ...
    def release(self) -> None: ...

    class RecordingCallback:
        def __init__(self) -> None: ...
        def onDisconnected(self, p0: str) -> None: ...
        def onConnectionFailed(self, p0: str) -> None: ...
        def onRecordingStopped(self, p0: Uri) -> None: ...
        def onTuned(self, p0: Uri) -> None: ...
        def onError(self, p0: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class SignalingDataInfo:
    CONTENT_ENCODING_BASE64: ClassVar[str]
    CONTENT_ENCODING_UTF_8: ClassVar[str]
    CREATOR: ClassVar[Any]
    LLS_NO_GROUP_ID: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    @overload
    def __init__(self, p0: str, p1: str, p2: int, p3: int) -> None: ...
    @overload
    def __init__(self, p0: str, p1: str, p2: int, p3: int, p4: str) -> None: ...
    def getSignalingDataType(self) -> str: ...
    def getVersion(self) -> int: ...
    def getGroup(self) -> int: ...
    def getEncoding(self) -> str: ...
    def getTable(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel

class TvTrackInfo:
    CREATOR: ClassVar[Any]
    TYPE_AUDIO: ClassVar[int]
    TYPE_SUBTITLE: ClassVar[int]
    TYPE_VIDEO: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getAudioChannelCount(self) -> int: ...
    def getVideoFrameRate(self) -> float: ...
    def isEncrypted(self) -> bool: ...
    def getAudioSampleRate(self) -> int: ...
    def getVideoHeight(self) -> int: ...
    def getVideoWidth(self) -> int: ...
    def getVideoActiveFormatDescription(self) -> int: ...
    def isAudioDescription(self) -> bool: ...
    def getVideoPixelAspectRatio(self) -> float: ...
    def isHardOfHearing(self) -> bool: ...
    def isSpokenSubtitle(self) -> bool: ...
    def getExtra(self) -> Bundle: ...
    def getLanguage(self) -> str: ...
    def equals(self, p0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def getId(self) -> str: ...
    def getType(self) -> int: ...
    def getEncoding(self) -> str: ...
    def getDescription(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class Builder:
        def __init__(self, p0: int, p1: str) -> None: ...
        def setAudioSampleRate(self, p0: int) -> Any: ...
        def setVideoFrameRate(self, p0: float) -> Any: ...
        def setAudioChannelCount(self, p0: int) -> Any: ...
        def setAudioDescription(self, p0: bool) -> Any: ...
        def setHardOfHearing(self, p0: bool) -> Any: ...
        def setEncrypted(self, p0: bool) -> Any: ...
        def setSpokenSubtitle(self, p0: bool) -> Any: ...
        def setVideoActiveFormatDescription(self, p0: int) -> Any: ...
        def setVideoHeight(self, p0: int) -> Any: ...
        def setVideoPixelAspectRatio(self, p0: float) -> Any: ...
        def setVideoWidth(self, p0: int) -> Any: ...
        def setExtra(self, p0: Bundle) -> Any: ...
        def setDescription(self, p0: str) -> Any: ...
        def setLanguage(self, p0: str) -> Any: ...
        def build(self) -> "TvTrackInfo": ...
        def setEncoding(self, p0: str) -> Any: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class TimelineRequest:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CREATOR: ClassVar[Any]
    REQUEST_OPTION_AUTO_UPDATE: ClassVar[int]
    REQUEST_OPTION_ONESHOT: ClassVar[int]
    REQUEST_OPTION_ONEWAY: ClassVar[int]
    REQUEST_OPTION_REPEAT: ClassVar[int]
    @overload
    def __init__(self, p0: int, p1: int, p2: int) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: str) -> None: ...
    def getIntervalMillis(self) -> int: ...
    def getSelector(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class TsResponse:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CREATOR: ClassVar[Any]
    RESPONSE_RESULT_CANCEL: ClassVar[int]
    RESPONSE_RESULT_ERROR: ClassVar[int]
    RESPONSE_RESULT_OK: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: int, p3: str) -> None: ...
    def getSharedFilterToken(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.content.AttributionSource import AttributionSource
from android.content.Context import Context
from android.graphics.Canvas import Canvas
from android.graphics.Region import Region
from android.media.PlaybackParams import PlaybackParams
from android.media.tv.AitInfo import AitInfo
from android.media.tv.TvContentRating import TvContentRating
from android.net.Uri import Uri
from android.os.Bundle import Bundle
from android.util.AttributeSet import AttributeSet
from android.util.Property import Property
from android.view.InputEvent import InputEvent
from android.view.KeyEvent import KeyEvent
from android.view.MotionEvent import MotionEvent

class TvView:
    FOCUS_AFTER_DESCENDANTS: ClassVar[int]
    FOCUS_BEFORE_DESCENDANTS: ClassVar[int]
    FOCUS_BLOCK_DESCENDANTS: ClassVar[int]
    LAYOUT_MODE_CLIP_BOUNDS: ClassVar[int]
    LAYOUT_MODE_OPTICAL_BOUNDS: ClassVar[int]
    PERSISTENT_ALL_CACHES: ClassVar[int]
    PERSISTENT_ANIMATION_CACHE: ClassVar[int]
    PERSISTENT_NO_CACHE: ClassVar[int]
    PERSISTENT_SCROLLING_CACHE: ClassVar[int]
    ACCESSIBILITY_DATA_SENSITIVE_AUTO: ClassVar[int]
    ACCESSIBILITY_DATA_SENSITIVE_NO: ClassVar[int]
    ACCESSIBILITY_DATA_SENSITIVE_YES: ClassVar[int]
    ACCESSIBILITY_LIVE_REGION_ASSERTIVE: ClassVar[int]
    ACCESSIBILITY_LIVE_REGION_NONE: ClassVar[int]
    ACCESSIBILITY_LIVE_REGION_POLITE: ClassVar[int]
    ALPHA: ClassVar[Property]
    AUTOFILL_FLAG_INCLUDE_NOT_IMPORTANT_VIEWS: ClassVar[int]
    AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_DATE: ClassVar[str]
    AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_DAY: ClassVar[str]
    AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_MONTH: ClassVar[str]
    AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_YEAR: ClassVar[str]
    AUTOFILL_HINT_CREDIT_CARD_NUMBER: ClassVar[str]
    AUTOFILL_HINT_CREDIT_CARD_SECURITY_CODE: ClassVar[str]
    AUTOFILL_HINT_EMAIL_ADDRESS: ClassVar[str]
    AUTOFILL_HINT_NAME: ClassVar[str]
    AUTOFILL_HINT_PASSWORD: ClassVar[str]
    AUTOFILL_HINT_PHONE: ClassVar[str]
    AUTOFILL_HINT_POSTAL_ADDRESS: ClassVar[str]
    AUTOFILL_HINT_POSTAL_CODE: ClassVar[str]
    AUTOFILL_HINT_USERNAME: ClassVar[str]
    AUTOFILL_TYPE_DATE: ClassVar[int]
    AUTOFILL_TYPE_LIST: ClassVar[int]
    AUTOFILL_TYPE_NONE: ClassVar[int]
    AUTOFILL_TYPE_TEXT: ClassVar[int]
    AUTOFILL_TYPE_TOGGLE: ClassVar[int]
    CONTENT_SENSITIVITY_AUTO: ClassVar[int]
    CONTENT_SENSITIVITY_NOT_SENSITIVE: ClassVar[int]
    CONTENT_SENSITIVITY_SENSITIVE: ClassVar[int]
    DRAG_FLAG_ACCESSIBILITY_ACTION: ClassVar[int]
    DRAG_FLAG_GLOBAL: ClassVar[int]
    DRAG_FLAG_GLOBAL_PERSISTABLE_URI_PERMISSION: ClassVar[int]
    DRAG_FLAG_GLOBAL_PREFIX_URI_PERMISSION: ClassVar[int]
    DRAG_FLAG_GLOBAL_SAME_APPLICATION: ClassVar[int]
    DRAG_FLAG_GLOBAL_URI_READ: ClassVar[int]
    DRAG_FLAG_GLOBAL_URI_WRITE: ClassVar[int]
    DRAG_FLAG_HIDE_CALLING_TASK_ON_DRAG_START: ClassVar[int]
    DRAG_FLAG_OPAQUE: ClassVar[int]
    DRAG_FLAG_START_INTENT_SENDER_ON_UNHANDLED_DRAG: ClassVar[int]
    DRAWING_CACHE_QUALITY_AUTO: ClassVar[int]
    DRAWING_CACHE_QUALITY_HIGH: ClassVar[int]
    DRAWING_CACHE_QUALITY_LOW: ClassVar[int]
    FIND_VIEWS_WITH_CONTENT_DESCRIPTION: ClassVar[int]
    FIND_VIEWS_WITH_TEXT: ClassVar[int]
    FOCUSABLE: ClassVar[int]
    FOCUSABLES_ALL: ClassVar[int]
    FOCUSABLES_TOUCH_MODE: ClassVar[int]
    FOCUSABLE_AUTO: ClassVar[int]
    FOCUS_BACKWARD: ClassVar[int]
    FOCUS_DOWN: ClassVar[int]
    FOCUS_FORWARD: ClassVar[int]
    FOCUS_LEFT: ClassVar[int]
    FOCUS_RIGHT: ClassVar[int]
    FOCUS_UP: ClassVar[int]
    GONE: ClassVar[int]
    HAPTIC_FEEDBACK_ENABLED: ClassVar[int]
    IMPORTANT_FOR_ACCESSIBILITY_AUTO: ClassVar[int]
    IMPORTANT_FOR_ACCESSIBILITY_NO: ClassVar[int]
    IMPORTANT_FOR_ACCESSIBILITY_NO_HIDE_DESCENDANTS: ClassVar[int]
    IMPORTANT_FOR_ACCESSIBILITY_YES: ClassVar[int]
    IMPORTANT_FOR_AUTOFILL_AUTO: ClassVar[int]
    IMPORTANT_FOR_AUTOFILL_NO: ClassVar[int]
    IMPORTANT_FOR_AUTOFILL_NO_EXCLUDE_DESCENDANTS: ClassVar[int]
    IMPORTANT_FOR_AUTOFILL_YES: ClassVar[int]
    IMPORTANT_FOR_AUTOFILL_YES_EXCLUDE_DESCENDANTS: ClassVar[int]
    IMPORTANT_FOR_CONTENT_CAPTURE_AUTO: ClassVar[int]
    IMPORTANT_FOR_CONTENT_CAPTURE_NO: ClassVar[int]
    IMPORTANT_FOR_CONTENT_CAPTURE_NO_EXCLUDE_DESCENDANTS: ClassVar[int]
    IMPORTANT_FOR_CONTENT_CAPTURE_YES: ClassVar[int]
    IMPORTANT_FOR_CONTENT_CAPTURE_YES_EXCLUDE_DESCENDANTS: ClassVar[int]
    INVISIBLE: ClassVar[int]
    KEEP_SCREEN_ON: ClassVar[int]
    LAYER_TYPE_HARDWARE: ClassVar[int]
    LAYER_TYPE_NONE: ClassVar[int]
    LAYER_TYPE_SOFTWARE: ClassVar[int]
    LAYOUT_DIRECTION_INHERIT: ClassVar[int]
    LAYOUT_DIRECTION_LOCALE: ClassVar[int]
    LAYOUT_DIRECTION_LTR: ClassVar[int]
    LAYOUT_DIRECTION_RTL: ClassVar[int]
    MEASURED_HEIGHT_STATE_SHIFT: ClassVar[int]
    MEASURED_SIZE_MASK: ClassVar[int]
    MEASURED_STATE_MASK: ClassVar[int]
    MEASURED_STATE_TOO_SMALL: ClassVar[int]
    NOT_FOCUSABLE: ClassVar[int]
    NO_ID: ClassVar[int]
    OVER_SCROLL_ALWAYS: ClassVar[int]
    OVER_SCROLL_IF_CONTENT_SCROLLS: ClassVar[int]
    OVER_SCROLL_NEVER: ClassVar[int]
    REQUESTED_FRAME_RATE_CATEGORY_DEFAULT: ClassVar[float]
    REQUESTED_FRAME_RATE_CATEGORY_HIGH: ClassVar[float]
    REQUESTED_FRAME_RATE_CATEGORY_LOW: ClassVar[float]
    REQUESTED_FRAME_RATE_CATEGORY_NORMAL: ClassVar[float]
    REQUESTED_FRAME_RATE_CATEGORY_NO_PREFERENCE: ClassVar[float]
    ROTATION: ClassVar[Property]
    ROTATION_X: ClassVar[Property]
    ROTATION_Y: ClassVar[Property]
    SCALE_X: ClassVar[Property]
    SCALE_Y: ClassVar[Property]
    SCREEN_STATE_OFF: ClassVar[int]
    SCREEN_STATE_ON: ClassVar[int]
    SCROLLBARS_INSIDE_INSET: ClassVar[int]
    SCROLLBARS_INSIDE_OVERLAY: ClassVar[int]
    SCROLLBARS_OUTSIDE_INSET: ClassVar[int]
    SCROLLBARS_OUTSIDE_OVERLAY: ClassVar[int]
    SCROLLBAR_POSITION_DEFAULT: ClassVar[int]
    SCROLLBAR_POSITION_LEFT: ClassVar[int]
    SCROLLBAR_POSITION_RIGHT: ClassVar[int]
    SCROLL_AXIS_HORIZONTAL: ClassVar[int]
    SCROLL_AXIS_NONE: ClassVar[int]
    SCROLL_AXIS_VERTICAL: ClassVar[int]
    SCROLL_CAPTURE_HINT_AUTO: ClassVar[int]
    SCROLL_CAPTURE_HINT_EXCLUDE: ClassVar[int]
    SCROLL_CAPTURE_HINT_EXCLUDE_DESCENDANTS: ClassVar[int]
    SCROLL_CAPTURE_HINT_INCLUDE: ClassVar[int]
    SCROLL_INDICATOR_BOTTOM: ClassVar[int]
    SCROLL_INDICATOR_END: ClassVar[int]
    SCROLL_INDICATOR_LEFT: ClassVar[int]
    SCROLL_INDICATOR_RIGHT: ClassVar[int]
    SCROLL_INDICATOR_START: ClassVar[int]
    SCROLL_INDICATOR_TOP: ClassVar[int]
    SOUND_EFFECTS_ENABLED: ClassVar[int]
    STATUS_BAR_HIDDEN: ClassVar[int]
    STATUS_BAR_VISIBLE: ClassVar[int]
    SYSTEM_UI_FLAG_FULLSCREEN: ClassVar[int]
    SYSTEM_UI_FLAG_HIDE_NAVIGATION: ClassVar[int]
    SYSTEM_UI_FLAG_IMMERSIVE: ClassVar[int]
    SYSTEM_UI_FLAG_IMMERSIVE_STICKY: ClassVar[int]
    SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN: ClassVar[int]
    SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION: ClassVar[int]
    SYSTEM_UI_FLAG_LAYOUT_STABLE: ClassVar[int]
    SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR: ClassVar[int]
    SYSTEM_UI_FLAG_LIGHT_STATUS_BAR: ClassVar[int]
    SYSTEM_UI_FLAG_LOW_PROFILE: ClassVar[int]
    SYSTEM_UI_FLAG_VISIBLE: ClassVar[int]
    SYSTEM_UI_LAYOUT_FLAGS: ClassVar[int]
    TEXT_ALIGNMENT_CENTER: ClassVar[int]
    TEXT_ALIGNMENT_GRAVITY: ClassVar[int]
    TEXT_ALIGNMENT_INHERIT: ClassVar[int]
    TEXT_ALIGNMENT_TEXT_END: ClassVar[int]
    TEXT_ALIGNMENT_TEXT_START: ClassVar[int]
    TEXT_ALIGNMENT_VIEW_END: ClassVar[int]
    TEXT_ALIGNMENT_VIEW_START: ClassVar[int]
    TEXT_DIRECTION_ANY_RTL: ClassVar[int]
    TEXT_DIRECTION_FIRST_STRONG: ClassVar[int]
    TEXT_DIRECTION_FIRST_STRONG_LTR: ClassVar[int]
    TEXT_DIRECTION_FIRST_STRONG_RTL: ClassVar[int]
    TEXT_DIRECTION_INHERIT: ClassVar[int]
    TEXT_DIRECTION_LOCALE: ClassVar[int]
    TEXT_DIRECTION_LTR: ClassVar[int]
    TEXT_DIRECTION_RTL: ClassVar[int]
    TRANSLATION_X: ClassVar[Property]
    TRANSLATION_Y: ClassVar[Property]
    TRANSLATION_Z: ClassVar[Property]
    VISIBLE: ClassVar[int]
    X: ClassVar[Property]
    Y: ClassVar[Property]
    Z: ClassVar[Property]
    @overload
    def __init__(self, p0: Context, p1: AttributeSet, p2: int) -> None: ...
    @overload
    def __init__(self, p0: Context, p1: AttributeSet) -> None: ...
    @overload
    def __init__(self, p0: Context) -> None: ...
    def sendAppPrivateCommand(self, p0: str, p1: Bundle) -> None: ...
    def getSelectedTrack(self, p0: int) -> str: ...
    def selectTrack(self, p0: int, p1: str) -> None: ...
    def dispatchUnhandledInputEvent(self, p0: InputEvent) -> bool: ...
    def onUnhandledInputEvent(self, p0: InputEvent) -> bool: ...
    def setOnUnhandledInputEventListener(self, p0: Any) -> None: ...
    def overrideTvAppAttributionSource(self, p0: AttributionSource) -> None: ...
    @overload
    def tune(self, p0: str, p1: Uri, p2: Bundle) -> None: ...
    @overload
    def tune(self, p0: str, p1: Uri) -> None: ...
    def resumePlayback(self) -> None: ...
    def selectAudioPresentation(self, p0: int, p1: int) -> None: ...
    def setCaptionEnabled(self, p0: bool) -> None: ...
    def setInteractiveAppNotificationEnabled(self, p0: bool) -> None: ...
    def setStreamVolume(self, p0: float) -> None: ...
    def setTimeShiftPositionCallback(self, p0: Any) -> None: ...
    def setTvMessageEnabled(self, p0: int, p1: bool) -> None: ...
    def setVideoFrozen(self, p0: bool) -> None: ...
    def timeShiftPause(self) -> None: ...
    def timeShiftPlay(self, p0: str, p1: Uri) -> None: ...
    def timeShiftResume(self) -> None: ...
    def timeShiftSeekTo(self, p0: int) -> None: ...
    def timeShiftSetMode(self, p0: int) -> None: ...
    def timeShiftSetPlaybackParams(self, p0: PlaybackParams) -> None: ...
    def getTracks(self, p0: int) -> list: ...
    def reset(self) -> None: ...
    def dispatchGenericMotionEvent(self, p0: MotionEvent) -> bool: ...
    def dispatchKeyEvent(self, p0: KeyEvent) -> bool: ...
    def dispatchTouchEvent(self, p0: MotionEvent) -> bool: ...
    def dispatchTrackballEvent(self, p0: MotionEvent) -> bool: ...
    def dispatchWindowFocusChanged(self, p0: bool) -> None: ...
    def draw(self, p0: Canvas) -> None: ...
    def gatherTransparentRegion(self, p0: Region) -> bool: ...
    def setCallback(self, p0: Any) -> None: ...
    def getAudioPresentations(self) -> list: ...
    def setZOrderMediaOverlay(self, p0: bool) -> None: ...
    def setZOrderOnTop(self, p0: bool) -> None: ...
    def stopPlayback(self, p0: int) -> None: ...

    class TvInputCallback:
        def __init__(self) -> None: ...
        def onDisconnected(self, p0: str) -> None: ...
        def onConnectionFailed(self, p0: str) -> None: ...
        def onTvMessage(self, p0: str, p1: int, p2: Bundle) -> None: ...
        def onVideoSizeChanged(self, p0: str, p1: int, p2: int) -> None: ...
        def onAvailableSpeeds(self, p0: str, p1: Any) -> None: ...
        def onContentAllowed(self, p0: str) -> None: ...
        def onContentBlocked(self, p0: str, p1: TvContentRating) -> None: ...
        def onTimeShiftMode(self, p0: str, p1: int) -> None: ...
        def onTimeShiftStatusChanged(self, p0: str, p1: int) -> None: ...
        def onTrackSelected(self, p0: str, p1: int, p2: str) -> None: ...
        def onTracksChanged(self, p0: str, p1: list) -> None: ...
        def onTuned(self, p0: str, p1: Uri) -> None: ...
        def onVideoAvailable(self, p0: str) -> None: ...
        def onVideoFreezeUpdated(self, p0: str, p1: bool) -> None: ...
        def onVideoUnavailable(self, p0: str, p1: int) -> None: ...
        def onAudioPresentationsChanged(self, p0: str, p1: list) -> None: ...
        def onCueingMessageAvailability(self, p0: str, p1: bool) -> None: ...
        def onSignalStrengthUpdated(self, p0: str, p1: int) -> None: ...
        def onAudioPresentationSelected(self, p0: str, p1: int, p2: int) -> None: ...
        def onAitInfoUpdated(self, p0: str, p1: AitInfo) -> None: ...
        def onChannelRetuned(self, p0: str, p1: Uri) -> None: ...

    class TimeShiftPositionCallback:
        def __init__(self) -> None: ...
        def onTimeShiftCurrentPositionChanged(self, p0: str, p1: int) -> None: ...
        def onTimeShiftStartPositionChanged(self, p0: str, p1: int) -> None: ...

    class OnUnhandledInputEventListener:
        def onUnhandledInputEvent(self, p0: InputEvent) -> bool: ...

from typing import Any, ClassVar, overload
from android.net.Uri import Uri
from android.os.Parcel import Parcel
from android.os.SharedMemory import SharedMemory

class TableResponse:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CREATOR: ClassVar[Any]
    RESPONSE_RESULT_CANCEL: ClassVar[int]
    RESPONSE_RESULT_ERROR: ClassVar[int]
    RESPONSE_RESULT_OK: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: int, p3: Uri, p4: int, p5: int) -> None: ...
    def getTableUri(self) -> Uri: ...
    def getTableByteArray(self) -> Any: ...
    def getTableSharedMemory(self) -> SharedMemory: ...
    def getVersion(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getSize(self) -> int: ...

    class Builder:
        def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
        def setTableByteArray(self, p0: Any) -> Any: ...
        def build(self) -> "TableResponse": ...
        def setTableSharedMemory(self, p0: SharedMemory) -> Any: ...
        def setTableUri(self, p0: Uri) -> Any: ...

