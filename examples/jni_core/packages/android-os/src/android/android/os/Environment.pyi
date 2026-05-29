from typing import Any, ClassVar, overload
from java.io.File import File

class Environment:
    DIRECTORY_ALARMS: ClassVar[str]
    DIRECTORY_AUDIOBOOKS: ClassVar[str]
    DIRECTORY_DCIM: ClassVar[str]
    DIRECTORY_DOCUMENTS: ClassVar[str]
    DIRECTORY_DOWNLOADS: ClassVar[str]
    DIRECTORY_MOVIES: ClassVar[str]
    DIRECTORY_MUSIC: ClassVar[str]
    DIRECTORY_NOTIFICATIONS: ClassVar[str]
    DIRECTORY_PICTURES: ClassVar[str]
    DIRECTORY_PODCASTS: ClassVar[str]
    DIRECTORY_RECORDINGS: ClassVar[str]
    DIRECTORY_RINGTONES: ClassVar[str]
    DIRECTORY_SCREENSHOTS: ClassVar[str]
    MEDIA_BAD_REMOVAL: ClassVar[str]
    MEDIA_CHECKING: ClassVar[str]
    MEDIA_EJECTING: ClassVar[str]
    MEDIA_MOUNTED: ClassVar[str]
    MEDIA_MOUNTED_READ_ONLY: ClassVar[str]
    MEDIA_NOFS: ClassVar[str]
    MEDIA_REMOVED: ClassVar[str]
    MEDIA_SHARED: ClassVar[str]
    MEDIA_UNKNOWN: ClassVar[str]
    MEDIA_UNMOUNTABLE: ClassVar[str]
    MEDIA_UNMOUNTED: ClassVar[str]
    def __init__(self) -> None: ...
    @staticmethod
    def getRootDirectory() -> File: ...
    @staticmethod
    def getStorageDirectory() -> File: ...
    @staticmethod
    def getDataDirectory() -> File: ...
    @staticmethod
    def getExternalStorageDirectory() -> File: ...
    @staticmethod
    def getExternalStoragePublicDirectory(p0: str) -> File: ...
    @staticmethod
    def getDownloadCacheDirectory() -> File: ...
    @overload
    @staticmethod
    def getExternalStorageState() -> str: ...
    @overload
    @staticmethod
    def getExternalStorageState(p0: File) -> str: ...
    @staticmethod
    def getStorageState(p0: File) -> str: ...
    @overload
    @staticmethod
    def isExternalStorageRemovable() -> bool: ...
    @overload
    @staticmethod
    def isExternalStorageRemovable(p0: File) -> bool: ...
    @overload
    @staticmethod
    def isExternalStorageEmulated() -> bool: ...
    @overload
    @staticmethod
    def isExternalStorageEmulated(p0: File) -> bool: ...
    @overload
    @staticmethod
    def isExternalStorageLegacy(p0: File) -> bool: ...
    @overload
    @staticmethod
    def isExternalStorageLegacy() -> bool: ...
    @overload
    @staticmethod
    def isExternalStorageManager() -> bool: ...
    @overload
    @staticmethod
    def isExternalStorageManager(p0: File) -> bool: ...
