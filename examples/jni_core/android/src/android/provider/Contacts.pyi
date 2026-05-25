from typing import Any, ClassVar, overload
from android.content.ContentResolver import ContentResolver
from android.content.ContentValues import ContentValues
from android.content.Context import Context
from android.database.Cursor import Cursor
from android.graphics.Bitmap import Bitmap
from android.net.Uri import Uri
from java.io.InputStream import InputStream

class Contacts:
    AUTHORITY: ClassVar[str]
    CONTENT_URI: ClassVar[Uri]
    KIND_EMAIL: ClassVar[int]
    KIND_IM: ClassVar[int]
    KIND_ORGANIZATION: ClassVar[int]
    KIND_PHONE: ClassVar[int]
    KIND_POSTAL: ClassVar[int]

    class SettingsColumns:
        KEY: ClassVar[str]
        VALUE: ClassVar[str]
        _SYNC_ACCOUNT: ClassVar[str]
        _SYNC_ACCOUNT_TYPE: ClassVar[str]

    class Settings:
        CONTENT_DIRECTORY: ClassVar[str]
        CONTENT_URI: ClassVar[Uri]
        DEFAULT_SORT_ORDER: ClassVar[str]
        SYNC_EVERYTHING: ClassVar[str]
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]
        KEY: ClassVar[str]
        VALUE: ClassVar[str]
        _SYNC_ACCOUNT: ClassVar[str]
        _SYNC_ACCOUNT_TYPE: ClassVar[str]
        @staticmethod
        def getSetting(p0: ContentResolver, p1: str, p2: str) -> str: ...
        @staticmethod
        def setSetting(p0: ContentResolver, p1: str, p2: str, p3: str) -> None: ...

    class PresenceColumns:
        AVAILABLE: ClassVar[int]
        AWAY: ClassVar[int]
        DO_NOT_DISTURB: ClassVar[int]
        IDLE: ClassVar[int]
        IM_ACCOUNT: ClassVar[str]
        IM_HANDLE: ClassVar[str]
        IM_PROTOCOL: ClassVar[str]
        INVISIBLE: ClassVar[int]
        OFFLINE: ClassVar[int]
        PRESENCE_CUSTOM_STATUS: ClassVar[str]
        PRESENCE_STATUS: ClassVar[str]
        PRIORITY: ClassVar[str]

    class PhotosColumns:
        DATA: ClassVar[str]
        DOWNLOAD_REQUIRED: ClassVar[str]
        EXISTS_ON_SERVER: ClassVar[str]
        LOCAL_VERSION: ClassVar[str]
        PERSON_ID: ClassVar[str]
        SYNC_ERROR: ClassVar[str]

    class Photos:
        CONTENT_DIRECTORY: ClassVar[str]
        CONTENT_URI: ClassVar[Uri]
        DEFAULT_SORT_ORDER: ClassVar[str]
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]
        DATA: ClassVar[str]
        DOWNLOAD_REQUIRED: ClassVar[str]
        EXISTS_ON_SERVER: ClassVar[str]
        LOCAL_VERSION: ClassVar[str]
        PERSON_ID: ClassVar[str]
        SYNC_ERROR: ClassVar[str]

    class PhonesColumns:
        ISPRIMARY: ClassVar[str]
        LABEL: ClassVar[str]
        NUMBER: ClassVar[str]
        NUMBER_KEY: ClassVar[str]
        TYPE: ClassVar[str]
        TYPE_CUSTOM: ClassVar[int]
        TYPE_FAX_HOME: ClassVar[int]
        TYPE_FAX_WORK: ClassVar[int]
        TYPE_HOME: ClassVar[int]
        TYPE_MOBILE: ClassVar[int]
        TYPE_OTHER: ClassVar[int]
        TYPE_PAGER: ClassVar[int]
        TYPE_WORK: ClassVar[int]

    class Phones:
        CONTENT_FILTER_URL: ClassVar[Uri]
        CONTENT_ITEM_TYPE: ClassVar[str]
        CONTENT_TYPE: ClassVar[str]
        CONTENT_URI: ClassVar[Uri]
        DEFAULT_SORT_ORDER: ClassVar[str]
        PERSON_ID: ClassVar[str]
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]
        ISPRIMARY: ClassVar[str]
        LABEL: ClassVar[str]
        NUMBER: ClassVar[str]
        NUMBER_KEY: ClassVar[str]
        TYPE: ClassVar[str]
        TYPE_CUSTOM: ClassVar[int]
        TYPE_FAX_HOME: ClassVar[int]
        TYPE_FAX_WORK: ClassVar[int]
        TYPE_HOME: ClassVar[int]
        TYPE_MOBILE: ClassVar[int]
        TYPE_OTHER: ClassVar[int]
        TYPE_PAGER: ClassVar[int]
        TYPE_WORK: ClassVar[int]
        CUSTOM_RINGTONE: ClassVar[str]
        DISPLAY_NAME: ClassVar[str]
        LAST_TIME_CONTACTED: ClassVar[str]
        NAME: ClassVar[str]
        NOTES: ClassVar[str]
        PHONETIC_NAME: ClassVar[str]
        PHOTO_VERSION: ClassVar[str]
        SEND_TO_VOICEMAIL: ClassVar[str]
        STARRED: ClassVar[str]
        TIMES_CONTACTED: ClassVar[str]
        @overload
        @staticmethod
        def getDisplayLabel(p0: Context, p1: int, p2: str) -> str: ...
        @overload
        @staticmethod
        def getDisplayLabel(p0: Context, p1: int, p2: str, p3: Any) -> str: ...

    class PeopleColumns:
        CUSTOM_RINGTONE: ClassVar[str]
        DISPLAY_NAME: ClassVar[str]
        LAST_TIME_CONTACTED: ClassVar[str]
        NAME: ClassVar[str]
        NOTES: ClassVar[str]
        PHONETIC_NAME: ClassVar[str]
        PHOTO_VERSION: ClassVar[str]
        SEND_TO_VOICEMAIL: ClassVar[str]
        STARRED: ClassVar[str]
        TIMES_CONTACTED: ClassVar[str]

    class People:
        CONTENT_FILTER_URI: ClassVar[Uri]
        CONTENT_ITEM_TYPE: ClassVar[str]
        CONTENT_TYPE: ClassVar[str]
        CONTENT_URI: ClassVar[Uri]
        DEFAULT_SORT_ORDER: ClassVar[str]
        DELETED_CONTENT_URI: ClassVar[Uri]
        PRIMARY_EMAIL_ID: ClassVar[str]
        PRIMARY_ORGANIZATION_ID: ClassVar[str]
        PRIMARY_PHONE_ID: ClassVar[str]
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]
        CUSTOM_RINGTONE: ClassVar[str]
        DISPLAY_NAME: ClassVar[str]
        LAST_TIME_CONTACTED: ClassVar[str]
        NAME: ClassVar[str]
        NOTES: ClassVar[str]
        PHONETIC_NAME: ClassVar[str]
        PHOTO_VERSION: ClassVar[str]
        SEND_TO_VOICEMAIL: ClassVar[str]
        STARRED: ClassVar[str]
        TIMES_CONTACTED: ClassVar[str]
        ISPRIMARY: ClassVar[str]
        LABEL: ClassVar[str]
        NUMBER: ClassVar[str]
        NUMBER_KEY: ClassVar[str]
        TYPE: ClassVar[str]
        TYPE_CUSTOM: ClassVar[int]
        TYPE_FAX_HOME: ClassVar[int]
        TYPE_FAX_WORK: ClassVar[int]
        TYPE_HOME: ClassVar[int]
        TYPE_MOBILE: ClassVar[int]
        TYPE_OTHER: ClassVar[int]
        TYPE_PAGER: ClassVar[int]
        TYPE_WORK: ClassVar[int]
        AVAILABLE: ClassVar[int]
        AWAY: ClassVar[int]
        DO_NOT_DISTURB: ClassVar[int]
        IDLE: ClassVar[int]
        IM_ACCOUNT: ClassVar[str]
        IM_HANDLE: ClassVar[str]
        IM_PROTOCOL: ClassVar[str]
        INVISIBLE: ClassVar[int]
        OFFLINE: ClassVar[int]
        PRESENCE_CUSTOM_STATUS: ClassVar[str]
        PRESENCE_STATUS: ClassVar[str]
        PRIORITY: ClassVar[str]
        @staticmethod
        def markAsContacted(p0: ContentResolver, p1: int) -> None: ...
        @staticmethod
        def addToMyContactsGroup(p0: ContentResolver, p1: int) -> Uri: ...
        @overload
        @staticmethod
        def addToGroup(p0: ContentResolver, p1: int, p2: str) -> Uri: ...
        @overload
        @staticmethod
        def addToGroup(p0: ContentResolver, p1: int, p2: int) -> Uri: ...
        @staticmethod
        def createPersonInMyContactsGroup(p0: ContentResolver, p1: ContentValues) -> Uri: ...
        @staticmethod
        def queryGroups(p0: ContentResolver, p1: int) -> Cursor: ...
        @staticmethod
        def setPhotoData(p0: ContentResolver, p1: Uri, p2: Any) -> None: ...
        @staticmethod
        def openContactPhotoInputStream(p0: ContentResolver, p1: Uri) -> InputStream: ...
        @staticmethod
        def loadContactPhoto(p0: Context, p1: Uri, p2: int, p3: Any) -> Bitmap: ...

        class Phones:
            CONTENT_DIRECTORY: ClassVar[str]
            DEFAULT_SORT_ORDER: ClassVar[str]
            _COUNT: ClassVar[str]
            _ID: ClassVar[str]
            ISPRIMARY: ClassVar[str]
            LABEL: ClassVar[str]
            NUMBER: ClassVar[str]
            NUMBER_KEY: ClassVar[str]
            TYPE: ClassVar[str]
            TYPE_CUSTOM: ClassVar[int]
            TYPE_FAX_HOME: ClassVar[int]
            TYPE_FAX_WORK: ClassVar[int]
            TYPE_HOME: ClassVar[int]
            TYPE_MOBILE: ClassVar[int]
            TYPE_OTHER: ClassVar[int]
            TYPE_PAGER: ClassVar[int]
            TYPE_WORK: ClassVar[int]
            CUSTOM_RINGTONE: ClassVar[str]
            DISPLAY_NAME: ClassVar[str]
            LAST_TIME_CONTACTED: ClassVar[str]
            NAME: ClassVar[str]
            NOTES: ClassVar[str]
            PHONETIC_NAME: ClassVar[str]
            PHOTO_VERSION: ClassVar[str]
            SEND_TO_VOICEMAIL: ClassVar[str]
            STARRED: ClassVar[str]
            TIMES_CONTACTED: ClassVar[str]

        class Extensions:
            CONTENT_DIRECTORY: ClassVar[str]
            DEFAULT_SORT_ORDER: ClassVar[str]
            PERSON_ID: ClassVar[str]
            _COUNT: ClassVar[str]
            _ID: ClassVar[str]
            NAME: ClassVar[str]
            VALUE: ClassVar[str]

        class ContactMethods:
            CONTENT_DIRECTORY: ClassVar[str]
            DEFAULT_SORT_ORDER: ClassVar[str]
            _COUNT: ClassVar[str]
            _ID: ClassVar[str]
            AUX_DATA: ClassVar[str]
            DATA: ClassVar[str]
            ISPRIMARY: ClassVar[str]
            KIND: ClassVar[str]
            LABEL: ClassVar[str]
            TYPE: ClassVar[str]
            TYPE_CUSTOM: ClassVar[int]
            TYPE_HOME: ClassVar[int]
            TYPE_OTHER: ClassVar[int]
            TYPE_WORK: ClassVar[int]
            CUSTOM_RINGTONE: ClassVar[str]
            DISPLAY_NAME: ClassVar[str]
            LAST_TIME_CONTACTED: ClassVar[str]
            NAME: ClassVar[str]
            NOTES: ClassVar[str]
            PHONETIC_NAME: ClassVar[str]
            PHOTO_VERSION: ClassVar[str]
            SEND_TO_VOICEMAIL: ClassVar[str]
            STARRED: ClassVar[str]
            TIMES_CONTACTED: ClassVar[str]

    class Organizations:
        CONTENT_DIRECTORY: ClassVar[str]
        CONTENT_URI: ClassVar[Uri]
        DEFAULT_SORT_ORDER: ClassVar[str]
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]
        COMPANY: ClassVar[str]
        ISPRIMARY: ClassVar[str]
        LABEL: ClassVar[str]
        PERSON_ID: ClassVar[str]
        TITLE: ClassVar[str]
        TYPE: ClassVar[str]
        TYPE_CUSTOM: ClassVar[int]
        TYPE_OTHER: ClassVar[int]
        TYPE_WORK: ClassVar[int]
        @staticmethod
        def getDisplayLabel(p0: Context, p1: int, p2: str) -> str: ...

    class OrganizationColumns:
        COMPANY: ClassVar[str]
        ISPRIMARY: ClassVar[str]
        LABEL: ClassVar[str]
        PERSON_ID: ClassVar[str]
        TITLE: ClassVar[str]
        TYPE: ClassVar[str]
        TYPE_CUSTOM: ClassVar[int]
        TYPE_OTHER: ClassVar[int]
        TYPE_WORK: ClassVar[int]

    class Intents:
        ATTACH_IMAGE: ClassVar[str]
        EXTRA_CREATE_DESCRIPTION: ClassVar[str]
        EXTRA_FORCE_CREATE: ClassVar[str]
        SEARCH_SUGGESTION_CLICKED: ClassVar[str]
        SEARCH_SUGGESTION_CREATE_CONTACT_CLICKED: ClassVar[str]
        SEARCH_SUGGESTION_DIAL_NUMBER_CLICKED: ClassVar[str]
        SHOW_OR_CREATE_CONTACT: ClassVar[str]
        def __init__(self) -> None: ...

        class UI:
            FILTER_CONTACTS_ACTION: ClassVar[str]
            FILTER_TEXT_EXTRA_KEY: ClassVar[str]
            GROUP_NAME_EXTRA_KEY: ClassVar[str]
            LIST_ALL_CONTACTS_ACTION: ClassVar[str]
            LIST_CONTACTS_WITH_PHONES_ACTION: ClassVar[str]
            LIST_DEFAULT: ClassVar[str]
            LIST_FREQUENT_ACTION: ClassVar[str]
            LIST_GROUP_ACTION: ClassVar[str]
            LIST_STARRED_ACTION: ClassVar[str]
            LIST_STREQUENT_ACTION: ClassVar[str]
            TITLE_EXTRA_KEY: ClassVar[str]
            def __init__(self) -> None: ...

        class Insert:
            ACTION: ClassVar[str]
            COMPANY: ClassVar[str]
            EMAIL: ClassVar[str]
            EMAIL_ISPRIMARY: ClassVar[str]
            EMAIL_TYPE: ClassVar[str]
            FULL_MODE: ClassVar[str]
            IM_HANDLE: ClassVar[str]
            IM_ISPRIMARY: ClassVar[str]
            IM_PROTOCOL: ClassVar[str]
            JOB_TITLE: ClassVar[str]
            NAME: ClassVar[str]
            NOTES: ClassVar[str]
            PHONE: ClassVar[str]
            PHONETIC_NAME: ClassVar[str]
            PHONE_ISPRIMARY: ClassVar[str]
            PHONE_TYPE: ClassVar[str]
            POSTAL: ClassVar[str]
            POSTAL_ISPRIMARY: ClassVar[str]
            POSTAL_TYPE: ClassVar[str]
            SECONDARY_EMAIL: ClassVar[str]
            SECONDARY_EMAIL_TYPE: ClassVar[str]
            SECONDARY_PHONE: ClassVar[str]
            SECONDARY_PHONE_TYPE: ClassVar[str]
            TERTIARY_EMAIL: ClassVar[str]
            TERTIARY_EMAIL_TYPE: ClassVar[str]
            TERTIARY_PHONE: ClassVar[str]
            TERTIARY_PHONE_TYPE: ClassVar[str]
            def __init__(self) -> None: ...

    class GroupsColumns:
        NAME: ClassVar[str]
        NOTES: ClassVar[str]
        SHOULD_SYNC: ClassVar[str]
        SYSTEM_ID: ClassVar[str]

    class Groups:
        CONTENT_ITEM_TYPE: ClassVar[str]
        CONTENT_TYPE: ClassVar[str]
        CONTENT_URI: ClassVar[Uri]
        DEFAULT_SORT_ORDER: ClassVar[str]
        DELETED_CONTENT_URI: ClassVar[Uri]
        GROUP_ANDROID_STARRED: ClassVar[str]
        GROUP_MY_CONTACTS: ClassVar[str]
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]
        NAME: ClassVar[str]
        NOTES: ClassVar[str]
        SHOULD_SYNC: ClassVar[str]
        SYSTEM_ID: ClassVar[str]

    class GroupMembership:
        CONTENT_DIRECTORY: ClassVar[str]
        CONTENT_ITEM_TYPE: ClassVar[str]
        CONTENT_TYPE: ClassVar[str]
        CONTENT_URI: ClassVar[Uri]
        DEFAULT_SORT_ORDER: ClassVar[str]
        GROUP_ID: ClassVar[str]
        GROUP_SYNC_ACCOUNT: ClassVar[str]
        GROUP_SYNC_ACCOUNT_TYPE: ClassVar[str]
        GROUP_SYNC_ID: ClassVar[str]
        PERSON_ID: ClassVar[str]
        RAW_CONTENT_URI: ClassVar[Uri]
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]
        NAME: ClassVar[str]
        NOTES: ClassVar[str]
        SHOULD_SYNC: ClassVar[str]
        SYSTEM_ID: ClassVar[str]

    class ExtensionsColumns:
        NAME: ClassVar[str]
        VALUE: ClassVar[str]

    class Extensions:
        CONTENT_ITEM_TYPE: ClassVar[str]
        CONTENT_TYPE: ClassVar[str]
        CONTENT_URI: ClassVar[Uri]
        DEFAULT_SORT_ORDER: ClassVar[str]
        PERSON_ID: ClassVar[str]
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]
        NAME: ClassVar[str]
        VALUE: ClassVar[str]

    class ContactMethodsColumns:
        AUX_DATA: ClassVar[str]
        DATA: ClassVar[str]
        ISPRIMARY: ClassVar[str]
        KIND: ClassVar[str]
        LABEL: ClassVar[str]
        TYPE: ClassVar[str]
        TYPE_CUSTOM: ClassVar[int]
        TYPE_HOME: ClassVar[int]
        TYPE_OTHER: ClassVar[int]
        TYPE_WORK: ClassVar[int]

    class ContactMethods:
        CONTENT_EMAIL_ITEM_TYPE: ClassVar[str]
        CONTENT_EMAIL_TYPE: ClassVar[str]
        CONTENT_EMAIL_URI: ClassVar[Uri]
        CONTENT_IM_ITEM_TYPE: ClassVar[str]
        CONTENT_POSTAL_ITEM_TYPE: ClassVar[str]
        CONTENT_POSTAL_TYPE: ClassVar[str]
        CONTENT_TYPE: ClassVar[str]
        CONTENT_URI: ClassVar[Uri]
        DEFAULT_SORT_ORDER: ClassVar[str]
        PERSON_ID: ClassVar[str]
        POSTAL_LOCATION_LATITUDE: ClassVar[str]
        POSTAL_LOCATION_LONGITUDE: ClassVar[str]
        PROTOCOL_AIM: ClassVar[int]
        PROTOCOL_GOOGLE_TALK: ClassVar[int]
        PROTOCOL_ICQ: ClassVar[int]
        PROTOCOL_JABBER: ClassVar[int]
        PROTOCOL_MSN: ClassVar[int]
        PROTOCOL_QQ: ClassVar[int]
        PROTOCOL_SKYPE: ClassVar[int]
        PROTOCOL_YAHOO: ClassVar[int]
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]
        AUX_DATA: ClassVar[str]
        DATA: ClassVar[str]
        ISPRIMARY: ClassVar[str]
        KIND: ClassVar[str]
        LABEL: ClassVar[str]
        TYPE: ClassVar[str]
        TYPE_CUSTOM: ClassVar[int]
        TYPE_HOME: ClassVar[int]
        TYPE_OTHER: ClassVar[int]
        TYPE_WORK: ClassVar[int]
        CUSTOM_RINGTONE: ClassVar[str]
        DISPLAY_NAME: ClassVar[str]
        LAST_TIME_CONTACTED: ClassVar[str]
        NAME: ClassVar[str]
        NOTES: ClassVar[str]
        PHONETIC_NAME: ClassVar[str]
        PHOTO_VERSION: ClassVar[str]
        SEND_TO_VOICEMAIL: ClassVar[str]
        STARRED: ClassVar[str]
        TIMES_CONTACTED: ClassVar[str]
        @staticmethod
        def encodePredefinedImProtocol(p0: int) -> str: ...
        @staticmethod
        def encodeCustomImProtocol(p0: str) -> str: ...
        @staticmethod
        def decodeImProtocol(p0: str) -> Any: ...
        def addPostalLocation(self, p0: Context, p1: int, p2: float, p3: float) -> None: ...
        @staticmethod
        def getDisplayLabel(p0: Context, p1: int, p2: int, p3: str) -> str: ...
