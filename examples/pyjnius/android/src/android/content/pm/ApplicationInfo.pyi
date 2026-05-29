from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.content.pm.PackageManager import PackageManager
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel
from android.util.Printer import Printer
from java.util.UUID import UUID

class ApplicationInfo:
    CATEGORY_ACCESSIBILITY: ClassVar[int]
    CATEGORY_AUDIO: ClassVar[int]
    CATEGORY_GAME: ClassVar[int]
    CATEGORY_IMAGE: ClassVar[int]
    CATEGORY_MAPS: ClassVar[int]
    CATEGORY_NEWS: ClassVar[int]
    CATEGORY_PRODUCTIVITY: ClassVar[int]
    CATEGORY_SOCIAL: ClassVar[int]
    CATEGORY_UNDEFINED: ClassVar[int]
    CATEGORY_VIDEO: ClassVar[int]
    CREATOR: ClassVar[Any]
    FLAG_ALLOW_BACKUP: ClassVar[int]
    FLAG_ALLOW_CLEAR_USER_DATA: ClassVar[int]
    FLAG_ALLOW_TASK_REPARENTING: ClassVar[int]
    FLAG_DEBUGGABLE: ClassVar[int]
    FLAG_EXTERNAL_STORAGE: ClassVar[int]
    FLAG_EXTRACT_NATIVE_LIBS: ClassVar[int]
    FLAG_FACTORY_TEST: ClassVar[int]
    FLAG_FULL_BACKUP_ONLY: ClassVar[int]
    FLAG_HARDWARE_ACCELERATED: ClassVar[int]
    FLAG_HAS_CODE: ClassVar[int]
    FLAG_INSTALLED: ClassVar[int]
    FLAG_IS_DATA_ONLY: ClassVar[int]
    FLAG_IS_GAME: ClassVar[int]
    FLAG_KILL_AFTER_RESTORE: ClassVar[int]
    FLAG_LARGE_HEAP: ClassVar[int]
    FLAG_MULTIARCH: ClassVar[int]
    FLAG_PERSISTENT: ClassVar[int]
    FLAG_RESIZEABLE_FOR_SCREENS: ClassVar[int]
    FLAG_RESTORE_ANY_VERSION: ClassVar[int]
    FLAG_STOPPED: ClassVar[int]
    FLAG_SUPPORTS_LARGE_SCREENS: ClassVar[int]
    FLAG_SUPPORTS_NORMAL_SCREENS: ClassVar[int]
    FLAG_SUPPORTS_RTL: ClassVar[int]
    FLAG_SUPPORTS_SCREEN_DENSITIES: ClassVar[int]
    FLAG_SUPPORTS_SMALL_SCREENS: ClassVar[int]
    FLAG_SUPPORTS_XLARGE_SCREENS: ClassVar[int]
    FLAG_SUSPENDED: ClassVar[int]
    FLAG_SYSTEM: ClassVar[int]
    FLAG_TEST_ONLY: ClassVar[int]
    FLAG_UPDATED_SYSTEM_APP: ClassVar[int]
    FLAG_USES_CLEARTEXT_TRAFFIC: ClassVar[int]
    FLAG_VM_SAFE_MODE: ClassVar[int]
    GWP_ASAN_ALWAYS: ClassVar[int]
    GWP_ASAN_DEFAULT: ClassVar[int]
    GWP_ASAN_NEVER: ClassVar[int]
    MEMTAG_ASYNC: ClassVar[int]
    MEMTAG_DEFAULT: ClassVar[int]
    MEMTAG_OFF: ClassVar[int]
    MEMTAG_SYNC: ClassVar[int]
    RAW_EXTERNAL_STORAGE_ACCESS_DEFAULT: ClassVar[int]
    RAW_EXTERNAL_STORAGE_ACCESS_NOT_REQUESTED: ClassVar[int]
    RAW_EXTERNAL_STORAGE_ACCESS_REQUESTED: ClassVar[int]
    ZEROINIT_DEFAULT: ClassVar[int]
    ZEROINIT_DISABLED: ClassVar[int]
    ZEROINIT_ENABLED: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    appComponentFactory: str
    backupAgentName: str
    category: int
    className: str
    compatibleWidthLimitDp: int
    compileSdkVersion: int
    compileSdkVersionCodename: str
    dataDir: str
    descriptionRes: int
    deviceProtectedDataDir: str
    enabled: bool
    flags: int
    largestWidthLimitDp: int
    manageSpaceActivityName: str
    minSdkVersion: int
    nativeLibraryDir: str
    permission: str
    processName: str
    publicSourceDir: str
    requiresSmallestWidthDp: int
    sharedLibraryFiles: Any
    sourceDir: str
    splitNames: Any
    splitPublicSourceDirs: Any
    splitSourceDirs: Any
    storageUuid: UUID
    targetSdkVersion: int
    taskAffinity: str
    theme: int
    uiOptions: int
    uid: int
    banner: int
    icon: int
    isArchived: bool
    labelRes: int
    logo: int
    metaData: Bundle
    name: str
    nonLocalizedLabel: str
    packageName: str
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: "ApplicationInfo") -> None: ...
    def toString(self) -> str: ...
    def dump(self, p0: Printer, p1: str) -> None: ...
    def getKnownActivityEmbeddingCerts(self) -> set: ...
    def areAttributionsUserVisible(self) -> bool: ...
    @staticmethod
    def getCategoryTitle(p0: Context, p1: int) -> str: ...
    def getGwpAsanMode(self) -> int: ...
    def getMemtagMode(self) -> int: ...
    def getNativeHeapZeroInitialized(self) -> int: ...
    def getRequestRawExternalStorageAccess(self) -> int: ...
    def isProfileable(self) -> bool: ...
    def isProfileableByShell(self) -> bool: ...
    def isResourceOverlay(self) -> bool: ...
    def isVirtualPreload(self) -> bool: ...
    def loadDescription(self, p0: PackageManager) -> str: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...

    class DisplayNameComparator:
        def __init__(self, p0: PackageManager) -> None: ...
        @overload
        def compare(self, p0: "ApplicationInfo", p1: "ApplicationInfo") -> int: ...
        @overload
        def compare(self, p0: Any, p1: Any) -> int: ...
